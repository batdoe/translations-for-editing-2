# APPLIED — Inn Trouble - ASSEMBLED - FORMATTED_German (2026-10-27)

- Backup: `translated\corrected\_bak\Inn Trouble - ASSEMBLED - FORMATTED_German.pre-proofread2-20261027.docx`
- Method: run-level edits on <w:t> nodes only (lxml); paragraph text verified against a full snapshot before editing; minimal-diff splice; whole-paragraph post-check after every edit. No run collapse; italic run count 22 -> 22.
- Applied: 144 text edits + glyph conversion in 386 paragraphs. Refused by verification: 0. Report quotes not found: 0.
- Counts by class: address 31, bt 7, cider 11, clue 9, grammar 6, honorific 8, mistranslation 13, name 5, note-word 15, sign 3, term 35, units 1
- Italic text changed (translation inside existing italic runs, intended): ch2 note (clue wording), ch4 exhibit card ('Dem Volk' -> 'Den Menschen'), Theo's ch19 catalogue card (clue), ch20 recalled line (Eingangshalle -> Lobby), ch26 confrontation clue phrase. preflight --verify therefore reports 'italic sequence DIFFERS' and 'bt -7' — both declared.

| Para | Was | Now | Why |
|---|---|---|---|
| 28 | `<bt>Yarn Tales</bt>` | `Yarn Tales` | stray <bt> on a non-title (ruling 5) |
| 30 | `<bt>Winter Wonderland Inn</bt>` | `Winter Wonderland Inn` | stray <bt> on a non-title (ruling 5) |
| 860 | `<bt>Yarn Tales</bt>` | `Yarn Tales` | stray <bt> on a non-title (ruling 5) |
| 896 | `<bt>Yarn Tales</bt>` | `Yarn Tales` | stray <bt> on a non-title (ruling 5) |
| 869 | `<bt>Gazette</bt>` | `Gazette` | stray <bt> on a non-title (ruling 5) |
| 877 | `<bt>Holly Jolly Bakery</bt>` | `Holly Jolly Bakery` | stray <bt> on a non-title (ruling 5) |
| 459 | `der <bt>The Holly Jolly Bakery</bt> bereit` | `der Holly Jolly Bakery bereit` | stray <bt> + English article 'The' after German 'der' (ruling 5) |
| 30 | `samt einem einzelnen Zweig Stechpalmenbeeren für das herbstliche Orange` | `samt einem einzelnen Zweig Baumwürger für das herbstliche Orange` | EN 'bittersweet' (orange-berried Celastrus = Baumwürger), not holly; holly pre-empted the ch6 holly miracle |
| 84 | `sich der Handarbeitskreis traf` | `sich der Strickkreis traf` | knitting circle = Strickkreis/Kreis (German Book 1 form) |
| 96 | `in das kleine Lesezimmer abseits der Lobby` | `in das kleine Wohnzimmer abseits der Lobby` | Fiona's 'little sitting room' had 3 names (Lesezimmer/Empfangszimmer/Wohnzimmer); unified to Wohnzimmer |
| 101 | `die deine Urgroßmutter den Blackburns gestohlen hat, der mit dem Saphir im Herzen, und dem Geschäft in Ridgeline` | `die deine Urgroßmutter den Blackburns gestohlen hat – der Saphir in ihrem Herzen –, und von dem Geschäft in Ridgeline` | KEY CLUE: identical 5-word wording 'der Saphir in ihrem Herzen' in note/reading/card/confrontation |
| 102 | `Der Saphir im Herzen.` | `Der Saphir in ihrem Herzen.` | KEY CLUE identical wording |
| 119 | `Der Saphir im Herzen, genau diese Worte.` | `Der Saphir in ihrem Herzen, genau diese Worte.` | KEY CLUE identical wording |
| 132 | `einer davon war eine Schatulle, die nur Fiona öffnen konnte` | `einer davon war ein Koffer, den nur Fiona öffnen konnte` | the locked trunk is 'Koffer' everywhere else; 'Schatulle' (casket) broke the reference |
| 139 | `Das kleine Empfangszimmer mit der lauten Uhr.` | `Das kleine Wohnzimmer mit der lauten Uhr.` | sitting room unified |
| 139 | `den mit dem Geld gekauften Gasthof` | `der mit dem Geld gekaufte Gasthof` | case agreement in nominative list |
| 179 | `wobei das letzte S ganz am Ende` | `wobei das letzte E ganz am Ende` | translated banner ends in E (JAHRE) - squeezed-letter joke kept working (ruling 3) |
| 179 | `einen Tisch mit Apfelwein und Ingwerpfeffernüssen` | `einen Tisch mit heißem Apfelsaft und Ingwerpfeffernüssen` | cider non-alcoholic (ruling 6) |
| 181 | `Er hätte sogar den Apfelwein beschriftet` | `Er hätte sogar den Apfelsaft beschriftet` | ruling 6 |
| 193 | `Dem Volk von Frost Falls als Leihgabe überlassen.` | `Den Menschen von Frost Falls als Leihgabe überlassen.` | 'the people of Frost Falls' - 'Volk' is wrong register/connotation |
| 196 | `am Apfelweintisch auf mich zu` | `am Apfelsafttisch auf mich zu` | ruling 6 |
| 202 | `alle zum Apfelwein einzuladen` | `alle zum Apfelsaft einzuladen` | ruling 6 |
| 203 | `ein Erpresserbrief, der genau wusste` | `ein Erpresserzettel, der genau wusste` | blackmail NOTE must never share the word 'Brief' with the Blackburn LETTERS |
| 207 | `ging weiter zum Apfelwein,` | `ging weiter zum Apfelsaft,` | ruling 6 |
| 211 | `direkt neben den Brief.` | `direkt neben den Zettel.` | the note, not a letter |
| 211 | `am Apfelweintisch saß` | `am Apfelsafttisch saß` | ruling 6 |
| 215 | `Die Strickrunde hatte an diesem Nachmittag` | `Der Strickkreis hatte an diesem Nachmittag` | circle = Strickkreis |
| 217 | `denn die Strickrunde erfuhr alles` | `denn der Strickkreis erfuhr alles` | circle = Strickkreis |
| 218 | `die die Strickrunde jedes Jahr` | `die der Strickkreis jedes Jahr` | circle = Strickkreis |
| 241 | `eine enorme Last für das Inn,` | `eine enorme Last für den Gasthof,` | 'das Inn' vs 'Gasthof' - inn = Gasthof outside the proper name |
| 242 | `die Strickrunde ist da, falls sie uns braucht` | `der Strickkreis ist da, falls sie uns braucht` | circle = Strickkreis |
| 244 | `Genau das ist der Sinn einer Strickrunde.` | `Genau das ist der Sinn eines Kreises.` | Martha's key line - now echoes ch24/ch29 'Sinn eines Kreises' / 'ein Kreis zum Anlehnen' |
| 249 | `die nicht einmal einen Bruchteil davon besaß` | `die nicht einmal ein Zehntel davon besaß` | EN 'didn't have a tenth of it' (Bruchteil then reused for 'a fraction') |
| 251 | `was die Strickrunde mir anvertraut hatte` | `was der Strickkreis mir anvertraut hatte` | circle = Strickkreis |
| 260 | `Schneeball saß` | `Snowball saß` | Martha's dog = Snowball (Book 1 + rest of this book) |
| 267 | `Schneeball habe fast` | `Snowball habe fast` | Snowball |
| 269 | `zwischen Schneeball und` | `zwischen Snowball und` | Snowball |
| 288 | `ein Erpresserbrief, eine Vorstandssitzung` | `ein Erpresserzettel, eine Vorstandssitzung` | note != letters |
| 304 | `einem Erpresserbrief ist er` | `einem Erpresserzettel ist er` | note != letters |
| 312 | `und zu einem Feldweg wurde` | `und zu einer Landstraße wurde` | EN 'became a road' - not a dirt field track |
| 313 | `Ich hatte den Erpressungsbrief seit` | `Ich hatte den Erpresserzettel seit` | note != letters |
| 320 | `in Fionas Empfangsbereich.` | `in Fionas Lobby.` | inn lobby = Lobby (had 4 names) |
| 329 | `über die Anfänge des Inns? Wie Fionas Familie dazu kam, es zu besitzen` | `über die Anfänge des Gasthofs? Wie Fionas Familie dazu kam, ihn zu besitzen` | inn = Gasthof |
| 330 | `es zu besitzen? Sie besitzen es schon immer.` | `ihn zu besitzen? Sie besitzen ihn schon immer.` | pronoun agreement after Gasthof |
| 330 | `Ihre Urgroßmutter hat es gegründet` | `Ihre Urgroßmutter hat ihn gegründet` | pronoun agreement after Gasthof |
| 333 | `in diesen Empfangsbereich gesteckt` | `in diese Lobby gesteckt` | lobby |
| 334 | `Der gesamte Empfangsbereich war von seinem Eisen` | `Die gesamte Lobby war von seinem Eisen` | lobby |
| 334 | `Alles, was in diesem Empfangsbereich zurückgelassen` | `Alles, was in dieser Lobby zurückgelassen` | lobby |
| 349 | `ein Tagebuch des Gehilfen` | `ein Tagesjournal des Gehilfen` | EN 'clerk's daybook' (business record), not a diary |
| 366 | `das muss ich Ihnen sagen.` | `das muss ich dir sagen.` | Bram <-> Jessica informal (ruling 2; Book 1 du) |
| 368 | `und erklären Sie mir mal, Mrs. Claus,` | `und erklär du mir mal, Mrs. Claus,` | Bram du |
| 368 | `und ich erzähle Ihnen dasselbe` | `und ich erzähle dir dasselbe` | Bram du |
| 392 | `den Namen des Zirkels` | `den Namen des Strickkreises` | circle = Strickkreis ('Zirkel' = compass/esoteric circle) |
| 402 | `den Zirkel in ihrer` | `den Strickkreis in ihrer` | circle |
| 408 | `Der Zirkel ist eingetragen.` | `Der Strickkreis ist eingetragen.` | circle |
| 425 | `Frau Pelletier,` | `Mrs. Pelletier,` | edition (and Book 1) keep Mr./Mrs.; 9 stray Herr/Frau normalised |
| 426 | `und Frau Claus hier` | `und Mrs. Claus hier` | Mrs. Claus |
| 437 | `„Du würdest nie wieder eine Bahn für dich allein bekommen.“` | `„Sie würden nie wieder eine Bahn für sich allein bekommen.“` | Jamal = acquaintance, formal both ways (he says Sie) |
| 447 | `„Du hast Theo bei der Ausstellung geholfen“` | `„Sie haben Theo bei der Ausstellung geholfen“` | Jamal Sie |
| 447 | `Hast du einen Blick hineingeworfen, während du da drin warst?` | `Haben Sie einen Blick hineingeworfen, während Sie da drin waren?` | Jamal Sie |
| 448 | `ich habe Vitrinen zu zweit geschleppt` | `ich habe immer zwei Vitrinen auf einmal geschleppt` | EN 'two at a time' - 'zu zweit' means with a partner |
| 450 | `„du bist ein guter Freund für Theo, dass du all diese Muskelkraft geliehen hast, wo du doch deine eigenen Sorgen hattest.` | `„Sie sind ein guter Freund für Theo, dass Sie all diese Muskelkraft geliehen haben, wo Sie doch Ihre eigenen Sorgen hatten.` | Jamal Sie |
| 452 | `„Du bist der richtige Mann` | `„Sie sind der richtige Mann` | Jamal Sie |
| 466 | `schauen Sie sie sich nur an` | `schau sie dir nur an` | Bram du |
| 466 | `würden Sie sehen, dass es ihr nicht leid tut` | `würdest du sehen, dass es ihr nicht leid tut` | Bram du |
| 483 | `Sie hatte sie von Herrn Kim,` | `Sie hatte sie von Mr. Kim,` | Mr. Kim elsewhere |
| 485 | `„So erzählt Herr Kim das aber nicht.“` | `„So erzählt Mr. Kim das aber nicht.“` | Mr. Kim |
| 521 | `Die Duftspur weist auf das Inn,` | `Die Duftspur weist auf den Gasthof,` | inn = Gasthof |
| 525 | `und die Urkunde des Inns muss` | `und die Urkunde des Gasthofs muss` | inn = Gasthof |
| 540 | `außer Hörweite des Foyers` | `außer Hörweite der Lobby` | lobby |
| 546 | `Fionas Foyer war voll davon` | `Fionas Lobby war voll davon` | lobby |
| 548 | `die Schmiede in drei Countys stehen` | `die Schmiede in drei Landkreisen stehen` | 'county' = Landkreis elsewhere in the edition |
| 564 | `was im Erpresserbrief stand. Es stand mehr darin als in dem Brief` | `was im Erpresserzettel stand. Es stand mehr darin als auf dem Zettel` | note != letters |
| 565 | `wie der Brief Ihre Freundin glauben machen will` | `wie der Zettel Ihre Freundin glauben machen will` | EN 'the note wants your friend to believe' |
| 574 | `Es war der Zettelkasten, der dem ein Ende setzte.` | `Es war der Karteikasten, der dem ein Ende setzte.` | card index called 'Zettel'-kasten in the very chapter where 'Zettel' = the note; Karteikasten (matches 'Karteikarten') |
| 575 | `Bäckereiquittungen, Musikpavillon-Spenden` | `Bäckereiquittungen, Beiträge Musikpavillon` | B-cards: alphabetical filing joke kept (ruling 3) |
| 577 | `(der Saphir im Herzen)` | `(der Saphir in ihrem Herzen)` | KEY CLUE on Theo's card |
| 578 | `Der Saphir im Herzen.` | `Der Saphir in ihrem Herzen.` | KEY CLUE |
| 579 | `gefaltete Erpresserbrief enthielt` | `gefaltete Erpresserzettel enthielt` | note != letters |
| 579 | `Der Saphir im Herzen. Es war` | `Der Saphir in ihrem Herzen. Es war` | KEY CLUE; 'fünf Wörter' now true (5 words) |
| 579 | `Er stand im Erpresserbrief genau so` | `Er stand im Erpresserzettel genau so` | note != letters |
| 582 | `B, B, Bridge-Turnier, Wimpelketten, Überschuss` | `B, B, Bridge-Turnier, Banner und Wimpel, Überschuss` | B-card alphabetical joke (EN 'Bunting, Surplus' = one B card) |
| 582 | `hatte die Briefe geschrieben, die Fiona in Angst und Schrecken versetzten. Oder seine Sorgfalt bei der Aufbewahrung dieser Briefe hatte jemand anderem erlaubt, sie zu schreiben,` | `hatte die Zettel geschrieben, die Fiona in Angst und Schrecken versetzten. Oder seine Sorgfalt bei der Aufbewahrung jener Briefe hatte es jemand anderem ermöglicht, die Zettel zu schreiben,` | REVERSED DEDUCTION: German said Theo wrote the LETTERS and someone else wrote the letters; EN = wrote the NOTES / care of the letters let someone else write the notes |
| 589 | `keinen Pfennig` | `keinen Cent` | US setting - Cent as elsewhere |
| 610 | `in das kleine Lesezimmer gesperrt` | `in das kleine Wohnzimmer gesperrt` | sitting room |
| 610 | `er ist in meine Eingangshalle gelaufen` | `er ist in meine Lobby gelaufen` | EN 'my lobby'; front hall is a different room |
| 623 | `Er ist in meine Eingangshalle gelaufen.` | `Er ist in meine Lobby gelaufen.` | echo of Fiona's words |
| 630 | `die Teigtaschen von Herrn Kims Frau` | `die Teigtaschen von Mr. Kims Frau` | Mr. Kim |
| 630 | `mit den Fausthandschuhen des Strickkreises` | `mit den Fäustlingen des Strickkreises` | mittens = Fäustlinge throughout |
| 630 | `Apfelweinbuden und Stände` | `Buden mit heißem Apfelsaft und Stände` | ruling 6 |
| 633 | `am Apfelweinstand auf` | `am Apfelsaftstand auf` | ruling 6 |
| 633 | `dass Frau Claus ihre Sternbilder` | `dass Mrs. Claus ihre Sternbilder` | Mrs. Claus |
| 633 | `zwei Bechern Apfelwein` | `zwei Bechern Apfelsaft` | ruling 6 |
| 633 | `ein Paar Fausthandschuhe in die Hand` | `ein Paar Fäustlinge in die Hand` | mittens |
| 635 | `lediglich Frau Pelletier vom` | `lediglich Mrs. Pelletier vom` | Mrs. Pelletier |
| 635 | `Frau Pelletier sah ratlos` | `Mrs. Pelletier sah ratlos` | Mrs. Pelletier |
| 636 | `am Apfelweinstand, in ihrem Parka` | `am Apfelsaftstand, in ihrem Parka` | ruling 6 |
| 637 | `„Du sahst aus, als würdest du Frau Pelletier gleich umwerfen“` | `„Sie sahen aus, als würden Sie Mrs. Pelletier gleich umwerfen“` | Noriko formal until the EN puts them on first names (ch25) |
| 639 | `von ihrem Apfelwein.` | `von ihrem Apfelsaft.` | ruling 6 |
| 639 | `zwei von euch, die` | `zwei von Ihnen, die` | Noriko formal |
| 642 | `„Du weißt, wo die Wache ist.` | `„Sie wissen, wo die Wache ist.` | Noriko formal |
| 642 | `„Dein Pinguin hat` | `„Ihr Pinguin hat` | Noriko formal |
| 643 | `„Sag ihr das bloß nicht“` | `„Sagen Sie ihr das bloß nicht“` | Noriko formal |
| 644 | `in der wir Schneeball gefunden` | `in der wir Snowball gefunden` | Snowball |
| 654 | `Der Saphir in seinem Herzen: fünf Wörter` | `Der Saphir in ihrem Herzen: fünf Wörter` | KEY CLUE (was a 3rd variant) |
| 654 | `die im Erpresserbrief genau so standen` | `die im Erpresserzettel genau so standen` | note != letters |
| 659 | `in ein Foyer voll von Festivalgästen getragen` | `in eine Lobby voller Festivalgäste getragen` | lobby |
| 673 | `die mir gerade direkt ins Gesicht gesehen` | `die mir direkt ins Gesicht gesehen` | 'gerade' (just now) not in EN - she said it on earlier visits |
| 676 | `„geht es dir gut? Wirklich. Du siehst gar nicht gut aus.“` | `„geht es Ihnen gut? Wirklich. Sie sehen gar nicht gut aus.“` | Jessica <-> Vera formal (Vera always Sie) |
| 680 | `katalogisiert, den Saphir in ihrem Herzen, und dann` | `katalogisiert – der Saphir in ihrem Herzen –, und dann` | KEY CLUE kept in the identical nominative form |
| 732 | `„Setzt euch bitte, ihr beiden“` | `„Setzen Sie sich bitte, Sie beide“` | Noriko with Theo/Vera = professional, formal (ruling 2) |
| 732 | `danach werdet ihr beide jeweils` | `danach werden Sie beide jeweils` | formal |
| 732 | `Setzt euch.“` | `Setzen Sie sich.“` | formal |
| 735 | `„Die Erpresserbriefe an Fiona` | `„Die Erpresserzettel an Fiona` | confrontation: notes != Blackburn letters |
| 735 | `als der Saphir im Herzen bezeichnet` | `als der Saphir in ihrem Herzen bezeichnet` | KEY CLUE in the confrontation |
| 740 | `in deinem Ablagekorb` | `in Ihrem Ablagekorb` | Jessica -> Vera formal |
| 740 | `Du hattest die Urkunde. Und du hattest die Beine, Vera.` | `Sie hatten die Urkunde. Und Sie hatten die Beine, Vera.` | Vera formal |
| 740 | `Ich bin dir an jenem Morgen selbst auf der Treppe begegnet, mit deinen Parkausweisen.` | `Ich bin Ihnen an jenem Morgen selbst auf der Treppe begegnet, mit Ihren Parkausweisen.` | Vera formal |
| 740 | `Das warst du.“` | `Das waren Sie.“` | Vera formal |
| 742 | `Sie wog sich ein wenig` | `Sie wiegte sich ein wenig` | rocking = wiegen/wiegte (wog = weighed) |
| 745 | `„Ihr habt es beide freimütig zugegeben, und das zählt mehr, als ihr beide jetzt noch begreifen könnt.` | `„Sie haben es beide freimütig zugegeben, und das zählt mehr, als Sie beide jetzt noch begreifen können.` | Noriko with Theo/Vera formal |
| 748 | `Die beiden Briefe wurden zu Beweismitteln` | `Die beiden Zettel wurden zu Beweismitteln` | the two NOTES became evidence |
| 760 | `„Du hast etwas Falsches getan“` | `„Sie haben etwas Falsches getan“` | Vera formal |
| 760 | `„Und du büßt dafür` | `„Und Sie büßen dafür` | Vera formal |
| 760 | `Aber du hast es genau in dem Moment zugegeben, als man dich fragte, Vera. Du hast nicht gelogen und dich nicht herausgewunden.` | `Aber Sie haben es genau in dem Moment zugegeben, als man Sie fragte, Vera. Sie haben nicht gelogen und sich nicht herausgewunden.` | Vera formal |
| 760 | `Das ist der Teil von dir, der` | `Das ist der Teil von Ihnen, der` | Vera formal |
| 760 | `dass du daran festhältst. Der Weg zurück ist auch für dich lang.` | `dass Sie daran festhalten. Der Weg zurück ist auch für Sie lang.` | Vera formal |
| 760 | `Lass dir von niemandem einreden, es gäbe keinen, und vor allem rede es dir nicht selbst ein.` | `Lassen Sie sich von niemandem einreden, es gäbe keinen, und vor allem reden Sie es sich nicht selbst ein.` | Vera formal |
| 762 | `Die Briefe hatten aufgehört.` | `Es kamen keine Zettel mehr.` | EN 'The notes had stopped' |
| 776 | `diese peinlichen kleinen Tombolen` | `diese peinlichen kleinen Tombolas` | plural matches 780 'Tombolas' |
| 789 | `im Sterben lag, der man eingetrichtert hatte, dankbar` | `im Sterben lag; man hatte dem Mädchen eingetrichtert, dankbar` | relative clause attached 'told to be grateful' to the dying MOTHER; EN = Constance |
| 807 | `Schneeball trug` | `Snowball trug` | Snowball |
| 815 | `ich frage Sie!` | `ich frage dich!` | Bram du |
| 852 | `Greta hatte seit vierzig Jahren dieselbe Zimtschnecke gebacken. Sie hatte sie am Morgen nach dem Begräbnis ihres Mannes gebacken, weil sie nicht gewusst hatte, wohin mit ihren Händen.` | `Greta backt seit vierzig Jahren dieselbe Zimtschnecke. Sie hat sie am Morgen nach dem Begräbnis ihres Mannes gebacken, weil sie nicht wusste, wohin mit ihren Händen.` | blurb tense drift (EN present-perfect/present; German pluperfect then present) |
| 868 | `der bereits doppelt so groß wie der von allen anderen` | `der bereits anderthalbmal so groß wie der von allen anderen` | EN 'half again the size' = 1.5x |
| 869 | `das Bett hütete oder Enkelkinder hütete` | `das Bett hütete oder auf Enkelkinder aufpasste` | doubled verb 'hütete' |
| 874 | `meinen Tannenzapfenschuppen zu` | `meinen Reisigschuppen zu` | EN 'my scales of balsam' (the overlapping sprigs), not pinecone scales |
| 875 | `Nicht die Meilen. Es waren eine ganze Menge davon gewesen, aber die Meilen meinte ich nicht.` | `Nicht die Kilometer. Es waren eine ganze Menge davon gewesen, aber die Kilometer meinte ich nicht.` | spelled-out imperial 'miles' (no number) - SAFE: metric word swap, nothing to compute |
| 879 | `Ihr Bagage tut es ja sonst nicht für euch selbst.` | `Ihr tut es ja sonst nicht für euch selbst.` | 'Ihr Bagage' ungrammatical (die Bagage) |
| 879 | `mit dem Balsam, Schokolade` | `mit dem Tannenduft, Schokolade` | 'balsam' = balsam fir (Tannenreisig elsewhere); German 'Balsam' = ointment |
| 879 | `gelagert über kaltem` | `gelegt über kaltem` | 'laid over' (gelagert = stored) |
| 884 | `jeder Penny geht` | `jeder Cent geht` | Cent |
| 573 | `einem herrlich aufgetakelten Wrack` | `einem herrlichen Schiffbruch` | EN 'a glorious shipwreck' ('aufgetakelt' = dolled up/rigged) |
| 600 | `Nicks Worte aus der Nacht, in der wir die Liste sahen, stiegen` | `Nicks Worte aus der Nacht mit der Liste stiegen` | EN 'the night of the list' (she wrote it; they did not 'see' it) |
| 386 paras | „ “ ‚ ‘ | » « › ‹ | ruling 1 / dossier |

## Needs a decision
DE2-D1 scene break ch10; DE2-D3 Mark address; DE2-D4 ch20 italic. DE2-D2 = formatter note. DE2-D5/D6 applied, please confirm.

## Refused
None.
