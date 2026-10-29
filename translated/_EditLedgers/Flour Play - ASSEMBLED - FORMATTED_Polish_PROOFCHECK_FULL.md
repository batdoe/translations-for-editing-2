# PROOFCHECK (FULL) — Flour Play - ASSEMBLED - FORMATTED_Polish (2026-10-29, cloud)

- **Mode:** FULL. No sub-agents. Every section read sentence by sentence with python-docx, EN paragraph next to its PL paragraph(s), one chapter at a time: front matter + blurb [0]–[37], **Ch1 → Ch27 (all 27)**, closing scenes, sell lines, What's Next [1985]–[1997]. *The Binder's Bequest* excerpt [1998]–[2048] is the published Polish text (FP-PL-8) — spot-read only (no English, no debris).
- **Backup:** `_proofcheck_backups/Flour Play - ASSEMBLED - FORMATTED_Polish.20261029-004317.full.docx`
- **Skipped per brief:** step 2 full diff audit and the 20-row ledger sample (done in today's targeted pass). Flags: the targeted report already judged all of them (B×5, H×8, I×1 = false positives); unchanged after this pass (A0 B5 C0 D0 E0 F0 G0 H8 I1 J0).
- **Edits:** 205 in 177 paragraphs. 0 refusals (one multi-run match was refused once, then applied as two single-run edits). Paragraphs 2049 = 2049.
- **PC-PL-ITF-2 applied:** [77] and [110] miasto → miasteczko, [124] „rząd bałwanów”, blurb [35] masculine „ktokolwiek to zrobił, kupił… znał… złożył” → neutral „tu proszek kupiono, dawkę znano, a w złożonej skardze powołano się…”.

## Spoiler-gender check (culprit = Joyce, a woman)
Every pre-reveal reference to the unknown wrongdoer/figure was checked (Ch2–Ch21). Policy (same as the Inn Trouble PL full read): `ktoś/ktokolwiek/ten, kto` + masculine past is the grammatical default and gives nothing away, so it stays; explicit gendered forms the English lacks were neutralised. Fixed:
- **[1111] Ch17 Danny's figure** — bare feminine „Stała… ruszyła… Nigdzie nie weszła. Zgubiłem ją” (reads "SHE stood… she went") → neuter „To stało… ruszyło… weszło… Zgubiłem to” (EN "it"; mirrors Ch13 „przeganiał pan to”). The figure, not Danny, passes the pharmacy light ✓.
- **[701] Ch9** bare feminine „Zacytowała podpunkty.” (subject = the complaint, but read as "she cited") → „Skarga cytowała podpunkty.” (italic run kept).
- **[783] Ch10** „…że zmarzł… że chciał… Ten celuje” → ungendered present „marznie… chce… Ta dłoń celuje”.
- **[1014] Ch15** generic "you" rendered feminine „wiedziałaś… byłaś tą, która je przyniosła” → impersonal „się wiedziało… samemu się je sprowadzało”.
- **[35] blurb** (PC-PL-ITF-2, above).
- Logged, not changed: **[899] Ch13** Pete's figure is masculine („Dorosły człowiek… Wiedział… zniknął”) → PC-FPPL-F1.

## Clue chain (re-traced after the edits)
| Term | Result |
|---|---|
| sour base | `kwaśna baza` ×18 in every case form; zakwas/zaczyn only in Doc's "sourdough tang without the starter" [813] ✓ |
| walk-in vs cold room | `chłodnia` vs Joyce's `zimny pokój` (×8 in the slip lines) — never merged; Ch18 [1199] generic "a cold room at midnight" = EN's own phrase ✓ |
| ten times / rye | „Dziesięć razy tyle…” [813], „dziesięciokrotnie” [815] ✓ |
| Greta's nose | „Nic, co potrafię nazwać” [805] ✓ |
| two degrees below | „o dwa stopnie poniżej normy” ×3, identical ✓ |
| order book | `zeszyt (zamówień)` ×18; księga only = account books ✓ |
| gate key / lock | [1386] „Nigdy jej nie zmieniałam”, [1605] „Nigdy jej nie zmieniłaś” = the lock ✓; [1597] „Drugi dorobiłam dla ciebie” ✓ |
| poison | none (trując = wpatrując/zaopatrujący) ✓ |
| Pip | she/her; fixed [801] „pingwinem, który poszedł” and [1935] „ty mały żebraku” |
| numbers | 65 [1692], 25 yrs / 15 together, „do dwudziestego” ✓ |
| DIRTY / Grange / Snowball | BRUDNE ×8 · świetlica ×15 · Snowball ×9 ✓ |
| gold shop | Dot's "the gold shop" [974] was „sklep ze złotem” (= a shop selling gold) → „złoty sklep” as in Ch19 [1257] |
| capsule cards / founder's line | [1000] = [1846]/[1884], [507] = [1873] identical ✓ |
| Binder's Bequest anchors | 9 spans kept; closing CTA still missing (FP-PL-6) |
| FP-lesson lines | Ch13 temper = „temperament/usposobienie” ✓ · Ch17 figure passes the light ✓ · Ch19 Danny never named the gold shop ✓ · printer's „próbny wydruk” ✓ · Ch23 lock ✓ · Ch24 „przyjęła zeznanie Danny'ego” ✓ · Ch1 „o połowę większy” ✓ · bakery box „z piekarni” ✓ · Ch25 [1785] Greta = the woman Joyce tried to rob ✓ · Ch22 speaker turns intact ✓ |

## Missed by the first pass (and by the targeted pass) — the material ones
| Para | Ch | Polish (before) | English | Class |
|---|---|---|---|---|
| 1111 | 17 | `Stała… ruszyła… Nigdzie nie weszła. Zgubiłem ją` | "It stood… it went… I lost it" | **Spoiler-gender** |
| 701 | 9 | `Zacytowała podpunkty.` | "It named the sub-clauses." | **Spoiler-gender** |
| 517 | 6 | `w przednim oknie, któremu Towarzystwo przyznało honorowe miejsce` | "where the Society had given IT the place of honor" | **Reversed** (window got the honour, not the capsule) |
| 543 | 6 | `…i nie odpłaciła jej tym samym` | "…and not have hers in return" | **Reversed who-repays-whom** |
| 556 | 7 | `to samo, na które wychodziła mąka Grety` | "the same yard as Greta's flour [came in through]" | Reversed direction |
| 554 | 7 | `zanim zamknęli` | "before he shut" (Pete) | Wrong subject |
| 1059 | 16 | `…niż kiedykolwiek dało się gdziekolwiek zarobić… ten jeden stary sklep z wypiekami` | "more sweet trade… than it's ever had anywhere to spend… the one old bakery" | Mistranslation + bakery word |
| 1802 | 25 | `co do centa za to, co zmarnowała` | "what she spoiled" (Joyce) | Pronoun reference (read as Greta) |
| 923 | 14 | `nazwisko sprawcy, który napisał coś… Tym chłopakiem był Danny Ott` | "A name was going around…" | States Danny's guilt as fact |
| 1041 / 1493 | 16 / 22 | past `zrobiłam… Przyjrzałam się` / `Sprawa trafiła` | "I'd do…" / "it would go to the law" | Tense: a plan narrated as done |
| 1836 | 26 | `z kolanami oblepionymi bibułą` | "the blotting-work on his knees" | Mistranslation |
| 668 | 8 | `Sprawiłeś, że cała reszta wzdycha w górę alei` | "You've got all the others mooning up the lane" | Wrong place + causation |
| 422 | 5 | `poduszka została podbita` | "it [the nest] had been plumped" | Invented object |
| 974 | 14 | `w sklepie ze złotem` | "at the gold shop" | Term (clue word) |
| 309… | 4 | `szalunek` ×5 | "clapboard" | Wrong word (concrete formwork); = blurb's `szalówka` |
| 657 / 661 | 8 | `pieca kaflowego` / `w zagrodzie` | "woodstove" / "paddock" | Series terms → `kozy` / `na wybiegu` (corrected Inn Trouble PL) |
- Plus, book-wide: `miasto` for Frost Falls → `miasteczko` (36 edits); `wianek/wianuszek` → `wieniec` (11); nominative `Jessica` used as vocative → `Jessico` (18); ~60 agreement/case/aspect/calque fixes (full list below).

## Regressions introduced by earlier passes
| Para | Ch | Raw | Corrected (before) | Fix |
|---|---|---|---|---|
| 1847 | 26 | `stare pudełko… go… Jego` | `bezpieczne… stara skrzynka… go… Jego` (noun swapped, agreement not) | `bezpieczna… jej… Jej` |
| 545 | 6 | `przyciągną` | `przyciągnie` (subject = słowa, pl.) | `przyciągną` |
| 951 | 14 | `Twój Danny` | `Pani Danny` (reads "Mrs Danny") | `Pani syn, Danny,` |

## Ledger mismatches
Not re-sampled (done today in targeted mode: 0 real mismatches).

## Decisions added (PROOFCHECK_DECISIONS.md, section "— FULL PROOFCHECK (2026-10-29)")
- PC-FPPL-F1 — Ch13 [899] masculine figure (rec. keep).
- PC-FPPL-F2 — Inn Trouble PL follow-ups (excerpt [65] [142], blurb [31] [35]).

## Re-checked open items
PC-FPPL-1 (pie „orzechowy” ×11) left as instructed; PC-FPPL-3 (Ch1 [87]/[88] split) unchanged; FP-PL-6 CTA still missing; FP-PL-1/2/3/5/7 quotes still accurate.

## Checks after the fixes
- looks_english: `[]`
- bt_anchors check: 9 spans (Flour Play, Frost and Found, Inn Trouble, The Binder's Bequest), 0 unpaired
- check_matter: 1 PASS, 0 FAIL
- preflight --verify: "source or corrected copy missing" (raw is in `_superseded/`); vs my backup: paragraphs 2049 = 2049, italic runs 46 = 46 (only change: text inside the [701] italic run), `<bt>` 9 = 9, scene breaks 60 = 60, 177 paragraphs changed
- proofcheck re-run: A0 B5 C0 D0 E0 F0 G0 H8 I1 J0 (unchanged; all false positives, none of the defects was flaggable)

## Verdict
**SIGNIFICANT** — two spoiler-gender giveaways (Ch9, Ch17), two reversed-meaning lines (Ch6 ×2), a wrong-direction/wrong-subject pair in Ch7, a mistranslated Renée speech (Ch16) and a pronoun slip that made Greta the spoiler (Ch25) survived both earlier passes. All fixed. Rate: 205 edits in 29 sections read (front, 27 chapters, back) ≈ 7 per section; ≈ 25 material (meaning/plot) defects ≈ 0.9 per section, the rest consistency/grammar.

## Full edit list
| Para | Ch | Polish (before) | Polish (now) | Class |
|---|---|---|---|---|
| 31 | blurb | `Pożyczona waga. Wciąż kwaśne.` | `Pożyczona waga. Wciąż kwaśna.` | blurb agreement: 'still sour' = the roll (fem.) |
| 35 | blurb | `ponieważ ktokolwiek to zrobił, kupił proszek, znał dawkę i złożył skargę powołującą się na odpowiedni podpunkt przepisów sanitarnych.` | `ponieważ tu proszek kupiono, dawkę znano, a w złożonej skardze powołano się na odpowiedni podpunkt przepisów sanitarnych.` | PC-PL-ITF-2 spoiler-gender: masculine 'whoever did this' -> neutral impersonal |
| 65 | 1 | `w gnieździe uknutym z upadłego motka` | `w gnieździe uwitym ze spadłego motka` | wrong word: uknuty = plotted; nest = uwity; fallen skein = spadły |
| 77 | 1 | `jak miasto bywa życzliwe wobec gościa` | `jak miasteczko bywa życzliwe wobec gościa` | PC-PL-ITF-2 town = miasteczko |
| 110 | 1 | `żeby miasto ci się gapiło na ręce` | `żeby miasteczko ci się gapiło na ręce` | PC-PL-ITF-2 town = miasteczko |
| 124 | 1 | `zbudowali wzdłuż niego rzędami bałwany` | `zbudowali wzdłuż niego rząd bałwanów` | PC-PL-ITF-2 a row of snowmen |
| 142 | 1 | `Inaczej mówiąc, wciąż wałęsała się nocami` | `Wciąż wałęsała się nocami` | addition: 'In other words' not in EN |
| 178 | 2 | `bo przecież Greta nikomu nie słuchała rozkazów` | `bo przecież Greta od nikogo nie przyjmowała rozkazów` | grammar (słuchać + dat. wrong) |
| 182 | 2 | `jedną ręką powiązaną za plecami` | `jedną ręką związaną za plecami` | wrong word: powiązany = linked |
| 182 | 2 | `Święto Dziękczynienia, a ja nie potrafię upiec` | `Święto Dziękczynienia, nie potrafię upiec` | fragment sentence |
| 182 | 2 | `i wyszło to co tam.` | `i wyszło to, co widzisz.` | garbled |
| 186 | 2 | `biegam jak w kółko` | `kręcę się w kółko` | idiom (chasing my tail) |
| 194 | 2 | `Ale tu mieliśmy bułki, pączki i chleb` | `Ale tu chodziło o bułki, pączki i chleb` | masc. plural 'mieliśmy' for two women |
| 221 | 3 | `wieczorem, kiedy odbywało się wiązanie wianuszków` | `wieczorem tego dnia, kiedy krąg wiązał wieńce` | term drift wreath = wieniec |
| 225 | 3 | `Pâtisserie, Jessica. Nie piekarnia.` | `Pâtisserie, Jessico. Nie piekarnia.` | vocative |
| 227 | 3 | `zupełnie niepodobna do wianuszków, które robiłyśmy` | `zupełnie niepodobna do wieńców, które robiłyśmy` | term drift wreath = wieniec |
| 248 | 3 | `a w tym samym tchu, bez żadnej mojej prośby` | `a zarazem, bez żadnej mojej prośby` | calque |
| 250 | 3 | `a Hal Thompson opierał się o nią, nachylając się wspólnie nad kartką papieru` | `a Hal Thompson opierał się o nią; oboje nachylali się nad kartką papieru` | EN 'the two of them with their heads together' (participle had Hal alone) |
| 260 | 3 | `Dla niektórych ludzi w tym mieście długa zima oznacza coś więcej niż miły ogień w kominku i wianek na drzwiach.` | `Dla niektórych ludzi w tym miasteczku długa zima oznacza coś więcej niż miły ogień w kominku i wieniec na drzwiach.` | town = miasteczko; wreath = wieniec |
| 260 | 3 | `kolumny: artykuły spożywcze, w puszkach, ciepłe rzeczy` | `kolumny: produkty suche, konserwy, ciepłe rzeczy` | dry goods / canned |
| 262 | 3 | `— Pomagasz więc?` | `— Pomożesz więc?` | tense (You'll help) |
| 263 | 3 | `— Miasto mogłoby tego potrzebować w tym roku.` | `— Miasteczku by się to w tym roku przydało.` | town = miasteczko; calque |
| 270 | 3 | `Holly Jolly pogrążony był w mroku.` | `Holly Jolly pogrążona była w mroku.` | gender: Holly Jolly (piekarnia) fem. elsewhere |
| 275 | 4 | `i nigdy więcej o tym nie wspominamy.` | `i nigdy więcej o tym nie wspomnimy.` | tense (we'll never speak of it) |
| 299 | 4 | `— Jessica. Zejdź do Holly Jolly.` | `— Jessico. Zejdź do Holly Jolly.` | vocative |
| 309 | 4 | `na jasnych deskach szalunku elewacji` | `na jasnych deskach szalówki elewacji` | clapboard = szalówka (szalunek = concrete formwork); matches blurb [33] |
| 317 | 4 | `w słowo BRUDNE na szalunku, który szorowała` | `w słowo BRUDNE na szalówce, którą szorowała` | clapboard = szalówka |
| 333 | 4 | `nie niszcząc farby na szalunku.` | `nie niszcząc farby na szalówce.` | clapboard = szalówka |
| 408 | 4 | `czerwonej farby z szalunku` | `czerwonej farby z szalówki` | clapboard = szalówka |
| 416 | 4 | `W samo południe szalunek był już czysty.` | `Do południa szalówka była już czysta.` | clapboard = szalówka; 'By noon' |
| 329 | 4 | `oraz swoją poręczną wiertarką` | `oraz swoją dobrą wiertarką` | his good drill |
| 331 | 4 | `zbił dziurę na równo i szczelnie zabezpieczył ją przed wiatrem` | `zabił otwór sklejką na równo i szczelnie zabezpieczył go przed wiatrem` | wrong verb: zbić = smash |
| 369 | 4 | `— Greta.` | `— Greto.` | vocative |
| 371 | 4 | `oderwała wzrok od kaloryferów` | `oderwała wzrok od kaloryfera` | one radiator |
| 394 | 4 | `— Do tej pory pomyli mu się cała trasa.` | `— Pewnie już mu się pomyliła cała trasa.` | 'by now' ≠ 'until now' |
| 404 | 4 | `— Zmuś ją do jedzenia czegoś.` | `— Zmuś ją, żeby coś zjadła.` | calque |
| 419 | 5 | `— Usiądź, Jessica.` | `— Usiądź, Jessico.` | vocative |
| 420 | 5 | `Tom zdarł farbę.` | `Tom zmył farbę.` | got the paint off (with remover) ≠ tore |
| 421 | 5 | `Zabrałam się za układanie igliwia, jedno na drugim, wszystkie zwrócone w tę samą stronę` | `Zabrałam się za układanie gałązek, jedną na drugiej, wszystkie skierowane do domu` | 'all pointing home' (Ch1 wording); igliwie uncountable |
| 422 | 5 | `stwierdziła, że poduszka została podbita pod jej nieobecność` | `stwierdziła, że pod jej nieobecność ktoś je spulchnił` | wrong referent: the nest was plumped, there is no pillow |
| 444 | 5 | `Obróciła wianek w dłoniach.` | `Obróciła wieniec w dłoniach.` | term drift wreath = wieniec |
| 453 | 5 | `zostało powiedziane i zawstydzone` | `zostało powiedziane i że się wstydzimy` | calque |
| 458 | 5 | `Obróciłam wianek.` | `Obróciłam wieniec.` | term drift wreath = wieniec |
| 461 | 5 | `Uniosłam skończony wianek` | `Uniosłam skończony wieniec` | term drift wreath = wieniec |
| 503 | 6 | `te suche kości miasta.` | `te suche kości miasteczka.` | town = miasteczko |
| 503 | 6 | `— A potem odwracasz coś na drugą stronę.` | `— A potem odwraca się coś na drugą stronę.` | address: Theo is formal with Jessica; keep the impersonal of 'Przegląda się' |
| 511 | 6 | `do czego jej zdaniem miasto miało służyć` | `do czego jej zdaniem miasteczko miało służyć` | town = miasteczko |
| 513 | 6 | `W roku, w którym miasto niemal nie przetrwało` | `W roku, w którym miasteczko niemal nie przetrwało` | town = miasteczko |
| 517 | 6 | `w przednim oknie, któremu Towarzystwo przyznało honorowe miejsce, spoczywała` | `w przednim oknie, gdzie Towarzystwo wyznaczyło jej honorowe miejsce, spoczywała` | reversed: the capsule got the place of honour, not the window |
| 525 | 6 | `Zasada, którą narzucił sobie wbrew dziękowaniu, i zamierzał` | `Zasada, którą sobie narzucił, by nie przyjmować podziękowań, i zamierzał` | garbled calque |
| 527 | 6 | `jak daleko może zawieźć człowieka jeden fałszywy krok` | `jak daleko może zaprowadzić człowieka jeden fałszywy krok` | wrong verb |
| 533 | 6 | `fotografia rysunku trafiła do Gazette — po obu stronach,` | `fotografia rysunku trafiła do Gazette — obie strony,` | 'both sides' of the drawing |
| 539 | 6 | `— Miasto o tym wie.` | `— Miasteczko o tym wie.` | town = miasteczko |
| 543 | 6 | `i nie odpłaciła jej tym samym.` | `a nie mogła liczyć, że Greta odwdzięczy się tym samym.` | reversed who-repays-whom (Greta will return the support) |
| 545 | 6 | `— Ale przyciągnie ludzi do środka` | `— Ale przyciągną ludzi do środka` | agreement: subject = słowa założycielki (pl.) |
| 554 | 7 | `późnym popołudniem, zanim zamknęli` | `późnym popołudniem, zanim zamknął` | EN 'before he shut' = Pete, not the Society |
| 556 | 7 | `zwróconym fasadą ku Parkowi od jego dalszej strony` | `zwróconym fasadą ku skwerowi od jego dalszej strony` | the green/Park = skwer (series term) |
| 556 | 7 | `to samo, na które wychodziła mąka Grety` | `to samo, przez które dowożono mąkę Grety` | mistranslation: flour came IN through the yard |
| 560 | 7 | `w mieście, w którym ma pan swój sklep` | `w miasteczku, w którym ma pan swój sklep` | town = miasteczko |
| 564 | 7 | `— Ten — rzekł Pete, poklepując łopatę.` | `— Ta — rzekł Pete, poklepując łopatę.` | agreement (łopata fem.) |
| 578 | 7 | `należą jej się przeprosiny, którą dostanie` | `należą jej się przeprosiny, które dostanie` | agreement |
| 602 | 7 | `— Miastu, które już mnie skazało?` | `— Miasteczku, które już mnie skazało?` | town = miasteczko |
| 612 | 7 | `gdy trudny temat zszedł na dalszy plan` | `gdy trudne słowa miał już za sobą` | EN 'now the hard thing was out' (said) |
| 622 | 7 | `kogoś, kogo miasto już nie lubiło` | `kogoś, kogo miasteczko już nie lubiło` | town = miasteczko |
| 633 | 8 | `gdy nowy człowiek podchodził do bloku i spojrzał` | `gdy nowy człowiek podchodził do bloku i spoglądał` | tense/aspect mix |
| 635 | 8 | `Ale miasto nie składało się z samych Halów.` | `Ale miasteczko nie składało się z samych Halów.` | town = miasteczko |
| 641 | 8 | `zaopatrujący zszokowaną armię` | `zaopatrujący zdumioną armię` | 'wondering' ≠ shocked |
| 644 | 8 | `gdzie miasto rzedniało w pola` | `gdzie miasteczko rzedniało w pola` | town = miasteczko |
| 655 | 8 | `— Miasto uznało, że to dzieci i odwilż.` | `— Miasteczko uznało, że to dzieci i odwilż.` | town = miasteczko |
| 656 | 8 | `a jednocześnie niemożliwego do potępienia` | `a jednocześnie takiego, na które nie sposób się długo gniewać` | 'impossible to stay cross about' ≠ condemn |
| 657 | 8 | `Nie ciepłem pieca kaflowego, który gasł powoli w kącie pokoju.` | `Nie ciepłem kozy, przygaszonej po drugiej stronie pokoju.` | woodstove = koza (Inn Trouble PL term; piec kaflowy = tile stove); 'across the room' |
| 661 | 8 | `będzie dalej rozgrzewać świecę do złota` | `będzie dalej złocić świece` | 'turning a candle gold' |
| 661 | 8 | `zamknąłby ją w zagrodzie razem z reniferami` | `zamknąłby ją na wybiegu razem z reniferami` | paddock = wybieg (Inn Trouble PL series term) |
| 667 | 8 | `gdy tłum już się rozstąpił` | `gdy tłum już się rozszedł` | 'had gone in' ≠ parted |
| 668 | 8 | `— Sprawiłeś, że cała reszta wzdycha w górę alei, a ty stanąłeś tutaj` | `— Wszystkie pozostałe wzdychają w stronę Hollyhock Lane, a ty stanąłeś tutaj` | 'mooning up the lane' = Hollyhock Lane, not the avenue; the snowman didn't cause it |
| 674 | 9 | `że ani przez chwilę nie wątpiła w magię tego sezonu` | `że ani przez chwilę nie wątpiła w ten sezon` | addition ('magic' not in EN 'never doubted the season') |
| 679 | 9 | `— Alan Varney. Inspekcja sanitarna.` | `— Alan Varney. Inspekcja sanitarna hrabstwa.` | 'County health' (county = hrabstwo) |
| 701 | 9 | `kształtu. Zacytowała podpunkty. Nie wściekły sąsiad.` | `kształtu. Skarga cytowała podpunkty. Nie wściekły sąsiad.` | SPOILER-GENDER: bare feminine 'Zacytowała' (subject = the complaint) read as 'SHE cited' — the culprit unknown; EN 'It named' |
| 701 | 9 | `które napisało na ścianie` | `które napisałoby na ścianie` | EN conditional 'who'd have written' |
| 701 | 9 | `bo tylko tyle potrafiło napisać` | `bo tylko tyle potrafiłoby napisać` | EN conditional |
| 719 | 10 | `upiec w kuchni kruche ciasteczka Grety` | `upiec w kuchni maślane ciasteczka Grety` | term drift: shortbread = maślane ciasteczka (Ch6) |
| 719 | 10 | `w tym roku są tak daleko w tyle` | `w tym roku mają takie zaległości` | 'so far behind' = arrears |
| 727 | 10 | `Ale miasto ma na myśli wybite okno` | `Ale miasteczko ma w głowie wybite okno` | town = miasteczko |
| 727 | 10 | `tym bardziej wyglądam, jakby mną kierował powód, dla którego potrzebują obrony` | `tym bardziej wyglądam, jakbym znał powód, dla którego trzeba ich bronić` | 'like I know a reason' |
| 731 | 10 | `— Cicho. — Powiedział` | `— Po cichu. — Powiedział` | 'Quiet' = quietly (it reaches them), not 'hush' |
| 731 | 10 | `w tamten koniec miasta raz w tygodniu i niczyim interesem nie jest, na czyim progu ląduje` | `w tamten koniec miasteczka raz w tygodniu i nikogo nie powinno obchodzić, na czyim progu ląduje` | town = miasteczko; calque |
| 745 | 10 | `do tego jest ciężka, a ja jestem stara, więc zrobiłabyś mi przysługę, zabierając mi ją z rąk` | `do tego to ciężkie, a ja jestem stara, więc zrobiłabyś mi przysługę, zabierając mi to z rąk` | agreement: 'it' = the box, not the flour |
| 749 | 10 | `Małe, wycięte figurki` | `Małe, rzeźbione figurki` | carved = rzeźbione |
| 753 | 10 | `i dach, który w większym stopniu trzyma się kupy` | `i dach, który jako tako się trzyma` | 'mostly holds' calque |
| 753 | 10 | `a całe miasto świeci jak obietnica` | `a całe miasteczko świeci jak obietnica` | town = miasteczko |
| 777 | 10 | `starannie winietowany` | `starannie poliniowany` | 'ruled' ≠ vignetted |
| 777 | 10 | `wrzucili więcej, niż zdołali zabrać` | `wrzucili więcej, niż wzięli` | 'than they took' |
| 781 | 10 | `Hal skreślił linię pod dziennym bilansem, precyzyjnie.` | `Hal pociągnął kreskę pod dziennym bilansem, precyzyjnie.` | 'ruled a line under' ≠ crossed out |
| 783 | 10 | `nie robi tego dlatego, że zmarzł. Robi to dlatego, że chciał pustego sklepu dla niej i pełnego dla siebie. To nie jest głodna dłoń. Głód by zagarnął. Ten celuje.` | `nie robi tego dlatego, że marznie. Robi to, bo chce, żeby jej sklep opustoszał, a własny się zapełnił. To nie jest głodna dłoń. Głód by zagarnął. Ta dłoń celuje.` | spoiler-gender: masc. 'zmarzł/chciał/Ten' before the reveal → ungendered present; garbled 'empty shop for her' |
| 791 | 10 | `żeby najstarsza piekarnia w alei pociemniała przed świętami` | `żeby w najstarszej piekarni przy alei zgasły światła przed świętami` | 'dark' = closed (cf. targeted fix 'zgasły światła') |
| 801 | 11 | `czyniło go zarazem miejskim chemikiem` | `czyniło go zarazem miejscowym chemikiem` | town (not city) |
| 801 | 11 | `i pingwinem, który poszedł prosto do jego pieca` | `i z Pip, która poszła prosto do jego pieca` | Pip she/her (masc. verb) |
| 815 | 11 | `wejść komuś do głowy, Jessica.` | `wejść komuś do głowy, Jessico.` | vocative |
| 820 | 11 | `chociaż miasto by to zrobiło` | `chociaż miasteczko by to zrobiło` | town = miasteczko |
| 822 | 11 | `to coś wolnego w mieście położyło mi rękę` | `to coś wolnego w miasteczku położyło mi rękę` | town = miasteczko |
| 825 | 11 | `Stał przez dwa dni, patrząc na tę alejkę` | `Bałwan stał przez dwa dni, patrząc na tę alejkę` | unclear subject after 'Magia…' |
| 835 | 12 | `dla piekarza, który tkwił przy piecach od ciemnej nocy` | `dla piekarki, która tkwiła przy piecach od ciemnej nocy` | gender: the baker is Greta |
| 840 | 12 | `I te dwa, które dzieliły rampę.` | `I te dwoje drzwi, które dzieliły rampę.` | agreement (drzwi plurale tantum; cf. [857] 'dwojga') |
| 845 | 12 | `Próbowałam tego uniknąć.` | `Starałam się tam nie patrzeć.` | EN 'I had been trying not to [look]' |
| 848 | 12 | `świeżo dorobione z warsztatu Toma` | `nowiutkie, prosto z półki u Toma` | 'bright off Tom's rack' (bought, not cut) |
| 857 | 12 | `a ona była uczciwym zwierzakiem` | `a ona była uczciwym ptakiem` | 'honest bird' |
| 885 | 13 | `Przyszłam panu powiedzieć, że brałam pana pod uwagę.` | `Przyszłam panu powiedzieć, że miałam pana na liście podejrzanych.` | 'I had you down for it'; the later 'skreśliłam pana z tej listy' needs the list |
| 885 | 13 | `że o świcie jest pan na tym podwórku` | `że przed świtem jest pan na tym podwórku` | 'before light' |
| 899 | 13 | `bez względu na to, co miasto chciałoby przypisać` | `bez względu na to, co miasteczko chciałoby przypisać` | town = miasteczko |
| 922 | 14 | `Miasteczko znalazło winnego szybciej ode mnie i padł on na chłopaka.` | `Miasteczko znalazło winnego szybciej ode mnie — i był nim chłopak.` | garbled |
| 923 | 14 | `niosąc swój notatnik — jak na złość zamknięty — i zaciśnięte usta` | `niosąc swój notatnik — wyjątkowo zamknięty — i z zaciśniętymi ustami` | 'closed for once' ≠ 'annoyingly' |
| 923 | 14 | `Po miasteczku krążyło nazwisko sprawcy, który napisał coś na ścianie Grety. Tym chłopakiem był Danny Ott.` | `Po miasteczku krążyło nazwisko tego, kto rzekomo pomalował ścianę Grety. Brzmiało ono: Danny Ott.` | 'Tym chłopakiem' had no antecedent; 'sprawca' stated his guilt as fact |
| 928 | 14 | `— Jessica, zwolniłam tego chłopaka` | `— Jessico, zwolniłam tego chłopaka` | vocative |
| 940 | 14 | `— Niech jej pani zapyta.` | `— Niech ją pani zapyta.` | case (zapytać + acc.) |
| 942 | 14 | `To stało się po wiadomościach. Narosło na problem, który ktoś inny zapoczątkował.` | `Pojawiło się dopiero, gdy rozeszły się wieści. Dołożyło się do kłopotu, który zaczął ktoś inny.` | 'came after the news' (the talk), garbled 'piled on' |
| 951 | 14 | `— Pani Danny nie malował tej ściany, pani Ott.` | `— Pani syn, Danny, nie malował tej ściany, pani Ott.` | 'Pani Danny' reads as 'Mrs Danny' |
| 953 | 14 | `tam, gdzie to miało znaczenie` | `tam, gdzie to ma znaczenie` | tense |
| 955 | 14 | `bez żadnych wianków` | `bez żadnych wieńców` | term drift wreath = wieniec |
| 961 | 14 | `— Tak czułam — powiedziała Claire` | `— Wiedziałam — powiedziała Claire` | 'I knew it' |
| 964 | 14 | `karmiła obiadem każde dziecko w tym miasteczku od dwudziestu lat` | `od dwudziestu lat karmi obiadem każde dziecko w tym miasteczku` | tense (has fed for twenty years) |
| 974 | 14 | `Powinny być dobre w sklepie ze złotem.` | `Powinny być dobre w tym złotym sklepie.` | 'the gold shop' = złoty sklep (Ch19 [1257]); 'sklep ze złotem' = a shop selling gold |
| 975 | 14 | `Jeszcze nie wstąpiła po wianek` | `Jeszcze nie wstąpiła po wieniec` | term drift wreath = wieniec |
| 994 | 15 | `— Jessica. Jak ona się trzyma?` | `— Jessico. Jak ona się trzyma?` | vocative |
| 1000 | 15 | `A teraz miasto przyszło, żeby dołożyć` | `A teraz miasteczko przyszło, żeby dołożyć` | town = miasteczko |
| 1004 | 15 | `jeśli miasto zrobi dach. Uratują to miejsce, Jessica.` | `jeśli miasteczko zrobi dach. Uratują to miejsce, Jessico.` | town = miasteczko; vocative |
| 1005 | 15 | `jak ciepło z polnego kominka Nicka` | `jak ciepło z kominka Nicka z polnych kamieni` | 'fieldstone hearth' (polny kominek = 'field fireplace') |
| 1009 | 15 | `co wypuszczała na swoją tablicę` | `co dopuszczała do swojej tablicy` | 'let onto her board' |
| 1013 | 15 | `kiedy handel się uspokoił` | `kiedy ruch by się już uspokoił` | tense (hypothetical) |
| 1013 | 15 | `cały świąteczny handel słodyczami w mieście` | `cały świąteczny handel słodyczami w miasteczku` | town = miasteczko |
| 1013 | 15 | `by schwytać każdą duszę. Wydrukowana, przypięta i opłacona na pełny tydzień przed tym` | `by schwytać każdą duszę. A ulotkę wydrukowano, przypięto i opłacono na pełny tydzień przed tym` | dangling participles attached to 'cukiernia'; EN = the flyer |
| 1014 | 15 | `Chyba że wiedziałaś, że nadchodzi, ponieważ to ty byłaś tą, która je przyniosła.` | `Chyba że się wiedziało, że nadchodzi, bo samemu się je sprowadzało.` | generic 'you' rendered feminine (gendered the unknown wrongdoer); impersonal |
| 1025 | 15 | `Kwas, powiedziała, ot tak, jak pogodę,` | `Kwas, powiedziała, lekko, jakby mówiła o pogodzie,` | garbled 'easy as weather' |
| 1029 | 15 | `bo nie mogłam myśleć w takim upale` | `bo nie mogłam myśleć w takim cieple` | 'warmth' ≠ heat wave |
| 1032 | 15 | `Nie powolna w obrabianiu mąki czy alejki.` | `Nie w rozpracowaniu mąki czy alejki.` | 'work the flour' = work out |
| 1032 | 15 | `rodziny liczącej metry drzewa` | `rodziny liczącej szczapy drewna` | cordwood (cf. Ch10 'szczapy') |
| 1033 | 15 | `Rzecz powiedziana głośno w tym mieście` | `Rzecz powiedziana głośno w tym miasteczku` | town = miasteczko |
| 1041 | 16 | `Kiedy więc moje dłonie zajmowały się jodłą, zrobiłam też tę drugą rzecz, po którą przyszłam. Przyjrzałam się jej uważnie.` | `Kiedy więc moje dłonie będą zajęte jodłą, zajmę się tą drugą sprawą, dla której tam szłam. Przyjrzę się jej z bliska.` | tense: night-time plan ('I'd do'), not a done deed |
| 1059 | 16 | `W to Boże Narodzenie w tym miasteczku jest więcej słodkiego utargu, niż kiedykolwiek dało się gdziekolwiek zarobić, ponieważ zawsze był tu tylko ten jeden stary sklep z wypiekami, u którego można było go zostawić.` | `W tym miasteczku jest na Boże Narodzenie więcej słodkiego utargu, niż kiedykolwiek miało gdzie go wydać, ponieważ zawsze była tu tylko ta jedna stara piekarnia, w której można było go zostawić.` | mistranslation ('more than ever earned anywhere'); 'the one old bakery' = Greta's bakery = piekarnia |
| 1059 | 16 | `Określenie „ten jeden stary sklep z wypiekami” przeszło` | `Określenie „ta jedna stara piekarnia” przeszło` | bakery = piekarnia |
| 1087 | 16 | `— Żeby stanąć wśród innych.` | `— Żeby wisiał wśród innych.` | the wreath hangs |
| 1099 | 17 | `Wianek dla Sugarplum leżał` | `Wieniec dla Sugarplum leżał` | term drift wreath = wieniec |
| 1100 | 17 | `W liceum była skrócona lekcja` | `W liceum był skrócony dzień zajęć` | 'a half day at the high school' |
| 1102 | 17 | `Ja to tylko przyniosłam.` | `Ja ją tylko rozniosłam.` | 'I only carried it' (the truth, spread it) |
| 1106 | 17 | `gdyby ktoś mnie zapytał zamiast samemu decydować` | `gdyby ktoś mnie zapytał, zamiast z góry przesądzać` | 'instead of deciding' |
| 1106 | 17 | `Słyszeli, jak całe miasto mówi` | `Słyszeli, jak całe miasteczko mówi` | town = miasteczko |
| 1111 | 17 | `Dorosły, w fartuchu piekarskim.` | `Ktoś dorosły, w fartuchu piekarskim.` | spoiler-gender (see next) |
| 1111 | 17 | `Stała przy jej tylnych schodkach przez chwilę, a potem ruszyła alejką w stronę drugiego końca. Nigdzie nie weszła. Zgubiłem ją za światłem przy aptece.` | `To stało przy jej tylnych schodkach przez chwilę, a potem ruszyło alejką w stronę drugiego końca. Nigdzie nie weszło. Zgubiłem to za światłem przy aptece.` | SPOILER-GENDER: bare feminine 'Stała/ruszyła/weszła/ją' read as 'SHE' before the reveal; EN 'it' → neuter 'to' (as Ch13 'przeganiał pan to'). The figure, not Danny, passes the light ✓ |
| 1113 | 17 | `to nie było jedno z jej worków na mąkę` | `to nie był żaden z jej worków na mąkę` | agreement |
| 1118 | 17 | `Pip odprowadziła ją wzrokiem bez większego wdzięku.` | `Pip niechętnie odprowadziła ją wzrokiem.` | 'with poor grace' = grudgingly |
| 1128 | 17 | `— Jestem weterynarzem, Jessica` | `— Jestem weterynarzem, Jessico` | vocative |
| 1146 | 17 | `Ostry, jak ocet.` | `Ostry zapach, jak ocet.` | agreement (no noun for 'Ostry') |
| 1158 | 17 | `przyniesie pani ten wianek, domyślam się — stwierdziła. — Gałązki jodły i złota wstążka.` | `przyniesie pani ten wieniec, domyślam się — stwierdziła. — Jodła i złota kokarda.` | wreath = wieniec; 'Balsam and a gold bow' = her own words in [1087] |
| 1162 | 17 | `— Zostaje to ze mną, Jessica — powiedział.` | `— To zostanie między nami, Jessico — powiedział.` | idiom 'That stays with me' = I'll keep it quiet; vocative |
| 1179 | 18 | `którego piec przestawał grzać` | `którego piec przestał grzać` | aspect ('had quit') |
| 1181 | 18 | `Cały koszt, jeśli miasto zrobi dach.` | `Cały koszt, jeśli miasteczko zrobi dach.` | town = miasteczko |
| 1181 | 18 | `Chodzi o zbiory, Jessica.` | `Chodzi o zbiory, Jessico.` | vocative |
| 1183 | 18 | `Miasto najpierw musiało wyciągnąć rękę.` | `Miasteczko najpierw musiało wyciągnąć rękę.` | town = miasteczko |
| 1184 | 18 | `komuś należał się wianuszek` | `komuś należał się wieniec` | term drift wreath = wieniec |
| 1184 | 18 | `moja pewność siebie usunięta spod nóg` | `moja pewność, która usunęła mi się spod nóg` | 'certainty' ≠ self-confidence |
| 1193 | 18 | `jedyną piękną rzecz u prostego, ostrożnego człowieka` | `jedyna piękna rzecz u prostego, ostrożnego człowieka` | case (apposition) |
| 1194 | 18 | `nie brać za to zasług, nie być przez nikogo dziękowanym. Bycie dziękowanym było właśnie tym, czemu się sprzeciwił i zamierzał sprzeciwiać` | `nie brać za to zasług i nie przyjmować od nikogo podziękowań. Przed podziękowaniami właśnie się wzbraniał i zamierzał się wzbraniać` | 'dziękowany' is not Polish (no passive of dziękować) |
| 1195 | 18 | `Utkwił w bezruchu między mokrą stroną` | `Zastygł między mokrą stroną` | wrong verb |
| 1223 | 19 | `W Evergreen leży śnieg od Halloween. Nikt nie podnosił luźnej cegły z tej ulicy.` | `Na Evergreen leży śnieg od Halloween. Nikt nie podniósł luźnej cegły z tej ulicy.` | preposition; aspect |
| 1227 | 19 | `Widziałam gruz na tej cegle i przeczytałam jej nazwisko.` | `Widziałam na tej cegle jej gruz i wyczytałam z niego jej nazwisko.` | 'saw HER rubble on that brick' |
| 1227 | 19 | `Gdybyś chciał, żeby miasto patrzyło na Sugarplum, gdzie byś pojechał po cegłę?` | `Gdybyś chciał, żeby miasteczko patrzyło na Sugarplum, gdzie byś poszedł po cegłę?` | town = miasteczko; 'go' |
| 1231 | 19 | `kolacje parafialne tego miasta` | `kolacje parafialne tego miasteczka` | town = miasteczko |
| 1235 | 19 | `i zobaczyłam jej imię, bo poszłam go poszukać` | `i zobaczyłam jej nazwisko, bo go szukałam` | consistency with [1227] 'nazwisko'; calque |
| 1261 | 19 | `— Mogłaby być. Ale po co` | `— Może i tak. Ale po co` | 'It might be' |
| 1293 | 19 | `Wtedy Doktor przeszukał` | `Wtedy doktor przeszukał` | capitalisation |
| 1308 | 20 | `— Jessica. Bardzo dobrze — powiedziała Olivia.` | `— Jessico. Dobrze, że jesteś — powiedziała Olivia.` | vocative; 'Good' (you're here) |
| 1310 | 20 | `skoro Holly Jolly jest zamknięte` | `skoro Holly Jolly jest zamknięta` | gender: Holly Jolly fem. elsewhere |
| 1330 | 20 | `— Jessica? — odezwała się Olivia.` | `— Jessico? — odezwała się Olivia.` | vocative |
| 1346 | 20 | `A urząd hrabstwa nie przyjdzie, dopóki` | `A urząd hrabstwa nie przyjdzie ponownie, dopóki` | 'won't come back' |
| 1358 | 20 | `Greta odwróciła się od pieca i spojrzała na mnie ponuro.` | `Greta odwróciła się od pieca i zmarszczyła brwi.` | 'frowned' |
| 1429 | 21 | `— Wylądował w koszu, Jessica.` | `— Wylądował w koszu, Jessico.` | vocative |
| 1445 | 21 | `— Jessica — powiedziała. — To ta Joyce od Grety.` | `— Jessico — powiedziała. — To ta Joyce od Grety.` | vocative |
| 1474 | 21 | `z drzemiącą u jego stóp Pip leżącą na furgonetce` | `z Pip drzemiącą u jego stóp na kartce z furgonetką` | 'asleep on the van' = on the printed page |
| 1477 | 21 | `Dobranoc, Jessica.` | `Dobranoc, Jessico.` | vocative |
| 1493 | 22 | `Sprawa trafiła więc w ręce wymiaru sprawiedliwości` | `Sprawa miała więc trafić w ręce wymiaru sprawiedliwości` | tense: a decision ('it would go'), not a done deed |
| 1502 | 22 | `— Jessica — odezwała się Tanaka.` | `— Jessico — odezwała się Tanaka.` | vocative |
| 1507 | 22 | `spojrzał na wydruk przesłany przez Claire z furgonetką` | `spojrzał na wydruk od Claire z furgonetką` | Claire printed it, didn't send it |
| 1518 | 22 | `— Będę jej chcieć.` | `— Będę jej potrzebować.` | calque |
| 1522 | 22 | `wyłożę jej wszystko prosto w oczy a ona` | `wyłożę jej wszystko prosto w oczy, a ona` | punctuation |
| 1524 | 22 | `Lubię, żeby robiono to w ten sam sposób.` | `Ja też wolę to robić w ten sposób.` | 'I like them done that way too' |
| 1546 | 22 | `szefowa policji w Frost Falls` | `szefowa policji we Frost Falls` | preposition (edition's own 'we Frost Falls') |
| 1563 | 23 | `z tym ponurym, chciwym zainteresowaniem` | `z tym poważnym, chciwym zainteresowaniem` | 'grave' = solemn, not gloomy |
| 1631 | 23 | `cieszyłam się, Bóg mi świadkiem, cieszyłam się` | `cieszyłam się, niech mi Bóg wybaczy, cieszyłam się` | 'God forgive me' ≠ 'God is my witness' |
| 1714 | 24 | `Wciąż było zamknięte, żółte zawiadomienie hrabstwa wisiało na szybie, dopóki Varney nie przyszedł go zdjąć` | `Wciąż była zamknięta, żółte zawiadomienie hrabstwa miało wisieć na szybie, dopóki Varney nie przyjdzie go zdjąć` | gender (Holly Jolly fem.); tense (until Varney comes) |
| 1758 | 24 | `— I co?` | `— A było?` | EN 'Was there?' (anything else) |
| 1783 | 25 | `po pudło do beczki z żywnością, po którą zawsze przychodził` | `po pudło do beczki z żywnością, po które zawsze przychodził` | agreement |
| 1802 | 25 | `— Jedno popołudnie, Jessica. A na dokładkę będą pieniądze z sądu, co do centa za to, co zmarnowała.` | `— Jedno popołudnie, Jessico. A na dokładkę będą pieniądze z sądu, co do centa za wszystko, co ona zepsuła.` | vocative; 'what SHE spoiled' (Joyce) — bare 'zmarnowała' read as Greta |
| 1809 | 25 | `— Nie pozwoliłaś im zrobić z tego mojej mąki — oświadczyła.` | `— Nie pozwoliłaś, żeby zwalili to na moją mąkę — oświadczyła.` | calque 'make it my flour' = blame my flour |
| 1817 | 26 | `gdyby miastu zabrakło funduszy` | `gdyby miasteczku zabrakło funduszy` | town = miasteczko |
| 1817 | 26 | `Jeśli miasto zapłaci za własny dach, budynek będzie należał do miasta` | `Jeśli miasteczko zapłaci za własny dach, budynek będzie należał do miasteczka` | town = miasteczko |
| 1820 | 26 | `Nie odchodzicie od pracy, żeby po nią iść.` | `Nie odchodźcie od pracy, żeby po nią iść.` | imperative |
| 1836 | 26 | `jak wtedy, gdy z kolanami oblepionymi bibułą pracował nad renowacją w zimnym tylnym pokoju` | `jak wtedy, gdy na kolanach osuszał bibułą papiery w zimnym tylnym pokoju` | mistranslation: 'on his knees' = kneeling, not knees covered in blotting paper |
| 1847 | 26 | `W przednim oknie, bezpieczne w gablocie za czystą szybą, stara skrzynka stała zapieczętowana. Niczyja dłoń go nie dotknęła. Jego kartka` | `W przednim oknie, bezpieczna w gablocie za czystą szybą, stara skrzynka stała zapieczętowana. Niczyja dłoń jej nie dotknęła. Jej kartka` | agreement (skrzynka fem.) |
| 1859 | 26 | `jaki powiesiliśmy w każdym oknie` | `jaki powiesiłyśmy w każdym oknie` | agreement (the circle women) |
| 1876 | 26 | `Miasto znało je już na pamięć.` | `Miasteczko znało je już na pamięć.` | town = miasteczko |
| 1935 | 27 | `— Nie, ty mały żebraku.` | `— Nie, ty mała żebraczko.` | Pip she/her |
| 443 | 5 | `Nasłała na niego miasto. On nasłał je na nią` | `Nasłała na niego gminę. On nasłał ją na nią` | 'called the town' = the municipality; no 'miasto' for Frost Falls |
| 578 | 7 | `i owszem, nasłała na mnie miasto, i owszem` | `i owszem, nasłała na mnie gminę, i owszem` | as [443] |
| 509 | 6 | `strzęp historii założenia miasta` | `strzęp historii założenia miasteczka` | town = miasteczko |
| 596 | 7 | `Z rejestracją spoza miasta;` | `Z rejestracją spoza miasteczka;` | town = miasteczko |
| 661 | 8 | `tam, gdzie miasto może ją zobaczyć` | `tam, gdzie miasteczko może ją zobaczyć` | town = miasteczko |
