#!/usr/bin/env python3
r"""Pre-flight an edition (or a whole book) BEFORE spending tokens on it.

Built 2026-08-12 after the Book-1 run, where the orchestrator burned real context
rediscovering the same facts by hand — and after a formatter batch was attempted
on 24 mafia files that turned out to have zero Heading1 paragraphs, which no
amount of proofreading would have fixed.

Answers, per edition, in one line each:
  * does the English source resolve, and where
  * chapter sequence 1..N, or exactly which numbers are missing/duplicated
  * Heading1 present?  (0 = the print formatter WILL hard-stop)
  * paragraph alignment vs the English (a big gap means omission OR duplication)
  * scene-break count vs the English
  * leftover Markdown `*emphasis*` spans (excluding `* * *` scene breaks)
  * imperial unit tokens still present
  * back-matter presence
  * which pipeline artifacts already exist (report / corrected / applied)

USAGE
    python preflight.py                          # every KB_H1 edition
    python preflight.py --book KB_H1_2           # one book, all languages
    python preflight.py --book KB_H1_2 --langs French,German,Italian
    python preflight.py --book KB_H1_1 --current # inspect corrected\ where it exists
    python preflight.py --verify "<stem>"        # integrity check: corrected vs source

`--verify` replaces the by-hand paragraph/italic/scene diffing the orchestrator
did after every sub-agent write. It caught two real defects on Book 1 (a dropped
italic run, and a naive `<w:i/>` string count that reports 0 because the writer
emits `<w:i />` with a space), so it stays — but as one PASS/FAIL line, not a
screenful.
"""
import argparse
import io as _io
import re
import sys
import zipfile

# The Windows console is cp1252. Any diff line containing Greek/Polish/Czech/Romanian
# text raised UnicodeEncodeError and killed the run mid-report -- so this tool could
# never print a diff for exactly the languages that most needed one. (Found 2026-08-26.)
if hasattr(sys.stdout, "buffer"):
    sys.stdout = _io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = _io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")
import os
from pathlib import Path
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
ROOT = Path(os.environ.get("SCRIPTS_ROOT") or r"C:\Users\User\Scripts")  # cloud: export SCRIPTS_ROOT=<repo root>
TRANSLATED = ROOT / "translated"
CORRECTED = TRANSLATED / "corrected"
LEDGERS = TRANSLATED / "_EditLedgers"
PROOFREAD_DIR = ROOT / "proofread"

# Where translated editions actually live. `proofread\` first: the live Kennedy
# Blake editions are there, while the similarly-named files in `translated\` are
# SUPERSEDED drafts. Getting this backwards means proofreading a dead file.
EDITION_DIRS = [PROOFREAD_DIR, TRANSLATED]
# English sources: `translate\` per the skill, `Scripts\` as the documented
# fallback (which is where the KB masters actually are).
SOURCE_DIRS = [ROOT / "translate", ROOT / "translate_now", ROOT]

CHAP = re.compile(
    r"^(Chapter|Chapitre|Kapitel|Capitolo|Capítulo|Hoofdstuk|Kapittel|Kapitola|"
    r"Rozdział|Capitolul|Κεφάλαιο|Kabanata|Bölüm|Kapitel)\s+(\d+)\s*$", re.I)
SCENE = re.compile(r"^[\*\s\u2022\u00b7]+$")
SPAN = re.compile(r"\*([^*\n]+?)\*")
IMPERIAL = re.compile(
    r"\b\d*\s*(pieds?|pouces?|livres?|milles?|Fuß|Zoll|Pfund|Meilen?|piedi|"
    r"pollic[ei]|libbr\w*|migli[ao]|acri|iarde|yards?|inch(es)?|feet|foot|"
    r"pounds?|ounces?|gallons?)\b", re.I)
# <bt>...</bt> book-title anchors (bt_anchors.py lifecycle). A proofread pass must
# NEVER strip these: `stamp` later swaps each span for the catalogue Title (local).
# Two agents silently removed all of them on 2026-08-24 and every other check passed.
BT_SPAN = re.compile(r"<bt>(.*?)</bt>", re.S)
BT_MARK = re.compile(r"</?bt>")

# Stray markup: any <tag> that is NOT a <bt> marker. Translation models have emitted
# <div>, <u>, <sup>, <indent>, <a name=...> and raw <bos> tokens into the prose. A <bos>
# can eat characters mid-word ("nu-<bos>4?" for "nu-i asa?"), so this is a text-integrity
# check, not just a cosmetic one. Found 2026-08-26 in 14 files; nothing scanned for it.
STRAY_TAG = re.compile(r"<(?!/?bt>)[a-zA-Z/][^>]{0,40}>")

_CAT_CACHE = {}


def catalogue_titles():
    """Every EN title in Lisa's catalogue. Used to check that a <bt> span actually
    wraps a book title -- `stamp` silently emits ENGLISH for anything it can't map."""
    if "t" in _CAT_CACHE:
        return _CAT_CACHE["t"]
    out = set()
    try:
        import openpyxl
        wb = openpyxl.load_workbook(
            r"C:\Users\User\Desktop\Excel Files\Book Catalogue.xlsx",
            read_only=True, data_only=True)
        rows = wb["Catalogue"].iter_rows(values_only=True)
        hdr = next(rows)
        idx = {h: i for i, h in enumerate(hdr) if h}
        for r in rows:
            if r and r[idx["Title (EN)"]]:
                out.add(str(r[idx["Title (EN)"]]).strip())
    except Exception:
        pass                      # catalogue unavailable -> check degrades to a no-op
    _CAT_CACHE["t"] = out
    return out


def norm_title(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    return re.sub(r"\s+", " ", s).strip().lower().rstrip("!.,")


# Real published works legitimately named inside the prose (not Lisa's, not in the
# catalogue). Anything outside catalogue+this set is a mis-tag, not a title.
REAL_WORKS = {norm_title(x) for x in (
    "The Wizard of Oz", "The Sunday Girl", "Pride and Prejudice", "Star Wars",
    "The Comedy of Errors", "True Detective", "Enola Holmes", "Alice in Wonderland",
    "Alice's Adventures in Wonderland", "The Mandalorian", "Strangers on a Train",
    "Die Hard", "Mad Max", "Tarzan", "Spider-Man", "Dune", "Rogue One",
    "Fiddler on the Roof", "Come Fly with Me", "A Mother's Reckoning", "Root Cause",
    "Ascending Chaos", "The Iron Rose", "The Moonlight Altar", "Haunted Portsmouth",
    "The History of the Sicilian Mafia", "Cotton, Clothing, and Controversy",
    "Christmas in Portsmouth", "Mountain Men of Cupid Lake",
    "Drostov's Book of Potions and the Healing Arts",
    "Drostov's Book of Potions and the Healing Art",
    # Real titles whose in-book form differs from the catalogue's plain-ASCII cell:
    # an accent the catalogue drops, or a title page carrying the series subtitle.
    "Weekend Fiancee", "Weekend Fiancée",
    "Kyle: Starke Private Security Book 1")}

BACKMATTER = ("Excerpt from", "Extrait de", "Leseprobe aus", "Estratto da",
              "What's Next", "Et ensuite", "Wie geht es weiter", "Cosa")


def parse(path):
    with zipfile.ZipFile(path) as z:
        x = ET.fromstring(z.read("word/document.xml"))
    paras, italics, h1 = [], [], 0
    for p in x.iter(W + "p"):
        t = "".join(q.text or "" for q in p.iter(W + "t")).strip()
        st = p.find(W + "pPr/" + W + "pStyle")
        sty = st.get(W + "val") if st is not None else ""
        if sty.startswith("Heading1"):
            h1 += 1
        paras.append(t)
    for r in x.iter(W + "r"):
        rpr = r.find(W + "rPr")
        # NOTE: parse the <w:i> CHILD ELEMENT. Do not string-count "<w:i/>" —
        # python-docx-style writers emit "<w:i />" with a space and the count
        # silently comes back 0.
        if rpr is not None and rpr.find(W + "i") is not None:
            s = "".join(q.text or "" for q in r.iter(W + "t")).strip()
            if s:
                italics.append(s)
    joined = chr(10).join(paras)
    bt = BT_SPAN.findall(joined)
    unpaired = len(BT_MARK.findall(joined)) - 2 * len(bt)
    stray = STRAY_TAG.findall(joined)
    return paras, italics, h1, bt, unpaired, stray


def chapters(paras):
    return [int(m.group(2)) for t in paras if (m := CHAP.match(t))]


def find_edition(stem):
    # " - FORMATTED" FIRST: that copy is the deliverable and the only one carrying
    # Heading1 styles. Preferring the bare stem picked up the raw pre-format draft
    # and reported "0 Heading1" for editions that are in fact fully styled.
    for d in EDITION_DIRS:
        for cand in (d / f"{stem} - FORMATTED.docx", d / f"{stem}.docx"):
            if cand.exists():
                return cand
    return None


def find_source(stem):
    base = re.sub(r"_[A-Z][A-Za-z ]+$", "", stem)
    for d in SOURCE_DIRS:
        for cand in (d / f"{base}.docx", d / f"{base} - FORMATTED.docx"):
            if cand.exists():
                return cand
    return None


def report(stem, current=False):
    # With --current, inspect the corrected\ copy when one exists — otherwise the
    # report describes the untouched source and re-flags work already done.
    ed = None
    if current and (CORRECTED / f"{stem}.docx").exists():
        ed = CORRECTED / f"{stem}.docx"
    if ed is None:
        ed = find_edition(stem)
    if not ed:
        print(f"  {stem[:52]:52} EDITION NOT FOUND")
        return
    src = find_source(stem)
    ep, ei, eh, _bt, _unp, _st = parse(ed)
    ne = [t for t in ep if t]
    chs = chapters(ep)
    scene = sum(1 for t in ep if t and SCENE.match(t))
    spans = sum(len(SPAN.findall(t)) for t in ep
                if t and not SCENE.match(t))
    units = sum(len(IMPERIAL.findall(t)) for t in ep)
    bm = any(any(b in t for b in BACKMATTER) for t in ep)

    # chapter sequence: allow one trailing restart (the Book-N sample chapter)
    body = chs[:-1] if len(chs) > 1 and chs[-1] == 1 else chs
    seq_ok = body == list(range(1, len(body) + 1))
    missing = [n for n in range(1, (max(body) if body else 0) + 1)
               if n not in body]
    dupes = sorted({n for n in body if body.count(n) > 1})

    if src:
        sp, _, _, _bt, _unp, _st = parse(src)
        sn = len([t for t in sp if t])
        sscene = sum(1 for t in sp if t and SCENE.match(t))
        delta = f"{len(ne) - sn:+d}"
        sc = f"{scene}/{sscene}"
    else:
        delta, sc = "NO SRC", str(scene)

    lang = stem.rsplit("_", 1)[-1]
    flags = []
    if not seq_ok:
        flags.append(f"CHAPTERS missing={missing or '-'} dup={dupes or '-'}")
    if eh == 0:
        flags.append("NO Heading1 (formatter will hard-stop)")
    if spans:
        flags.append(f"{spans} md-asterisk spans")
    if units:
        flags.append(f"{units} imperial tokens")
    if not bm:
        flags.append("no back matter")
    if src and abs(len(ne) - sn) > 60:
        flags.append(f"para gap {delta}")

    have = "".join([
        "R" if (LEDGERS / f"{stem}_PROOFREAD.md").exists()
             or (TRANSLATED / f"{stem}_proofread.md").exists() else "-",
        "C" if (CORRECTED / f"{stem}.docx").exists() else "-",
        "A" if (LEDGERS / f"{stem}_APPLIED.md").exists() else "-",
    ])

    print(f"  {lang:10} ch={len(chs):3} h1={eh:3} paras={len(ne):5} "
          f"vs-en={delta:>7} scene={sc:>8} [{have}]  "
          f"{'; '.join(flags) if flags else 'clean'}")


def verify(stem, expect_paras=0, expect_italics=0):
    """Integrity check: corrected\\<stem> against the source edition.

    Use after a sub-agent write. By default it demands EXACT equality, which is
    right for a proofread or units pass (those change text, never structure).

    When a pass legitimately adds material, declare it:
      --expect-paras 29     e.g. restored back matter
      --expect-italics 24   e.g. asterisk -> italic conversion
    An undeclared change is the failure this check exists to catch: on Book 1 a
    German grammar fix silently merged an italic run out of existence.
    """
    src = find_edition(stem)
    dst = CORRECTED / f"{stem}.docx"
    if not src or not dst.exists():
        print("verify: source or corrected copy missing")
        return 1
    sp, si, _, sbt, sunp, sstray = parse(src)
    dp, di, _, dbt, dunp, dstray = parse(dst)
    ss = sum(1 for t in sp if t and SCENE.match(t))
    ds = sum(1 for t in dp if t and SCENE.match(t))
    ok = True

    def line(label, a, b, allowed=0):
        nonlocal ok
        delta = b - a
        good = (delta == allowed)
        if not good:
            ok = False
        note = "ok" if good else f"UNDECLARED {delta:+d} (expected {allowed:+d})"
        print(f"    {label:22} {a!s:>7} -> {b!s:<7} {note}")

    line("paragraphs", len(sp), len(dp), expect_paras)
    line("italic runs", len(si), len(di), expect_italics)

    # Sequence check. With no declared additions the lists must match exactly;
    # with additions, every ORIGINAL italic run must still be present in order.
    if expect_italics == 0:
        same = si == di
        print(f"    {'italic sequence':22} {'identical' if same else 'DIFFERS':>7}")
        if not same:
            ok = False
            for n, (a, b) in enumerate(zip(si, di)):
                if a != b:
                    print(f"      first diff @{n}: {a[:44]!r} -> {b[:44]!r}")
                    break
    else:
        it = iter(di)
        kept = all(any(x == y for y in it) for x in si)
        print(f"    {'italic subsequence':22} "
              f"{'all originals kept' if kept else 'ORIGINAL RUN LOST':>7}")
        if not kept:
            ok = False

    line("scene breaks", ss, ds)

    # <bt> book-title anchors. NEVER an allowed delta: `bt_anchors.py stamp` needs
    # every span to localize titles. Losing them is invisible in the prose and
    # ships English titles in a translated edition.
    line("bt anchors", len(sbt), len(dbt))
    if sorted(sbt) != sorted(dbt):
        ok = False
        lost = [t for t in sbt if t not in dbt]
        print(f"    {'bt titles':22} MISMATCH  lost={lost[:4]}")
    else:
        print(f"    {'bt titles':22} {'identical' if sbt else 'none present':>7}")
    if dunp:
        ok = False
        print(f"    {'bt markers':22} UNPAIRED x{dunp} (malformed)")

    # Do the anchors actually wrap BOOK TITLES? `stamp` falls through to the ENGLISH
    # text for anything not in the catalogue, so a mis-tagged shop/place name ships
    # English into a translated edition. 134 such anchors were found corpus-wide
    # on 2026-08-26 (e.g. <bt>The Fancy Tart</bt>, <bt>familiar</bt>, <bt>63</bt>).
    cat = catalogue_titles()
    if cat:
        known = {norm_title(t) for t in cat} | REAL_WORKS
        mis = [t for t in dbt
               if norm_title(t) not in known
               and not norm_title(t).startswith("isabella proctor cozy myster")]
        if mis:
            ok = False
            print(f"    {'bt not-a-title':22} MIS-TAGGED x{len(mis)}  {mis[:4]}")
        else:
            print(f"    {'bt not-a-title':22} {'all titles' if dbt else 'n/a':>10}")

    # Stray markup / model tokens in the prose.
    if dstray:
        ok = False
        uniq = sorted(set(dstray))
        print(f"    {'stray tags':22} x{len(dstray)}  {uniq[:5]}")

    changed = sum(1 for a, b in zip(sp, dp) if a != b)
    print(f"    {'paragraphs changed':22} {changed}")
    print(f"    => {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", help="book stem prefix, e.g. KB_H1_2")
    ap.add_argument("--langs", help="comma-separated language list")
    ap.add_argument("--verify", help="stem to integrity-check")
    ap.add_argument("--current", action="store_true",
                    help="inspect corrected/ copies where they exist")
    ap.add_argument("--expect-paras", type=int, default=0,
                    help="paragraphs this pass legitimately ADDED (e.g. back matter)")
    ap.add_argument("--expect-italics", type=int, default=0,
                    help="italic runs this pass legitimately ADDED (e.g. asterisk conversion)")
    a = ap.parse_args()

    if a.verify:
        sys.exit(verify(a.verify, a.expect_paras, a.expect_italics))

    stems = set()
    for d in EDITION_DIRS:
        for p in d.glob("*.docx"):
            if p.name.startswith("~$"):
                continue
            s = p.stem
            if s.endswith(" - FORMATTED"):
                s = s[:-len(" - FORMATTED")]
            if a.book and not s.startswith(a.book):
                continue
            if not a.book and not s.startswith("KB_H1"):
                continue
            stems.add(s)

    if a.langs:
        want = {x.strip() for x in a.langs.split(",")}
        stems = {s for s in stems if s.rsplit("_", 1)[-1] in want}

    by_book = {}
    for s in sorted(stems):
        m = re.match(r"(KB_H1_\d|.+?)_[A-Z][A-Za-z ]*$", s)
        by_book.setdefault(s.rsplit("_", 1)[0], []).append(s)

    for book in sorted(by_book):
        print(f"\n{book}")
        for s in sorted(by_book[book]):
            report(s, a.current)
    print("\n[R]eport [C]orrected [A]pplied — '-' means absent")


if __name__ == "__main__":
    main()
