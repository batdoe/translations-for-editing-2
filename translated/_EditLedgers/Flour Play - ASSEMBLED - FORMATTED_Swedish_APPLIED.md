# APPLIED — Flour Play - ASSEMBLED - FORMATTED_Swedish (2026-10-27)

- File: `translated\corrected\Flour Play - ASSEMBLED - FORMATTED_Swedish.docx`. Backup of the starting copy: `corrected\_bak\Flour Play - ASSEMBLED - FORMATTED_Swedish.pre-proofread-20261027.docx` (= input + pre-flight's 5 asterisk conversions).
- Method: every paragraph's complete current text was matched before writing; edits applied at the `<w:t>` level by a token diff (runs never collapsed); five paragraphs then repaired by hand at run level so italics sit on the right words ([603] [696] [716] [2258] [2310]).
- Full per-finding table (para, verbatim before, why, after): `Flour Play - ASSEMBLED - FORMATTED_Swedish_PROOFREAD.md`.

## Counts
- Paragraphs changed: 991 of 1591 non-empty (paragraph count 2418 → 2418).
- Targeted fixes: 646 (incl. 50 excerpt paragraphs replaced verbatim from the published Swedish Binder's Bequest, 3 MT translator notes deleted, 1 whole English paragraph translated, 2 stray `<bt>` removed, 4 real-title anchors added) + 3 run-level italic repairs.
- Dialogue: 706 paragraphs converted to straight double quotes (661 dash-turn paragraphs, 45 « » / ”…” paragraphs); attribution verb 'sade' → 'sa' in 99 paragraphs; attribution comma moved inside the closing quote ("…," sa hon) in 35 paragraphs (Ch5's former « » dialogue + [1955]).
- By class: mistranslation/reversed ~217, term consistency/clue chain ~268, proper names/titles/pronouns/speakers 56, address (du) 24, untranslated English 15, units 13, sign/label text (ruling 3) 9, omissions/numbers 8, currency 5, ruling 5 bt 5.
- Refused by verification: 0 (6 drafts failed the pre-write match in the dry run — 4 were my own off-by-one quotes of the text, fixed and re-matched; 2 were dialogue overrides that also changed commas, re-validated).
- Prior report quoted but not found: n/a (no prior report).

## Needs a decision (PROOFREAD_DECISIONS.md, section "Flour Play - ASSEMBLED - FORMATTED_Swedish (2026-10-26)")
- FP-SV-D1 'two degrees under code' kept as the English figure, identical ×3 (applied provisionally).
- FP-SV-D2 100 lb → 45 kg (applied; MT had 50).
- FP-SV-D3 What's Next section (EN [1376]–[1382]) and the closing line [1444] are MISSING — suggested Swedish text logged; needs paragraphs added (not done: paragraph count must not change).
- FP-SV-D4 Book 1 SV still uses dash dialogue (informational).
- FP-SV-D5 du for everyone (informational).

## Verification (corrected file)
- Untranslated-English helper: [] (empty).
- `bt_anchors.py check`: 7 spans, 0 unpaired — Flour Play, Frost and Found, Inn Trouble, The Binder's Bequest.
- `check_matter.py --file`: 1 PASS, 0 FAIL.
- `preflight.py --verify`: paragraphs 2418 → 2418 ok; scene breaks 58 → 58 ok; italic runs 35 → 37 and sequence differs — declared: +5 pre-flight asterisk conversions, −3 of them deleted with the MT notes, and italic text translated/corrected at [603] [625] [716] [863] [877] [1370] [1373] [1390] [1392] [2326]; bt 5 → 7 declared (+4 title anchors, −'HOLLY JOLLY BAKERY', −injected Binder's Bequest at [2246]). Overall line reads FAIL only for these declared changes.
- Formatter notes (not changed): no Heading 1; TOC lists only Kapitel 27; TOC 'Vad händer härnäst?' has no section; title-page/TOC 'Kapitel 1/27' duplicates explained.
