#!/usr/bin/env python3
"""langcheck_report.py — corpus-wide untranslated-English scan -> Excel.

WHY NOT JUST `claude_translate.py langcheck`
That command's translation_files() globs ONLY translated\\ and explicitly skips
every "* - FORMATTED.docx". So it cannot see:
  * the 151 promoted deliverables sitting in proofread/
  * any FORMATTED deliverable anywhere — i.e. the actual upload artifacts
A first run reported 16 files / 799 words while never opening the files Lisa
would upload. This scans BOTH folders and BOTH kinds, reusing langcheck's own
paras()/looks_english() so the detector is identical, not a reimplementation.

Cross-references every hit against the promotion gate in promote_translations.py,
so the sheet says not just "this has English in it" but "...and it is currently
promoted as proofread", which is the combination that ships a defect.

OUTPUT  Translation_QA_<date>.xlsx
  Summary        corpus totals, worst languages, the promoted-and-dirty count
  Findings       one row per flagged file, with gate status and run length
  Passages       the actual untranslated paragraphs, quoted, with location
  All Editions   every edition x gate status, so clean files are visible too

USAGE
  python langcheck_report.py
  python langcheck_report.py --out "C:\\path\\to\\file.xlsx"
"""

from __future__ import annotations

import argparse
import collections
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

# Reuse the shipped detector rather than cloning its heuristics.
from claude_translate import TRANSLATED, paras, looks_english, lang_of, BLOCK_MARKER
import promote_translations as gate

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

ROOT = Path(r"C:\Users\User\Scripts")
SCAN_DIRS = [TRANSLATED, ROOT / "proofread", ROOT / "2buploaded"]

HDR = PatternFill("solid", fgColor="1F3864")
HDRF = Font(bold=True, color="FFFFFF", size=11)
BAD = PatternFill("solid", fgColor="FFC7CE")
WARN = PatternFill("solid", fgColor="FFEB9C")
OK = PatternFill("solid", fgColor="C6EFCE")
TITLE = Font(bold=True, size=14)
BOLD = Font(bold=True)


def scan_file(path: Path) -> dict | None:
    """Return a finding dict, or None if the file is clean / unreadable."""
    try:
        body = paras(path)
    except Exception as exc:
        return {"error": str(exc)}
    hits = [(i, t) for i, t in enumerate(body)
            if BLOCK_MARKER not in t and looks_english(t)]
    if not hits:
        return None
    # Group near-adjacent hits into runs: a 12-paragraph run is a dropped chunk,
    # twelve scattered singletons are usually names or borrowings.
    runs: list[list[int]] = []
    for i, _ in hits:
        if runs and i - runs[-1][-1] <= 3:
            runs[-1].append(i)
        else:
            runs.append([i])
    # WHERE the English sits decides whether it matters. A run at >92% through the
    # book is the untranslated blurb/also-by back matter — annoying, one paste to
    # fix, invisible to a reader of the story. The same run mid-body is dropped
    # narrative. Verified by hand on Snapshot_French (para 2236/2369 = blurb) vs
    # Net Worth_Dutch (para 1350/3348 = prose).
    first = hits[0][0]
    pos = 100.0 * first / max(1, len(body))
    if pos > 92:
        zone = "BACK MATTER"
    elif pos < 5:
        zone = "FRONT MATTER"
    else:
        zone = "BODY PROSE"
    return {
        "hits": hits,
        "runs": runs,
        "longest_run": max(len(r) for r in runs),
        "words": sum(len(t.split()) for _, t in hits),
        "paras_total": len(body),
        "zone": zone,
        "first_pct": round(pos, 1),
    }


def edition_stem(path: Path) -> str:
    s = path.stem
    return s[:-len(" - FORMATTED")] if s.endswith(" - FORMATTED") else s


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / f"Translation_QA_{date.today()}.xlsx"))
    args = ap.parse_args()

    led = gate.load_ledger()
    gate.seed_ledger(led)

    targets = []
    for d in SCAN_DIRS:
        if not d.exists():
            continue
        for p in sorted(d.glob("*.docx")):
            if p.name.startswith("~$"):
                continue
            if lang_of(p) is None:
                continue          # English masters etc.
            targets.append(p)

    print(f"scanning {len(targets)} file(s) across "
          f"{', '.join(d.name for d in SCAN_DIRS if d.exists())} ...")

    findings, errors, clean = [], [], 0
    verdict_cache: dict[str, dict] = {}
    for n, p in enumerate(targets, 1):
        if n % 40 == 0:
            print(f"   {n}/{len(targets)}")
        stem = edition_stem(p)
        if stem not in verdict_cache:
            verdict_cache[stem] = gate.evaluate(stem, led)
        v = verdict_cache[stem]
        r = scan_file(p)
        if r is None:
            clean += 1
            continue
        if "error" in r:
            errors.append((p, r["error"]))
            continue
        r.update({
            "path": p, "stem": stem, "lang": lang_of(p),
            "folder": p.parent.name,
            "is_deliverable": p.stem.endswith(" - FORMATTED"),
            "gate": "READY" if v["ready"] else "; ".join(v["blockers"]),
            "promoted": p.parent.name in ("proofread", "2buploaded"),
            "model": v["model"],
        })
        findings.append(r)

    findings.sort(key=lambda r: -r["words"])
    total_words = sum(r["words"] for r in findings)
    promoted_dirty = [r for r in findings if r["promoted"]]

    wb = openpyxl.Workbook()

    # ---------------------------------------------------------------- Summary
    ws = wb.active
    ws.title = "Summary"
    ws["A1"] = "Translation QA — untranslated English scan"
    ws["A1"].font = TITLE
    ws["A2"] = f"Generated {date.today()}   ·   detector: claude_translate.looks_english()"
    ws["A3"] = ("Scanned translated\\, proofread\\ and ready\\ — including "
                "'- FORMATTED' deliverables, which `langcheck` skips.")
    ws["A3"].font = Font(italic=True, size=10)

    rows = [
        ("", ""),
        ("CORPUS", ""),
        ("Files scanned", len(targets)),
        ("Clean (no English found)", clean),
        ("Flagged", len(findings)),
        ("Unreadable", len(errors)),
        ("Total untranslated words", total_words),
        ("", ""),
        ("WHERE THE ENGLISH SITS  (this decides severity)", ""),
        ("BODY PROSE — dropped narrative, real defect",
         sum(1 for r in findings if r["zone"] == "BODY PROSE")),
        ("BACK MATTER — untranslated blurb / also-by, cosmetic",
         sum(1 for r in findings if r["zone"] == "BACK MATTER")),
        ("FRONT MATTER — title/copyright page",
         sum(1 for r in findings if r["zone"] == "FRONT MATTER")),
        ("", ""),
        ("RISK", ""),
        ("Flagged files ALREADY PROMOTED as proofread", len(promoted_dirty)),
        ("Flagged files that are upload deliverables", sum(1 for r in findings if r["is_deliverable"])),
        ("Files with a run of 3+ paragraphs (dropped text)", sum(1 for r in findings if r["longest_run"] >= 3)),
        ("Worst single file (words)", findings[0]["words"] if findings else 0),
        ("", ""),
        ("GATE (promote_translations.py)", ""),
        ("Editions READY to upload", sum(1 for v in verdict_cache.values() if v["ready"])),
        ("Editions blocked", sum(1 for v in verdict_cache.values() if not v["ready"])),
    ]
    r0 = 5
    for i, (k, v) in enumerate(rows):
        ws.cell(r0 + i, 1, k)
        ws.cell(r0 + i, 2, v)
        if k and v == "":
            ws.cell(r0 + i, 1).font = BOLD
    for i, (k, _v) in enumerate(rows):
        if k.startswith("BODY PROSE"):
            ws.cell(r0 + i, 2).fill = BAD
        elif k.startswith(("BACK MATTER", "FRONT MATTER")):
            ws.cell(r0 + i, 2).fill = WARN
        elif k.startswith("Flagged files ALREADY PROMOTED"):
            ws.cell(r0 + i, 2).fill = BAD if promoted_dirty else OK

    lang_tally = collections.Counter()
    for r in findings:
        lang_tally[r["lang"]] += r["words"]
    ws.cell(r0 + len(rows) + 1, 1, "UNTRANSLATED WORDS BY LANGUAGE").font = BOLD
    for i, (lg, w) in enumerate(lang_tally.most_common(), start=r0 + len(rows) + 2):
        ws.cell(i, 1, lg)
        ws.cell(i, 2, w)

    ws.column_dimensions["A"].width = 52
    ws.column_dimensions["B"].width = 16

    # --------------------------------------------------------------- Findings
    ws = wb.create_sheet("Findings")
    cols = ["Severity", "File", "Book", "Language", "Folder", "Deliverable?",
            "Eng. words", "Eng. paras", "Longest run", "Total paras",
            "Starts at % of book", "Promoted as proofread?", "Gate status",
            "Proofread model"]
    for c, h in enumerate(cols, 1):
        cell = ws.cell(1, c, h)
        cell.fill, cell.font = HDR, HDRF
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    # Body prose first, then by size: the order Lisa should work in.
    ZORDER = {"BODY PROSE": 0, "FRONT MATTER": 1, "BACK MATTER": 2}
    for i, r in enumerate(sorted(findings,
                                 key=lambda x: (ZORDER[x["zone"]], -x["words"])),
                          start=2):
        lang, book = gate.split_lang(r["stem"])
        vals = [r["zone"], r["path"].name, book or "", r["lang"], r["folder"],
                "yes" if r["is_deliverable"] else "no",
                r["words"], len(r["hits"]), r["longest_run"], r["paras_total"],
                r["first_pct"], "YES" if r["promoted"] else "no",
                r["gate"], r["model"]]
        for c, v in enumerate(vals, 1):
            ws.cell(i, c, v)
        ws.cell(i, 1).fill = BAD if r["zone"] == "BODY PROSE" else WARN
        if r["longest_run"] >= 3:
            ws.cell(i, 9).fill = BAD
        elif r["longest_run"] > 1:
            ws.cell(i, 9).fill = WARN
        if r["promoted"]:
            ws.cell(i, 12).fill = BAD
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(cols))}{max(2, len(findings)+1)}"
    for c, w in enumerate([15, 58, 34, 15, 12, 12, 11, 11, 12, 12, 18, 22, 40, 24], 1):
        ws.column_dimensions[get_column_letter(c)].width = w

    # -------------------------------------------------------------- Passages
    ws = wb.create_sheet("Passages")
    cols = ["Severity", "File", "Language", "Para #", "In a run of", "Words",
            "Untranslated text"]
    for c, h in enumerate(cols, 1):
        cell = ws.cell(1, c, h)
        cell.fill, cell.font = HDR, HDRF
    row = 2
    for r in sorted(findings, key=lambda x: (ZORDER[x["zone"]], -x["words"])):
        runlen = {}
        for run in r["runs"]:
            for idx in run:
                runlen[idx] = len(run)
        for idx, txt in r["hits"]:
            ws.cell(row, 1, r["zone"]).fill = (
                BAD if r["zone"] == "BODY PROSE" else WARN)
            ws.cell(row, 2, r["path"].name)
            ws.cell(row, 3, r["lang"])
            ws.cell(row, 4, idx)
            ws.cell(row, 5, runlen.get(idx, 1))
            ws.cell(row, 6, len(txt.split()))
            # Excel hard-caps a cell at 32,767 chars; these are paragraphs, but clamp.
            ws.cell(row, 7, txt[:1000]).alignment = Alignment(wrap_text=True, vertical="top")
            if runlen.get(idx, 1) >= 3:
                ws.cell(row, 5).fill = BAD
            row += 1
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:G{max(2, row-1)}"
    for c, w in enumerate([15, 58, 14, 9, 13, 8, 120], 1):
        ws.column_dimensions[get_column_letter(c)].width = w

    # ----------------------------------------------------------- All Editions
    ws = wb.create_sheet("All Editions")
    cols = ["Edition", "Book", "Language", "Gate", "Blockers",
            "Proofread model", "Report?", "Corrections applied?",
            "Deliverable?", "Untranslated words"]
    for c, h in enumerate(cols, 1):
        cell = ws.cell(1, c, h)
        cell.fill, cell.font = HDR, HDRF
    dirty = collections.Counter()
    for r in findings:
        dirty[r["stem"]] += r["words"]
    for i, (stem, v) in enumerate(sorted(verdict_cache.items()), start=2):
        vals = [stem, v["book"] or "", v["lang"] or "",
                "READY" if v["ready"] else "BLOCKED",
                "; ".join(v["blockers"]), v["model"],
                "yes" if v["report"] else "no",
                "yes" if v["corrected"] else "no",
                "yes" if v["deliverable"] else "no",
                dirty.get(stem, 0)]
        for c, val in enumerate(vals, 1):
            ws.cell(i, c, val)
        ws.cell(i, 4).fill = OK if v["ready"] else BAD
        if dirty.get(stem, 0):
            ws.cell(i, 10).fill = BAD
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:J{max(2, len(verdict_cache)+1)}"
    for c, w in enumerate([60, 34, 15, 10, 44, 24, 10, 20, 13, 18], 1):
        ws.column_dimensions[get_column_letter(c)].width = w

    if errors:
        ws = wb.create_sheet("Unreadable")
        ws.cell(1, 1, "File").fill = HDR
        ws.cell(1, 1).font = HDRF
        ws.cell(1, 2, "Error").fill = HDR
        ws.cell(1, 2).font = HDRF
        for i, (p, e) in enumerate(errors, start=2):
            ws.cell(i, 1, str(p))
            ws.cell(i, 2, e)
        ws.column_dimensions["A"].width = 90
        ws.column_dimensions["B"].width = 60

    out = Path(args.out)
    wb.save(out)

    print(f"\n{len(findings)} flagged / {len(targets)} scanned  ·  "
          f"{total_words:,} untranslated English words")
    print(f"{len(promoted_dirty)} flagged file(s) are ALREADY promoted as proofread")
    if findings:
        print("\nworst:")
        for r in findings[:8]:
            flag = f"  <== RUN of {r['longest_run']}" if r["longest_run"] >= 3 else ""
            print(f"  {r['words']:>6}w  {r['path'].name[:62]:<64} [{r['folder']}]{flag}")
    print(f"\nwrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
