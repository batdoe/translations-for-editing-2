# Brief: Frost Falls translation proofread, Books 2 + 3 (run of 2026-10-26)

You proofread ONE edition. Follow the agent task in `C:\Users\User\.claude\commands\proofread.md`
("The agent's task", steps 1–8) **exactly**, with the overrides and additions below. Where this brief and
proofread.md disagree, this brief wins.

⚑ Do NOT use the Agent/Task tool. Read the chapters yourself, sequentially, with python-docx.

## Paths
- **Translation (your input):** `C:\Users\User\Scripts\translated\<stem>.docx`
- **English source (NOT in translate\ — use these):**
  - Inn Trouble → `C:\Users\User\Scripts\translate_now\Inn Trouble - ASSEMBLED - FORMATTED.docx`
  - Flour Play → `C:\Users\User\Scripts\translate_now\Flour Play - ASSEMBLED - FORMATTED.docx`
- **Output:** `C:\Users\User\Scripts\translated\corrected\<stem>.docx` (copy the input there first, edit the copy)
- **Ledgers:** `C:\Users\User\Scripts\translated\_EditLedgers\` — `<stem>_PROOFREAD.md`, `<stem>_APPLIED.md`,
  and APPEND to `PROOFREAD_DECISIONS.md` under a heading `## <stem> (2026-10-26)`. Re-read that file
  immediately before writing and change only your own section.
- **Language dossier:** `C:\Users\User\OneDrive\Documents\Claude\Projects\Multi-Book Translations\_kit\dossiers\<lang>.txt`
  (french, spanish, italian, german, dutch, norwegian, polish, romanian, czech, greek, filipino, swedish,
  brptg for Brazilian Portuguese, **turkish_cozy** for Turkish). Read it before you start.

## Prior work on Inn Trouble FR / NO / DE / ES / NL / IT
These six inputs were ALREADY proofread once today by a web session (154–420 fixes each). Their reports are
`_EditLedgers\<stem>_PROOFREAD_web-20261026.md` and `_APPLIED_web-20261026.md`; their decisions are in
`_EditLedgers\PROOFREAD_DECISIONS_web-20261026.md`. Treat them as hints (proofread.md step 2a). Do NOT undo
their fixes unless a fix is itself wrong against the English. That session did NOT have the rulings below
or the helper scripts — your job is the full bilingual read again PLUS everything it missed.

## Lisa's Frost Falls rulings (already given 2026-10-13 — apply them, don't escalate them)
Read rulings 1–7 in `_EditLedgers\FF_DECISIONS_BRIEF_20261013.md` and apply them to this edition:
1. **Dialogue punctuation: one system per language, internally consistent**, per the dossier (FR « » with
   NBSP; IT caporali «»; DE »…«; ES raya; every other language: the dossier's system). Rebuild attributions
   properly, don't just swap marks.
2. **Formal/informal "you"** per the address table in that brief (circle women, Nick, Bram = informal;
   new acquaintances formal; Noriko formal until the English puts them on first names). Log the table you used.
3. **English sign/label text gets translated** (keep italics).
4. "Fifty miles": leave as is.
5. **Stray `<bt>` markers — this OVERRIDES proofread.md step 2b.** Only three things are book titles here:
   **Frost and Found, Inn Trouble, Flour Play** (front matter, back matter, sell lines). Keep those markers
   exactly. Everything else inside `<bt>` is NOT a title — e.g. The Holly Jolly Bakery, Gazette, Winter
   Wonderland Inn, Yarn Tales, "Frost Falls", "the sapphire at its heart", numbers, signs. For each:
   remove the markers, and make the text read as this edition renders it elsewhere (shop/paper names: match
   the edition's own consistent form; ordinary phrases: translate). ⚑ **"the sapphire at its heart"** is
   Theo's catalogue-card wording that the blackmail note quotes back — the clue only works if BOTH places
   use the SAME target-language words. Translate it once and use it identically everywhere it appears.
6. **Cider is non-alcoholic** (served to children): no Apfelwein/cidre/sidro-style alcoholic word.
7. Straightforward consistency fixes (term variants, surname plurals, copyright line wording): fix them.
   Leave chapter headings / TOC / front-matter order / Heading styles to the formatter — just note them.

## Helper checks — run ALL of these on your corrected copy before you return
1. Untranslated English: `python -c "import sys; sys.path.insert(0,r'C:\Users\User\Scripts'); from claude_translate import paras, looks_english; P=paras(sys.argv[1]); print([p[:90] for p in P if looks_english(p)])" "<corrected file>"`
   → must be empty except genuine proper names / title anchors. Judge the language, not the ratio.
2. `python C:\Users\User\Scripts\bt_anchors.py check "<corrected file>"` → 0 unpaired, and the ONLY span
   texts left are Frost and Found / Inn Trouble / Flour Play.
3. `python C:\Users\User\Scripts\check_matter.py --file "<corrected file>"` → report the result. A missing
   series page / TOC is the FORMATTER's job: note it, don't build it.
4. `python C:\Users\User\Scripts\translated\_tools\preflight.py --verify "<stem>"` → paragraph count
   unchanged; italic runs unchanged except where you translated italic text (say where).

## Return (compact)
Edition · findings · applied · decisions · refusals · the four check results (one line each) · stray `<bt>`
removed (count) · dialogue paragraphs converted (count) · worst defect in one line.

## Lessons from the editions already done this run (FR, NO, DE) — check every one
- **The blackmail NOTE vs the 1924 Blackburn LETTERS.** Two editions used the same word for both (NO "brevene",
  DE "Briefe"), which REVERSED the Ch19/Ch22/Ch26 deduction. Give the note its own word ("note/slip" sense) and
  reserve the "letters" word for the 1924 letters. Check Ch19 [~582], Ch22, Ch26 explicitly against the English.
- **The clue phrase** "the sapphire at its heart": identical wording (article included) in the note, Jessica's
  readings, Theo's catalogue card, the Ch23 recap and the confrontation. Make any "five words" claim match the
  target phrase's real word count.
- **Spelled-out units hide from the pre-flight count** (NO had 7 "tomme" with a reported 0). Read for them.
  Body-part words (DE "Fuß") are false positives.
- **Currency:** dollars/cents only — no krone/øre/euro idioms (NO had 7).
- **Snowball** (the dog): use ONE form throughout, matching the same language's Book 1 (e.g. Book 1 Dutch uses
  "Sneeuwbal"). If Book 1 and this book differ, unify to Book 1 and log it as a decision.
- **The knitting circle's name:** check the same language's Book 1 (`translated\corrected\Frost and Found -
  ASSEMBLED - FORMATTED_<Lang>.docx` if present). If they differ, unify to Book 1 and log it as a decision.
- **Reversed meanings found so far:** the blurb making Sam the debtor (he is OWED the twenty dollars); the
  excerpt's "Very nearly" rendered as "absolutely". Check both.
- **Title page** may say "Chapter 1" instead of the book title, or be left in English — fix to match Book 1.
- **Reindeer names** (Comet, Dancer…): match the same language's Book 1 (Italian Book 1 keeps the English names).
- **Narrative tense is LOCKED per the dossier** (FR passé composé + imparfait; IT passato remoto + imperfetto; etc.) —
  check every chapter uses the same narrative tense.
- **Term variants already unified in other languages** — check yours for the same drift: town = small town/village
  (never "city"), festival (never a generic "party/fiesta"), the green = the park, porch = Book 1's word.

## FLOUR PLAY (Book 3) editions — read this too
- English: `C:\Users\User\Scripts\translate_now\Flour Play - ASSEMBLED - FORMATTED.docx` (Lisa's Oct 19 "no poison"
  version). These are RAW machine translations (no prior proofread). Expect the Filipino-level defect rate in places:
  code-switched English, systematic mistranslations of craft words (mittens/knit/coat), cider, address drift.
- The Inn Trouble clue/note lessons are Book-2 plot. For Book 3, apply the same IDEA to its own clue chain: every
  term the deduction rests on must be rendered the SAME way each time it appears and must say exactly what the English
  says — the flour, the sour base / acidulant, the "ten times" a rye dose, the old gate key, the order book, Greta's
  nose ("nothing I can name"). ⚑ This is the **no-poison** edition: if the translation says poison/poisoned/toxic
  where the English does not, that is a mistranslation — fix it to what the English says.
- Series consistency sources, in order: this language's Inn Trouble in `translated\corrected\` (done this run for
  FR NO DE ES NL IT Filipino), then its Frost and Found (`translated\corrected\` else `translated\`). Names, the
  circle, Snowball, Pip (she/her), reindeer, address table, the green/square/town words. Unify to them; log real
  conflicts as decisions.
- The Bk1+Bk2 "Books in this series" / sell lines name Frost and Found, Inn Trouble, Flour Play — those `<bt>`
  anchors stay; everything else in `<bt>` is ruling 5.
- **Flour Play's back matter excerpts _The Binder's Bequest_** (a real Lisa Bouchard book) — its `<bt>` anchors are
  REAL titles: keep them. If the excerpt or sell lines are left in English, translate them; if a published edition of
  The Binder's Bequest exists in this language (check `C:\Users\User\Scripts\2buploaded\` and `proofread\`), copy the
  excerpt text from it rather than re-translating, and log that you did.
- **Lessons from Flour Play French:** "sour base" had six renderings (unify to ONE); "walk-in" vs Joyce's giveaway
  word "cold room" must stay two DIFFERENT words or the Ch22/23 slip disappears; "two degrees below" is a Fahrenheit
  clue figure repeated at three places — keep it identical in all three and log it as a decision rather than converting;
  pounds of flour: accurate metric (100 lb → 45 kg) per the units rule, logged. Check for literal `M<sup>me</sup>`-style
  markup and English sentences mid-chapter (FR had two in Ch25). Title page may read "Chapter 3".
- **Lessons from Flour Play NO:** the machine translator sometimes printed its OWN NOTES into the prose ("Let's use …
  to preserve the source's …", "Correction: …") — search for them and delete. It also left an English duplicate of a
  paragraph next to its translation — empty the English one ONLY after confirming the translated twin is complete.
  "A hundred feet" in the snow means FOOTPRINTS, not distance. "Grange" hall needs one consistent rendering.
- **Lessons from Flour Play PL/Filipino:** gendered languages get Pip WRONG (Polish had Pip male ×11) and can
  masculinise the narrator (Jessica) — check every gendered form. Words from OTHER languages leak in (Portuguese,
  German, Vietnamese, Czech) — read for them. Numbers drift (Joyce 65, partnership 25 yrs ago / 15 together, "the
  twentieth"). Graffiti DIRTY must not become a vulgarity. Prices in local currency → dollars.
  The final English line "Start reading The Binder's Bequest today!" was DROPPED by the translator in NL and PL —
  check whether it exists; if missing, log it as a decision with your suggested translation (do not add paragraphs).
