# Inn Trouble - ASSEMBLED - FORMATTED_Romanian — PROOFCHECK (2026-10-28)

- **Mode:** targeted.
- **Edition:** `translated\corrected\Inn Trouble - ASSEMBLED - FORMATTED_Romanian.docx`, edited in place.
- **Backup:** `_proofcheck_backups\Inn Trouble - ASSEMBLED - FORMATTED_Romanian.20261028-173741.docx`.
- **Sources:** EN `translate_now\Inn Trouble - ASSEMBLED - FORMATTED.docx`; raw `translated\Inn Trouble - ASSEMBLED - FORMATTED_Romanian.docx`; series reference `translated\corrected\Flour Play - ASSEMBLED - FORMATTED_Romanian.docx`.

**Chapters read in full, EN against RO:**
- the three lowest-density chapters: Ch9, Ch27, Ch18;
- the plot-critical chapters: Ch2, Ch19, Ch22, Ch25, Ch26;
- also read in full: Ch6 and Ch14 (the perfect simplu → perfect compus conversion) and Ch10, Ch21, Ch24;
- front matter, blurb, What's Next, and the excerpt, checked against corrected Flour Play Ch1.

**First-pass diff:** all 470 changed paragraphs were diffed word by word, and every substantive change was read against the English. The 30 dash-only dialogue repairs were checked mechanically.

**Flags judged (A–J), 7 in total:** 0 real (2 already logged), 7 false positive.
- **E, stray heading at "[186]":** an artefact of the detector. The real stray heading is at [127], inside Ch2. It is already logged as IT-RO-2, and the body text around it is complete.
- **E, stray heading at [1187] inside Ch24:** heading line only; the body is complete (EN 756/757 → RO [1185]/[1189]). Already logged as IT-RO-2.
- **E, Ch2 at 44% and Ch3 at 184%:** side effects of the [127] heading. False positive.
- **F, 1924 in "Ch3":** this text sits in the real Ch2 ([129], [155]), and the English Ch2 has 1924. False positive.
- **G, Society missing in Ch2:** it is present at [163] and [183], which the heading drift put in "Ch3". False positive.
- **H, [876] „un picior":** Martha's foot (a body part, not a unit). False positive.
- Sections A, B, C, D, I and J had no flags.

## Missed by the first pass

| ¶ | Ch | Target (before) | English | Class | Fix |
|---|---|---|---|---|---|
| 1313 | 27 | „exact lucrul pe care Theo **îl ruinase** încercând să-l salveze" | "the very thing Theo had ruined himself trying to save" | reversed meaning (Theo ruined *himself*, not the Society) | „pe care Theo **se ruinase** încercând să-l salveze" — applied |
| 1315 | 27 | „Lucrul pe care îl făcuse greșit ca să o salveze continua să se prăbușească." | "The thing he had done wrong to save was still failing." | mistranslation (garbled sense) | „Lucrul pentru a cărui salvare greșise continua să se prăbușească." — applied |
| 600 | 9 | „asta ține doar de ei și de cine o da socoteală" | "between them and whatever they answer to" | garbled MT | „și de cel căruia îi dau socoteală" — applied |
| 963 | 18 | „Restul e între oameni și oricine o fi răspunzând ei." | "The rest is between people and whatever they answer to." | garbled MT (same callback as Ch9) | „Restul e între oameni și cel căruia îi dau socoteală." — applied |
| 161 | 2 | „Când familiile care **l-au stăpânit**" (= that owned the *town*) | "when the families that owned it [the paper] are gone" | mistranslation | „care **le-au deținut**" — applied |
| 957 | 18 | „Cineva stoarce descendentul." | "Someone's squeezing the descendant." (Fiona) | gender / missing *pe* | „Cineva o stoarce pe descendentă." — applied |
| 34 | blurb | „împărțea **pliante**… să ia **unul**" | "handing out cards" | term drift (the book uses *cărți de vizită*) | „cărți de vizită… să ia **una**" — applied |
| 1123 | 22 | „hârtia… pe care **îl** văzusem **stivuit**" | the stationery "I'd seen stacked" | agreement | „pe care **o** văzusem **stivuită**" — applied |
| 1124 | 22 | „**O luasem pe fiecare** în parte sperând că vreunul" (*drum*, neuter) | "I had walked down each of them hoping one would turn off" | agreement | „Pornisem pe fiecare dintre ele, sperând că vreunul" — applied |
| 1258 | 26 | „**L-am** potrivit fibră cu fibră" (*hârtia*, feminine) | "I matched it grain to grain" | agreement (in the confrontation) | „**Am potrivit-o** fibră cu fibră" — applied |
| 1262 | 26 | „încă **una** n-ar mai conta" | "one more [note] wouldn't matter" | agreement with *bilet* (the settled note word) | „încă **unul**" — applied |
| 826 | 14 | „Sau un **elf**." | "Or an elf." | term drift (Bram = *spiriduș* everywhere else) | „Sau un spiriduș." — applied |
| 371 | 5 | „Andrelele **Clairei**" | Claire's needles | name declension (a foreign name ending in -e takes *lui*; the excerpt has „lui Claire") | „lui Claire" — applied |
| 365 | 5 | „nici un cent" | "one thin dime" | orthography (DOOM: *niciun*) | „niciun cent" — applied |
| 1512 | excerpt | „bulevardului Evergreen" | Evergreen Avenue | capitalisation consistency (9× *Bulevardul*) | „Bulevardului Evergreen" — applied (FP follow-up PC-IT-RO-1) |
| 1604 | excerpt | „un rând întreg **întoarse**" | "a whole row of them turned" | agreement (copied from FP [150]) | „întors" — applied (FP follow-up PC-IT-RO-1) |

## Regressions introduced by the first pass

| ¶ | Ch | Target (before) | English | Class | Fix |
|---|---|---|---|---|---|
| 1102 | 21 | „**Păreați** gata s-o **pui** la pământ" | Noriko: "You looked like you were going to tackle Mrs. Pelletier" | address made half-formal (*Păreai→Păreați* only) | „s-o **puneți** la pământ" — applied |
| 418 | 6 | „Pip **venise și se așezase** alături, s-a uitat" | "Pip came and sat beside it, looked at it too" | tense-conversion leftover (pluperfect inside a narrative sequence) | „Pip **a venit și s-a așezat** alături" — applied |
| 866 | 15 | „Capul **Clairei**" (was „lui Claire") | Claire's head | declension changed the wrong way (inconsistent with *lui Constance* [892]) | „Capul lui Claire" — applied |

**Checked clean:**
- **Ch6 and Ch14 tense conversion:** the narration is perfect compus throughout. A search for perfect-simplu forms in the narration of the whole book finds none (only present tense and infinitives). No agreement errors from the conversion.
- **Book-wide replacements:**
  - *parcul*: every inflected form reads correctly (din/în/al parcului, parcul ăsta, actul parcului).
  - *suc de mere*: ×11, all correct (masa cu suc de mere, sucul de mere).
  - *Snowball*: ×12; *Dancer*: ×6 (lui Dancer).
  - *pridvor*: ×20. No *prispă*, *cidru*, *Vicleana*, *Societatea Istorică*, *Asociația*, *imaș*, *spațiu verde*, *bet* or *ji* left.
- **Clue chain:**
  - „safirul din inima ei" is identical at all 8 places: [118] note, [119], [151], [990] card, [992], [994], [1123], [1258]. The blurb [32] keeps the descriptive „safirul din inima broșei".
  - Every "five words" line says „patru cuvinte" ([994] ×2, [1008], [1123], [1203]). That matches the real count, per IT-RO-5.
  - *Bilet/bilete* is used for the note everywhere. *Scrisori* is used only for the 1924 letters, Fiona's mail ([1055], [1083] = EN "my letters"), the Pole letters and generic letters. *Fișă* is used for the cards. Ch19, Ch22, the Ch25 evidence list and Ch26 are all clean.
  - Ch22 [1129] quotes the note exactly as [118] has it.
  - Sam is owed the money (blurb [34], [474]). Cider is non-alcoholic.
  - Excerpt [1521]: „Foarte aproape" ("Very nearly"). The excerpt otherwise follows corrected FP Ch1 and Inn Trouble's own English (seven women [1510], eight [1566], bandstand, Sunday).

## Ledger mismatches
None. 20 random `_APPLIED.md` entries: 20/20 present. A full scan found all 691 "now" texts. The 21 apparent misses are the ledger's own `[…]`-truncated long texts, and each matches up to the truncation.

## Decisions added / refusals
- **Decision added:** PC-IT-RO-1 (informational): the same two excerpt slips are still in corrected Flour Play Romanian, at FP [150] and [44]/[726].
- **Re-checked:** IT-RO-1…7. Their quotes and paragraph numbers are still accurate, and none was applied beyond what it says.
- **Refusals:** none (19 of 19 edits applied).

## Checks (after the fixes)
- **looks_english:** `[]`.
- **bt_anchors check:** 8 spans, 0 unpaired. The only span texts are Inn Trouble, Frost and Found and Flour Play.
- **check_matter:** 1 PASS.
- **preflight --verify:** FAIL, as before. This comes from the raw → corrected first-pass deltas already declared in `_APPLIED.md` (italic −2 at [1198], `<bt>` 18→8 under ruling 5), not from this audit.
- **Against the pre-audit backup:** 1619 → 1619 paragraphs; the 28 italic runs are identical and in order; the `<bt>` spans are identical; 3 → 3 scene breaks. Only the 19 listed paragraphs differ.
- **proofcheck.py re-run:** A0 B0 C0 D0 E4 F1 G1 H1 I0 J0. Unchanged, because all seven flags were false positives or already-logged formatter items.

**Formatter items (already logged, not touched):**
- the stray „Capitolul 3" at [127] and [1187];
- the TOC collapsed to „Capitolul 31" [22];
- no Heading 1 styles.

## Verdict
**MINOR.** 19 fixes in total: 16 misses and 3 regressions. One is a reversed meaning in the Ch27 epilogue narration, [1313] (Theo "ruined the Society" instead of ruining himself). It is not in the plot chain. The clue chain, note/letters split, blurb, excerpt and omissions are all clean. Rate: 19 real defects across 13 chapters read in full plus front and back matter, about 1.5 per chapter read.
