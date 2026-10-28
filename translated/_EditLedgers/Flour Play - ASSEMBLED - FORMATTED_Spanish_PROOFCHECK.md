# PROOFCHECK — Flour Play - ASSEMBLED - FORMATTED_Spanish (2026-10-28)

**Verdict: SIGNIFICANT. A re-run in `full` mode is recommended.**
- A reversed who-said-what in the Ch19 deduction was missed: the text said Danny had mentioned the gold shop, when the point is that he never did.
- The flyer "proof" in the same chapter had been turned into "evidence".
- The first pass's own edits broke agreement in four places.

## Scope
- **Mode:** targeted.
- **Edition:** `translated/corrected/Flour Play - ASSEMBLED - FORMATTED_Spanish.docx`.
- **Raw input for the diff:** `_superseded/…_Spanish.docx`, same grid of 2434 paragraphs.
- **Backup:** `_EditLedgers/_proofcheck_backups/Flour Play - ASSEMBLED - FORMATTED_Spanish.20261028-201230.docx`.
- **Paragraph numbers:** every paragraph in the file is counted, as in the flag file. The first-pass ledgers count non-empty paragraphs only, so their numbers differ.

**Read in full, sentence by sentence, EN against ES (15 chapters plus matter):**
- front matter and the blurb;
- Ch1, Ch20 and Ch24 (the lowest change density);
- the walk-in, cold-room, sour-base and confrontation chapters: Ch9, Ch10 together with Ch11 (they are fused), Ch13, Ch17, Ch18, Ch19, Ch21, Ch22, Ch23 and Ch25;
- Ch27 and all the back matter.

**Diff-audited only (every changed paragraph read against the English):** Ch2–Ch8, Ch12, Ch14, Ch15, Ch16 and Ch26. That is 547 changed paragraphs book-wide.

## Flags judged (A–J)

| Section | Result |
|---|---|
| A, C, D, F, G | 0 flags. |
| B (2) | False positive. «Bûches de Noël» is French in the English too. |
| E (3) | One real item, already logged as FP-ES-1 (formatter): the «Capítulo 11» heading line is missing. The body is complete: ES [867]–[898] = EN [524]–[554], 31 of 31 paragraphs. The "Ch10 171%" and "Ch11 no text" flags are consequences of that same item. |
| H (9) | False positive. Eight are «poner un pie» (an idiom) and one is «acre» (an adjective). |
| I (1) | False positive. [976] «Piensa en el rencor», le dije a la tetera is inner speech quoted in « », per dossier rule 5. |
| J (1) | False positive. [0] «Capítulo 3» was emptied, and the English title page has no such line. |

**Totals:** 1 real (already a decision), 15 false positives.

## Clue chain (section K), traced at every occurrence
- **Walk-in and cold room are two different words.**
  - walk-in = «cámara frigorífica» ×7: [744] [1374] [1620]×2 [1624] [1800] [1882];
  - Joyce's slip = «el cuarto frío»: [744] [748] [1612] [1620]×2 [1800] [1882] [1884] [1995];
  - Ch18 [1458] "a cold room at midnight" is correctly a plain «habitación fría»;
  - Pete's locker = «almacén (frigorífico)»; the display case = «vitrina refrigerada».
- **Sour base** = «base agria» ×18. «masa madre» appears once, at [882], correctly, for the English "the starter".
- **Other terms:**
  - «Diez veces» ×2.
  - «llave de la verja», «libro de encargos» and «fregadero Hobart» ×5.
  - «Nada que pueda identificar» is said by Doc ([874]), as in the English.
  - «dos grados por debajo de lo reglamentario» is identical at [726], [1241] and [1245].
- **No poison or toxic words.**
- **Numbers and gender:**
  - Joyce is 65 ([1999]); 25 years / 15 years together; «el veinte»; dollars only.
  - Pip is feminine throughout (with «pingüino» as the noun).
  - SUCIO in the graffiti.
- **Back matter:** the *The Binder's Bequest* anchors are kept, the closing line is present at [2433], and the blurb is in the present tense.

## Missed by the first pass (22 paragraphs, 23 edits, all applied)

| Para | Ch | ES before | EN | Class | Fix |
|---|---|---|---|---|---|
| 1490 | 19 | «Mencionó la tienda dorada.» | "I heard the gold shop. He never said it went into Sugarplum." | **Reversed meaning (who said what)** | «Yo entendí que era la tienda dorada.» |
| 1490 | 19 | «y yo no oí el de nadie más.» | "and I heard nobody's." | Mistranslation | «y yo entendí que no era de nadie.» |
| 1509 | 19 | «Un folleto sirve de prueba en el mostrador de alguien» | "A flyer's a proof on somebody's counter" (a printer's proof) | Mistranslation (clue: the flyer seen in proof) | «Un folleto es una prueba de imprenta en el mostrador de alguien» |
| 1938 | 23 | «Llamaste a Martha. Le habrías arrebatado mi Acción de Gracias…» | "You'd have had my Thanksgiving off my own counter" | Who-to-whom (the «le» pointed at Martha) | «Te habrías llevado mi Acción de Gracias…» |
| 1908 | 23 | «Nunca la cambiaste.» | "You never changed it." (the lock) | Reference: it read as the key | «Nunca lo cambiaste.» |
| 1880 | 23 | «una sonrisa irónica» | "rueful" | Mistranslation | «una sonrisa contrita» |
| 1964 | 23 | «De lo que sea que se arrepienta…, no cambia» | "Whatever you're sorry for…, it doesn't change" | Grammar | «Se arrepienta de lo que se arrepienta…, eso no cambia» |
| 1987 | 24 | «había llevado a Danny a un lado» | "taken Danny's word gently off to one side" | Mistranslation | «le había tomado declaración a Danny aparte» |
| 2027 | 24 | «no iluminó su rostro para mí» | "didn't light her face for me" | Calque | «no se le iluminó la cara al verme» |
| 990 | 13 | «No le entretendré con su trabajo» | "I won't keep you from your work" | Mistranslation | «No quiero apartarle de su trabajo» |
| 1284 | 17 | «que no pude ser yo» | "couldn't have been me" | Grammar | «que no podía haber sido yo» |
| 1304 | 17 | «con delantal de panadera» | "in a baker's apron" (gender-neutral clue) | Clue neutrality | «de panadero» |
| 1340 | 17 | «—No. No tiene.» | "No. She doesn't." | Elliptical | «—No. No tiene por qué.» |
| 1424 | 17 | «segurísima de que no podría» | "so certain he would not" | Shifted meaning | «de que no lo haría» |
| 1443 | 18 | «Estaba Greta de por medio» | "There was Greta to mind" | Mistranslation | «Tenía que ocuparme de Greta y entregar una corona…» |
| 2080 | 25 | «Tanaka le había llevado el tarro» | "Tanaka had taken the jar" | Stray clitic | «Tanaka había llevado» |
| 2088 | 25 | «…se la puso en la mano… Se lo comió» | "He ate it" (the corner) | Agreement | «Se la comió» |
| 2164 | 25 | «Le había dicho el resto al otro lado…» | "She had said the rest to Joyce" | Who-to-whom | «…el resto a Joyce al otro lado…» |
| 230 | 3 | «Pero mírame a mí» (Renée, usted elsewhere) | "But listen to me" | Register | «Pero míreme a mí» |
| 549 | 6 | «un dibujo —lo dijo rotundamente» | narration beat | Dialogue punctuation (the Book 2 ES convention) | «un dibujo. —Lo dijo rotundamente» |
| 683 | 8 | «seguirá volviendo una vela dorada» | "turning a candle gold" | Word order | «volviendo dorada una vela» |
| 96 | 1 | «en el Grange» | Grange | Term drift (18× «la Grange») | «en la Grange» (PC-FPES-1) |
| 126 | 1 | «Les llevaré un pastel» | "a pie" | Term drift (pie = «tarta») | «una tarta» |

## Regressions introduced by the first pass (6, all fixed)

| Para | Ch | First-pass change | Problem | Fix |
|---|---|---|---|---|
| 1430 | 17 | brote → ramita | «…la primera ramita… y lo apoyé»: the agreement broke | «la apoyé» |
| 1792 | 22 | mortusinas → eperlanos | «Se las comió una a una»: the agreement broke | «Se los comió uno a uno» |
| 1852 | 23 | hervidor → tetera | «la tetera abollada y lo habían puesto»: the agreement broke | «la habían puesto» |
| 644 | 7 | lomo → aguja | «la aguja envuelta… hacia él»: the agreement broke | «hacia ella» |
| 475 | 5 | «No saldrá, y no lo haré» → «No depende de ti, pero yo no lo dejaré salir» | The meaning changed. EN "It won't be, and I won't" | «No saldrá de aquí, y yo no seré quien lo saque» |
| 60 | 1 | «triplicaba» → «la mitad más grande» | This reads as "the bigger half", not 1.5× | «una vez y media más grande» (PC-FPES-2) |

**Other first-pass edits:** no lost italics, no removed `<bt>`, no edit in the wrong paragraph, and no renames spilling onto other objects. That covers walk-in vs locker vs display case, verja vs cancela, and libro de encargos vs Hal's «libro de cuentas» vs Tanaka's «cuaderno» vs Claire's «libreta».

## Ledger check
20 random rows from `_PROOFREAD.md`: 20 of 20 "Corrected" texts were found in the file. 0 mismatches.

## Open decisions re-checked
- **FP-ES-1 (missing Ch11 heading):** accurate.
- **FP-ES-2 (two degrees):** accurate and identical ×3.
- **FP-ES-3 (45 kg / 23 kg):** accurate.
- **FP-ES-4 (Binder's Bequest anchors and excerpt):** accurate.
- **FP-ES-5 (Greta and Kelly on tú):** confirmed throughout.
- **FP-ES-6 (title page):** accurate.
- None was undone.

**New decisions in PROOFCHECK_DECISIONS.md:**
- **PC-FPES-1:** Inn Trouble ES [1505] «el Grange» should become «la Grange».
- **PC-FPES-2:** Inn Trouble ES [1469] «la mitad más grande» should become «una vez y media más grande».

Both are cross-book follow-ups for Inn Trouble ES. Neither was applied, because they are not in this edition.

**Refusals:** 0.

## Checks after the fixes
- **looks_english:** `[]`.
- **bt_anchors check:** 9 spans, 0 unpaired. The spans are Frost and Found / Inn Trouble / Flour Play / The Binder's Bequest.
- **check_matter --file:** 1 PASS, 0 FAIL.
- **preflight --verify:** reported "source missing", because the raw copy lives in `_superseded/`. Compared by hand against the backup: 2434 → 2434 paragraphs; italic runs 54 → 54, identical and in order; scene breaks 58 → 58; `<bt>` 9 → 9; 28 paragraphs changed.
- **proofcheck.py re-run:** A0 B2 C0 D0 E3 F0 G0 H9 I1 J1. This is unchanged, because every remaining flag is a false positive or the formatter item.

**Rate:** 29 real defects in 15 chapters read in full plus 12 chapters read diff-only, about 1.9 per chapter read in full.
