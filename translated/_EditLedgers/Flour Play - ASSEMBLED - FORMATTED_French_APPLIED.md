# APPLIED — Flour Play - ASSEMBLED - FORMATTED_French (2026-10-27)

Output: `translated\corrected\Flour Play - ASSEMBLED - FORMATTED_French.docx` (backup of the starting copy: `corrected\_bak\Flour Play - ASSEMBLED - FORMATTED_French.pre-proofread-20261027.docx`; that starting copy = the raw input plus an earlier asterisk→italic conversion at paras 43, 59, 544, kept).
Method: edits at the `w:t` level only — exact-substring replace inside a known paragraph (substring must occur exactly once, else refused), or a full-paragraph rebuild verified against the paragraph's complete current text; changes mapped onto the existing runs by character diff. No run merged, no paragraph added or removed (1419 → 1419 text paragraphs; 2226 → 2226 incl. empty). One new plain run was appended at [318] so a closing » would not be italic.

- Targeted fixes: 607 (557 rows + the 50-paragraph excerpt; table with para / was → now / why in `_PROOFREAD.md`). By class: mistranslation 226 · term/consistency/typo/tense 117 · untranslated 86 · grammar/agreement 58 · register/idiom/address 55 · dialogue rebuilt by hand 45 · units 14 · front matter 5 · omission 1.
- Dialogue (ruling 1): 321 paragraphs converted automatically (158 em-dash turns, 160 exchange-block closings, 139 attributions moved inside) + 45 hand rebuilds.
- Sweeps: alley → ruelle 25 · cheffe → chef 4 · mitaine → moufle 1 · tourte → tarte 1 · Mme/M. in speech → madame/monsieur 6 paragraphs.
- Typography: 4,189 apostrophes ’, 3 ellipses …, NBSP in 1,190 paragraphs, nested quotes “ ”.
- `<bt>`: 8 stray spans removed (ruling 5), 4 real title anchors added (title page + series list, as Inn Trouble FR), 5 The Binder's Bequest anchors kept (decision FP-FR-4). 13 → 9 spans, 0 unpaired.
- Decisions for Lisa: 6 (FP-FR-1…6; 1, 2, 4 open; 3, 5, 6 applied and flagged).
- Refused by verification: 0.
- Prior-report quotes not found: n/a (no prior report).

## Italic runs changed (declared)
- [128] [674] sign/flyer text: Patisserie → Pâtisserie; « Semaine de grande ouverture » → « Semaine de grande inauguration »; date range « du mardi 10 au dimanche 15 novembre ».
- [439] « sous-alinas » → « sous-alinéas » (typo). [677] « l’évier » → « le lave-mains » (term).
- [1359] [1367] English sell line translated (italics kept; title anchor untouched).
- Runs otherwise identical in content and order (apostrophe/NBSP normalisation aside). Count 45 → 45 vs the starting copy; 41 → 45 vs the raw input = the earlier asterisk conversion (+4, paras 43 ×2, 59, 544).

## Verify (helper checks on the corrected file)
- Untranslated-English helper: [] (empty).
- bt_anchors check: 9 spans, 0 unpaired; span texts = Flour Play, Frost and Found, Inn Trouble, The Binder's Bequest (kept, FP-FR-4).
- check_matter --file: 1 PASS, 0 FAIL.
- preflight --verify: paragraphs 2226→2226 ok; scene breaks 60→60 ok; italic runs 41→45 ok with --expect-italics 4 (earlier asterisk conversion), italic subsequence differs only at the declared paras above; bt anchors 13→9 = −8 stray (ruling 5) +4 real titles → reported FAIL on these declared deltas only.

## Formatter (not touched)
- « Chapitre 10 » heading missing before [454] (body present) — FP-FR-1. TOC lists only « Chapitre 27 ». No Heading 1. Back-matter `* * *` at [1358] [1366].
