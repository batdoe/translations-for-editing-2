# APPLIED — Inn Trouble - ASSEMBLED - FORMATTED_Dutch

## Verify (`python3 _tools/preflight.py --verify`)

- PASS paragraphs: 1567 = 1567
- PASS scene breaks: 4 = 4
- PASS bt spans: 10 = 10
- Italic runs: count 23 = 23, order unchanged. The tool reports FAIL because the text inside 7 italic runs changed. Every one of these changes is an intended, logged fix:
  - 177: the first blackmail note — 'die met de sapphire at its heart' → 'die met de saffier in haar hart' (key clue)
  - 178: italic run 'The sapphire at its heart' → 'De saffier in haar hart' (key clue; the translator-added italic is left for NL-D5)
  - 968: Theo's catalog card — 'door een huisknecht' → 'door een huisbediende'
  - 1037: the second note — 'Rode strik op de krans' → 'Rood lint op de krans'
  - 1100: italic run 'the sapphire at its heart' → 'De saffier in haar hart' (key clue)
  - 1112: italic run 'I know how your family came by this inn' → 'Ik weet hoe je familie aan deze herberg is gekomen' (quote of note 1; EN italic too)
  - 1135: deed-folder label 'PROPERTY — …' → 'VASTGOED — …'
- No other paragraph changed unintentionally. 226 paragraphs differ from the baseline, and each one is in the table below.

## Applied fixes (281 operations = 280 findings; para 624 was split into two operations around the italic 'nooit')

| Para | Was | Now | Why |
|---|---|---|---|
| 14 | met uitzondering van hetgeen is toegestaan krachtens de wet. | met uitzondering van hetgeen is toegestaan krachtens de Amerikaanse auteurswet. | EN 'as permitted by U.S. copyright law'; the jurisdiction was dropped |
| 24 | Wat is de volgende stap? | Wat komt er hierna? | EN 'What's Next?' = the next book; 'de volgende stap' = the next step (of a procedure) |
| 32 | er wordt de steen genoemd die the sapphire at its heart vormt | er wordt de steen genoemd die het hart van de broche vormt | EN 'names the stone at the brooch's heart'; English clue phrase left in text and giving the answer away |
| 32 | in een afgesloten kist op Fiona’s vliering | in een afgesloten koffer op Fiona’s vliering | the trunk = 'koffer' (12×) vs 'kist' (3×) |
| 34 | aan iedereen die er ener wil aannemen | aan iedereen die er een wil aannemen | typo 'ener' |
| 34 | over een zoekgeraakt broche | over een zoekgeraakte broche | 'broche' is de-word (de broche throughout) |
| 39 | haar moeder de suiker per ongeluk had laten karamelliseren | haar moeder de suiker met opzet had laten karamelliseren | EN 'burned the sugar on purpose'; 'per ongeluk' = by accident |
| 39 | in een warme keuken op een koud dag | in een warme keuken op een koude dag | adjective agreement 'koude dag' |
| 79 | kleine exemplaren die het vuurlicht ving | kleine exemplaren die het vuurlicht vingen | plural agreement |
| 87 | de staf gul aandroeg | het personeel een gulle fooi gaf | EN 'tipped the staff generously'; 'aandroeg' is meaningless here |
| 111 | Altijd al gedaan. | Altijd al. | anglicism ('Always have'); not Dutch |
| 115 | ik vertrouwde hem ongeveer evenveel als ik het haardscherm had kunnen gooien | ik vertrouwde hem niet verder dan ik het haardscherm had kunnen gooien | EN 'trusted it about as far as I could have thrown the fire screen'; Dutch said she trusted him as much as |
| 117 | wat er kwam bovenwaterdrijven | wat er kwam bovendrijven | non-word 'bovenwaterdrijven' |
| 135 | mijn schandelijk pinguïn | mijn schandelijke pinguïn | adjective inflection |
| 137 | dat de misstanden in het gezicht van Fiona even leken op | dat wat er mis was aan het gezicht van Fiona even leek op | EN 'the wrongness in Fiona's face'; 'misstanden' = abuses/malpractices |
| 141 | werd zachter, verwarmde en werd goud | werd zachter, werd warmer en werd goud | 'verwarmde' (transitive 'heated') wrong; EN 'warmed' |
| 153 | een alerte, bange blik in haar blik | een alerte, bange blik in haar gezicht | 'blik in haar blik' doubled; EN 'a watching look in her face' |
| 160 | schril door de stille keuken schaterde | schril door de stille keuken rinkelde | 'schateren' = to roar with laughter; EN 'rang, shrill' |
| 169 | onze voetstappen weerklinken op het lege trottoir | onze voetstappen weerklonken op het lege trottoir | tense drift (past narration) |
| 170 | precies zoals ze er de dag ervoor hadden bijgelegen | precies zoals ze er de dag ervoor bij hadden gehangen | 'bijgelegen' is wrong (lain); EN 'exactly as they'd been the day before' (front, wreath hanging) |
| 171 | het vertrouwelijke gekraak ervan | het vertrouwde gekraak ervan | EN 'familiar creak'; 'vertrouwelijk' = confidential |
| 177 | om haar handschrift te verhullen | om zijn handschrift te verhullen | EN 'their hand' (gender-neutral); 'haar' wrongly signals a female blackmailer — generic Dutch is 'zijn' |
| 177 | Vijf honderdduizend dollar. | Vijfhonderdduizend dollar. | numeral written as one word |
| 177 | die met de sapphire at its heart, en | die met de saffier in haar hart, en | key clue left in English; dominant Dutch rendering is 'de saffier in haar hart' (968–972), which is five words as the text later says |
| 178 | The sapphire at its heart | De saffier in haar hart | key clue left in English; unified with 968–972 |
| 181 | met iets daags in zich | met iets in zich | stray non-word 'daags' |
| 185 | Ze stikte hem, Jessica. | Ze stal hem, Jessica. | EN 'She stole it'; 'stikte' = suffocated/stitched |
| 188 | probeerde het tot me doordringen | probeerde het tot me door te laten dringen | missing 'te'; ungrammatical |
| 190 | een kinderachtig gebaar | een kinderlijk gebaar | EN 'a child's gesture'; 'kinderachtig' = childish (pejorative) |
| 190 | Dus dat ik hem opdeed, sprak vanzelf. | Dus dat ik hem opendeed, sprak vanzelf. | 'opdeed' (acquired) for 'opendeed' (opened) |
| 190 | haar ogen roodrandigd | haar ogen roodomrand | non-word |
| 195 | De saffier in het hart, precies die woorden. | De saffier in haar hart, precies die woorden. | 'those very words' must match the note's wording; unified with 968–972 |
| 202 | Vijf honderdduizend dollar. | Vijfhonderdduizend dollar. | numeral written as one word |
| 218 | met één zwemvlies over haar ogen | met één vleugel over haar ogen | EN 'one flipper'; 'zwemvlies' is the webbed foot, not the flipper |
| 218 | En de kist op zolder met het slot erop | En de koffer op zolder met het slot erop | trunk term ('koffer') |
| 220 | Toen bleef ze doodstil liggen | Toen bleef ze doodstil staan | EN 'went very still' while stretched up at the table edge; she is not lying down |
| 224 | wie er een hekel heeft aan Fiona”, zei hij. | wie er een hekel heeft aan Fiona,” zei hij. | comma inside closing quote as everywhere else in the edition |
| 226 | Ze is stellig over die kist, | Ze is stellig over die koffer, | trunk term ('koffer') |
| 228 | De Historische Kring.” | Het Historisch Genootschap.” | the Historical Society = 'Historisch Genootschap' (42×); 'Kring' also = the knitting circle — ambiguous |
| 234 | omdat je zult inzien dat het waar is tijdens alles wat hierna komt, anders pak je het verkeerd aan | omdat je het voor waar zult moeten blijven houden tijdens alles wat hierna komt, anders pak je het verkeerd aan | EN 'you'll need to hold it true the whole way through'; Dutch said 'you will come to see it is true' |
| 242 | in het Kringgebouw | in het gebouw van het Genootschap | Historical Society term (see 228) |
| 252 | met een lantaarn op zak | met een lantaarn | 'op zak' = in his pocket; EN just 'with a lantern' |
| 252 | gezaagd vurenhout | gezaagd grenenhout | EN 'cut pine' = grenen; 'vuren' = spruce |
| 258 | hebben het duisternis nodig | hebben de duisternis nodig | 'duisternis' is a de-word |
| 290 | in het duisternis rond | in de duisternis rond | 'duisternis' is a de-word |
| 292 | door het duisternis joeg | door de duisternis joeg | 'duisternis' is a de-word |
| 297 | De Frost Falls Historical Society was | Het Historisch Genootschap van Frost Falls was | institution name left in English; book term is 'Historisch Genootschap' |
| 301 | vaagke kaarten | vage kaarten | typo |
| 305 | Zijn huid had een grauwe waas. | Zijn huid had een grauw waas. | 'het waas' (neuter) |
| 313 | Hij lachte ook, opgelucht, | Hij lachte ook, blij, | EN 'pleased'; 'opgelucht' = relieved |
| 339 | Ik moet één teleurstelling op mijn geweten bekijken. | Ik moet één teleurstelling opbiechten. | EN 'I'll confess one sorrow'; Dutch phrase was meaningless |
| 339 | zijn glimlach werd zelfspot | zijn glimlach werd zelfspottend | noun for adjective |
| 343 | Theo trok zijn schouders op, verheugd, | Theo boog zijn hoofd, verheugd, | EN 'ducked his head'; 'trok zijn schouders op' = shrugged |
| 361 | voor de laatste keer een kwartcentimeter rechtlegde | voor de laatste keer een halve centimeter rechtlegde | SAFE unit rule: literal 'a final quarter-inch' (≈6 mm); 'kwartcentimeter' is neither the right value nor idiomatic |
| 361 | En naar de stapel crème briefpapier naast Vera’s elkaars dat het licht ving. | En naar de stapel crèmekleurig briefpapier naast Vera’s elleboog, die het licht ving. | garbled: 'elkaars' for 'elleboog' (EN 'beside Vera's elbow'); uninflected 'crème' |
| 365 | een eeuwenoud geheim | een honderd jaar oud geheim | EN 'a hundred-year-old secret'; 'eeuwenoud' = centuries old |
| 373 | net als al sinds voordat jij geboren bent | zoals het al is sinds voordat jij geboren bent | ungrammatical |
| 387 | drongen koud en helder tot me doordringen | drongen koud en helder tot me door | doubled verb |
| 387 | voor zijn nacht dicht zien slaan | voor zijn neus dicht zien slaan | EN 'shut in his face'; idiom is 'voor zijn neus' |
| 389 | Wie de geheimen uit de stukken haalt, weet waar hij moet zoeken, had Nick gezegd. | Weten dat het geheim uit de papieren kwam, vertelt je waar je moet gaan staan, had Nick gezegd. | EN 'Knowing the secret came from the papers tells you where to stand'; Dutch said 'whoever takes secrets from the documents knows where to look' |
| 389 | ik hield mijn hand gesloten | ik hield mijn hand open | EN 'I kept my fist open' (open-minded); reversed, contradicts 404 |
| 393 | of sneeuw op de eerste oktober | of een eerste sneeuw in oktober | EN 'an October first snow' (first snowfall in October), not snow on 1 October |
| 395 | Martha was niet achterlijk. | Martha was niet gek. | EN 'no one's fool'; 'achterlijk' is crude/offensive |
| 399 | ik moest even schrapen | ik moest even mijn keel schrapen | EN 'had to clear my throat'; object missing |
| 400 | alsof ze me zojuist niet het een en ander te horen had gegeven | alsof ze me zojuist helemaal niets had gegeven | EN 'as though she hadn't just handed me anything at all'; 'te horen geven' = to tell off |
| 401 | terwijl ze elkaar in de kou toeroepen | terwijl ze elkaar in de kou toeriepen | tense drift |
| 407 | voor een getergde geest | voor een onrustige geest | EN 'troubled mind'; 'getergd' = provoked/teased |
| 409 | om de boel an te kleden | om de boel aan te kleden | typo |
| 409 | de eerste dos wanten | het eerste dozijn wanten | typo: 'dozijn' (EN 'first dozen') |
| 413 | van een lampion die iemand al vroeg had uitgehold | van een pompoenlantaarn die iemand al vroeg had uitgehold | EN 'jack-o'-lantern'; 'lampion' is a paper lantern |
| 415 | Het speet me ontzettend, Emma. | Het spijt me ontzettend, Emma. | dialogue apology in present ('I am so sorry') |
| 427 | zag ik waarop ik had gehoopt op zijn gezicht te zien: ontspanning | zag ik op zijn gezicht waarop ik had gehoopt: ontspanning | garbled word order |
| 433 | kalebassen transporteren en gezellig | kalebassen transporterend en gezellig | parallel participles |
| 447 | na twintig jaar bij de staatsrecherche | na twintig jaar bij de staatspolitie | EN 'state police'; 'recherche' = CID/detective branch only |
| 459 | „Mevrouw Claus. Kijken.” | „Mevrouw Claus. Kijk.” | EN 'Look.' — imperative, not infinitive |
| 471 | en ik kruiste mijn hart, | en ik legde mijn hand op mijn hart, | 'cross my heart' calqued; not a Dutch gesture/idiom |
| 483 | mijn schaamteloze, pompoenharige vogeltje op | mijn schaamteloze vogeltje met de pompoen op haar kin op | EN 'pumpkin-chinned'; 'pompoenharig' = pumpkin-haired |
| 492 | op een goedkope studeerkamerstoel | op een goedkope studiostoel | EN 'cheap studio chair' (photo studio); 'studeerkamer' = study |
| 493 | Ze moet een jaar of een etentje, tweeëntwintig zijn geweest. | Ze moet een jaar of eenentwintig, tweeëntwintig zijn geweest. | garbled 'een etentje' (a dinner) for 'eenentwintig' (EN 'twenty-one, twenty-two') |
| 493 | besloot dat ze er niet tegenover zou sterven | besloot dat ze er niet tegenaan zou sterven | EN 'die against it' (the wall at her back); 'tegenover' = opposite |
| 520 | aan een vel crème papier | aan een vel crèmekleurig papier | uninflected/odd 'crème papier' |
| 542 | van de Historische Kring. | van het Historisch Genootschap. | Historical Society term (see 228) |
| 544 | omdat het niet in zijn opkomt was dat | omdat het niet bij hem was opgekomen dat | garbled |
| 548 | Je kunt door Fiona’s voorkamer lopen zonder iets aan te raken | Je kunt niet door Fiona’s voorkamer lopen zonder iets aan te raken | EN 'You can't walk through Fiona's front room without touching something I made' — negation dropped; this is the clue that the lobby smells of the forge |
| 556 | „Moet je doen.” | „Doe dat.” | Sam addresses Jessica as 'u' (514, 536, 924); EN 'Do.' |
| 558 | het gerinkel van zijn hamer weer opam | het gerinkel van zijn hamer weer inzette | non-word 'opam'; EN 'starting up again' |
| 569 | Achttien éénentnegentig. | Achttien eenennegentig. | spelling of the numeral |
| 573 | toen al een klein vermogen waard en tegenwoordig een kapitaal | toen al heel wat waard en tegenwoordig een klein vermogen | EN 'worth a great deal even then and a small fortune now'; magnitudes shifted |
| 599 | met waar ze ook verantwoording voor afleggen | met aan wie ze ook verantwoording afleggen | garbled preposition (EN 'whatever they answer to') |
| 601 | tot no nut | tot geen nut | typo |
| 612 | wreef zijn muts fijn tussen zijn handen | wrong zijn muts tussen zijn handen | EN 'wringing his cap'; 'fijnwrijven' = grind to powder |
| 624 | Niet dat ik wil snoeren hoor. | Niet dat ik wil neuzen hoor. | EN 'pry'; 'snoeren' = to string/tie (split around the italic 'nooit') |
| 624 |  snoeren. Het is |  neuzen. Het is | EN 'I would never pry' (second half of the split fix) |
| 632 | vers gezaagd vurenhout | vers gezaagd grenenhout | EN 'cut pine' = grenen (as fixed at 252) |
| 636 | onze adem wolkten samen op | onze adem wolkte samen op | subject-verb agreement |
| 650 | de lantaarn in had gelegd | de kaarsenhouder in had gelegd | EN 'light holder' — the candle holder bought at the forge (ch8: 'kaarsenhouder') |
| 654 | Ik keek naar beneden naar mijn slimme dier. | Ik keek naar beneden naar mijn slimme vogel. | EN 'my clever bird' |
| 661 | Het stadhuis was een puntig bakstenen gebouw | Het stadhuis was een opgesmukt bakstenen gebouw | EN 'fussy' (over-ornate); 'puntig' = pointed |
| 662 | een loper van leer | een leren onderlegger | EN 'leather blotter' ('onderlegger' at 671); 'loper' = runner/carpet |
| 664 | De festivallenlijst? | De festivallijst? | non-word compound |
| 666 | ik probeerde iets standkasters en harders te vinden dat niet zomaar weggewuifd kon worden als treurnis | ik probeerde iets steviger te vinden, iets wat minder makkelijk weg te wuiven was dan treurnis | garbled non-word 'standkasters'; EN 'something steadier and harder to wave off than sad' |
| 668 | houdt de straatverlichting niet brandende | houdt de straatverlichting niet brandend | inflection |
| 668 | Misschien brengt jullie festival | Misschien brengt uw festival | the mayor addresses Jessica as 'u' in the same speech |
| 668 | strooit in februari geen zout op de wegen | ruimt in februari geen sneeuw van de wegen | EN 'doesn't plow the roads in February'; Theo quotes the line back at 703, the two renderings must match |
| 671 | Ze had de festivallenlijst gereed | Ze had de festivallijst gereed | non-word compound |
| 677 | Ze schoof de festivallenlijst over | Ze schoof de festivallijst over | non-word compound |
| 677 | Ik beheer alleen de administratie. Ik lees ze niet eens. | Ik beheer alleen de registers. Ik lees ze niet eens. | EN 'I only keep the records. I don't read them.'; 'ze' had no plural antecedent; registers is the book's term (678, 684) |
| 679 | Door te dringen zou ik | Door aan te dringen zou ik | 'aandringen' (push) split wrongly |
| 681 | Niemand zijn rekeningen betalen zichzelf | Niemands rekeningen betalen zichzelf | ungrammatical possessive |
| 683 | met de nutteloze burgemeester | met de nietsdoende burgemeester | EN 'idle mayor'; 'nutteloos' = useless |
| 685 | Het kon niet meer betekenen dan een vermoeide vrouw | Misschien betekende het niet meer dan een vermoeide vrouw | EN 'It might mean nothing more than'; Dutch said 'it could not mean more than' |
| 689 | Het bestuur van de Historische Kring | Het bestuur van het Historisch Genootschap | Historical Society term (see 228) |
| 693 | pruttelde op een s-tafel | pruttelde op een bijzettafel | garbled 's-tafel' (EN 'side table') |
| 699 | die een van de oude mannen deed grimassen | die een van de oude mannen deed ineenkrimpen | 'grimassen' is not a verb; EN 'made one of the old men wince' |
| 699 | „ongeveer de kosten van de koffie” dekken. | „ongeveer de kosten van de koffie” dekten. | tense drift |
| 703 | De geschiedenis ploegt de wegen niet. | De geschiedenis ruimt geen sneeuw. | quote of the mayor's line (668); 'ploegt de wegen' is not Dutch |
| 705 | hoe de Kring waaraan hij | hoe het Genootschap waaraan hij | Historical Society term; 'de Kring' reads as the knitting circle |
| 707 | voor de Kring deed | voor het Genootschap deed | Historical Society term (see 705) |
| 717 | Dat de Kring werkelijk ten onder ging | Dat het Genootschap werkelijk ten onder ging | Historical Society term (see 705) |
| 728 | waar het hele dorp van wiste | waar het hele dorp van wist | typo |
| 740 | bij het festival van het dorp voor een fooi | bij het festival van het dorp tegen betaling | EN 'for a fee'; 'fooi' = tip |
| 740 | uit een geheim had kunnen welslepen | uit een geheim had kunnen slaan | non-word 'welslepen'; idiom 'geld slaan uit' |
| 746 | „Voorzichtig nou, voorzichtig, die is kostbaar”, | ‘Voorzichtig nou, voorzichtig, die is kostbaar’, | nested quotation marked with outer-level „ ” closes Jamal's speech prematurely |
| 752 | Ik zou het hem zelf lenen als ik wat had | Ik zou het hem zelf geven als ik wat had | EN 'I'd give him the money myself' |
| 777 | had zich ’s nachts losgemaakt in de paddock | had zich ’s nachts uit de weide bevrijd | EN 'let herself out of the paddock'; the paddock is 'de weide' throughout (264, 618, 636) |
| 783 | ze klommen gillen op de rand | ze klommen gillend op de rand | typo |
| 791 | het huisje en het atelier daarachter | het huisje en de werkplaats daarachter | Nick's workshop = 'werkplaats' throughout |
| 791 | en oogstde luid gejuich | en oogstte luid gejuich | spelling |
| 793 | „Ze koestert zich op het atelier af,” zei Bram terwijl hij bladeren van zijn knieën veegde. „Ze willen allemaal naar het atelier nu. Waarom willen ze toch allemaal naar het atelier, | „Ze gaat op de werkplaats af,” zei Bram terwijl hij bladeren van zijn knieën veegde. „Ze willen allemaal naar de werkplaats nu. Waarom willen ze toch allemaal naar de werkplaats, | garbled 'koestert zich ... af' (EN 'She's heading for the workshop'); workshop term |
| 834 | Mijn grootmoeder had één caméo, uit een kerkveiling. | Mijn grootmoeder had één camee, van een rommelmarkt van de kerk. | Dutch spelling 'camee'; EN 'church rummage sale' (a jumble sale, not an auction) |
| 850 | „Heb jij zijn kaartje?” zei ik. | „Heb jij zijn kaartje?” zei ze. | EN: Claire asks for the card ('she said'); Dutch made Jessica ask, contradicting the next line |
| 856 | Aan het einde van de nageslagen toer | Aan het einde van de toer | garbled 'nageslagen' |
| 866 | op Pip’s rug | op Pips rug | Dutch genitive has no apostrophe after a consonant |
| 879 | in een rechtszaak geen standhouden | in een rechtszaak niet standhouden | ungrammatical negation |
| 883 | Ik streek Sam niet van de lijst | Ik streepte Sam niet van de lijst | 'streek' (stroked/ironed) for 'streepte' (crossed off) |
| 885 | De broche, de losse steen, Ridgeline | De broche, de ene steen, Ridgeline | EN 'the single stone'; 'losse' = loose |
| 887 | precies degene die zouden vertellen | precies degenen die zouden vertellen | plural pronoun |
| 887 | zijn degene waarvan hij | zijn degenen waarvan hij | plural pronoun |
| 893 | als er niemand anders meer over is om te verduren | als er niemand anders meer over is om te verdenken | 'verduren' (endure) for 'verdenken' (suspect); EN 'no one else left to suspect' |
| 912 | terwijl ze kopje-unter ging | terwijl ze kopje-onder ging | typo |
| 924 | dan zeg je maar dat de smeden in drie graafschappen me nog gunsten schulden | dan zegt u maar dat de smeden in drie graafschappen me nog gunsten schuldig zijn | Sam addresses Jessica as 'u'/'mevrouw Claus' (514, 536 and this same speech); 'schulden' is not a verb |
| 932 | „Lekkere vent,” zei ze | „Echte firma,” zei ze | EN 'Real firm' (the firm exists); Dutch said 'tasty/hot guy' |
| 932 | doet precies wat je man zegt dat hij doet | doet precies wat Carter zegt dat hij doet | EN 'your man' = Neil Carter; 'je man' reads as Jessica's husband |
| 936 | „Daar houd ik je aan. | „Ga uw gang. | EN 'By all means'; Dutch said 'I'll hold you to that'; Neil addresses Jessica as 'u' |
| 940 | zwakjes ontstemde fascinatie | licht ontzette fascinatie | EN 'faintly appalled'; 'ontstemd' = annoyed |
| 945 | „Hier. Je kunt dit net zo goed hebben, | „Hier. U kunt dit net zo goed hebben, | Neil addresses Jessica as 'u' throughout (935–944) |
| 945 | het slechtste helft daarvan gebruikt om een [ZWSP][ZWSP]goede vrouw te tergen | de slechtste helft daarvan gebruikt om een goede vrouw te kwellen | article ('de helft'); two zero-width spaces in the text; EN 'torture' ('tergen' = provoke) |
| 948 | heel höfelijk vraagt | heel hoffelijk vraagt | typo (German-style umlaut) |
| 948 | waarop het briefje jouw vriendin wil doen geloven | waarop het briefje uw vriendin wil doen geloven | Neil addresses Jessica as 'u' |
| 950 | waar Fiona zichzelf bijna voor dood had gehouden om het maar te bewaren | waar Fiona zich bijna kapot voor had gemaakt om het maar te bewaren | EN 'half killing herself to keep'; 'voor dood houden' = to believe dead |
| 952 | Zeg je vriendin eens wat, | Zeg uw vriendin eens wat, | Neil addresses Jessica as 'u' |
| 952 | en elk stuk voor stuk bleek kleiner | en stuk voor stuk bleken ze kleiner | ungrammatical |
| 964 | Bakkerijbonen, | Bakkerijbonnen, | 'bonen' = beans; EN 'Bakery Receipts' = bonnen |
| 964 | drie trof met rood potlood bovenaan doorgestreept: | drie trof die bovenaan met rood potlood gemarkeerd waren: | EN 'marked across the top in red pencil'; 'doorgestreept' = crossed out |
| 968 | door een huisknecht; | door een huisbediende; | EN 'household servant' (gender-neutral); 'huisknecht' = manservant, but the thief was a maid |
| 982 | voor de Vereniging. | voor het Genootschap. | Historical Society = 'Genootschap' (42×) |
| 992 | Voor de Vereniging heeft hij zichzelf zowat van alles weten te overtuigen. | Voor het Genootschap heeft hij zichzelf zowat alles aangepraat. | Society term; 'zichzelf van alles overtuigen' is ungrammatical (EN 'talked himself into almost anything') |
| 1000 | vanuit het atelier, | vanuit de werkplaats, | workshop = 'werkplaats' throughout |
| 1002 | in de richting van het atelier | in de richting van de werkplaats | workshop term |
| 1004 | voordat je nog dieper afdalen in | voordat je nog dieper afdaalt in | verb agreement |
| 1006 | op de deur van het atelier | op de deur van de werkplaats | workshop term |
| 1037 | Hetzelfde crème papier. | Hetzelfde crèmekleurige papier. | uninflected 'crème' |
| 1037 | Rode strik op de krans als het klaar is. | Rood lint op de krans als het klaar is. | EN 'Red ribbon'; the ribbon is 'lint' everywhere else, incl. the first note (177) |
| 1043 | een rijke familielid | een rijk familielid | 'het familielid' (neuter) |
| 1047 | een kwestie was van hoe en of ik het in mijn eentje kon oplossen | een kwestie was van hoe, en of hij het alleen had gedaan | EN 'only a matter of how and whether-alone' = whether Theo acted alone (cf. 982); Dutch said whether Jessica could solve it alone |
| 1049 | „Ik ben in de buurt,” zei ik. | „Ik zit er dichtbij,” zei ik. | EN 'I'm close' (to the answer); 'in de buurt' = physically nearby |
| 1055 | Ze maakte een wegwerpbaren handbeweging | Ze maakte een wegwerpend handgebaar | non-word |
| 1059 | en het wie was al evenmin een raadsel | en het wie bijna ook | EN 'and nearly the who'; Dutch stated the who was certain |
| 1067 | voordat de laatsten vertrokken zijn | voordat de laatste daarvan voorbij is | EN 'before the last of them is gone' = the three days; Dutch said 'before the last people have left' |
| 1074 | een beschilderd winterachtergrond | een beschilderde winterachtergrond | 'de achtergrond' — inflected adjective |
| 1074 | sinds de kassa van Olivia weg was | sinds het geldkistje van Olivia | EN 'since Olivia's cash box'; Dutch added that the till was gone |
| 1076 | door de handige hand van haar vader | door de zorgvuldige hand van haar vader | EN 'her father's careful hand' |
| 1077 | was ik ook op mijn hoekje | was ik ook op mijn hoede | garbled idiom (EN 'I was watching too') |
| 1078 | Mevrouw Pelletier kelk ons verbaasd aan. | Mevrouw Pelletier keek ons verbaasd aan. | typo |
| 1085 | „Jullie pinguïn heeft | „Je pinguïn heeft | Noriko addresses Jessica alone as 'je' in the same speech; EN 'Your penguin' |
| 1088 | op een koud en helder dag | op een koude, heldere dag | adjective inflection ('de dag') |
| 1092 | Tegen die tijd was ze het, denk ik, al te weten gekomen. | Tegen die tijd was ze het, denk ik, al gaan vermoeden. | EN 'she'd begun to guess'; Dutch said she had found out |
| 1096 | was ik in een kleine kamer achterbleven | was ik in een kleine kamer achtergebleven | participle |
| 1100 | the sapphire at its heart | De saffier in haar hart | key clue left in English; unified with 968–972 ('de saffier in haar hart' = five words) |
| 1112 | I know how your family came by this inn | Ik weet hoe je familie aan deze herberg is gekomen | quote from the first note left in English; restored with the note's own Dutch wording (177) |
| 1112 | Dat was een vastgoaddossier. | Dat was een vastgoeddossier. | typo |
| 1116 | in de vastgoaddossiers waarvan | in de vastgoeddossiers waarvan | typo |
| 1116 | Theo had er daar één van. | Theo had er één van. | stray 'daar' |
| 1118 | Één persoon kon | Eén persoon kon | Dutch capital spelling 'Eén' |
| 1135 | In Vera's nete draadstalen mandje | In Vera's nette draadstalen mandje | typo |
| 1135 | PROPERTY — EVERGREEN AVE — WINTER WONDERLAND INN. | VASTGOED — EVERGREEN AVE — WINTER WONDERLAND INN. | English label word; the edition translates the matching drawer cards (671: AKTEN … VASTGOEDREGISTERS); street and inn names stay |
| 1141 | over marktlui en kraampllaatsen | over marktlui en standplaatsen | garbled 'kraampllaatsen' |
| 1141 | Ik had halverwege verwacht | Ik had half en half verwacht | EN 'I'd half expected'; 'halverwege' = halfway (along a route) |
| 1141 | iemand die iets heeft gehaald dat veel te groot voor haar is | iemand die iets heeft gedaan dat veel te groot voor haar is | EN 'has done a thing far too big for her'; 'gehaald' = fetched |
| 1147 | Haar ogen waren fel geworden | Haar ogen waren vochtig geworden | EN 'Her eyes had gone bright' (with tears); 'fel' = fierce |
| 1147 | die erin was geluisd door een man | die erin was meegezogen door een man | EN 'drawn into something by a man she trusted'; 'geluisd' = tricked/framed |
| 1147 | ze sliep geen zucht beter | ze sliep geen zier beter | idiom is 'geen zier' |
| 1151 | Theo had de diefstal gepleegd. Hij had het gevonden | Theo had het geheim van de diefstal. Hij had het gevonden | EN 'Theo had the theft' = he held that half of the secret; Dutch said Theo COMMITTED the theft |
| 1151 | de saffier in het hart daarvan | de saffier in haar hart | the card's wording (968–972) |
| 1151 | de steen, de pandjesbaas. | de steen, het pandjeshuis. | EN 'the pawnshop'; 'pandjesbaas' = the pawnbroker |
| 1157 | over twee van de huns. | over twee van de hunnen. | idiom 'een van de hunnen' |
| 1168 | De brieven zouden ophouden | De briefjes zouden ophouden | the blackmail notes are 'briefjes'; 'brieven' here reads as the Blackburn letters |
| 1168 | Theo zou zijn genootschap | Theo zou zijn Genootschap | institution name capitalised everywhere else |
| 1170 | Geen braaf oud man die | Geen brave oude man die | adjective inflection |
| 1176 | en dat op elke slechte avond, in elke wanhopige winter door de jaren heen, opnieuw zouden kunnen proberen | en dat ze het op elke slechte avond, in elke wanhopige winter door de jaren heen, opnieuw zouden kunnen proberen | subject and object missing |
| 1186 | zijn niet dezelfde. | zijn niet hetzelfde. | 'hetzelfde' (not the same thing) |
| 1188 | degene die het verdriet over hen hebt afgeroepen | degene die het verdriet over hen heeft afgeroepen | verb agreement |
| 1190 | ik had mijn plekje er duim voor duim veroverd | ik had mijn plekje er stukje bij beetje veroverd | EN 'an inch at a time' — idiom; imperial 'duim' calque does not read natively |
| 1190 | kon me een deel van die zwaarbevochten duim kosten | kon me een deel van dat zwaarbevochten plekje kosten | EN 'that hard-won inch' — idiom; 'duim' does not read natively |
| 1198 | En de mensen om wie het geeft komen er wel. | En de mensen om wie het gaat komen er wel. | 'om wie het gaat' (EN 'the ones who matter') |
| 1213 | achter die professionele onverschilligheid | achter die professionele zakelijkheid | EN 'professional flatness'; 'onverschilligheid' = indifference |
| 1215 | om redenen waarvan ze zichzelf er meer dan voor de helft van hadden overtuigd dat ze goed waren | om redenen waarvan ze zichzelf al meer dan half hadden overtuigd dat ze goed waren | doubled 'waarvan … ervan' |
| 1215 | wanneer iets goeds zal werken | wanneer iets vriendelijkers ook werkt | EN 'when something kinder will work' |
| 1221 | een goede man die op het padje was geraakt | een goede man die op het slechte pad was geraakt | EN 'a good man gone wrong'; idiom is 'op het slechte pad raken' |
| 1225 | mensen bij wie ze had gegeten en met wie ze aan haar tafels had gelachen | mensen die ze te eten had gegeven en met wie ze aan haar tafels had gelachen | EN 'people she had fed'; Dutch said she had eaten at their homes |
| 1237 | naar het gezicht van de vriend die hij probeerde te kwetsen | naar het gezicht van de vriendin die hij probeerde te kwetsen | Fiona is female ('vriendin' throughout) |
| 1246 | een boodschap van het burgemeestershuis | een boodschap van het burgemeesterskantoor | EN 'the mayor's office' ('burgemeesterskantoor' at 709); 'burgemeestershuis' = the mayor's house |
| 1248 | Fiona bleke en rechtop | Fiona bleek en rechtop | stray inflection |
| 1258 | Het zware crème papier met de scheprand. | Het zware crèmekleurige papier met de scheplijnen. | EN 'laid lines'; 'scheprand' = deckle edge; uninflected 'crème' |
| 1268 | „Vera,” zei ik. „Theo heeft de diefstal gepleegd. | „Vera,” zei ik. „Theo wist van de diefstal. | EN 'Theo had the theft' (held that half of the secret); Dutch said Theo COMMITTED the theft |
| 1268 | „Hij pleegde de diefstal. Jij had de akte. | „Hij had de helft over de diefstal. Jij had de akte. | EN 'He had the theft. You had the deed.'; Dutch said he committed it |
| 1268 | in je herindelingsmand | in je opbergmand | EN 'refile basket' ('opbergmand' at 1205); 'herindeling' = reorganisation |
| 1268 | Maar niemand blikt of plankt als | Maar niemand kijkt op als | garbled idiom ('zonder blikken of blozen'); EN 'no one blinks at' |
| 1272 | dat ik het zo liet klinken, omdat | dat ik het hem zo liet brengen, omdat | EN 'I let him make it sound that way'; Dutch said Vera made it sound so |
| 1274 | vanuit het duisternis | vanuit de duisternis | 'duisternis' is a de-word |
| 1283 | laten-we-dit-aljeblieft-vergeten | laten-we-dit-alsjeblieft-vergeten | typo |
| 1283 | geen gefingeerde verontwaardiging alsof een misdrijf geen misdrijf was geweest | geen gedoe alsof een misdrijf geen misdrijf was geweest | EN 'no pretending a crime had not been a crime'; Dutch added 'feigned indignation' |
| 1283 | De twee brieven werden bewijsmateriaal | De twee briefjes werden bewijsmateriaal | the blackmail notes = 'briefjes' |
| 1285 | noch een vrijgeleide was | noch gratie was | EN 'free pardon'; 'vrijgeleide' = safe-conduct |
| 1295 | als voorzitter van het Frost Falls Historical Society neer | als voorzitter van het Historisch Genootschap van Frost Falls neer | institution name left in English |
| 1297 | Het meest vernederende werk verrichten | Het nederigste werk verrichten | EN 'the humblest work'; 'vernederend' = humiliating |
| 1301 | alles met Kerstmis is vergeven | alles met Kerstmis is vergeten | EN 'all forgotten by Christmas' |
| 1311 | De brieven waren opgehouden. | De briefjes waren opgehouden. | the blackmail notes = 'briefjes' |
| 1315 | Datgene wat hij had verpest om te redden, | Datgene wat hij op de verkeerde manier had willen redden, | EN 'The thing he had done wrong to save'; Dutch said 'what he had ruined in order to save' |
| 1319 | dat de Historische Vereniging in diepe problemen zat | dat het Historisch Genootschap in diepe problemen zat | Historical Society = 'Historisch Genootschap'/'Genootschap' (42×); ch28 alone switches to 'Vereniging' |
| 1319 | naar een slecht pad hadden gedreven | op een slecht pad hadden gedreven | preposition |
| 1320 | dat de Historische Vereniging in ernstige financiële nood verkeert | dat het Historisch Genootschap in ernstige financiële nood verkeert | Historical Society = 'Historisch Genootschap'/'Genootschap' (42×); ch28 alone switches to 'Vereniging' |
| 1320 | en daarnaast een endowment om | en daarnaast een fonds om | English word 'endowment' ('fonds' at 383, 699) |
| 1322 | de geldproblemen van de Vereniging | de geldproblemen van het Genootschap | Historical Society = 'Historisch Genootschap'/'Genootschap' (42×); ch28 alone switches to 'Vereniging' |
| 1326 | dat het redden van de Vereniging alles rechtvaardigde | dat het redden van het Genootschap alles rechtvaardigde | Historical Society = 'Historisch Genootschap'/'Genootschap' (42×); ch28 alone switches to 'Vereniging' |
| 1326 | Als de Vereniging volgende week | Als het Genootschap volgende week | Historical Society = 'Historisch Genootschap'/'Genootschap' (42×); ch28 alone switches to 'Vereniging' |
| 1326 | „Een Vereniging die gered wordt door een gulle gast is slechts uitgesteld, meneer Worthington. Over vijf jaar zit ze in hetzelfde schuitje | „Een Genootschap dat gered wordt door een gulle gast is slechts uitgesteld, meneer Worthington. Over vijf jaar zit het in hetzelfde schuitje | Historical Society = 'Historisch Genootschap'/'Genootschap' (42×); ch28 alone switches to 'Vereniging' |
| 1326 | een zwak krijgt voor de dekens | een zwak krijgt voor de quilts | EN 'quilts' ('quilts' in ch1, 81–83, the callback) |
| 1327 | van puzzel naar een soort respect | van verbazing naar een soort respect | EN 'from puzzlement'; 'puzzel' = a puzzle |
| 1328 | Laat het bake-sales en gênante kleine loterijen houden | Laat het koekjesverkopen en gênante kleine loterijen houden | English 'bake-sales' ('koekjesverkopen' at 711) |
| 1330 | En de Vereniging bleef precies waar ze was geweest | En het Genootschap bleef precies waar het was geweest | Historical Society = 'Historisch Genootschap'/'Genootschap' (42×); ch28 alone switches to 'Vereniging' |
| 1330 | wat de situatie nog haperender maakte | wat de situatie nog wankeler maakte | EN 'more precarious'; 'haperend' = faltering/stuttering |
| 1331 | Ik had net een aardig mens gepraat van het oplossen van het enige concrete probleem dat aan de basis lag van de hele trieste affaire, | Ik had net een aardig mens het oplossen van het enige concrete probleem dat aan de basis lag van de hele trieste affaire uit het hoofd gepraat, | calque 'talked out of'; ungrammatical |
| 1332 | misschien langer: bake-sales, loterijen | misschien langer: koekjesverkopen, loterijen | English 'bake-sales' |
| 1333 | Maar de Vereniging bungelde | Maar het Genootschap bungelde | Historical Society = 'Historisch Genootschap'/'Genootschap' (42×); ch28 alone switches to 'Vereniging' |
| 1352 | Laat haar met rust. | Laat haar rusten. | EN 'Let her rest' (the dead Constance); 'met rust laten' = leave alone |
| 1358 | in het licht had geslepen | in het licht had gesleept | 'geslepen' (sharpened) for 'gesleept' (dragged) |
| 1362 | van my stuk had gebracht | van mijn stuk had gebracht | English 'my' for Dutch 'mijn' |
| 1369 | dus de vriendengroep en een goede helft | dus de kring en een goede helft | EN 'the circle' = the knitting circle ('de kring' throughout) |
| 1373 | en de brink is vier hectare groot | en de brink is zo'n anderhalve hectare groot | SAFE unit rule: literal 'four acres' ≈ 1.6 ha; the translator kept the number and changed the unit, making the green 2.5× larger |
| 1374 | stond de halve helft van Frost Falls | stond half Frost Falls | 'de halve helft' is a pleonasm (EN 'half of Frost Falls') |
| 1375 | De hele vriendengroep was aanwezig | De hele kring was aanwezig | EN 'the whole circle' |
| 1377 | de agente en de wijze vrouw allebei tegelijk | de politiechef en de wijze vrouw allebei tegelijk | EN 'the chief in her'; 'agente' = a (female) constable |
| 1382 | die weer uit de paddock was uitgebroken | die weer uit de weide was uitgebroken | the paddock = 'de weide' throughout |
| 1385 | Voorbij de paddock bevond zich | Voorbij de weide bevond zich | the paddock = 'de weide' throughout |
| 1392 | met Pip voor ons uit waggelde en Mark naast me | met Pip die voor ons uit waggelde en Mark naast me | missing relative pronoun |
| 1392 | als ze die opkroegen | als ze hem openmaakten | garbled 'opkroegen'; EN 'when they opened it' |
| 1398 | Omdat ze wil dat hij opengegaan is. Omdat ze elke ochtend vraagt | Ze wil dat hij opengaat. Ze vraagt elke ochtend | ungrammatical fragments (EN 'Wanting it opened. Asking every morning') |
| 1402 | Zijn stem sloeg een beetje ruw uit | Zijn stem werd een beetje schor | EN 'His voice went rough at the edge'; 'uitslaan' = to break out (rash/mould) |
| 1408 | staand in een laagje water van een centimeter | staand in een laagje water van een paar centimeter | SAFE unit rule: literal 'an inch of water' → 2–3 cm; '1 cm' undersells it |
| 1418 | richtte hij zich op en schrok terug | richtte hij zich op en zette zich schrap | EN 'straightened, and braced' |
| 1424 | Het is zoveel meer dan ik mezelf zou hebben toevertrouwd in hun schoenen. | Het is zoveel meer dan ik mezelf zou hebben gegund als ik in hun schoenen stond. | EN 'more than I'd have given me, in their place'; 'toevertrouwen' = entrust |
| 1430 | over het koude erf naar het werkhuis | over het koude erf naar de werkplaats | workshop = 'werkplaats' throughout |
| 1444 | bleef de haard in het werkhuis gloeien | bleef de haard in de werkplaats gloeien | workshop term |
| 1450 | Wat is de volgende stap? | Wat komt er hierna? | EN 'What's Next?' heading (see 24) |
| 1452 | omdat ze geen raad wiste met haar handen | omdat ze geen raad wist met haar handen | typo |
| 1458 | die kende de dosis van het poeder, wist het middel te vinden | die kocht het poeder, kende de dosis | EN 'bought the powder, knew the dose' |
| 1468 | Ik bevestigde het draad langzaam | Ik bevestigde de draad langzaam | 'de draad' (wire) |
| 1484 | die al half zo groot was als die van de anderen | die al anderhalf keer zo groot was als die van de anderen | EN 'half again the size' (1.5×); 'half zo groot' = half the size — reversed |
| 1484 | in negentienhonderdlzoveel | in negentienhonderdtachtig-en-nog-wat | garbled; EN 'nineteen eighty-something' |
| 1490 | vind je tot in de lente nog gouden appels in de bank | vind je tot in de lente nog gouden dennenappels in de bank | EN 'gold cones' (gilded pinecones) |
| 1506 | Jullie tuig doet het immers niet voor jezelf. | Jullie doen het immers niet voor jezelf. | EN 'You lot' (affectionate); 'tuig' = riffraff/scum |
| 1518 | over het strooirochema | over het strooischema | typo |
| 1520 | omdat het nu eenmaal Claire’s vak was | omdat het nu eenmaal Claires vak was | Dutch genitive |
| 1524 | los van het draad | los van de draad | 'de draad' |
| 1532 | om dingen op zij te schuiven | om dingen opzij te schuiven | spelling |
| 1540 | met de muzentent aan de ene kant | met de muziektent aan de ene kant | 'muzentent' (muses' tent) for 'muziektent' (bandstand) |
| 1544 | de lange blauwe schaduwen van het hek bij de muzentent | de lange blauwe schaduwen van het hek bij de muziektent | bandstand |
| 1548 | „ ’s Nachts omgedraaid. | „’s Nachts omgedraaid. | stray space after opening quote |
| 1552 | Die hebben ze erachter weggesveegd. | Die hebben ze erachter weggeveegd. | typo |
| 1558 | Langzaam en geduldig in zijn werkhuis, | Langzaam en geduldig in zijn werkplaats, | workshop term |

## Decisions logged

NL-D1 … NL-D15 were appended under `## Inn Trouble - ASSEMBLED - FORMATTED_Dutch` in `PROOFREAD_DECISIONS.md`. They cover: chapter 1 heading (37), TOC (22), scene breaks (996/1446/1462/1564), bt spans and the key clue at 1258, added italics, 'vijftig mijl' (185), the English banner (297), the B index cards (978), Sneeuwbal/Snowball, the green, dorp/stadje/stad, minor terms, dialogue punctuation, Emma's u/jij, and bitterzoet.

## Refusals

- Para 624: `Niet dat ik wil snoeren hoor. Ik zou nooit snoeren.`. The `old` string crossed the italic run 'nooit'. I re-applied it as two fixes (`Niet dat ik wil snoeren hoor.` and ` snoeren. Het is`), and both were APPLIED. No unresolved refusals.

## Quotes not found

- None.
