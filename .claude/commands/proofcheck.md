You are running **PROOFCHECK** — the second-pass audit of Lisa's finished translation proofreads.
**Scope: Frost Falls Book 2 _Inn Trouble_ and Book 3 _Flour Play_ ONLY, all 14 languages.** Anything else →
stop and say this command doesn't cover it.

The first pass (`/proofread`) already read every edition against the English and wrote
`translated\corrected\<stem>.docx`. Your job is to find what it **missed**, what it **got wrong**, and what
it **broke** — not to redo it. You are the ORCHESTRATOR: run the free script, then one sub-agent per edition,
strictly sequential, foreground.

⚑ **NO API KEY. EVER.** Same rule as /proofread: the proofreader is you and your sub-agents. Never call
`claude_translate.py proofread/apply`, never import `anthropic`.
⚑ **Sub-agents: one per edition, FOREGROUND (`run_in_background: false`), one at a time.** No Workflow tool.
⚑ **Sub-agents must NOT spawn sub-agents.** Tell every one: *"Do NOT use the Agent/Task tool. Read the
chapters yourself, sequentially, with python-docx."*
⚑ Questions for Lisa = plain text / the decisions file. **Never a popup.**
⚑ Do NOT promote, format or publish. Lisa does that locally.

## PATHS (Windows → cloud repo: see CLAUDE.md's table; `C:\Users\User\Scripts\` = repo root)
- English: `translate_now\Inn Trouble - ASSEMBLED - FORMATTED.docx`, `translate_now\Flour Play - ASSEMBLED - FORMATTED.docx`
- Edition under audit: `translated\corrected\<stem>.docx` (stem = `<Book> - ASSEMBLED - FORMATTED_<Language>`)
- Raw input the first pass started from (READ-ONLY, for diffing): Inn Trouble → `translated\<stem>.docx`;
  Flour Play → `_superseded\<stem>.docx` (same paragraph grid as corrected — verified 2026-10-27).
- First-pass ledgers: `translated\_EditLedgers\<stem>_PROOFREAD.md`, `<stem>_APPLIED.md`; decisions in
  `PROOFREAD_DECISIONS.md` (local run) or `PROOFREAD_DECISIONS2.md` (Inn Trouble PL RO CS SV TR EL PT-BR, cloud run).
- Run rules: `translated\_EditLedgers\FF_PROOFREAD_BRIEF_20261026.md` (all "Lessons" bullets) and Lisa's rulings
  `translated\_EditLedgers\FF_DECISIONS_BRIEF_20261013.md`. The audit holds the edition to these, too.
- Dossiers: `_kit\dossiers\<lang>.txt` (brptg = Brazilian Portuguese, turkish_cozy = Turkish).
- **Outputs (this command):**
  - `translated\_EditLedgers\<stem>_PROOFCHECK_FLAGS.md` — written by the script
  - `translated\_EditLedgers\<stem>_PROOFCHECK.md` — the agent's audit report
  - `translated\_EditLedgers\PROOFCHECK_DECISIONS.md` — new questions for Lisa (APPEND, own section only)
  - `translated\_EditLedgers\PROOFCHECK_QUEUE.md` — LIVE STATUS on top (OVERWRITE), one row per edition done
  - backups before any write: `translated\_EditLedgers\_proofcheck_backups\<stem>.<timestamp>.docx`

## STEP 0 — PARSE THE ARGUMENTS AND STATE THE PLAN
`$ARGUMENTS` may be:
- empty or `all` → both books, every language that has a `corrected\` copy (28 editions)
- `Inn Trouble` or `Flour Play` → that book, all languages
- a book plus languages: `Inn Trouble Polish,Greek`
- a quoted full stem → exactly that one
- add `full` anywhere → **FULL mode** (agent re-reads every chapter bilingually, not just the targeted set — ~2× the tokens)
- add `--force` → redo editions that already have a `_PROOFCHECK.md`

**Skip** any edition that already has `<stem>_PROOFCHECK.md` unless `--force` (resume property).
**Order:** Inn Trouble before Flour Play; within a book, the editions with the most script flags in sections
A–G and J first (those are the likeliest real misses).
State in plain text before spawning: how many editions, which, mode, where outputs land.

## STEP 1 — RUN THE SCRIPT (free, no model)
```
export SCRIPTS_ROOT="$(pwd)"            # cloud only
python translated\_tools\proofcheck.py --book "<Book>" [--langs L1,L2]      # or --all
```
One summary line per edition (`A=.. B=.. … J=..`) and a `_PROOFCHECK_FLAGS.md` each. Sections:
A English left · B other alphabets/foreign letters · C MT debris · D MT loops · E chapter length + heading
oddities · F numbers not in the English chapter · G names missing from a chapter · H watch-words (units,
currency, cider, poison) · I dialogue system · J **the first pass's own deletions/cuts** · K the book's clue
chain (English side, per chapter) · L the four standard checks · M first-pass change density per chapter.
Every flag is a HINT. Do not read the flag files into your own context beyond the summary line.

## STEP 2 — ONE AUDIT AGENT PER EDITION (sequential, foreground)
Give each agent this brief (fill in the stem, language, dossier, decisions file and mode):

### The audit agent's task
**Read first:** this command file's "audit agent" section, the run brief + Lisa's rulings (above), the dossier,
the edition's `_APPLIED.md` (to learn the settled terms: the note/letters words, the clue wording, the address
table, Snowball, the circle, dialogue system), its section of the decisions file, and its `_PROOFCHECK_FLAGS.md`.

Do NOT use the Agent/Task tool. Read the chapters yourself, sequentially, with python-docx. Never paste a whole
manuscript into context; read EN + target chapter by chapter.

**1. Judge every flag** in sections A–J against the English. Each one: REAL (fix or decision) or FALSE POSITIVE
(one-word reason). Section E heading oddities and missing chapters: confirm whether body text is missing
(omission = fix if the English is right there and the gap is a sentence or two; a missing chapter/scene =
decision) or only the heading line (formatter → decision, never renumber). Section J: every paragraph the
first pass emptied or cut — confirm the English really has no such text there (a deleted English twin is fine
only if its translated twin is complete).

**2. Audit the first pass's own edits.** Diff raw vs corrected (paragraph-by-paragraph, same grid). Read every
changed paragraph next to its English. Hunt for **regressions**: meaning changed away from the English, a fix
applied to the wrong paragraph, broken grammar/agreement/declension from a substitution (book-wide
`replace` of a term inside an inflected word), lost italics, a <bt> title anchor removed, dialogue punctuation
mangled, a "consistency" change that hit a place where the English really differs. Also take **20 random
entries from `_APPLIED.md`** and confirm each "now" text is actually in the file.

**3. Trace the clue chain end to end** (section K gives the English chapters). For every term, list each target
occurrence and confirm it uses the settled wording and says what the English says.
- **Inn Trouble:** "the sapphire at its heart" — IDENTICAL wording (article and case included) in the note,
  Jessica's readings, Theo's catalogue card, the Ch22 recap and the Ch26 confrontation, and every "five
  words" line matches the real word count of the target phrase · the blackmail **note(s)** have their own word
  everywhere and NEVER share the 1924 **letters'** word (nor Theo's index **cards'**) — check Ch19, Ch22,
  Ch25 evidence list, Ch26 explicitly · Sam is **owed** the twenty dollars (blurb + text) · cider non-alcoholic ·
  Snowball / circle / reindeer / the green / porch = the edition's settled forms · the excerpt (Flour Play Ch1)
  matches the same language's corrected Flour Play, "Very nearly" not "absolutely".
- **Flour Play:** "sour base" ONE rendering, never sourdough starter/yeast · acidulant · **walk-in vs cold
  room stay two DIFFERENT words** — Joyce's "cold room" slip (Ch22–24) must survive · "ten times" the rye
  dose · the old gate key · the order book · Greta's "nothing I can name" · "two degrees below" identical at all
  three places · **no poison/toxic** where the English has none · Pip she/her, Jessica never masculine, Joyce's
  gender · Joyce 65, partnership 25 years ago / 15 together, "the twentieth" · DIRTY graffiti not a vulgarity ·
  Grange one rendering · dollars only · *The Binder's Bequest* anchors kept; closing "Start reading The
  Binder's Bequest today!" present or already logged.

**4. Fresh bilingual read where the first pass looked least.**
- **Targeted mode (default):** read fully, EN vs target, sentence by sentence: (a) the **3 chapters with the
  lowest change density** (section M) — untouched text is where misses hide; (b) the **plot-critical chapters**
  — Inn Trouble Ch2, Ch19, Ch22, Ch25, Ch26; Flour Play: the chapters section K shows for walk-in/cold room,
  sour base and the confrontation; (c) front matter + blurb + all back matter.
- **FULL mode:** every chapter.
Hunt the /proofread defect classes in order: untranslated English, omissions, mistranslation/reversed meaning
(negation, comparatives, who-did-what-to-whom), names/gender/declension, register/address vs the table,
term drift, tense drift vs the dossier, missing scene breaks, units/currency.

**5. Re-check the open decisions.** For each of this edition's items in the decisions file: is the quote still
accurate against the current text? Did the first pass apply something that was a judgment call (chapter
renumbering, round-number units, a series-name change against Book 1)? Report; don't undo a ruling Lisa gave.

**6. Apply only one-answer fixes**, exactly as /proofread step 5: back up first; match the paragraph's complete
current text (near-match = refusal, logged); edit only `<w:t>` nodes, never `set_para_text()`; keep italics
(rebuild runs, clone `<w:rPr>`); keep `<bt>` title anchors; paragraph count must not change; change nothing
the audit didn't find. Judgment calls → `PROOFCHECK_DECISIONS.md` under `## <stem> — PROOFCHECK (<date>)`
(create the file with a `# PROOFCHECK DECISIONS` header if missing; re-read it right before writing; each item:
verbatim target quote, English, options, your recommendation, why it can't be settled automatically).

**7. Re-run the four checks** (looks_english, `bt_anchors.py check`, `check_matter.py --file`,
`preflight.py --verify "<stem>"`) and re-run `proofcheck.py --book "<Book>" --langs <Lang>`; the flag counts
for anything you fixed should drop.

**8. Write `<stem>_PROOFCHECK.md`:**
- header: mode, chapters read in full, flags judged (real / false positive per section)
- **Missed by the first pass** — each: para #, chapter, verbatim target quote, English, class, fix (applied?)
- **Regressions introduced by the first pass** — same format
- **Ledger mismatches** — APPLIED.md claims not found in the file
- decisions added, refusals
- **Verdict:** `CLEAN` (nothing material missed) · `MINOR` (fixed here, no plot/omission defects) ·
  `SIGNIFICANT` (a plot-chain, omission or reversed-meaning defect was missed → recommend `full` mode for
  this edition) — plus the rate: real defects found per chapter read.

**9. Return (compact, ≤ 20 lines):** edition · mode · chapters read · flags real/false · missed found ·
regressions found · applied · decisions · refusals · four checks (one line each) · verdict · worst miss in one
line · and one queue row:
`| <Book>_<Lang> | <mode> | <missed> | <regressions> | <applied> | <decisions> | <verdict> | <worst miss> |`

### After each agent returns
1. `preflight.py --verify "<stem>"` yourself: paragraph count unchanged.
2. Update `PROOFCHECK_QUEUE.md`: LIVE STATUS block on top (total, done, remaining, next — OVERWRITE), the
   agent's row appended to the table below it.
3. **Cloud:** `git add -A && git commit -m "Proofcheck <stem>: <verdict>" && git push` — a killed session loses at
   most one edition.
4. Hard blocker (unreadable file, no English) → log it, one line to Lisa, carry on to the next edition.
5. Next agent. Don't stop for approval between editions.

## STEP 3 — WRAP
Plain-text report to Lisa, outcome first: editions audited, verdict counts (CLEAN / MINOR / SIGNIFICANT),
total missed defects and regressions found and fixed, new decisions (in `PROOFCHECK_DECISIONS.md`), any
edition recommended for a `full` re-run, and — if the run died — which edition it died on. Never present a
partial run as finished.

## WHAT THIS COMMAND IS NOT
- Not a re-proofread: don't re-do fixes that are right, don't re-word correct prose, don't re-litigate settled
  term choices unless they are wrong against the English or Lisa's rulings.
- Not prose polishing, not de-AI, not formatting (headings, TOC, Heading 1 styles = formatter; just note them).
