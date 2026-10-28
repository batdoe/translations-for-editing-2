# Flour Play - ASSEMBLED - FORMATTED_Czech — PROOFCHECK (2026-10-28)

- **Mode:** targeted. Paragraph numbers are `w:p` indices (the proofcheck.py / FLAGS grid). The first pass's `_APPLIED.md` uses claude_translate's grid, which counts only non-empty paragraphs. To convert: APPLIED ¶k (k < 381) = the k-th non-empty w:p; APPLIED ¶381 = w:p 682; APPLIED ¶k (k > 381) = the (k−1)-th non-empty w:p.
- **Read in full, sentence by sentence, EN against CS:** the front matter and blurb; Ch2, Ch4 and Ch17 (the lowest change density, section M); Ch1 (the Inn Trouble excerpt source); Ch9, Ch11, Ch13 and Ch17–Ch24 (walk-in/cold room, sour base, the deduction, the confrontation, the charges); the back matter (sell lines, What's Next blurb, end of book). The excerpt (published *Knihařův odkaz* text) was checked by structure only: 50 = 50 paragraphs.
- **Diff audit (raw `_superseded` against corrected):** I read every changed paragraph in Ch3, 5, 6, 7, 8, 10, 12, 14, 15, 16, 25, 26 and 27 as word-level hunks, and checked the doubtful ones against the English. Changed paragraphs in the chapters read in full were checked in place.
- **APPLIED ledger:** I checked all 637 rows by machine: 634 "now" texts are present. The other 3 are superseded by later fixes in the same paragraph (¶275 rukavici→palčáku, ¶1087 Gretinu, ¶381 emptied). I also took 20 random rows by hand: 20 of 20 are present.
- **Flags judged:** 10 real, 0 false positives.
  - A: 0. B: 2, false positive (*Bûches de Noël* is French in the English too). C/D/E/F/G: 0. I: 0 (539 paragraphs open with „, and the dialogue is consistent).
  - H: 7, false positive. *korunovaní* = crowned; *korunkový uzávěr* = bottle cap ×3; *stopa* ×2 = footprint; Ch12 "Sto stop" = a hundred FOOTPRINTS (correct).
  - J: 1, false positive. [682] was a stray "Kapitola 3" with no English text. EN 421→422 has no scene break there. The paragraph stays (empty), as already logged in FP-CS-10.

## Clue chain (Step 3) — all traced
- **sour base** = *kyselý základ*. There are 21 occurrences (EN 20, one Czech repeat), matching chapter by chapter (Ch11 3, Ch13 1, Ch17 4, Ch18 1, Ch19 1, Ch21 4, Ch22 2, Ch23 2, Ch24 2). The word is never *kvásek*: *kvásek* survives only in Doc's correct "kváskovou kyselost bez kvásku". Two near-collisions were fixed: Renée's "kvas" quip [1243] and Doc's "na moučném základu" (flour carrier) [1510].
- **walk-in** = *chladicí box*. All 7 places are correct: Ch9, Ch17, Ch20 ×3, Ch22, Ch23.
- **Joyce's cold room** = *‚chladírna‘*. All 9 places are correct: Ch9 ×2, Ch20 ×3, Ch22, Ch23 ×2, Ch24. The Ch18 literal "cold room" = *promrzlá místnost* (correctly NOT chladírna). Pete's locker = *mrazírenský sklad*, which stays distinct.
- **hand-sink** = umyvadlo, and Joyce's word = *hobartský dřez*.
- **two degrees under code:** "o dva stupně pod normou", identical at all three places (FP-CS-5).
- **ten times:** "Desetkrát víc" / "v desetinásobné dávce" (Ch11).
- **"Nothing I can name":** *„Nic, co bych uměl pojmenovat“* (Doc).
- **gate / lock / key:** brána, zámek and klíč are consistent. *branka* is used only for house garden gates, and that is correct. Ch20 "Nikdy jsem ho neměnila" = the lock ✓. Ch23 had an ambiguous "Ty jsi to nikdy nevyměnila", now fixed to the lock.
- **order book** = *kniha objednávek* (Ch2 has *účetní kniha* for EN "ledger" ✓).
- **Grange** = *spolkový dům* everywhere.
- **No poison or toxic wording** (0 hits).
- **DIRTY graffiti** = ŠPINAVÉ throughout.
- **Money:** dollars and cents only.
- **Pip:** no masculine forms. **Jessica:** never masculine.
- **Numbers:** Joyce is 65. "Forty years ago… Fifteen years" in Ch5 matches the EN, and 25 years (Ch20/Ch23) matches the EN. *dvacátého* is in Ch15 and Ch20.
- **Binder's Bequest:** the `<bt>` anchors are kept. The closing CTA is still missing (already logged as FP-CS-8).
- **Lesson lines:**
  - Ch13 "povahu, jakou neměl" = disposition ✓.
  - Ch17: the FIGURE disappears past the pharmacy light ✓.
  - Ch19: Danny never named the shop ✓.
  - Ch1: o polovinu větší ✓. Greta's box = *krabice na cukroví*, not the patisserie word ✓.
  - Ch22: turns are not split ✓.
  - Ch19 proof, Ch23 lock, Ch24 "Danny's word" and Ch18 "by half" were wrong; they are fixed below.

## Missed by the first pass (26) — all applied
| ¶ | Ch | Czech (before) | English | Class | Fix |
|---|---|---|---|---|---|
| 35 | blurb | `Tohle nebyl výbuch vzteku. Tohle bylo řemeslo.` | That is not a temper. That is a trade. | tense (blurb is present elsewhere) | `Tohle není výbuch vzteku. Tohle je řemeslo.` |
| 56 | 1 | `o polovinu větší než kdokoli jiného` | half again the size of anyone else's | grammar (PC-CS-1, from the IT CS audit) | `než věnec kohokoli jiného` (now = IT CS excerpt) |
| 273 | 4 | `Čtyřicet let se nezapomene přes noc a jen tak ve vlastní kuchyni.` | …and only in your kitchen | meaning blurred | `…přes noc, a už vůbec ne jen ve vlastní kuchyni.` |
| 307 | 4 | `snažil se odlákat obchody z jejího bloku` | trying to move the town's trade off her block | mistranslation (obchody = shops) | `snažil se, aby město chodilo nakupovat jinam než do jejího bloku` |
| 694 | 8 | `do ohrady k sobům` | in the paddock with the reindeer | series term (paddock = výběh, as unified in IT CS / Book 1) | `do výběhu k sobům` |
| 705 | 9 | `tři dny po cihle, skle i zlatých písmenech, kdy nápis` | three days after the brick, glass and gold letters both | garbled (glass read as part of "after") | `Greta dostala výlohu zpátky tři dny po té cihle, sklo i zlatá písmena, a nápis` |
| 706 | 9 | `Byla jsem ve frontě třetí od konce` | I was three back in the line | mistranslation | `Byla jsem ve frontě třetí` |
| 710 | 9 | `Šířilo se jako mráz po okenní tabulce` | The light … went as frost covers a window, from the edges in | reversed image (the light *spread*) | `Mizelo tak, jak mráz pokrývá okenní tabulku, od okrajů ke středu` |
| 714 | 9 | `přes mizející obchod` | across the emptying shop | mistranslation | `přes vyprazdňující se obchod` |
| 726, 729 | 9 | `pomatení sousedé` / `Žádný pomatený soused` | a mad neighbor | mistranslation (mad = angry) | `naštvaní sousedé` / `Žádný naštvaný soused` |
| 808 | 11 | `jenže teď to bylo mnohem osobnější a tvrdší` | only closer now, and harder | mistranslation | `jenže teď těsněji a neúprosněji` |
| 819 | 11 | `která ukazovala někam ke správnému směru` | that pointed anywhere at all | meaning shift | `která vůbec někam ukazovala` |
| 911 | 13 | `že jste v té uličce před rozedněním` | you're in that yard before light | term (yard ≠ alley) | `na tom dvoře` |
| 1141 | 17 | `ať si pro ni přijde, až se mu to rozleží v hlavě` | told him to bring it to me when it came clear | garbled | `ať s ní za mnou přijde, až se mu to vyjasní` |
| 1243 | 17 | `Do croissantu se přece kvas nestrká` | One doesn't put sour in a croissant | term (kvas ≈ starter; sour base ≠ starter) | `Do croissantu se přece nic kyselého nedává` |
| 1302 | 18 | `střecha stojí dvakrát tolik` | the bigger sum by half | number (1.5×, not 2×) | `střecha stojí o polovinu víc` |
| 1388 | 19 | `Leták je důkazem na něčím pultu` | A flyer's a proof on somebody's counter | **plot chain** (printer's proof → "evidence") | `Leták leží v korektuře na něčím pultu` (= Ch22 "v korektuře") |
| 1431 | 20 | `Nemohla jsem to slovo slyšet` | I couldn't stand to hear them (both words) | number | `ta slova` |
| 1510 | 21 | `na moučném základu` | on a flour carrier | term collision with *kyselý základ* | `na moučném nosiči` |
| 1529 | 22 | `„Jessiko,“` | "Jessica," | vocative typo | `„Jessico,“` |
| 1546 | 22 | `do ní může sáhnout` | can reach into it (the dumpster) | agreement | `do něj` |
| 1632 | 23 | `Ty jsi to nikdy nevyměnila.` | You never changed it. (the lock) | **lock vs key** (ambiguous) | `Ten zámek jsi nikdy nevyměnila.` |
| 1705 | 24 | `Dannyho vzala stranou s veškerou šetrností` | taken Danny's word gently off to one side | mistranslation (took him aside) | `Dannyho výpověď si s veškerou šetrností vyslechla stranou` |
| 1733 | 24 | `jako místo, kde by se něco takového stalo` | like the sort of shop that would do it | agency lost | `jako obchod, který by něco takového udělal` |
| 1741 | 24 | `Joyce se do toho trochu vložila až úplně nakonec` | Joyce got there at the very end, a little | mistranslation (got involved) | `Joyce k tomu trochu dospěla až úplně nakonec` |

## Regressions introduced by the first pass (5) — all applied
| ¶ | Ch | First-pass text | English | Problem | Fix |
|---|---|---|---|---|---|
| 287 | 4 | `stál asi tucet lidí a mluvila tlumeným hlasem` | A dozen or so people stood … keeping their voices down | "dvacítka" → "tucet" left the feminine verb behind (broken agreement) | `stál asi tucet lidí, kteří mluvili tlumeným hlasem` |
| 1110 | 16 | `byl to jediná záminka` | (the wreath as) the one excuse | rewrite broke agreement | `byla to jediná záminka` |
| 1131 | 16 | `Dala mi jistotu a nic, s čím by se dalo něco dělat` | She had given me the recognition and nothing whatever to do with it | "recognition" became "certainty" | `Nechala mě to poznat, ale nedala mi nic, s čím by se dalo něco dělat` |
| 1396 | 20 | `„Jessiko. Výborně,“` | "Jessica. Good," | vocative fix introduced a typo | `„Jessico. Výborně,“` |
| 1692 | 23 | `Pak zvedla svazek, aniž se podívala, našla správný klíč` | picked up the ring, found the key without looking | "without looking" moved to the wrong verb | `Pak zvedla svazek, naslepo na něm našla ten správný klíč` |

The diff audit found no other regressions:
- Book-wide renames inflect correctly: kroužek, náves, Snowball, spolkový dům, Společnost, umyvadlo, palčák and brána were all grepped with the word before them.
- There was no spill onto other objects: walk-in ≠ Pete's sklad; kyselý základ ≠ droždí/kvásek; kniha objednávek ≠ účetní kniha; the brána key ≠ the shop key or van key.
- No italics were lost and no `<bt>` was removed.

## Ledger mismatches
None. The 3 rows not found verbatim are superseded by later fixes in the same paragraph.

## Open decisions (Step 5)
- FP-CS-1 to FP-CS-10 are still accurate against the current text.
- The FP-CS-10 paragraph number [381] is in the APPLIED grid; it is w:p 682.
- The CTA is still missing (FP-CS-8).
- Doc ↔ Jessica is formal throughout Ch11, Ch17 and Ch21 (FP-CS-6).
- The units are as logged (FP-CS-4).
- No judgment call was applied silently. Nothing was undone.
- IT-CS-7 (`Jessice Claus` in the blurb) is not re-raised.

## Decisions added / refusals
- **Decisions:** 1, PC-FP-CS-1 (flour-bin word mixed nádoba/bedna; informational) in `PROOFCHECK_DECISIONS.md`.
- **Refusals:** 0.

## Checks (after fixes)
1. **looks_english:** `[]`
2. **bt_anchors check:** 9 spans, 0 unpaired (Flour Play / Frost and Found / Inn Trouble / The Binder's Bequest).
3. **check_matter:** 1 PASS, 0 FAIL.
4. **preflight --verify:** "source or corrected copy missing" (the raw file is in `_superseded/`), so I compared against the backup myself. Paragraphs 2013 → 2013. Italic runs 43 → 43, identical sequence. `<bt>` 9 → 9. Scene breaks 60 → 60. Changed paragraphs = exactly the 31 listed.
- **proofcheck.py re-run:** A=0 B=2 C=0 D=0 E=0 F=0 G=0 H=7 I=0 J=1. These are unchanged because all of them are false positives.

Backup: `translated/_EditLedgers/_proofcheck_backups/Flour Play - ASSEMBLED - FORMATTED_Czech.20261028-221915.docx`

## Verdict
**SIGNIFICANT (borderline) → a `full` re-read is recommended.** The clue-term chain itself was clean. The misses are:
- the Ch19 printer's **proof** read as "evidence", in the deduction;
- the Ch23 "you never changed it" left ambiguous rather than pinned to the lock;
- the Ch24 "took Danny aside";
- the Ch18 "by half" read as double;
- the Ch9 reversed frost image;
- 5 first-pass regressions.

The rate is 31 real defects in 15 sections read in full (≈ 2.1 per chapter read).
