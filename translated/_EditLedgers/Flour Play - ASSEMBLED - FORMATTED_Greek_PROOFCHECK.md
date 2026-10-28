# Flour Play - ASSEMBLED - FORMATTED_Greek — PROOFCHECK (2026-10-28)

- **Mode:** targeted
- **Files:** corrected `translated/corrected/Flour Play - ASSEMBLED - FORMATTED_Greek.docx` · raw `_superseded/…_Greek.docx` (same 2,056-paragraph grid) · EN `translate_now/Flour Play - ASSEMBLED - FORMATTED.docx`
- **Backup:** `_EditLedgers/_proofcheck_backups/Flour Play - ASSEMBLED - FORMATTED_Greek.20261028-200111.docx`
- **Read in full, EN against EL sentence by sentence:** front matter, blurb, Ch3, Ch12 and Ch13 (lowest change density); Ch9, 11, 17, 18 and 20–25 (the walk-in / cold room, sour base, gate key, order book, confrontation and exoneration chapters); back matter (sell lines, What's Next blurb, CTA).
- **Spot-read:** Ch1, where the Inn Trouble Greek audit had pointed at [39] and [85]. The rest of the book was covered by greps only.
- **Paragraph numbers** below are full-grid indices (the same grid as the flag file).

## Flags judged
- **A=0, C=0, D=0, F=0, G=0, H=0, I=0, J=0:** nothing to judge.
- **B=1:** false positive. The Latin-script words are deliberate kept names: shop and business names, van lettering, financiers, Hobart, *Bûches de Noël*, and the book titles (FP-EL-5 and FP-EL-9).
- **E=7:** all real, but they are formatter items already logged as FP-EL-1. The stray heading lines are [467] «Κεφάλαιο 3» in Ch6, [625] «Κεφάλαιο 17», [633] «Κεφάλαιο 3» and [645] «Κεφάλαιο 12» in Ch9, [684] «Κεφάλαιο 3» in Ch10, and [911] «Κεφάλαιο 17» and [922] «Κεφάλαιο 14» in Ch14. The script did not flag two more: [608] «Κεφάλαιο » in Ch9 and [1859] «Κεφάλαιο» in Ch26.
- For each of the nine headings I checked the paragraphs before and after it against the English. The body text is complete every time; only the heading line is extra. Nothing was renumbered.
- **K (clue chain):** traced. Section "Clue chain" below has the results.
- **Totals:** 7 real (all formatter items, already logged) and 1 false positive.

## Clue chain (section K)
- **Sour base:** «ξινή βάση» at all 19 English places. There is one extra occurrence in Ch17 [1169], "sour in a croissant", which is fine. There are no προζύμι/μαγιά slips. «μαγιά» appears only where the English says yeast (Ch2, Ch10, Ch11).
- **Walk-in vs Joyce's word:** the walk-in is «θάλαμος ψύξης» and Joyce's giveaway is «“το κρύο δωμάτιο”». They stay two different terms at every place: Ch9 [627] [631], Ch17 [1157], Ch20 [1393] [1397], Ch22 [1528], Ch23 [1613] [1615] and Ch24 [1737]. Ch18's generic "a cold room at midnight" is «παγωμένο δωμάτιο», not Joyce's word, which is correct.
- **Sinks:** the hand-sink is «νιπτήρας» and the Hobart sink is «“ο νεροχύτης Hobart”» everywhere.
- **Ten times the dose:** ×2 in Ch11.
- **Bolted back door:** «μανταλωμένη/μανταλώνει» in Ch9 [590] and Ch22 [1528]. The first pass had already reversed the earlier "unbolted" error.
- **Gate, padlock and key:** «πύλη / λουκέτο / κλειδί» consistently in Ch12, 20 and 23.
- **Order book:** «βιβλίο παραγγελιών» throughout.
- **"Nothing I can name":** Doc says it in Ch11 [725], as in the English.
- **"Two degrees below":** identical at [615], [1040] and [1043].
- **Poison:** none in the text (the poison/toxic grep finds nothing).
- **Gendered forms:** Joyce, Pip, Greta and Jessica are feminine everywhere I checked (grep across the whole book plus full reads).
- **Numbers:** Joyce is 65 (Ch24), 25 years / 15 together (Ch20, Ch23, Ch27) and "the twentieth" (Ch20 [1373]), all as in the English.
- **Other terms:**
  - The graffiti reads ΒΡΩΜΙΚΟ.
  - The Grange is «Γκρέιντζ», shortened to «η αίθουσα» in Ch15 after «η αίθουσα του Γκρέιντζ».
  - Prices are in dollars.
- **Back matter:** the *Binder's Bequest* `<bt>` anchors are kept and the CTA is present at [2055].
- **Series consistency with Inn Trouble Greek (corrected 2026-10-28):** Σνόουμπολ, Φροστ Φολς, Έβεργκριν, Κλος, κύκλος, Έμα/Έμας and Μάρθα/Μάρθας all match. Inn Trouble uses «της Φιόνας», which led to fix #19 below.

## Missed by the first pass (all applied)
| # | ¶ | Ch | target (was) | EN | class | fix |
|---|---|---|---|---|---|---|
| 1 | 39 | 1 | «Κάτσαμε εκεί με ρετσίνι…» | "I sat there with sap…" | mistranslation (1st sg → 1st pl; PC-EL-1 from Inn Trouble) | «Καθόμουν εκεί με ρετσίνι» |
| 2 | 85 | 1 | «κατά τη διάρκεια του χιονιού των Αποκριών» | "during the Halloween snow" | mistranslation (Halloween ≠ Carnival; IT-EL-11) | «με το χιόνι του Χάλογουιν» |
| 3 | 62 | 1 | «ένα κουτί ζαχαροπλαστείου» | "a bakery box" (Greta's) | term drift: Greta's bakery given the rival's patisserie word | «ένα κουτί αρτοποιείου» |
| 4 | 49 | 1 | «ήδη μισό σχεδόν μεγαλύτερο» | "already half again the size" | mistranslation ("almost half bigger") | «ήδη μιάμιση φορά μεγαλύτερο» |
| 5 | 29 | blurb | «Η Γκρέτα έφτιαχνε… επί σαράντα χρόνια. Το είχε φτιάξει… τι άλλο να κάνει τα χέρια της.» | "Greta has made… for forty years. She made it…" | blurb tense (past = she no longer makes it); missing «με» | «φτιάχνει… εδώ και σαράντα χρόνια. Το έφτιαξε… να κάνει με τα χέρια της.» |
| 6 | 722 | 11 | «τον έκανε και φαρμακοποιό της» | "the town's chemist too" (analyst) | mistranslation (pharmacist) | «χημικό της» |
| 7 | 1203 | 17 | «την είχα συγχωρήσει» | "I had excused her" (cleared of suspicion) | mistranslation (forgave) | «την είχα απαλλάξει» |
| 8 | 1254 | 18 | «να μην ευχαριστηθεί από κανέναν» | "be thanked by no one" | mistranslation (= "be pleased") | «να μην τον ευχαριστήσει κανείς» |
| 9 | 1266 | 18 | «Ούτε τον αθώωσα. … να το δώσω» | "I did not absolve him… not mine to give" | mistranslation (acquit) + dangling pronoun | «Ούτε του έδωσα άφεση. … να τη δώσω» |
| 10 | 1494 | 21 | «η σίκαλη πήγε περίπατο μαζί της» | "the rye went with it" (the inn account) | pronoun reference (read as "with her") | «μαζί του» |
| 11 | 1610 | 23 | «έστρεψε το χαμόγελό της στην Γκρέτα, με ένα πικρό χαμόγελο» | "turned her smile on Greta, rueful" | awkward/doubled; "bitter" ≠ rueful | «γύρισε προς την Γκρέτα με ένα απολογητικό χαμόγελο» |
| 12 | 1626 | 23 | «την έχει βάλει στο μάτι εκείνο το μαγαζί» | "has had it in for that shop" | grammar (double object) | «έχει βάλει στο μάτι εκείνο το μαγαζί» |
| 13 | 1699 | 23 | «Η πίτα ήταν πάλι δική μου» | "The pie was still mine" | mistranslation (πάλι = again) | «Η πίτα ήταν, παρ’ όλα αυτά, δική μου» |
| 14 | 1710 | 23 | «Αυτό που έχω είναι το αρχείο…, την ταύτιση…, έναν άντρα…» | "What I have is a supplier's record…" | grammar (nominative/accusative mix in the evidence list) | «Έχω το αρχείο…» |
| 15 | 1785 | 25 | «Τα τρία φθαρμένα σημεία… ήταν οι ίδιες» | "the same ones" | agreement | «ήταν τα ίδια» |
| 16 | 780 | 12 | «ποιανού άλλης» | "God knew whose" | grammar | «ποιανού άλλου» |
| 17 | 806 | 12 | «να κάνουν κακό σε κανενός την ψυχή» | "without meaning a soul harm" | ungrammatical calque | «χωρίς να θέλουν το κακό κανενός» |
| 18 | 1325 | 20 | «τύλιγε μια τούφα μαλλί» | "winding a skein" | craft word (tuft ≠ skein) | «μια κούκλα μαλλί» |
| 19 | 1545 | 22 | «στο σαλόνι της Φιόνα» | "Fiona's sitting room" | declension (Inn Trouble Greek: «της Φιόνας» ×21) | «της Φιόνας» |
| 20 | 1880 | 26 | «της Ελίζα Φροστ» | "Eliza Frost's" | declension | «της Ελίζας Φροστ» |

## Regressions introduced by the first pass
- I found none.
- **Method:** I diffed the raw and corrected files paragraph by paragraph. I scanned every token that is new in the corrected file and absent from both the raw file and Inn Trouble Greek (452 tokens), looking for broken inflection from the name, genitive and final-ν sweeps, and none were broken. I checked final-ν and genitive patterns and guillemet balance in every paragraph (0 unbalanced). The italic run sequence is unchanged and the `<bt>` spans are intact.
- **Book-wide rename spill:** walk-in vs cold room, sour base vs yeast, order book vs other books, gate key vs other keys: no rename spilled onto the other term.
- **Dialogue splits:** a few English paragraphs are split in the Greek grid with narration in between (Ch12 [812]–[816], Ch13 [853]/[855], Ch23 [1580]–[1584], [1609]–[1611], [1648]–[1650], [1694]–[1696] and others). Each resumed speech has its own «» and the narration paragraph between names the speaker, so no line reads as the wrong speaker. These splits come from the raw grid, not from the first pass.

## Ledger mismatches
- **Spot check:** 20 random `_APPLIED.md` entries; all 20 "now" texts are present.
- **Full check:** all 1,045 rows; 16 "now" texts are not present verbatim. All 16 were later superseded by the first pass's own documented sweeps:
  - Latin → Greek names: rows 202, 212, 213, 650, 651, 657, 726, 1039, 1061, 1281, 1343, 1354, 1367, 1368 and 1369 (e.g. "Greta" became «Γκρέτα»).
  - Punctuation moved outside the guillemet: row 1202.
- None of the 16 is a lost fix.

## Open decisions re-checked (PROOFREAD_DECISIONS.md, FP-EL-1…12)
- The quotes are still accurate. FP-EL-1's indices count non-empty paragraphs only; the flag file uses full-grid indices for the same headings.
- Judgment calls the first pass applied and logged rather than escalating:
  - FP-EL-4: round-number units.
  - FP-EL-5: names in Greek script.
  - FP-EL-6: Σνόουμπολ.
  - FP-EL-11: «η γειτονιά».
- No chapter renumbering was applied. No ruling was undone.

## Decisions added (PROOFCHECK_DECISIONS.md)
- **PC-FPEL-1:** "Stillwater" appears in both Greek and Latin script (Ch21 vs Ch22).
- **PC-FPEL-2:** Pete's description of the unseen figure uses the generic masculine (Ch13 [865]). I recommend leaving it.

## Refusals
- None. All 20 edits matched exactly once.
- Every edit fell inside a single `<w:t>` node, so no italics were touched.

## Checks after fixes
1. **looks_english:** `[]`.
2. **`bt_anchors.py check`:** 9 spans, 0 unpaired. The only titles are Flour Play, Frost and Found, Inn Trouble and The Binder's Bequest.
3. **`check_matter.py --file`:** 1 PASS, 0 FAIL.
4. **`preflight.py --verify`:** reports "source or corrected copy missing" (the raw file is in `_superseded/`). I compared the corrected file against the backup myself:
   - paragraphs 2056 → 2056
   - italic runs 37 → 37, same sequence
   - `<bt>` 9 → 9
   - scene breaks 61 → 61
   - 20 paragraphs changed
5. **`proofcheck.py` re-run:** A=0 B=1 C=0 D=0 E=7 F=0 G=0 H=0 I=0 J=0. The counts are unchanged because none of the 20 fixes were flag items.

## Verdict: **MINOR**
- I fixed 20 real defects. None of them break the plot chain, omit text or reverse who did what: the clue chain, the confrontation and Greta's exoneration all read correctly.
- **Rate:** 20 defects across about 16 chapter-units read (13 full chapters, front + blurb, back matter, and the Ch1 spot-read), roughly 1.2 per chapter. Most are wording and grammar slips.
- **Worst miss:** Ch1 [62] gives Greta's "bakery box" the rival's patisserie word («κουτί ζαχαροπλαστείου»). The two Ch1 slips that carried over from Inn Trouble are a close second: «Κάτσαμε» ("we sat") for "I sat", and «Απόκριες» (Greek Carnival) for Halloween.
