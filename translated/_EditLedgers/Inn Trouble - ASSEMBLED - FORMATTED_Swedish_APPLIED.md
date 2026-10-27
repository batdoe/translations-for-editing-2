# Inn Trouble - ASSEMBLED - FORMATTED_Swedish — APPLIED (2026-10-27)

Output: `translated\corrected\Inn Trouble - ASSEMBLED - FORMATTED_Swedish.docx` (edited in place on top of the mechanical sweep, which had converted 2 Markdown `*…*` spans to italics; a pre-proofread backup of that file was kept in the session scratch dir). Report with the full per-finding table (para, verbatim before, why, after): `_EditLedgers\Inn Trouble - ASSEMBLED - FORMATTED_Swedish_PROOFREAD.md`. Decisions: `_EditLedgers\PROOFREAD_DECISIONS2.md`, section "Inn Trouble - ASSEMBLED - FORMATTED_Swedish (2026-10-27)".

Method: python-docx/lxml, `<w:t>` nodes only, no `set_para_text()`. Order per build: (1) dialogue conversions — each accepted only if the paragraph's text with quote marks/dashes/whitespace stripped was IDENTICAL before and after (punctuation-only change); (2) book-wide rules; (3) targeted edits — each required its exact quoted span to occur exactly once in the paragraph's current text, reduced to character-level operations, refused if a replacement crossed an italic boundary. Paragraph count unchanged (1698 → 1698).

## Counts
- Paragraphs changed: **733** (of 1129 non-empty).
- Targeted fixes: **539** — incl. 55 excerpt paragraphs from corrected Flour Play SV (34 verbatim, 21 adapted to this excerpt's older English), 5 What's Next paragraphs verbatim from Flour Play SV, ~53 note-vs-letters fixes, 9 clue-phrase/word-count fixes, 3 stray `<bt>` removed + 2 title anchors added, 4 untranslated-English passages + 3 sell lines, 4 sign/label translations, 8 reversed meanings, 4 speaker/pronoun errors, 14 address (ni→du), 12 unit fixes (3 measures + 9 figurative inches), 4 currency.
- Dialogue: **457** paragraphs converted to straight double quotes (dash turns, « », ”…”).
- Book-wide rules: `sade` → `sa` 97 paragraphs; `Snöboll` → Snowball 4; cider → äppelmust 11 (ruling 6).
- Refused by verification: **0** (during the build 1 dialogue override failed the punctuation-only check because I had used ’…’ for a nested quote; the check was widened to ’ and it re-applied).
- Prior report quoted but not found: n/a (no prior report).

## Checks on the corrected file
1. Untranslated English: `[]`
2. `bt_anchors.py check`: 8 spans, 0 unpaired — only Inn Trouble / Frost and Found / Flour Play.
3. `check_matter.py --file`: 1 PASS, 0 FAIL.
4. `preflight.py --verify`: paragraphs 1698 → 1698 ok; scene breaks 3 → 3 ok; italic runs 22 → 24 = the sweep's +2; italic SEQUENCE differs only where italic text itself was translated/corrected in place: the note [116] (clue wording, ribbon), drawer labels [696] (SKÖTESTÄLLEN→KÖPEBREV), Theo's card [1141] (clue wording), Fiona's quoted words [1234] (mina brev→min post), the note quotation [1276] (EN→SV), file tab [1292] (PROPERTY→FASTIGHET), sell lines [1622] [1632] [1697] (EN→SV). bt 9 → 8 (−3 stray, +2 anchors) — preflight prints FAIL for these declared changes, as for the other editions.

## Needs a decision (PROOFREAD_DECISIONS2.md)
IT-SV-1 Kapitel 8 heading missing (body present); IT-SV-2 clue phrase = 4 words; IT-SV-3 excerpt English is an older draft of FP Ch1; IT-SV-4 du for everyone (informational); IT-SV-5 Historical Society name vs Book 1; IT-SV-6 Flour Play SV follow-ups; IT-SV-7 formatter items; IT-SV-8 record of applied rulings.

## Refused by verification
None.

## Applied
See the findings table in `_PROOFREAD.md` (all 539 targeted fixes, verbatim before/after) and its lists of book-wide rules and dialogue paragraphs.
