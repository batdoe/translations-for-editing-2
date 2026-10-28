# PROOFCHECK — Flour Play - ASSEMBLED - FORMATTED_French (2026-10-28)

- **Mode:** targeted.
- **Edition:** `translated/corrected/Flour Play - ASSEMBLED - FORMATTED_French.docx`.
- **Backup:** `_proofcheck_backups/Flour Play - ASSEMBLED - FORMATTED_French.20261028-210100.docx`.
- **Inputs:**
  - Raw for the diff: `_superseded/…_French.docx`, on the same 2226-paragraph grid.
  - English: `translate_now/Flour Play - ASSEMBLED - FORMATTED.docx`.
- Paragraph numbers are full-document indices (empty paragraphs included), which is the PROOFCHECK_FLAGS numbering. The first-pass `_PROOFREAD.md` numbers count text paragraphs only.

## Chapters read in full (EN vs FR, sentence by sentence)
- **Front matter + blurb:** blurb tense is present ✓ and BAKERY ≠ pâtisserie ✓.
- **Ch1:** the excerpt source.
- **Ch16, Ch20, Ch17:** the lowest change density.
- **Plot-critical:**
  - Ch9: the complaint / cold room.
  - Ch11: sour base, ten times, "nothing I can name".
  - Ch13: Pete cleared.
  - Ch18: the literal "cold room".
  - Ch19: the deduction.
  - Ch21: Pelkey's.
  - Ch22: the case.
  - Ch23: the confrontation.
  - Ch24: the charges.
  - Ch25: Greta's exoneration.
- **Ch27 closing scenes + all back matter:** sell lines, What's Next, and the excerpt structure (50/50 paragraphs; text from the published French edition, per FP-FR-6).
- **Not read in full:** Ch2–8, Ch10, Ch12, Ch14, Ch15, Ch26. These were covered by the raw→corrected diff review only.

## Flags judged
- **A–D, G, I, J:** 0 flags.
- **E (3):** all REAL but known.
  - The Ch10 heading line is missing, and Ch10's body runs on under Ch9. That explains "Ch9 209%" and "no text under Ch10". The body is complete (EN 39 paragraphs present). This is formatter work, already logged as FP-FR-1. No body text is missing.
- **F (1):** FALSE POSITIVE. Ch15 "20" is « d'ici le 20 » = "by the twentieth" (also Ch20 [1478]).
- **H (16):** all FALSE POSITIVE.
  - *livres de* = books or ledgers.
  - *mille* = thousand.
  - *pouce* = thumb.
  - *deux pieds* = "on my feet".
  - *centime* ×2 is the stock idiom; it comes under PC-FR2-1.
  - Poison/toxic/cider: none.
- **Totals:** 4 real (all known decision FP-FR-1) · 17 false positives.

## Clue chain (step 3) — traced at every occurrence
- **Sour base:** « base acide » at all 20 EN places (Ch11 ×3, Ch13, Ch17 ×4, Ch18, Ch19, Ch21 ×4, Ch22 ×2, Ch23 ×2, Ch24 ×2). It is never levain/levure.
  - [797] had « base acide de boulangerie industrielle ». EN is "a bread kitchen's"; fixed to « à pain ».
- **Walk-in vs cold room:** the two stay different words.
  - Walk-in = « chambre frigorifique ». Joyce's word = « la chambre froide ». Hand-sink = « lave-mains », and her word = « l'évier Hobart ».
  - These hold in Ch9 [683] [685], Ch17 [1265], Ch20 [1498] [1502], Ch22 [1666], Ch23 [1741] [1743] and Ch24 [1848].
  - Pete's locker = « local frigorifique », which does not leak.
  - Ch18's literal "a cold room at midnight" = « une pièce froide », which does not collide with Joyce's word.
  - The first-pass rename did not spill.
- **Ten times:** « Dix fois » / « à dix fois le dosage » ✓.
- **Gate key / lock:**
  - The gate key is « la clé du portail » [1512]. The padlock is « cadenas » throughout.
  - "You never changed it" = « le cadenas » [1765] ✓.
  - The key is handed back [1823]–[1835] ✓.
- **Order book:** « carnet de commandes » ×7 ✓. Elsewhere it is « carnet » only for that book; Tanaka's notebook is also « carnet », which is fine.
- **"Nothing I can name":** « Rien que je puisse nommer » [785] ✓.
- **Two degrees:** now identical, « deux degrés sous la norme », at [676] [1134] [1138] ([676] fixed). °F is still open as FP-FR-2.
- **No poison:** ✓.
- **Pip:** she/her ✓ (gender grep + reads).
- **Jessica:** feminine ✓.
- **Joyce:** feminine; 65 [1852]; 25 years ago and 15 years together ✓; « d'ici le 20 » ✓.
- **Other terms:**
  - DIRTY = SALE (not a vulgarity) ✓.
  - Grange = « la Grange » (one rendering) ✓.
  - Dollars ✓.
  - *The Binder's Bequest* anchors kept (9 spans) ✓.
  - The closing "Start reading…" is MISSING (PC-FR3-1).

## Lessons checked explicitly
- **Ch13** "a temper he didn't have" = « un tempérament qu'il ne possédait pas » (disposition) ✓.
- **Ch17:** the FIGURE goes past the pharmacy light (« Je l'ai perdu de vue après la lumière de la pharmacie ») ✓.
- **Ch19:**
  - Jessica supplied the gold shop (« Moi, j'ai entendu : la boutique dorée. Il n'a jamais dit… ») ✓.
  - The printer's "proof" = « une épreuve » ✓.
- **Ch23:**
  - Lock = « le cadenas » ✓.
  - Greta would have been robbed (« Tu aurais subtilisé mon Thanksgiving ») ✓.
  - Subject/object and negation in the whole confrontation ✓.
- **Ch24:** "took Danny's word" = « recueilli… le témoignage de Danny » ✓.
- **Ch1:**
  - "half again" = « une fois et demie » ✓.
  - Chocolate-pecan = pacanes/pécan (not walnut) ✓.
  - The bakery box (fixed).
- **Ch22:** Tanaka's turns are intact, and the Nick/Jessica attribution was fixed by the first pass ✓.
- **Speaker continuity in multi-speaker scenes:**
  - Ch21 splits EN paragraphs into speech / narration / speech, but each resumed turn follows a narration beat about the same speaker. No wrong-speaker reading.
- **Renames:**
  - alley → ruelle, walk-in/cold room, sour base, order book, pie → tarte, mitaine → moufle: no spill and no broken agreement found.
  - porch: one drift (fixed).
  - paddock = « paddock » ✓.
- **Cross-book (Inn Trouble FR audit, PC-FR2):** its excerpt slips (1.5×, « à la Grange ») were IT-side; FP FR already had them right. Porch → porche and paddock → paddock now match IT FR.

## Step 2 — first-pass edits audited
- 574 paragraphs differ from the raw input after typography normalisation, and every one was reviewed word-diffed.
- Edits checked against the English included: [440] base-ball, [599]/[836] local frigorifique, [631] cafetière, [636]/[1409] Hollyhock Lane, [642], [1235] (the English "says" line removed — the French twin is complete), [1655] a-t-il, [1666]/[1741] the cold-room lines, [1840], [1856] restitution, [1912], [2003] and [2046].
- Three regressions were found (below).
- **20 random `_PROOFREAD.md` rows** (seeded sample): the "now" text was present at the logged paragraph in 20/20. No ledger mismatches.

## Missed by the first pass (all APPLIED)
| # | Para | Ch | French (before) | English | Class | Fix |
|---|---|---|---|---|---|---|
| 1 | 51 | 1 | « À peu près. » | "Very nearly." | mistranslation (weakened; lesson line) | « À très peu de choses près. » (= Inn Trouble FR excerpt) |
| 2 | 76 | 1 | une boîte à pâtisserie de la taille d'une boîte à chapeau | a bakery box | term (Greta's bakery ≠ rival pâtisserie) | une boîte de boulangerie… |
| 3 | 676 | 9 | deux degrés en dessous de la norme | two degrees under code | clue wording not identical at its 3 places | deux degrés sous la norme |
| 4 | 797 | 11 | une base acide de boulangerie industrielle | a bread kitchen's sour base | mistranslation | …de boulangerie à pain |
| 5 | 804 | 11 | Ce qui était arrivé aux pâtisseries de Greta | Greta's baking | term (bakery ≠ pâtisserie) | aux fournées de Greta |
| 6 | 1229 | 17 | elle n'a rien à vous montrer | she doesn't have to show you a thing | mistranslation ("has nothing to show") | elle n'est pas obligée de vous montrer quoi que ce soit |
| 7 | 1434 | 20 | de la boulangerie Wendt là-bas à Bridgton | Wendt's Bakehouse over in Bridgton | business-name consistency | de Wendt's Bakehouse, là-bas à Bridgton |
| 8 | 1444 | 20 | Elle ne refile pas ses clients à n'importe qui. | She doesn't hand her customers to anybody. | meaning ("not to just anyone") | Elle ne refile ses clients à personne. |
| 9 | 1524 | 20 | Que nous étions trop vieilles pour continuer. | too old to keep it up (the quarrel) | ambiguity (reads as "keep working") | …pour faire durer la brouille. |
| 10 | 1544 | 20 | Je ne viendrai pas te voir tant que je ne serai pas fixée. | I won't come to you with it until I do. | mistranslation | Je ne t'en parlerai pas tant que je n'en serai pas sûre. |
| 11 | 1652 | 22 | un dossier que j'avais bâti moi-même et vérifié auprès de personne | checked against nobody | grammar (missing ne) | …et que je n'avais vérifié auprès de personne |
| 12 | 1791 | 23 | sans penser à mal | without a thought in my head | mistranslation (= "without ill intent") | sans réfléchir une seconde |
| 13 | 1819 | 23 | Tout ce que j'ai entre les mains, c'est… | What I have is… | nuance ("all I've got" undercuts the case) | Ce que j'ai entre les mains, c'est… |
| 14 | 1937 | 25 | Il l'a mangée en entier debout… | He ate it…, every crumb | agreement (le coin) + "every crumb" | Il l'a mangé jusqu'à la dernière miette, debout… |
| 15 | 1941 | 25 | Elle avait gâché la farine exprès | She'd soured the flour | term (aigrir = the book's sour word) | Elle avait aigri la farine exprès |
| 16 | 1957 | 25 | avait tenté de s'accaparer à Bridgton | tried to carry off to Bridgton | mistranslation | avait tenté d'emporter à Bridgton |
| 17 | 2130 | 27 | les marches du perron | the porch steps | series term (porch = porche; perron = stoop) | les marches du porche |

## Regressions introduced by the first pass (all APPLIED)
| # | Para | Ch | French (before) | English | Class | Fix |
|---|---|---|---|---|---|---|
| 1 | 911 | 13 | avait besoin d' un tempérament | — | typography: stray space from the first-pass rewrite | d'un |
| 2 | 1337 | 18 | à deux bons mètres | six clean feet (1.83 m) | units: the rewrite overstated it (>2 m) | à près de deux mètres |
| 3 | 1945 | 25 | la buée couvrait la vitre si épais qu'on… | the steam stood on the glass so thick | grammar in the first pass's own translation of an English sentence | la buée était si épaisse sur la vitre qu'on… |

## Ledger mismatches
- None. 20/20 sampled rows verified.

## Open decisions re-checked (step 5)
- **FP-FR-1:** the Ch10 heading quote is still accurate ([701] « Le nom m'est parvenu de biais… »). Formatter.
- **FP-FR-2:** the quote [429]/[676] now reads « deux degrés sous la norme », identical ×3 (PC-FR3-3).
- **FP-FR-3:** 45 kg / 23 kg are present ([795] [1267]).
- **FP-FR-4:** anchors kept (9 spans).
- **FP-FR-5:** Kelly/Hal on « tu ». This judgment call is applied provisionally and stays for Lisa.
- **FP-FR-6:** the excerpt from the published edition is present (50/50 paragraphs).
- No ruling was undone.

## Decisions added (PROOFCHECK_DECISIONS.md)
- **PC-FR3-1:** the closing CTA "Start reading The Binder's Bequest today!" is missing. It is an omission and was not logged by the first pass. Suggested text: « Commencez la lecture de <bt>The Binder's Bequest</bt> dès aujourd'hui ! »
- **PC-FR3-2:** follow-up for the Inn Trouble FR excerpt. [1426] « boîte à pâtisserie » should be aligned to the new FP wording.
- **PC-FR3-3:** FP-FR-2 status. Currency idioms come under PC-FR2-1.

## Refusals
- None. One edit first missed on NBSP spacing; it was re-matched exactly and applied.

## Checks after fixing
- looks_english: [].
- bt_anchors check: 9 spans, 0 unpaired (Flour Play / Frost and Found / Inn Trouble / The Binder's Bequest).
- check_matter --file: 1 PASS 0 FAIL.
- preflight --verify: "source or corrected copy missing", because the raw file lives in `_superseded/`. A manual comparison against the backup was run instead:
  - 2226 → 2226 paragraphs.
  - Italic runs 45 → 45, identical and in order.
  - `<bt>` spans 9 → 9, identical.
  - Scene breaks 60 → 60.
  - Only the 20 listed paragraphs changed.
- proofcheck.py re-run: A0 B0 C0 D0 E3 F1 G0 H16 I0 J0. No change is expected, because every remaining flag is a false positive or the known FP-FR-1.

## Verdict
**MINOR.**
- The clue chain is intact. Walk-in/cold room survives, sour base is one rendering, the lock and key are right, and no confrontation reversal was found.
- The misses are local mistranslations, term drift (bakery ≠ pâtisserie, porch), one clue-wording mismatch (two degrees) and grammar.
- The one omission is the back-matter CTA line, which was logged as a decision.
- **Rate:** 20 real defects fixed, plus 1 omission logged, over 16 units read (front matter + 14 chapters + back matter), about 1.3 per chapter.
