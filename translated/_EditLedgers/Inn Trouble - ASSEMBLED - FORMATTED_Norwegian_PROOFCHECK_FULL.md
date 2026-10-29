# PROOFCHECK (FULL) — Inn Trouble - ASSEMBLED - FORMATTED_Norwegian (2026-10-29)

- **Mode:** FULL. I read the whole book bilingually, each English paragraph next to its Norwegian paragraph(s), in order: front matter, blurb, Ch1–Ch31, the sell lines, What's Next? and the Flour Play excerpt. This follows the same day's targeted pass (`…_PROOFCHECK.md`, 33 edits).
- **Files:** edited `translated/corrected/Inn Trouble - ASSEMBLED - FORMATTED_Norwegian.docx` in place. English: `translate_now/Inn Trouble - ASSEMBLED - FORMATTED.docx`. Raw `_superseded/…_Norwegian.docx` (read-only) was used only to sort each defect into miss vs regression.
- **Backup:** `_EditLedgers/_proofcheck_backups/Inn Trouble - ASSEMBLED - FORMATTED_Norwegian.20261029-000204.full.docx`
- **Chapters read in full:** 31 of 31 + front matter, blurb, all back matter.
- **Skipped per brief:** step-2 diff audit and 20-row ledger sample (done by the targeted pass).
- **Flags (step 1):** re-run A=0 B=0 C=0 D=0 E=0 F=0 G=0 H=6 I=0 J=0 — the same 6 H flags the targeted report already judged false positives (`sider` = sides, `tomme` = empty ×4, `fem mil` ruling 4). Nothing left unjudged.
- **Totals:** 61 text edits in 55 paragraphs: 60 misses (already in the raw file) + 1 regression. Refusals: 0. Every match sat inside a single `<w:t>`; no runs merged.
- **Paragraph numbers** = full `<w:p>` grid (as `proofcheck.py` counts).

## Today's targeted checks (all ✓)
- **Note = `utpressingslapp`/`lapp`, never `brev`:** 0 `utpressingsbrev` left; `brev` only for the 1924 letters, Constance's letter [950], rejection letters, Fiona's mail, North Pole letters. Ch19 card = `kortet` ([981] "Og kortet var i Theos hånd"), [973] "til sin søster" ✓.
- **Theft:** "Theo visste om tyveriet" / "Han visste om tyveriet" at Ch22 [1120], Ch23 [1157], Ch26 [1274] ×2; no `sto for` / `hadde tyveriet` ✓.
- **Paddock:** `luftegården` everywhere (0 `innhegning`; the 3 `hagen` in Ch10 are the front garden, EN "front garden") ✓. **Comet** English ✓ (0 `Komet`).
- **Clue phrase** `safiren i hjertet` identical at all places; "five words" lines = `tre ord` ✓. Blurb now says `steinen` as the English does ("the stone at the brooch's heart").
- **Spoiler-gender:** every pre-reveal reference to the writer/courier checked (`den som hadde skrevet den`, `forfatteren`, `noen andre`, `en skikkelse`, `de`/`dem`, `vedkommende`, `en eller annen småtyv`). All neutral. The only gendered ones (`han`, `hans makt`, `En mann hadde strukket seg ut fra mørket`, Fiona's `han har gått inn i foajeen min`) mirror an English "he/a man" ✓.
- **Run lessons:** Ch19 [997] `som tillater ham det` ✓ · Ch27 [1319] `ruinert seg for å berge` ✓ · Blackburn papers (`Blackburn-papirene`) vs deed (`skjøte`) distinct ✓ · `han din` = "your man" ✓ · green `allmenningen` ✓ · `eplemost` ✓ · Sam is owed ✓ · "six letters" kept ✓ · narration preteritum throughout (no presens perfektum drift found).

## Missed by the first pass (all APPLIED)
| Para | Ch | Norwegian (was) | English | Class | Fix |
|---|---|---|---|---|---|
| 1192 | 24 | `Theo slipper aldri å bli en mann som kan bli tilgitt.` | "Theo never has to become a man who could be forgiven." | **reversed meaning** (*slipper aldri å* = is never spared from) | `Theo trenger aldri å bli en mann som kan tilgis.` |
| 1291 | 27 | `kvinnen de hadde forgrepet seg på` · `historikk med svik` | "the woman they had wronged" · "history of harm" | **mistranslation** (*forgripe seg på* = sexually abuse/assault) | `kvinnen de hadde gjort urett mot` · `historikk med å skade noen` |
| 469 | 8 | `skille mennene som kan vise følelser fra dem…` | "men who can **wear** a feeling" (put one on) | reversed sense | `som kan ta på seg en følelse, fra dem…` |
| 645 | 10 | `som intet mindre enn det hun hadde krav på` | "no more than her plain due" | comparative reversed | `intet annet enn` |
| 116 | 2 | (note) `brosjen oldemor tok` | "your great-grandmother" | possessive dropped in the clue note | `oldemoren din` |
| 479 | 8 | `Denne gamle historien hennes, hvis det da er en historie` | "This old trouble of hers, if it is trouble" | mistranslation | `Dette gamle trøbbelet hennes, hvis det da er trøbbel` |
| 733 | 12 | `ved den absolutte enden av sin tålmodighet` | "at the absolute end of his rope" | idiom | `som var kommet helt til veis ende` |
| 1307 | 27 | `Du slipper den enkle utveien` | "You don't get the easy version" | sense (*slippe* = be spared) | `Du får ikke den enkle versjonen` |
| 1309 | 27 | `hardere enn en tilgivelse` | "harder than a pardon" | term (legal; [1291] `benådning`) | `en benådning` |
| 1326 | 28 | `med sin kone ved sin side i sin kremfargede kashmirgenser og med sin fine kåpe` | "his wife beside him in **her** cream cashmere with **her** good coat" | pronoun reference (reflexive *sin* = his) | `mens kona hans sto ved siden av ham i den kremfargede kashmirgenseren sin med den fine kåpen sin over armen` |
| 1233 | 25 | `den halvparten som skammet deg` | "the half of it that shames you" | verb sense | `den halvparten du skammet deg over` |
| 1418 | 30 | `akkurat slik en hånd hadde satt den fra seg` | "exactly **where** a hand had set it down" | mistranslation | `akkurat der` |
| 1406 | 30 | `lagt en boks med byens skatter oppi og gravd den ned` | "sealed up a box … and buried it" | garbled | `forseglet en boks med byens skatter og gravd den ned` |
| 1471 | 31 | `den ettermiddagen den kom opp av jorden` | "the afternoon it came up" (out of a pumpkin) | addition | `den spirte fram` |
| 1473 | 31 | `Det har ikke en gang hengt med hodet` | (the holly, m.) | agreement | `Den har ikke engang…` |
| 32 | blurb | `den nevner safiren i hjertet av brosjen` | "names the **stone** at the brooch's heart" | addition (blurb deliberately says stone) | `steinen` |
| 269 | 4 | `Papiret hadde vært her.` | "The paper was here." (still is) | tense changes meaning | `Papiret var her.` |
| 337 | 5 | `som om hun ikke akkurat hadde gitt meg en bit av verden` | "as though she hadn't just handed me anything at all" | altered image | `noe som helst` |
| 1397 | 29 | `som om hun ikke akkurat hadde knust meg fullstendig` | "undone me entirely" (moved, not crushed) | sense | `rørt meg helt i stykker` |
| 1375 | 29 | `litt uforsonlig` | "a little fierce" | sense (*uforsonlig* = implacable) | `litt kampklar` |
| 1102 | 22 | `på ovnsforleggeren` | "the hearth rug" | mistranslation (stove floor plate) | `på teppet foran ildstedet` |
| 387 | 6 | `Jeg lette opp den som ledde…` · `i femtiårene` | "went looking for whoever ran" · "about fifty" | sense · number | `Jeg lette etter den som ledet…` · `på rundt femti` |
| 1159 | 23 | `uten at noen ville ense det en tanke` | "no one would think a thing of it" | garbled idiom | `uten at noen ville tenke noe over det` |
| 1227 | 25 | `holdt pusten og noens hånd` | "held breath" (noun list) | garbled | `tilbakeholdt pust` |
| 1274 | 26 | `eiendomsnotering` · `i arkiveringskurven din` · `på trappen der den morges` | "property record" · "refile basket" · "that morning" | term drift (Ch22 `eiendomsdokument`; settled `kurven for gjeninnplassering`) · grammar | fixed all three |
| 1280 | 26 | `så trette til døds av å bære på det` | "tired half to death" | garbled | `halvt dødstrette` |
| 148 | 2 | `Noe som etterlot det andre.` | "Which left the other." | calque | `Da gjensto bare det andre.` |
| 95 | 1 | `for nøyaktig å spørre om det` | "to ask about exactly that" | misplaced adverb | `for å spørre om nettopp det` |
| 65 | 1 | `med fast stram kjeve` | "jaw set" | garbled | `med sammenbitte kjever` |
| 880 | 16 | `aldri leser de samme papirene` | "the very papers" | sense | `nettopp de papirene` |
| 1092 | 21 | `…støvelen min, Emmas vottekledde hånd fant min` | — | comma splice | `mens Emmas…` |
| 799, 809, 823, 827 ×2 | 14 | `… – Hun skjøv bollene` · `– Han dro,` · `– Jeg så Prancer` · `– Han sukket.` · `– Han luntet` | narration after speech | **dialogue system**: a turn dash in front of narration | dash removed (book-wide grep: only Ch14 had it) |
| 253 | 4 | `Blackburns en gang eide` | "the Blackburns" | name-form drift | `Blackburn-familien` |
| 270 | 4 | `kassene` | "the boxes" | term drift (`eskene`) | `eskene` |
| 313 | 5 | `kommet på villspor` | "gone astray" (Ch4 `på avveie`) | term drift | `på avveie` |
| 379 | 6 | `et gresskar som hadde fornærmet ham` | "a gourd" | term (`pyntegresskar`) | `et pyntegresskar` |
| 417 | 6 | `blant alle esker og kasser` | "among his boxes" | addition | `blant eskene sine` |
| 461 | 8 | `gnistfangeren` | "the fire screen" (Ch1 `peisskjerm`) | term drift | `peisskjermen` |
| 893, 913, 919 | 17 | `jernbeslagene` / `beslagene` | "(porch/iron) brackets" (Ch1/Ch8 `verandabrakettene`) | term drift | `jernbrakettene` / `brakettene` |
| 30, 737 | blurb, 12 | `cardiganen` | (edition: `kardigan` ×2) | spelling drift | `kardiganen` |
| 652 ×2 | 11 | `Foajéen` / `foajéen` | (edition: `foajeen`) | spelling drift | `foajeen` |
| 950, 1038, 1066 | 18, 20 | `gikk sin veg` | (edition spells `vei`) | spelling drift | `vei` (1066 is italic, kept italic) |
| 1311 | 27 | `på den nederste trappen` | "bottom step" | word choice | `det nederste trinnet` |
| 1636 | excerpt | `hadde de snudd seg mot veien` | "they'd **faced** the road" (the turning is the clue) | sense | `hadde de stått vendt mot veien` |
| 1638 | excerpt | `I morges hadde den i midten…` | "This morning" (past narration) | deixis | `Denne morgenen` |
| 1655 | excerpt | `som et fotavtrykk i min egen trapp` | "a footstep on my own stair" | sense (sound, not print) | `som skritt i min egen trapp` |

## Regressions introduced by the first pass
| Para | Ch | Raw | Corrected (before) | Problem | Fix |
|---|---|---|---|---|---|
| 863 | 15 | `hang hyssingen over disken og seg i midten` | `Ved femtiden seg hyssingen over disken ned på midten` | the rewrite left the typo *seg* for *seig* (sagged) | `seig` ✔ |

## Clue chain — traced end to end
Unchanged from the targeted report and re-confirmed in the full read: note/letters/cards three separate words; `safiren i hjertet` identical ×9; `tre ord` correct; Sam owed; deed ≠ Blackburn papers; reveal logic Ch22 [1116]–[1124] / Ch23 [1157]–[1161] / Ch26 [1274] reads as the English two-halves deduction.

## Excerpt (Flour Play Ch1)
Audited against Inn Trouble's own English (war memorial, weekend, overnight, bandstand all present as in IT EN; chocolate-pecan ✓; "Very nearly" → `Nesten.` ✓; snowmen question ✓). Three meaning fixes ([1636] [1638] [1655]). Separate-translation vs FP NO wording = PC-FIL2-1 / PC-NO2-2 class, not re-raised. PC-NO2-3 (Dot's split line [1648]–[1649]) logged, not re-raised.

## Decisions / refusals
- **New decisions:** 0 questions for Lisa (one-answer fixes only). Section added to `PROOFCHECK_DECISIONS.md` for the record.
- **Open items re-checked:** NO2-D1 (circle `syklubben` vs Book 1 `sirkelen`) still open, quote still accurate. PC-NO2-1/2/3 unchanged.
- **Refusals:** 0.

## Four checks
- **looks_english:** [] (empty).
- **bt_anchors check:** 8 spans, 0 unpaired; only Inn Trouble / Frost and Found / Flour Play.
- **check_matter:** 1 PASS, 0 FAIL.
- **preflight --verify:** "source or corrected copy missing" (raw is in `_superseded/`). Verified by hand vs the backup: 1664 → 1664 paragraphs; 55 paragraphs changed; 29 italic runs, same order (text changed inside 2 italic runs, [116] and [1066], formatting kept); 8 `<bt>` spans unchanged; 3 `* * *` unchanged.

## Verdict: **SIGNIFICANT**
- Missed reversed meanings in Jessica's reasoning (Ch24 [1192] "Theo slipper aldri å bli…" = the opposite of the English) and Ch8 [469]/Ch10 [645]; a seriously wrong connotation in Ch27 [1291] (`forgrepet seg på` = sexual abuse) for "wronged"; and the note's own wording dropped "your" ([116]).
- Rate: 61 edits / 31 chapters ≈ 2.0 real defects per chapter read (most minor wording/term drift).
