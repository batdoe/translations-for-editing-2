# PROOFCHECK — Flour Play - ASSEMBLED - FORMATTED_Filipino — 2026-10-28

- **Mode:** targeted.
- **Files:**
  - Corrected (edited in place): `translated/corrected/Flour Play - ASSEMBLED - FORMATTED_Filipino.docx`
  - Backup: `translated/_EditLedgers/_proofcheck_backups/Flour Play - ASSEMBLED - FORMATTED_Filipino.20261028-202652.docx`
  - Raw input used for the diff: `_superseded/Flour Play - ASSEMBLED - FORMATTED_Filipino.docx`
- **Read in full, English against Filipino, sentence by sentence:**
  - Front matter and blurb.
  - Ch4, Ch12 and Ch13, the three chapters with the lowest change density.
  - Ch9, 11, 17, 20, 21, 22, 23 and 24: walk-in / cold room, sour base, the confrontation and the charges.
  - Ch27 and all back matter (sell lines, What's Next, the closing line).
  - The Binder's Bequest excerpt only for anchors and the closing line. It is the published text (FIL3-D4).
- **Diff-reviewed:** Ch1–3, 5–8, 10, 14–16, 18, 19, 25 and 26. Every paragraph the first pass changed was read next to its English, as a word diff against the raw input.

## Flags judged (script sections A–J)

| Section | Count | Verdict |
|---|---|---|
| A | 0 | — |
| B | 2 | False positives. [2074] *Bûches de Noël* is the French product name, kept as in the English sign. |
| C, D | 0 | — |
| E | 4 | Real, already logged as FIL3-D1: four stray `Kabanata 3` lines in Ch8 (docx [711][717][723][731]). Only the heading line is wrong; no body text is missing around them (checked against EN Ch8). This is a decision, not a renumber. |
| F, G | 0 | — |
| H | 27 | False positives under the imperial-units ruling (FIL2-D3/FIL3-D3): pulgada, talampakan, milya, libra. "sentimo" means cents, which is correct with dollars. No piso and no poison words. |
| I | 0 | 540 “ openers, one system. |
| J | 0 | — |

## Clue chain (section K), traced to every target occurrence

- **Sour base** = `maasim na base`: 20 out of 20. Ch22 has the second one at [1868] `Maasim na base, isang sako`. No starter or yeast rendering, and `pampaalsa`/`lebadura` are used only for yeast.
- **Walk-in and Joyce's word:**
  - Walk-in = `palamigan`: 7 out of 7. Ch9 [796]; Ch17 [1421] (Renée's walk-in); Ch20 [1682] ×3; Ch22 [1864]; Ch23 [1939].
  - Joyce's word = `‘ang malamig na silid’`: at all 10 English places. The two words never merge, so the Ch22–24 slip survives.
  - Pete's locker = `imbakan`, kept distinct.
- **"Ten times"** = `Sampung beses` [938] and `sampung beses na dami` [942]. The [938] sentence was ungrammatical after the first pass; fixed.
- **Gate key and lock:** gate key = `susi ng tarangkahan` [1692]. The shop key is distinct (`susi niya sa tindahan`). The Ch23 key and lock lines read correctly.
- **Order book** = `aklat ng order`: 7 out of 7. It never spilled onto Hal's book or the ring binder.
- **"Nothing I can name"** = `Wala akong mapangalanan` [922], once (said by Doc, as in the English).
- **"Two degrees below"** is identical at [782][1294][1298].
- **Other plot facts:**
  - No poison or toxic words.
  - Joyce is 65 [2050].
  - The partnership ended 25 years ago, after 15 years together. Checked at [467][471][1708][1898][1975][1997].
  - "The twentieth" = ikadalawampu [1254][1658].
  - Dollars only.
  - DIRTY is rendered MARUMI, not a vulgarity.
- **Grange** = one rendering, `Grange`: 16 out of 16.
- **Anchors:** the Binder's Bequest anchors are kept, and the closing line `Simulan nang basahin ang <bt>The Binder's Bequest</bt> ngayon din!` is present [2426].

## Missed by the first pass (25 edits in 23 paragraphs, all applied)

| para | Ch | target (before) | English | class | fix |
|---|---|---|---|---|---|
| 31 | blurb | `…panaderya at sinabi kay Jessica` | is standing … telling Jessica | blurb tense | `sinasabi` |
| 33 | blurb | `Pagkatapos, may lumipad na ladrilyo sa bintana` | Then a brick comes through the window | blurb tense | `may ladrilyong lumulusot sa bintana` |
| 56 | 1 | `na may kalakihang kalahati na kaysa sa sinuman` | half again the size of anyone else's | comparative (reads "half the size") | `na mas malaki nang kalahati kaysa sa sinuman` |
| 796 | 9 | `Sasabihin ko sa iyo ito` | I'll tell you this much | address (Varney to stranger) | `sa inyo` |
| 824 | 9 | `na may mukha na parang panahon` | with a face like weather | literal idiom | `na nakasimangot na parang nagbabadyang bagyo` |
| 863 | 10 | `nakatayo na sa mantel` | on the mantel | mistranslation (mantel = tablecloth) | `sa patungan sa ibabaw ng tsimenea` |
| 946 | 11 | `nanatili sa aking pinakalayong bahagi` | kept to my far side | mistranslation | `sa kabilang tabi ko` |
| 995 | 12 | `nakabukas nang kalahati sa bawat umaga` | stood open half of every morning | meaning ("half-open") | `nakabukas sa kalahati ng bawat umaga` |
| 1027 | 12 | `na bukas ang kalahati sa bawat madilim na umaga` | stood open half of every dark morning | same | `na bukas sa kalahati ng bawat…` |
| 1013 | 12 | `masama ang naging itsura niya kaysa dati` | he looked worse than he ever had | comparative lost | `mas masama … kaysa kailanman` |
| 1052 | 13 | `may taglay na init ng ulo na wala siya at isang kalakal…` | held a temper he didn't have and a trade he didn't know | **reversed reasoning**: "temper" (disposition) rendered "init ng ulo" (anger), which Pete plainly HAS | `nangangailangan ng ugaling wala sa kaniya at ng hanapbuhay…` |
| 1062 | 13 | `gustong magkaroon ng init ng ulo para sa kadiliman…` | wanted a temper for the dark and a baker's trade | same | `nangailangan ng ugaling sanay sa dilim at ng hanapbuhay ng panadero` |
| 1060 | 13 | `isang lalaking lumaki na umaasa…` | a man grown to expect one thing through his door | mistranslation ("grew up") | `nasanay nang umasa ng iisang bagay mula sa mga pumapasok…` |
| 1064 | 13 | `Tinitigan niya ako nang sandali` | a long moment | meaning | `nang matagal` |
| 1231 | 15 | `ang dalawang guwantes na kasinglaki ng hinlalaki ni Bram` | Bram's two thumb-sized mittens | possession (craft word) | `ang dalawang guwantes ni Bram na kasinglaki ng hinlalaki` |
| 1353 | 17 | `Nawala ito sa akin nang lampasan ko ang ilaw sa parmasya.` | I lost it past the light at the pharmacy | **who did what**: Danny was at his window; the figure passed the light | `…nang lumampas ito sa ilaw…` |
| 1377 | 17 | `Akala ninyo siya ang gumawa nito.` | You think she did this | nuance ("akala" = mistaken belief) | `Sa tingin ninyo…` |
| 1411 | 17 | `sapat upang maasim ang lahat` | enough to sour everything | grammar | `mapaasim` |
| 1743 | 21 | `huwag mo rin akong kausaping may pagpapakaawa` | don't be kind to me | mistranslation ("begging") | `huwag mo rin akong kaawaan` |
| 1888 | 22 | `Tinawagan siya sa telepono ni Tanaka,` | Tanaka phoned her | ambiguous agent | `Tinawagan siya ni Tanaka,` |
| 1894 | 22 | `nayupit na ibon` ×2 | the bent bird | typo | `nayuping ibon` |
| 1927 | 23 | `Binuksan niya ang brown folder.` | the brown folder | code-switch (and [1911] uses kayumangging) | `kayumangging folder` |
| 1975 | 23 | `Kalahati ko ang tindahan.` | The shop was half mine | unclear in the confrontation | `Kalahati ng tindahan ay akin.` |
| 2017 | 23 | `Sasampahan kayo ngayon.` | You'll be charged today | incomplete | `Sasampahan kayo ng kaso ngayong araw.` |

## Regressions introduced by the first pass (5 edits in 4 paragraphs, all applied)

| para | Ch | raw → first pass | English | problem | fix |
|---|---|---|---|---|---|
| 938 | 11 | `Sampung beses kaysa sa kailanman ay ilalagay ng isang panadero` → `Sampung beses ng kailanman ay ilalagay ng sinumang panadero ng tinapay` | Ten times what any bread baker would ever put in | the clue line was made ungrammatical | `Sampung beses ng dami na kailanman ay ilalagay…` |
| 938 | 11 | `sa bawat sako` → `nang tig-iisang sako` | buy it by the sack | "one sack each" | `nang kada sako` |
| 1597 | 19 | `ay patunay sa counter` → `ay isang proof sa counter` | a proof on somebody's counter | English left in | `ay borador muna ng imprenta sa counter` |
| 1866 | 22 | `nakalagay sa patunay` → `nakalatag bilang proof` | lay in proof on her counter | English left in | `nakalatag bilang borador ng imprenta` |
| 1753 | 21 | `Aasa ako sa pangako mong iyan.` → `Hahawakan kita sa dalawang pangakong iyan.` | I'm holding you to both halves of that | calque ("I'll physically hold you") | `Panghahawakan ko ang dalawang pangakong iyan.` |

- No other regressions were found in the changed paragraphs of the diff-reviewed chapters.
- The sweeps checked clean:
  - `lupon`→`bilog` did not hit "the board" at [584][634][1492], which correctly stays `lupon`.
  - `abenida`, `taong-niyebe`, `MARUMI` and `Araw ng Pasasalamat` have no inflection or capitalisation breakage and no leftovers.
- Italics and `<bt>` are intact.

## Ledger check
- I sampled 20 random entries from `_PROOFREAD.md` and found each "now" text in the file: 20 out of 20. The two that first missed only differed in straight versus curly quotes.
- `_APPLIED.md` counts match: 1376 non-empty paragraphs, 2427 docx paragraphs, 44 italic runs, 10 bt.

## Decisions added (PROOFCHECK_DECISIONS.md)
- **PC-FIL3-1.** Ch22 [1881]/[1882]: Tanaka's line was split, so "I sat in Fiona's sitting room with you…" reads as Jessica speaking. This needs a paragraph merge. Recommended: merge.
- **Note for PC-FIL2-1** (Inn Trouble excerpt): if Lisa copies Flour Play Ch1 into it, she should copy the current text, which includes the [56] fix.
- **FIL3-D1–D4** were re-checked: the quotes are still accurate, and nothing that was a judgment call was applied.

## Refusals
- 0. All 30 edits matched exactly once inside a single `<w:t>` node.

## Checks after the fixes
- **Paragraphs:** 2427 → 2427. Italic runs 44 → 44, identical sequence. bt 10 → 10. Scene breaks 58 → 58. Only the 28 paragraphs listed above changed (compared against the backup).
- **looks_english:** `[]`.
- **bt_anchors check:** 10 spans, 0 unpaired. The only span texts are Flour Play, Frost and Found, Inn Trouble and The Binder's Bequest.
- **check_matter:** 1 PASS, 0 FAIL.
- **preflight --verify:** reports "source or corrected copy missing", because the raw file is kept in `_superseded/`. The integrity checks were done by hand against the backup (see "Paragraphs" above).
- **proofcheck.py re-run:** A=0 B=2 C=0 D=0 E=4 F=0 G=0 H=27 I=0 J=0. The counts are unchanged because none of these flags was a fixable defect: B and H are false positives, and E is FIL3-D1.

## Verdict: **SIGNIFICANT**
- 30 defects in 28 paragraphs, all fixed: 25 missed and 5 regressions. Plus 1 decision. That is about 1.1 real defects per chapter, counted over the 27 chapters read in full or diff-reviewed.
- Under the rubric, a missed reversed-meaning defect makes the verdict SIGNIFICANT. This edition had two:
  - Ch13 [1052][1062], Pete's exoneration: "a temper he didn't have" was rendered as anger. Pete plainly has anger, so the reasoning that clears him read backwards.
  - Ch17 [1353], Danny's sighting: he was made to walk past the pharmacy light. In fact the figure did.
- Both are fixed. The clue chain is intact and no text is omitted.
- **Recommend `full` mode** for this edition. The unchanged paragraphs of the 14 diff-reviewed chapters (Ch1–3, 5–8, 10, 14–16, 18, 19, 25, 26) were not re-read bilingually, and both reversals sat in text the first pass never touched.
