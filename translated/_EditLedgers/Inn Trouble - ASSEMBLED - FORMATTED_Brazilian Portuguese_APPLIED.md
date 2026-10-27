# APPLIED — Inn Trouble - ASSEMBLED - FORMATTED_Brazilian Portuguese (2026-10-27)

## Files
- **Output:** `translated\corrected\Inn Trouble - ASSEMBLED - FORMATTED_Brazilian Portuguese.docx`, edited in place on top of the mechanical sweep (5 Markdown `*…*` spans → italics, kept). A pre-proofread backup of that file was kept in the session scratch dir.
- The raw input `translated\…_Brazilian Portuguese.docx` was not touched.

## Method
- python-docx/lxml, `<w:t>` text only, never `set_para_text()`. Every edit had to match an exact substring occurring exactly once in the paragraph's live text, was reduced to character-level operations and was refused if it crossed a formatting boundary. Book-wide terms were applied one occurrence at a time with unique context. Paragraph count unchanged (1542 → 1542).
- Full per-finding table (para, verbatim before → after, why): `_EditLedgers\Inn Trouble - ASSEMBLED - FORMATTED_Brazilian Portuguese_PROOFREAD.md`.

## Applied: 375

| Class | Count |
|---|---|
| Term / series consistency (praça, círculo, varanda, pousada, chalé, Jessica, Avenida Evergreen, Snowball, Dancer, Constance, invariable surnames, Sra. Claus, chefe de polícia…) | 121 |
| Mistranslation | 53 |
| Excerpt rebuilt from corrected Flour Play PT-BR Ch1 (32 verbatim, 17 adapted to this excerpt's older English) | 49 |
| Grammar / agreement | 30 |
| Address (ruling 2) | 28 |
| Clue chain (note «bilhete» ≠ letters «cartas», «a safira em seu coração», «ficha») | 20 |
| Typo / non-word | 13 |
| Untranslated English (incl. the translator's note in [1315]) | 12 |
| Cider → «suco de maçã (quente)» (ruling 6) | 11 |
| Idiom / calque | 9 |
| Reversed meaning (blurb [31], fist ×2, gallows, not-sleeping) | 5 |
| What's Next copied verbatim from corrected Flour Play PT-BR blurb | 5 |
| Front matter (title page, series-list anchors, heading) | 4 |
| Signs/labels translated (ruling 3: banner [348], drawer labels [691], file tab [1072], B-index [942]) | 4 |
| Register | 3 |
| Stray `<bt>` (ruling 5) — direct edits; 5 more removed inside other rows | 2 |
| Language leak (Vietnamese «cái», Spanish «tuve») | 2 |
| Units (SAFE) | 1 (+1 inside a term row: [1326] four acres) |
| European Portuguese («nenhuns»; «concedeu-mo» counted as Register) | 1 |
| Scene break not in the English emptied ([1162]) | 1 |
| Dialogue punctuation | 1 |

## Rulings
1. **Dialogue (ruling 1):** the edition already used the travessão throughout — **0 paragraphs converted**; 1 incise straggler rebuilt ([1338] «— continuou Noriko —,»). Quotes inside narration use "…" consistently.
2. **Address (ruling 2):** 28 edits; table in `_PROOFREAD.md` (Sam/Jamal/Vera/Neil formal both ways; Bram, circle, Nick, Mark, Theo informal; Noriko formal → informal from Ch25; Emma → «a senhora»).
3. **Signs (ruling 3):** FROST FALLS ATRAVÉS DOS ANOS [348] (the "last S" joke still works), ESCRITURAS. ALVARÁS. CADASTROS FISCAIS. REGISTROS DE PROPRIEDADE, 1900–1950. [691], PROPRIEDADE — AV. EVERGREEN — WINTER WONDERLAND INN. [1072]; the Ch19 "B" index entries reworded to file under B [942] [949]; italics kept.
4. **Ruling 4:** "fifty miles" [206] left as the MT has it («cinquenta quilômetros»).
5. **`<bt>` (ruling 5):** 7 stray spans removed — Winter Wonderland Inn [723], The Holly Jolly Bakery [775] [1477], "the sapphire at its heart" [1201] (and translated), Yarn Tales [1435] [1515], Gazette [1461]. 3 title anchors added: [0] [20] [21]. 12 → 8 spans, 0 unpaired; only Inn Trouble / Frost and Found / Flour Play remain.
6. **Cider (ruling 6):** «cidra» ×11 → «suco de maçã (quente)».
7. **Ruling 7:** «os Blackburns» ×13 / «os Worthingtons» ×3 → invariable; copyright line «Copyright 2026 por Lisa Bouchard.» already matches Flour Play PT-BR (Book 1 has «de», FP-PTBR-8).

## Needs a decision
IT-PTBR-1…12 in `PROOFREAD_DECISIONS2.md`. Only IT-PTBR-1 (title), IT-PTBR-2 (missing Capítulo 31 heading — formatter) and IT-PTBR-4 (Sam's register) want a ruling; the rest are applied provisionally or informational. None blocks the file.

## Refused by verification
- **0** in the final build. (During the build 4 blocks failed the exact-match check because I had written the dump's `_italic_` markers into the quoted text; corrected and re-applied.)
- Report quotes not found: n/a (no prior report).

## Italic runs (vs the sweep copy: 32 → 32 runs, order identical)
Content changed only where italic text was itself translated/corrected: [348] banner, [691] drawer labels, [944] card «(a safira em seu coração)», [1050] recap phrase (EN → PT), [1056] the quoted note line (EN → PT), [1072] file tab, [1315] the translator's-note run emptied (text removed, run left empty). preflight counts non-empty runs: 27 → 31 = +5 sweep − 1 ([1315]).

## Helper checks on the corrected file
1. Untranslated English (`looks_english`): `[]`.
2. `bt_anchors.py check`: 8 spans, 0 unpaired; texts: Inn Trouble, Frost and Found, Flour Play.
3. `check_matter.py --file`: 1 PASS, 0 FAIL.
4. `preflight.py --verify`: "FAIL" on declared deltas only — paragraphs 1542 → 1542 ok; italic runs 27 → 31 (+5 sweep, −1 [1315]); italic sequence differs only at the runs listed above; scene breaks 4 → 3 ([1162] emptied); bt 12 → 8 (−7 stray, +3 title anchors).

## Formatter (not touched)
- «Capítulo 31» heading missing in the body (text present from [1355]); TOC [24] lists only «Capítulo 31»; no Heading 1; «Sobre este Livro» [23] vs «Sobre Este Livro» [28].
- Back-matter `* * *` [1413] [1429] [1539] where the English has blank paragraphs; [1162] is now an empty paragraph.
- Blank paragraphs between every text paragraph in most chapters (not in Ch4).
- Sweep italics on names (Yarn Tales [385], Gazette [387] [401] [407]) and on the Ch22 recap phrase [1050] — roman in the English.
