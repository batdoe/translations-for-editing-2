# APPLIED — Flour Play - ASSEMBLED - FORMATTED_Filipino — 2026-10-27

File: `translated/corrected/Flour Play - ASSEMBLED - FORMATTED_Filipino.docx`.
Base: the pre-flight copy already in `corrected/` (the `translated/` input + 8 asterisk spans converted to italics). Backed up first to `corrected/_bak/Flour Play - ASSEMBLED - FORMATTED_Filipino.pre-proofread-20261027.docx`. The original in `translated/` was not touched.

Method: run-level edits only. Each fix matched its target string exactly once in the live paragraph before writing (no match or multiple matches = refusal); a multi-run match was allowed only when all spanned runs had identical formatting; italic text was edited inside its own run. `set_para_text` was not used; no paragraph was collapsed. Sweeps edited `<w:t>` nodes in place and refused any paragraph where a term crossed a run boundary (0 such). Stray `<bt>` markers sat in their own runs and were blanked run by run.

- **Applied: 1,028** targeted edits (978 fixes + 50 excerpt paragraphs from the published Filipino *Binder's Bequest*, `2buploaded/1. Binder's Bequest_Filipino.docx` [53]–[102]). Para / was / now / why for each is in `Flour Play - ASSEMBLED - FORMATTED_Filipino_PROOFREAD.md`.
- **Sweeps: 99** replacements in 93 paragraph edits (log below).
- **Dialogue punctuation:** 604 paragraphs straight → curly “ ” (2,180 marks, 0 unbalanced); 11 nested pairs → ‘ ’ ([426][911][1014][1073][1074][1127]).
- **Refused by verification: 0.** Two entries were first refused (my quoted context had "ang" for "ng" at [1216]; a cross-format match at [1263] where the card text is italic); both were re-matched to the live text (the italic card edited inside its own run) and applied.
- **Report quotes not found:** 0.
- **Paragraphs:** 1376 → 1376 (docx-level 2427 → 2427). Nothing added or deleted; the 4 stray Ch8 headings and the Ch22 split are left for Lisa / the formatter.
- **Italic runs:** 44 → 44 against the pre-flight copy, same order. Content changed only where italic text was translated: founder's note [302], "sub-clause" [429], the ledger line [473], the flyer [662], Renée's echo [681], the capsule card [1263], Joyce's letter [1279], the sell lines [1316][1323] and the closing line [1375]. Against the original `translated/` input preflight shows 36 → 44: the +8 are the pre-flight asterisk conversions, not mine.
- **`<bt>`:** 17 → 10. 12 stray spans removed (Sugarplum Patisserie, Yarn Tales, Frost Falls ×5, Holly Jolly Bakery, financier, Wendt's Bakehouse, Bridgton ×2, and an inserted "The Binder's Bequest:" in Ch26 [1232]); 5 title anchors added ([0] title page `<bt>Flour Play</bt>` as on Inn Trouble Filipino; series list [9][10][11]; closing line [1375]). Only Frost and Found / Inn Trouble / Flour Play / The Binder's Bequest remain.

## Needs a decision (logged in PROOFREAD_DECISIONS.md, section "Flour Play - ASSEMBLED - FORMATTED_Filipino (2026-10-26)")
FIL3-D1 four stray `Kabanata 3` lines in Ch8 · FIL3-D2 Kelly/Hal informal · FIL3-D3 "two degrees under code" kept as a °F figure ×3 · FIL3-D4 published Binder's Bequest text copied with its own slips ("Si Ginoo Hartwell").

## Helper checks on the corrected file
1. Untranslated English (looks_english): `[]`. A word-level sweep (English function words + c/f/v/z/th/sh tokens) cleared the remaining code-switches; what is left is names, pastry/brand words (financier, couverture, croissant, brioche, Hobart), loans (batch, counter, van, oven), and the published excerpt's own wording.
2. `bt_anchors.py check`: 10 spans, 0 unpaired; span texts only Flour Play / Frost and Found / Inn Trouble / The Binder's Bequest.
3. `check_matter.py --file`: 1 PASS, 0 FAIL.
4. `preflight.py --verify`: paragraphs 2427 → 2427 ok; scene breaks 58 → 58 ok. It prints FAIL only on declared deltas: italic 36 → 44 (pre-flight asterisk conversions; 44 → 44 against the pre-flight copy), italic sequence differs where italic text was translated (listed above), bt 17 → 10 (12 strays removed, 5 title anchors added).


## Sweep log (paragraph · pattern → replacement · count)

- [24] `lupon` → `bilog` ×1
- [32] `lupon` → `bilog` ×1
- [33] `lupon` → `bilog` ×1
- [34] `lupon` → `bilog` ×1
- [49] `lupon` → `bilog` ×1
- [52] `lupon` → `bilog` ×1
- [56] `lupon` → `bilog` ×1
- [68] `lupon` → `bilog` ×2
- [71] `lupon` → `bilog` ×1
- [231] `lupon` → `bilog` ×2
- [232] `lupon` → `bilog` ×1
- [234] `lupon` → `bilog` ×1
- [236] `lupon` → `bilog` ×1
- [237] `lupon` → `bilog` ×1
- [248] `lupon` → `bilog` ×1
- [251] `lupon` → `bilog` ×1
- [263] `lupon` → `bilog` ×1
- [265] `lupon` → `bilog` ×1
- [267] `lupon` → `bilog` ×1
- [285] `lupon` → `bilog` ×1
- [693] `lupon` → `bilog` ×1
- [697] `lupon` → `bilog` ×1
- [1216] `lupon` → `bilog` ×1
- [1243] `lupon` → `bilog` ×1
- [58] `taong yelo` → `taong-niyebe` ×1
- [59] `taong yelo` → `taong-niyebe` ×1
- [60] `taong yelo` → `taong-niyebe` ×2
- [68] `taong yelo` → `taong-niyebe` ×1
- [69] `taong yelo` → `taong-niyebe` ×1
- [70] `taong yelo` → `taong-niyebe` ×1
- [71] `taong yelo` → `taong-niyebe` ×1
- [508] `taong yelo` → `taong-niyebe` ×1
- [509] `taong yelo` → `taong-niyebe` ×1
- [512] `taong yelo` → `taong-niyebe` ×1
- [513] `taong yelo` → `taong-niyebe` ×1
- [514] `taong yelo` → `taong-niyebe` ×1
- [856] `taong yelo` → `taong-niyebe` ×2
- [109] `avenida` → `abenida` ×1
- [121] `avenida` → `abenida` ×1
- [135] `avenida` → `abenida` ×1
- [146] `avenida` → `abenida` ×1
- [154] `avenida` → `abenida` ×2
- [157] `avenida` → `abenida` ×1
- [364] `avenida` → `abenida` ×1
- [375] `avenida` → `abenida` ×1
- [378] `avenida` → `abenida` ×1
- [399] `avenida` → `abenida` ×1
- [999] `avenida` → `abenida` ×1
- [1027] `avenida` → `abenida` ×1
- [178] `avenue` → `abenida` ×1
- [179] `avenue` → `abenida` ×1
- [197] `avenue` → `abenida` ×1
- [199] `avenue` → `abenida` ×1
- [200] `avenue` → `abenida` ×1
- [228] `avenue` → `abenida` ×1
- [336] `avenue` → `abenida` ×1
- [667] `avenue` → `abenida` ×1
- [745] `avenue` → `abenida` ×1
- [749] `avenue` → `abenida` ×1
- [777] `avenue` → `abenida` ×1
- [789] `avenue` → `abenida` ×1
- [799] `avenue` → `abenida` ×1
- [854] `avenue` → `abenida` ×1
- [858] `avenue` → `abenida` ×1
- [176] `DIRTY` → `MARUMI` ×1
- [180] `DIRTY` → `MARUMI` ×1
- [183] `DIRTY` → `MARUMI` ×1
- [229] `DIRTY` → `MARUMI` ×1
- [315] `DIRTY` → `MARUMI` ×1
- [417] `DUMI` → `MARUMI` ×1
- [429] `DUMI` → `MARUMI` ×2
- [584] `DUMI` → `MARUMI` ×1
- [176] `UNSAFE` → `MAPANGANIB` ×1
- [183] `UNSAFE` → `MAPANGANIB` ×1
- [176] `DON'T EAT HERE` → `HUWAG KUMAIN DITO` ×1
- [183] `DON'T EAT HERE` → `HUWAG KUMAIN DITO` ×1
- [89] `Thanksgiving` → `Araw ng Pasasalamat` ×1
- [91] `Thanksgiving` → `Araw ng Pasasalamat` ×1
- [217] `Thanksgiving` → `Araw ng Pasasalamat` ×1
- [241] `Thanksgiving` → `Araw ng Pasasalamat` ×1
- [1091] `Thanksgiving` → `Araw ng Pasasalamat` ×1
- [1100] `Thanksgiving` → `Araw ng Pasasalamat` ×1
- [1131] `Thanksgiving` → `Araw ng Pasasalamat` ×1
- [1287] `Thanksgiving` → `Araw ng Pasasalamat` ×1
- [1288] `Thanksgiving` → `Araw ng Pasasalamat` ×1
- [243] `tsokolate-pekan` → `tsokolate-pecan` ×1
- [41] `chocolate-pecan cupcake` → `tsokolate-pecan na cupcake` ×1
- [293] `Chief Tanaka` → `Hepe Tanaka` ×1
- [299] `Chief Tanaka` → `Hepe Tanaka` ×1
- [673] `flyer` → `polyeto` ×1
- [679] `flyer` → `polyeto` ×1
- [683] `flyer` → `polyeto` ×1
- [901] `takuri` → `takure` ×1
