# PROOFCHECK — Inn Trouble - ASSEMBLED - FORMATTED_Czech (2026-10-28, cloud)

- **Mode:** targeted. No sub-agents. Read with python-docx, EN next to CZ, one chapter at a time.
- **Read in full, sentence by sentence:** front matter + blurb; Ch2, Ch4, Ch18 (lowest change density, section M: 18 / 17 / 15 %); Ch19, Ch22, Ch25, Ch26 (plot-critical); Ch27 (the "ruined himself" lesson); Ch15 first half incl. the restored loop paragraph [778]; back matter (sell lines, What's Next, the Flour Play excerpt [1471]–[1565], closing line). Ch23 [1136]–[1138] read for the "Theo had the theft" chain.
- **Diff audit:** all 468 changed paragraphs, raw vs corrected, on the same grid, as word-level diffs (24 punctuation-only dialogue conversions, 444 with word edits). Doubtful edits were checked against the English.
- **Ledger check:** every one of the 649 "now" texts in `_PROOFREAD.md` was looked up in the file (covers the 20-entry random sample). 630 found verbatim; the other 19 are paragraphs edited twice, where the later edit superseded the first (e.g. [960] Theoov- → Theov-, [52] alej → třída). 0 real mismatches.
- **Flags judged** (A–J):
  - A, B, C, D, E, F, G, I = 0. A separate scan of every letter outside the Czech alphabet and of zero-width characters found nothing: the Vietnamese / Cyrillic / Greek leaks are gone and nothing else remains.
  - H×8: all FALSE. `korunovaci` / `korunách` / `korunovaní` = coronation / treetops / crowned; `otravuje` / `Otravoval` / `otrávená` / `otráveným` = pesters / bothered / fed up; `jediná stopa` [1547] = footprint.
  - J×2: REAL but already handled. [2] = the MT's invented title, emptied, IT-CS-1. [778] = the Ch15 MT loop; the restored text „Každý v tomhle městě chce mluvit o sobovi … ale nikdo nechce mluvit o tom, že se Historická společnost zavírá.“ is complete against EN [538] (cuff = manžeta ✔).

## Missed by the first pass (all applied)
| Para | Ch | Czech (before) | English | Class | Fix |
|---|---|---|---|---|---|
| 1136 | 23 | `Theo měl krádež na svědomí.` | Theo had the theft. | **Reversed meaning / clue chain.** „mít na svědomí“ = 'he committed it'. Constance stole the brooch; Theo only *had* that half from the letters (same as the TR/PT-BR lesson) | `Theo měl krádež.` (= Ch22 [1101] „Měl krádež.“, Ch26 „On měl krádež.“) |
| 1253 | 26 | `„Theo měl na starosti krádež.` | "Theo had the theft." | **Reversed meaning / clue chain.** 'Theo was in charge of the theft' | `„Theo měl krádež.` (matches the two-halves line „On měl krádež. Vy jste měla listinu.“ in the same paragraph) |
| 863 | 16 | `nečetl Blackburnovy listiny jen tak obecně` | didn't only read the Blackburn papers in general | **Clue-chain term clash.** `listina` is the settled word for the DEED, and the deduction is that the deed was NOT among the Blackburn papers | `Blackburnovy písemnosti` (Ch19's word) |
| 713 | 13 | `v Blackburnových listinách` | in the Blackburn papers | same | `v Blackburnových písemnostech` |
| 855 | 16 | `klíče od starých městských listin. Vera má na starosti kupní smlouvy a pozemkové knihy` | the keys to the town's old papers. Vera keeps the deeds and the property records | same, plus deed drift. The settled terms are listina and majetkové záznamy (drawer labels LISTINY / MAJETKOVÉ ZÁZNAMY) | `…městských písemností. Vera má na starosti listiny a majetkové záznamy` |
| 290, 294, 336 | 4 | `zažloutlé kupní smlouvy` / `něco o smlouvách` / `staré smlouvy` | yellowed deeds / about the deeds / the old deeds | Term drift: deed = listina (the first pass's table) | `listiny` / `o listinách` / `staré listiny` |
| 649 | 11 | `k listinám hostince` | the deed to the Winter Wonderland Inn | Number: one deed | `k listině hostince` |
| 909 | 18 | `dělá přesně to, co tvůj muž říká, že dělá` | does what your man says it does | Mistranslation: `tvůj muž` = 'your husband'. Claire means Neil, the man Jessica asked about | `co ten tvůj chlapík říká` |
| 911 | 18 | `v duchu už téměř rozhodnutá` | already most of the way to certain | Mistranslation: decided ≠ certain | `téměř jistá` |
| 1243 | 26 | `aby se nikdo neodvážil pátrat po tom, co v nich stálo` | so that nobody would think to ask what was in them | Mistranslation: 'dare' ≠ 'think to' | `aby nikoho ani nenapadlo zeptat se, co v nich stálo` |
| 1243 | 26 | `na hlavičkovém papíře Společnosti` | on the Society's stationery | Term drift: stationery = dopisní papír (Ch23, Ch27); hlavičkový = letterhead | `na dopisním papíře Společnosti` |
| 35 | blurb | `nejteplejší týden, jaký tu za poslední roky zažila —` | the warmest week the town has had in years — | Subject: the TOWN's warmest week, not Jessica's. Also the dash: em → en, as blurb [31] and the edition | `jaký město za poslední roky zažilo –` |
| 253, 281, 742, 1380, 1386 | 3, 14, 30 | `ohrada` ×5 | paddock (EN ×10) | Term drift: the same paddock was `výběh` ×5 (Ch10, Ch19) and `ohrada` ×5. Book 1 Czech uses `výběh` ×4 | `výběh` (s výběhem / za výběhem / z výběhu) — now 10/10 |
| 956 | 19 | `Adelaide Blackburnová její sestře` (Theo's card, italic) | Adelaide Blackburn to her sister | Grammar: Czech needs the reflexive (`její` = someone else's sister) | `své sestře` (italic run kept; clue wording untouched) |
| 948 | 19 | `Archiv byla dlouhá zadní místnost` | The archive was the long back room | Agreement (masc. subject, fem. verb) | `Archivem byla dlouhá zadní místnost` |
| 176 | 2 | `rodiny, které ho vlastnily, pryč nebo ho nechtějí` | the families that owned it… don't want it underfoot | Agreement: the antecedent is `staré papíry` (plural) | `které je vlastnily … je nechtějí` |
| 1247 | 26 | `„Ne od Fiony.` | "Not from Fiona." | Calque (krást komu, not od) | `„Ne Fioně.` |
| 98 | 2 | `poslali dítě s vzkazem` | sent a child with a note | Preposition form (se before vz-) | `se vzkazem` |
| 786 | 15 | `byl u ještě někoho ten chlápek` | has anybody else had the man | Word order | `byl ještě u někoho` |
| 498 | 8 | `teplého kruhu, který vrhval oheň` | the warm circle the fire threw | Typo | `vrhal` |
| 1487 | excerpt | `o polovinu větší než kdokoli jiného` | half again the size of anyone else's | Broken case (nominative + genitive). Copied verbatim from Flour Play CZ [56] → PC-CS-1 | `než věnec kohokoli jiného` |
| 102, 162, 826, 978, 1031 | 2, 15, 19, 20 | `„Prosím?“ přitiskla…` / `„…nechápeš?“ zavrtěla…` / `„…Max,“ sledovala mě Dot.` / `„…přes něj,“ můj hlas zněl drsně.` / `„…kdo to je,“ podívala se mi do tváře…` | (action beats after speech) | Dialogue system: a non-speech verb after the closing quote starts a new sentence | Capitalised / rebuilt as `řekla Dot a sledovala mě`, `přes něj.“ Hlas mi zněl drsně.`, `řekla a pozorovala mou tvář…` |

## Regressions introduced by the first pass
| Para | Ch | Czech (corrected) | Raw | English | Fix |
|---|---|---|---|---|---|
| 964 | 19 | `A ten vzkaz byl psán Theovou rukou.` | `A ten lístek byl psán Theoovou rukou.` | And the card was in Theo's hand. | **Clue chain.** The book-wide lístek→vzkaz rename (note = vzkaz) also hit the CARD. The sentence now said that the *blackmail note* was in Theo's handwriting, but the note is written in a disguised hand and the clue is the card. Restored `A ten lístek byl psán Theovou rukou.` (keeping the first pass's Theov- declension) |

Otherwise, no regressions:
- **vzkaz forms:** all 61 were checked in context. The cases are correct, because lístek and vzkaz decline alike (masc. inanimate). Every remaining `lístek` is a card, the pawn receipt [158] or holly leaves [1411]. No note is called `dopis`.
- **Dialogue conversions** (Ch1, Ch13–14): balanced, with attributions rebuilt correctly.
- **Address edits:** Sam / Bram / Noriko / Vera / Neil, all per the table.
- **The other targeted edits:** read against the English.
- **The excerpt:** it follows Inn Trouble's own English. The pecans are `čokoládovo-pekanových`. The snowmen question „Nestáli včera ti dětští sněhuláci všichni čelem k silnici?“ is correct. "Very nearly" = `Skoro.`. The war memorial, the weekend and the overnight snow are all in this English too. No half-paragraph was dropped.
- **Blurb:** `Jessice Claus` [1457] is an inherited Flour Play form. It is already logged as IT-CS-7.

## Clue chain (traced end to end)
- **„safír v jejím srdci“** is identical at all 9 places: [132] [134] [168] (Ch2), [956] [958] [960] (card / Ch19), [1085] (Ch22), [1136] (Ch23), [1243] (Ch26). The "five words" claims all say four, which is true: [960] ×2, [974], [1085], [1190]. No `pět slov` is left.
- **Note vs letters vs cards:** the note is `vzkaz` everywhere, the 1924 letters are `dopisy` and the cards are `lístek/karta`. Ch19, Ch22, the Ch25 evidence list [1190] and Ch26 are clean after the [964] fix.
- **Theo had the theft:** Ch22 was right. Ch23 and Ch26 were wrong and are fixed.
- **Sam is owed the money:** blurb [33] ✔, Ch8 [512] ✔. Cider = `mošt`. Snowball ✔ (no Sněhulák / Snížek left). The circle = `kroužek` (the 7 remaining `kruh` are ordinary circles). The green = `náves`. Porch = `veranda` (23 = EN 23). Paddock = `výběh` (now 10/10).
- **Ch19 short lines:** "It's the love that lets him, Jess" = „Právě láska mu to umožňuje, Jess.“, so the pronoun is not reversed. **Ch27:** "ruined himself trying to save" = „kterou se Theo pokusil zachránit a zničil u toho sám sebe“ ✔.

## Open decisions re-checked (PROOFREAD_DECISIONS2.md IT-CS-1…8)
All the quotes are still accurate. No judgment call was applied that should not have been: there was no renumbering, the units were changed only by the SAFE rule, and the series names agree with FP CS / Book 1. Nothing was undone. (IT-CS-4 Theo↔Jessica ty / FP vy is still open.)

## Decisions added / refusals
- PROOFCHECK_DECISIONS.md: **PC-CS-1** (informational, a Flour Play CZ follow-up: the same broken `než kdokoli jiného` in FP CZ [56], plus the elliptic `Ten od Ivy je pro kostel a Ellie pro nemocnici` in FP [88] / here [1519]).
- Refusals: 0.

## Checks (after fixes)
1. looks_english: `[]`
2. bt_anchors check: 8 spans, 0 unpaired (Inn Trouble / Frost and Found / Flour Play only)
3. check_matter: 1 PASS 0 FAIL
4. preflight --verify (raw→corrected): 1570→1570 ok, scene breaks 3→3 ok. The italic / bt FAIL comes from the first pass's declared changes (sweep +1 italic, −8 stray bt / +4 anchors) and is unchanged.
   - Own comparison, backup vs corrected: 1570 = 1570 paragraphs. 21 = 21 italic runs, in order, and the only italic text changed is the card [956] (`její`→`své`). 8 = 8 `<bt>`. 3 = 3 scene breaks. Changed paragraphs: exactly the 32 listed above.
- proofcheck.py re-run: A=0 B=0 C=0 D=0 E=0 F=0 G=0 H=8 I=0 J=2. All were judged above, and none of the fixes touched a flag.

## Verdict
**SIGNIFICANT** — two clue-chain defects in the plot chapters were missed or introduced:
- the first pass's own rename made the blackmail note "in Theo's hand" [964];
- "Theo had the theft" read as "Theo committed the theft" in Ch23 [1136] and Ch26 [1253].

Further defects:
- "Blackburn papers" used the deed word ×3, which blurs the two-halves deduction;
- "tvůj muž" (= your husband) [909].

All are fixed. 33 real defects (32 paragraphs) in ≈11 units read (9 chapters + front + back matter) ≈ **3 per chapter**. A `full` re-run of the remaining 22 chapters is recommended.
