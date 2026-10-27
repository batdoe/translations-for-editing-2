# APPLIED — Flour Play - ASSEMBLED - FORMATTED_Norwegian (2026-10-27)

- File: `translated\corrected\Flour Play - ASSEMBLED - FORMATTED_Norwegian.docx`; backup of the starting copy: `corrected\_bak\Flour Play - ASSEMBLED - FORMATTED_Norwegian.pre-proofread-20261027.docx`.
- Method: run-level edits on `<w:t>` nodes only (minimal diff per fix; a fix crossing differently formatted runs is refused). Never `set_para_text`. Every fix matched its exact text in its pinned paragraph before writing.
- Applied: 634 targeted fixes (full table in the _PROOFREAD.md, para / was / now / why) + 49 excerpt paragraphs + 2 meta-note deletions ([1162] truncated after '… en full uke før ', completed as the English; [1163] emptied) + 2 card translations as new italic runs ([2078] [2140]) + 13 stray `<bt>` spans removed (26 marker deletions) + 5 real-title anchors added + 66 dialogue paragraphs converted « » to dash.
- Refused by verification: 0. (The first dry run refused 8 because the search strings carried my dump's italic markers; they were corrected and re-matched, and one duplicate entry was dropped.)
- Quoted but not found: 0.

## Excerpt paragraphs replaced (published NO edition, Kapittel 1 [53]–[102])
[2259], [2260], [2261], [2262], [2263], [2264], [2265], [2266], [2267], [2268], [2269], [2270], [2271], [2272], [2273], [2274], [2275], [2276], [2277], [2278], [2279], [2280], [2281], [2282], [2283], [2284], [2285], [2286], [2287], [2288], [2289], [2290], [2291], [2292], [2293], [2294], [2295], [2296], [2297], [2298], [2299], [2300], [2301], [2303], [2304], [2305], [2306], [2307], [2308]

## Italic runs changed (text translated inside existing italic runs)
[596] the founder's note, [625] Hal's heading, [1149] the new-capsule card, [1157] the flyer ('Grand Opening Week'), [1160] Varney quoted, [1176] Doc quoted, [1178] Renée quoted, [2169] [2171] Joyce's letter, [2247] [2257] sell lines (series name), [2312] closing line. Removed: the 3 italic runs that held translator meta-notes [1162] [1163]. Added: 2 italic runs [2078] [2140] (card texts, italic in the English).

## Needs a decision
FP-NO-D1 … D6 in PROOFREAD_DECISIONS.md (all applied provisionally or informational).

## Verification (corrected file)
- Untranslated-English helper: [] (empty).
- bt_anchors check: 10 spans, 0 unpaired; titles only Flour Play / Frost and Found / Inn Trouble / The Binder's Bequest.
- check_matter.py --file: 1 PASS, 0 FAIL.
- preflight --verify: paragraphs 2313 → 2313 ok; scene breaks 61 → 61 ok; italic runs 42 → 45 (= +4 pre-flight asterisk conversions, −3 meta-note runs, +2 card runs; 'ok' with --expect-italics 3). The tool still prints FAIL, for two declared reasons only: the italic subsequence differs where italic text was translated (listed above), and bt anchors 18 → 10 (ruling 5: 13 non-title spans removed, 5 title anchors added).
