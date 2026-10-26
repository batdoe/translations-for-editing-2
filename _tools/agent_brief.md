# PROOFREAD sub-agent brief — Inn Trouble (Frost Falls Book 2)

You are proofreading ONE translated edition against its English source, for Lisa Bouchard (the author).
This is the translation-certification pass from `proofread.md` (repo root — read its STEP 1 section if
anything below is unclear; this brief adapts its Windows paths to this repo).

## Hard rules
- **Do NOT use the Agent/Task tool. Do NOT spawn sub-agents. Read the chapters yourself, sequentially, with python-docx.**
- No Anthropic API / SDK calls. You are the proofreader.
- Never touch the original `<stem>.docx` in the repo root. Edit ONLY `corrected/<stem>.docx` (the working copy,
  already created by the mechanical sweep). `corrected/_baseline/` is the comparison snapshot — never edit it.
- Do not git commit or push; the orchestrator does that.
- Do not paste whole chapters into your final answer. Your returned summary is short (see end).
- Scratch scripts go in `/tmp/claude-0/-home-user-translations-for-editing-2/beaf4105-b370-54bf-9d9a-8abcff11ec46/scratchpad/`, not the repo.
- This is NOT prose improvement and NOT a re-translation. The only question: does this faithfully say what the
  English says, in fluent target-language prose? If an edition is broken beyond sentence-level fixing, say so and stop.

## Paths (repo root = /home/user/translations-for-editing-2)
- Translation (original, read-only): `<stem>.docx`
- Working copy you edit: `corrected/<stem>.docx`
- English source: `_source/Inn Trouble - ASSEMBLED - FORMATTED.docx`
- Ledgers: `_EditLedgers/<stem>_PROOFREAD.md`, `_EditLedgers/<stem>_APPLIED.md`,
  `_EditLedgers/PROOFREAD_DECISIONS.md` (APPEND only — create with a `# PROOFREAD DECISIONS` header if missing)

## Tools (already written, use them)
- `python3 _tools/pair.py "<stem>" --map | --front | --ch N | --back` — prints English and translation side by side
  with paragraph indices (indices are the real `doc.paragraphs` indices of the working copy). Chapters 1–31.
  `--back` shows the translation from its chapter 31 to the end; match its tail against the English back matter
  (What's Next?, Excerpt from Flour Play).
- `_tools/apply_fix.py` — `Fixer(stem).fix(idx, expected_full_text, old, new, why)` then `.save()`.
  It edits only the `<w:t>` text of the affected run(s), keeps every other run (italics!) intact, and REFUSES on
  any mismatch. A refusal is logged, never forced. If `old` crosses differently-formatted runs, split it into one
  fix per run. Call `.save()` once at the end (or in batches) — and re-open a new Fixer after saving.
- `python3 _tools/preflight.py --verify "<stem>"` — run after writing. Compares paragraphs, scene breaks,
  `<bt>` span count, italic runs (content AND order) against the baseline. Paragraph count, scene breaks and bt
  count MUST stay equal. Italic-run differences are allowed only when you deliberately fixed text inside an
  italic run — list each one in the APPLIED log.

## Known facts about this book (from the orchestrator's pre-flight)
- English has 31 chapters + front matter (title, series, book number, author, copyright, Books in This Series,
  Table of Contents, About this Book) + back matter (What's Next?, Excerpt from Flour Play).
- English has NO `* * *` scene-break markers anywhere. Translations contain 3–5 such lines. For each, check what
  is at that position in the English (e.g. a blank line/scene shift, the excerpt, nothing). Report them; do NOT
  delete them (it changes paragraph count) — put them in one decision item with your recommendation.
- Every translation has 0 Heading 1 paragraphs (English: 35). That's a FORMATTER defect: mention it once in the
  report header, don't fix it.
- `<bt>…</bt>` marks a book title for a later stamping step. **It is NOT corruption.** Never delete the markers,
  never translate the text inside, never report them as a defect. Keep span count identical.
- Book titles (`Inn Trouble`, `Frost and Found`, `Flour Play`), whether in `<bt>` or bare: do NOT translate or
  change them. If the edition's handling looks inconsistent (e.g. title page shows a translated title, or a chapter
  label instead of the title), report it as ONE decision item with a recommendation.
- Place names / proper nouns in the English (Frost Falls, Winter Wonderland Inn, Evergreen Avenue, Ridgeline,
  Blackburn, character names, Pip, Snowball) stay as in English unless the translation consistently localises
  one; flag inconsistency.
- Italic runs: the English has ~15 italic runs (the blackmail notes, document labels, "do not lose", a
  plaque inscription, "Flour Play is coming soon" lines, one thought line). The mechanical sweep converted the
  translator's Markdown `*x*` into real italics. Where the translation italicises something the English does
  NOT (translator-added emphasis), report it, but do not remove it — collect those into ONE decision item.
  Where the English italicises something the translation does not, report it (restoring the italic is a decision
  item too, since it's a formatting change, not text).
- Some English paragraphs contain two lines of dialogue merged into one paragraph (a source formatting quirk).
  Not a translation defect; ignore unless the translation drops one of the lines.
- Imperial units in the English that are LITERAL measurements (convert these if the translation kept them):
  para 66 "four inches" (of snow); 108 "about an inch from a glass pear"; 149 "the richest for fifty miles";
  253 "a final quarter-inch"; 456 "six feet away"; 694 "a few yards off"; 898 "an inch of water";
  936 "a good clean six inches" (snow); 973 "Six inches of clean overnight" (snow).
  Everything else with feet/inch/mile/ounce in the English is idiom ("at my feet", "inch by inch", "every ounce",
  "set foot", "not the miles"): an idiomatic target-language equivalent is correct; a literal imperial unit
  rendered as such in an idiom is fine ONLY if it reads natively — otherwise flag it.
  Unit rule (apply it, state which rule fired per finding):
  - SAFE to apply: arithmetic conversion of an exact/literal number, rounded the way a native writer would
    (four inches → 10 cm; six feet → about two metres; an inch → 2–3 cm; six inches → 15 cm).
  - ESCALATE: round/rhetorical figures where conversion loses roundness or changes emphasis
    ("fifty miles" → 80 km), or anything you can't settle arithmetically.
- There is NO prior proofread report for this edition. Write `Prior report: none` at the top of yours.

## What to do
1. Read the English and the translation IN FULL: front matter, all 31 chapters, back matter. Use `pair.py`
   chapter by chapter. Every chapter must be covered — state coverage (e.g. 31/31) in your report.
2. Hunt these defect classes, most serious first:
   1. UNTRANSLATED ENGLISH (any passage left in English — front matter included). Judge the actual language,
      not word overlap (Dutch/German/Norwegian share words with English).
   2. OMISSIONS — source sentences/content missing.
   3. MISTRANSLATIONS / reversed meaning (negation, passive, comparatives, false friends).
   4. PROPER NAMES — untranslated/wrongly declined; pronoun & gender agreement.
   5. REGISTER/formality drift (tu/vous, du/Sie, etc. inconsistent for the same pair of characters); wrong or
      over-literal idiom.
   6. TERM INCONSISTENCY across the book (same in-world noun two ways: the Historical Society, the archive,
      the brooch, the festival, the circle…); tense drift; typos.
   7. Scene-break markers vs English (see above).
   8. UNITS AND MEASUREMENTS (see above).
   Also: chapter heading numbering. **Chapter renumbering is ALWAYS a decision for Lisa** — never fix a chapter
   number yourself, even an obvious one.
3. Write `_EditLedgers/<stem>_PROOFREAD.md`. Header: edition, English source, `Prior report: none`, coverage,
   counts. Each finding: number, class, para index, the **target-language quote VERBATIM** (never translated),
   a short **English** explanation, the **corrected target-language phrasing**, and status
   (APPLIED / DECISION / REFUSED). If nothing is wrong, write exactly `NO FINDINGS`.
4. APPLY every fix that has exactly ONE correct answer (fact restoration: mistranslated word, wrong declension,
   typo, untranslated run whose English is right there, an omitted sentence restored by translating the English
   sentence into the existing paragraph, a SAFE unit conversion). Use `apply_fix.Fixer`. Change nothing the
   report did not ask for. No voice tuning, no smoothing.
5. Do NOT guess judgment calls — append each to `PROOFREAD_DECISIONS.md` under a `## <stem>` heading
   (create the heading once; add items under it): quote, options, your recommendation, and why it can't be
   settled automatically. Judgment calls include: ambiguous word choice, round-number units, chapter
   renumbering, title-localisation questions, scene-break markers, italic additions/removals, anything that
   would add or remove whole paragraphs, and any ADAPTATION that changes what the text literally states to make
   it work in the target language (e.g. changing a stated word count, letter-based wordplay, renaming labels to
   keep an alphabetical detail). Those go to decisions with your proposed wording — do not apply them.
6. Run `python3 _tools/preflight.py --verify "<stem>"`. Paragraphs / scene breaks / bt must PASS. Explain every
   italic difference. If something you didn't intend changed, fix it.
7. Write `_EditLedgers/<stem>_APPLIED.md`: verify result, then a table of applied fixes (para #, was → now,
   why), decisions logged, refusals (and why), and anything quoted that couldn't be found.
8. Return a compact summary ONLY: edition, coverage, findings count, applied count, decisions count,
   refusals count, verify result, and the one-line worst defect.
