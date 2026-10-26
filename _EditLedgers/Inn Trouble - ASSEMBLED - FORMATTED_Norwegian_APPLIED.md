# APPLIED — Inn Trouble - ASSEMBLED - FORMATTED_Norwegian

## Verify

```
PASS paragraphs: baseline=1664 now=1664
PASS scene breaks: baseline=3 now=3
PASS bt spans: baseline=11 now=11
FAIL italic runs (content+order): baseline=29 now=29  (count and order unchanged; content differs only where text inside an italic run was fixed, see below)
INFO paragraphs changed vs baseline: 309
```

Italic-run content changes (all intended, text fixes inside existing italic runs):
- 116 blackmail note: 'safiren i hjørnet' → 'safiren i hjertet'; 'det gule båndet' → 'gullbåndet'
- 245 'å se' → 'å, se'
- 670 drawer cards translated (DEEDS… → SKJØTER…)
- 969 'Bakery Receipts', 'Bandstand Subscriptions', 'MISSING – refile when found.' translated
- 973 catalog card translated
- 983 'Bridge Tournament', 'Bunting', 'Surplus' translated
- 1104 'the sapphire at its heart' → 'Safiren i hjertet'
- 1139 'PROPERTY' → 'EIENDOM'
- 1545 'Det vrimler av nye mysterier…' → 'Det venter flere mysterier…' (same EN line as 1529)

## Applied fixes

| Para | Was | Now | Why |
|---|---|---|---|
| 43 | Spinnvettet hadde | Spinnvevet hadde | 'Spinnvettet' is not a word; cobwebs = spinnvev |
| 49 | lampene langs veggene | lampeholderne langs veggene | EN 'lamp brackets' (Sam made the brackets, not lamps) |
| 49 | ved ilyet | ved ildstedet | 'ilyet' is not a word; hearth = ildsted |
| 51 | Kardiganen hennes var knappe feil med en knapp. | Kardiganen hennes var kneppet skjevt med én knapp. | garbled: 'knappe feil' is not grammatical ('buttoned wrong by one button') |
| 52 | Stemmen hennes var til og med gal, | Til og med stemmen hennes var feil, | 'gal' = crazy; EN 'Even her voice was wrong' |
| 56 | til de nykommere, | til nykommerne, | definite form required |
| 58 | nei, diamanter, små noen, | nei, diamanter, små sådanne, | 'små noen' ungrammatical ('small ones') |
| 65 | og verandaforankringene klirret | og verandabrakettene klirret | EN 'porch brackets' = 'Verandabrakettene' in next para; 'forankringer' = anchorages |
| 72 | Fremmedarbeideren var spenstig | Den fremmede var spenstig | 'Fremmedarbeider' = immigrant worker; EN 'The stranger' |
| 72 | skrukketrete måten | skrukkete måten | 'skrukketrete' typo |
| 72 | det gamle gipsmedaljongen | den gamle gipsmedaljongen | medaljong is masculine |
| 76 | man hører jo i hverdagen, | man hører jo ting, | EN 'one hears'; 'i hverdagen' (in everyday life) is an addition that makes no sense |
| 84 | omtrent en tomme fra en glasspære | omtrent et par centimeter fra en glasspære | SAFE rule: literal 'about an inch' -> 2-3 cm |
| 86 | smålåten | smålig | 'smålåten' = modest; EN 'not above spite' -> smålig (petty) |
| 86 | En halv dose gjester | Et halvt dusin gjester | 'dose' for 'dozen'; = dusin |
| 86 | min vanærede pingvin | min skammelige pingvin | 'vanæret' = dishonoured; EN 'disgraceful' |
| 93 | der morgensidene fylte | der morgenbaksten fylte | 'morgensidene' is meaningless; EN 'the morning's bread' |
| 94 | som været som slår om før | som når været slår om før | missing 'når' ('like the turn in the weather before...') |
| 97 | Hun kvitret angrende. | Hun kvitret uten snev av anger. | EN 'unrepentant'; 'angrende' = repentant |
| 43 | Mr. Kim hadde | Herr Kim hadde | English 'Mr.'; edition uses fru/herr (46x) elsewhere |
| 45 | mot bygdetunet, | mot allmenningen, | the green = 'allmenningen' (18x) elsewhere |
| 57 | – Mr. Worthington, Mrs. Worthington, sa hun. | – Herr Worthington, fru Worthington, sa hun. | English 'Mr./Mrs.'; edition uses herr/fru |
| 59 | sa Mrs. Worthington. | sa fru Worthington. | English 'Mrs.' |
| 76 | den berømte Mrs. Claus. | den berømte fru Claus. | English 'Mrs.'; Neil says 'Fru Claus' in ch4 |
| 83 | En sann fornøyelse, Mrs. Claus. | En sann fornøyelse, fru Claus. | English 'Mrs.' |
| 87 | Nede på tunet holdt | Nede på allmenningen holdt | the green = 'allmenningen' |
| 93 | forbi det grønne tunet med | forbi allmenningen med | the green = 'allmenningen' |
| 34 | ved siden av en kjele han | ved siden av en fyrkjele han | EN 'a boiler'; 'kjele' alone = pot/kettle (front matter blurb) |
| 103 | løsne kntingen på | løsne knuten på | 'kntingen' typo |
| 109 | kransen med det gule båndet | kransen med gullbåndet | EN 'gold ribbon' (= gullbåndet in ch1); 'gule' = yellow |
| 109 | at jeg visste det var bråk på innsiden | at jeg visste det var trøbbel der inne | 'bråk' = noise/row; EN 'trouble inside it' |
| 110 | Jeg dytter opp | Jeg dyttet opp | present tense slip in past narration |
| 111 | med kardiganen feilknappet i dag, men ellers var alt galt med henne | med kardiganen riktig knappet i dag, men alt annet ved henne var galt | EN 'her cardigan buttoned right today' |
| 111 | Bestemorsklokken i hjørnet tikket. | Gulvuret i hjørnet tikket. | grandfather clock = gulvur ('bestemorsklokke' is not Norwegian usage) |
| 114 | mykt av elda i kantene | mykt av elde i kantene | Bokmål 'elde' |
| 116 | den med safiren i hjørnet, | den med safiren i hjertet, | EN 'the sapphire at its heart' (key clue); 'hjørnet' = corner. Front matter has 'i hjertet' |
| 116 | Ta ned det gule båndet på kransen | Ta ned gullbåndet på kransen | EN 'gold ribbon' |
| 117 | Bestemorsklokken tikket. | Gulvuret tikket. | grandfather clock = gulvur |
| 117 | Safiren i hjørnet. | Safiren i hjertet. | EN 'The sapphire at its heart.' (key clue) |
| 127 | feiret et eller annet til en hver tid | feiret et eller annet på et eller annet tidspunkt | 'til enhver tid' = at all times; EN 'at one time or another' |
| 129 | som noe du ikke bærer over med å kaste og ikke bærer over med å se på heller | som noe du ikke klarer å kaste og ikke klarer å se på heller | 'bære over med' = tolerate (a person); EN 'can't bear to throw away' |
| 134 | Safiren i hjørnet, akkurat de ordene. Og den nevner | Safiren i hjertet, akkurat de ordene. Og det nevner | key clue 'at its heart'; pronoun agrees with 'brevet' (det) |
| 136 | Hvem som helst som har skrevet denne lappen | Den som har skrevet denne lappen | EN 'Whoever wrote this note' = den som; 'hvem som helst' = anyone at all |
| 136 | i 1924, gjorde de vel ikke? | i 1924, ikke sant? | EN 'didn't they' (they did); 'gjorde de vel ikke' implies they didn't |
| 140 | Jeg ber deg bare om hvor denne viten | Jeg spør deg bare hvor denne viten | 'be om' = ask for; EN 'asking where' |
| 150 | Hun kvitterte med en liten lyd | Hun kvitret | 'kvittere' = acknowledge/sign a receipt; EN 'She chirped' |
| 150 | gjennom den våkne byen | gjennom den våknende byen | EN 'the waking town' |
| 106 | tok kappen av knaggen | tok kåpen av knaggen | 'kappe' = cape/cloak; Jessica's coat = 'kåpen' (ch4 onward) |
| 145 | innerlommen på kappen, | innerlommen på kåpen, | coat = kåpe |
| 147 | lå brettet mot kappen min. | lå brettet mot kåpen min. | coat = kåpe |
| 155 | uten å stille en eneste byge av spørsmål | uten å stille et eneste spørsmål | 'byge av spørsmål' (shower of questions) is an odd addition; EN 'didn't ask a single question' |
| 157 | med den ene lanken over øynene | med den ene luffen over øynene | 'lanke' = paw; a penguin's flipper = luffe |
| 157 | pantesjappene to byer unna | pantelånerbutikken to byer unna | EN 'the pawnshop' (singular) |
| 157 | kroen kjøpt for pengene | vertshuset kjøpt for pengene | the inn = 'vertshuset' throughout |
| 173 | sa han, er en av | sa han, – er en av | dialogue resumes after attribution; missing dash |
| 173 | Han nesten gråt da | Han gråt nesten da | word order |
| 177 | hvis bøtte som ble firt ned i den | hvem sin bøtte det var som ble firt ned i den | ungrammatical relative clause |
| 183 | over en tallerken av ingefærkjeksene mine | over en tallerken med ingefærkjeksene mine | 'tallerken med' |
| 185 | Jeg delte æren broderlig med | Jeg delte æren raust med | 'broderlig' = fraternally; EN 'handsomely' |
| 189 | med nytt sagflis på ermet | med ny sagflis på ermet | sagflis is masculine/feminine |
| 197 | Løk gjør det. | Blomsterløk gjør det. | EN 'Bulbs' (flower bulbs); 'løk' alone reads as onions |
| 199 | sa jeg, og det har aldri | sa jeg, – og det har aldri | dialogue resumes after attribution; missing dash |
| 205 | et dypalt, stødig gull | et dypt, stødig gull | 'dypalt' typo |
| 205 | fra kirken til stasjonen | fra allmenningen til stasjonen | EN 'from the green to the station'; no church in source |
| 238 | vanligvis prydede falmede | vanligvis prydet falmede | past tense of pryde = prydet |
| 239 | jeg betraktede ham | jeg betraktet ham | past tense = betraktet |
| 245 | å se | å, se | EN 'oh look'; without the comma it reads 'to see' |
| 246 | med Blackburn-arkivene innen rekkevidde | med Blackburn-eskene innen rekkevidde | EN 'the Blackburn boxes' |
| 248 | knppet helt opp | kneppet helt opp | typo |
| 251 | Deres Mr. Hussein | Din herr Hussein | Neil says 'du' to Jessica everywhere else; 'Deres' is formal/ambiguous ('their'); 'Mr.' -> 'herr' (edition uses fru/herr 46x) |
| 253 | ikke et eneste ett skrevet | ikke ett eneste skrevet | word order |
| 255 | de tingene folk ikke klarte å bære å kaste. | de tingene folk ikke klarte å kaste. | 'klarte å bære å kaste' ungrammatical; EN 'couldn't bear to throw away' |
| 261 | og jeg betraktede måten | og jeg betraktet måten | past tense = betraktet |
| 264 | Jeg saknet ikke engang farten | Jeg saktnet ikke engang farten | saktne |
| 265 | gjennom forgangen | gjennom forhallen | 'forgangen' is not a word; EN 'front hall' |
| 265 | en krøll med festhugget bånd | en krøll med festivalbånd | 'festhugget' is not a word; EN 'festival ribbon' |
| 268 | i kåpelommen for det om, | i kåpelommen likevel, | 'for det om' is garbled; EN 'all the same' |
| 268 | med gutten store av undring | med store øyne av undring | garbled; EN 'the boy's eyes wide' |
| 268 | en siste kvarttomme | en siste halv centimeter | SAFE rule: literal 'a final quarter-inch' (~6 mm) -> en halv centimeter |
| 236 | Frost Falls historiske forening holdt til | Frost Falls historielag holdt til | Historical Society = 'Historielaget' (13x) elsewhere |
| 275 | stakk nebbet under en lalle | stakk nebbet under en luffe | 'lalle' is not a word; flipper = luffe |
| 289 | den store, lune latten | den store, lune latteren | 'latten' typo |
| 303 | Kjelen er eldre enn meg. | Fyrkjelen er eldre enn meg. | EN 'The boiler'; 'kjelen' alone reads as a cooking pot/kettle |
| 303 | Hun rister sakte på hodet. | Hun ristet sakte på hodet. | present tense slip |
| 305 | skjøt Claire inn, og jeg vet | skjøt Claire inn, – og jeg vet | dialogue resumes after attribution; missing dash |
| 309 | en eneste tynn selt | en eneste rød øre | 'selt' is not a word; EN 'one thin dime' = idiom 'en rød øre' |
| 315 | Å syns synd på | Å synes synd på | infinitive 'synes' |
| 321 | Tristere historier rister | Triste historier rister | comparative error; EN 'Sad stories' |
| 323 | om en snøstorm første oktober | om første snø allerede i oktober | EN 'an October first snow' (the first snow coming in October), not a snowstorm on 1 October |
| 325 | mye å bære for kroken, | mye å bære for vertshuset, | 'kroken' = hook/nook; EN 'the inn' |
| 327 | Martha var ingen hvem som helst. | Martha lot seg ikke lure. | EN 'Martha was no one's fool' |
| 327 | Det er ikke en eneste trøbbel | Det er ikke et eneste trøbbel | trøbbel is neuter |
| 335 | og måtte rømme seg. | og måtte rømme meg. | reflexive must be first person |
| 339 | tilbake på gressplenen | tilbake på allmenningen | the green = 'allmenningen' |
| 341 | en god, gråsprengt mann | en god, gråblek mann | EN 'gray-faced'; 'gråsprengt' = greying hair |
| 349 | den store almreisa i den andre | den store almen i den andre | 'almreisa' is not a word; EN 'the great elm' |
| 349 | Det skulle bæres ut bukkeord | Det skulle bæres ut bukkebord | trestle tables = bukkebord |
| 349 | tusen små pyntegraskar | tusen små pyntegresskar | gresskar |
| 349 | levere sirkelens første dusin votter | levere syklubbens første dusin votter | the (knitting) circle = 'syklubben' in ch5 |
| 349 | ble jeg stukket i hånden av en kasse med paigresskar av en mann jeg ikke kjente, som sa: | fikk jeg en kasse med paigresskar stukket i hendene av en mann jeg ikke kjente, som sa: | 'stukket i hånden av en kasse' = stung in the hand by a crate; EN 'handed a crate' |
| 353 | med den enøyde saligheten | med den målrettede saligheten | 'enøyd' = one-eyed; EN 'single-minded' |
| 359 | den gjorde meg bedre til vilje enn en ukes søvn | den gjorde meg bedre enn en ukes søvn | 'til vilje' is garbled; EN 'did me more good than a week of sleep' |
| 373 | fraktet pyntegraskar | fraktet pyntegresskar | gresskar |
| 381 | Det finnes heile timer | Det finnes hele timer | Nynorsk/dialect form in Bokmål text |
| 387 | og fant sjefen for det hele. | og fant politisjefen. | EN 'found the chief of police' |
| 387 | og dirigerer folk | og dirigerte folk | present tense slip |
| 389 | skrev talen ned | skrev tallet ned | 'talen' = the speech; EN 'wrote the number down' |
| 411 | så henne kvele en bevegelse med hånden over kristtornen | så henne kupe hånden over kristtornen | garbled; EN 'watched her cup her hand over the holly' |
| 415 | sammen med en jente som var på helsestoff, | sammen med en jente som holdt på å bli hel igjen, | 'på helsestoff' is meaningless; EN 'a healing girl' |
| 417 | en utpressingstrussel brettet sammen i jakken min | et utpressingsbrev brettet sammen i kåpen min | EN 'blackmail note' (= utpressingsbrev ch4) in her coat (= kåpen) |
| 419 | «Slik at det blir i morgen til samme tid?» | «Samme tid i morgen?» | garbled; EN 'Same time tomorrow?' |
| 421 | «Slik at det blir i morgen til samme tid,» | «Samme tid i morgen,» | garbled; EN 'Same time tomorrow' |
| 423 | den skamløse, gresskarkledde fuglen min | den skamløse fuglen min med gresskar på haken | 'gresskarkledd' = dressed in pumpkin; EN 'pumpkin-chinned' |
| 430 | saktere hun farten | saktnet hun farten | verb 'saktne' |
| 431 | en liten, misfornøyd lat. | en liten, misfornøyd latter. | 'lat' = lazy; laugh = latter |
| 432 | ut i forgangen, | ut i forhallen, | 'forgangen' is not a word; EN 'front hall' |
| 435 | som kom inn i kulden | som kom inn fra kulden | EN 'came in cold' = came in from the cold |
| 436 | som om hun viste sin lille ære | som om hun viste sin lille ærbødighet | 'ære' = honour; EN 'paying her small respects' |
| 442 | en ordentlig lott frem i henne | en ordentlig latter frem i henne | 'lott' = lot/share; laugh = latter |
| 447 | holdt utpressingstrusselen opp | holdt utpressingsbrevet opp | blackmail note = 'utpressingsbrev' (ch4, ch7) |
| 451 | Når stjernen gikk | Da stjernen gikk | single past event = 'da' |
| 453 | – De er her for lysestaken. | – Du er her for lysestaken. | archaic formal 'De'; Sam and Jessica are on 'du' terms (455, 475) |
| 459 | Den var på brettet, og den var her. | Den var på brevet, og den var her. | 'brettet' (the tray/board) for 'brevet' (the note) |
| 471 | og lukten var på brettet. | og lukten var på brevet. | 'brettet' for 'brevet' |
| 475 | det vet jeg lige godt som noen | det vet jeg like godt som noen | Danish 'lige' |
| 475 | være sur for litt vekselpengelignende en smålig kar. | være sur for litt småpenger som en smålig kar. | garbled; EN 'being sore over pocket change like a small man' |
| 477 | spurt om kvinnen han blødde, hadde det bra | spurt om kvinnen han presset for penger, hadde det bra | 'blø' is not transitive in Norwegian; EN 'the woman he was bleeding' (extorting) |
| 481 | Oldemoromoren hennes startet det | Oldemoren hennes startet det | 'Oldemoromoren' garbled; EN 'Her great-grandmother' |
| 487 | uten å berøre noe jeg har lagt, | uten å berøre noe jeg har laget, | 'lagt' (laid) for 'laget' (made) |
| 489 | Jeg falt til ro inni meg. | Jeg ble helt stille inni meg. | EN 'I went still inside' (alert), not 'calmed down' |
| 499 | om at lukten på brettet markerte | om at lukten på brevet markerte | 'brettet' for 'brevet' |
| 512 | Sjenerte, de gamle, | Gavmilde, de gamle, | 'sjenert' = shy; EN 'Generous' |
| 560 | desto sannsynligtere er det | desto sannsynligere er det | comparative 'sannsynligere' |
| 566 | hver eneste gram av den | hvert eneste gram av den | gram is neuter |
| 574 | – antar at du fant ut | – anta at du fant ut | imperative 'anta' (EN 'suppose') |
| 605 | mens hun stod på utsiden. | mens hun stod foran den. | EN 'with her standing in front of it' (she was inside the garden, gate latched from outside) |
| 613 | kommer for å avlevere strømmåleren | kommer for å lese av strømmåleren | EN 'come to read the meter' |
| 615 | den lille, stakkarslige trøsten i å dele en fortred | den lille, stakkarslige trøsten i å ha selskap i harmen | 'fortred' = harm; EN 'the comfort of company in a grievance' |
| 627 | Den hørte aldri til på Nordpolen, Polen var bare stedet den satt. | Den hørte aldri til på Nordpolen, Nordpolen var bare stedet den satt. | 'Polen' = Poland in Norwegian; EN 'the Pole' |
| 627 | gule der de skulle ha vært oransje | gylne der de skulle ha vært oransje | EN 'gold'; 'gule' = yellow |
| 633 | Jeg lot det ligge som et åpent spørsmål. | Jeg sa det ikke som et spørsmål. | EN 'I didn't make it a question' |
| 639 | Jeg hadde brevet i frakkelommen, | Jeg hadde brevet i kåpelommen, | Jessica's coat = 'kåpen' elsewhere |
| 639 | vraltet med stor verdighet bort fra meg | vraltet målbevisst bort fra meg | EN 'with great purpose'; 'verdighet' = dignity |
| 650 | en krusete mursteinsbygning | en overpyntet mursteinsbygning | 'krusete' = curly; EN 'fussy' (over-ornate) |
| 650 | å føre kretsens navn opp | å føre syklubbens navn opp | the (knitting) circle = 'syklubben' |
| 652 | en telefon og en lærpad, | en telefon og et skriveunderlag i lær, | 'lærpad' is not Norwegian; EN 'leather blotter' |
| 656 | Er det festivalinnsamlingen? | Er det festivallisten? | EN 'The festival list?' (list of helpers), not a fundraiser |
| 660 | og han avse det fra bak | og han avså det fra bak | past tense 'avså' |
| 660 | At kjelen var inne i sin siste vinter. | At fyrkjelen var inne i sin siste vinter. | EN 'The boiler' |
| 664 | sa han da jeg var ferdig. Theo gjør | sa han da jeg var ferdig. – Theo gjør | speech resumes after attribution; missing dash (narration and speech run together) |
| 664 | ved å lytte. Kanskje festivalen | ved å lytte. – Kanskje festivalen | speech resumes; missing dash |
| 666 | samtykket jeg. Det er noe | samtykket jeg. – Det er noe | speech resumes; missing dash |
| 670 | pent opprettet på lærunderlaget | pent rettet inn på lærunderlaget | 'opprettet' = established; EN 'squared' |
| 670 | Hun hadde festivalisten klar | Hun hadde festivallisten klar | festival + liste |
| 670 | og la til kretsen med | og la til syklubben med | the circle = 'syklubben' |
| 670 | DEEDS. PERMITS. TAX ROLLS. PROPERTY RECORDS, 1900–1950. | SKJØTER. TILLATELSER. SKATTELISTER. EIENDOMSARKIV, 1900–1950. | drawer cards left in English (text inside existing italic run; 'eiendomsarkiv' matches 674/710) |
| 672 | med sin egen speilbilde | med sitt eget speilbilde | speilbilde is neuter |
| 674 | pennens skrapende stillhet. Hele veien tilbake. | pennens skrapende stillhet. – Hele veien tilbake. | speech resumes; missing dash |
| 678 | fortsatte å bevege seg. Mest for å klage | fortsatte å bevege seg. – Mest for å klage | speech resumes; missing dash |
| 686 | bak henne. Det der er Theos avdeling. | bak henne. – Det der er Theos avdeling. | speech resumes; missing dash |
| 688 | Hun skjøv festivalisten over | Hun skjøv festivallisten over | festival + liste |
| 690 | Kretsen er lagt til. | Syklubben er lagt til. | the circle = 'syklubben' |
| 696 | sa jeg. Takk skal du ha, Vera. | sa jeg. – Takk skal du ha, Vera. | speech resumes; missing dash |
| 700 | sa hun. Og ordføreren betaler | sa hun. – Og ordføreren betaler | speech resumes; missing dash |
| 706 | – Nei, sa hun. Det gjør de ikke. | – Nei, sa jeg. – Det gjør de ikke. | wrong speaker: EN '"No," I said.' (Jessica answers Vera); plus missing dash |
| 725 | med en papirbinge foran seg | med en papirbunke foran seg | 'binge' = bin; EN 'a stack of papers' |
| 725 | med sin omstendelige historikerstemme | med sin omhyggelige historikerstemme | 'omstendelig' = long-winded; EN 'careful' (= 'omhyggelige' in 731) |
| 727 | Kjelen, erklært utrangert | Fyrkjelen, erklært utrangert | EN 'The boiler' |
| 731 | hvert fond i tre fylker. | hvert fond i tre stater. | EN 'three states' (= 'tre stater' in ch5) |
| 731 | til en stiftelse i byen, | til en stiftelse i storbyen, | EN 'in the city'; 'i byen' reads as Frost Falls itself |
| 733 | som så samfunnet han hadde gitt sitt liv til | som så laget han hadde gitt sitt liv til | EN 'the Society' (Historical Society = Historielaget), not 'society/community' |
| 737 | og den knappe cardiganen, | og den tilknappede cardiganen, | 'knapp' = scant; EN 'her buttoned cardigan' |
| 754 | et hårfin hakk for stramt i vikene | et hårfint hakk for stramt i munnvikene | neuter agreement; 'vikene' alone = bays/coves (EN 'at the corners') |
| 762 | vil de ha en skjema til | vil de ha et skjema til | skjema is neuter |
| 766 | Han pustet ut en lang anstrengelse, | Han pustet langt ut, | EN 'He blew out a long breath'; 'anstrengelse' = effort |
| 766 | de tidlige timene, klokka halv seks om morgenen, | de tidlige timene, boot camp klokka halv seks om morgenen, | EN 'five-thirty boot camp' — the kind of class was dropped |
| 770 | og det betød at jeg | og det betydde at jeg | past tense 'betydde' |
| 776 | brosjen, steinen, pantehylla, | brosjen, steinen, pantelåneren, | EN 'the pawnshop'; 'pantehylla' = the pawn shelf |
| 778 | – Vel, sa jeg, du er en god venn | – Vel, sa jeg, – du er en god venn | speech resumes after attribution; missing dash |
| 791 | blitt litt tøffere i fisken | blitt litt tøffere i trynet | the idiom is 'tøff i trynet'; 'i fisken' is meaningless |
| 795 | Greta hadde en stor snøkula i glass | Greta hadde en stor snøkule i glass | indefinite form 'snøkule' |
| 795 | med byparken og rådhuset | med allmenningen og rådhuset | the green = 'allmenningen' |
| 795 | med den sta livsgladen til | med den sta munterheten til | 'livsgladen' is not a noun; EN 'determined cheer' |
| 805 | Ute på byparken var | Ute på allmenningen var | the green = 'allmenningen' |
| 813 | En fontene uten vann var en pingvin til null nytte. | En fontene uten vann var til null nytte for en pingvin. | garbled word order (says 'was a penguin of no use') |
| 817 | og lene meg tett inntil | og lente meg tett inntil | past tense 'lente' |
| 817 | ingenting på denne parken som | ingenting på denne allmenningen som | the green = 'allmenningen' |
| 827 | Han sukkede. | Han sukket. | past tense 'sukket' |
| 831 | følte hjertet mitt seg som en drage som tok fyr. | steg hjertet mitt til værs som en drage. | EN 'my heart was going up like a kite'; 'tok fyr' = caught fire |
| 834 | De i sirkelen hadde dratt stolene sine tett inntil vedovnen, med kurv med skoggrønn ull | Syklubben hadde dratt stolene sine tett inntil vedovnen, med kurver med garn i skolens grønnfarge | the circle = 'syklubben'; EN 'baskets of school-green wool' ('skoggrønn' = forest green; 'kurv' should be plural) |
| 837 | Hun hadde den fra Mr. Kim, | Hun hadde den fra herr Kim, | English 'Mr.' |
| 839 | Det er ikke sånn Mr. Kim forteller det. | Det er ikke sånn herr Kim forteller det. | English 'Mr.' |
| 839 | den store, lune lattern | den store, lune latteren | latteren |
| 843 | en rapport fra et sykesrom | en rapport fra et sykerom | sykerom |
| 844 | sa Ivy, er det noen | sa Ivy, – er det noen | speech resumes after attribution; missing dash |
| 850 | i New Hampshire og. | i New Hampshire òg. | 'og' (and) for 'òg' (also) |
| 852 | Jeg hadde sitti på | Jeg hadde sittet på | Bokmål participle 'sittet' |
| 860 | Innlosjeringen er full til festivalen | Vertshuset er fullt til festivalen | EN 'The inn's full'; 'innlosjeringen' = the lodging arrangement |
| 862 | Martha gled den ene foten ut av skoen | Martha lot den ene foten gli ut av skoen | 'gli' is intransitive |
| 863 | hang hyssingen over disken og seg i midten | seg hyssingen over disken ned på midten | garbled; EN 'the twine over the counter sagged in the middle' |
| 872 | Hele stipendet hans handlet om å være | Hele hans historiske lærdom handlet om å være | 'stipend' = grant; EN 'his whole history scholarship' (learning) |
| 872 | både klokken fem-tretti-treningen og nattvakt | både boot camp klokka halv seks og nattvakt | 'fem-tretti' is an anglicism; Norwegian time is 'halv seks' (as in ch13) |
| 874 | over alt i foajeen | overalt i foajeen | one word |
| 874 | lukter av smelten hans | lukter av ilden hans | 'smelte' = melt; EN 'smelling of his fire' |
| 876 | Lukten peker mot kroen, | Lukten peker mot vertshuset, | the inn = 'vertshuset' |
| 877 | din brautende mr. Carter. | din brautende herr Carter. | English 'Mr.' |
| 878 | til Constance's dør | til Constances dør | Norwegian genitive has no apostrophe |
| 880 | og kroens skjøte ligger | og vertshusets skjøte ligger | the inn = 'vertshuset' |
| 883 | Det er en forferdelig fasit. | Det er en forferdelig form. | 'fasit' = answer key; EN 'It's a terrible shape' (continues 'den samme formen' above) |
| 884 | sa Nick, i stedet for | sa Nick, – i stedet for | speech resumes after attribution; missing dash |
| 886 | Jeg vil ha dem begge ut av verden, | Jeg vil ha dem begge ute av bildet, | 'ut av verden' = dead/out of the world; EN 'I want them both gone' (cleared) |
| 897 | – Sam, jeg skyldte deg en ting. | – Sam, jeg skylder deg en ting. | EN 'I owe you something' (present) |
| 905 | vært sur for tyve kroner mens | vært sur for tjue dollar mens | currency changed: EN 'twenty dollars' ('tjue dollar' everywhere else) |
| 905 | Si til henne at det er slettet. De tyve kronene, | Si til henne at det er tilgitt. De tjue dollarene, | EN 'Tell her it's forgiven. The twenty dollars'; currency |
| 917 | når du forteller om de tyve kronene. | når du forteller om de tjue dollarene. | currency: EN 'the twenty dollars' |
| 926 | «Skikkelig solid,» sa hun | «Ekte firma,» sa hun | EN 'Real firm' = it is a real (existing) firm, not 'really solid' |
| 926 | «Gamlemåten, to stater unna, gjør nøyaktig det han din sier den gjør, | «Et gammelt et, to stater unna, gjør nøyaktig det han din sier det gjør, | EN 'Old one' (an old firm); 'Gamlemåten' = the old way; pronoun agrees with 'firma' |
| 926 | et ekte, pågående ett. | et ekte, pågående et. | 'ett' is the numeral |
| 926 | døde nede i byen i vår | døde nede i storbyen i vår | EN 'down in the city'; 'i byen' reads as Frost Falls |
| 926 | og ikke en dritt av pengene. | og ingenting av pengene. | vulgarity not in EN 'none of the money' |
| 926 | for å gre ut i det. | for å gre det ut. | 'gre ut i det' ungrammatical |
| 940 | slapp ut et lavt fløytetone. | slapp ut en lav plystring. | tone is feminine/masc; EN 'a low whistle' = plystring |
| 940 | Han riste langsomt på hodet | Han ristet langsomt på hodet | past tense 'ristet' |
| 940 | vil ikke ha venninnens dine penger | vil ikke ha pengene til venninnen din | garbled possessive |
| 940 | Den som blør venninnen din, | Den som presser venninnen din, | 'blø' is not transitive; EN 'Whoever's bleeding your friend' (extorting) |
| 948 | Og den sa ikke det utpressingstrusselen sa. | Og den sa ikke det utpressingsbrevet sa. | blackmail note = 'utpressingsbrevet' |
| 950 | Jeg har klagene der i, | Jeg har klagene der inne, | 'der i' incomplete |
| 950 | og støvsugde en brosje | og tørket støv av en brosje | EN 'dusting'; 'støvsuge' = vacuum (anachronistic, absurd for a brooch) |
| 950 | verre fundamenter for et herberge. | verre fundamenter for et vertshus. | the inn = 'vertshus' |
| 956 | mindre og vondere enn | mindre og tristere enn | EN 'smaller and sadder'; 'vondere' = more painful/worse |
| 965 | på en lav stabapel med esker | på en lav stabel med esker | 'stabapel' is not a word |
| 969 | Bakery Receipts | Bakerikvitteringer | index-card label left in English (EN plain text; italic added by translator kept — see decision); keeps the B-ordering |
| 969 | Bandstand Subscriptions | Bidrag til musikkpaviljongen | index-card label left in English; Norwegian label chosen to keep the B-ordering |
| 969 | MISSING – refile when found. | MANGLER – arkiveres når funnet. | red-pencil card marking left in English (italic in EN and TR) |
| 973 | Correspondence, Adelaide Blackburn to her sister, winter 1924. Re: the theft of the family brooch (the sapphire at its heart) by a household servant; the piece later pawned at Ridgeline. Of significant local interest. | Korrespondanse, Adelaide Blackburn til sin søster, vinteren 1924. Ang.: tyveriet av familiens brosje (safiren i hjertet) begått av en av tjenestefolkene; smykket senere pantsatt i Ridgeline. Av betydelig lokal interesse. | catalog card (the key clue) left entirely in English; italic run kept; 'safiren i hjertet' matches the note (116) |
| 975 | The sapphire at its heart. | Safiren i hjertet. | key-clue line left in English (pre-flight item); matches the note |
| 977 | The sapphire at its heart. Det er | Safiren i hjertet. Det er | key-clue phrase left in English |
| 977 | de samme fem ordene i samme rekkefølge | de samme tre ordene i samme rekkefølge | Norwegian phrase 'safiren i hjertet' has three words; EN 'five words' counts the English phrase |
| 977 | de samme fem rare ordene | de samme tre rare ordene | word count must match Norwegian phrase |
| 983 | Bridge Tournament | Bridgeturnering | index-card label left in English (B-ordering kept) |
| 983 | Bunting | Bannerpynt | index-card label left in English (B-ordering kept) |
| 983 | Surplus | Overskudd | index-card label left in English |
| 983 | sa noe om varmtvannsberederen | sa noe om fyrkjelen | EN 'the boiler' (the heating boiler, = fyrkjelen elsewhere); 'varmtvannsbereder' = water heater |
| 987 | hva det kunne bety for Selskapet? | hva det kunne bety for Historielaget? | the Society = 'Historielaget' throughout |
| 991 | De fem ordene. | De tre ordene. | Norwegian phrase has three words (see 977) |
| 997 | For Selskapet har han snakket seg inn i hva som helst. | For Historielaget har han snakket seg inn i nesten hva som helst. | the Society = 'Historielaget'; EN 'almost anything' |
| 1011 | der den gamle peisen på Pol-huset ville ha stått | der den gamle peisen på Nordpolen ville ha stått | EN 'the old hearth of the Pole'; 'Pol-huset' is invented |
| 1011 | og sirklet langsommelig rundt | og sirklet langsomt rundt | 'langsommelig' is not a word |
| 1013 | knapt mer enn en hvitvisking. | knapt mer enn en hvisking. | 'hvitvisking' typo |
| 1015 | og gulllyset spilte | og gullyset spilte | triple l |
| 1017 | i gløden fra den uante ilden | i gløden fra den utente ilden | 'uant' = unsuspected; EN 'the unlit fire' |
| 1026 | Menn bar bukebord ut | Menn bar bukkebord ut | bukkebord |
| 1026 | kom Vera Reed ut fra verandatrappen idet | kom Vera Reed ned verandatrappen idet | EN 'coming down the porch steps' |
| 1026 | knppet igjen i halsen | kneppet igjen i halsen | typo |
| 1046 | ut av en lomme som holdes oppned. | ut av en lomme som holdes opp ned. | 'opp ned' |
| 1052 | Jeg har alltid et blikk, å dømme etter. | Jeg har alltid et blikk, etter alt å dømme. | idiom is 'etter alt å dømme' |
| 1056 | Være dommer ved kakebordet på lørdag. | Være dommer ved paibordet på lørdag. | EN 'the pie table' (= 'pai-bordet' ch15) |
| 1058 | sa jeg, og jeg skal bære | sa jeg, – og jeg skal bære | speech resumes after attribution; missing dash |
| 1062 | De svake vannmerkene presset inn | De svake linjene presset inn | 'vannmerker' = watermarks; EN 'faint laid lines' (= 'fine parallelle linjer' ch4) |
| 1062 | ved døren til Det historiske selskaps lokaler | ved døren til Historielagets lokaler | the Society = 'Historielaget' |
| 1062 | på Selskapets papir. | på Historielagets papir. | the Society = 'Historielaget' |
| 1068 | Noen som bevegde seg | Noen som beveget seg | past tense 'beveget' |
| 1077 | Bymarken var ugjenkjennelig siden morgenen. Bukkbordene vi hadde båret ut og diltet rundt med, | Allmenningen var ugjenkjennelig siden morgenen. Bukkebordene vi hadde båret ut og stelt med, | the green = 'allmenningen'; 'Bukkbordene' typo; 'diltet rundt med' = trailed around with (EN 'fussed over') |
| 1077 | et helt bord med votter fra syforeningen | et helt bord med votter fra syklubben | the circle = 'syklubben' |
| 1078 | de første pengene foreningen hadde fått inn | de første pengene laget hadde fått inn | the Society = 'Historielaget/laget' |
| 1079 | Jeg bevegde meg | Jeg beveget meg | past tense 'beveget' |
| 1080 | løftet på hatten tvers over marken | løftet på luen tvers over allmenningen | the green = 'allmenningen'; EN 'tipped his cap' |
| 1082 | Jeg satte i gang over marken | Jeg satte i gang over allmenningen | the green = 'allmenningen' |
| 1082 | fru Pelletier fra foreningsstyret | fru Pelletier fra styret i Historielaget | the Society = 'Historielaget' |
| 1083 | da jeg kom tilbake over marken, | da jeg kom tilbake over allmenningen, | the green = 'allmenningen' |
| 1089 | spilt inn mer penger til foreningen i dag | spilt inn mer penger til Historielaget i dag | the Society = 'Historielaget' |
| 1091 | gulllysene kom til sin rett | gullysene kom til sin rett | triple l |
| 1091 | dalte ned over marken, | dalte ned over allmenningen, | the green = 'allmenningen' |
| 1092 | snøen, gulllyset, de hundre | snøen, gullyset, de hundre | triple l |
| 1104 | the sapphire at its heart | Safiren i hjertet | key-clue phrase left in English (inside existing italic run) |
| 1104 | : fem ord, en historikers | : tre ord, en historikers | word count must match the Norwegian phrase (three words) |
| 1104 | som lå i utpressingbrevet | som lå i utpressingsbrevet | compound needs linking s |
| 1104 | Brevet var skrevet på Selskapets kremfargede brevpapir, det tykke linpapiret | Brevet var skrevet på Historielagets kremfargede brevpapir, det tykke riflede papiret | Society = 'Historielaget'; 'linpapir' = linen paper, EN 'laid stock' (paper with laid lines) |
| 1104 | hadde kommet på avveier. | hadde kommet på avveie. | fixed expression 'på avveie' |
| 1108 | et ark fra Selskapets brevpapir | et ark fra Historielagets brevpapir | Society = 'Historielaget' |
| 1110 | Mannen som hadde holdt hender med meg | Mannen som hadde holdt hendene mine | 'holde hender med' = hold hands (romantically); EN 'held my hands' |
| 1110 | Han hadde funnet brosjrens historie | Han hadde funnet brosjens historie | brosjens |
| 1110 | over et døende Selskap | over et døende historielag | Society = 'Historielaget' |
| 1114 | inn i en vestibyle full av festivalgjester | inn i en foajé full av festivalgjester | 'vestibyle' is not Bokmål; lobby = 'foajeen' in this chapter group |
| 1120 | Brosjrens tyveri | Brosjens tyveri | brosjens |
| 1126 | Jeg gikk opp i sengen med den tanken | Jeg gikk opp og la meg med den tanken | 'gikk opp i sengen' is not idiomatic; EN 'went up to bed' |
| 1139 | PROPERTY — EVERGREEN AVE — WINTER WONDERLAND INN. | EIENDOM — EVERGREEN AVE — WINTER WONDERLAND INN. | folder tab label 'PROPERTY' left in English (inside existing italic run; drawer cards in 670 translated) |
| 1141 | Innens skjøt. | Vertshusets skjøte. | 'inn' is an English calque (= vertshuset throughout); 'skjøt' is not the noun (skjøte) |
| 1143 | Skjøtet til innets eiendom, | Skjøtet til vertshusets eiendom, | English calque 'inn'; = vertshuset |
| 1145 | en kopi av allmenningens skjøt, | en kopi av allmenningens skjøte, | noun is 'skjøte' |
| 1145 | og på et vis var det enda vondere. | og på et vis var det enda tristere. | EN 'somehow that was sadder' |
| 1153 | med allmenningens skjøt i vesken | med allmenningens skjøte i vesken | noun is 'skjøte' |
| 1157 | med sin omstendelige hånd, safiren i dens indre, | med sin omhyggelige hånd, safiren i hjertet, | 'omstendelig' = long-winded (EN 'careful'); key clue must read 'safiren i hjertet' as in the note and card |
| 1157 | at innet hadde blitt kjøpt | at vertshuset hadde blitt kjøpt | English calque 'inn' |
| 1157 | båret notatene tvers over byen | båret brevene tvers over byen | the blackmail notes = 'brevene' in this chapter group |
| 1159 | på innets resepsjonsskranke | på vertshusets resepsjonsskranke | English calque 'inn' |
| 1159 | som svingte innom innet. | som svingte innom vertshuset. | English calque 'inn' |
| 1159 | på innets trapp selv, den morgenen den andre beskjeden kom | på vertshustrappen selv, den morgenen det andre brevet kom | English calque 'inn'; the second note = 'det andre brevet' |
| 1161 | Theo for Selskapet han så dø tomme tommer for tommer. | Theo for Historielaget han så dø tomme for tomme. | Society = 'Historielaget'; garbled doubled idiom |
| 1169 | med allmenningens skjøt i vesken | med allmenningens skjøte i vesken | noun is 'skjøte' |
| 1174 | Theo ville beholde foreningen sin og sitt gode navn | Theo ville beholde historielaget sitt og sitt gode navn | the Society = 'Historielaget' |
| 1174 | at to av egne hadde stelt seg ille | at to av dens egne hadde stelt seg ille | missing possessive |
| 1180 | lenge og vurdere saken | lenge og vurderte saken | past tense 'vurderte' |
| 1182 | forandre hvem som forvarte hemmeligheten hennes | forandre hvem som oppbevarte hemmeligheten hennes | 'forvarte' is not a word |
| 1184 | Og det lå en andre løgn | Og det lå en annen løgn | 'en annen' |
| 1196 | et hundenavn utropt der, en stol dratt fram i strikkeringen | en hundeleting der, en stol dratt fram i syklubben | EN 'a dog search there' ('hundenavn utropt' = a dog's name called out); the circle = 'syklubben' |
| 1198 | i ringen, med hånden på kneet mitt. Uansett hva det er du bærer på, må du ikke bære det alene. Det er hele vitsen med en ring. | i syklubben, med hånden på kneet mitt. Uansett hva det er du bærer på, behøver du ikke bære det alene. Det er hele poenget med en syklubb. | 'må du ikke' = you must not (EN 'you don't have to'); quotes Martha's ch5 words, which read 'behøver du ikke … hele poenget med en syklubb' |
| 1204 | stolte og sorgmuntre på en og samme gang | stolte og sørgmodige på en og samme gang | 'sorgmunter' = wistfully cheerful; EN 'proud and sorrowing' |
| 1204 | kommer dit de og. | kommer dit de òg. | 'og' (and) for 'òg' (too) |
| 1209 | for dette var skremmende mennesker, ikke dyr | for dette var skremte mennesker, ikke dyr | 'skremmende' = frightening; EN 'frightened people' |
| 1211 | Theos katalogkort med de fem matchende ordene. Selskapets brevpapir | Theos katalogkort med de tre matchende ordene. Historielagets brevpapir | word count of 'safiren i hjertet'; Society = 'Historielaget' |
| 1211 | Innets skjøte som lå | Vertshusets skjøte som lå | English calque 'inn' |
| 1211 | Constance, brosjyren, pantelåneren | Constance, brosjen, pantelåneren | 'brosjyre' = brochure; EN 'the brooch' |
| 1225 | stukket under trinnene til innet i mørket | stukket under trinnene til vertshuset i mørket | English calque 'inn' |
| 1235 | mens bestefarsklokken tikket. | mens gulvuret tikket. | grandfather clock = 'gulvuret' (as fixed in ch2) |
| 1247 | når innet ville falle til ro | når vertshuset ville falle til ro | English calque 'inn' |
| 1211 | Lensmann Tanaka lyttet | Politisjef Tanaka lyttet | EN 'Chief Tanaka' (chief of police of a US town); 'lensmann' is a Norwegian rural office |
| 1227 | og lensmannen ved vår side | og politisjefen ved vår side | EN 'the chief of police' |
| 1252 | skrapingen av bukkeordene som ble foldet sammen på gresset | skrapingen av bukkebordene som ble foldet sammen på allmenningen | 'bukkeord' typo; the green = 'allmenningen' |
| 1252 | en sak for Selskapet, | en sak for Historielaget, | the Society = 'Historielaget' |
| 1254 | lensmannen på den andre siden | politisjefen på den andre siden | EN 'the chief of police' |
| 1264 | ble skrevet på Selskapets brevpapir. Det tykke, kremfargede arket med filtkant. | ble skrevet på Historielagets brevpapir. Det tykke, kremfargede papiret med de fine linjene. | Society = 'Historielaget'; 'filtkant' = felt edge, EN 'the laid lines' |
| 1264 | – Og dere beskriver brosjen som safiren i dens hjerte. | – Og de beskriver brosjen som safiren i hjertet. | 'dere' = you (plural); EN 'they' (the notes); key clue must match 'safiren i hjertet' |
| 1264 | en måte å redde Selskapet i de brevene | en måte å redde Historielaget i de brevene | Society = 'Historielaget' |
| 1268 | Kjelen holder på å ryke. | Fyrkjelen holder på å ryke. | EN 'The boiler' |
| 1278 | Halvt fra veret av det, og snakket om Selskapet, | Halvt fra seg av det, og snakket om Historielaget, | 'fra veret' garbled (EN 'half out of his mind'); Society = 'Historielaget' |
| 1278 | og at det ville redde Selskapet, | og at det ville redde Historielaget, | Society = 'Historielaget' |
| 1291 | som verken var en fengselscelle eller en betinget dom. | som verken var en fengselscelle eller en full benådning. | 'betinget dom' = suspended sentence (which is roughly what they got); EN 'nor a free pardon' |
| 1293 | over en kopp kaffe på kroa. | over en kopp kaffe på vertshuset. | the inn = 'vertshuset' |
| 1295 | hadde funnet en sukkerbit på gulvet | hadde funnet en sukkerpose på gulvet | EN 'a sugar packet' |
| 1299 | ettersom Selskapet var hele hans hjerte, og Selskapet var det ene | ettersom Historielaget var hele hans hjerte, og Historielaget var det ene | the Society = 'Historielaget' |
| 1301 | ved hjelp av Selskapets samling og brevpapir | ved hjelp av Historielagets samling og brevpapir | the Society = 'Historielaget' |
| 1303 | Han kunne få være frivillig i Selskapet. | Han kunne få være frivillig i Historielaget. | the Society = 'Historielaget' |
| 1305 | hadde stålsettt seg | hadde stålsatt seg | 'stålsatt' |
| 1315 | og Pip og je spaserte | og Pip og jeg spaserte | 'je' |
| 1317 | og begynte, bare så vidt hadde begynt, på | og begynte, bare så vidt begynte, på | tense mismatch in parenthesis |
| 1319 | saken om selve Selskapet, | saken om selve Historielaget, | the Society = 'Historielaget' |
| 1324 | noe som overraskede meg, | noe som overrasket meg, | past tense 'overrasket' |
| 1326 | De velpolerte, velmenende Worthington-paret | Det velpolerte, velmenende Worthington-paret | 'paret' is singular neuter |
| 1326 | Mr. Worthington fant meg | Herr Worthington fant meg | English 'Mr.' |
| 1326 | i sin kremgule kashmirgenser og med sin fine kappe over armen | i sin kremfargede kashmirgenser og med sin fine kåpe over armen | 'kremgul' = cream-yellow (ch1 'i fargen krem'); 'kappe' = cape, EN 'good coat' |
| 1326 | selvfølgeligheten som kjenner en mann | selvfølgeligheten som kjennetegner en mann | 'kjenner' (knows) for 'kjennetegner' (characterises) |
| 1328 | – Mrs. Claus, sa han. | – Fru Claus, sa han. | English 'Mrs.' |
| 1332 | taket, kjelen, og et legat | taket, fyrkjelen, og et legat | EN 'the boiler' |
| 1340 | Mr. Worthington, sa jeg. | herr Worthington, sa jeg. | English 'Mr.' |
| 1344 | sa jeg, fordi en god mann | sa jeg, – fordi en god mann | speech resumes after attribution; missing dash |
| 1348 | er bare utsatt, Mr. Worthington. | er bare utsatt, herr Worthington. | English 'Mr.' |
| 1350 | Mr. Worthington så på meg | Herr Worthington så på meg | English 'Mr.' |
| 1352 | veldig mye penger, Mrs. Claus. | veldig mye penger, fru Claus. | English 'Mrs.' |
| 1356 | Mrs. Worthington smilte da | Fru Worthington smilte da | English 'Mrs.' |
| 1360 | med sviktende tak og døende kjel, | med sviktende tak og døende fyrkjele, | EN 'the boiler dying'; 'kjel' is a dialect form of pot |
| 1366 | Legetiden for menneskene oppi det hele hadde begynt. Men laget svevde fortsatt | Helingen av menneskene oppi det hele hadde begynt. Men laget svevet fortsatt | 'Legetiden' = the doctor's hours; EN 'The healing of the people in it'; past tense 'svevet' |
| 1381 | tjenestejente i vintre 1924 | tjenestejente vinteren 1924 | 'i vintre' = last winter; EN 'in the winter of 1924' |
| 1385 | i strikkeringen, med pinnene | i syklubben, med pinnene | the circle = 'syklubben' |
| 1393 | og brakt vanry over stedet | og brakt sorg over stedet | 'vanry' = disrepute; EN 'grieved the place' |
| 1395 | De fleste ville ha sett den andre veien. | De fleste ville ha sett en annen vei. | anglicism; Norwegian idiom is 'se en annen vei' |
| 1397 | Martha tok tak i hånden min i strikkeringen | Martha tok tak i hånden min i syklubben | the circle = 'syklubben' |
| 1397 | At en ring er til for å lene seg på? | At en syklubb er til for å lene seg på? | echoes Martha's ch5 words ('hele poenget med en syklubb') |
| 1397 | Du lente deg ikke bare på ringen da du trengte det. Du var ringen, for Fiona, | Du lente deg ikke bare på syklubben da du trengte det. Du var syklubben, for Fiona, | the circle = 'syklubben' |
| 1399 | etter en kappe som ikke var gått til ennå. Og et sted i den verste affæren jeg hadde sett i Frost Falls, i utførelsen av en vanskelig ting på riktig måte, hadde kappen gått seg til. | etter en kåpe som ikke hadde gått seg til ennå. Og et sted i den verste affæren jeg hadde sett i Frost Falls, i utførelsen av en vanskelig ting på riktig måte, hadde kåpen gått seg til. | 'kappe' = cape; EN 'a coat that wasn't broken in yet' (+ 'gått seg til' needs 'seg') |
| 1404 | Selskapet trengte litt opprydding etter Theo, så vennegjengen og | Historielaget trengte litt opprydding etter Theo, så syklubben og | the Society = 'Historielaget'; the circle = 'syklubben' ('vennegjengen' = the gang of friends) |
| 1408 | Et lite blekksvart kart | Et lite blekktegnet kart | EN 'a small inked map'; 'blekksvart' = ink-black |
| 1410 | de aller brevene som hadde satt i gang | de samme brevene som hadde satt i gang | 'de aller brevene' is garbled; EN 'the very letters' |
| 1412 | og allmenningen er på fire mål. | og allmenningen er på seksten mål. | SAFE rule: literal 'four acres' = 16.2 dekar; 'fire mål' (4,000 m²) is the wrong size |
| 1416 | og pusten vår skylte opp som en sky i kulden | og pusten vår steg opp som en sky i kulden | 'skylte' = rinsed; EN 'our breath going up' |
| 1416 | Hele vennegjengen var der | Hele syklubben var der | the circle = 'syklubben' |
| 1424 | det første gode ting han får stå i nærheten av igjen | den første gode tingen han får stå i nærheten av igjen | agreement |
| 1424 | akkurat den medisin han trenger | akkurat den medisinen han trenger | definite form |
| 1432 | – Låsen, fru Claus! | – Klinken, fru Claus! | the latch = 'klinken' (ch10) |
| 1436 | almen og gulllysene, | almen og gullysene, | triple l |
| 1438 | Vi bar boksen opp til Selskapet i fellesskap | Vi bar boksen opp til Historielaget i fellesskap | the Society = 'Historielaget' |
| 1438 | å holde Selskapets dører åpne | å holde Historielagets dører åpne | the Society = 'Historielaget' |
| 1440 | under gulllysene. | under gullysene. | triple l |
| 1443 | det grønne gresset var feid, og de innleide stolene | allmenningen var feid, og de lånte stolene | the green = 'allmenningen'; EN 'borrowed chairs' ('innleide' = hired) |
| 1443 | Men de gule lysene hang fremdeles oppe over hele byen. Ingen tok dem ned, og ingen spurte hvorfor de hadde blitt gule. | Men de gylne lysene hang fremdeles oppe over hele byen. Ingen tok dem ned, og ingen spurte hvorfor de hadde blitt gylne. | EN 'gold lights' / 'gone gold'; 'gule' = yellow |
| 1445 | med Pip luskende foran oss | med Pip vraltende foran oss | 'luske' = sneak; EN 'waddling' |
| 1449 | som en stein i elv. | som en stein i en elv. | missing article |
| 1471 | stående i en tomme vann. | stående i et par centimeter vann. | SAFE rule: literal 'an inch of water' -> et par centimeter |
| 1473 | fra kransen på innsektet. | fra kransen på vertshuset. | 'innsektet' is not a word; EN 'the inn' |
| 1481 | Han var på Selskapet, | Han var på Historielaget, | the Society = 'Historielaget' |
| 1517 | Selskapet sto fremdeles på kanten av stupet | Historielaget sto fremdeles på kanten av stupet | the Society = 'Historielaget' |
| 1517 | Kobberboksen forseglet i Selskapets forrom | Kobberboksen forseglet i Historielagets forrom | the Society = 'Historielaget' |
| 1517 | gnistret i lys og dørvinkler | gnistret i lys og dørklinker | EN 'latches'; 'dørvinkler' = door brackets |
| 1519 | hele veien fra Polhavet, | hele veien fra Nordpolen, | 'Polhavet' = the Arctic Ocean; EN 'the Pole' |
| 1525 | kreve å bli slipt inn i varmen | kreve å bli sluppet inn i varmen | 'slipt' = sharpened; = sluppet |
| 1533 | Greta ha bakt nøyaktig | Greta har bakt nøyaktig | 'har' |
| 1537 | Så kommer det en stein gjennom vinduet | Så kommer det en murstein gjennom vinduet | EN 'a brick' |
| 1539 | en kjedelig gutt med en stjålet boks | en gutt som kjedet seg, med en stjålet boks | 'kjedelig' = boring; EN 'a bored boy' |
| 1539 | kjente doseringen og viste til en helseforskrift med underparagraf. Det er ikke et raserianfall. Det er en handel. | kjente doseringen og sendte inn en klage som viste til helseforskriften med underparagraf. Det er ikke et raserianfall. Det er et fag. | 'filed a complaint' dropped; EN 'That is a trade' (a craft/profession), 'handel' = commerce |
| 1541 | har et nytt konditori datert sin storslåtte åpning til den ene uken | har et nytt konditori lagt sin storslåtte åpning til den ene uken | 'datere til' is not idiomatic; EN 'dated its grand opening to' |
| 1549 | Hver eneste kvinne i sirkelen hadde tatt med | Hver eneste kvinne i syklubben hadde tatt med | the circle = 'syklubben' (main text) |
| 1551 | med maissstenger og papirkalkuner | med maisstengler og papirkalkuner | maisstengler |
| 1555 | og la den neste bunt over den første | og la den neste bunten over den første | definite form |
| 1564 | fra den andre siden av sirkelen, uten å se opp fra sin egen krans, som allerede var halvparten så stor igjen som andres | fra den andre siden av ringen, uten å se opp fra sin egen krans, som allerede var halvannen gang så stor som de andres | here 'circle' = the ring of chairs; EN 'half again the size' = 1.5x |
| 1565 | Hun var ute etter mitt i nitten åttifem eller noe sånt. | Hun var ute etter mitt en gang på åttitallet. | EN 'nineteen eighty-something' (not 1985) |
| 1569 | Hele sirkelen, når | Hele syklubben, når | the circle = 'syklubben' |
| 1569 | plukket den opp igjen et tak senere enn resten av oss | plukket den opp igjen et øyeblikk etter resten av oss | 'et tak senere' garbled; EN 'a beat behind' |
| 1569 | hvis låt var så stor og så lett | hvis latter var så stor og så lett | 'låt' = song; EN 'whose laugh' |
| 1569 | Og Ellie, snill og ukynnet, | Og Ellie, snill og rolig, | 'ukynnet' is not a word; EN 'unhurried' |
| 1571 | som ikke var en del av sirkelen | som ikke var en del av syklubben | the circle = 'syklubben' |
| 1573 | du kommer til å finne gullkonger i sofaen | du kommer til å finne gullkongler i sofaen | 'gullkonger' = gold kings |
| 1583 | Jeg hadde fortjent meg det raskt | Jeg hadde gjort meg fortjent til det raskt | 'fortjene seg' is not idiomatic |
| 1590 | Svaret var dere alle sammen, så værs god. | Svaret var dere alle sammen, så vær så god. | 'vær så god' |
| 1609 | slik sirkelprat gjerne gjør | slik syklubbprat gjerne gjør | the circle = 'syklubben' |
| 1611 | Det var Claire som bragte på banen dette | Det var Claire som brakte på bane dette | 'brakte på bane' |
| 1615 | Det fanget sirkelens oppmerksomhet | Det fanget syklubbens oppmerksomhet | the circle = 'syklubben' |
| 1615 | i enden av en lys kvartal | i enden av et lyst kvartal | kvartal is neuter |
| 1626 | Det kom et samstemt mumling | Det kom en samstemt mumling | mumling is masculine/feminine |
| 1628 | jeg kunne ha oppgitt for sirkelen | jeg kunne ha oppgitt for syklubben | the circle = 'syklubben' |
| 1634 | – Nå var da rart | – Nå var det da rart | missing 'det' |
| 1636 | Gressplenen lå tvers overfor Yarn Tales | Allmenningen lå tvers overfor Yarn Tales | the green = 'allmenningen' |
| 1640 | med pinjearmene slått ut til sidene, det klumpete kullansiktet vendt vekk oppover plenen | med pinnearmene slått ut til sidene, det klumpete kullansiktet vendt vekk oppover allmenningen | 'pinje' = stone pine; EN 'stick arms'; the green = 'allmenningen' |
| 1653 | og sirkelen kjøpte det | og syklubben kjøpte det | the circle = 'syklubben' |
| 1653 | som sirkelprat gjerne gjør | som syklubbprat gjerne gjør | the circle = 'syklubben' |
| 1655 | Gjorde festivallysene om fra oransje til gule. | Gjorde festivallysene om fra oransje til gylne. | EN 'from orange to gold' |
| 1657 | akkurat dit pinjearmene dens pekte | akkurat dit pinnearmene dens pekte | EN 'stick arms' |
| 1657 | for hva som betød noe | for hva som betydde noe | past tense 'betydde' |
| 1659 | Men jeg sa ikke noe av dette til sirkelen. | Men jeg sa ikke noe av dette til syklubben. | the circle = 'syklubben' |
| 1659 | Snøen lå lys på plenen | Snøen lå lys på allmenningen | the green = 'allmenningen' |
| 1545 | Det vrimler av nye mysterier for Jessica Claus!  | Det venter flere mysterier for Jessica Claus!  | same EN line as 1529 ('There are more mysteries afoot…'); render identically (inside existing italic run) |

## Decisions logged (11)

- NO-D1 Title localisation (para 0): Inn Trouble
- NO-D2 2 Omission (TOC) (para 22): Regenerate TOC in formatter
- NO-D3 7 Scene breaks (para 1527, 1543, 1661): Delete at formatting stage
- NO-D4 bt spans on non-titles (para 277, 305, 317, 710, 795, 1126): Drop markers, keep text
- NO-D5 6 Term (Gazette) (para 43, 93, 277, 305, 317, 717, 1176, 1381, 1569): 'Gazette' (proper name) throughout
- NO-D6 Italics added by translator (para 245, 969, 983, 1066, 1104): Remove; all 15 EN italic runs are present
- NO-D7 5 Dialogue punctuation (para ch6, ch12, ch18, ch27 (+ e.g. 799, 809, 823, 827)): Normalise to Norwegian dash dialogue
- NO-D8 8 Units (round — ESCALATE) (para 124): 'i milevis omkring' or 'på åtte mil'
- NO-D9 3 Mistranslation (plant) (para 45): 'med en enslig kvist med oransje bær'
- NO-D10 4 Proper name (para 361, 375, 379, 1091, 1416 vs 1445–1477, 1569, 1609): 'Snowball' throughout (series rule: names stay English)
- NO-D11 6 Term (note / lobby) (para note: e.g. 116, 131, 874, 1024; lobby: 49–87 vs 110+): note = 'brevet'; lobby = 'foajeen'

## Refusals

None.

## Quoted text not found

None.
