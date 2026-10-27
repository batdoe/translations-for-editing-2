# APPLIED — Flour Play - ASSEMBLED - FORMATTED_Brazilian Portuguese (2026-10-27)

## Files
- **Output:** `translated\corrected\Flour Play - ASSEMBLED - FORMATTED_Brazilian Portuguese.docx`.
- **Backup of the starting copy:** `corrected\_bak\Flour Play - ASSEMBLED - FORMATTED_Brazilian Portuguese.pre-proofread-20261027.docx` (raw input + pre-flight asterisk→italic conversion, 18 spans — kept).
- The original `translated\…_Brazilian Portuguese.docx` was not touched.

## Method
- Edits touched `w:t` text only; each fix had to be an exact substring of the paragraph's live text, occurring exactly once, or it was refused. Changes were mapped onto the existing runs by token diff — no runs merged, no paragraph collapsed.
- No paragraph added or removed (2026 → 2026). Edit sets: scratchpad `ptfp\e00…e28.py`, `eglob.py`, `efin.py`; every row is in `_PROOFREAD.md` (para, verbatim before → after, why).

## Applied: 556

| Class | Count |
|---|---|
| Term / series consistency | 107 |
| Mistranslation (incl. 3 reversed meanings) | 95 |
| Clue chain (base azeda, câmara frigorífica vs «o cômodo frio», livro de encomendas, denúncia/incisos, guarnição, cadeado, depósito, founder's line, "dois graus abaixo do exigido") | 66 |
| Excerpt replaced from the published PT-BR edition | 61 |
| Register / address | 47 |
| European Portuguese — Ch19 rewritten (+1 spurious scene break emptied) | 47 |
| Grammar | 40 |
| Typo | 16 |
| Tense (present/«nesta manhã» in past narration) | 10 |
| Typography (ellipsis glyph) | 9 |
| Echo / quoted consistency | 8 |
| Stray `<bt>` removed / corruption restored | 7 |
| Language leak (Spanish/European) | 7 |
| Untranslated English (back matter, slogan) | 6 |
| Dialogue stragglers rebuilt | 6 |
| Idiom | 6 |
| Units (4 SAFE, 2 ESCALATED-applied) | 6 |
| Front matter (title page, series-list anchors) | 4 |
| Word choice / omission / addition / signs | 8 |
| Italic restored ([1805]) | 1 |

## Rulings
1. **Dialogue (ruling 1):** the edition already used the travessão throughout — **0 paragraphs converted**. 6 stragglers rebuilt: [390] (one speech split in two paragraphs read as a new speaker), [739] (narration turned into speech), [1047] (quoted speech run into narration with no marks), [1073] (narration inside Renée's speech, no closing travessão), [1507] [1559] (cut-off speech: trailing travessão, not «...»). Quotes inside narration: «» in Ch20 changed to "…" to match the rest of the book.
2. **Address (ruling 2):** 47 edits; table in `_PROOFREAD.md`.
3. **Signs (ruling 3):** PADARIA HOLLY JOLLY [171] [658]; web slogan [1418] translated (italic kept); graffiti SUJA / INSEGURA / NÃO COMA AQUI unified; van lettering WENDT'S BAKEHOUSE · BRIDGTON, «Sugarplum / Patisserie & Confiserie» and «Bûches de Noël» kept as business names (French also in the English).
4. **Ruling 4:** no "fifty miles" in this book.
5. **`<bt>` (ruling 5):** 8 stray spans removed — HOLLY JOLLY BAKERY [171], Wendt's Bakehouse, Bridgton [838] [1643], Sugarplum Patisserie [1101] [1147] [1173], Binding Thread [1981] (via the published excerpt), and the stray «The Binder's Bequest» that had replaced the capsule card [1805]. 4 real-title anchors added: title page [0] and series list [16]–[18]. The Binder's Bequest ×5 kept (real title). Result 14 → 10 spans, 0 unpaired.
6. **Cider (ruling 6):** no cider in this book.
7. **Ruling 7:** term variants unified (see `_PROOFREAD.md`); surname plural «os Doucettes» → «os Doucette» (×5).

## Needs a decision
FP-PTBR-1…9 in PROOFREAD_DECISIONS.md. Only **FP-PTBR-1** (catalogue title «Farinha Envenenada» = "Poisoned Flour" on the no-poison edition) needs Lisa; the rest are applied provisionally or informational. None blocks the file.

## Refused by verification
- **0.** No edit failed the exact-match check.
- **Report quotes not found:** n/a (no prior report).

## Italic runs
- Against the starting copy: 54 → 56 runs. Order identical; content changed only where italic text was itself translated/corrected:
  - [463] «Os bons vizinhos. / os bons vizinhos.» and [485] Gazette subhead «…pelos bons vizinhos.» (founder's line)
  - [1038] flyer «Semana da Grande Inauguração.»
  - [1047] Renée's line «Dá gosto pensar»
  - [1418] slogan «Fresquinho na sua porta toda manhã»
  - [1843] card «Para ser lacrada quando a antiga for aberta, no ano novo.» (= [1030])
  - [1949] [1959] [2025] sell lines translated (title anchors kept italic)
  - +2: [1805] restored capsule-card question, italic as in the English.
- Against the raw input (preflight baseline): 36 → 56 = +18 pre-flight asterisk conversion + 2 above.

## Helper checks on the corrected file
1. **Untranslated English (`looks_english`):** `[]` (empty).
2. **bt_anchors check:** 10 spans, 0 unpaired; span texts: Flour Play, Frost and Found, Inn Trouble, The Binder's Bequest (real title, back matter — kept as the other Flour Play editions did).
3. **check_matter --file:** 1 PASS, 0 FAIL.
4. **preflight --verify:** "FAIL" on declared deltas only — paragraphs 2026 → 2026 ok; italic runs 36 → 56 (+18 earlier asterisk conversion, +2 [1805]; content changes listed above); scene breaks 62 → 61 (spurious [1314] emptied); bt 14 → 10 (−8 stray, +4 real titles).

## Formatter (not touched)
- TOC lists only «Capítulo 27» ([21]); no Heading 1; «Sobre este Livro» [20] vs «Sobre Este Livro» [27].
- Back-matter `* * *` separators [1947] [1957] [2023] (EN 58 scene breaks vs 61 here).
- [1314] is now an empty paragraph (was a spurious mid-scene `* * *`).
- Many chapters carry blank paragraphs between every text paragraph (Ch1–4, 6, 7, 12–14, 17, 23–24, 27); others don't.
