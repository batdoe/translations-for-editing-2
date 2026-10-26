#!/usr/bin/env python3
"""claude_translate.py — translation and proofreading for the book pipeline, on Claude.

Written to replace the Gemini free-tier path in translate_books_overnight.py, which
stalls on GenerateRequestsPerDayPerProjectPerModel: ~18-20 proofread requests/day on
the good model, which is why only 14 of 132 translations ever got proofread. Claude's
paid limits are per-minute, not per-day, so a whole-corpus run finishes overnight
instead of over weeks.

THREE COMMANDS
  blocked    Fill [[⚠ PASSAGE BLOCKED BY CONTENT FILTER ...]] placeholders.
             Requires a mapping file (see --map); this script does NOT guess which
             English paragraph a placeholder replaces. Paragraph counts drift between
             editions (measured -82..+29), and automated alignment was wrong by 44
             paragraphs on a hand-verified case, so the mapping is an input, not a
             derivation.

  proofread  Whole-book bilingual proofread -> a Markdown findings report.
             This is the pass that would have caught the untranslated-English runs.
             ⚑⚑ THIS COMMAND NEEDS AN ANTHROPIC API KEY AND LISA DOES NOT HAVE ONE.
             She pays for Claude Code / Cowork / the app and is not buying API
             access as well. USE THE `/proofread` SLASH COMMAND INSTEAD — it does
             the same pass (plus applies the fixes) using Claude Code sub-agents,
             sequentially over the whole folder, at no API cost. This code is kept
             only because `blocked` shares its docx plumbing; do not build on it.

  langcheck  Deterministic scan for untranslated English prose. No API calls, no cost.
             Run this FIRST — it is free and catches the defect class that both the
             structural sweep and the length-sanity check pass silently.

WHY A SEPARATE SCRIPT
Left translate_books_overnight.py alone: it holds the chunking, bible-building,
italics/bold preservation, and .docx rebuild logic, and rewriting its model layer
in place would risk 132 already-translated files. This handles the two passes that
were quota-starved, reading and writing the same .docx files.

USAGE
  pip install anthropic
  setx ANTHROPIC_API_KEY sk-ant-...        # or: ant auth login

  python claude_translate.py langcheck
  python claude_translate.py proofread --file "translated/<book>_Greek.docx"
  python claude_translate.py proofread --all --limit 5
  python claude_translate.py blocked --map blocked_map.json --dry-run

Every write is gated on a verification pass and backs up the original first.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import unicodedata
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
TRANSLATED = SCRIPTS / "translated"
CORRECTED = TRANSLATED / "corrected"
EN_DIRS = [SCRIPTS / "translate", SCRIPTS]
DOC = "word/document.xml"

MODEL = "claude-opus-5"
BLOCK_MARKER = "CONTENT FILTER"

# Chapter word per language, as the translation kit emits it.
CHAP_WORDS = {
    "French": "Chapitre", "German": "Kapitel", "Italian": "Capitolo",
    "Spanish": "Capítulo", "Brazilian Portuguese": "Capítulo",
    "Romanian": "Capitolul", "Greek": "Κεφάλαιο",
    "Turkish": "Bölüm", "Tagalog": "Kabanata", "Filipino": "Kabanata",
    "Czech": "Kapitola", "Dutch": "Hoofdstuk", "Norwegian": "Kapittel",
    "Swedish": "Kapitel", "Polish": "Rozdział", "Danish": "Kapitel",
}

BACKUPS = {
    "blocked": TRANSLATED / "_claude_blocked_backups",
    "proofread": None,          # proofread never edits the .docx
}


# ---------------------------------------------------------------- docx plumbing

def _clean(para_xml: str) -> str:
    """Visible text of one <w:p>, with nested tags stripped.

    MMM.docx carries <w:rPr> runs inside <w:t>, so a bare findall leaks tag soup
    into the text — hence the second re.sub.
    """
    t = "".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", para_xml, re.S))
    t = re.sub(r"<[^>]+>", "", t)
    return (t.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
             .replace("&quot;", '"').replace("&apos;", "'")).strip()


def para_spans(xml: str) -> list[tuple[int, int, str]]:
    """(start, end, text) for every paragraph, in document order."""
    return [(m.start(), m.end(), _clean(m.group(0)))
            for m in re.finditer(r"<w:p[ >].*?</w:p>", xml, re.S)]


def paras(path: Path) -> list[str]:
    with zipfile.ZipFile(path) as z:
        xml = z.read(DOC).decode("utf8", "replace")
    return [t for _, _, t in para_spans(xml)]


def set_para_text(para_xml: str, new_text: str) -> str | None:
    """Replace a paragraph's text, keeping the first run's formatting.

    Returns None when there is no run to clone — callers must treat that as a
    failure rather than writing a malformed paragraph.
    """
    esc = new_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    runs = list(re.finditer(r"<w:r[ >].*?</w:r>", para_xml, re.S))
    if not runs:
        return None
    first = runs[0].group(0)
    if re.search(r"<w:t[^>]*>.*?</w:t>", first, re.S):
        new_first = re.sub(r"(<w:t[^>]*>).*?(</w:t>)",
                           lambda m: m.group(1) + esc + m.group(2),
                           first, count=1, flags=re.S)
    else:
        new_first = first.replace(
            "</w:r>", f'<w:t xml:space="preserve">{esc}</w:t></w:r>')
    return para_xml[:runs[0].start()] + new_first + para_xml[runs[-1].end():]


def write_docx(path: Path, xml: str, backup_dir: Path | None, tag: str) -> None:
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        others = {n: z.read(n) for n in names if n != DOC}
    if backup_dir is not None:
        backup_dir.mkdir(exist_ok=True)
        shutil.copy2(path, backup_dir / f"{path.stem}.{tag}.docx")
    tmp = path.with_suffix(".docx.tmp")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as out:
        for n in names:
            out.writestr(n, xml.encode("utf8") if n == DOC else others[n])
    shutil.move(str(tmp), str(path))


def lang_of(path: Path) -> str | None:
    stem = re.sub(r" - (FORMATTED|REPAIRED)$", "", path.stem)
    return next((l for l in CHAP_WORDS if stem.endswith("_" + l)), None)


def en_source_for(path: Path) -> Path | None:
    stem = re.sub(r" - (FORMATTED|REPAIRED)$", "", path.stem)
    m = re.search(r"^(.*)_([A-Z][A-Za-z ]+)$", stem)
    if not m:
        return None
    base = m.group(1)
    for d in EN_DIRS:
        for cand in (base + ".docx", base + " - FORMATTED.docx"):
            if (d / cand).exists():
                return d / cand
    return None


def translation_files() -> list[Path]:
    return [p for p in sorted(TRANSLATED.glob("*.docx"))
            if not p.name.startswith("~$")
            and " - FORMATTED.docx" not in p.name]


# ----------------------------------------------------------------- Claude client

def make_client():
    try:
        import anthropic
    except ImportError:
        sys.exit("The anthropic SDK is not installed.  pip install anthropic")
    # Zero-arg constructor resolves ANTHROPIC_API_KEY, ANTHROPIC_AUTH_TOKEN, or an
    # `ant auth login` profile — so it works without an env var after a CLI login.
    try:
        return anthropic.Anthropic()
    except Exception as exc:
        sys.exit(f"Could not construct the Anthropic client: {exc}\n"
                 "Set ANTHROPIC_API_KEY or run: ant auth login")


def call_claude(client, *, system: str, user: str, max_tokens: int,
                effort: str = "high") -> str:
    """One request, streamed.

    Streaming is not optional at these sizes: a whole-book proofread runs long
    enough that a non-streaming call risks an HTTP timeout, and the SDK refuses
    large non-streaming max_tokens outright.
    """
    import anthropic
    try:
        with client.messages.stream(
            model=MODEL,
            max_tokens=max_tokens,
            system=system,
            output_config={"effort": effort},
            messages=[{"role": "user", "content": user}],
        ) as stream:
            msg = stream.get_final_message()
    except anthropic.RateLimitError as exc:
        retry = exc.response.headers.get("retry-after", "60") if exc.response else "60"
        raise RuntimeError(f"rate limited; retry after {retry}s") from exc
    except anthropic.APIStatusError as exc:
        raise RuntimeError(f"API error {exc.status_code}: {exc.message}") from exc

    # A refusal is a successful HTTP 200 with an empty/partial content list, so
    # stop_reason has to be checked before indexing into content.
    if msg.stop_reason == "refusal":
        cat = getattr(getattr(msg, "stop_details", None), "category", None)
        raise RuntimeError(f"model declined the request (category={cat})")
    text = "".join(b.text for b in msg.content if b.type == "text")
    if not text.strip():
        raise RuntimeError(f"empty response (stop_reason={msg.stop_reason})")
    return text.strip()


# ------------------------------------------------------------------- langcheck

# English function words that are rare or absent in the target languages. A
# paragraph dense in these, with no target-language diacritics, is untranslated.
_EN_WORDS = set("""
the and that with was were have has had been from they them their there this
these those which would could should about into over after before because while
when what where who whom how said says like just only very much more most her
his him she he it its our your you i me my we not no but for of to in on at by
as is are am be being do does did done get got make made take took see saw know
knew think thought want wanted come came look looked stay stays room
""".split())

_DIACRITICS = re.compile(
    r"[àâäçèéêëîïôöùûüßñáíóúãõęółśćźżăîșțčřšžůěαβγδεζηθικλμνξοπρστυφχψω]", re.I)

# English titles legitimately appear in back-matter blurbs ("The series continues
# with Name on the Door") — those are not translation failures.
_TITLES = re.compile(
    r"(Women of the Ice|Out of His League|Name on the Door|Money Can|"
    r"Above the Fold|More Than a Legend|Hard Checked|Net Worth|Power Play|"
    r"Safe Zone|Snapshot|Kestrels|Glaciers)", re.I)


def looks_english(text: str, *, min_words: int = 10, threshold: float = 0.28) -> bool:
    words = [w.strip(".,!?;:\"“”«»‘’'()—–…").lower() for w in text.split()]
    words = [w for w in words if w]
    if len(words) < min_words:
        return False
    if _DIACRITICS.search(text):
        return False
    share = sum(1 for w in words if w in _EN_WORDS) / len(words)
    if share < threshold:
        return False
    if _TITLES.search(text) and len(words) < 25:
        return False
    return True


def cmd_langcheck(args) -> int:
    files = translation_files()
    if args.file:
        files = [Path(args.file)]
    rows = []
    for path in files:
        lang = lang_of(path)
        if not lang:
            continue
        try:
            body = paras(path)
        except Exception as exc:
            print(f"  !! {path.name}: {exc}")
            continue
        hits = [(i, t) for i, t in enumerate(body)
                if BLOCK_MARKER not in t and looks_english(t)]
        if not hits:
            continue
        runs: list[list[int]] = []
        for i, _ in hits:
            if runs and i - runs[-1][-1] <= 3:
                runs[-1].append(i)
            else:
                runs.append([i])
        rows.append({
            "file": path.name, "lang": lang, "hits": hits, "runs": runs,
            "words": sum(len(t.split()) for _, t in hits),
        })

    rows.sort(key=lambda r: -r["words"])
    total = 0
    for r in rows:
        longest = max(len(run) for run in r["runs"])
        flag = f"   <== RUN of {longest} paragraphs" if longest >= 3 else ""
        print(f"{r['words']:>6}w  {len(r['hits']):>3}p  "
              f"{r['file'][:58]:<60} [{r['lang']}]{flag}")
        for i, t in r["hits"][:args.show]:
            print(f"           [{i}] {t[:100]}")
        if len(r["hits"]) > args.show:
            print(f"           ... {len(r['hits']) - args.show} more")
        total += r["words"]
    print(f"\n{len(rows)} file(s), {total:,} untranslated English words")
    if not rows:
        print("No untranslated English prose detected.")
    return 0


# ------------------------------------------------------------------- proofread

PROOF_SYSTEM = """You are a senior literary proofreader working into {lang}.

You are given a {lang} translation of a published romance novel and the English
source it was translated from. Report concrete, fixable problems, most serious
first.

Check for, in priority order:
1. UNTRANSLATED ENGLISH — any passage left in English. Report every occurrence.
2. Omissions — source content missing from the translation.
3. Mistranslations, reversed meaning (negation, passive, comparatives), false friends.
4. Untranslated or wrongly declined proper names; pronoun and gender agreement.
5. Register or formality drift; wrong or over-literal idiom.
6. Name/term inconsistency across the book; tense drift; typos.
7. Missing scene-break markers.

Output rules:
- Output ONLY a Markdown list of findings. No preamble, no closing summary.
- Write every explanation in ENGLISH so an English-speaking author can act on it.
- Quote the {lang} text VERBATIM; never translate a quote into English.
- Give the corrected phrasing in {lang}.
- Each finding: (1) the {lang} quote, (2) an English explanation, (3) the fix.
- If you find nothing worth fixing, output exactly: NO FINDINGS."""


def cmd_proofread(args) -> int:
    # Defer client construction so --dry-run works without the SDK or a key —
    # it only reports what would be sent.
    client = None if args.dry_run else make_client()
    if args.file:
        targets = [Path(args.file)]
    elif args.all:
        targets = translation_files()
    else:
        sys.exit("Pass --file <path> or --all")

    done = skipped = failed = 0
    for path in targets:
        if args.limit and done >= args.limit:
            print(f"\nStopping at --limit {args.limit}.")
            break
        lang = lang_of(path)
        if not lang:
            continue
        out_path = TRANSLATED / f"{path.stem}_proofread.md"
        if out_path.exists() and not args.force:
            skipped += 1
            continue
        en_path = en_source_for(path)
        if en_path is None:
            print(f"  !! {path.name}: no English source found")
            failed += 1
            continue

        target_text = "\n\n".join(t for t in paras(path) if t)
        source_text = "\n\n".join(t for t in paras(en_path) if t)
        print(f"proofreading {path.name}  [{lang}]  "
              f"({len(target_text.split()):,} words vs "
              f"{len(source_text.split()):,} English)")
        if args.dry_run:
            done += 1
            continue

        user = (f"ENGLISH SOURCE:\n{source_text}\n\n"
                f"=== END OF SOURCE ===\n\n"
                f"{lang.upper()} TRANSLATION TO PROOFREAD:\n{target_text}")
        try:
            report = call_claude(
                client,
                system=PROOF_SYSTEM.format(lang=lang),
                user=user,
                max_tokens=32000,
                effort=args.effort,
            )
        except RuntimeError as exc:
            print(f"  !! {exc}")
            failed += 1
            continue

        header = (f"# Proofread — {path.name}\n\n"
                  f"Language: {lang}  ·  model: {MODEL}  ·  effort: {args.effort}\n"
                  f"English source: {en_path.name}\n\n---\n\n")
        out_path.write_text(header + report + "\n", encoding="utf8")
        n = len([l for l in report.splitlines() if l.strip().startswith(("-", "*", "#"))])
        print(f"  wrote {out_path.name}  (~{n} finding lines)")
        done += 1

    print(f"\nproofread {done}, skipped {skipped} (report exists), failed {failed}")
    if skipped and not args.force:
        print("Use --force to regenerate existing reports.")
    return 0 if not failed else 1


# --------------------------------------------------------------------- blocked

BLOCKED_SYSTEM = """You are a professional literary translator working into {lang}.

Translate the passage into {lang}. It is from a commercially published
contemporary romance novel and depicts consenting adults.

Preserve the author's voice, rhythm, register, and level of explicitness exactly.
Do not soften, censor, summarise, omit, or add anything. Match the surrounding
narrative style — first person, and the tense as written.

Output ONLY the {lang} translation: no notes, no preamble, no quotation marks
wrapped around the whole thing, no commentary about the content."""

# A model can "succeed" while refusing — returning an apology or offering a
# summary. One such reply was spliced into a book before this check existed.
_REFUSAL = re.compile(
    r"\b(I cannot|I can't|I can’t|I am unable|I'm unable|cannot translate"
    r"|copyrighted work|as an AI|I apologize|I'm sorry|general summary"
    r"|instead,? I can|here is a summary)\b", re.I)

_NON_LATIN = {"Greek"}


def validate_translation(out: str, src: str, lang: str) -> tuple[bool, str]:
    if not out or len(out.split()) < 3:
        return False, "empty or too short"
    if _REFUSAL.search(out):
        return False, "model refused or offered a summary"
    ratio = len(out.split()) / max(1, len(src.split()))
    if ratio < 0.45:
        return False, f"far too short ({ratio:.2f}x source) — likely a summary"
    if ratio > 2.6:
        return False, f"far too long ({ratio:.2f}x source)"
    if lang in _NON_LATIN:
        letters = [c for c in out if c.isalpha()]
        if letters and sum(1 for c in letters if ord(c) < 128) / len(letters) > 0.5:
            return False, "output is mostly Latin script, not Greek"
    return True, ""


def cmd_blocked(args) -> int:
    """Fill placeholders from an explicit mapping file.

    Mapping format — a list of objects, one per placeholder:
      [{"file": "<name>.docx", "para": 853, "en_para": 839}, ...]
    or, to supply the English text directly:
      [{"file": "<name>.docx", "para": 853, "en_text": "..."}]

    'para' is the paragraph index in the translated .docx; 'en_para' the index in
    its English source. Both are 0-based, matching langcheck's output. The mapping
    is required rather than derived — see the module docstring.
    """
    map_path = Path(args.map)
    if not map_path.exists():
        sys.exit(f"Mapping file not found: {map_path}\n"
                 "Each entry needs: file, para, and either en_para or en_text.")
    entries = json.loads(map_path.read_text(encoding="utf8"))
    if not isinstance(entries, list):
        sys.exit("Mapping file must contain a JSON list.")

    by_file: dict[str, list[dict]] = {}
    for e in entries:
        by_file.setdefault(e["file"], []).append(e)

    client = None if args.dry_run else make_client()
    filled = failed = 0

    for fname, items in by_file.items():
        path = TRANSLATED / fname
        if not path.exists():
            print(f"  !! {fname}: not found")
            failed += len(items)
            continue
        lang = lang_of(path)
        if not lang:
            print(f"  !! {fname}: cannot determine language")
            failed += len(items)
            continue

        with zipfile.ZipFile(path) as z:
            xml = z.read(DOC).decode("utf8")
        plist = para_spans(xml)
        en_body = None
        print(f"\n== {fname}  [{lang}]  {len(items)} placeholder(s)")

        edits = []
        for item in sorted(items, key=lambda i: -i["para"]):
            idx = item["para"]
            if idx >= len(plist):
                print(f"  !! para {idx} out of range")
                failed += 1
                continue
            if BLOCK_MARKER not in plist[idx][2]:
                print(f"  -- para {idx}: no placeholder here (already filled?)")
                continue

            src = item.get("en_text")
            if src is None:
                if en_body is None:
                    en_path = en_source_for(path)
                    if en_path is None:
                        print(f"  !! no English source for {fname}")
                        failed += 1
                        continue
                    en_body = paras(en_path)
                ep = item["en_para"]
                if ep >= len(en_body):
                    print(f"  !! en_para {ep} out of range")
                    failed += 1
                    continue
                src = en_body[ep]

            print(f"  para {idx} <- {len(src.split())} English words")
            print(f"      EN: {src[:100]}")
            if args.dry_run:
                continue

            try:
                out = call_claude(
                    client,
                    system=BLOCKED_SYSTEM.format(lang=lang),
                    user=src,
                    max_tokens=8000,
                    effort=args.effort,
                )
            except RuntimeError as exc:
                print(f"      !! {exc}")
                failed += 1
                continue

            ok, why = validate_translation(out, src, lang)
            if not ok:
                print(f"      !! rejected — {why}; placeholder left in place")
                failed += 1
                continue

            s, e, _ = plist[idx]
            replacement = set_para_text(xml[s:e], out)
            if replacement is None:
                print("      !! no run to clone; placeholder left in place")
                failed += 1
                continue
            edits.append((s, e, replacement))
            print(f"      -> {out[:90]}")

        if edits and not args.dry_run:
            for s, e, rep in sorted(edits, key=lambda r: -r[0]):
                xml = xml[:s] + rep + xml[e:]
            left = len([1 for _, _, t in para_spans(xml) if BLOCK_MARKER in t])
            write_docx(path, xml, BACKUPS["blocked"], "preclaude")
            filled += len(edits)
            print(f"  WRITTEN — {len(edits)} filled, {left} placeholder(s) remain")

    print(f"\nfilled {filled}, failed {failed}")
    if args.dry_run:
        print("(dry run — no API calls, nothing written)")
    return 0 if not failed else 1


# ------------------------------------------------------------------------ main

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Translation QA on Claude: langcheck / proofread / blocked.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("langcheck", help="free scan for untranslated English")
    p.add_argument("--file", help="one .docx (default: every translation)")
    p.add_argument("--show", type=int, default=6, help="examples per file")
    p.set_defaults(func=cmd_langcheck)

    p = sub.add_parser("proofread", help="whole-book bilingual proofread report")
    p.add_argument("--file")
    p.add_argument("--all", action="store_true")
    p.add_argument("--limit", type=int, help="stop after N books")
    p.add_argument("--force", action="store_true", help="regenerate existing reports")
    p.add_argument("--effort", default="high",
                   choices=["low", "medium", "high", "xhigh", "max"])
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(func=cmd_proofread)

    p = sub.add_parser("blocked", help="fill content-filter placeholders")
    p.add_argument("--map", required=True, help="JSON mapping file (see --help)")
    p.add_argument("--effort", default="high",
                   choices=["low", "medium", "high", "xhigh", "max"])
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(func=cmd_blocked)

    args = ap.parse_args()
    if not TRANSLATED.exists():
        sys.exit(f"No translated/ folder beside this script: {TRANSLATED}")
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
