# -*- coding: utf-8 -*-
"""<bt> book-title anchors — the two halves of the title-safe translation path.

Per PUBLISH_PIPELINE_BUILD_PLAN.md ("<bt> anchor lifecycle", lines 192-199):

  wrap  : English consolidated .docx  ->  translator copy carrying <bt>…</bt> around every
          book-title occurrence (title page + all back-matter titles).
          ⚑ The English book that goes to the FORMATTER must never carry anchors — the
          formatter hard-errors (exit 6) on any <...> token. So this writes a SEPARATE file.

  stamp : translated .docx (anchors preserved by the translator)  ->  clean localized .docx,
          with each <bt> span replaced by the catalogue's Title (local) and the markers
          stripped. Nothing downstream ever sees a <bt>.

Usage:
  python bt_anchors.py wrap  "<english.docx>" [--out "<translator_copy.docx>"]
  python bt_anchors.py stamp "<translated.docx>" --lang "Polish" [--out "<clean.docx>"]
  python bt_anchors.py check "<any.docx>"

The catalogue is READ-ONLY here (it is Lisa's source of truth).
"""
import sys, os, re, argparse

CATALOGUE = r"C:\Users\User\Desktop\Excel Files\Book Catalogue.xlsx"

# Titles that may appear inside these books' front/back matter. Longest-first matching so
# no title that is a prefix of another gets half-wrapped.
KNOWN_TITLES = [
    "All the Wild Places",
    "Sparks We Left Behind",
    "Where the River Remembers",
    "What the Land Holds",
    "Every Little Thing",
    # cross-series promo target (Book 5 back matter)
    "Hitched and Ditched",
]

BT_SPAN_RE = re.compile(r"<bt>(.*?)</bt>", re.S)


def _titles_longest_first():
    return sorted(KNOWN_TITLES, key=len, reverse=True)


def load_catalogue_titles(language):
    """{Title (EN): Title (local)} for one language, from the catalogue."""
    import openpyxl
    wb = openpyxl.load_workbook(CATALOGUE, read_only=True, data_only=True)
    ws = wb["Catalogue"]
    rows = ws.iter_rows(values_only=True)
    hdr = next(rows)
    idx = {h: i for i, h in enumerate(hdr) if h}
    out = {}
    for r in rows:
        if not r or not r[idx["Language"]]:
            continue
        if str(r[idx["Language"]]).strip().lower() != language.strip().lower():
            continue
        en = (r[idx["Title (EN)"]] or "").strip()
        loc = (r[idx["Title (local)"]] or "").strip()
        if en and loc:
            out[en] = loc
    return out


# ---------------------------------------------------------------- wrap
def wrap_docx(src, dst):
    """Copy src -> dst, wrapping every known book title in <bt>…</bt>.

    Runs are edited in place at the XML level so italics/bold on the title survive: a title
    sitting inside one run gets the markers inside that same run. A title split across runs
    (Word does this freely) is handled by rewriting the paragraph's first run to the fully
    marked text and blanking the rest — the paragraph's formatting comes from its first run,
    which is what the title page and back-matter headings rely on.
    """
    from docx import Document
    d = Document(src)
    titles = _titles_longest_first()
    n_wrapped = 0
    n_paras = 0

    # ⚑ Only the TITLE PAGE and the BACK MATTER get anchors.
    # The formatter BUILDS the "Other Books by"/"Books in this series" pages and the Table of
    # Contents itself, from the catalogue, language-scoped — and rebuilds them on the translated
    # run too. Anchoring a title inside those regions is pointless at best; at worst we stamp a
    # localized title into a block the formatter is about to regenerate, or wrap an unrelated
    # series' title (e.g. the Evergreen catalogue list) that this book's back matter never cites.
    # So: wrap paragraph 0..(end of title page), then everything from the LAST chapter onward.
    texts = [p.text.strip() for p in d.paragraphs]
    chap_idx = [i for i, t in enumerate(texts) if re.fullmatch(r"Chapter\s+\d+", t)]
    # the TOC repeats "Chapter N"; real chapters are the LATER, monotonically-final run
    last_chapter = chap_idx[-1] if chap_idx else 0
    # title page = up to the copyright line (or the first catalogue-page heading)
    stop_front = next((i for i, t in enumerate(texts)
                       if t.startswith("Copyright") or t.startswith("Other Books")
                       or t.startswith("Books in this")), 8)

    def in_scope(i):
        return i < stop_front or i > last_chapter

    for i, p in enumerate(d.paragraphs):
        if not in_scope(i):
            continue
        full = p.text
        if not full.strip():
            continue
        if not any(t in full for t in titles):
            continue
        marked = full
        hits = 0
        for t in titles:
            if t in marked and f"<bt>{t}</bt>" not in marked:
                cnt = marked.count(t)
                marked = marked.replace(t, f"<bt>{t}</bt>")
                hits += cnt
        if marked == full:
            continue
        runs = p._p.xpath('.//w:r')
        if not runs:
            continue
        # write everything into the first run, clear the others (keeps the paragraph's look)
        from docx.text.run import Run
        first = Run(runs[0], p)
        first.text = marked
        for r_el in runs[1:]:
            Run(r_el, p).text = ""
        n_wrapped += hits
        n_paras += 1

    d.save(dst)
    return n_wrapped, n_paras


# ---------------------------------------------------------------- stamp
def stamp_docx(src, dst, language):
    """Replace every <bt>English title</bt> span with the catalogue's Title (local), strip markers."""
    from docx import Document
    from docx.text.run import Run
    mapping = load_catalogue_titles(language)
    d = Document(src)
    n_stamped = 0
    missing = set()
    leftover = 0

    for p in d.paragraphs:
        full = p.text
        if "<bt>" not in full and "</bt>" not in full:
            continue

        def sub(m):
            nonlocal n_stamped
            en = m.group(1).strip()
            loc = mapping.get(en)
            if loc:
                n_stamped += 1
                return loc
            missing.add(en)
            return en          # fall back to the English title rather than leaving a marker

        new = BT_SPAN_RE.sub(sub, full)
        # any unpaired markers the model mangled: drop the tag, keep the words
        new2 = new.replace("<bt>", "").replace("</bt>", "")
        if new2 != new:
            leftover += 1
        runs = p._p.xpath('.//w:r')
        if not runs:
            continue
        first = Run(runs[0], p)
        first.text = new2
        for r_el in runs[1:]:
            Run(r_el, p).text = ""

    d.save(dst)
    return n_stamped, sorted(missing), leftover


# ---------------------------------------------------------------- check
def check_docx(src):
    from docx import Document
    d = Document(src)
    spans, unpaired = [], 0
    for p in d.paragraphs:
        t = p.text
        spans += BT_SPAN_RE.findall(t)
        if t.count("<bt>") != t.count("</bt>"):
            unpaired += 1
    return spans, unpaired


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["wrap", "stamp", "check"])
    ap.add_argument("input")
    ap.add_argument("--out")
    ap.add_argument("--lang")
    a = ap.parse_args()

    if a.mode == "wrap":
        out = a.out or re.sub(r"\.docx$", " - FOR TRANSLATION.docx", a.input)
        n, paras = wrap_docx(a.input, out)
        print(f"wrapped {n} title occurrence(s) across {paras} paragraph(s)")
        print("->", out)
        spans, unpaired = check_docx(out)
        print(f"verify: {len(spans)} <bt> span(s), {unpaired} unpaired-marker paragraph(s)")
        for s in dict.fromkeys(spans):
            print("   ", repr(s))

    elif a.mode == "stamp":
        if not a.lang:
            sys.exit("stamp needs --lang")
        out = a.out or re.sub(r"\.docx$", " - STAMPED.docx", a.input)
        n, missing, leftover = stamp_docx(a.input, out, a.lang)
        print(f"stamped {n} title span(s) with {a.lang} catalogue titles -> {out}")
        if missing:
            print("  ! no catalogue Title (local) for:", missing,
                  "\n    (left in English — fill the catalogue and re-stamp)")
        if leftover:
            print(f"  ! {leftover} paragraph(s) had unpaired <bt> markers; tags stripped, text kept")
        spans, unpaired = check_docx(out)
        if spans or unpaired:
            print(f"  !! {len(spans)} span(s) still present — investigate")
        else:
            print("  verify: no <bt> tokens remain (formatter-safe)")

    else:
        spans, unpaired = check_docx(a.input)
        print(f"{len(spans)} <bt> span(s), {unpaired} unpaired-marker paragraph(s)")
        for s in dict.fromkeys(spans):
            print("   ", repr(s))


if __name__ == "__main__":
    main()
