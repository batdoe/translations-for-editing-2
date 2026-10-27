# APPLIED — Inn Trouble - ASSEMBLED - FORMATTED_Dutch (second pass, 2026-10-27)

Target: `translated\corrected\Inn Trouble - ASSEMBLED - FORMATTED_Dutch.docx` (copied fresh from `translated\`; the old corrected copy was byte-identical and is backed up as `corrected\_bak\Inn Trouble - ASSEMBLED - FORMATTED_Dutch.pre-proofread2-20261027.docx`).

Method: run-level edits only (lxml; only the `<w:t>` text that changes is touched; an edit that would cross a formatting boundary is refused). Every edit matched its exact Dutch string once in the stated paragraph before writing.

- Applied: 1 book-wide dialogue pass (385 paragraphs „…” → ‘…’; 43 attributions rebuilt ”, → ,’; 2 nested quotes → “…”; 51 straight apostrophes → ’) + 171 targeted edits (2 batches: 166 + 5). Total findings applied: 172.
- Refused by verification: 0.
- Prior-report quotes not found: 0 of 281 (all web fixes present and kept).
- Needs a decision: 5 (NL2-D1 … NL2-D5 in `PROOFREAD_DECISIONS.md`).
- Italic runs changed (text only, where italic text was translated/corrected): para 297 banner 'FROST FALLS THROUGH THE YEARS' → 'FROST FALLS DOOR DE JAREN'; para 1037 (second note) 'de hele stad' → 'het hele stadje'. Italic run count 23 → 23, order unchanged.
- `<bt>` spans: 10 → 4 (6 non-title spans removed under ruling 5; remaining: Inn Trouble ×2, Frost and Found, Flour Play).
- Paragraph count: 1567 → 1567.

## Checks on the corrected copy
1. looks_english: `[]` (empty).
2. bt_anchors check: 4 spans, 0 unpaired; texts = Inn Trouble, Frost and Found, Flour Play.
3. check_matter --file: 1 PASS, 0 FAIL.
4. preflight --verify: paragraphs 1567 → 1567 ok; italic runs 23 → 23 ok; italic sequence DIFFERS only at the two translated italic runs above; scene breaks 4 → 4 ok; bt anchors 10 → 4 'UNDECLARED -6' and 'lost' = The Holly Jolly Bakery, Frost Falls, Winter Wonderland Inn, the sapphire at its heart (Yarn Tales ×2 also removed) — all required by ruling 5; overall FAIL on those expected items only.

## Edits (para, was → now, why)
| # | Para | Class | Was | Now | Why |
|---|---|---|---|---|---|
| 1 | 34 | 3 Reversed meaning | Een smid die twintig dollar schuldig was en | Een smid die nog twintig dollar tegoed had en | EN 'A blacksmith owed twenty dollars' = Sam is OWED the money; Dutch made him the debtor |
| 2 | 45 | 6 Term | waggelde het portiek op zodra | waggelde de veranda op zodra | porch = 'veranda' (15× here, Book 1 throughout) vs 'portiek' (Ch1 only) |
| 3 | 47 | 6 Term | de treden van het portiek afstapte | de treden van de veranda afstapte | porch = veranda |
| 4 | 53 | 6 Term | met een portiek dat zich om twee kanten | met een veranda die zich om twee kanten | porch = veranda (a wraparound porch) |
| 5 | 65 | 6 Tense | een lach die ergens diep ontspringt en in één keer losbarst | een lach die ergens diep ontsprong en in één keer losbarstte | present tense in past narration (EN 'started … arrived') |
| 6 | 83 | 5 Register | ‘Ik vind het alleen maar fijn als jullie blijven.’ | ‘Ik vind het alleen maar fijn als u blijft.’ | innkeeper to guests the Worthingtons: mixed jullie/je in one speech; guests = u |
| 7 | 83 | 5 Register | ‘De suite is van jullie zolang jullie willen. En de quilts zijn lokaal, ik zal de naam voor je opschrijven, | ‘De suite is van u zolang u wilt. En de quilts zijn lokaal, ik zal de naam voor u opschrijven, | same speech, guests = u |
| 8 | 93 | 6 Term | de portiekbeugels rinkelden | de verandabeugels rinkelden | porch = veranda |
| 9 | 95 | 6 Term | ‘De portiekbeugels. | ‘De verandabeugels. | porch = veranda |
| 10 | 135 | 6 Term | door de voordeur en het portiek op | door de voordeur en de veranda op | porch = veranda |
| 11 | 137 | 6 Term | bij de balustrade van het portiek staan | bij de balustrade van de veranda staan | porch = veranda |
| 12 | 170 | 6 Term | toen we naar het dorpsplein draaiden, | toen we richting de brink afsloegen, | EN 'rounded toward the green'; the green = 'de brink' ('dorpsplein' = the square) |
| 13 | 172 | 3 Mistranslation | Fiona dook op uit een zijkamer | Fiona dook op uit een zijdeur | EN 'appeared from a side door' |
| 14 | 209 | 5 Idiom | Wat de andere overliet. | Dan bleef de andere over. | calque of 'Which left the other'; not idiomatic Dutch |
| 15 | 211 | 6 Term | Ze tsjilpte en | Ze tjirpte en | Pip's chirp is 'tjirpen' everywhere else |
| 16 | 268 | 3 Mistranslation | een vastberaden goud. | een standvastig goud. | EN 'a steady gold'; 'vastberaden' = determined (of a person) |
| 17 | 297 | 1 Untranslated sign (ruling 3) | FROST FALLS THROUGH THE YEARS | FROST FALLS DOOR DE JAREN | banner text left in English; translated, italic kept |
| 18 | 297 | 1 Sign adaptation (ruling 3) | waarbij de laatste S erg krap | waarbij de laatste N erg krap | the crowded last letter of the translated banner is N |
| 19 | 297 | Ruling 6 cider | een tafel neergezet met cider en gemberkoekjes | een tafel neergezet met warme appelsap en gemberkoekjes | Dutch 'cider' is alcoholic; the drink is non-alcoholic |
| 20 | 301 | Ruling 6 cider | Hij zou de cider nog van een label | Hij zou de appelsap nog van een label | non-alcoholic |
| 21 | 327 | 6 Term / 5 Register | Die meneer Hussein van u heeft de stad een echte dienst bewezen, of de stad dat nu weet of niet. Moet je hier eens kijken. | Die meneer Hussein van u heeft het stadje een echte dienst bewezen, of het stadje dat nu weet of niet. Kijkt u hier eens. | 'stad' = city (Frost Falls is a small town, 'stadje'); Neil addresses Jessica as u |
| 22 | 331 | Ruling 6 cider | bij de cidertafel naar me toe | bij de appelsaptafel naar me toe | non-alcoholic |
| 23 | 331 | 3 Mistranslation | Dat deel haalt de familiepapiertjes blijkbaar niet. | Dat deel haalt de familiepapieren blijkbaar niet. | EN 'the family papers'; diminutive belittles the archive |
| 24 | 335 | 6 Term | Hij bedankte de stad. | Hij bedankte het stadje. | 'stad' = city |
| 25 | 345 | 6 Term / key distinction | zat een afpersbrief waarin precies stond | zat een afpersingsbriefje waarin precies stond | the blackmail NOTE must not share the word for the 1924 LETTERS ('brieven') in the same sentence |
| 26 | 353 | Ruling 6 cider | liep door naar de cider alsof | liep door naar de appelsap alsof | non-alcoholic |
| 27 | 357 | 6 Term / key distinction | exact datzelfde rood dat de brief Fiona had opgedragen | exact datzelfde rood dat het briefje Fiona had opgedragen | the blackmail note = 'briefje'; 'brief' reads as the Blackburn letters |
| 28 | 361 | 6 Term / key distinction | naast de brief. Ik richtte | naast het briefje. Ik richtte | the blackmail note = 'briefje' |
| 29 | 361 | Ruling 6 cider | gehurkt bij de cidertafel zat | gehurkt bij de appelsaptafel zat | non-alcoholic |
| 30 | 363 | 3 Mistranslation | Het papier was hier geweest. | Het papier was hier. | EN 'The paper was here' (still there, contrasted with the letters that HAD been) |
| 31 | 372 | 3 Mistranslation | ‘Zeker nu het festival naar dit weekend is vervroegd.’ | ‘Zeker nu het festival naar volgend weekend is vervroegd.’ | EN 'moved up to next weekend' |
| 32 | 401 | 6 Term | stonden de mannen weer op het grasveld de laatste | stonden de mannen weer op de brink de laatste | the green = 'de brink' |
| 33 | 409 | 6 Term | het eerste dozijn wanten van de breiclub bij de feestcommissie af | het eerste dozijn wanten van de kring bij de festivalcommissie af | the circle = 'de kring' (Book 1 and this book); festival term |
| 34 | 409 | 6 Term | de plek waar het feest zou plaatsvinden | de plek waar het festival zou plaatsvinden | the festival = 'festival' throughout; 'feest' variant |
| 35 | 409 | 6 Term | Het grasveld was de plek waar het festival zou plaatsvinden, de grote gemeenschappelijke weide ten zuiden | De brink was de plek waar het festival zou plaatsvinden, het grote gemeenschappelijke grasveld ten zuiden | the green = 'de brink'; 'weide' is reserved for the paddock |
| 36 | 421 | 4 Proper name | Sneeuwbal zat aan | Snowball zat aan | the dog keeps its English name (Book 1 majority, series rule) |
| 37 | 429 | 6 Term | of de pinguïn ook naar het feest komt,’ zei hij. ‘Ik denk dat wat Emma betreft Pip het hele feest is. | of de pinguïn ook naar het festival komt,’ zei hij. ‘Ik denk dat wat Emma betreft Pip het hele festival is. | festival term |
| 38 | 435 | 4 Proper name | dat Sneeuwbal bijna | dat Snowball bijna | dog's name |
| 39 | 439 | 4 Proper name | tussen Sneeuwbal en | tussen Snowball en | dog's name |
| 40 | 447 | 6 Term | Noriko Tanaka stond midden op het grasveld in | Noriko Tanaka stond midden op de brink in | the green = 'de brink' |
| 41 | 449 | 5 Register (ruling 2) | Dank je wel. En je rendieren | Dank u wel. En uw rendieren | Noriko and Jessica are formal at their first meeting (Ch6) |
| 42 | 459 | 1 Untranslated | naar de jack-o’-lantern die Pip | naar de pompoenlantaarn die Pip | English 'jack-o'-lantern' (rendered 'pompoenlantaarn' at 413) |
| 43 | 465 | 5 Register (ruling 2) | ‘Heb jij dat gedaan?’ | ‘Heeft u dat gedaan?’ | Emma addresses adults formally ('uw pinguïn' at 411) |
| 44 | 465 | 5 Register (ruling 2) | Heb jij kerst uit een pompoen | Heeft u kerst uit een pompoen | Emma → Jessica = u |
| 45 | 473 | 6 Term | aan de rand van het grasveld, en niet | aan de rand van de brink, en niet | the green = 'de brink' |
| 46 | 477 | 6 Term / key distinction | Er zat nog steeds een dreigbrief gevouwen | Er zat nog steeds een afpersingsbriefje gevouwen | the blackmail NOTE gets its own word (briefje), kept apart from the 1924 letters (brieven) |
| 47 | 481 | 6 Term | de rest van het feest niet uit elkaar sloopt | de rest van het festival niet uit elkaar sloopt | festival term |
| 48 | 497 | 6 Term | Na honderd jaar en een op slot gedraaide koffer en een afpersingsbrief is het nog steeds het warmste huis in de stad. | Na honderd jaar en een op slot gedraaide koffer en een afpersingsbriefje is het nog steeds het warmste huis in het stadje. | note = 'briefje' (kept apart from the 1924 'brieven'); 'stad' = city |
| 49 | 508 | 6 Term / key distinction | Ik had de afpersingsbrief sinds Fiona hem mij had overhandigd | Ik had het afpersingsbriefje sinds Fiona het mij had overhandigd | the note = 'briefje', never 'brief' |
| 50 | 516 | 5 Register (ruling 2) | Het halve stadje hangt vol met je werk dit seizoen. | Het halve stadje hangt vol met uw werk dit seizoen. | Jessica ↔ Sam formal (acquaintance; Sam says u) |
| 51 | 520 | 6 Term / key distinction | Hij zat op de brief, en hij was hier. | Hij zat op het briefje, en hij was hier. | the note |
| 52 | 522 | 5 Register (ruling 2) | ‘Je hebt de herberg gedaan,’ | ‘U heeft de herberg gedaan,’ | Jessica → Sam = u |
| 53 | 532 | 6 Term / key distinction | en de geur zat op de brief. | en de geur zat op het briefje. | the note |
| 54 | 540 | 5 Register (ruling 2) | Weet jij iets over de beginjaren | Weet u iets over de beginjaren | Jessica → Sam = u |
| 55 | 548 | 6 Term | De consolebeugels voor de veranda. | De verandabeugels. | EN 'The porch brackets'; one term for them (verandabeugels, as in Book 1) |
| 56 | 548 | 5 Idiom | ‘Best prima. | ‘Prima zo. | 'Best prima' is not idiomatic for 'Suits me' |
| 57 | 552 | 6 Term / key distinction | De brief rook naar de smederij. Maar rook hij naar de smederij omdat Sam Patel er met een pen over gebogen had, of omdat hij ergens was geweest | Het briefje rook naar de smederij. Maar rook het naar de smederij omdat Sam Patel er met een pen over gebogen had, of omdat het ergens was geweest | the note |
| 58 | 554 | 5 Register (ruling 2) | ‘Dank je wel, Sam,’ | ‘Dank u wel, Sam,’ | Jessica → Sam = u |
| 59 | 560 | 6 Term / key distinction | de geur op de brief aangaf waar hij was geweest | de geur op het briefje aangaf waar het was geweest | the note |
| 60 | 569 | 6 Term | voor de kerk aan het pleintje. | voor de kerk aan de brink. | EN 'the church on the green'; the green = 'de brink' (dominant form); 'pleintje' = the square |
| 61 | 591 | 6 Term | in het lichtste vertrek van de stad, | in het lichtste vertrek van het stadje, | 'stad' = city |
| 62 | 616 | 5 Register (ruling 2) | en vertel u mij eens, mevrouw Claus, | en vertel jij mij eens, mevrouw Claus, | Bram ↔ Jessica informal both ways |
| 63 | 616 | 5 Register (ruling 2) | Dan zal ik u precies hetzelfde vertellen | Dan zal ik jou precies hetzelfde vertellen | Bram → Jessica = jij |
| 64 | 634 | 3 Mistranslation | ‘Hij trekt aan ze. De rendieren voelen het nog voor wij het in de gaten hebben. Dat is altijd al zo geweest, sinds de eerste keer.’ | ‘Het trekt aan ze. De rendieren voelen het nog voor wij het in de gaten hebben. Dat is altijd al zo geweest, sinds het eerste rendier.’ | 'Hij' after 'De grendel' makes the LATCH the subject; EN 'It' = the magic; 'since the first one' = the first reindeer |
| 65 | 650 | 3 Mistranslation | telkens deed als we in de buurt kwamen | telkens deed als het briefje in de buurt was | EN 'whenever it [the note] was near' |
| 66 | 650 | 6 Term | gaf één helder, stellig tjilpje | gaf één helder, stellig tjirpje | Pip's chirp = 'tjirpen' throughout |
| 67 | 654 | 6 Term / key distinction | De brief ruikt naar de smidse, | Het briefje ruikt naar de smidse, | the note |
| 68 | 654 | 6 Term / key distinction | Waar die brief ook is geweest, | Waar dat briefje ook is geweest, | the note |
| 69 | 661 | 6 Term | aan het begin van de dorpsweide, | aan het begin van de brink, | the green = 'de brink' |
| 70 | 673 | 5 Register (ruling 2) | ‘Jij beheert de vastgoedregisters,’ | ‘U beheert de vastgoedregisters,’ | Jessica ↔ Vera formal (Vera says 'mevrouw Claus') |
| 71 | 673 | 5 Register (ruling 2) | naar je toekomt als ze willen weten | naar u toekomt als ze willen weten | Jessica → Vera = u |
| 72 | 674 | 5 Idiom | een kleine beweging, er meteen weer vandoor, | een kleine beweging, die er was en meteen weer verdween, | 'er meteen weer vandoor' (ran off) for 'there and gone' |
| 73 | 675 | 5 Register (ruling 2) | dat jij als geen ander zou weten | dat u als geen ander zou weten | Jessica → Vera = u |
| 74 | 680 | 5 Register (ruling 2) | ‘Dat is alles,’ zei ik. ‘Dank je wel, Vera. Je ziet er uitgeput uit, als je me dat vergeeft. Ze laten je hier ook veel te hard werken.’ | ‘Dat is alles,’ zei ik. ‘Dank u wel, Vera. U ziet er uitgeput uit, als u me dat vergeeft. Ze laten u hier ook veel te hard werken.’ | Jessica → Vera = u |
| 75 | 684 | 6 Tense | Een vrouw met geldzorgen die haar nek afknellen. | Een vrouw met geldzorgen die zwaar op haar drukten. | present tense in past narration ('pressing on her') |
| 76 | 685 | 3 Mistranslation | En nu waren er twee mensen in Frost Falls bij wie ik niet aan de naam Blackburn kon denken zonder dat het ergens aan schuurde. | En nu waren er twee mensen in Frost Falls aan wie ik moest denken zodra ik de naam Blackburn hoorde. | EN 'two people I couldn't hear the name Blackburn without thinking of'; Dutch said the reverse direction |
| 77 | 724 | 5 Register (ruling 2) | ‘Je zou nooit meer een hele baan voor jezelf hebben.’ | ‘U zou nooit meer een hele baan voor uzelf hebben.’ | Jessica ↔ Jamal formal (Jamal says u / mevrouw Claus) |
| 78 | 736 | 5 Register (ruling 2) | een zware last om in je eentje te dragen | een zware last om in uw eentje te dragen | Jessica → Jamal = u |
| 79 | 740 | 6 Term / key distinction | dat paste niet bij een afpersingsbrief voor | dat paste niet bij een afpersingsbriefje voor | the note |
| 80 | 744 | 5 Register (ruling 2) | ‘Je hebt Theo geholpen met de tentoonstelling,’ zei ik. ‘Al die oude papieren. Heb je daar nog iets van ingezien toen je daar binnen was? | ‘U heeft Theo geholpen met de tentoonstelling,’ zei ik. ‘Al die oude papieren. Heeft u daar nog iets van ingezien toen u daar binnen was? | Jessica → Jamal = u |
| 81 | 750 | 5 Register (ruling 2) | ‘Nou,’ zei ik, ‘je bent een goede vriend voor Theo, door al je spierkracht uit te lenen terwijl je zelf je zorgen had. | ‘Nou,’ zei ik, ‘u bent een goede vriend voor Theo, door al uw spierkracht uit te lenen terwijl u zelf uw zorgen had. | Jessica → Jamal = u |
| 82 | 752 | 3 Reversed meaning | Maar hij heeft zich de hele tijd doodgerust om die plek. | Maar hij heeft zich de hele tijd doodongerust gemaakt om die plek. | EN 'Worried sick'; 'doodgerust' = perfectly calm |
| 83 | 754 | 5 Register (ruling 2) | ‘Jij bent de juiste man | ‘U bent de juiste man | Jessica → Jamal = u |
| 84 | 763 | 3 Mistranslation | met de laatste restjes daarvan op de hielen gezeten door Bram, die zijn wanhoop aan me uitstortte. | het laatste stuk met Bram op mijn hielen, die zijn wanhoop aan me uitstortte. | EN 'the last of it [the morning] with Bram at my heels'; Dutch said the last remnants of the evidence were chased by Bram |
| 85 | 767 | Ruling 5 stray <bt> | op de toonbank van <bt>The Holly Jolly Bakery</bt>, | op de toonbank van de Holly Jolly Bakery, | not a book title; markers removed, matched to the edition's own form ('de Holly Jolly Bakery') |
| 86 | 767 | 6 Term | met het groen en het stadhuis en al. | met de brink en het stadhuis en al. | 'het groen' for the green; book term 'de brink' |
| 87 | 771 | 5 Register (ruling 2) | ‘Trek je niets aan van die bol. | ‘Trekt u zich niets aan van die bol. | Greta (shopkeeper) addresses 'mevrouw Claus' → u |
| 88 | 783 | 3 Mistranslation | Er had zich inderdaad een flinke, opgetogen menigte verzameld. | Er had zich inderdaad een kleine, opgetogen menigte verzameld. | EN 'A small crowd' |
| 89 | 808 | 3 Mistranslation / 6 Term | die ze bewaarde voor noodgevallen en rommelmarkten. | die ze bewaarde voor noodgevallen en koekjesverkopen. | EN 'bake sales' ('koekjesverkopen' in Ch12 and Ch28); 'rommelmarkt' = jumble sale |
| 90 | 904 | 5 Register (ruling 2) | ‘Sam, ik ben je iets schuldig.’ | ‘Sam, ik ben u iets schuldig.’ | Jessica → Sam = u |
| 91 | 914 | 5 Register (ruling 2) | ‘Dat wist je ook niet,’ zei ik. ‘Hoe had je dat kunnen weten? Dat is precies de reden waarom ik het je nu wel vertel.’ | ‘Dat wist u ook niet,’ zei ik. ‘Hoe had u dat kunnen weten? Dat is precies de reden waarom ik het u nu wel vertel.’ | Jessica → Sam = u |
| 92 | 916 | 6 Term | zoals de hele stad het zei zodra | zoals het hele stadje het zei zodra | 'stad' = city |
| 93 | 922 | 5 Register (ruling 2) | Jij hebt scherpe ogen en je staat hier sowieso op die ladder. | U heeft scherpe ogen en u staat hier sowieso op die ladder. | Jessica → Sam = u |
| 94 | 924 | 5 Register | Zeg haar dat ook, als je haar over die twintig dollar vertelt. | Zeg haar dat ook, als u haar over die twintig dollar vertelt. | Sam addresses Jessica as u in this same speech |
| 95 | 943 | 6 Term | haar angst was voor de blikken van de stad. | haar angst was voor de blikken van het stadje. | 'stad' = city |
| 96 | 945 | 6 Term | in jullie mooie stad de slechtste helft | in jullie mooie stadje de slechtste helft | 'stad' = city |
| 97 | 972 | 6 Typo | Ik hoefde het briefje niet te tevoorschijn te halen | Ik hoefde het briefje niet tevoorschijn te halen | doubled 'te' |
| 98 | 978 | 1 Untranslated (ruling 3) | B, B, Bridgetournament, Bunting, Surplus | B, B, Bridgetoernooi, Banieren, overtollige | index-card names left half in English; translated keeping the B-run and the inverted archival card ('Bunting, Surplus' → 'Banieren, overtollige') |
| 99 | 978 | 6 Term | zonder de verhalen van hun stad te kennen | zonder de verhalen van hun stadje te kennen | 'stad' = city |
| 100 | 1000 | 3 Mistranslation / 6 Term | stroomde het naar binnen vanuit de wei achter het erf, vanuit de werkplaats, | stroomde het naar binnen van voorbij de weide, vanuit de werkplaats, | EN 'from out past the paddock'; the paddock = 'de weide' |
| 101 | 1023 | 6 Term | naar buiten op het dorpsplein gedragen | naar buiten op de brink gedragen | the green = 'de brink' |
| 102 | 1037 | 6 Term | anders leest de hele stad maandagochtend | anders leest het hele stadje maandagochtend | 'stad' = city (inside the note; italic kept) |
| 103 | 1057 | 6 Term | De fijne, evenwijdige waterlijntjes | De fijne, evenwijdige scheplijntjes | laid lines = 'scheplijnen' (Ch4, Ch26); 'waterlijn' is a different watermark feature |
| 104 | 1072 | 6 Term | Het feest begon om twaalf uur. | Het festival begon om twaalf uur. | festival term |
| 105 | 1073 | 6 Term | De dorpsweide was sinds de ochtend | De brink was sinds de ochtend | the green = 'de brink' |
| 106 | 1073 | 6 Term | een hele tafel vol wanten van het handwerkkringetje, | een hele tafel vol wanten van de kring, | the circle = 'de kring' |
| 107 | 1073 | 6 Term / ruling 6 | Langs de hele dorpsweide stonden kraampjes met cider en geroosterde kastanjes, | Langs de hele brink stonden kraampjes met warme appelsap en geroosterde kastanjes, | the green = 'de brink'; cider non-alcoholic |
| 108 | 1076 | 6 Term | een dorpsbewoonster op het feest van haar dorp, | een dorpsbewoonster op het festival van haar dorp, | festival term |
| 109 | 1076 | Ruling 6 cider | Emma Redfern vond me bij de cider en | Emma Redfern vond me bij de appelsap en | non-alcoholic |
| 110 | 1076 | Ruling 6 cider | met twee bekers cider en | met twee bekers appelsap en | non-alcoholic |
| 111 | 1076 | 6 Term | vanaf de overkant van de weide, | vanaf de overkant van de brink, | the green = 'de brink' ('weide' is the paddock) |
| 112 | 1077 | 6 Term | dat het feest zondag eindigt, | dat het festival zondag eindigt, | festival term (the note says 'Het festival eindigt zondag') |
| 113 | 1078 | 6 Term | Ik liep veel te snel over de weide, | Ik liep veel te snel over de brink, | the green = 'de brink' |
| 114 | 1079 | Ruling 6 cider | bij de ciderkraam, | bij de appelsapkraam, | non-alcoholic |
| 115 | 1079 | 6 Term | toen ik weer over de weide terugkwam, | toen ik weer over de brink terugkwam, | the green |
| 116 | 1080 | 5 Register (ruling 2) | ‘Je deed net alsof je mevrouw Pelletier wilde tackelen,’ | ‘U deed net alsof u mevrouw Pelletier wilde tackelen,’ | Noriko ↔ Jessica formal until first names (Ch24–26); she says 'mevrouw Claus' in this scene |
| 117 | 1082 | Ruling 6 cider | Ze nam een slok van haar cider. | Ze nam een slok van haar appelsap. | non-alcoholic |
| 118 | 1085 | 5 Register (ruling 2) | ‘Je weet waar het bureau is. | ‘U weet waar het bureau is. | Noriko → Jessica = u |
| 119 | 1085 | 5 Register (ruling 2) | ‘Je pinguïn heeft | ‘Uw pinguïn heeft | Noriko → Jessica = u |
| 120 | 1087 | 4 Proper name / 6 Term | de week dat we Sneeuwbal vonden. Dikke, trage vlokken daalden neer over de weide, | de week dat we Snowball vonden. Dikke, trage vlokken daalden neer over de brink, | dog keeps English name; the green = 'de brink' |
| 121 | 1093 | 6 Term | Het feest had nog twee dagen te gaan, | Het festival had nog twee dagen te gaan, | festival term |
| 122 | 1100 | 6 Term / key distinction | die precies zo in de afpersingsbrief stonden | die precies zo in het afpersingsbriefje stonden | the note = 'briefje'; 'brief' is reserved for the 1924 letters in this same deduction |
| 123 | 1106 | Ruling 5 stray <bt> | De aardigste man van <bt>Frost Falls</bt>. | De aardigste man van Frost Falls. | the town name is not a book title; markers removed |
| 124 | 1106 | 4 Gender | en dat tegen een vriend gebruikt. | en dat tegen een vriendin gebruikt. | the friend is Fiona |
| 125 | 1116 | 6 Term | lag op het gemeentehuis, | lag in het stadhuis, | Town Hall = 'het stadhuis' (Ch11, Ch20) |
| 126 | 1122 | Ruling 5 stray <bt> | de akte van de <bt>Winter Wonderland Inn</bt> ergens | de akte van de Winter Wonderland Inn ergens | the inn's name is not a book title; markers removed |
| 127 | 1129 | 6 Term | Het gemeentehuis was de week | Het stadhuis was de week | Town Hall = 'het stadhuis' |
| 128 | 1131 | 3 Mistranslation | waar een marktkraam zijn wagen mocht neerzetten | waar een marktkoopman zijn kar mocht neerzetten | EN 'a vendor … his cart'; a stall cannot park its own cart |
| 129 | 1143 | 5 Register (ruling 2) | Echt waar. Je ziet er slecht uit.’ | Echt waar. U ziet er slecht uit.’ | Jessica → Vera = u |
| 130 | 1190 | 6 Term | een aangeschoven stoel bij de breiclub. | een aangeschoven stoel bij de kring. | the knitting circle = 'de kring' (the next paragraph: 'Dat is het hele nut van een kring') |
| 131 | 1205 | 6 Term / 3 Mistranslation | Hoofdinspecteur Tanaka hoorde me aan in haar kleine kantoor op het bureau, met | Politiechef Tanaka hoorde me aan in haar kleine kantoor op het politiebureau, met | Chief = 'politiechef' (Ch6); 'op het bureau … op het bureau' confused the station with the desk |
| 132 | 1219 | 3 Mistranslation | geen lokbriefje dat in het donker | geen lokenvelop die in het donker | EN 'decoy envelope'; keeps 'briefje' for the real notes |
| 133 | 1221 | 6 Term | en de hoofdinspecteur van politie aan onze zijde | en de politiechef aan onze zijde | Chief of police = 'politiechef' |
| 134 | 1246 | 6 Term | schraagtafels die op de weide werden ingeklapt | schraagtafels die op de brink werden ingeklapt | the green = 'de brink' ('weide' is the paddock) |
| 135 | 1252 | 5 Register (ruling 2) | ‘Ga alsjeblieft zitten, allebei,’ | ‘Gaat u alstublieft zitten, allebei,’ | professional scene: Noriko → Theo and Vera = u |
| 136 | 1252 | 5 Register (ruling 2) | en daarna krijgen jullie beiden een keuze te maken. Ga zitten.’ | en daarna krijgt u beiden een keuze te maken. Gaat u zitten.’ | Noriko → Theo and Vera = u |
| 137 | 1258 | 3 KEY distinction (note vs letters) | ‘De afpersingsbrieven aan Fiona zijn geschreven | ‘De afpersingsbriefjes aan Fiona zijn geschreven | the notes were called 'brieven' in the same speech as the Blackburn 'brieven' — blurs the deduction; notes = 'briefjes' |
| 138 | 1258 | 1 Untranslated KEY CLUE / ruling 5 | als <bt>the sapphire at its heart</bt>. | als de saffier in haar hart. | clue left in English inside a stray <bt>; now identical to the note, the card and the recap |
| 139 | 1258 | 6 Term | waarvan je de hele stad bij de opening vertelde | waarvan je het hele stadje bij de opening vertelde | 'stad' = city |
| 140 | 1262 | 6 Term | Honderd jaar aan herinneringen van deze stad, | Honderd jaar aan herinneringen van dit stadje, | 'stad' = city |
| 141 | 1262 | 6 Term | Ik hou zoveel van de geschiedenis van deze stad dat ik ben vergeten dat de stad uit levende mensen bestaat. | Ik hou zoveel van de geschiedenis van dit stadje dat ik ben vergeten dat het stadje uit levende mensen bestaat. | 'stad' = city |
| 142 | 1268 | 5 Register (ruling 2) | in je opbergmand, | in uw opbergmand, | Jessica ↔ Vera formal |
| 143 | 1268 | 5 Register / 6 Term / 3 Clarity | ‘Hij had de helft over de diefstal. Jij had de akte. En jij had de benen, Vera. Hij had deze stad niet onopgemerkt kunnen doorkruisen | ‘Hij had het geheim van de diefstal. U had de akte. En u had de benen, Vera. Hij had dit stadje niet onopgemerkt kunnen doorkruisen | Jessica → Vera = u; 'stad' = city; 'de helft over de diefstal' unclear — matches the Ch23 recap 'het geheim van de diefstal' |
| 144 | 1268 | 5 Register (ruling 2) | Ik kwam je die ochtend zelf op de trappen tegen, met je parkeerkaarten. | Ik kwam u die ochtend zelf op de trappen tegen, met uw parkeerkaarten. | Jessica → Vera = u |
| 145 | 1268 | 5 Register / 6 Term | zich onopgemerkt door de stad kon bewegen. Dat was jij.’ | zich onopgemerkt door het stadje kon bewegen. Dat was u.’ | Jessica → Vera = u; 'stad' = city |
| 146 | 1272 | 5 Register | schulden waarvan je het bestaan niet zou geloven | schulden waarvan u het bestaan niet zou geloven | Vera is addressing 'mevrouw Claus' in this sentence |
| 147 | 1278 | 5 Register (ruling 2) | ‘Jullie hebben het allebei toegegeven, uit vrije wil, en dat weegt zwaarder dan jullie je nu nog kunnen beseffen. | ‘U hebt het allebei toegegeven, uit vrije wil, en dat weegt zwaarder dan u nu nog kunt beseffen. | professional scene: Noriko → Theo and Vera = u |
| 148 | 1291 | 6 Term | het neerleggen van haar functie op het gemeentehuis. | het neerleggen van haar functie op het stadhuis. | Town Hall = 'het stadhuis' |
| 149 | 1305 | 6 Term | de laatste spullen van haar bureau in het gemeentehuis inpakte, | de laatste spullen van haar bureau in het stadhuis inpakte, | Town Hall = 'het stadhuis' |
| 150 | 1307 | 5 Register (ruling 2) | ‘Je hebt iets verkeerds gedaan,’ zei ik. ‘En je boet daar nu voor, op de juiste manier, en dat is terecht. Maar je hebt het direct bekend zodra ernaar werd gevraagd, Vera. Je hebt niet gelogen en je hebt je er niet onderuit gewurmd. Dat is niet niks. Dat is het stuk in jou dat nog steeds goed is, en dat is groter dan het stuk dat de fout beging, en ik wil dat je dat vasthoudt. De weg terug is lang voor je. Maar hij is er wel. Laat niemand je wijsmaken dat het niet zo is, en praat het vooral jezelf ook niet aan.’ | ‘U hebt iets verkeerds gedaan,’ zei ik. ‘En u boet daar nu voor, op de juiste manier, en dat is terecht. Maar u hebt het direct bekend zodra ernaar werd gevraagd, Vera. U hebt niet gelogen en u hebt zich er niet onderuit gewurmd. Dat is niet niks. Dat is het stuk in u dat nog steeds goed is, en dat is groter dan het stuk dat de fout beging, en ik wil dat u dat vasthoudt. De weg terug is lang voor u. Maar hij is er wel. Laat niemand u wijsmaken dat het niet zo is, en praat het vooral uzelf ook niet aan.’ | Jessica ↔ Vera formal throughout (no first-name/intimacy switch in the English) |
| 151 | 1313 | 5 Idiom | Hij was er nu verdwenen. | Hij was er nu niet meer bij. | 'er verdwenen' is not idiomatic for 'He was gone from it' |
| 152 | 1318 | 6 Term | voordat ze uit de stad vertrokken, | voordat ze uit het stadje vertrokken, | 'stad' = city |
| 153 | 1334 | 3 Mistranslation | Tegen de tijd dat ik ons steegje bereikte, | Tegen de tijd dat ik ons laantje bereikte, | EN 'our lane'; 'steegje' = alley |
| 154 | 1350 | 6 Term | in de breiclub, terwijl | in de kring, terwijl | the circle = 'de kring' |
| 155 | 1358 | 5 Idiom | Ik had meer dan ten dele verwacht | Ik had meer dan half verwacht | EN 'more than half expected'; 'ten dele' does not fit |
| 156 | 1362 | 6 Term | op een grauwe middag in de breiclub mijn hand, | op een grauwe middag in de kring mijn hand, | the circle = 'de kring' (Martha's line 'Dat een kring er is…' depends on it) |
| 157 | 1366 | 6 Term | Het feest was voorbij en opgeruimd, | Het festival was voorbij en opgeruimd, | festival term |
| 158 | 1375 | 4 Proper name | Sneeuwbal droeg zijn gewei-muts. | Snowball droeg zijn gewei-muts. | dog's name stays English |
| 159 | 1380 | 3 Reversed meaning | Mensen morden instemmend, | Mensen mompelden instemmend, | EN 'murmured, low and agreeing'; 'morren' = to grumble |
| 160 | 1383 | 6 Term | ‘Het klinkje, mevrouw Claus!’ | ‘De grendel, mevrouw Claus!’ | the paddock latch = 'grendel' (Ch10) |
| 161 | 1390 | 6 Term | het dorpsplein was aangeveegd | de brink was aangeveegd | the green = 'de brink' |
| 162 | 1400 | 4 Gender / clarity | Ik keek hoe Emma met Snowball haar riem slingerde | Ik keek hoe Emma met de riem van Snowball slingerde | 'Snowball haar riem' gives the male dog a female possessive |
| 163 | 1406 | 4 Gender / clarity | duwde Emma Snowball haar riem in mijn hand. | duwde Emma de riem van Snowball in mijn hand. | same |
| 164 | 1452 | 6 Tense | Greta bakte al veertig jaar lang dezelfde kaneelrol. Ze had hem gebakken op de ochtend | Greta bakt al veertig jaar lang dezelfde kaneelrol. Ze bakte hem op de ochtend | sell copy is in the present (the next sentences: 'Deze week komt hij…') |
| 165 | 1460 | 3 Mistranslation / 1 Untranslated | heeft een nieuwe patissier zijn grand opening gepland | heeft een nieuwe patisserie haar feestelijke opening gepland | EN 'a new patisserie' (a shop, not a pastry chef); English 'grand opening' left in |
| 166 | 1468 | Ruling 5 stray <bt> | de voorkamer van <bt>Yarn Tales</bt> zoals | de voorkamer van Yarn Tales zoals | shop name, not a book title; markers removed (the edition keeps 'Yarn Tales' elsewhere) |
| 167 | 1470 | 1 Untranslated | hun skeletten en jack-o’-lanterns ingeruild | hun skeletten en pompoenlantaarns ingeruild | English 'jack-o'-lanterns' ('pompoenlantaarn' in Ch6) |
| 168 | 1486 | 3 Mistranslation | standvastige tederheid legde ze in een ijzeren frame. | standvastige tederheid legde ze in een draadframe. | EN 'a wire frame'; 'ijzeren' = iron |
| 169 | 1540 | Ruling 5 stray <bt> / 6 Term | Het grasveld lag tegenover <bt>Yarn Tales</bt>, een brede witte strook met de muziektent aan de ene kant en het Oorlogsmonument | De brink lag tegenover Yarn Tales, een brede witte strook met de muziektent aan de ene kant en het oorlogsmonument | shop name not a title (markers removed); the green = 'de brink'; 'oorlogsmonument' lower-case as in Ch6 |
| 170 | 1544 | 6 Term | wees weg over het grasveld richting de winkels | wees weg over de brink richting de winkels | the green = 'de brink' |
| 171 | 1562 | 6 Term | De sneeuw lag stralend wit op het veld met | De sneeuw lag stralend wit op de brink met | EN 'on the green' |
