# PROOFCHECK — Inn Trouble - ASSEMBLED - FORMATTED_Polish (2026-10-28, cloud)

- **Mode:** targeted. No sub-agents. Read with python-docx/lxml, EN next to PL, one chapter at a time.
- **Read in full, sentence by sentence:** front matter + blurb [0]–[29]; Ch2, Ch22, Ch20 (lowest change density, section M: 21 / 24 / 25 %); Ch19, Ch25, Ch26 (plot-critical; Ch2 and Ch22 are both); back matter (sell lines, What's Next [1343]–[1347], the Flour Play excerpt [1353]–[1411], closing line). Targeted reads: Ch23 [1045] ("Theo had the theft"), Ch27 [1210]–[1242] ("ruined himself"), Ch1 [42]/[140] (flag G), Ch23 [1053] (flag I).
- **Diff audit:** raw vs corrected on the same grid (1416 = 1416). 458 paragraphs had word-level changes beyond the dash/ellipsis passes; every one was read as a word diff, and doubtful ones (~25) were checked against the English. The global passes were checked mechanically: the `–`→`—` pass touched no hyphenated word and no number range (the only `–` left are 1910–1930 [315] and 1900–1950 [609], correct); the `broszka`→`brosza` sweep was checked for every inflected form.
- **Ledger check:** all 532 "now" texts in `_APPLIED.md` were looked up in the file, which covers the 20-entry random sample (20/20 found). 528 were found verbatim. The other 4 ([317], [581], [1099], [1131]) are older "now" texts that a later book-wide pass replaced (broszk- → brosz-, Fiona → Fiono), so 0 real mismatches.
- **Flags judged (A–J):** A–F = 0, J = 0.
  - **G ×1 REAL:** Ch1 'Gazette' ×0. The paper's name was dropped twice ([42] „redakcji gazety”, [140] „gazeciarskiego szkieletu”, where 'gazeciarz' means paperboy). Fixed below.
  - **H ×19 FALSE:** 'pół miliona' = the ransom; „pięćdziesięciu mil” = ruling 4; „kilka stopni” = degrees of rotation; „jedną stopę” = a foot (body part); „złotych świateł” = golden lights.
  - **I ×1 FALSE:** [1053] remembered speech inside narration (EN [744] "Finding the truth…, Nick had said"), set in „…” on purpose per the dossier's rule for quoted speech in narration.
- **Clue chain:**
  - „szafir w jej sercu” appears 9× (Ch2 ×3, Ch19 ×3, Ch22, Ch23, Ch26), the same as the EN's 9, worded identically each time.
  - Each "five words" line reads „cztery słowa” ×3, and [1099] has „czterema”. The count is true.
  - The blackmail note is always liścik / notatka / wiadomość. All 67 `list*` hits are the 1924 letters, ordinary mail, or the 'lista' sense.
  - Theo's index card is karta / fiszka.
  - The Blackburn papers (papiery / dokumenty) and the deeds (akt własności, „aktami Blackburnów” = EN "Blackburn deeds") are kept apart.
  - Sam is owed the money (blurb [28] and Ch8 [497]).
  - Cider is sok jabłkowy, with no 'cydr' left.
  - The settled forms hold everywhere: Snowball, krąg, skwer, ganek, wybieg, palenisko.
  - Excerpt: „Prawie.” is right. The snowman question is not inverted. War memorial, overnight and weekend are all in this excerpt's own English. The text is verbatim from corrected Flour Play wherever the two English texts match.

## Missed by the first pass (all applied)
| Para | Ch | Polish (before) | English | Class | Fix |
|---|---|---|---|---|---|
| 1183 | 26 | `Kradzież popełnił Theo.` | "Theo had the theft." | **Reversed meaning / clue chain.** 'Theo committed the theft'. Constance stole the brooch; Theo only *had* that half (from the letters). This is the TR/PT-BR/CS lesson. | `Theo miał kradzież.` (= Ch22 [1009], Ch23 [1045]) |
| 1187 | 26 | `— On dokonał kradzieży.` | "He had the theft. You had the deed." | same | `— On miał kradzież.` (pairs with „Pani miała akt własności.”) |
| 1240 | 27 | `dokładnie tego miejsca, które Theo zrujnował, próbując je ratować` | the very thing Theo had ruined himself trying to save | **Reversed reflexive** (the RO lesson): said Theo ruined the Society | `dokładnie tego, co Theo próbował ocalić, rujnując przy tym samego siebie` |
| 862 | 19 | `Adelaide Blackburn do jej siostry` | to her sister | Pronoun (the SV/CS lesson): 'jej' can read as someone else's sister. Text is inside the italic card, and the italics were kept | `do siostry` |
| 1183 | 26 | `To wpis w księgach.` | That's a property record. | Clue-chain term drift: Ch22 [1005] has „To był rejestr nieruchomości.” | `To rejestr nieruchomości.` |
| 1099 | 25 | `Katalogową kartkę Theo … Papier listowy Towarzystwa, dopasowany` | Theo's catalog card … The Society's stationery, matched | Term drift: card = karta katalogowa, stationery = papeteria (Ch22) | `Kartę katalogową Theo … Papeterię Towarzystwa, dopasowaną` |
| 999 | 22 | `na cios wymierzony w przyjaciela` | turned it on a friend | Gender: the friend is Fiona | `w przyjaciółkę` |
| 776 | 16 | `Cała jego kariera historyka` | His whole history scholarship | Mistranslation: Jamal is a gym owner, not a historian | `Cała jego wiedza historyczna` |
| 27 | blurb | `wymienia szafir w sercu broszy` | names the stone at the brooch's heart | Mistranslation: the blurb deliberately does not name the stone | `wymienia kamień w sercu broszy` |
| 26 | blurb | `zapięła kardigan na opak` | buttoned her cardigan wrong | Mistranslation: 'na opak' = inside out / back to front. Ch1 says "one button off" | `zapięła kardigan krzywo` |
| 42 | 1 | `W oknie redakcji gazety` | The Gazette office | Name dropped (flag G) | `W oknie redakcji Gazette` |
| 140 | 1 | `obok gazeciarskiego szkieletu czytającego gazetę` | past the Gazette's newspaper-reading skeleton | Name dropped; 'gazeciarski' = paperboy's | `obok czytającego gazetę szkieletu z okna Gazette` |

## Regressions introduced by the first pass
| Para | Ch | Polish (before) | Class | Fix |
|---|---|---|---|---|
| 106, 522, 784 | 1, 9, 16 | `Broszki.` / `Broszka. Prawdziwe cacko.` / `Broszka, pojedynczy kamień` | **Incomplete book-wide replacement** (the "capitalised variant" lesson). The broszka→brosza sweep (31 runs) skipped the three sentence-initial forms, which left the book mixed | `Broszy.` (gen. after poszukuję) / `Brosza.` / `Brosza,` |

All other declined forms are correct: broszy ×20, brosza ×14, broszę ×11, broszą ×4, brosze (pl.) ×1. No other regressions were found. The address changes, gender fixes, unit conversions, excerpt rebuild and „cztery słowa” edits all read correctly against the English.

## Ledger mismatches
None (see the ledger check above).

## Re-checked decisions (PROOFREAD_DECISIONS2.md, Polish IT-PL-1…7)
All the quotes are still accurate in the current text: „…zabrała Blackburnom — szafir w jej sercu — i o sklepie…”, „z czterema pasującymi słowami”, „i powiedz mi, pani Claus, jakim cudem…”, „Słyszała pani?” (Ch31), „Nigdy nie pomyślałam o pani…”. The file is uniform on Snowball and on szefowa. The first pass applied no judgment call beyond what it logged. No chapters were renumbered; the TOC and Heading items are left to the formatter (IT-PL-7).

## Notes, not changed
- Excerpt [1377] „czekoladowo-orzechowych babeczek” (EN chocolate-pecan). [1380] does say „orzechy pekan”. The wording is verbatim from corrected Flour Play [81], so changing it here alone would break the excerpt policy. Logged as PC-PL-IT-1.
- Fiona's vocative is mostly „Jessica” (×16), with „Jessico” ×2 ([469], [927]). Both are acceptable colloquial Polish; left as is.
- „w Frost Falls” ×9 alongside „we Frost Falls”: both are acceptable.

## Decisions added
- PC-PL-IT-1 (pecan wording in the excerpt and in Flour Play Ch1): see `PROOFCHECK_DECISIONS.md`.

## Refusals
None (15 edits, 15 applied, each matched exactly once inside its paragraph).

## Checks after the fixes
- looks_english: `[]`
- bt_anchors check: 8 spans (Inn Trouble ×2, Frost and Found, Flour Play ×5), 0 unpaired
- check_matter: 1 PASS, 0 FAIL
- preflight --verify: paragraphs 1416→1416 ok and scene breaks 3→3 ok. It still prints the same FAIL as before this audit: the first pass's declared +2 italic runs and −6 stray `<bt>` (ruling 5). Corrected vs my backup: same paragraph count, 24 = 24 italic runs in order (only [862] changed text inside the italic run), 8 = 8 `<bt>`, 3 = 3 scene breaks, 14 paragraphs changed.
- proofcheck re-run: G 1→0; H=19 and I=1 are unchanged (both false positives).

## Verdict
**SIGNIFICANT.** The plot-chain reversal "Theo had the theft" → "Theo committed the theft" was still in the Ch26 confrontation (twice), and "ruined himself" → "ruined the Society" was still in Ch27. Both are fixed now. Recommend a `full` re-read of this edition. Rate: 15 real defects across 8 sections read in full (front matter, 6 chapters, back matter) plus the targeted passages, about 1.9 per section.
