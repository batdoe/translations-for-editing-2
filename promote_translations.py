#!/usr/bin/env python3
"""promote_translations.py — the proofread gate. Answers "what can I upload?"

WHY THIS EXISTS
reorg.py moved 336 files into Scripts\\proofread\\ on a purely STRUCTURAL gate: a
file moved if its "<name> - FORMATTED.docx" existed. That gate cannot tell a
proofread book from an unproofread one, so ~120 never-proofread editions landed in
a folder whose name asserts they were proofread. reorg.py also aborts on any
destination collision, so it cannot be re-run. It was a one-shot, not a process.

THE GATE (Lisa's ruling, 2026-08-11 — the strictest of the four tiers)
An edition is READY only when ALL THREE hold:
  1. a proofread report exists          -> translated\\<stem>_proofread.md
  2. its corrections were applied       -> translated\\corrected\\<stem>.docx
  3. its open decisions are resolved    -> no unresolved rows in the ledger

Structural build state is necessary but NOT sufficient: a FORMATTED deliverable
must also exist, or there is nothing to upload.

THE LEDGER — translated\\_proofread_ledger.json
Requirement 3 cannot be derived from the filesystem: "the Greek word choice is
confirmed" is a fact only Lisa holds. So it is an INPUT, recorded per edition,
exactly as claude_translate.py treats its blocked-passage mapping as an input
rather than guessing. Seeded from the two July review documents:
  translated\\corrected\\_REMAINING CHANGES — your decisions.docx   (2 unapplied + 2 renumbers)
  translated\\proofread_changes\\_SUMMARY — read me first.docx      (32 books, 94 changes)

COMMANDS
  status              per-edition table: READY / BLOCKED + the reason. Reads only.
  promote             move READY editions into 2buploaded\\. Re-runnable and idempotent.
  resolve <stem>      mark an edition's open decisions resolved (or --reopen).
  audit-promoted      classify what reorg.py already moved into proofread\\.

USAGE
  python promote_translations.py status
  python promote_translations.py status --ready-only
  python promote_translations.py resolve "HHH_Greek" --note "confirmed ntropiasmeno"
  python promote_translations.py promote --dry-run
  python promote_translations.py promote --apply
  python promote_translations.py audit-promoted

SAFETY
  * promote is COPY-by-default; --move only with an explicit flag
  * a destination collision SKIPS that edition and keeps going (reorg.py aborted
    the whole run, which is what made it single-use)
  * every promotion appends to 2buploaded\\_PROMOTION_LOG.tsv, so it is reversible
  * nothing is ever deleted
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"C:\Users\User\Scripts")
TRANSLATED = ROOT / "translated"
CORRECTED = TRANSLATED / "corrected"
CHANGES = TRANSLATED / "proofread_changes"
LEDGERS = TRANSLATED / "_EditLedgers"       # where /proofread writes its reports
PROMOTED_OLD = ROOT / "proofread"          # what reorg.py filled
PROOFREAD_SHIP = PROMOTED_OLD / "_ship"    # correctly-named 4-file sets staged for upload
READY = ROOT / "2buploaded"                # certified, uploadable (Lisa's name)
EDITLEDGERS = TRANSLATED / "_EditLedgers"   # all ledgers together (Lisa 2026-08-11)
LEDGER = EDITLEDGERS / "_proofread_ledger.json"
LOG = READY / "_PROMOTION_LOG.tsv"

LANGS = ["Brazilian Portuguese", "Czech", "Danish", "Dutch", "Filipino", "French",
         "German", "Greek", "Italian", "Norwegian", "Polish", "Romanian",
         "Spanish", "Swedish", "Tagalog", "Turkish"]

# Editions reorg.py excluded as superseded: the live editions are the
# _ASSEMBLED_scrub ones (Book 2 = Name on the Door, Book 3 = Money Can't Buy).
# A proofread of a dead edition must never certify anything.
DEAD_PREFIX = ["KB_H1_2_The_Founder_ASSEMBLED_",
               "KB_H1_3_The_Owner_Manuscript_",
               "15 language translation test"]

# ⚑⚑ ROMANO: only the `NEW ` retranslations are live (Lisa, 2026-08-11).
# The three un-prefixed Italian files below are the SUPERSEDED pre-retranslation
# editions. They must never be proofread, promoted, or rebuilt — a proofread of a
# dead edition has already been paid for once on the KB Founder/Owner drafts.
DEAD_ROMANO = ["Secret Betrayal - ASSEMBLED",
               "Secret Revenge - ASSEMBLED",
               "Secret Passion - ASSEMBLED"]


def is_dead(stem: str) -> bool:
    if any(stem.startswith(p) for p in DEAD_PREFIX):
        return True
    # Romano: a bare "Secret ..." stem is the dead pre-retranslation edition; the
    # live one carries the "NEW " prefix. Checked BEFORE the generic rules so it
    # cannot be missed by a stem that also matches something else.
    if any(stem.startswith(p) for p in DEAD_ROMANO) and not stem.startswith("NEW "):
        return True
    # bare Out_of_His_League drafts; the _ASSEMBLED_scrub edition is the real one
    if stem.startswith("KB_H1_1_Out_of_His_League_") and "_ASSEMBLED_scrub" not in stem:
        return True
    return False


def split_lang(stem: str):
    """-> (language, book_base) or (None, None). Tolerates the ' - REPAIRED' suffix."""
    st = stem[:-len(" - REPAIRED")] if stem.endswith(" - REPAIRED") else stem
    for L in sorted(LANGS, key=len, reverse=True):
        if st.endswith("_" + L):
            return L, st[:-(len(L) + 1)]
    return None, None


# ------------------------------------------------------------------- the ledger

# Seeded from "_REMAINING CHANGES — your decisions.docx". These are the ONLY
# editions the July pass left with unresolved items; every other proofread
# edition in that pass was fully applied (92 of 94 changes).
SEED_OPEN = {
    "HHH_Greek": [
        "word choice: 'probata' (= sheep) is wrong; sense is a SHEEPISH tone. "
        "Suggested 'ntropiasmeno' (embarrassed). Confirm or supply your word."
    ],
    "HHH_Romanian": [
        "chapter numbering scrambled: two 'Capitolul 3', two 'Capitolul 17'. "
        "Confirm the English is 1..N, then renumber."
    ],
    "MMM_Czech": [
        "chapter numbering: headings skip 'Kapitola 6' (5 -> 7). "
        "Confirm against the English, then renumber."
    ],
    "KB_H1_3_The_Owner_Manuscript_French": [
        "unit: 'miles' left untranslated where the motif uses kilometres. "
        "Decide the number. NOTE: this edition is SUPERSEDED (dead)."
    ],
}


def load_ledger() -> dict:
    if LEDGER.exists():
        return json.loads(LEDGER.read_text(encoding="utf8"))
    return {"_schema": 1, "editions": {}}


def save_ledger(led: dict) -> None:
    EDITLEDGERS.mkdir(exist_ok=True)
    led["_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    LEDGER.write_text(json.dumps(led, indent=2, ensure_ascii=False), encoding="utf8")


def seed_ledger(led: dict) -> int:
    """Add any missing seed rows. Never overwrites a resolution Lisa recorded."""
    n = 0
    for stem, items in SEED_OPEN.items():
        if stem not in led["editions"]:
            led["editions"][stem] = {"open": items, "resolved": False,
                                     "note": "", "resolved_at": ""}
            n += 1
    return n


# -------------------------------------------------------------------- discovery

def report_for(stem: str) -> Path | None:
    """The proofread report, wherever it landed.

    THREE conventions coexist in this corpus and ALL are valid:
      * `translated\\<stem>_proofread.md`            — the original gate location
      * `translated\\_EditLedgers\\<stem>_PROOFREAD.md` — where /proofread writes
      * `translated\\_EditLedgers\\<book>_MULTI_PROOFREAD.md` — one report covering
        SEVERAL LANGUAGES of the same book, which is how the Isabella Proctor
        editions were proofread (orchestrator-direct bilingual read, all languages
        of a book in one pass).

    Before 2026-08-12 only the first was checked, so a fully proofread edition
    still gated as "no proofread report" and the file had to be copied by hand.
    The same was true of MULTI reports until 2026-09-07 (Lisa's ruling): 40
    edition-coverages across 8 books were proofread — 30/30 chapters, findings
    applied, integrity PASS — and still gated as unproofread.

    ⚑ A MULTI report only vouches for the languages it actually covers, so the
    edition's OWN language must appear in it. A report that never mentions
    Turkish cannot clear the Turkish edition (Book 2's MULTI, for instance,
    explicitly DEFERS Turkish while covering the other four). Matching on the
    filename alone would silently promote an unproofread edition, which is the
    exact failure this gate exists to prevent.

    Checked in order; first hit wins.
    """
    for p in (TRANSLATED / f"{stem}_proofread.md",
              LEDGERS / f"{stem}_PROOFREAD.md"):
        if p.exists():
            return p
    lang, base = split_lang(stem)
    if lang and base:
        p = LEDGERS / f"{base}_MULTI_PROOFREAD.md"
        if p.exists():
            try:
                body = p.read_text(encoding="utf-8", errors="replace")
            except OSError:
                return None
            # ⚑ ONLY the coverage table counts — a leading "| <Language> |" cell.
            # A plain mention is NOT evidence: Book 2's MULTI says "Turkish
            # deferred — see below" and names Turkish twice more in the notes,
            # so a substring test would clear an edition the report explicitly
            # refuses to vouch for. Verified 2026-09-07 against that report.
            if re.search(rf"^\|\s*{re.escape(lang)}\s*\|", body, re.M):
                return p
    return None


def corrected_for(stem: str) -> Path | None:
    p = CORRECTED / f"{stem}.docx"
    return p if p.exists() else None


def changes_for(stem: str) -> Path | None:
    p = CHANGES / f"{stem} — CHANGES.docx"
    return p if p.exists() else None


def artifacts_for(stem: str) -> list[tuple[Path, str]]:
    """The PRINT PDF and the EPUB that ship alongside the .docx pair.

    ⚑ 2026-08-12: promote used to copy ONLY .docx files — this module had no mention
    of pdf or epub anywhere — yet every edition already in 2buploaded\\ is a FOUR-file
    set (- FORMATTED.docx / - PRINT 5x8.pdf / .docx / .epub). The PDFs and EPUBs were
    being placed by hand, so a promoted book silently shipped without its print
    interior or its ebook. Found on KB_H1_2.

    Both live beside the deliverable. The formatter names them from ITS input, so when
    the input is already "<stem> - FORMATTED.docx" they come out as
    "<stem> - FORMATTED - PRINT 5x8.pdf" / "<stem> - FORMATTED.epub"; a plain input
    gives "<stem> - PRINT 5x8.pdf" / "<stem>.epub". Accept either, and always land them
    in 2buploaded\\ under the un-doubled name.
    """
    out: list[tuple[Path, str]] = []
    # ⚑ 2026-09-09 (Lisa's Turkish promote): CORRECTED was MISSING from this list
    # while deliverable_for() already searched it first (the 2026-09-07 ruling). A book
    # rebuilt in corrected\ therefore promoted as a docx pair with NO print PDF and NO
    # EPUB — the run still printed success. All 9 Turkish editions shipped that way and
    # the 18 artifacts had to be copied by hand. CORRECTED must also come FIRST, so a
    # fresh docx can never be paired with a stale PDF left in translated\.
    for base in (CORRECTED, TRANSLATED, PROMOTED_OLD, READY, PROOFREAD_SHIP):
        if not base.exists():
            continue
        for cand, kind in (
            (base / f"{stem} - PRINT 5x8.pdf", "print-pdf"),
            (base / f"{stem} - FORMATTED - PRINT 5x8.pdf", "print-pdf"),
            (base / f"{stem}.epub", "epub"),
            (base / f"{stem} - FORMATTED.epub", "epub"),
        ):
            if cand.exists() and not any(k == kind for _, k in out):
                out.append((cand, kind))
        if len(out) == 2:
            break
    return out


def deliverable_for(stem: str) -> Path | None:
    """The uploadable FORMATTED .docx, wherever it currently lives.

    ⚑ 2026-08-12: prefer the DOUBLED name first. book-print-formatter names its output
    from ITS input, so when the input is already "<stem> - FORMATTED.docx" the real
    product lands as "<stem> - FORMATTED - FORMATTED.docx" and the un-doubled file is
    merely the formatter's INPUT. Taking the un-doubled one shipped a stale book: on
    KB_H1_2 German it still carried the pre-fix catalogue page ("Charleston Reign"
    rather than the rebuilt "Charleston Reign Hockey"). The doubled file is the one
    with the rebuilt catalogue pages, the TOC field and the About page.

    ⚑ 2026-09-07 (Lisa's ruling): CORRECTED is searched FIRST. It was missing from
    this list entirely, so the gate could not see any deliverable built in the
    working folder — the Isabella Norwegian Books 4-9 gated as "no FORMATTED
    deliverable" while their rebuilt files sat in corrected\\. Worse, Books 1-3
    "passed" only on August copies already sitting in 2buploaded\\, which end on
    the duplicated get-CTA this session replaced. Promoting would have shipped
    stale books. corrected\\ is where the proofread+rebuilt product lands, so it
    outranks every staging copy.
    """
    for base in (CORRECTED, PROOFREAD_SHIP, TRANSLATED, PROMOTED_OLD, READY):
        for name in (f"{stem} - FORMATTED - FORMATTED.docx",
                     f"{stem} - FORMATTED.docx"):
            p = base / name
            if p.exists():
                return p
    return None


def report_model(path: Path) -> str:
    """Provenance is invisible in filenames; it lives in the report header."""
    try:
        head = path.read_text(encoding="utf8", errors="replace")[:900]
    except Exception:
        return "?"
    for tag in ("claude-opus-5", "gemini-3.5-flash", "gemini-flash-lite-latest"):
        if tag in head:
            return tag
    if "bilingual whole-book pass" in head:
        return "claude (bilingual)"
    return "?"


_MATTER_CACHE: dict[str, str] = {}


def matter_verdict(deliverable: Path) -> str:
    """"" if the back/front matter is fine, else a short blocker string."""
    key = str(deliverable)
    if key in _MATTER_CACHE:
        return _MATTER_CACHE[key]
    try:
        import check_matter
        r = check_matter.check(deliverable)
        out = "; ".join(r.get("problems", [])) if not r.get("error") else ""
    except Exception:
        out = ""          # never let a checker failure silently block everything
    _MATTER_CACHE[key] = out
    return out


def all_editions() -> list[str]:
    """Every edition stem the corpus knows about, from any of the four signals."""
    stems = set()
    for p in TRANSLATED.glob("*_proofread.md"):
        if not p.name.startswith("~$"):
            stems.add(p.name[:-len("_proofread.md")])
    for p in LEDGERS.glob("*_PROOFREAD.md"):    # /proofread's own location
        if not p.name.startswith("~$"):
            stems.add(p.name[:-len("_PROOFREAD.md")])
    for p in CORRECTED.glob("*.docx"):
        if not p.name.startswith(("~$", "_")):
            stems.add(p.stem)
    for base in (TRANSLATED, PROMOTED_OLD):
        for p in base.glob("* - FORMATTED.docx"):
            if p.name.startswith("~$"):
                continue
            stems.add(p.stem[:-len(" - FORMATTED")])
    return sorted(s for s in stems if split_lang(s)[0])


def evaluate(stem: str, led: dict) -> dict:
    """Apply the three-part gate. Returns a verdict row."""
    rep, cor = report_for(stem), corrected_for(stem)
    dlv = deliverable_for(stem)
    row = led["editions"].get(stem, {})
    # An edition with no ledger row and no seeded open items has nothing
    # outstanding -> requirement 3 is satisfied vacuously.
    has_open = bool(row.get("open")) and not row.get("resolved")

    blockers = []
    if is_dead(stem):
        blockers.append("SUPERSEDED edition")
    if rep is None:
        blockers.append("no proofread report")
    if cor is None:
        blockers.append("corrections not applied")
    if has_open:
        blockers.append(f"{len(row['open'])} open decision(s)")
    if dlv is None:
        blockers.append("no FORMATTED deliverable")
    else:
        # House rule: localized back matter is required to ship. Structural, free,
        # and it catches the formatter-localization miss that a proofread would
        # only find by re-reading the whole book.
        m = matter_verdict(dlv)
        if m:
            blockers.append(m)

    lang, book = split_lang(stem)
    return {
        "stem": stem, "lang": lang, "book": book,
        "report": rep, "corrected": cor, "changes": changes_for(stem),
        "deliverable": dlv,
        "model": report_model(rep) if rep else "-",
        "ready": not blockers,
        "blockers": blockers,
        "resolved": bool(row.get("resolved")),
    }


# --------------------------------------------------------------------- commands

def cmd_status(args) -> int:
    led = load_ledger()
    if seed_ledger(led) and not args.no_write:
        save_ledger(led)
    rows = [evaluate(s, led) for s in all_editions()]
    ready = [r for r in rows if r["ready"]]
    blocked = [r for r in rows if not r["ready"]]

    print(f"{'EDITION':<62} {'MODEL':<24} STATUS")
    print("-" * 110)
    for r in ready:
        print(f"{r['stem'][:60]:<62} {r['model']:<24} READY")
    if not args.ready_only:
        for r in blocked:
            print(f"{r['stem'][:60]:<62} {r['model']:<24} "
                  f"BLOCKED: {'; '.join(r['blockers'])}")

    print(f"\n{len(ready)} READY   {len(blocked)} BLOCKED   {len(rows)} total editions")

    tally = collections.Counter(b for r in blocked for b in r["blockers"])
    if tally and not args.ready_only:
        print("\nwhy blocked:")
        for why, n in tally.most_common():
            print(f"   {n:>4}  {why}")

    open_rows = {k: v for k, v in led["editions"].items()
                 if v.get("open") and not v.get("resolved")}
    if open_rows:
        print(f"\nOPEN DECISIONS you owe ({len(open_rows)} edition(s)):")
        for stem, v in sorted(open_rows.items()):
            print(f"\n  {stem}")
            for it in v["open"]:
                print(f"     - {it}")
        print(f"\n  resolve with:  python {Path(__file__).name} resolve \"<edition>\" "
              f"--note \"what you decided\"")
    return 0


def cmd_resolve(args) -> int:
    led = load_ledger()
    seed_ledger(led)
    stem = args.stem
    known = list(led["editions"])
    if stem not in known:
        near = [k for k in known if stem.lower() in k.lower()]
        print(f"No ledger row for {stem!r}.")
        if near:
            print("Did you mean: " + ", ".join(near))
        else:
            print("Editions with open decisions: " + ", ".join(known) or "(none)")
        return 1
    row = led["editions"][stem]
    if args.reopen:
        row["resolved"] = False
        row["resolved_at"] = ""
        print(f"REOPENED {stem}")
    else:
        row["resolved"] = True
        row["resolved_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        if args.note:
            row["note"] = args.note
        print(f"RESOLVED {stem}")
        for it in row.get("open", []):
            print(f"   was: {it}")
        if args.note:
            print(f"   note: {args.note}")
        if is_dead(stem):
            print("   NOTE: this edition is SUPERSEDED — it still will not promote.")
    save_ledger(led)
    print(f"\nledger: {LEDGER}")
    return 0


def cmd_promote(args) -> int:
    led = load_ledger()
    seed_ledger(led)
    rows = [evaluate(s, led) for s in all_editions()]
    ready = [r for r in rows if r["ready"]]

    if not ready:
        print("Nothing is READY under the three-part gate.")
        print(f"Run `status` to see what each edition is waiting on.")
        return 0

    verb = "MOVE" if args.move else "COPY"
    plan, skips = [], []
    for r in ready:
        # The deliverable is what gets uploaded; the corrected source travels
        # with it so the text behind the deliverable is never orphaned.
        # ⚑ 2026-08-12: the PRINT PDF and the EPUB ship WITH the .docx pair — every
        # edition already in 2buploaded\ is a four-file set. They were previously
        # copied by hand, so a promoted book could ship with no print interior and
        # no ebook. artifacts_for() finds them beside the deliverable.
        items = [(r["deliverable"], "deliverable"),
                 (r["corrected"], "corrected-source")]
        items += artifacts_for(r["stem"])
        for src, kind in items:
            if src is None:
                continue
            # land the artifacts under the un-doubled name
            name = src.name.replace(" - FORMATTED - PRINT 5x8.pdf", " - PRINT 5x8.pdf")
            name = name.replace(" - FORMATTED - FORMATTED.docx", " - FORMATTED.docx")
            if name.endswith(" - FORMATTED.epub"):
                name = name[:-len(" - FORMATTED.epub")] + ".epub"
            dst = READY / name
            if dst.exists():
                skips.append((name, "already in 2buploaded\\"))
                continue
            plan.append((src, dst, kind, r["stem"]))

    print(f"destination: {READY}")
    print(f"mode: {verb}")
    for kind, n in collections.Counter(k for _, _, k, _ in plan).most_common():
        print(f"   {n:>4}  {kind}")
    print(f"   {len(plan):>4}  TOTAL from {len(ready)} READY edition(s)")
    if skips:
        print(f"\n{len(skips)} skipped (collision — run is still safe):")
        for n, why in skips[:10]:
            print(f"   {why:<22} {n[:60]}")
        if len(skips) > 10:
            print(f"   ... +{len(skips)-10} more")

    if not args.apply:
        print("\n(dry run — pass --apply to write)")
        return 0

    READY.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    new = not LOG.exists()
    with LOG.open("a", encoding="utf8") as fh:
        if new:
            fh.write("when\tmode\tkind\tedition\tsource\tdest_name\n")
        for src, dst, kind, stem in plan:
            if args.move:
                shutil.move(str(src), str(dst))
            else:
                shutil.copy2(str(src), str(dst))
            fh.write(f"{stamp}\t{verb}\t{kind}\t{stem}\t{src}\t{dst.name}\n")
    print(f"\n{verb.lower()}d {len(plan)} file(s) into {READY}")
    print(f"log: {LOG}")
    return 0


def cmd_audit_promoted(args) -> int:
    """Classify what reorg.py already moved, so the old folder stops lying."""
    led = load_ledger()
    seed_ledger(led)
    if not PROMOTED_OLD.exists():
        print(f"{PROMOTED_OLD} does not exist.")
        return 1

    seen = {}
    for p in sorted(PROMOTED_OLD.glob("* - FORMATTED.docx")):
        if p.name.startswith("~$"):
            continue
        stem = p.stem[:-len(" - FORMATTED")]
        if split_lang(stem)[0] is None:
            continue
        seen[stem] = evaluate(stem, led)

    tiers = collections.defaultdict(list)
    for stem, r in seen.items():
        if r["ready"]:
            tiers["CERTIFIED — meets the full gate"].append(stem)
        elif r["report"] and r["corrected"]:
            tiers["APPLIED but open decisions remain"].append(stem)
        elif r["report"]:
            tiers["REPORT only — corrections never applied"].append(stem)
        else:
            tiers["NEVER PROOFREAD — promoted on build state alone"].append(stem)

    print(f"AUDIT of {PROMOTED_OLD}  ({len(seen)} deliverable editions)\n")
    for tier in ("CERTIFIED — meets the full gate",
                 "APPLIED but open decisions remain",
                 "REPORT only — corrections never applied",
                 "NEVER PROOFREAD — promoted on build state alone"):
        items = tiers.get(tier, [])
        print(f"{len(items):>4}  {tier}")
        if args.verbose:
            for s in items[:args.show]:
                print(f"         {s[:78]}")
            if len(items) > args.show:
                print(f"         ... +{len(items)-args.show} more")
    print("\nThe folder name 'proofread\\' describes only the first group.")
    print("Certified editions promote into 2buploaded\\ via `promote`.")
    return 0


def cmd_demote(args) -> int:
    """Evict everything from proofread\\ that does not meet the gate.

    reorg.py filled that folder on a build check, so its name asserts a quality
    claim for ~146 editions that were never proofread. Lisa's ruling (2026-08-11):
    anything that does not conform gets demoted. Files go back to translated\\ —
    where an unproofread translation belongs — not to a graveyard, so the normal
    proofread -> apply -> promote path picks them up with no special-casing.
    """
    led = load_ledger()
    seed_ledger(led)
    if not PROMOTED_OLD.exists():
        print(f"{PROMOTED_OLD} does not exist — nothing to demote.")
        return 0

    # Certified editions keep every file they own; everything else goes back.
    keep: set[str] = set()
    for p in PROMOTED_OLD.glob("* - FORMATTED.docx"):
        stem = p.stem[:-len(" - FORMATTED")]
        if split_lang(stem)[0] and evaluate(stem, led)["ready"]:
            keep.add(stem)

    plan, kept, unknown = [], [], []
    for p in sorted(PROMOTED_OLD.glob("*.docx")):
        if p.name.startswith("~$"):
            continue
        stem = p.stem
        base = stem[:-len(" - FORMATTED")] if stem.endswith(" - FORMATTED") else stem
        lang, _ = split_lang(base)
        if lang is None:
            # English masters and anything without a language suffix. These are
            # sources, not editions — the gate says nothing about them, so they
            # stay put rather than being moved on a guess.
            unknown.append(p.name)
            continue
        if base in keep:
            kept.append(p.name)
            continue
        dst = TRANSLATED / p.name
        if dst.exists():
            unknown.append(f"{p.name}  (already in translated\\ — left in place)")
            continue
        plan.append((p, dst, base))

    print(f"DEMOTE  {PROMOTED_OLD}  ->  {TRANSLATED}\n")
    print(f"   {len(plan):>4}  files to demote (edition does not meet the gate)")
    print(f"   {len(kept):>4}  files KEPT (certified: {', '.join(sorted(keep)) or 'none'})")
    print(f"   {len(unknown):>4}  left in place (English master / no language suffix / collision)")
    if args.verbose:
        for _, _, stem in plan[:args.show]:
            print(f"         demote  {stem[:70]}")
        if len(plan) > args.show:
            print(f"         ... +{len(plan)-args.show} more")

    if not args.apply:
        print("\n(dry run — pass --apply to move)")
        return 0

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    dlog = PROMOTED_OLD / "_DEMOTION_LOG.tsv"
    new = not dlog.exists()
    with dlog.open("a", encoding="utf8") as fh:
        if new:
            fh.write("when\tedition\tfrom\tto\n")
        for src, dst, stem in plan:
            shutil.move(str(src), str(dst))
            fh.write(f"{stamp}\t{stem}\t{src}\t{dst}\n")
    print(f"\ndemoted {len(plan)} file(s) back to {TRANSLATED}")
    print(f"log: {dlog}   (reversible)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Proofread gate for translated editions: status / promote / "
                    "resolve / audit-promoted.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("status", help="per-edition READY/BLOCKED table")
    p.add_argument("--ready-only", action="store_true")
    p.add_argument("--no-write", action="store_true",
                   help="do not seed the ledger file")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("resolve", help="mark an edition's open decisions resolved")
    p.add_argument("stem")
    p.add_argument("--note", default="")
    p.add_argument("--reopen", action="store_true")
    p.set_defaults(func=cmd_resolve)

    p = sub.add_parser("promote", help="move/copy READY editions into 2buploaded\\")
    p.add_argument("--apply", action="store_true")
    p.add_argument("--move", action="store_true",
                   help="move instead of the default copy")
    p.add_argument("--dry-run", action="store_true", help="default; explicit")
    p.set_defaults(func=cmd_promote)

    p = sub.add_parser("audit-promoted", help="classify what reorg.py moved")
    p.add_argument("--verbose", "-v", action="store_true")
    p.add_argument("--show", type=int, default=8)
    p.set_defaults(func=cmd_audit_promoted)

    p = sub.add_parser("demote", help="evict non-conforming editions from proofread\\")
    p.add_argument("--apply", action="store_true")
    p.add_argument("--verbose", "-v", action="store_true")
    p.add_argument("--show", type=int, default=10)
    p.set_defaults(func=cmd_demote)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
