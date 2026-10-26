---
description: Sequential whole-folder TRANSLATION PROOFREAD loop — the pass that certifies a translated edition as sellable. Walks the queue of un-proofread translated editions in `C:\Users\User\Scripts\translated\`, and for EACH ONE spawns a sub-agent that reads the English source alongside the translation, reports every concrete defect (untranslated English, omissions, mistranslations, reversed meaning, wrong proper-name declension, register drift, term inconsistency, missing scene breaks), APPLIES every fix that has exactly one safe answer, and STOPS for Lisa's ruling on anything needing a judgment call. Runs on Claude Code — no API key, no Anthropic SDK, no per-token API bill. Checkpoints to disk PER EDITION so a killed run resumes at the next un-proofread book instead of restarting the corpus. Writes a report + an apply-log + a decisions ledger to `translated\_EditLedgers\`, then hands off to `promote_translations.py promote`, which moves certified editions into `2buploaded\`. ⚑ This REPLACES the API-based `claude_translate.py proofread` + `apply` commands — Lisa has no Anthropic API key and does not want one. NOT prose editing (/janet), NOT de-AI (/sixtell) — it hunts TRANSLATION defects against an English source.
argument-hint: [count | "all" | <edition stem>] — e.g. /proofread 5  ·  /proofread all  ·  /proofread "NEW Secret Betrayal - ASSEMBLED - FORMATTED_Norwegian"
model: opus
---

You are running **PROOFREAD** — Lisa's translation-certification loop. You are the ORCHESTRATOR: you walk the
queue of un-proofread translated editions and spawn **one sub-agent per edition, strictly sequentially**, each
agent reading the English source + the translation, applying the safe fixes, and logging the rest.

⚑ **NO API KEY. EVER.** Lisa pays for Claude Code / Cowork / the app and is **not** buying an Anthropic API key.
The model doing the proofreading is **you and your sub-agents** — Claude Code. Do **NOT** call
`claude_translate.py proofread`, do **NOT** call `claude_translate.py apply`, do **NOT** import the `anthropic`
SDK, do **NOT** suggest setting `ANTHROPIC_API_KEY`. Those commands exist in that script for historical reasons
and are dead to this workflow. If you catch yourself reaching for one, stop — you are doing it wrong.

⚑ **Sub-agents ARE used**, one per edition, **FOREGROUND and BLOCKING** (`run_in_background: false`), one at a
time, never detached — the same harness shape as `/fastbrad`. Do NOT use the Workflow tool. Do NOT set
`run_in_background: true`. Sequential blocking Agent calls only, so nothing dies on a reload mid-write.

Any question to Lisa = **plain text in chat, NEVER a popup** (memory `no-popup-questions-use-text`).

## THE PINNED PATHS
- **Translations (the queue):** `C:\Users\User\Scripts\translated\` — `<book>_<Language>.docx` and
  `<book>_<Language> - FORMATTED.docx` (the deliverable).
  ⚑⚑ **BUT NOT ALWAYS — CHECK `Scripts\proofread\` FIRST FOR KENNEDY BLAKE.** The live KB_H1
  editions live in `Scripts\proofread\` (the `PROMOTED_OLD` folder), and the similarly-named
  `KB_H1_*_<Language>.docx` files sitting in `translated\` are **SUPERSEDED drafts**. Proofreading
  the wrong copy wastes a whole edition's tokens — it happened once. `preflight.py` resolves this
  for you; run it before spawning anything.
- **English sources:** `C:\Users\User\Scripts\translate\` (fall back to `C:\Users\User\Scripts\`).
  ⚑ The KB_H1 masters are in the FALLBACK (`Scripts\*scrub - FORMATTED.docx`), not `translate\`.
- **Corrected output:** `C:\Users\User\Scripts\translated\corrected\<stem>.docx`
- **Ledgers (ALL of them, Lisa's call 2026-08-11):** `C:\Users\User\Scripts\translated\_EditLedgers\`
  - `<stem>_PROOFREAD.md` — the findings report
  - `<stem>_APPLIED.md` — what was changed, was→now, per paragraph
  - `PROOFREAD_DECISIONS.md` — the running list of items needing Lisa's ruling (APPEND, never overwrite)
  - `PROOFREAD_QUEUE.md` — the live queue state (LIVE STATUS block on top, OVERWRITE — memory `status-note-format`)
- **The gate:** `C:\Users\User\Scripts\promote_translations.py`
  ⚑ Since 2026-08-12 it reads the report from EITHER `translated\<stem>_proofread.md` OR
  `_EditLedgers\<stem>_PROOFREAD.md`. No more copying files by hand to satisfy the gate.
- **The structural check:** `C:\Users\User\Scripts\check_matter.py`
- **⚑ PRE-FLIGHT (run this FIRST, before any sub-agent):**
  `python translated\_tools\preflight.py --book <BOOK> --langs <L1,L2,...>`
  One line per edition: chapter sequence, Heading1 presence, paragraph alignment vs English,
  scene-break count, leftover Markdown asterisks, imperial-unit tokens, back-matter presence, and
  which artifacts already exist `[R]eport [C]orrected [A]pplied`. **This is the cheapest token in
  the pipeline** — it tells you what each edition actually needs instead of the agent discovering
  it, and it catches "this file can never be formatted" (0 Heading1) before you spend anything.
  Add `--current` to inspect `corrected\` copies rather than the untouched sources.
- **⚑ INTEGRITY CHECK (after every sub-agent write):**
  `python translated\_tools\preflight.py --verify "<stem>"` — one PASS/FAIL block comparing
  paragraphs, italic-run content AND order, and scene breaks. Replaces reading paragraph dumps.
- **⚑ MECHANICAL SWEEP (before the proofread agents):**
  `python translated\_tools\sweep_mechanical.py --book <BOOK> --langs <...> [--apply]`
  Converts leftover Markdown `*emphasis*` to real italic runs across many editions with no model
  in the loop, and reports each edition's imperial-token count so the units agent gets a worklist
  instead of discovering one. Scene-break markers are protected and the run aborts if their count
  would change.

## ⚑ THE ORDER OF OPERATIONS (added 2026-08-12 — follow it; it is the token budget)

The Book-1 run cost **1.32M sub-agent tokens for 3 editions (~442k each)**, and most of the
ORCHESTRATOR's context went on rediscovery and by-hand verification rather than on the work. Run the
phases in this order and the cheap tools absorb everything the expensive ones used to:

1. **PRE-FLIGHT** — `preflight.py --book <B> --langs <...>`. Free. Tells you what each edition needs
   and catches unfixable-by-proofreading conditions (0 Heading1) before a single token is spent.
2. **MECHANICAL SWEEP** — `sweep_mechanical.py --book <B> --langs <...> --apply`. No model. Does the
   asterisk→italics conversion for every edition at once and hands you the imperial-token counts.
   ⚑⚑ **RUN IT WITH `--apply`. A DRY RUN IS NOT ENOUGH.** (2026-08-24: the orchestrator dry-ran
   it, eyeballed the 7 Swedish spans and hand-fixed some — leaving `*innan*` in raw Markdown. The
   proofread agent, told to hunt markup leakage, then DELETED the asterisks and flattened an
   authorial emphasis.) The mechanical pass exists to make markup unambiguous BEFORE a reasoning
   model sees it. Converting `*x*` to a real italic run is what protects it from the agent.
   ⚑ A `0` from this sweep is NOT proof of clean: it matches known token spellings only. Spelled-out
   units (`fem tum`, `seksti fot`, `et halvt pund`) have survived a reported-zero TWICE.
3. **PROOFREAD AGENTS** — one per edition, sequential, foreground. This is the ONLY phase that needs
   a reasoning model: the bilingual read is irreducible.
4. **UNITS / BACK MATTER AGENTS** — only for editions pre-flight flagged, and only after Lisa has
   ruled. Feed them the pre-flight worklist rather than making them discover it.
5. **VERIFY** — `preflight.py --verify "<stem>"` after every write. One PASS/FAIL block.

**Do not paste manuscript text into the orchestrator's context.** Read by path, summarise by number.
The sub-agents' returned summaries are the interface; their reports live on disk for Lisa.

## STEP 0 — BUILD THE QUEUE AND STATE IT
1. Parse `$ARGUMENTS`:
   - a **number** (e.g. `5`) → do that many editions this run (default if bare `/proofread`: **3**)
   - `all` → walk the whole queue until done
   - a **quoted edition stem** → do exactly that one
2. **Build the queue.** Run `python promote_translations.py status` and read it. An edition BELONGS in the queue
   when it has a `- FORMATTED` deliverable but is blocked on `no proofread report` or `corrections not applied`.
   ⚑ **EXCLUDE** anything blocked as `SUPERSEDED edition` — those are dead editions (KB `The_Founder`,
   `The_Owner_Manuscript`, the bare `Out_of_His_League` drafts). Proofreading a dead edition is pure waste; six
   of them were already paid for once.
   ⚑⚑ **ROMANO: only the `NEW ` prefixed editions are live** (Lisa, 2026-08-11). `NEW Secret Betrayal` /
   `NEW Secret Revenge` / `NEW Secret Passion` are the retranslations and the ONLY Romano files to work with.
   The three bare `Secret {Betrayal,Revenge,Passion} - ASSEMBLED - FORMATTED_Italian.docx` files are the
   superseded pre-retranslation editions — never proofread, promote, or rebuild them. `promote_translations.is_dead()`
   enforces this, so they will already be excluded; do not add them back by hand. ⚑ Note `Secrets and Sacrifice`
   (Vitale Empire) also starts with "Secret" and is a LIVE book — do not catch it in this rule.
3. **Order the queue by real risk, not alphabetically.** Read `Translation_QA_<date>.xlsx` if present (or run
   `python langcheck_report.py`) and put editions with **BODY PROSE** untranslated-English runs FIRST, longest
   run first. Those are dropped narrative. Back-matter-only hits are cosmetic and go last.
4. **Skip what's already done.** An edition with BOTH `_EditLedgers\<stem>_PROOFREAD.md` and
   `corrected\<stem>.docx` is finished — do not redo it unless Lisa says `--force`. **This is the resume
   property: a killed run picks up at the first unfinished edition, never at the top.**
5. **STATE THE PLAN in plain text before spawning anything** — the queue length, which editions this run covers,
   the resolved paths, and where the ledgers land. So Lisa can catch a wrong turn before the tokens burn.

## STEP 1 — PER-EDITION LOOP (one sequential foreground sub-agent per edition)
For each queued edition, in order, spawn ONE sub-agent (`run_in_background: false`) with this job:

⚑⚑ **THE AGENT MUST NOT SPAWN SUB-AGENTS.** (2026-08-24: the Norwegian agent spawned three
parallel chapter-readers on its own initiative and cost **307k** tokens; the Swedish agent, briefed
not to, cost **150k** for the same book at the same 28/28 coverage.) Tell every proofread agent:
*"Do NOT use the Agent/Task tool. Read the chapters yourself, sequentially, with python-docx."*
Nested agents also break the token accounting — the harness bills them to this run but you cannot
see their coverage.

### The agent's task
1. **Resolve the pair.** The translation is `translated\<stem>.docx`. Find its English source by stripping the
   `_<Language>` suffix and looking in `translate\` then `Scripts\`. ⚑ **If no English source exists, STOP that
   edition and report it** — a monolingual read cannot catch an omission, and omissions are defect class #2.
2. **Read both, in full.** Use the docx text extractor already in `claude_translate.py` (`paras()`) via a short
   inline python call, or read the XML directly — do NOT paste whole manuscripts into chat.
2a. ⚑⚑ **IF A PRIOR `_proofread.md` EXISTS, TREAT IT AS A HINT — NEVER AS FACT** (added 2026-08-11 after the
   first live run). That run's pre-existing report had **6 of 13 findings describing text that is not in the
   file** — including all three it labelled "critical / must be corrected before this edition ships"
   (`mr. Romano` ×2, `miss Ricci`, verified absent by grep). It also asserted the edition keeps English titles,
   which the Book Catalogue disproved. Likely cause: the Romano **`NEW ` prefix retranslation** convention —
   reports written against superseded pre-retranslation text. So:
   - **Re-verify EVERY prior finding against the live file** by locating its verbatim quote. No quote, no finding.
   - ⚑ **MEASURED RATES, 2026-08-12 (KB_H1_1, all three editions).** Prior reports written by
     *gemini-3.5-flash* against the SUPERSEDED editions scored **French 11/23 = 48% not found**,
     **German 6/10 = 60%**, **Italian 14/32 = 44%**. Live-vs-superseded paragraph overlap was only
     **10% / 19% / 17%** — these are DIFFERENT TRANSLATIONS, not revisions. Expect roughly half of any
     prior report to describe text that no longer exists. Books 2–5 carry the same stale reports.
   - Compute the **not-found fraction** = (findings whose quote is absent) / (total findings).
   - **Record it at the top of your report:** `Prior report: N/M findings not found (XX%)`.
   - If that fraction is **≥ 30%**, add `⚑ PRIOR REPORT IS STALE — treated as a hint only.` to the report AND
     say so in your returned summary, so Lisa knows to distrust that report.
   - **Never** carry a prior finding forward on the report's authority alone.
2b. ⚑⚑ **PROTECTED MARKUP — `<bt>…</bt>` IS NOT CORRUPTION.** (Added 2026-08-24 after BOTH
   agents on Leaf of Faith NO+SV silently stripped every anchor; the Swedish agent reported them as
   "corrupt artifacts". Every other integrity check passed and it nearly shipped.)
   `<bt>Title</bt>` marks a book title for `bt_anchors.py stamp`, which later replaces each span with
   the catalogue's **Title (local)** and removes the markers. Stripping them without stamping leaves
   the title in ENGLISH in a translated edition and `stamp` can never find it again — invisible in
   the prose, visible in the finished book.
   - **Do NOT delete the markers. Do NOT translate the text inside them. Do NOT report them as a defect.**
   - If an edit touches a paragraph containing a span, keep `<bt>` and `</bt>` intact and adjacent to
     the same title.
   - Verify with `python bt_anchors.py check "<file>"` — the corrected copy must carry the SAME span
     count as the original.

3. **Hunt these defect classes, most serious first:**
   1. **UNTRANSLATED ENGLISH** — any passage left in English. Report every occurrence.
      ⚑ Note the corpus false-positive pattern: Dutch/German share basic vocabulary with English, so a
      *fully translated* Dutch line can look English to a word-ratio detector. Judge the actual language, not
      a ratio. A real hit is English words in an otherwise-target-language book (`"Ik: I know. Dat is niet…"`,
      `"Een match made in heaven"`).
   2. **Omissions** — source content missing from the translation.
   3. **Mistranslations / reversed meaning** — negation, passive, comparatives, false friends.
   4. **Proper names** — untranslated or wrongly declined; pronoun and gender agreement.
   5. **Register / formality drift**; wrong or over-literal idiom.
   6. **Term inconsistency across the book** (the same in-world noun rendered two ways); tense drift; typos.
   7. **Missing scene-break markers** vs the English.
   8. ⚑⚑ **UNITS AND MEASUREMENTS** — added 2026-08-11 after the first live run, where this was the single
      biggest class of real defect and was NOT on the list. A translation can be linguistically flawless and
      still leave **American units** sitting in a metric-market edition. The first run found `seksti fot`
      (sixty feet), `en fot fra hverandre` (a foot apart), and `hver tomme` (every inch) in a Norwegian book.
      **Feet, inches, miles, yards, pounds, ounces, °F, gallons** all need converting for every metric-market
      language. (Keep imperial only where the target market is imperial — there is none in the current
      15-language set.)
      **THE AUTO-APPLY RULE — apply it, do not improvise it:**
      - **SAFE to apply** when the conversion is arithmetic and the source number is exact or clearly
        literal: `60 ft` → `18 meter`, `one foot apart` → `tretti centimeter`, `every inch` → idiomatic
        metric equivalent. Round the way a native writer would (`18 meter`, not `18,29 meter`).
      - **ESCALATE to Lisa** when the English number is a **round/rhetorical figure** whose conversion
        would either lose the roundness or change the emphasis — e.g. "a hundred pounds of silk" → 45.4 kg,
        where the translator wrote `femti kilo` (50) to keep it round and *inflated the quantity 10%*.
        Lisa's ruling on that case (2026-08-11) was to correct it to the accurate figure, but the ESCALATION
        was correct: a round-number tradeoff is an authorial call, not arithmetic.
      - State which rule fired for every unit finding, so the choice is auditable.
4. **Write the report** to `_EditLedgers\<stem>_PROOFREAD.md`. Each finding: the **target-language quote
   VERBATIM** (never translated to English), a short **English** explanation so Lisa can act on it, and the
   **corrected target-language phrasing**. If nothing is wrong, write exactly `NO FINDINGS`.
5. **APPLY the safe fixes — this is the half that used to be missing.** A fix is safe when it has exactly ONE
   correct answer: a mistranslated word, a wrong name declension, a typo, an untranslated run whose English
   source is right there. That is a **fact restoration**, not a rewrite.
   - Copy `translated\<stem>.docx` → `translated\corrected\<stem>.docx` and edit **the copy**. Never touch the
     original. (If a `corrected\` copy already exists and Lisa passed `--force`, back it up first.)
   - ⚑⚑ **VERIFY BEFORE EVERY WRITE.** Match the paragraph's **complete exact current text** before replacing
     it. A near-match is a REFUSAL, not a fuzzy edit — paragraph counts drift −82..+29 between editions and
     automated alignment was once wrong by 44 paragraphs on a hand-verified case. Log every refusal.
   - ⚑⚑ **DO NOT USE `claude_translate.set_para_text()`.** (This instruction previously RECOMMENDED it —
     corrected 2026-08-12 after it silently destroyed 15 italic runs across 12 paragraphs on the KB Book-1
     French pass.) It collapses a paragraph into its FIRST RUN, so every italic/bold run in a
     mixed-formatting paragraph is lost. The damage is invisible in the text and only shows up in the
     printed book.
   - **Instead:** edit only the `<w:t>` nodes containing your target. If a replacement would merge text
     across a run boundary, rebuild the affected runs as separate runs (plain / italic / plain), cloning the
     original `<w:rPr>` onto each. A German fix (`ein`→`einen Vermögenswert`) did exactly this merge and
     dropped an authorial italic; the English italicises that word, so it was a real defect.
   - ⚑⚑ **VERIFYING ITALICS: parse, never string-count.** `xml.count("<w:i/>")` returns **0** on a written
     file because the writer emits `<w:i />` **with a space**. Compare the TEXT of every run whose `<w:rPr>`
     contains a `<w:i>` CHILD ELEMENT, and require the source and result lists to be **identical in content
     AND order** — a plain count matches even when two runs have swapped. Easiest: run
     `python translated\_tools\preflight.py --verify "<stem>"` after writing.
   - **Change nothing the report did not ask for.** No voice tuning, no smoothing, no "while I'm here."
6. **Do NOT guess a judgment call.** These are ALWAYS Lisa's ruling, never an agent's:
   - an ambiguous word choice (the HHH Greek `πρόβατα`/"sheepish" case)
   - a number/unit that cannot be derived (the KB Book 3 `miles` vs kilometres case)
   - **chapter renumbering — ALWAYS. It cascades** (HHH Romanian's duplicate `Capitolul 3`/`17`, MMM Czech's
     skipped `Kapitola 6`).
   Append each to `_EditLedgers\PROOFREAD_DECISIONS.md` with the edition, the quote, the options, and why it
   can't be settled automatically.
7. **Write the apply-log** to `_EditLedgers\<stem>_APPLIED.md`: what was applied (para #, was→now, why), what
   needs a decision, what was refused by verification, and what the report quoted but couldn't be found.
8. **Return a compact summary** (not the whole report): edition, findings count, applied count, decisions count,
   refusals count, and the one-line worst defect.

### After each agent returns — checkpoint, then continue
- **Update `_EditLedgers\PROOFREAD_QUEUE.md`** with a LIVE STATUS block on top (OVERWRITE, never append —
  memory `status-note-format`): total queue, done, remaining, and the next edition. **This is the per-edition
  disk checkpoint that makes the run resumable — write it after EVERY edition, never only at the end.**
- If the agent reported a **hard blocker** (no English source, unreadable docx), log it, tell Lisa in one line,
  and **carry on to the next edition** — one bad file must not kill the run.
- Then spawn the next agent. Do not stop for approval between editions.

## STEP 2 — WRAP THE RUN
1. **Run the structural gate:** `python check_matter.py --dir translated` — every translated edition must have
   **LOCALIZED back matter** (Lisa's house rule 2026-08-11). Report the pass/fail count.
   ⚑ Missing back matter is a **formatter** defect, not a proofreading one — do NOT try to write back matter
   into a book here. Flag it and move on.
2. **Run the gate:** `python promote_translations.py status` and report the new READY count.
3. **Promote:** show Lisa `python promote_translations.py promote --dry-run`, then — only if she says go —
   `--apply`, which copies certified editions into `C:\Users\User\Scripts\2buploaded\`.
   ⚑ **Everything in `2buploaded\` is sellable.** That is the whole contract of this pipeline. Never promote an
   edition that did not pass all four gate requirements (report + corrections applied + decisions resolved +
   localized back matter).
4. **Report honestly, in plain text.** State: editions proofread this run, total applied fixes, how many need
   Lisa's decision, how many were refused by verification, the new READY count, and what remains in the queue.
   ⚑ **If the run died partway, say which edition it died on** — never present a partial corpus as finished
   (memory `background-execution-allowed`).
5. Tell Lisa the open decisions are in `_EditLedgers\PROOFREAD_DECISIONS.md`, and that resolving one is
   `python promote_translations.py resolve "<stem>" --note "what you decided"`.

## WHAT THIS COMMAND IS NOT
- **NOT `/janet`** — no developmental edit, no continuity audit, no Definition-of-Done. This pass measures the
  translation against its English source, nothing else.
- **NOT `/sixtell` or `/scrubpersonify`** — those de-AI the ENGLISH before translation. By the time a book is
  here, that work is done.
- **NOT prose improvement.** If you are making a correct translation *nicer*, you are out of scope. The
  question is only ever "does this faithfully say what the English says, in fluent target-language prose?"
- **NOT a re-translation.** A badly translated book is a re-translate (`/translate`), not a proofread. If an
  edition is defective beyond fixing at the sentence level, say so and stop rather than patching 200 paragraphs.
