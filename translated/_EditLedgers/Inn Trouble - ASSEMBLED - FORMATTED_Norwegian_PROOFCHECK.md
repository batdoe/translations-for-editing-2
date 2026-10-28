# PROOFCHECK — Inn Trouble - ASSEMBLED - FORMATTED_Norwegian (2026-10-28)

- **Mode:** targeted.
- **Files:** audited `translated/corrected/Inn Trouble - ASSEMBLED - FORMATTED_Norwegian.docx`. Raw for the diff: `_superseded/…_Norwegian.docx` (pre-web-pass, same 1664-paragraph grid), so the diff covers the web pass and the local pass together. English: `translate_now/Inn Trouble - ASSEMBLED - FORMATTED.docx`.
- **Backup:** `_EditLedgers/_proofcheck_backups/Inn Trouble - ASSEMBLED - FORMATTED_Norwegian.20261028-193246.docx`.
- **Paragraph numbers** below are the full `<w:p>` grid (as `proofcheck.py` counts). The first-pass ledgers number only non-empty paragraphs, so their numbers are lower.
- **Chapters read in full (EN vs NO, sentence by sentence):**
  - lowest change density: Ch9, Ch17, Ch20;
  - plot-critical: Ch2, Ch19, Ch22, Ch25, Ch26, plus Ch23 for the "Theo had the theft" lesson;
  - front matter and blurb;
  - all back matter (What's Next?, sell line, the Flour Play excerpt).
  - That makes 9 chapters plus the front and back matter. Ch27 [1319] ("ruined himself") and Ch18 "your man" were spot-checked.
- **Diff audit:** all 348 paragraphs whose text changed (37 glyph-only dialogue conversions excluded) were read as a word diff, and the doubtful ones were checked against the English. All 130 `_APPLIED.md` "now" strings are in the file: a random 20 were checked, then all 130.
- **Flags judged:**
  - **H (6):** all false positives. [45] `sider` = sides of the house. [108] [1011] [1507] [1613] `tomme` = "empty". [124] `fem mil` is left as is under ruling 4.
  - **A–G, I, J:** 0 flags.
  - **Total:** 0 real / 6 false.
  - **Re-run after the fixes:** A=0 B=0 C=0 D=0 E=0 F=0 G=0 H=6 I=0 J=0. No change was expected, because none of the fixes was a flagged item.

## Missed by the first pass
| Para | Ch | Norwegian (was) | English | Class | Fix (applied) |
|---|---|---|---|---|---|
| 1274 | Ch26 | `– Vera, sa jeg. – Theo sto for tyveriet.` … `Han sto for tyveriet. Du hadde skjøtet.` | "Theo had the theft." … "He had the theft. You had the deed." | **reversed meaning / clue chain.** `sto for` = "was behind / committed". It makes Theo the thief, but Constance stole the brooch and Theo only knew of it. This breaks the two-halves deduction in the confrontation | `Theo visste om tyveriet.` … `Han visste om tyveriet. Du hadde skjøtet.` ✔ |
| 1120 | Ch22 | `Han hadde tyveriet.` | "He had the theft." | clue chain: a word-for-word calque that reads oddly | `Han visste om tyveriet.` ✔ |
| 1157 | Ch23 | `Theo hadde tyveriet.` | "Theo had the theft." | same calque, same deduction | `Theo visste om tyveriet.` ✔ |
| 260, 437, 768, 977 ×2, 1104, 1264 | Ch4, Ch7, Ch13, Ch19, Ch22, Ch26 | `utpressingsbrev(et/ene)` | "the blackmail note(s)" | **note/letters collision.** The note was still called a *brev* in 7 places, including Ch19 [977] next to `brevet kortet oppsummerte` (the 1924 letter), Ch22 [1104] next to `brevene som beskrev brosjen`, and the Ch26 confrontation [1264]. The first pass had kept the compound as a set phrase. The rule says the note never shares the letters' word | `utpressingslapp(en/ene)`, gender agreed (`en`). This matches Ch8 [447] `utpressingslappen` ✔ |
| 393 | Ch6 | `på grunn av Komet i Maple Street` | "for Comet on Maple Street" | reindeer name. Every other reindeer keeps its English name, and Book 1 NO has `Comet` | `Comet` ✔ |
| 203, 231, 805, 1003, 1430, 1436 | Ch3, Ch14, Ch19, Ch30 | `hagen` ×2 / `innhegningen` ×4 | "the paddock" | term drift. This edition had *luftegården* ×4 (Ch10), *innhegningen* ×4 and *hagen* ×2 (*hage* = garden). Book 1 NO and Flour Play NO both use *luftegård* | `luftegården` ✔. [1436] became `Bortenfor luftegården lå ildstedet` ("Out past the paddock") |
| 147 | Ch2 | `jeg ble stående på trappen` | "I stood on the porch" | porch drift. The other 22 places use *veranda* | `på verandaen` ✔ |
| 129 | Ch2 | `med en lapp på i hennes håndskrift` | "with a tag on it" | term collision: *lapp* is the note's word | `med en merkelapp på` ✔ |
| 149, 650, 660, 668, 1078, 1174 | Ch2, Ch11, Ch21, Ch24 | `historielaget` | "the Society" | name-case drift. The edition writes `Historielaget` 39× | `Historielaget` ✔. Generic `et døende historielag` and `Frost Falls historielag` were left as they are |
| 1211 | Ch25 | `i Veras mappeboks` | "in Vera's refile basket" | term drift. Ch23 says `kurven for gjeninnplassering` | `i Veras kurv for gjeninnplassering` ✔ |
| 905 | Ch17 | `Han presset håndbaken hardt mot pannen` | "the heel of one hand" | mistranslation (*håndbak* = back of the hand) | `håndroten` ✔ |
| 1535 | What's Next? | `En innleid vekt.` | "A borrowed scale." | mistranslation (*innleid* = hired) | `En lånt vekt.` ✔ |
| 1539 | What's Next? | `en gutt som kjedet seg, med en stjålet boks` | "a bored boy with a stolen can" (the graffiti) | ambiguity (*boks* = box/tin) | `en stjålet sprayboks` ✔ |
| 1622 | excerpt | `med mindre man rømmer ut et lokale` | "unless you're clearing a space out" | wrong verb (*rømme* = flee/evacuate). Corrected Flour Play NO has `rydder ut et lokale` | `rydder ut et lokale` ✔ (FP wording reused) |

## Regressions introduced by the first pass (web pass or local pass)
| Para | Ch | Raw | Corrected (before this audit) | Problem | Fix (applied) |
|---|---|---|---|---|---|
| 417 | Ch6 | `en utpressingstrussel` | `et utpressingsbrev` | The fix moved the note onto the letters' word | `en utpressingslapp` ✔ |
| 948 | Ch18 | `det utpressingstrusselen sa` | `det utpressingsbrevet sa` | Same problem, in the sentence about Neil's folder vs the note | `det utpressingslappen sa` ✔ |

No other regressions were found:
- Every term swap was grepped for broken forms (`lappen`/`den` agreement, `ildsted` neuter, `eplemost`, `foajé/foajeen`, `Historielaget`), and none were found.
- The 348 changed paragraphs keep their meaning against the English. These doubtful changes were checked and are right:
  - [111] `kardiganen riktig knappet` (EN "buttoned right today");
  - [389] `talte dem og skrev tallet ned`;
  - [905] `tilgitt`;
  - [1056] `paibordet`;
  - [1062] / [1264] `linjene` (laid lines);
  - [1291] `full benådning` ("free pardon");
  - [1412] `seksten mål` (four acres ≈ 16.2 dekar, accurate);
  - [1196] `en hundeleting`;
  - [1395] `en annen vei`;
  - the excerpt [1560] `– Nesten.`
- Ch19 [997] Nick: `Det er kjærligheten som tillater ham det, Jess` (pronoun right).
- Ch27 [1319] `akkurat det Theo hadde ruinert seg for å berge` (reflexive right).
- Ch18 `han din` (= "your man", not "husband").
- Italic runs (29) are unchanged, and the 8 `<bt>` spans are unchanged.

## Clue chain (traced end to end)
- **"The sapphire at its heart"** = `safiren i hjertet`. It is identical in every place:
  - the note [116];
  - Jessica's readings [117] [134];
  - the card [973] (in parentheses);
  - [975] [977] ×2;
  - the Ch22 recap [1104];
  - Ch23 [1157];
  - the confrontation [1264].

  Every "five words" line reads `tre ord` ([977] ×2, [991], [1104], [1211]), and that is right because the phrase has 3 words. The blurb paraphrases the phrase, as the English does.
- **Note vs letters vs cards.** The note is now `lapp(en/ene)` / `utpressingslapp` everywhere. `brev` means only:
  - the 1924 letters;
  - Constance's letter [950];
  - rejection letters [731] [737];
  - Fiona's mail [1038];
  - North Pole letters;
  - generic letters [54] [383].

  The cards are `kort`. Ch19 [981] reads `Og kortet var i Theos hånd`, and [973] has `til sin søster` (reflexive). The Blackburn papers (`Blackburn-familiens papirer`) and the deed (`skjøte`) use different words.
- **Sam is owed:**
  - blurb [34]: `som har tjue dollar til gode og ikke får et rett svar`;
  - Ch17 [905]: `Si til henne at det er tilgitt`.
- **The other terms:**
  - cider = `eplemost` everywhere (0 *sider/cider*);
  - Snowball ×12;
  - circle = `syklubben` (NO2-D1 still open);
  - green = `allmenningen` (34; [349] `gressletten` is a deliberate apposition);
  - porch = `veranda`;
  - paddock = `luftegården` (now unified).
- **Currency and units:** 0 krone/øre and 0 spelled-out *tomme* (inch). The 7 currency fixes and 7 *tomme* fixes were confirmed.
- **Blurb tense:** present, as in the English. That is fine.

## Excerpt (Flour Play Ch1, back matter)
- **Wording:** the excerpt is 1:1 with Inn Trouble's own English (war memorial, weekend, bandstand, permit board, chocolate-pecan → `sjokolade- og pekannøttmuffins`, "Very nearly" → `Nesten.`, snowmen question right). But it is a separate translation from corrected Flour Play NO Ch1, even where the two English texts match. This is the same class as PC-FIL2-1 / PC-NL2-2, so it is not re-raised. One FP wording was reused where the excerpt's verb was wrong ([1622]).
- **Circle word:** the first pass changed the excerpt's `sirkelen` to `syklubben`. Flour Play NO uses `sirkelen`. This follows whatever Lisa rules on NO2-D1.
- **Note, not fixed:** EN [977] has Dot's two lines in one paragraph ("Brushed them out… Or the wind filled them." "It's a joke…"). The NO grid splits them into two dash turns, [1648] and [1649], which reads as two speakers. Fixing this would need a paragraph merge, and the paragraph count may not change.

## Decisions / refusals
- **Decisions:** no new question for Lisa. Two informational items were added to `PROOFCHECK_DECISIONS.md`: the paddock unification, and the excerpt circle word tied to NO2-D1.
- **NO2-D1** (circle name) is still open. Its quote is still accurate: `syklubben` about 29×.
- **Refusals:** 0.

## Four checks
- **looks_english:** [] (empty).
- **bt_anchors check:** 8 spans, 0 unpaired. The only span texts are Inn Trouble / Frost and Found / Flour Play.
- **check_matter:** 1 PASS, 0 FAIL.
- **preflight --verify:** returns "source or corrected copy missing", because the raw file is in `_superseded/`. Verified by hand against the backup instead:
  - 1664 → 1664 paragraphs;
  - 31 paragraphs changed;
  - 29 italic runs, identical and in order;
  - 8 `<bt>` spans unchanged;
  - 3 `* * *` unchanged.

## Verdict: **SIGNIFICANT**
- The Ch26 confrontation said Theo committed the theft (`Theo sto for tyveriet`). That reverses the two-halves deduction. The blackmail note also still shared the letters' word in 8 places, including Ch19, Ch22 and Ch26.
- Real defects found: 31 paragraphs, 33 edits. That is about 3.4 per chapter read, though many are book-wide term drift.
- Recommend a `full` re-read of this edition.
