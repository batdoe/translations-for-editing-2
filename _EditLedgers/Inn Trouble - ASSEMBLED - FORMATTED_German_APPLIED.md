# APPLIED — Inn Trouble - ASSEMBLED - FORMATTED_German

## Verify (`python3 _tools/preflight.py --verify`)

```
VERIFY Inn Trouble - ASSEMBLED - FORMATTED_German
  PASS paragraphs: baseline=1248 now=1248
  PASS scene breaks: baseline=4 now=4
  PASS bt spans: baseline=15 now=15
  FAIL italic runs (content+order): baseline=22 now=22
      --- 
      +++ 
      @@ -1 +1 @@
      -Ich weiß, wie deine Familie zu diesem Gasthof gekommen ist. Ich weiß von der Brosche, die deine Urgroßmutter den Blackburns gestohlen hat, der mit dem Saphir im Herzen, und dem Geschäft in Ridgeline, wo sie sie verkaufte, um diesen Ort zu kaufen. Zahlt, oder die ganze Stadt erfährt die Wahrheit. Lass das Geld unter den Stufen des Haupteingangs zurück. Nimm die goldene Schleife vom Kranz ab und steck stattdessen eine rote an ihren Platz, damit ich weiß, dass das Geld da ist.
      +Ich weiß, wie deine Familie zu diesem Gasthof gekommen ist. Ich weiß von der Brosche, die deine Urgroßmutter den Blackburns gestohlen hat, der mit dem Saphir im Herzen, und dem Geschäft in Ridgeline, wo sie sie verkaufte, um diesen Ort zu kaufen. Zahl, oder die ganze Stadt erfährt die Wahrheit. Lass das Geld unter den Stufen des Haupteingangs zurück. Nimm die goldene Schleife vom Kranz ab und steck stattdessen eine rote an ihren Platz, damit ich weiß, dass das Geld da ist.
      @@ -8,2 +8,2 @@
      -Korrespondenz, Adelaide Blackburn an ihre Schwester, Winter 1924. Betr.: Der Diebstahl der Brosche der Familie (der Saphir im Herzen) durch eine Hausangestellte; das Stück später bei Ridgeline verpfändet. Von erheblichem ortsgeschichtlichem Interesse.
      -Das Fest endet Sonntag. Habt das Geld bis dahin bereit, oder die ganze Stadt liest am Montagmorgen von eurer Familie. Rote Schleife an den Kranz, wenn es erledigt ist. Seid diesbezüglich nicht dumm.
      +Korrespondenz, Adelaide Blackburn an ihre Schwester, Winter 1924. Betr.: Der Diebstahl der Brosche der Familie (der Saphir im Herzen) durch eine Hausangestellte; das Stück später in Ridgeline verpfändet. Von erheblichem ortsgeschichtlichem Interesse.
      +Das Fest endet Sonntag. Hab das Geld bis dahin bereit, oder die ganze Stadt liest am Montagmorgen von deiner Familie. Rote Schleife an den Kranz, wenn es erledigt ist. Sei diesbezüglich nicht dumm.
      @@ -11,3 +11,3 @@
      -Ich weiß, wie Ihre Familie zu diesem Gasthof gekommen ist
      -PROPERTY — EVERGREEN AVE — WINTER WONDERLAND INN.
      -the sapphire at its heart
      +Ich weiß, wie deine Familie zu diesem Gasthof gekommen ist
      +GRUNDBESITZ — EVERGREEN AVE — WINTER WONDERLAND INN.
      +der Saphir im Herzen
  INFO paragraphs changed vs baseline: 208
RESULT: FAIL (check that every difference is an intended, logged fix)
```

Paragraphs (1248), scene breaks (4) and bt spans (15) PASS. The italic-run 'FAIL' is expected: every difference is a deliberate fix of text inside an existing italic run (run count unchanged, 22 = 22, order unchanged):

- 111 (first blackmail note): 'Zahlt' → 'Zahl' (du register)
- 726 (catalog card): 'bei Ridgeline' → 'in Ridgeline'
- 785 (second note): 'Habt' → 'Hab', 'eurer' → 'deiner', 'Seid' → 'Sei' (du, as in the first note)
- 835 (quotation of the first note): 'Ihre Familie' → 'deine Familie'
- 851 (folder tab): 'PROPERTY' → 'GRUNDBESITZ'
- 953: 'the sapphire at its heart' → 'der Saphir im Herzen' (key clue left in English)

## Applied fixes (263)

| Para | Was | Now | Why |
|---|---|---|---|
| 28 | sowie den Saphir im Herzen der Brosche | sowie den Stein im Herzen der Brosche | EN blurb deliberately says 'names the stone at the brooch's heart'; German gives away 'Saphir' |
| 28 | die in genau einer verschlossenen Truhe auf Fionas Dachboden | die in genau einem verschlossenen Koffer auf Fionas Dachboden | the trunk = 'Koffer' throughout the book |
| 29 | Ein Hufschmied schuldete | Ein Schmied schuldete | EN 'A blacksmith'; Sam is a smith ('Schmied' throughout); 'Hufschmied' = farrier |
| 29 | Ein Schmied schuldete zwanzig Dollar und verweigerte eine klare Antwort. | Ein Schmied, dem man zwanzig Dollar schuldete und eine klare Antwort verweigerte. | reversed: EN 'A blacksmith owed twenty dollars and refused a straight answer' = Sam is owed the money and refused an answer (by Fiona); German had the smith owing and refusing |
| 37 | vier Zoll hoch | zehn Zentimeter hoch | SAFE unit rule: literal 'four inches' of snow -> 10 cm |
| 41 | „Sie dir nur dieses Band an“ | „Sieh dir nur dieses Band an“ | typo: imperative 'Sieh' (EN 'Look at that ribbon') |
| 49 | Das brachte ihr ein halbes Lächeln ab | Das rang ihr ein halbes Lächeln ab | idiom: 'jemandem etwas abringen'; 'abbringen' means to dissuade |
| 53 | ein Mann, der offenkundig noch nie im Leben auf seinen Zug hatte warten müssen | ein Mann, der offenkundig noch nie im Leben hatte warten müssen, bis er an der Reihe war | EN 'never had to wait his turn'; 'auf seinen Zug warten' reads as waiting for a train |
| 53 | an der Decke tanzten ließen | an der Decke tanzen ließen | typo: infinitive 'tanzen' |
| 60 | in dessen Knochenfalten | in dessen Knöchelfalten | EN 'creases of his knuckles'; 'Knochenfalten' (bone folds) is not a word |
| 60 | Mit zusammenbissener Kieferpartie | Mit zusammengebissener Kieferpartie | typo: past participle 'zusammengebissen' |
| 66 | nicht unkindlich | nicht unfreundlich | EN 'not unkindly'; 'unkindlich' = un-childlike (false friend) |
| 77 | Das ist verdammt viel Arbeit | Das ist sehr viel Arbeit | EN 'a great deal of work'; translator added a swear word |
| 79 | kaum einen Zoll von einer Glasbirne | kaum zwei Zentimeter von einer Glasbirne | SAFE unit rule: literal 'about an inch' -> 2 cm |
| 82 | spannten Männer Leitern und zogen Festbeleuchtung zwischen den Masten ein | spannten Männer auf Leitern die Festbeleuchtung zwischen den Laternenmasten | EN 'men on ladders were stringing the festival lights between the lampposts'; German said men were stretching ladders |
| 82 | barkte ein Hund | bellte ein Hund | 'barkte' is an anglicism, not German |
| 83 | flackerte die unterste Lichterkette | flackerte die nächstgelegene Lichterkette | EN 'the nearest string', not 'the lowest' |
| 97 | „Jessica?“, Fionas Stimme | „Jessica?“ Fionas Stimme | stray comma: no speech verb follows |
| 97 | wie eine Drahtseil | wie ein Drahtseil | gender: 'das Drahtseil' |
| 103 | Evergreen Street | Evergreen Avenue | place name is Evergreen Avenue everywhere else |
| 111 | Zahlt, oder die ganze Stadt | Zahl, oder die ganze Stadt | the note addresses Fiona as du throughout ('deine', 'Lass', 'Nimm'); 'Zahlt' is plural |
| 115 | ihr dunkles Haar in den Zwanzigern dicht am Kopf gewellt | ihr dunkles Haar im Stil der Zwanzigerjahre dicht am Kopf gewellt | EN 'in the style of the twenties'; German read as 'in her twenties' |
| 117 | „Constance hat sie all die Jahre behalten. | „Constance hat es all die Jahre behalten. | EN 'Constance kept it' = the photograph (das Foto, neuter) |
| 119 | die reichsten im Umkreis von fünfzig Meilen | die reichste im Umkreis von fünfzig Meilen | agreement: 'die reichste' (Familie); the miles figure is a separate decision |
| 122 | erbaut auf einen Diebstahl | erbaut auf einem Diebstahl | dative after 'erbaut auf' |
| 124 | hat je einem leiblichen Menschen ein Wort gesagt | hat je einer Menschenseele ein Wort gesagt | EN 'a living soul'; 'leiblicher Mensch' is not idiomatic |
| 124 | und ihre Augen waren roh | und ihre Augen waren wund | EN 'raw' (eyes); 'roh' = uncooked |
| 126 | Sie gestikulierte auf den Zettel | Sie deutete auf den Zettel | 'gestikulieren auf' is not German; EN 'gestured at' |
| 128 | konnte mir verdammt noch mal nicht ins Gedächtnis rufen | konnte mir beim besten Willen nicht ins Gedächtnis rufen | EN 'for the life of me'; translator added a swear |
| 140 | ich bin sehr starrschnäppig | ich bin sehr stur | 'starrschnäppig' is not a word; EN 'very stubborn' |
| 152 | den Flossen über den Augen | eine Flosse über den Augen | EN 'one flipper over her eyes'; 'den Flossen' is ungrammatical |
| 152 | das mit dem Geld gekaufte Gasthaus | den mit dem Geld gekauften Gasthof | the inn = 'Gasthof' throughout |
| 154 | genau wie damals, wenn sie eine Fährte | genau wie immer, wenn sie eine Fährte | EN 'as she did when' (habitual), not 'back then' |
| 160 | Sie ist sich sicher was den Koffer | Sie ist sich sicher, was den Koffer | missing comma |
| 160 | nicht von ihrer Seite durchsickert | nicht von ihrer Seite durchgesickert | past participle 'durchgesickert' |
| 162 | „Theos Archiv. Der Geschichtsverein.“ | „Theos Archiv. Der Historische Verein.“ | the Historical Society = 'Historischer Verein' (134, 144, 231 …) |
| 168 | für die Kindernachlesestunde samstags | für die Kindervorlesestunde samstags | EN 'children's reading hour'; 'Nachlese' = gleaning |
| 172 | Schulkinder auf Wandertag | Schulkinder beim Wandertag | missing article |
| 182 | und ich ließ es dabei bewogen sein | und ich ließ es dabei bewenden | garbled idiom 'es dabei bewenden lassen' |
| 186 | „What are you building out there?“ Ich brach ab. „Was baust du da draußen eigentlich?“ | „Was baust du da draußen eigentlich?“ | untranslated English line plus translator meta-text ('Ich brach ab') not in EN |
| 200 | jede einzelne Strähne, vom Grün bis zum Bahnhof | jede einzelne Kette, vom Anger bis zum Bahnhof | strand of lights = 'Kette' ('Strähne' = strand of hair); the green = 'Anger' throughout |
| 216 | Mit dem, what ever da draußen in der Werkstatt ist?“ Ich strich den Anglizismus. „Mit dem, was da draußen in der Werkstatt ist?“ | Mit dem, was da draußen in der Werkstatt ist?“ | English 'what ever' plus translator meta-text ('Ich strich den Anglizismus') left in the text |
| 218 | wenn die wahre Antwort ja lautet und er | wenn die wahre Antwort ja lautete und er | tense drift (past narration) |
| 245 | denn Neil hatte sich genau dorthin begeben, was ich sehen wollte | denn Neil hatte sich genau zu dem begeben, was ich sehen wollte | ungrammatical relative ('dorthin ..., was'); EN 'drifted toward the very thing I wanted to see' |
| 246 | ob die Stadt das nun weiß oder nicht.“ | ob die Stadt das nun weiß oder nicht. Sehen Sie hier.“ | omission: EN 'Look here.' |
| 249 | und ich hegte diesen Gedanken weiter | und ich merkte es mir | EN 'I filed it away'; 'hegte ... weiter' misreads it |
| 263 | noch einmal um einen Viertelzoll zurechtrückte | noch einmal um einen halben Zentimeter zurechtrückte | SAFE unit rule: literal 'a final quarter-inch' -> half a centimetre |
| 263 | mit ganzem, müden Herzen | mit ganzem, müdem Herzen | adjective declension (strong dative: müdem) |
| 264 | Das Papier war hier gewesen. | Das Papier war hier. | EN 'The paper was here' (still present) vs the letters that had been |
| 267 | Olivia saß natürlich mittenminder | Olivia saß natürlich mittendrin | typo/nonword 'mittenminder' |
| 270 | Sie waren bei den Festsocken, den Socken mit eingestricktem Namen | Sie waren bei den Festfäustlingen, den Fäustlingen mit eingestricktem Namen | EN 'festival mittens' — socks is wrong; mittens = 'Fäustlinge' elsewhere (326, 601) |
| 270 | damit nie eine Socke mit dem falschen Kind | damit nie ein Fäustling mit dem falschen Kind | mittens, not socks |
| 270 | Claire hielt eine halbefertige in der Farbe | Claire hielt einen halbfertigen in der Farbe | agreement with 'Fäustling' + typo 'halbefertige' |
| 270 | und drehte sie ins Licht | und drehte ihn ins Licht | pronoun follows the mittens fix ('der Fäustling') |
| 274 | „Du strickst wie eine Arbeiterin im Akkord.“ | „Du strickst wie eine, die nach Stunden bezahlt wird.“ | reversed meaning: EN 'paid by the hour' (slow); 'im Akkord' = piecework (fast) |
| 279 | Er sieht aus wie vom Winde verweht. | Er sieht aus wie durch den Wolf gedreht. | EN 'like something the cat dragged in'; 'vom Winde verweht' (Gone with the Wind) is the wrong idiom |
| 282 | Die Gesellschaft ist pleite, Jessica. | Der Verein ist pleite, Jessica. | the Historical Society = 'Verein' throughout |
| 288 | Wenn man das Geheimnis aus den Papieren kennt, weiß man, wo man suchen muss, hatte Nick gesagt. | Zu wissen, dass das Geheimnis aus den Papieren stammt, zeigt einem, wo man stehen muss, hatte Nick gesagt. | EN 'Knowing the secret came from the papers tells you where to stand' (echo of ch3); German said 'if you know the secret from the papers' |
| 288 | Sehr viele Leute in Frost Falls taten Theo leid. | Theo tat sehr vielen Leuten in Frost Falls leid. | reversed: EN 'A great many people were sorry for Theo' |
| 289 | über das Neujahr hinaus | über Neujahr hinaus | no article with 'Neujahr' |
| 292 | den Socken, dem neuen Baby | den Fäustlingen, dem neuen Baby | mittens, not socks |
| 292 | ob ein Schnee am ersten Oktober | ob ein erster Schnee im Oktober | EN 'an October first snow' = a first snowfall in October, not snow on 1 October |
| 299 | wieder ihrer Socke zu | wieder ihrem Fäustling zu | mittens, not socks |
| 306 | südlich des Evergreen-Viertels | südlich der Evergreen Avenue | EN 'south of Evergreen' = the avenue; there is no 'Evergreen district' |
| 311 | Marthas kleinen Hund geschnorgt | Marthas kleinen Hund geschnappt | nonword 'geschnorgt' |
| 316 | ob the penguin auch zum Fest kommt | ob der Pinguin auch zum Fest kommt | untranslated English 'the penguin' |
| 317 | Ermutigen Sie sie bloß nicht. | Ermutige sie bloß nicht. | Jessica addresses Mark with du everywhere else (321, 323, 1081) |
| 322 | „Es geht. Mittlerweile | „Es geht uns besser. Mittlerweile | EN 'We're better'; 'Es geht' = 'so-so' |
| 322 | Sie und dieser lässige Vogel | Sie und dieser lächerliche Vogel | EN 'that ridiculous bird'; 'lässig' = cool/casual |
| 340 | zwischen seinen Umzugskartons | zwischen seinen Kisten | EN 'among his boxes' (archive boxes); 'Umzugskartons' = moving boxes |
| 342 | Achten Sie nur darauf, dass sie nicht | Achte nur darauf, dass sie nicht | Jessica addresses eight-year-old Emma; adult-to-child is du (Emma's Sie to Jessica is correct) |
| 343 | meinen schamfreien, kürbisbäuchigen Vogel | meinen schamlosen, kürbisverschmierten Vogel | EN 'shameless, pumpkin-chinned'; 'kürbisbäuchig' = pumpkin-bellied; 'schamfrei' not idiomatic |
| 351 | Sie war nur anonymer Name an einer Wand | Sie war nur ein Name an einer Wand | missing article; 'anonymer' not in EN ('just a name on a wall') |
| 355 | Fionas Stimme wurde rauchig. | Fionas Stimme wurde belegt. | EN 'voice thickened' (with emotion); 'rauchig' = smoky |
| 357 | einer verschlossenen Truhe und einem Erpresserbrief | einem verschlossenen Koffer und einem Erpresserbrief | the trunk = 'Koffer' throughout (11x) |
| 362 | ebenso gut wie der Suppe bei ihr | ebenso gut wie ihr die Suppe | garbled comparison ('as the soup had done her') |
| 363 | und mir war verdammt klar geworden | und mir war um einiges klarer geworden | EN 'a good deal clearer'; translator-added swear |
| 367 | um ein paar Grade drehte | um ein paar Grad drehte | 'Grad' takes no plural -e as a measure |
| 372 | an einem Bogen cremefarbenem Papier haftete, welcher | an einem Bogen cremefarbenen Papiers haftete, der | case after 'Bogen' |
| 373 | „Sie haben das Gasthaus gemacht“ | „Sie haben den Gasthof gemacht“ | the inn = 'Gasthof' throughout |
| 374 | wie ein Kind, das sein Taschengeld bekommt | wie ein Kind, dem man sein Taschengeld schuldet | EN 'like a kid owed his allowance'; German said 'gets his allowance' |
| 378 | dass mir the Mann sympathisch war | dass mir der Mann sympathisch war | untranslated English 'the' |
| 380 | das weiß so gut wie jeder andere | das weiß ich so gut wie jeder andere | missing subject |
| 380 | beleidigt zu sein wie ein kleiner Mensch | beleidigt zu sein wie ein kleinlicher Mensch | EN 'like a small man' = petty, not short |
| 392 | auf eine Antwort zustehen | auf eine Antwort zusteuern | wrong verb ('zustehen' = be entitled to); EN 'walking straight at an answer' |
| 398 | mit der gequerten Sorgfalt | mit der leidgeprüften Sorgfalt | nonword 'gequert'; EN 'put-upon care' |
| 400 | „Einundneunzig. Die Blackburns | „Achtzehnhunderteinundneunzig. Die Blackburns | EN 'Eighteen ninety-one'; the century was dropped |
| 410 | reißt die Spur hier ab und wird zwei Orte weiter wieder ganz schwach | reißt die Spur hier ab und wird zwei Orte weiter wieder warm, wenn auch schwach | EN 'goes cold here and warm again, faint, two towns over'; German lost 'warm again' |
| 442 | und er stand nun völlig auf dem Schlauch vor lauter Aufregung | und er war nun in heller Aufregung | wrong idiom: 'auf dem Schlauch stehen' = to be slow on the uptake; EN 'at full fret' |
| 453 | Das tun sie schon immer, seit dem ersten Mal. | Das tun sie schon immer, seit dem allerersten Rentier. | EN 'since the first one' (the first reindeer) |
| 460 | denn sie ist noch nicht fertig, und ich weiß nicht, ob sie standhalten wird | denn er ist noch nicht fertig, und ich weiß nicht, ob er standhalten wird | pronoun: 'it' = the place he is building (der Ort), not the magic (sie) |
| 462 | am unteren Querholz des Koppels | am unteren Querholz der Koppel | 'die Koppel' is feminine |
| 462 | stieß einen einzigen, scharfen und sicheren Schrei aus | stieß einen einzigen, scharfen und sicheren Piepser aus | EN 'chirped'; Pip's chirp = 'Piepser/piepste' throughout, not a scream |
| 469 | Das Rathaus war ein schnörkelloser Backsteinbau | Das Rathaus war ein verschnörkelter Backsteinbau | reversed: EN 'a fussy brick building' (over-ornate); 'schnörkellos' = plain |
| 469 | stets vier Minuten nachging | stets vier Minuten vorging | reversed: EN 'run four minutes fast'; para 491 correctly says 'vorging' |
| 470 | saß der Bürgermeister höchstselbst | saß Bürgermeister Blackburn höchstselbst | EN 'Mayor Blackburn himself'; the name (the point of the paragraph) was dropped |
| 485 | She sah mich an | Sie sah mich an | untranslated English 'She' |
| 485 | sechs Fuß entfernt | knapp zwei Meter entfernt | SAFE unit rule: literal 'six feet away' -> about two metres |
| 488 | Sie schuften Sie hier auch viel zu hart. | Man lässt Sie hier auch viel zu hart schuften. | EN 'They work you far too hard'; German read 'You work you' |
| 497 | Der Vorstand des Geschichtsvereins | Der Vorstand des Historischen Vereins | the Historical Society = 'Historischer Verein' |
| 499 | In der Deckenfleck über dem Fenster | In der Deckenecke über dem Fenster | typo: EN 'In the corner of the ceiling' ('Deckenfleck' + wrong article) |
| 504 | bei einer Stiftung in der Stadt | bei einer Stiftung in der Großstadt | EN 'a foundation in the city' (a big city elsewhere), not this town |
| 508 | die Türen über das neue Jahr hinaus offen zu halten | die Türen bis zum neuen Jahr offen zu halten | EN 'keep the doors open through the new year' (= until then, cf. 503); 'darüber hinaus' = beyond |
| 514 | ganz aus Glas und hellem, greifbarem Licht | ganz aus Glas und hellem, hartem Licht | EN 'bright hard light'; 'greifbar' = tangible |
| 526 | die im Durchzug ein wenig hin und her wölbte | die sich im Durchzug ein wenig hin und her wölbte | reflexive 'sich wölben' |
| 534 | um halb sechs Uhr morgens Kniebeugen beizubringen | um halb sechs Uhr morgens Ausfallschritte beizubringen | EN 'lunges' = Ausfallschritte; Kniebeugen = squats |
| 534 | auf ehrliche, anstrengende, zentimetergenaue Weise aus seinem Loch zu klettern | auf ehrliche, anstrengende Weise Zentimeter für Zentimeter aus seinem Loch zu klettern | EN 'inch-by-inch'; 'zentimetergenau' = precise to the centimetre |
| 540 | Ich hätte Ihnen eine Blackburn von einer Brombeere nicht unterscheiden können. | Ich hätte einen Blackburn nicht von einer Brombeere unterscheiden können. | garbled syntax ('Ihnen' + misplaced 'nicht') |
| 540 | Vorsicht jetzt, vorsicht, | Vorsicht jetzt, Vorsicht, | noun capitalisation |
| 542 | Was auch immer der Erpresser in den Blackburn-Papieren, der Brosche, dem Stein, dem Pfandhaus gelesen hatte, | Was auch immer der Erpresser in den Blackburn-Papieren gelesen hatte – die Brosche, den Stein, das Pfandhaus –, | EN apposition (what he read = brooch, stone, pawnshop); German listed them as places read in |
| 552 | Er war rein. | Er war entlastet. | EN 'He was clear' (cleared of suspicion); 'rein' = pure/clean |
| 554 | durch die goldenerleuchtete Kälte | durch die golden erleuchtete Kälte | spelling (adverb + participle written apart) |
| 561 | grün und Rathaus und alles drum und dran | Anger und Rathaus und alles drum und dran | EN 'green and Town Hall' = the village green (Anger), not the colour |
| 571 | selbst aus dem Paddock gelassen | selbst aus der Koppel gelassen | paddock = 'Koppel' throughout |
| 571 | Nun stand sie knietief in verwehtem Laub | Nun stand sie knöcheltief in verwehtem Laub | EN 'ankle-deep' |
| 585 | den Weg hinauf in Richtung Hütte und der Werkstatt dahinter | den Weg hinauf in Richtung unseres Häuschens und der Werkstatt dahinter | the cottage = 'Häuschen' throughout; 'Hütte' = hut |
| 589 | genau wie das Licht | genau wie die Lichter | EN 'same as the lights' (the festival lights) |
| 595 | Ich ging den Hufabdrücken eines Reentiers nach nach Hause | Ich ging den Hufabdrücken eines Rentiers nach nach Hause | typo 'Reentiers' |
| 595 | sie zog zu einer Feuerstelle hin | sie zog zu einer Herdstelle hin | hearth = 'Herdstelle' (ch10, Nick's explanation) |
| 595 | zu einer Feuerstelle nach Hause wanderte | zu einer Herdstelle nach Hause wanderte | hearth = 'Herdstelle' (ch10) |
| 607 | dass das Historische Museum schließt | dass der Historische Verein schließt | the Historical Society = 'Historischer Verein'; it is not a museum |
| 611 | „Apropos Museum“ | „Apropos Verein“ | the Historical Society = 'Verein' |
| 621 | „Hast du seine Visitenkarte?“ fragte sie. | „Hast du seine Visitenkarte?“, fragte sie. | comma after closing quote before speech tag |
| 630 | Auf den letzten Nadeln meines Bündchens stand MAXIMILIAN | Auf dem letzten Bündchen auf meinen Nadeln stand MAXIMILIAN | EN 'The last cuff on my needles read'; German garbled it to 'the last needles of my cuff' |
| 643 | Sein ganzes Geschichtsstipendium beruhte auf dem Motto | Seine ganze Geschichtsgelehrsamkeit beruhte auf dem Motto | EN 'history scholarship' = learning (ironic); 'Stipendium' = a grant |
| 655 | fast bis vor Contances Haustür | fast bis vor Constances Haustür | name typo |
| 665 | Und die nächste stattdessen nur einen weiteren Stein hineinsetzen. | Und die nächste setzt stattdessen nur einen weiteren Stein hinein. | verbless fragment; EN 'the next fact keeps setting another stone in it' |
| 667 | einen sehr kurzen Kreis von Leuten | einen sehr kleinen Kreis von Leuten | 'kurzer Kreis' is not German (EN 'a very short list') |
| 671 | dass sie beide ganz sicher verschwunden sind | dass sie beide ganz sicher vom Tisch sind | EN 'gone for certain, cleared'; 'verschwunden' = vanished (they are people) |
| 681 | „Können wir eine Minute lang gehen? | „Können wir kurz ein paar Schritte gehen? | EN 'Can we walk a minute?'; literal 'eine Minute lang gehen' is not idiomatic |
| 683 | Dass sie Angst hatte, Sam, nicht kalt. Niemals kalt. | Dass sie Angst hatte, Sam, nicht abweisend war. Niemals abweisend. | EN 'frightened, not cold' (= unfriendly); German 'kalt' reads as 'not freezing' |
| 690 | prägen Sie sich mir das Gesicht ein | prägen Sie sich für mich das Gesicht ein | EN 'remember their face for me'; 'sich mir einprägen' is ungrammatical here |
| 691 | eisenbergig und warm | eisenrau und warm | nonword 'eisenbergig'; EN 'iron-rough' |
| 696 | „Echtes Kaliber“ | „Echte Kanzlei“ | EN 'Real firm' (the law firm on the card is real) |
| 696 | macht genau das, was dein Mann sagt: | macht genau das, was er behauptet: | EN 'your man' = Neil Carter; 'dein Mann' reads as 'your husband' (Nick) |
| 696 | ist diesen Frühling in der Stadt gestorben | ist diesen Frühling in der Großstadt gestorben | EN 'down in the city' (a big city), not this town |
| 702 | der sein halbes Leben lang kalten, hundert Jahre alten Papierstapeln hinterhergejagt ist | der sein ganzes Berufsleben lang einer kalten, hundert Jahre alten Papierspur hinterhergejagt ist | EN 'spent his whole career chasing a cold hundred-year-old paper trail'; the next clause continues 'die Spur' |
| 703 | Da presst jemand den Nachfahren aus. | Da presst jemand die Nachfahrin aus. | Fiona is female ('the descendant') |
| 711 | Jedes verdammte Mal. | Jedes Mal. | EN 'Every time.'; translator-added swear |
| 718 | Er empfand mich dort aschfahl und dankbar | Er empfing mich dort aschfahl und dankbar | typo: 'empfing' (met), not 'empfand' (felt) |
| 722 | wie es sich für einen guten Archivar gehrte | wie es sich für einen guten Archivar gehörte | typo 'gehrte' |
| 726 | das Stück später bei Ridgeline verpfändet | das Stück später in Ridgeline verpfändet | EN 'pawned at Ridgeline' (in the town); 'bei' = near |
| 736 | als hätte sich der Boden des Raumes gerade unauffällig unter meinem Stuhl geöffnet | als hätte sich der Boden des Raumes nicht gerade unauffällig unter meinem Stuhl geöffnet | reversed: EN 'as though the floor of the room had not just opened quietly under my chair' |
| 748 | Ich weiß, dass jeder, der diesen Zettel geschrieben hat, | Ich weiß, dass derjenige, der diesen Zettel geschrieben hat, | EN 'whoever wrote that note' (one person); 'jeder' = everyone who |
| 752 | und ließ es mir trotzdem durchgehen | und gab es mir trotzdem mit | EN 'he let me have it anyway' (gave me the thought); 'durchgehen lassen' = let something slide |
| 756 | von draußen hinter dem Koppel her | von draußen hinter der Koppel her | 'die Koppel' is feminine |
| 762 | während das Gold mit jedem Schritt heller aufspritzte | während das Gold mit jedem Schritt heller hervorquoll | EN 'the gold spilling brighter'; 'aufspritzen' = splash up |
| 764 | wo früher der alte Herdstock gestanden hätte | wo der alte Herd am Pol gestanden hätte | nonword 'Herdstock'; omission of 'of the Pole' |
| 766 | „Ein Kamin“, sagte ich | „Eine Herdstelle“, sagte ich | EN 'A hearth' — the reveal echoes Nick's 'A hearth' = 'Eine Herdstelle' in ch10 (460) |
| 768 | „Ein Kamin.“ Sein Arm legte sich um mich. „Er ist noch nicht fertig. Er kann es noch nicht halten | „Eine Herdstelle.“ Sein Arm legte sich um mich. „Sie ist noch nicht fertig. Sie kann es noch nicht halten | hearth = 'Herdstelle' (ch10); pronouns follow |
| 768 | Das sind jahrelange Arbeit | Das ist jahrelange Arbeit | verb agreement |
| 770 | im Schein des unbefeuerten Feuers | im Schein des unentzündeten Feuers | EN 'unlit fire'; 'unbefeuert' is not idiomatic |
| 778 | als ich die Evergreen Street herunterkam | als ich die Evergreen Avenue herunterkam | place name is Evergreen Avenue |
| 785 | Habt das Geld bis dahin bereit | Hab das Geld bis dahin bereit | second note must address Fiona with du like the first note (111: 'deine Familie', 'Lass', 'Nimm') |
| 785 | von eurer Familie | von deiner Familie | du register, as in the first note |
| 785 | Seid diesbezüglich nicht dumm. | Sei diesbezüglich nicht dumm. | du register, as in the first note |
| 788 | etwas beliehen | etwas beleihen | infinitive 'beleihen' (parallel to 'verkaufen') |
| 790 | nur eine Frage des Wie und des Alleinseins war | nur eine Frage des Wie und des Ob-allein war | EN 'how and whether-alone' (whether he acted alone); 'Alleinsein' = loneliness |
| 796 | Das klärte das Ortliche ohne jeden Zweifel | Das klärte das Wo ohne jeden Zweifel | EN 'the where of it'; 'das Ortliche' is not a word |
| 797 | Er konnte Frost Falls nicht durchqueren | Er konnte in Frost Falls keinen Raum durchqueren | EN 'He could not cross a room in Frost Falls' |
| 801 | I ging hinaus in die Kälte | Ich ging hinaus in die Kälte | untranslated English 'I' |
| 805 | als ihr ureigenerstes Recht | als ihr ureigenstes Recht | typo 'ureigenerstes' |
| 805 | Sie lehnte jedes Stück Mürbeteig | Sie lehnte jedes Stück Mürbegebäck | EN 'shortbread' (baked); 'Mürbeteig' = raw shortcrust dough |
| 807 | so wie ich es ihn gebeten hatte | worum ich ihn gebeten hatte | ungrammatical ('jemanden um etwas bitten') |
| 808 | hielt ich ebenfalls Wächterei | hielt ich ebenfalls Wache | nonword 'Wächterei' |
| 815 | „Heute nicht“, sagte sie. | „Heute nicht“, sagte ich. | EN 'I said' — Jessica answers Noriko |
| 818 | an den Innenseiten der Gasthöfchenster | an den Innenseiten der Gasthoffenster | typo 'Gasthöfchenster' |
| 827 | mit der Wahrheit zurückgelassen, vor der ich sie als Schutzschild benutzt hatte | mit der Wahrheit zurückgelassen, der ich mit ihrer Hilfe ausgewichen war | EN 'the truth I'd been using them to avoid'; German relative clause was garbled |
| 828 | ohne zusammenzucken | ohne zusammenzuzucken | 'ohne ... zu' infinitive |
| 829 | auf dem cremefarbenen Briefpapier der Gesellschaft geschrieben | auf dem cremefarbenen Briefpapier des Vereins geschrieben | the Society = 'Verein' throughout |
| 831 | einen Bogen des Briefpapiers der Gesellschaft | einen Bogen des Briefpapiers des Vereins | the Society = 'Verein' |
| 832 | über eine sterbende Gesellschaft | über einen sterbenden Verein | the Society = 'Verein' |
| 835 | Ich weiß, wie Ihre Familie zu diesem Gasthof gekommen ist | Ich weiß, wie deine Familie zu diesem Gasthof gekommen ist | quotes the first note, which reads 'deine Familie' (111, du) |
| 836 | in einer Wand von Aktenordnern | in einer Wand von Aktenschubladen | EN 'a wall of filing drawers' (cf. 'Schubladen' 840) |
| 847 | die alte Urkunde für das Anger | die alte Urkunde für den Anger | 'der Anger' is masculine |
| 851 | PROPERTY — EVERGREEN AVE | GRUNDBESITZ — EVERGREEN AVE | English archive label left untranslated; the drawer cards in ch11 (479) are translated |
| 855 | lange genug her, dass sie sie nicht weggeräumt hatte | vor so kurzer Zeit, dass sie sie noch nicht weggeräumt hatte | reversed: EN 'lately enough that she hadn't put it away' |
| 867 | Theo hatte den Diebstahl begangen. | Theo wusste vom Diebstahl. | EN 'Theo had the theft' = held that half of the secret; German says Theo committed the 1924 theft |
| 867 | an einem belebten Festtag hellen Tages auf einen vollen Schreibtisch legen | am helllichten Festtag auf einen vollen Schreibtisch legen | garbled phrase; EN 'in broad festival daylight' |
| 867 | sich nicht unbemerkt die Evergreen Avenue entlangwagen, um sein Leben zu retten | sich nicht unbemerkt die Evergreen Avenue entlangwagen, und wenn sein Leben davon abhinge | EN idiom 'to save his life' rendered literally (reads as a purpose clause) |
| 884 | Theo würde seine Gesellschaft und seinen guten Ruf behalten | Theo würde seinen Verein und seinen guten Ruf behalten | the Society = 'Verein' |
| 902 | das alles weiflüstern | das alles wegflüstern | typo 'weiflüstern' |
| 902 | Und der Schmutz bleibt unten in der Wand, wo ich ihn nicht sehen kann, und wächst. | Und die Fäulnis bleibt unten in der Wand, wo ich sie nicht sehen kann, und wächst. | EN 'the rot stays down inside the wall ... growing'; 'Schmutz' = dirt (does not grow) |
| 906 | auf denselben Gehältern laufen lernten | auf denselben Gehwegen laufen lernten | typo/wrong word: 'Gehältern' = salaries; EN 'sidewalks' |
| 919 | Chief Tanaka hörte sich die Sache | Polizeichefin Tanaka hörte sich die Sache | English title 'Chief' left untranslated (she is 'die Polizeichefin' elsewhere, 325/927) |
| 919 | Das Briefpapier der Gesellschaft | Das Briefpapier des Vereins | the Society = 'Verein' |
| 924 | Hier ist, what ich tun werde. | Hier ist, was ich tun werde. | untranslated English 'what' |
| 924 | Wir nennen das restorative Gerechtigkeit. | Wir nennen das restaurative Gerechtigkeit. | the German term is 'restaurative Gerechtigkeit' |
| 925 | „Genau das habe ich gehofft, dass du es sagen würdest.“ | „Genau das hatte ich gehofft, von dir zu hören.“ | ungrammatical construction |
| 927 | einem anständig gebliebenen Mann, der vom Weg abgekommen ist | einem guten Mann, der vom Weg abgekommen war | EN 'a good man gone wrong'; 'anständig geblieben' (stayed decent) contradicts it |
| 931 | dem goldenen Pendel | dem Messingpendel | EN 'the brass pendulum' |
| 937 | die Menschenmassen nach Hause gegangen und das Aufräumen noch nicht begonnen hatte | die Menschenmassen nach Hause gegangen waren und das Aufräumen noch nicht begonnen hatte | auxiliary: 'gegangen waren' |
| 941 | eine Angelegenheit der Gesellschaft genannt hatte | eine Angelegenheit des Vereins genannt hatte | the Society = 'Verein' |
| 953 | auf dem Briefpapier der Gesellschaft geschrieben | auf dem Briefpapier des Vereins geschrieben | the Society = 'Verein' |
| 953 | the sapphire at its heart | der Saphir im Herzen | KEY CLUE left in English in Jessica's accusation; rendered with the edition's dominant form (111, 112, 129, 728, 730); see decision on the five-word phrasing |
| 953 | die Gesellschaft mit diesen Briefen zu retten | den Verein mit diesen Briefen zu retten | the Society = 'Verein' |
| 957 | das Gasthaus sei sowieso mit gestohlenem Geld gekauft worden | der Gasthof sei sowieso mit gestohlenem Geld gekauft worden | the inn = 'Gasthof' |
| 963 | „Vera“, sagte ich. „Theo hat den Diebstahl begangen. | „Vera“, sagte ich. „Theo wusste vom Diebstahl. | EN 'Theo had the theft' (knew that half); German accuses Theo of the 1924 theft |
| 963 | Aber in den Notizen stand, dass das Gasthaus mit dem Geld | Aber in den Zetteln stand, dass der Gasthof mit dem Geld | notes = 'Zettel' throughout ('Notizen' = jottings); inn = 'Gasthof' |
| 963 | die Urkunde für dieses Gasthaus | die Urkunde für diesen Gasthof | the inn = 'Gasthof' |
| 963 | griffbereit auf dem Schreibtisch | kürzlich angefasst auf dem Schreibtisch | EN 'handled' (recently touched), not 'within reach' |
| 963 | „Er beging den Diebstahl. Du hattest die Urkunde. | „Er wusste vom Diebstahl. Du hattest die Urkunde. | EN 'He had the theft. You had the deed.' |
| 963 | im Gasthaus vorbeischaut | im Gasthof vorbeischaut | the inn = 'Gasthof' |
| 967 | erzählte von der Gesellschaft | erzählte von dem Verein | the Society = 'Verein' |
| 967 | dass es die Gesellschaft retten würde | dass es den Verein retten würde | the Society = 'Verein' |
| 978 | versucht hatten, einen Dritten um eine halbe Million | versucht hatten, eine Dritte um eine halbe Million | the third citizen is Fiona (female) |
| 982 | „Restorative Justice“, erklärte sie | „Restaurative Gerechtigkeit“, erklärte sie | English term; 924 already uses the German term |
| 986 | und es kostete sie verdammt viel | und es kostete sie sehr viel | EN 'cost her badly'; translator-added swear |
| 988 | denn die Gesellschaft war sein ganzer Lebensinhalt gewesen, und die Gesellschaft war das Einzige | denn der Verein war sein ganzer Lebensinhalt gewesen, und der Verein war das Einzige | the Society = 'Verein' |
| 990 | Er trat als Leiter der Frost Falls Historical Society zurück | Er trat als Leiter des Historischen Vereins von Frost Falls zurück | English institution name left untranslated (231: 'Der Historische Verein von Frost Falls') |
| 990 | des Briefpapiers der Gesellschaft | des Briefpapiers des Vereins | the Society = 'Verein' |
| 992 | Aber sie verwarfen ihn nicht völlig. | Aber sie verstießen ihn nicht. | EN 'they did not cast him out'; 'verwerfen' = reject (an idea) |
| 992 | Er durfte bei der Gesellschaft ehrenamtlich mitarbeiten. | Er durfte beim Verein ehrenamtlich mitarbeiten. | the Society = 'Verein' |
| 992 | Ohne Vertrauen in die Schlüssel. | Ohne dass man ihm die Schlüssel anvertraute. | EN 'Not trusted with the keys'; German said he had no trust in the keys |
| 992 | Zoll für Zoll den Platz zurückzuverdienen | Zentimeter für Zentimeter den Platz zurückzuverdienen | idiom 'an inch at a time': imperial 'Zoll' reads foreign; matches the same phrase at 906 |
| 1000 | der oben aus dem Karton herausliff | der oben aus dem Karton herauslugte | nonword 'herausliff'; EN 'poking out of the top' |
| 1004 | diese steife,geknöpfte Frau | diese steife, zugeknöpfte Frau | missing space; EN 'buttoned' = 'zugeknöpft' (cf. 507) |
| 1006 | und begannen – gerade erst zu beginnen –, den langen Marsch | und begannen – gerade erst –, den langen Marsch | garbled insertion ('only just beginning') |
| 1008 | die Sache mit der Gesellschaft selbst | die Sache mit dem Verein selbst | the Society = 'Verein' |
| 1015 | in arigen finanziellen Nöten | in argen finanziellen Nöten | typo 'arigen' |
| 1021 | Gefallen an den Quilts findet | Gefallen an den Steppdecken findet | the quilts = 'Steppdecken' (ch1, 54/57); callback to Mrs. Worthington's question |
| 1034 | kam sie zu mir in die Hütte, Nials Ordner | kam sie zu mir ins Häuschen, Neils Ordner | name typo 'Nials' (Neil); the cottage = 'Häuschen' throughout, 'Hütte' = hut |
| 1037 | für den Gazette schreiben, zusammen mit Nials Dokumenten | für die Gazette schreiben, zusammen mit Neils Dokumenten | 'die Gazette' everywhere else; name typo 'Nials' |
| 1038 | weil die Wahrheit sich als gut erwies | weil die Wahrheit sich als gütig erwies | EN 'the truth turned out to be kind' (echoes 'Claire was kind') |
| 1040 | das diesen Ort seither seit hundert Jahren warmgehalten hat | das diesen Ort seither hundert Jahre lang warmgehalten hat | doubled 'seither seit' |
| 1044 | zog drüben auf lauter Evergreen Avenue respektvoll den Hut | zog quer über die Evergreen Avenue hinweg respektvoll den Hut | garbled 'auf lauter'; EN 'clear across Evergreen Avenue' |
| 1044 | ich hätte die Sache besser gehandelt | ich hätte die Sache besser gehandhabt | anglicism 'gehandelt' (= traded/acted); 'handhaben' = handle |
| 1045 | wenn du es brauchst | wenn du es brauchtest | tense (past) |
| 1046 | der noch nicht richtig eingenäht war | der noch nicht richtig eingetragen war | EN 'not broken in yet'; 'eingenäht' = sewn in; next sentence uses 'eingetragen' |
| 1046 | in ihrer langsamen, verschmitzten Art | in ihrer langsamen, verhaltenen Art | EN 'slow sideways way'; 'verschmitzt' = mischievous |
| 1050 | Die Gesellschaft brauchte nach Theo | Der Verein brauchte nach Theo | the Society = 'Verein' |
| 1054 | der Anger ist vier Hektar groß | der Anger ist anderthalb Hektar groß | EN 'four acres' = about 1.6 ha; the translation swapped acres for hectares (2.5x too large). SAFE arithmetic conversion |
| 1055 | stand die halbe Frost Falls | stand das halbe Frost Falls | town names are neuter |
| 1056 | das in der kalten Luft hinhängte | das in der kalten Luft hängen blieb | nonword 'hinhängte'; EN 'hung in the cold air' |
| 1057 | genau dorthin, wo eine Hand sie | genau dort, wo eine Hand sie | location, not direction |
| 1060 | Er sollte dabeisein | Er sollte dabei sein | spelling |
| 1063 | kam Bram über den Anger herbeigeeilt und wring seine Mütze aus | kam Bram über den Anger herbeigeeilt, die Mütze in den Händen ringend | EN 'wringing his cap' (as in 442); 'wring ... aus' is a wrong verb form and means wringing out laundry |
| 1063 | sich schon wieder aus dem Paddock gelassen | sich schon wieder aus der Koppel gelassen | paddock = 'Koppel' throughout |
| 1064 | „Das Schloss, Mrs. Claus!“ | „Der Riegel, Mrs. Claus!“ | the latch = 'Riegel' (ch10, 442–451) |
| 1066 | Hinter dem Paddock lag die Feuerstelle | Hinter der Koppel lag die Herdstelle | paddock = 'Koppel'; hearth = 'Herdstelle' |
| 1067 | hinauf zur Gesellschaft | hinauf zum Verein | the Society = 'Verein' |
| 1067 | die eine vor hundert Jahren untergegangene Stadt es wert gefunden hatte, für uns aufzuheben | die die Stadt vor hundert Jahren für wert befunden hatte, für uns aufzuheben | EN 'a town a hundred years gone' (the town of a century ago); 'untergegangen' = perished |
| 1067 | die Türen der Gesellschaft | die Türen des Vereins | the Society = 'Verein' |
| 1071 | das Gras gemäht | der Anger gefegt | EN 'the green swept'; nobody mows grass in November |
| 1073 | wenn sie ihn öffneten, schließlich sei sie direkt dagewesen, als er aus der Erde geholt worden war | wenn man die Kiste öffnete, schließlich sei sie direkt dabei gewesen, als sie aus der Erde geholt worden war | pronouns: 'it' = the copper box (die Kiste), not the treasure |
| 1087 | „Warte“, sagte sie. „Geh noch nicht.“ | „Warten Sie“, sagte sie. „Gehen Sie noch nicht.“ | Emma addresses Jessica with Sie everywhere else (307, 331, 334, 336) |
| 1091 | Dad glaubt, ich hätte ihn | Papa glaubt, ich hätte ihn | English 'Dad' left in German dialogue |
| 1105 | Ich beschvähre mich nicht. | Ich beschwere mich nicht. | typo 'beschvähre' |
| 1111 | Der Herd, den er gebaut hatte, glühte | Die Herdstelle, die er gebaut hatte, glühte | hearth = 'Herdstelle' (ch10, ch19) |
| 1115 | bis ein Herd groß genug gebaut ist | bis eine Herdstelle groß genug gebaut ist | hearth = 'Herdstelle' |
| 1125 | Pip schlug uns beide an der Küchentür | Pip war vor uns beiden an der Küchentür | EN 'beat us both to the kitchen door'; 'schlug uns' = hit us |
| 1125 | glühte der Herd in der Werkstatt weiter | glühte die Herdstelle in der Werkstatt weiter | hearth = 'Herdstelle' |
| 1167 | das Haus hüttete oder Enkelkinder hütete | das Bett hütete oder Enkelkinder hütete | typo 'hüttete'; idiom 'das Bett hüten' (laid up) |
| 1183 | in der Größe einer Hutfuhr | in der Größe einer Hutschachtel | nonword 'Hutfuhr'; EN 'hatbox' |
| 1191 | richtete rechtfertigend einen mehligen Finger | richtete triumphierend einen mehligen Finger | EN 'in vindication' (proved right), not 'justifying herself' |
| 1199 | die kleinen Neuigkeiten eines ganzen Vormorgens | die kleinen Neuigkeiten eines ganzen Vormittags | nonword 'Vormorgens' |
| 1199 | und ich sagte, ich solle das Kind grüßen | und ich sagte, sie solle das Kind von mir grüßen | EN 'I said give the child my love'; German reversed who greets whom |
| 1205 | It was the kind of gap in a row of shops people learn not to look at, so as not to feel the little pang of it.  | Es war die Art Lücke in einer Ladenzeile, bei der die Leute lernen wegzusehen, um den kleinen Stich nicht zu spüren.  | untranslated English sentence |
| 1211 | sagte Ivy with satisfaction | sagte Ivy zufrieden | untranslated English 'with satisfaction' |
| 1225 | das klobige Kohlegesicht von den Geschäften weg den Anger hinauf gerichtet | das klobige Kohlegesicht den Anger hinauf zu den Geschäften gerichtet | reversed: EN 'pointed away up the green toward the shops' |
| 1237 | keines Spassvogels | keines Spaßvogels | spelling (ß) |
| 1239 | einen Herd, in dem sie sich niederlassen konnte | eine Herdstelle, in der sie sich niederlassen konnte | hearth = 'Herdstelle' |
| 1243 | den ganzen Vormund über | den ganzen Vormittag über | wrong word 'Vormund' (guardian); EN 'all morning' |

## Decisions logged (15)

- DE-D1 7 Scene breaks (para 455, 1127, 1143, 1245): Delete all four at the formatting stage (455 especially, as it splits a continuous scene); the other three may be replaced by plain spacing.
- DE-D2 2 Omission (TOC) (para 22): Regenerate the TOC in the formatter once the 35 Heading 1 styles are restored.
- DE-D3 `<bt>` spans on things that are not book titles (para 38, 40, 561, 1149, 1167, 1183, 1221): Drop the markers on the 7 non-titles, keep the text; at 561 also drop the English article: 'auf dem Tresen der Holly Jolly Bakery'.
- DE-D4 6 Term / adaptation (KEY CLUE, word count) (para 28, 111, 112, 129, 726, 728, 730, 744, 829, 867, 953): Option A (recommended): unify on the five-word 'der Saphir in ihrem Herzen' (ihrem = der Brosche) at 111, 112, 129 ×2, 726, 728, 730, 829, 867, 953 — keeps 'fünf Wörter' true and fixes 829's wrong 'seinem'. Option B: keep 'der Saphir im Herzen' everywhere (fix 829, 867) and change 'fünf' → 'vier' at 730 ×2, 744, 829.
- DE-D5 1 Untranslated / 6 Term (honorifics) (para Mr./Mrs. ×56 vs Herr/Frau ×9 (503, 504, 604, 606, 804, 807, 809 ×2)): Keep Mr./Mrs. throughout and normalise the nine Frau/Herr instances (Frau Pelletier → Mrs. Pelletier, Frau Claus → Mrs. Claus, Herr(n) Kim(s) → Mr. Kim(s)). Alternative: Herr/Frau throughout (65 edits; 'Frau Claus' loses the Santa association).
- DE-D6 4 Proper name (the dog) (para 312, 319, 321, 818, 1056 vs 1073, 1081, 1085, 1087, 1095, 1167, 1199): 'Snowball' throughout (series rule: character names stay English; matches NO-D10).
- DE-D7 6 Term (the circle) (para 94, 267, 269, 270, 294, 296, 303, 306, 469, 479, 485, 601, 804, 906, 908, 1039, 1045 …): 'Strickkreis' at first mention in a scene, 'Kreis' thereafter; replace Handarbeitskreis/Strickrunde/Zirkel; make 296 read 'Genau das ist der Sinn eines Kreises' so the echoes at 908/1045 match.
- DE-D8 5 Register (Jessica → Vera) (para 488 vs 859, 1002): Sie throughout (fix 859 and the whole 1002 speech), mirroring Vera's Sie; alternatively du from ch23 on if Lisa reads ch27 as a deliberate softening.
- DE-D9 5 Register (Noriko ↔ Jessica) (para 326, 328 vs 811–817, 921–925): du throughout (change 326 'Ihre' → 'deine', 328 'Sagen Sie' → 'Sag'); or keep ch6 Sie if Lisa wants the first meeting formal.
- DE-D10 8 Units (round figure — ESCALATE) (para 119): 'die reichste im Umkreis von achtzig Kilometern' or idiomatic 'die reichste weit und breit'. (The 'reichsten' → 'reichste' grammar fix was applied.)
- DE-D11 Adaptation (banner joke) (para 231): Change 'das letzte S' → 'das letzte E' (simplest), or keep the banner in English as an in-world sign so the S joke works.
- DE-D12 Adaptation (alphabetical catalog cards) (para 722, 736): 722: 'Bäckereiquittungen, Blaskapellen-Pavillon: Beiträge'; 736: 'B, B, Bridge-Turnier, Banner und Wimpel, Überschuss'.
- DE-D13 Italics added by translator (para 797, 953): Remove the italic at 797; at 953 either remove it or keep it as quotation marking (if kept, consider „…“ instead).
- DE-D14 3 Mistranslation (plant) (para 40): 'samt einem einzelnen Zweig Baumwürger für das herbstliche Orange' or plainer 'samt einem einzelnen Zweig mit orangefarbenen Beeren für das herbstliche Orange'.
- DE-D15 6 Term (minor variants) (para lobby 44–834; inn 293, 382, 651, 659, 708; cider 231–813): Lobby → 'Lobby' throughout (or 'Foyer'); 'Gasthof' for the inn except in the proper name; cider → 'heißer Apfelsaft' / 'Apfelpunsch'.

## Refusals

None outstanding. One first attempt was refused by the Fixer (851: `old` crossed from the roman run into the italic folder-tab run); it was re-applied as a fix on the italic run only and succeeded.

## Quoted text not found

None.
