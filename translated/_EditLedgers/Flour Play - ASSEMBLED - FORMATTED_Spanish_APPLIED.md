# APPLIED — Flour Play - ASSEMBLED - FORMATTED_Spanish (2026-10-27)

## Files
- **Output:** `translated\corrected\Flour Play - ASSEMBLED - FORMATTED_Spanish.docx`.
- **Backup of the starting copy:** `corrected\_bak\Flour Play - ASSEMBLED - FORMATTED_Spanish.pre-proofread-20261027.docx`. The starting copy was the raw input plus the pre-flight asterisk→italic conversion (10 spans). That conversion was kept.
- The original `translated\…_Spanish.docx` was not touched.

## Method
- Edits touched `w:t` text only.
- Each fix had to be an exact substring of the paragraph's live text, occurring exactly once, or it was refused.
- Changes were mapped onto the existing runs by character diff. No runs were merged.
- No paragraph was added or removed (2434 → 2434, as counted by preflight).
- The edit sets live in the scratchpad (`esfp\e*.py`). Every row is in `_PROOFREAD.md` with para, before → after, and why.

## Applied: 711
- 643 targeted fixes.
- 68 excerpt paragraphs, taken from the published Spanish *El Legado de la Artesana* (FP-ES-4).

| Class | Count |
|---|---|
| Mistranslation (incl. reversed meanings) | ~165 |
| Term / series consistency | ~140 |
| Clue chain (cámara frigorífica / cuarto frío, base agria, libro de encargos, verja, denuncia, lechada, lavamanos, 'dos grados por debajo de lo reglamentario' ×3, founder's line) | 75 |
| Register / address | 77 |
| Peninsular variety (pararse, adentro, aserrín, papa, cuadra, mamá, estambre, prolijo, costo…) | ~52 |
| Grammar / typo / typography | ~50 |
| Dialogue rebuilt | 25 |
| Consistency of quoted echoes | 19 |
| Units | 11 (2 escalated) |
| Signs | 9 |
| Stray `<bt>` | 6 spans |
| Front matter | 5 |
| Back-matter sell lines | 3 |
| No-poison | 1 |

## Rulings
1. **Dialogue (ruling 1):** the edition was already raya throughout, so 0 paragraphs were converted. 25 stragglers were fixed (listed in `_PROOFREAD.md`).
2. **Address (ruling 2):** 77 edits. The table is in `_PROOFREAD.md`.
3. **Signs (ruling 3):** 9 translated: shop lettering ×3, graffiti ×5 places, web slogan.
4. **Ruling 4:** no "fifty miles" in this book.
5. **`<bt>` (ruling 5):**
   - 6 stray spans removed (Sugarplum Patisserie ×5, Holly Jolly Bakery ×1).
   - 4 real-title anchors added: series list [10][11][12], closing line [1508].
   - The Binder's Bequest ×5 kept (FP-ES-4).
6. **Cider (ruling 6):** cider does not occur in this book.
7. **Ruling 7:** term variants were unified to Book 1/2 ES:
   - parque, prado, el Holly Jolly, cancela, centavo, círculo, pingüino, manoplas, posadas.
   - Title page: the stray «Capítulo 3» was removed; the title is now «Harina de otro costal» (catalogue).

## Needs a decision
FP-ES-1 … FP-ES-6 are in PROOFREAD_DECISIONS.md. All are applied provisionally or are informational; none blocks the file.

## Refused by verification
- **0 net.** 18 strings failed the first dry run and were re-quoted against the live text, then applied:
  - Most included the italic view markers or a leading raya that is not at that position.
  - [1178] needed the preceding «—. ».
- **Report quotes not found:** 0. There was no prior report.

## Italic runs
Count: 54 → 53 against the starting copy; 44 → 53 against the raw input. The +10 is the earlier asterisk conversion; the −1 is [1497] «networking», now «hacer contactos» from the published text, plain.

Content changed only where italic text was itself translated or corrected:

| Para | Change |
|---|---|
| [319] | «Los/los buenos vecinos» |
| [323] | Capsule card «como dispusieron nuestros antepasados» |
| [330] | Gazette subhead, founder's line |
| [418] | «PANADERÍA HOLLY JOLLY» |
| [445] | «Citaba los subapartados.» |
| [695] | Flyer «Semana de Gran Inauguración» |
| [698] | Varney's line, now identical to [435] |
| [715] | Doc's line, now identical to [520]/[522] |
| [717] | Renée's line, now identical to [135] |
| [1036] | Slogan «Fresco a su puerta cada mañana» |
| [1377] | New-capsule card, now identical to [687] |
| [1392] | Joyce's letter «no pensé que fueras a creer» |
| [1393] | Joyce's letter «Sobre la tarta…» |
| [1431] | Sell-line series name «Lomos y Hechizos» |
| [1438] | Sell-line series name «Lomos y Hechizos» |
| [1508] | Closing line, now with a `<bt>` title anchor |

All other italic runs are identical in content and order.

## Helper checks on the corrected file
1. **Untranslated English** (`looks_english`): `[]` (empty).
2. **bt_anchors check:** 9 spans, 0 unpaired. The span texts are only Frost and Found, Inn Trouble, Flour Play and The Binder's Bequest. The Binder's Bequest is a real title (FP-ES-4).
3. **check_matter --file:** 1 PASS, 0 FAIL.
4. **preflight --verify:** reports "FAIL", but only on declared deltas:
   - paragraphs 2434 → 2434 ok
   - scene breaks 58 → 58 ok
   - italic runs 44 → 53: +10 earlier asterisk conversion, −1 [1497]; the subsequence differs only at the paras above
   - bt 11 → 9: −6 stray, +4 real titles

## Formatter (not touched)
- The «Capítulo 11» heading line is missing before [505]. The body is present (FP-ES-1).
- The TOC lists only «Capítulo 27».
- The title-page line [0] is now an empty paragraph (it held «Capítulo 3»).
- There is no Heading 1.
