# Inn Trouble - ASSEMBLED - FORMATTED_Turkish — PROOFCHECK (2026-10-28)

- **Mode:** targeted.
- **Edition:** `translated/corrected/Inn Trouble - ASSEMBLED - FORMATTED_Turkish.docx`, edited in place.
- **Backup:** `_proofcheck_backups/Inn Trouble - ASSEMBLED - FORMATTED_Turkish.20261028-174947.docx`.
- **Chapters read in full, English against Turkish, sentence by sentence:**
  - Front matter and blurb.
  - Ch8, Ch26 and Ch28. These are the three chapters the first pass changed least (22%, 23% and 24%).
  - Ch2, Ch19, Ch22, Ch25 and Ch26, which are the plot-critical chapters.
  - All the back matter: the sell lines, What's Next, and the excerpt. For the excerpt I matched each paragraph against Flour Play's English and the corrected Flour Play TR Ch1.
- **First pass's edits audited:** the raw and corrected files were diffed on the same 1565-paragraph grid.
  - 607 paragraphs had changed. 413 have word changes; each of those was read as a word diff next to its English.
  - 194 changed only in punctuation (the « » → dash conversions). These were checked by machine scan, and the 42 DLG rebuilds made by hand were read in full.
  - Book-wide sweeps: apostrophe suffixes on every name (vowel harmony and consonant assimilation), Cemiyet / kasaba / Bayan / Bay inflections, note vs letters, the clue phrase, the "five words" claims, Snowball, reindeer / ren geyiği, cider = elma suyu, kaban, meydan / ağıl, and units.
- **Flags judged:**
  - A, B, C, D: 0 flags.
  - E (3): real but already logged as IT-TR-D1. The Ch19 heading is missing, but the body is complete at [986]–[1046], and I confirmed that by reading it. The Ch18 length flag (232%) is the same issue, because Ch19 is folded into Ch18.
  - F, G: 0 flags.
  - H (24): all false positives.
    - 13 × "yarım milyon" are dollar sums.
    - "elli millik" is covered by ruling 4.
    - The two "bir ayak" hits are body parts (a footprint and a footstep).
    - The nine *kuruş* idioms are logged as decision PC-IT-TR-1.
  - I (1): false positive. [436] is Nick's remembered words quoted inside narration in "…", which the dossier calls for. It is not a spoken turn.
  - J (2): real and correct. [660] `***` and [1024] `* * *` were emptied, and the English has no break at either place: EN [410] is followed directly by Chapter 10, and EN [646]→[647] runs straight on.
- **Clue chain:** it holds.
  - The phrase is `kalbindeki safir` at all 9 places: [191] (accusative, IT-TR-D2), [193], [227], [996], [998], [1000], [1147], [1185] and [1291].
  - Every "five words" claim now reads "iki kelime", matching the two-word phrase: [1000] ×2, [1014], [1147] and [1238].
  - The note is *not* everywhere. *Mektup* is used only for the 1924 letters and for ordinary letters; I checked all 23 singular forms, and none refers to the note. Theo's cards are *kart* (*fiş* = 0).
  - Ch19, Ch22, Ch25 and Ch26 were checked explicitly.
  - Sam is owed the twenty dollars: blurb [31] `Yirmi dolar alacağı olup`, and Ch8 and Ch17.
  - Other settled forms: cider = elma suyu (*şıra* = 0), Snowball (Kartopu = 0), çember, meydan, veranda.
  - The excerpt has "Very nearly" = `— Neredeyse.` [1517].
- **20 random APPLIED rows:** all 20 "now" texts are in the file.

## Missed by the first pass (all applied)
| ¶ | Ch | target (was) | English | class | now |
|---|---|---|---|---|---|
| 1020 | 19 | `Sana bunu yapma izni veren sevgidir, Jess.` | It's the love that lets **him**, Jess. | reversed (who-did-what) | `Ona bunu yapma izni veren sevgidir` |
| 1020 | 19 | `Kendi kendine … inandırılarak` | By telling himself… | grammar (wrong passive) | `Kendini … inandırarak` |
| 1547 | back | `— Dün … yola bakmıyordu sanki?` ("it seems they weren't facing the road") | Weren't the snowmen all facing the road yesterday? | reversed (copied from FP TR [110], see PC-IT-TR-2) | `hep yola bakmıyor muydu?` |
| 1274 | 25 | `akşam kalabalığı gelmeden … hemen önce` | the crowds gone home | mistranslation | `akşamdan önce, kalabalık evine dağılmışken ve ortalık henüz toplanmaya başlamamışken` |
| 157 | 2 | `Telefon çaldığında, ellerim…` | The call came **the next morning** | omission | `Ertesi sabah telefon çaldığında` |
| 1264 | 25 | `Baştan sona anlatıldığında hatta… o sadece` | Of a thing that, told whole, isn't even… | partial omission | `Baştan sona anlatıldığında hiç de… olmayan bir şeyden… o sadece` |
| 1354 | 28 | `o utangaç küçük çekilişlerini` (shy) | embarrassing little raffles | mistranslation | `o biraz utanç verici küçük çekilişlerini` |
| 181, 193, 1262 | 2, 25 | `dedem saati` ("my-grandpa clock") | grandfather clock | lexical | `dede saati` ×3 |
| 1148 | 22 | `saptırır … hiçbiri saptırmamıştı` | hoping one would turn off | grammar (transitive verb) | `sapar … sapmamıştı` |
| 213 | 2 | `Kasabenin` | (typo the `kasabe` sweep missed, because it is capitalised) | typo | `Kasabanın` |
| 207 | 2 | `Blackburnler'in` | the Blackburns | typo (apostrophe; the 18 other `Blackburnler-` forms take no apostrophe) | `Blackburnlerin` |
| 373 | 4 | `Neil’a` | toward Neil | vowel harmony (book has Neil’i/Neil’in ×9) | `Neil’e` |
| 500, 671, 679 | 6, 10 | `Bram'e`, `Bram’in` ×2, `Bram’i` | — | vowel harmony (book has Bram’a/Bram’ın/Bram’la) | `Bram'a`, `Bram’ın` ×2, `Bram’ı` |
| 1397 | 29 | `Frost Falls'da` | — | consonant assimilation (×15 `Falls'ta/-tan/-taki`) | `Falls'ta` |
| 520 | 6 | `çayırlığın kenarındaki` | at the edge of **the green** | term drift (green = meydan) | `meydanın kenarındaki` |
| 1279 | 26 | `çayırda katlanan` | folded **on the green** | term drift | `meydanda katlanan` |

## Regressions introduced by the first pass (all applied)
| ¶ | Ch | target (was) | English | class | now |
|---|---|---|---|---|---|
| 1305 | 26 | `Kulağa neredeyse soylu bir şeymiş gibi getirdi.` (ungrammatical rewrite) | He made it sound almost noble. | broken grammar | `… gibi gelmesini sağladı.` |
| 340 | 3 | `çitle çevrili çayırın ötesinde` (rewrite of `çitin hemen ötesinde`) | out past the paddock | term drift against the pass's own paddock = ağıl unification (×7) | `ağılın ötesinde` |
| 671 | 10 | `Bram'le` (rewrite of `Bram ile`) | — | vowel harmony | `Bram'la` |
| 859 | 15 | `Ocak ayına` (rewrite capitalised the month) | till January | orthography (month names are lower case outside dates) | `ocak ayına` |

Other checks:
- **Dialogue system:** no regressions. The scan found no leftover « » “ ”, no odd straight quotes, no dash without its space, no capitalised or period-led speech verbs, and no stray space before punctuation. Every English dialogue paragraph opens with "—", except two that are deliberate: the 2 MT splits in Ch8 ([563] [569], narration) and [773], where the narration leads into the speech. All 42 hand-rebuilt attributions read correctly.
- **The Bayan/Bay, Cemiyet and kasaba sweeps:** every inflected form is correct (Cemiyet-i/-e/-te/-ten/-in, Bayan Pelletier’nin, Bay Kim’in…). The only exception is the capitalised `Kasabenin` above.

## Ledger mismatches
- None (20 of 20 found).

## Decisions added (`PROOFCHECK_DECISIONS.md`)
- **PC-IT-TR-1:** the nine *kuruş* idioms against the dollars-only lesson. I recommend keeping them.
- **PC-IT-TR-2:** a Flour Play TR follow-up. FP [110] has the same reversed question that is fixed here at [1547]. FP [134] and [1560] here share `Köknarı kökünden bağladım` ("bound the balsam home"); I suggest changing it in both books.

## Open first-pass decisions re-checked
- IT-TR-D1, D2, D4, D5, D6 and D8: the quotes are still accurate.
  - The heading lines are untouched, and nothing was renumbered.
  - The units are SAFE-rule conversions, all logged: on altı dönüm, on santim, bir parmak, yarım santim and iki metre.
- IT-TR-D3 (Theo sen against Flour Play siz) is still open and unchanged, for example [1291] and [1477].
- IT-TR-D7: the excerpt policy holds.
  - 31 paragraphs are verbatim from Flour Play TR, wherever the two English texts match.
  - Every paragraph where the English differs follows Inn Trouble's own English: [1513] "Over the weekend", [1548] bandstand / war memorial, [1558] present-tense "Because I know", and [1559] with its extra clause.

## Refusals
- None. All 25 edits matched their text exactly once. Only `<w:t>` nodes were edited.
- Compared with the backup: paragraphs 1565 → 1565; italic runs 25 → 25, same text and order; bt 8 → 8; scene breaks 3 → 3. Only the 22 listed paragraphs changed.

## Four checks (after the fixes)
- **looks_english:** `[]`.
- **bt_anchors check:** 8 spans, 0 unpaired. The only span texts are Inn Trouble, Frost and Found and Flour Play.
- **check_matter --file:** 1 PASS, 0 FAIL.
- **preflight --verify:** paragraphs 1565 → 1565 OK. The rest of the FAIL line is the first pass's declared changes, compared with raw (italics +4 from the sweep, breaks −2, bt −5+3), plus 5 more paragraphs that now differ from raw.
- **proofcheck.py re-run:** A=0 B=0 C=0 D=0 E=3 F=0 G=0 H=24 I=1 J=2. This is unchanged, because none of today's fixes were A–J flags.

## Verdict: **SIGNIFICANT** (borderline)
- The plot chain is intact: the clue phrase, note vs letters, word counts, owed dollars and cider all hold.
- The verdict is SIGNIFICANT because two reversed-meaning sentences were missed. In Ch19 [1020], Nick's "the love that lets **him**" had become "lets **you**". In the excerpt [1547], the snowmen question was inverted.
- One omission and two partial or semantic slips were also missed, in Ch2 and Ch25.
- **Rate:** about 14 real defects in the 9 units read in full (7 chapters + front + back), so about 1.5 per chapter. The other 11 edits came from the diff audit and the sweeps.
- **Recommendation:** a `full` re-read of the 23 chapters not read today, aimed at sentence-level slips. The clue chain doesn't need it.
