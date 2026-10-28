# PROOFCHECK (FULL) — Inn Trouble - ASSEMBLED - FORMATTED_Czech (2026-10-28, cloud)

- **Mode:** full. No sub-agents. Read with python-docx, EN paragraph next to its CZ paragraph(s), in order.
- **Read in full, sentence by sentence:** front matter, blurb, **all 31 chapters** (Ch1 → Ch31, including the chapters the targeted pass had already read), the sell lines, What's Next and the Flour Play excerpt [1471]–[1565], and the closing line. The chapters align 1:1 (Ch1 −1 = the EN [79]/[80] fusion at [54], already logged as IT-CS-6).
- **Backup before the first write:** `_proofcheck_backups/Inn Trouble - ASSEMBLED - FORMATTED_Czech.20261028-231812.full.docx`.
- **Skipped, per the run override:**
  - step 2's diff audit and the 20-row ledger sample (both done by today's targeted pass);
  - step 1 — all ten flag sections (A–J) were already judged in the targeted report, and the re-run shows the same counts: A–G = 0, I = 0, H = 8 (all false), J = 2 (both real and handled).
- **Edits:** 46, in 44 paragraphs. 44 were missed by the first pass (2 of those refine wording that the targeted pass had set). 2 were first-pass regressions. There were 0 refusals.

## Missed by the first pass (all applied)
| Para | Ch | Czech (before) | Class / English | Fix |
|---|---|---|---|---|
| 37 | Ch1 | `o chlup víc, než bylo zdrávo,` | mistranslation: 'a shade past golden' (not 'more than was healthy') | `o chlup déle než do zlatova,` ✔ |
| 37 | Ch1 | `takhle peklá.` | typo: peklá → pekla | `takhle pekla.` ✔ |
| 38 | Ch1 | `pod mísu kostkovanou utěrku` | mistranslation: cloth AROUND the dish | `kolem mísy kostkovanou utěrku` ✔ |
| 40 | Ch1 | `pohněte sebou` | address: Pip → Jessica informal (plural/formal imperative) | `pohni sebou` ✔ |
| 52 | Ch1 | `„Vždycky musela,“` | mistranslation: 'I should always have' (was 'she always had to') | `„Vždycky bych měla,“` ✔ |
| 53 | Ch1 | `láhev s horkou vodou` | calque: hot water bottle = termofor | `termofor` ✔ |
| 70 | Ch1 | `sádcový medailon` | typo (sádcový; sádrový elsewhere) | `sádrový medailon` ✔ |
| 85 | Ch1 | `se na okamžik zdála být` | agreement: to znepokojivé … zdálo | `se na okamžik zdálo být` ✔ |
| 130 | Ch2 | `Byl na tom hůř.` | mistranslation: 'the worse of the two' (was 'in worse shape') | `Byl horší z těch dvou.` ✔ |
| 132 | Ch2 | `abych věděl, že peníze jsou tam.` | spoiler-gender: the note's 'so I'll know' was masculine (abych věděl); EN neutral → present 'ať vím' | `ať vím, že peníze jsou tam.` ✔ |
| 172 | Ch2 | `Buď se ti do toho kufru nějak podařilo vniknout,` | who-did-what: 'ti … podařilo' = YOU managed; EN 'they have been into your trunk' | `Buď se jim nějak podařilo dostat se do tvého kufru,` ✔ |
| 200 | Ch2 | `festivalová světla podél střech` | term: eaves = okapy (Ch1 ×2) | `festivalová světla podél okapů` ✔ |
| 316 | Ch4 | `přičemž se jedním prstem skla sotva dotkl` | mistranslation: 'one finger not quite touching the glass' (was 'barely touched') | `přičemž se prstem skla tak docela nedotkl` ✔ |
| 324 | Ch4 | `o věcech, které lidé nedokázali unést a vyhodit` | mistranslation: 'the things people couldn't bear to throw away' | `o věcech, které lidé neměli srdce vyhodit` ✔ |
| 340 | Ch4 | `napsaná žádost o půl milionu dolarů` | word choice: demand ≠ request (žádost) | `napsaný požadavek půl milionu dolarů` ✔ |
| 359 | Ch5 | `Probíraly festivalové palčáky, palčáky se jmény na manžetách,` | mistranslation: 'were on the mittens' = working on them (was 'discussing') | `Pracovaly na festivalových palčácích, palčácích se jmény na manžetách,` ✔ |
| 369 | Ch5 | `Přehmátla si očko.` | mistranslation: 'She picked a stitch' | `Nabrala očko.` ✔ |
| 383 | Ch5 | `kvůli tomu Redfernovic klukovi` | gender: the Redfern child is Emma (a girl, Book 1) | `kvůli té Redfernovic holčičce` ✔ |
| 386 | Ch5 | `Byla to Martha Green,` | name form: Martha Greenová (Book 1 CZ ×3; edition declines surnames) | `Byla to Martha Greenová,` ✔ |
| 427 | Ch6 | `tykví, která se ho dotkla.` | ambiguity: 'a gourd that had offended him' (dotkla = touched) | `tykví, která ho urazila.` ✔ |
| 463 | Ch6 | `Měla bych mít obavy a malá` | tense: 'I should have been worried' (past narration) | `Měla jsem mít obavy a malá` ✔ |
| 490 | Ch7 | `Ať už se stalo cokoliv jiného,` | tense/sense: 'Whatever else happened' = whatever might happen (was 'whatever had happened') | `Ať už se stane cokoliv jiného,` ✔ |
| 542 | Ch8 | `a to poděkování patřilo mnohem víc než jen za tu věc.` | grammar: broken construction (patřilo … za) | `a to poděkování nebylo jen za ten držák.` ✔ |
| 578 | Ch10 | `mistr přesunuté dílny` | term: foreman = předák (settled; Bram says 'Dělám předáka' [590]) | `předák přesunuté dílny` ✔ |
| 631 | Ch11 | `Udělala jsem pro Společnost, co bylo v mých silách.` | sense: 'I made the case for the Society' (the following 'O střeše…' list needs a speech verb) | `Přimlouvala jsem se za Společnost, jak nejlépe jsem uměla.` ✔ |
| 668 | Ch12 | `a paní Clausová tu byla dnes ráno znovu, a říká` | mistranslation: 'Mrs. Claus here went again this morning' (to the mayor), not 'was here' | `a paní Clausová, která tu sedí, za ním byla dnes ráno znovu, a on říká` ✔ |
| 699 | Ch13 | `Úsměv vydržel, ale stálo ho to nějakou námahu. — Pomalu, — připustil. — Banka na té půjčce sedí. Už třetí měsíc. Pokaždé, když si …` | dialogue system: leftover dash-turn paragraph converted to „…“ (ruling 1); 'tu ležím' → 'ležím' | `Úsměv vydržel, ale stálo ho to nějakou námahu. „Pomalu,“ připustil. „Banka na té půjčce sedí. Už třetí měsíc. Pokaždé, když si mys…` ✔ |
| 705 | Ch13 | `Jeho odpovědí bylo, že celou noc střežil městský festival za honorář a učil babičky` | tense/sense: his plan (to stand guard / teach), not already done | `Jeho odpovědí bylo, že bude celou noc za honorář střežit městský festival a učit babičky` ✔ |
| 754 | Ch14 | `— Nic na téhle návsi není ani zdaleka tak teplé jako doma, — řekla jsem tiše, jen pro ni. — Jestli chceš teplo, běž domů. Běž se podívat.` | dialogue system: leftover dash-turn paragraph converted to „…“ (ruling 1) | `„Nic na téhle návsi není ani zdaleka tak teplé jako doma,“ řekla jsem tiše, jen pro ni. „Jestli chceš teplo, běž domů. Běž se podívat.“` ✔ |
| 768 | Ch14 | `je něco hřejivého.` | comparative dropped: 'something warmer up the lane' | `je něco hřejivějšího.` ✔ |
| 833 | Ch16 | `jinak to on nebyl.` | spoiler-gender: EN 'or it wasn't them' (neutral) had 'on' (he); now plural, matching 'Mohli … věděli' | `jinak to nebyli oni.` ✔ |
| 909 | Ch18 | `tím, za co se ti vydával.` | nuance: 'exactly what he told you he is' (vydával = passed himself off as, implies pretence — the point is that he was honest) | `tím, co ti o sobě řekl.` ✔ |
| 978 | Ch19 | `vymalované červenou tužkou` | word choice: 'in red pencil' (vymalované = painted) | `napsané červenou tužkou` ✔ |
| 996 | Ch19 | `„Krb,“ pronesla jsem` | term: hearth = ohniště (Nick's word in Ch10 'Ohniště', Ch14, and [994] here) | `„Ohniště,“ pronesla jsem` ✔ |
| 998 | Ch19 | `„Krb.“ Jeho paže mě objala kolem ramene. „Ještě není hotový.` | term: hearth = ohniště (echo of Ch10), agreement adjusted | `„Ohniště.“ Jeho paže mě objala kolem ramene. „Ještě není hotové.` ✔ |
| 1045 | Ch20 | `číma rukama` | grammar: instrumental of čí = čími | `čími rukama` ✔ |
| 1101 | Ch22 | `dopisní papír. Měl krádež. Ale` | clue chain/idiom: 'He had the theft' rendered by sense (the literal 'Měl krádež' reads oddly and can be heard as 'he had/committed a theft'; run lesson) | `dopisní papír. Měl tajemství krádeže. Ale` ✔ |
| 1136 | Ch23 | `Theo měl krádež. Našel ji` | clue chain/idiom: 'Theo had the theft' = he knew that half (run lesson: render the sense, not 'Theo měl krádež') | `Theo věděl o krádeži. Našel ji` ✔ |
| 1222 | Ch25 | `podívat do tváře příteli, kterého se pokusil zranit` | gender: 'the friend he tried to hurt' is Fiona (was masculine příteli, kterého) | `podívat do tváře přítelkyni, kterou se pokusil zranit` ✔ |
| 1247 | Ch26 | `a byl tam, půl milionu dolarů, jen tak ležel v minulosti,` | agreement: 'půl milionu' takes neuter singular (was masc byl/ležel) | `a bylo to tam, půl milionu dolarů, jen tak to leželo v minulosti,` ✔ |
| 1253 | Ch26 | `„Vero,“ řekla jsem. „Theo měl krádež. Ale` | clue chain/idiom: 'Theo had the theft' by sense (= Ch23 [1136]) | `„Vero,“ řekla jsem. „Theo věděl o krádeži. Ale` ✔ |
| 1253 | Ch26 | `„On měl krádež. Vy jste měla listinu.` | two-halves line by sense: 'He had the theft. You had the deed.' (= Ch22 [1101] 'Měl tajemství krádeže') | `„On měl tajemství krádeže. Vy jste měla listinu.` ✔ |
| 1349 | Ch29 | `se ten kabát rozseděl.` | idiom: 'the coat had broken in' (rozseděl = sat itself loose; meaningless for a coat) | `mi ten kabát konečně padl jako ulitý.` ✔ |
| 1409 | Ch31 | `„Počkej,“ řekla. „Nechoď pryč.“` | address: Emma → Jessica formal (ruling 2; Emma is vy everywhere else: [447] [453] [457]) | `„Počkejte,“ řekla. „Nechoďte pryč.“` ✔ |

## Regressions introduced by the first pass (applied)
Both come from the excerpt rebuild, which copied corrected Flour Play CZ Ch1 over raw text that had been right.
- [1545]: the raw had `otočil úplně dozadu`.
- [1521]: the raw had `drobné zprávy celého dopoledne`.

| Para | Ch | Czech (before) | Class / English | Fix |
|---|---|---|---|---|
| 1521 | Excerpt | `drobná dopolední novinka vměstnaná do prostor mezi` | mistranslation: 'a whole morning's small news' (was a single 'novinka'); inherited from FP CZ [90] | `drobné novinky celého dopoledne vměstnané do mezer mezi` ✔ |
| 1545 | Excerpt | `otočený úplně dokola.` | mistranslation: 'turned clean around' = faced the other way (dokola = a full circle, i.e. facing the same way again); inherited from FP CZ [114] | `otočený čelem vzad.` ✔ |

## Worst finds
- **[172] Ch2 — who-did-what reversal in the plot set-up.**
  - Before: `Buď se ti do toho kufru nějak podařilo vniknout`. That says *you* (Fiona) managed to break into the trunk.
  - English: "Either they have somehow been into your trunk".
  - This is the first half of the two-sources deduction.
- **[132] Ch2 — spoiler-gender in the note itself.**
  - Before: `abych věděl, že peníze jsou tam`. This is a masculine first-person "so I'll know" in the blackmail note, which the English keeps neutral.
  - After: `ať vím`, which is neutral. The italic run was kept.
- **[833] Ch16 — spoiler-gender.**
  - Before: `jinak to on nebyl` ("he"). English: "or it wasn't them".
  - After: `jinak to nebyli oni`.
- **[52] Ch1 — reversed line.**
  - Before: `„Vždycky musela,“` ("she always had to"). English: "I should always have".
- **[699] Ch13 and [754] Ch14 — two leftover dash-turn dialogue paragraphs** (`— Pomalu, — připustil.`).
  - The first pass converted Ch13–14 but missed these two.
  - The I-flag cannot see them, because each paragraph opens with narration.
- **[1101] / [1136] / [1253] "Theo had the theft".** These now render the sense, per the run lesson. Logged as PC-CS-F1.
  - [1101]: `Měl tajemství krádeže.`
  - [1136]: `Theo věděl o krádeži.`
  - [1253]: `Theo věděl o krádeži.` … `On měl tajemství krádeže. Vy jste měla listinu.`
  - The bare `Theo měl krádež` reads oddly in Czech and can be heard as "had a theft (done)".
- **[1545] excerpt (regression).**
  - `otočený úplně dokola` means turned a full circle, so the snowman would face the road again and the clue would be undone.
  - The phrase came from FP CZ [114]. Logged as PC-CS-F2.

## Run lessons checked explicitly
- **Ch26 "Theo had the theft":** fixed by sense in Ch22, Ch23 and Ch26 (see above). Constance is the thief everywhere: [148], [1212], [1331].
- **Ch19 "It's the love that lets him, Jess":** [980] `Právě láska mu to umožňuje` ✔. The pronoun is not reversed.
- **Ch27 "ruined himself":** [1298] `zničil u toho sám sebe` ✔.
- **Excerpt:**
  - No half-paragraph was dropped: E971–973 = [1543]–[1547], 1:1.
  - The snowmen question [1541] is correct. The pecans are `čokoládovo-pekanových`.
  - The war memorial, the overnight snow and the weekend are in this English, so they are correct here.
  - "Very nearly" = `Skoro.` ✔
- **Settled terms grepped for broken forms:**
  - clue phrase ×9, identical;
  - "four words" ×5, true;
  - `pět slov` 0; `ohrad` 0; `výběh` 10/10;
  - `Sněhulák` / `Snížek` 0;
  - `kroužek` (the 7 `kruh` are ordinary circles);
  - `lístek` is used only for the card, the pawn receipt [158] and holly leaves [1411]; 75 `vzkaz`; no note called `dopis`.
- **Ch19 card / note sentences:** [956] `své sestře` ✔; [962] `jejž lístek shrnoval` ✔; [964] `A ten lístek byl psán Theovou rukou.` ✔
- **"Blackburn papers" vs deed:** the papers are `dokumenty` [213] [227] and `písemnosti` [713] [855] [863] [1097]. The deed is `listina` everywhere. They are never the same word.
- **"your man" [909]:** `ten tvůj chlapík` ✔.
- **Theo and Max:** [826] "six letters" kept, faithful to the EN slip (PC-NL2F-2), and not re-logged.

## Spoiler-gender sweep (every unknown-culprit reference, Ch2–Ch25)
- **Fixed:** [132] (the note's own `věděl`) and [833] (`on`).
- **Left as they are:**
  - Generic `někdo / kdokoli / ten, kdo … napsal / četl / ho`: [229] [281] [354] [962] [1049] [1095]. In Czech, `někdo` and `kdokoli` take grammatical masculine agreement, and that is the neutral form. A Czech reader does not take it as "a man". It also points away from Vera, so it gives nothing away. There is no neutral alternative short of rewriting the sentences.
  - `vyděrač`: the generic noun.
- **Where the English itself says "he/his" for the blackmailer:** Ch9 [565], Ch16 [851], Ch20 [1021] [1027] [1047], Ch21 [1073]. Faithful.
- **Feminine forms:** none appear before the reveal. `postava` in [1063] is the grammatical gender of "figure", and the figure turns out to be Mrs. Pelletier.

## Open decisions re-checked
- IT-CS-1…8 and PC-CS-1: the quotes are still accurate, and nothing contradicts a ruling.
- Emma → Jessica is now **vy** in Ch31 [1409] too (ruling 2; the first-pass table says "children → adults formal").
- IT-CS-4 (Theo ↔ Jessica ty) is untouched.

## Decisions added
- PC-CS-F1 (theft wording, applied, informational).
- PC-CS-F2 (FP CZ follow-up: Ch1 [114] `dokola` and [90] `drobná dopolední novinka`, both fixed in IT; not applied to FP).

## Checks (after fixes)
1. **looks_english:** `[]`
2. **bt_anchors check:** 8 spans, 0 unpaired. Only Inn Trouble, Frost and Found and Flour Play.
3. **check_matter:** 1 PASS, 0 FAIL.
4. **preflight --verify (raw → corrected):**
   - Paragraphs 1570 → 1570 ok; scene breaks 3 → 3 ok.
   - The italic / bt "FAIL" is the first pass's declared changes, unchanged from before this pass.
   - My own comparison of the backup against the corrected file:
     - 1570 = 1570 paragraphs.
     - 21 = 21 italic runs, in order. The only italic text changed is the note [132] (`abych věděl` → `ať vím`).
     - 8 = 8 `<bt>`; 3 = 3 scene breaks.
     - Changed paragraphs: exactly the 44 listed.
- **proofcheck.py re-run:** A=0 B=0 C=0 D=0 E=0 F=0 G=0 H=8 I=0 J=2. These are unchanged; the flags are all judged, and none was touched.

## Verdict
**SIGNIFICANT.** The targeted pass and the first pass both missed these defects:
- a who-did-what reversal in the Ch2 two-sources set-up [172];
- a masculine first person inside the blackmail note [132] and a "he" for the unknown culprit [833];
- a reversed line [52];
- two un-converted dialogue paragraphs;
- two excerpt regressions, one of which turns the snowman clue back to the road [1545].

All are fixed. That is 46 defects in 44 paragraphs over 31 chapters + front matter + back matter, ≈ **1.4 per chapter**. The plot chain (clue phrase, note / card / letters, deed vs papers, theft vs deed) is now clean end to end.
