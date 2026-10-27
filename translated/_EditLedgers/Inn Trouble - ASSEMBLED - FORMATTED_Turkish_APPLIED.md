# APPLIED — Inn Trouble - ASSEMBLED - FORMATTED_Turkish (2026-10-27, cloud run)

- File: `translated\corrected\Inn Trouble - ASSEMBLED - FORMATTED_Turkish.docx`, edited in place on top of the mechanical sweep (4 asterisk spans → italics). Pre-proofread backup: session scratch dir (`backup_pre_proofread.docx`).
- Method: every edit matched its target text exactly (once) in the paragraph's complete current text before writing; the final paragraph text was written onto the existing `<w:t>` nodes by a character diff (runs never collapsed, `set_para_text` not used); italic runs checked run-by-run afterwards (same 25 runs, same order; text changed only where intended — below).
- Full per-finding table (para, class, Turkish before verbatim, why, Turkish after): `Inn Trouble - ASSEMBLED - FORMATTED_Turkish_PROOFREAD.md`.

## Counts
- Paragraphs changed: 607 (preflight); paragraph count 1565 → 1565.
- Itemised fixes: 578 table rows (incl. 39 per-paragraph global-sweep rows) + 366 dialogue-conversion paragraphs.
- By class: mistranslation 193 (+12 reversed meanings), term consistency 94, typos 57, excerpt rebuild 49, dialogue rebuilds 44, sweeps 39, address (sen/siz) 28, clue chain 19, untranslated English 18, units 5, stray bt 5, blurb 5, title anchors 3, omissions 2, spurious scene breaks 2, foreign-language leaks 2, sign 1.
- Stray `<bt>` removed: 5 (Yarn Tales, Winter Wonderland Inn ×3, Frost Falls). Title anchors added: 3 ([0] [18] [19]).
- Dialogue paragraphs converted: 366 (« » 356 + straight quotes 10) + ~45 attribution/narration rebuilds by hand (DLG rows).
- Refused by verification: 0. Prior report quoted but not found: n/a (no prior report).

## Omissions restored (from the English, sentence level)
- [575] 'He didn't look at me.' (Sam, Ch8). [611] 'I walked away with a better question' (Ch8). [1291] the clue phrase in Jessica's confrontation (Ch26) — see worst defect 2.

## Needs a decision (PROOFREAD_DECISIONS2.md, section "Inn Trouble - ASSEMBLED - FORMATTED_Turkish (2026-10-27)")
- IT-TR-D1 Ch19 heading missing (body present) + six spelled-out headings — formatter.
- IT-TR-D2 clue phrase = "kalbindeki safir" (2 words; accusative in the note) — applied.
- IT-TR-D3 Theo ↔ Jessica kept **sen** in Book 2; Flour Play TR has siz — needs Lisa.
- IT-TR-D4 the two notes unified to siz — applied.
- IT-TR-D5 spurious scene breaks emptied; back-matter separators — formatter.
- IT-TR-D6 four acres → on altı dönüm — applied.
- IT-TR-D7 excerpt rebuilt from corrected Flour Play TR Ch1 (adapted where the English differs) — informational.
- IT-TR-D8 address table / Vera farewell register — applied.

## Verification (corrected file)
- Untranslated-English helper: [] (empty).
- `bt_anchors.py check`: 8 spans, 0 unpaired — only Inn Trouble, Frost and Found, Flour Play.
- `check_matter.py --file`: 1 PASS, 0 FAIL.
- `preflight.py --verify`: paragraphs 1565 → 1565 ok; italic runs 21 → 25 = the +4 sweep conversions already in the starting copy (vs the starting copy: 25 → 25, same order); italic TEXT intentionally changed at [191] (the note: siz + 'büyük büyükannenizin' + clue phrase), [996] (card: clue phrase), [1089] (Fiona's 'letters' → posta), [1169] (file tab translated), [1404] (stray « » removed from the quoted letter line), [1499] [1509] [1564] (English sell lines translated); scene breaks 5 → 3 (spurious [660] [1024] emptied, = English 3); bt 10 → 8 (−5 stray, +3 title anchors). Overall line reads FAIL only for these declared changes.

## Dialogue-converted paragraphs (366)
40, 42, 48, 52, 56, 64, 66, 70, 74, 76, 78, 80, 86, 92, 94, 96, 98, 104, 106, 108, 110, 112, 118, 122, 124, 126, 130, 142, 152, 161, 163, 165, 167, 169, 173, 185, 195, 197, 201, 203, 207, 211, 215, 217, 219, 221, 227, 229, 231, 233, 235, 237, 239, 241, 247, 249, 257, 272, 274, 276, 278, 282, 284, 286, 290, 292, 294, 300, 302, 304, 306, 308, 310, 318, 322, 324, 326, 328, 330, 332, 334, 338, 357, 359, 361, 375, 377, 379, 383, 387, 389, 405, 419, 420, 421, 422, 427, 428, 429, 430, 431, 432, 433, 436, 437, 438, 439, 440, 441, 442, 444, 446, 447, 456, 458, 462, 470, 472, 476, 478, 486, 488, 490, 492, 496, 498, 500, 506, 512, 514, 516, 518, 526, 528, 535, 536, 538, 540, 542, 544, 545, 546, 547, 548, 620, 622, 624, 628, 630, 634, 636, 648, 650, 652, 665, 667, 669, 673, 675, 677, 679, 683, 687, 691, 693, 695, 697, 699, 705, 707, 720, 722, 728, 730, 738, 740, 742, 746, 752, 754, 756, 773, 774, 780, 786, 788, 796, 798, 800, 802, 808, 810, 814, 816, 818, 831, 833, 836, 839, 840, 842, 843, 845, 852, 853, 855, 856, 857, 858, 859, 861, 862, 863, 864, 865, 866, 867, 868, 869, 871, 873, 874, 875, 876, 877, 881, 882, 889, 893, 895, 897, 901, 903, 905, 907, 909, 913, 915, 917, 921, 923, 932, 934, 942, 944, 946, 952, 954, 962, 992, 1014, 1016, 1018, 1020, 1032, 1038, 1040, 1053, 1057, 1059, 1063, 1069, 1071, 1073, 1077, 1079, 1081, 1093, 1095, 1108, 1116, 1118, 1120, 1124, 1126, 1128, 1136, 1138, 1177, 1179, 1201, 1213, 1215, 1219, 1221, 1229, 1231, 1242, 1244, 1248, 1250, 1252, 1260, 1264, 1266, 1268, 1270, 1272, 1285, 1291, 1295, 1301, 1305, 1311, 1317, 1323, 1324, 1327, 1338, 1346, 1350, 1352, 1354, 1356, 1375, 1385, 1393, 1395, 1404, 1410, 1418, 1422, 1430, 1432, 1445, 1449, 1451, 1453, 1457, 1461, 1463, 1471, 1473, 1475, 1477, 1483, 1485, 1491, 1493, 1514, 1515, 1516, 1517, 1518, 1519, 1520, 1523, 1525, 1526, 1529, 1530, 1531, 1532, 1535, 1536, 1539, 1541, 1542, 1543, 1545, 1547, 1552, 1553, 1554, 1555, 1556
