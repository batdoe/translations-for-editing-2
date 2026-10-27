# PROOFREAD — Inn Trouble - ASSEMBLED - FORMATTED_German (2026-10-26 run, done 2026-10-27)

- Edition: German. English: `translate_now\Inn Trouble - ASSEMBLED - FORMATTED.docx`. Input: `translated\` (web-proofread 2026-10-26). Output: `translated\corrected\`.
- Prior report (web 2026-10-26, hint only): 1/263 applied fixes not found verbatim (0.4%) — #3 'Ein Schmied schuldete' was later rewritten into the current (correct) blurb sentence. Not stale; its fixes were kept.
- Coverage: front matter + ch1-31 + What's Next? + Flour Play excerpt, read in full against the English.
- Findings: 144 text fixes + 1 book-wide dialogue-punctuation finding (386 paragraphs) + 6 decision items (3 open, 1 formatter note, 2 applied-for-confirmation). Refused: 0.
- Worst defect: ch19 para 582 REVERSED the deduction — the German said Theo 'had written the LETTERS (Briefe)' and that his care of 'these letters' let someone else 'write them'; English = he wrote the NOTES / his care of the letters let someone else write the NOTES. The blackmail note was called 'Brief' 14 times (Erpresserbrief, 'die beiden Briefe', 'Die Briefe hatten aufgehört'), so note and 1924 Blackburn letters were indistinguishable through the Ch19/Ch22/Ch26 deduction. Second: the key clue had 3 wordings and a false 'five words' count.
- Dialogue: the whole book used „…“ (non-fiction convention); converted to »…« / nested ›…‹ per the German dossier and ruling 1 (glyph swap at run level; attribution comma placement was already German-correct).
- Units: preflight's 10 tokens = 7x body-part 'Fuß' (false positives) + 'fünfzig Meilen' (kept, ruling 4) + 2x spelled-out 'Meilen' in the Flour Play excerpt ('Not the miles', no number) -> 'Kilometer' (SAFE rule: word swap, nothing to compute). EN 'four acres' is already 'anderthalb Hektar' (fine).

## Address table used (ruling 2)
- du both ways: Jessica <-> Fiona, Nick, the circle women, Theo (du since Book 1), Bram (6 Sie->du fixes: ch10 366/368, ch14 466, ch30 815).
- Children: Emma -> Jessica Sie; Jessica -> Emma du.
- Sie both ways: Jamal (Jessica's du -> Sie, ch13 x5), Vera (ch23 676, ch26 740, ch27 760), Sam, Neil, Greta, the Mayor, the Worthingtons.
- Noriko <-> Jessica: Sie ch6-ch21 (ch21 637/639/642/643 du -> Sie); du from ch25, where the English puts them on first names.
- Noriko -> Theo/Vera (ch26, professional): Sie (732/745 ihr -> Sie).
- Theo/Vera/Fiona among themselves: du (neighbours), unchanged. Mark <-> Jessica: left asymmetric (DE2-D3).

## Findings (German quoted verbatim as found; para = paras() index)
| # | Class | Para | German (verbatim) | Why (English) | Corrected | Status |
|---|---|---|---|---|---|---|
| 1 | bt | 28 | `<bt>Yarn Tales</bt>` | stray <bt> on a non-title (ruling 5) | `Yarn Tales` | APPLIED |
| 2 | bt | 30 | `<bt>Winter Wonderland Inn</bt>` | stray <bt> on a non-title (ruling 5) | `Winter Wonderland Inn` | APPLIED |
| 3 | bt | 860 | `<bt>Yarn Tales</bt>` | stray <bt> on a non-title (ruling 5) | `Yarn Tales` | APPLIED |
| 4 | bt | 896 | `<bt>Yarn Tales</bt>` | stray <bt> on a non-title (ruling 5) | `Yarn Tales` | APPLIED |
| 5 | bt | 869 | `<bt>Gazette</bt>` | stray <bt> on a non-title (ruling 5) | `Gazette` | APPLIED |
| 6 | bt | 877 | `<bt>Holly Jolly Bakery</bt>` | stray <bt> on a non-title (ruling 5) | `Holly Jolly Bakery` | APPLIED |
| 7 | bt | 459 | `der <bt>The Holly Jolly Bakery</bt> bereit` | stray <bt> + English article 'The' after German 'der' (ruling 5) | `der Holly Jolly Bakery bereit` | APPLIED |
| 8 | mistranslation | 30 | `samt einem einzelnen Zweig Stechpalmenbeeren für das herbstliche Orange` | EN 'bittersweet' (orange-berried Celastrus = Baumwürger), not holly; holly pre-empted the ch6 holly miracle | `samt einem einzelnen Zweig Baumwürger für das herbstliche Orange` | APPLIED |
| 9 | term | 84 | `sich der Handarbeitskreis traf` | knitting circle = Strickkreis/Kreis (German Book 1 form) | `sich der Strickkreis traf` | APPLIED |
| 10 | term | 96 | `in das kleine Lesezimmer abseits der Lobby` | Fiona's 'little sitting room' had 3 names (Lesezimmer/Empfangszimmer/Wohnzimmer); unified to Wohnzimmer | `in das kleine Wohnzimmer abseits der Lobby` | APPLIED |
| 11 | clue | 101 | `die deine Urgroßmutter den Blackburns gestohlen hat, der mit dem Saphir im Herzen, und dem Geschäft in Ridgeline` | KEY CLUE: identical 5-word wording 'der Saphir in ihrem Herzen' in note/reading/card/confrontation | `die deine Urgroßmutter den Blackburns gestohlen hat – der Saphir in ihrem Herzen –, und von dem Geschäft in Ridgeline` | APPLIED |
| 12 | clue | 102 | `Der Saphir im Herzen.` | KEY CLUE identical wording | `Der Saphir in ihrem Herzen.` | APPLIED |
| 13 | clue | 119 | `Der Saphir im Herzen, genau diese Worte.` | KEY CLUE identical wording | `Der Saphir in ihrem Herzen, genau diese Worte.` | APPLIED |
| 14 | term | 132 | `einer davon war eine Schatulle, die nur Fiona öffnen konnte` | the locked trunk is 'Koffer' everywhere else; 'Schatulle' (casket) broke the reference | `einer davon war ein Koffer, den nur Fiona öffnen konnte` | APPLIED |
| 15 | term | 139 | `Das kleine Empfangszimmer mit der lauten Uhr.` | sitting room unified | `Das kleine Wohnzimmer mit der lauten Uhr.` | APPLIED |
| 16 | grammar | 139 | `den mit dem Geld gekauften Gasthof` | case agreement in nominative list | `der mit dem Geld gekaufte Gasthof` | APPLIED |
| 17 | sign | 179 | `wobei das letzte S ganz am Ende` | translated banner ends in E (JAHRE) - squeezed-letter joke kept working (ruling 3) | `wobei das letzte E ganz am Ende` | APPLIED |
| 18 | cider | 179 | `einen Tisch mit Apfelwein und Ingwerpfeffernüssen` | cider non-alcoholic (ruling 6) | `einen Tisch mit heißem Apfelsaft und Ingwerpfeffernüssen` | APPLIED |
| 19 | cider | 181 | `Er hätte sogar den Apfelwein beschriftet` | ruling 6 | `Er hätte sogar den Apfelsaft beschriftet` | APPLIED |
| 20 | mistranslation | 193 | `Dem Volk von Frost Falls als Leihgabe überlassen.` | 'the people of Frost Falls' - 'Volk' is wrong register/connotation | `Den Menschen von Frost Falls als Leihgabe überlassen.` | APPLIED |
| 21 | cider | 196 | `am Apfelweintisch auf mich zu` | ruling 6 | `am Apfelsafttisch auf mich zu` | APPLIED |
| 22 | cider | 202 | `alle zum Apfelwein einzuladen` | ruling 6 | `alle zum Apfelsaft einzuladen` | APPLIED |
| 23 | note-word | 203 | `ein Erpresserbrief, der genau wusste` | blackmail NOTE must never share the word 'Brief' with the Blackburn LETTERS | `ein Erpresserzettel, der genau wusste` | APPLIED |
| 24 | cider | 207 | `ging weiter zum Apfelwein,` | ruling 6 | `ging weiter zum Apfelsaft,` | APPLIED |
| 25 | note-word | 211 | `direkt neben den Brief.` | the note, not a letter | `direkt neben den Zettel.` | APPLIED |
| 26 | cider | 211 | `am Apfelweintisch saß` | ruling 6 | `am Apfelsafttisch saß` | APPLIED |
| 27 | term | 215 | `Die Strickrunde hatte an diesem Nachmittag` | circle = Strickkreis | `Der Strickkreis hatte an diesem Nachmittag` | APPLIED |
| 28 | term | 217 | `denn die Strickrunde erfuhr alles` | circle = Strickkreis | `denn der Strickkreis erfuhr alles` | APPLIED |
| 29 | term | 218 | `die die Strickrunde jedes Jahr` | circle = Strickkreis | `die der Strickkreis jedes Jahr` | APPLIED |
| 30 | term | 241 | `eine enorme Last für das Inn,` | 'das Inn' vs 'Gasthof' - inn = Gasthof outside the proper name | `eine enorme Last für den Gasthof,` | APPLIED |
| 31 | term | 242 | `die Strickrunde ist da, falls sie uns braucht` | circle = Strickkreis | `der Strickkreis ist da, falls sie uns braucht` | APPLIED |
| 32 | term | 244 | `Genau das ist der Sinn einer Strickrunde.` | Martha's key line - now echoes ch24/ch29 'Sinn eines Kreises' / 'ein Kreis zum Anlehnen' | `Genau das ist der Sinn eines Kreises.` | APPLIED |
| 33 | mistranslation | 249 | `die nicht einmal einen Bruchteil davon besaß` | EN 'didn't have a tenth of it' (Bruchteil then reused for 'a fraction') | `die nicht einmal ein Zehntel davon besaß` | APPLIED |
| 34 | term | 251 | `was die Strickrunde mir anvertraut hatte` | circle = Strickkreis | `was der Strickkreis mir anvertraut hatte` | APPLIED |
| 35 | name | 260 | `Schneeball saß` | Martha's dog = Snowball (Book 1 + rest of this book) | `Snowball saß` | APPLIED |
| 36 | name | 267 | `Schneeball habe fast` | Snowball | `Snowball habe fast` | APPLIED |
| 37 | name | 269 | `zwischen Schneeball und` | Snowball | `zwischen Snowball und` | APPLIED |
| 38 | note-word | 288 | `ein Erpresserbrief, eine Vorstandssitzung` | note != letters | `ein Erpresserzettel, eine Vorstandssitzung` | APPLIED |
| 39 | note-word | 304 | `einem Erpresserbrief ist er` | note != letters | `einem Erpresserzettel ist er` | APPLIED |
| 40 | mistranslation | 312 | `und zu einem Feldweg wurde` | EN 'became a road' - not a dirt field track | `und zu einer Landstraße wurde` | APPLIED |
| 41 | note-word | 313 | `Ich hatte den Erpressungsbrief seit` | note != letters | `Ich hatte den Erpresserzettel seit` | APPLIED |
| 42 | term | 320 | `in Fionas Empfangsbereich.` | inn lobby = Lobby (had 4 names) | `in Fionas Lobby.` | APPLIED |
| 43 | term | 329 | `über die Anfänge des Inns? Wie Fionas Familie dazu kam, es zu besitzen` | inn = Gasthof | `über die Anfänge des Gasthofs? Wie Fionas Familie dazu kam, ihn zu besitzen` | APPLIED |
| 44 | term | 330 | `es zu besitzen? Sie besitzen es schon immer.` | pronoun agreement after Gasthof | `ihn zu besitzen? Sie besitzen ihn schon immer.` | APPLIED |
| 45 | term | 330 | `Ihre Urgroßmutter hat es gegründet` | pronoun agreement after Gasthof | `Ihre Urgroßmutter hat ihn gegründet` | APPLIED |
| 46 | term | 333 | `in diesen Empfangsbereich gesteckt` | lobby | `in diese Lobby gesteckt` | APPLIED |
| 47 | term | 334 | `Der gesamte Empfangsbereich war von seinem Eisen` | lobby | `Die gesamte Lobby war von seinem Eisen` | APPLIED |
| 48 | term | 334 | `Alles, was in diesem Empfangsbereich zurückgelassen` | lobby | `Alles, was in dieser Lobby zurückgelassen` | APPLIED |
| 49 | mistranslation | 349 | `ein Tagebuch des Gehilfen` | EN 'clerk's daybook' (business record), not a diary | `ein Tagesjournal des Gehilfen` | APPLIED |
| 50 | address | 366 | `das muss ich Ihnen sagen.` | Bram <-> Jessica informal (ruling 2; Book 1 du) | `das muss ich dir sagen.` | APPLIED |
| 51 | address | 368 | `und erklären Sie mir mal, Mrs. Claus,` | Bram du | `und erklär du mir mal, Mrs. Claus,` | APPLIED |
| 52 | address | 368 | `und ich erzähle Ihnen dasselbe` | Bram du | `und ich erzähle dir dasselbe` | APPLIED |
| 53 | term | 392 | `den Namen des Zirkels` | circle = Strickkreis ('Zirkel' = compass/esoteric circle) | `den Namen des Strickkreises` | APPLIED |
| 54 | term | 402 | `den Zirkel in ihrer` | circle | `den Strickkreis in ihrer` | APPLIED |
| 55 | term | 408 | `Der Zirkel ist eingetragen.` | circle | `Der Strickkreis ist eingetragen.` | APPLIED |
| 56 | honorific | 425 | `Frau Pelletier,` | edition (and Book 1) keep Mr./Mrs.; 9 stray Herr/Frau normalised | `Mrs. Pelletier,` | APPLIED |
| 57 | honorific | 426 | `und Frau Claus hier` | Mrs. Claus | `und Mrs. Claus hier` | APPLIED |
| 58 | address | 437 | `„Du würdest nie wieder eine Bahn für dich allein bekommen.“` | Jamal = acquaintance, formal both ways (he says Sie) | `„Sie würden nie wieder eine Bahn für sich allein bekommen.“` | APPLIED |
| 59 | address | 447 | `„Du hast Theo bei der Ausstellung geholfen“` | Jamal Sie | `„Sie haben Theo bei der Ausstellung geholfen“` | APPLIED |
| 60 | address | 447 | `Hast du einen Blick hineingeworfen, während du da drin warst?` | Jamal Sie | `Haben Sie einen Blick hineingeworfen, während Sie da drin waren?` | APPLIED |
| 61 | mistranslation | 448 | `ich habe Vitrinen zu zweit geschleppt` | EN 'two at a time' - 'zu zweit' means with a partner | `ich habe immer zwei Vitrinen auf einmal geschleppt` | APPLIED |
| 62 | address | 450 | `„du bist ein guter Freund für Theo, dass du all diese Muskelkraft geliehen hast, wo du doch deine eigenen Sorgen hattest.` | Jamal Sie | `„Sie sind ein guter Freund für Theo, dass Sie all diese Muskelkraft geliehen haben, wo Sie doch Ihre eigenen Sorgen hatten.` | APPLIED |
| 63 | address | 452 | `„Du bist der richtige Mann` | Jamal Sie | `„Sie sind der richtige Mann` | APPLIED |
| 64 | address | 466 | `schauen Sie sie sich nur an` | Bram du | `schau sie dir nur an` | APPLIED |
| 65 | address | 466 | `würden Sie sehen, dass es ihr nicht leid tut` | Bram du | `würdest du sehen, dass es ihr nicht leid tut` | APPLIED |
| 66 | honorific | 483 | `Sie hatte sie von Herrn Kim,` | Mr. Kim elsewhere | `Sie hatte sie von Mr. Kim,` | APPLIED |
| 67 | honorific | 485 | `„So erzählt Herr Kim das aber nicht.“` | Mr. Kim | `„So erzählt Mr. Kim das aber nicht.“` | APPLIED |
| 68 | term | 521 | `Die Duftspur weist auf das Inn,` | inn = Gasthof | `Die Duftspur weist auf den Gasthof,` | APPLIED |
| 69 | term | 525 | `und die Urkunde des Inns muss` | inn = Gasthof | `und die Urkunde des Gasthofs muss` | APPLIED |
| 70 | term | 540 | `außer Hörweite des Foyers` | lobby | `außer Hörweite der Lobby` | APPLIED |
| 71 | term | 546 | `Fionas Foyer war voll davon` | lobby | `Fionas Lobby war voll davon` | APPLIED |
| 72 | term | 548 | `die Schmiede in drei Countys stehen` | 'county' = Landkreis elsewhere in the edition | `die Schmiede in drei Landkreisen stehen` | APPLIED |
| 73 | note-word | 564 | `was im Erpresserbrief stand. Es stand mehr darin als in dem Brief` | note != letters | `was im Erpresserzettel stand. Es stand mehr darin als auf dem Zettel` | APPLIED |
| 74 | note-word | 565 | `wie der Brief Ihre Freundin glauben machen will` | EN 'the note wants your friend to believe' | `wie der Zettel Ihre Freundin glauben machen will` | APPLIED |
| 75 | note-word | 574 | `Es war der Zettelkasten, der dem ein Ende setzte.` | card index called 'Zettel'-kasten in the very chapter where 'Zettel' = the note; Karteikasten (matches 'Karteikarten') | `Es war der Karteikasten, der dem ein Ende setzte.` | APPLIED |
| 76 | sign | 575 | `Bäckereiquittungen, Musikpavillon-Spenden` | B-cards: alphabetical filing joke kept (ruling 3) | `Bäckereiquittungen, Beiträge Musikpavillon` | APPLIED |
| 77 | clue | 577 | `(der Saphir im Herzen)` | KEY CLUE on Theo's card | `(der Saphir in ihrem Herzen)` | APPLIED |
| 78 | clue | 578 | `Der Saphir im Herzen.` | KEY CLUE | `Der Saphir in ihrem Herzen.` | APPLIED |
| 79 | note-word | 579 | `gefaltete Erpresserbrief enthielt` | note != letters | `gefaltete Erpresserzettel enthielt` | APPLIED |
| 80 | clue | 579 | `Der Saphir im Herzen. Es war` | KEY CLUE; 'fünf Wörter' now true (5 words) | `Der Saphir in ihrem Herzen. Es war` | APPLIED |
| 81 | note-word | 579 | `Er stand im Erpresserbrief genau so` | note != letters | `Er stand im Erpresserzettel genau so` | APPLIED |
| 82 | sign | 582 | `B, B, Bridge-Turnier, Wimpelketten, Überschuss` | B-card alphabetical joke (EN 'Bunting, Surplus' = one B card) | `B, B, Bridge-Turnier, Banner und Wimpel, Überschuss` | APPLIED |
| 83 | note-word | 582 | `hatte die Briefe geschrieben, die Fiona in Angst und Schrecken versetzten. Oder seine Sorgfalt bei der Aufbewahrung dieser Briefe hatte jemand anderem erlaubt, sie zu schreiben,` | REVERSED DEDUCTION: German said Theo wrote the LETTERS and someone else wrote the letters; EN = wrote the NOTES / care of the letters let someone else write the notes | `hatte die Zettel geschrieben, die Fiona in Angst und Schrecken versetzten. Oder seine Sorgfalt bei der Aufbewahrung jener Briefe hatte es jemand anderem ermöglicht, die Zettel zu schreiben,` | APPLIED |
| 84 | term | 589 | `keinen Pfennig` | US setting - Cent as elsewhere | `keinen Cent` | APPLIED |
| 85 | term | 610 | `in das kleine Lesezimmer gesperrt` | sitting room | `in das kleine Wohnzimmer gesperrt` | APPLIED |
| 86 | term | 610 | `er ist in meine Eingangshalle gelaufen` | EN 'my lobby'; front hall is a different room | `er ist in meine Lobby gelaufen` | APPLIED |
| 87 | term | 623 | `Er ist in meine Eingangshalle gelaufen.` | echo of Fiona's words | `Er ist in meine Lobby gelaufen.` | APPLIED |
| 88 | honorific | 630 | `die Teigtaschen von Herrn Kims Frau` | Mr. Kim | `die Teigtaschen von Mr. Kims Frau` | APPLIED |
| 89 | term | 630 | `mit den Fausthandschuhen des Strickkreises` | mittens = Fäustlinge throughout | `mit den Fäustlingen des Strickkreises` | APPLIED |
| 90 | cider | 630 | `Apfelweinbuden und Stände` | ruling 6 | `Buden mit heißem Apfelsaft und Stände` | APPLIED |
| 91 | cider | 633 | `am Apfelweinstand auf` | ruling 6 | `am Apfelsaftstand auf` | APPLIED |
| 92 | honorific | 633 | `dass Frau Claus ihre Sternbilder` | Mrs. Claus | `dass Mrs. Claus ihre Sternbilder` | APPLIED |
| 93 | cider | 633 | `zwei Bechern Apfelwein` | ruling 6 | `zwei Bechern Apfelsaft` | APPLIED |
| 94 | term | 633 | `ein Paar Fausthandschuhe in die Hand` | mittens | `ein Paar Fäustlinge in die Hand` | APPLIED |
| 95 | honorific | 635 | `lediglich Frau Pelletier vom` | Mrs. Pelletier | `lediglich Mrs. Pelletier vom` | APPLIED |
| 96 | honorific | 635 | `Frau Pelletier sah ratlos` | Mrs. Pelletier | `Mrs. Pelletier sah ratlos` | APPLIED |
| 97 | cider | 636 | `am Apfelweinstand, in ihrem Parka` | ruling 6 | `am Apfelsaftstand, in ihrem Parka` | APPLIED |
| 98 | address | 637 | `„Du sahst aus, als würdest du Frau Pelletier gleich umwerfen“` | Noriko formal until the EN puts them on first names (ch25) | `„Sie sahen aus, als würden Sie Mrs. Pelletier gleich umwerfen“` | APPLIED |
| 99 | cider | 639 | `von ihrem Apfelwein.` | ruling 6 | `von ihrem Apfelsaft.` | APPLIED |
| 100 | address | 639 | `zwei von euch, die` | Noriko formal | `zwei von Ihnen, die` | APPLIED |
| 101 | address | 642 | `„Du weißt, wo die Wache ist.` | Noriko formal | `„Sie wissen, wo die Wache ist.` | APPLIED |
| 102 | address | 642 | `„Dein Pinguin hat` | Noriko formal | `„Ihr Pinguin hat` | APPLIED |
| 103 | address | 643 | `„Sag ihr das bloß nicht“` | Noriko formal | `„Sagen Sie ihr das bloß nicht“` | APPLIED |
| 104 | name | 644 | `in der wir Schneeball gefunden` | Snowball | `in der wir Snowball gefunden` | APPLIED |
| 105 | clue | 654 | `Der Saphir in seinem Herzen: fünf Wörter` | KEY CLUE (was a 3rd variant) | `Der Saphir in ihrem Herzen: fünf Wörter` | APPLIED |
| 106 | note-word | 654 | `die im Erpresserbrief genau so standen` | note != letters | `die im Erpresserzettel genau so standen` | APPLIED |
| 107 | term | 659 | `in ein Foyer voll von Festivalgästen getragen` | lobby | `in eine Lobby voller Festivalgäste getragen` | APPLIED |
| 108 | mistranslation | 673 | `die mir gerade direkt ins Gesicht gesehen` | 'gerade' (just now) not in EN - she said it on earlier visits | `die mir direkt ins Gesicht gesehen` | APPLIED |
| 109 | address | 676 | `„geht es dir gut? Wirklich. Du siehst gar nicht gut aus.“` | Jessica <-> Vera formal (Vera always Sie) | `„geht es Ihnen gut? Wirklich. Sie sehen gar nicht gut aus.“` | APPLIED |
| 110 | clue | 680 | `katalogisiert, den Saphir in ihrem Herzen, und dann` | KEY CLUE kept in the identical nominative form | `katalogisiert – der Saphir in ihrem Herzen –, und dann` | APPLIED |
| 111 | address | 732 | `„Setzt euch bitte, ihr beiden“` | Noriko with Theo/Vera = professional, formal (ruling 2) | `„Setzen Sie sich bitte, Sie beide“` | APPLIED |
| 112 | address | 732 | `danach werdet ihr beide jeweils` | formal | `danach werden Sie beide jeweils` | APPLIED |
| 113 | address | 732 | `Setzt euch.“` | formal | `Setzen Sie sich.“` | APPLIED |
| 114 | note-word | 735 | `„Die Erpresserbriefe an Fiona` | confrontation: notes != Blackburn letters | `„Die Erpresserzettel an Fiona` | APPLIED |
| 115 | clue | 735 | `als der Saphir im Herzen bezeichnet` | KEY CLUE in the confrontation | `als der Saphir in ihrem Herzen bezeichnet` | APPLIED |
| 116 | address | 740 | `in deinem Ablagekorb` | Jessica -> Vera formal | `in Ihrem Ablagekorb` | APPLIED |
| 117 | address | 740 | `Du hattest die Urkunde. Und du hattest die Beine, Vera.` | Vera formal | `Sie hatten die Urkunde. Und Sie hatten die Beine, Vera.` | APPLIED |
| 118 | address | 740 | `Ich bin dir an jenem Morgen selbst auf der Treppe begegnet, mit deinen Parkausweisen.` | Vera formal | `Ich bin Ihnen an jenem Morgen selbst auf der Treppe begegnet, mit Ihren Parkausweisen.` | APPLIED |
| 119 | address | 740 | `Das warst du.“` | Vera formal | `Das waren Sie.“` | APPLIED |
| 120 | grammar | 742 | `Sie wog sich ein wenig` | rocking = wiegen/wiegte (wog = weighed) | `Sie wiegte sich ein wenig` | APPLIED |
| 121 | address | 745 | `„Ihr habt es beide freimütig zugegeben, und das zählt mehr, als ihr beide jetzt noch begreifen könnt.` | Noriko with Theo/Vera formal | `„Sie haben es beide freimütig zugegeben, und das zählt mehr, als Sie beide jetzt noch begreifen können.` | APPLIED |
| 122 | note-word | 748 | `Die beiden Briefe wurden zu Beweismitteln` | the two NOTES became evidence | `Die beiden Zettel wurden zu Beweismitteln` | APPLIED |
| 123 | address | 760 | `„Du hast etwas Falsches getan“` | Vera formal | `„Sie haben etwas Falsches getan“` | APPLIED |
| 124 | address | 760 | `„Und du büßt dafür` | Vera formal | `„Und Sie büßen dafür` | APPLIED |
| 125 | address | 760 | `Aber du hast es genau in dem Moment zugegeben, als man dich fragte, Vera. Du hast nicht gelogen und dich nicht herausgewunden.` | Vera formal | `Aber Sie haben es genau in dem Moment zugegeben, als man Sie fragte, Vera. Sie haben nicht gelogen und sich nicht herausgewunden.` | APPLIED |
| 126 | address | 760 | `Das ist der Teil von dir, der` | Vera formal | `Das ist der Teil von Ihnen, der` | APPLIED |
| 127 | address | 760 | `dass du daran festhältst. Der Weg zurück ist auch für dich lang.` | Vera formal | `dass Sie daran festhalten. Der Weg zurück ist auch für Sie lang.` | APPLIED |
| 128 | address | 760 | `Lass dir von niemandem einreden, es gäbe keinen, und vor allem rede es dir nicht selbst ein.` | Vera formal | `Lassen Sie sich von niemandem einreden, es gäbe keinen, und vor allem reden Sie es sich nicht selbst ein.` | APPLIED |
| 129 | note-word | 762 | `Die Briefe hatten aufgehört.` | EN 'The notes had stopped' | `Es kamen keine Zettel mehr.` | APPLIED |
| 130 | term | 776 | `diese peinlichen kleinen Tombolen` | plural matches 780 'Tombolas' | `diese peinlichen kleinen Tombolas` | APPLIED |
| 131 | grammar | 789 | `im Sterben lag, der man eingetrichtert hatte, dankbar` | relative clause attached 'told to be grateful' to the dying MOTHER; EN = Constance | `im Sterben lag; man hatte dem Mädchen eingetrichtert, dankbar` | APPLIED |
| 132 | name | 807 | `Schneeball trug` | Snowball | `Snowball trug` | APPLIED |
| 133 | address | 815 | `ich frage Sie!` | Bram du | `ich frage dich!` | APPLIED |
| 134 | grammar | 852 | `Greta hatte seit vierzig Jahren dieselbe Zimtschnecke gebacken. Sie hatte sie am Morgen nach dem Begräbnis ihres Mannes gebacken, weil sie nicht gewusst hatte, wohin mit ihren Händen.` | blurb tense drift (EN present-perfect/present; German pluperfect then present) | `Greta backt seit vierzig Jahren dieselbe Zimtschnecke. Sie hat sie am Morgen nach dem Begräbnis ihres Mannes gebacken, weil sie nicht wusste, wohin mit ihren Händen.` | APPLIED |
| 135 | mistranslation | 868 | `der bereits doppelt so groß wie der von allen anderen` | EN 'half again the size' = 1.5x | `der bereits anderthalbmal so groß wie der von allen anderen` | APPLIED |
| 136 | grammar | 869 | `das Bett hütete oder Enkelkinder hütete` | doubled verb 'hütete' | `das Bett hütete oder auf Enkelkinder aufpasste` | APPLIED |
| 137 | mistranslation | 874 | `meinen Tannenzapfenschuppen zu` | EN 'my scales of balsam' (the overlapping sprigs), not pinecone scales | `meinen Reisigschuppen zu` | APPLIED |
| 138 | units | 875 | `Nicht die Meilen. Es waren eine ganze Menge davon gewesen, aber die Meilen meinte ich nicht.` | spelled-out imperial 'miles' (no number) - SAFE: metric word swap, nothing to compute | `Nicht die Kilometer. Es waren eine ganze Menge davon gewesen, aber die Kilometer meinte ich nicht.` | APPLIED |
| 139 | grammar | 879 | `Ihr Bagage tut es ja sonst nicht für euch selbst.` | 'Ihr Bagage' ungrammatical (die Bagage) | `Ihr tut es ja sonst nicht für euch selbst.` | APPLIED |
| 140 | mistranslation | 879 | `mit dem Balsam, Schokolade` | 'balsam' = balsam fir (Tannenreisig elsewhere); German 'Balsam' = ointment | `mit dem Tannenduft, Schokolade` | APPLIED |
| 141 | mistranslation | 879 | `gelagert über kaltem` | 'laid over' (gelagert = stored) | `gelegt über kaltem` | APPLIED |
| 142 | term | 884 | `jeder Penny geht` | Cent | `jeder Cent geht` | APPLIED |
| 143 | mistranslation | 573 | `einem herrlich aufgetakelten Wrack` | EN 'a glorious shipwreck' ('aufgetakelt' = dolled up/rigged) | `einem herrlichen Schiffbruch` | APPLIED |
| 144 | mistranslation | 600 | `Nicks Worte aus der Nacht, in der wir die Liste sahen, stiegen` | EN 'the night of the list' (she wrote it; they did not 'see' it) | `Nicks Worte aus der Nacht mit der Liste stiegen` | APPLIED |
| 145 | dialogue | 386 paras | `„…“` / `‚…‘` | German fiction house standard is »…« / ›…‹ (dossier, ruling 1); the book used „…“ throughout | `»…«` / `›…‹` | APPLIED |

## Decision items (also in PROOFREAD_DECISIONS.md)
| ID | Class | Para | German | Issue | Options | Status |
|---|---|---|---|---|---|---|
| DE2-D1 | 7 Scene break | ch10 para 379 (and back-matter 849/857/908) | * * * | English has no break here - Nick's explanation runs straight on; the marker splits one scene. Deleting a paragraph is structural, so not done here. | Delete para 379 at the formatting stage; back-matter separators are the formatter's. | OPEN |
| DE2-D2 | Structure (formatter) | 14, chapter headings | Kapitel 31 | Pre-flight 'chapter 31 detected twice' = the Inhaltsverzeichnis lists only 'Kapitel 31' (Kapitel 1-30 missing) plus the real ch31 heading; 0 Heading 1; preflight sees no back matter. check_matter.py itself reports OK. | Formatter: restore Heading 1 x31, regenerate TOC. Not touched. | NOTE |
| DE2-D3 | 5 Register | ch6 265/270/271, ch31 826 | Sie und dieser lächerliche Vogel / Du wirst dasselbe für den Nächsten tun | Mark Redfern says Sie to Jessica, Jessica says du to Mark. Mark is not in your 2026-10-13 address table. | (a) keep (natural older-woman du / younger-man Sie); (b) du both ways; (c) Sie both ways. | OPEN |
| DE2-D4 | Italics | ch20 para 623 | Er ist in meine Lobby gelaufen. Er stand an meinem eigenen Tresen. ... | Jessica recalling Fiona's words is italic in German, plain in English (web DE-D13). Removing it changes the italic run list. | Keep or remove the italic. | OPEN |
| DE2-D5 | 6 Term (series) | 84, 215-251, 392-408, 244 | Handarbeitskreis / Strickrunde / Zirkel -> Strickkreis / Kreis | German Book 1 (corrected) uses Strickkreis (2x) / Kreis (30x); this book mixed five names. APPLIED to match Book 1; Martha's line now 'Genau das ist der Sinn eines Kreises' and is echoed exactly in ch24/ch29. | Confirm (applied; reversible). | APPLIED-CONFIRM |
| DE2-D6 | Key clue | 101,102,119,577,578,579,654,680,735 | der Saphir in ihrem Herzen | Was 3 variants (im Herzen / in seinem Herzen / in ihrem Herzen) under a 'fünf Wörter' claim the main variant (4 words) did not meet. Now 'der Saphir in ihrem Herzen' (5 words; 'ihrem' = die Brosche) in the note, Jessica's readings, Theo's card and the confrontation. The note and the ch23 recap were recast as a dash apposition so even the article is identical (nominative). 'fünf Wörter' x4 now true. | Confirm (applied). | APPLIED-CONFIRM |

## Notes (no change)
- 'fünfzig Meilen' (ch2) kept per ruling 4.
- Stray <bt> removed (7): Yarn Tales x3, Winter Wonderland Inn, The Holly Jolly Bakery (+ the English 'The' after German 'der'), Holly Jolly Bakery, Gazette. Kept 8: Inn Trouble x2, Frost and Found, Flour Play x5.
- Mr./Mrs. kept (edition + German Book 1 convention); 9 stray Herr/Frau normalised (ruling 7).
- English source note: MAXIMILIAN -> Max saves seven letters, the text says six (follows the English).
