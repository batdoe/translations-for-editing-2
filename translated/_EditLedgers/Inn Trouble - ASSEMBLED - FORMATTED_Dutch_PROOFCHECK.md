# PROOFCHECK — Inn Trouble - ASSEMBLED - FORMATTED_Dutch (2026-10-28)

- **Mode:** targeted.
- **Files:** audited `translated/corrected/Inn Trouble - ASSEMBLED - FORMATTED_Dutch.docx`. Raw for the diff: `_superseded/…_Dutch.docx`, the pre-web-pass file, so the diff covers the web pass and the local pass together. English: `translate_now/Inn Trouble - ASSEMBLED - FORMATTED.docx`.
- **Backup:** `_EditLedgers/_proofcheck_backups/Inn Trouble - ASSEMBLED - FORMATTED_Dutch.20261028-181952.docx`.
- **Chapters read in full (EN vs NL, sentence by sentence):**
  - lowest change density: Ch17, Ch23, Ch29;
  - plot-critical: Ch2, Ch19, Ch22, Ch25, Ch26;
  - front matter and blurb;
  - all back matter (sell lines, What's Next?, the Flour Play excerpt).
  - Ch27 [1313] was also read for the reflexive lesson.
  - That makes 8 chapters plus the front and back matter.
- **Diff audit:** all 357 paragraphs whose text changed (quote-glyph-only changes excluded) were read next to the English. 20 random `_APPLIED.md` entries were checked: all 20 "now" strings are in the file. I then checked all 171 rows: none is missing.
- **Flags judged:**
  - **B (2):** both false positives. `gênante` [1328] is standard Dutch spelling. `Jíj` [1362] is the Dutch stress accent, and the English has emphasis there ("You were the circle").
  - **E (1):** REAL. [37] read `Hoofdstuk 3`, but the body is EN Ch1 verbatim and the next heading is `Hoofdstuk 2`, so it was a lone wrong digit. Fixed to `Hoofdstuk 1` (resolves NL2-D1).
  - **H (3):** all false positives. [185] `vijftig mijl` is left as is under ruling 4. [881] `een voet in het archief gezet` is the "never set foot" idiom. [1498] `Niet de afgelegde mijlen` is the "not the miles" idiom.
  - **A, C, D, F, G, I, J:** 0 flags.
  - **Total:** 1 real / 5 false.
  - **Re-run after the fixes:** A=0 B=2 C=0 D=0 E=0 F=0 G=0 H=3 I=0 J=0 (E went from 1 to 0).

## Missed by the first pass
| Para | Ch | Dutch (was) | English | Class | Fix (applied) |
|---|---|---|---|---|---|
| 37 | Ch1 | `Hoofdstuk 3` | Chapter 1 | heading digit | `Hoofdstuk 1` ✔ |
| 1313 | Ch27 | `precies datgene wat Theo had verwoest in zijn poging het te redden` | "the very thing Theo had ruined himself trying to save" | reversed meaning (reflexive: the Dutch said Theo ruined the Society) | `precies datgene waarvoor Theo zichzelf te gronde had gericht in zijn poging het te redden` ✔ |
| 343 | Ch4 | `ging verder met iedereen uit te nodigen voor de cider.` | "invite everyone to the cider" | ruling 6 (Dutch *cider* is alcoholic). This is the only one of the 11 left | `voor de appelsap.` ✔ |
| 208 | Ch2 | `bleef ik even op de stoep staan` | "I stood on the porch" | term drift (porch = veranda; the other 21 places are right) | `op de veranda staan` ✔ |
| 1116 | Ch22 | `Hij had de diefstal.` | "He had the theft." | clue-chain wording. It is unidiomatic, and it differs from the same deduction at [1151] / [1268] (`het geheim van de diefstal`) | `Hij had het geheim van de diefstal.` ✔ |
| 1358 | Ch29 | `…in het licht had gesleept en de boel overhoop had gehaald` | "dragged Theo Hussein up into the light and grieved the place" | mistranslation: the Dutch said "stirred things up" where the English says "brought grief" | `…en het dorp verdriet had gedaan` ✔ |
| 1556 | excerpt | `die naar het begin van de straat stond te staren` | "facing up the block" | direction reversed. [1544] says it points to the FAR end of the block | `die de straat op stond te staren` ✔ |

## Regressions introduced by the first pass
| Para | Ch | Dutch (was) | English | Class | Fix (applied) |
|---|---|---|---|---|---|
| 409 | Ch6 | `het grote gemeenschappelijke grasveld ten zuiden van Evergreen die vanaf het dorpsplein afliep` | "the big common south of Evergreen that ran down from the square" | broken agreement: *de weide … die* became *het grasveld … die* | `…Evergreen dat vanaf…` ✔ |

No other regressions were found. Every term swap was grepped for broken forms, and none turned up:
- de/het brink, Genootschap, festival, stadje, briefje, veranda, kring, appelsap;
- briefje followed by hem/hij (all are the smell, not the note);
- Genootschap followed by ze/haar.

The 357 changed paragraphs keep their meaning against the English. All of these are correct now:
- [389] "kept my fist open";
- [685] Blackburn direction;
- [752] worried sick;
- [1151] / [1268] "Theo had the theft" = *wist van / had het geheim van* (not "committed");
- [992] Nick: *Het is de liefde die het hem toestaat, Jess*.

## Clue chain (traced end to end)
- **"The sapphire at its heart"** = `de saffier in haar hart`. It is identical in every place:
  - the note [177];
  - Jessica's readings [178] [195] [972];
  - Theo's card [968] [970];
  - the Ch22 recap [1100];
  - Ch23 [1151];
  - the confrontation [1258].

  It has 5 words, so the "vijf woorden" lines at [972] ×2, [986], [1100] and [1205] are all true.
- **Note vs letters.** The note family is always *briefje* (afpersingsbriefje / dreigbriefje / chantagebriefje). *Brief/brieven* is used only for the 1924 letters, Fiona's mail [1035] [1061], rejection letters [703] [709], Constance's letter [948] and the Pole letters. I checked every occurrence, Ch19, Ch22, the Ch25 evidence list [1205] and Ch26 [1258] included.
- **Sam is owed.** The blurb [34] has `nog twintig dollar tegoed had`, and the text is consistent with it.
- **Other settled terms:**
  - cider = appelsap, now 11/11;
  - Snowball ×12;
  - circle = kring (`handwerkkring` stays as a descriptive form at [160] [368]);
  - green = brink, 39×; `dorpsplein` / `pleintje` appear only where the English says "square";
  - paddock = weide;
  - porch = veranda, now 22/22.
- **Excerpt:** "Very nearly" = `Nagenoeg wel`.

## Excerpt vs policy (PC-FIL2-1 class, not re-raised)
The Dutch excerpt follows Inn Trouble's OWN English. It has the Inn Trouble-only material, with nothing carried over from Flour Play:
- "In het weekend";
- the muziektent / oorlogsmonument;
- "hek bij de muziektent";
- "zondag";
- the permit-board line;
- "En ik zei niet wat ik dacht";
- "Er stond iets te gebeuren";
- the magic's "nose" line;
- "al vele jaren weduwe";
- chocolade-pecan.

However, like Filipino, it is a **separate translation**: almost none of corrected Flour Play NL Ch1's wording is reused, even where the two English texts are identical. For example, FP has `‘Nou ja, bijna.’` and this edition has `‘Nagenoeg wel.’`. PC-FIL2-1 (option a/b) covers this, and Lisa's ruling there should be applied to Dutch too. No paragraph was dropped (48/48), and the snowmen question is not inverted.

## Open decisions re-checked (PROOFREAD_DECISIONS.md, NL2-D1…D5)
- **NL2-D1 (para 37):** RESOLVED here. It was a one-digit fix: the body is clearly Ch1, and no renumbering of other chapters was needed.
- **NL2-D2 ([996] `* * *`):** still accurate. The English has no break there. Left for the formatter.
- **NL2-D3 (italics the translator added):** still accurate. [26] [178] [616] [622] [624] [1061] [1100] are italic in Dutch and roman in the English. The raw file had literal `*…*` markers, which the web pass turned into italic runs.
- **NL2-D4 (dorp/stadje):** still accurate.
- **NL2-D5 (bitterzoet [53]):** still accurate.
- **FP-NL-3 (Snowball vs Book 1 Sneeuwbal):** this edition uses Snowball ×12. Not changed, as instructed.
- **Leftover:** the TOC lists only `Hoofdstuk 31` [22]. That is formatter work.

## Decisions added / refusals
- No new questions for Lisa. Two informational notes were added to PROOFCHECK_DECISIONS.md: PC-NL2-1 (NL2-D1 resolved) and PC-NL2-2 (the excerpt falls under PC-FIL2-1).
- No refusals: all 8 edits matched the paragraph's complete current text inside a single `<w:t>`.

## Four checks (after the fixes)
1. **looks_english:** `[]`.
2. **bt_anchors check:** 4 spans, 0 unpaired. The spans are Inn Trouble ×2, Frost and Found and Flour Play.
3. **check_matter --file:** 1 PASS, 0 FAIL.
4. **preflight --verify:** it reported "source or corrected copy missing" because the raw file is in `_superseded/`. I compared the corrected file with the backup by hand:
   - paragraphs 1567 → 1567;
   - italic runs 23 → 23, identical and in order;
   - `<bt>` spans identical;
   - scene breaks [996, 1446, 1462, 1564] unchanged;
   - the only changed paragraphs are [37, 208, 343, 409, 1116, 1313, 1358, 1556].

## Verdict
**SIGNIFICANT.** The first pass missed a reversed-meaning defect, the "ruined himself" reflexive at [1313]. That is the same class the Romanian audit found. All the other misses are minor and are fixed. The clue chain, the note/letters split and the excerpt are sound.
- **Rate:** 8 real defects across about 10 sections read in full (8 chapters plus the front and back matter), about 0.8 per section.
- **Recommendation:** a FULL-mode pass on this edition, because 23 unread chapters may hide more reflexive or pronoun reversals.
