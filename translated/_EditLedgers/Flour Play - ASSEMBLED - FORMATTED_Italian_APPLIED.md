# APPLIED — Flour Play - ASSEMBLED - FORMATTED_Italian — 2026-10-27

- File: `translated/corrected/Flour Play - ASSEMBLED - FORMATTED_Italian.docx`.
- Backup of the previous corrected copy (identical to the input): `corrected/_bak/Flour Play - ASSEMBLED - FORMATTED_Italian.pre-proofread-20261027.docx`.
- The original `translated/…_Italian.docx` was not touched.

## Method
- Edits were made at run level: only `<w:t>` text was changed and no paragraph's runs were collapsed.
- Before each edit, the paragraph's live text was checked to contain the exact target exactly once. A run-spanning edit was allowed only when every spanned run had identical formatting; otherwise it was refused.

## Applied
- **650 targeted edits.** Each one's para, was, now and why are in `Flour Play - ASSEMBLED - FORMATTED_Italian_PROOFREAD.md`. They break down as:
  - 600 targeted fixes.
  - 50 excerpt paragraphs, copied from the published *Il Lascito del Legatore*.
- **342 dialogue paragraphs** normalised to the caporali house system (ruling 1).
- **28 typography paragraphs** changed (’ → ', … glyph).

**By class:**

| Class | Count |
|---|---|
| Untranslated English, signs, back matter | 25 |
| Omissions restored | 2 |
| Mistranslations | 195 |
| Names, agreement | 21 |
| Register and address | 83 |
| Term consistency, typos | 263 |
| Front matter and scene break | 5 |
| Units | 6 |
| Excerpt | 50 |

## Refused by verification
0 net. Three entries first failed and were then re-matched to the live text and applied:
- [550]: the italic run ended before the period, so the edit was narrowed to the italic text.
- [1125]: the quoted span started mid-paragraph, not at «.
- [1356]: the English slogan was its own italic run, so the edit was narrowed to that run.

## Report quotes not found
0.

## Italic runs (43 → 43, same order)
Content changed in 10 runs, all of them translated or corrected italic text:

| Para | Change |
|---|---|
| [550] | founder's gloss «badate di ricordare come» |
| [978] | flyer «Settimana della Grande Inaugurazione» |
| [1356] | slogan «Fresco alla tua porta ogni mattina» |
| [1743] | Joyce's letter «del capo», «riesco a smettere» |
| [1744] | Joyce's letter «dal giorno in cui», «cartoncino» |
| [1782] (2 runs) | sell line |
| [1790] (2 runs) | sell line |
| [1843] | closing line, now with a `<bt>` anchor |

## Structure
| Item | Before → after | Note |
|---|---|---|
| Paragraphs | 1844 → 1844 | unchanged |
| Scene breaks | 59 → 58 | the spurious `* * *` at Ch19 [1252] was emptied; now equals the English |
| `<bt>` spans | 9 → 10 | see below |

`<bt>` changes:
- Removed 4 non-title spans: [676], [705], [1696], [1727].
- Added 5 real-title anchors: [0], [16], [17], [18], [1843].

## Address table (ruling 2)
See the PROOFREAD report. In summary:
- **tu:** circle, Greta, Kelly, Hal, Nick, Theo, and Tanaka with Jessica.
- **Lei:** Renée, Joyce, Pete, Doc, Anne Doucette, Varney, and Tanaka with Greta, Joyce and Renée.
- **Children → adults:** Lei.

## Needs a decision
FP-IT-1 … FP-IT-5 in PROOFREAD_DECISIONS.md. All of them are applied provisionally or kept as they were, so none blocks the file.

## Helper checks on the corrected file
1. **Untranslated English** (`looks_english`): `[]` (empty).
2. **bt_anchors check:** 10 spans, 0 unpaired. The span texts are only Flour Play, Frost and Found, Inn Trouble and The Binder's Bequest, the last being a real title (FP-IT-4).
3. **check_matter --file:** 1 PASS, 0 FAIL.
4. **preflight --verify:** reports "FAIL", but only because of the declared deltas:
   - paragraphs 1844 → 1844 ok
   - italic runs 43 → 43 ok; the sequence differs only in the 10 declared runs above
   - scene breaks 59 → 58 (declared spurious break)
   - bt 9 → 10 (declared, ruling 5 + title anchors)
   - no stray tags

## Formatter notes (not touched)
- There is no Heading 1.
- The TOC lists only «Capitolo 27».
- The MT paragraph splits Ch3 [225]/[226] and Ch22 [1426]/[1427] were kept so the paragraph count would not change.
