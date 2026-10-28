# PROOFCHECK — Inn Trouble - ASSEMBLED - FORMATTED_Swedish (2026-10-28, cloud)

- **Mode:** targeted. No sub-agents. Read with python-docx, EN next to SV, one chapter at a time.
- **Read in full, sentence by sentence:** front matter + blurb; Ch2, Ch19, Ch22, Ch25, Ch26 (plot-critical); Ch12, Ch16, Ch26 (lowest change density, section M: 23 / 26 / 27 %); back matter (sell lines, What's Next, the Flour Play excerpt [1634]–[1693], closing line). Ch27 was also read in Swedish for the "ruined himself" lesson.
- **Diff audit:** all 733 changed paragraphs, raw vs corrected, on the same grid. 263 are punctuation-only (dialogue conversion), 45 are `sade`→`sa` only, and 425 contain targeted edits. Every targeted edit was read as a word-level diff, and the doubtful ones were checked against the English.
- **Ledger check:** every one of the 539 "Corrected" texts in `_PROOFREAD.md` is present in the file, which covers the 20-entry random sample. 0 mismatches.
- **Flags judged** (A–J):
  - E×3: REAL but already logged. The Kapitel 8 heading line is missing and the body is complete: [455] is the last line of Ch7, and [456] = EN [358] "The Forge sat…". The Ch7 247 % / Ch8 "no text" flags follow from that missing heading. This is a formatter job, IT-SV-1.
  - F×1: FALSE. `vintern -24` = 'that winter of 'twenty-four'.
  - H×2: FALSE. `inte ett uns hyfs` [368] and `varje uns av den träningen` [1145] are native idioms for 'an ounce of…'.
  - A, B, C, D, G, I, J = 0.

## Missed by the first pass
| Para | Ch | Swedish (before) | English | Class | Fix (applied) |
|---|---|---|---|---|---|
| 1427 | 26 | `"Vera," sa jag. "Theo stod för stölden.` | "Vera," I said. "Theo had the theft." | **Reversed meaning / clue chain.** `stå för stölden` = 'was behind / committed the theft', but Constance stole the brooch and Theo only *had* it from the letters. Ch22 [1278] and Ch23 [1310] already say `hade stölden` | `"Theo hade stölden.` ✔ |
| 1431 | 26 | `"Han stod för stölden. Du stod för köpebrevet.` | "He had the theft. You had the deed." | same, the two-halves line | `"Han hade stölden. Du hade köpebrevet.` ✔ (matches Ch22 `Han hade stölden`) |
| 1141 | 19 | `Korrespondens, Adelaide Blackburn till hennes syster` (Theo's card, italic) | Adelaide Blackburn to her sister | Grammar. `hennes` points to somebody else's sister, and Swedish needs the reflexive `sin` | `till sin syster` ✔ (italic run kept; the clue wording is untouched) |
| 1375 | 25 | `"I år ut och år in.` | "For years and years." | Ungrammatical | `"År ut och år in.` ✔ |
| 1116 | 18 | `Jag har klagomålen där i, de andra tjänarna…` | I've got the complaints in there | Broken phrasing | `där inne,` ✔ |
| 1131 | 19 | `i akt och mening att fria honom` | meaning to clear him | Term consistency. 'clear' = `rentvå` everywhere else (×10). The first pass itself changed `friat/fria` → `rentvått/rentvå` in Ch22 [1268]. `fria honom` also reads as 'propose to him' | `att rentvå honom` ✔ |

## Regressions introduced by the first pass
None found.
- Dialogue conversions (457): the scan found 0 paragraphs with an odd number of quotes, 0 attributions trapped inside the quotes, 0 cases of `." sa`, 0 dash-opened turns and 0 leftover ”/«» marks. The paragraphs read in full had correct turns, with resumed speech re-opened.
- `sade`→`sa` (97): the swap only touched the stand-alone word `sade`. No compound was hit: visade, bevisade, korsade, pressade, låtsades and the rest are all intact. No `sade` is left.
- Targeted edits read against the English: allmänningen / staden / Historiska sällskapet / köpebrev / lapp-vs-brev / äppelmust / herr-fru / du-address. All are correct in place, and none landed in a paragraph where the English differs. `parken` [87] is kept correctly (EN 'park'); [565] `kyrkan vid allmänningen` = 'church on the green' ✔.
- Italics: no runs were lost, and the `<bt>` spans are exactly 8 (Inn Trouble, Frost and Found, Flour Play).

## Clue chain (traced end to end)
- **"safiren i dess hjärta"** is identical at all 9 places: [116] [117] [134] (note / Ch2), [1141] [1143] [1145] (card / Ch19), [1270] (Ch22), [1310] (Ch23), [1401] (Ch26). The "five words" claims say `fyra` and match: [1145] ×2, [1159], [1270], [1362]. No `fem … ord` is left.
- **The note and the letters keep separate words.** The note is `lapp/lappen/lapparna/utpressningslapp(en/arna)` everywhere. Every remaining `brev/breven/brevet` was checked in context: all are the 1924 letters, other ordinary letters (refusal letters, the North Pole letters, Constance's letter) or compounds such as `köpebrev` and `brevpapper`. Ch19, Ch22, the Ch25 evidence list and Ch26 are clean.
- **Theo had the theft:** Ch22 and Ch23 were right. Ch26 was wrong and is fixed (above).
- **Sam is owed the money:** the blurb [34] and Ch1/Ch8/Ch17 all have it right. Cider = `äppelmust`, with 0 `cider` left. Snowball ×all, with 0 `Snöboll` left. The circle = `cirkeln`. The green = `allmänningen`. Porch = `veranda`. Paddock = `hagen` (10/10, = EN 10).
- **Ch19 short lines:** "It's the love that lets him" = `Det är kärleken som tillåter det`. The pronoun is not reversed. **Ch27:** "ruined himself" = `fördärvat sig själv` ✔.
- **Excerpt (Flour Play Ch1):**
  - The wording follows Inn Trouble's own English.
  - It has `choklad- och pekannötsmuffins`, so no walnuts.
  - The snowmen question `Stod inte barnens snögubbar vända mot vägen i går?` is correct, not inverted.
  - "Very nearly" = `Så gott som.`
  - The war memorial, the weekend and the overnight snow are all in Inn Trouble's English too, so they belong.
  - No half-paragraph was dropped where Flour Play splits a paragraph: every EN paragraph has its full SV text.
  - The tense slip `drar sig ihop` [1667] is verbatim from FP SV [108] → PC-SV-1.

## Open decisions re-checked (PROOFREAD_DECISIONS2.md IT-SV-1…8)
All the quotes are still accurate. No judgment call was applied that should not have been: there was no renumbering, the units were changed only by the SAFE rule, and the series names agree with FP SV. Nothing was undone.

## Decisions added / refusals
- PROOFCHECK_DECISIONS.md: PC-SV-1 (informational, FP-side tense slip).
- Refusals: 0.

## Checks (after fixes)
1. looks_english: `[]`
2. bt_anchors check: 8 spans, 0 unpaired (Inn Trouble / Frost and Found / Flour Play only)
3. check_matter: 1 PASS 0 FAIL
4. preflight --verify (raw→corrected): 1698→1698 ok, scene breaks 3→3 ok. Italic/bt FAIL = the first pass's declared changes, unchanged.
   - Own comparison, backup vs corrected: 1698 = 1698 paragraphs. 24 = 24 italic runs, in the same order, and the only italic text that changed is the card [1141] (`hennes`→`sin`). 8 = 8 `<bt>`. 3 = 3 scene breaks. Changed paragraphs: exactly [1116] [1131] [1141] [1375] [1427] [1431].
- proofcheck.py re-run: A=0 B=0 C=0 D=0 E=3 F=1 G=0 H=2 I=0 J=0 (all judged above; the fixes touched no flag).

## Verdict
**SIGNIFICANT (borderline):** one plot-chain reversal was missed. In the Ch26 confrontation, "Theo had the theft" read as "Theo was behind the theft", in 2 sentences. Ch22/23 had it right, and the rest of the chain traces clean, so a `full` re-run is optional rather than necessary. Rate: 6 real defects / 9 units read (7 chapters + front + back) ≈ 0.67 per chapter.
