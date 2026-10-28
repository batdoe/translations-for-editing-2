# PROOFCHECK (FULL) — Inn Trouble - ASSEMBLED - FORMATTED_Dutch (2026-10-28)

- **Mode:** FULL — sentence-by-sentence bilingual read (EN paragraph next to NL paragraph, in order) of front matter, blurb, Ch1–Ch31, sell lines, What's Next? and the Flour Play excerpt. This follows the targeted pass of the same day (`…_PROOFCHECK.md`, 8 fixes).
- **Files:** `translated/corrected/Inn Trouble - ASSEMBLED - FORMATTED_Dutch.docx` (edited in place). English: `translate_now/Inn Trouble - ASSEMBLED - FORMATTED.docx`. Raw (read-only, to classify each defect): `_superseded/…_Dutch.docx`.
- **Backup:** `_EditLedgers/_proofcheck_backups/Inn Trouble - ASSEMBLED - FORMATTED_Dutch.20261028-230831.full.docx`.
- **Chapters read in full:** 31 of 31, plus front matter, blurb and all back matter.
- **Skipped per the brief:** the step-2 diff audit and the 20-row ledger sample (done in the targeted pass).
- **Flags (step 1):** the re-run shows A=0 B=2 C=0 D=0 E=0 F=0 G=0 H=3 I=0 J=0, the same 5 flags the targeted report already judged as false positives. No flag was left unjudged.

## Missed by the first pass (all 20 paragraphs were present in the raw file, so these are misses, not regressions) — all APPLIED

| Para | Ch | Dutch (was) | English | Class | Fix |
|---|---|---|---|---|---|
| 177 | 2 | `om zijn handschrift te verhullen` | "working hard to disguise their hand" | spoiler-gender (the raw file had `haar`, the first pass made it `zijn`; both give the unknown writer a sex) | `om het eigen handschrift te verhullen` |
| 292 | 3 | `om zijn hand te sluiten om de keel` | "close a hand around a good woman's throat" | spoiler-gender | `om een hand te sluiten om de keel` |
| 331 | 4 | `Er kwam net iemand bij de appelsaptafel` | "A man came up to me at the cider table" | omission | `Er kwam net een man …` |
| 439 | 6 | `een pompoen die hem had beledigd` | "a gourd that had offended him" | term (gourd = `kalebas`, as at [409] and [433]) | `een kalebas …` |
| 522 | 8 | `de lampenarmen` | "the lamp brackets" | term drift (Ch1 [61] has `lantaarnbeugels`) | `de lantaarnbeugels` |
| 548 | 8 | `…in die lobby gestopt, weet je.` | Sam → Jessica | register (Sam says `u` / `mevrouw Claus`) | `weet u.` |
| 554 | 8 | `En dat je zo oprecht…` | Jessica → Sam | register (the same speech has `Dank u wel, Sam`) | `En dat u zo oprecht…` |
| 707 | 12 | `Ik nam het hem niet in dank af.` | "I didn't forgive it." | mistranslation (*niet in dank afnemen* = to resent) | `Ik vergaf het niet.` |
| 887 | 16 | `de akten en de eigendomsregisters` | "the deeds and the property records" | term drift (Ch11 [673] and [684] have `vastgoedregisters`) | `…de vastgoedregisters` |
| 900 | 17 | `de laatste ijzeren steunen` | "the last of the iron brackets" | term drift (porch brackets = `(veranda)beugels`) | `ijzeren beugels` |
| 920 | 17 | `Fiona’s receptie hing er vol mee` · `de steunen die op de veranda…` | "Fiona's lobby was full of it … the brackets going up on the porch" | mistranslation (lobby ≠ reception desk) and term drift | `Fiona’s lobby` · `de beugels` |
| 926 | 17 | `bij zijn steunen` | "to his brackets" | term drift | `bij zijn beugels` |
| 941 | 18 | `Wie uw vriendin ook aan het leegbloeden is` | "Whoever's bleeding your friend" | mistranslation (*leegbloeden* is intransitive, "to bleed out", so the sentence was garbled) | `…aan het uitzuigen is` |
| 968 | 19 | card: `verpand bij Ridgeline` | "pawned at Ridgeline" (a town) | wording, on the clue card | `verpand in Ridgeline` (italic run kept) |
| 1080 | 21 | `U deed net alsof u mevrouw Pelletier wilde tackelen` | "You looked like you were going to tackle" | mistranslation (*deed alsof* = pretended) | `U zag eruit alsof u…` |
| 1268 | 26 | `Dat is een eigendomsregister.` | "That's a property record." | term drift in the deduction (Ch22 [1112] has `Dat was een vastgoeddossier.`) | `Dat is een vastgoeddossier.` |
| 1274 | 26 | `Niemand had naar hen gegrepen vanuit de duisternis.` | "No one had reached out of the dark." | mistranslation (adds an object and loses the echo of the trap's hand) | `Niemand had vanuit de duisternis een hand uitgestoken.` |
| 1295 | 27 | `Je kon als man geen buurman proberen af te persen` | "A man could not extort a neighbor" | gender (the neighbour is Fiona) | `Een man kon geen buurvrouw proberen af te persen` |
| 1307 | 27 | `De weg terug is lang voor u.` | "The road back is long for you too." | omission ("too") | `De weg terug is ook voor u lang.` |
| 1548 | excerpt | `‘Iemands stomme grap,’` | "Somebody's idea of a joke," | added word ("stupid") | `‘Iemands grapje,’` |

These are 21 edits in 20 paragraphs. All 21 matched once inside a single `<w:t>`, so there were **0 refusals**.

## Regressions introduced by the first pass
None. Every defect above is already in the raw file.

Para [177] needs a note. The raw file's `haar handschrift` would have revealed the sex before the reveal. The first pass changed it to `zijn`, which is the generic masculine but still gendered. It is now neutral.

## Spoiler-gender check (whole book, before the Ch26 reveal)
- **Where the English is neutral, the Dutch now is too:** `iemand` / `degene` / `die` / `wie … ook` / `de gestalte` / `ze` (plural). This covers [177], [197], [240], [292], [365], [402]–[403], [974], [1063], [1078] and [1077].
- **Where the English itself says "he"** (Ch9 [591], Ch16 [885], Ch20 [1035]–[1053], Ch21 [1088]), the Dutch `hij` follows the source. That is not a defect.
- **`de afperser`** is the generic noun, the same as English "blackmailer". It was left as is.

## Clue chain (re-traced in the full read)
- **Clue phrase:** `de saffier in haar hart` is identical in the note [177], the readings [178] and [195], the card [968] and [970], [972], the recap [1100], Ch23 [1151] and Ch26 [1258]. It is 5 words, so every "vijf woorden" line is true.
- **Note vs letters:** the note family is always `briefje(s)`; the 1924 letters are always `brieven`; the index card is `kaartje` / `cataloguskaart(je)`. Ch19 [976] `En het kaartje was van Theo’s hand` (card, not note) is correct.
- **The theft and the deed:** "Theo had the theft" reads `Hij had het geheim van de diefstal` [1116], `Theo had het geheim van de diefstal` [1151], and `Theo wist van de diefstal` / `Hij had het geheim van de diefstal` [1268]. None of these says "he committed it". The deed is `akte` throughout, kept apart from the Blackburn letters (`brieven`).
- **"to his sister" [968]:** `aan haar zuster` is correct, because the writer is Adelaide.
- **Ch19 Nick [992]:** `Het is de liefde die het hem toestaat` is correct.
- **Ch27 [1313]:** the "ruined himself" fix from the targeted pass is present.
- **Other terms:** Sam is owed (blurb [34] `nog twintig dollar tegoed had`), cider = `appelsap` (0 × "cider"), Snowball ×12, porch = `veranda`, green = `brink`, paddock = `weide` (all 9 occurrences are the paddock). There is no "your man → husband" confusion; [932] renders it as `Carter`.

## Excerpt (PC-FIL2-1 policy, not re-raised)
The excerpt follows Inn Trouble's own English:
- `Nagenoeg wel`;
- `chocolade-pecan…` / `pecannoten`;
- the snowmen question is not inverted [1538];
- the "eight women" and "seven women" figures follow the English;
- the war memorial and bandstand appear only where the English has them.

The only change in this pass was [1548].

## Decisions added
In `PROOFCHECK_DECISIONS.md`, section `## Inn Trouble - ASSEMBLED - FORMATTED_Dutch — FULL PROOFCHECK (2026-10-28)`:
- **PC-NL2F-1:** Ch14 paragraph split [799] / [801] (informational, formatter).
- **PC-NL2F-2:** English-source arithmetic, "six letters" at [870] (MAXIMILIAN − MAX = 7).

## Four checks (after the fixes)
1. **looks_english:** `[]`.
2. **bt_anchors check:** 4 spans, 0 unpaired. The spans are Inn Trouble ×2, Frost and Found and Flour Play.
3. **check_matter --file:** 1 PASS, 0 FAIL.
4. **preflight --verify:** it reported "source or corrected copy missing" because the raw file is in `_superseded/`. I compared the corrected file with the backup by hand:
   - paragraphs 1567 → 1567;
   - italic runs 23 → 23, same order. The only text change inside an italic run is at [968], on the card;
   - `<bt>` 4 → 4;
   - scene breaks [996, 1446, 1462, 1564] unchanged;
   - the changed paragraphs are exactly the 20 listed above.

**proofcheck.py re-run:** A=0 B=2 C=0 D=0 E=0 F=0 G=0 H=3 I=0 J=0, unchanged. The remaining 5 flags are the false positives already judged.

## Verdict
**MINOR.** No plot-chain, omission-of-substance or reversed-deduction defect remained. The clue chain, the note / letters / card split, the theft / deed halves and the reflexive and pronoun checks are all sound.
- **What was missed:** two spoiler-gender possessives, a mistranslation that masculinised Fiona ([1295] `buurman`), five small mistranslations, two small omissions, two register slips and seven term drifts.
- **Rate:** 21 real defects over 33 sections read in full (31 chapters plus front matter and back matter), about 0.6 per section.
- **Worst miss:** [1295] `Je kon als man geen buurman proberen af te persen`. It made Fiona, the victim, a man. A close second is the garbled [941] `aan het leegbloeden`.
