# PROOFCHECK (FULL) — Inn Trouble - ASSEMBLED - FORMATTED_Swedish (2026-10-29, cloud)

- **Mode:** FULL. No sub-agents. Read with python-docx: EN chapter and SV chapter one after the other, sentence by sentence, Ch1 → Ch31, plus the front matter, the blurb, the sell lines, What's Next and the whole Flour Play excerpt [1634]–[1697].
- **Chapters read in full:** 31/31. Ch7 and Ch8 were read together, because the Kapitel 8 heading is missing (IT-SV-1, already logged). Front matter and back matter were also read.
- **Skipped per the run override:** the step-2 diff audit and the 20-row ledger sample, both done in today's targeted pass. Every flag was already judged there (E×3 real and logged, F×1 false, H×2 false, everything else 0), so no flag was left to judge.
- **Backup:** `_proofcheck_backups/Inn Trouble - ASSEMBLED - FORMATTED_Swedish.20261029-020441.full.docx`.

## Today's targeted items
- **"Theo had the theft":** Ch22 [1278] `Han hade stölden`, Ch23 [1310] `Theo hade stölden` and Ch26 [1427] [1431] `Theo hade stölden … Han hade stölden. Du hade köpebrevet.` are all correct (Ch26 was fixed earlier today). Nothing in the book says Theo committed or stole it.
- **The note word `lapp`:** checked in every chapter. The blackmail notes are `lapp(en/arna)`/`utpressningslapp` throughout. The 1924 letters are `brev(en)`, Theo's cards are `kort`, and the deed is `köpebrev`; no two of these share a word. Ch19 card sentences: [1149] `kortet var i Theos hand` was ambiguous (it can mean 'in his hand' = held) and is now `skrivet med Theos handstil` (FIXED). [1151] `hade skrivit de lappar` is the note word, correct.
- **The card `till sin syster`** [1141] is reflexive and correct.
- **Straight double quotes:** the house rule holds everywhere. The only `’…’` are nested quotes, per the dossier.
- **PC-FPSV-F2:** [1627] `låg efter med oljan` → `ligger efter med oljan`. It is a one-word change, and no blurb-tense decision exists for SV (FP-SV-D1…D5 do not cover it). APPLIED. The blurb now matches corrected FP SV [35] word for word.
- **Kapitel 8 heading:** still missing, already logged as IT-SV-1. Not re-raised.
- **MAXIMILIAN `sex bokstäver`** [966] stays faithful to the English, per the override. Not re-logged.

## Lessons checked
- **Spoiler gender, pre-reveal:** every unknown-culprit reference is neutral, e.g. `någon … sin stil` [116], `de` [136], `det de inte hade med att göra` [165], `hen` [973], `De hade just de breven` [1045], `en gestalt` [1250], `ingens blick … på dem` [1236]. The `han/hans` forms at [619], [1007], [1206], [1214] and [1226] mirror the English's own "he/his/the man", so the translation adds no gender the English doesn't have.
- **Short-line pronouns:** Ch19 `Det är kärleken som tillåter det` has the right referent. The reflexives in Ch27 are right: `fördärvat sig själv` [1484] and `sin systers hus` [1480]. One reflexive was wrong: Ch28 [1490] gave Mrs Worthington's coat to her husband (`sin` pointed to him). FIXED.
- **"your man" ≠ "your husband":** Ch18 [1092] had Claire saying `det din man säger`, which reads as 'what your husband says', but the man is Neil Carter. FIXED to `din herr Carter`.
- **Blackburn papers vs deed:** papers = `papper/handlingar`, deed = `köpebrev`. They never share a word.
- **Settled terms:** checked for broken forms after book-wide replacements, including `allmänningen` ×all, `hagen`, `veranda`, `äppelmust`, `Snowball` and `cirkeln`. None found. Two motif terms had drifted:
  - **Hearth:** Ch10 used `härd` ×4, while Ch14/19/30/31 use `eldstad` ×13. Ch19's "A hearth," I said → `En eldstad` echoes Nick's Ch10 line, so Ch10 was unified to `eldstad`.
  - **"precious":** Ch13 had `skör` and Ch16 had `ömtåligt`; both are now `dyrbar(t)`.
- **Excerpt:** read line by line against Inn Trouble's own English and FP SV Ch1. It has seven/eight women, `choklad- och pekannötsmuffins`, `Stod inte barnens snögubbar vända mot vägen i går?`, `Så gott som.`, the bandstand/war memorial and `dagarna krympte`, and no half-paragraph is dropped. The only change was the typo `novembres` → `novembers` [1634], which FP SV [40] shares (follow-up PC-SVF-1).

## Missed by the first pass (fixed here)
62 edits in 55 paragraphs. All are one-answer edits on `<w:t>` text only, and the italic run at [800] was kept.

| Para | Ch | Swedish (before) | After | Class / why |
|---|---|---|---|---|
| 38 | Ch1 | `trygg i ett varmt kök en koldag.` | `trygg i ett varmt kök en kall dag.` | typo koldag = 'cold day' |
| 38 | Ch1 | `Jag hade lagt till det åt henne på det sättet alltsedan dess.` | `Jag hade bakat den åt henne på det sättet alltsedan dess.` | 'I'd made it that way' mistranslated as 'added it' |
| 51 | Ch1 | `som inte pudret hade döljt` | `som inte pudret hade dolt` | participle dolt |
| 76 | Ch1 | `jag litade på det ungefär lika mycket som jag skulle ha kunnat kasta gnistskyddet` | `jag litade på det ungefär lika långt som jag hade kunnat kasta gnistskyddet` | idiom 'as far as I could throw' |
| 116 | Ch2 | `Femhundra tusen dollar.` | `Femhundratusen dollar.` | number spelling (one word) |
| 120 | Ch2 | `blicken mötte kameran rakt på sak med` | `blicken mötte kameran rakt på med` | 'rakt på sak' (=to the point) for 'straight on' |
| 141 | Ch2 | `Femhundra tusen dollar.` | `Femhundratusen dollar.` | number spelling |
| 171 | Ch3 | `gnolad på något` | `gnolat på något` | supine |
| 191 | Ch3 | `medan lamporna blev gula av sig själva` | `medan lamporna blev gyllene av sig själva` | gold, not yellow (gyllene/guld elsewhere) |
| 310 | Ch5 | `Inte när festivalen är framflyttad till nästa helg.` | `Inte när festivalen är tidigarelagd till nästa helg.` | 'moved up' = brought forward; framflyttad reads as postponed |
| 311 | Ch5 | `"Den är inte framflyttad,"` | `"Den är inte tidigarelagd,"` | same |
| 359 | Ch5 | `Fem hundra tusen dollar, krävda` | `Femhundratusen dollar, krävda` | number spelling |
| 360 | Ch5 | `vem som helst annan i världen` | `vem som helst annars i världen` | grammar |
| 375 | Ch6 | `om att få fråga om pingvinen kom till festivalen` | `om att jag skulle fråga om pingvinen skulle komma till festivalen` | who asks: Emma wants Mark to ask |
| 393 | Ch6 | `den timmen sedan Pip hade slitit upp den` | `under den timme som gått sedan Pip hade slitit upp den` | 'in the hour since' |
| 415 | Ch7 | `saktade hon in och kände efter.` | `saktade hon in och smakade.` | 'slowed and tasted' (tasting is the point) |
| 478 | Ch8 | `att hålla kolet i min öppna hand och inte knyta näven om det` | `att hålla glöden i min öppna hand och inte knyta näven om den` | coal motif = glöd as Ch5 [334] |
| 538 | Ch8 | `eller burits i en ficka` | `eller bars i en ficka` | parallel tense |
| 577 | Ch9 | `"Släktutredningar. Det är mitt yrke` | `"Dödsboutredningar. Det är mitt yrke` | 'Estate research', not genealogy |
| 650 | Ch10 | `äter opp det goda kålet` | `äter opp den goda kålen` | kål is common gender |
| 667 | Ch10 | `En härd som den hade nött slät` | `En eldstad som den hade nött slät` | hearth = eldstad (book majority: Ch14/19/30/31, and Ch19 'En eldstad' echoes Nick's line) |
| 667 | Ch10 | `Och här har den ingen härd.` | `Och här har den ingen eldstad.` | hearth unify |
| 672 | Ch10 | `En härd. Så att den slutar` | `En eldstad. Så att den slutar` | hearth unify |
| 681 | Ch10 | `byggde min man en härd för en hemlös magi` | `byggde min man en eldstad för en hemlös magi` | hearth unify |
| 685 | Ch11 | `stod den nuvarande borgmästarens dörr på glänt` | `stod den nuvarande borgmästarens dörr öppen` | EN 'stood open' (his 'open door' twice later) |
| 717 | Ch11 | `drev det arkiv dit breven hade försvunnit` | `drev det arkiv där breven hade försvunnit` | grammar |
| 790 | Ch13 | `Sams tjugodollarsedel` | `Sams tjugo dollar` | a debt, not a banknote |
| 800 | Ch13 | `den där är skör` | `den där är dyrbar` | 'precious' (italic run) |
| 800 | Ch13 | `bar den sköra lådan dit` | `bar den dyrbara lådan dit` | precious |
| 800 | Ch13 | `efter nästa sköra låda` | `efter nästa dyrbara låda` | precious |
| 806 | Ch13 | `broschen, stenen, pantlåneaffären` | `broschen, stenen, pantbanken` | term = pantbanken |
| 824 | Ch13 | `Han var fri.` | `Han var utom misstanke.` | 'He was clear' |
| 900 | Ch15 | `som finns där i,` | `som finns där inne,` | broken 'där i' (as [1116]) |
| 904 | Ch15 | `från sin campingstol` | `från sin fällstol` | = Ch14 fällstol |
| 916 | Ch15 | `Jag satt igenom två timmar av det.` | `Jag satt där i två timmar.` | calque 'sat through' |
| 979 | Ch16 | `’försiktigt, det där är ömtåligt’` | `’försiktigt, det där är dyrbart’` | 'that's precious' = Ch13 |
| 1011 | Ch16 | `Han kan hemligheten,` | `Han känner till hemligheten,` | wording |
| 1092 | Ch18 | `gör det din man säger att det gör` | `gör det din herr Carter säger att det gör` | 'your man' = Neil Carter, NOT 'your husband' (din man) |
| 1120 | Ch18 | `som Fiona hade nästan tagit död på sig själv` | `som Fiona nästan hade tagit död på sig själv` | word order (subordinate clause) |
| 1149 | Ch19 | `Och kortet var i Theos hand.` | `Och kortet var skrivet med Theos handstil.` | 'in Theo's hand' = handwriting (ambiguous 'i hans hand') |
| 1232 | Ch20 | `vilkas händer de breven hade passerat igenom` | `vems händer de breven hade passerat igenom` | 'whose hands' (one person; plural vilkas pre-empts 'how many hands') |
| 1245 | Ch21 | `De långbord som vi hade burit ut` | `De bockbord som vi hade burit ut` | trestle tables = bockbord (Ch6/Ch20) |
| 1245 | Ch21 | `hundra burkar inlagda grönsaker` | `hundra burkar sylt och marmelad` | 'preserves' ≠ pickled vegetables |
| 1259 | Ch21 | `och guldlyktorna kom till sin rätt` | `och de gyllene festivalljusen kom till sin rätt` | 'gold festival lights' (lyktor = the lanterns in the trees) |
| 1296 | Ch23 | `Hon hade haft framme det.` | `Hon hade haft det framme.` | word order |
| 1347 | Ch24 | `"Det är den svåraste vägen,"` | `"Det är den svårare vägen,"` | comparative 'the harder road' |
| 1445 | Ch26 | `som satt nu i ruinerna` | `som nu satt i ruinerna` | word order (subordinate clause) |
| 1456 | Ch27 | `bad om upprättelse snarare än ruin` | `bad om gottgörelse snarare än ruin` | 'mending' (upprättelse = vindication) |
| 1462 | Ch27 | `Det var jag som hade ställt till det.` | `Det var jag som hade orsakat det.` | 'I had brought it about' (ställa till = mess up) |
| 1474 | Ch27 | `svårare än en förlåtelse och långt bättre` | `svårare än en benådning och långt bättre` | 'pardon' = benådning as [1456] |
| 1490 | Ch28 | `med sin fru vid sin sida i krämfärgad kashmir och med sin fina kappa över armen,` | `med sin fru vid sin sida, hon i krämfärgad kashmir och med sin fina kappa över armen,` | the coat is the WIFE's (reflexive sin pointed to him) |
| 1497 | Ch28 | `att räddningen av sällskapet helgade medlen,` | `att räddningen av sällskapet rättfärdigade vad som helst,` | 'justified anything' (avoid medlen twice) |
| 1497 | Ch28 | `att slutet skulle ursäkta medlen` | `att målet skulle ursäkta medlen` | 'the end' = goal, not ending |
| 1511 | Ch29 | `Jag trodde att Fiona ville begrava` | `Jag trodde att Fiona skulle vilja begrava` | 'would want' |
| 1525 | Ch29 | `som hade kämpat, misstagit sig och uthärdat` | `som hade kämpat, felat och uthärdat` | 'erred' |
| 1535 | Ch29 | `Jag hade stålsatt mig för att bli outsidern som krossade` | `Jag hade stålsatt mig för att bli den utomstående som krossade` | = Ch24 'den utomstående' |
| 1535 | Ch29 | `att staden skulle svalna mot mig, att önska att jag hade låtit det bero, att komma ihåg,` | `att staden skulle svalna mot mig, önska att jag hade låtit det bero, komma ihåg,` | broken parallel after 'skulle' |
| 1537 | Ch29 | `en burk med sina inlagda frukter` | `en burk med sin hemkokta sylt` | 'preserves' (= Ch21 sylt) |
| 1582 | Ch31 | `"Det är hela staden också,"` | `"Det kommer hela staden att vara också,"` | 'So's the whole town' (= will be impossible too) |
| 1591 | Ch31 | `kvisten från pumpan, stående i några centimeters vatten` | `kvisten från pumpan, i några centimeters vatten` | stod … stående |
| 1627 | What's | `familjen som låg efter med oljan` | `familjen som ligger efter med oljan` | Next blurb present tense = FP SV [35] (PC-FPSV-F2) |
| 1634 | Excerpt | `novembres första lediga morgon` | `novembers första lediga morgon` | typo (FP SV [40] has the same typo → follow-up) |
**Most material:**
- [1092] `din man` (husband) for Neil Carter.
- [1490] the wife's coat given to the husband.
- [375] who asks: Emma wanted her father to ask Jessica.
- [310]/[311] `framflyttad`, which reads as 'postponed' for "moved up".
- [577] `Släktutredningar` (genealogy) for "estate research".
- [38] 'I'd made it that way' rendered as `lagt till det` ('added it').
- [1245]/[1537] preserves rendered as pickles.
- [1259] the gold festival lights rendered as `guldlyktorna` (lanterns).

None of these touches the clue chain.

## Regressions introduced by the first pass
| Para | Ch | Raw | First pass | Now |
|---|---|---|---|---|
| 360 | 5 | `vem som helst annars i världen` (correct) | `vem som helst annan i världen` | `vem som helst annars` (restored) |

Inherited, not regressions: [1627] `låg` and [1634] `novembres` came in verbatim with the FP SV copy, and FP [35] was itself fixed today. No other first-pass edit was found to be wrong during the full read.

## Ledger mismatches
None. The targeted pass confirmed all 539, and this pass has no new APPLIED claims to check.

## Decisions added / refusals
- PROOFCHECK_DECISIONS.md, section "Inn Trouble - ASSEMBLED - FORMATTED_Swedish — FULL PROOFCHECK (2026-10-29)": PC-SVF-1 (informational, FP SV [40] `novembres` typo follow-up).
- Refusals: 1. The [800] three-span edit crossed the italic boundary, so it was refused and then re-applied as three separate spans, with the italic kept.

## Checks (after fixes)
1. looks_english: `[]`
2. bt_anchors check: 8 spans, 0 unpaired (Inn Trouble / Frost and Found / Flour Play only).
3. check_matter: 1 PASS 0 FAIL.
4. preflight --verify (raw→corrected): 1698→1698 ok, scene breaks 3→3 ok. The italic/bt FAIL is the first pass's declared changes, unchanged since the targeted report.
   - Own comparison, full backup vs now: 1698 = 1698 paragraphs. 24 = 24 italic runs in the same order, and the only italic text that changed is [800] (`skör` → `dyrbar`). 8 = 8 `<bt>`. 3 = 3 `***`. 55 paragraphs changed, exactly those listed above.
- proofcheck.py re-run: A=0 B=0 C=0 D=0 E=3 F=1 G=0 H=2 I=0 J=0. The flags are unchanged, and all were judged in the targeted pass.

## Verdict
**MINOR.**
- The plot chain (clue phrase, note/letters/cards/deed words, the two-halves deduction, Sam owed) was already sound after the targeted pass and traces clean in every chapter.
- The full read found no omission and no reversal on the clue chain. It found 62 one-answer defects: mistranslations, two who/whose slips ([1092], [1490]), a who-asks slip ([375]), agreement, word order, motif drift and one first-pass regression.
- Rate: 62 edits / 33 units read (31 chapters + front + back) ≈ 1.9 per chapter.
