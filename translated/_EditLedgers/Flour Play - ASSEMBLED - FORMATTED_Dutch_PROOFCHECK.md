# PROOFCHECK — Flour Play - ASSEMBLED - FORMATTED_Dutch (2026-10-28)

**Verdict: MINOR.** Nothing was reversed and nothing was omitted. The audit fixed 17 one-answer items, all applied. Four of them sit on the plot chain:
- **Lock vs key** (Ch20 [1507], Ch23 [1694]): «Je hebt hem nooit vervangen» read as the key. It now says the lock.
- **Pete's "temper he didn't have"** (Ch13): rendered as «humeur» (a mood). It is now the disposition sense.
- **Ch22 [1624]**: a «Hij» bound to the culprit instead of Pete.

**Rate:** 17 real defects across about 17 chapters read in full, roughly 1 per chapter, all low severity.

## Scope
- **Mode:** targeted.
- **Edition:** `translated/corrected/Flour Play - ASSEMBLED - FORMATTED_Dutch.docx`.
- **Raw for the diff:** `_superseded/…_Dutch.docx`. It has the same 2095-paragraph grid.
- **Backup:** `_EditLedgers/_proofcheck_backups/Flour Play - ASSEMBLED - FORMATTED_Dutch.20261028-203137.docx`.
- **Paragraph numbers:** these are every-`w:p` indices, as in the flag file. The first-pass ledgers count non-empty paragraphs only, so their numbers differ.

**Read in full, EN against NL, sentence by sentence:**
- front matter and the blurb (present tense ✓);
- the lowest-density chapters: Ch12, Ch18 and Ch4;
- Ch1 (half again, BAKERY box, Very nearly);
- the walk-in, cold-room, sour-base and confrontation chapters: Ch9, Ch11, Ch13, Ch17, Ch19, Ch20, Ch21, Ch22, Ch23 and Ch24;
- Ch27 and all back matter.

The excerpt of *The Binder's Bequest* was copied by the first pass from the published Dutch edition. I checked it for completeness (50 of 50 paragraphs) and did not re-proof it.

**Diff-audited:** every changed paragraph in Ch2, Ch3, Ch5–Ch8, Ch10, Ch14–Ch16, Ch25 and Ch26 was read against the English. I filtered out the paragraphs whose only change was the quote conversion.

## Flags judged (A–J)

| Section | Result |
|---|---|
| A, C, D, E, G, I | 0 flags. |
| B (3) | False positive. «wíst» [1006] and «míjn» [1853] are Dutch emphasis accents, and «Bûches de Noël» [1770] is French in the English too. |
| F (1) | False positive. Ch22 «14:00» = EN "2:00" on the 24-hour clock (an afternoon meeting). |
| H (9) | False positive. Eight are «een voet / een duim / een pond» idioms or EN figures, and «mijlen» [70] is EN "the miles", rhetorical. |
| J (1) | False positive. [294] the English duplicate "I read it, and went cold." was emptied. Its Dutch twin [295] is complete. |

**Totals:** 0 real, 14 false positives.

## Clue chain (section K), traced at every occurrence
- **Walk-in vs cold room are two different words, everywhere.**
  - walk-in = «koelcel»: Ch9 [704], Ch17 [1259], Ch20 [1497] ×3, Ch22 [1624], Ch23 [1682]. That is 7, matching the English.
  - Joyce's slip = «de koude kamer»: [704] [708] [1493] [1497] [1624] [1682] [1683] [1742].
  - The Ch23 "walk-in a walk-in" slip is gone, and the rename did not spill anywhere.
  - The other cold spaces keep their own words. Ch18 "a cold room at midnight" = «een koud lokaal». Pete's locker = «koelopslag». The display case = «koelvitrine».
- **Sour base** = «zuurmiddel» ×20. «zuurdesemstarter» appears only at [791] for EN "the starter", which is correct. «gist» is used only for real yeast.
- **No poison or toxic words.** The one hit is «gift» [1356], which is Dutch for an anonymous donation.
- **Other clue terms:**
  - «Tien keer» ×2 ✓.
  - The gate key is «poortsleutel» / «de sleutel van Greta's hangslot» ✓.
  - The order book is «bestelboek» throughout, and no other book received the rename.
  - Doc's line is «Niets dat ik een naam kan geven» [783] (in the English, Doc says it).
  - «twee graden onder de norm» is identical at [692], [1132] and [1136] (FP-NL-1).
- **Characters, numbers and names:**
  - Pip is she/her throughout, and Jessica is feminine.
  - Joyce is 65 [1746]; 25 years ago / 15 together ([424], [1513], [1523], [1700], [1711], [1960]); «de twintigste» [1473]; dollars only.
  - The graffiti is VIES ✓ (not a vulgarity).
  - The Grange is «de dorpszaal» everywhere (FP-NL-7).
- **Back matter:** the *The Binder's Bequest* anchors are kept (9 spans). The closing "Start reading…" line is still missing, already logged as FP-NL-5.
- **Lessons list, checked explicitly:**
  - Ch17: the FIGURE is lost past the pharmacy light ✓.
  - Ch19: Danny never named the gold shop («Ik hoorde de goudwinkel … Ik heb die winkel daar zelf neergezet») ✓, and «drukproef» is used ✓.
  - Ch23: who would have been robbed is correct ✓.
  - Ch24: «Danny's verklaring rustig apart genomen» = his word, not him ✓.
  - Ch1: «anderhalf keer zo groot» ✓; the box is a «bakkersdoos», never patisserie ✓; «chocolade-pecannoten» ✓.
  - Ch22: no split turns (1:1 paragraphs) ✓.

## Missed by the first pass (17 edits in 17 paragraphs, all applied)

| Para | Ch | NL before | EN | Class | Fix |
|---|---|---|---|---|---|
| 1694 | 23 | «Je hebt hem nooit vervangen.» | "You never changed it." (the lock) | **Reference (lock vs key)**: «hem» binds to the key in Greta's previous line | «Je hebt het slot nooit vervangen.» |
| 1507 | 20 | «sinds Harold hem heeft opgehangen. Ik heb hem nooit vervangen.» | "since Harold hung it. I never changed it." | Reference: «slot» is a het-word, so «hem» reads as «de poortsleutel» | «…het heeft opgehangen. Ik heb het nooit vervangen.» |
| 889 | 13 | «een humeur dat hij niet had» | "a temper he didn't have" (a disposition) | **Mistranslation (exoneration logic)**: «humeur» means mood | «een aard die hij niet had» |
| 899 | 13 | «het vergde een humeur voor het duister» | "wanted a temper for the dark" | Same | «het vergde een aard die het duister opzoekt» |
| 911 | 13 | «Geen jongen, en geen humeur.» | "Not a boy, and not a temper." | Same | «Geen jongen, en geen driftkop.» |
| 1624 | 22 | «…kwam op die manier binnen. Hij zag voor dag en dauw een busje» | "He [Pete] saw a van" | **Who-did-what**: «Hij» binds to «degene die het deed» | «Pete zag voor dag en dauw een busje» |
| 1539 | 20 | «Ik kom er pas mee naar je toe als dat zo is.» | "I won't come to you with it until I do [know]." | Mistranslation: "if it is so" | «…als ik het zeker weet.» |
| 850 | 12 | «en zie hier, hij had er zijn naam op staan» | "here it was, and it had his name over it" | Subject shift (it → he) | «en hier was ze dan, met zijn naam erop.» |
| 1199 | 17 | «‘Heb je hier wat aan?’» (Danny) | "Is it any use?" | Address drift: Danny uses u everywhere else | «‘Hebt u hier wat aan?’» |
| 789 | 11 | «Als je hierdoor een deeg mengt» | "You mix a dough with this through it" | Mistranslation: «hierdoor» = "because of this" | «Als je een deeg maakt waar dit doorheen zit» |
| 800 | 11 | «het ding dat los rondloopt» | "the thing loose in the town" | Tense drift (o.v.t.) | «rondliep» |
| 810 | 12 | «Niet wie haar haat.» | "Not who hated her." | Tense drift | «haatte» |
| 842 | 12 | «Drie deuren van Greta's open deur was … drie en vier ochtenden» | "Three doors from … three and four mornings" | Grammar | «…open deur vandaan was … drie à vier ochtenden» |
| 1396 | 19 | «boven jouw gebraad» | "over your roast" | Calque | «bij jouw gebraad» |
| 730 | 9 | «met een gezicht dat stond als het weer» | "with a face like weather" | Calque (meaningless in Dutch) | «met een gezicht als een onweersbui» |
| 1205 | 17 | «Pip keek het met lange tanden na.» | "watched it go with poor grace" | Wrong idiom (refers to eating) | «Pip keek het met tegenzin na.» |
| 35 | blurb | «Jessica zoekt naar hetgeen dat klopt» | "reaches for the thing that fits" | Grammar | «datgene wat klopt» |

## Regressions introduced by the first pass
- None found. All 676 first-pass edits are well-grounded fixes.
- The quote conversion is clean: no unmatched ‘, and nested “ ” are used for quotes inside dialogue.
- No italic run or `<bt>` anchor was lost.
- The address-table changes (Renée/Joyce/Danny/Tanaka→Greta u; Pete/Doc je) are applied consistently, apart from the Danny straggler at [1199] fixed above.

## Ledger mismatches
- None. I sampled 20 random rows of the 676-row findings table (seed 28), and all 20 "Corrected" texts are present in the file.

## Decisions
- **Re-check of FP-NL-1…8:**
  - The quotes are still accurate: «twee graden onder de norm» ×3, Snowball, «Wat nu?», the missing sell line, the Grange = dorpszaal, and «zuurmiddel» / «koude kamer».
  - The first pass made no unlogged judgment calls.
  - Snowball was not changed against Book 1 (FP-NL-3 is still open).
- **Added:** PC-FPNL-1 (Ch20 «overval» for "hasp") and PC-FPNL-2 (Ch9 "a week into the season") in `PROOFCHECK_DECISIONS.md`.
- **Cross-book:** the Inn Trouble NL audit listed no slips to fix in this edition. Its excerpt-vs-Flour-Play divergence (PC-NL2-2) belongs to Inn Trouble.

## Refusals
- None.

## Checks (after fixes)
- **looks_english:** `[]`.
- **bt_anchors check:** 9 spans, 0 unpaired. The titles are Flour Play, Frost and Found, Inn Trouble and The Binder's Bequest.
- **check_matter --file:** 1 PASS, 0 FAIL.
- **preflight --verify:** reports "source or corrected copy missing" (the raw is in `_superseded/`). I compared corrected against the backup myself:
  - paragraphs 2095 → 2095 (paras() 1371 → 1371);
  - italic runs 42 → 42, identical in order;
  - `<bt>` 9 → 9;
  - scene breaks 58 → 58;
  - changed paragraphs = exactly the 17 listed above.
- **proofcheck.py re-run:** A=0 B=3 C=0 D=0 E=0 F=1 G=0 H=9 I=0 J=1. The counts are unchanged because every flag was a false positive.
