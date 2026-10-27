# Flour Play - ASSEMBLED - FORMATTED_Polish — APPLIED (2026-10-27)

Output: `translated\corrected\Flour Play - ASSEMBLED - FORMATTED_Polish.docx`
Backup of the pre-proofread corrected copy (identical to the input): `translated\corrected\_bak\Flour Play - ASSEMBLED - FORMATTED_Polish.pre-proofread-20261027.docx`
Method: run-level edits of `<w:t>` nodes only; every fix matched the paragraph's exact current text exactly once before writing. No `set_para_text()`. Excerpt paragraphs rebuilt from the published edition's runs (text + italic/bold), base formatting cloned from the original first run.

- Text fixes applied: 622 (0 refused, 0 not found)
- Excerpt paragraphs replaced from the published edition: 50
- Dialogue: 584 dialogue paragraphs converted en-dash → em-dash (659 paragraphs touched incl. narration dashes); ellipsis "..." → "…" ×10
- Stray `<bt>` removed: 20 (ruling 5); title anchors added: 4 ([0], [16]–[18], matching Book 1)
- Italic runs: 44 → 46. +2 = the two capsule-card texts in Ch26 [1846], [1884], italic in the English (ruling 3). Italic runs whose TEXT changed (translated/corrected in place, count unchanged): [533] [687] [701] BRUDNY→BRUDNE; [1000] "zepieczętowania" typo; [1008] date range; [1011] Varney's line echo; [1025] Doc's words echo; [1716] "Orders taken until December 20" translated; [1907] "Greta," → "Greto,"; [1909]–[1910] Joyce's letter; [1987] [1997] sell lines.

## Checks on the corrected file
1. Untranslated English: `[]`
2. `bt_anchors.py check`: 9 spans, 0 unpaired; only Flour Play / Frost and Found / Inn Trouble / The Binder's Bequest
3. `check_matter.py --file`: 1 PASS 0 FAIL
4. `preflight.py --verify`: paragraphs 2049 → 2049 ok; scene breaks 60 → 60 ok; italic 44 → 46 (declared +2; sequence differs only at the in-place translations listed above); bt 25 → 9 = ruling 5 removals (−20) + Book-1 title anchors (+4) — reports FAIL by design of the check, which predates ruling 5.


## Applied (para · was → now · why)

| ¶ | was | now | why |
|---|---|---|---|
| 0 | `Rozdział 3` | `<bt>Flour Play</bt>` | title page: title page read "Chapter 3" instead of the book title; now matches Book 1 (title anchor, stamped later with the catalogue Polish title) |
| 4 | `Księga 3` | `Tom 3` | consistency: series line: Book 1 Polish uses "Tom 1" |
| 10 | `Wszystkie prawa zastrzeżone.` | `Wszelkie prawa zastrzeżone.` | consistency: ruling 7: copyright block wording matched to Book 1 |
| 12 | `Żadna część tej publikacji nie może być powielana, rozpowszechniana ani przekazywana w jakiejkolwiek formie i za pomocą jakichkolwiek środków, w tym kserokopii, nagrań lub innych metod elektronicznych czy mechanicznych, bez uprzedniej pisemnej zgody wydawcy, z wyjątkiem przypadków dozwolonych przez amerykańskie prawo autorskie.` | `Żaden fragment tej publikacji nie może być powielany, rozpowszechniany ani przekazywany w jakiejkolwiek formie ani przy użyciu jakichkolwiek środków, w tym kserokopii, nagrań lub innych metod elektronicznych lub mechanicznych, bez uprzedniej pisemnej zgody wydawcy, z wyjątkiem przypadków dozwolonych przez amerykańskie prawo autorskie.` | consistency: ruling 7: rights paragraph matched to Book 1 verbatim |
| 14 | `Ta historia, wszystkie imiona, postacie i wydarzenia przedstawione w tym utworze są fikcyjne. Nie zamierzano sugerować jakichkolwiek powiązań z rzeczywistymi osobami (żyjącymi lub zmarłymi), miejscami, budynkami i produktami, ani też nie należy takich powiązań wyciągać.` | `Przedstawiona tu historia, wszelkie imiona, postacie i wydarzenia są całkowicie fikcyjne. Wszelkie podobieństwo do prawdziwych osób (żyjących lub zmarłych), miejsc, budynków i produktów jest niezamierzone i nie powinno być wyciągane jako wniosek.` | consistency: ruling 7: fiction disclaimer matched to Book 1 verbatim |
| 15 | `Książki z tej serii` | `Książki w tej serii` | consistency: series-page heading matched to Book 1 |
| 16 | `Frost and Found` | `<bt>Frost and Found</bt>` | title anchor: Book 1 carries title anchors on its series list; restored so stamp() localises the titles |
| 17 | `Inn Trouble` | `<bt>Inn Trouble</bt>` | title anchor: as above |
| 18 | `Flour Play` | `<bt>Flour Play</bt>` | title anchor: as above |
| 25 | `Fragment powieści <bt>` | `Fragment książki <bt>` | consistency: TOC entry matched to the back-matter heading (and Book 1) |
| 37 | `nowa cukiergarnia` | `nowa cukiernia` | typo: non-word |
| 98 | `a każdy grosz idzie` | `a każdy cent idzie` | currency: dollars/cents only (no Polish currency idioms) |
| 42 | `na sześć cali grubości` | `na piętnaście centymetrów grubości` | units: "six inches" of snow: imperial unit; 6 in ≈ 15 cm (safe arithmetic) |
| 128 | `Sześć cali świeżego` | `Piętnaście centymetrów świeżego` | units: "Six inches" of fresh fall; 15 cm (safe arithmetic) |
| 77 | `Nie chodziło o mile.` | `Nie chodziło o kilometry.` | units: "Not the miles" — rhetorical distance; metric equivalent keeps the sense (safe, idiomatic) |
| 88 | `widziałam cię w Gminie` | `widziałam cię w świetlicy` | mistranslation: "at the Grange" (the Grange hall, a community hall) rendered "w Gminie" (= municipal office); unified rendering "świetlica" (community hall) — see term table |
| 92 | `w geście usprawiedliwienia` | `triumfalnie` | mistranslation: "in vindication" ≠ "usprawiedliwienie" (excuse/justification) |
| 73 | `zaprzecziłam` | `zaprzeczyłam` | typo: spelling |
| 122 | `bałwane dzieciaków` | `bałwany dzieciaków` | typo: plural of bałwan is bałwany |
| 136 | `Zatarły za sobą szczotką` | `Zatarli ślady za sobą` | grammar: missing object ("brushed them [the prints] out"); agreement with the "Obrócili" of the previous line |
| 124 | `z węglanymi oczami` | `z oczami z węgielków` | mistranslation: "węglany" means carbonate; "coal-eyed" |
| 140 | `na ten środkowy bałwan zwrócony` | `na tego środkowego bałwana zwróconego` | grammar: accusative of bałwan is bałwana |
| 124 | `Zieleniec rozciągał się naprzeciwko Yarn Tales, szeroki, biały skwer z pomnikiem` | `Skwer rozciągał się naprzeciwko Yarn Tales, szerokie, białe błonie z pomnikiem` | consistency: the green = "skwer" (Book 1 Polish, dominant form); "common" = błonie |
| 128 | `skierowaną w górę zieleńca` | `skierowaną w górę skweru` | consistency: the green = skwer |
| 146 | `Śnieg lśnił jasno na zieleńcu` | `Śnieg lśnił jasno na skwerze` | consistency: the green = skwer |
| 149 | `Tej rangi słyszałam` | `Tego ranka słyszałam` | typo: "rangi" (rank) for "ranka" (morning) |
| 166 | `Próbowałem nie skrzywić` | `Próbowałam nie skrzywić` | gender: female narrator rendered male |
| 162 | `co do cholery się stało?` | `co się, na litość boską, stało?` | register: "what on earth" softened to cozy register (cholera = swear) |
| 172 | `Przepadał.` | `Przepadł.` | grammar: aspect: "Gone." completed |
| 180 | `Pip obenglowała podłogę` | `Pip obwąchiwała podłogę` | typo: non-word "obenglowała"; EN "had been inspecting" (she investigates nose first) |
| 182 | `zagnieździłam czystą partię` | `zagniotłam czystą partię` | mistranslation: "zagnieździć" = to nest; "mixed a clean batch" = zagnieść |
| 186 | `zamówienia na Święta Dziękczynienia` | `zamówienia na Święto Dziękczynienia` | grammar: Thanksgiving is singular "Święto Dziękczynienia" elsewhere |
| 190 | `z całym dobrobytem i szyldem` | `z całym dobytkiem i szyldem` | mistranslation: "dobrobyt" = prosperity; "lock, stock" = dobytek |
| 194 | `Niedbalstvo nie wyszłoby` | `Niedbalstwo nie wyszłoby` | typo: Czech/Slovak spelling |
| 200 | `Zdejmowałam pokrywę` | `Zdjęłam pokrywę` | grammar: aspect: single completed action |
| 214 | `ramę po ramie` | `naręcze po naręczu` | mistranslation: "armful by armful" ≠ "frame by frame" |
| 219 | `Kiedy wyszłam na aleję Evergreen,` | `Kiedy wyszłam na Evergreen Avenue,` | consistency: street name: edition uses "Evergreen Avenue" everywhere else |
| 186 | `a zamówienia na Święto Dziękczynienia czekają w tej księdze` | `a zamówienia na Święto Dziękczynienia czekają w tym zeszycie` | clue: "the order book" — ONE rendering: "zeszyt zamówień" (Ch20 uses it ×10; Joyce copies the names from it) |
| 188 | `Na ladzie leżał otwarty rejestr` | `Na ladzie leżał otwarty zeszyt zamówień` | clue: order book = zeszyt zamówień |
| 190 | `Położyła dłoń płasko na otwartej księdze.` | `Położyła dłoń płasko na otwartym zeszycie.` | clue: order book |
| 222 | `w towarzystwie Pipa` | `w towarzystwie Pip` | names: Pip is female (she/her); female foreign name stays undeclined as in Book 1 ("do Pip") |
| 238 | `Spojrzała w dół na Pipa.` | `Spojrzała w dół na Pip.` | names: Pip is female; undeclined |
| 230 | `– Musisz być panią Claus` | `– Pani zapewne jest panią Claus` | address: Renée has just met Jessica: formal until Jessica offers "Jessica is fine" (ruling 2); the next sentence already uses "o pani" |
| 241 | `Laby były marmurowe` | `Lady były marmurowe` | typo: "lada/lady" = counters |
| 242 | `rozejmując po swoim lśniącym królestwie` | `rozglądając się po swoim lśniącym królestwie` | typo: non-word; "smiled around at her gleaming room" |
| 246 | `Jakiś piekarz hurtowy z Bridgton chce mi sprzedawać swój chleb. Bardzo jej na tym zależy.` | `Jest taka hurtowa piekarka z Bridgton, która chce mi sprzedawać swój chleb. Bardzo jej na tym zależy.` | gender: the Bridgton wholesale baker is a woman (Joyce Wendt — the culprit); "piekarz" (male) contradicted "jej" |
| 248 | `kryła się chłód` | `krył się chłód` | grammar: chłód is masculine |
| 254 | `sięgnęła po financiers i zjadła je` | `sięgnęła po jedno financier i je zjadła` | grammar: EN "took a financier" (one) |
| 260 | `zima przyszyła w tym roku` | `zima przyszła w tym roku` | typo: "przyszyła" = sewed on |
| 260 | `Zbiór żywności.` | `Zbiórka żywności.` | mistranslation: "food drive" = zbiórka żywności ("zbiór" = harvest/collection set) |
| 263 | `Pomyślałam o Gredie` | `Pomyślałam o Grecie` | names: locative of Greta = Grecie (as elsewhere ×9) |
| 267 | `gdy latarnie sklepu rozbłyskiwały` | `gdy światła sklepów rozbłyskiwały` | mistranslation: "the shop lights came on" (plural shops); "latarnie sklepu" = the shop's street lamps |
| 267 | `podsycany niezwykle delikatnie` | `podsycanymi niezwykle delikatnie` | grammar: agrees with "plotkami" |
| 270 | `lolała złotem` | `lśniła złotem` | typo: non-word |
| 232 | `Witaj we Frost Falls.` | `Witamy we Frost Falls.` | address: ruling 2: Renée is a new acquaintance → formal both ways; Polish keeps "pani" + first name after "Jessica is fine" (pani Jessico), which also matches her later "Mrs. Claus" |
| 235 | `Masz już przecież piekarnię, wiem.` | `Macie już przecież piekarnię, wiem.` | address: "you" = the town (as in "radziliście" just before) |
| 237 | `Chociaż powiem ci, że w tym fachu` | `Chociaż powiem pani, że w tym fachu` | address: ruling 2 (Renée formal) |
| 237 | `Ale posłuchaj mnie, gadam o interesach, podczas gdy ty przyszłaś tylko się przywitać. Wejdź. Chcę, żebyś zobaczyła piece.` | `Ale proszę mnie posłuchać, gadam o interesach, podczas gdy pani przyszła tylko się przywitać. Proszę wejść. Chcę, żeby pani zobaczyła piece.` | address: ruling 2 |
| 239 | `Przepisy sanitarne. Rozumiesz.` | `Przepisy sanitarne. Pani rozumie.` | address: ruling 2 |
| 242 | `Znam grudzień, Jessica.` | `Znam grudzień, pani Jessico.` | address: ruling 2 — first name with formal address |
| 243 | `– Będziesz robić to wszystko sama?` | `– Będzie pani robić to wszystko sama?` | address: ruling 2 |
| 244 | `niż tabliczki, które kupujesz w sklepie, widzisz, dzięki czemu` | `niż zwykłe tabliczki ze sklepu, rozumie pani, dzięki czemu` | address: ruling 2 |
| 246 | `Musisz mi wybaczyć.` | `Musi mi pani wybaczyć.` | address: ruling 2 |
| 279 | `Wyciągnęła blaszę` | `Wyciągnęła blachę` | typo: blacha |
| 281 | `Duzina miękkich bułek` | `Tuzin miękkich bułek` | typo: non-word "Duzina"; a dozen = tuzin |
| 309 | `wysokie na stopę` | `wysokie na trzydzieści centymetrów` | units: "a foot high" → 30 cm (safe arithmetic) |
| 309 | `Pierwszym słowem było DIRTY. Drugim UNSAFE.` | `Pierwszym słowem było BRUDNE. Drugim NIEBEZPIECZNE.` | sign: ruling 3: graffiti text translated (neuter, agreeing with "jedzenie" — "her food was filthy") |
| 309 | `widniały trzy kolejne: DON'T EAT HERE.` | `widniały trzy kolejne: NIE JEDZCIE TU.` | sign: ruling 3; three words, as the English says "three more" |
| 313 | `żyje ze swojego imienia` | `żyje dzięki swojej renomie` | consistency: echo of Renée's exact line in Ch3 ("Piekarnia żyje dzięki swojej renomie") |
| 315 | `tak szybko, że aż nie zdołałam go odrzucić` | `tak szybko, że aż mu nie zaufałam` | mistranslation: EN "so quickly that I didn't trust it" (reversed: she distrusts the hunch, not fails to reject it) |
| 317 | `a za nią zieło wnętrze` | `a za nią ziało wnętrze` | typo: "ziało" |
| 317 | `wpatrywała się w słowo DIRTY` | `wpatrywała się w słowo BRUDNE` | sign: ruling 3 |
| 323 | `Ktoś, kto napisał DIRTY, UNSAFE i DON'T EAT HERE,` | `Ktoś, kto napisał BRUDNE, NIEBEZPIECZNE i NIE JEDZCIE TU,` | sign: ruling 3 |
| 323 | `Było to zbyt wyrachowane, by mówić jej o tym w najgorszym poranku jej życia` | `Było to zbyt mgliste, by mówić jej o tym w najgorszy poranek jej życia` | mistranslation: EN "too half-seen" (a half-formed idea), not "too calculated" |
| 327 | `Nie stali tam długo.` | `Nie staliśmy tam długo.` | mistranslation: EN "We didn't stand around long" — first person plural |
| 333 | `Niech ktoś znajdzie Toma z metalowego.` | `Niech ktoś znajdzie Toma z żelaznego.` | mistranslation: "the hardware store" = sklep żelazny; "metalowy" is not a shop |
| 335 | `Zjawiała się w towarzystwie większości klubu dziewiarskiego` | `Zjawiła się w towarzystwie większości kręgu dziewiarskiego` | consistency: the circle = "krąg" (Book 1 and this edition); aspect |
| 343 | `większość koła dziewiarskiego` | `większość kręgu dziewiarskiego` | consistency: the circle = krąg |
| 347 | `podczas gdy wszyscy wokół krzątali się w milczeniu` | `podczas gdy krąg krzątał się wokół nas` | mistranslation: EN "with the circle busy all around us" ("w milczeniu" was invented) |
| 359 | `Tom niósł w kombinezonie puszkę` | `Tom, w kombinezonie, niósł puszkę` | mistranslation: "in coveralls with a can" — not carrying the can inside his coveralls |
| 373 | `odezwałą się przybyszka` | `odezwała się przybyszka` | typo:  |
| 377 | `– Przytrzymaj, ja będę naganiać – poleciła. – Trzymaj swojego ptaka z daleka stąd.` | `– Pani trzyma, ja zamiatam – poleciła. – Niech pani trzyma swojego ptaka z daleka stąd.` | address: ruling 2: Joyce has not met Jessica yet → formal; "naganiać" (to herd game) for "push" the broom |
| 379 | `Nie podjdzie tu` | `Nie podejdzie tu` | typo:  |
| 381 | `odkąd tu wszła` | `odkąd tu weszła` | typo:  |
| 386 | `– Ty musisz być panią Claus.` | `– A pani to pewnie pani Claus.` | address: ruling 2: formal until the first-name exchange that follows |
| 398 | `Joyce wypila łyk` | `Joyce wypiła łyk` | typo:  |
| 402 | `Wczoraj wcisnęłam herbatę.` | `Wczoraj wcisnęłam w nią herbatę.` | grammar: missing object ("got tea into her") |
| 404 | `zamaszystymi, starannymi cyframi` | `kanciastymi, starannymi cyframi` | mistranslation: EN "square, careful figures"; "zamaszysty" = sweeping (opposite) |
| 404 | `a nie doliczy do rachunku` | `a nie zawyży rachunku` | mistranslation: "he won't pad the bill" |
| 408 | `a krąg sąsiadów zaczął rozchodzić się` | `a kobiety z kręgu zaczęły rozchodzić się` | mistranslation: "the circle" = the knitting circle, not "a circle of neighbours" |
| 416 | `widniało DIRTY` | `widniało BRUDNE` | sign: ruling 3 |
| 392 | `obok księgi zamówień na Święto Dziękczynienia, która leżała otwarta` | `obok zeszytu zamówień na Święto Dziękczynienia, który leżał otwarty` | clue: order book = zeszyt zamówień (the scene where Joyce copies the customers) |
| 418 | `Zanim koło spotkało się` | `Zanim krąg spotkał się` | consistency: the circle = krąg (Book 1 + rest of edition); this chapter switched to "koło" |
| 418 | `wszyscy w alei zdążyli się już niemal ochrypnięć` | `wszyscy na alei zdążyli się już niemal ochrypnąć` | typo: infinitive "ochrypnąć"; "na alei" |
| 418 | `Kobiety z koła zostawiły` | `Kobiety z kręgu zostawiły` | consistency: krąg |
| 419 | `pochylona nad swoimi ramami` | `pochylona nad swoimi stelażami` | consistency: wreath frame = "stelaż" (Ch1) |
| 419 | `na czele koła.` | `na czele kręgu.` | consistency: krąg |
| 421 | `w ciepłym środku koła` | `w ciepłym środku kręgu` | consistency: krąg |
| 421 | `świeżą ramę, a obok niej` | `świeży stelaż, a obok niego` | consistency: wreath frame = stelaż |
| 422 | `pod krzesłem Marty. Zanim rozmowa zdążyła się na dobre rozkręcić, Marta pochyliła` | `pod krzesłem Marthy. Zanim rozmowa zdążyła się na dobre rozkręcić, Martha pochyliła` | names: Martha (edition's dominant form, ×26; Book 1 also uses Martha) |
| 423 | `– Ciesz się, że się tym zajmujesz` | `– Cieszę się, że się tym zajmujesz` | reversed: "I'm glad you're looking into it" rendered as an imperative "Be glad" |
| 424 | `żeby koło nie zobaczyło` | `żeby krąg nie zobaczył` | consistency: krąg |
| 425 | `w stronę całego koła` | `w stronę całego kręgu` | consistency: krąg |
| 430 | `Dwadzieścia pięć lat temu. Daj spokój, mniej więcej.` | `Dwadzieścia pięć lat temu. Plus minus.` | mistranslation: "Give or take" ≠ "Daj spokój" (come on/leave it) |
| 432 | `żadna nie zamierzała ustąpić ani na cal. – Dot wzruszyła ramami.` | `żadna nie zamierzała ustąpić ani o krok. – Dot wzruszyła ramionami.` | units/typo: idiom "give an inch" → Polish idiom; "ramami" (frames) for "ramionami" (shoulders) |
| 436 | `Obejrzała koło.` | `Powiodła wzrokiem po kręgu.` | consistency: krąg; "looked around the circle" |
| 439 | `Połowa koła wydała z siebie cichy dźwięk, druga połowa zamilkla.` | `Połowa kręgu wydała z siebie cichy dźwięk, druga połowa milczała.` | consistency/typo: krąg; "zamilkla" typo |
| 442 | `Miejsce na jedną ciężarówkę, a chcą jej dwie.` | `Miejsce na jedną ciężarówkę, a chętnych dwoje.` | mistranslation: "two of them wanting it" (Pete and Greta), not "two [women] want it" |
| 443 | `Nasyłała na niego miasto. On na nią w sprawie szczurów przy jej koszach.` | `Nasłała na niego miasto. On nasłał je na nią w sprawie szczurów przy jej koszach.` | grammar: aspect; missing verb |
| 445 | `gdyby mi go pominęła` | `gdybym go pominęła` | grammar:  |
| 446 | `najlepsze kości na swoim pomoście` | `najlepsze kości na swojej rampie` | mistranslation: "dock" = loading dock (rampa), not a pier |
| 448 | `może to zrobił ktoś desperat` | `może to zrobił jakiś desperat` | grammar:  |
| 450 | `oto twój rzucający cegłami` | `oto ten, kto rzucił cegłą` | grammar: calque |
| 451 | `a koło uniosło wzrok` | `a krąg uniósł wzrok` | consistency: krąg |
| 453 | `na tym temat w koło się skończył` | `na tym temat w kręgu się skończył` | consistency: krąg |
| 455 | `a w koło rozlała się powszechna ulga` | `a po kręgu rozlała się powszechna ulga` | consistency: krąg |
| 455 | `ze ukradzioną puszką` | `z ukradzioną puszką` | typo:  |
| 458 | `chciał ostemplować ścianę` | `chciał oznaczyć ścianę` | mistranslation: "wanted the wall marked" |
| 458 | `żeby się tym podziwiać` | `żeby to podziwiać` | grammar:  |
| 458 | `partie towaru não musiały być` | `wypieki nie musiały być` | untranslated: Portuguese word "não" left in the Polish text ("didn't have to be"); "ruined batches" |
| 462 | `przytaknęła Marta` | `przytaknęła Martha` | names: Martha |
| 465 | `z miną pingwina, który czuje się głęboko ustatysfakcjonowany` | `z miną pingwina, któremu ogromnie pochlebiono` | mistranslation: "deeply flattered" ≠ "satisfied" |
| 467 | `a Marta zaśmiała się` | `a Martha zaśmiała się` | names: Martha |
| 468 | `upomniała dziecko Marta` | `upomniała dziecko Martha` | names: Martha |
| 473 | `od poręczy werandy` | `od poręczy ganku` | consistency: porch = "ganek" (Book 1 Polish dominant form) |
| 474 | `Nikt w kole nie wymienił` | `Nikt w kręgu nie wymienił` | consistency: krąg |
| 477 | `budynek wydawał się jeszcze o cal starszy i bardziej zniszczony` | `budynek wydawał się jeszcze bardziej zniszczony` | units: figurative "another inch" — imperial idiom dropped (safe) |
| 479 | `Zostawiłam Pipa w domu` | `Zostawiłam Pip w domu` | names: Pip is female; undeclined |
| 489 | `Chief Tanaka każe mi` | `Szefowa Tanaka każe mi` | untranslated: English title "Chief" left in Polish; edition's own form is "szefowa Tanaka" (×3) |
| 501 | `– Chief Tanaka kazała mi` | `– Szefowa Tanaka kazała mi` | untranslated: as above |
| 507 | `W tamtym roku drewno w cudzym składziku nie należało do nikogo, podobnie jak spiżarnia żadnej kobiety.` | `W tamtym roku niczyj stos drewna nie należał tylko do niego, niczyja spiżarnia tylko do niej.` | mistranslation: founder's note: "No man's woodpile his own that year, no woman's larder" = everything was shared; the Polish said someone else's wood belonged to nobody |
| 507 | `— E. Frost, jej ręka, 1809.` | `— E. Frost, własnoręcznie, 1809.` | mistranslation: "her hand" = signed in her own hand |
| 519 | `wydobyto je z zimnej ziemi spod trawnika` | `wydobyto je z zimnej ziemi spod skweru` | consistency: "under the green" = skwer |
| 519 | `ręcznie wypisane kartonowe zgłoszenie` | `ręcznie wypisany kartonik` | mistranslation: "a hand-lettered card"; "zgłoszenie" = an application/report |
| 527 | `nie zamierzał przywłaszczyć sobie ani cala gruntu` | `nie zamierzał przywłaszczyć sobie ani skrawka gruntu` | units: idiom "one inch of ground" |
| 533 | `Claire dowiedziała się o tym przed kolumną.` | `Claire wiedziała o tym przed kolacją.` | mistranslation: "Claire had it by suppertime"; "kolumna" (column) is wrong |
| 533 | `trafiła do Gazety` | `trafiła do Gazette` | consistency: paper name: edition's form is "Gazette" (undeclined) |
| 533 | `za ladą Staright przy kasie` | `za ladą Starlight przy kasie` | typo: café name |
| 533 | `BRUDNY` | `BRUDNE` | sign: same graffiti word as Ch4 (italic kept) |
| 541 | `łatającym cal po calu budynek` | `łatającym kawałek po kawałku budynek` | units: idiom "an inch at a time" |
| 541 | `piszącej, że w tamtym roku cudze drewno nie należało do nikogo` | `piszącej, że w tamtym roku niczyj stos drewna nie należał tylko do niego` | mistranslation: same founder line as [507] |
| 543 | `zaciągnę Nika, żeby` | `zaciągnę Nicka, żeby` | names: Nick → Nicka (edition's form) |
| 545 | `Ale przyciągną ludzi do środka` | `Ale przyciągnie ludzi do środka` | grammar: subject = the barrel (singular) |
| 545 | `nie będą potrafili tego odlyszeć` | `nie będą potrafili o tym zapomnieć` | typo: non-word "odlyszeć" ("un-hear") |
| 491 | `– Masz teraz słuch dozorcy, nie sklepikarza.` | `– Ma pan teraz słuch dozorcy, nie sklepikarza.` | address: ruling 2: Theo addresses Jessica formally ("pani Claus", EN "Mrs. Claus"); Jessica's one-sided "ty" made symmetric-formal |
| 491 | `Przyniosłam ci to. Przepis Grety, moje ręce. Więc nie oceniaj jej po nich.` | `Przyniosłam to panu. Przepis Grety, moje ręce. Więc niech pan nie ocenia jej po nich.` | address: ruling 2 (Theo formal both ways) |
| 497 | `– Co znalazłeś?` | `– Co pan znalazł?` | address: ruling 2 |
| 523 | `– To, co zrobiłeś, odnajdując ten napis` | `– To, co pan zrobił, odnajdując ten napis` | address: ruling 2 |
| 539 | `liczą się z każdym groszem` | `liczą się z każdym centem` | currency: dollars/cents only |
| 556 | `znajdowała się naprzeciwko skweru przy Evergreen Avenue` | `znajdowała się po drugiej stronie skweru, naprzeciw Evergreen Avenue` | mistranslation: EN "across the green from Evergreen Avenue" — the shop is NOT on Evergreen (this is why his meat comes through the shared yard) |
| 556 | `jak bardzo tamte porachunki wiążą jego problem z jej sprawą` | `jak bardzo to jedno podwórko wiąże jego kłopoty z jej kłopotami` | mistranslation: EN "how that one yard tied his trouble to hers" |
| 556 | `unikał się słaby, żelazny posmak` | `unosił się słaby, żelazny posmak` | typo:  |
| 556 | `z prószoną solą i pieprzem skroniami` | `ze skroniami przyprószonymi siwizną` | grammar: calque "salt-and-pepper", garbled |
| 560 | `niż ci się wydaje` | `niż się panu wydaje` | address: ruling 2: Pete is an acquaintance and addresses Jessica formally throughout — Jessica's "ty" made it one-sided |
| 560 | `w mieście, w którym masz swój sklep. Co masz dla dwóch osób` | `w mieście, w którym ma pan swój sklep. Co pan ma dla dwóch osób` | address: ruling 2 (Pete formal both ways) |
| 562 | `Obejszła ladę i zważył` | `Obszedł ladę i zważył` | gender/typo: Pete is male |
| 562 | `gdyby ostostało się tam coś` | `gdyby ostało się tam coś` | typo:  |
| 562 | `Stanęła przy ladze` | `Stanęła przy ladzie` | typo:  |
| 564 | `Zostawisz to w spokoju, co, jak słyszałem, jest dla pani najtrudniejsze` | `Zostawi to pani w spokoju, co, jak słyszałem, jest dla pani najtrudniejsze` | address: mixed ty/pani in one sentence |
| 564 | `Zwiążę to. Daj mi minutę.` | `Zwiążę to. Proszę dać mi minutę.` | address: Pete formal |
| 578 | `niż zadało sobie trud większość` | `niż zadała sobie trud większość` | grammar: agreement |
| 578 | `należy jej się przeprosina` | `należą jej się przeprosiny` | grammar: "przeprosiny" is plurale tantum |
| 584 | `– Tom mówi mi, że kręciłaś się w alei` | `– Tom mówi mi, że kręcił się pan w alejce` | gender/address: feminine "kręciłaś" for Pete; ruling 2 formal |
| 588 | `Nie zamierzam zostawiać swojej szafki otwartej` | `Nie zamierzam zostawiać swojego składu otwartego` | consistency: Pete's "cold-storage locker" = "skład chłodniczy" (Ch5); "szafka" = a cupboard. Kept distinct from Greta's walk-in and Joyce's "cold room" |
| 596 | `wcale nie byłem tam sam` | `wcale nie bywałem tam sam` | grammar: tense agreement with "kiedy jestem" |
| 596 | `Ktoś kręcił się z tyłu za jej domem.` | `Ktoś kręcił się z tyłu za jej sklepem.` | mistranslation: "around the back of hers" = her shop |
| 596 | `przy aptece z zgaszonymi światłami` | `przy aptece ze zgaszonymi światłami` | typo:  |
| 600 | `– Mówiłeś komuś o tym?` | `– Mówił pan komuś o tym?` | address: ruling 2 (Pete formal both ways) |
| 602 | `Cokolwiek robią tej kobiecie, to nie moja sprawa` | `Cokolwiek robią tej kobiecie, to nie ja to robię` | reversed: EN "I didn't do it"; Polish said "it's none of my business" |
| 604 | `gruby na sześć cali` | `gruby na piętnaście centymetrów` | units: 6 in → 15 cm |
| 606 | `Wmawiałem sobie, że to dostawców` | `Wmawiałem sobie, że to ślady dostawców` | grammar: missing noun |
| 606 | `rzeźnikiem z szafką na tyłach` | `rzeźnikiem ze składem na tyłach` | consistency: locker = skład |
| 612 | `Zostaw to w spokoju. I` | `Niech pani zostawi to w spokoju. I` | address: Pete formal |
| 612 | `powiesz jej, jeśli nadarzy się okazja, że nigdy nie dotknęłam jej okna` | `powie jej pani, jeśli nadarzy się okazja, że nigdy nie dotknąłem jej okna` | gender/address: Pete rendered female ("dotknęłam"); formal |
| 612 | `ludzie ci powiedzą` | `ludzie pani powiedzą` | address: Pete formal |
| 622 | `Gdybym szukała prostego rozwiązania dla kręgu podejrzeń, w jaki go ubrano i przewiązano sznurkiem: kłótnia, szafka, godziny przed świtem.` | `Gdybym szukała łatwego nazwiska dla kręgu, miałam go podanego jak na tacy i przewiązanego jego własnym sznurkiem: kłótnia, skład, godziny przed świtem.` | mistranslation: garbled; EN "If I had wanted an easy name for the circle he was gift-wrapped and tied with his twine" |
| 628 | `zobaczyć zieleniec` | `zobaczyć skwer` | consistency: the green = skwer |
| 632 | `O stopę, góra o dwie.` | `O trzydzieści centymetrów, góra o sześćdziesiąt.` | units: "A foot, perhaps two" (safe arithmetic, approximations kept) |
| 632 | `na zieleńcu stali` | `na skwerze stali` | consistency: skwer |
| 632 | `koło pomnika wojennego` | `koło pomnika weteranów` | consistency: war memorial = "pomnik weteranów" (Ch1) |
| 633 | `gdzie mógł stać żartowniś, żeby ulepić figurę` | `gdzie mógł stać żartowniś, żeby pchać figurę` | mistranslation: "stood to heave" (push it), not "to sculpt" |
| 644 | `przeszłam powoli zieleniec` | `obeszłam powoli skwer` | consistency: skwer |
| 646 | `W ogóle nie ruszył na zieleniec.` | `W ogóle nie ruszył na skwer.` | consistency: skwer |
| 646 | `tyłem do zaułka, ku któremu chyliły się wszystkie pozostałe` | `tyłem do Hollyhock Lane, ku której chyliły się wszystkie pozostałe` | mistranslation: "its back to the lane all the rest were leaning toward" = Hollyhock Lane (Nick's workshop), not the alley it faces — the Polish made the snowman face away from and toward the same alley |
| 646 | `Odszedł dobre dziesięć stóp` | `Odszedł dobre trzy metry` | units: 10 ft ≈ 3 m |
| 647 | `przy worku z mąką Grety` | `przy pojemniku na mąkę Grety` | mistranslation: "Greta's flour bin" (Ch2) — a key clue object |
| 655 | `Zebrały się na zieleńcu` | `Zebrały się na skwerze` | consistency: skwer |
| 656 | `z tą żałobną czułością` | `z tą pobłażliwą czułością` | mistranslation: "rueful tenderness"; "żałobny" = funereal |
| 656 | `Chodź, stanij przy nim.` | `Chodź, stań przy nim.` | typo:  |
| 657 | `Wielki kominkowy ruszt z polnych kamieni` | `Wielki kominek z okrągłych polnych kamieni` | mistranslation: "the great fireplace of round fieldstones" |
| 661 | `To jest dom, który dla tego buduję, żeby przestał pożyczać bałwany.` | `To jest dom, który dla niej buduję, żeby przestała pożyczać bałwany.` | grammar: referent = magia (feminine) |
| 661 | `Jeszcze lata dziczy przed nami` | `Jeszcze lata pracy przed nami` | typo: "dziczy" (wilderness) — nonsense here |
| 661 | `wozić dziecięce bałwany po ciemku` | `przestawiać dziecięce bałwany po ciemku` | mistranslation: "walking the snowmen around" |
| 663 | `i nie mogłam tak po prostu rzucić pośród tego zimnego, dziwnego faktu.` | `i nie mogłam wtrącić w sam środek tego wszystkiego zimnej, dziwnej wiadomości o jednym bałwanie.` | grammar: garbled clause, missing object |
| 671 | `której nie potrafiło jeszcze nazwać, a ja nie potrafiłam zrobić tego za nie` | `której nie potrafiła jeszcze nazwać, a ja nie potrafiłam zrobić tego za nią` | grammar: referent = magia (feminine) |
| 675 | `podczas gdy Pip badał okruchy` | `podczas gdy Pip badała okruchy` | gender: Pip is she/her |
| 684 | `pustężejącego sklepu` | `pustoszejącego sklepu` | typo:  |
| 685 | `Wcisnął termometr do chłodni i zapisał wynik.` | `Wcisnął termometr do gabloty chłodniczej i zapisał wynik.` | consistency: "cold-case" (display fridge) ≠ the walk-in; "chłodnia" is reserved for the walk-in (Varney/Joyce clue pair) |
| 685 | `Pip trzymał się okruchów pod ladą i pozwalał mu` | `Pip trzymała się okruchów pod ladą i pozwalała mu` | gender: Pip she/her |
| 687 | `BRUDNY` | `BRUDNE` | sign: same graffiti word as Ch4 (italic kept) |
| 689 | `A woda ma temperaturę o dwa stopnie niższą niż przewidują normy.` | `A woda ma temperaturę o dwa stopnie poniżej normy.` | clue: "two degrees under code" — one fixed wording used at all three places (Ch9, Ch20 recap, Ch26); Fahrenheit figure kept (decision) |
| 695 | `a Pip szedł za nami` | `a Pip szła za nami` | gender: Pip she/her |
| 698 | `zanim jeszcze postawiłam stopę w środku` | `zanim jeszcze postawiłem stopę w środku` | gender: Varney (male) rendered female |
| 700 | `gdy usłyszały słowa „pomieszczenie chłodnicze”` | `gdy padły słowa „zimny pokój”` | grammar/clue: hands cannot hear; cold room = "zimny pokój" (see [698]) |
| 701 | `BRUDNY` | `BRUDNE` | sign: same graffiti word (italic kept) |
| 702 | `kobiety z kółka dziewiarskiego` | `kobiety z kręgu` | consistency: the circle = krąg |
| 704 | `z przeznaczeniem do kosza z żywnością` | `z przeznaczeniem do beczki na żywność` | consistency: Hal's food-drive "barrel" = beczka (Ch3, Ch6) |
| 704 | `dopóki Hal miał wolny kosz do napełnienia` | `dopóki Hal miał beczkę do napełnienia` | consistency: barrel = beczka |
| 705 | `Pakowaliśmy ostatnie bułeczki` | `Pakowałyśmy ostatnie bułeczki` | gender: Jessica and Greta (two women) |
| 707 | `Pip potuptał przez podłogę` | `Pip potuptała przez podłogę` | gender: Pip she/her |
| 709 | `Pip został przy drzwiach` | `Pip została przy drzwiach` | gender: Pip she/her |
| 710 | `Potem Pip i ja wyszliśmy na Aleję Wiecznie Zieloną` | `Potem Pip i ja wyszłyśmy na Evergreen Avenue` | consistency/gender: street name translated only here ("Aleja Wiecznie Zielona") — edition keeps "Evergreen Avenue"; Pip female |
| 712 | `Hal zabrał pudełko bułeczek do kosza.` | `Hal zabrał pudełko bułeczek do beczki.` | consistency: barrel = beczka |
| 714 | `odsunęły ją w swoich umysłach o cal od poczucia bezpieczeństwa` | `odsunęły ją w swoich umysłach o krok dalej od poczucia bezpieczeństwa` | units: idiom "one inch further from safe" |
| 715 | `z Pipem tuż przy pięcie` | `z Pip tuż przy pięcie` | names: Pip female, undeclined |
| 698 | `Nazwała chłodnię „pomieszczeniem chłodniczym”, jakby to była nazwa własna, a zlew umywalkowy „zlewem Hobarta”.` | `Nazwała chłodnię „zimnym pokojem”, jakby to była nazwa własna, a zlew umywalkowy „zlewem Hobarta”.` | clue: Joyce's giveaway word "the cold room" must be ONE homely phrase used identically in Ch9, Ch20 and the recaps, and different from the walk-in (chłodnia). Ch20 had swapped them (cold room = "chłodnia", walk-in = "mroźnia"), which destroyed the slip |
| 719 | `Druga rzekła: – Cóż, w tym roku są tak daleko w tyle, a zdesperowani ludzie robią zdesperowane rzeczy. Pierwsza odparła: – Nic nie mówię. Odszły` | `Druga rzekła: „Cóż, w tym roku są tak daleko w tyle, a zdesperowani ludzie robią zdesperowane rzeczy”. Pierwsza odparła: „Nic nie mówię”. Odeszły` | dialogue/typo: overheard speech embedded in a narration paragraph: dossier wants „…” inside narration, not mid-paragraph dialogue dashes; "Odszły" typo |
| 727 | `weil łatwiej przetrawić` | `bo łatwiej przetrawić` | untranslated: German word "weil" left in the Polish |
| 731 | `Ale pakuła trafia` | `Ale paczka trafia` | mistranslation: "pakuła" = oakum; "a box goes out" |
| 731 | `cała nieśmiałość z niego ufrunęła` | `cała nieśmiałość z niego uleciała` | typo: non-word |
| 741 | `– Jak najlepiej – powiedziałam jej przy furtce. – To dumni ludzie. Nie gapi się.` | `– Zachowuj się jak najlepiej – powiedziałam jej przy furtce. – To dumni ludzie. Nie gapimy się.` | grammar: "Best behavior… We don't stare" — fragment and wrong person |
| 751 | `Anne Doucette nie miała zamiaru być biedna tylko przed panią Claus, i to nie kosztem reszty dobrej herbaty, którą mogła na to poświęcić.` | `Anne Doucette nie zamierzała być przed panią Claus jedynie biedna, choćby miało ją to kosztować resztkę dobrej herbaty.` | reversed: EN "not if it cost her the last of the good tea to prevent it" — she spends the tea; Polish said she would NOT spend it |
| 761 | `– Za kogo, twoim zdaniem, nas mają?` | `– A co pani zdaniem mówią?` | address/mistranslation: ruling 2: Anne is a new acquaintance and calls Jessica "pani" → formal both ways; EN "What do you think they're saying?" (Jessica's question, not "us") |
| 763 | `– Wie pani, za kogo. –` | `– Wie pani, co mówią. –` | mistranslation: follows the corrected question: "You know what they're saying" |
| 763 | `niemal bezgoryczowym grymasie` | `grymasie niemal pozbawionym goryczy` | typo: non-word |
| 767 | `są zbyt dobrzy, by popełnić błąd` | `są zbyt dobrzy, by zrobić coś złego` | mistranslation: "to do a wrong" (a wrongdoing), not "make a mistake" |
| 769 | `Spsuło trzy ciasta` | `Zepsuło trzy ciasta` | typo:  |
| 785 | `Hal zamknął swój notes.` | `Hal zamknął swój rejestr.` | consistency: Hal's "book" = rejestr in the previous paragraph |
| 787 | `żeby kupić to, co ją sfałszowało` | `żeby kupić to, co ją zakwasiło` | mistranslation: "whatever soured it"; "sfałszować" = to forge/adulterate (and pre-empts the reveal) |
| 789 | `– To małe kółko – stwierdził Hal.` | `– To wąski krąg – stwierdził Hal.` | consistency: "small circle" — keeps the circle word (krąg) and Polish idiom |
| 798 | `by zatrzymać to, czemu mój nos – jak ufałam – nie pozwoliłby się zbliżyć.` | `by zatrzymać to, do czego nie chciał się zbliżyć nos, któremu ufałam.` | mistranslation: EN "keep what a nose I trusted would not go near" — Pip's nose, not Jessica's |
| 801 | `czyniło go zarazem miejskim aptekarzem` | `czyniło go zarazem miejskim chemikiem` | mistranslation: "chemist" = analyst here (he runs tests); "aptekarz" = pharmacist (the town has a separate pharmacy) |
| 801 | `trzymał niską ławkę z wagą` | `trzymał niski stół roboczy z wagą` | mistranslation: "bench" = workbench (later "stół") |
| 807 | `spalił szczyptę w naczynisku` | `spalił szczyptę w naczynku` | typo:  |
| 807 | `Papier zczerwieniał` | `Papierek poczerwieniał` | typo:  |
| 809 | `– Pukał w słoik.` | `– Postukał w słoik.` | grammar: aspect |
| 810 | `– W takim razie zmarnowałam panu popołudnie` | `– W takim razie zmarnowałam ci popołudnie` | address: Doc and Jessica are on first names ("Jessica", "Doc") and use ty everywhere else; one stray "pan" |
| 813 | `Mlekowy to ten sam kwas, który kwaśne mleko.` | `Mlekowy to ten sam kwas, który zakwasza mleko.` | grammar: missing verb |
| 813 | `żeby natchnąć chleb żytni i kanapkowy nutą zakwasu bez samego zaczynu` | `żeby nadać chlebom żytnim i delikatesowym nutę zakwasu bez samego zaczynu` | mistranslation: "natchnąć" = to inspire; "rye and deli loaves" |
| 813 | `żeby celowo zrujnować sto funtów mąki` | `żeby celowo zrujnować czterdzieści pięć kilogramów mąki` | units: 100 lb → 45 kg (accurate figure, per the Flour Play French ruling and the 2026-08-11 round-number ruling) |
| 819 | `z półki u kolonialnego kupca` | `z półki w sklepie spożywczym` | mistranslation: "off a grocer's shelf"; "kupiec kolonialny" is archaic |
| 819 | `To pasowało do pisemnego zgłoszenia, w którym powoływano się na paragrafy, do ręki, która znała na pamięć kod do zlewu.` | `To pasowało do wydrukowanej skargi, w której powoływano się na podpunkty, do ręki, która znała na pamięć normę dla zlewu umywalkowego.` | consistency: "the typed complaint that cited the sub-clauses" (Ch9 wording: wydrukowana, podpunkty); "code" = regulation, not a PIN "kod"; hand-sink = zlew umywalkowy |
| 823 | `Szłam w dół ku zielonemu skwerkowi` | `Szłam w dół ku skwerowi` | consistency: the green = skwer |
| 823 | `zamiast pochylać się ku zielonemu skwerkowi wraz z resztą` | `zamiast pochylać się ku skwerowi wraz z resztą` | consistency: skwer |
| 825 | `patrzyłam tam, gdzie ona patrzyła` | `patrzyłam tam, gdzie on patrzył` | grammar: referent = the snowman |
| 825 | `Stawał przez dwa dni, patrząc na tę aleję` | `Stał przez dwa dni, patrząc na tę alejkę` | mistranslation: "that alley" (alejka, the back alley) — "aleja" is Evergreen Avenue |
| 835 | `który tkwił przy piecach od świtu` | `który tkwił przy piecach od ciemnej nocy` | reversed: EN "since dark" — she bakes from 4 a.m., before light; "od świtu" (since dawn) contradicts the open-door-in-the-dark logic |
| 836 | `Wymieszać go jej własną łopatką.` | `Wymieszać go jej własną szufelką.` | consistency: Greta's scoop = szufelka (Ch2) |
| 840 | `Szeroka w sam raz na jedną furgonetkę i ani cala więcej. Szyłam nią` | `Szeroka w sam raz na jedną furgonetkę i ani trochę więcej. Szłam nią` | units/typo: inch idiom; "Szyłam" (sewed) for "Szłam" |
| 840 | `Chłodnia Pete'a, stare pomieszczenie` | `Skład chłodniczy Pete'a, stare pomieszczenie` | consistency: Pete's locker = skład chłodniczy; "chłodnia" is reserved for Greta's walk-in (clue pair with Joyce's "cold room") |
| 840 | `wyparte na jasny kolor wokół klamki` | `wytarte do jasności wokół klamki` | typo: "wyparte" (displaced) for "wytarte" (worn) |
| 842 | `jej samy, pługu` | `jej samej, pługu` | typo:  |
| 843 | `mógł ustać dokładnie w tym miejscu` | `mógł stanąć dokładnie w tym miejscu` | grammar: "ustać" = to remain standing |
| 856 | `rzeźnik z zapleczem u dostawców` | `rzeźnik mający konto u dostawcy` | mistranslation: "a butcher on a supplier's books" |
| 856 | `kto stał w tych drzwiach tak bezczelnie pewnie` | `kto stał w tych drzwiach tak wyraźnie` | mistranslation: "squarely in the door" — "bezczelnie" (insolently) adds an accusation not in the English |
| 858 | `Zmusić człowieka do przejścia obok dowodów dostępu to znacznie trudniejsza sprawa.` | `Przy dostępie znacznie trudniej oczyścić człowieka z podejrzeń.` | mistranslation: "Access is a harder thing to walk a man past" (to clear him past) |
| 859 | `Wyszłam z alejki na ulicę Evergreen` | `Wyszłam z alejki na Evergreen Avenue` | consistency: street name |
| 867 | `a Pipa jako ciepły ciężar` | `a Pip jako ciepły ciężar` | names: Pip female, undeclined |
| 867 | `kto mógł stać na tamtym parapecie` | `kto mógł stać na tamtym progu` | mistranslation: the door "sill" = próg (Ch12); "parapet" = window sill |
| 871 | `ponieważ Pip spał zbyt mocno, by go angażować` | `ponieważ Pip spała zbyt mocno, by ją angażować` | gender: Pip she/her |
| 873 | `odróżnienie kwaśnego zaczynu od odrobiny kredy` | `odróżnienie kwaśnej bazy od odrobiny kredy` | clue: "sour base" must be ONE term (kwaśna baza) and never a sourdough-starter word ("zaczyn") |
| 873 | `jak mnie rozbięcie tuszy` | `jak mnie rozebranie tuszy` | typo:  |
| 877 | `a tym razem pominęłam myśli „chyba”` | `a tym razem pominęłam „nie sądzę”` | consistency: echoes Ch7 "Nie sądzę, żeby to zrobił" (EN "I don't think") |
| 881 | `Zostawiłam Pipa śpiącego na ciepłych cegłach` | `Zostawiłam Pip śpiącą na ciepłych cegłach` | gender: Pip she/her |
| 883 | `odłożył nóż płasko, stawiając go na baczność, tak jak wtedy` | `odłożył nóż płasko i zesztywniał, tak jak wtedy` | mistranslation: "braced" describes Pete, not the knife |
| 885 | `– Nie będę ci przerywać pracy – rzekłam. – Przyszłam ci powiedzieć, że brałam cię pod uwagę.` | `– Nie będę panu przerywać pracy – rzekłam. – Przyszłam panu powiedzieć, że brałam pana pod uwagę.` | address: ruling 2: Pete formal both ways (Ch7) |
| 885 | `że o świcie jesteś na tym podwórku` | `że o świcie jest pan na tym podwórku` | address: ruling 2 |
| 885 | `wyłożyć człowieku całą` | `wyłożyć człowiekowi całą` | typo: dative |
| 885 | `– Oraz przyszłam ci powiedzieć, że wykreśliłam cię z powrotem.` | `– Oraz przyszłam panu powiedzieć, że wykreśliłam pana z powrotem.` | address: ruling 2 |
| 885 | `a ty nie masz ani jednego, ani drugiego. Kłócisz się w samo południe i rąbasz mięso. To do ciebie nie pasuje.` | `a pan nie ma ani jednego, ani drugiego. Kłóci się pan w samo południe i rąbie mięso. To do pana nie pasuje.` | address: ruling 2 |
| 889 | `– Nie przyszłaś tu chyba po to, żeby mi słodzić, stara znachorko.` | `– Nie przyszła pani tu chyba po to, żeby słodzić staremu zrzędzie.` | mistranslation/address: "an old grouch" is Pete describing HIMSELF; Polish turned it into an insult to Jessica ("old quack-woman"); formal |
| 891 | `– Przyszłam powiedzieć ci, że ci ufam.` | `– Przyszłam powiedzieć panu, że panu ufam.` | address: ruling 2 |
| 895 | `– I to jakiej – odparł.` | `– Owszem, jest – odparł.` | grammar: "It is [a novelty]" |
| 895 | `Jesteś jedyną osobą` | `Jest pani jedyną osobą` | address: ruling 2 |
| 895 | `W takim razie weźmiesz kotlet. Bez dyskusji. Nie pozwolę ci płacić i kropka.` | `W takim razie weźmie pani kotlet. Bez dyskusji. Nie pozwolę pani płacić i kropka.` | address: ruling 2 |
| 899 | `– Ta sylwetka, o której ci mówiłem` | `– Ta sylwetka, o której pani mówiłem` | address: ruling 2 |
| 899 | `Pewnie będziesz chciała wiedzieć o tym wszystko, skoro mi uwierzyłaś.` | `Pewnie będzie pani chciała wiedzieć o tym wszystko, skoro mi pani uwierzyła.` | address: ruling 2 |
| 903 | `– I ścigałeś to – powiedziałam. – Tamtych ranków. Nie tylko to widziałeś.` | `– I przeganiał pan to – powiedziałam. – Tamtych ranków. Nie tylko pan to widział.` | address: ruling 2 |
| 905 | `Nie dlatego, że ją uwielbiam, uwierz mi.` | `Nie dlatego, że ją uwielbiam, niech mi pani wierzy.` | address: ruling 2 |
| 905 | `Nhưng ktoś skradający się` | `Ale ktoś skradający się` | untranslated: Vietnamese word "Nhưng" (= but) left in the Polish |
| 905 | `– Nikomu jej tego nie mówiłem.` | `– Jej też tego nie mówiłem.` | mistranslation: EN "I never told her that either" — "Nikomu jej" is ungrammatical and changes the sense |
| 909 | `– Jesteś lepszym sąsiadem, niż wskazywałaby na to wasza kłótnia` | `– Jest pan lepszym sąsiadem, niż wskazywałaby na to pańska kłótnia` | address: ruling 2 |
| 911 | `– Nawet – rzekł, czerwieniąc się – nie waż się komukolwiek mówić, że to powiedziałaś.` | `– Niech pani – rzekł, czerwieniąc się – nikomu nie mówi, że pani to powiedziała.` | address: ruling 2 |
| 917 | `czując, że świat stał się uboższy o jednego porządnego człowieka, choć nie uważałam tego za stratę` | `z polem podejrzeń węższym o jednego porządnego człowieka, i nie uważałam tego za stratę` | mistranslation: EN "the field gone narrower by one good man" (one fewer suspect) — Polish said the world was poorer by one good man |
| 923 | `dowiedzieli się od dzieciaków z placu` | `dowiedzieli się od dzieciaków ze skweru` | consistency: the green = skwer |
| 924 | `kręcący się po placu po zmroku` | `kręcący się po skwerze po zmroku` | consistency: skwer |
| 927 | `Greta zastygła, gdy wypowiedziała jego imię.` | `Greta zastygła, gdy wypowiedziałam jego imię.` | mistranslation: "when I said his name" — wrong person |
| 928 | `– Odeszła od larsu... zaszła ladę z drugiej strony. –` | `– Wyszła zza lady. –` | untranslated: machine-translation debris ("larsu…" self-correction) printed in the prose; EN "She came around the counter." |
| 928 | `namalował słowo SRAKA na mojej ścianie` | `namalował słowo BRUDNE na mojej ścianie` | mistranslation: DIRTY rendered as a vulgarity ("SRAKA" = shit); the graffiti word is BRUDNE everywhere else |
| 940 | `Niech pani zapyta Państwa Petersenów` | `Niech pani zapyta państwa Petersenów` | typo: lowercase "państwa" |
| 941 | `Nie psikasz słów na ścianę w nocy, a zarazem nie odmierzasz mąki łopatką aptekarza.` | `Nikt nie psika w nocy słów na ścianę, a zarazem nie dozuje proszku do mąki z dokładnością chemika.` | mistranslation: EN "dose flour by the scoop to a chemist's measure" (the same hand wouldn't do both); Polish said "measure flour with a pharmacist's shovel" |
| 947 | `– No to zachowaj to dla siebie – powiedziałam` | `– No to nie wypuszczaj tego z pamięci – powiedziałam` | reversed: "Hold onto it… and bring it to me" — "zachowaj to dla siebie" means "keep it to yourself", contradicting "bring it to me" |
| 950 | `His... Jego matka wyszła do drzwi` | `Jego matka wyszła do drzwi` | untranslated: English/MT debris "His..." in the prose |
| 951 | `– Twój Danny nie malował tej ściany, pani Ott.` | `– Pani Danny nie malował tej ściany, pani Ott.` | address: mixed ty/pani in one sentence to Mrs Ott (new acquaintance → formal) |
| 952 | `wypuściła długie powietrze` | `wypuściła powietrze długim wydechem` | grammar:  |
| 955 | `ponieważ kosz Hala na ciepłe ubrania opróżniono` | `ponieważ beczkę Hala na ciepłe ubrania opróżniono` | consistency: barrel = beczka |
| 955 | `Stojaki pozostały więc w zapleczu` | `Stelaże pozostały więc na zapleczu` | consistency: wreath frames = stelaże |
| 964 | `– Jego matka karm... karmiła obiadem` | `– Jego matka karmiła obiadem` | untranslated: MT stutter debris ("karm...") — Dot does not stammer in the English |
| 965 | `rozmowy o Dannym Otte w kręgu` | `rozmowy o Dannym Otcie w kręgu` | names: locative of Ott |
| 978 | `część do miejskiego pługa śnieżnego` | `część do miejskiej odśnieżarki` | mistranslation: "snowblower" |
| 981 | `Druty w rękach Marty zwolniły tempo. – Powiedz jej, że nadal chcę moje dwa czekoladowo-orzechowe ciastka` | `Druty w rękach Marthy zwolniły tempo. – Powiedz jej, że nadal chcę moje dwa placki czekoladowo-orzechowe` | names/mistranslation: Martha; "two chocolate-pecans" are the PIES (the disputed recipe), not cookies |
| 984 | `O dziewiątej pudło na kosz Hala` | `O dziewiątej pudło do beczki Hala` | consistency: barrel = beczka |
| 984 | `Pip ułożyła na niej podbródkiem i zamknęła oczy.` | `Pip wsunęła ją sobie pod podbródek i zamknęła oczy.` | grammar: garbled; "tucked it under her chin" |
| 933 | `Znalazłam Danny'ego Otta na placu` | `Znalazłam Danny'ego Otta na skwerze` | consistency: the green = skwer |
| 987 | `Salka w Grange została otworzona dla obu zbiórek naraz` | `Świetlica została otwarta dla obu zbiórek naraz` | consistency: the Grange hall = "świetlica" throughout (Ch1 "w Gminie" was a mistranslation; mixed "Grange"/"salka" here); "otworzona" non-standard |
| 990 | `pod tylne drzwi Grange cofnął się` | `pod boczne drzwi świetlicy cofnął się` | consistency/mistranslation: Grange = świetlica; EN "side door" |
| 993 | `Spojrzały na skrzynki` | `Spojrzał na skrzynki` | grammar: Hal (singular, male) |
| 994 | `Jest tego więcej, skąd to się wzięło.` | `Tam, skąd to przyszło, jest tego więcej.` | grammar: garbled idiom |
| 1000 | `stało otwarte na boku od października` | `stało otwarte na bocznym stoliku od października` | mistranslation: "on its side table", not "on its side" |
| 1000 | `z garścią wczesnych ofiar na dnie` | `z garścią wczesnych darów na dnie` | mistranslation: "ofiara" also means victim/sacrifice; "offerings" = dary |
| 1000 | `karteczką z przepisem Grety na ciastka czekoladowo-orzechowe` | `karteczką z przepisem Grety na placek czekoladowo-orzechowy` | mistranslation: the chocolate-pecan is the PIE (the disputed recipe; Ch26 card) |
| 1000 | `Tego ranka Theo zniósł ją do Grange` | `Tego ranka Theo zaniósł ją do świetlicy` | consistency: Grange = świetlica |
| 1000 | `Do zepieczętowania, gdy stara zostanie otwarta` | `Do zapieczętowania, gdy stara zostanie otwarta` | typo:  |
| 1001 | `którą uknułam dla niej w październiku` | `którą zrobiłam dla niej na drutach w październiku` | mistranslation: "uknuć" = to plot/scheme; "knit" |
| 1003 | `Hal podeszła i stanął obok mnie` | `Hal podszedł i stanął obok mnie` | gender: Hal is male |
| 1007 | `na tablicy ogłoszeń w Grange pomiędzy rozkładami orki a spotkaniami kościelnymi` | `na tablicy ogłoszeń w świetlicy pomiędzy harmonogramami odśnieżania a kolacjami parafialnymi` | mistranslation: "plow schedules" = snowplough (Ch1 "harmonogram odśnieżania"), not ploughing fields; "church suppers" |
| 1008 | `Wtorek, 10 listopada do niedzieli, 15 listopada.` | `od wtorku 10 listopada do niedzieli 15 listopada.` | grammar: date range (italic kept) |
| 1009 | `gdzie sekretarz z Grange ostemplowała kartkę` | `gdzie sekretarka świetlicy ostemplowała kartkę` | consistency: Grange = świetlica; female secretary |
| 1009 | `Zdjąłem ją, żeby się upewnić. POSTED i data.` | `Zdjęłam ją, żeby się upewnić. WYWIESZONO i data.` | gender/sign: Jessica rendered male; stamp text "POSTED" left in English (ruling 3) |
| 1011 | `zostało zawieszone do odwołania z powodu konieczności dokonania poprawek` | `zostało zawieszone do czasu usunięcia uchybień` | consistency: echo of Varney's exact phrase (Ch9 "do czasu usunięcia uchybień") |
| 1011 | `Może dłużej, jeśli części do zlewu nie przyjdą.` | `Może dłużej, jeśli części do zlewu nie dotrą na czas.` | consistency: verbatim echo of Varney's line in Ch9 |
| 1017 | `czym jest finansjerka` | `czym jest financier` | mistranslation: "finansjerka" = the financial elite; the cake (financier) as elsewhere in the edition |
| 1025 | `z jego ławki pośród brązowych butelek.` | `znad jego stołu pośród brązowych butelek.` | mistranslation: "bench" = his work table (Ch11) |
| 1025 | `Wysuszony kwas. Ktoś to tam wrzucił. I wiedział dokładnie, ile wrzucić.` | `Suszony kwas. Ktoś to tam włożył. I dokładnie wiedział, ile wsypać.` | clue: Jessica recalls Doc's exact words — must match Ch11 verbatim (italic kept) |
| 1026 | `Doktor powiedział, że piekarnia nie miałaby pożytku z tego świństwa w kubełku Grety.` | `Doktor powiedział, że cukiernia nie miałaby pożytku z tego świństwa w pojemniku Grety.` | clue: EN "a pastry kitchen" (Ch11 "Cukiernia") — the distinction bakery vs pastry kitchen is the deduction (a BREAD kitchen buys sour base); flour bin = pojemnik |
| 1027 | `Motyw był ode mnie od pierwszego dnia` | `Motyw był przede mną od pierwszego dnia` | typo:  |
| 992 | `U hodowcy świń dostałabym za nie grosze.` | `U hodowcy świń dostałabym za nie parę centów.` | currency: dollars/cents only ("pennies") |
| 1011 | `na żółtym powiatowym papierze` | `na żółtym papierze z hrabstwa` | consistency: county = hrabstwo |
| 1013 | `człowiek z powiatu` | `człowiek z hrabstwa` | consistency: county = hrabstwo |
| 1041 | `Kobiety z koła przyozdabiały` | `Kobiety z kręgu przyozdabiały` | consistency: krąg |
| 1041 | `by wyłapać, na czym spoczęło zaklęcie` | `by wyłapać, co kryło się pod tym urokiem` | mistranslation: "the charm" = her charm (urok), not a magic spell ("zaklęcie") — misleading in a book with real magic |
| 1043 | `zatrzymała się na zamczonym progu` | `zatrzymała się na zamiecionym progu` | typo: "swept step" |
| 1043 | `wzięła do inspekcji kapsla, którego znalazła w rynsztoku` | `zabrała się do oględzin kapsla, który znalazła w rynsztoku` | grammar:  |
| 1047 | `– Przyszłaś zobaczyć, jak go przyozdobiono.` | `– Przyszła pani zobaczyć, jak go przyozdobiono.` | address: ruling 2: Renée addresses Jessica formally in this scene ("Pani Claus", "z pani strony", "Nie widziała pani") — stray ty-forms aligned |
| 1049 | `Koło robi wieńce na drzwiach` | `Krąg robi wieńce na drzwi` | consistency: krąg |
| 1053 | `Zmierz więc drzwi i zostań na kawę.` | `Niech pani więc zmierzy drzwi i zostanie na kawę.` | address: ruling 2 (Renée formal) |
| 1055 | `Zmierzłam więc drzwi` | `Zmierzyłam więc drzwi` | typo:  |
| 1059 | `W cenach dla wieśniaków.` | `Po wiejskich cenach.` | mistranslation: "At country prices" — "dla wieśniaków" (for yokels) is an insult not in the English |
| 1063 | `Zlew gospodarczy podłączony jest do starej rury i brakuje ci dwóch stopni do normy, a dowiadujesz się o tym dopiero` | `Zlew umywalkowy działa na starej rurze, woda jest o dwa stopnie poniżej normy, a człowiek dowiaduje się o tym dopiero` | clue: Renée must name the three faults in Varney's exact words: hand-sink = "zlew umywalkowy" (not "gospodarczy", a utility sink) and "o dwa stopnie poniżej normy" (identical ×3) |
| 1067 | `Zlew gospodarczy na starych rurach, brakuje mu dwóch stopni do normy.` | `Zlew umywalkowy na starej rurze, o dwa stopnie poniżej normy.` | clue: same three-fault echo; identical clue wording |
| 1067 | `jak wymieniała je pisana na maszynie skarga` | `jak wymieniała je wydrukowana skarga` | consistency: "the typed complaint" (Ch9: przyszła wydrukowana) |
| 1069 | `Raport wstępny należał do Grety` | `Decyzja tymczasowa należała do Grety` | consistency: "the provisional" = decyzja tymczasowa (Varney, Ch9) |
| 1075 | `i ani o cal bliższa czemukolwiek` | `i ani o krok bliższa czemukolwiek` | units: inch idiom |
| 1077 | `– Znasz się świetnie na kuchniach` | `– Zna się pani świetnie na kuchniach` | address: ruling 2 (Renée formal both ways) |
| 1079 | `– To mój fachy.` | `– To mój fach.` | typo:  |
| 1083 | `Wiedza o fudze to nie rozsypywanie trucizny.` | `Wiedza o fudze to nie wsypywanie proszku.` | no-poison: EN "Knowing the grout was not pouring the powder" — "trucizna" (poison) is not in the English (no-poison edition) |
| 1085 | `– Przyślę wieniec do piątku – rzekłam` | `– Wieniec zawiśnie do piątku – rzekłam` | mistranslation: "I'll have your wreath up by Friday" — she hangs it herself (Ch16 end), she does not send it |
| 1093 | `Wracaliśmy wzdłuż alei` | `Wracałyśmy wzdłuż alei` | gender: Jessica and Pip (both female) |
| 1095 | `Ale potrzebowałbym czegoś` | `Ale potrzebowałabym czegoś` | gender: female narrator rendered male |
| 1097 | `do obręczy drzwi Sugarplum` | `do obręczy na drzwi Sugarplum` | grammar: "the hoop for Sugarplum's door" |
| 1059 | `kościelne podwieczorki` | `kolacje parafialne` | consistency: "church suppers" (one rendering) |
| 1099 | `na ławce w parku Danny Ott` | `na ławce na skwerze Danny Ott` | consistency: the green = skwer |
| 1099 | `żeby mi je przynieósł` | `żeby mi je przyniósł` | typo:  |
| 1100 | `zupełnie jak w parku` | `zupełnie jak na skwerze` | consistency: skwer |
| 1101 | `Cokolwiek powiedziałaś pani Bennett, rozeszło się.` | `Cokolwiek pani powiedziała pani Bennett, rozeszło się.` | address: ruling 2: children address adults formally (Danny uses "pani" in Ch14) |
| 1101 | `Wiem, że to byłaś ty.` | `Wiem, że to była pani.` | address: ruling 2 |
| 1104 | `jeśli ktoś jeszcze raz wywoła twoje imię` | `jeśli ktoś jeszcze raz wspomni twoje nazwisko` | grammar:  |
| 1104 | `Pilnujesz tego parku po zmroku.` | `Pilnujesz tego skweru po zmroku.` | consistency: skwer |
| 1108 | `Pokwitał głową` | `Pokiwał głową` | typo:  |
| 1109 | `Ta, którą kazałaś mi zachować.` | `Ta, którą kazała mi pani zachować.` | address: ruling 2 |
| 1109 | `kiedy świeci światło nad magazynem Pete'a` | `kiedy świeci światło nad składem Pete'a` | consistency: Pete's locker = skład |
| 1111 | `– Był taki poranek, kiedy widziałam kogoś` | `– Był taki poranek, kiedy widziałem kogoś` | gender: Danny (boy) rendered female |
| 1111 | `Zgubiłam ją za światłem przy aptece.` | `Zgubiłem ją za światłem przy aptece.` | gender: Danny |
| 1113 | `Powiedziałaś, żeby mi to przynieść, gdy stanie się wyraźne.` | `Powiedziała pani, żebym to przyniósł, gdy stanie się wyraźne.` | address/grammar: ruling 2; garbled "żeby mi to przynieść" |
| 1121 | `spojrzał na słoik weck, który postawiłam` | `spojrzał na słoik do przetworów, który postawiłam` | consistency: "the preserving jar" (Ch2 "słoik po przetworach"); brand word "weck" |
| 1122 | `Na wypadek, gdybyśmy się mylili.` | `Na wypadek, gdybym się myliła.` | mistranslation: EN "In case I'm wrong" |
| 1126 | `wymieniła mi fugę, uszczelkę i zlewozmywak` | `wymieniła mi fugę, uszczelkę i zlew umywalkowy` | clue: the three faults keep Varney's words (hand-sink = zlew umywalkowy) |
| 1128 | `Nie policją i nie musi ci niczego pokazywać.` | `Nie policjantem, a ona nie musi ci niczego pokazywać.` | grammar:  |
| 1136 | `– Twice in one day, Mrs. Claus – powiedziała. – And you've brought the veterinarian. Is the wreath unwell?` | `– Dwa razy jednego dnia, pani Claus – powiedziała. – I przyprowadziła pani weterynarza. Czyżby wieniec zachorował?` | untranslated: whole line of Renée's dialogue left in English |
| 1137 | `– Czy mogłybyśmy porozmawiać na zapleczu?` | `– Czy moglibyśmy porozmawiać na zapleczu?` | gender: Jessica and Doc (mixed group) |
| 1138 | `rzuciła słowo do swojej dziewczyny` | `rzuciła słowo do swojej pomocnicy` | mistranslation: "her girl" = her shop assistant (Ch9), not "girlfriend" |
| 1140 | `Kwas piekarniczy, dość mocny` | `Kwas z piekarni chleba, dość mocny` | clue: EN "A bread kitchen's acid" — the bread-vs-pastry distinction carries the deduction |
| 1140 | `Dziś rano wymieniłaś mi fugę, uszczelkę i zlew` | `Dziś rano wymieniła mi pani fugę, uszczelkę i zlew umywalkowy` | address/clue: ruling 2 (Renée formal both ways); hand-sink wording |
| 1140 | `Przyszłam więc zapytać cię wprost. To byłaś ty?` | `Przyszłam więc zapytać panią wprost. Czy to była pani?` | address: ruling 2 |
| 1142 | `czy sabotażowałam mąkę` | `czy sabotowałam mąkę` | typo:  |
| 1144 | `– Patrz pani zatem. Obejrzyj to wszystko. A potem stąd wyjdziecie.` | `– Proszę więc patrzeć. Proszę obejrzeć wszystko. A potem państwo stąd wyjdą.` | address: mixed ty/pani in one line |
| 1145 | `Worki mąki z młyna w Portland` | `Worki mąki z hurtowni w Portland` | mistranslation: "the Portland house" = the bulk house (Ch3 hurtownia) |
| 1146 | `Szczypta na pięćdziesiąt funtów.` | `Szczypta na dwadzieścia trzy kilogramy.` | units: 50 lb ≈ 22.7 kg (accurate, rounded as a native writer would) |
| 1146 | `Wiadro kwaśnego rozczynu poczułoby się` | `Wiadro kwaśnej bazy poczułoby się` | clue: sour base = ONE term "kwaśna baza"; "rozczyn" is a sourdough/leaven word (forbidden) |
| 1149 | `podczas gdy ja stałam przy stosie spłaszczonych kartonów, czekając przy tylnych drzwiach na kubeł – złote etykiety i cała reszta.` | `podczas gdy ja stałam przy stosie spłaszczonych kartonów, czekających przy tylnych drzwiach na wywóz – ze złotymi etykietami i całą resztą.` | mistranslation: it is the CARTONS (with gold labels — a clue echo) that wait by the back door, not Jessica |
| 1150 | `Żadnego kwaśnego rozczynu.` | `Żadnej kwaśnej bazy.` | clue: sour base = kwaśna baza |
| 1154 | `Odesłała segregator od Doca` | `Odebrała segregator od Doca` | typo:  |
| 1157 | `– Dziękuję, że nam to pokazałaś` | `– Dziękuję, że nam to pani pokazała` | address: ruling 2 |
| 1158 | `tak samo, jak wtedy, gdy wchodziłyśmy` | `tak samo, jak wtedy, gdy wchodziliśmy` | gender: Jessica and Doc |
| 1167 | `Byłam pewna od czasu spotkania w Grange` | `Byłam pewna od czasu zbiórki w świetlicy` | consistency: Grange = świetlica |
| 1167 | `nigdy w życiu nie topzyła czekolady` | `nigdy w życiu nie topiła czekolady` | typo:  |
| 1168 | `w jednej chwili wybaczyłam Joyce to, czego odmawiałam Renée przez cały tydzień` | `w jednej chwili dałam Joyce to, czego przez cały tydzień odmawiałam Renée` | mistranslation: "given Joyce in a breath" (the benefit of the doubt) — not "forgave" |
| 1171 | `Przy pomniku wojennym Pip` | `Przy pomniku weteranów Pip` | consistency: war memorial = pomnik weteranów |
| 1171 | `Zjechałam za nią powolną metodą, na własnych nogach.` | `Zeszłam za nią powoli, na własnych nogach.` | mistranslation: "I went down after her the slow way, on my feet" — she walks, not slides |
| 1172 | `zdejmowałam jodłowe gałązki z koła po jednej, aż przede mną nie zostało nic oprócz gołej stalowej ramy` | `zdejmowałam jodłowe gałązki z obręczy po jednej, aż przede mną nie zostało nic oprócz gołego stalowego stelaża` | consistency: ring = obręcz, frame = stelaż (Ch1/Ch16) |
| 1174 | `Mróz nadszedł bez ostrzeżenia, co do pogody, jak Dot powtarzała mi, że te tęgie zawsze robią.` | `Mróz nadszedł bez żadnej zapowiedzi w pogodzie, tak jak według Dot zawsze nadchodzą te najcięższe.` | grammar: garbled sentence |
| 1174 | `okna zmrożone w białe paprocie aż po rogach` | `okna zmrożone w białe paprocie aż po rogi` | grammar:  |
| 1174 | `budynku Towarzystwa na placu` | `budynku Towarzystwa przy rynku` | consistency: "the square" = rynek (Ch6 "przy rynku"); "plac" was also used for the green |
| 1178 | `Żadnego zaskoczenia, żadnego słabego, letniego podmuchu pchanego w górę schodów.` | `Tym razem nie zaskoczył; żaden słaby, letni podmuch nie popłynął w górę schodów.` | mistranslation: "No catch" = the boiler did not catch/ignite (Ch6 "Potem zaskoczył"), not "no surprise" |
| 1178 | `zanim cokolwiek dowiedziało się, że ogień zgasł` | `zanim ktokolwiek dowiedział się, że ogień zgasł` | grammar:  |
| 1180 | `na ćwierć cala w poprzek desek` | `na pół centymetra w poprzek desek` | units: quarter-inch ≈ 6 mm (safe) |
| 1180 | `zadowolona z stojącej wody` | `zadowolona ze stojącej wody` | typo:  |
| 1181 | `Powzeka do wiosny.` | `Powie: zaczekajmy do wiosny.` | typo: non-word |
| 1182 | `Leżało bezpiecznie sześć czystych stóp dalej` | `Leżało bezpiecznie dobre dwa metry dalej` | units: 6 ft ≈ 1.8 m (safe) |
| 1183 | `pudło z cedru zapełniające się w Grange, nazwisko założyciela w każdym oknie` | `pudło z cedru zapełniające się w świetlicy, słowa założycielki w każdym oknie` | consistency/mistranslation: Grange = świetlica; "the founder's line" = Eliza Frost's words (female founder), not "the founder's name" |
| 1184 | `zapasy Renée otwarte dla Doc półka po półce` | `zapasy Renée otwarte dla Doca półka po półce` | grammar: declension |
| 1184 | `Podsypany kubeł mąki i skarga pisana na maszynie` | `Zaprawiony pojemnik z mąką i wydrukowana skarga` | consistency: "dosed flour bin" (bin = pojemnik); "typed complaint" (Ch9) |
| 1188 | `gdy robił coś ze swoimi nitami` | `gdy pracował nad swoimi gwoździkami` | consistency: "his brads" = gwoździki (Ch6) |
| 1188 | `Noc była bardzo mroczna.` | `Noc była bardzo mroźna.` | mistranslation: "very cold", not "very dark" |
| 1199 | `Zdejmę jednak płaszcz` | `Zdjęłam jednak płaszcz` | grammar: tense |
| 1203 | `wróciłam ze Stowarzyszenia` | `wróciłam z Towarzystwa` | consistency: the Historical Society = Towarzystwo throughout |
| 1221 | `a to była nasza przeszkoda przed nami` | `i to był nasz kwartał ulic` | mistranslation: "the block" = the city block, not an obstacle |
| 1223 | `– Cegła – zacząłem. – Miała stary, szary zaprawowy tynk na jednym licu` | `– Cegła – zaczęłam. – Miała starą, szarą zaprawę na jednym licu` | gender/mistranslation: female narrator rendered male; "mortar" |
| 1223 | `leży śnieg od Wszystkich Świętych` | `leży śnieg od Halloween` | consistency: EN "since Halloween" (as everywhere else) |
| 1223 | `Postawiłam wiecznicę od cukiernicy za pieprzniczką. – W kontenerze za posiadłością Fenwicków` | `Postawiłam pokrywkę od cukiernicy za pieprzniczką. – W kontenerze za dawnym lokalem Fenwicków` | typo/consistency: non-word "wiecznica" (lid); "the Fenwick place" = lokal (Ch1) |
| 1231 | `wyliczyła mi kościelne festyny tego miasta` | `wyliczyła mi kolacje parafialne tego miasta` | consistency: "church suppers" (Ch15) |
| 1243 | `Puknęłam w wiecznicę cukiernicy` | `Puknęłam w pokrywkę cukiernicy` | typo:  |
| 1247 | `nosząca pudry do pracy w pudełku z nazwiskiem sklepu z boku` | `niosąca proszek do roboty w pudełku z nazwą sklepu na boku` | mistranslation: "carrying her powder" ("pudry" = face powders) |
| 1247 | `Uwierzylabym w to` | `Uwierzyłabym w to` | typo:  |
| 1253 | `Raz na swoim osiedlu, nad twoją pieczenią.` | `Raz przy swoim pniaku, nad twoją pieczenią.` | mistranslation: "at his block" = butcher's block, not a housing estate |
| 1253 | `Nie od mięsarza.` | `Nie dostawcy mięsa.` | consistency: "the meat man" (Ch7 "dostawca mięsa") |
| 1257 | `powiedział, że to nie mięsarza` | `powiedział, że to nie dostawca mięsa` | consistency: meat man |
| 1257 | `pod parapetem Grety` | `pod progiem Grety` | mistranslation: door sill = próg |
| 1257 | `Słyszałam o złoconym sklepie.` | `Usłyszałam w tym złoty sklep.` | mistranslation: "I heard the gold shop" — she read the gold shop into his words |
| 1261 | `Ale po cholerę jej furgonetka?` | `Ale po co jej w ogóle furgonetka?` | register: no swearing in the English |
| 1261 | `zejść pod parapet Grety` | `zejść pod próg Grety` | mistranslation: door sill |
| 1261 | `Furgonetka z zgaszonymi światłami` | `Furgonetka ze zgaszonymi światłami` | typo:  |
| 1269 | `– Rankiem, kiedy wszyscy szli, reszta poszła na zieleńce i pochyliła się wzdłuż alei w stronę twojego paleniska. Ten jeden poszedł w drugą stronę, dziesięć stóp od ich kompanii` | `– Tego ranka, kiedy wszystkie ruszyły, reszta poszła na skwer i pochyliła się ku Hollyhock Lane, w stronę twojego paleniska. Ten jeden poszedł w drugą stronę, trzy metry od ich kompanii` | mistranslation/units: the snowmen leaned "up the lane" (Hollyhock Lane), not along the avenue; green = skwer; 10 ft ≈ 3 m |
| 1281 | `Odsuwałam miskę. – Przeczytałam to w Grange` | `Odsunęłam miskę. – Przeczytałam to w świetlicy` | grammar/consistency: aspect; Grange = świetlica |
| 1289 | `Od schodków w Grange miałam to na opak.` | `Od schodków świetlicy miałam to na opak.` | consistency: Grange = świetlica |
| 1295 | `Jej dziewczyna za ladą.` | `Jej pomocnica za ladą.` | mistranslation: "her girl at the counter" = shop assistant |
| 1310 | `Dwa pekanowe z czekoladą i tuzin bułek` | `Dwa placki czekoladowo-orzechowe i tuzin bułek` | consistency: "two chocolate-pecans" = the pies (one rendering; Ch14) |
| 1316 | `widziałam furgonetkę przed domem` | `widziałam furgonetkę przed sklepem` | mistranslation: "out front" of the shop |
| 1324 | `Sama wpisałam to w zeszyt Grety` | `Sama wpisałam to do zeszytu Grety` | grammar:  |
| 1328 | `Widziałam ją ranka z witryną, gdy wokół trwało sprzątanie` | `Widziałam ją tamtego ranka, kiedy wybito szybę, gdy wokół trwało sprzątanie` | grammar: "the morning of the window" |
| 1346 | `– Zlew jeszcze nie dotarł – powiedziała` | `– Część do zlewu jeszcze nie dotarła – powiedziała` | mistranslation: "The sink part still hasn't come" |
| 1346 | `Nie mam ci do tego nic dać.` | `Nie mam ci nic do tego podać.` | grammar:  |
| 1356 | `Dodałaś ten zeszyt komuś?` | `Dawałaś ten zeszyt komuś?` | typo: "Dodałaś" (added) for "dawałaś" (gave) |
| 1360 | `Dwa pekanowe z czekoladą i tuzin bułek. Ivy też dostała, z trzema dyniowymi.` | `Dwa placki czekoladowo-orzechowe i tuzin bułek. Ivy też dostała, z trzema dyniowymi.` | consistency: the pies |
| 1372 | `Odeszła od lady i ciężko opadła` | `Wyszła zza lady i ciężko opadła` | mistranslation: "came around the counter" |
| 1374 | `powiedział „chłodnia”.` | `powiedział „zimny pokój”.` | clue: the cold room = "zimny pokój" (Joyce's word, Ch9) |
| 1378 | `To jest mroźnia. Zawsze była mroźnią dla Harolda` | `To jest chłodnia. Zawsze była chłodnią dla Harolda` | clue: walk-in = "chłodnia" (Ch9, Ch17); "mroźnia" is a freezer |
| 1378 | `Joyce nazywała to chłodnią. Mówiła: idę do chłodni, Greto` | `Joyce nazywała ją zimnym pokojem. Mówiła: idę do zimnego pokoju, Greto` | clue: Joyce's word must differ from the walk-in word or the slip disappears |
| 1378 | `nazywała go zlewiskiem Hobarta` | `nazywała go zlewem Hobarta` | clue: "the Hobart sink" = "zlew Hobarta" (Ch9) |
| 1378 | `Mówiłam mroźnia. Zmuszałam się do tego.` | `Mówiłam chłodnia. Zmuszałam się do tego.` | clue: walk-in = chłodnia |
| 1382 | `– Pete mówi, że zamek w bramie na podwórko znowu wam odpada` | `– Pete mówi, że twoja kłódka ciągle spada z bramy na podwórko` | consistency: padlock = kłódka (Ch5, Ch7); "your lock" |
| 1384 | `Zostawiam go otwartego niektóre ranka i z powrotem zapinam na łańcuch. Myślałam, że to on. Robi to na złość. Zdejmuje go, żeby` | `Niektórymi rankami zastaję ją otwartą i z powrotem zapinam na łańcuchu. Myślałam, że to on. Robi to na złość. Zdejmuje ją, żeby` | reversed: "I find it hanging open" — Polish said Greta herself leaves it open |
| 1386 | `– Ile jest kluczy do tego zamku? – Dwa. Nie musiała się nad tym zastanawiać. – Jeden jest na moim kółku.` | `Zapytałam, ile jest kluczy do tej kłódki. – Dwa – odparła bez zastanowienia. – Jeden jest na moim kółku.` | dialogue: two speakers had been merged into one paragraph with no attribution; rebuilt (paragraph count unchanged) |
| 1386 | `To ten sam zamek, który wisiał na tej bramie, odkąd Harold ją powiesił. Nigdy go nie zmieniałam.` | `To ta sama kłódka, która wisi na tej bramie, odkąd Harold ją tam zawiesił. Nigdy jej nie zmieniałam.` | consistency: padlock = kłódka; "Harold ją powiesił" read as "Harold hanged the gate" |
| 1392 | `Tamtego ranka z oknem.` | `Tamtego ranka, kiedy wybito szybę.` | grammar:  |
| 1398 | `a zmyłam ją wczoraj wieczorem i postawiłam przy drzwiach, żeby jej oddać. – Nie spojrzała na naczynie. – Zamierzałam sama zawieźć ją do Bridgton.` | `a wczoraj wieczorem umyłam naczynie i postawiłam je przy drzwiach, żeby jej oddać. – Nie spojrzała na naczynie. – Zamierzałam sama zawieźć je do Bridgton.` | grammar: referent = the dish (neuter), not the casserole |
| 1386 | `kiedy odszła, a ja` | `kiedy odeszła, a ja` | typo:  |
| 1425 | `Rozdział dwudziesty pierwszy` | `Rozdział 21` | heading: the only spelled-out chapter heading — the pre-flight read Ch21 as MISSING because of it; body is complete. Same number, digits like every other heading (not a renumbering) |
| 1430 | `Gdyby jakaś piekarnia szukała zakwasu, gdzie by go zamówiła?` | `Gdyby jakaś piekarnia chleba szukała kwaśnej bazy, gdzie by ją zamówiła?` | clue: sour base = kwaśna baza, never "zakwas" (sourdough starter); "a bread kitchen" |
| 1435 | `Opowiedzę ci po co` | `Powiem ci po co` | typo: non-word |
| 1443 | `to prawie zawsze właściciel. Otworzyła kolejne okno` | `to prawie zawsze właściciel. – Otworzyła kolejne okno` | dialogue: missing dash before resumed narration |
| 1444 | `Rankiem po incydencie z witryną stała na alei` | `Tamtego ranka, gdy wybito szybę, stała na alei` | mistranslation: "the morning of the window", not the morning after |
| 1447 | `białą tablicą stanu Maine z górzakiem` | `białą tablicą stanu Maine z sikorką` | mistranslation: "chickadee" = sikorka; "górzak" is not a word |
| 1450 | `Drukarka uruchomiła się z zgrzytem` | `Drukarka uruchomiła się ze zgrzytem` | typo:  |
| 1455 | `– Mówiłeś mi, że na samym końcu przy aptece stał zaparkowany samochód z zgaszonymi światłami.` | `– Mówił mi pan, że na samym końcu przy aptece stała zaparkowana furgonetka ze zgaszonymi światłami.` | address/consistency: ruling 2 (Pete formal); "a van" (furgonetka), not a car |
| 1457 | `– Pukał w tablicę rejestracyjną.` | `– Postukał w tablicę rejestracyjną.` | grammar: aspect |
| 1458 | `– Powiedziałbyś to szefowej?` | `– Powiedziałby pan to szefowej?` | address: ruling 2 |
| 1461 | `Warknął. – Uczciwie. – Spojrzałam za siebie na Pip, która wciąż stała w jego trocinach. – Powiedz jej, że dopiero to zmiotłem.` | `Mruknął. – Uczciwie. – Spojrzał ponad mną na Pip, która wciąż stała w jego trocinach. – Niech jej pani powie, że dopiero to zmiotłem.` | mistranslation/address: it is PETE who looks past Jessica at Pip; ruling 2 |
| 1463 | `W domu Nick rozpalil w piecu, a zupa mrugała na fajerkach.` | `W domu Nick rozpalił w piecu, a zupa grzała się na brzegu blachy.` | typo/mistranslation: "rozpalil" typo; "mrugała" (blinked) |
| 1466 | `– Doktor znalazł zakwas w mące Grety` | `– Doktor znalazł kwaśną bazę w mące Grety` | clue: sour base term |
| 1466 | `Holly Jolly Bakery. A firma` | `Holly Jolly. A firma` | consistency: EN "Holly Jolly orders" |
| 1466 | `– Czy może pani sprawdzić, czy Pelkey z Lewiston dostarczył tej jesieni zakwas do Wendt's Bakehouse?` | `– Czy możesz sprawdzić, czy Pelkey z Lewiston dostarczył tej jesieni kwaśną bazę do Wendt's Bakehouse?` | address/clue: ruling 2: Noriko and Jessica are on first names/informal since Inn Trouble Ch24–26 (Noriko already uses ty here); sour base term |
| 1475 | `Worek zakwasu co kilka tygodni` | `Worek ich kwaśnej bazy co kilka tygodni` | clue: sour base term ("a sack of their sour base") |
| 1480 | `– Octan sodu to ocet wysuszony na soli` | `– Dioctan sodu to ocet wysuszony na soli` | clue: sodium DIacetate (as on the product sheet just quoted) |
| 1481 | `położył w nim świeży pasek papierka lakmusowego` | `położył w nim świeży pasek papierka pH` | consistency: pH paper (Ch11) |
| 1483 | `po czym oderwał stronę i mi ją poddał` | `po czym oderwał stronę i podał mi ją` | typo: "poddał" (surrendered) |
| 1492 | `wypowiedziała nazwisko Renée w sali społecznej` | `wypowiedziała nazwisko Renée w jakiejś sali` | mistranslation: "in a hall" (any hall) |
| 1503 | `leżał już na jej podkładce na biurko` | `leżał już na jej podkładce na biurku` | typo:  |
| 1505 | `– Księga zamówień Grety na Święto Dziękczynienia leżała otwarta na jej ladzie` | `– Zeszyt zamówień Grety na Święto Dziękczynienia leżał otwarty na jej ladzie` | clue: order book = zeszyt zamówień |
| 1505 | `z ofertą przejęcia ich zamówień dla Holly Jolly. Co do pojedynczych ciast.` | `z ofertą przejęcia ich zamówień z Holly Jolly. Łącznie z plackami.` | mistranslation: "Down to the pies" |
| 1507 | `– W skardze chłodnię nazwano chłodnym pomieszczeniem, a zlew kuchenny zlewem Hobarta.` | `– W skardze chłodnię nazwano zimnym pokojem, a zlew umywalkowy zlewem Hobarta.` | clue: recap must use the same giveaway words as Ch9/Ch20 (walk-in = chłodnia, cold room = zimny pokój, hand-sink = zlew umywalkowy, Hobart sink = zlew Hobarta) |
| 1507 | `Zamek w bramie na podwórko nigdy nie był wymieniany, a Pete twierdzi, że wciąż z niego spada.` | `Kłódki na bramie podwórka nigdy nie wymieniono, a Pete twierdzi, że ciągle spada z łańcucha.` | consistency: padlock = kłódka; "it keeps coming off" (the lock itself) |
| 1507 | `więc kto wie, czy sprawca nie wchodził tędy. Widział furgonetkę` | `więc sprawca wchodził właśnie tędy. Pete widział furgonetkę` | mistranslation: EN states it ("whoever did it was coming in that way"); Polish hedged it. Missing subject made "He saw a van" read as the culprit |
| 1509 | `przy oknie Grety przed świtem` | `przy progu Grety przed świtem` | mistranslation: "at Greta's sill" = the back-door sill |
| 1509 | `który Greta darła w sierpniu` | `który Greta podarła w sierpniu` | grammar: aspect |
| 1509 | `leżała w próbkach na jej ladzie przez cały październik` | `leżała jako próbny wydruk na jej ladzie przez cały październik` | mistranslation: "lay in proof" (a printer's proof) |
| 1509 | `Ulotka nie pojawiła się na tablicy w Grange aż do trzydziestego. Worek Pelkeya trafił do Bridgton dwugodzinnego... dwudziestego siódmego. A notatka Doktora mówi, że proszek w moim słoiku pasuje do kwasu bazowego, test po teście.` | `Ulotka nie pojawiła się na tablicy w świetlicy aż do trzydziestego. Worek Pelkeya trafił do Bridgton dwudziestego siódmego. A notatka Doktora mówi, że proszek w moim słoiku pasuje do kwaśnej bazy, test po teście.` | clue/untranslated: MT debris "dwugodzinnego..." printed in the key date sentence; sour base term ("kwas bazowy" a third variant); Grange = świetlica |
| 1511 | `Kwas bazowy, jeden worek, dostarczony` | `Kwaśna baza, jeden worek, dostarczona` | clue: invoice line "Sour base, one sack" |
| 1513 | `Telefony. Słowa. Zamek. Furgonetka.` | `Telefony. Słowa. Kłódka. Furgonetka.` | consistency: padlock |
| 1518 | `Skąd się wzięło, jest prawdopodobne, nie udowodnione.` | `Skąd się wzięła, jest prawdopodobne, nie udowodnione.` | grammar: referent = cegła |
| 1518 | `Złoty na etykiecie, tak mówiłaś.` | `Ze złotem na etykiecie, tak mówiłaś.` | grammar:  |
| 1519 | `ponieważ byłam jej winna tę szczerzość` | `ponieważ byłam jej winna tę szczerość` | typo:  |
| 1532 | `Potem odwróciła stronę Claire` | `Potem sięgnęła po kartkę od Claire` | mistranslation: "turned to Claire's page" |
| 1533 | `Chcieli tej działki, z inwentarzem, całym dobytkiem i nazwą.` | `Chcieli wszystkiego, z całym dobytkiem i szyldem.` | mistranslation/consistency: "the lot, lock, stock and name" — "the lot" = everything (not a plot of land); echoes Ch2 "z całym dobytkiem i szyldem" |
| 1539 | `– Greta...` | `– Greto...` | grammar: vocative |
| 1540 | `– Siedziałam przy sąsiedniej ławce z tą kobietą przez piętnaście lat.` | `– Pracowałam przy sąsiednim stole z tą kobietą przez piętnaście lat.` | mistranslation: "the next bench" = work bench (15 years together — partnership figure) |
| 1548 | `Kiedy Tanaka odkładała telefon i napisała` | `Kiedy Tanaka odłożyła telefon i napisała` | grammar: aspect |
| 1537 | `Nie musisz być w pokoju. Większość ludzi na twoim miejscu` | `Nie musi pani być w pokoju. Większość ludzi na pani miejscu` | address: ruling 2: a police interview at the station is a professional scene → Tanaka formal with Greta (as with Joyce) |
| 1539 | `– Greto...` | `– Pani Greto…` | address: ruling 2: first name kept as in the English, with formal address |
| 1542 | `Nie musisz odezwać się ani słowem, chyba że będziesz chciała.` | `Nie musi się pani odzywać ani słowem, chyba że będzie pani chciała.` | address: ruling 2 |
| 1544 | `W takim razie usiądziesz tam, gdzie ona cię zobaczy` | `W takim razie usiądzie pani tam, gdzie ona panią zobaczy` | address: ruling 2 |
| 1553 | `Wyszczerbiony czajnik został przyniesiony` | `Wgnieciony czajnik został przyniesiony` | consistency: "the dented kettle" (Ch22 "z wgnieceniem") |
| 1559 | `Obejściem stołu ruszyła w jej stronę` | `Obeszła stół, kierując się w jej stronę` | grammar:  |
| 1561 | `w śród których` | `wśród których` | typo:  |
| 1565 | `odsunęła kółko o kilka cali poza zasięg` | `odsunęła pęk o kilka centymetrów poza zasięg` | units: inches → cm; "ring" of keys = pęk (as in the line above) |
| 1577 | `– W piątek wieczorem twoja piekarnia zadzwoniła do dwóch klientek Grety – powiedziała Tanaka – oferując realizację ich zamówień na święta, słowo w słowo zgodnie z notesem Grety. Siedziałaś przy tym notesie w poranek wybicia szyby z wyciągniętym telefonem.` | `– W piątek wieczorem pani piekarnia zadzwoniła do dwóch klientek Grety – powiedziała Tanaka – oferując realizację ich zamówień z Holly Jolly, słowo w słowo według zeszytu Grety. Siedziała pani przy tym zeszycie tego ranka, gdy wybito szybę, z telefonem w ręku.` | address/clue: ruling 2: a police interview is formal (Tanaka opened with "pani"); order book = zeszyt zamówień; "Holly Jolly orders" |
| 1581 | `– W skardze złożonej w hrabstwie jej pomieszczenie gospodarcze nazwano komorą chłodniczą, a zlew – zlewem firmy Hobart. Greta twierdzi, że nikt tak ich nie nazywał od czasów, gdy ty tam byłaś.` | `– W skardze złożonej w hrabstwie jej chłodnię nazwano zimnym pokojem, a zlew umywalkowy zlewem Hobarta. Greta twierdzi, że nikt tak ich nie nazywał od pani czasów.` | clue/address: the confrontation must use the SAME giveaway words: walk-in = chłodnia, cold room = zimny pokój, hand-sink = zlew umywalkowy, Hobart sink = zlew Hobarta (Polish had a 4th and 5th variant: "pomieszczenie gospodarcze", "komora chłodnicza"); formal |
| 1583 | `– Połowa piekarzy w moim wieku mówi komora chłodnicza.` | `– Połowa piekarzy w moim wieku mówi „zimny pokój”.` | clue: Joyce repeats the giveaway phrase |
| 1585 | `– Doktor Mitchell dopasował proszek w jej mące do bazy zakwasowej. Pelkey dostarczył ci worek takowej dwudziestego siódmego października, po miesiącach przerwy. Podpisałaś pokwitowanie.` | `– Doktor Mitchell dopasował proszek w jej mące do kwaśnej bazy. Pelkey dostarczył pani worek tej bazy dwudziestego siódmego października, po miesiącach przerwy. Podpisała pani pokwitowanie.` | clue/address: sour base term (never a sourdough "zakwas" word); formal |
| 1587 | `– Piekę żytni, szefowo.` | `– Piekę chleb żytni, szefowo.` | grammar:  |
| 1587 | `Każdy piekarz żytni w Nowej Anglii kupuje bazę zakwasową.` | `Każdy piekarz chleba żytniego w Nowej Anglii kupuje kwaśną bazę.` | clue: sour base term |
| 1589 | `jest zarejestrowana na ciebie.` | `jest zarejestrowana na panią.` | address: formal |
| 1589 | `To ta furgonetka, którą tu dzisiaj przyjechałaś.` | `To ta furgonetka, którą pani tu dzisiaj przyjechała.` | address: formal |
| 1593 | `– Ktoś przeszedł przez furtkę na moim podwórku – powiedziała Greta.` | `– Ktokolwiek to był, wszedł przez bramę na moje podwórko – powiedziała Greta.` | mistranslation: "Whoever it was came in through my yard gate" (the gate = brama, Ch5/7/20) |
| 1595 | `odkąd Joyce wszła` | `odkąd Joyce weszła` | typo:  |
| 1597 | `– Pete ma na tej furtce swój łańcuch` | `– Pete ma na tej bramie swój łańcuch` | consistency: gate = brama |
| 1601 | `dziób uniósł się o cal` | `dziób uniósł się odrobinę` | units: inch |
| 1603 | `zaśmiała się, krótko i bezciepliwie` | `zaśmiała się, krótko i bez cienia ciepła` | typo: non-word |
| 1613 | `– To ciasto było moje.` | `– Ten placek był mój.` | consistency: "the pie" = placek (Ch20 "ten placek"); one rendering of the motif |
| 1617 | `– To ciasto było moje. Opracowałam je przy tym stole, podczas pierwszej zimy, posługując się przepisem na ciasto pekanowe mojej matki i funtem czekolady` | `– Ten placek był mój. Opracowałam go przy tym stole, podczas pierwszej zimy, z placka pekanowego mojej matki i pół kilo czekolady` | consistency/units: pie motif; "a pound of chocolate" ≈ 0.45 kg (rounded idiomatically) |
| 1617 | `Nazwę nad drzwiami. To ciasto.` | `Nazwę nad drzwiami. Placek.` | consistency: pie motif |
| 1617 | `po czekoladowo-pekanowe Grety. W tym pudełku w Grange jest kartka z przepisem. Wsadzają go do ziemi. Przeczytałam to` | `po placek czekoladowo-orzechowy Grety. W tym pudełku w świetlicy jest kartka z przepisem. Wsadzają ją do ziemi. Przeczytałam ją` | consistency: pie name (Ch5, Ch14, Ch15); Grange = świetlica; referent = the card |
| 1621 | `o czwartej rano masz już dość ciasta` | `masz już dość placków o czwartej rano` | consistency: pie motif |
| 1631 | `Nie zrobiłam tego. To jest moje.` | `Nie zrobiłam tego. To moja wina.` | mistranslation: "That one's mine" = that fault is mine |
| 1631 | `Nie pomyślałam o tobie. To też jest moje.` | `Nie pomyślałam o tobie. To też moja wina.` | mistranslation: as above |
| 1635 | `– Ale nie zrobiłaś tego dla ciasta` | `– Ale nie zrobiłaś tego dla placka` | consistency: pie motif |
| 1635 | `Zadzwoniłaś do Marty.` | `Zadzwoniłaś do Marthy.` | names: Martha |
| 1635 | `każde nazwisko z tego notesu` | `każde nazwisko z tego zeszytu` | clue: order book = zeszyt zamówień |
| 1639 | `Cztery wypieki.` | `Cztery partie.` | mistranslation: "Four batches" |
| 1649 | `– To ciasto nadal było moje – oświadczyła.` | `– Ten placek nadal był mój – oświadczyła.` | consistency: pie motif |
| 1659 | `z zamówieniami z notesu, do którego nie miała pani prawa zaglądać` | `z zamówieniami z zeszytu, do którego nie miała pani prawa zaglądać` | clue: order book |
| 1659 | `oraz dwoma kobietami` | `oraz dwiema kobietami` | grammar:  |
| 1665 | `bezszelestnie odnalazła właściwy klucz` | `bez patrzenia odnalazła właściwy klucz` | mistranslation: "found the key without looking" |
| 1673 | `człapała z powrotem pod stół` | `poczłapała z powrotem pod stół` | grammar: aspect |
| 1573 | `i polubiłam ją w Grange z ramionami` | `i polubiłam ją w świetlicy z ramionami` | consistency: Grange = świetlica |
| 1684 | `Chodzi o mąkę, o to kwaśne ciasto, które wrzuciła, żeby zepsuć cztery partie ciasta Grety. Do tego dochodzi wybita szyba. W niedzielę sama przyniosła tę cegłę z zaplecza Grety w zaułku i przyłożyła ją do gruzu wciąż leżącego w kontenerze za Sugarplum. Ta sama stara czerwona cegła, z tą samą szarą zaprawą po jednej stronie. Farba` | `Chodzi o mąkę, o kwaśną bazę, którą wsypała, żeby zepsuć cztery partie ciasta Grety. Do tego dochodzi wybita szyba. – W niedzielę sama zaniosła alejką cegłę z półki na zapleczu Grety i przyłożyła ją do gruzu wciąż leżącego w kontenerze za Sugarplum. Ta sama stara czerwona cegła, z tą samą szarą zaprawą na jednym licu. – Farba` | clue/dialogue: "the sour base she put in it" rendered "kwaśne ciasto" (sour dough); the narration sentence about the brick had been fused into Tanaka's speech (she spoke of herself in the 3rd person) — dashes restored |
| 1688 | `Skarga. Chłodnia i zlew z Hobart, opisane i wysłane do hrabstwa` | `Skarga. Zimny pokój i zlew Hobarta, wydrukowane i wysłane do hrabstwa` | clue: "The cold room and the Hobart sink, typed up" — the cold room is Joyce's word, not the walk-in |
| 1692 | `– Nie, nie po kolacji.` | `– Nie dłużej niż do kolacji.` | mistranslation: "Not past supper" |
| 1692 | `a ja ją wylegitymowałem... to znaczy wylegitymowałam – ucięła, poprawiając się w duchu – a komisarz` | `a ja ją zatrzymałam i spisałam, a komisarz` | untranslated: machine-translation self-correction printed as prose (male form, then "I mean…", then an invented tag "ucięła, poprawiając się w duchu"); EN "and I booked her" |
| 1696 | `grozi jej więżenie` | `grozi jej więzienie` | typo:  |
| 1696 | `O to, o co prosić będzie biuro prokuratora okręgowego, to odszkodowanie.` | `To, o co poprosi biuro prokuratora okręgowego, to odszkodowanie.` | grammar:  |
| 1696 | `Za każdą zepsutą torbę mąki i za szybę. Oraz za wszystko, co Greta straciła, stojąc z zamkniętymi drzwiami w Święto Dziękczynienia.` | `Za każdy zepsuty worek mąki i za szybę. Oraz za wszystko, co Greta straciła, stojąc zamknięta tuż przed Świętem Dziękczynienia.` | mistranslation: "sack"; "with Thanksgiving coming" (before, not on, the holiday) |
| 1698 | `– Ona trzyma każdą – powiedziałam.` | `– Ona trzyma każdy – powiedziałam.` | grammar: referent = rachunek (m.) |
| 1702 | `Wendt ma stanową licencję` | `Wendt's ma stanową licencję` | mistranslation: "Wendt's" = the bakery business |
| 1706 | `Zakwas to żywność.` | `Kwaśna baza to żywność.` | clue: sour base term (never "zakwas") |
| 1706 | `Ich menedżer ds. żywienia zadzwonił do mnie, odkąd tylko otworzyłam drzwi` | `Ich kierowniczka ds. żywienia zadzwoniła do mnie, gdy tylko otworzyłam drzwi` | gender/grammar: EN "told HER"; "odkąd" (since) for "as soon as" |
| 1716 | `Bûches de Noël. Orders taken until December 20.` | `Bûches de Noël. Zamówienia przyjmujemy do 20 grudnia.` | sign: ruling 3: English sign text left untranslated (French product name kept, as in the English) |
| 1736 | `Dziękuję, że przyszła mi to powiedzieć.` | `Dziękuję, że przyszła pani mi to powiedzieć.` | grammar: missing "pani" |
| 1742 | `Kobiety z kościelnych spotkań` | `Kobiety z kolacji parafialnych` | consistency: "church suppers" |
| 1746 | `Kiedy wracałam do domu, Nick palił w kozie w warsztacie, a na stole obok heblowanej płozy sanki stał imbryk` | `Kiedy wróciłam do domu, Nick palił w kozie w warsztacie, a na stole obok heblowanej płozy sań stał imbryk` | grammar: aspect; "sanki" (sledge, nom.) for "sań" (sleigh, gen.) |
| 1746 | `w stronę kominka z łupanego kamienia` | `w stronę kominka z polnych kamieni` | consistency: "fieldstone hearth" (Ch8) |
| 1748 | `Nalewał mi kubek` | `Nalał mi kubek` | grammar: aspect |
| 1772 | `Tanaka zabrała słoik i fałszywą skargę do powiatu` | `Tanaka zabrała słoik i fałszywą skargę do hrabstwa` | consistency: county = hrabstwo throughout |
| 1772 | `przy sklepie wypełnionym po połowę ludźmi` | `przy sklepie w połowie wypełnionym ludźmi` | grammar:  |
| 1773 | `ze wszystkimi pieczęciami urzędowymi u góry` | `z pieczęcią hrabstwa u góry` | mistranslation: "county seal at the top" (one seal) |
| 1773 | `Przyniósłbym ciasto, żeby przeprosić` | `Przyniósłbym placek, żeby przeprosić` | consistency: pie motif |
| 1776 | `która przynosiła chleb do Grange` | `która przynosiła chleb do świetlicy` | consistency: Grange = świetlica |
| 1778 | `tupząc w zimnie` | `tupiąc w zimnie` | typo:  |
| 1778 | `Kakaowe bułeczki zeszły przed wpół do czwartej. Ciasteczka imbirowe sięgały dna słoika.` | `Kakaowe bułeczki zeszły przed wpół do trzeciej. Imbirowe ciasteczka wykupiono do dna słoika.` | mistranslation: "gone by half past" (two) — Polish moved it past three, after the 3 o'clock batch; "to the bottom of the jar" = sold out |
| 1782 | `wyjaśniła kolejsce` | `wyjaśniła kolejce` | typo:  |
| 1783 | `Hal przyszedł po skrzynkę na darówkę` | `Hal przyszedł po pudło do beczki z żywnością` | consistency: "the food-barrel box"; barrel = beczka |
| 1784 | `– Na darówki – powiedział i położył pieniądze na ladzie w równym stosunku.` | `– Do beczek – powiedział i położył pieniądze na ladzie w równym stosiku.` | consistency/typo: barrel = beczka; "stosunek" (ratio) for "stosik" (stack) |
| 1788 | `– Z tą farbou.` | `– Ta farba.` | typo: non-word "farbou" |
| 1793 | `– No, nie stoj w moim zimnie` | `– No, nie stój w moim zimnie` | typo:  |
| 1794 | `Podeszł do lady, kupił czekoladowo-orzechowe ciastko, którego wyraźnie nie chciał, i stanął, jedząc je` | `Podszedł do lady, kupił czekoladowo-orzechowy placek, którego wyraźnie nie chciał, i stanął, jedząc go` | typo/consistency: "Podeszł"; the chocolate-pecan is the pie |
| 1803 | `Jej książka zamówień na Święto Dziękczynienia leżała otwarta` | `Jej zeszyt zamówień na Święto Dziękczynienia leżał otwarty` | clue: order book = zeszyt zamówień |
| 1804 | `Zapisuję cię na dwa czekoladowo-orzechowe i tuzin bułek` | `Zapisuję cię na dwa placki czekoladowo-orzechowe i tuzin bułek` | consistency: pie motif |
| 1804 | `– Nie, kochanie. Nikt mi tego nie zapełni oprócz mnie.` | `– Nie, kochanie. Nikt poza mną tego nie zrealizuje.` | mistranslation: "Nobody's filling it but me" (fill = fulfil an order) |
| 1808 | `Wcisnęła mi placka` | `Wcisnęła mi placek` | grammar:  |
| 1808 | `zapakowała całego czekoladowo-orzechowego w pudełko` | `zapakowała cały placek czekoladowo-orzechowy w pudełko` | grammar:  |
| 1811 | `i ojrzałam na Holly Jolly` | `i obejrzałam się na Holly Jolly` | typo:  |
| 1812 | `Pip poststała przy mnie` | `Pip postała przy mnie` | typo:  |
| 1812 | `jedzie do domu całe ciasto` | `jedzie do domu cały placek` | consistency: pie motif |
| 1817 | `oferował pokrycie całej sumy jednym czeku` | `oferował pokrycie całej sumy jednym czekiem` | grammar:  |
| 1817 | `Stałam na ubitym śniegu na placu` | `Stałam na ubitym śniegu na rynku` | consistency: "the square" = rynek (Ch6) |
| 1819 | `Stała u stóp schodów wejściowych` | `Stał u stóp schodów wejściowych` | gender: Hal is male |
| 1819 | `Szłyśmy aleją tak samo jak wtedy po beczki Hala, tylko że zamiast puszek niesiemy teraz belki stropowe.` | `Szliśmy aleją tak samo jak wtedy do beczek Hala, tylko że zamiast puszek nieśliśmy teraz belki stropowe.` | grammar: "we" = the whole town (mixed); tense |
| 1825 | `Dwudziestu mężczyzn, z których żaden` | `Tuzin mężczyzn, z których żaden` | mistranslation: "A dozen men" |
| 1826 | `lutując palnikiem okalonym sadzą stare przewody z nowym kotłem` | `lutując stare przewody z nowym kotłem dłońmi poczerniałymi od kuźni` | mistranslation: "with his forge-blackened hands" |
| 1827 | `Idź policzyć komuś innemu.` | `Idź policzyć kogoś innego.` | grammar: "Go count somebody else" |
| 1829 | `Zbiórka kapsułek też coś przyniosła. Ludzie, którzy zanosili swoje resztki do cedrowego pudełka` | `Zbiórka do kapsuły też coś przyniosła. Ludzie, którzy zanosili swoje skrawki do cedrowego pudełka` | mistranslation: "the capsule drive" (one capsule); "scraps" of the present (not leftovers) |
| 1829 | `Koło gospodyń urządziło loterię.` | `Krąg urządził loterię.` | mistranslation: "The circle" = the knitting circle, not "Koło Gospodyń" (a rural housewives' club) |
| 1833 | `W popołudniowym półmroku Hal posłał` | `Do połowy popołudnia Hal posłał` | mistranslation: "By midafternoon" |
| 1842 | `Greta wciskała ostatnie drożdżówki z kakao ekipie od dachu` | `Greta wciskała ostatnie kakaowe bułeczki ekipie od dachu` | consistency: cocoa buns = kakaowe bułeczki (Ch9, Ch25) |
| 1843 | `stał na trawniku zwrócony` | `stał na skwerze zwrócony` | consistency: the green = skwer |
| 1846 | `Towarzystwo otworzyło drzwi dla całego miasta.` | `Towarzystwo otworzyło drzwi dla całego miasteczka.` | consistency: town = miasteczko |
| 1846 | `karta z przepisem Grety na czekoladę z pekanami oraz dwie malutkie pary rękawiczek Brama` | `karteczka z przepisem Grety na placek czekoladowo-orzechowy oraz dwie malutkie rękawiczki Brama` | mistranslation: "chocolate-pecan recipe card" (the pie, as in Ch15); "two tiny mittens" (one pair, Ch15), not two pairs |
| 1846 | `Claire przypięła kartkę ze zbiórki Grange. What shall we send them, a hundred years on?` | `Claire przypięła kartkę ze zbiórki w świetlicy. Co im wyślemy za sto lat?` | untranslated/consistency: ruling 3+5: card text was a non-title <bt> span left in English; now identical to the Ch15 card; Grange = świetlica |
| 1847 | `stare pudełko siedziało zamknięte` | `stara skrzynka stała zapieczętowana` | mistranslation: "the old box sat sealed" |
| 1851 | `i składali swoje ofiary` | `i składali swoje dary` | mistranslation: "offerings" (ofiara also = victim) |
| 1858 | `i zacisnęła dłonie nad pudełkiem` | `i złożyła dłonie nad pudełkiem` | mistranslation: "folded her hands" |
| 1859 | `Członkinie koła wrzuciły mały wieniec, który upletliśmy z suszonego balsamowca i jagód` | `Kobiety z kręgu włożyły mały wieniec, który uplotłyśmy z suszonej jodły i jagód` | consistency: krąg; "balsam" = jodła (Ch1); feminine "we" |
| 1863 | `na dłoń o dwa rozmiary mniejszą` | `na dłoń o dwa lata mniejszą` | mistranslation: "two years smaller" |
| 1865 | `którą ja sama położyłam w Grange` | `którą ja sama położyłam w świetlicy` | consistency: Grange = świetlica |
| 1867 | `Theo Hussein podeszedl blisko końca.` | `Theo Hussein podszedł pod koniec.` | typo:  |
| 1868 | `pojedynczy mosiężny nit` | `pojedynczy mosiężny gwoździk` | consistency: brad = gwoździk (Ch6) |
| 1870 | `Cofał się pod ścianę` | `Cofnął się pod ścianę` | grammar: aspect |
| 1871 | `Wtedy Hal odczytał na głos słowa założyciela.` | `Wtedy Hal odczytał na głos słowa założycielki.` | gender: the founder is Eliza Frost |
| 1872 | `z sztywnymi ołówkowymi wizerunkami założycieli po jednej stronie i brązową dłonią Elizy Frost po drugiej` | `ze sztywnymi ołówkowymi wizerunkami założycieli po jednej stronie i brązowym pismem Elizy Frost po drugiej` | mistranslation: "Eliza Frost's brown hand" = handwriting |
| 1873 | `„Niechaj zostanie zapisane, że Frost Falls nie zostało wzniesione przez silnych. Zostało wzniesione przez sąsiadów”.` | `„Niechaj będzie zapisane, że Frost Falls nie zbudowali ci silni. Zbudowali je ci sąsiedzcy”.` | consistency: the founder's line is a quotation — must match Ch6 and the Gazette headline word for word |
| 1876 | `Nie były to jej drożdżówki z kakao.` | `Nie były to jej kakaowe bułeczki.` | consistency: cocoa buns |
| 1876 | `który jej babci przywiozła ze starych stron` | `który jej babcia przywiozła ze starych stron` | typo:  |
| 1880 | `Usadowiła się na moim ramieniu` | `Przywarła do mojego ramienia` | mistranslation: "subsided against my arm" (Jessica is holding her) |
| 1883 | `Włożył go pomiędzy rękawiczki a nit.` | `Włożył go pomiędzy rękawiczki a gwoździk.` | consistency: brad |
| 1884 | `świeżą kartkę: To be sealed when the old one is opened, at the new year.` | `świeżą kartkę: Do zapieczętowania, gdy stara zostanie otwarta, w nowym roku.` | untranslated/consistency: ruling 3+5: card text left in English inside a non-title <bt>; now identical to the Ch15 card |
| 1886 | `w poprzek trawnika i wzdłuż chodnika, zwrócony twarzami ku oświetlonym oknom; dziesiątki z nich, które dzieci ulepiły w dużej liczbie.` | `w poprzek skweru i wzdłuż chodnika, zwrócony twarzami ku oświetlonym oknom; dziesiątki, choć dzieci ulepiły ich zaledwie garstkę.` | reversed: "dozens of them where the children had built a handful" — Polish said the children built many (kills the magic); green = skwer |
| 1891 | `Kiedy rano zszeszłam po zamówienie` | `Kiedy rano zeszłam po zamówienie` | typo:  |
| 1895 | `– Jesteś wcześnie – rzuciła Greta` | `– Przyszłaś wcześnie – rzuciła Greta` | grammar:  |
| 1907 | `Greta,` | `Greto,` | grammar: letter salutation takes the vocative |
| 1909 | `o tym nie mogę przestać myśleć i jest mi z tym wstyd.` | `o tym nie mogę przestać myśleć, i przepraszam cię za to.` | mistranslation: Joyce's letter: "I'm sorry for it" — the apology itself (Greta's answer turns on it) |
| 1910 | `O tym cieście. Przez dwadzieścia pięć lat wmawiałam sobie, że było moje.` | `Co do placka. Przez dwadzieścia pięć lat wmawiałam sobie, że był mój.` | consistency: pie motif = placek |
| 1910 | `a ty pieczesz je każdego ranka. Zostaw swoją wizytówkę w pudełku.` | `a ty pieczesz go każdego ranka. Zostaw swoją kartkę w pudełku.` | mistranslation: "Leave your card in the box" = Greta's RECIPE card in the time capsule (Ch15/26), not a business card — the point of the letter |
| 1915 | `A ona usiadła przy moim barze w okularach do czytania i przekartkowała moich klientów z notesu.` | `A ona usiadła przy mojej ladzie w okularach do czytania i spisała moich klientów z mojego zeszytu.` | mistranslation/clue: "counter" (not a bar); "read my customers off my book" — order book = zeszyt zamówień |
| 1915 | `odkąd rozpalone zostały piece` | `odkąd rozpaliłam piece` | grammar:  |
| 1917 | `oraz oficjalna skarga do rady powiatu` | `oraz wydrukowana skarga do hrabstwa` | consistency: "a typed complaint to the county" (Ch9) |
| 1919 | `– Odpowiedz jej ciastem – rzuciłam.` | `– Odpowiedz jej plackiem – rzuciłam.` | consistency: pie motif |
| 1923 | `że to ciasto należy do ciebie. Wyślij jej jedno` | `że placek należy do ciebie. Wyślij jej jeden` | consistency: pie motif |
| 1925 | `wsunęła na tył notesu z zamówieniami na Święto Dziękczynienia` | `wsunęła na tył zeszytu zamówień na Święto Dziękczynienia` | clue: order book |
| 1927 | `Mam pełną księgę zamówień do wydania` | `Mam pełen zeszyt zamówień do zrealizowania` | clue: order book |
| 1929 | `że odnowiona piekarnia zalega jej z odprawą` | `że odnowiona piekarnia zalega jej z wypłatą` | mistranslation: "back-pay" ("odprawa" = severance) |
| 1945 | `z opuszczonym wiekiem i świeżą wizytówką` | `z opuszczonym wiekiem i świeżą kartką` | mistranslation: "its fresh card" (Ch26) |
| 1947 | `uwalniając kolejny nit` | `uwalniając kolejny gwoździk` | consistency: brad = gwoździk |
| 1951 | `skakała po schodach werandy tuż za nią` | `zbiegała w podskokach po schodkach ganku tuż za nią` | consistency: porch = ganek |
| 1955 | `Ale za karę będzie przez tydzień żądać dodatkowych ryb` | `Ale z tego powodu będzie przez tydzień żądać dodatkowych ryb` | mistranslation: "because of it", not "as a punishment" |
| 1963 | `wszystko spoczywa na waszych barkach` | `wszystko spoczywa na twoich barkach` | grammar: addressed to Emma alone |
| 1977 | `Przyciągało całe jeszcze bliżej z każdą nocą.` | `Przez cały tydzień przysuwało się coraz bliżej, z każdą nocą.` | grammar: garbled |
| 1979 | `W Evergreen Greta musiałaby trzymać` | `Na Evergreen Greta z pewnością trzymała` | grammar:  |
| 1987 | `Szukasz innej tajemnicy? Rozpocznij cykl Spine and Spells z książką ` | `Szukasz kolejnej zagadki? Zacznij cykl Tajemnice spod magicznego grzbietu od książki ` | untranslated: sell line: series name left in English; published Polish series name "Tajemnice spod magicznego grzbietu" (2buploaded\1. Binder's Bequest_Polish) |
| 1990 | `Spadek po zmarłej ciotce` | `Spadek po zmarłej ciotecznej babce` | mistranslation: "great-aunt" |
| 1990 | `prezes Towarzystwa Historycznego pada bez tchu na Balu Maskowym pod Księżycem` | `przewodnicząca Towarzystwa Historycznego pada bez tchu na Balu Maskowym w Świetle Księżyca` | consistency: names as in the published Polish edition |
| 1993 | `Rozpocznij tajemnice z cyklu Spine & Spells od książki ` | `Zacznij cykl Tajemnice spod magicznego grzbietu od książki ` | untranslated: series name (published Polish form) |
| 1997 | `Szukasz innej tajemnicy? Rozpocznij cykl Spine and Spells z książką ` | `Szukasz kolejnej zagadki? Zacznij cykl Tajemnice spod magicznego grzbietu od książki ` | untranslated: as [1987] |
| 1999 | `Droga do Pinecrest wiła się wokół wzgórz niczym refleksja op…` | `Droga do Pinecrest wiła się wokół wzgórz jakby od niechcenia…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 53) |
| 2000 | `Mój samochód z wypożyczalni, nijaki srebrny sedan pachnący s…` | `Mój wynajęty samochód, nijaki srebrny sedan pachnący syntety…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 54) |
| 2001 | `Byłam tu już wcześniej, ale moje wspomnienia były pofragment…` | `Byłam tu już kiedyś, ale moje wspomnienia były pofragmentowa…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 55) |
| 2002 | `Biuro adwokata schowane było pomiędzy piekarnią pompującą w …` | `Kancelaria prawnika mieściła się między piekarnią, która wtł…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 56) |
| 2003 | `Pan Hartwell, mężczyzna, którego okrągła twarz i okrąglejsze…` | `Pan Hartwell, mężczyzna, którego okrągła twarz i jeszcze okr…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 57) |
| 2004 | `Wzmianka o mojej karierze uderzyła niczym ołowiany ciężar. M…` | `Wzmianka o mojej karierze opadła jak ołowiany ciężar. Miał n…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 58) |
| 2005 | `– Wszystko jest w paczce – rzekł, wskazując grubą manilową k…` | `— Wszystko w teczce — powiedział, wskazując na grubą kopertę…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 59) |
| 2006 | `Nie chciałam dziedzictwa. Chciałam czystego rejestru. Chciał…` | `Nie chciałam dziedzictwa. Chciałam czystej księgi rachunkowe…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 60) |
| 2007 | `– Dziękuję, panie Hartwell. – Wepchnęłam klucz do kieszeni, …` | `— Dziękuję, panie Hartwell. — Schowałam klucz do kieszeni, w…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 61) |
| 2008 | `Sklep Flanagan's Fine Binding & Restoration znajdował się be…` | `Flanagan’s Fine Binding & Restoration mieściło się dokładnie…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 62) |
| 2009 | `Moja dłoń drżała, gdy wsuwałam żelazny klucz do zamka. Zamek…` | `Ręka mi drżała, gdy wsuwałam żelazny klucz do zamka. Zamek o…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 63) |
| 2010 | `Powietrze, które wypłynęło mi naprzeciw, miało fizyczną obec…` | `Powietrze, które wytoczyło się mi na spotkanie, było fizyczn…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 64) |
| 2011 | `Widmo wspomnienia przemknęło na skraju mojej świadomości. Ni…` | `Na skraju mojej świadomości zamigotał cień wspomnienia. Cich…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 65) |
| 2012 | `Weszłam do środka i pozwoliłam drzwiom zatrzasnąć się za mną…` | `Weszłam do środka i pozwoliłam drzwiom zatrzasnąć się za mną…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 66) |
| 2013 | `Sklep był katastrofą nagromadzonej historii. Książki ułożone…` | `Sklep był katastrofą nagromadzonej historii. Książki piętrzy…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 67) |
| 2014 | `Światło słoneczne z trudem przebijało się przez brudną przed…` | `Światło słoneczne przebijało się z trudem przez brudną front…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 68) |
| 2015 | `Mój plan, zgrabna i uporządkowana lista, którą ułożyłam w dr…` | `Mój plan, schludna i uporządkowana lista, którą ułożyłam w d…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 69) |
| 2016 | `Uczucie bycia obserwowaną zaszczypało mnie w kark. Standardo…` | `Poczucie bycia obserwowaną zjeżyło mi włosy na karku. Standa…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 70) |
| 2017 | `Naprzeciwko, wtulona w witrynę z bogatego, ciemnego drewna, …` | `Po drugiej stronie, ulokowana w witrynie z bogatego, ciemneg…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 71) |
| 2018 | `A stojąc za ladą, polerując szklankę białą szmatką, stał męż…` | `A za ladą, polerując szklankę białą ściereczką, stał mężczyz…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 72) |
| 2019 | `Mój zawodowy sceptycyzm był tarczą i uniosłam ją wysoko. On …` | `Mój zawodowy sceptycyzm był tarczą i uniosłam ją. Był zmienn…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 73) |
| 2020 | `Potrzebowałam systematycznego podejścia. Przeszukiwania siat…` | `Potrzebowałam systematycznego podejścia. Przeszukiwania meto…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 74) |
| 2021 | `Wesoły brzęk dzwonka za moimi plecami sprawił, że podskoczył…` | `Wesoły brzęk dzwonka za moimi plecami sprawił, że podskoczył…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 75) |
| 2022 | `Kobieta, która wpadła przez drzwi, była moim przeciwieństwem…` | `Kobieta, która wpadła przez drzwi, była moim przeciwieństwem…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 76) |
| 2023 | `– Jesteś! – zawołała, a jej głos brzmiał ciepło, wylewnie i …` | `— Jesteś! — wykrzyknęła ciepłym, wylewnym potokiem. — Widzia…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 77) |
| 2024 | `Wpatrywałam się w nią, a moja skonstruowana analityczna bańk…` | `Wpatrzyłam się w nią, a moja zbudowana analityczna bańka pęk…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 78) |
| 2025 | `– O, Boże, gdzie są moje maniery? Pewnie w innej torebce. – …` | `— O Boże, gdzie moje maniery? Pewnie zostały w drugiej toreb…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 79) |
| 2026 | `Uściskałam jej dłoń. Jej uścisk był mocny i ciepły. – To… mi…` | `Uścisnęłam jej dłoń. Uchwyt miała stanowczy i ciepły. — To..…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 80) |
| 2027 | `– To niesamowite w końcu cię poznać – kontynuowała, omijając…` | `— To takie niesamowite, że wreszcie cię poznaję — ciągnęła, …` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 81) |
| 2028 | `– Jest… zagracone – powiedziałam, a słowo to wyszło ostrzej,…` | `— Jest... zagracone — powiedziałam, a słowo wyszło ostrzej, …` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 82) |
| 2029 | `Tavi nic sobie z tego nie zrobiła. – Ono żyje! Maeve zawsze …` | `Tavi zdawała się tego nie zauważać. — Jest zamieszkane! Maev…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 83) |
| 2030 | `Jej przenikliwość rozbroiła mnie. Miałam ją za roztrzepaną e…` | `Jej spostrzegawczość rozbrajała. Miałam ją wstępnie ocenioną…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 84) |
| 2031 | `– Spotkałaś już Bindy'ego? – zapytała.…` | `— Poznałaś już Bindy’ego? — zapytała.…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 85) |
| 2032 | `– Nie, właściwie nie spotkałam tu wielu ludzi – odparłam.…` | `— Nie, naprawdę niewielu tu ludzi poznałam — powiedziałam.…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 86) |
| 2033 | `Tavi się roześmiała. – Nie, Bindy to kot. Bindings Midnight …` | `Tavi roześmiała się. — Nie, Bindy to kot. Bindings Midnight …` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 87) |
| 2034 | `– Mam swój system – rzuciłam, gestykulując wymownie telefone…` | `— Mam swój system — powiedziałam, machając niejasno telefone…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 88) |
| 2035 | `– Oczywiście, że sobie poradzisz. Maeve mówiła, że jesteś na…` | `— Oczywiście, że sobie poradzisz. Maeve mówiła, że jesteś na…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 89) |
| 2036 | `Mrugnęłam. Ta konwersacyjna wolta wywołała u mnie ból karku.…` | `Zamrugałam. Ten konwersacyjny zakręt o sto osiemdziesiąt sto…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 90) |
| 2037 | `– Na Bal Maskowy pod Księżycem! – oznajmiła, jakby to była n…` | `— Na Bal Maskowy w Świetle Księżyca! — powiedziała, jakby to…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 91) |
| 2038 | `Bal. Bal maskowy. Ten pomysł był tak monumentalnie nieatrakc…` | `Bal. Bal maskowy. Pomysł był tak monumentalnie nieatrakcyjny…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 92) |
| 2039 | `– O, ten stary stos kurzu może poczekać jedną noc – machnęła…` | `— Och, ta stara kupa kurzu może poczekać jedną noc — powiedz…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 93) |
| 2040 | `– Nie szukam orientacji w terenie – odparłam, a moja cierpli…` | `— Nie szukam rozeznania w terenie — powiedziałam, a moja cie…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 94) |
| 2041 | `– Tavi – poprawiła odruchowo. – A regulowanie spadku w Pinec…` | `— Tavi — poprawiła automatycznie. — A regulowanie spadku w P…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 95) |
| 2042 | `Znalazła szczelinę w mojej zbroi. To był rozsądny, logiczny …` | `Znalazła szczelinę w mojej zbroi. To był rozsądny, logiczny …` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 96) |
| 2043 | `– Nie mam w co się ubrać na… bal maskowy – powiedziałam, chw…` | `— Nie mam w czym pójść na... bal maskowy — powiedziałam, chw…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 97) |
| 2044 | `Twarz Tavi rozjaśniła się tak, jakbym właśnie wręczyła jej w…` | `Twarz Tavi rozjaśniła się, jakbym właśnie wręczyła jej wygra…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 98) |
| 2045 | `Ona nie pytała. Ona wydawała polecenia. Czułam się jak okaz …` | `Nie pytała. Wydawała polecenia. Czułam się jak okaz przypięt…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 99) |
| 2046 | `Ale z moich ust, ku mojemu własnemu głębokiemu przerażeniu, …` | `Ale to, co wyszło, ku mojemu własnemu głębokiemu przerażeniu…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 100) |
| 2047 | `Tavi klasnęła w dłonie, wydając ostry, triumfalny dźwięk. – …` | `Tavi klasnęła w dłonie, ostrym, triumfalnym dźwiękiem. — Wsp…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 101) |
| 2048 | `I z tymi słowami zniknęła, a dzwonek zadźwięczał w ślad za n…` | `I z tym zniknęła, a dzwonek zabrzęczał w jej śladzie, zostaw…` | excerpt: copied verbatim from the published Polish edition (2buploaded\1. Binder's Bequest_Polish - FORMATTED.docx, Rozdział 1 para 102) |

## <bt> markers removed (ruling 5)

- [40] `Yarn Tales`
- [81] `Holly Jolly Bakery`
- [124] `Yarn Tales`
- [305] `HOLLY JOLLY BAKERY`
- [309] `DIRTY`
- [309] `UNSAFE`
- [309] `DON'T EAT HERE`
- [317] `DIRTY`
- [323] `DIRTY`
- [323] `UNSAFE`
- [323] `DON'T EAT HERE`
- [363] `WENDT'S BAKEHOUSE · BRIDGTON`
- [416] `DIRTY`
- [418] `Yarn Tales`
- [427] `Holly Jolly Bakery`
- [428] `Holly Jolly Bakery`
- [458] `Holly Jolly Bakery`
- [1675] `Wendt's Bakehouse, Bridgton`
- [1846] `What shall we send them, a hundred years on?`
- [1884] `To be sealed when the old one is opened, at the new year.`

## Italicised (English italic; translated card text)

- [1846] `Co im wyślemy za sto lat?`
- [1884] `Do zapieczętowania, gdy stara zostanie otwarta, w nowym roku.`


## Needs a decision (logged in PROOFREAD_DECISIONS.md)
1. Snowball: Book 1 Polish is split (Śnieżek ×25 / Snowball ×24); this book uses Snowball ×9 — kept.
2. "Two degrees under code": °F clue figure kept, identical ×3.
3. Round-number unit conversions applied accurately (100 lb → 45 kg, 50 lb → 23 kg, 1 lb chocolate → pół kilo).
4. Dash glyph: em-dash applied (dossier + published Polish Binder's Bequest); Book 1 Polish mixes en/em and will need the same.
5. Address edge cases: Hal and Doc kept informal (first names), Theo/Pete/Renée formal both ways.
6. Missing closing CTA after the excerpt — not inserted.
7. Shop names / van lettering (Holly Jolly Bakery, WENDT'S BAKEHOUSE · BRIDGTON) kept in English as names.

## Refused by verification
None.

## Quoted but not found
None (no prior report existed).
