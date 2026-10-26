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
