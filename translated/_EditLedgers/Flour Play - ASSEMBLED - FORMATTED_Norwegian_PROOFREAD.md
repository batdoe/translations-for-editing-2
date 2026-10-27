# PROOFREAD — Flour Play - ASSEMBLED - FORMATTED_Norwegian (2026-10-26 run, done 2026-10-27)

- Edition: Norwegian Bokmål, Frost Falls Book 3. Input `translated\Flour Play - ASSEMBLED - FORMATTED_Norwegian.docx` (raw MT, never proofread). English: `translate_now\Flour Play - ASSEMBLED - FORMATTED.docx` (Oct 19 no-poison version). Output: `translated\corrected\Flour Play - ASSEMBLED - FORMATTED_Norwegian.docx`.
- Starting copy: the existing `corrected\` file (= input + the pre-flight's 4 asterisk-to-italic conversions at [1162] [1163] [1613]), backed up to `corrected\_bak\Flour Play - ASSEMBLED - FORMATTED_Norwegian.pre-proofread-20261027.docx`.
- Prior report: none (0/0 not found).
- Dossier norwegian.txt (dash dialogue, preteritum, du for everyone). Rulings FF_DECISIONS_BRIEF_20261013 1–7 + FF_PROOFREAD_BRIEF_20261026 incl. Lessons and the Flour Play section.
- Series sources: Inn Trouble NO (`corrected\`, 2026-10-26) first, then Frost and Found NO (`translated\`). FR/DE/IT/ES Flour Play ledgers used for the clue-term CHOICES only.
- Coverage: front matter, blurb, Ch 1–27, What's Next, Binder's Bequest excerpt. Every chapter read against the English, sequentially, no sub-agents.
- Paragraph numbers = index of `<w:p>` in document.xml (= python-docx `document.paragraphs`), NOT `paras()`.
- Input `bt_anchors check` (ruling 5): 18 spans, 0 unpaired. Non-titles: Sugarplum Patisserie, Yarn Tales, Starlight, Frosty's Groceries, Sugarplum, Holly Jolly, Doc Mitchell ×2, Frosty's, Evergreen, Nick, and two ENGLISH card texts ('What shall we send them, a hundred years on?', 'To be sealed when the old one is opened, at the new year.').
- Totals: 634 targeted fixes + 49 excerpt paragraphs replaced from the published Norwegian edition + 2 translator meta-notes deleted + 2 English card texts translated (italic) + 13 stray `<bt>` spans removed + 5 real-title anchors added + 66 dialogue paragraphs converted « » to dash. Refused: 0. Decisions logged: 6 (FP-NO-D1…D6), all applied provisionally or informational; none blocks the file.

## Worst defects
1. **The cold-room clue erased in the confrontation and the charges.** Ch23 [1781] `Klagen til kommunen omtalte butikklokalet hennes som kjølerommet og oppvaskkummen som Hobart-vasken` (the shop room called "the walk-in"; Joyce's giveaway word 'det kalde rommet' gone), and Joyce's defence [1782] `Halvparten på min alder sier kjølerom.` used GRETA's word, so her slip vanished. Ch24 [1840] charged her with 'Kjølerrommet og Hobart-vasken'. Now walk-in = **kjølerommet**, Joyce's word = **«det kalde rommet»**, hand-sink = **håndvasken**, her word = **«Hobart-vasken»**, identical in Ch9 [804] [808], Ch20 [1548] [1552], Ch22 [1692], Ch23 [1781] [1782], Ch24 [1840].
2. **Translator meta-notes printed in the prose (Ch15 [1162]–[1163]):** `– fylkesmannen i kilden er county man, her helse-/etatsinspektøren – … La oss bruke "tilsynsmennene" eller "kontrolløren" … for å bevare kildens "county man".` and `Retting: før mannen fra fylket …`. Deleted; the sentence completed as the English.
3. **Sour base had 6+ renderings**, three wrong in kind: `sur base` (a chemical contradiction), `surdeig` / `surdeigskultur` (= the sourdough STARTER the acid replaces — in Jessica's call to Greta, to Tanaka, and on Pelkey's invoice), `surdeigsbase`, `surdeigsgrunnlag`, `sure grunndeigen`, `en sur deig`. Unified to **syrningsmiddel** (acidulant) in Doc's analysis, Renée's search, the invoice, the confrontation and the charges.
4. **No-poison violation:** Ch18 [1407] `En forgiftet melkasse` (EN 'A dosed flour bin') → `En dosert meldunk`. No other gift/forgift/giftig in the book.
5. **English left in:** [614] a whole English paragraph (duplicate of [615]; emptied), [1242] an English sentence, [416] `was hardnet`, [2052] `Theo was`, [822] `waddlet`, [2312] the closing line, [1157] flyer 'Grand Opening Week', the two `<bt>` card texts [2078] [2140], [678] `hasp`, [499] `snipet` / `den alle`.
6. **Reversed / wrong meanings (sample):** [2142] the snowmen 'dozens of them where the children had built a handful' → NO 'where the children had built a whole heap'; [1307] 'she doesn't have to show you' → 'hun må ikke' (she must not); [1186] [1678] [2181] lines given to the wrong speaker; [1484] 'at suppertime' → 'i tretiden'; [1941] 'half past (two)' → 'halv fire'; [1404] 'bigger sum by half' → 'det dobbelte'; [972] 'A hundred feet' (footprints) read as a distance; [1218] 'two degrees under code' → 'to grader unna'; the blurb's 'a bored boy' → 'en utleid gutt' (a rented boy) and 'a brick' → 'brostein'.

## Clue chain (brief §Flour Play): one rendering each
- flour bin = **meldunk** (was melbøtte/melbinge/melkasse/binge/tønne/bøtte); order book = **bestillingsboken / Thanksgiving-bestillingsboken** (was protokoll, høsttakkefestens bestillingsbok, takksigelsesbestillingsbok, Takketakkingsordreboken); sour base = **syrningsmiddel**; 'ten times' = «Ti ganger så mye» / «i ti ganger dosen» (Ch11, one scene); Doc's 'Nothing I can name' = «Ingenting jeg kan navngi» (single occurrence); Doc's «Noen puttet det der. Og de visste nøyaktig hvor mye de skulle ha i.» quoted back identically in Ch15 [1176]; Renée's «Stakkars menneske. Så synd med alt trøbbelet hennes akkurat nå» quoted back identically [1178]; Varney's «En uke. Kanskje mer, hvis delene til håndvasken ikke kommer frem.» identical [794] [1160].
- grout / weather-strip / hand-sink = **fugen / tetningslisten / håndvasken** in Varney's list, Renée's recital, Jessica's accusations and Greta's repairs (was also dørlistene, værlistene, tettelisten, listverket, vasken, utslagsvasken, oppvaskkummen).
- 'two degrees under code' = «to grader under forskriftene» identical at [790] [1214] [1218] (decision FP-NO-D1).
- the old gate key = portnøkkelen; 'never changed' = «Jeg skiftet den aldri» / «Du skiftet den aldri» (echo restored, [1793]); the key was 'cut' (laget), not 'slipt'.
- Joyce's white baker's coat = **hvit bakerjakke** (was also bakerfrakken); Pete's 'smock' = kittel (was kjeledress); the shape at the back door = skikkelse (was skyggen); brick = **murstein** (teglstein ×9, brostein); Pete's locker = **kjølelageret** (skapet, lageret); Greta's back-door sill = dørstokk (karm / vinduskarm); the founder's line identical in Ch6 [594], the Gazette [621] and Ch26 [2122] (Ch26 had a different wording).

## Lessons checklist (FF_PROOFREAD_BRIEF)
- Note vs letters: Book-2 plot, n/a. The lawyer's letter stays 'brev'; the complaint is never 'brevet' ([1226] → 'klagen').
- No poison: fixed [1407]; none left (grep gift/forgift/giftig/toksisk).
- Units (SAFE rule unless stated): 'a foot high' 30 cm [342]; 'a foot, perhaps two' 30/60 cm [722]; 'six inches' 15 cm [694] (Ch1 was already metric); 'a quarter-inch' ½ cm [1403]; 'six clean feet' nearly 2 m [1405]; 'a few inches' [1771], 'an inch' [1791] → centimetres; 'fifty pounds' 23 kg [1343]; 'a pound of chocolate' et halvt kilo [1799]; '100 lb' 45 kilo [931] (FP-NO-D2); figurative inch idioms [477] [562] [615] [629] [1226] → millimeter / litt / smule / bit for bit / hårsbredd; [972] 'A hundred feet' = footprints → 'Hundre fotspor'. Kept: 'two degrees' (FP-NO-D1); [69] 'Ikke milene' (figurative; 'mil' is a native word; cf. ruling 4); [485] 'fire linjer' (column inches, idiomatic). Pre-flight's '2 imperial tokens' were 'tomme/tommer' [694] and 'pund' [931]; the spelled-out ones found by reading are listed above.
- Currency: [87] øre → cent, [483] krone → cent. No other krone/øre idiom.
- Snowball: 'Snowball' ×10 (= Books 1–2 NO). Pip she/her throughout.
- Circle: 'sirkelen' (= Frost and Found NO); strikkeklubben [368], kretsen [1103] [1113], gjengen [376] [380] [440], Syklubben [2046] fixed. See FP-NO-D4.
- Reindeer: none named. Cider: none in this book.
- Title page 'Kapittel 1' → `<bt>Flour Play</bt>` (as Inn Trouble NO); copyright line and legal boilerplate matched to Inn Trouble NO.
- 'Very nearly' = «Nær sagt.» (not reversed); the blurb has no Sam/debtor content.
- Narrative tense: preteritum in every chapter; the blurb was in the past, put back in the present like the English and Inn Trouble NO.
- Term variants unified: avenue = **alléen** (alleen ×12, avyen ×7, hovedgaten, 'halve allmenningen'); the green = **allmenningen** (Parken/parken ×4, plenen ×2, gressplenen, 'fra alleen' [334]); Historical Society = **Historielaget** (Selskapet ×16, museet ×10 → as Inn Trouble NO); the Grange = **grendehuset** (Losjen, Grange-salen ×5, bedehuset ×5, avholdslokalet, Samvirkelaget ×2, bygdelaget); Chief Tanaka = **politisjef** (Sjef/sjefen ×11, Lensmann ×4); Doc = **doktor Mitchell / Doktoren** (Frost and Found NO; Doc ×8, Dr.); town = byen (bygda ×6); balsam = **granbar** (barlind = yew ×7, edelgran ×6, balsamgran ×4, barblanding, barløv); hearth = **ildsted**, grate = **rist** (arnested, arnen, gruben, ristverket, 'ristet magien'); couverture = overtrekkssjokolade; gingersnaps = ingefærkjeks (pepperkaker, pekasiner); cinnamon rolls = kanelboller (kanelsnurrer); cocoa buns = kakaoboller; the chocolate-pecan = sjokolade-pekannpai (pekannøtter/-kaker ×8); mittens = votter (vante); inns = vertshus (kroer, gjestgiverier); 'Pelkey's' as in English (Pelkeys); Mr./Ms./Dr. → herr/fru/doktor; Thanksgiving always 'Thanksgiving'; coats: Jessica kåpe, men frakk, boys jakke (kappe/pels fixed).

## Address table used (ruling 2)
Norwegian dossier: **du for everyone** (formal De/Dem/Deres reads archaic), as Inn Trouble NO. Every pair is du (Jessica ↔ circle, Greta, Nick, Theo, Pete, Doc, Renée, Joyce, Tanaka, Varney, Danny, Anne Doucette); courtesy titles carry the register (fru Claus, herr Worthington, fru Wendt, fru Ott, frøken Bennett, herr Pelkey). Checked: 0 formal De/Dem/Deres. Fixed: [1927] Varney 'Kjøkkenet deres' → 'ditt' (to Greta alone).

## Dialogue (ruling 1)
- Book system: '– ' opening each turn (as the other 527 dash paragraphs and Inn Trouble NO), attribution after a comma, resumed speech opens a new '– '. Words quoted inside narration keep « » ([808] [1031] [1204] [1210] [1548] [1552] [1692] [1761] [1781] [1782] [1840] [1973], and the two reported remarks in narration [841]).
- Converted « » to dash: 66 paragraphs (Ch10, Ch11, Ch19): 847, 849, 851, 853, 857, 863, 867, 875, 877, 879, 881, 883, 899, 901, 903, 905, 907, 909, 911, 921, 922, 923, 927, 928, 929, 930, 931, 932, 933, 944, 946, 1429, 1431, 1432, 1433, 1434, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1445, 1446, 1447, 1448, 1451, 1452, 1453, 1454, 1455, 1457, 1459, 1460, 1461, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1475.
- Stray em-dash turn openers fixed [598] [612]; narration inside speech set off with dashes [668] [702]; the excerpt's '—' normalised to '–'.
- The MT split ~30 paragraphs at speech/narration boundaries (Ch22, Ch25 mostly); kept so the paragraph count does not change (formatter may merge).

## Stray `<bt>` (ruling 5)
- Removed (13): [209] Sugarplum Patisserie, [221] Yarn Tales, [265] Starlight, [283] Frosty's Groceries, [305] Sugarplum + Holly Jolly, [919] [920] Doc Mitchell (→ doktor/Doktor Mitchell), [936] Frosty's, [941] Evergreen, [943] Nick ('<bt>Nick</bt>en min' → 'Nick min'), [2078] and [2140] the two English card texts → translated identically to the Ch15 card [1149] and set in italics as in the English.
- Added (5) real-title anchors: title page [0], series list [16] [17] [18], closing line [2312]. Kept: The Binder's Bequest [25] [2247] [2253] [2257] [2258].
- Result: 10 spans, titles only Frost and Found / Inn Trouble / Flour Play / The Binder's Bequest; 0 unpaired.

## Excerpt: The Binder's Bequest
- A published Norwegian edition exists: `2buploaded\1. Binder's Bequest_Norwegian.docx` (title *Bokbinderens Arv*, series *Rygger og Trolldom*). The 50 excerpt paragraphs [2259]–[2308] align 1:1 with its Kapittel 1 [53]–[102]; 49 were replaced verbatim (1 already identical), with the dialogue dash '—' normalised to this book's '–'. Series name in the sell lines [2247] [2253] [2257] → 'Rygger og Trolldom' (title anchors kept for stamping). What's Next blurb fixed [2249] [2250] (ball name as published; the president, not Fiona, clutches the diary).

## Notes: formatter's job (ruling 7), not changed
- No Heading 1 anywhere. TOC [19]–[25] lists only 'Om denne boken / Kapittel 27 / Hva skjer nå? / Utdrag fra …' (Kapittel 1–26 missing); that line plus the old title page was the pre-flight's 'chapters 1 and 27 detected twice'. TOC 'Hva skjer nå?' differs from the back-matter heading [2248] 'Hva blir det neste?'.
- Scene breaks 61 vs EN 58: the extra three are back-matter separators [2245] (after Ch27), [2255], [2310]. Body chapters match the English.
- +33 paragraphs vs English = MT splits at speech boundaries (kept) + the emptied English duplicate [614] + the emptied meta-note [1163].
- [1613] 'Gazettes' became italic in the pre-flight asterisk conversion (EN not italic); left.

## Findings (Norwegian verbatim as found; para = document.xml index; all APPLIED)
| # | Para | Class | Norwegian (verbatim, before) | Why (English) | Corrected |
|---|---|---|---|---|---|
| 1 | 0 | 1 Title page | Kapittel 1 | title page carried a chapter label instead of the book title (EN 'Flour Play'); anchored as Inn Trouble NO [0] | <bt>Flour Play</bt> |
| 2 | 8 | 7 Copyright line | Opphavsrett 2026 tilhører Lisa Bouchard. | copyright line wording matched to Inn Trouble NO (ruling 7) | Copyright 2026 av Lisa Bouchard. |
| 3 | 12 | 7 Copyright line | Ingen del av denne utgivelsen kan reproduseres, distribueres eller overføres i noen form eller med noen midler, herunder fotokopiering, opptak eller andre elektroniske eller mekaniske metoder, uten forutgående skriftlig tillatelse fra utgiveren, unntatt slik det er tillatt i henhold til amerikansk opphavsrettslovgivning. | legal boilerplate matched verbatim to Inn Trouble NO (ruling 7) | Ingen deler av denne utgivelsen kan reproduseres, distribueres eller overføres i noen form eller med noen midler, herunder fotokopiering, opptak eller andre elektroniske eller mekaniske metoder, uten på forhånd innhentet skriftlig tillatelse fra utgiveren, unntatt det som er tillatt i henhold til amerikansk lov om åndsverk. |
| 4 | 14 | 3 Mistranslation | Enhver likhet med faktiske personer (levende eller døde), steder, bygninger og produkter er utilsiktet og skal ikke tas som intetsigende eller utledes. | 'skal ikke tas som intetsigende' (= must not be taken as meaningless) is nonsense for 'is intended or should be inferred'; matched to Inn Trouble NO | Ingen likhet med faktiske personer (levende eller avdøde), steder, bygninger og produkter er tilsiktet eller skal kunne utledes. |
| 5 | 14 | 7 Copyright line | figurer og hendelser | matched to Inn Trouble NO | skikkelser og hendelser |
| 6 | 16 | Ruling 5 | Frost and Found | series-page title anchored (real book title; as Inn Trouble NO) | <bt>Frost and Found</bt> |
| 7 | 17 | Ruling 5 | Inn Trouble | series-page title anchored (real book title) | <bt>Inn Trouble</bt> |
| 8 | 18 | Ruling 5 | Flour Play | series-page title anchored (real book title) | <bt>Flour Play</bt> |
| 9 | 29 | 6 Tense | Greta hadde laget den samme kanelbollen i førti år. Hun laget den morgenen etter ektemannens begravelse fordi hun ikke visste hva annet hun skulle gjøre med hendene. Denne uken kom den sur ut av ovnen, og det gjorde den neste omgangen også, og den etter den igjen. | blurb is in the present in the English and in Inn Trouble NO; the MT put it in the past | Greta har laget den samme kanelbollen i førti år. Hun laget den morgenen etter ektemannens begravelse fordi hun ikke visste hva annet hun skulle gjøre med hendene. Denne uken kommer den sur ut av ovnen, og det gjør neste omgang også, og den etter der igjen. |
| 10 | 31 | 6 Tense | Innen torsdag sto Greta i sitt eget bakeri og fortalte Jessica Claus at hendene hennes endelig hadde glemt hvordan. | blurb present tense (EN) | Innen torsdag står Greta i sitt eget bakeri og forteller Jessica Claus at hendene hennes endelig har glemt hvordan. |
| 11 | 33 | 3 Mistranslation | Så kom en brostein gjennom vinduet, og et ord ble hengt opp på treveggen med rødt der hvert eneste barn på Evergreen Avenue kom til å lese det på vei forbi. | EN 'a brick' (brostein = cobblestone; the body calls it 'mursteinen'); 'a word goes up on the clapboard in red' is paint, not 'hengt opp'; present tense | Så kommer en murstein gjennom vinduet, og et ord blir malt med rødt på kledningen der hvert eneste barn på Evergreen Avenue kommer til å lese det på vei forbi. |
| 12 | 35 | 3 Mistranslation | Byen grep til de enkle navnene: slakteren som lenket fast lasteporten, familien som lå etter med oljen, en utleid gutt med en stjålet boks. Jessica grep til det som passet – for hvem enn som gjorde dette, kjøpte pulveret, kjente dosen og leverte en klage som henviste til helseforskriften etter underparagraf. Det var ikke et raseri. Det var et håndverk. | EN 'a bored boy' (utleid = rented out); 'stolen can' = spray can; 'not a temper' = not a fit of anger; present tense | Byen griper til de enkle navnene: slakteren som lenket fast lasteporten, familien som ligger etter med oljeregningen, en uttråkket gutt med en stjålet sprayboks. Jessica griper til det som passer – for den som gjorde dette, kjøpte pulveret, kjente dosen og leverte en klage som siterte helseforskriften ned til underpunktet. Det er ikke et sinneutbrudd. Det er et håndverk. |
| 13 | 37 | 6 Idiom/Tense | Og i den lyse enden av alléen hadde et nytt konditori datert sin åpningsfest til den ene uken Holly Jolly kom til å være stengt. | 'datert sin åpningsfest til' is a calque of 'dated its grand opening to'; present tense | Og i den lyse enden av alléen har et nytt konditori lagt den store åpningen sin til den ene uken Holly Jolly kommer til å være stengt. |
| 14 | 39 | 3 Mistranslation | hadde tatt med sin egen barblanding | EN 'balsam' (balsam-fir boughs); unified to 'granbar' (MT had barblanding / barlind = yew) | hadde tatt med sitt eget granbar |
| 15 | 39 | 3 Mistranslation | etter den første nevefulle barlind. | 'barlind' = yew, not balsam fir | etter den første neven med granbar. |
| 16 | 57 | 6 Term | som skrev for avisen, | EN 'who wrote for the Gazette'; paper's name as in Inn Trouble NO | som skrev for Gazette, |
| 17 | 57 | 3 Mistranslation | snill og ukunstlet, | EN 'unhurried'; 'ukunstlet' = unaffected/artless | snill og rolig, |
| 18 | 61 | 6 Typo | gullkonger i sofaen | 'gullkonger' = gold kings; cones = kongler | gullkongler i sofaen |
| 19 | 67 | 3 Mistranslation | barlindskjellene mine | balsam = granbar (barlind = yew) | granbarskjellene mine |
| 20 | 69 | 3 Mistranslation | Det hadde jeg fortjent i en feilfri fart gjennom en hard høst, | EN 'I'd earned that quickly'; 'feilfri' = flawless | Det hadde jeg gjort meg fortjent til i full fart gjennom en hard høst, |
| 21 | 73 | 3 Mistranslation | hun var bygget som bollene sine, | EN 'built like her doughnuts' | hun var bygget som smultringene sine, |
| 22 | 77 | 3 Mistranslation | blandet seg med barlinden midt i rommet | balsam = granbar | blandet seg med granbaret midt i rommet |
| 23 | 77 | 3 Mistranslation | det er ingefærpekasiner i bunnen | EN 'gingersnaps' = ingefærkjeks (as [127] [133]); 'pekasiner' is not a word | det er ingefærkjeks i bunnen |
| 24 | 77 | 4 Proper name | jeg så du gjorde det på Losjen | EN 'the Grange' = community hall; Inn Trouble NO uses 'grendehuset' ('Losjen' = a lodge) | jeg så du gjorde det på grendehuset |
| 25 | 87 | Currency | hver eneste øre går til | EN 'every penny'; dollars/cents only (Inn Trouble NO has the same line with 'cent') | hver eneste cent går til |
| 26 | 103 | 3 Mistranslation | Jeg snudde en barlindkvist | balsam = granbar | Jeg snudde en granbarkvist |
| 27 | 107 | 3 Mistranslation | barlindrester | balsam = granbar (barlind = yew) | granbarrester |
| 28 | 115 | 6 Typo/Grammar | Femten centimeter rent natten-fall, | 'natten-fall' is not Norwegian (EN 'clean overnight fall') | Femten centimeter ren nysnø fra natten, |
| 29 | 133 | 3 Mistranslation | Jeg bandt barlinden fast, | balsam = granbar | Jeg bandt granbaret fast, |
| 30 | 136 | 2 Addition | Jeg dvelte ikke ved det, men dyttet døren til bakeriet opp, | 'Jeg dvelte ikke ved det' is not in the English ('I pushed the bakery door open') | Jeg dyttet døren til bakeriet opp, |
| 31 | 150 | 3 Mistranslation | mot en skål på bordet | EN 'saucer' | mot et tefat på bordet |
| 32 | 150 | 3 Mistranslation | at jeg ikke er blitt spissformet i hodet. | 'spissformet i hodet' (pointed in the head) is meaningless; EN 'going soft in the head' | at jeg ikke er i ferd med å bli blød i hodet. |
| 33 | 160 | 3 Mistranslation | knipe seg i det og så le av det. | EN 'wince then laugh about it'; 'knipe seg i det' = pinch herself | skjære en grimase og så le av det. |
| 34 | 174 | 6 Term (clue) | En protokoll lå oppslått på disken, | this 'ledger' is Greta's order book (clue item) = 'bestillingsboken' throughout | En bestillingsbok lå oppslått på disken, |
| 35 | 176 | 2 Omission | Disse neste ukene er hele året mitt, | EN 'These next six weeks' | Disse seks neste ukene er hele året mitt, |
| 36 | 180 | 3 Mistranslation | Ett brett kunne gå galt en uke morgen, | EN 'on a bad morning'; 'en uke morgen' is garbled | Ett brett kunne gå galt en dårlig morgen, |
| 37 | 188 | 3 Mistranslation | til det utspilte melet på flisene | EN 'the spilled flour'; 'utspilt' = splayed | til det sølte melet på flisene |
| 38 | 190 | 3 Mistranslation | Så vegret hun seg. | EN 'Then she recoiled'; 'vegret seg' = refused | Så for hun tilbake. |
| 39 | 192 | 3 Mistranslation | som om hun hadde blitt knipebiterskt bitt, | 'knipebiterskt bitt' is not Norwegian; EN 'as though she'd been pinched' | som om noen hadde klypt henne, |
| 40 | 192 | 3 Mistranslation | Hun linet seg rundt det i en vid bue | 'linet seg' is not a word; EN 'sidled around it' | Hun gikk rundt det i en vid bue |
| 41 | 200 | 3 Mistranslation | skrudde lokket på og stakk det i pappen, | EN 'put it in my coat'; 'pappen' = the cardboard | skrudde lokket på og stakk det i kåpelommen, |
| 42 | 209 | 3 Mistranslation | kvelden kransetreet ble tent. Innen morgenen visste alle på hovedgaten | EN 'the night of the wreath circle' (no tree was lit); avenue = 'alléen' | samme kveld som sirkelen laget kranser. Innen morgenen visste alle i alléen |
| 43 | 211 | 6 Grammar | noe som var uvanlig til Kelly å være. | garbled comparison | noe som var uvanlig for Kelly. |
| 44 | 221 | 3 Mistranslation | mørkt glass og brungult papir, | EN 'brown paper' (as Ch1) | mørkt glass og brunt papir, |
| 45 | 221 | 3 Mistranslation | En lyslenke av granbar hang over døren, | EN 'A swag of greenery'; 'lyslenke' = a string of lights (the lights come later in the sentence) | En guirlande av granbar hang over døren, |
| 46 | 237 | 6 Grammar | at dere har klart oss. | reflexive pronoun wrong ('klart oss') | at dere har klart dere. |
| 47 | 249 | 3 Mistranslation | Frost Falls kommer til å bli en hvilepute. | EN 'is going to be a rest'; 'hvilepute' = a complacent resting-place | Frost Falls kommer til å bli rene ferien. |
| 48 | 253 | 3 Mistranslation | smør og sjokolade i pallvis, | EN 'couverture'; the joke turns on Renée explaining the trade word | smør og overtrekkssjokolade i pallvis, |
| 49 | 253 | 3 Mistranslation | Hun fortsatte om sjokoladen, langsomt, | EN 'She went on to the couverture' | Hun fortsatte om overtrekkssjokoladen, langsomt, |
| 50 | 253 | 6 Typo | stivner med et knekke. | 'et knekke' → 'et knekk' | stivner med et knekk. |
| 51 | 255 | 3 Mistranslation | Jeg hadde visst at sjokolade var til dypping | EN 'I had known that couverture was for dipping'; plain 'sjokolade' made Jessica's point absurd | Jeg hadde visst at overtrekkssjokolade var til dypping |
| 52 | 265 | 3 Mistranslation | Jeg bar resten av kakeboksene tilbake | EN 'the rest of the financiers' (there was one box) | Jeg bar resten av financierne tilbake |
| 53 | 293 | 3 Mistranslation | puttet det bort i pelsen, | EN 'put it away in his coat'; 'pelsen' = his fur | puttet det bort i frakken, |
| 54 | 299 | 3 Mistranslation | og snakket om det allerede i fri flyt på gaten, hjulpet frem så altfor varsomt | 'snakket' read as a verb (Greta talking); EN 'the talk about it already loose on the street, helped along ever so gently' | og pratet om det allerede i omløp på gaten, hjulpet frem aldri så varsomt |
| 55 | 308 | 3 Mistranslation | Hele fasaden var gjort om på. | EN 'She had the front done over entirely' = the front room, cleaned (next sentences: floor, cases); 'fasaden' = the exterior | Hele butikklokalet var gjort i stand. |
| 56 | 310 | 6 Term (clue) | Ikke bøtten. | EN 'Not the bin' = the flour bin ('meldunken', Ch2); 'bøtten' is the garbage bin in Ch2 | Ikke dunken. |
| 57 | 324 | 6 Term (clue) | unna melbøtten | flour bin = meldunken | unna meldunken |
| 58 | 334 | 3 Mistranslation | kald liten vind fra alleen. | EN 'off the green' = allmenningen (series term); 'alleen' = the avenue | kald liten vind fra allmenningen. |
| 59 | 338 | 6 Term | En rød teglstein | brick = murstein (24× vs teglstein 9×) | En rød murstein |
| 60 | 342 | 8 Units (SAFE) | røde bokstaver som var en fot høye. | EN 'a foot high' → 30 cm (exact, literal) | røde bokstaver som var tretti centimeter høye. |
| 61 | 342 | Ruling 3 | Det første ordet var DIRTY. Det andre var UNSAFE. | graffiti words translated (sign/label text) | Det første ordet var SKITTENT. Det andre var HELSEFARLIG. |
| 62 | 342 | Ruling 3 | kom tre til: DON'T EAT HERE. | graffiti translated; still three words | kom tre til: IKKE SPIS HER. |
| 63 | 346 | 6 Term (echo) | lever av ryktet sitt. | Jessica quotes Renée's Ch3 line 'A bakery lives on its name' ([241] 'lever av navnet sitt') — must echo it | lever av navnet sitt. |
| 64 | 346 | 6 Term | alleen | avenue spelled 'alléen' (22×) / 'alleen' (15×) / 'avyen' (7×); unified to 'alléen' | alléen |
| 65 | 348 | 6 Term | alleen | avenue spelled 'alléen' (22×) / 'alleen' (15×) / 'avyen' (7×); unified to 'alléen' | alléen |
| 66 | 350 | Ruling 3 | så på ordet DIRTY på treveggen | graffiti translated | så på ordet SKITTENT på treveggen |
| 67 | 356 | 3 Mistranslation | Vilje til faenskap ville ha skrevet noe personlig, | EN 'Spite would have written' | Ren ondskap ville ha skrevet noe personlig, |
| 68 | 356 | Ruling 3 | Hvem enn som hadde skrevet DIRTY og UNSAFE og DON'T EAT HERE, | graffiti translated | Den som hadde skrevet SKITTENT og HELSEFARLIG og IKKE SPIS HER, |
| 69 | 356 | 3 Mistranslation | Det var for ugjennomskuelig til å legges fram | EN 'too half-seen' (Jessica's own half-formed idea); 'ugjennomskuelig' = opaque | Det var for halvferdig en tanke til å legges fram |
| 70 | 362 | 6 Grammar | Han kastet én blikk på vinduet og én på Greta, | gender agreement (et blikk) | Han kastet ett blikk på vinduet og ett på Greta, |
| 71 | 368 | 6 Term | det meste av strikkeklubben bak seg, | the circle = 'sirkelen' (Book 1 NO and the rest of this book) | det meste av sirkelen bak seg, |
| 72 | 370 | 6 Typo | arbeidhansker | missing linking s | arbeidshansker |
| 73 | 372 | 3 Mistranslation | en stabel pappkanner, | EN 'paper cups'; 'kanner' = jugs | en stabel pappkrus, |
| 74 | 376 | 6 Term | og nesten hele gjengen kom opp gaten | EN 'most of the circle' | og nesten hele sirkelen kom opp gaten |
| 75 | 380 | 6 Typo/Term | Hun kom og stelte seg ved siden av meg, stødigere nå, med gjengen i full sving | 'stelte' typo; EN 'the circle' | Hun kom og stilte seg ved siden av meg, stødigere nå, med sirkelen i full sving |
| 76 | 392 | 6 Typo | og Ellie og jug fulgte etter henne, | 'jug' | og Ellie og jeg fulgte etter henne, |
| 77 | 406 | 3 Mistranslation | Sjåføren min tar innruten, | EN 'My driver does the inn run'; 'innruten' is opaque | Sjåføren min kjører ruten til vertshuset, |
| 78 | 408 | 6 Typo | Hun begynte i ytterkantene av glassfonsen | 'glassfonsen' | Hun begynte i ytterkantene av glassfonnen |
| 79 | 408 | 3 Mistranslation | nikket hun mot brettet ved døren. | EN 'the dustpan' | nikket hun mot feiebrettet ved døren. |
| 80 | 416 | 1 Untranslated English | en hånd som was hardnet av år med deig. | 'was hardnet' is English/garbled; EN 'a hand rough from years of dough' | en hånd som var ru etter år med deig. |
| 81 | 424 | 6 Term | ved siden av høsttakkefestens bestillingsbok som lå oppslått | Thanksgiving is 'Thanksgiving' everywhere else in the book; order book = bestillingsboken | ved siden av Thanksgiving-bestillingsboken, som lå oppslått |
| 82 | 440 | 3 Mistranslation | og gjengen hadde begynt å rusle av toppen til morgenrutinen sin, | EN 'the circle had begun to drift off to their mornings'; 'rusle av toppen' is garbled | og sirkelen hadde begynt å rusle hver til sitt, |
| 83 | 444 | 3 Mistranslation | Hun feiret det bort med nøklene. | EN 'She waved it off'; 'feiret' = celebrated | Hun vinket det bort med nøklene. |
| 84 | 446 | 6 Term | alleen | avenue spelled 'alléen' (22×) / 'alleen' (15×) / 'avyen' (7×); unified to 'alléen' | alléen |
| 85 | 448 | Ruling 3 | Du kunne fremdeles se hvor DIRTY hadde stått, | graffiti translated | Du kunne fremdeles se hvor SKITTENT hadde stått, |
| 86 | 451 | 6 Typo | snakket seg halvt harkehearse om Greta. | 'harkehearse' is a garbled English/Norwegian hybrid (EN 'half hoarse') | snakket seg halvt hese om Greta. |
| 87 | 451 | 6 Term | avyen | 'avyen' is not a Norwegian word; avenue = alléen | alléen |
| 88 | 453 | 3 Mistranslation | kom inn og stemplet inn med støvlene. | EN 'came in stamping'; 'stemplet inn' = clocked in | kom inn og stampet av meg snøen. |
| 89 | 453 | 6 Term | med edelgranen og den samme krukken | balsam = granbar (unified) | med granbaret og den samme krukken |
| 90 | 457 | 6 Term | en neve edelgran ved siden av | balsam = granbar | en neve granbar ved siden av |
| 91 | 459 | 6 Typo | lene Martha seg over tomrommet | verb form | lente Martha seg over tomrommet |
| 92 | 461 | 6 Term | Jeg bøyde meg over edelgranen | balsam = granbar | Jeg bøyde meg over granbaret |
| 93 | 471 | 6 Typo | Thanksgiving-pajene | 'pajene' | Thanksgiving-paiene |
| 94 | 477 | 8 Units (idiom) | ingen av dem kom til å rikke seg en tomme. | 'not give an inch' → idiomatic metric (as Inn Trouble NO) | ingen av dem kom til å rikke seg en millimeter. |
| 95 | 483 | Currency | ikke ville ha en krone for det. | EN 'a dime'; dollars/cents only | ikke ville ha en cent for det. |
| 96 | 487 | 3 Mistranslation | Jeg la kvistene mine, lyttet og holdt kjeft. | EN 'gave none of it back'; 'holdt kjeft' (shut my trap) is coarse for Jessica's narration | Jeg la kvistene mine, lyttet og sa ingenting selv. |
| 97 | 489 | 5 Register | siden jeg er gammel og gir faen. | EN 'old and past caring'; 'gir faen' (don't give a f—) is far stronger than the English in a cozy | siden jeg er gammel og ikke bryr meg lenger. |
| 98 | 495 | 6 Grammar | Dot tvunget en kvist på plass, | 'tvunget' is a participle; EN 'wound a sprig home' | Dot bandt en kvist på plass, |
| 99 | 495 | 3 Mistranslation | på grunn av den bakgårdsalleen siden i sommer. | EN 'that back alley' = smug ('allé' = avenue) | på grunn av det bakgårdssmuget siden i sommer. |
| 100 | 499 | 6 Typo/Register | Hun snipet av en ståltråd. – Drittsekkting å si om en baker. | 'snipet' is English; EN 'Filthy thing to say about a baker' | Hun klippet av en ståltråd. – En skitten ting å si om en baker. |
| 101 | 499 | 3 Mistranslation | har luskefart nede i den alle til alle døgnets tider | 'den alle' = the alley (English); 'luskefart' not a word | har lusket nede i smuget til alle døgnets tider |
| 102 | 505 | 3 Mistranslation | de beste beinene fra brygga si til Walters hund | EN 'on his dock' = loading dock; 'brygga' = a pier | de beste beinene på lasterampen sin til Walters hund |
| 103 | 515 | 3 Mistranslation | en malingsboks å avse til ren sjalusi. | EN 'spite'; 'sjalusi' = jealousy | en malingsboks å avse til ren ondskap. |
| 104 | 523 | 3 Mistranslation | En kjedelig gutt med en stjålet boks, | EN 'A bored boy' (kjedelig = boring); 'can' = spray can | En uttråkket gutt med en stjålet sprayboks, |
| 105 | 529 | 3 Mistranslation | det kunne være en kjedsommelig unge | EN 'a bored kid'; 'kjedsommelig' = tedious | det kunne være en uttråkket unge |
| 106 | 533 | 6 Term | binder edelgran | balsam = granbar | binder granbar |
| 107 | 539 | 6 Term | i vanten sin | mitten = vott (Book 1 NO, Ch15) | i votten sin |
| 108 | 557 | 6 Typo | som hadde falt av verandaforgjellet, | 'verandaforgjellet' not a word; EN 'porch rail' | som hadde falt av verandarekkverket, |
| 109 | 562 | 6 Term | Frost Falls historiske museum holdt til i | EN 'Historical Society' = Historielaget (Inn Trouble NO, 48×); MT used 'museum' through this chapter | Frost Falls historielag holdt til i |
| 110 | 562 | 8 Units (idiom) | så den ut til å ha blitt slitt en tomme til. | 'worn down another inch' → idiomatic (no imperial token) | så den ut til å ha blitt slitt enda litt mer. |
| 111 | 562 | 6 Grammar | som rakk om lag halvveis til å bli lunk og ikke lenger. | 'å bli lunk' is ungrammatical; EN 'got about halfway to warm and no further' | som rakk om lag halvveis til varm og ikke lenger. |
| 112 | 568 | 6 Typo | med en urmakertrekker i stedet for å tvinges. | 'urmakertrekker' (jeweler's screwdriver) | med en urmakerskrutrekker i stedet for å tvinges. |
| 113 | 568 | 6 Term | Han flikket på museet, stift for stift, | Historical Society = Historielaget | Han flikket på Historielaget, stift for stift, |
| 114 | 572 | 3 Mistranslation | trettheten han hadde båret på siden alle halloweens ulykker. | EN 'the tiredness he'd carried since Halloween'; 'alle halloweens ulykker' is an addition | trettheten han hadde båret på siden halloween. |
| 115 | 574 | 4 Title | Sjef Tanaka sier jeg skal | EN 'Chief Tanaka' = police chief; 'Sjef' alone = boss | Politisjef Tanaka sier jeg skal |
| 116 | 584 | 6 Term | Museets papirer hadde havnet i uorden | Historical Society = Historielaget | Historielagets papirer hadde havnet i uorden |
| 117 | 586 | 4 Title | – Sjef Tanaka har satt meg | Chief Tanaka = politisjef | – Politisjef Tanaka har satt meg |
| 118 | 596 | 6 Grammar | og husk for all del å huske hvordan | doubled 'husk … å huske' | og husk for all del hvordan |
| 119 | 598 | 1 Dialogue (ruling 1) | med begge hender. — De som | resumed speech opens with the book's dash '– ' (em dash stray) | med begge hender. – De som |
| 120 | 604 | 6 Term | der museet hadde gitt den hedersplassen, | Historical Society = Historielaget | der Historielaget hadde gitt den hedersplassen, |
| 121 | 606 | 6 Term | fra den kalde jorden under gressplenen helt | EN 'under the green' = allmenningen | fra den kalde jorden under allmenningen helt |
| 122 | 606 | 6 Term | Noen hadde lagt en kvist balsamedelgran ved siden av den. | balsam = granbar | Noen hadde lagt en kvist granbar ved siden av den. |
| 123 | 608 | 6 Typo | Han ristet på hovedet. | 'hovedet' (archaic/Danish spelling) | Han ristet på hodet. |
| 124 | 612 | 1 Dialogue (ruling 1) | hvor mye det nagde. — Hvem enn | resumed speech opens with '– ' | hvor mye det nagde. – Hvem enn |
| 125 | 614 | 1 Untranslated English | I let him have the humbleness, because it was true. But I saw how he wouldn't take one inch of ground that wasn't plainly his.  | stray English duplicate of the start of [615] (the Norwegian follows in [615]); text emptied, paragraph kept so the count is unchanged |  |
| 126 | 615 | 3 Mistranslation | Jeg lot ham beholde sjenertheten, | EN 'the humbleness'; 'sjenerthet' = shyness | Jeg lot ham beholde ydmykheten, |
| 127 | 615 | 8 Units (idiom) | ikke ville ta imot én tomme med ære som | 'one inch of ground' → idiomatic | ikke ville ta imot en eneste smule ære som |
| 128 | 615 | 6 Term | plassen i spissen for museet han elsket, | Historical Society = Historielaget | plassen i spissen for Historielaget han elsket, |
| 129 | 621 | 6 Term | var et fotografi av tegningen å finne i avisen, | EN 'in the Gazette' | var et fotografi av tegningen å finne i Gazette, |
| 130 | 621 | Ruling 3 | Der ordet SKITTEN hadde blitt vasket bort | graffiti word identical to Ch4 (SKITTENT) | Der ordet SKITTENT hadde blitt vasket bort |
| 131 | 623 | 6 Term | begynte folk å vende tankene sine mot museet. | Historical Society = Historielaget | begynte folk å vende tankene sine mot Historielaget. |
| 132 | 625 | 6 Term | Ta vare på museet | Hal's heading 'Keep the Society' (italic kept) | Ta vare på Historielaget |
| 133 | 627 | 4 Proper name | I går hos Frosty hørte jeg | shop name 'Frosty's' as elsewhere | I går hos Frosty's hørte jeg |
| 134 | 627 | 3 Mistranslation | – Så. En bønn om en tønne til museet. | EN 'A barrel for the Society'; 'En bønn om' (a plea for) is an addition | – Så. En tønne til Historielaget. |
| 135 | 629 | 8 Units (idiom) | hvordan han flikket tomme for tomme på en bygning | 'an inch at a time' → idiomatic | hvordan han flikket bit for bit på en bygning |
| 136 | 631 | 6 Term | – Museet er fremdeles i skikkelig trøbbel, | Historical Society = Historielaget | – Historielaget er fremdeles i skikkelig trøbbel, |
| 137 | 635 | 3 Mistranslation | Han puttet papiret i pelsen sin. | EN 'in his coat' | Han puttet papiret i frakken sin. |
| 138 | 639 | 3 Mistranslation | mellom den bygningen og rivningssekken. | EN 'the wrecking of it'; 'rivningssekken' is not a thing | mellom den bygningen og rivningskulen. |
| 139 | 641 | 6 Term | i museets fremre vindu: | Historical Society = Historielaget | i Historielagets fremre vindu: |
| 140 | 644 | 6 Term | på Selskapet | Historical Society = Historielaget (Inn Trouble NO 48×, Frost and Found NO); 'Selskapet' (the Company) was used 35× | på Historielaget |
| 141 | 646 | 6 Term | som vendte mot Parken fra den andre siden. | the green/the Park = allmenningen (series term) | som vendte mot allmenningen fra den andre siden. |
| 142 | 646 | 6 Typo | Han parterte en slaktahalvdel | 'slaktahalvdel' | Han parterte en slakthalvdel |
| 143 | 658 | 5 Register | Jeg holdt kjeft med vilje | EN 'I held my tongue'; 'holdt kjeft' is coarse in Jessica's narration | Jeg tidde med vilje |
| 144 | 664 | 3 Mistranslation | med aggresjonen slitt helt ut på utsiden av seg, | EN 'the resentment worn right out on the front of him'; garbled | med harmen båret helt utenpå seg, |
| 145 | 668 | 3 Mistranslation | og jeg vil ikke ta deg i å fange meg i det senere. | EN 'I won't have you catching me in it later'; reversed roles | og jeg vil ikke at du skal ta meg i det senere. |
| 146 | 668 | 1 Dialogue | og ja, kjeven hans arbeidet, jeg sa en ting | narration inside the speech must be set off (EN 'and yes,' his jaw worked, 'I said') | og ja – kjeven hans arbeidet – jeg sa en ting |
| 147 | 668 | 6 Grammar | og hun skyldes en unnskyldning som hun skal få | 'hun skyldes en unnskyldning' is ungrammatical; EN 'she's owed an apology' | og hun har en unnskyldning til gode som hun skal få |
| 148 | 668 | 6 Term | Det er ikke en sannhet om en stein gjennom en rute. | EN 'a brick through a window'; brick = murstein throughout | Det er ikke en sannhet om en murstein gjennom et vindu. |
| 149 | 678 | 6 Term/1 English | Jeg kommer ikke til å la skapet mitt stå ulåst fordi hun ikke gidder å bry seg med en skikkelig hasp. | Pete's 'locker' = his cold-storage locker ('kjølelageret', Ch5); 'hasp' is English (= krampe) | Jeg kommer ikke til å la kjølelageret mitt stå ulåst fordi hun ikke gidder å bry seg med en skikkelig krampe. |
| 150 | 678 | 6 Grammar | for at vi skal være oppfylt når vi åpner. | 'være oppfylt' = be fulfilled; EN 'to have us stocked by open' | for at vi skal ha fylt opp når vi åpner. |
| 151 | 678 | 3 Mistranslation | akkurat som for tjue år siden. Bare at nå har noen kastet en stein | EN 'same as twenty years' = for twenty years (not 'as twenty years ago'); brick = murstein | slik jeg har gjort i tjue år. Bare at nå har noen kastet en murstein |
| 152 | 686 | 6 Grammar | De morgener jeg er nede | definite plural | De morgenene jeg er nede |
| 153 | 686 | 6 Grammar | En av de morgener var det | definite plural | En av de morgenene var det |
| 154 | 692 | 3 Mistranslation | Han bredte ut de store hendene, bitrere og ærligere. | EN 'bitter and honest' (comparatives added) | Han bredte ut de store hendene, bitter og ærlig. |
| 155 | 694 | 8 Units (SAFE) | seks tommer som lå like ren | 'six inches' → 15 cm (as Ch1) | femten centimeter som lå like ren |
| 156 | 696 | 3 Mistranslation | eller mine som var spadd over. | EN 'mine tracked over'; 'spadd' = shovelled | eller mine egne som var tråkket over. |
| 157 | 696 | 6 Term | slakteren med skapet bak | Pete's locker = kjølelageret | slakteren med kjølelageret bak |
| 158 | 702 | 1 Dialogue | Og, han så ikke opp mens han rettet på hyssingrullen som ikke trengte retting, du får si til henne, | narration inside speech must be set off | Og – han så ikke opp mens han rettet på hyssingrullen som ikke trengte retting – du får si til henne, |
| 159 | 702 | 3 Mistranslation | angående den kaia, | EN 'that dock' = loading dock ('kaia' = a quay) | angående den lasterampen, |
| 160 | 712 | 3 Mistranslation | Om jeg hadde villet ha et enkelt navn på sirkelen han var ferdiginnpakket og bundet med hyssing i: | EN 'If I had wanted an easy name for the circle he was gift-wrapped and tied with his twine'; garbled | Om jeg hadde villet ha et enkelt navn å gi sirkelen, var han ferdig innpakket og bundet med hyssingen sin: |
| 161 | 712 | 6 Term | feiden, skapet, timene før daggry. | Pete's locker = kjølelageret | feiden, kjølelageret, timene før daggry. |
| 162 | 718 | 6 Term | alleen | avenue spelled 'alléen' (22×) / 'alleen' (15×) / 'avyen' (7×); unified to 'alléen' | alléen |
| 163 | 719 | 3 Mistranslation | Jeg tok på meg kappen. | EN 'coat'; 'kappe' = cape (fixed the same way in Inn Trouble NO) | Jeg tok på meg kåpen. |
| 164 | 722 | 8 Units (SAFE) | En fot, kanskje to. | 'A foot, perhaps two' → 30/60 cm | Tretti centimeter, kanskje seksti. |
| 165 | 722 | 3 Mistranslation | Han stod på tå i en fremoverlent stilling på sokkelen sin. | EN 'He stood tipped forward on his base'; 'på tå' (on tiptoe) is an addition | Han stod tippet fremover på sokkelen sin. |
| 166 | 723 | 3 Mistranslation | der en spøkfugl kunne ha stått for å måke. | EN 'to heave'; 'måke' = shovel; 'spøkfugl' typo | der en spøkefugl kunne ha stått for å dytte. |
| 167 | 723 | 3 Mistranslation | Bare snømannen selv, flyttet på og samlet i en fullstendig uskyldig positur som statuer som absolutt ikke har vært noen steder. | EN 'Only the snowmen themselves' (plural); simile garbled | Bare snømennene selv, flyttet og samlet, med den fullstendig uskyldige minen til statuer som absolutt ikke har vært noen steder. |
| 168 | 730 | 6 Grammar | Noe guttestreker. | agreement | Noen guttestreker. |
| 169 | 730 | 6 Term | alleen | avenue spelled 'alléen' (22×) / 'alleen' (15×) / 'avyen' (7×); unified to 'alléen' | alléen |
| 170 | 732 | 3 Mistranslation | De leste ikke alle den samme veien. | EN 'They were not all leaning the same way'; 'leste' = read | De lente seg ikke alle samme vei. |
| 171 | 733 | 6 Term | alleen | avenue spelled 'alléen' (22×) / 'alleen' (15×) / 'avyen' (7×); unified to 'alléen' | alléen |
| 172 | 735 | 3 Mistranslation | med ryggen til alleen som alle de andre lente seg mot, | EN 'its back to the lane' (Hollyhock Lane), not the avenue | med ryggen mot veien som alle de andre lente seg mot, |
| 173 | 736 | 6 Term (clue) | ved Gretas melkasse. | flour bin = meldunken (Ch2) | ved Gretas meldunk. |
| 174 | 736 | 6 Typo | hørte til resten av undret. | 'undret' → 'underet' | hørte til resten av underet. |
| 175 | 745 | 3 Mistranslation | over det kalde, tomme jernet, og ovenfor ristet magien i løse gulltråder, | EN 'over the cold, empty grate, and above the grate the magic hung'; 'ristet' = shook; grate = 'rist' (Inn Trouble NO) | over den kalde, tomme risten, og over risten hang magien i løse gulltråder, |
| 176 | 745 | 6 Grammar | som brant på lav bluss | gender | som brant på lavt bluss |
| 177 | 747 | 3 Mistranslation | som enhver unghund. | EN 'like any young thing'; 'unghund' = young dog | som alt som er ungt. |
| 178 | 755 | 6 Term | alleen | avenue spelled 'alléen' (22×) / 'alleen' (15×) / 'avyen' (7×); unified to 'alléen' | alléen |
| 179 | 756 | 3 Mistranslation | til å drømme seg oppover alleen, | EN 'mooning up the lane' (Hollyhock Lane) | til å drømme seg oppover veien, |
| 180 | 762 | 6 Term | Hun solgte pepperkaker til en kø | gingersnaps = ingefærkjeks (Ch1) | Hun solgte ingefærkjeks til en kø |
| 181 | 786 | Ruling 3 | holde seg foran ordet SKITTEN. | graffiti word as in Ch4 | holde seg foran ordet SKITTENT. |
| 182 | 790 | 6 Term (clue) | Glippe under bakdøren der dørlistene er slitt. | EN 'weather-strip' (one trade word, echoed by Renée in Ch16) = tetningslisten | Glippe under bakdøren der tetningslisten er slitt. |
| 183 | 790 | 6 Term (clue) | Han slo på kranen på vasken og holdt | EN 'the hand-sink' = håndvasken (clue term) | Han slo på kranen på håndvasken og holdt |
| 184 | 794 | 6 Term (clue) | hvis delene til vasken ikke kommer frem. | hand-sink = håndvasken | hvis delene til håndvasken ikke kommer frem. |
| 185 | 798 | 6 Term | sjokoladebollene | cocoa buns = kakaoboller (Ch15, Ch26) | kakaobollene |
| 186 | 802 | 6 Typo | spurde jeg, lett i tonen, | 'spurde' is Nynorsk; Bokmål 'spurte' | spurte jeg, lett i tonen, |
| 187 | 802 | 6 Typo | Men han ristet på hovedet | 'hovedet' | Men han ristet på hodet |
| 188 | 804 | 3 Mistranslation | halvparten av det bare ren granbarhet, og jeg luker ut det gretne på dørstokken | 'ren granbarhet' (pure fir-ness) is nonsense; EN 'half of it spite, and I sort the spite out on the doorstep' | halvparten av det ren ondskap, og jeg luker ut ondskapen på dørstokken |
| 189 | 804 | 3 Mistranslation (clue) | Den kom ferdig utskrevet, | EN 'It came in typed' — the typed complaint is a clue (Ch18 'en maskinskrevet klage') | Den kom maskinskrevet, |
| 190 | 810 | 3 Mistranslation/Ruling 3 | Ikke et kjedet barn med en boks maling som ville skrevet SKITTEN over en vegg fordi SKITTEN var alt | EN 'a bored child'; graffiti word as Ch4 | Ikke et uttråkket barn med en boks maling som ville skrevet SKITTENT over en vegg fordi SKITTENT var alt |
| 191 | 812 | 6 Term | ved siden av det sure melet og skyggen ved bakdøren i mørket, | EN 'the shape at the back door' = 'skikkelse' (Pete, Ch7) | ved siden av det sure melet og skikkelsen ved bakdøren i mørket, |
| 192 | 816 | 3 Mistranslation | i bokser for matfatet. | EN 'the food barrel' (Hal's barrel); 'matfatet' = the food platter | i bokser til mattønnen. |
| 193 | 816 | 6 Term | sjokoladebollene | cocoa buns = kakaoboller | kakaobollene |
| 194 | 818 | 3 Mistranslation | i en svart kappe, | EN 'coat' | i en svart kåpe, |
| 195 | 822 | 1 Untranslated English | Pip waddlet over gulvet | 'waddlet' = English verb | Pip vagget over gulvet |
| 196 | 830 | 6 Grammar | i hele denne grusomste saken. | superlative doubled | i hele denne grusomme saken. |
| 197 | 832 | 6 Grammar | satte seg rett ned for å holde med selskaper til Greta. | garbled; EN 'went straight in to sit with Greta' | gikk rett inn for å holde Greta med selskap. |
| 198 | 832 | 3 Mistranslation | Hal tok med seg esken med boller til matfatet. | EN 'for the barrel' | Hal tok med seg esken med boller til tønnen. |
| 199 | 841 | 3 Mistranslation | fylte en pose med hvetemelet som Hal | EN 'flour' ('hvetemel' needless) | fylte en pose med melet som Hal |
| 200 | 845 | 3 Mistranslation | med den særkrevne omsorgen han ga | EN 'fussy care'; 'særkrevne' is not a word | med den pirkete omsorgen han ga |
| 201 | 849 | 6 Typo | stolben og dybler. | 'stolben' typo; EN 'chair legs and dowels' | stolbein og plugger. |
| 202 | 855 | 3 Mistranslation | en tvinn med te. | EN 'a twist of tea' (paper twist) | et kremmerhus med te. |
| 203 | 861 | 6 Typo | ved helen min | 'helen' → 'hælen' | ved hælen min |
| 204 | 887 | 6 Term | En desperat mann kan kaste en stein. | brick = murstein | En desperat mann kan kaste en murstein. |
| 205 | 889 | 6 Term | Men steinen og malingen var | brick = murstein | Men mursteinen og malingen var |
| 206 | 889 | 6 Term (clue) | hvordan man nådde en binge bak en låst dør. | flour bin = meldunk | hvordan man nådde en meldunk bak en låst dør. |
| 207 | 907 | 6 Term (clue) | Og en vei til å nå en melbinge bak | flour bin = meldunk | Og en vei til å nå en meldunk bak |
| 208 | 911 | 3 Mistranslation | Ikke en gutteunge med en boks. | EN 'a boy with a can' (spray can) | Ikke en gutteunge med en sprayboks. |
| 209 | 915 | 3 Mistranslation | mot kirkekanten og det lille | EN 'the church end' (as [859] 'kirkenden') | mot kirkeenden og det lille |
| 210 | 917 | 3 Mistranslation | fordi jeg hadde levd lenge nok til å ta vare på det nesen min stolte på, og som jeg visste ikke ville gå nær. | EN 'to keep what a nose I trusted would not go near' (Pip's nose); MT made it Jessica's nose | fordi jeg hadde levd lenge nok til å ta vare på det en nese jeg stolte på, ikke ville gå nær. |
| 211 | 919 | 4 Proper name | Doc Mitchell drev | Doc Mitchell = doktor Mitchell (Frost and Found NO) | doktor Mitchell drev |
| 212 | 920 | 3 Mistranslation | gjorde ham til byens apoteker også. | EN 'the town's chemist' (one who analyses), not a pharmacist | gjorde ham til byens kjemiker også. |
| 213 | 920 | 6 Typo | Han hadde fått rareligere ting | 'rareligere' | Han hadde fått rarere ting |
| 214 | 920 | 4 Proper name | Doc Mitchell var | Doc Mitchell = doktor Mitchell | Doktor Mitchell var |
| 215 | 922 | 4 Proper name | Si meg at det er fordervelse, Doc. | Doc = 'doktor/Doktoren' as in Frost and Found NO | Si meg at det er fordervelse, doktor. |
| 216 | 925 | 3 Mistranslation | fra tinnet han holdt til for å teste | EN 'the tin' (container); 'tinnet' = the metal | fra boksen han holdt til for å teste |
| 217 | 927 | 3 Mistranslation | «Vel,» sa han. «Det har ikke gått i stykker, | EN 'It's not gone off'; 'gått i stykker' = broken | «Vel,» sa han. «Det har ikke blitt dårlig, |
| 218 | 927 | 3 Mistranslation | og dette er tørt som en benk. | EN 'dry as a bone'; 'tørt som en benk' is a calque-garble | og dette er knusktørt. |
| 219 | 929 | 3 Mistranslation | og det er det som surrer til baksten hennes, fordi det gjør absolutt ingenting tørt i en binge | 'surrer til' = buzzes; EN 'souring her bakes'; bin = dunk | og det er det som syrner baksten hennes, fordi det gjør absolutt ingenting tørt i en dunk |
| 220 | 931 | 6 Term (clue) | «Det er en sur base. Tørket syre, | sour base had 6 renderings (sur base / surdeig / surdeigskultur / surdeigsbase …); 'sur base' is a chemical contradiction and 'surdeig(skultur)' is the starter the acid replaces. Unified to 'syrningsmiddel' (acidulant) everywhere | «Det er et syrningsmiddel. Tørket syre, |
| 221 | 931 | 3 Mistranslation | Melkesyren er den samme syren som surrer melk. | 'surrer' = buzzes | Melkesyren er den samme syren som syrner melk. |
| 222 | 931 | 8 Units (decision) | for å ødelegge hundre pund mel. | 100 lb → 45 kg (accurate-figure rule, as Lisa ruled 2026-08-11; logged FP-NO-D2) | for å ødelegge 45 kilo mel. |
| 223 | 933 | 6 Term (clue) | ikke dyrker frem en sur base for industrielt brød over natten i tiodobbel mengde ved et uhell | sour base = syrningsmiddel; 'ten times' kept identical to [931] | ikke dyrker frem et syrningsmiddel for brødbakerier over natten, i ti ganger dosen, ved et uhell |
| 224 | 933 | 6 Term (clue) | en binge med godt mel | flour bin = dunk | en dunk med godt mel |
| 225 | 933 | 6 Grammar | «Noen puttet den der. | agreement with syrningsmiddel; Doc's line is quoted back identically in Ch15 [1176] | «Noen puttet det der. |
| 226 | 936 | 4 Proper name | Jeg sto der på Docs trinn | Doc = doktoren | Jeg sto der på doktorens trapp |
| 227 | 937 | 6 Term (clue) | Du kunne ikke kjøpe en sur base sekkevis fra en kjøpmannshylle. Den kom fra | sour base = syrningsmiddel (+ agreement) | Du kunne ikke kjøpe syrningsmiddel sekkevis fra en kjøpmannshylle. Det kom fra |
| 228 | 937 | 6 Grammar | Du kunne heller ikke dosere den på øyemål. | agreement with syrningsmiddel | Du kunne heller ikke dosere det på øyemål. |
| 229 | 937 | 3 Mistranslation | mens hun jaktet på en feil som aldri var i herverkets hender, | EN 'a fault that was never in her hands'; 'herverkets hender' = the vandalism's hands | mens hun jaktet på en feil som aldri lå i hendene hennes, |
| 230 | 938 | 4 Proper name | mens jeg sto på Docs trinn. | Doc = doktoren | mens jeg sto på doktorens trapp. |
| 231 | 941 | 3 Mistranslation | helte seg fremdeles innover mot den varme, usynlige varmen deres, | EN 'leaned'; 'helte' = poured; 'their warm invisible fire' | lente seg fremdeles innover mot den varme, usynlige ilden sin, |
| 232 | 941 | 3 Mistranslation | og i stedet for å helle mot allmenningen sammen med resten, helte den hardt den andre veien, | 'helle' = pour; EN 'lean' | og i stedet for å lene seg mot allmenningen sammen med resten, lente den seg hardt den andre veien, |
| 233 | 942 | 3 Mistranslation | og snømannen som helte hardt mot baksidene | 'helte' = poured | og snømannen som lente seg hardt mot baksidene |
| 234 | 943 | 3 Mistranslation | og nå helte den mot baksidene | 'helte' = poured | og nå lente den seg mot baksidene |
| 235 | 943 | 6 Grammar | Nicken min | '<bt>Nick</bt>en min' — name declined with a suffix; EN 'my Nick' | Nick min |
| 236 | 944 | 6 Typo/Term | som hadde rygget unna melbingen med fjærene til vers før jeg skjønte en ting. «Nesten din | flour bin = meldunken; 'til vers' garbled; 'Nesten' → 'Nesen' | som hadde rygget unna meldunken med fjærene på stritt før jeg skjønte en ting. «Nesen din |
| 237 | 946 | 3 Mistranslation | snømannen som helte seg bort fra alle sine feller. | 'helte' = poured | snømannen som lente seg bort fra alle sine feller. |
| 238 | 950 | 6 Typo | Hvem som kunne nå hvetemellet hennes. | 'hvetemellet' misspelt; EN 'her flour' | Hvem som kunne nå melet hennes. |
| 239 | 954 | 3 Mistranslation | Lastegården Pete hadde murret over over roastbiffen min, | EN 'over my roast' (the chuck roast, Ch7); 'roastbiff' is a different dish; doubled 'over' | Lastegården Pete hadde murret over mens han bandt steika mi, |
| 240 | 954 | 6 Term | rygget inn til lasterommet i de små, | EN 'the dock' = lasterampen (Ch7) | rygget inn til lasterampen i de små, |
| 241 | 954 | 6 Term (clue) | Hun bar dem til tønnene langs bakveggen | EN 'the bins' = flour bins = dunk (Ch2) | Hun bar dem til dunkene langs bakveggen |
| 242 | 954 | 6 Term (clue) | Melet stod der mellom kjerren og tønnen, | bin = dunk | Melet stod der mellom kjerren og dunken, |
| 243 | 958 | 6 Term (clue) | Og mellom dem en tønne med mel | bin = dunk ('tønne' is Hal's barrel) | Og mellom dem en dunk med mel |
| 244 | 960 | 6 Term | Røre det ut med spaden hennes. | EN 'her scoop' (Ch2 'øsen') | Røre det ut med øsen hennes. |
| 245 | 960 | 6 Term (clue) | Hun bar det manipulerte melet til tønnene selv | bin = dunk | Hun bar det manipulerte melet til dunkene selv |
| 246 | 968 | 6 Typo | i det flate morgendlyset, | 'morgendlyset' | i det flate morgenlyset, |
| 247 | 968 | 3 Mistranslation | Der var apotekets stålpropp, | EN 'the pharmacy's steel door'; 'stålpropp' = steel plug | Der var apotekets ståldør, |
| 248 | 968 | 6 Term | Og der de to som delte lasterommet. Petes kjølelager, et gammelt murbygd rom med en tung haspe, | dock = lasterampen; hasp = krampe (Ch7) | Og der de to som delte lasterampen. Petes kjølelager, et gammelt murbygd rom med en tung krampe, |
| 249 | 972 | 6 Typo | varebil sjåførens, | split compound | varebilsjåførens, |
| 250 | 972 | 3 Mistranslation | Hundre fot. Ikke ett av dem et navn. | EN 'A hundred feet' = a hundred footprints, not a distance | Hundre fotspor. Ikke ett av dem et navn. |
| 251 | 982 | 6 Term | nedover det opprørte lasterommet. | dock = lasterampen | nedover den opprørte lasterampen. |
| 252 | 984 | 6 Term | Pete Garcia hadde lasterommet og tjue vintre | dock = lasterampen | Pete Garcia hadde lasterampen og tjue vintre |
| 253 | 984 | 6 Term | over akkurat dette lasterommet. | dock = lasterampen | over akkurat denne lasterampen. |
| 254 | 1004 | 6 Term | ned den kalde halsen på lasterommet, | dock | ned den kalde halsen på lasteplassen, |
| 255 | 1008 | 6 Typo | over den hardtrammede snøen | 'hardtrammede' | over den hardtrampede snøen |
| 256 | 1027 | 3 Mistranslation (clue) | og ville like lite kjenne igjen en sur surdeig eller et meldyss som jeg ville vite hvordan man parterer en storfekjøtt. | EN 'would no more know a sour base from a dusting of chalk than I would know how to break down a steer'; sour base = syrningsmiddel | og ville like lite skille et syrningsmiddel fra et dryss kritt som jeg ville vite hvordan man parterer en okse. |
| 257 | 1035 | 6 Term | teglsteinene | the warm bricks by the stove = 'mursteinene' (Ch19 [1428] [1449] [1473]) | mursteinene |
| 258 | 1049 | 3 Mistranslation (clue) | En lang kåpe, eller en kjeledress, | EN 'A long coat, or a smock' — the pale working garment is a clue; 'kjeledress' = overalls | En lang frakk, eller en kittel, |
| 259 | 1049 | 6 Typo | Han riste på det grå hodet. | verb form | Han ristet på det grå hodet. |
| 260 | 1049 | 6 Typo | med en stripe rødfarget refleksrefleks over bakdørene. | 'refleksrefleks' doubled; EN 'red reflector tape' | med en stripe rød refleksteip over bakdørene. |
| 261 | 1053 | 6 Grammar | – De morgenen. | definite plural | – De morgenene. |
| 262 | 1055 | 3 Mistranslation | da jeg tok den på fersken like ved, | EN 'when I caught it close'; 'på fersken' is used again in the same sentence | da jeg kom tett innpå den, |
| 263 | 1057 | 3 Mistranslation | for under en skyet himmel ville han ikke få takk | EN idiom 'under a cloud' = under suspicion | for under mistanke ville han ikke få takk |
| 264 | 1067 | 3 Mistranslation | Jeg gikk hjem i het, hard morgensol | EN 'in the hard early light'; 'het' = hot | Jeg gikk hjem i det harde morgenlyset |
| 265 | 1069 | 6 Term | teglsteinene | the warm bricks by the stove = 'mursteinene' (Ch19 [1428] [1449] [1473]) | mursteinene |
| 266 | 1074 | 3 Mistranslation | Moren lager skolematen der i gården. | 'der i gården' (in that household) is an addition; EN 'His mom does the school lunches' | Moren hans lager skolematen. |
| 267 | 1075 | 3 Mistranslation | Jeg takket henne og hentet pelsen min. | EN 'got my coat' | Jeg takket henne og hentet kåpen min. |
| 268 | 1080 | 6 Typo | At såtheten slo om. | 'såtheten' | At sårheten slo om. |
| 269 | 1081 | 3 Mistranslation | basere meg på din medlidenhet eller håndtrykket hans. | EN 'your fondness'; 'medlidenhet' = pity | basere meg på din godhet for ham eller håndtrykket hans. |
| 270 | 1083 | 3 Mistranslation | Han var ved enden av krigsminnesmerket sammen med | EN 'at the war-memorial end' (of the green) | Han var i enden ved krigsminnesmerket sammen med |
| 271 | 1083 | 3 Mistranslation | en lang og tynn gutt i en kåpe som var | a boy's coat; 'kåpe' is a woman's coat | en lang og tynn gutt i en jakke som var |
| 272 | 1084 | 3 Mistranslation | – Jeg tok ikke veggen hennes. | EN 'I didn't do her wall' (paint it) | – Jeg malte ikke veggen hennes. |
| 273 | 1088 | 6 Typo | Faren hadde tatt nattkiftet | 'nattkiftet' | Faren hadde tatt nattskiftet |
| 274 | 1088 | 6 Typo | smaken på hosteboljeksene, | 'hosteboljeksene' not a word | smaken på hostedropsene, |
| 275 | 1091 | 3 Mistranslation | Jeg satt i kulden ved siden av ham og koblet veggen sammen med hvetemelet. Man sprayet ikke ord på en vegg om natten og målte samtidig opp hvetemel på farmasøytmål. | EN 'set the wall beside the flour … dose flour by the scoop to a chemist's measure' | Jeg satt i kulden ved siden av ham og stilte veggen opp ved siden av melet. Man sprayet ikke ord på en vegg om natten og doserte samtidig mel med øse etter en kjemikers mål. |
| 276 | 1092 | 6 Term | alleen | avenue spelled 'alléen' (22×) / 'alleen' (15×) / 'avyen' (7×); unified to 'alléen' | alléen |
| 277 | 1094 | 3 Mistranslation | ødela ikke hvetemelet hennes. | EN 'didn't sour her flour' | syrnet ikke melet hennes. |
| 278 | 1099 | 6 Grammar | med et kjøkkenhåndkle klemmer i begge hender. | participle | med et kjøkkenhåndkle klemt i begge hender. |
| 279 | 1103 | 6 Term | Kretsen møttes den kvelden | the circle = sirkelen | Sirkelen møttes den kvelden |
| 280 | 1103 | 3 Mistranslation | hver eneste rest av kardet garn i hele butikken. | EN 'every worsted end' | hver eneste kamgarnrest i hele butikken. |
| 281 | 1107 | 3 Mistranslation | Han var hjemme hele kvelden og passet | EN 'the whole night' | Han var hjemme hele natten og passet |
| 282 | 1113 | 6 Term | ferdigsnakket i kretsen. | the circle = sirkelen | ferdigsnakket i sirkelen. |
| 283 | 1118 | 3 Mistranslation | Pip hadde det blå nøstet i osteredet sitt | 'osteredet' (cheese nest); EN 'her nest' | Pip hadde det blå nøstet i redet sitt |
| 284 | 1119 | 3 Mistranslation | og halve allmenningen var der inne | EN 'half the avenue'; allmenningen = the green | og halve alléen var der inne |
| 285 | 1128 | 6 Grammar | hver eneste morgenen uansett, | definite form after 'hver' | hver eneste morgen uansett, |
| 286 | 1129 | 3 Mistranslation | mine to sjokolade-pekannøtter | EN 'my two chocolate-pecans' = pies | mine to sjokolade-pekannpaier |
| 287 | 1132 | 6 Register | brakt ferdig fra heimen, | 'heimen' dialectal | brakt ferdige hjemmefra, |
| 288 | 1132 | 3 Mistranslation | i det røde osteredet under vinduet. | 'osteredet' (cheese nest) | i det røde redet under vinduet. |
| 289 | 1136 | 4 Proper name/6 Term | Grange-salen var åpnet for de to innsamlingene samtidig, Hals og Selskapets, | the Grange = grendehuset (Inn Trouble NO); Society = Historielaget | Grendehuset var åpnet for de to innsamlingene samtidig, Hals og Historielagets, |
| 290 | 1136 | 3 Mistranslation | Hal sto ved matfatene i den ene enden | EN 'the food barrels'; 'matfatene' = food platters | Hal sto ved mattønnene i den ene enden |
| 291 | 1139 | 4 Proper name | rygget en hvit varebil inn til Grange-salens sidedør | the Grange = grendehuset | rygget en hvit varebil inn til sidedøren på grendehuset |
| 292 | 1142 | 3 Mistranslation | – Det er mer brød enn jeg har hatt hele måneden, sa hun – neida, sa han. – Jeg kommer | garbled MT self-correction ('sa hun – neida, sa han'); Hal speaks | – Det er mer brød enn jeg har fått inn hele måneden, sa han. – Jeg kommer |
| 293 | 1149 | 6 Term | Selskapets sedertrekledde eske | Society = Historielaget | Historielagets sedertrekledde eske |
| 294 | 1149 | 3 Mistranslation | Gretas sjokolade-pekannøttoppskrift, | EN 'Greta's chocolate-pecan recipe card' (the pie) | Gretas oppskriftskort på sjokolade-pekannpai, |
| 295 | 1149 | 4 Proper name | hadde Theo båret den ned til Grange-salen | the Grange = grendehuset | hadde Theo båret den ned til grendehuset |
| 296 | 1149 | 6 Grammar | Som skal forsegles når den gamle åpnes, | card text began with a dangling relative 'Som' | Skal forsegles når den gamle åpnes, |
| 297 | 1151 | 6 Term | forseglet under skiltet sitt i Selskapets fremre rom | Society = Historielaget; EN 'its card' (Ch6 'Et håndskrevet kort') | forseglet under kortet sitt i Historielagets fremre rom |
| 298 | 1151 | 6 Term (echo) | i selskapelig lag, slik forfedrene hadde ment det. | echoes the old card '… i selskap, slik våre forfedre mente' (Ch6) | i selskap, slik forfedrene mente. |
| 299 | 1153 | 6 Term | – Selskapet. Ingen har bedt | Society = Historielaget | – Historielaget. Ingen har bedt |
| 300 | 1154 | 3 Mistranslation | som varme fra Nicks klebersteinshoved. | EN 'Nick's fieldstone hearth'; 'klebersteinshoved' (soapstone head) is wrong | som varme fra Nicks ildsted av marksteiner. |
| 301 | 1154 | 6 Term | alleen | avenue spelled 'alléen' (22×) / 'alleen' (15×) / 'avyen' (7×); unified to 'alléen' | alléen |
| 302 | 1156 | 3 Mistranslation | mellom ploglistene og kirkemiddagen, | EN 'the plow schedules and the church suppers' | mellom brøyteplanene og kirkemiddagene, |
| 303 | 1156 | 4 Proper name | Den hang på Grange-salens oppslagstavle | the Grange = grendehuset | Den hang på oppslagstavlen i grendehuset |
| 304 | 1157 | Ruling 3 | Grand Opening Week. | English flyer text translated (italic kept) | Stor åpningsuke. |
| 305 | 1158 | 4 Proper name | der Grange-sekretæren hadde stemplet arket | the Grange = grendehuset | der sekretæren i grendehuset hadde stemplet arket |
| 306 | 1158 | 6 Typo | INGLAGT, og en dato. | 'INGLAGT' not a word; EN 'POSTED' | OPPSLÅTT, og en dato. |
| 307 | 1160 | 6 Term (echo) | En uke. Kanskje mer, hvis delene til vasken ikke kommer. | Jessica quotes Varney's Ch9 line verbatim — must match [794] | En uke. Kanskje mer, hvis delene til håndvasken ikke kommer frem. |
| 308 | 1162 | 6 Term | alleen | avenue spelled 'alléen' (22×) / 'alleen' (15×) / 'avyen' (7×); unified to 'alléen' | alléen |
| 309 | 1168 | 3 Mistranslation | i sedertresekken, | EN 'the cedar box'; 'sekk' = sack | i sedertreesken, |
| 310 | 1169 | 3 Mistranslation | Nå sto hun blant en klynge av dem ved matfatene, | EN 'by the food barrels' | Nå sto hun blant en klynge av dem ved mattønnene, |
| 311 | 1169 | 6 Typo | ettermidagens dronning. | 'ettermidagens' | ettermiddagens dronning. |
| 312 | 1174 | 3 Mistranslation | Men i hvitdagsmengder vil man | EN 'at holiday numbers'; 'hvitdags-' = Whitsun | Men i julemengder vil man |
| 313 | 1176 | 6 Term (echo) | Og de visste nøyaktig hvor mye de skulle putte. | Doc's Ch11 line quoted back — identical wording | Og de visste nøyaktig hvor mye de skulle ha i. |
| 314 | 1176 | 3 Mistranslation | til en ring av kvinner ved et matfat. | EN 'by a food barrel' | til en ring av kvinner ved en mattønne. |
| 315 | 1176 | 3 Mistranslation | En kvinne som visste på et visst vis hvor mye | EN 'knew to a whisper how much' | En kvinne som visste på grammet hvor mye |
| 316 | 1177 | 4 Name/6 Term (clue) | Doktor hadde sagt at et konditorikjøkken ikke ville ha bruk for det stoffet i Gretas bøtte. | Doc = Doktoren; flour bin = dunk | Doktoren hadde sagt at et konditorikjøkken ikke ville ha bruk for det stoffet i Gretas dunk. |
| 317 | 1177 | 6 Typo | Muresteinen på Gretas fliser | 'Muresteinen' | Mursteinen på Gretas fliser |
| 318 | 1177 | 6 Term | den eneste haugen med gammel teglstein i kvartalet | brick = murstein | den eneste haugen med gammel murstein i kvartalet |
| 319 | 1177 | 4 Proper name | Doktor hadde ikke stått her og hørt henne. | Doc = Doktoren | Doktoren hadde ikke stått her og hørt henne. |
| 320 | 1178 | 6 Term (echo) | stakkars menneske, så synd på problemene hennes akkurat nå. | Renée's Ch3 line quoted back verbatim ([237]) | stakkars menneske, så synd med alt trøbbelet hennes akkurat nå. |
| 321 | 1180 | 6 Grammar | Jeg pinte det fast på tavlen igjen der jeg hadde funnet den, | 'pinte' anglicism; agreement | Jeg festet det på tavlen igjen der jeg hadde funnet det, |
| 322 | 1186 | 3 Mistranslation | – Ja, sa hun. – Inn. | wrong speaker: EN '"Yes," I said. "In."' (Pip cannot speak) | – Ja, sa jeg. – Inn. |
| 323 | 1187 | 3 Mistranslation | forbi sedertresekken og forbi Renée | EN 'the cedar box' | forbi sedertreesken og forbi Renée |
| 324 | 1192 | 3 Mistranslation | ville ha vært det som utmerket seg. | EN 'would've been the marked thing'; 'utmerket seg' = excelled | ville ha vært det som ble lagt merke til. |
| 325 | 1192 | 3 Mistranslation | med Pete over hoggestabben hans. | EN 'his chopping block' (butcher's block, Ch13 'slakteblokken') | med Pete over slakteblokken hans. |
| 326 | 1194 | 6 Typo | Pip ble med meg og lunket av gårde | 'lunket' | Pip ble med meg og luntet av gårde |
| 327 | 1198 | 6 Typo | Ikke en krumme på marmoren. | 'krumme' (Danish) | Ikke en smule på marmoren. |
| 328 | 1204 | 6 Term/3 Mistranslation | – Balsamgran, antar jeg, det landlige grønne. Det vil få fasaden til å skille seg ut. | balsam = granbar; EN 'It'll set the front off' (show it off nicely) | – Granbar, antar jeg, det landlige grønne. Det vil pynte opp fasaden. |
| 329 | 1206 | 6 Typo | som koste mer enn hele disken | verb form | som kostet mer enn hele disken |
| 330 | 1208 | 3 Mistranslation | Hun snakket om butikken. | EN 'She talked shop' (as Ch15 'snakket fag') | Hun snakket fag. |
| 331 | 1210 | 3 Mistranslation | hele feriekalenderen dere opprettholder. | EN 'the whole holiday calendar you keep' (holiday = festive season, not vacation) | hele høytidskalenderen dere holder. |
| 332 | 1214 | 3 Mistranslation | En liten lyd, halvveis en lystig latter. | EN 'half a laugh'; 'lystig' is an addition | En liten lyd, halvveis en latter. |
| 333 | 1214 | 6 Term (clue) | Fugen ryker. Værlistene ryker. | Renée must use Varney's own trade words (Ch9 'tetningslisten') — the recital proves she knew the complaint | Fugen ryker. Tetningslisten ryker. |
| 334 | 1218 | 3 Mistranslation (clue) | Fugen. Værlistene. Håndvasken to grader unna et gammelt rør. | EN 'The hand-sink two degrees shy off an old pipe'; 'to grader unna' lost the direction; 'two degrees under code' kept identical at [790] [1214] [1218] (decision FP-NO-D1) | Fugen. Tetningslisten. Håndvasken to grader under forskriftene på grunn av et gammelt rør. |
| 335 | 1220 | 3 Mistranslation | Det foreløpige var Gretas, og Varneys, og mitt. | EN 'The provisional was Greta's…' (the provisional closure) | Den midlertidige stengingen var Gretas sak, og Varneys, og min. |
| 336 | 1222 | 6 Term (clue) | – Vet alle om Gretas vask da? | hand-sink = håndvask | – Vet alle om Gretas håndvask da? |
| 337 | 1226 | 3 Mistranslation | og hånden som hadde skrevet brevet. | EN 'the hand that had typed the paper' = the complaint ('brevet' = letter) | og hånden som hadde skrevet klagen. |
| 338 | 1226 | 8 Units (idiom) | og ikke én tomme nærmere noe | 'not one inch nearer' → idiomatic | og ikke et hårsbredd nærmere noe |
| 339 | 1238 | 6 Term | – Balsamgran og en gullsløyfe, | balsam = granbar | – Granbar og en gullsløyfe, |
| 340 | 1242 | 1 Untranslated English | Pip was where I'd left her, on the step, with the bottle cap laid square between her feet. | English sentence left in the Norwegian text | Pip var der jeg hadde forlatt henne, på trappetrinnet, med flaskekorken lagt pent mellom føttene. |
| 341 | 1246 | 3 Mistranslation | Altfor glad i Gretas fall, | 'glad i' = fond of; EN 'glad of' | Altfor glad for Gretas fall, |
| 342 | 1246 | 3 Mistranslation | en kvinne som allerede hadde tilbragt en sesong som ennå ikke hadde kommet. | EN 'had already spent a season' (spent as money), not 'passed time' | en kvinne som allerede hadde brukt opp en sesong som ennå ikke var kommet. |
| 343 | 1248 | 6 Grammar | Hjemme tok jeg granbaren inn | granbar is neuter | Hjemme tok jeg granbaret inn |
| 344 | 1248 | 6 Typo | jeg bandt den første buntingen med granbar | 'buntingen' | jeg bandt den første bunten med granbar |
| 345 | 1251 | 6 Term | med edelgran bundet en tredjedel | balsam = granbar | med granbar bundet en tredjedel |
| 346 | 1251 | 6 Term/Typo | på en benk i parken, hadde Danny Ott strukket seg etter et minutt | the green = allmenningen; 'minutt' → 'minne' (memory) | på en benk på allmenningen, hadde Danny Ott strukket seg etter et minne |
| 347 | 1253 | 6 Typo | Det var en halv skidag på videregående, | 'skidag' (ski day); EN 'a half day at the high school' | Det var halv skoledag på videregående, |
| 348 | 1253 | 6 Term | akkurat som hun hadde gjort i parken. | the green = allmenningen | akkurat som hun hadde gjort på allmenningen. |
| 349 | 1261 | 6 Term | Du holder øye med den parken etter mørkets frambrudd. | the green = allmenningen | Du holder øye med allmenningen etter mørkets frambrudd. |
| 350 | 1263 | 3 Mistranslation | Kyle skaffet en boks fra skjulet | EN 'a can' (spray paint) | Kyle skaffet en sprayboks fra skjulet |
| 351 | 1269 | 6 Term | når lyset er på over lageret til Pete. | Pete's locker = kjølelageret | når lyset er på over kjølelageret til Pete. |
| 352 | 1273 | 3 Mistranslation | så noen helt bakerst hos Greta. | EN 'at the back of Greta's' (outside, at the back door) | så noen bak butikken til Greta. |
| 353 | 1273 | 5 Register | blekt, med en kåpe under. | Danny doesn't know the figure's sex; 'kåpe' is a woman's coat | blekt, med en frakk under. |
| 354 | 1287 | 3 Mistranslation | Han trakk glidelåsen på kåpen opp til haken | a boy's coat = jakke (Ch14) | Han trakk glidelåsen på jakken opp til haken |
| 355 | 1293 | 3 Mistranslation | med en bondeformet sekk med havre åpen foran seg | EN 'a farmer's sack of oats'; 'bondeformet' = farmer-shaped | med en bondes havresekk åpen foran seg |
| 356 | 1293 | 6 Term | og så på Norgesglasset jeg satte ned | the preserving jar = krukken (Ch11); 'Norgesglass' is a Norwegian brand name | og så på syltekrukken jeg satte ned |
| 357 | 1295 | 6 Term (clue) | som kjenner igjen en surdeig om han finner en. | sour base = syrningsmiddel ('surdeig' = sourdough) | som kjenner igjen et syrningsmiddel om han finner det. |
| 358 | 1295 | 6 Term | avyen | 'avyen' is not a Norwegian word; avenue = alléen | alléen |
| 359 | 1303 | 6 Grammar | sto trykket på en flygeblad før | gender | sto trykket på et flygeblad før |
| 360 | 1303 | 6 Term (clue) | nevnte hun fugen og tettelisten og vasken for meg, | Varney's three trade words (Ch9) | nevnte hun fugen og tetningslisten og håndvasken for meg, |
| 361 | 1303 | 6 Term | avyen | 'avyen' is not a Norwegian word; avenue = alléen | alléen |
| 362 | 1307 | 3 Mistranslation | Jeg er ikke politiet, og hun må ikke vise deg en dritt. | 'må ikke' = must not (reversed); EN 'she doesn't have to show you a thing'; 'dritt' too coarse | Jeg er ikke politiet, og hun trenger ikke å vise deg noe som helst. |
| 363 | 1309 | 3 Mistranslation | – Nei. Det må hun ikke. | 'må ikke' = must not; EN 'No. She doesn't.' | – Nei. Det trenger hun ikke. |
| 364 | 1311 | 3 Mistranslation | Så tok han kåpen ned fra knaggen. | a man's coat = frakk | Så tok han frakken ned fra knaggen. |
| 365 | 1319 | 6 Grammar | tok tak i enden av skolissene hans med nebbet og trakk den sakte opp. | singular (EN 'his bootlace'; 'den') | tok tak i enden av skolissen hans med nebbet og trakk den sakte opp. |
| 366 | 1331 | 6 Term (clue) | – Noen hadde oppi surdeig i melet til Greta, sa jeg. – Et syrnet bakekjøkken, nok til å syrne alt hun bakte. I morges nevnte du fugen og tettelisten og vasken for meg, | sour base = syrningsmiddel; EN 'A bread kitchen's acid' ('Et syrnet bakekjøkken' = a soured kitchen); trade words as Ch9 | – Noen hadde et syrningsmiddel i melet til Greta, sa jeg. – Syre fra et brødbakeri, nok til å syrne alt hun bakte. I morges nevnte du fugen og tetningslisten og håndvasken for meg, |
| 367 | 1341 | 3 Mistranslation | Kokesjokoladen i poser | EN 'couverture' (Ch3) | Overtrekkssjokoladen i poser |
| 368 | 1343 | 8 Units (SAFE) | – En klype i femti pund. Deigblandingsmiddel. | 'a pinch in fifty pounds' → 23 kg; 'dough conditioner' = deigforbedrer | – En klype per 23 kilo. Deigforbedrer. |
| 369 | 1343 | 6 Term (clue) | En bøtte med surdeig ville du luktet | sour base = syrningsmiddel | En bøtte med syrningsmiddel ville du luktet |
| 370 | 1351 | 3 Mistranslation | – Mel, smør, kokesjokolade, mandler, | couverture | – Mel, smør, overtrekkssjokolade, mandler, |
| 371 | 1351 | 6 Term (clue) | – Ingen surdeig. Ikke på en eneste side. | sour base = syrningsmiddel | – Ikke noe syrningsmiddel. Ikke på en eneste side. |
| 372 | 1353 | 3 Mistranslation | – Man har da vel ikke surdeig i en croissant, doktor, | EN 'One doesn't put sour in a croissant' | – Man har da ikke noe surt i en croissant, doktor, |
| 373 | 1359 | 6 Term | avyen | 'avyen' is not a Norwegian word; avenue = alléen | alléen |
| 374 | 1367 | 6 Term (echo) | – Edelgran og gullsløyfe. | she repeats her Ch16 order ([1238] 'Granbar og en gullsløyfe') | – Granbar og en gullsløyfe. |
| 375 | 1383 | 6 Term | avyen | 'avyen' is not a Norwegian word; avenue = alléen | alléen |
| 376 | 1385 | 4 Proper name | Jeg hadde vært sikker siden bedehuset, | EN 'since the Grange' (the flyer); 'bedehuset' = prayer house | Jeg hadde vært sikker siden grendehuset, |
| 377 | 1385 | 3 Mistranslation | Hun hadde forklart kokesjokolade for meg | EN 'explained couverture to me' | Hun hadde forklart overtrekkssjokolade for meg |
| 378 | 1387 | 3 Mistranslation | Hun hadde bodd ved siden av den i årevis. | EN 'She had baked beside it for years' | Hun hadde bakt ved siden av den i årevis. |
| 379 | 1387 | 3 Mistranslation | Hun hadde hentet sopelimen til Greta | EN 'Greta's broom' = the push broom (Ch4 'brede kost') | Hun hadde hentet kosten til Greta |
| 380 | 1391 | 6 Grammar | ved lunsjtider. | 'lunsjtider' | ved lunsjtid. |
| 381 | 1393 | 6 Typo/Grammar | der barna hadde akte, slapp seg ned på magen og suste ned i én lang, glatt renn, | 'akte'; gender | der barna hadde aket, slapp seg ned på magen og suste ned i ett langt, glatt renn, |
| 382 | 1395 | 6 Term | løftet barløvet av ringen | balsam = granbar | løftet granbaret av ringen |
| 383 | 1395 | 6 Grammar | til det ikke var noe igjen foran meg enn den nakne stålrammen. | missing 'annet' | til det ikke var noe igjen foran meg annet enn den nakne stålrammen. |
| 384 | 1397 | 3 Mistranslation | slik Dot hadde fortalt meg at de strenge vintrene alltid gjorde. | EN 'as Dot had told me the hard ones always did' = hard freezes, not winters | slik Dot hadde fortalt meg at de verste kuldene alltid gjorde. |
| 385 | 1397 | 6 Term | Selskapets smale | Historical Society = Historielaget (Inn Trouble NO 48×, Frost and Found NO); 'Selskapet' (the Company) was used 35× | Historielagets smale |
| 386 | 1400 | 6 Term | Selskapets kjel | Historical Society = Historielaget (Inn Trouble NO 48×, Frost and Found NO); 'Selskapet' (the Company) was used 35× | Historielagets kjel |
| 387 | 1403 | 8 Units (SAFE) | det brune vannet som sto en kvart tomme over gulvbordene | 'a quarter-inch' → about half a centimetre | det brune vannet som sto en halv centimeter over gulvbordene |
| 388 | 1403 | 3 Mistranslation | hang i rommet, kvalmende og endelig. | EN 'sweetish'; 'kvalmende' = nauseating | hang i rommet, søtlig og endelig. |
| 389 | 1404 | 6 Typo/3 Mistranslation | Men nå har taket ryki det også, og taket koster det dobbelte, | 'ryki'; EN 'the roof's the bigger sum by half' (not double) | Men nå har taket røket også, og taket er halvparten dyrere, |
| 390 | 1405 | 8 Units (SAFE) | Den var berget med seks rene fot til gode, | 'six clean feet' → nearly two metres | Den var berget med nesten to meter til gode, |
| 391 | 1406 | 3 Mistranslation | Den gode følelsen fra kjøreturen, sedertasken som fylte seg opp på bedehuset | EN 'the drive' = fundraising drive (not a car trip); 'the cedar box … at the Grange' (bedehus = prayer house) | Den gode følelsen fra innsamlingen, sedertreesken som ble fylt opp i grendehuset |
| 392 | 1406 | 4 Title | Jeg tenkte på mr. Worthington, | English 'mr.'; Inn Trouble NO uses 'herr Worthington' | Jeg tenkte på herr Worthington, |
| 393 | 1406 | 6 Term | tro at Selskapet var | Historical Society = Historielaget (Inn Trouble NO 48×, Frost and Found NO); 'Selskapet' (the Company) was used 35× | tro at Historielaget var |
| 394 | 1406 | 6 Term | Selskapets eldste | Historical Society = Historielaget (Inn Trouble NO 48×, Frost and Found NO); 'Selskapet' (the Company) was used 35× | Historielagets eldste |
| 395 | 1407 | 6 Term (clue) | Renées lager åpnet for Doc hylle for hylle uten en eneste tone av surhet blant dem, | EN 'not a grain of sour base among them'; Doc = doktoren | Renées lager åpnet for doktoren hylle for hylle uten et eneste gram syrningsmiddel blant dem, |
| 396 | 1407 | 3 Mistranslation (no-poison) | En forgiftet melkasse og en maskinskrevet klage, | EN 'A dosed flour bin' — 'forgiftet' (poisoned) is not in the English (no-poison edition) | En dosert meldunk og en maskinskrevet klage, |
| 397 | 1408 | 6 Term | at Selskapet skulle | Historical Society = Historielaget (Inn Trouble NO 48×, Frost and Found NO); 'Selskapet' (the Company) was used 35× | at Historielaget skulle |
| 398 | 1411 | 3 Mistranslation | jeg hadde sett ham gjøre med bindersene sine, | EN 'his brads' (Ch6 'stifter'); 'binders' = paper clips | jeg hadde sett ham gjøre med stiftene sine, |
| 399 | 1411 | 6 Typo | Trekpapir mellom de verste av dem, | 'Trekpapir' | Trekkpapir mellom de verste av dem, |
| 400 | 1411 | 3 Mistranslation | Og han gjorde det i kåpen sin med frostrøyk | a man's coat = frakk | Og han gjorde det i frakken sin med frostrøyk |
| 401 | 1416 | 6 Typo | Smeltearbeidet, trekpapiret, | 'trekpapiret' | Smeltearbeidet, trekkpapiret, |
| 402 | 1416 | 6 Typo | ingen bystyrekomité bevegde seg raskt nok | verb form | ingen bystyrekomité beveget seg raskt nok |
| 403 | 1423 | 6 Typo/3 Mistranslation | mens ovnet tikket og det sprukne, kalde jernet lå stumt ned i kjelleren. I skinnende lys fra en lånt lykt | 'ovnet', 'ned i'; EN 'By the light of one borrowed lantern' | mens ovnen tikket og det sprukne, kalde jernet lå stumt nede i kjelleren. I lyset fra én lånt lykt |
| 404 | 1426 | 6 Term | fra Selskapet | Historical Society = Historielaget (Inn Trouble NO 48×, Frost and Found NO); 'Selskapet' (the Company) was used 35× | fra Historielaget |
| 405 | 1435 | 3 Mistranslation | hele Evergreen lagt ut i sennepsflasker. | EN 'laid out in cruets' (salt, pepper, sugar), not mustard bottles | hele Evergreen lagt ut i bordflasker og bøsser. |
| 406 | 1436 | 4 Proper name | Jeg satte lokket til sukkerkoppen bak pepperen. «I containeren bak Fenwick-plassen, | 'the Fenwick place' = Fenwick-huset (Ch1); sugar bowl | Jeg satte lokket til sukkerskålen bak pepperen. «I containeren bak Fenwick-huset, |
| 407 | 1448 | 3 Mistranslation | og som bærer pudderet sitt til jobben | EN 'her powder'; 'pudder' = face powder | og som bærer pulveret sitt til jobben |
| 408 | 1451 | 3 Mistranslation | Først i kvartalet hans, over steika di. | EN 'Once at his block' = his butcher's block | Først ved slakteblokken hans, over steika di. |
| 409 | 1453 | 3 Mistranslation | Han sa aldri at den gikk inn i Sugarplum. Jeg hørte den fjerne enden. | EN 'He said the far end' — the point is what Danny said vs what Jessica heard | Han sa aldri at den gikk inn i Sugarplum. Han sa den fjerne enden. |
| 410 | 1453 | 3 Mistranslation | ved Gretas karm før ovnene hennes ble tent, | EN 'Greta's sill' = the back-door sill (Ch12), not a window frame | ved Gretas dørstokk før ovnene hennes ble tent, |
| 411 | 1455 | 3 Mistranslation | er for en som må komme langveis fra, | EN 'for someone who has to come from somewhere' | er for en som må komme et sted fra, |
| 412 | 1455 | 3 Mistranslation | ned til Gretas karm og hjem igjen, | Greta's (back-door) sill | ned til Gretas dørstokk og hjem igjen, |
| 413 | 1455 | 6 Term | alleen | avenue spelled 'alléen' (22×) / 'alleen' (15×) / 'avyen' (7×); unified to 'alléen' | alléen |
| 414 | 1459 | 6 Term | lente seg oppover veien mot arnen din. | hearth = ildsted | lente seg oppover veien mot ildstedet ditt. |
| 415 | 1459 | 6 Term | alleen | avenue spelled 'alléen' (22×) / 'alleen' (15×) / 'avyen' (7×); unified to 'alléen' | alléen |
| 416 | 1460 | 5 Register | Den kan ikke fortelle deg en dritt. | EN 'It can't tell you a thing' said gently; 'en dritt' is coarse | Den kan ikke fortelle deg noe som helst. |
| 417 | 1465 | 4 Name/3 Mistranslation | Jeg leste det på bedehuset som et tegn på at hun visste at nedleggelsen var på vei. Man kan ikke trykke en åpning for en nedleggelse | the Grange = grendehuset (bedehus = prayer house); closure = stenging ('nedleggelse' = permanent shutdown) | Jeg leste det i grendehuset som et tegn på at hun visste at stengingen var på vei. Man kan ikke trykke en åpning for en stenging |
| 418 | 1468 | 3 Mistranslation | «Så nedleggelsen ble timet etter åpningen.» | closure = stenging | «Så stengingen ble timet etter åpningen.» |
| 419 | 1469 | 4 Proper name | fra trinnet på bedehuset og ut. | the Grange step | fra trappen på grendehuset og ut. |
| 420 | 1471 | 6 Term (clue) | og det var ingen surdeig der, og hun fortalte meg hvem som hadde fortalt henne om Gretas fuger. | sour base = syrningsmiddel; grout = fugen | og det var ikke noe syrningsmiddel der, og hun fortalte meg hvem som hadde fortalt henne om Gretas fuge. |
| 421 | 1471 | 3 Mistranslation | Et flygeblad er et bevis på noens disk | EN 'A flyer's a proof' = printer's proof, not evidence | Et flygeblad ligger som prøvetrykk på noens disk |
| 422 | 1478 | 6 Typo | på lørdagsformidlene med kjelen på | 'lørdagsformidlene' | på lørdagsformiddagene med kjelen på |
| 423 | 1478 | 3 Mistranslation | med fjærene stilt mot kulden. | EN 'feathers puffed out against the cold' | med fjærene pustet opp mot kulden. |
| 424 | 1480 | 6 Typo | med kåpen fremdeles knppet, | 'knppet' | med kåpen fremdeles kneppet, |
| 425 | 1482 | 3 Mistranslation | – Kom og si til Martha at hun ikke er fra seg. | EN 'she isn't losing her mind'; 'fra seg' = distraught | – Kom og si til Martha at hun ikke holder på å gå fra vettet. |
| 426 | 1484 | 3 Mistranslation | – Jeg har da aldri sagt at jeg er fra meg, | EN 'I never said I was losing my mind' | – Jeg har da aldri sagt at jeg holdt på å gå fra vettet, |
| 427 | 1484 | 3 Mistranslation | En dame ringte meg i går kveld, i tretiden. | EN 'last night, at suppertime'; 'i tretiden' = around three o'clock | En dame ringte meg i går kveld, ved middagstid. |
| 428 | 1484 | 3 Mistranslation/6 Grammar | To sjokolade-pekannøttkaker og en dussin rundstykker, | Martha's order must match Ch14 ('to sjokolade-pekannpaier og et dussin rundstykker'); 'en dussin' | To sjokolade-pekannpaier og et dussin rundstykker, |
| 429 | 1490 | 3 Mistranslation | Joyce tok med seg en kasserolle til henne på mandag, | EN 'a casserole' (the dish of food); 'kasserolle' = a saucepan | Joyce tok med seg en gryterett til henne på mandag, |
| 430 | 1490 | 3 Mistranslation | Kanskje de to endelig har skvett opp i det. | EN 'patched it up'; 'skvett opp i det' is not an idiom | Kanskje de to endelig har begravet stridsøksen. |
| 431 | 1500 | 6 Grammar | og tok krusen hun stakk i hånden min, | 'krus' is neuter | og tok kruset hun stakk i hånden min, |
| 432 | 1502 | 6 Term (clue) | tynn og rask i den hvite bakerfrakken sin, | Joyce's white baker's coat = 'hvit bakerjakke' (Ch4, Ch15) | tynn og rask i den hvite bakerjakken sin, |
| 433 | 1502 | 6 Register | Hun hadde sitti der mens Greta laget te. | 'sitti' dialectal | Hun hadde sittet der mens Greta laget te. |
| 434 | 1506 | 6 Grammar | og satte fra meg krusen full. | neuter | og satte fra meg kruset fullt. |
| 435 | 1518 | 3 Mistranslation | den dagen Joyce kom med kasserollen, | casserole = gryterett | den dagen Joyce kom med gryteretten, |
| 436 | 1520 | 3 Mistranslation/6 Term (clue) | – Vasken er fremdeles ikke kommet, sa hun før jeg hadde sagt hei. – Tom ordnet listverket på torsdag. Jeg fuget fugene selv. Og fylkesfyren kommer ikke tilbake før vasken er i orden. | EN 'The sink part still hasn't come'; Varney's three items (grout/weather-strip/hand-sink) in the same words as Ch9 | – Delen til håndvasken er fremdeles ikke kommet, sa hun før jeg hadde sagt hei. – Tom ordnet tetningslisten på torsdag. Jeg tettet fugen selv. Og fylkesfyren kommer ikke tilbake før håndvasken er i orden. |
| 437 | 1524 | 3 Mistranslation | sto en vasket og tørket glasskasserolle med lokket på. | EN 'a glass casserole dish' (Ch12 'ildfast form') | sto en vasket og tørket ildfast glassform med lokket på. |
| 438 | 1534 | 3 Mistranslation | To sjokolade-pekannøttkaker og et dussin rundstykker. Ivy fikk en hun også, med sine tre gresskar. | pies; 'tre gresskar' = three pumpkins | To sjokolade-pekannpaier og et dussin rundstykker. Ivy fikk en hun også, med sine tre gresskarpaier. |
| 439 | 1538 | 6 Register | – Hvem har sitti ved denne boken? | 'sitti' | – Hvem har sittet ved denne boken? |
| 440 | 1538 | 6 Register | Hvem har sitti akkurat der ved siden av den? | 'sitti' | Hvem har sittet akkurat der ved siden av den? |
| 441 | 1548 | 3 Mistranslation | – Da fylkesmannens mann gikk ut døren min, | EN 'the county man'; 'fylkesmannens mann' = the county governor's man | – Da mannen fra fylket gikk ut døren min, |
| 442 | 1556 | 3 Mistranslation | – Pete sier låsen på hageporten din stadig ramler av, | EN 'the yard gate' (the shared loading-yard gate), not a garden gate | – Pete sier låsen på porten til bakgården din stadig ramler av, |
| 443 | 1558 | 6 Term | for å poengtere det med haspen min. | hasp = krampe (Ch7) | for å poengtere det med krampen min. |
| 444 | 1568 | 6 Term | kom ut med skrubbekosten min, | EN 'my push broom' (Ch4 'Gretas brede kost') | kom ut med den brede kosten min, |
| 445 | 1570 | 6 Term (clue) | kunne jeg se skrubbekosten på spikeren ved bakdøren, et skritt unna der listverket under døren var blitt nedslitt og fugene ved foten | push broom; weather-strip/grout as Ch9 | kunne jeg se den brede kosten på spikeren ved bakdøren, et skritt unna der tetningslisten under døren var blitt nedslitt og fugen ved foten |
| 446 | 1574 | 6 Typo | til å holde det igang. | 'igang' | til å holde det gående. |
| 447 | 1580 | 3 Mistranslation | – Det må du da heller ikke. | EN 'You don't have to'; 'må … ikke' = must not | – Det trenger du ikke. |
| 448 | 1588 | 6 Typo | Jeg reiste meg, stelte meg ved siden av henne, | 'stelte' | Jeg reiste meg, stilte meg ved siden av henne, |
| 449 | 1600 | 3 Mistranslation | der hun plukket opp den rene kasserollen. | casserole dish = formen | der hun plukket opp den rene formen. |
| 450 | 1607 | 6 Term (clue) | Hvis et bakeri trengte en surdeigskultur, hvor ville de ha bestilt den fra? | sour base = syrningsmiddel ('surdeigskultur' = sourdough starter, the very thing the acid replaces); EN 'a bread kitchen' | Hvis et brødbakeri trengte et syrningsmiddel, hvor ville de ha bestilt det fra? |
| 451 | 1608 | 4 Proper name | – Pelkeys i Lewiston. Hver eneste grossistbaker på denne siden av fjellene kjøper fra Pelkeys. | supplier's name as in the English ('Pelkey's'); MT had Pelkeys/Pelkey/Pelkey's | – Pelkey's i Lewiston. Hver eneste grossistbaker på denne siden av fjellene kjøper fra Pelkey's. |
| 452 | 1615 | 3 Mistranslation | Alle selskaper må registrere seg i et fylke, | EN 'register with a state' | Alle selskaper må registrere seg i en delstat, |
| 453 | 1622 | 6 Typo | Hun hadde vært nede på gaven med notatblokken sin | 'gaven' (the gift); EN 'on the avenue' | Hun hadde vært nede i alléen med notatblokken sin |
| 454 | 1625 | 3 Mistranslation | En stripe med rød refleks-teip gikk langs bakdørene, kjennemerket var et hvitoppgitt Maine-skilt med en nordamerikansk meis på, | EN 'ran across the rear doors' (as Pete saw it, Ch13); 'hvitoppgitt' garbled; chickadee = svartkappemeis | En stripe med rød refleksteip gikk tvers over bakdørene, kjennemerket var et hvitt Maine-skilt med en svartkappemeis på, |
| 455 | 1635 | 6 Typo | sagmugghaugen han hadde sopte opp | participle | sagmugghaugen han hadde sopt opp |
| 456 | 1637 | 4 Title | – Ville du sagt det til sjefen? | EN 'the chief' = politisjefen | – Ville du sagt det til politisjefen? |
| 457 | 1639 | 4 Title | – Jeg vil helst at sjefen skal få det | Chief = politisjefen | – Jeg vil helst at politisjefen skal få det |
| 458 | 1644 | 4 Title | og ringte sjefen hjemme hos henne. | Chief = politisjefen | og ringte politisjefen hjemme. |
| 459 | 1644 | 6 Term | teglsteinene | the warm bricks by the stove = 'mursteinene' (Ch19 [1428] [1449] [1473]) | mursteinene |
| 460 | 1647 | 6 Term (clue) | – Doktoren fant en surdeigskultur i Gretas mel, | sour base = syrningsmiddel | – Doktoren fant et syrningsmiddel i Gretas mel, |
| 461 | 1647 | 6 Term (clue) | leverte surdeigskultur til Wendt's Bakehouse i høst? | sour base = syrningsmiddel | leverte syrningsmiddel til Wendt's Bakehouse i høst? |
| 462 | 1647 | 4 Proper name | om Pelkeys i Lewiston leverte | supplier name | om Pelkey's i Lewiston leverte |
| 463 | 1649 | 4 Proper name | – Pelkeys er stengt. | supplier name | – Pelkey's er stengt. |
| 464 | 1650 | 4 Title | – Er Mr. Pelkey det? | English 'Mr.'; courtesy titles herr/fru (Inn Trouble NO) | – Er herr Pelkey det? |
| 465 | 1656 | 6 Term (clue) | En sekk med surdeigskulturen deres med et par ukers mellomrom, til rugbrødet hun bakte for kroene, | sour base = syrningsmiddel; inns = vertshusene (Ch5) | En sekk av syrningsmiddelet deres med et par ukers mellomrom, til rugbrødet hun bakte for vertshusene, |
| 466 | 1656 | 6 Term | hun mistet den store kro-kontoen sin | inn = vertshus | hun mistet den store vertshuskontoen sin |
| 467 | 1663 | 4 Proper name | Doc Mitchell hadde bare lampen | Doc Mitchell = doktor Mitchell (Frost and Found NO) | Doktor Mitchell hadde bare lampen |
| 468 | 1663 | 6 Typo | og en cardigan knppet over | 'knppet' | og en cardigan kneppet over |
| 469 | 1664 | 3 Mistranslation | Han ristet litt ut på en ren skål | EN 'a clean saucer' | Han ristet litt ut på et rent tefat |
| 470 | 1665 | 4 Proper name | – Det er den typen, sa Doc. | Doc = doktoren | – Det er den typen, sa doktoren. |
| 471 | 1665 | 6 Typo | stemmer overens med dette arkket. | 'arkket' | stemmer overens med dette arket. |
| 472 | 1672 | 4 Proper name | Ved siden av lå Docs lapp, | Doc = doktoren | Ved siden av lå doktorens lapp, |
| 473 | 1678 | 3 Mistranslation | – Tanaka, sa hun. | wrong speaker: Nick says it | – Tanaka, sa han. |
| 474 | 1682 | 3 Mistranslation | helt til jeg satte ned en skål med brisling til henne. | EN 'a saucer of smelts' (krøkle; brisling = sprats) | helt til jeg satte ned et tefat med krøkle til henne. |
| 475 | 1687 | 4 Proper name | En tynn bunke med Pelkeys fakturaer | supplier name | En tynn bunke med fakturaer fra Pelkey's |
| 476 | 1689 | 6 Term | – Gretas takksigelsesbestillingsbok lå oppe på disken hennes | Thanksgiving / the order book (clue item) as elsewhere | – Gretas Thanksgiving-bestillingsbok lå oppslått på disken hennes |
| 477 | 1692 | 6 Term (clue) | – Klagen kalte kjølerommet for det kalde rommet og utslagsvasken for Hobart-vasken. | hand-sink = håndvasken (Ch9); Joyce's two words set off as quoted words as in Ch9 | – Klagen kalte kjølerommet «det kalde rommet» og håndvasken «Hobart-vasken». |
| 478 | 1692 | 6 Term | Låsen på gårdsplassporten har aldri vært skiftet, | yard gate (as Ch20) | Låsen på porten til bakgården har aldri vært skiftet, |
| 479 | 1692 | 3 Mistranslation | Og surringen stanset den morgenen Greta begynte å skyve helslåen for bakdøren sin etter mursteinen, så hvem som helst som gjorde det, kom inn den veien. | 'surringen' (the buzzing) = the souring; 'helslåen' not a word; 'whoever did it' | Og syrningen stanset den morgenen Greta begynte å skyve slåen for bakdøren sin etter mursteinen, så den som gjorde det, kom inn den veien. |
| 480 | 1692 | 6 Term | og det var ikke kjøttmannens. I går så han på Claires utskrift av Wendts varebil | 'not the meat man's' (Ch7 'Ikke kjøttbilens'); bakery name | og det var ikke kjøttbilens. I går så han på Claires utskrift av Wendt's-varebilen |
| 481 | 1694 | 3 Mistranslation | ved Gretas vinduskarm før daggry, | Greta's back-door sill | ved Gretas dørstokk før daggry, |
| 482 | 1696 | 4 Proper name | Flygebladet kom ikke opp på tavlen til avholdslokalet før den trettiende. Pelkeys sekk gikk | the Grange board ('avholdslokalet' = temperance hall); supplier name | Flygebladet kom ikke opp på tavlen i grendehuset før den trettiende. Sekken fra Pelkey's gikk |
| 483 | 1696 | 6 Term (clue) | Og Docs lapp sier at pulveret i krukken min stemmer overens med surdeigsgrunnlaget, test for test. | sour base = syrningsmiddel; Doc = doktoren | Og doktorens lapp sier at pulveret i krukken min stemmer overens med syrningsmiddelet, test for test. |
| 484 | 1698 | 6 Term (clue) | Surdeigsgrunnlag, én sekk, levert til Wendts Bakehouse, Bridgton. Signert for, J. Wendt. | the invoice must name the same substance; 'Signert for,' is a calque | Syrningsmiddel, én sekk, levert til Wendt's Bakehouse, Bridgton. Mottak kvittert: J. Wendt. |
| 485 | 1703 | 6 Typo | Saktsomt, der hun gjentok | 'Saktsomt' | Sakte, mens hun gjentok |
| 486 | 1711 | 6 Term | – Ut av søppelkassen bak Sugarplum, tror jeg, akkurat som mursteinen. Hvem som helst i kvartalet kan nå opp i den. | the dumpster = containeren (Ch19); 'reach into it' | – Fra containeren bak Sugarplum, tror jeg, akkurat som mursteinen. Hvem som helst i kvartalet kan nå ned i den. |
| 487 | 1732 | 6 Typo | kom opp stasetrappene like etterpå | 'stasetrappene' | kom opp trappen til politistasjonen like etterpå |
| 488 | 1739 | 3 Mistranslation (echo) | – Stillwater. De ville ha tomten, hele greia og navnet. | EN 'They wanted the lot, lock, stock and name' — echoes her Ch2 line ('med hud, hår og navn'); 'tomten' = the plot of land | – Stillwater. De ville ha alt, med hud, hår og navn. |
| 489 | 1751 | 3 Mistranslation | Hun kom med en form til meg, og jeg spiste den. | EN 'a casserole' (the food) | Hun kom med en gryterett til meg, og jeg spiste den. |
| 490 | 1765 | 4 Title | Lensmann Tanaka hadde ordnet i stand rommet selv, | Chief Tanaka = politisjef ('lensmann' is a Norwegian rural sheriff) | Politisjef Tanaka hadde ordnet i stand rommet selv, |
| 491 | 1767 | 4 Title | – Lensmann. Joyce satte posen | Chief = politisjef | – Politisjef. Joyce satte posen |
| 492 | 1771 | 8 Units (SAFE) | skjøv ringen et par tommer utenfor rekkevidde. | 'a few inches' → noen centimeter | skjøv ringen noen centimeter utenfor rekkevidde. |
| 493 | 1774 | 4 Title | – Ms. Wendt, sa Tanaka, du er ikke pågrepet. | English 'Ms.'; Ch22 uses 'Fru Wendt' | – Fru Wendt, sa Tanaka, du er ikke pågrepet. |
| 494 | 1777 | 6 Term/4 Name | der hun stod med piassavakosten i hendene, og jeg hadde likt henne i bedehuset | the push broom (Ch4); the Grange = grendehuset ('bedehuset' = prayer house) | der hun stod med den brede kosten i hendene, og jeg hadde likt henne i grendehuset |
| 495 | 1780 | 6 Typo | hver eneste bakerikunne vi kan finne, | 'bakerikunne' | hver eneste bakerikunde vi kan finne, |
| 496 | 1781 | 3 Mistranslation (CLUE) | – Klagen til kommunen omtalte butikklokalet hennes som kjølerommet og oppvaskkummen som Hobart-vasken. | EN 'called her walk-in the cold room and her hand-sink the Hobart sink' — the NO had 'the shop room' called 'the walk-in' and dropped Joyce's word 'det kalde rommet' entirely, so the confrontation lost its key slip; also 'kommunen' → the county | – Klagen til fylket kalte kjølerommet hennes «det kalde rommet» og håndvasken hennes «Hobart-vasken». |
| 497 | 1782 | 3 Mistranslation (CLUE) | – Halvparten på min alder sier kjølerom. | EN 'Half the bakers my age say cold room' — Joyce's defence must use her own giveaway word; 'kjølerom' is Greta's ordinary word (walk-in) | – Halvparten av bakerne på min alder sier «det kalde rommet». |
| 498 | 1783 | 6 Term (clue) | – Dr. Mitchell matchet pulveret i melet hennes med en surdeigsbase. Pelkey's leverte en sekk til deg den 27. oktober, etter flere måneder uten. Du signerte fraktbrevet. | sour base = syrningsmiddel; 'the ticket' = følgeseddelen (Ch21); Doc = doktor | – Doktor Mitchell har funnet at pulveret i melet hennes stemmer med et syrningsmiddel. Pelkey's leverte en sekk til deg den 27. oktober, etter flere måneder uten. Du kvitterte på følgeseddelen. |
| 499 | 1784 | 4 Title | – Jeg baker rug, lensmann. | Chief = politisjef | – Jeg baker rug, politisjef. |
| 500 | 1784 | 6 Term (clue) | – Alle rugbakere i New England kjøper surdeigsbase. | Joyce's defence must name the same substance | – Alle rugbakere i New England kjøper syrningsmiddel. |
| 501 | 1785 | 6 Typo | før det lysnede, | verb form | før det lysnet, |
| 502 | 1787 | 3 Mistranslation | kom gjennom hageporten min, | EN 'my yard gate' | kom gjennom porten til bakgården min, |
| 503 | 1789 | 3 Mistranslation | Den ene henger i ringen min. Den andre fikk jeg slipt til deg | EN 'on my ring' (Ch20 'på knippet mitt'); 'had cut for you' (a key is made, not ground) | Den ene henger på knippet mitt. Den andre fikk jeg laget til deg |
| 504 | 1790 | 6 Typo/3 Mistranslation | Joyces hånd fløy til nøkelringen | 'nøkelringen'; EN 'went to' (she didn't know she'd done it) | Joyces hånd gikk til nøkkelringen |
| 505 | 1791 | 8 Units (SAFE) | nebbet kom en tomme opp, | 'an inch' → et par centimeter | nebbet løftet seg et par centimeter, |
| 506 | 1793 | 6 Term (echo) | Du forandret den aldri. | echoes Greta's 'Jeg skiftet den aldri' (Ch20) — the old gate lock | Du skiftet den aldri. |
| 507 | 1799 | 8 Units (SAFE) | et pund sjokolade vi ikke hadde råd til. | 'a pound of chocolate' → et halvt kilo | et halvt kilo sjokolade vi ikke hadde råd til. |
| 508 | 1799 | 4 Proper name | Det ligger et kort i den esken på bedehuset | the Grange = grendehuset | Det ligger et kort i den esken i grendehuset |
| 509 | 1801 | 4 Title | om lensmannen vil lese dem. | Chief = politisjef | om politisjefen vil lese dem. |
| 510 | 1801 | 3 Mistranslation | engros, lastebiler, bedrifter, | EN 'trucks, accounts' | engros, lastebiler, kundekontoer, |
| 511 | 1806 | 6 Grammar | var jeg glad, Gud for meg tilgi, | garbled word order | var jeg glad, Gud tilgi meg, |
| 512 | 1808 | 6 Term | Du kastet en teglstein | brick = murstein | Du kastet en murstein |
| 513 | 1814 | 6 Typo | Joyce stansed. | 'stansed' | Joyce stanset. |
| 514 | 1815 | 3 Mistranslation | hadde ansiktet stivnet igjen, rent som en lukket eske. | EN 'her face had closed again, neat as a shut box' | hadde ansiktet lukket seg igjen, pent som en lukket eske. |
| 515 | 1820 | 4 Title | – Du vil nok ha en advokat nå, Ms. Wendt, | English 'Ms.' | – Du vil nok ha en advokat nå, fru Wendt, |
| 516 | 1824 | 6 Typo | Ved døren stansed hun | 'stansed' | Ved døren stanset hun |
| 517 | 1828 | 3 Mistranslation | messingnøkkelen hun hadde slipt til Joyce det året de åpnet, holdt den i håndflaten et øyeblikk, la den vekk i kappelommen og knep klaffen fast over den. | key 'cut'; 'kappe' = cape; 'buttoned the flap' | messingnøkkelen hun hadde fått laget til Joyce det året de åpnet, holdt den i håndflaten et øyeblikk, la den vekk i kåpelommen og kneppet klaffen igjen over den. |
| 518 | 1830 | 4 Title | Sjef Tanaka hadde siktelsene klare | Chief = politisjef | Politisjef Tanaka hadde siktelsene klare |
| 519 | 1832 | 4 Proper name | fra Docs låste skap selv, | Doc = doktoren | fra doktorens låste skap selv, |
| 520 | 1834 | 3 Mistranslation | Pip glimret forbi det mot søppelbøtta ved døren | EN 'Pip passed it up for the wastebasket'; 'glimret forbi' is meaningless | Pip lot den være og gikk heller til papirkurven ved døren |
| 521 | 1836 | 6 Term (clue) | – Skadeverk. Det er melet, den sure grunndeigen hun puttet oppi for å ødelegge fire deiger for Greta. | sour base = syrningsmiddel ('sure grunndeigen' = sour base dough) | – Skadeverk. Det er melet, syrningsmiddelet hun puttet oppi for å ødelegge fire omganger av Gretas deig. |
| 522 | 1836 | 3 Mistranslation | Hun hadde båret teglsteinen fra Gretas bakromsuke ned bakgaten selv på søndag og holdt den mot ruinene | EN 'from Greta's back-room shelf' ('bakromsuke' garbled); 'rubble'; brick = murstein; alley = smuget | Hun hadde båret mursteinen fra hyllen i Gretas bakrom ned smuget selv på søndag og holdt den mot byggeavfallet |
| 523 | 1836 | 6 Term | Den samme gamle røde teglsteinen | brick = murstein | Den samme gamle røde mursteinen |
| 524 | 1840 | 3 Mistranslation (CLUE) | Kjølerrommet og Hobart-vasken, skrevet på maskin | EN 'The cold room and the Hobart sink' — Joyce's words, not 'kjølerommet' (Greta's walk-in word); typo 'Kjølerrommet' | «Det kalde rommet» og «Hobart-vasken», skrevet på maskin |
| 525 | 1848 | 3 Mistranslation | – Det er rettens avdeling. | EN 'That's the court's business' | – Det er rettens sak. |
| 526 | 1852 | 4 Title | over sjefens bord, | Chief = politisjef | over politisjefens bord, |
| 527 | 1852 | 6 Typo | hørte på tapene som ble rammet opp | 'rammet' | hørte på tapene som ble ramset opp |
| 528 | 1858 | 6 Term (clue) | – Ikke som han fant. En sur deig er en matvare. Den ødelegger bare den feile deigen. | sour base = syrningsmiddel ('en sur deig' = a sour dough) | – Ikke som han fant. Et syrningsmiddel er en matvare. Det ødelegger bare feil deig. |
| 529 | 1858 | 6 Term/3 Mistranslation | to gjestgiverier ringte sjåføren hennes før han var ferdig med å laste varen. | inns = vertshus; EN 'loading the van' | to vertshus ringte sjåføren hennes før han var ferdig med å laste varebilen. |
| 530 | 1860 | 3 Mistranslation | Pip kom opp fra søppelbøtta | EN 'the wastebasket' | Pip kom opp fra papirkurven |
| 531 | 1866 | 3 Mistranslation | Summen var sjefens oppgave å overbringe. | EN 'The figure was the chief's to bring her' | Tallet var det politisjefen som skulle bringe henne. |
| 532 | 1868 | 3 Mistranslation | på et lite gullmaleri: | EN 'a little gold easel' ('gullmaleri' = gold painting) | på et lite gullstativ: |
| 533 | 1870 | 3 Mistranslation/6 Term | Pip kjente reglene ved det laget og stanset på trinnet, under balsamkransen | EN 'knew the rule by now'; balsam = granbar | Pip kjente regelen nå og stanset på trinnet, under granbarkransen |
| 534 | 1880 | 4 Proper name | med Doc Mitchell og la det frem | Doc = doktor | med doktor Mitchell og la det frem |
| 535 | 1888 | 4 Title | – Sjefen var innom i går kveld | Chief = politisjef | – Politisjefen var innom i går kveld |
| 536 | 1888 | 6 Term | at teglsteinen kom ut | brick = murstein | at mursteinen kom ut |
| 537 | 1894 | 3 Mistranslation | Kvinner fra kirkens kveldsmåltider stod alt | EN 'Women from the church suppers' (Ch14 'kirkemiddagen') | Kvinner fra kirkemiddagene stod alt |
| 538 | 1898 | 6 Typo/3 Mistranslation | ved siden av en med som han holdt på å tilpasse. Pip stakk rett bort til skiferhørnet, | 'en med' → 'en mede' (sleigh runner); EN 'the fieldstone hearth' ('skiferhørnet' = slate corner) | ved siden av en mede som han holdt på å forme. Pip stakk rett bort til ildstedet av marksteiner, |
| 539 | 1900 | 3 Mistranslation | lot meg slå meg ned på hjertekanten | EN 'the hearth's edge'; 'hjertekanten' = the heart's edge | lot meg slå meg ned på kanten av ildstedet |
| 540 | 1904 | 3 Mistranslation | – Theo eide det i det sekundet han ble funnet, | EN 'Theo owned it' = admitted it | – Theo vedgikk det i det sekundet han ble avslørt, |
| 541 | 1904 | 6 Term | Sykehuset har droppet henne. Gjestgiveriene også. | inns = vertshus | Sykehuset har droppet henne. Vertshusene også. |
| 542 | 1912 | 6 Term | Jeg så gullet vende seg over det tomme ristverket. | grate = rist | Jeg så gullet vende seg over den tomme risten. |
| 543 | 1925 | 6 Term (clue) | Delen til vasken hadde kommet | hand-sink = håndvasken | Delen til håndvasken hadde kommet |
| 544 | 1927 | 6 Grammar | Kjøkkenet deres var i orden | EN 'Your kitchen' addressed to Greta alone (du throughout) | Kjøkkenet ditt var i orden |
| 545 | 1933 | 3 Mistranslation | Greta så på papiret en lang stund med hendene i kors. | EN 'hands folded'; 'hendene i kors' = hands crossed | Greta så på papiret en lang stund med hendene foldet. |
| 546 | 1933 | 6 Term | skar av ham hjørnet av en sjokoladepekannkake | the chocolate-pecan is a pie (Ch5 'Sjokolade-pekannpaien') | skar av ham hjørnet av en sjokolade-pekannpai |
| 547 | 1937 | 4 Proper name | hun som pleide å ta med brødet til bygdelaget. | EN 'who brought the bread to the Grange' (one occasion); the Grange = grendehuset | hun som tok med brødet til grendehuset. |
| 548 | 1941 | 6 Typo | mens de stamphoppet i kulden. | 'stamphoppet' | mens de stampet i kulden. |
| 549 | 1941 | 3 Mistranslation | Sjokoladebollene var borte ved halv fire-tiden. Pepperkakene var søkk borte i bunnen av krukken. Hun satte i gang en omgang kanelsnurrer klokken tre | EN 'gone by half past' (two); gingersnaps = ingefærkjeks; cinnamon rolls = kanelboller (blurb, Ch2) | Sjokoladebollene var borte ved halv tre-tiden. Ingefærkjeksene var borte helt ned til bunnen av krukken. Hun satte i gang en omgang kanelboller klokken tre |
| 550 | 1941 | 3 Mistranslation | før de hadde reist seg ordentlig. | EN 'before they'd cooled' | før de rakk å bli kalde. |
| 551 | 1947 | 6 Term | sjokoladeboller | cocoa buns = kakaoboller | kakaoboller |
| 552 | 1951 | 3 Mistranslation | Hal kom for den matboksen han alltid kom for, | EN 'the food-barrel box' | Hal kom for esken til mattønnen han alltid kom for, |
| 553 | 1953 | 3 Mistranslation | – Til boksene, sa han, | EN 'For the barrels' | – Til tønnene, sa han, |
| 554 | 1965 | 6 Term | sjokoladebolle | cocoa buns = kakaoboller | kakaobolle |
| 555 | 1973 | 6 Term | kjøpte en sjokoladepekannkake han åpenbart | pie | kjøpte en sjokolade-pekannpai han åpenbart |
| 556 | 1977 | 6 Typo | Utpå senettertermiddagen | 'senettertermiddagen' | Utpå senettermiddagen |
| 557 | 1983 | 6 Grammar | Hun hadde helt sparepengene sine i god mel | neuter | Hun hadde helt sparepengene sine i godt mel |
| 558 | 1985 | 4 Title | Sjefen leste opp beløpet | Chief = politisjef | Politisjefen leste opp beløpet |
| 559 | 1987 | 6 Typo | Hun pressede på skuffen med rotet av hånden og ga opp. | 'pressede'; 'rotet av hånden' = the mess of the hand; EN 'heel of her hand' | Hun presset på skuffen med håndroten og ga opp. |
| 560 | 1991 | 6 Term | etter kanelsnurrer som hun | cinnamon rolls = kanelboller | etter kanelboller som hun |
| 561 | 1993 | 6 Typo/Term (clue) | Takketakkingsordreboken hennes lå oppe på bakbordet | 'Takketakkingsordreboken' garbled; order book = bestillingsboken | Thanksgiving-bestillingsboken hennes lå oppslått på bakbordet |
| 562 | 1995 | 3 Mistranslation | Jeg har ført deg opp på to sjokoladepekannkaker og et dusin snurrer, | Martha's order (Ch14/Ch20): two chocolate-pecan pies and a dozen rolls (rundstykker) | Jeg har ført deg opp på to sjokolade-pekannpaier og et dusin rundstykker, |
| 563 | 2005 | 6 Term | men hun pakket inn en hel sjokoladepekannkake i en eske, | pie | men hun pakket inn en hel sjokolade-pekannpai i en eske, |
| 564 | 2009 | 4 Title | til Joyce over sjefens bord, | Chief = politisjef | til Joyce over politisjefens bord, |
| 565 | 2020 | 6 Term | reddet vi Selskapet | Historical Society = Historielaget (Inn Trouble NO 48×, Frost and Found NO); 'Selskapet' (the Company) was used 35× | reddet vi Historielaget |
| 566 | 2022 | 4 Title | hadde Mr. Worthington tilbudt seg | English 'Mr.' | hadde herr Worthington tilbudt seg |
| 567 | 2022 | 3 Mistranslation | i det tidlige grålysene, med frostrøyk som slo opp, mens de første slepene og hanskjerrene kom | 'grålysene' typo; EN 'my breath going up white'; 'sleds and hand-trucks' | i det tidlige grålyset, med pusten som sto hvit, mens de første kjelkene og sekketrallene kom |
| 568 | 2022 | 6 Term | Tilbudet hans sto fremdeles ved lag hvis bygda kom til kort, og jeg akterte ikke å hente det med mindre vi måtte. Hvis bygda betalte for sitt eget tak, ville bygningen tilhøre bygda, | town = byen throughout the book ('bygda' = rural parish); 'akterte' typo | Tilbudet hans sto fremdeles ved lag hvis byen kom til kort, og jeg aktet ikke å hente det med mindre vi måtte. Hvis byen betalte for sitt eget tak, ville bygningen tilhøre byen, |
| 569 | 2022 | 6 Term | mot Selskapets grønne dør | Historical Society = Historielaget (Inn Trouble NO 48×, Frost and Found NO); 'Selskapet' (the Company) was used 35× | mot Historielagets grønne dør |
| 570 | 2026 | 3 Mistranslation | med et nyopprettet ark på platen sin, | EN 'a fresh ruled sheet on his board' | med et nylinjert ark på skriveplaten sin, |
| 571 | 2028 | 6 Typo | kjellarlaget nede, | Nynorsk 'kjellar' | kjellerlaget nede, |
| 572 | 2038 | 3 Mistranslation | Ved lunsjtider var det dekket til med ny tro og nye takbord, | EN 'fresh sheathing and new shingle'; 'ny tro' = new faith | Ved lunsjtid var det dekket med nytt undertak og ny takspon, |
| 573 | 2040 | 6 Typo | Under dem slet kjellarlaget | Nynorsk 'kjellar' | Under dem slet kjellerlaget |
| 574 | 2042 | 3 Mistranslation | – Gå og hjelp noen andre. | EN 'Go count somebody else' (Hal with his tally) | – Gå og tell opp noen andre. |
| 575 | 2046 | 6 Term | Det sto et Norgesglass på disken til Kelly | EN 'a jar'; 'Norgesglass' is a brand name | Det sto en krukke på disken til Kelly |
| 576 | 2046 | 3 Mistranslation | siden matutdelingen startet. | EN 'the food drive' (a collection) | siden matinnsamlingen startet. |
| 577 | 2046 | 6 Term | Syklubben hadde arrangert et lotteri. | the circle = sirkelen in this book and Book 1 NO | Sirkelen hadde arrangert et lotteri. |
| 578 | 2050 | 6 Typo | av venligere folk. | 'venligere' | av vennligere folk. |
| 579 | 2052 | 6 Grammar | Nær lunsjtider fisket Hal opp en konvolutt av sigarboksen uten navn på | 'lunsjtider'; word order | Nær lunsjtid fisket Hal opp en konvolutt uten navn på fra sigarboksen |
| 580 | 2052 | 1 Untranslated English | hos en urmaker to bygder unna. Theo was oppe på stigen | 'was' is English; 'two towns over' (Ch18 'to byer unna') | hos en urmaker to byer unna. Theo var oppe på stigen |
| 581 | 2060 | 3 Mistranslation | Ingen hadde glemt den siste måneden, | EN 'last month' | Ingen hadde glemt forrige måned, |
| 582 | 2070 | 6 Typo | stappet hun en boll ut i den. | 'boll'; 'ut i' wrong | stappet hun en bolle i den. |
| 583 | 2072 | 6 Term | sto en rad med barnas snømenn på plenen, | the green = allmenningen | sto en rad med barnas snømenn på allmenningen, |
| 584 | 2072 | 6 Term | vendt mot Selskapet | Historical Society = Historielaget (Inn Trouble NO 48×, Frost and Found NO); 'Selskapet' (the Company) was used 35× | vendt mot Historielaget |
| 585 | 2078 | 6 Term | Selskapet hadde åpnet dørene for hele bygda. | town = byen | Selskapet hadde åpnet dørene for hele byen. |
| 586 | 2078 | 6 Term | Gretas oppskriftskort på sjokolade og pekannøtter, og Brams to ørlite små vanten, | matches Ch15 ('oppskriftskort på sjokolade-pekannpai', 'Brams … votter'); 'ørlite' typo | Gretas oppskriftskort på sjokolade-pekannpai, og Brams to bitte små votter, |
| 587 | 2078 | 4 Proper name | hadde Claire nålet fast kortet fra Samvirkelagets innsamling. | EN 'the card from the Grange drive' ('Samvirkelaget' = the Co-op) | hadde Claire nålet fast kortet fra innsamlingen i grendehuset. |
| 588 | 2078 | 6 Term | Selskapet hadde åpnet | Historical Society = Historielaget (Inn Trouble NO 48×, Frost and Found NO); 'Selskapet' (the Company) was used 35× | Historielaget hadde åpnet |
| 589 | 2080 | 6 Grammar | kom heller ikke til gjøre det, | missing 'å' | kom heller ikke til å gjøre det, |
| 590 | 2082 | 4 Title | Sjef Tanaka sa noen enkle ord. | Chief = politisjef | Politisjef Tanaka sa noen enkle ord. |
| 591 | 2090 | 6 Typo | der alle myntet øynene mot lyset. | 'myntet øynene' (coined their eyes); EN 'all of them squinting' | der alle myste mot lyset. |
| 592 | 2100 | 6 Term | av tørket balsamgran og bær, | balsam = granbar | av tørket granbar og bær, |
| 593 | 2108 | 6 Term | Hun hadde en vante. Bare én. | mittens = votter (Ch15, Book 1 NO) | Hun hadde en vott. Bare én. |
| 594 | 2110 | 4 Proper name | og den jeg hadde lagt i hos Samvirkelaget, | EN 'at the Grange' | og den jeg hadde lagt i i grendehuset, |
| 595 | 2116 | 6 Term | Selskapets bygning | Historical Society = Historielaget (Inn Trouble NO 48×, Frost and Found NO); 'Selskapet' (the Company) was used 35× | Historielagets bygning |
| 596 | 2122 | 6 Term (echo) | – La det være opptegnet at Frost Falls ikke ble bygd av de sterke. Det ble bygd av de som holdt sammen med naboene sine. | the founder's line must read identically in Ch6 [594], the Gazette [621] and here (EN identical) | – La det være opptegnet at Frost Falls ikke ble bygget av de sterke. Det ble bygget av de som var gode naboer. |
| 597 | 2124 | 6 Term | Selskapets samling | Historical Society = Historielaget (Inn Trouble NO 48×, Frost and Found NO); 'Selskapet' (the Company) was used 35× | Historielagets samling |
| 598 | 2128 | 6 Term | De kunne bygda utenat fra før. | town = byen | De kunne byen utenat fra før. |
| 599 | 2130 | 6 Term | at det fantes en sardin i frakkelommen min. | Jessica's coat = kåpe | at det fantes en sardin i kåpelommen min. |
| 600 | 2132 | 6 Term | over bygdas latter, | town = byen | over byens latter, |
| 601 | 2138 | 6 Term | Han la den oppi blant vantene og stiften. | mittens = votter | Han la den oppi blant vottene og stiften. |
| 602 | 2140 | 3 Mistranslation | i det tilsølte snekkerforkleet sitt, | EN 'his blacked apron' (the blacksmith); 'snekker' = carpenter | i det svertede forkleet sitt, |
| 603 | 2142 | 3 Mistranslation (reversed) | oppstilt over plenen og oppover gangstien, snudd for å møte de opplyste vinduene, dusinvis av dem der barna hadde bygd en hel haug. | EN 'dozens of them where the children had built a handful' — the NO said the children had built 'a whole heap', losing the magic; the green = allmenningen | oppstilt over allmenningen og oppover gangstien, snudd mot de opplyste vinduene, dusinvis av dem, der barna bare hadde bygd en håndfull. |
| 604 | 2146 | 6 Typo | som hun overhode kunne komme. | 'overhode' | som hun overhodet kunne komme. |
| 605 | 2149 | 3 Mistranslation | for å hente kranseringens faste bestilling. | EN 'the wreath-circle's standing order'; 'kranseringen' (the wreath ring) is garbled | for å hente sirkelens faste kransbestilling. |
| 606 | 2151 | 3 Mistranslation | Greta sto ved det lange bordet i hvetemelet sitt, | EN 'in her flour' | Greta sto ved det lange bordet i melet sitt, |
| 607 | 2151 | 6 Typo | ved disken og kntet frakker over pakker, | 'kntet' | ved disken og kneppet frakker over pakker, |
| 608 | 2161 | 4 Title | Jeg tok den med ned til sjefen før jeg åpnet den, | Chief = politisjef | Jeg tok den med ned til politisjefen før jeg åpnet den, |
| 609 | 2169 | 4 Title | Inne på sjefens kontor begynte | Chief = politisjef (italic letter kept) | Inne på politisjefens kontor begynte |
| 610 | 2171 | 6 Grammar | Morens mine pekannøtter, min idé. | 'Morens mine' garbled; EN 'My mother's pecans' | Min mors pekannøtter, min idé. |
| 611 | 2177 | 6 Grammar | – I førti år har jeg kjent den kvinne, | definite form | – I førti år har jeg kjent den kvinnen, |
| 612 | 2179 | 6 Register | Siden Joyce gikk sin veg, | 'veg' (Nynorsk/radical form) | Siden Joyce gikk sin vei, |
| 613 | 2181 | 3 Mistranslation | – Svar med en pai, sa hun. | wrong speaker: EN '"Answer it with a pie," I said.' | – Svar med en pai, sa jeg. |
| 614 | 2187 | 6 Grammar/Term | og stakk det ned i bakerst i bestillingsboka for Thanksgiving. | 'ned i bakerst' garbled; order book = bestillingsboken | og stakk det inn bakerst i Thanksgiving-bestillingsboken. |
| 615 | 2203 | 6 Term | avyen | 'avyen' is not a Norwegian word; avenue = alléen | alléen |
| 616 | 2203 | 6 Term | i retning av Selskapet | Historical Society = Historielaget (Inn Trouble NO 48×, Frost and Found NO); 'Selskapet' (the Company) was used 35× | i retning av Historielaget |
| 617 | 2205 | 6 Term | Selskapshuset var varmt, | Society building = Historielagets hus | Historielagets hus var varmt, |
| 618 | 2205 | 6 Term | Selskapet føltes | Historical Society = Historielaget (Inn Trouble NO 48×, Frost and Found NO); 'Selskapet' (the Company) was used 35× | Historielaget føltes |
| 619 | 2207 | 3 Mistranslation | Den nye, treskaftesken med lokket igjen | EN 'the cedar box' ('treskaftesken' = wooden-shaft box) | Den nye sedertreesken med lokket igjen |
| 620 | 2225 | 6 Term | avyen | 'avyen' is not a Norwegian word; avenue = alléen | alléen |
| 621 | 2229 | 6 Term | og fant Nick inne ved arnestedet. | hearth = ildsted (Ch8, Inn Trouble NO) | og fant Nick inne ved ildstedet. |
| 622 | 2231 | 6 Term | Han satt foran det kalde jernet | EN 'the cold grate' = rist | Han satt foran den kalde risten |
| 623 | 2235 | 6 Term | Og i gruben, der det aldri hadde vært lagt noe, | EN 'in the grate' | Og i risten, der det aldri hadde vært lagt noe, |
| 624 | 2237 | 3 Mistranslation | Men den er nærmere brannen i kveld | EN 'nearer the fire' (hearth-fire, not a blaze) | Men den er nærmere ilden i kveld |
| 625 | 2239 | 6 Term | trukket en håndsbredd nærmere arnestedet sitt. | hearth = ildsted | trukket en håndsbredd nærmere ildstedet sitt. |
| 626 | 2239 | 6 Term | i Selskapet og | Historical Society = Historielaget (Inn Trouble NO 48×, Frost and Found NO); 'Selskapet' (the Company) was used 35× | i Historielaget og |
| 627 | 2241 | 6 Grammar/Term | heiv seg ned på den varme ildstedet med et lite grynt. Hun strakte luffene mot varmen som ingen brann skapte, | EN 'the warm hearthstone' (gender clash 'den … ildstedet'); 'no fire made' | heiv seg ned på den varme ildstedsteinen med et lite grynt. Hun strakte luffene mot varmen som ingen ild skapte, |
| 628 | 2243 | 6 Term | og et arnested som var varmere | hearth = ildsted | og et ildsted som var varmere |
| 629 | 2247 | Ruling 7/Sell line | Start serien Spine and Spells med  | series name as published in Norwegian (2buploaded. Binder's Bequest_Norwegian.docx: 'Rygger og Trolldom'); title anchor kept for stamping | Start serien Rygger og Trolldom med  |
| 630 | 2249 | 3 Mistranslation | og sakkyndigrevisoren som kunne oppdage en forfalskning ved første øyekast, mistet alt unntak for forstørrelsesglasset sitt. | EN 'the forensic document examiner … lost everything but her loupe'; 'sakkyndigrevisoren' (expert auditor), 'unntak for' garbled | og den rettsmedisinske dokumentgranskeren som kunne avsløre en forfalskning ved første øyekast, mistet alt unntatt luppen sin. |
| 631 | 2250 | 3 Mistranslation | Så kollapser formannen i Historielaget på Måneskinnballmaskeraden, mens hun klamrer seg til en liten skinn dagbok, | EN 'the president … collapses … clutching a small leather diary' (MT made Fiona the one clutching it); ball name as in the published NO edition | Så faller lederen av Historielaget om på Måneskinnsmaskerade-ballet, med en liten skinndagbok klemt i hånden, |
| 632 | 2253 | Ruling 7/Sell line | Start Spine & Spells-mysteriet med  | series name as published in Norwegian; EN 'mysteries' | Begynn på Rygger og Trolldom-mysteriene med  |
| 633 | 2257 | Ruling 7/Sell line | Start serien Spine and Spells med  | series name as published in Norwegian | Start serien Rygger og Trolldom med  |
| 634 | 2312 | 1 Untranslated English | Start reading The Binder's Bequest today! | closing line left in English; translated and the real title anchored for stamping (as the other two sell lines) | Begynn å lese <bt>The Binder's Bequest</bt> i dag! |
| + | 1162 | AI meta-text | (translator meta-note text) | the MT left translator notes in the prose ('– fylkesmannen i kilden er county man …', 'La oss bruke … for å bevare kildens "county man"'); deleted, sentence completed as EN 'before the county man ever set foot in Greta's kitchen'. Removes 2 italic runs that came from asterisk-marked meta-notes | (deleted; sentence ends '... før mannen fra fylket i det hele tatt satte foten sin i Gretas kjøkken.') |
| + | 1163 | AI meta-text | (translator meta-note text) | 'Retting: før mannen fra fylket …' is a translator's correction note, not prose; emptied (paragraph kept). Removes 1 italic run | (deleted; sentence ends '... før mannen fra fylket i det hele tatt satte foten sin i Gretas kjøkken.') |
| + | 2078 | Ruling 5 + Ruling 3 | &lt;bt&gt;What shall we send them, a hundred years on?&lt;/bt&gt; | stray <bt> on English card text; translated identically to the Ch15 card [1149] and set in italics as in the English (+1 italic run) | _Hva skal vi sende dem, hundre år frem i tid?_ |
| + | 2140 | Ruling 5 + Ruling 3 | &lt;bt&gt;To be sealed when the old one is opened, at the new year.&lt;/bt&gt; | stray <bt> on English card text; translated identically to the Ch15 card and set in italics as in the English (+1 italic run) | _Skal forsegles når den gamle åpnes, ved det nye året._ |
