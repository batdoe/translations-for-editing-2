# PROOFREAD — Inn Trouble - ASSEMBLED - FORMATTED_Swedish (2026-10-27, cloud run)

- Edition: Swedish, Frost Falls Book 2. Input `translated\Inn Trouble - ASSEMBLED - FORMATTED_Swedish.docx` (raw MT, never proofread). English: `translate_now\Inn Trouble - ASSEMBLED - FORMATTED.docx`. Output: `translated\corrected\Inn Trouble - ASSEMBLED - FORMATTED_Swedish.docx`, edited in place on top of the mechanical sweep (2 Markdown asterisk spans → italics); a pre-proofread backup of that file was kept in the session scratch dir.
- Prior report: none (0/0 not found).
- Rules: dossier swedish.txt (STRAIGHT double quotes "…", nested ’…’, preteritum); Lisa's rulings 1–7 (FF_DECISIONS_BRIEF_20261013); FF_PROOFREAD_BRIEF_20261026 incl. every Lesson. Series sources: corrected Flour Play SV (+ its ledgers: du for everyone, sa not sade, herr/fru, allmänningen, staden, cirkeln, Snowball) and Frost and Found SV (raw).
- Coverage: front matter, blurb, Ch 1–31, What's Next, Flour Play excerpt, sell lines. Every chapter read against the English, sequentially, no sub-agents. Paragraph numbers = python-docx `document.paragraphs` index.
- Paragraph gap +193 (pre-flight): the MT split ~190 English paragraphs at speech/narration boundaries (Ch4, 5, 7/8, 9, 11, 13–18, 25, 26, 28, 29, 31) and put an empty paragraph between every paragraph in 18 chapters (569 empties). No duplicated paragraphs, no English twins, no translator notes found. Splits kept (paragraph count must not change).
- Kapitel 8: heading line missing, BODY PRESENT — SV [456]–[554] = EN [358]–[386], complete; [455] (last line of Ch7) runs straight into [456]. Formatter/Lisa (IT-SV-1). 'dup=[31]' = the TOC's lone 'Kapitel 31' line.

## Worst defects
1. **The note and the 1924 letters shared one word — the Ch19/22/26 deduction collapsed.** The note was `lappen` in Ch1–2 but `brevet`/`breven`/`utpressningsbrevet` from Ch3 on (≈50 places), e.g. Ch22 [1276] `Brevet visste inte bara att broschen var stulen … fanns inte i något av Blackburns brev`, [1279] `Theo kunde inte ha burit breven till värdshuset`, Ch23 [1310], Ch26 [1427] `Men breven visste att värdshuset köptes … det stod aldrig i något Blackburnbrev`. Now note = **lapp/lappen/lapparna** everywhere (also Fiona's 'mail' = `post`, decoy 'envelope' = `kuvert`, Martha's card note kept `lapp`), 1924 letters = **brev**.
2. **Clue phrase in three forms + left in English.** Note/Ch2 `safiren i sitt hjärta`; Theo's card Ch19 [1141] [1143] [1145] `safiren i dess mitt` (= at its centre — the match the whole deduction rests on was broken); Ch22 [1270] English inside a stray `<bt>the sapphire at its heart</bt>`; Ch26 [1401] literal `<it>safiren i dess hjärta</it>` markup. Now **"safiren i dess hjärta"** at all 9 places; "five words" → "fyra ord" ×5 (IT-SV-2).
3. **Blurb made Sam the debtor** [34] `En smed som var skyldig tjugo dollar` → `som hade tjugo dollar att fordra`; blurb also `i morgon` for 'this morning', `Brevet` for the note.
4. **Dialogue system:** 440 dash-turn paragraphs (often without a dash for resumed speech) + 22 « » + 6 ”…” paragraphs. 457 paragraphs converted to straight quotes, each against the English; attribution comma inside the quote ("…," sa hon); `sade` → `sa` ×97.
5. **Reversed / wrong meanings (sample):** [135] 'Untouched' → `Rörda` (touched); [334] [361] 'kept my fist open' → `höll handen knuten` ×2; [310] 'not unhappily' → `inte utan ett visst missnöje`; [460] 'I didn't hurry him' → `jag skyndade på honom`; [1443] 'the not-sleeping' → `på att få sova`; [1456] 'nor a free pardon' → `ovillkorlig dom`; [1108] 'unasked' → `ombedd eller ej`; [1491] 'this morning' → `i morgon bitti`; speaker errors [1256] [1258] [1263] (Jessica's lines given to Noriko/Fiona); [1431] `Hon behövde` (Theo); sign `SKÖTESTÄLLEN` (changing tables) for DEEDS [696]; `vindsresåren` (attic elastic) for the attic trunk [1335]; `polpuln` [1335]; `vargtimme` for a knitting session [896]; `glasronn` for the glass pear [84].
6. **English left in:** Ch22 note quotation `I know how your family came by this inn` [1276], the clue in `<bt>` [1270], file tab `PROPERTY` [1292], `Frost Falls Historical Society` [1466], three sell lines [1622] [1632] [1697], Ch19 index card `Bunting`.

## Clue chain — one rendering each
- the note = **lappen** (utpressningslappen); the 1924 letters = **breven** (Blackburnbreven); clue phrase = **safiren i dess hjärta** (4 words; IT-SV-2); the deed = **köpebrevet** (Ch23 had `lagfartsbrev` ×7, Ch16 `skötebrev`, Ch22 `skötehandling`, Ch24 `skötebrev`, Ch25 `fastighetsbrev`, Ch26 `lagfart`) — drawer label KÖPEBREV [696]; the refile basket = **återarkiveringskorgen**; the laid lines = **räfflade**; the trunk = **kofferten** (`kista` ×4); 'gone astray' = **kommit på villovägar** (MT also `på avvägar`, `på drift`); the boiler = **pannan**; the light holder = **ljushållaren**; the porch brackets = **verandakonsolerna** (`järnhyllorna`, `verandafästena`, `hyllorna`); fire screen = **gnistskyddet**; parking passes = **parkeringstillstånd**; Vera's 'town wage for a city's work' echoed identically Ch11/Ch23.
- 'two sets of hands' (Ch22–26): the note-carrying / deed half now reads cleanly (lapparna vs breven) in [1275] [1279] [1310] [1312] [1427] [1431].

## Lessons checklist
- Note vs letters: fixed (worst defect 1). Ch19 [1145], Ch22, Ch26 checked against the English.
- Clue phrase identical ×9, word count true (IT-SV-2).
- Units (SAFE): 'an inch from a glass pear' → ett par centimeter [84]; 'a final quarter-inch' → en halv centimeter [299]; 'four acres' → drygt ett och ett halvt hektar [1561] (MT `fyra tunnland`); figurative inches → bit för bit / ett steg [203] [654] [790] [1314] [1349]×2 [1468] [1606] [1614]. Already metric in MT: four inches = en decimeter [42], six inches = 15 cm (excerpt), six feet = två meter [704], a few yards = ett par meter [1251]. 'Fifty miles' = `fem mils avstånd` [124] left (ruling 4). Kept as native idioms: `inte ett uns hyfs` [368], `varje uns av den träningen` [1145], `satt min fot i`.
- Currency: öre → cent ×4 ([331] 'one thin dime', [433], [486], [1165]); [1011] neutral `slant` kept; no öre/krona left.
- Snowball = Snowball (Snöboll ×4 fixed). Pip she/her throughout (checked). Jessica's forms feminine (checked).
- Circle = **cirkeln** (MT `syföreningen` [99], `föreningens vantar` [1245], `ringen` ×7 in Ch29, excerpt `ringen` ×9 — replaced from FP).
- Reindeer: Dancer, Prancer, Vixen, Comet (= Frost and Found SV); MT `Komet` [388], `Dansö` ×3 fixed. Elf = **alv** (MT `tomtenisse` ×2 for Bram).
- Reversed meanings checked: blurb debtor (fixed); excerpt 'Very nearly' = "Så gott som." [1641].
- Title page already `<bt>Inn Trouble</bt>`; 'Bok 2', 'Andra upplagan' kept.
- Narrative tense: preteritum in every chapter (checked); blurb present as in the English.
- Term variants: town = staden/stan (Ch3 `samhället` ×9, `byn` ×1 fixed; `två samhällen bort` kept = 'two towns over'); the green = **allmänningen** (`parken` ×3, `grönområdet` ×6, `bytorget` ×3, `byplanen` ×2, `torget` ×4 when it meant the green, `gräset`, `gräsplanen`, `det gröna`); the park kept `parken` where EN says park [87]; porch = veranda; Historical Society = **Historiska sällskapet** (`Hembygdsföreningen` ×3, `hembygdsgården` ×2, `föreningen` ×8; IT-SV-5); Mr./Mrs. → herr/fru (18 places); the Gazette = Gazette.
- Cider (ruling 6): `cider` ×11 → **äppelmust** (mustbordet, mustståndet).
- Gendered/foreign leaks: none found; 'hen' left in two narration lines ([415] [973]).

## Address table (ruling 2 — Swedish series rule, FP-SV-D5)
**du for everyone** (as corrected Flour Play SV), titles carry the register (fru Claus, herr Worthington, herr Carter). Singular ni/er → du in: Neil → Jessica [76] [81] [239]; Emma → Jessica [366]; Noriko → Jessica [386]; Sam ↔ Jessica (Ch8 [468] [472] [480] [518] [532] [542]); mayor → Jessica [693]; Jessica → Vera [1427]; Vera generic 'you' [1439]. Plural ni/er kept (Fiona to the Worthingtons, Theo/Noriko to groups, Dot/Greta to the circle, Bram to everyone).

## Dialogue (ruling 1)
Straight double quotes per turn; attribution after a comma inside the closing quote; resumed speech re-opened; narration interrupts outside the quotes; quoted words in narration "…"; nested ’…’ [979]. 457 paragraphs converted (dash turns, « », ”…”); no dash-opened turn and no odd quote count left in the body.

## Stray `<bt>` (ruling 5)
Removed 3: [833] `<bt>The Holly Jolly Bakery</bt>` → Holly Jolly Bakery (the edition's form, Ch21/excerpt), [833] `<bt>Frost Falls</bt>` → Frost Falls, [1270] `<bt>the sapphire at its heart</bt>` → Safiren i dess hjärta. Added 2 real-title anchors (series list [18] [19], as Flour Play SV). Result 8 spans: Inn Trouble, Frost and Found, Flour Play; 0 unpaired.

## Back matter
- What's Next [1623]–[1628] present (Flour Play's What's Next was the missing one); blurb [1624]–[1628] copied verbatim from corrected Flour Play SV [29]–[37] (EN identical).
- Sell lines [1622] [1632] and closing line [1697] were in English → `Fler mysterier väntar Jessica Claus! <bt>Flour Play</bt> kommer snart.` / `<bt>Flour Play</bt> kommer snart!` (italics kept).
- Excerpt [1634]–[1693] (60 paragraphs, this file's splits kept): rebuilt from corrected Flour Play SV Ch1 [40]–[158]: 34 copied verbatim where the English is identical, 21 adapted where this excerpt's English is the older draft (bandstand/war memorial, 'widow these many years', 'volunteered … three days a week', 'Over the weekend', no 'said Dot' + 'by Sunday, mark me', present-tense 'I know the difference', the extra sentences 'And I didn't say what I was thinking', '…a nose for what mattered before I did', 'Something was starting', 'cool prickle at the back of my neck'); 5 already matched after the dialogue conversion. IT-SV-3.

## Formatter's job (ruling 7) — not changed
No Heading 1; TOC [21]–[26] lists only 'Kapitel 31'; Kapitel 8 heading missing (IT-SV-1); empty paragraphs between paragraphs in 18 chapters; split paragraphs; `***` [1620] [1630] [1695] back-matter separators (scene breaks 3 = 3).

## Findings (Swedish verbatim as found; para = document index; ALL APPLIED)
Book-wide rules are listed after the table; the 457 dialogue conversions are listed by paragraph at the end.

| # | Para | Class | Swedish (before) | Why (English) | Corrected |
|---|---|---|---|---|---|
| 1 | 8 | Ruling 7 copyright | Copyright © 2026 av Lisa Bouchard. | copyright line matched to Flour Play SV (EN has no ©) | Copyright 2026 av Lisa Bouchard. |
| 2 | 12 | Ruling 7 copyright | Eftertryck förbjudet. | rights line matched to Flour Play SV | Alla rättigheter förbehållna. |
| 3 | 14 | Ruling 7 copyright | Ingen del av denna publikation får reproduceras, distribueras eller överföras i någon form eller på något sätt, inklusive fotokopiering, inspelning eller andra elektroniska eller mekaniska metoder, utan skriftligt tillstånd i förväg från förlaget, utom i den u … | rights paragraph matched to Flour Play SV verbatim (same EN) | Ingen del av denna publikation får reproduceras, distribueras eller överföras i någon form eller på något sätt, inklusive fotokopiering, inspelning eller andra elektroniska eller mekaniska metoder, utan föregående skriftligt tillstånd från förlaget, utom i den … |
| 4 | 16 | Ruling 7 / 3 Mistranslation | Verket, samtliga namn, karaktärer och händelser som skildras i denna produktion är fiktiva. Ingen likhet med verkliga personer (levande eller avlidna), platser, byggnader och produkter är avsedd eller bör inläsas. | disclaimer matched to Flour Play SV verbatim (MT "bör inläsas" = should be read in) | Berättelsen, alla namn, karaktärer och händelser som skildras i detta verk är fiktiva. Ingen koppling till verkliga personer (levande eller avlidna), platser, byggnader och produkter är avsedd eller bör antas. |
| 5 | 18 | Ruling 5 anchor | Frost and Found | series-page title anchored, as Flour Play SV [16] | <bt>Frost and Found</bt> |
| 6 | 19 | Ruling 5 anchor | Inn Trouble | series-page title anchored, as Flour Play SV [17] | <bt>Inn Trouble</bt> |
| 7 | 30 | 3 Mistranslation | har värmt halva Frost Falls vid det här laget. | EN 'at one time or another' | har värmt halva Frost Falls vid ett eller annat tillfälle. |
| 8 | 30 | 3 Mistranslation | och i morgon har hon knäppt koftan fel | EN 'this morning'; MT 'tomorrow' | och i morse har hon knäppt koftan fel |
| 9 | 32 | Note vs letters | Brevet kräver en halv miljon dollar. Det vet vad | EN 'The note demands'; note = lapp | Lappen kräver en halv miljon dollar. Den vet vad |
| 10 | 32 | Note vs letters | och det nämner stenen i broschens hjärta | pronoun for lappen (descriptive phrase, not the quoted clue — as EN) | och den nämner stenen i broschens hjärta |
| 11 | 32 | 6 Term | i exakt en låst kista på Fionas vind | the trunk = kofferten (Ch2) | i exakt en låst koffert på Fionas vind |
| 12 | 34 | 3 Reversed meaning | En smed som var skyldig tjugo dollar och vägrade ge ett rakt svar. | EN 'A blacksmith owed twenty dollars' — Sam is OWED the money (Ch1); MT made him the debtor | En smed som hade tjugo dollar att fordra och som vägrade ge ett rakt svar. |
| 13 | 1622 | 1 Untranslated | There are more mysteries afoot for Jessica Claus! <bt>Flour Play</bt> is coming soon. | sell line left in English; translated, title anchor kept | Fler mysterier väntar Jessica Claus! <bt>Flour Play</bt> kommer snart. |
| 14 | 1632 | 1 Untranslated | There are more mysteries afoot for Jessica Claus! <bt>Flour Play</bt> is coming soon. | sell line left in English; translated, title anchor kept | Fler mysterier väntar Jessica Claus! <bt>Flour Play</bt> kommer snart. |
| 15 | 1697 | 1 Untranslated | <bt>Flour Play</bt> is coming soon! | closing line left in English; translated, title anchor kept | <bt>Flour Play</bt> kommer snart! |
| 16 | 1624 | What's Next | Greta har bakat samma kanelbulle i fyrtio år. Hon bakade den morgonen efter sin mans begravning eftersom hon inte visste vad hon annars skulle ta sig till med händerna. Den här veckan kommer den ut ur hennes ugn sur, och det gör nästa plåt också, och den däref … | Flour Play blurb copied verbatim from corrected Flour Play SV [29] (EN identical); MT had "slaktaren som kedjade fast lastkajen", "en stulen burk" (fixed in FP) | Greta har gjort samma kanelbulle i fyrtio år. Hon bakade den morgonen efter sin mans begravning eftersom hon inte visste vad hon annars skulle ta sig till med händerna. Den här veckan kommer den ut sur ur ugnen, och det gör nästa plåt också, och den därefter. |
| 17 | 1625 | What's Next | Nytt mjöl. Nytt vatten. En lånad våg. Fortfarande sur. Vid torsdagen står Greta i sitt eget bageri och berättar för Jessica Claus att hennes händer till slut har glömt bort hur man gör. | Flour Play blurb copied verbatim from corrected Flour Play SV [31] (EN identical); MT had "slaktaren som kedjade fast lastkajen", "en stulen burk" (fixed in FP) | Nytt mjöl. Nytt vatten. En lånad våg. Fortfarande sur. Vid torsdagen står Greta i sitt eget bageri och berättar för Jessica Claus att händerna till slut har glömt bort hur man gör. |
| 18 | 1626 | What's Next | Sedan flyger en tegelsten genom fönstret, och ett ord dyker upp med rött på träpanelen där varje barn på Evergreen Avenue kommer att läsa det när de går förbi. | Flour Play blurb copied verbatim from corrected Flour Play SV [33] (EN identical); MT had "slaktaren som kedjade fast lastkajen", "en stulen burk" (fixed in FP) | Sedan flyger en tegelsten genom fönstret, och ett ord dyker upp i rött på fasadpanelen där vartenda barn på Evergreen Avenue kommer att läsa det på väg förbi. |
| 19 | 1627 | What's Next | Staden griper efter de enkla namnen: slaktaren som kedjade fast lastkajen, familjen som ligger efter med sin olja, en uttråkad pojke med en stulen burk. Jessica sträcker sig efter det som passar – för den som gjorde detta köpte pulvret, kände till dosen och an … | Flour Play blurb copied verbatim from corrected Flour Play SV [35] (EN identical); MT had "slaktaren som kedjade fast lastkajen", "en stulen burk" (fixed in FP) | Staden griper efter de enkla namnen: slaktaren som kedjade fast grinden till lastgården, familjen som låg efter med oljan, en uttråkad grabb med en stulen sprayburk. Jessica sträcker sig efter det som passar – för den som gjorde det här köpte pulvret, kände ti … |
| 20 | 1628 | What's Next | Och i den ljusa änden av avenyn har ett nytt konditori bestämt sin premiär till den enda vecka då Holly Jolly kommer att vara mörkt. | Flour Play blurb copied verbatim from corrected Flour Play SV [37] (EN identical); MT had "slaktaren som kedjade fast lastkajen", "en stulen burk" (fixed in FP) | Och i den ljusa änden av avenyn har ett nytt konditori bokat sin invigning till just den vecka då Holly Jolly kommer att hålla stängt. |
| 21 | 42 | 3 Mistranslation | Under den torrlövsdoftande senhösten fanns det en ren och kyla i luften som jag hade känt till länge. | EN 'Underneath the dry-leaf smell of late autumn there was a clean cold edge to the air'; MT garbled ('en ren och kyla') | Under senhöstens doft av torra löv fanns det en ren, kall skärpa i luften som jag hade känt länge. |
| 22 | 43 | 3 Mistranslation | Spöknäten hade satts upp | EN 'The cobwebs'; 'spöknät' = a lost fishing net | Spindelväven hade satts upp |
| 23 | 43 | 3 Mistranslation | ganska många år av mitt långa liv | EN 'a great many years'; 'ganska många' = 'quite a few' | väldigt många år av mitt långa liv |
| 24 | 43 | 6 Term | Mr. Kim hade | Mr. -> herr (Flour Play SV rule) | Herr Kim hade |
| 25 | 43 | 6 Term | Tidningsredaktionen hade ett skelett | EN 'The Gazette office'; the paper is 'Gazette' everywhere else in the edition | Gazettes redaktion hade ett skelett |
| 26 | 45 | 6 Term | breddades mot parken, | the green = allmänningen (Flour Play SV / Frost and Found SV) | breddades mot allmänningen, |
| 27 | 45 | 3 Mistranslation | med en ensam kvist bittergröna för säsongens orangea färg. | EN 'a sprig of bittersweet' (the orange-berried vine); 'bittergröna' is not a word | med en ensam kvist träddödare med orange bär för säsongens färg. |
| 28 | 49 | 3 Mistranslation | och rummet fanns det lätta sorlet i hos en plats där folk trivdes. | garbled syntax | och rummet hade det lättsamma sorlet hos en plats där folk trivs. |
| 29 | 53 | 3 Mistranslation | Protesterar du så har jag gått med den hela vägen längs avenyn och Pip försökte äta upp din krans, så det har kostat på. | EN 'Don't argue with me, I've walked it all the way down the avenue'; MT 'if you protest, then I have walked it' | Protestera inte, jag har burit den hela vägen längs avenyn och Pip försökte äta upp din krans, så den har kostat mig. |
| 30 | 54 | 3 Mistranslation | Jag har läst ganska många brev | EN 'a great many letters' | Jag har läst väldigt många brev |
| 31 | 56 | 3 Mistranslation | Ytterdörren öppnades av en kyla som fick elden att fladdra | EN 'opened on a gust of cold'; MT 'was opened by a cold' | Ytterdörren öppnades med en kall vindil som fick elden att fladdra |
| 32 | 56 | 6 Typo | letade fram till nyanlända | missing article | letade fram till de nyanlända |
| 33 | 57 | 6 Term | "Mr. Worthington, Mrs. Worthington," | Mr./Mrs. -> herr/fru | "Herr Worthington, fru Worthington," |
| 34 | 59 | 6 Term | sa Mrs. Worthington. | Mrs. -> fru | sa fru Worthington. |
| 35 | 59 | 3 Mistranslation | Jag har kommit av mig med att fråga vem som har gjort dem. | EN 'I keep meaning to ask'; MT 'I have lost the thread of asking' | Jag tänker hela tiden fråga vem som har gjort dem. |
| 36 | 61 | 5 Idiom | dränerades värmen ur Fionas ansikte igen | calque of 'drained' | rann värmen ur Fionas ansikte igen |
| 37 | 62 | 4 Proper name | Worthington var den sorts gäster | EN 'The Worthingtons' (the couple) | Familjen Worthington var den sortens gäster |
| 38 | 76 | 3 Mistranslation | jag skulle ha kunnat kasta eldstaden. | EN 'the fire screen' (= 'gnistskyddet' in [49]); MT 'the fireplace' | jag skulle ha kunnat kasta gnistskyddet. |
| 39 | 76 | 5 Address | Då är ni den berömda Mrs. Claus. | Mrs. -> fru; du per the Swedish series address rule (Flour Play SV FP-SV-D5) | Då är du den berömda fru Claus. |
| 40 | 79 | 3 Mistranslation | sa hon i ett nafs, och | EN 'in a rush'; 'i ett nafs' = 'in no time' | sa hon hastigt och |
| 41 | 81 | 3 Mistranslation | "Lättrörlig, er vän." | EN 'Skittish'; 'lättrörlig' = easily moved/agile; du per series rule | "Skygg, din vän." |
| 42 | 83 | 6 Term | Ett rent nöje, Mrs. Claus. | Mrs. -> fru | Ett rent nöje, fru Claus. |
| 43 | 84 | 8 Units / 3 Mistranslation | omkring en tum från ett glasronn | EN 'about an inch from a glass pear' (SAFE: 1 in = 2.5 cm); 'glasronn' (glass rowan) is wrong — it is Fiona's pear | ett par centimeter från ett glaspäron |
| 44 | 86 | 6 Typo | präglad av djup och uråldrig svikelse | 'svikelse' is not a word; svek | präglad av djupt och uråldrigt svek |
| 45 | 86 | 6 Typo | halvställde sig upp | 'halvställde' is not a word; EN 'half rose from her chair' | reste sig halvvägs ur stolen |
| 46 | 87 | 6 Term | Nere på parken sträckte | the green = allmänningen (EN distinguishes the green from 'the park' later in this paragraph) | Nere på allmänningen sträckte |
| 47 | 93 | 5 Idiom | En lek av kylan på trötta ögon. | calque of 'A trick of the cold on tired eyes' | Kylan som spelade trötta ögon ett spratt. |
| 48 | 93 | 6 Term | förbi parken med de halvuppsatta | the green = allmänningen | förbi allmänningen med de halvuppsatta |
| 49 | 93 | 6 Term | förbi tidningsredaktionens tidningsläsande skelett | EN 'the Gazette's' | förbi Gazettes tidningsläsande skelett |
| 50 | 99 | 6 Term | vilken eftermiddag som syföreningen skulle träffas | EN 'the circle' = cirkeln (Frost and Found / Flour Play SV); 'syföreningen' = a sewing society | vilken eftermiddag cirkeln skulle träffas |
| 51 | 106 | 3 Mistranslation | tog av mig kappan från kroken | EN 'took my coat off its hook' | tog ner kappan från kroken |
| 52 | 106 | 1 Anglicism | i en tight, ängslig cirkel | 'tight' is English | i en tät, ängslig cirkel |
| 53 | 109 | 6 Term | dess grågröna fasad och krans med guldrosett | the gold ribbon = guldbandet (Ch1) | dess grågröna fasad och krans med guldband |
| 54 | 111 | 3 Mistranslation | koftan knäppt ända upp i dag | EN 'her cardigan buttoned right today' (Ch1 it was buttoned wrong) | koftan rätt knäppt i dag |
| 55 | 116 | Clue phrase | den med safiren i sitt hjärta, | 'the sapphire at its heart' — one wording everywhere: 'safiren i dess hjärta' (as Ch23/Ch26) | den med safiren i dess hjärta, |
| 56 | 116 | 6 Term | Ta ner guldrosetten på kransen och sätt upp en röd i stället, | the ribbon = band (Ch1, Ch5 signal) | Ta ner guldbandet på kransen och sätt upp ett rött i stället, |
| 57 | 117 | Clue phrase | Safiren i sitt hjärta. | one wording everywhere | Safiren i dess hjärta. |
| 58 | 120 | 6 Typo | i kläder från för ett hundra år sedan | grammar | i kläder från för hundra år sedan |
| 59 | 120 | 6 Typo | det mörka hår vågigt tätt mot huvudet i tjugotalsstil | grammar; EN 'waved close to her head' | det mörka håret ondulerat tätt intill huvudet i tjugotalsstil |
| 60 | 122 | 4 Proper name | Fionans röst stockade sig. | name misspelt | Fionas röst stockade sig. |
| 61 | 122 | 3 Mistranslation | alla pengar i läktet. | EN 'in the county'; 'läktet' is not a word | alla pengar i länet. |
| 62 | 124 | 6 Typo | Hon drog efter andan som skakade till. | garbled syntax | Hon drog ett andetag som skakade. |
| 63 | 126 | 4 Proper name | Fionans röst sprack | name misspelt | Fionas röst sprack |
| 64 | 129 | 3 Mistranslation | en barnsgestalt. | EN 'a child's gesture'; 'barnsgestalt' = a child's figure | en barnslig gest. |
| 65 | 129 | 6 Term / clue | med en lapp på i hennes stil | EN 'a tag'; 'lapp' is reserved for the blackmail note | med en etikett på i hennes stil |
| 66 | 132 | 3 Mistranslation | Det ordet landade inom mig | EN 'That landed in me' (not 'that word') | Det landade inom mig |
| 67 | 133 | 5 Idiom | kunde för allt i smörvyn inte komma på var. | garbled idiom | kunde för allt smör i Småland inte komma på var. |
| 68 | 134 | Clue phrase | Safiren i sitt hjärta, just de orden. | one wording everywhere | Safiren i dess hjärta, just de orden. |
| 69 | 135 | 3 Reversed meaning | Låsta. Rörda." | EN 'Untouched'; MT 'Rörda' = touched | Låsta. Orörda." |
| 70 | 136 | 6 Typo | En så sådan familj, | doubled word | En sådan familj, |
| 71 | 136 | 6 Term / clue | en lapp till försäkringsagenten, | 'lapp' is reserved for the blackmail note | ett meddelande till försäkringsagenten, |
| 72 | 137 | 4 Proper name | "Blackburns papper," | EN 'The Blackburns' papers' | "Familjen Blackburns papper," |
| 73 | 139 | 6 Term | "Hembygdsföreningen." | the Historical Society = Historiska sällskapet (this edition's majority, = Flour Play SV) | "Historiska sällskapet." |
| 74 | 139 | 3 Mistranslation | Han grät vid grundarlagsavläsningen för två år sedan. | EN 'the founders' day reading'; 'grundarlagsavläsningen' is not a word | Han grät vid uppläsningen på grundardagen för två år sedan. |
| 75 | 140 | 3 Mistranslation | varsamt, och tittade på den. | EN 'looked at her' | varsamt, och tittade på henne. |
| 76 | 141 | 4 Proper name | Worthingtons bra vecka | EN 'the Worthingtons' | familjen Worthingtons goda vecka |
| 77 | 147 | 6 Term | jag stod på förstukvisten en stund | the inn's porch = verandan (Ch1) | jag stod på verandan en stund |
| 78 | 149 | 6 Term | "Vi går till Hembygdsföreningen. | Historical Society = Historiska sällskapet | "Vi går till Historiska sällskapet. |
| 79 | 154 | Note vs letters | Brevet, det röda bandet och pengarna under trappan. | EN 'The note'; the blackmail note is 'lappen' (Ch1–2); 'brev' is reserved for the 1924 letters | Lappen, det röda bandet och pengarna under trappan. |
| 80 | 154 | 6 Term | Och den låsta kistan på vinden | the trunk = kofferten (Ch2) | Och den låsta kofferten på vinden |
| 81 | 155 | Note vs letters | När jag lade brevet på bordet | EN 'the note' | När jag lade lappen på bordet |
| 82 | 156 | Note vs letters | och brevet som låg vikt mot mitt bröst | EN 'the note' | och lappen som låg vikt mot mitt bröst |
| 83 | 157 | 6 Term | en enda själ i det här samhället som | town = staden/stan (Flour Play SV) | en enda själ i den här stan som |
| 84 | 158 | 6 Term | "Hon är säker på kistan, | the trunk = kofferten | "Hon är säker på kofferten, |
| 85 | 159 | 6 Term | "Vart allting gammalt i det här samhället tar vägen." | town = stan; grammar (dit, not vart) | "Dit allting gammalt i den här stan tar vägen." |
| 86 | 159 | 6 Term | "Theos arkiv. Hembygdsföreningen." | Historical Society = Historiska sällskapet | "Theos arkiv. Historiska sällskapet." |
| 87 | 161 | 5 Idiom | som en damm som mojnar. | 'mojna' is said of wind | som en damm som stillnar. |
| 88 | 162 | 6 Term | Han tar med choklad till barnens sagostund på lördagarna, den goda chokladen med de små marshmallowsarna, | cocoa = kakao (Ch2 [139]) | Han tar med kakao till barnens sagostund på lördagarna, den goda kakaon med de små marshmallowsarna, |
| 89 | 162 | 6 Typo | hela vägen igenom vad det än är det här rör sig om, | garbled syntax | hela vägen igenom, vad det här än rör sig om, |
| 90 | 166 | 6 Term | Theo har bott på föreningen för att få allt klart, | the Society = sällskapet | Theo har bott på sällskapet för att få allt klart, |
| 91 | 166 | 6 Term | Och halva samhället kommer att vara där | town = stan | Och halva stan kommer att vara där |
| 92 | 167 | 6 Term | "Då är halva samhället ett utmärkt ställe | town = stan | "Då är halva stan ett utmärkt ställe |
| 93 | 177 | 6 Term | för att se ut över samhället som gjorde sig redo för natten. | town = staden | för att se ut över staden som gjorde sig redo för natten. |
| 94 | 177 | 6 Term | och sedan samhället där nedanför. Samhället var upplyst. | town = staden | och sedan staden där nedanför. Staden var upplyst. |
| 95 | 178 | 6 Term / 3 Mistranslation | mellan lyktstolparna på bytorget, brann i gult i stället för orange, ett djupt, stadigt gult sken, varenda tråd av dem, från det gröna till stationen, | the green = allmänningen ('det gröna' = 'the green colour'); gold = guld (Ch1), not yellow | mellan lyktstolparna på allmänningen, brann i guld i stället för orange, ett djupt, stadigt guld, varenda slinga av dem, från allmänningen till stationen, |
| 96 | 179 | 3 Mistranslation | i ett stadigt gult sken. | EN 'a steady gold' (not yellow) | i ett stadigt guldsken. |
| 97 | 181 | 3 Mistranslation / 6 Term | det gulblossande samhället | EN 'the gold-burning town' | den guldbrinnande staden |
| 98 | 187 | 3 Mistranslation | "Det gör inte ont på någon, Jess. | EN 'It won't hurt anybody'; 'göra ont på' is not idiomatic | "Det skadar ingen, Jess. |
| 99 | 189 | 6 Typo | de äldsta och sanna tingen. | EN 'the oldest and truest things' | de äldsta och sannaste tingen. |
| 100 | 191 | 3 Mistranslation / 6 Term | tittade på det gula samhället, | EN 'the gold town' | tittade på den gyllene staden, |
| 101 | 192 | 6 Term | I morgon skulle jag gå ner i samhället | town = staden | I morgon skulle jag gå ner till staden |
| 102 | 195 | Ruling 3 sign | där det sista S:et var hoptryckt i slutet | EN 'the last S crowded in'; the Swedish banner ends in N (GENOM ÅREN) | där det sista N:et var hoptryckt i slutet |
| 103 | 199 | 3 Mistranslation | en liten, prydlig, sluttande handstil | 'sluttande' is for terrain; EN 'sloping hand' = lutande | en liten, prydlig, lutande handstil |
| 104 | 203 | 8 Units (idiom) | backa undan tum för tum. | EN 'by inches' (figurative) — inch idiom removed | backa undan bit för bit. |
| 105 | 203 | 6 Typo | Hans slips var knuten en kvarts varv fel, | grammar | Hans slips var knuten ett kvarts varv snett, |
| 106 | 203 | 3 Mistranslation | som han inte hade någon uppmärksamhet kvar till att lägga märke till, kameralt nog att ens göra rent. | EN 'that he hadn't the attention left to notice, let alone clean'; 'kameralt nog' is nonsense | som han inte hade uppmärksamhet nog kvar att lägga märke till, än mindre torka bort. |
| 107 | 211 | 3 Mistranslation | Jag slutar inte gå runt här och ha svårt att tro att jag fick till det." | EN 'I keep walking through it and not believing I got it done'; garbled | Jag går runt här gång på gång och kan inte tro att jag fick det gjort." |
| 108 | 221 | 6 Typo | Han skrattade han med, nöjd, | doubled pronoun | Han skrattade också, nöjd, |
| 109 | 227 | 5 Idiom | sköt han fram en dämpad hand för att stadga den | EN 'put out a quiet hand'; 'en dämpad hand' is a calque | sträckte han lugnt fram en hand för att stadga den |
| 110 | 229 | 6 Typo | så att de linjerade exakt, | 'linjerade' = ruled (with lines) | så att de låg exakt i linje, |
| 111 | 231 | 3 Mistranslation | Och vid Blackburnmontrarna, | EN 'the Blackburn display' (one case) | Och vid Blackburnmontern, |
| 112 | 233 | 3 Mistranslation | Utställningen var en lång glasdisk med ett halvt dussin gamla brev uppfjädrade inuti, | EN 'The display was a long glass case … letters fanned open'; 'uppfjädrade' is not a word | Montern var en lång glasmonter med ett halvt dussin gamla brev utbredda i solfjäder inuti, |
| 113 | 239 | 5 Address | Er Mr. Hussein har gjort staden | du per the series rule; Mr. -> herr | Din herr Hussein har gjort staden |
| 114 | 241 | 6 Term | Han pekade på disken med ett finger | the case = montern | Han pekade på montern med ett finger |
| 115 | 271 | 6 Term | Men de finns inte i disken, | the case = montern | Men de finns inte i montern, |
| 116 | 281 | 3 Mistranslation | Theo drog in huvudet, nöjd, och fortsatte med att bjuda in alla till äppelmusten. | EN 'ducked his head … invite everyone to the cider' | Theo böjde ned huvudet, nöjd, och fortsatte med att bjuda alla på äppelmusten. |
| 117 | 283 | Note vs letters | fanns en utpressningssedel som visste | the note = lapp ('sedel' = banknote) | fanns en utpressningslapp som visste |
| 118 | 285 | 5 Idiom | Jag bearbetade rummet efter det, långsamt. | calque of 'I worked the room' | Jag gick runt bland folket efter det, långsamt. |
| 119 | 293 | 6 Typo | av grönska vid trappen, | 'trappen' dialectal; trappan elsewhere | av grönska vid trappan, |
| 120 | 295 | 6 Typo | och hon dansade undan precis ut ur mitt räckviddshåll, | 'räckviddshåll' is not a word | och hon dansade undan precis utom räckhåll för mig, |
| 121 | 295 | Note vs letters | exakt den röda nyans som brevet hade sagt åt Fiona | EN 'the note' | exakt den röda nyans som lappen hade sagt åt Fiona |
| 122 | 295 | 6 Typo | pengarna väntade under trappen. | trappan | pengarna väntade under trappan. |
| 123 | 299 | 8 Units | en sista kvarts tum. | EN 'a final quarter-inch' (SAFE: ~6 mm) | en sista halv centimeter. |
| 124 | 309 | 3 Mistranslation | vantarna med insydda namn | EN 'named-cuff mittens' (knitted, not sewn) | vantarna med instickade namn |
| 125 | 310 | 3 Reversed meaning | sa hon, inte utan ett visst missnöje, snarare som ett rent konstaterande, | EN 'not unhappily'; MT 'not without a certain displeasure' | sa hon, inte missnöjt, snarare som ett rent konstaterande, |
| 126 | 314 | 6 Typo | otvvungna | typo | otvungna |
| 127 | 319 | 5 Idiom | Martha hade lärt ut i skolan | EN 'had taught school' | Martha hade undervisat i skolan |
| 128 | 325 | 3 Mistranslation | De har ingen nämnvärd grundplåt. | EN 'an endowment'; 'grundplåt' = seed money | De har inget kapital att tala om. |
| 129 | 325 | 3 Mistranslation | det de drog in på sommarkvarten, | EN 'the summer fair'; 'sommarkvarten' is not a word | det de drog in på sommarmarknaden, |
| 130 | 325 | 6 Typo | läcker in varje gång det regnar. | grammar | läcker varje gång det regnar. |
| 131 | 327 | 5 Register | "Nobbad. Nobbad. Nobbad. | EN 'Turned down' (grant applications); 'nobbad' = snubbed (a person) | "Avslag. Avslag. Avslag. |
| 132 | 328 | 6 Term | för jag frågade honom för tidningens räkning | EN 'for the Gazette' | för jag frågade honom för Gazettes räkning |
| 133 | 331 | Currency | Han lämnar inte ett enda tunnt öre till att hålla lyset igång resten av året. | EN 'one thin dime'; öre -> cent (dollars only) | Han ger inte en enda cent till att hålla lyset tänt resten av året. |
| 134 | 332 | 6 Typo | Formen av det hela sjönk in i mig, kalla och tydliga, maska för maska. | agreement | Formen av det hela sjönk in i mig, kall och tydlig, maska för maska. |
| 135 | 332 | 6 Typo | en enda sak i denna världen | grammar | en enda sak i den här världen |
| 136 | 333 | 6 Term | hade kommit på drift. | EN 'gone astray' — Theo's phrase, 'kommit på villovägar' in Ch4 | hade kommit på villovägar. |
| 137 | 334 | 3 Reversed meaning | och jag höll handen knuten, | EN 'I kept my fist open' | och jag höll handen öppen, |
| 138 | 341 | 3 Mistranslation | till om en snö den första oktober betydde | EN 'an October first snow' (a first snowfall in October), not 'snow on the first of October' | till om en första snö i oktober betydde |
| 139 | 344 | 3 Mistranslation | Festivalen är väldigt mycket för värdshuset, helt ensam." | EN 'a great deal for the inn, all on her own'; MT says the inn is alone | Festivalen är väldigt mycket arbete för värdshuset, och hon är helt ensam." |
| 140 | 358 | 6 Term | männen var tillbaka på grönområdet och spände upp de sista festivalbelysningarna | the green = allmänningen | männen var tillbaka på allmänningen och spände upp de sista festivalslingorna |
| 141 | 358 | 6 Term | de nya trådarna som drogs upp mörka, | light strands = slingor | de nya slingorna som drogs upp mörka, |
| 142 | 359 | 3 Mistranslation | Och en god, gråhudad man som hade sprungit fast helt när det gällde ärliga dörrar att knacka på. | EN 'a good, gray-faced man who'd run clean out of honest doors to knock on'; garbled | Och en god, gråblek man som inte hade några ärliga dörrar kvar att knacka på. |
| 143 | 360 | 6 Typo | vem som helst annars i världen. | grammar | vem som helst annan i världen. |
| 144 | 361 | 3 Mistranslation | och viljan hade aldrig förändrat vad som var sant. Så jag höll viljan i den ena handen | EN 'wanting' = wishing, not 'the will' | och önskningar hade aldrig förändrat vad som var sant. Så jag höll önskan i den ena handen |
| 145 | 361 | 3 Reversed meaning | och jag skulle hålla min hand knuten. | EN 'I would keep my fist open' | och jag skulle hålla handen öppen. |
| 146 | 364 | 6 Term | Grönområdet var den plats där festivalen skulle äga rum, den stora allmänningen söder om Evergreen | the green = allmänningen | Allmänningen var den plats där festivalen skulle äga rum, den stora öppna gräsytan söder om Evergreen |
| 147 | 364 | 5 Idiom | och det rörde mig inte i ryggen. | EN 'I didn't mind it at all'; 'det rörde mig inte i ryggen' = I couldn't care less | och jag hade inget emot det alls. |
| 148 | 366 | 5 Address | "Fru Claus, er pingvin äter en pumpa." | du per the Swedish series rule | "Fru Claus, din pingvin äter en pumpa." |
| 149 | 367 | 3 Mistranslation | i det avslitna locket på en lykta som någon skurit till i förtid, | EN 'a jack-o'-lantern' | i den avslitna toppen på en pumpalykta som någon skurit ut i förtid, |
| 150 | 370 | 3 Mistranslation | den sorten som rycker i en som barn innan hon bestämt sig för om hon ska släppa fram det, | garbled | den sorten som slinker ur ett barn innan hon har bestämt sig för om hon ska släppa fram det, |
| 151 | 371 | 5 Idiom | och iakttog Pip längs med hela nosen med djup misstänksamhet. | calque | och betraktade Pip längs nosryggen med djup misstänksamhet. |
| 152 | 374 | 3 Mistranslation | med båda händerna och inget mer därtill. | EN 'and nothing left over' | med båda händerna och inget över. |
| 153 | 378 | 6 Typo | kunde läsa på femte klassnivå | compound | kunde läsa på femteklassnivå |
| 154 | 380 | 3 Mistranslation | en skör fred mellan Snowball och en pumpa som hade förolämpat honom. | EN 'a gourd' | en skör fred mellan Snowball och en kalebass som hade förolämpat honom. |
| 155 | 382 | 3 Mistranslation | Jag hade läst en hel del brev | EN 'a great many letters' | Jag hade läst väldigt många brev |
| 156 | 385 | 6 Term | Noriko Tanaka stod mitt i grönområdet | the green = allmänningen | Noriko Tanaka stod mitt på allmänningen |
| 157 | 385 | 6 Typo | med gråänkta tinningar | 'gråänkta' is not a word | med gråsprängda tinningar |
| 158 | 386 | 5 Address | Och era renar finns inte med | du per the Swedish series rule | Och dina renar finns inte med |
| 159 | 388 | 4 Proper name | för Komet på Maple Street, | reindeer names as Frost and Found SV (Comet, Dancer) | för Comet på Maple Street, |
| 160 | 389 | 1 Anglicism | det glänsande metallclipet på urklippsblocket | 'clip' -> klämma | den glänsande metallklämman på urklippsblocket |
| 161 | 392 | 3 Mistranslation | Hon hade gått tillbaka till den lykta som Pip | EN 'the jack-o'-lantern' | Hon hade gått tillbaka till den pumpalykta som Pip |
| 162 | 394 | 6 Typo | tittade på den hon med och lutade på huvudet. | word order | tittade också på den och lutade på huvudet. |
| 163 | 399 | 6 Term | i kanten av grönområdet, | the green = allmänningen | i kanten av allmänningen, |
| 164 | 401 | Note vs letters | Det fanns fortfarande ett utpressningsbrev hopvikt i min jacka, | EN 'a blackmail note … in my coat'; brev is reserved for the 1924 letters; coat = kappa (Ch2) | Det fanns fortfarande en utpressningslapp hopvikt i min kappa, |
| 165 | 413 | 6 Typo | Det är det enda jag är bevisvis bra på. | 'bevisvis' is not a word; EN 'reliably good at' | Det är det enda jag är pålitligt bra på. |
| 166 | 423 | 3 Mistranslation | högkragade klänning och tätt vågade hår, | EN 'close-waved hair'; 'vågade' = dared | högkragade klänning och tätt ondulerade hår, |
| 167 | 423 | 6 Typo | lika stadigt som Blackburns kvinnas hade gjort | genitive | lika stadigt som Blackburnkvinnans hade gjort |
| 168 | 433 | Currency | tog aldrig ett enda öre och talade aldrig om det. | EN 'never charged a cent'; öre -> cent | tog aldrig betalt en enda cent och talade aldrig om det. |
| 169 | 439 | 6 Typo | och hon tittade upp på fotografiet hon med, med på snett hållet huvud, | garbled | och hon tittade också upp på fotografiet, med huvudet på sned, |
| 170 | 441 | Note vs letters | Efter hundra år och en låst kista och ett utpressningsbrev är det | EN 'a blackmail note'; brev reserved for the 1924 letters; trunk = koffert | Efter hundra år och en låst koffert och en utpressningslapp är det |
| 171 | 443 | 3 Mistranslation | Över en halv miljon dollar som jag aldrig kommer att ha | EN 'Over five hundred thousand dollars' = because of; 'Över' reads as 'more than' | På grund av en halv miljon dollar som jag aldrig kommer att ha |
| 172 | 455 | 3 Mistranslation | och det stod ganska klart för mig vad i all sin dar det var jag kämpade för. | EN 'a good deal clearer about what, exactly'; 'vad i all sin dar' = 'what on earth' | och det stod betydligt klarare för mig vad, exakt, jag kämpade för. |
| 173 | 458 | Note vs letters | Jag hade burit utpressningsbrevet till näsan ett dussin gånger sedan Fiona gav det till mig, | EN 'the blackmail note' | Jag hade burit utpressningslappen till näsan ett dussin gånger sedan Fiona gav den till mig, |
| 174 | 460 | 3 Reversed meaning | och jag skyndade på honom. | EN 'I didn't hurry him' | och jag skyndade inte på honom. |
| 175 | 464 | 6 Term | "Mrs. Claus." | Mrs. -> fru | "Fru Claus." |
| 176 | 466 | 1 Anglicism | vilket lämnade fräscha, mörka strimmor över de gamla. | 'fräscha' = fresh (clean) | vilket lämnade nya, mörka strimmor över de gamla. |
| 177 | 468 | 5 Address | "Ni är här för ljushållaren. | du per the Swedish series rule | "Du är här för ljushållaren. |
| 178 | 472 | 5 Address | "Jag förutsätter att ni gör det," sa jag. "Det borde ni. Ert arbete finns | du per the Swedish series rule | "Jag förutsätter att du gör det," sa jag. "Det borde du. Ditt arbete finns |
| 179 | 478 | Note vs letters | Den fanns på brevet, och den fanns här. | EN 'It was on the note' | Den fanns på lappen, och den fanns här. |
| 180 | 480 | 5 Address | "Ni gjorde värdshuset," | du | "Du gjorde värdshuset," |
| 181 | 480 | 6 Term | lampetterna, gnistskärmen." | the fire screen = gnistskyddet (Ch1) | lampetterna, gnistskyddet." |
| 182 | 486 | Currency | jag har sett ett öre för det sista av det. | EN 'a penny'; öre -> cent | jag har sett en cent för det sista av det. |
| 183 | 500 | 6 Typo | Hans ilska var en vänners ilska, | grammar | Hans ilska var en väns ilska, |
| 184 | 502 | Note vs letters | och lukten fanns på brevet. | EN 'on the note' | och lukten fanns på lappen. |
| 185 | 510 | 3 Mistranslation | Jag bryr mig inte om att ha en vän som kämpar i skuld till mig, Mrs. Claus. | EN 'I don't mind being owed by a friend who's struggling'; 'bryr mig inte om' = don't care about; Mrs. -> fru | Jag har inget emot att en vän som kämpar är skyldig mig pengar, fru Claus. |
| 186 | 514 | 5 Register | som en småskuren skit." | EN 'like a small man'; 'skit' is a vulgarity the English doesn't have | som en småaktig karl." |
| 187 | 518 | 6 Typo | "Det här gamla trubblelet med henne, om det nu är ett trubbel," | 'trubblelet' is not a word | "Det här gamla bekymret hennes, om det nu är ett bekymmer," |
| 188 | 518 | 5 Address | "Vet ni något om de tidiga dagarna | du | "Vet du något om de tidiga dagarna |
| 189 | 524 | 3 Mistranslation | uppenbarligen ställd inför frågan. | EN 'plainly baffled at the question' | uppenbart förbryllad över frågan. |
| 190 | 532 | 6 Term | "Verandafästena. Det sista av beställningen. | the porch brackets = verandakonsolerna (Ch1) | "Verandakonsolerna. Det sista av beställningen. |
| 191 | 532 | 5 Address | i den foajén i år, vet ni. | du | i den foajén i år, vet du. |
| 192 | 538 | 6 Typo | vad som än sattes ner på receptionen eller stuckits in under en dörr | tense agreement | vad som än sattes ner på receptionen eller stacks in under en dörr |
| 193 | 540 | Note vs letters | Brevet luktade smedja. Men luktade det smedja för att Sam Patel hade lutat sig över det med en penna, eller för att det hade varit någonstans där Sam Patels järn fanns? | EN 'The note' | Lappen luktade smedja. Men luktade den smedja för att Sam Patel hade lutat sig över den med en penna, eller för att den hade varit någonstans där Sam Patels järn fanns? |
| 194 | 542 | 5 Address | Och för att ni frågade efter henne av hela ert hjärta. Jag ska tala om för henne att ni gjorde det. | du | Och för att du frågade efter henne av hela ditt hjärta. Jag ska tala om för henne att du gjorde det. |
| 195 | 552 | Note vs letters | om att lukten på brevet markerade var det hade befunnit sig. | EN 'the smell on the note' | om att lukten på lappen markerade var den hade befunnit sig. |
| 196 | 563 | 6 Typo | Han vände på ett sprött liggarblad mot mig | grammar | Han vände ett sprött liggarblad mot mig |
| 197 | 565 | 6 Typo | "Adertonhundranittioett. | modern form | "Artonhundranittioett. |
| 198 | 565 | 3 Mistranslation | till kyrkan vid torget. | EN 'the church on the green' (the square is a different place) | till kyrkan vid allmänningen. |
| 199 | 577 | 6 Typo | var någon värdefull föremål har tagit vägen, | agreement | vart något värdefullt föremål har tagit vägen, |
| 200 | 619 | Note vs letters | Den som hade skrivit det där brevet arbetade i mörkret. | EN 'that note' | Den som hade skrivit den där lappen arbetade i mörkret. |
| 201 | 619 | 6 Term | att hänga en röd rosett på sin krans | ribbon = band | att hänga ett rött band på sin krans |
| 202 | 623 | 3 Mistranslation | Om inte själva uppståndelsen var själva slugheten. | EN 'the advertising' | Om inte själva skyltandet var själva slugheten. |
| 203 | 649 | 6 Term | och en liten tomtenisse som var alldeles ifrån sig | elf = alv (Frost and Found SV, this book elsewhere) | och en liten alv som var alldeles ifrån sig |
| 204 | 650 | 6 Term | Bram var tomtenissen som följt med oss söderut, | elf = alv | Bram var alven som följt med oss söderut, |
| 205 | 650 | 5 Idiom | och jag gillar inte utseendet på något av det här, | calque of 'I don't like the look of any of it' | och jag tycker inte om hur något av det här ser ut, |
| 206 | 651 | 5 Idiom | "God eftermiddag på dig själv, Bram," | EN 'to you too' | "God eftermiddag på dig också, Bram," |
| 207 | 651 | 5 Idiom | "Nå. Varför gillar du inte utseendet på det?" | calque | "Nå. Varför tycker du inte om hur det ser ut?" |
| 208 | 654 | 8 Units (idiom) | Hon lät sig inte ledas en tum av Bram, | EN 'one inch' (figurative) | Hon lät sig inte ledas ett enda steg av Bram, |
| 209 | 657 | 6 Typo | och nu stängs jag ute från halva som om | EN 'kept out of the half of it'; noun missing | och nu stängs jag ute från halva verkstaden som om |
| 210 | 663 | 6 Typo | Nynsandet tystnade. | typo | Nynnandet tystnade. |
| 211 | 667 | 6 Typo | Den tillhörde aldrig polen, polen var bara platsen där den vilade. | the Pole = Polen (Nordpolen), capitalised | Den tillhörde aldrig Polen, Polen var bara platsen där den vilade. |
| 212 | 674 | Note vs letters | som var större än en brosch och ett brev. | EN 'a brooch and a note' | som var större än en brosch och en lapp. |
| 213 | 675 | Note vs letters | Jag hade brevet i kappfickan, och nu gjorde hon det hon hade lagt sig till med så fort det var i närheten. | EN 'the note' | Jag hade lappen i kappfickan, och nu gjorde hon det hon hade lagt sig till med så fort den var i närheten. |
| 214 | 675 | 6 Term | där jag hade lagt lykthållaren som jag burit hem | the light holder = ljushållaren (Ch8) | där jag hade lagt ljushållaren som jag burit hem |
| 215 | 677 | Note vs letters | "Brevet luktar smedja, | EN 'The note' | "Lappen luktar smedja, |
| 216 | 677 | Note vs letters / 3 Mistranslation | Varthän det brevet har tagit vägen, det är det hennes nos känner till." | EN 'Wherever that note has been' | Var den lappen än har varit, det är det hennes nos känner till." |
| 217 | 681 | 3 Mistranslation | Ljusen brann i gult över Frost Falls, | EN 'burned gold' (not yellow) | Ljusen brann i guld över Frost Falls, |
| 218 | 684 | 3 Mistranslation | Jag gick dit i måndags tillsammans med Pip, | EN 'on the Monday' (narrative past), not 'last Monday' | Jag gick dit på måndagen tillsammans med Pip, |
| 219 | 689 | 6 Term | Att panncentralen gjorde sin sista vinter. | the boiler = pannan (Ch5) | Att pannan gjorde sin sista vinter. |
| 220 | 692 | 3 Mistranslation | som har bestämt sig för att han har varit generös som faktiskt lyssnat. | EN 'had decided he'd been generous by listening' | som har bestämt sig för att han har varit generös bara genom att lyssna. |
| 221 | 693 | 5 Address | "Er festival kommer kanske | du per the Swedish series rule | "Din festival kommer kanske |
| 222 | 696 | 3 Mistranslation | lade till cirkeln med sin smått jämna hand, | EN 'in her small even hand' | lade till cirkeln med sin lilla, jämna handstil, |
| 223 | 696 | Ruling 3 sign / 3 Mistranslation | SKÖTESTÄLLEN. TILLSTÅND. | drawer label EN 'DEEDS'; 'SKÖTESTÄLLEN' = changing tables; deeds = köpebrev in this edition | KÖPEBREV. TILLSTÅND. |
| 224 | 704 | 3 Mistranslation | och Blackburns handlingar fyllda i skåpen bakom henne. | EN 'Blackburn deeds filling the drawers' | och Blackburnska köpebrev som fyllde skåpen bakom henne. |
| 225 | 704 | 6 Term | Det historiska sällskapet. | the Society's name as elsewhere | Historiska sällskapet. |
| 226 | 707 | 3 Mistranslation | för en så obetydlig och förställd fråga, | EN 'so small and idle a question'; 'förställd' = feigned | för en så obetydlig och tillfällig fråga, |
| 227 | 708 | 3 Mistranslation | I stället mjuknade jag upp i hela min upptoning. | EN 'I gentled my whole manner'; 'upptoning' is nonsense | I stället mjukade jag upp hela mitt sätt. |
| 228 | 710 | 3 Mistranslation | och ansiktet darrade till som om det höggs i sten innan hon hejdade sig. | EN 'her face wavered toward spilling before she caught it'; MT 'as if carved in stone' | och ansiktet var nära att brista innan hon tog sig samman. |
| 229 | 711 | 3 Mistranslation | betalar en kommunal lön för en stad av arbete, | EN 'a town wage for a city's worth of work' | betalar en småstadslön för en storstads arbete, |
| 230 | 735 | 3 Mistranslation | till en stiftelse i staden, | EN 'a foundation in the city' (not this town) | till en stiftelse i storstaden, |
| 231 | 737 | 6 Typo | som såg det sällskap han vigt sitt åt sjunka | word missing | som såg det sällskap han vigt sitt liv åt sjunka |
| 232 | 737 | 6 Typo | och plåshinken fångade upp regnet. | typo | och plåthinken fångade upp regnet. |
| 233 | 739 | 3 Mistranslation | och sträcka sig efter den med tanken att han gjorde det för Sällskapets skull. | EN 'telling himself the whole way' | och sträcka sig efter den och hela tiden intala sig att han gjorde det för Sällskapets skull. |
| 234 | 766 | 6 Typo | snett och förstuet, | 'förstuet' is not a word; EN 'sideways and slow' | från sidan och i lugn takt, |
| 235 | 768 | 3 Mistranslation | med gliporna förhängda med plast | EN 'the gap hung with plastic sheeting' | med öppningen förhängd med plast |
| 236 | 790 | 5 Register | och lära ut utfallsteg till gummor klockan halv sex på morgonen. | EN 'grandmothers'; 'gummor' is pejorative | och lära mormödrar att göra utfallsteg klockan halv sex på morgonen. |
| 237 | 790 | 8 Units (idiom) | utmattande, tum för tum-sättet, | EN 'inch-by-inch' (figurative) | utmattande sättet, bit för bit, |
| 238 | 790 | Note vs letters | och det gick inte ihop med ett utpressningsbrev på en halv miljon dollar. | EN 'a blackmail note' | och det gick inte ihop med en utpressningslapp på en halv miljon dollar. |
| 239 | 794 | 3 Mistranslation | Blackburn-papperet, de gamla breven?" | EN 'The Blackburn things' | Blackburn-sakerna, de gamla breven?" |
| 240 | 820 | 6 Typo | Det räknas det också." | doubled pronoun | Det räknas också." |
| 241 | 822 | 6 Typo | från listan i mitt huvudsak, | 'huvudsak' = main thing | från listan i mitt huvud, |
| 242 | 829 | 3 Mistranslation | hade blivit lite modigare i och med festivalveckan. | EN 'had grown a little bolder by the week of the festival' | hade blivit lite djärvare till festivalveckan. |
| 243 | 833 | Ruling 5 bt / 3 Mistranslation | på disken i <bt>The Holly Jolly Bakery</bt>, en turistpryl med ett litet keramiskt <bt>Frost Falls</bt> inuti, grönt och stadshuset och allt. | stray <bt> around the bakery name and the town (not book titles) removed; bakery name as the edition renders it ('Greta ägde Holly Jolly Bakery'); EN 'green and Town Hall and all' = the green, not 'gr … | på disken i Holly Jolly Bakery, en turistpryl med ett litet keramiskt Frost Falls inuti, allmänningen och stadshuset och allt. |
| 244 | 833 | 6 Typo | med en beslutsam munterhet hos en kvinna | grammar | med den beslutsamma munterheten hos en kvinna |
| 245 | 847 | 6 Term | Ute på byplanen var det Brams bekymmer som gällde. Prancer hade rymt från hagen under natten och tagit sig ner i byn, | the green = allmänningen; town = stan (never village) | Ute på allmänningen var det Brams bekymmer som gällde. Prancer hade rymt från hagen under natten och tagit sig ner till stan, |
| 246 | 855 | 6 Typo | vilket jag kan erkänna var i mesta laget av optimism." | garbled idiom | vilket jag kan erkänna var väl optimistiskt." |
| 247 | 857 | 6 Typo | Prancer betraktade honom med en varelses lugna likgiltighet som inte hade för avsikt | relative clause attached to the wrong noun | Prancer betraktade honom med den lugna likgiltigheten hos en varelse som inte hade för avsikt |
| 248 | 859 | 3 Mistranslation | tog sig in i kyrksalen på något sätt | EN 'the church hall' | tog sig in i församlingssalen på något sätt |
| 249 | 861 | 5 Register | och gamla gubben Kim från bilverkstan | EN 'old Mr. Kim'; 'gubben' is disrespectful | och gamle herr Kim från bilverkstan |
| 250 | 865 | 3 Mistranslation | Du bryter sönder något, på dig eller henne." | EN 'You'll dislocate something' | Du drar något ur led, på dig själv eller henne." |
| 251 | 869 | 6 Term | på den här byplanen som är ens hälften | the green = allmänningen | på den här allmänningen som är ens hälften |
| 252 | 871 | 5 Idiom | och drog ner ett jubel från barnen. | 'dra ner' = to pull down | och lockade fram ett jubel från barnen. |
| 253 | 889 | 5 Register | och gubben Kim fällde ihop sin stol, | EN 'Mr. Kim' | och herr Kim fällde ihop sin stol, |
| 254 | 896 | 3 Mistranslation | Olivia kallade till en extra vargtimme om vantarna den eftermiddagen. | EN 'an extra session'; 'vargtimme' = the hour of the wolf | Olivia kallade till en extra stickträff för vantarna den eftermiddagen. |
| 255 | 898 | 3 Mistranslation | med korgar av skogsgrön ull på golvet | EN 'school-green wool' (the school colours, Ch5) | med korgar av garn i skolans gröna färg på golvet |
| 256 | 904 | 6 Term | återberättad av mr Kim, | Mr. -> herr | återberättad av herr Kim, |
| 257 | 908 | 6 Term | så mr Kim berättar det." | Mr. -> herr | så herr Kim berättar det." |
| 258 | 908 | 6 Typo | otvvungna | typo | otvungna |
| 259 | 910 | 6 Term | Dot jobbade på en resår med sammanbiten mun. | cuff = mudd (Ch5); 'resår' = elastic | Dot jobbade på en mudd med sammanbiten mun. |
| 260 | 912 | 6 Term | att hembygdsgården lägger ner." | Historical Society = Historiska sällskapet | att Historiska sällskapet lägger ner." |
| 261 | 920 | 6 Term | "Apropå hembygdsgården," | the Society = Sällskapet | "Apropå Sällskapet," |
| 262 | 946 | 6 Term | Jag hade haft det kvar i rocken alltsedan biblioteket. | coat = kappa | Jag hade haft det kvar i kappan alltsedan biblioteket. |
| 263 | 964 | 6 Term | Den sista resåren på mina stickor | cuff = mudd | Den sista mudden på mina stickor |
| 264 | 975 | 3 Mistranslation | om ditt välsignade tystlåtna sinne." | EN 'your great quiet mind' | om ditt stora, tystlåtna sinne." |
| 265 | 979 | 3 Mistranslation | Hela hans historiestipendium gick ut på | EN 'His whole history scholarship' (learning), not a stipend | Hela hans historiska lärdom gick ut på |
| 266 | 979 | 3 Mistranslation | både femtio-i-ett-träningslägret och nattvakten. | EN 'the five-thirty boot camp'; MT 'fifty-in-one training camp' | både träningspasset halv sex och nattvakten. |
| 267 | 987 | 5 Idiom | tillhör Theos bord, | EN 'Theo's department' (as Sam says it in Ch8) | är Theos avdelning, |
| 268 | 991 | 3 Mistranslation | "Smedjan satte upp honom på listan, och jag tror att smedjan kommer att vara | EN 'The forge smell' | "Smedjelukten satte upp honom på listan, och jag tror att smedjelukten kommer att vara |
| 269 | 991 | 3 Mistranslation | att lappen luktar som Sams järn, inte som Sam. | EN 'the note smells of where Sam's iron is, not of Sam' — the deduction rests on 'where' | att lappen luktar av platsen där Sams järn finns, inte av Sam. |
| 270 | 999 | 6 Term | hr Carter." | Mr. -> herr | herr Carter." |
| 271 | 1003 | 6 Term | fastighetsadvokaternas håll, | EN 'the estate lawyers' (= dödsboadvokaternas, Ch9) | dödsboadvokaternas håll, |
| 272 | 1021 | 3 Mistranslation | Vera tar hand om skötebreven och fastighetsregistren, ett sekel av vem-som-ägde-vad, värdshusets skötebrev någonstans bland dem. | EN 'deeds'; 'skötebrev' is not a word (deeds = köpebrev in this edition) | Vera tar hand om köpebreven och fastighetsregistren, ett sekel av vem-som-ägde-vad, värdshusets köpebrev någonstans bland dem. |
| 273 | 1025 | 6 Term | hade kommit på avvägar." | Theo's phrase 'gone astray' = 'kommit på villovägar' (Ch4) | hade kommit på villovägar." |
| 274 | 1035 | 3 Mistranslation | Men viljan är inga bevis, Nick, det har den aldrig varit, | EN 'wanting isn't evidence' | Men att vilja något är inga bevis, Nick, det har det aldrig varit, |
| 275 | 1045 | 6 Typo | Gå dit och erbjuda dina. | imperative | Gå dit och erbjud dina. |
| 276 | 1051 | 6 Typo | rentvådda bort alla rimliga tvivel, | garbled | rentvådda bortom allt tvivel, |
| 277 | 1051 | 3 Mistranslation | att inte hänga fast vid honom förrän | EN 'not to settle on him' | att inte slå mig till ro med honom förrän |
| 278 | 1060 | 3 Mistranslation | för att hänga upp den sista av järnhyllorna, | EN 'the iron brackets' (= verandakonsolerna, Ch1); 'hyllor' = shelves | för att hänga upp den sista av järnkonsolerna, |
| 279 | 1064 | 3 Mistranslation | att anförtro honom en bit av sanningen som tack. | EN 'in return' | att anförtro honom en bit av sanningen i gengäld. |
| 280 | 1068 | 6 Term | utom hörhåll från lobbyn, | lobby = foajén (Ch1) | utom hörhåll från foajén, |
| 281 | 1068 | 6 Typo | Att hon var skrämda, Sam, | agreement | Att hon var skrämd, Sam, |
| 282 | 1078 | 3 Mistranslation | trots att jag hade kommit för att sona mitt brott och inte för att hitta bevis. | EN 'to make amends'; 'sona mitt brott' = atone for my crime | trots att jag hade kommit för att gottgöra honom och inte för att hitta bevis. |
| 283 | 1080 | 6 Term | Fionas lobby var full av den, trappräcket, eldstadsskärmen, hyllorna som sattes upp på verandan, | lobby = foajé; fire screen = gnistskyddet; brackets = konsoler | Fionas foajé var full av den, trappräcket, gnistskyddet, konsolerna som sattes upp på verandan, |
| 284 | 1082 | 5 Register | så kom ihåg hens ansikte åt mig. | pronoun | så kom ihåg ansiktet åt mig. |
| 285 | 1084 | 3 Mistranslation | att smederna i tre grevskap är skyldiga mig | EN 'three counties' (US); 'grevskap' = English shires | att smederna i tre län är skyldiga mig |
| 286 | 1086 | 3 Mistranslation | och lämnade honom till hans hyllor. | EN 'his brackets' | och lämnade honom åt hans konsoler. |
| 287 | 1092 | 6 Typo | "Riktigt bolag," | grammar | "Ett riktigt företag," |
| 288 | 1092 | 3 Mistranslation | bouppteckningar och egendomar och efterforskning | EN 'probate and estates' | bouppteckningar och dödsbon och efterforskning |
| 289 | 1092 | 3 Mistranslation | dog nere i staden i våras, inga barn, inget testamente av värde, | EN 'down in the city' (not this town); 'no will worth the name' | dog nere i storstaden i våras, inga barn, inget testamente värt namnet, |
| 290 | 1104 | 3 Mistranslation | Över en sak som lagen inte kan röra." | EN 'Over a thing' = about; 'Över' reads 'more than' | För en sak som lagen inte kan röra." |
| 291 | 1106 | 3 Mistranslation | och det vill i synnerhet inte ha hennes hud. | EN 'it certainly doesn't want her hide'; literal 'her skin' | och ännu mindre vill det komma åt henne. |
| 292 | 1106 | 5 Idiom | Den som blöder din vän säljer henne | calque of 'bleeding your friend' | Den som pressar din vän på pengar säljer henne |
| 293 | 1108 | 3 Mistranslation | Neil hade just berättat för mig, ombedd eller ej, | EN 'unasked' — the point is he volunteered it | Neil hade just berättat för mig, oombedd, |
| 294 | 1115 | Note vs letters | Och den sa inte vad utpressningsbrevet sa. Den sa mer än brevet, | EN 'the blackmail note … the note' | Och den sa inte vad utpressningslappen sa. Den sa mer än lappen, |
| 295 | 1116 | 3 Mistranslation | de andra tjänarna som gick i strejk, | EN 'who walked out' (quit), not a strike | de andra tjänarna som slutade, |
| 296 | 1116 | 3 Mistranslation | bad om sin uppskjutna lön | EN 'back wages' | bad om sin innestående lön |
| 297 | 1118 | Note vs letters | på det enkla sätt som brevet vill få din vän att tro | EN 'the note' | på det enkla sätt som lappen vill få din vän att tro |
| 298 | 1118 | 3 Mistranslation | Hon betalade igen sig själv med det enda hon kunde nå, | EN 'She paid herself back'; 'betala igen' = retaliate | Hon tog betalt åt sig själv med det enda hon kunde nå, |
| 299 | 1124 | 6 Typo | hemligstmakeriet | typo | hemlighetsmakeriet |
| 300 | 1133 | 3 Mistranslation | Han mötte mig där, gråhårig och tacksam, | EN 'gray and grateful' (his face, Ch4 'gray cast'), not gray-haired | Han mötte mig där, grå i ansiktet och tacksam, |
| 301 | 1133 | 3 Mistranslation | mässingsgemmen i mitt tråg. | EN 'paper clips in my tray'; 'tråg' = trough | mässingsgemen på min bricka. |
| 302 | 1137 | 3 Mistranslation | med hans lilla sluttande handstil | 'sloping hand' = lutande | med hans lilla lutande handstil |
| 303 | 1137 | Ruling 3 sign | B-avdelningen – Bagerikvitton, Bandstand-abonnemang – | EN index cards 'Bandstand Subscriptions' — translated, B-initial kept so the alphabetical run still works | B-avdelningen – Bagerikvitton, Bidrag till musikpaviljongen – |
| 304 | 1141 | 6 Term | just de brev som hade kommit på avvägar. | Theo's 'gone astray' = 'kommit på villovägar' | just de brev som hade kommit på villovägar. |
| 305 | 1141 | Clue phrase | (safiren i dess mitt) | EN '(the sapphire at its heart)' — MT 'i dess mitt' (at its centre) on the card broke the match with the note's 'safiren i dess hjärta'; one wording everywhere | (safiren i dess hjärta) |
| 306 | 1143 | Clue phrase | Safiren i dess mitt. | one wording everywhere | Safiren i dess hjärta. |
| 307 | 1145 | Note vs letters | eftersom utpressningsbrevet hopvikt i min kappa | EN 'the blackmail note' — the note must not share the 1924 letters' word | eftersom utpressningslappen hopvikt i min kappa |
| 308 | 1145 | Clue phrase | Safiren i dess mitt. Det är ett egendomligt sätt | one wording everywhere | Safiren i dess hjärta. Det är ett egendomligt sätt |
| 309 | 1145 | Note vs letters / clue count | Den stod i utpressningsbrevet precis som den stod på Theos kort, samma fem ord i samma ordning. Två personer beskriver inte ett smycke med samma fem udda ord av en slump. | note = lapp; the Swedish phrase 'safiren i dess hjärta' has four words, so 'five' -> 'fyra' (decision IT-SV-2) | Den stod i utpressningslappen precis som den stod på Theos kort, samma fyra ord i samma ordning. Två personer beskriver inte ett smycke med samma fyra udda ord av en slump. |
| 310 | 1151 | Ruling 3 sign | B, B, Bridge-turnering, Bunting, Överskott, | EN 'Bridge Tournament, Bunting, Surplus' — 'Bunting' left in English; translated with B kept | B, B, Bridgeturnering, Banderoller, överskott, |
| 311 | 1151 | 6 Term | sa något om värmepannan | the boiler = pannan | sa något om pannan |
| 312 | 1151 | 3 Mistranslation | mannen som köpte den goda kakan med de små marshmallowsarna | EN 'the good cocoa'; 'kakan' = the cake | mannen som köpte den goda kakaon med de små marshmallowsarna |
| 313 | 1151 | Note vs letters | hade skrivit de brev som skrämde livet ur Fiona. | EN 'the notes' — not 'brev' (the 1924 letters are named in the next sentence) | hade skrivit de lappar som skrämde livet ur Fiona. |
| 314 | 1157 | 6 Typo | när hon visste att något stod inte rätt till. | word order | när hon visste att något inte stod rätt till. |
| 315 | 1159 | Clue count | De fem orden. | the Swedish clue phrase has four words (decision IT-SV-2) | De fyra orden. |
| 316 | 1159 | 3 Mistranslation | sa han inte att det var ledsamt, | EN 'he didn't say I'm sorry' | sa han inte att han var ledsen, |
| 317 | 1165 | Currency / 5 Idiom | Theo skulle aldrig stjäla ett enda öre för egen del. För Sällskapet pratade han omkull sig själv till att göra nästan vad som helst. | öre -> cent; 'prata omkull' = talk someone down | Theo skulle aldrig stjäla en enda cent för egen del. För Sällskapets skull övertalade han sig själv till nästan vad som helst. |
| 318 | 1171 | 3 Mistranslation | Det vällde upp gult vid fönstren, | EN 'It came up gold' | Det vällde upp ett guldsken vid fönstren, |
| 319 | 1179 | 6 Term | hade han byggt en stor spis av fältsten, | EN 'a great fireplace' = eldstad ('A hearth' = 'En eldstad' in the next lines); 'spis' = cooker | hade han byggt en stor eldstad av fältsten, |
| 320 | 1187 | 6 Typo | en vän som hölls på att kvävas i den mörka staden | grammar | en vän som höll på att kvävas i den mörka staden |
| 321 | 1187 | 3 Mistranslation | Nicks ord från natten då listan upptäcktes dök upp | EN 'the night of the list' (Ch16, when she wrote it) | Nicks ord från kvällen med listan dök upp |
| 322 | 1192 | Note vs letters | Det andra brevet kom nästa morgon, | EN 'The second note' | Den andra lappen kom nästa morgon, |
| 323 | 1194 | 6 Term | Män bar ut bockbord på bytorget | the green = allmänningen | Män bar ut bockbord på allmänningen |
| 324 | 1194 | 6 Term | kom Vera Reed ner för farstukvisten när jag gick uppför den, | EN 'the porch steps'; porch = veranda | kom Vera Reed ner för verandatrappan när jag gick uppför den, |
| 325 | 1196 | 3 Mistranslation | "Parkeringsbiljetter," | EN 'Parking passes'; 'parkeringsbiljett' = a ticket | "Parkeringstillstånd," |
| 326 | 1206 | Note vs letters | och lade det bland mina brev och gick sin väg, | EN 'among my letters' = the morning mail; 'brev' kept for the 1924 letters | och lade det bland min post och gick sin väg, |
| 327 | 1208 | Note vs letters | Kortare än det första, det här, | the note = lappen (common gender) | Kortare än den första, den här, |
| 328 | 1212 | 5 Register | så vad fan vill han egentligen? | EN 'what does he even want' — no swearword in the English | så vad vill han egentligen? |
| 329 | 1214 | Note vs letters | sa jag och vände på brevet i händerna, läste det igen. | EN 'the note' | sa jag och vände på lappen i händerna, läste den igen. |
| 330 | 1214 | Note vs letters | Brevet har skrämt mig för din räkning i dagar. | EN 'The note' | Lappen har skrämt mig för din räkning i dagar. |
| 331 | 1226 | Note vs letters | Jag höll upp brevet. "Får jag behålla det? Tillsammans med det första?" | EN 'the note … with the first one' | Jag höll upp lappen. "Får jag behålla den? Tillsammans med den första?" |
| 332 | 1228 | Note vs letters | och jag vek ihop det och lade undan det. | pronoun for lappen | och jag vek ihop den och lade undan den. |
| 333 | 1230 | Note vs letters | Jag vände på brevet och tittade | EN 'I turned the note over' | Jag vände på lappen och tittade |
| 334 | 1230 | Note vs letters | Samma som det första brevet, | EN 'the first note' | Samma som den första lappen, |
| 335 | 1230 | Note vs letters | Det andra brevet bekräftade det bara. | EN 'The second note' | Den andra lappen bekräftade det bara. |
| 336 | 1232 | 6 Typo | Det avgjorde var någonstans ifrån utan tvivel, och nästan vem. | garbled | Det avgjorde varifrån bortom allt tvivel, och nästan vem. |
| 337 | 1234 | Note vs letters | Han lade det bland mina brev och gick sin väg, | Fiona's mail, not the 1924 letters | Han lade det bland min post och gick sin väg, |
| 338 | 1234 | Note vs letters | som jag nu trodde hade skrivit det i den bilden, | pronoun for lappen | som jag nu trodde hade skrivit den i den bilden, |
| 339 | 1236 | Note vs letters | Men med två brev i handen anade jag | EN 'with two notes in my hand' | Men med två lappar i handen anade jag |
| 340 | 1240 | Note vs letters | lade undan brevet tillsammans med det första. | EN 'put the note away with the first' | lade undan lappen tillsammans med den första. |
| 341 | 1240 | 3 Mistranslation | innan den sista av dem har åkt. | EN 'before the last of them is gone' (days) | innan den sista av dem har gått. |
| 342 | 1245 | 6 Term | Bytorget hade förvandlats sedan morgonen. | the green = allmänningen | Allmänningen hade förvandlats sedan morgonen. |
| 343 | 1245 | 6 Term | ett helt bord med föreningens vantar | EN 'the circle's mittens' | ett helt bord med cirkelns vantar |
| 344 | 1245 | 6 Typo | och att det var med den saken som det var. | garbled idiom for 'and that was that' | och därmed basta. |
| 345 | 1246 | 3 Mistranslation | som sin urgamla rättmätiga egendom. | EN 'her ancient due' | som sin urgamla rätt. |
| 346 | 1248 | 6 Term | från andra sidan torget, | the green = allmänningen | från andra sidan allmänningen, |
| 347 | 1249 | Note vs letters | Det andra brevet hade sagt att festivalen slutar på söndag, | EN 'The second note' | Den andra lappen hade sagt att festivalen slutar på söndag, |
| 348 | 1249 | Note vs letters | där ett tredje brev kunde ha lämnats bland festivalbesökarna. | EN 'a third note' | där en tredje lapp kunde lämnas bland festivalbesökarna. |
| 349 | 1250 | 3 Mistranslation | En gestalt svingade sig upp på värdshusets veranda, | EN 'slipped up onto' | En gestalt smög upp på värdshusets veranda, |
| 350 | 1250 | 6 Term | Jag började gå över torget för fort, | the green = allmänningen | Jag började gå över allmänningen för fort, |
| 351 | 1251 | 6 Term | när jag kom tillbaka över torget | the green = allmänningen | när jag kom tillbaka över allmänningen |
| 352 | 1255 | Note vs letters | och på brevet som hade kommit till henne den morgonen, | EN 'the note' | och på lappen som hade kommit till henne den morgonen, |
| 353 | 1256 | 4 Speaker | "Inte i dag," sa hon. | EN 'I said' — Jessica answers Noriko; MT gave the line to Noriko | "Inte i dag," sa jag. |
| 354 | 1258 | 4 Speaker | "Säg inte det till henne," sa hon. | EN 'I said' | "Säg inte det till henne," sa jag. |
| 355 | 1259 | 5 Idiom | Frostormbunkar växte upp på insidan | EN 'Frost ferns' on a window = isblommor | Isblommor växte upp på insidan |
| 356 | 1259 | 6 Typo / Term | Tjocka, långsamma flingor daledes ner över torget, | 'daledes' is not a word; the green = allmänningen | Tjocka, långsamma flingor dalade ner över allmänningen, |
| 357 | 1260 | 6 Typo | Jag stod i det fallande snöfallet bland mina grannar | tautology | Jag stod i den fallande snön bland mina grannar |
| 358 | 1263 | 4 Speaker | "Det är det," sa hon. | EN 'I said' — Jessica answers Fiona | "Det är det," sa jag. |
| 359 | 1268 | 3 Mistranslation | Jag hade friat tre män, och att fria dem hade lämnat mig | EN 'cleared'; 'fria' = propose marriage / acquit | Jag hade rentvått tre män, och att rentvå dem hade lämnat mig |
| 360 | 1269 | Note vs letters | de två breven, kopian jag hade gjort | EN 'the two notes' — must not share the word with the 1924 letters (the Ch22 deduction separates them) | de två lapparna, kopian jag hade gjort |
| 361 | 1270 | Ruling 5 bt / 1 Untranslated / Clue phrase | Brevet citerade Theos egna ord. <bt>the sapphire at its heart</bt>: fem ord, formulerade som av en historiker och inte av en tjuv, som låg i utpressningsbrevet precis som de låg på kortet | the clue phrase was left in ENGLISH inside a stray <bt>; now the edition's one wording 'safiren i dess hjärta' (four words — decision IT-SV-2); note = lapp | Lappen citerade Theos egna ord. Safiren i dess hjärta: fyra ord, formulerade som av en historiker och inte av en tjuv, som låg i utpressningslappen precis som de låg på kortet |
| 362 | 1270 | Note vs letters | Brevet var skrivet på Sällskapets krämfärgade brevpapper, | EN 'The note' | Lappen var skriven på Sällskapets krämfärgade brevpapper, |
| 363 | 1270 | 6 Term | som beskrev broschen hade kommit på avvägar. | Theo's 'gone astray' | som beskrev broschen hade kommit på villovägar. |
| 364 | 1272 | Note vs letters | Jag tog det andra brevet och ett ark | EN 'the second note' | Jag tog den andra lappen och ett ark |
| 365 | 1272 | Note vs letters | Brevet hade skrivits på papper från Theos förråd, | EN 'The note' | Lappen hade skrivits på papper från Theos förråd, |
| 366 | 1275 | Note vs letters | i Fionas vardagsrum. Theo hade skrivit breven. Men Theo kunde omöjligt ha burit det andra till en foajé full av festivalgäster och gått därifrån utan att en enda själ lade märke till det. Någon annan hade gått med det till värdshuset. | EN 'Theo had written the notes … the second one'; 'sitting room' = sällskapsrummet (Ch2) | i Fionas sällskapsrum. Theo hade skrivit lapparna. Men Theo kunde omöjligt ha burit den andra till en foajé full av festivalgäster och gått därifrån utan att en enda själ lade märke till det. Någon annan hade gått med den till värdshuset. |
| 367 | 1276 | 1 Untranslated / Note vs letters | Brevet visste inte bara att broschen var stulen. Det visste att värdshuset hade köpts för pengarna. I know how your family came by this inn, hade det första brevet sagt. | the quotation of the note was left in ENGLISH; now the note's own Swedish wording from Ch2 [116]; note = lapp — the deduction ('not in any Blackburn letter') needs the two words distinct | Lappen visste inte bara att broschen var stulen. Den visste att värdshuset hade köpts för pengarna. Jag vet hur din familj kom över det här värdshuset, hade den första lappen sagt. |
| 368 | 1276 | 3 Mistranslation | En skötehandling. | EN 'A deed' (= köpebrev in this edition); 'skötehandling' is not a word | Ett köpebrev. |
| 369 | 1277 | 3 Mistranslation | Och värdshusets skötehandling förvarades | EN 'the inn's deed' | Och värdshusets köpebrev förvarades |
| 370 | 1279 | Note vs letters | och Theo kunde inte ha burit breven till värdshuset. | EN 'carried the notes to the inn' | och Theo kunde inte ha burit lapparna till värdshuset. |
| 371 | 1281 | 3 Mistranslation | med skötehandlingen till Winter Wonderland Inn | EN 'the deed' | med köpebrevet till Winter Wonderland Inn |
| 372 | 1288 | 6 Term / 3 Mistranslation | det gamla lagfartsbrevet för allmänningen, själva byalaget, | deed = köpebrev throughout (Ch4, Ch11 drawer label, Ch16, Ch22); EN 'the common land itself' ('byalaget' = a village association) | det gamla köpebrevet för allmänningen, själva den gemensamma marken, |
| 373 | 1288 | 3 Mistranslation | Hon suckade, den där tunga suck som kvinnor stönar fram när de ombeds göra en sak till en lång dag, | garbled | Hon suckade, den där plågade sucken hos en kvinna som ombeds göra en liten sak till under en lång dag, |
| 374 | 1290 | 6 Typo | som vems som helst blick vandrar i när man väntar. | garbled | som vem som helst låter blicken vandra medan man väntar. |
| 375 | 1290 | 6 Term | vid mässingsskyltarna längs arkivlådorna, | EN 'the brass card frames' (= mässingsramarna, Ch11) | vid mässingsramarna längs arkivlådorna, |
| 376 | 1292 | Ruling 3 sign | löd: PROPERTY — EVERGREEN AVE — WINTER WONDERLAND INN. | file tab 'PROPERTY' left in English; translated | löd: FASTIGHET — EVERGREEN AVE — WINTER WONDERLAND INN. |
| 377 | 1294 | 6 Term | Värdshusets lagfartsbrev. Ute ur sin låda. Liggande i återarkiveringskorgen, nyligen hanterad, | deed = köpebrev; agreement | Värdshusets köpebrev. Ute ur sin låda. Liggande i återarkiveringskorgen, nyligen hanterat, |
| 378 | 1296 | 6 Term | Hon hade haft framme den. Lagfartsbrevet för värdshuset, | deed = köpebrev; pronoun | Hon hade haft framme det. Köpebrevet för värdshuset, |
| 379 | 1298 | 6 Term | med en kopia av allmänningens lagfartsbrev | deed = köpebrev | med en kopia av allmänningens köpebrev |
| 380 | 1306 | 6 Term | med allmänningens lagfartsbrev i väskan, | deed = köpebrev | med allmänningens köpebrev i väskan, |
| 381 | 1310 | 6 Term | broschen, stenen, pantlånekontoret. | the pawnshop = pantbanken (Ch2, Ch9) | broschen, stenen, pantbanken. |
| 382 | 1310 | Note vs letters | Och han kunde inte ha burit breven tvärs över staden och lagt ett på ett fullsmäckat skrivbord | EN 'carried the notes' — 'breven' here would mean the 1924 letters he had just pulled | Och han kunde inte ha burit lapparna tvärs över staden och lagt en på ett fullsmäckat skrivbord |
| 383 | 1312 | 6 Term | Vera hade lagfartsbrevet, beviset på köpet, | deed = köpebrev | Vera hade köpebrevet, beviset på köpet, |
| 384 | 1312 | Note vs letters | samma morgon som det andra brevet dök upp, | EN 'the second note' | samma morgon som den andra lappen dök upp, |
| 385 | 1314 | 6 Term / 8 idiom | Theo för den förening han såg tyna bort i sakta farten. | EN 'the Society he was watching die by inches' (Society = sällskapet) | Theo för det sällskap han såg dö bit för bit. |
| 386 | 1314 | 6 Term | en stadslön för en storstads arbete | echo of Vera's own words in Ch11 | en småstadslön för en storstads arbete |
| 387 | 1322 | 6 Term | med allmänningens lagfartsbrev i väskan | deed = köpebrev | med allmänningens köpebrev i väskan |
| 388 | 1322 | 6 Typo | det slag jag inte behövt ta sedan den dag | collocation | det slag jag inte hade behövt fatta sedan den dag |
| 389 | 1327 | 3 Mistranslation | värdshusets skötebrev som låg framme ur lådan. | EN 'the inn's deed' (= köpebrev) | värdshusets köpebrev som låg framme ur lådan. |
| 390 | 1327 | Note vs letters | Breven skulle upphöra, | EN 'The notes would stop' | Lapparna skulle upphöra, |
| 391 | 1327 | 6 Term | tillbaka i sin kista på vinden. | the trunk = kofferten | tillbaka i sin koffert på vinden. |
| 392 | 1333 | 6 Typo | och till slut såg jag vart den lätta utvägen bar åt fel håll. | garbled | och till slut såg jag var den lätta utvägen gick fel. |
| 393 | 1335 | 3 Mistranslation | förvandlade den där vindsresåren till en förmögenhet. | EN 'that attic trunk'; 'vindsresår' (attic elastic) is nonsense | förvandlade den där vindskofferten till en förmögenhet. |
| 394 | 1335 | 3 Mistranslation | Jag hade läst tiotusen brev på polpuln, | EN 'at the Pole'; 'polpuln' is not a word | Jag hade läst tiotusen brev på Nordpolen, |
| 395 | 1341 | 3 Mistranslation | "Jag funderar," sa jag. | EN 'I'm choosing' — the chapter's word | "Jag väljer," sa jag. |
| 396 | 1345 | 3 Mistranslation | Med lagen inblandad, varsamt hållen, med barmhärtighet, men ändå. | EN 'done gently, done with mercy, but done' | Med lagen inblandad, varsamt utfört, med barmhärtighet, men utfört. |
| 397 | 1349 | 8 Units (idiom) | och jag hade kämpat mig in en tum i taget, | EN 'an inch at a time' (figurative) | och jag hade kämpat mig in en bit i taget, |
| 398 | 1349 | 8 Units (idiom) | kunde kosta mig en del av den hårt förvärvade tummen. | EN 'that hard-won inch' (figurative) | kunde kosta mig en del av den mödosamt vunna marken. |
| 399 | 1351 | 3 Mistranslation | Sedan lät jag den bero, | EN 'Then I let it go' | Sedan släppte jag den, |
| 400 | 1362 | 3 Mistranslation | på sin lilla expedition på stationen | EN 'her small office' | på sitt lilla kontor på stationen |
| 401 | 1362 | Note vs letters / clue count | De två breven. Theos katalogkort med de fem matchande orden. | EN 'The two notes … the five matching words' — note = lapp; the Swedish phrase has four words (IT-SV-2) | De två lapparna. Theos katalogkort med de fyra matchande orden. |
| 402 | 1362 | 6 Term | Värdshusets fastighetsbrev som låg framme utanför sin låda i Veras arkiveringskorg. | deed = köpebrev; the refile basket (Ch23) | Värdshusets köpebrev som låg framme utanför sin låda i Veras återarkiveringskorg. |
| 403 | 1364 | Note vs letters | Två brev, ett penningkrav, | EN 'Two notes' | Två lappar, ett penningkrav, |
| 404 | 1365 | 6 Typo | att få både ock." | typo | att få både och." |
| 405 | 1367 | 3 Mistranslation | som gjorde en dum sak av skäl | EN 'a bad thing' | som gjorde en dålig sak av skäl |
| 406 | 1367 | 6 Typo / Term | Vi kallas det medlande rättvisa. | EN 'restorative justice' = reparativ rättvisa; 'kallas' typo | Vi kallar det reparativ rättvisa. |
| 407 | 1369 | 3 Mistranslation | inget lockbrev instucket under värdshusets trappa i mörkret. Det där hör till på film. | EN 'no decoy envelope' (brev reserved for the 1924 letters); idiom | inget lockkuvert instucket under värdshusets trappa i mörkret. Det där hör hemma på film. |
| 408 | 1373 | 6 Typo | att dölja den hälften av det som skammar dig, | 'skammar dig' is not idiomatic | att dölja den hälften av det som du skäms för, |
| 409 | 1374 | 3 Mistranslation | Det fanns en lättnad invävd i vart och ett av dem. | EN 'There was relief threaded all through it' | Det fanns lättnad invävd i hela gråten. |
| 410 | 1379 | 6 Typo | måste ha rätrat på sina | typo | måste ha rätat på sina |
| 411 | 1380 | 6 Typo | att vara rädd för mitt eget vindsvåning." | agreement; EN 'my own attic' | att vara rädd för min egen vind." |
| 412 | 1385 | 6 Term | skrapet av bockbord som fälldes ihop på gräset. | EN 'on the green' | skrapet av bockbord som fälldes ihop på allmänningen. |
| 413 | 1385 | 6 Term | det hon kallade en föreningsangelägenhet, | EN 'a Society matter' | det hon kallade en angelägenhet för Sällskapet, |
| 414 | 1391 | 6 Typo | Ingen sitter i handfängsel. | 'handfängsel' is archaic/odd; handbojor (Ch25) | Ingen sitter i handbojor. |
| 415 | 1397 | Note vs letters / Term | "Utpressningsbreven till Fiona skrevs på föreningens brevpapper. Det tjocka, krämfärgade papperet med vattenstämplade linjer. | EN 'The blackmail notes … the Society's stationery … the laid lines' (= räfflade, Ch4/Ch22; not watermarked) | "Utpressningslapparna till Fiona skrevs på Sällskapets brevpapper. Det tjocka, krämfärgade papperet med de räfflade linjerna. |
| 416 | 1401 | Markup / 3 Mistranslation | "Och ni beskriver broschen som <it>safiren i dess hjärta</it>. | literal '<it>…</it>' markup printed in the text, removed (the English is not italic here); EN 'they describe' (the notes), MT 'ni' (you) | "Och de beskriver broschen som safiren i dess hjärta. |
| 417 | 1401 | 6 Typo | att ingen skulle komma på tanke att fråga | idiom | att ingen skulle komma på tanken att fråga |
| 418 | 1405 | 6 Term | ett sätt att rädda föreningen i de breven. | the Society = Sällskapet | ett sätt att rädda Sällskapet i de breven. |
| 419 | 1413 | 6 Term | "Taket faller in. Värmepannan håller på att ge upp. | the boiler = pannan | "Taket faller in. Pannan håller på att ge upp. |
| 420 | 1413 | 6 Term | varenda brev och fotografi och köpekontrakt, | deed = köpebrev | varenda brev och fotografi och köpebrev, |
| 421 | 1427 | Note vs letters | Men breven visste att värdshuset köptes | EN 'the notes knew' — the sentence goes on to say it was 'never in any Blackburn letter', so the two words must differ | Men lapparna visste att värdshuset köptes |
| 422 | 1427 | 6 Term / 5 Address | En lagfart. Och lagfarten till det här värdshuset låg ute ur sin låda i er omplaceringskorg i går morse, framtagen, | deed = köpebrev; the refile basket (Ch23); du | Ett köpebrev. Och köpebrevet till det här värdshuset låg ute ur sin låda i din återarkiveringskorg i går morse, framtaget, |
| 423 | 1431 | 6 Term | Du stod för lagfarten. | deed = köpebrev | Du stod för köpebrevet. |
| 424 | 1431 | 5 Idiom | Han kunde inte korsa den här staden obemärkt för sitt liv, | EN 'to save his life' | Han kunde inte korsa den här staden obemärkt om så hans liv hängde på det, |
| 425 | 1431 | 6 Term | med dina parkeringsbiljetter. | parking passes (Ch20) | med dina parkeringstillstånd. |
| 426 | 1431 | 4 Pronoun | Hon behövde någon som kunde röra sig | EN 'He needed someone' (Theo) | Han behövde någon som kunde röra sig |
| 427 | 1435 | 6 Term | och talade om föreningen, | the Society | och talade om Sällskapet, |
| 428 | 1439 | 5 Address | och jag har skulder som ni inte skulle tro, sådana som inte låter er sova, | du per the series rule; generic you | och jag har skulder som du inte skulle tro, sådana som inte låter en sova, |
| 429 | 1439 | 6 Term | och att det skulle rädda föreningen, | the Society | och att det skulle rädda Sällskapet, |
| 430 | 1443 | 3 Reversed meaning | Jag tänkte bara på pengarna och på att få sova. | EN 'the money and the not-sleeping' | Jag tänkte bara på pengarna och på sömnlösheten. |
| 431 | 1454 | Note vs letters | De två breven blev bevisföring, märkta och arkiverade. | EN 'The two notes became evidence' | De två lapparna blev bevismaterial, märkta och arkiverade. |
| 432 | 1456 | 3 Reversed meaning | som varken var en fängelsecell eller en ovillkorlig dom. | EN 'neither a prison cell nor a free pardon'; MT 'an unconditional sentence' | som varken var en fängelsecell eller en fri benådning. |
| 433 | 1458 | 6 Term | "Restorativ rättvisa," | same term as Ch25 | "Reparativ rättvisa," |
| 434 | 1462 | 6 Term | och att lämna borgmästarexpeditionen. | EN 'the mayor's office' | och att lämna borgmästarens kontor. |
| 435 | 1466 | 1 Untranslated | Han avgick som ordförande för Frost Falls Historical Society, | the Society's name left in English; as Ch4 | Han avgick som ordförande för Frost Falls historiska sällskap, |
| 436 | 1468 | 8 Units (idiom) | börja förtjäna tillbaka en tum i taget av den plats | EN 'an inch at a time' (figurative) | börja förtjäna tillbaka, bit för bit, den plats |
| 437 | 1470 | 6 Typo | och det var en mans gråt som hade ställt in sig på galgen | relative clause | och det var gråten hos en man som hade ställt in sig på galgen |
| 438 | 1476 | 6 Typo | Pip väntade på det nedersta trappstegen | typo | Pip väntade på det nedersta trappsteget |
| 439 | 1482 | Note vs letters | Fiona var fri. Breven hade upphört. | EN 'The notes had stopped' | Fiona var fri. Lapparna hade upphört. |
| 440 | 1489 | 4 Proper name | Worthingtons kom för att leta upp mig | EN 'The Worthingtons' | Familjen Worthington kom för att leta upp mig |
| 441 | 1490 | 4 Proper name | De välpolerade, vänliga Worthingtons hade, | EN 'the Worthingtons' | De välpolerade, vänliga makarna Worthington hade, |
| 442 | 1490 | 3 Mistranslation | till en olämplig handling. | EN 'a bad place'; 'olämplig' = inappropriate | till en dålig handling. |
| 443 | 1490 | 6 Term | Mr. Worthington hittade mig på värdshusets veranda under deras sista morgon, | Mr. -> herr | Herr Worthington hittade mig på värdshusets veranda på deras sista morgon, |
| 444 | 1491 | 6 Term | "Mrs. Claus," sa han. | Mrs. -> fru | "Fru Claus," sa han. |
| 445 | 1491 | 3 Mistranslation | Jag skriver gärna checken innan vi åker i morgon bitti. | EN 'before we go this morning' — it is their last morning | Jag skriver gärna checken innan vi åker i förmiddag. |
| 446 | 1495 | 6 Term | du har, Mr. Worthington," | Mr. -> herr | du har, herr Worthington," |
| 447 | 1497 | 6 Term | är bara uppskjutet, Mr. Worthington. | Mr. -> herr | är bara uppskjutet, herr Worthington. |
| 448 | 1498 | 6 Term | Mr. Worthington betraktade mig länge, | Mr. -> herr | Herr Worthington betraktade mig länge, |
| 449 | 1499 | 6 Term | pengar, Mrs. Claus." | Mrs. -> fru | pengar, fru Claus." |
| 450 | 1500 | 3 Mistranslation | "Inte till din välvilja, den gör jag mig aldrig av med. | EN 'Not your kindness, never that' | "Inte till din välvilja, aldrig till den. |
| 451 | 1500 | 3 Mistranslation | Låt den hålla sina bakluckeloppisar | EN 'bake sales' (Ch12 'basarer'); 'bakluckeloppis' = car-boot sale | Låt den hålla sina kakförsäljningar |
| 452 | 1501 | 6 Term | Mrs. Worthington log då, | Mrs. -> fru | Fru Worthington log då, |
| 453 | 1503 | 6 Typo | med ett tak som läkte och en panna | 'läkte' = healed; the roof leaks | med ett tak som läckte och en panna |
| 454 | 1504 | 6 Typo | för en principstarks skull | 'principstark' is an adjective | för en princips skull |
| 455 | 1505 | 3 Mistranslation | bakluckeloppisar, lotterier och den långsamma, enstaka generositeten | EN 'bake sales … the slow, stubborn generosity'; 'enstaka' = occasional | kakförsäljningar, lotterier och den långsamma, envisa generositeten |
| 456 | 1511 | 3 Mistranslation | modigare än att möta Theo mitt i det lilla rummet. | EN 'across the little sitting room' | modigare än att möta Theo tvärs över det lilla sällskapsrummet. |
| 457 | 1515 | 6 Term | få av sig rocken. | coat = kappa | få av sig kappan. |
| 458 | 1525 | 3 Mistranslation | Ingen drog efter andan. | EN 'Nobody recoiled' | Ingen ryggade tillbaka. |
| 459 | 1527 | 6 Term | Martha sa det sannaste om saken, i ringen, | the circle = cirkeln (Frost and Found / Flour Play SV) | Martha sa det sannaste om saken, i cirkeln, |
| 460 | 1529 | 3 Mistranslation | för jag kände till en sådan saknad när jag var ung, verklig saknad, | EN 'want' = poverty; 'saknad' = longing/missing someone | för jag visste vad sådan nöd var när jag var ung, verklig nöd, |
| 461 | 1543 | 6 Term | Martha grep tag i min hand i ringen en grå eftermiddag, | the circle = cirkeln | Martha grep tag i min hand i cirkeln en grå eftermiddag, |
| 462 | 1545 | 6 Term | Att en ring är till för att luta sig mot?" | the circle = cirkeln (echo of Ch5 'Det är hela poängen med en cirkel') | Att en cirkel är till för att luta sig mot?" |
| 463 | 1549 | 6 Term | Du lutade dig inte bara mot ringen när du behövde det. Du var ringen, för Fiona, | the circle = cirkeln | Du lutade dig inte bara mot cirkeln när du behövde det. Du var cirkeln, för Fiona, |
| 464 | 1551 | 3 Mistranslation | som om hon inte just hade monterat ner mig totalt där jag satt. | EN 'undone me entirely'; 'monterat ner' = dismantled | som om hon inte just hade fått mig att falla helt i bitar där jag satt. |
| 465 | 1553 | 6 Typo | och sträckt mig varje kyla morgon efter en kappa | typo | och sträckt mig varje kall morgon efter en kappa |
| 466 | 1553 | 6 Typo | hade kappan gått in. | echo of 'ännu inte var ingången' | hade kappan blivit ingången. |
| 467 | 1555 | 3 Mistranslation | nästan alla guldgula vid det här laget, | EN 'gold' | nästan alla gyllene vid det här laget, |
| 468 | 1557 | 3 Mistranslation | Sällskapet behövde städas upp efter Theo, | EN 'needed sorting' | Sällskapet behövde ordnas upp efter Theo, |
| 469 | 1558 | 6 Term / 3 Mistranslation | hade samlats på byallmänningen, lagt ner stadens skatter i en låda och grävt ned den | the green = allmänningen; EN 'sealed up a box' | hade samlats på allmänningen, förseglat en låda med stadens skatter och grävt ned den |
| 470 | 1561 | 8 Units | och allmänningen är på fyra tunnland. Den ligger under almen. Den har suttit där hela tiden." | EN 'four acres' (SAFE: 1.6 ha); 'tunnland' is an old Swedish unit (~0.5 ha), not acres | och allmänningen är på drygt ett och ett halvt hektar. Den ligger under almen. Den har legat där hela tiden." |
| 471 | 1570 | 6 Typo / Term | En stund senare kom Bram kuta över allmänningen och vridande på sin keps, | grammar; his cap = mössa (Ch10) | En stund senare kom Bram kutande över allmänningen och vred sin mössa, |
| 472 | 1570 | 4 Proper name | Dansös den här gången, | reindeer name 'Dancer' as Ch10 and Frost and Found SV | Dancer den här gången, |
| 473 | 1571 | 6 Term | "Spärren, fru Claus!" ropade Bram och kom fram och var andfådd. | the latch = regeln (Ch10) | "Regeln, fru Claus!" ropade Bram andfådd när han kom fram. |
| 474 | 1571 | 6 Typo | besturen går dit folket är, | typo | bestarna går dit folket är, |
| 475 | 1572 | 4 Proper name | slå armarna om Dansös hals. | reindeer name | slå armarna om Dancers hals. |
| 476 | 1573 | 4 Proper name | ställa sig under Dansös nos | reindeer name | ställa sig under Dancers nos |
| 477 | 1573 | 6 Typo | som skulle kretsa där tills vi kom hem. | EN 'by the time we got home' | som skulle kretsa där när vi kom hem. |
| 478 | 1577 | 6 Term | gräsplanen sopats av | EN 'the green swept' | allmänningen sopats |
| 479 | 1582 | 6 Typo | Det är lite som är meningen med det. | garbled | Det är ju lite det som är meningen med det. |
| 480 | 1591 | 3 Mistranslation | Järneken låg i den, | EN 'standing in … water' | Järneken stod i den, |
| 481 | 1606 | 8 Units (idiom) | En centimeter i taget. | EN 'An inch at a time' (figurative) | Ett litet steg i taget. |
| 482 | 1614 | 3 Mistranslation | en hel säsong av bakluckeloppisar och enveten liten generositet | EN 'bake sales and stubborn small generosity' (as Ch28) | en hel säsong av kakförsäljningar och envis liten generositet |
| 483 | 1614 | 8 Units (idiom) | centimeter efter hård centimeter. | EN 'inch by hard inch' (figurative) | steg för mödosamt steg. |
| 484 | 1615 | 6 Typo | hela vägen från polen, | the Pole = Polen | hela vägen från Polen, |
| 485 | 1634 | Excerpt | Varje kvinna i ringen hade tagit med sin egen ädelgran, och jag hade tagit med Nordpolens sätt att binda den på, vilket Olivia hade svurit på att stjäla från mig före jul. Jag fäste ståltråden vid stommen långsamt, så att alla kunde följa med. Först därefter s … | adapted from corrected Flour Play SV Ch1 [40] — this excerpt's EN reads 'the shop's own wool' | Varje kvinna i cirkeln hade med sig sin egen ädelgran, och jag hade tagit med Nordpolens sätt att binda den, vilket Olivia hade svurit på att stjäla från mig före jul. Jag fäste ståltråden vid stommen långsamt, så att alla kunde följa med. Först därefter sträc … |
| 486 | 1635 | Excerpt | Snön hade fallit under natten. Inte oktobers tidiga snö, som försvunnit igen i en svit av milda dagar. Riktig snö. Den djupårstyp som hade börjat vid halloween och skulle ligga kvar till våren. Den låg längs med Evergreen Avenue nu i ett rejält, rent lager på  … | adapted from corrected Flour Play SV Ch1 [42] — EN 'Over the weekend the shops had traded' (FP final: 'Overnight … started'); FP's 'rent lagom' read as 'rent lager' (FP follow-up) | Snön hade fallit under natten. Inte den tidiga snön i oktober, som försvann igen efter ett par milda dagar. Riktig snö. Den djupsäsongsbetonade sorten som hade börjat vid halloween och skulle ligga kvar till våren. Den låg längs Evergreen Avenue nu i ett gott, … |
| 487 | 1636 | Excerpt | "Sakta ner," sa Olivia och lutade sig fram från nästa stol. "Jag kan inte stjäla det om jag inte kan se det." | verbatim from corrected Flour Play SV Ch1 [44] (EN identical) | "Sakta ner," sa Olivia och lutade sig fram från stolen intill. "Jag kan inte stjäla det om jag inte kan se det." |
| 488 | 1637 | Excerpt | Jag saktade ner för henne. Jag lade tre kvistar mot stommen, band dem med två varv ståltråd och lade nästa knippe över det första så att det dolde bindningen. | verbatim from corrected Flour Play SV Ch1 [46] (EN identical) | Jag saktade ner för hennes skull. Jag lade tre kvistar mot stommen, band dem med två varv ståltråd och lade nästa knippe över det första så att det dolde bindningen. |
| 489 | 1638 | Excerpt | – Varje kvist täcker den föregående, som fiskfjäll. Allihop pekande hemåt. | verbatim from corrected Flour Play SV Ch1 [48] (EN identical) | "Var och en täcker den föregående, som fiskfjäll. Alla pekar hemåt." |
| 490 | 1640 | Excerpt | – Min ser precis ut som din. | verbatim from corrected Flour Play SV Ch1 [52] | "Min ser precis ut som din." |
| 491 | 1642 | Excerpt | "Var är Nordpolen i den då?" | verbatim from corrected Flour Play SV Ch1 [56] (EN identical) | "Men var är Nordpolen i den?" |
| 492 | 1644 | Excerpt | Dot skrattade sitt korta, torra skratt tvärs över ringen, utan att titta upp från sin egen krans, som redan var hälften till storleken större än någon annans och dubbelt så tät. | adapted from corrected Flour Play SV Ch1 [60] — EN 'her own wreath' | Dot gav till sitt korta, torra skratt från andra sidan cirkeln, utan att titta upp från sin egen krans, som redan var hälften större än någon annans och dubbelt så tät. |
| 493 | 1645 | Excerpt | – Hon har varit efter ditt knep ända sedan den dagen du klev in. Hon var efter min å nittonåttio-någonting. | verbatim from corrected Flour Play SV Ch1 [62] | "Hon har varit ute efter ditt trick ända sedan den dag du klev in här. Hon var ute efter mitt nån gång på åttiotalet." |
| 494 | 1646 | Excerpt | Dot var bastant och grå och sa mycket i väldigt få ord. Hon hade gjort kransar i den butiken i årtionden. Det syntes på hennes händer. De stannade aldrig och fumlade aldrig. | verbatim from corrected Flour Play SV Ch1 [64] | Dot var bastant och gråhårig och sa mycket med väldigt få ord. Hon hade bundit kransar i den butiken i årtionden. Det syntes på hennes händer. De stannade aldrig upp och fumlade aldrig. |
| 495 | 1647 | Excerpt | Vi var alla där den morgonen. Hela ringen, när ingen var sängliggande med en förkylning eller passade barnbarn. Olivia vid dess huvud i sin egen butik, garnhärvor uppstaplade bakom henne i alla färger som en vinter kan önska. Dot bredvid henne, enkel och snabb … | adapted from corrected Flour Play SV Ch1 [66] — this excerpt's EN: 'her own shop', 'widow these many years', 'volunteered at the hospital three days a week' (older draft) | Vi var alla där den morgonen. Hela cirkeln, när ingen var sängliggande med en förkylning eller passade barnbarn. Olivia i spetsen för det hela i sin egen butik, med ullhärvor uppstaplade bakom sig i varje färg en vinter kan önska sig. Dot bredvid henne, enkel  … |
| 496 | 1648 | Excerpt | Och Pip, som inte var en del av ringen men skulle bli djupt kränkt av att lämnas utanför någon räkning över vilka som var närvarande. Hon hade installerat sig under det främre fönstret i den enda fläcken av låg novembersol, i ett bo hon hade byggt av en fallen … | adapted from corrected Flour Play SV Ch1 [68] — EN 'on the proceedings. On anything that shone, particularly.' | Och Pip, som inte tillhörde cirkeln men som skulle bli djupt kränkt om hon utelämnades ur någon räkning över vilka som var närvarande. Hon hade installerat sig under det främre fönstret i den enda fläcken av låg novembersol, i ett bo hon hade byggt av en falle … |
| 497 | 1649 | Excerpt | "Nu är knepet med kottarna," sa jag och höll upp en, "att man sätter ståltråd på dem innan man stoppar in dem, annars barrar de rakt ut på dig till nyår och du kommer att hitta guldiga kottar i soffan till våren – Pip. Pip, jag ser dig. Det där är inte till di … | verbatim from corrected Flour Play SV Ch1 [70] (EN identical) | "Tricket med kottarna nu," sa jag och höll upp en, "är att man sätter ståltråd om dem innan man stoppar in dem, annars barrar de rakt ut på dig vid nyår och så får man leta guldkottar i soffan ända till våren – Pip. Pip, jag ser dig. Det där är inte för dig." |
| 498 | 1650 | Excerpt | Pip hade rest sig och påbörjat en långsam, avslappnad drift över golvbrädorna mot guldbandet, med en varelse som låtsas vara på väg någon annanstans helhjärtat studerade likgiltighet. Hon stannade. Hon tittade i taket. Hon satte sig där hon var, som om det had … | verbatim from corrected Flour Play SV Ch1 [72] (EN identical) | Pip hade rest sig och påbörjat en långsam, oberörd glidning över golvbrädorna mot guldbandet, med en studerad likgiltighet som hos en varelse som låtsas vara på väg någon annanstans över huvud taget. Hon stannade. Hon tittade i taket. Hon satte sig där hon var … |
| 499 | 1651 | Excerpt | "Hon skäms inte för fem öre," sa Dot, med det som lät som godkännande. | verbatim from corrected Flour Play SV Ch1 [74] (EN identical) | "Hon har ingen skam i kroppen," sa Dot med något som lät som gillande. |
| 500 | 1652 | Excerpt | – Hon skäms ganska mycket, sa jag. – Hon sparar den helt enkelt till tillfällen då den gör henne någon nytta. Vilket detta inte är ett av. | verbatim from corrected Flour Play SV Ch1 [76] (EN identical) | "Hon skäms en hel del," sa jag. "Hon sparar det bara till tillfällen då det faktiskt kan göra henne någon nytta. Vilket detta inte är ett av." |
| 501 | 1653 | Excerpt | Jag gav Pip den blick som betyder att jag inte har slutat titta på dig, och hon gav mig den som betyder att jag inte har slutat vilja ha bandet, och vi förstod varandra. Jag återvände till mina granrisfjäll. | verbatim from corrected Flour Play SV Ch1 [78] (EN identical) | Jag gav Pip den blick som betyder att jag inte har slutat titta på dig, och hon gav mig den som betyder att jag inte har slutat vilja ha bandet, och vi förstod varandra. Jag återvände till mina grankvistar. |
| 502 | 1654 | Excerpt | Det slog mig då, när jag lade de små kvistarna den ena över den andra, hur långt jag hade färdats för att sitta där. Inte milen. Det fanns en väldig massa sådana, men jag menade inte milen. Inte för länge sedan hade jag varit nykomlingen i Frost Falls. Kvinnan … | verbatim from corrected Flour Play SV Ch1 [80] (EN identical) | Det slog mig då, när jag lade de små kvistarna omlott, hur långt jag hade färdats för att sitta där. Inte milen. Det var väldigt många sådana, men jag menade inte milen. Inte för länge sedan hade jag varit nykomlingen i Frost Falls. Kvinnan från Nordpolen med  … |
| 503 | 1655 | Excerpt | Klockan ovanför dörren plingade till, en pust av kall luft kom in, och bakom den, i en stor varm svallvåg, kom Greta. | verbatim from corrected Flour Play SV Ch1 [82] (EN identical) | Klockan ovanför dörren ringde, en pust av kall luft kom in, och bakom den, i en stor, varm flod, kom Greta. |
| 504 | 1656 | Excerpt | – Res er inte på grund av det här, tillkännagav hon, vilket ingen hade visat minsta tecken på att göra. Hon satte ner en bagerikardong stor som en hattask på bordet mellan kottarna och bandet, och satte händerna i sidorna för att syna oss. Greta ägde Holly Jol … | adapted from corrected Flour Play SV Ch1 [84]+[86] (this file keeps them in one paragraph) — EN 'her own doughnuts, round and warm' | "Ingen som reser sig," tillkännagav hon, vilket ingen hade visat minsta tecken på att göra. Hon ställde en bagerilåda i hattaskstorlek på bordet mellan kottarna och bandet, och satte händerna i sidorna för att syna oss. Greta ägde Holly Jolly Bakery längre ner … |
| 505 | 1657 | Excerpt | – Jag fick en plåt choklad- och pekannötsmuffins ur ugnen för inte en timme sedan och jag sa till mig själv, Greta, vem sitter i en kall butik och gör sig till nytta den här morgonen, och svaret var ni allihop, så var så goda. | verbatim from corrected Flour Play SV Ch1 [88] | "Jag fick en plåt choklad- och pekannötsmuffins ur ugnen för inte en timme sedan och så sa jag till mig själv, Greta, vem sitter i en kall butik och gör sig till nytta den här morgonen, och svaret var ni allihop, så var så god." |
| 506 | 1659 | Excerpt | – Någon måste göra det. Ni drägg kommer inte att göra det åt er själva. | from corrected Flour Play SV Ch1 [92] (EN "You lot" vs "You all", same sense) | "Någon måste göra det. Ni själva gör det då inte." |
| 507 | 1660 | Excerpt | Hon höll redan på att lyfta på locket. Doften vällde ut och blandades med ädelgranen mitt i rummet, choklad och pekannöt och farinsocker lagt över kallt grönt barr. Det var, tänkte jag, så nära doften av den kommande säsongen som något jag kände till. | adapted from corrected Flour Play SV Ch1 [94] — EN 'chocolate and pecan and brown sugar' | Hon höll redan på att lyfta på locket. Doften vällde ut och blandades med grandoften mitt i rummet, choklad och pekannöt och farinsocker lagt över kallt, grönt barr. Det var, tänkte jag, så nära doften av hela den kommande årstiden som något jag kände till. |
| 508 | 1661 | Excerpt | – Och det är ingefärskakor i botten, så se till att ni inte bara tar muffinsarna och lämnar kakorna, Dot, jag såg dig göra det på Logen och jag har inte glömt det. | from corrected Flour Play SV Ch1 [96] | "Och det ligger pepparkakor i botten, så att ni inte bara tar muffinsarna och lämnar kakorna, Dot, jag såg dig göra det på bygdegården och det har jag inte glömt." |
| 509 | 1662 | Excerpt | – Det var en enda gång, sa Dot, och de var mycket goda muffins. | verbatim from corrected Flour Play SV Ch1 [98] (EN identical) | "Det var en enda gång," sa Dot, "och det var väldigt goda muffins." |
| 510 | 1663 | Excerpt | Greta pekade ett mjöligt finger åt henne som upprättelse och började dela runt muffinsarna på pappersservetter. | verbatim from corrected Flour Play SV Ch1 [100] (EN identical) | Greta pekade ett mjöligt finger mot henne som till upprättelse och började dela ut muffinsarna på pappersservetter. |
| 511 | 1664 | Excerpt | Hon prackade på mig en muffins innan jag hade bett om det, och en till Claire, som protesterade och tog emot den. Hon stod över Martha tills Martha lovade att äta sin. Och först när alla hade en tog hon en själv. Hon åt den stående, medan hon tittade på när vi … | verbatim from corrected Flour Play SV Ch1 [102] (EN identical) | Hon prackade på mig en muffins innan jag hade bett om det, och en till Claire, som protesterade och tog emot den. Hon ställde sig över Martha tills Martha lovade att äta upp sin. Och först när alla hade en tog hon en själv. Hon åt den stående och såg på när vi … |
| 512 | 1665 | Excerpt | "Varför sitter ni alla och gör kransar?" frågade hon och nickade mot våra stommar med munnen full. | verbatim from corrected Flour Play SV Ch1 [104] (EN identical) | "Varför håller ni på och binder kransar allihop?" frågade hon och nickade mot våra stommar med munnen full. |
| 513 | 1666 | Excerpt | "Dörrkransar till affärerna," sa Olivia. "De betalar vad de vill, och vartenda öre går till Sällskapets takfond. Ivys är till kyrkan och Ellies till sjukhuset. De två ger vi bort." | verbatim from corrected Flour Play SV Ch1 [106] (EN identical) | "Dörrkransar till affärerna," sa Olivia. "De betalar vad de vill, och varenda cent går till Historiska sällskapets takfond. Ivys är till kyrkan och Ellies till sjukhuset. De där två skänker vi bort." |
| 514 | 1667 | Excerpt | Vi kastade oss över arbetet på allvar då, åtta kvinnor, en kartong muffins, en pingvin och en sovande hund. Pratet gick in och ut ur arbetet som ringprat brukar, en hel morgons små nyheter rymda i mellanrummen när vi band kvistar. Ivys dotter hade ett nytt job … | verbatim from corrected Flour Play SV Ch1 [108] (EN identical) | Vi kastade oss över arbetet på allvar då, åtta kvinnor, en kartong muffins, en pingvin och en sovande hund. Pratet flätades in i och ur arbetet som cirkelprat brukar, en hel morgons små nyheter som rymdes i utrymmena mellan bindandet av kvistar. Ivys dotter ha … |
| 515 | 1668 | Excerpt | Det var Claire som tog upp butiken, eftersom det var Claires yrke att märka att någonting har förändrats och alla andras enbart att skvallra om det efteråt. | verbatim from corrected Flour Play SV Ch1 [110] (EN identical) | Det var Claire som förde på tal det där med butiken, eftersom det låg i Claires natur att lägga märke till att någonting hade förändrats och i alla andras att bara skvallra om det efteråt. |
| 516 | 1669 | Excerpt | "Är det någon som vet vad som ska flytta in i gamla Fenwicks lokal?" frågade hon utan att titta upp. "Den tomma, förbi apoteket. Någon har tapetserat fönstren." | verbatim from corrected Flour Play SV Ch1 [112] (EN identical) | "Är det någon som vet vad som ska flytta in i gamla Fenwicks lokal?" frågade hon utan att titta upp. "Det tomma stället, förbi apoteket. Någon har satt upp papper för fönstren." |
| 517 | 1670 | Excerpt | Det fångade ringens uppmärksamhet från ståltråden. Gamla Fenwicks lokal hade stått tom ett bra år, med mörka fönster vid änden av ett ljust kvarter. Det var den typen av lucka i en rad butiker som folk lär sig att inte titta på, för att slippa känna det lilla  … | verbatim from corrected Flour Play SV Ch1 [114] (EN identical) | Det där flyttade cirkelns uppmärksamhet från ståltråden. Gamla Fenwicks lokal hade stått tom ett helt år, med mörka fönster i änden av ett ljust kvarter. Det var den sortens glugg i en rad av butiker som folk lär sig att inte titta på, för att slippa känna det … |
| 518 | 1671 | Excerpt | – Tapetserade hur? frågade Dot. | verbatim from corrected Flour Play SV Ch1 [116] (EN identical) | "Papper på vilket sätt?" frågade Dot. |
| 519 | 1672 | Excerpt | – Brunpapper, innanför glaset. Som man gör när man inreder en lokal och inte vill att staden ska titta på när man gör det. | verbatim from corrected Flour Play SV Ch1 [118] | "Brunpapper, på insidan av glaset. Som man gör när man gör i ordning en lokal och inte vill att stan ska stå och glo när man håller på." |
| 520 | 1674 | Excerpt | – Ingen skylt. Inget namn på tillståndstavlan heller än, jag kollade. Men det står en container på bakgården och det var en skåpbil där i lördags, och man hyr inte en container om man inte röjer ur ett utrymme. | adapted from corrected Flour Play SV Ch1 [122] — this excerpt's EN adds 'No name on the permit board yet either, I checked' | "Ingen skylt. Inget namn på tillståndstavlan än heller, jag kollade. Men det står en container på bakgården och det var en skåpbil där i lördags, och man hyr inte en container om man inte röjer ur en lokal." |
| 521 | 1675 | Excerpt | – Nå, sa Ivy med tillfredsställelse, någonting öppnar. På tiden. En mörk butik är en skam på en gata. | verbatim from corrected Flour Play SV Ch1 [124] | "Nå," sa Ivy med belåtenhet, "någonting öppnar i alla fall. Det var på tiden. En mörk butik är en skam för en gata." |
| 522 | 1676 | Excerpt | Det hördes ett allmänt mumlande av medhåll, eftersom folk i en stad som Frost Falls ser en tom butikslokal som en liten personlig sorg och en ny som en liten personlig gåva. | adapted from corrected Flour Play SV Ch1 [126] — this excerpt's EN keeps 'because folks in a town like Frost Falls …' | Ett allmänt samförståndssurr hördes, eftersom folk i en stad som Frost Falls ser en tom butikslokal som en liten personlig sorg och en ny som en liten personlig gåva. |
| 523 | 1677 | Excerpt | Jag vände på en granriskvist mellan mina klibbiga fingrar, och jag kände, av ingen anledning som jag kunde ha uppgivit för ringen, ett litet svalt stick av nyfikenhet i nackskinnet. Jag arkiverade det, som jag har lärt mig under en väldig massa år att arkivera … | adapted from corrected Flour Play SV Ch1 [128] — EN 'a small cool prickle … at the back of my neck', present 'I've learned' | Jag vände på en grankvist i mina klibbiga fingrar, och jag kände, utan någon som helst anledning som jag hade kunnat sätta ord på inför cirkeln, en liten sval ilning av nyfikenhet i nacken. Jag arkiverade den, som jag under ett mycket långt liv har lärt mig at … |
| 524 | 1678 | Excerpt | – Nå, vem det än är, sa Greta makligt och samlade ihop servetterna, – så kommer de att vilja ha mat precis som vem som helst. Jag ska ta med dem en paj den dagen de öppnar. | verbatim from corrected Flour Play SV Ch1 [130] (EN identical) | "Nå, vem det än är," sa Greta bekvämt och samlade ihop servetterna, "de vill nog ha mat i magen som folk mest. Jag tar med dem en paj den dagen de slår upp portarna." |
| 525 | 1679 | Excerpt | Det var Ellie, som gått till fönstret för att skaka av sig granrisbitar från ärmen, som fick syn på snögubben. | verbatim from corrected Flour Play SV Ch1 [132] (EN identical) | Det var Ellie, som gått bort till fönstret för att skaka av sig granbarr från ärmen, som fick syn på snögubben. |
| 526 | 1680 | Excerpt | – Nu är det där underligt, sa hon på sitt milda sätt, och något i mildheten fick oss alla att se upp. | adapted from corrected Flour Play SV Ch1 [134], first half (this file splits the paragraph) | "Nu är det där bra märkligt," sa hon på sitt milda sätt, och något i den mildheten fick oss alla att titta upp. |
| 527 | 1681 | Excerpt | – Låg inte barnens snögubbar vända mot vägen igår? | adapted from corrected Flour Play SV Ch1 [134], second half | "Stod inte barnens snögubbar vända mot vägen i går?" |
| 528 | 1682 | Excerpt | Grönområdet låg mitt emot Yarn Tales, en bred vit allmänning med bandstandet i ena änden och krigsmonumentet i den andra. Skolbarnen hade byggt en rad snögubbar längs det under den första riktiga snön. Tre stycken, tjocka och sneda och krönta med vad barnen än … | adapted from corrected Flour Play SV Ch1 [136] — this excerpt's EN: 'the bandstand at one end and the war memorial at the other', 'during the first good snow' | Allmänningen låg mitt emot Yarn Tales, en bred, vit gräsplan med musikpaviljongen i ena änden och krigsmonumentet i den andra. Skolbarnen hade byggt en rad snögubbar längs den under den första riktiga snön. Tre stycken, tjocka och sneda och krönta med vad barn … |
| 529 | 1683 | Excerpt | Den här morgonen hade den i mitten vänt sig helt om. | verbatim from corrected Flour Play SV Ch1 [138] (EN identical) | Den här morgonen hade den mellersta vänt sig helt om. |
| 530 | 1684 | Excerpt | Den stod med ryggen mot vägen nu, med pinnarmar utsträckta åt båda hållen, det klumpiga kolansiktet riktat bort upp över grönområdet mot butikerna. Mot, om man ville vara exakt med det, den bortre änden av kvarteret där den gamla Fenwicks lokal låg bakom sitt  … | adapted from corrected Flour Play SV Ch1 [140] — EN 'the long blue shadows of the bandstand rail'; FP typo 'obrutnen' -> 'obruten' (FP follow-up) | Den stod med ryggen mot vägen nu, med pinnarmarna utslagna åt båda håll, med det klumpiga kolansiktet vänt uppåt allmänningen mot butikerna. Mot, om man skulle vara noga med det, den bortre änden av kvarteret där gamla Fenwicks lokal låg bakom sitt brunpapper. … |
| 531 | 1685 | Excerpt | Vi trängdes alla mot fönstret, muffinsen bortglömda, och tittade. | verbatim from corrected Flour Play SV Ch1 [142] (EN identical) | Vi trängdes allihop vid fönstret, med muffinsarna bortglömda, och tittade. |
| 532 | 1686 | Excerpt | "Någons idé om ett skämt," konstaterade Dot. "Vridit på den under natten. Ungar." | verbatim from corrected Flour Play SV Ch1 [144] (EN identical) | "Någons skämt," konstaterade Dot. "Vridit på den under natten. Ungar." |
| 533 | 1687 | Excerpt | "Det finns inga spår," sa Claire. "Hur skulle de ha vridit den utan några spår?" | verbatim from corrected Flour Play SV Ch1 [146] (EN identical) | "Det finns inga spår," sa Claire. "Hur skulle de ha vridit den utan att lämna spår?" |
| 534 | 1688 | Excerpt | – Sopat bort dem bakom sig. Eller så blåste vinden igen dem. Det är ett skämt. Ett barn med kalla fingrar som inte har något bättre för sig. Det kommer att vara en hel rad av dem vända till på söndag, märk mina ord, när de andra ser att det går att göra. | adapted from corrected Flour Play SV Ch1 [148] — this excerpt's EN has no 'said Dot' and reads 'by Sunday, mark me' | "Borstat ut dem bakom sig. Eller så blåste vinden igen dem. Det är ett skämt. Något barntroll med kalla fingrar som inte hade något bättre för sig. Det kommer att vara en hel rad av dem som blivit vridna till på söndag, märk mina ord, när de väl märker att det … |
| 535 | 1689 | Excerpt | "Den behövde inte ens vridas. Allt någon behövde göra var att flytta ansiktet till andra sidan," sa Martha. | verbatim from corrected Flour Play SV Ch1 [150] (EN identical) | "Den behövde inte ens vridas. Allt som behövdes var att flytta ansiktet till andra sidan," sa Martha. |
| 536 | 1690 | Excerpt | Och det var den förnuftiga synpunkten, och ringen köpte den, och någon sa barnen nuförtiden och någon annan sa att det aldrig snöade så här när jag var ung, och pratet gick vidare, som ringprat brukar, och Ivy gick tillbaka för att ta en till ingefärskaka. Men … | adapted from corrected Flour Play SV Ch1 [152] + this excerpt's extra sentence 'And I didn't say what I was thinking.' | Och det var den förnuftiga synen, och cirkeln köpte den, och någon sa att ungarna nuförtiden och någon annan sa att det aldrig snöade så här när jag var ung, och samtalet gick vidare, som cirkelprat brukar göra, och Ivy gick tillbaka för att ta en pepparkaka t … |
| 537 | 1691 | Excerpt | Eftersom jag känner till skillnaden. Jag har levt en lång tid nu tillsammans med julens magi. Tillräckligt länge för att känna den i mina ben, lika tydligt som ett fotsteg på min egen trappa. Det här var inte ett barn med kalla fingrar. Magin var lös i Frost F … | adapted from corrected Flour Play SV Ch1 [154] — this excerpt's EN is in the present ('I know the difference. I've lived'), 'my own stair', 'warm and clumsy' | För jag känner till skillnaden. Jag har levt länge nu vid sidan av julens magi. Tillräckligt länge för att känna den i benmärgen, lika påtagligt som ett fotsteg i min egen trappa. Det här var inget barn med kalla fingrar. Magin var lös i Frost Falls. Den hade  … |
| 538 | 1692 | Excerpt | Jag tittade från den vända snögubben uppåt kvarteret mot den gamla Fenwicks lokals brunpappersförsedda fönster, exakt dit dess pinnarmar pekade, och tänkte att magin, vad man än i övrigt kunde säga om den, alltid hade haft en nos för det som spelade roll innan … | adapted from corrected Flour Play SV Ch1 [156] + this excerpt's extra clause | Jag flyttade blicken från den vridna snögubben uppåt kvarteret mot de brunpappersförsedda fönstren till gamla Fenwicks lokal, exakt dit dess pinnarmar pekade, och tänkte att magin, vad man än i övrigt kunde säga om den, alltid hade haft näsa för det som spelad … |
| 539 | 1693 | Excerpt | Men jag sa inget av detta till ringen. Jag tog en ingefärskaka, sa nej till Pip när hon tittade på smulorna, och satte mig ner vid min krans igen. Jag band fast granriset, kvist över kvist, allihop pekande åt samma håll. Bakom mig knäppte till en vedklabbe i k … | adapted from corrected Flour Play SV Ch1 [158] + this excerpt's extra sentence 'Something was starting.' | Men jag sa inget av detta till cirkeln. Jag tog en pepparkaka, sa nej till Pip när hon kastade lystna blickar på smulorna, och satte mig till rätta vid kransen igen. Jag band fast granen, kvist efter kvist, alla pekande åt samma håll. Bakom mig knäppte det til … |

### Book-wide rules
- 6 Term: `\bsade\b` → `sa` — attribution verb 'sa' (Flour Play SV / published series; MT mixed sa/sade) — 97 paragraph(s): 157, 162, 163, 166, 167, 168, 172, 175, 176, 180, 182, 187, 190, 219, 229, 249, 263, 265, 283, 295, 472, 480, 500, 504, 518, 528, 532, 540, 542, 571, 575, 603, 613, 627, 631, 640, 651, 654, 655, 656 …
- 6 Term: `\bSnöboll` → `Snowball` — Snowball = 'Snowball' (Frost and Found SV 38x, Flour Play SV) — 4 paragraph(s): 371, 378, 380, 1563
- Ruling 6 cider: `\bciderbordet\b` → `mustbordet` — cider is non-alcoholic (served to children): äppelmust — 2 paragraph(s): 255, 299
- Ruling 6 cider: `\bciderståndet\b` → `mustståndet` — cider is non-alcoholic: äppelmust — 1 paragraph(s): 1251
- Ruling 6 cider: `\bcidern\b` → `äppelmusten` — cider is non-alcoholic: äppelmust — 4 paragraph(s): 199, 281, 291, 1248
- Ruling 6 cider: `\bCider\b` → `Äppelmust` — cider is non-alcoholic: äppelmust — 1 paragraph(s): 1245
- Ruling 6 cider: `\bcider\b` → `äppelmust` — cider is non-alcoholic: äppelmust — 3 paragraph(s): 195, 1248, 1254

### Dialogue paragraphs converted (ruling 1) — 457
40, 44, 46, 48, 52, 53, 55, 57, 58, 59, 60, 63, 66, 67, 68, 69, 72, 73, 74, 75, 76, 79, 81, 82, 83, 85, 91, 96, 101, 102, 103, 104, 105, 107, 113, 118, 119, 121, 122, 124, 126, 128, 129, 130, 131, 134, 135, 136, 137, 138, 139, 140, 141, 144, 145, 149, 157, 158, 159, 160, 162, 163, 164, 166, 167, 168, 171, 172, 173, 174, 175, 176, 180, 182, 183, 184, 185, 186, 187, 188, 190, 207, 211, 215, 217, 219, 235, 239, 243, 247, 249, 251, 255, 259, 263, 267, 271, 275, 279, 285, 295, 310, 311, 312, 313, 318, 319, 321, 322, 323, 325, 327, 328, 329, 331, 335, 336, 338, 340, 342, 344, 345, 347, 349, 351, 353, 355, 356, 364, 366, 368, 372, 373, 375, 376, 380, 381, 382, 383, 386, 387, 388, 392, 395, 396, 397, 398, 402, 403, 411, 413, 417, 421, 425, 429, 433, 437, 441, 443, 445, 449, 451, 464, 468, 472, 474, 480, 482, 486, 490, 492, 494, 498, 504, 506, 510, 514, 518, 522, 526, 532, 536, 542, 544, 548, 561, 565, 569, 571, 573, 577, 581, 585, 589, 591, 595, 599, 603, 605, 609, 613, 627, 631, 635, 638, 640, 650, 651, 652, 655, 656, 657, 658, 661, 664, 667, 668, 669, 670, 672, 676, 677, 687, 688, 691, 693, 694, 698, 700, 701, 704, 706, 709, 711, 713, 714, 731, 733, 735, 743, 747, 754, 758, 760, 768, 772, 776, 778, 780, 784, 788, 794, 796, 800, 804, 808, 810, 814, 818, 820, 837, 841, 845, 851, 855, 859, 865, 869, 873, 875, 879, 883, 887, 900, 902, 906, 908, 912, 914, 916, 920, 922, 924, 926, 928, 930, 932, 936, 940, 944, 948, 952, 954, 956, 958, 966, 968, 975, 979, 983, 985, 987, 991, 997, 999, 1003, 1007, 1011, 1015, 1017, 1021, 1025, 1029, 1031, 1035, 1039, 1041, 1045, 1051, 1053, 1062, 1064, 1072, 1074, 1076, 1082, 1084, 1092, 1095, 1097, 1099, 1102, 1104, 1106, 1109, 1110, 1113, 1116, 1118, 1121, 1122, 1124, 1161, 1163, 1165, 1175, 1181, 1183, 1196, 1200, 1202, 1206, 1212, 1214, 1218, 1220, 1222, 1224, 1226, 1238, 1240, 1248, 1252, 1253, 1254, 1256, 1257, 1258, 1262, 1263, 1300, 1304, 1339, 1341, 1345, 1347, 1355, 1357, 1364, 1365, 1367, 1368, 1369, 1373, 1375, 1376, 1377, 1378, 1380, 1391, 1397, 1401, 1405, 1409, 1413, 1417, 1421, 1427, 1431, 1435, 1439, 1443, 1449, 1458, 1470, 1472, 1478, 1491, 1495, 1497, 1499, 1500, 1502, 1515, 1519, 1529, 1539, 1545, 1549, 1561, 1565, 1567, 1571, 1572, 1579, 1581, 1582, 1584, 1585, 1589, 1592, 1593, 1597, 1598, 1600, 1601, 1603, 1605, 1606, 1610, 1611, 1613, 1616, 1617, 1636, 1641, 1642, 1643, 1649, 1651, 1658, 1665, 1666, 1669, 1686, 1687, 1689
