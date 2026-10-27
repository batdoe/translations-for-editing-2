# APPLIED — Flour Play - ASSEMBLED - FORMATTED_German (2026-10-27)

- Output: `translated\corrected\Flour Play - ASSEMBLED - FORMATTED_German.docx`.
- Backup of the starting copy: `corrected\_bak\Flour Play - ASSEMBLED - FORMATTED_German.pre-proofread-20261027.docx`. That starting copy was the raw input plus an earlier asterisk-to-italic conversion at [996] (`*Wo*` → italic `Wo`), which is kept.
- The original `translated\…_German.docx` was not touched.

## Method
- Edits were made at the `w:t` level only. Each fix was an exact substring of the paragraph's live text, and it had to occur exactly once, or the fix was refused.
- Changes were mapped onto the existing runs by character diff. No runs were merged, and no paragraph was added or removed (1373 → 1373 text paragraphs; 1952 → 1952 including empty ones).
- One edit touched two differently formatted runs: [1229], plain text plus the italic capsule card. The italic run was checked afterwards and contains exactly the card text.

## Applied
- **680 targeted fixes.** Each one's para, was, now and why are in `_PROOFREAD.md`.
- **49 excerpt paragraphs** were replaced from the published German *The Binder's Bequest* (FP-DE-6).
- **633 dialogue paragraphs** were converted from „…“ to »…« and from ‚…‘ to ›…‹ (ruling 1).

| Class | Count |
|---|---|
| Mistranslation / idiom | 222 |
| Term / series consistency (Avenue, Anger, Verein, Landkreis, Fass, Kuchen, Polizeichefin, Vitrine…) | 193 |
| Grammar / typo | 104 |
| Clue chain (Kühlzelle/Kühlraum, Säuerungsmittel, Bestellbuch, Torschlüssel, Kühllager, Fugenmörtel/Wetterabdichtung/Handwaschbecken, Lieferwagen, Flyer, Bäckerjacke, "zwei Grad unter Vorschrift") | 65 |
| Address du/Sie (ruling 2) | 45 |
| Stray `<bt>` removed (ruling 5) | 14 |
| Units | 13 |
| Signs translated (ruling 3): DIRTY / UNSAFE / DON'T EAT HERE → DRECKIG / GEFÄHRLICH / ESST HIER NICHT; POSTED → AUSGEHÄNGT; "Grand Opening Week" → Große Eröffnungswoche | 9 |
| Untranslated English | 9 |
| Reversed meaning (plus others counted under clue/mistranslation) | 2 |
| Omission restored ([717]) | 1 |
| No-poison ([804] `mit Gift versetzt`) | 1 |
| Scene break (spurious Ch19 `* * *` at [855] emptied; paragraph kept) | 1 |
| Front matter (title page) | 1 |

- Real-title `<bt>` anchors added: [0] [9] [10] [11] [1372].

## Needs a decision
FP-DE-1 … FP-DE-7 are in PROOFREAD_DECISIONS.md. All are applied provisionally or kept as they were, so none blocks the file.

## Refused by verification
0.

## Report quotes not found
0 (there was no prior report).

## Italic runs (44 → 45; +1 = the earlier [996] conversion)
Content changed only where italic text was itself translated or corrected:

| Para | Change |
|---|---|
| [316] | Gazette subhead, founder's line made identical to [303] |
| [318] | Hal's heading «Rettet das Museum» → «Rettet den Verein» |
| [662] | Varney's quoted words made identical to [418] |
| [676] | Doc's quoted words made identical to [497] |
| [678] | Renée's quoted words made identical to [124] |
| [1229] | Capsule card made identical to [651] |
| [1275] | Joyce's letter, mistranslation fixed |
| [1276] | Joyce's letter, mistranslation fixed |
| [1313] | Sell line series name |
| [1320] | Sell line series name |
| [1372] | Closing line translated, with a `<bt>` title anchor |

The order of all other italic runs is unchanged.

## Helper checks on the corrected file
1. **Untranslated English** (`looks_english`): `[]` (empty).
2. **bt_anchors check:** 10 spans, 0 unpaired. The span texts are only Flour Play, Frost and Found, Inn Trouble and The Binder's Bequest. The Binder's Bequest is a real title, kept per the brief.
3. **check_matter** (the tool takes a positional file argument; it has no `--file` flag): `OK`, 1/1 clean.
4. **preflight --verify --expect-italics 1:** reports "FAIL", but only because of declared deltas:
   - paragraphs 1952 → 1952 ok
   - italic runs 44 → 45 ok
   - italic subsequence differs only at the declared paras above
   - scene breaks 59 → 58 (the spurious break was removed; this now equals the English)
   - bt 19 → 10 (−14 stray per ruling 5, +5 real titles)

## Formatter (not touched)
- There is no Heading 1.
- The TOC lists only «Kapitel 27».
- The MT paragraph split at Ch2 [105]/[106] was kept so the paragraph count would not change.
