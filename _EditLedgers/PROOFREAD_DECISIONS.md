# PROOFREAD DECISIONS

## Inn Trouble - ASSEMBLED - FORMATTED_French

### FR-D1. 7 Scene breaks — para 1370, 1386, 1488
- Quote: `***`
- Issue: English has NO `* * *` markers. At these positions the English has only blank spacer paragraphs (EN 918–921 after ch31, 929–932 after the What's Next? blurb, and before the closing 'Flour Play is coming soon!' line).
- Recommendation: Delete the three `***` lines at the formatting stage (or replace with an empty paragraph) so the edition matches the English; not deleted here because it changes paragraph count.
- Why not automatic: Options: (a) remove, (b) keep as a typographic ornament. Recommend (a).

### FR-D2. 5 Dialogue punctuation — para whole book
- Quote: `« Allô ? » … / — Oui, bon, tu viens, lui ai-je dit.`
- Issue: Three dialogue systems are mixed: guillemets « » (ch2–5, 8–13, 15–19, 21, 23–29, most of 31), em-dash tirets (ch1, 6, 14, 20, 30, part of 31), and a hybrid «…/— continuation… » (ch7). Within the « » chapters there are also English-style patterns: comma inside the closing guillemet (ch15, e.g. 772 « Elle sait ce qu'il y a dedans, » a dit Olivia), closing guillemet placed after the incise (e.g. 189, 198, 205, 816, 819, 891, 915, 925, 1406, 1418, 1426, 1428, 1438, 1450, 1462, 1478), and narration left inside the quotation in em-dash chapters (e.g. 954, 964, 966, 1324, 1358).
- Recommendation: Normalise the whole book to « » with incises inside (« …, ai-je dit, … ») and — only for change of speaker inside a quotation, as done in 24 of 31 chapters. Narration-inside-quote cases I could settle without restyling (347, 617, 631, 639, 877) were fixed.
- Why not automatic: Book-wide punctuation restyle (hundreds of paragraphs) is a house-style decision, not a single-answer fix.

### FR-D3. 1 Untranslated (front matter) — para 4
- Quote: `Book 2`
- Issue: Series volume number left in English. The edition uses neither 'Tome' nor 'Livre' anywhere else.
- Recommendation: Tome 2
- Why not automatic: Both 'Tome 2' and 'Livre 2' are in use in French; 'Tome' is the conventional series label. Other front-matter boilerplate (5 lines) was translated and applied.

### FR-D4. 2 Omission (TOC) — para 22
- Quote: `Chapitre 31`
- Issue: Translated Table of Contents lists only 'Chapitre 31' then the back matter; entries Chapitre 1–30 (EN 22–51) are missing.
- Recommendation: Regenerate the TOC in the formatter (it will also need the 35 missing Heading 1 styles).
- Why not automatic: Restoring 30 TOC lines adds paragraphs.

### FR-D5. Book title / <bt> markers — para 727, 1011, 1248
- Quote: `<bt>The Holly Jolly Bakery</bt> / <bt>the sapphire at its heart</bt> / <bt>Gazette</bt>`
- Issue: Three <bt> spans wrap things that are not book titles: a bakery name (plain elsewhere, 1426), the newspaper name, and — worst — the English phrase 'the sapphire at its heart', which is the key clue and is printed in English in the middle of a French sentence (1011). Book-title spans (Flour Play ×5) are correct; title page keeps 'Inn Trouble' untranslated — correct.
- Recommendation: 1011: replace `<bt>the sapphire at its heart</bt>` with `Le saphir en son cœur` (no markers). 727 and 1248: drop the markers, keep text.
- Why not automatic: Removing markers changes the bt-span count (8 → 5), which this pass must keep equal.

### FR-D6. Italics added by translator — para 655, 662, 974, 1160, 1420 (+117, 1051)
- Quote: `registres fonciers / Gazette / Il est entré dans mon hall… / le saphir en son cœur / je n'ai pas cessé de te surveiller`
- Issue: Italic in French but not in the English. Also 117 and 1051 contained literal `<it>…</it>` / `<hi>…</hi>` tags printed as text: I removed the tags (text unchanged), so 'broche' (117) and 'le saphir en son cœur' (1051) are now roman.
- Recommendation: Remove the added italics to match the English; optionally keep 974/1420 (quoted speech/looks) if Lisa likes them.
- Why not automatic: Italic additions/removals are formatting decisions. All 15 English italic runs are present in French.

### FR-D7. 1 Untranslated (in-world sign) — para 297
- Quote: `FROST FALLS THROUGH THE YEARS`
- Issue: Exhibition banner left in English (italic, as in EN). The sentence then jokes that the last S was crammed in.
- Recommendation: FROST FALLS AU FIL DES ANNÉES (still ends in S, joke survives)
- Why not automatic: Could be read as a deliberately untranslated in-world sign; other labels (drawer cards, catalog cards, exhibit card) are translated.

### FR-D8. 5 Register tu/vous — para Vera 645 vs 1041/1170/1209; Jamal 684 vs 704/710/714; Mark 387 vs 396/398
- Quote: `Vous avez l'air épuisée / Tu n'as pas du tout bonne mine`
- Issue: Jessica's address to three characters switches between vous and tu with no story trigger. (Neil ch4, Sam ch17, Noriko ch21, the stranger in ch6 and the second blackmail note were clear-cut against a dominant pattern and were fixed.)
- Recommendation: Vera: vous throughout (fix 1041, 1170, 1209). Jamal: tu (he vouvoies her; fix 684). Mark: tu (fix 387).
- Why not automatic: Which register is intended for each pair is a characterisation choice.

### FR-D9. 6 Term (penguin) — para 306, 328, 375, 385, 386, 421, 682, 745, 895, 1307
- Quote: `pingouin`
- Issue: Pip is 'pingouin' 10× and 'manchot' 7×. Zoologically a penguin is a manchot; pingouin is the everyday word.
- Recommendation: manchot throughout (or pingouin throughout in children's dialogue only).
- Why not automatic: Word choice.

### FR-D10. 3 False friend (mittens) — para 337 + 12 more
- Quote: `mitaines`
- Issue: In France 'mitaines' are fingerless gloves; children's mittens are 'moufles'. Fine for Canadian French.
- Recommendation: moufles throughout, unless the target market is Québec.
- Why not automatic: Depends on target market.

### FR-D11. 8 Units (round figure — ESCALATE) — para 185
- Quote: `la plus riche à cinquante kilomètres à la ronde`
- Issue: EN 'the richest for fifty miles' (≈80 km). The translator converted the number but not the distance.
- Recommendation: à quatre-vingts kilomètres à la ronde / à des lieues à la ronde
- Why not automatic: Round/rhetorical figure: conversion loses roundness — escalate per unit rule. All SAFE literal units were checked: 66→'une dizaine de centimètres' OK, 456→'moins de deux mètres' OK, 694→'quelques mètres' OK, 936/973→'quinze centimètres' OK; 108, 253, 898 fixed (pouce → cm).

### FR-D12. 6 Tense drift — para ch9 (507–549), ch22 (1009–1022); scattered passé simple (137, 448, 1172)
- Quote: `J'avais eu l'intention… Il avait levé les yeux…`
- Issue: Two whole chapters are narrated in the plus-que-parfait where the English is simple past and the rest of the book uses passé composé; it reads as background to a missing main line.
- Recommendation: Recast ch9 and ch22 in passé composé.
- Why not automatic: Chapter-wide recast is beyond sentence-level fixing.

### FR-D13. 6 Term (the green / the note) — para e.g. 53, 170, 266, 374, 934, 1029, 1148, 1464
- Quote: `place gazonnée / square / pelouse / place du village / parc`
- Issue: 'the green' is rendered six different ways; 'the (blackmail) note' alternates mot / note / lettre.
- Recommendation: the green = 'la place' (dominant); the note = 'le mot' (or 'la lettre') consistently.
- Why not automatic: Picking the house term is a judgment call; fixed only unambiguous cases (terrain vague).

## Inn Trouble - ASSEMBLED - FORMATTED_Norwegian

### NO-D1. Title localisation: para 0
- Quote: `Kapittel 1`
- Issue: The title page shows a chapter label where the English has the book title 'Inn Trouble'. Chapter 1's own heading is at para 37, so this is a duplicate label, not the chapter start. The French edition keeps 'Inn Trouble' untranslated.
- Recommendation: Replace with `Inn Trouble` (untranslated, as the brief requires for book titles).
- Why not automatic: The brief makes every title-page and title-localisation question a decision.

### NO-D2. 2 Omission (TOC): para 22
- Quote: `Kapittel 31`
- Issue: The Table of Contents lists only 'Kapittel 31' and then the back matter. Entries for Kapittel 1–30 (EN 22–51) are missing.
- Recommendation: Regenerate the TOC in the formatter. It also needs the 35 missing Heading 1 styles.
- Why not automatic: Restoring 30 TOC lines adds paragraphs.

### NO-D3. 7 Scene breaks: para 1527, 1543, 1661
- Quote: `* * *`
- Issue: The English has no `* * *` markers. At these positions it has only blank spacer paragraphs: after ch31 before the first 'Flour Play is coming soon' line, after the What's Next? blurb, and before the closing 'Flour Play is coming soon!'.
- Recommendation: Delete the three lines at the formatting stage, or turn them into empty paragraphs.
- Why not automatic: Deleting them changes the paragraph count.

### NO-D4. `<bt>` spans on things that are not book titles: para 277, 305, 317, 710, 795, 1126
- Quote: `<bt>Gazette</bt>` (277, 305, 317) / `<bt>Winter Wonderland Inn</bt>` (710, 1126) / `<bt>The Holly Jolly Bakery</bt>` (795)
- Issue: These markers wrap a newspaper, the inn and the bakery. If they are kept, the stamping step will treat these names as book titles. The real book-title spans (Flour Play ×5) are correct. 'Frost and Found' and 'Inn Trouble' in Books in This Series (18–19) are not in `<bt>`; this is noted only.
- Recommendation: Remove the markers and keep the text. At 795, also consider 'Holly Jolly Bakery' without the English article, as the excerpt has it (1589).
- Why not automatic: Removing markers changes the bt-span count (11 → 5), and this pass must keep that count equal.

### NO-D5. 6 Term (the Gazette): para 43, 93, 277, 305, 317, 717, 1176, 1381, 1569
- Quote: `Lokalaviskontoret` / `lokalavisens` / `Gazette` / `Avisen` / `avisen` / `avisa`
- Issue: The town newspaper (EN 'the Gazette', a proper name) appears in five different forms.
- Recommendation: Use 'Gazette' as the name throughout, e.g. 'Gazette-kontoret' (43), 'Gazettes' (93), 'Gazette' (717). 'avisen'/'avisa' can stay where the English says 'the paper'.
- Why not automatic: This is a choice between keeping the proper name and localising it to 'lokalavisen'. It also overlaps with the bt markers in NO-D4.

### NO-D6. Italics added by the translator: para 245, 969, 983, 1066, 1104
- Quote: `å, se` + `er det en pingvin` (245) / `Bakerikvitteringer`, `Bidrag til musikkpaviljongen` (969) / `Bridgeturnering`, `Bannerpynt`, `Overskudd` (983) / `Han har gått inn i foajeen min…` (1066) / `Safiren i hjertet` (1104)
- Issue: These are italic in the Norwegian and roman in the English. All 15 English italic runs are present in the Norwegian. The English text inside the 969/983/1104 runs was translated in this pass, and the italics were left as they were.
- Recommendation: Remove the added italics. Optionally keep 1066, Fiona's words recalled, if Lisa likes it.
- Why not automatic: Adding or removing italics is a formatting decision.

### NO-D7. 5 Dialogue punctuation: ch6 (346–423), ch12 (715–745), ch18 (922–960), ch27 (1285–1321); also e.g. 799, 809, 823, 827
- Quote: `«Han liker henne ikke,» betrodde Emma meg` / `– Den har holdt på sånn siden daggry. – Hun skjøv bollene mine over disken.`
- Issue: 27 chapters use Norwegian dash dialogue. Four chapters use « » guillemets instead, and ch6, ch12 and ch18 also place the comma inside the closing guillemet, English-style. In the dash chapters, some lines put a dash before plain narration, so the narration looks like speech (ch14). I fixed only the missing dashes where speech resumes after an attribution (about 25 places).
- Recommendation: Normalise the whole book to dash dialogue (– …, sa hun. – …), with no dash before narration.
- Why not automatic: This is a book-wide punctuation restyle across hundreds of paragraphs, so it is a house-style decision.

### NO-D8. 8 Units (round figure — ESCALATE): para 124
- Quote: `de rikeste på fem mil`
- Issue: EN 'the richest for fifty miles' is about 80 km, which is 8 Norwegian mil. The translator turned 50 miles into 50 km. All SAFE literal units were checked or fixed: 42 'ti centimeter' OK; 84, 268 and 1471 fixed (tomme → cm); 686 'to meter' OK; 1083 'et par meter' OK; 1551 and 1640 'femten centimeter' OK. 1412 'fire mål' (four acres) was corrected to 'seksten mål'.
- Recommendation: `de rikeste i milevis omkring` keeps the rhetoric. Alternatively use `på åtte mil`.
- Why not automatic: This is a round, rhetorical figure, so the unit rule says escalate.

### NO-D9. 3 Mistranslation (plant): para 45
- Quote: `med en enslig kvist bitterhet for sesongens oransje farge`
- Issue: 'bitterhet' means bitterness. EN 'a sprig of bittersweet' is the orange-berried American vine.
- Recommendation: `med en enslig kvist med oransje bær for sesongens skyld`. Use 'klatrebeinved' if Lisa wants a botanical name.
- Why not automatic: There is no settled everyday Norwegian name for American bittersweet.

### NO-D10. 4 Proper name (the dog): para 361, 375, 379, 1091, 1416 vs 1445, 1455, 1463, 1465, 1477, 1569, 1609
- Quote: `Snøball` / `Snowball`
- Issue: Martha's dog is 'Snøball' in ch6, ch21 and ch30 and 'Snowball' in ch31 and the excerpt.
- Recommendation: Use `Snowball` throughout (series rule: names stay English), or `Snøball` throughout if the Norwegian Book 1 localised it. Check Frost and Found NO.
- Why not automatic: It depends on how Book 1 handled the name.

### NO-D11. 6 Term (blackmail note; lobby): note e.g. 116/127 vs 131/874/1024; lobby 49–87 vs 110 onward
- Quote: `brevet` / `lappen`; `lobbyen` / `foajeen`
- Issue: The blackmail note alternates between 'brevet' (21×) and 'lappen' (22×), sometimes within one chapter (ch2, ch16, ch20). The inn lobby is 'lobbyen' in ch1 and 'foajeen' afterwards. I already settled 'utpressingsbrevet' and the inconsistent 'utpressingstrussel', 'beskjeden' and 'notatene' where they occurred.
- Recommendation: Use 'brevet' for the note (it is a typed-up demand on stationery) and 'foajeen' for the lobby.
- Why not automatic: Both words are acceptable Norwegian. Choosing one means about 25 stylistic replacements.

## Inn Trouble - ASSEMBLED - FORMATTED_German

### DE-D1. 7 Scene breaks — para 455, 1127, 1143, 1245
- Quote: `* * *`
- Issue: English has NO `* * *` markers. 455 sits mid-chapter 10 between EN 426 and 427 (no break in EN — Nick's explanation continues straight on); 1127 = EN blank spacers 917–921 after the end of ch31; 1143 = EN blanks 929–932 after the What's Next? blurb; 1245 = EN blanks 983–987 before the closing 'Flour Play is coming soon!'.
- Recommendation: Delete all four at the formatting stage (455 especially, as it splits a continuous scene); the other three may be replaced by plain spacing.
- Why not automatic: Removing them changes paragraph count.

### DE-D2. 2 Omission (TOC) — para 22
- Quote: `Kapitel 31`
- Issue: The translated Table of Contents lists only 'Kapitel 31' followed by the back matter; entries Kapitel 1–30 (EN 22–51) are missing. (Formatter also produced 0 Heading 1 paragraphs.)
- Recommendation: Regenerate the TOC in the formatter once the 35 Heading 1 styles are restored.
- Why not automatic: Restoring 30 TOC lines adds paragraphs.

### DE-D3. `<bt>` spans on things that are not book titles — para 38, 40, 561, 1149, 1167, 1183, 1221
- Quote: `<bt>Yarn Tales</bt>` (38, 1149, 1221) / `<bt>Winter Wonderland Inn</bt>` (40) / `<bt>The Holly Jolly Bakery</bt>` (561) / `<bt>Gazette</bt>` (1167) / `<bt>Holly Jolly Bakery</bt>` (1183)
- Issue: 7 of the 15 spans wrap a shop, the inn, a bakery or the newspaper — none are book titles, and the same names appear unmarked elsewhere (e.g. Yarn Tales 267, Gazette 38/269). 561 also reads 'auf dem Tresen der The Holly Jolly Bakery' (German article + English 'The'). The 8 genuine title spans (Inn Trouble ×2, Frost and Found, Flour Play ×5) are correct; the title page keeps 'Inn Trouble' untranslated — correct.
- Recommendation: Drop the markers on the 7 non-titles, keep the text; at 561 also drop the English article: 'auf dem Tresen der Holly Jolly Bakery'.
- Why not automatic: Removing markers changes the bt-span count (15 → 8), which this pass must keep equal.

### DE-D4. 6 Term / adaptation (KEY CLUE, word count) — para 28, 111, 112, 129, 726, 728, 730, 744, 829, 867, 953
- Quote: `der Saphir im Herzen` (111, 112, 129, 726, 728, 730, 953) / `Der Saphir in seinem Herzen: fünf Wörter` (829) / `den Saphir in ihrem Herzen` (867) / `dieselben fünf Wörter` (730, 744 'Die fünf Wörter')
- Issue: The clue 'the sapphire at its heart' is rendered three ways, and the dominant German form ('der Saphir im Herzen') has FOUR words while the text says 'fünf Wörter' three times (730 ×2, 744, 829). 953 had the phrase in English — applied as 'der Saphir im Herzen' (dominant form) so it can be changed with the rest. (28, the blurb, now says 'den Stein im Herzen der Brosche' as in EN.)
- Recommendation: Option A (recommended): unify on the five-word 'der Saphir in ihrem Herzen' (ihrem = der Brosche) at 111, 112, 129 ×2, 726, 728, 730, 829, 867, 953 — keeps 'fünf Wörter' true and fixes 829's wrong 'seinem'. Option B: keep 'der Saphir im Herzen' everywhere (fix 829, 867) and change 'fünf' → 'vier' at 730 ×2, 744, 829.
- Why not automatic: Changing a stated word count / the wording of the central clue is an adaptation decision.

### DE-D5. 1 Untranslated / 6 Term (honorifics) — para Mr./Mrs. ×56 vs Herr/Frau ×9 (503, 504, 604, 606, 804, 807, 809 ×2)
- Quote: `Mrs. Claus` (39×), `Mr. Worthington`, `Mr. Kim` … vs `Frau Pelletier` (503, 809), `Frau Claus` (504, 807), `Herrn Kim` / `Herr Kim` (604, 606), `Herrn Kims` (804)
- Issue: The edition mostly keeps English honorifics (a common convention in German translations of US-set fiction, and 'Mrs. Claus' is the established German name of Santa's wife), but switches to Frau/Herr nine times; Mrs. Pelletier and Mr. Kim appear both ways.
- Recommendation: Keep Mr./Mrs. throughout and normalise the nine Frau/Herr instances (Frau Pelletier → Mrs. Pelletier, Frau Claus → Mrs. Claus, Herr(n) Kim(s) → Mr. Kim(s)). Alternative: Herr/Frau throughout (65 edits; 'Frau Claus' loses the Santa association).
- Why not automatic: House-style choice affecting 65 places.

### DE-D6. 4 Proper name (the dog) — para 312, 319, 321, 818, 1056 vs 1073, 1081, 1085, 1087, 1095, 1167, 1199
- Quote: `Schneeball` (5×) vs `Snowball` (7×)
- Issue: Martha's dog is translated as 'Schneeball' in ch6, ch21 and ch30 but kept as 'Snowball' in ch31 and the Flour Play excerpt.
- Recommendation: 'Snowball' throughout (series rule: character names stay English; matches NO-D10).
- Why not automatic: Name-localisation choice.

### DE-D7. 6 Term (the circle) — para 94, 267, 269, 270, 294, 296, 303, 306, 469, 479, 485, 601, 804, 906, 908, 1039, 1045 …
- Quote: `Handarbeitskreis` (94) / `Strickrunde` (267–303) / `Strickkreis` (306, 804, 906, 1039, 1045) / `Zirkel` (469, 479, 485) / `Kreis` (601, 908, 1045, excerpt)
- Issue: The knitting circle has five names. 'Zirkel' (a drawing compass / esoteric circle) is the least natural. Martha's key line 'That's the whole point of a circle' is 'Sinn einer Strickrunde' at 296 but 'Sinn eines Kreises' when echoed at 908 and 1045.
- Recommendation: 'Strickkreis' at first mention in a scene, 'Kreis' thereafter; replace Handarbeitskreis/Strickrunde/Zirkel; make 296 read 'Genau das ist der Sinn eines Kreises' so the echoes at 908/1045 match.
- Why not automatic: Word choice across ~40 places.

### DE-D8. 5 Register (Jessica → Vera) — para 488 vs 859, 1002
- Quote: `Danke, Vera, Sie sehen erschöpft aus` (488) vs `geht es dir gut? Wirklich. Du siehst gar nicht gut aus` (859) / `Du hast etwas Falsches getan … ` (1002)
- Issue: Jessica says Sie to Vera in ch11 and du in ch23 and ch27 with no trigger; Vera always says Sie/'Mrs. Claus' to Jessica.
- Recommendation: Sie throughout (fix 859 and the whole 1002 speech), mirroring Vera's Sie; alternatively du from ch23 on if Lisa reads ch27 as a deliberate softening.
- Why not automatic: Characterisation choice.

### DE-D9. 5 Register (Noriko ↔ Jessica) — para 326, 328 vs 811–817, 921–925
- Quote: `Und Ihre Rentiere stehen dieses Jahr nicht auf dem Programm` / `Sagen Sie es Bram` (ch6) vs `Du sahst aus, als würdest du Frau Pelletier gleich umwerfen` (811), `Du verstehst, dass ich das …` (921)
- Issue: Noriko uses Sie at their first meeting (ch6) and du from ch21 on (both ways), while still calling her 'Mrs. Claus'.
- Recommendation: du throughout (change 326 'Ihre' → 'deine', 328 'Sagen Sie' → 'Sag'); or keep ch6 Sie if Lisa wants the first meeting formal.
- Why not automatic: Characterisation choice; the shift could be read as growing familiarity.

### DE-D10. 8 Units (round figure — ESCALATE) — para 119
- Quote: `die reichste im Umkreis von fünfzig Meilen`
- Issue: EN 'the richest for fifty miles' is a round, rhetorical figure. Literal conversion is 80 km.
- Recommendation: 'die reichste im Umkreis von achtzig Kilometern' or idiomatic 'die reichste weit und breit'. (The 'reichsten' → 'reichste' grammar fix was applied.)
- Why not automatic: Round-number unit conversion (ESCALATE rule).

### DE-D11. Adaptation (banner joke) — para 231
- Quote: `FROST FALLS IM LAUFE DER JAHRE, wobei das letzte S ganz am Ende hineingequetscht war`
- Issue: The banner was translated, but the sentence still jokes that the last S was squeezed in — the German banner ends in E.
- Recommendation: Change 'das letzte S' → 'das letzte E' (simplest), or keep the banner in English as an in-world sign so the S joke works.
- Why not automatic: Letter-based detail; adaptation.

### DE-D12. Adaptation (alphabetical catalog cards) — para 722, 736
- Quote: `Ich arbeitete mich gerade durch die B-Karten – Bäckereiquittungen, Musikpavillon-Spenden –` / `B, B, Bridge-Turnier, Wimpelketten, Überschuss`
- Issue: Jessica is refiling the B cards; the German labels 'Musikpavillon-Spenden', 'Wimpelketten', 'Überschuss' do not start with B, so the alphabetical detail breaks (EN 'Bandstand Subscriptions', 'Bunting, Surplus' — one card).
- Recommendation: 722: 'Bäckereiquittungen, Blaskapellen-Pavillon: Beiträge'; 736: 'B, B, Bridge-Turnier, Banner und Wimpel, Überschuss'.
- Why not automatic: Renaming labels to keep an alphabetical detail is an adaptation.

### DE-D13. Italics added by translator — para 797, 953
- Quote: `Er ist in meine Eingangshalle gelaufen. Er stand an meinem eigenen Tresen. …` (797) / `der Saphir im Herzen` (953)
- Issue: Italic in German but not in the English (797 = Jessica recalling Fiona's words; 953 = the clue quoted in dialogue, formerly the English phrase in italics). All 15 English italic runs are present in German.
- Recommendation: Remove the italic at 797; at 953 either remove it or keep it as quotation marking (if kept, consider „…“ instead).
- Why not automatic: Italic additions/removals are formatting decisions.

### DE-D14. 3 Mistranslation (plant) — para 40
- Quote: `samt einem einzelnen Zweig Stechpalmenbeeren für das herbstliche Orange`
- Issue: EN 'a single sprig of bittersweet for the orange of the season'. Stechpalme = holly (red berries), which clashes with 'Orange' and pre-empts the ch6 holly miracle.
- Recommendation: 'samt einem einzelnen Zweig Baumwürger für das herbstliche Orange' or plainer 'samt einem einzelnen Zweig mit orangefarbenen Beeren für das herbstliche Orange'.
- Why not automatic: Plant-name choice (botanical vs descriptive).

### DE-D15. 6 Term (minor variants) — para lobby 44–834; inn 293, 382, 651, 659, 708; cider 231–813
- Quote: `Lobby` / `Foyer` / `Eingangshalle` / `Empfangsbereich`; `das Inn` (293, 382, 651, 659) vs `der Gasthof`; `Apfelwein` (11×)
- Issue: The inn lobby has four names; 'das Inn' alternates with 'Gasthof'; US festival cider (served to children) is 'Apfelwein', which in German is alcoholic.
- Recommendation: Lobby → 'Lobby' throughout (or 'Foyer'); 'Gasthof' for the inn except in the proper name; cider → 'heißer Apfelsaft' / 'Apfelpunsch'.
- Why not automatic: Word choice across many places; none changes the plot.

## Inn Trouble - ASSEMBLED - FORMATTED_Spanish

### ES-D1. Title localisation — para 0 vs 18–19
- Quote: `Problemas en la posada` (title page) vs `Inn Trouble` (series list, 19) and `Frost and Found` (18)
- Issue: The title page carries a translated title, while the series list and every `<bt>` span keep the English titles (series rule: book titles are not translated).
- Options: (a) title page → `Inn Trouble` (consistent with series rule); (b) keep `Problemas en la posada` as the Spanish market title and decide whether the series list should then show Spanish titles too.
- Recommendation: (a), unless Lisa wants localised titles for the Spanish storefront — then apply it everywhere, including `<bt>` stamping.
- Why not automatic: title localisation is Lisa's call.

### ES-D2. Table of Contents truncated — para 20–28
- Quote: `Índice` / `Acerca de este libro` / `Capítulo 31` / `¿Y ahora qué?` / `Extracto de <bt>Flour Play</bt>`
- Issue: The English TOC lists About this Book, Chapter 1–31, What's Next?, Excerpt. The Spanish TOC lists only `Capítulo 31` — the entries for chapters 1–30 are missing.
- Recommendation: Regenerate the TOC at formatting time (Capítulo 1 … Capítulo 31) — it will be rebuilt anyway once the missing Heading 1 styles are restored.
- Why not automatic: would add 30 paragraphs.

### ES-D3. Scene-break lines (`* * *`) — paras 1178, 1348, 1427, 1443, 1565
- English has no `* * *` anywhere. At 1427 (before the first "¡Se avecinan más misterios…" line), 1443 (before the second one) and 1565 (before "¡Flour Play estará disponible pronto!") the English has a run of 4–5 blank paragraphs (EN 917–921, 929–932, 983–987), so these three stand in for a real gap.
- 1178 (ch25, between EN 778 "It was right…" and 779 "Then I went to Fiona…") and 1348 (ch30, between EN 880 frost on the elm and 881 "A moment later Bram…") have nothing in the English: translator-added breaks.
- Recommendation: keep 1427/1443/1565 (or replace by the formatter's standard spacing); delete 1178 and 1348.
- Why not automatic: changes paragraph count.

### ES-D4. Key clue printed in English inside `<bt>` — paras 1064, 1213
- Quote: `La nota citaba las palabras de Theo. <bt>The sapphire at its heart</bt>: cinco palabras…` (1064); `—Y describen el broche como <bt>the sapphire at its heart</bt>. Esas son tus palabras, Theo.` (1213)
- Issue: The book's central clue appears in English (wrapped as if it were a book title) in two places, while the note (134, 136, 172) and Theo's card (915, 917, 919, 1104) give it in Spanish. After applied fixes the Spanish form is uniformly `el zafiro en su corazón` — five words, so the "cinco palabras" remark (1064, 1160) still holds.
- Recommendation: replace the whole span including markers: 1064 `<bt>The sapphire at its heart</bt>` → `El zafiro en su corazón`; 1213 `<bt>the sapphire at its heart</bt>` → `el zafiro en su corazón` (bt count 9 → 7).
- Why not automatic: `<bt>` spans must not be edited or removed in this pass.

### ES-D5. Units — round figures (ESCALATE) — paras 150, 1330
- Quote: `la más rica en un radio de cincuenta millas` (150); `el prado tiene cuatro acres` (1330)
- Issue: EN "the richest for fifty miles" is rhetorical; 80 km loses the round figure. "four acres" (not on the literal list) is ~1.6 ha; "acres" reads as foreign in Spain.
- Recommendation: 150 → `la más rica en muchos kilómetros a la redonda` (or `en ochenta kilómetros a la redonda`); 1330 → `y el prado tiene casi dos hectáreas`.
- Why not automatic: round-number conversion (ESCALATE rule).

### ES-D6. Alphabetical "B" index cards — paras 911, 925
- Quote: `Estaba revisando las B —Recibos de panadería, Suscripciones al templete de música—` (911); `—B, B, Torneo de bridge, Banderines, Excedentes—` (925)
- Issue: Jessica is refiling the B cards; in Spanish only "Banderines" starts with B, so the alphabetical detail is lost (EN Bakery Receipts, Bandstand Subscriptions; Bridge Tournament, Bunting, Surplus).
- Recommendation: 911 `—Bollería: recibos; Banda de música: suscripciones—`; 925 `—B, B, Bridge: torneo, Banderines: excedentes—`.
- Why not automatic: renaming labels to keep a letter-based detail is an adaptation.

### ES-D7. "The green" and "the paddock" — many paras
- Quote: the green = `parque` (45, 87, 93, 377, 397, 410, 599, 1019, 1025, 1029, 1031, 1047), `plaza` (505, 748, 762, 968, 1019), `pradera` (120, 377), `prado` (235, 370, 1205, 1324–1363, 1541, 1563), `zona verde` (1082, 1092, 1100, 1116, 1541); the paddock = `prado` (234, 249, 554, 572, 588, 596, 748, 945) and `cercado` (1350, 1356).
- Issue: the town green has five names, and `prado` is also the reindeer paddock (234 and 235 use `prado` for both in consecutive paragraphs). At 87 "Down on the green … toward the park" both are `parque`. `plaza` also collides with "the square" (253, 377).
- Recommendation: green → `el prado` (dominant, and used in the climax ch30); paddock → `el cercado` (as 1350/1356); real park (87, second mention) stays `parque`; legal "the green's deed" → `la escritura del prado`.
- Why not automatic: word choice across ~45 places.

### ES-D8. Gender of the inn's name — paras 45, 651 vs 120, 154, 1075
- Quote: `El Winter Wonderland Inn se alzaba…` (45), `la escritura del Winter Wonderland Inn` (651) vs `La Winter Wonderland Inn apareció…` (120), `Esta misma. La Winter Wonderland Inn.` (154), `la escritura de la Winter Wonderland Inn` (1075)
- Recommendation: masculine `el Winter Wonderland Inn` throughout (implied "el hotel/el inn"); the blurb (30) `La posada Winter Wonderland Inn` is fine as is.
- Why not automatic: either gender is defensible; pick one.

### ES-D9. Register Sam Patel ↔ Jessica — ch8 vs ch17
- Quote: ch8 both usted (`Viene por el portavelas`, `Su trabajo está por todo el pueblo`, `Dígale…`); ch17 both tú (`Sam, te debo una`, `Tú no lo sabías`, `Dime qué debo vigilar`, `dile que…`) while Sam still says `señora Claus`.
- Recommendation: usted both ways in ch17 too (849 `le debo una`, 854 `Usted no lo sabía… ¿Cómo iba a saberlo? … se lo he contado`, 855 `Dígame … Dígame quién`, 853/859 `Dígale`, 858 `Vigile … recuérdeme … Tiene buen ojo … estará … No los detenga, no diga … no deje … recuerde`); alternatively read ch17 as a deliberate move to tú after she confides in him.
- Why not automatic: characterisation choice across a whole chapter. (Emma, Noriko and Bram had in-scene mismatches and were fixed to their dominant form — see APPLIED.)

### ES-D10. Italics added by the translator — paras 346, 1006, 1075, 1487
- Quote: `Conocer el secreto de los papeles te indica dónde pararte` / `No quién` (346); `Entró en mi vestíbulo. Se detuvo en mi propio mostrador. Lo puso entre mis cartas y se marchó, y yo ni lo vi` (1006); `Winter Wonderland Inn` (1075); `no te he dejado de vigilar` / `no he dejado de desear la cinta` (1487).
- Issue: none of these is italic in the English (EN 279, 680, 724, 949). All 15 English italic runs are present in Spanish.
- Recommendation: remove the italic at 1075 (plainly accidental); remove at 346, 1006 and 1487 as well to match the source (or keep as the Spanish convention for remembered/unspoken words).
- Why not automatic: italic additions/removals are formatting decisions.

### ES-D11. Bittersweet — para 45
- Quote: `con una sola ramita de agridulce que aportaba el naranja de la temporada`
- Issue: EN "a sprig of bittersweet" (American bittersweet, orange berries). `agridulce` is only an adjective in Spanish, so the phrase reads as nonsense.
- Recommendation: `con una sola ramita de celastro que aportaba el naranja de la temporada`, or plainer `con una sola ramita de bayas anaranjadas…`.
- Why not automatic: plant-name choice (botanical vs descriptive).

### ES-D12. Martha's circle line and its echoes — paras 363, 1145, 1314
- Quote: `Sea lo que sea lo que llevas a cuestas, no tienes que cargar con ello tú sola. De eso trata el círculo.` (363) vs `Lleves lo que lleves a cuestas, no tienes por qué cargarlo tú sola. De eso trata exactamente el círculo.` (1145) and `¿Que un círculo está para apoyarse en él?` (1314)
- Issue: 1145 quotes Martha's words from 363 (EN repeats them verbatim); the Spanish quotes them with different wording.
- Recommendation: make 1145 repeat 363 word for word: `Sea lo que sea lo que llevas a cuestas, no tienes que cargar con ello tú sola. De eso trata el círculo.`
- Why not automatic: wording choice for a remembered quotation.

### ES-D13. Banner kept in English — para 253
- Quote: `FROST FALLS THROUGH THE YEARS, con la última S amontonada al final`
- Issue: the banner is an in-world English sign; keeping it preserves the "last S" joke. All other labels (exhibit card, MISSING card, drawer labels, folder tab) are now in Spanish.
- Recommendation: keep as is (alternative: `FROST FALLS A TRAVÉS DE LOS AÑOS` + `la última S` stays correct, since it also ends in S).
- Why not automatic: sign localisation choice.
