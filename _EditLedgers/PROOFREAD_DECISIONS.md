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
