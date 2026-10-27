# Translation proofreading — cloud workspace

This repo is a mirror of Lisa's local `C:\Users\User\Scripts\` folder, set up so translation proofreads can
run in a Claude Code **cloud** session. The pipeline docs were written for Windows paths. Read every path
through this table:

| Docs say | In this repo |
|---|---|
| `C:\Users\User\Scripts\` | the repo root |
| `C:\Users\User\Scripts\translate_now\` (and `translate\`) | `translate_now/` — the English sources |
| `C:\Users\User\Scripts\translated\` | `translated/` — raw translations (proofread INPUT) |
| `…\translated\corrected\` | `translated/corrected/` — proofread OUTPUT |
| `…\translated\_EditLedgers\` | `translated/_EditLedgers/` |
| `…\translated\_tools\` | `translated/_tools/` |
| `…\Multi-Book Translations\_kit\dossiers\` | `_kit/dossiers/` |
| `C:\Users\User\.claude\commands\proofread.md` | `.claude/commands/proofread.md` |
| `2buploaded\` / `proofread\` (published editions) | not in this repo — see "Excerpts" below |

## Setup (once per session)
```bash
pip install python-docx openpyxl
export SCRIPTS_ROOT="$(pwd)"     # preflight.py, sweep_mechanical.py, check_matter.py read this
```

## The job
Follow `.claude/commands/proofread.md` and the run brief
`translated/_EditLedgers/FF_PROOFREAD_BRIEF_20261026.md` (read ALL of it — the "Lessons" bullets were
learned on 21 editions and each one caught real defects). The brief wins over proofread.md where they
differ. Lisa's Frost Falls rulings are in `translated/_EditLedgers/FF_DECISIONS_BRIEF_20261013.md`.

- One sub-agent per edition, sequential, foreground. Sub-agents must NOT spawn sub-agents.
- Series consistency for each language: `translated/corrected/` Inn Trouble + Flour Play (done 2026-10-26/27)
  for the 7 languages that have them; otherwise Flour Play `corrected/` + Frost and Found (`corrected/` if present,
  else `translated/`).
- **Excerpts:** Inn Trouble's back matter excerpts Flour Play Ch1. Use the SAME language's corrected Flour Play
  (`translated/corrected/Flour Play - …_<Lang>.docx`) as the reference for that excerpt's wording.
- After every edition: run the four helper checks from the brief, append to
  `translated/_EditLedgers/PROOFREAD_QUEUE.md`, then **commit and push** (`git add -A && git commit && git push`)
  so a killed session loses at most one edition.
- `bt_anchors.py stamp` needs Lisa's Windows catalogue and will not run here. `bt_anchors.py check` works.
- Questions for Lisa go in `translated/_EditLedgers/PROOFREAD_DECISIONS.md`, never as popups.
- Do NOT promote, format or publish anything. Lisa does that locally.

## Folder notes
- `_superseded/` — old raw files from earlier uploads. Do not use them.
- `translated/Frost and Found …` — Book 1 raw translations, for reference only (FR/DE/IT/ES Book 1 corrected
  copies are in `translated/corrected/`).
