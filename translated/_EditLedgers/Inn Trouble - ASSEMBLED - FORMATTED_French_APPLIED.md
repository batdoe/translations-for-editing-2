# APPLIED — Inn Trouble - ASSEMBLED - FORMATTED_French (2026-10-26, second pass)

Output: `translated\corrected\Inn Trouble - ASSEMBLED - FORMATTED_French.docx` (backup of the starting copy: `corrected\_bak\Inn Trouble - ASSEMBLED - FORMATTED_French.pre-proofread2-20261026.docx`).
Method: edits at the `w:t` level only (exact-match replace inside the paragraph, or a character diff mapped onto the existing runs). No run merged, no paragraph added or removed (1491 → 1491). Every replace verified the exact current paragraph text first.

- Targeted fixes: 204 (table with para / was → now / why in `_PROOFREAD.md`)
- Sweeps: 29 hits (manchot 13, moufle(s) 16)
- Dialogue paragraphs converted: 146 (93 em-dash/exchange rebuilt + 53 attributions moved inside)
- Typography: 3,770 apostrophes, 3 ellipses, NBSP in 426 paragraphs, 2 inner-quote pairs
- Decisions for Lisa: 3 (IT2-FR-26-1..3)
- Refused by verification: 0
- Prior-report quotes not found: 0/230

## Italic runs changed (declared)
- [177] first blackmail note: « celle qui a un saphir en son cœur » → « celle avec le saphir en son cœur » (clue wording, ruling 5)
- [297] banner: FROST FALLS THROUGH THE YEARS → FROST FALLS AU FIL DES ANNÉES (ruling 3; still ends in S)
- Apostrophe / NBSP normalisation inside italic runs; text otherwise identical. Italic run count 26 → 26.

## Verify
- Untranslated-English helper: [] (empty)
- bt_anchors check: 8 spans, 0 unpaired; span texts = Inn Trouble, Frost and Found, Flour Play
- check_matter: 0/1 clean — BANNED « À propos de ce livre » ×2, MISSING What's Next heading, get-it CTA (#14), continue-reading line (#18): formatter's job, not touched
- preflight --verify: paragraphs 1491→1491 ok; italic runs 26→26 ok; italic sequence DIFFERS only at [177] / [297] (declared); scene breaks 3→3 ok; bt anchors 8→8 ok; bt titles "lost" = the 3 stray spans removed per ruling 5 → FAIL on declared deltas only
