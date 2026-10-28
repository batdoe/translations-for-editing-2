# PROOFCHECK — Flour Play - ASSEMBLED - FORMATTED_Swedish (2026-10-28)

- **Mode:** targeted. No sub-agents. Chapters were read EN against SV with python-docx, sentence by sentence.
- **Read in full:**
  - Front matter and the blurb.
  - Ch1, Ch2, Ch3, Ch12. Ch12, Ch2 and Ch3 are the 3 lowest change-density chapters (23 / 26 / 27 %). Ch1 was read for the lessons and the Inn Trouble excerpt.
  - The plot-critical chapters: Ch9, Ch11, Ch13, Ch17, Ch18, Ch19, Ch20, Ch21, Ch22, Ch23, Ch24. These are the chapters in section K for walk-in / cold room / sour base / gate key / order book, plus the confrontation.
  - The end of Ch27, the back matter and the Binder's Bequest excerpt. Echo lines were also spot-checked in Ch15, Ch16 and Ch26.
- **File:** `translated/corrected/Flour Play - ASSEMBLED - FORMATTED_Swedish.docx`. The backup is in `translated/_EditLedgers/_proofcheck_backups/` (`….20261028-222941.docx`).

## Flags judged (PROOFCHECK_FLAGS.md)
- **A–J:** only B has flags (2). Both are false positives: [2104] `Bûches de Noël` is the French product name on Sugarplum's card, and the English has it too.
  - **E:** 0. All 27 chapters are present. The TOC/heading oddities are the formatter's job (FP-SV notes).
  - **J:** 0. The first pass emptied no paragraphs.
- **K (clue chain), traced:**
  - **sour base = syrningsmedel:** 17 + 2 occurrences. One rendering, with neuter agreement checked. `surdeg` appears only in Doc's 'sourdough tang' (`surdegssmak`). There is no starter or yeast spill.
  - **walk-in = kylrummet and Joyce's word = 'kallrummet' / kallrum.** These stay separate words at [867] [875] [1711] [1719] [1723] [1892] [1989] [1991] [2090]. Renée's walk-in is [1496] `kylrummet`. Pete's locker is `kylförråd`, which does not collide. Ch18's ordinary "a cold room at midnight" = `ett kallt rum`, which is correct and is not the clue word.
  - **'ten times':** one scene ✓.
  - **gate key / lock:** `Jag har aldrig bytt det` [1741] and `Du bytte det aldrig` [2013] both mean the LOCK ✓. The key was `lät göra` ✓.
  - **order book = beställningsboken:** 7 = EN 7, with no spill onto other books.
  - **"Inget jag kan sätta namn på":** the line is Doc's, in Ch11 ✓.
  - **'two degrees':** identical ×3 ✓.
  - **No poison:** the only `gift` hits are `uppgift` ✓.
  - **Pip:** she throughout ✓. Jessica is never masculine ✓.
  - **Numbers:** Joyce 65 ✓, 23 / 15 / 25 years ✓, "the twentieth" ✓.
  - **Other terms:** DIRTY = SMUTSIGT ✓, the Grange = bygdegården ×15 ✓, dollars/cents only ✓.
  - **Anchors:** the Binder's Bequest `<bt>` anchors are kept. The closing line is still missing, which is already logged as FP-SV-D3.
- **Lesson lines checked explicitly:**
  - Ch13 'a temper he didn't have' = `ett lynne han inte hade` (a disposition) ✓.
  - Ch17: the FIGURE goes past the pharmacy light (`Jag tappade bort det efter ljuset vid apotekets hörna`) ✓.
  - Ch19 'proof' = `korrektur` ✓.
  - Ch19 'I heard the gold shop' was **reversed**, and is fixed below.
  - Ch23: who would have been robbed is right ✓.
  - Ch24 'took Danny's word … to one side' ✓.
  - Ch1 'half again' = `hälften större` (1.5×) ✓.
  - Greta's box = `bagerilåda` ✓. `konditori` is used only for Sugarplum or patisseries in general (8 places checked).
  - Ch22 split turns: every narration beat names its own subject. No Tanaka line reads as Jessica's.
  - The blurb is in the present tense ✓.
- **L (four standard checks):** clean (see below).
- **M:** used to choose the chapters to read.

## Missed by the first pass (all APPLIED)
- [42] Ch1 MT 'lagom' for 'lager' (layer): 'a good clean six inches'. Was `ett gott, rent lagom på femton centimeter` → now `ett gott, rent lager på femton centimeter`. APPLIED.
- [80] Ch1 calque 'Not long ago' ('inte för länge sedan' = not too long ago). Was `Inte för länge sedan hade jag` → now `För inte så länge sedan hade jag`. APPLIED.
- [108] Ch1 present-tense slip in preteritum narration (PC-SV-1, IT excerpt [1667]). Was `dagarna drar sig ihop så fort nu` → now `dagarna krympte så fort nu`. APPLIED.
- [161] Ch2 subordinate-clause word order (BIFF). Was `att något stod inte rätt till` → now `att något inte stod rätt till`. APPLIED.
- [199] Ch2 'my busiest season' ('värsta' = worst). Was `under min värsta högsäsong` → now `mitt i min mest hektiska säsong`. APPLIED.
- [268] Ch3 'the night of the wreath circle': circle = cirkeln (term drift 'krets'). Was `samma kväll som kransbindarkretsen träffades` → now `samma kväll som cirkeln band kransar`. APPLIED.
- [316] Ch3 'frank and rueful' ('ångerfull' = remorseful). Was `uppriktig och ångerfull` → now `uppriktig och beklagande`. APPLIED.
- [330] Ch3 'cheaper by half' ('hälften så billigt' reads as half as cheap). Was `och hälften så billigt i de mängder jag tar` → now `och till halva priset i de mängder jag tar`. APPLIED.
- [730] Ch7 three dots -> single ellipsis character (dossier). Was `hur...,` → now `hur…,`. APPLIED.
- [984] Ch11 preserving jar = syltburk (Ch2); 'konservburk' = tin can. Was `i en konservburk i min kappa` → now `i en syltburk i min kappa`. APPLIED.
- [1004] Ch12 'since dark' = in the pre-dawn dark; 'sedan det mörknat' = since dusk. Was `som hållit på vid ugnarna sedan det mörknat` → now `som hållit på vid ugnarna sedan långt före gryningen`. APPLIED.
- [1020] Ch12 'with her back to it' — SV gave the door the back. Was `Öppen mot luften med ryggen vänd mot den,` → now `Öppen mot luften medan hon stod med ryggen mot den,`. APPLIED.
- [1416] Ch16 Renée's 'Poor woman' = Ch3 [306] / [1392] / [1525] wording. Was `Stackars kvinna.` → now `Stackars människa.`. APPLIED.
- [1446] Ch17 spray-painted word: 'klistrade' = pasted. Was `och de klistrade det värsta ordet` → now `och de målade det värsta ordet`. APPLIED.
- [1467] Ch17 preserving jar = syltburk. Was `på konservburken som jag ställde ned` → now `på syltburken som jag ställde ned`. APPLIED.
- [1529] Ch17 penguin 'flippers' = wings (Ch22 'under vingen'); 'simfötter' = webbed feet. Was `med simfötterna bakåt` → now `med vingarna bakåt`. APPLIED.
- [1538] Ch18 'a wake' = likvaka ('vakstuga' = sickroom watch). Was `det kändes som en vakstuga där` → now `det kändes som en likvaka där`. APPLIED.
- [1551] Ch18 'out of the wet'. Was `bortom det blöta` → now `undan det blöta`. APPLIED.
- [1594] Ch19 REVERSED: EN 'I heard the gold shop' = Jessica supplied it; SV said someone told her. Was `Jag fick höra talas om guldbutiken.` → now `Jag hörde guldbutiken i det han sa.`. APPLIED.
- [1612] Ch19 'a complaint to land in it' (in that week); 'i tid' = on time. Was `och skrev ett klagomål till länet för att få in det i tid.` → now `och skrev ett klagomål till länet som skulle landa just den veckan.`. APPLIED.
- [1616] Ch19 'saw that flyer early'. Was `flygbladet i tid?` → now `flygbladet i förväg?`. APPLIED.
- [1719] Ch20 agreement: handfatet (neuter) -> det. Was `stod bredvid den i flera år, tills motorn la av, så hon kallade den för Hobart-diskhon` → now `stod bredvid det i flera år, tills motorn la av, så hon kallade det för Hobart-diskhon`. APPLIED.
- [1741] Ch20 'since Harold hung it' = the lock (det), not the gate. Was `sedan Harold hängde upp den.` → now `sedan Harold satte dit det.`. APPLIED.
- [1841] Ch21 licence plate = skylt (as [1828] [1839]). Was `en plåt jag inte läste` → now `en skylt jag inte läste`. APPLIED.
- [1859] Ch21 'the signed tickets' = the driver's ticket (fraktsedel) named in the same line. Was `och de signerade följesedlarna` → now `och de signerade fraktsedlarna`. APPLIED.
- [1866] Ch21 agreement: tefat (neuter). Was `remsa pH-papper i den.` → now `remsa pH-papper i det.`. APPLIED.
- [1969] Ch23 REVERSED: 'unzipping her parka' (she zips it at [2069]). Was `drog upp dragkedjan på parkasen` → now `drog ner dragkedjan på parkasen`. APPLIED.
- [1979] Ch23 attribution: after Tanaka's turn 'sa hon' read as Tanaka (EN 'Joyce said'). Was `"Självklart," sa hon och lutade` → now `"Självklart," sa Joyce och lutade`. APPLIED.
- [1987] Ch23 'rueful'. Was `mot Greta, ångerfullt.` → now `mot Greta, beklagande.`. APPLIED.
- [1993] Ch23 'You signed the ticket' = Ch21's driver's ticket. Was `Du skrev under följesedeln.` → now `Du skrev under fraktsedeln.`. APPLIED.
- [2001] Ch23 'Whoever it was came in through my yard gate' (doubled 'kom in'). Was `"Den som kom in kom in genom min gårdsgrind,"` → now `"Vem det än var så kom den in genom min gårdsgrind,"`. APPLIED.
- [2099] Ch24 agreement: syrningsmedel (neuter). Was `Den förstör bara fel deg.` → now `Det förstör bara fel deg.`. APPLIED.
- [2119] Ch24 singular 'a sleigh runner' = en med ('medar' is plural). Was `bredvid en medar som han` → now `bredvid en med som han`. APPLIED.
- [2127] Ch24 'Did she offer you a coffee' — answer is 'Det gjorde hon inte'. Was `Bjöds det på kaffe den här gången?` → now `Bjöd hon på kaffe den här gången?`. APPLIED.
- [2348] Ch27 porch = veranda (as [928] [564] and Inn Trouble SV 'verandatrappan'). Was `ner för farstubron` → now `nerför verandatrappan`. APPLIED.
- [2361] Ch27 'Greta would have all six ovens going' (supposition, not fact). Was `Nere på Evergreen hade Greta alla sex ugnarna igång` → now `Nere på Evergreen skulle Greta ha alla sex ugnarna igång`. APPLIED.
- [2362] Ch27 penguin 'flippers' = wings. Was `Hon sträckte på simfötterna mot värmen` → now `Hon sträckte ut vingarna mot värmen`. APPLIED.
**Classes:**
- Reversed meaning / who-said-what (4): [1594], [1969], [1979], [2127].
- Mistranslation / wrong word (16).
- Agreement / grammar (7).
- Term drift (6): circle, preserving jar ×2, porch, plate, ticket.
- Tense / mood (2): [108], [2361].
- Typography (1).
- Consistency of a quoted echo (1): [1416].

## Regressions introduced by the first pass
- None found. The changed paragraphs in the 15 chapters I read were checked against the English:
  - the dialogue conversion,
  - the sade→sa change,
  - the term unifications.
- I grepped every settled term's inflected forms (syrningsmedel/-et, kylrum/kallrum, beställningsbok, mjöltunna, bagarrock, lastkaj, handfat, bygdegård, allmänning, polischef). I found no broken agreement and no rename spilling onto another object.
- The 4 defects at [984] [1979] [1993] [2001] sit in paragraphs the first pass touched only for quote marks / `sade` / `Doc`. They are MT text the first pass carried through, so they are misses, not regressions.

## Ledger mismatches
- I sampled 20 random rows of the `_PROOFREAD.md` findings table (the `_APPLIED.md` is a summary only). 19 of them are present verbatim.
- 1 row, #136 [682], reads `sade jag` in the table but `sa jag` in the file. This is explained by the later book-wide sade→sa rule that the same ledger declares. It is not a real mismatch.

## Cross-book follow-up
- **PC-SV-1** (Inn Trouble SV audit): I fixed it here as `dagarna krympte så fort nu`, which is idiomatic, rather than `drog sig ihop`.
- To keep the Inn Trouble excerpt identical, Inn Trouble SV [1667] should get the same change. See PC-FPSV-1.
- **Shared terms vs corrected Inn Trouble SV:**
  - Snowball ✓, `sa` (0 `sade`) ✓, the green = allmänningen ✓.
  - Paddock = `hagen` ✓.
  - Porch: `veranda`, now ×3 (the one `farstubron` is fixed).

## Open first-pass decisions re-checked (PROOFREAD_DECISIONS.md, FP-SV-D1…D5)
- **D1:** the quotes at [829] [1416] [1418] are still accurate (`två grader under normen`).
- **D2:** [977] `fyrtiofem kilo` is accurate.
- **D3:** What's Next and the closing line are still missing, so paragraphs need to be added.
- **D4 and D5:** informational, and still accurate.
- No ruling was undone. No renumbering was done. The units change was logged.

## Decisions added / refusals
- **Added to PROOFCHECK_DECISIONS.md:** PC-FPSV-1 (Inn Trouble excerpt follow-up) and PC-FPSV-2 (a low-priority formatter merge of the split narration "och den andra svarade:" [905]–[911]).
- **Refusals:** 0. All 37 edits matched the complete paragraph text and were applied at `<w:t>` level.

## Four checks (after the fixes)
1. **looks_english:** `[]`.
2. **bt_anchors check:** 7 spans, 0 unpaired: Flour Play, Frost and Found, Inn Trouble, The Binder's Bequest.
3. **check_matter --file:** 1 PASS, 0 FAIL.
4. **preflight --verify:** this check cannot find the raw file in `_superseded/` ("source or corrected copy missing"), so I compared against my backup myself. The results were:
   - paragraphs 2418 → 2418,
   - italic runs 37 → 37, same sequence,
   - `<bt>` 7 → 7,
   - scene breaks 58 → 58.
- **proofcheck.py re-run:** A=0 B=2 (both false positives) C–J=0.

## Verdict
**SIGNIFICANT**, at a rate of 37 real defects over 15 chapters plus matter (≈2.3 per chapter read). Two of them reverse who-did-what:
- Ch19 [1594]: "I heard the gold shop" became "I got told about the gold shop". This undoes the self-correction the deduction depends on.
- Ch23 [1979]: Joyce's "Of course" read as Tanaka's line.

A `full` re-read is recommended for the 12 chapters not read here (Ch4–8, 10, 14–16, 25–27).
