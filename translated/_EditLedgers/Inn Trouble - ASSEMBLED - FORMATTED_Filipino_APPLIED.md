# APPLIED — Inn Trouble - ASSEMBLED - FORMATTED_Filipino — 2026-10-27

File: `translated/corrected/Inn Trouble - ASSEMBLED - FORMATTED_Filipino.docx`.
Base: the pre-flight copy already in `corrected/` (the original `translated/` input + 5 asterisk spans converted to italics). It was backed up first to `corrected/_bak/Inn Trouble - ASSEMBLED - FORMATTED_Filipino.pre-proofread-20261027.docx`. The original in `translated/` was not touched.

Method: run-level edits. Only `<w:t>` text inside the affected run(s) changed. Before every write, each paragraph was checked against its full snapshot text and the target string had to occur exactly once. A multi-run match was allowed only when all spanned runs had identical formatting. 3 italic-segment edits (the clue phrase at [189][1119][1264]) rebuilt that paragraph's runs with the original rPr cloned onto each. No paragraph was collapsed to its first run. `set_para_text` was not used.

- **Applied: 653** targeted edits. Para / was / now / why for each is in `Inn Trouble - ASSEMBLED - FORMATTED_Filipino_PROOFREAD.md`.
- **Dialogue punctuation:** 388 paragraphs, straight → curly “ ” (dossier, ruling 1). 0 odd-count paragraphs.
- **Refused by verification: 0.** Three entries first missed because my quoted context did not match the live text (a different preceding word at [886] and [1221], and [28] vs [26] for the blurb). Each was re-matched to the live text and then applied.
- **Report quotes not found:** 0.
- **Paragraphs:** 1552 → 1552 (nothing added or deleted. The 3 stray Ch19 headings and the Ch7 split are left for Lisa).
- **Italic runs:** 28 → 28 against the pre-flight copy, same order. Content changed only where italic text was translated: the note [187], the clue [189][1119][1264], `do not lose` [213], the drawer labels [691], the question [864], the folder tab [1141], the note quotation [1125], and the sell lines [1488][1498][1551]. Against the original `translated/` input, preflight shows 23 → 28. Those +5 are the pre-flight asterisk conversions, not mine.
- **`<bt>`:** 11 → 8. 4 stray spans removed (Yarn Tales, The Holly Jolly Bakery, Frost Falls [788], Winter Wonderland Inn [1130]; ruling 5). 1 title-page anchor added at [0] `<bt>Inn Trouble</bt>`, matching Book 1 Filipino's title page. Only Frost and Found / Inn Trouble / Flour Play remain.

## Needs a decision (logged in PROOFREAD_DECISIONS.md, section "Inn Trouble - ASSEMBLED - FORMATTED_Filipino (2026-10-26)")
FIL2-D1 stray Ch19 chapter headings · FIL2-D2 chapter-heading wording · FIL2-D3 imperial units in Filipino · FIL2-D4 Ch7 split paragraph · FIL2-D5 Book 1 quote style.

## Noted, not changed (formatter)
No Heading 1. TOC block is `Tungkol sa Aklat na Ito / Kabanata 31 / Ano ang Susunod? / Sipi mula sa…`, same pattern as Book 1. Two `***` back-matter separators [1486][1496] and one [1549]. "Tungkol sa Aklat na Ito" appears twice (TOC line + heading).

## Helper checks on the corrected file
1. Untranslated English (looks_english): `[]`. An extra word-level sweep also cleared code-switches (nag-waddle, i-blackmail, mang-extort, archive, endowment, snow globe, fountain, snowman…).
2. `bt_anchors.py check`: 8 spans, 0 unpaired. The span texts are only Inn Trouble / Frost and Found / Flour Play.
3. `check_matter.py --file`: 1 PASS, 0 FAIL.
4. `preflight.py --verify`: paragraphs 1552 → 1552 ok; scene breaks 3 → 3 ok. It prints "FAIL" only on deltas I declared: italic 23 → 28 (pre-flight asterisk conversions; my edits kept the 28 runs and their order), italic sequence differs where italic text was translated (listed above), and bt 11 → 8 (4 strays removed, 1 title anchor added).
