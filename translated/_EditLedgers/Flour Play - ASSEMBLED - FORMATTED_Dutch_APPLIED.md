# APPLIED — Flour Play - ASSEMBLED - FORMATTED_Dutch (2026-10-27)

Output: `translated\corrected\Flour Play - ASSEMBLED - FORMATTED_Dutch.docx`. Backup of the starting copy: `translated\corrected\_bak\Flour Play - ASSEMBLED - FORMATTED_Dutch.pre-proofread-20261027.docx`.
Method: run-level edits only (`<w:t>` text; a span crossing runs was edited only when every run had identical formatting, otherwise refused and re-matched per run). No paragraph added or removed (1371 → 1371). Italic runs: 41 → 42 (+1 = the restored capsule card [1228], italic as the English); every original italic run kept in place, text changed only where the italic text itself was translated/unified: [305] ×2, [316], [659] ×2, [662], [676], [678], [1259], [1274], [1275], [1312] ×2, [1319] ×2 (and [542] apostrophe only).

## Applied
- 676 targeted fixes — the full list (para, was → now, why) is the findings table in `Flour Play - ASSEMBLED - FORMATTED_Dutch_PROOFREAD.md`.
- [1228] capsule card restored: three runs `<bt>` `The Binder's Bequest` `</bt>` → one italic run `Wat zullen we ze sturen, over honderd jaar?` (EN italic).
- [1321]–[1370] Binder's Bequest excerpt: the 50 English paragraphs replaced by the published Dutch edition's text (`2buploaded\1. Binder's Bequest_Dutch.docx` [53]–[102], 1:1 aligned, verified first/last paragraph); this edition's paragraph properties kept, runs carried over (plain).
- [177] English duplicate emptied (its Dutch twin [178] is complete).
- Book-wide: 605 dialogue paragraphs converted to ‘…’ (150 attributions rebuilt, 4 nested “…”, 125 apostrophes).
- `<bt>`: 4 non-title spans removed, 4 real-title anchors added, 5 kept (9 → 9).

## Refused by verification (then re-matched and applied)
- [778] NOTFOUND: `„Je brengt de krans vast alsnog,”` — the quote was a fragment of a longer clause (`…alsnog, neem ik aan,`); re-matched on `„Je brengt de krans vast alsnog,` and applied.
- [1312] CROSSFORMAT: `Looking for another mystery? Start the Spine and Spells series with <bt>The Binder's Beque` — the sell line is split into italic runs around the plain `<bt>` runs; re-matched per italic run and applied (italics and anchor kept).
- [1319] CROSSFORMAT: `Looking for another mystery? Start the Spine and Spells series with <bt>The Binder's Beque` — the sell line is split into italic runs around the plain `<bt>` runs; re-matched per italic run and applied (italics and anchor kept).

Final refusals: 0.

## Needs a decision (see PROOFREAD_DECISIONS.md, FP-NL-1…8)
- FP-NL-1 "two degrees under code" kept (Fahrenheit clue figure ×3). FP-NL-2 100 lb → 45 kilo. FP-NL-3 Snowball vs Book 1's Sneeuwbal. FP-NL-4 What's Next label ('Wat nu?' here vs Inn Trouble NL 'Wat komt er hierna?'). FP-NL-5 missing final continue-reading line. FP-NL-6 Pete/Doc ↔ Jessica = je. FP-NL-7 the Grange = 'dorpszaal' here vs 'de Grange' in Inn Trouble NL's excerpt. FP-NL-8 sour base / cold-room term choices (informational).

## Quoted but not found
- None (no prior report).

## Checks on the corrected copy
- Untranslated English helper: `[]`.
- `bt_anchors.py check`: 9 spans, 0 unpaired; titles Flour Play, Frost and Found, Inn Trouble, The Binder's Bequest.
- `check_matter.py`: MISSING continue-reading sell line (#18) — FP-NL-5, formatter/Lisa; ORDER: get-CTA after the excerpt heading — false positive, the excerpt detector fires on the TOC entry [16] `Fragment uit …` (the formatter rebuilds the TOC).
- `preflight.py --verify`: paragraphs 2095 → 2095 ok; scene breaks 58 → 58 ok; bt anchors 9 → 9 ok; italic runs 41 → 42 (+1 restored card, declared above); italic sequence differs only where italic text was translated (listed above); bt titles 'lost' = the 3 non-title shop/van anchors removed under ruling 5 (+ the fake Ch26 anchor swapped for the 4 real series anchors) → FAIL by design of the tool, explained.
