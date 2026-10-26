# APPLIED — Inn Trouble - ASSEMBLED - FORMATTED_Italian

Working copy: `corrected/Inn Trouble - ASSEMBLED - FORMATTED_Italian.docx` (original and `_baseline/` untouched).

## Verify (`python3 _tools/preflight.py --verify`)
- PASS paragraphs: 1247 = 1247
- PASS scene breaks: 3 = 3
- PASS bt spans: 9 = 9
- Italic runs: count 21 = 21. Content differs only in runs whose text was deliberately fixed:
  - 177 (blackmail note, italic): 'lo zaffiro al cuore' → 'lo zaffiro al suo cuore' (key-clue consistency)
  - 916 (quoted note, italic): English 'I know how your family came by this inn,' → Italian
  - 932 (file tab, italic): 'PROPERTY' → 'PROPRIETÀ'
  - 1183, 1193 (italic, ×2 runs each): 'There are more mysteries afoot for Jessica Claus! ' / ' is coming soon.' → Italian
  - 1246 (italic): ' is coming soon!' → ' arriverà presto!'
- Preflight prints RESULT: FAIL only because of these intended italic-text changes. No formatting was added or removed.

## Applied fixes (245)

| Para | Was | Now | Why |
|---|---|---|---|
| 10 | Seconda Edizione | Seconda edizione | 6 Typography: Italian does not capitalise 'edizione' |
| 17 | Libri di Questa Serie | Libri di questa serie | 6 Typography: Italian title case |
| 30 | si bottonò male il cardigan | si era abbottonata male il cardigan | 6 Typo/nonword: 'bottonò' is not Italian; EN 'has buttoned her cardigan wrong' |
| 32 | esistevano esattamente in un baule | esistevano soltanto in un baule | 3 Mistranslation: EN 'exist in exactly one locked trunk'; 'esattamente in un' reads as 'precisely in a' |
| 36 | avesse avuto in anni | avesse avuto da anni | 6 Grammar: anglicism 'in years' |
| 63 | quando ci riuscì, | quando ci riuscii, | 6 Typo: 1st person passato remoto |
| 73 | attaccoi | attaccai | 6 Typo: nonword |
| 83 | «Sarò felicissima di avervi qui ancora» replicai. | «Sarò felicissima di avervi qui ancora.» | 3 Wrong speaker: 'replicai' gives Fiona's line to Jessica; EN: Fiona said it |
| 107 | Lo straniero era snello, dagli occhi vispi, sulla cinquantina, | Lo sconosciuto era snello, dagli occhi vispi, sui cinquantacinque anni, | 3 False friend: stranger = sconosciuto (straniero = foreigner); EN 'middle fifties' |
| 115 | ma mi fidai di esso circa quanto avrei potuto scagliare lontano il parafuoco | ma non mi fidavo di lui più di quanto avrei potuto scagliare lontano il parafuoco | 5 Idiom: garbled rendering of 'trusted it about as far as I could have thrown the fire screen' |
| 115 | la famosa signorina Claus | la famosa signora Claus | 3 Mistranslation: Mrs. Claus = signora (signorina = Miss) |
| 121 | attraverso la porta a vetri | attraverso la porta a battente | 3 Mistranslation: EN 'swinging door' (123 'porta a battente') |
| 125 | «Schizzinosa, la sua amica.» | «Nervosa, la sua amica.» | 3 False friend: EN 'skittish'; schizzinosa = fussy/squeamish |
| 129 | Tutti vedono tutto. | Tutti vedono tutti. | 3 Mistranslation: EN 'Everyone sees everyone' |
| 131 | a circa un pollice da una pera | a due o tre centimetri da una pera | 8 Units (SAFE): literal 'about an inch' -> 2-3 cm |
| 135 | Trassi entrambi fuori | Trassi entrambe fuori | 4 Agreement: Jessica and Pip are both female |
| 137 | la falsità sul volto di Fiona | ciò che non andava sul volto di Fiona | 3 Mistranslation: EN 'the wrongness in Fiona's face'; falsità = falseness |
| 139 | Scendei i gradini | Scesi i gradini | 6 Typo: passato remoto of scendere |
| 139 | per guardare l'inn, | per guardare la locanda, | 6 Term: 'the inn' = 'la locanda' everywhere else |
| 139 | sfarfollò | sfarfallò | 6 Typo: nonword |
| 153 | E uno straniero con un bel sorriso | E uno sconosciuto con un bel sorriso | 3 False friend: stranger = sconosciuto |
| 157 | verso i tetti dell'inn, | verso i cornicioni della locanda, | 6 Term: 'the inn' = 'la locanda'; EN 'the inn's eaves' (139 'cornicioni') |
| 169 | nel viadotto | nel viottolo | 3 Mistranslation: EN 'the lane'; viadotto = viaduct |
| 169 | ristagliava | ristagnava | 6 Typo: nonword |
| 169 | risonavano | risuonavano | 6 Typo: misspelling |
| 177 | Cinquecento mila dollari | Cinquecentomila dollari | 6 Typography: numeral written as one word |
| 181 | appuntita appena sotto il colletto | appuntata appena sotto il colletto | 3 Mistranslation: pinned = appuntata (appuntita = pointed) |
| 188 | calò sul stanzino | calò sullo stanzino | 6 Grammar: article before st- |
| 190 | i suoi occhi erano vivi dal dolore | i suoi occhi erano arrossati dal pianto | 5 Idiom: EN 'her eyes were raw'; 'vivi dal dolore' not idiomatic |
| 190 | E nessuno di noi ne ha mai fatto parola | E nessuna di noi ne ha mai fatto parola | 4 Agreement: mother, grandmother, Fiona: all women |
| 191 | Mi porsi in avanti | Mi sporsi in avanti | 6 Typo: lean forward = sporsi |
| 199 | le famiglie che la possedevano | le famiglie che le possedevano | 4 Agreement: refers to 'le vecchie carte' |
| 202 | Cinquecento mila dollari | Cinquecentomila dollari | 6 Typography: numeral written as one word |
| 206 | Non te ne stai più in giro da sola. | Non porti più questo peso da sola. | 3 Mistranslation: EN 'You're not carrying this alone anymore' |
| 214 | oppure si intristivano e tagliavano legna | oppure si chiudevano nel silenzio e spaccavano legna | 3 Mistranslation: EN 'went quiet and chopped wood' |
| 216 | Mescolò due porzioni di una minestra | Versò col mestolo due scodelle di una minestra | 3 Mistranslation: EN 'ladled out two bowls' |
| 218 | il rigattiere due paesi più in là | il banco dei pegni due paesi più in là | 6 Term: pawnshop = 'banco dei pegni' (187); rigattiere = junk dealer |
| 238 | uno straniero incuriosito | uno sconosciuto incuriosito | 3 False friend: stranger = sconosciuto |
| 258 | I bulbi ce l'hanno. | Per i bulbi è così. | 3 Mistranslation: EN 'Bulbs do' (need the dark); 'ce l'hanno' = 'have it' |
| 266 | dal verde fino alla stazione | dal prato fino alla stazione | 6 Term: 'the green' = 'il prato'; 'dal verde' is not idiomatic |
| 297 | un edificio in mattoni stretti | uno stretto edificio in mattoni | 3 Mistranslation: EN 'a narrow brick building' (not narrow bricks) |
| 308 | e tornò a mettersi di sbieco | e tornò ad appoggiarsi alla parete | 3 Mistranslation: EN 'went back to leaning' |
| 309 | bottonata fino alla gola | abbottonata fino alla gola | 6 Typo: nonword |
| 314 | «Divertente, vero? Venti lettere e nessuna | «Curioso, vero? Vent'anni di lettere e nessuna | 3 Mistranslation: EN 'Funny, that. Twenty years of letters' |
| 315 | la archiviavi | la archiviai | 6 Typo: passato remoto 1st person |
| 321 | c'era una lettera di ricatto | c'era un biglietto di ricatto | 6 Term: the note = 'biglietto' (ch2); distinguishes it from the Blackburn letters |
| 322 | «un gran fracasso per la posta degli altri» | «un sacco di storie per la posta degli altri» | 3 Mistranslation: EN 'a lot of fuss'; fracasso = loud noise |
| 322 | per sentirla respirare | per sentirlo respirare | 4 Agreement: refers to 'un bambino' |
| 323 | la carta bianca che usavano | la carta non stampata che usavano | 3 Mistranslation: EN 'the blank stock'; 'bianca' contradicts 'color crema' |
| 326 | da un festone di verdura | da un festone di rami sempreverdi | 3 Mistranslation: EN 'swag of greenery'; verdura = vegetables |
| 327 | in un edificio ghermito di oro e arancio | in un edificio addobbato d'oro e d'arancio | 3 Mistranslation: EN 'festooned'; ghermito = seized |
| 327 | lo stesso rosso che la lettera aveva detto | lo stesso rosso che il biglietto aveva detto | 6 Term: the note = 'biglietto' |
| 329 | Ma lo piallai nella tasca del cappotto comunque, accanto alla lettera. | Ma lo piegai nella tasca del cappotto comunque, accanto al biglietto. | 3 Mistranslation: 'piallai' = planed; EN 'folded'; note = biglietto |
| 329 | intenta a raddrizzare per l'ennesima frazione di pollice la sua scatola di documenti | intenta a raddrizzare di un ultimo mezzo centimetro la sua scatola di documenti | 8 Units (SAFE): literal 'a final quarter-inch' (~6 mm) |
| 53 | si allargava verso il parco, | si allargava verso il prato, | 6 Term: 'the green' = 'il prato' throughout (170, 266, 374, 885…); 'parco' = the park |
| 137 | Giù al parco, alcuni uomini | Giù al prato, alcuni uomini | 6 Term: EN 'Down on the green'; same para has 'the park' = parco, so the two collided |
| 149 | oltre il parco con le sue luci | oltre il prato con le sue luci | 6 Term: EN 'past the green' |
| 170 | La Winter Wonderland Inn spuntò | Il Winter Wonderland Inn spuntò | 6 Term: inn name is masculine elsewhere (30, 53, 588, 921) |
| 187 | La Winter Wonderland Inn. | Il Winter Wonderland Inn. | 6 Term: inn name is masculine elsewhere |
| 334 | già tre ferri avanti a tutte | già tre giri avanti a tutte | 3 Mistranslation: EN 'three rows ahead'; knitting rows = giri/ferri di lavoro, 'tre ferri' reads as three needles |
| 335 | sotto un'alula | sotto una natatoia | 6 Term: flipper = 'natatoia' (218); alula is a bird-wing feather |
| 343 | per rimborsarmi il tè | per versarmi altro tè | 3 Mistranslation: EN 'refill my tea'; rimborsare = reimburse |
| 355 | tenni il pugno chiuso | tenni il pugno aperto | 3 Reversed meaning: EN 'kept my fist open' (not clenching on the suspicion) |
| 359 | se la neve del primo ottobre | se una prima neve in ottobre | 3 Mistranslation: EN 'an October first snow' (first snowfall in October), not 'snow on 1 October' |
| 370 | avrei tenuto il pugno chiuso | avrei tenuto il pugno aperto | 3 Reversed meaning: EN 'I would keep my fist open' |
| 361 | per il figlio dei Redfern | per la bambina dei Redfern | 4 Gender: the Redfern child is Emma (376); 244 'la bambina dei Redfern' |
| 374 | C'erano tavoli da cavalletto | C'erano tavoli a cavalletto | 6 Typo: trestle tables = tavoli a cavalletto |
| 374 | il comitato vi avrebbe confabulato sopra per un'ora | il comitato ci avrebbe armeggiato sopra per un'ora | 3 Mistranslation: EN 'fussed over'; confabulare = whisper together |
| 374 | la prima dozzina di paia di guanti del circolo | la prima dozzina di manopole del circolo | 3 False friend / Term: mittens = manopole (ch5); EN 'first dozen mittens' |
| 374 | «Le metteresti lungo il fronte del palco? Fa' attenzione a quella morbida». | «Le metterebbe lungo il fronte del palco? Faccia attenzione a quella morbida». | 5 Register: a stranger addressing Jessica: Lei |
| 376 | con la beatitudine monotona che | con la beatitudine assorta che | 3 Mistranslation: EN 'single-minded bliss'; monotona = monotonous |
| 379 | si era mobilitato per cercarle. Alla fine le avevo trovate entrambe, | si era mobilitato per cercarli. Alla fine li avevo trovati entrambi, | 4 Agreement: girl + (male) dog = masculine plural |
| 383 | con un bracciolo carico di sedie | con una bracciata di sedie | 3 Mistranslation: EN 'an armful'; bracciolo = armrest |
| 390 | su un ghiaccio di cui non era ancora sicuro. «Stiamo meglio. Ora c'erano intere ore in cui dimenticavo, e poi mi ricordavo, e il ricordo non mi stendeva più al tappeto. Camminava solo al mio fianco per un po' e poi si placava di nuovo.» | su un ghiaccio di cui non è ancora sicuro. «Stiamo meglio. Ora ci sono intere ore in cui dimentico, e poi mi ricordo, e il ricordo non mi stende più al tappeto. Cammina solo al mio fianco per un po' e poi si placa di nuovo.» | 6 Tense drift: Mark speaks in the present (EN 'There are whole hours now where I forget') |
| 393 | I guanti erano ancora nella mia borsa. | Le manopole erano ancora nella mia borsa. | 3 False friend / Term: mittens = manopole |
| 394 | Prese i guanti, li contò | Prese le manopole, le contò | 3 False friend / Term: mittens = manopole |
| 396 | «Dillo a Bram. | «Lo dica a Bram. | 5 Register: Noriko addresses Jessica as Lei (394 'le sue renne') |
| 400 | Fuori dalla polpa d'arancia bagnata | Fuori dalla polpa arancione bagnata | 3 Mistranslation: pumpkin flesh is orange-coloured; 'd'arancia' = of an orange (fruit) |
| 419 | «È divertente, vero. | «Strano, vero? | 3 Mistranslation: EN 'Funny, isn't it' = odd, not amusing |
| 425 | è ancora la casa più calda della città. Non è niente. | è ancora la casa più calda della città. Non è poco. | 3 Reversed meaning: EN 'That's not nothing' (= it's something) |
| 428 | rise, bagnata. | rise tra le lacrime. | 5 Idiom: EN 'laughed, wetly'; 'bagnata' = soaked |
| 34 | Un maniscalco doveva venti dollari e si rifiutava di dare una risposta chiara. | Un fabbro in credito di venti dollari che non riusciva a ottenere una risposta chiara. | 3 Reversed meaning: Sam is OWED the $20 (ch1, ch8), the Italian made him the debtor; maniscalco = farrier, text uses 'fabbro' |
| 438 | girandola di qualche grado a ogni battito | girandola di qualche grado a ogni colpo | 3 Mistranslation: 'battito' = heartbeat; EN 'blow' |
| 448 | Era sulla nota, ed era lì. | Era sulla lettera, ed era lì. | 6 Term: 'nota' is not used for the blackmail note anywhere else; chapter uses 'lettera' |
| 450 | Tutta quella ferratura nella hall di Fiona. Le stelle sul caminetto, le staffe delle lampade, il parasale». | Tutto quel ferro battuto nella hall di Fiona. Le stelle sul caminetto, le staffe delle lampade, il parafuoco». | 3 Mistranslation: ferratura = horseshoeing; 'parasale' is a nonword (fire screen = parafuoco, ch1) |
| 452 | So che baccano fa. Un uomo adulto che fa storie per venti dollari, come un ragazzino a cui è dovuto l'assegno. | So come suona. Un uomo adulto che fa storie per venti dollari, come un ragazzino a cui devono la paghetta. | 3 Mistranslation: EN 'I know how it sounds… like a kid owed his allowance' |
| 458 | priva di quella fredda calcolusità tipica di un ricattatore | priva del freddo calcolo tipico di un ricattatore | 6 Typo/nonword: 'calcolusità' is not Italian |
| 466 | ponendo la domanda per cui ero venuta a metà sotto l'influsso di quell'odore | ponendo la domanda per cui, oltre che per l'odore, ero venuta | 3 Mistranslation: EN 'the thing I'd half come for under the smell' (the smell was the cover); Italian said asked under the smell's influence |
| 476 | o senza essergli vicini | o senza stargli vicino | 6 Grammar: agreement/idiom |
| 482 | E per esserti interessato a lei con tutto il cuore. Le dirò che l'hai fatto. | E per essersi interessato a lei con tutto il cuore. Le dirò che l'ha fatto. | 5 Register: Jessica and Sam use Lei to each other in this scene (442–484) |
| 313 | «Sei ancora a caccia della tua spilla,» dissi. | «È ancora a caccia della sua spilla,» dissi. | 5 Register: Jessica addresses Neil as Lei everywhere else (499, 525–529) |
| 497 | per la chiesa sulla piazza | per la chiesa sul prato | 6 Term: EN 'the church on the green'; 'the square' is a different place |
| 499 | «È molto interessata ai Blackburn» | «È molto interessato ai Blackburn» | 4 Agreement: Jessica is addressing Neil (male) |
| 501 | intorno al dicianquettentaquattro | intorno al millenovecentoventiquattro | 6 Typo/nonword: garbled numeral; EN 'around 1924' |
| 507 | Un banchino dei pegni a Ridgeline. | Un banco dei pegni a Ridgeline. | 6 Term: pawnshop = banco dei pegni |
| 519 | Chiunque avesse scritto quella nota | Chiunque avesse scritto quel biglietto | 6 Term: 'nota' not used for the blackmail note |
| 533 | Non ero pronta ad accantonare la sua posizione. | Non ero pronta a scagionarlo del tutto. | 3 Mistranslation: EN 'I wasn't ready to set him down all the way' (clear him) |
| 539 | «È Fulmine. | «È Ballerina. | 4 Proper name: EN 'Dancer' = Ballerina in Italian (used at 1143); Fulmine is Blitzen |
| 540 | Fuori in giardino, Fulmine sollevò | Fuori in giardino, Ballerina sollevò | 4 Proper name: Dancer = Ballerina |
| 542 | sulla spalla calda di Fulmine. | sulla spalla calda di Ballerina. | 4 Proper name: Dancer = Ballerina |
| 542 | Fulmine allungò il muso | Ballerina allungò il muso | 4 Proper name: Dancer = Ballerina |
| 545 | Non mi impiccierei mai. | Non mi impiccerei mai. | 6 Typo: spelling |
| 547 | lo stesso oro che i lampioni della festa stavano assumendo | lo stesso oro che le luci della festa stavano assumendo | 3 Mistranslation: EN 'the festival lights' (strings of lights), not lampposts |
| 561 | la credenza in cui tenevano le sardine | la credenza in cui tenevamo le sardine | 6 Grammar: EN 'where the sardines were kept' (by Jessica/Nick) |
| 565 | un edificio in mattoni pretenziosi in fondo alla piazza | un pretenzioso edificio in mattoni in cima al prato | 3 Mistranslation: EN 'a fussy brick building at the head of the green' |
| 572 | Sono sicura che troveranno il modo | Sono sicuro che troveranno il modo | 4 Agreement: the mayor is male |
| 572 | Sbozzò un sorriso | Sfoderò un sorriso | 3 Mistranslation: EN 'produced a smile'; sbozzare = rough-hew |
| 583 | Invece addolciti ogni mio modo di fare. | Invece addolcii ogni mio modo di fare. | 6 Typo: passato remoto 1st person |
| 579 | Le ho detto che lei saprebbe meglio di chiunque altro | Le ho detto che tu sapresti meglio di chiunque altro | 5 Register: Jessica addresses Vera as tu everywhere else (584, 940, 1034, 1055); 'lei saprebbe' was the lone Lei |
| 585 | Non per chiunque quest'anno. | Non per nessuno quest'anno. | 6 Grammar: EN 'Not for anyone this year' (negative) |
| 589 | una donna stanca a cui non importava ricevere domande ficcanaso | una donna stanca a cui non piacevano le domande ficcanaso | 3 Reversed meaning: EN 'didn't care for' = disliked; 'non le importava' = didn't mind |
| 589 | due persone a Frost Falls di cui non potevo sentire il nome Blackburn senza pensarci | due persone a Frost Falls a cui non potevo fare a meno di pensare sentendo il nome Blackburn | 3 Mistranslation: garbled: said the two people's name was Blackburn |
| 593 | perché la gazzetta voleva | perché la Gazette voleva | 4 Proper name: newspaper name is 'Gazette' everywhere else |
| 593 | riguardo a ciò che avevo con me | riguardo al peso che mi portavo dentro | 3 Mistranslation: EN 'what I'd been carrying' (a burden, not an object) |
| 611 | Non lo giustificavo. | Non lo perdonavo. | 3 Mistranslation: EN 'I didn't forgive it' |
| 613 | Trscrisse le cifre | Trascrisse le cifre | 6 Typo: missing letter |
| 615 | votarono per mantenere le porte aperte oltre il nuovo anno | votarono per mantenere le porte aperte fino al nuovo anno | 3 Mistranslation: EN 'through the new year'; the money only lasts until then (605) |
| 625 | il pinguino, che la tollerò con l'aria | il pinguino, che tollerò la cosa con l'aria | 4 Agreement: 'la' had no referent (pinguino is masculine); EN 'who tolerated it' |
| 626 | «Se ne aprirebbe una tutta sua nel giro di una settimana» | «Se ne impadronirebbe nel giro di una settimana» | 3 Mistranslation: EN 'She'd take it over inside a week' |
| 637 | cercando di non piantare un piede dentro una sedia vecchia di cent'anni | cercando di non sfondare con un piede una sedia vecchia di cent'anni | 5 Idiom: EN 'put my foot through a hundred-year-old chair' |
| 642 | alla sua splendida palestra | alla sua scintillante palestra | 3 Mistranslation: EN 'glittering gym' (the snow-globe decorations) |
| 651 | il verde del parco cittadino e tutto il resto | il prato, il municipio e tutto il resto | 2 Omission / 6 Term: EN 'green and Town Hall and all': Town Hall dropped; the green = il prato |
| 651 | Turbineggiava e turbinava | Turbinava e turbinava | 6 Typo/nonword: 'turbineggiava' is not standard; EN 'It swirled and swirled' |
| 655 | «È il frullatore grande, credo. | «È l'impastatrice grande, credo. | 3 Mistranslation: a bakery's big mixer = impastatrice (frullatore = blender) |
| 657 | colpa del frullatore | colpa dell'impastatrice | 3 Mistranslation: mixer = impastatrice |
| 665 | guardatela... oh, non è qui, è in chiesa, ma se fosse qui vedreste che | la guardi... oh, non è qui, è in chiesa, ma se fosse qui vedrebbe che | 5 Register: Bram is speaking to Mrs. Claus (Lei), not to a group |
| 671 | Ti dislocherai qualcosa, a te o a lei. | Ti slogherai qualcosa, tu o lei. | 6 Grammar: EN 'You'll dislocate something, yours or hers'; 'dislocare' not used for joints |
| 673 | «Non c'è niente in questo paese che sia caldo | «Non c'è niente su questo prato che sia caldo | 3 Mistranslation: EN 'on this green' |
| 687 | e un'amicizia stremata per mezzo milione di dollari | e un'amica messa alle strette per mezzo milione di dollari | 3 Mistranslation: EN 'a friend being squeezed for half a million dollars' |
| 729 | La sua intera borsa di studio in storia si basava sul | Tutta la sua erudizione storica si riduceva al | 3 Mistranslation: EN 'His whole history scholarship' = learning (joke), not a grant |
| 731 | la polvere gli fa starnutire | la polvere lo fa starnutire | 6 Grammar: fare + infinitive takes direct object |
| 735 | quella degli avvocati della tenuta | quella degli avvocati della successione | 3 Mistranslation: EN 'estate lawyers' (probate), cf. 509 'avvocati della successione' |
| 737 | si è alzato a annunciare | si è alzato ad annunciare | 6 Typo: euphonic d |
| 740 | Pressi le mani aperte | Premetti le mani aperte | 6 Typo/nonword: passato remoto of premere |
| 740 | il volere non è una prova, Nick, non lo è mai stata | il volere non è una prova, Nick, non lo è mai stato | 4 Agreement: refers to 'il volere' |
| 743 | Sam e lo straniero. | Sam e lo sconosciuto. | 3 False friend: stranger = sconosciuto |
| 745 | Me ne tenni stretta mentre salivo le scale per andare a letto, considerandola la gentilezza che era. | Mi aggrappai a quelle parole mentre salivo le scale per andare a letto, prendendole per la gentilezza che erano. | 6 Grammar: 'Me ne tenni stretta' is ungrammatical; EN 'I held onto that… took it for the kindness it was' |
| 758 | una faccenda vecchia di cent'anni e che non c'entrava affatto con lei | una faccenda vecchia di cent'anni di cui lei non aveva alcuna colpa | 3 Mistranslation: EN 'not her fault at all' (it does concern her) |
| 770 | Un maniscalco rifinisce il ferro | Un fabbro rifinisce il ferro | 3 Mistranslation: smith = fabbro (maniscalco = farrier); Sam is 'fabbro' elsewhere |
| 770 | il parascintille | il parafuoco | 6 Term: fire screen = parafuoco (ch1) |
| 774 | dille che i maniscalchi di tre contee | dille che i fabbri di tre contee | 3 Mistranslation: smiths = fabbri |
| 789 | Qualcuno sta stringendo alle corde la discendente. | Qualcuno sta mettendo alle corde la discendente. | 5 Idiom: idiom is 'mettere alle corde'; EN 'squeezing the descendant' |
| 790 | ripulendosi un po' di più a ogni parola | scagionandosi un po' di più a ogni parola | 3 Mistranslation: EN 'clearing himself' (of suspicion) |
| 794 | nel modo semplice in cui la nota vuole far credere | nel modo semplice in cui la lettera vuole far credere | 6 Term: 'nota' not used for the blackmail note; 793 'la lettera di ricatto' |
| 797 | «Tienila pure. | «La tenga pure. | 5 Register: Neil addresses Jessica as Lei throughout (same para 'Dica una cosa alla sua amica') |
| 797 | Ogni fottuta volta. | Ogni volta. | 3 Mistranslation (added profanity): EN 'Every time.' — translator added an obscenity absent from the source |
| 177 | quella con lo zaffiro al cuore, | quella con lo zaffiro al suo cuore, | 3 Key clue (consistency): the note must quote the card verbatim: card (807/808/809) reads 'lo zaffiro al suo cuore' and the text says 'the same five words in the same order'; note had 4 words |
| 178 | Lo zaffiro al cuore. Un modo | Lo zaffiro al suo cuore. Un modo | 3 Key clue (consistency): match the card wording (five words) |
| 195 | Lo zaffiro al cuore, esattamente quelle parole. | Lo zaffiro al suo cuore, esattamente quelle parole. | 3 Key clue (consistency): 'those very words' must match the note/card |
| 856 | Pensa che tu abbia qualche ricca parente | Pensa che tu abbia qualche parente ricco | 4 Gender: EN 'a rich relation' (unspecified); feminine was invented |
| 856 | Crede che la paura in persona | Crede che la paura stessa | 5 Idiom: EN 'the fear itself'; 'in persona' personifies |
| 856 | Le persone agiate non immaginarono | Le persone agiate non immaginano | 6 Tense: general statement in present; 'immaginarono' is passato remoto |
| 858 | a qualsiasi asse le passi accanto | a qualsiasi asse gli passi accanto | 4 Agreement: refers to 'un nuotatore' |
| 870 | ciò che dicevano le lettere di Blackburn | ciò che dicevano le lettere dei Blackburn | 6 Grammar: family name takes the plural article |
| 885 | con le moffole del circolo | con le manopole del circolo | 6 Term: mittens = manopole everywhere else (337, 690, 722) |
| 886 | fu il primo denaro che la Società aveva incassato dalla cassetta delle offerte di Olivia | fu il primo denaro che la Società incassava dai tempi della cassetta delle offerte di Olivia | 3 Mistranslation: EN 'the first money the Society had taken in since Olivia's cash box' (since, not from) |
| 888 | un paio di moffole prese dal tavolo | un paio di manopole prese dal tavolo | 6 Term: mittens = manopole |
| 890 | Mi diressi verso il prato camminando troppo in fretta | Attraversai il prato camminando troppo in fretta | 3 Mistranslation: EN 'I started across the green' (she is already on it) |
| 892 | «Avevi l'aria di voler placcare | «Aveva l'aria di voler placcare | 5 Register: Noriko addresses Jessica as Lei (394, 894 'signora Claus') |
| 897 | «Sai dov'è la stazione. | «Sa dov'è il comando. | 5 Register / 3 Mistranslation: Noriko → Jessica: Lei; EN 'the station' = police station ('stazione' reads as train station) |
| 897 | «Il tuo pinguino oggi | «Il suo pinguino oggi | 5 Register: Noriko → Jessica: Lei |
| 898 | «Non glielo dire» dissi. | «Non glielo dica» dissi. | 5 Register: Jessica ↔ Noriko on Lei terms |
| 899 | in cui avevamo trovato Snowball. | in cui avevamo trovato Palla di Neve. | 4 Proper name: the dog is 'Palla di Neve' everywhere else (380, 387, 1125…) |
| 448 | un foglio di carta color avorio piegato | un foglio di carta color crema piegato | 6 Term: EN 'cream paper'; 'color crema' elsewhere (323, 850) |
| 910 | sulla carta color avorio della Società | sulla carta color crema della Società | 6 Term: EN 'cream stationery' |
| 911 | sperando che una di esse deviaste altrove | sperando che una di esse deviasse altrove | 6 Typo: congiuntivo 3rd person |
| 912 | uno bianco che Theo mi aveva dato | uno non scritto che Theo mi aveva dato | 3 Mistranslation: EN 'a blank one'; 'bianco' contradicts the cream colour |
| 912 | Lo stesso avorio. | Lo stesso color crema. | 6 Term: EN 'The same cream' |
| 916 | I know how your family came by this inn, | So come la tua famiglia è entrata in possesso di questa locanda, | 1 Untranslated: quotation of the first note left in English (text inside existing italic run); wording copied from 177 |
| 918 | Aveva il furto. | Aveva le carte del furto. | 3 Mistranslation: EN 'He had the theft' = he held the record of the theft; 'Aveva il furto' reads as nonsense / as if he committed it |
| 928 | il terreno comune in persona | il terreno comunale vero e proprio | 5 Idiom: EN 'the common land itself'; 'in persona' personifies |
| 930 | sulle etichette d'ottone delle cartelline lungo i cassetti degli schedari | sulle cornici d'ottone dei cartellini lungo i cassetti degli schedari | 3 Mistranslation: EN 'the brass card frames along the filing drawers' (cf. 575/576 'cornice d'ottone') |
| 932 | PROPERTY — EVERGREEN AVE | PROPRIETÀ — EVERGREEN AVE | 1 Untranslated: English file label; the other drawer labels are translated (575 'ARCHIVI IMMOBILIARI') |
| 934 | Messo nel cestino del riarchiviazione | Messo nel cestino delle cose da riarchiviare | 6 Grammar: 'del riarchiviazione' is ungrammatical |
| 936 | in nessuna lettera di Blackburn | in nessuna lettera dei Blackburn | 6 Grammar: family name takes the plural article |
| 938 | Avevo quasi sperato, quando finalmente | Mi ero quasi aspettata, quando finalmente | 3 Mistranslation: EN 'I'd half expected', not 'hoped' |
| 938 | Le mani non le tremavano mentre raddrizzava il cestino. | Le mani le tremavano mentre raddrizzava il cestino. | 3 Reversed meaning: EN 'Her hands weren't steady' |
| 948 | Theo aveva il furto. Lo aveva trovato nelle lettere di Blackburn, | Theo aveva le carte del furto. Lo aveva trovato nelle lettere dei Blackburn, | 3 Mistranslation: EN 'Theo had the theft' = held the record of it; 'aveva il furto' is meaningless/misleading; article |
| 948 | il zaffiro nel suo cuore | lo zaffiro al suo cuore | 3 Key clue (consistency): key phrase must match the card verbatim (807 'lo zaffiro al suo cuore'); also 'il zaffiro' is ungrammatical |
| 954 | In fondo c'erano due persone che avevo conosciuto e apprezzato, un'intera e calda cittadina | In fondo c'erano due persone che avevo conosciuto e apprezzato, un'amica che i due avevano stretto in una morsa e un'intera e calda cittadina | 2 Omission: EN 'a friend they had been squeezing between them' dropped |
| 963 | davanti al cammino | davanti al camino | 6 Typo: cammino = path; camino = fireplace |
| 965 | Avrebbero pianto di sollievo per essere stati scagionati. | Avrebbero pianto di sollievo per averla scampata. | 3 Mistranslation: EN 'let off'; 'scagionati' = cleared/proved innocent |
| 967 | sulla Gazzetta. | sulla Gazette. | 4 Proper name: newspaper is 'Gazette' everywhere else |
| 983 | Theo non deve mai diventare un uomo che potrebbe essere perdonato. | Theo non è mai costretto a diventare un uomo che possa essere perdonato. | 3 Mistranslation: EN 'Theo never has to become…'; 'non deve mai' = must never |
| 987 | una ricerca di cani là | la ricerca di un cane là | 3 Mistranslation: EN 'a dog search' = the search for Martha's dog |
| 995 | I suoi occhi erano fieri e addormentati insieme. | I suoi occhi erano fieri e addolorati insieme. | 3 Mistranslation: EN 'proud and sorrowing'; addormentati = asleep |
| 1001 | nel suo piccolo ufficio alla stazione | nel suo piccolo ufficio al comando | 3 Mistranslation: police station; 'stazione' reads as railway station |
| 1001 | L'atto di proprietà dell'locanda | L'atto di proprietà della locanda | 6 Typo: article |
| 1004 | per tutto il tragitto fino alla stazione | per tutto il tragitto fino al comando | 3 Mistranslation: police station |
| 1006 | per motivi di cui si erano più che convinti che fossero giusti | per motivi che si erano convinti, più che a metà, fossero giusti | 6 Grammar: ungrammatical; EN 'reasons they'd more than half talked themselves into believing were good' |
| 1012 | «Pendevi che il segreto | «Pensavi che il segreto | 6 Typo: pendevi = were hanging |
| 1017 | l'amico che ha cercato di ferire | l'amica che ha cercato di ferire | 4 Gender: the friend is Fiona |
| 1020 | ci saremmo seduti a parlare | ci saremmo sedute a parlare | 4 Agreement: Jessica, Noriko and Fiona are all women |
| 1029 | Quella pesante color avorio con le vergate. L'ho confrontata grammo per grammo | Quella pesante color crema con le linee vergate. L'ho confrontata fibra per fibra | 3 Mistranslation: EN 'heavy cream stock with the laid lines… grain to grain' (paper grain, not grams) |
| 1029 | come la saffira al suo cuore | come lo zaffiro al suo cuore | 3 Key clue: 'saffira' is not a word; the key phrase must match the card verbatim ('lo zaffiro al suo cuore') |
| 1031 | L'ho vista incanutire. | L'ho vista farsi grigia in volto. | 3 Mistranslation: EN 'I watched her go gray' (ashen); incanutire = hair turning white |
| 1034 | «Vera», dissi. «Theo ha compiuto il furto. | «Vera», dissi. «Theo aveva le carte del furto. | 3 Mistranslation (critical): EN 'Theo had the theft' = held the record of it; Italian says Theo COMMITTED the theft (Constance did, in 1924) |
| 1034 | «Lui ha compiuto il furto. Tu avevi l'atto. | «Lui aveva le carte del furto. Tu avevi l'atto. | 3 Mistranslation (critical): same: EN 'He had the theft. You had the deed.' |
| 1036 | Barcollò leggermente, | Si dondolò leggermente, | 3 Mistranslation: EN 'She rocked a little' (seated); barcollare = stagger |
| 1049 | Fese un passo indietro. Non per una stagione, per poi essere reinsediato quattamente sulla sua poltrona | Fece un passo indietro. Non per una stagione, per poi essere reinsediato senza clamore sulla sua poltrona | 6 Typo/nonword: 'Fese', 'quattamente' are not Italian; EN 'quietly slipped back' |
| 1055 | voglio che tu vi ti aggrappi | voglio che tu ti ci aggrappi | 6 Grammar: clitic order |
| 1056 | faceva molto male più che lasciarla stare | faceva molto più male che lasciarla stare | 6 Grammar: comparative |
| 1058 | la cosa stessa che Theo aveva rovinato pur di salvare | la cosa stessa per salvare la quale Theo si era rovinato | 3 Reversed meaning: EN 'the very thing Theo had ruined himself trying to save'; Italian said Theo ruined the Society |
| 1059 | La cosa sbagliata che aveva fatto per salvare continuava a fallire. | Ciò che aveva cercato di salvare nel modo sbagliato continuava ad andare in rovina. | 3 Mistranslation: garbled; EN 'The thing he had done wrong to save was still failing' |
| 1066 | Una parte di me, stante stanca su quel freddo portico, | Una parte di me, stanca com'ero su quel freddo portico, | 6 Grammar: 'stante stanca' is ungrammatical; EN 'standing tired' |
| 1071 | e a sua discolpa la sua espressione cambiò | e a suo merito la sua espressione cambiò | 3 Mistranslation: EN 'to his credit'; 'a sua discolpa' = in his defence |
| 1073 | Abbiamo comprato la nostra strada in troppe cose nel corso degli anni. Sarebbe una novità, alla nostra età, esservi invitati. | Ci siamo comprati l'ingresso in fin troppe cose nel corso degli anni. Sarebbe una novità, alla nostra età, essere invitati a farne parte. | 5 Idiom: calque of 'bought our way into'; not Italian |
| 1074 | Così la lasciarono andare in quel modo. Nessun assegno. Una promessa invece, tenuta in riserbo | Così la cosa restò in quei termini. Nessun assegno. Una promessa invece, tenuta in serbo | 3 Mistranslation: EN 'So they left it that way'; 'in riserbo' = in reserve of discretion, idiom is 'in serbo' |
| 1086 | quello che mi dicesti | quello che mi hai detto | 6 Tense: passato remoto for something said a few days earlier, in speech |
| 1090 | con il suo bravo cattivo senza macchia e il suo bravo delitto pulito | con il suo cattivo bello netto e il suo delitto bello netto | 3 Mistranslation: EN 'clean little villain'; 'senza macchia' = spotless/blameless, the opposite |
| 1098 | le moffole finite | le manopole finite | 6 Term: mittens = manopole |
| 1100 | in quei stessi giorni | in quegli stessi giorni | 6 Grammar: article form before st- |
| 1106 | Che un cerchio serve per appoggiarsi? | Che un circolo serve per appoggiarsi? | 6 Term: echo of Martha's line at 363 ('il senso di un circolo'): the knitting circle |
| 1106 | Dissi che me lo ricordava bene. | Dissi che me lo ricordavo bene. | 6 Typo: 1st person |
| 1106 | ad appoggiarti al cerchio quando | ad appoggiarti al circolo quando | 6 Term: the knitting circle |
| 1106 | Sei stata tu il cerchio, | Sei stata tu il circolo, | 6 Term: the knitting circle |
| 1106 | alla sua moffola | alla sua manopola | 6 Term: mittens = manopole |
| 1115 | si erano riunite sul pratone, | si erano riunite sul prato, | 6 Term: 'the green' = 'il prato' in chs 1–29; ch30 switches to 'pratone' |
| 1121 | sepolta sul pratone, e il pratone misura | sepolta sul prato, e il prato misura | 6 Term: the green = il prato |
| 1123 | si radunò sul pratone intorno | si radunò sul prato intorno | 6 Term: the green = il prato |
| 1125 | l'intero pratone emise | l'intero prato emise | 6 Term: the green = il prato |
| 1139 | attraverso il pratone torcendosi | attraverso il prato torcendosi | 6 Term: the green = il prato |
| 1139 | nel mezzo del pratone con la brina | nel mezzo del prato con la brina | 6 Term: the green = il prato |
| 1145 | Rimasi lì sul pratone a guardare | Rimasi lì sul prato a guardare | 6 Term: the green = il prato |
| 1129 | la capa in lei e la saggia allo stesso tempo | il capo della polizia e la donna saggia allo stesso tempo | 5 Register/Idiom: 'capa' is slang; EN 'the chief in her and the wise woman both' |
| 1145 | e mi chiesi quanta altra ne avrebbe sprigionata per quando fossimo tornati a casa. | e mi chiesi quanta altra magia vi avrebbe trovato, a girare in tondo, per quando fossimo tornati a casa. | 3 Mistranslation: EN 'how much more of it would be circling there by the time we got home'; Italian said the hearth would emit it |
| 1149 | e Theo sarebbe stato lì a vederlo. | e Theo sarebbe stato lì a vederla. | 4 Agreement: refers to 'la scatola' |
| 375 | «Signora Claus, il suo pinguino sta mangiando una zucca». | «Signora Claus, il tuo pinguino sta mangiando una zucca». | 5 Register: Emma addresses Jessica as tu everywhere else (399, 402, 404, 1160) |
| 1162 | Babbo pensa che l'abbia preso | Papà pensa che l'abbia preso | 5 Register/Ambiguity: 'Babbo' (regional) collides with Babbo Natale in a book about Mrs. Claus; Emma means her father |
| 1169 | se devo essere sincera | se devo essere sincero | 4 Agreement: Theo is male |
| 1183 | There are more mysteries afoot for Jessica Claus!  | Altri misteri attendono Jessica Claus!  | 1 Untranslated: end-of-book line left in English (italic run kept) |
| 1183 |  is coming soon. |  arriverà presto. | 1 Untranslated: end-of-book line left in English (italic run kept; <bt> untouched) |
| 1184 | What's Next? | Cosa c'è dopo? | 1 Untranslated: back-matter heading left in English; TOC (24) has 'Cosa c'è dopo?' |
| 1187 | una parola compariva in rosso sul compensato della facciata | una parola compariva in rosso sul rivestimento di assi della facciata | 3 Mistranslation: EN 'clapboard'; compensato = plywood |
| 1193 | There are more mysteries afoot for Jessica Claus!  | Altri misteri attendono Jessica Claus!  | 1 Untranslated: line left in English |
| 1193 |  is coming soon. |  arriverà presto. | 1 Untranslated: line left in English |
| 1194 | Excerpt from  | Estratto da  | 1 Untranslated: back-matter heading left in English; TOC (26) has 'Estratto da' |
| 1195 | come la lana del negozio non riusciva mai a fare del tempo. | come la lana del negozio non riusciva mai a fare. | 6 Grammar: stray 'del tempo' makes the sentence nonsensical |
| 1203 | che era già grossa il doppio di quella di chiunque altra e doppiamente densa | che era già grande una volta e mezza quella di chiunque altra e due volte più fitta | 3 Mistranslation: EN 'half again the size of anyone else's and twice as dense' |
| 1217 | Ne pressò uno su di me prima che potessi chiederlo | Me ne mise in mano uno prima che potessi chiederlo | 5 Idiom: calque of 'pressed a cupcake on me' |
| 1230 | «Wren... Non erano rivolti | «Non erano rivolti | 1 Untranslated / corruption: 'Wren...' is a garbled English fragment ('Weren't'); not in the source |
| 1231 | Gli scolari ne avevano costruito una fila durante la prima vera nevicata. Tre pupazzi, fatiscenti e sbilenchi | Gli scolari avevano costruito una fila di pupazzi di neve durante la prima vera nevicata. Tre pupazzi, grassocci e sbilenchi | 3 Mistranslation: 'ne' had no referent; EN 'fat and lopsided' — fatiscenti = crumbling |
| 1234 | Ci accalcate tutte alla finestra | Ci accalcammo tutte alla finestra | 6 Typo: passato remoto 1st plural |
| 1240 | facendo fare due passaggi al pupazzo di neve di un bambino nel buio per affrontare | facendo girare nel buio il pupazzo di neve di un bambino per guardare | 3 Mistranslation: EN 'walking a child's snowman around in the dark to face' |
| 1246 |  is coming soon! |  arriverà presto! | 1 Untranslated: closing line left in English (italic run kept) |

## Decisions logged (13) — `_EditLedgers/PROOFREAD_DECISIONS.md`, section `## Inn Trouble - ASSEMBLED - FORMATTED_Italian`

- IT-D1. Title localisation — para 0
- IT-D2. 2 Omission (TOC) — para 20–28
- IT-D3. 7 Scene breaks — para 1181, 1191, 1244
- IT-D4. Key clue in English inside a `<bt>` span; `<bt>` on a bakery name — para 910, 651
- IT-D5. Italics added by translator — para 633
- IT-D6. 5 Dialogue punctuation — whole book
- IT-D7. 8 Units (round figures — ESCALATE) — para 185, 1121
- IT-D8. Adaptation (alphabetical 'B' index cards) — para 805, 812
- IT-D9. Adaptation (banner joke) — para 297
- IT-D10. 4 Proper names (reindeer) — para 396, 539–542, 661–694, 1139–1145
- IT-D11. 5 Register (Sam ↔ Jessica; Noriko ↔ Jessica) — ch8 (442–484) vs ch17 (752–774)
- IT-D12. 6 Term (the blackmail note) — whole book
- IT-D13. 6 Term (festival; forge) — whole book

## Refusals

None (0). Every fix matched its paragraph exactly and stayed inside one run's formatting.

## Quoted but not found

None.
