# PROOFCHECK — Flour Play - ASSEMBLED - FORMATTED_Polish (2026-10-28, cloud)

- **Mode:** targeted. No sub-agents. Read with python-docx, EN next to PL, one chapter at a time.
- **Backup:** `_proofcheck_backups/Flour Play - ASSEMBLED - FORMATTED_Polish.20261028-204028.docx`
- **Read in full, sentence by sentence:**
  - front matter and blurb [0]–[37];
  - Ch20, Ch6 and Ch13 (lowest change density, section M: 30 / 31 / 31 %);
  - the plot-critical chapters: Ch9, Ch11, Ch17, Ch19, Ch21, Ch22, Ch23 and Ch24 (walk-in/cold room, sour base, the flyer reasoning, the confrontation, the charges);
  - Ch1 (the excerpt source: half again, bakery box, pecan);
  - back matter [1941]–[1997] (closing scenes, sell lines, What's Next). The Binder's Bequest excerpt was spot-read only, because it is the published text.
- **Diff audit:** raw (`_superseded`) vs corrected on the same grid (2049 = 2049). 929 paragraphs differ. 521 of them have word-level changes beyond the dash and ellipsis passes, and every one was read as a word diff. About 30 doubtful ones were checked against the English.
- **Ledger check:** all 672 "now" texts in `_APPLIED.md` were looked up in the file, which covers the 20-entry random sample (18/20 verbatim). After normalising the later `–`→`—` pass and the truncated excerpt cells, 670/672 are found. The other two ([1539] „Greto…”, [2026]) are earlier "now" texts that a later ledger row replaced. **0 real mismatches.**
- **Flags judged:** A = C = D = E = F = G = J = 0.
  - **B ×5, all FALSE.** `Pâtisserie` [225]/[233] is Greta's and Renée's own French word (EN "A patisserie… Not a bakery"). `Bûches de Noël` [1716] is the English window card's own text.
  - **H ×8, all FALSE.** `złotych` = golden (×4). `dwa stopnie` ×3 is the FP-PL-2 clue figure, identical at all three places. „sto osiemdziesiąt stopni” is the excerpt's 180° turn.
  - **I ×1, FALSE.** [1873] is the founder's line read aloud from the drawing (EN [1308]). It is quoted document text, so „…” is right.

## Clue chain
| Term | Result |
|---|---|
| sour base | `kwaśna baza` ×18 (18 of EN 20; the other 2 are pronoun or "the base"), never zakwas/drożdże. 'zakwas'/'zaczyn' appear only in Doc's "sourdough tang without the starter" [813]. |
| walk-in vs cold room | Walk-in = `chłodnia`; Joyce's slip = `„zimny pokój”` [698] [700] [1378] [1507] [1581] [1583] [1688]. The two never merge. Pete's locker is `skład chłodniczy` (a separate object). Varney's cold-case is `gablota chłodnicza`. |
| ten times, rye | „Dziesięć razy tyle… dawce dziesięciokrotnie większej” [813] [815] ✓ |
| Greta's nose | „Nic, co potrafię nazwać” [805] ✓ |
| two degrees below | `o dwa stopnie poniżej normy` [689] [1063] [1067], identical ✓ |
| order book | `zeszyt zamówień` / `zeszyt` ×18. No `księga`/`notes` drift (notes = notepads). |
| lock vs key | kłódka ×12 / klucz. Ch20 [1386] „Nigdy jej nie zmieniałam” ✓. **Ch23 [1605] was wrong** („Nigdy go nie zmieniłaś” = the key). Fixed. |
| poison | none. The 5 'trując' hits are 'wpatrując'. |
| Pip | she/her throughout. No masculine first-person narrator forms. Joyce, Greta and Tanaka are feminine throughout. |
| numbers | Joyce 65 [1692], 25 years / 15 together [1392] [1402] [1406] [1540] [1605] [1617], „do dwudziestego” [1354] ✓ |
| DIRTY | `BRUDNE` ×8 ✓ |
| Grange | `świetlica` ×15 ✓ |
| Snowball | ×9 uniform ✓ |
| currency | dollars/cents ✓ |
| The Binder's Bequest anchors | kept (9 spans) |
| closing CTA | still absent (FP-PL-6, already logged) |

## Missed by the first pass (all applied)
| Para | Ch | Polish (before) | English | Class | Fix |
|---|---|---|---|---|---|
| 1605 | 23 | `Nigdy go nie zmieniłaś.` | "You never changed it." | **Lock vs key (clue chain).** 'go' = the key; it is the LOCK that was never changed | `Nigdy jej nie zmieniłaś.` |
| 1257 | 19 | `Usłyszałam w tym złoty sklep. Nigdy nie powiedział, że wszedł do Sugarplum.` | "I heard the gold shop. He never said it went into Sugarplum." | **Who-did-what.** Masculine 'wszedł' put Danny into Sugarplum; "it" is the figure | `W jego słowach usłyszałam złoty sklep. Nigdy nie powiedział, że ta postać weszła do Sugarplum.` |
| 1257 | 19 | `a ja nie słyszałam niczyjej.` | "and I heard nobody's" | Mistranslation | `a ja usłyszałam w tym tylko „niczyja”.` |
| 1293 | 19 | `Ulotka jest dowodem na czyjejś ladzie` | "A flyer's a proof on somebody's counter" | **Printer's proof ≠ evidence** (the lesson item; Ch22 [1509] already says „próbny wydruk”) | `Ulotka leży jako próbny wydruk na czyjejś ladzie… zanim zawiśnie na tablicy.` |
| 1680 | 24 | `i wzięła Danny'ego na stronę, po dobroci` | "taken Danny's word gently off to one side" | **Took his statement, not him** (the lesson item) | `i na osobności spokojnie przyjęła zeznanie Danny'ego` |
| 1957 | 27 | `Uniosłam rękę na powitanie. Odpowiedział tym samym.` | "He lifted a hand to me. I lifted mine." | **Reversed who-did-what** | `Uniósł rękę na powitanie. Odpowiedziałam tym samym.` |
| 1117 | 17 | `niż żeby po prostu uszło mi to na sucho` | "than just being off the hook" | **Reversed meaning.** 'got away with it' implies Danny's guilt | `niż tylko to, że przestali mnie podejrzewać` |
| 899 | 13 | `I zamaskowany.` | "And covered. A long coat, or a smock" | Mistranslation (masked ≠ covered) | `I okryty.` |
| 885 | 13 | `wymagało mroku w duszy` | "wanted a temper for the dark" | **Temper = disposition** (the lesson item); 'darkness of soul' | `wymagało usposobienia do działania po ciemku` |
| 885 | 13 | `wykreśliłam pana z powrotem` | "I've taken you back out" | Calque | `skreśliłam pana z tej listy` |
| 883 | 13 | `rozbijał poranną ćwiartkę` | "breaking down the morning's side" | Mistranslation (smash) | `rozbierał` |
| 873 | 13 | `Mógł stać w każdym czarnym poranku…` | "every black morning of his life" | Grammar | `Mógł stać pod jej otwartymi drzwiami każdego czarnego poranka swojego życia` |
| 907 | 13 | `przed wypowiedzeniem którego wolałby chyba umrzeć, niż nazwać je życzliwością` | "a sentence he would have died before calling kindness" | Garbled | `które prędzej by umarł, niż nazwał życzliwością` |
| 1281/1283/1285 | 19 | `kiedy Greta zgasła` / `Greta mogła zgasnąć` / `Nie zgasła.` | "the very week Greta went dark" | Mistranslation ('Greta died out') | `u Grety zgasły światła` ×2; `— Nie z pecha. Varney nie przychodzi przypadkiem.` |
| 1466 | 21 | `kwaśną bazę… — Taki, jaki piekarnia kupuje` | "The kind a bread kitchen buys" | Agreement (the rename left the masculine) | `— Taką, jaką piekarnia chleba kupuje do żytniego.` |
| 1466 | 21 | `w sprawie odkupienia Grety` | "to buy Greta out" | Mistranslation ('redeeming Greta') | `w sprawie odkupienia jej sklepu` (= [1589]) |
| 1527 | 22 | `Wymyśliła to wczoraj` | "She worked that out" | Mistranslation ('made it up') | `Domyśliła się tego wczoraj` |
| 1522 | 22 | `i będzie musiała się wytłumaczyć` | "and she gets to answer it" | Nuance (her right becomes her obligation) | `a ona będzie mogła na to odpowiedzieć` |
| 1512 | 22 | `Sama w sobie to po prostu piekarz` | "By itself, that's…" | Agreement | `Samo w sobie` |
| 1507 | 22 | `z furgonetką Wendtów` | "the Wendt's van" | Name ('the Wendt family') | `z furgonetką Wendt's Bakehouse` |
| 1659 | 23 | `a sądzę, że czegoś żałuje` | "and I think there's something" | Address (Tanaka is formal with Joyce) | `czegoś pani żałuje` |
| 81 | 1 | `pudło cukiernicze` | "a bakery box" | **Bakery ≠ patisserie** (the lesson item) | `pudło z piekarni` |
| 81 | 1 | `czekoladowo-orzechowych babeczek` | "chocolate-pecan cupcakes" | Pecan ≠ walnut (PC-PL-IT-1, one answer) | `czekoladowo-pekanowych babeczek` |
| 81 | 1 | `miała fartuch tak zaznaczony mąką, że nawet nie zadała sobie trudu, by ją otrzepać` | "flour all down her apron that she hadn't troubled to brush off" | Mistranslation (invented causal link) | `cały fartuch miała w mące, której nawet nie zadała sobie trudu otrzepać` |
| 118 | 1 | `Cóż, cokolwiek to będzie` | "Well, whoever it is" | Mistranslation | `Cóż, kimkolwiek oni są` |
| 142 | 1 | `spacerując nocą z dziecięcym bałwanem, by spojrzeć na to wszystko, co…` | "walking a child's snowman around in the dark to face whatever…" | Mistranslation | `obracając nocą dziecięcego bałwana przodem do tego, co akurat przykuło jej błądzącą uwagę` |
| 29 | blurb | `Greta piekła… przez czterdzieści lat.` / `wyciąga je z pieca kwaśne` | "Greta has made… for forty years." / "it comes out of her oven sour" | **Blurb tense** (the lesson item) + agreement ('je' for a singular roll) | `Greta od czterdziestu lat piecze…` / `wychodzi jej z pieca kwaśna, kolejna partia też` |
| 31 | blurb | `Do czwartku Greta stoi` | "By Thursday Greta is standing" | Mistranslation ('until Thursday') | `W czwartek Greta stoi już` |
| 35 | blurb | `za olej` | "behind on their oil" (heating oil) | Ambiguity (cooking oil) | `za olej opałowy` |
| 674 | 9 | `Piece sprawowały się tak samo cudownie, jak wcześniej kaprysiły.` | "had come right as strangely as they'd gone wrong" | Meaning drift (miraculously ≠ strangely) | `Piece wróciły do formy równie zagadkowo, jak wcześniej zaczęły kaprysić.` |
| 1479 | 21 | `a kardigan miał zapięte guziki nałożone na to…` | "a cardigan buttoned over whatever he'd meant to sleep in" | Garbled | `a na to, w czym zamierzał spać, narzucił zapięty kardigan.` |
| 1682 | 24 | `Pip minęła go w poszukiwaniu…` | "Pip passed it up for the wastebasket" | Mistranslation ('passed it' = the office) | `Pip zlekceważyła piecyk na rzecz kosza na śmieci…` |
| 1392 | 20 | `że ona nadal wie, gdzie ona wisi` | "she still knows where it hangs" | Pronoun ambiguity | `gdzie ta miotła wisi` |
| 2006 | excerpt | `wręcić` | "hand" | Typo (non-word; carried over from the published text) | `wręczyć` |

## Regressions introduced by the first pass
| Para | Ch | Polish (before) | Class | Fix |
|---|---|---|---|---|
| 519 | 6 | `Oparte o nią było ręcznie wypisany kartonik.` | **Broken agreement from a substitution.** The noun 'zgłoszenie' (neuter) became 'kartonik', but the verb and participle were not changed | `Oparty o nią był ręcznie wypisany kartonik.` |
| 1466 | 21 | `— Taki, jaki…` (listed above) | Agreement broken by the sour-base rename (zakwas → kwaśna baza) | applied |

All other first-pass edits read correctly against the English. That covers the address changes, the gender fixes (Pip ×11, Varney, Joyce), the unit conversions, the cold-room unification in Ch20, DIRTY → BRUDNE, the order-book unification and the excerpt rebuild.

## Ledger mismatches
None (see the ledger check above).

## Re-checked decisions (PROOFREAD_DECISIONS.md, FP-PL-1…8)
The quotes are still accurate:
- FP-PL-1: Snowball, uniform ×9.
- FP-PL-2: dwa stopnie ×3.
- FP-PL-3: 45 kg / 23 kg / pół kilo.
- FP-PL-5: the address table holds in every chapter read.
- FP-PL-6: the CTA is still missing.
- FP-PL-7: formatter items unchanged.

The first pass applied no judgment call beyond what it logged. No chapters were renumbered; the Ch21 heading digit is the same number.

## Cross-book (Inn Trouble Polish audit)
PC-PL-IT-1 (pecan) is applied on the Flour Play side ([81]). Inn Trouble [1376] [1377] [1396] [1343] [1344] [1346] now need the matching Flour Play text: see **PC-FPPL-2**. The shared series terms (Snowball, krąg, skwer, ganek) match corrected Inn Trouble Polish.

## Decisions added (PROOFCHECK_DECISIONS.md)
- PC-FPPL-1: the pie „czekoladowo-orzechowy” ×11 → „czekoladowo-pekanowy”?
- PC-FPPL-2: Inn Trouble excerpt and blurb follow-ups.
- PC-FPPL-3: the Ch1 [87]/[88] Greta turn split (low priority).

## Refusals
None (38 edits, 38 applied, each matched exactly once inside a single run; no italic runs touched).

## Checks after the fixes
- looks_english: `[]`
- bt_anchors check: 9 spans (Flour Play, Frost and Found, Inn Trouble, The Binder's Bequest), 0 unpaired
- check_matter: 1 PASS, 0 FAIL
- preflight --verify: "source or corrected copy missing" (the raw is in `_superseded/`). Compared corrected vs my backup instead:
  - paragraphs: 2049 = 2049
  - italic runs: 46 = 46, identical sequence
  - `<bt>`: 9 = 9
  - scene breaks: 60 = 60
  - paragraphs changed: 32
- proofcheck re-run: A0 B5 C0 D0 E0 F0 G0 H8 I1 J0, unchanged. All remaining flags are false positives; none of the defects found were flaggable.

## Verdict
**SIGNIFICANT.** Several reversed-meaning and clue-chain defects survived the first pass:
- Ch23 "you never changed it" pointed at the key, not the lock.
- Ch19 had Danny, not the figure, "going into Sugarplum", and the printer's proof read as "evidence".
- Ch24 had Tanaka take Danny aside instead of taking his statement.
- Ch17 had Danny say he'd rather this than "get away with it".
- Ch27 reversed who waved first.

All of them are fixed. Recommend a `full` re-read of this edition (Ch2–5, 7–8, 10, 12, 14–16, 18, 25–27 were not read in full). Rate: 37 real defects (35 missed + 2 regressions; 38 edits) in 14 sections read in full (front, 12 chapters, back), about 2.6 per section.
