# PROOFCHECK — Inn Trouble - ASSEMBLED - FORMATTED_Brazilian Portuguese (2026-10-28)

- **Mode:** targeted.
- **Files:** audited `translated/corrected/Inn Trouble - ASSEMBLED - FORMATTED_Brazilian Portuguese.docx`, edited in place. Backup: `_proofcheck_backups/Inn Trouble - ASSEMBLED - FORMATTED_Brazilian Portuguese.20261028-175959.docx`. Raw input for the diff: `translated/…_Brazilian Portuguese.docx`, read-only.
- **Read in full, English against PT-BR, sentence by sentence:**
  - The three chapters with the lowest first-pass change density: Ch3, Ch14 and Ch29.
  - The plot-critical chapters: Ch2, Ch19, Ch22, Ch25 and Ch26.
  - Front matter and blurb [0]–[32], all of Ch31 [1355]–[1411] (checked line by line for completeness), What's Next [1415]–[1431], and the whole excerpt [1433]–[1541].
- **First-pass edits audited:** all 289 changed paragraphs, word-diffed raw → corrected. Every suspicious change was read against its English.
- **Ledger check:** 20 random `_PROOFREAD.md` rows, plus a sweep of all 375. Every "after" text is in the file. The 25 apparent misses are rows the ledger truncates with " …", and their segments are present.

## Flags judged (A–J)
- **A–D, F, G, I: 0 flags.** Nothing to judge.
- **E (2): both are a formatter issue, not missing text.**
  - The Ch30 length of 206% and "Ch31 no text" are one issue: the «Capítulo 31» heading line is missing.
  - The Ch31 text is complete. It runs [1355]–[1411]: 29 PT paragraphs for 28 EN, at a length ratio of 1.10, and every EN paragraph has its PT counterpart.
  - Already logged as IT-PTBR-2.
- **H (10): 0 real.**
  - [18] «reais» = "real persons", not the currency (false positive).
  - The 8 «centavo» are "a penny / a cent / every cent" idioms. They are dollar-neutral and acceptable in BR, so false positives.
  - [850] «um pé do sapato» is a body part (false positive).
- **J (3): 1 real.**
  - [2] emptied «Problema na Pousada»: correct. EN [2] is "Frost Falls", which is at [4]. Logged as IT-PTBR-1.
  - [1162] emptied `***`: correct. EN Ch25 has no break between [778] and [779], and the first pass logged it.
  - **[1471] cut to 43%: REAL (regression, fixed).** See below.

## Missed by the first pass
1. **[1211] Ch26, the confrontation (mistranslation, plot).**
   - **Target:** «— Theo cometeu o furto. … — Ele cometeu o furto. A senhora tinha a escritura.» ("Theo committed the theft")
   - **English:** "Theo had the theft. … He had the theft. You had the deed."
   - **Why it matters:** this is the two-halves-of-the-secret deduction. Theo held the knowledge of the 1924 theft; Constance stole the brooch. The PT text made Theo the thief.
   - **Fix (APPLIED):** «Theo tinha o roubo.» / «Ele tinha o roubo.», mirroring Ch22 [1058] «Ele tinha o roubo.»
2. **[1211] Ch26 (mistranslation).**
   - **Target:** «nunca lê os registros que guarda nas costas» ("keeps on her back")
   - **English:** "never reads the records at her back"
   - **Fix (APPLIED):** «os registros que ficam atrás dela», as in Ch23 [1074].
3. **[315] and [343] Ch3 (term drift).**
   - **Target:** «com o pasto e o formato escuro da oficina» and «lá além do pasto meu marido».
   - **English:** "paddock"
   - **Fix (APPLIED):** «piquete», the edition's form at 8 other places and the form in Book 1 PT-BR. [343] now matches its twin sentence at [668].
4. **[1281] Ch29 (calque).**
   - **Target:** «Eu deveria saber melhor.»
   - **English:** "I should have known better."
   - **Fix (APPLIED):** «Eu devia ter imaginado.»
5. **[1477] excerpt (term).**
   - **Target:** «cupcakes de chocolate com nozes» ("walnuts / nuts")
   - **English:** "chocolate-pecan cupcakes"
   - **Fix (APPLIED):** «chocolate com noz-pecã». This matches [1481] «noz-pecã» and Greta's settled «chocolate com noz-pecã» throughout Flour Play PT-BR.
   - The same slip is in corrected Flour Play PT-BR [77]; see PC-IT-PTBR-1.

## Regressions introduced by the first pass
1. **[1471] excerpt (omission).**
   - **What happened:** the first pass replaced the whole paragraph with corrected Flour Play PT-BR [68]. FP splits this English paragraph in two, so the second half, FP [69], was lost.
   - **Lost text (English):** "I gave Pip the look that means I have not stopped watching you, and she gave me the one that means I have not stopped wanting the ribbon, and we understood each other. I went back to my scales of balsam."
   - **Fix (APPLIED):** appended FP [69]'s wording verbatim: «Dei a Pip o olhar que significa não tirei os olhos de você, e ela me deu o olhar que significa não parei de querer a fita, e nos entendemos. Voltei às minhas escamas de abeto.»
   - **Italics:** left roman. Inn Trouble's English is roman here; FP italicises the two looks.
   - **No other cases:** every other excerpt paragraph was checked against EN [935]–[982], and nothing else is cut.
- **Nothing else found** among the 289 edits. The checks covered:
  - grammar after the term swaps: bilhete m., the «os Blackburn» invariables, «o chalé», «as couves», «terminado», «surpreso»;
  - the formal-address rebuilds for Sam, Vera, Neil and Jamal (Ch8, 11, 13, 17, 23, 26, 27);
  - the dialogue incises.
- **Untouched:** italics (32 runs, order unchanged) and the `<bt>` title anchors.

## Clue chain (traced end to end): consistent
- **«a safira em seu coração»** is identical at [190] [192] [228] [944] [945] [946] [1050] [1088] [1201]. "Five words" [946] ×2, [953], [1050] and [1144] is true in PT.
- **The note is «bilhete(s) (de chantagem)»** in every place. No note uses «carta» or «nota»: the remaining «nota» hits are «bloco de notas» and «notas de dólar».
- **The 1924 letters are «cartas»** everywhere, including Ch19 [949] «permitira que outra pessoa os escrevesse», the Ch22 recap, the Ch25 evidence list [1144]/[1148] «Os dois bilhetes» and the Ch26 confrontation [1201]/[1211].
- **Theo's card is «ficha»**, distinct from Neil's business «cartão».
- **The other settled terms all hold:**
  - Sam is owed the money: blurb [31] «a quem deviam» and [552] «Ela me deve vinte dólares».
  - Cider: 0 «cidra»; it is «suco de maçã (quente)».
  - Snowball ×12. Circle = «círculo»; no «roda» or «grupo» left.
  - Reindeer: Dancer, Prancer, Vixen.
  - The green = «praça»; [426] «gramado» = "common", as settled.
  - Porch = «varanda».
- **Excerpt:** "Very nearly" = «— Quase.» [1449]. The excerpt follows Inn Trouble's own English draft (bandstand/war memorial, "by Sunday, mark me", present tense "conheço", "Something was starting", the permit board line).

## European-Portuguese drift
- **None material.** There is no «estar a» + infinitive, no tu/teu, no EP vocabulary, no mesoclisis, and no «-mo» contractions.
- **Kept:** 5 «Ele virou-se»-type enclises after a subject in narration ([71] [103] [111] [609] [922]). They are acceptable in literary BR.

## Open decisions re-checked (IT-PTBR-1…12)
- **The quotes are still accurate:** [0], [2] empty, [24] and the missing «Capítulo 31» heading, [206] «cinquenta quilômetros», [380] «meio centímetro», [1326], [942]/[949], and [23] vs [28].
- **IT-PTBR-3 (excerpt):** now also covers the [1471] regression fixed here.
- **Nothing the first pass applied oversteps a ruling.**

## Decisions added
- PC-IT-PTBR-1: Flour Play PT-BR follow-up, informational. FP [77] has «chocolate com nozes».

## Refusals
- 0

## Checks after the fixes
1. `looks_english`: `[]`.
2. `bt_anchors.py check`: 8 spans, 0 unpaired. The spans are Inn Trouble, Frost and Found and Flour Play.
3. `check_matter.py --file`: 1 PASS, 0 FAIL.
4. `preflight.py --verify` against raw: 1542 → 1542, ok. The italics (27 → 31), scene breaks (4 → 3) and bt anchors (12 → 8) show the same first-pass deltas already declared in `_APPLIED.md`. Against my backup: the paragraph count and the italic sequence are identical, and only [315] [343] [1211] [1281] [1471] [1477] changed.
5. `proofcheck.py`: J went from 3 to 2 (the [1471] cut is gone). E is unchanged at 2, the formatter issue. H is unchanged at 10, all false positives.

## Verdict: **SIGNIFICANT**
- **Why:** a plot-chain mistranslation in the Ch26 confrontation, where Theo was made the thief ("had the theft"), was missed. There was also an excerpt omission that the first pass introduced itself.
- **Counts:** 5 missed and 1 regression across 9 chapters plus the front and back matter, read bilingually. That is about 0.5 real defects per chapter read.
- **Recommendation:** a `full` re-read of the remaining 22 chapters. The rest of the first pass held up well, so this is optional, but the Ch26 miss sat in a chapter the first pass had marked as dense.
