# PROOFCHECK (FULL) — Inn Trouble - ASSEMBLED - FORMATTED_Polish (2026-10-28, cloud)

- **Mode:** full. No sub-agents. Read with python-docx, EN paragraph next to its PL paragraph(s), in order.
- **Read in full, sentence by sentence:** front matter, blurb, **all 31 chapters** (Ch1 → Ch31, including the chapters the targeted pass had already read), the sell lines, What's Next [1343]–[1347], the Flour Play excerpt [1353]–[1411] and the closing line.
- **Backup before the first write:** `_proofcheck_backups/Inn Trouble - ASSEMBLED - FORMATTED_Polish.20261028-233145.full.docx`.
- **Skipped, per the run override:** step 2's diff audit and the 20-row ledger sample (done by today's targeted pass). Step 1: every flag section had already been judged in the targeted report; the re-run shows the same counts (A–G = 0, J = 0, H = 19 all false — ransom "pół miliona", ruling-4 miles, degrees of rotation, a foot, "złotych świateł"; I = 1 false — [1053] remembered speech in „…”).
- **Edits:** 96, in 89 paragraphs. 88 were missed by the first pass, 4 were first-pass regressions (the note it translated + the excerpt rebuild), and 4 refine today's targeted wording of "Theo had the theft". 0 refusals. Paragraph count 1416 → 1416.

## Brief items checked explicitly
- **"Theo had the theft" (Ch22 [1009], Ch23 [1045], Ch26 [1183], [1187]).** The targeted pass had set the literal `Miał kradzież` / `Theo miał kradzież` / `On miał kradzież`, which reads oddly and can be heard as "had a theft done". Now by sense: **`Theo miał w ręku tajemnicę kradzieży.`**, and in the confrontation **`On miał w ręku tajemnicę kradzieży. Pani miała w ręku akt własności.`** (had/had parallel kept). Constance stays the thief everywhere; Theo only held that half of the secret.
- **Spoiler-gender (Polish past tense is gendered).** Every "someone / whoever / the person / the blackmailer / the courier" reference before the Ch22 reveal was read. Fixed where the PL used an explicit gendered form the English does not have:
  - [185] Ch2 — the note itself: `żebym wiedział` ("so I'll know") made the writer **say he is male** → `na znak, że pieniądze tam są`.
  - [791] Ch16 — `On trzymał w rękach dokładnie tamte listy` (EN "They had those exact letters") → `osoba, która napisała … Dokładnie tamte listy musiały być w jej rękach`.
  - [957] Ch20 — the unknown courier (really Vera): `niczyje oko się na nim nie zatrzymało` (EN "on them") → `niczyje oko nie miało się na czym zatrzymać`.
  - Soft cases neutralised as well: [235] `niż jej autor zamierzał`, [379] `by okazał się nim`, [773] `inaczej to nie był on`, [822] `jego twarz`.
  - **Kept, on purpose:** the generic masculine noun `szantażysta` ("the blackmailer") and `ktoś/ktokolwiek … -ł` — this is unmarked Polish, not a reveal — and every place where the English itself says "he/his" (Ch9 [540], Ch16 [784], Ch20 Fiona's and Jessica's "he" [927]–[955]). Noted as PC-PL-ITF-3.
- **Ch19 card vs note:** every Ch19 card/note sentence checked — card = karta/fiszka, note = notatka/liścik, the card is in Theo's hand, `do siostry` (no `jej`). [862] "a household servant" was `przez domową służbę` (the household staff) → `przez kogoś ze służby domowej` (inside the italic card run; italics kept).
- **Ch19 [886] "It's the love that lets him, Jess"** — `To miłość pozwala mu na to, Jess.` correct (him, not you).
- **Ch27 [1240] "ruined himself"** — targeted fix holds (`rujnując przy tym samego siebie`).
- **Blackburn papers vs deed(s):** kept apart (papiery/dokumenty vs akt własności); [641] "the deed" to the inn made singular.
- **"your man" (Claire, [831]) = `twój człowiek`** (Neil), not husband. ✔
- **Settled terms grepped after the edits:** skwer/błonie (no zieleniec/plac/park for the green), wybieg ×10, ganek ×24 (no weranda), no `cydr`, no `miasto` for Frost Falls in the body (2 hits = "wielkiego miasta", correct), Snowball, krąg, palenisko. Drift fixed: stationery `papier firmowy` → `papeteria` ([327], [1222]); latch `zatrzask`/`zamki` → `zasuwa` ([1295], [1333]); fire screen [490]; boiler [599]; woodstove [767]; Ratusz [693]; cardigan [58]; Gazette [353] [648].
- **Excerpt** (policy PC-FIL2-1): read against Inn Trouble's own English. `Prawie.` ✔, the snowman question not inverted ✔, chocolate-pecan now `czekoladowo-pekanowych` ✔ (PC-PL-IT-1 applied), war memorial/overnight/weekend all in this excerpt's own English ✔, no half-paragraph dropped at the FP split points ✔. Three lines carried over from FP were wrong against the English and are fixed here (see Regressions; FP follow-up in PC-PL-ITF-2).
- **"six letters"** [769] left faithful to the English (override; not re-logged).

## Missed by the first pass (all applied)
| Para | Ch | Polish (before) | Class / English | Fix |
|---|---|---|---|---|
| 26 | blurb | `Fiona Okafor prowadziła ją tak samo, jak jej rodzina od stu lat, a dzisiaj` | blurb tense drift: EN present "has run it"; PL past prowadziła mixed with present nie może | `Fiona Okafor prowadzi ją tak samo, jak od stu lat prowadziła ją jej rodzina, a dzisiaj` ✔ |
| 60 | Ch1 | `Nawet jej głos brzmiał fałszywie, cienki` | mistranslation: "wrong" ≠ fałszywie (insincere/off-key) | `Nawet jej głos brzmiał nie tak, cienki` ✔ |
| 128 | Ch1 | `że fałsz na twarzy Fiony wydawał mi się na moment czymś, co sobie wyobraziłam.` | mistranslation: "the wrongness in Fiona's face" ≠ fałsz (falseness) | `że to, co było nie tak w twarzy Fiony, wydawało mi się na moment czymś, co sobie wyobraziłam.` ✔ |
| 175 | Ch2 | `dzisiaj z zapiętym równo kardiganem, ale ze wszystkim innym postawionym na głowę.` | mistranslation: "everything else about her wrong" ≠ "turned upside down" | `dzisiaj z zapiętym równo kardiganem, ale poza tym wszystko w niej było nie tak.` ✔ |
| 220 | Ch2 | `by odczytać ciasny szlaczek pisma,` | word choice: "cramped scrawl" ≠ szlaczek (decorative border) | `by odczytać ciasne gryzmoły,` ✔ |
| 235 | Ch2 | `Notatka może nam powiedzieć więcej, niż jej autor zamierzał.` | spoiler-gender (soft): "its writer meant" — masculine autor zamierzał; neutralised | `Notatka może nam powiedzieć więcej, niż miała zdradzić.` ✔ |
| 266 | Ch3 | `Milczał, a kiedy przemówił ponownie` | omission: "He was quiet and sad" — "and sad" dropped | `Milczał i był smutny, a kiedy przemówił ponownie` ✔ |
| 274 | Ch3 | `i pozwoliłam, by na tym się skończyło.` | mistranslation: "I let it be only that" ≠ "let it end there" | `i pozwoliłam, żeby tak zostało.` ✔ |
| 280 | Ch3 | `w odniesieniu do budki dla ptaków, o której mi opowiadałeś w tygodniu, kiedy się tu wprowadziliśmy.` | sense: he TOLD her it was a birdhouse (not "a birdhouse you told me about") | `w odniesieniu do budki dla ptaków, a właśnie to mi powiedziałeś w tygodniu, kiedy się tu wprowadziliśmy.` ✔ |
| 312 | Ch4 | `To on to wszystko przywiózł.` | mistranslation: "He'd carried all of this" (by hand) ≠ przywiózł (brought by vehicle) | `To on to wszystko przeniósł.` ✔ |
| 326 | Ch4 | `przyglądałam się, jakich dotykał — a raczej` | mistranslation: "how he touched them" (jakich = which ones) | `przyglądałam się, jak ich dotykał — a raczej` ✔ |
| 327 | Ch4 | `leżał stos papieru firmowego Towarzystwa —` | clue-chain term drift: stationery = papeteria (Ch22/23/25/26) | `leżał stos papeterii Towarzystwa —` ✔ |
| 337 | Ch5 | `W środku było ciepło i zacisznie.` | mistranslation: "warm and dim" (zacisznie = snug) | `W środku było ciepło i panował półmrok.` ✔ |
| 340 | Ch5 | `Rozmawiały o festiwalowych rękawiczkach — rękawiczkach z podpisanymi mankietami,` | mistranslation: "They were on the festival mittens" = working on them, not talking about them | `Pracowały nad festiwalowymi rękawiczkami — rękawiczkami z podpisanymi mankietami,` ✔ |
| 353 | Ch5 | `ponieważ pytałam go o to dla gazety,` | name dropped: "for the Gazette" (edition writes Gazette) | `ponieważ pytałam go o to dla Gazette,` ✔ |
| 379 | Ch5 | `pragnęłam, by okazał się nim ktokolwiek inny na świecie.` | spoiler-gender (soft): "for it to turn out to be anybody else" — masculine okazał się nim implied a male culprit | `pragnęłam, by okazało się, że to ktokolwiek inny na świecie.` ✔ |
| 423 | Ch6 | `Była krępą kobietą po pięćdziesiątce` | mistranslation: "about fifty" ≠ "past fifty" | `Była krępą kobietą około pięćdziesiątki` ✔ |
| 451 | Ch6 | `Powinnam się martwić, a jakaś` | tense: "I should have been worried" (past conditional) | `Powinnam była się martwić, a jakaś` ✔ |
| 468 | Ch7 | `która była panną Blackburn w całej swojej krasie.` | mistranslation: "a Blackburn in her finery" — panna asserts unmarried | `która była jedną z Blackburnów w całej swojej krasie.` ✔ |
| 471 | Ch7 | `Taka kobieta z niej wyrastała.` | tense/aspect: "That's the woman she became" | `Taką kobietą się stała.` ✔ |
| 471 | Ch7 | `Głos Fiony pociemniał.` | mistranslation: voice "thickened" ≠ "darkened" | `Głos Fiony nabrzmiał.` ✔ |
| 482 | Ch8 | `Kiedy podeszłam do otwartego boksu,` | mistranslation: "the open side" ≠ boks (stall) | `Kiedy podeszłam od otwartej strony,` ✔ |
| 484 | Ch8 | `a ja nie spieszyłam się z tym.` | mistranslation: "I didn't hurry him" | `a ja go nie poganiałam.` ✔ |
| 490 | Ch8 | `Gwiazdy na kominku, kinkiety, osłona przeciwiskrowa.` | term drift: fire screen = ekran kominkowy (Ch1 ×2) | `Gwiazdy na kominku, kinkiety, ekran kominkowy.` ✔ |
| 494 | Ch8 | `nauczyłam się odróżniać ludzi potrafiących okazać emocje od tych, którzy mają tylko jedną twarz.` | reversed sense: "men who can wear a feeling" = put one on (fake), not "show emotion" | `nauczyłam się odróżniać ludzi, którzy potrafią przybrać dowolne uczucie jak maskę, od tych, którzy mają tylko jedną twarz.` ✔ |
| 498 | Ch8 | `wydarłbym rachunek` | word choice: "torn the bill up" = podrzeć (wydrzeć = tear out) | `podarłbym rachunek` ✔ |
| 500 | Ch8 | `jak rodzina Fiony weszła w jego posiadanie` | agreement: gospoda is feminine | `jak rodzina Fiony weszła w jej posiadanie` ✔ |
| 501 | Ch8 | `Spojrzał na mnie bezmyślnie. — Weszła w posiadanie? Zawsze do nich należał.` | mistranslation "blankly" ≠ bezmyślnie; agreement gospoda (f.) | `Spojrzał na mnie bez zrozumienia. — Weszła w posiadanie? Zawsze do nich należała.` ✔ |
| 501 | Ch8 | `Jej prababcia go założyła,` | agreement: gospoda (f.) | `Jej prababcia ją założyła,` ✔ |
| 528 | Ch9 | `Kradzież, na sto procent, choć` | mistranslation: "almost certainly" ≠ "a hundred percent" | `Kradzież, niemal na pewno, choć` ✔ |
| 573 | Ch10 | `twarz Nicka — rozemocjonowana, zadowolona,` | mistranslation: "flushed" = zarumieniona | `twarz Nicka — zarumieniona, zadowolona,` ✔ |
| 579 | Ch10 | `Twoja niespodzianka. To część tego planu.` | addition: "It's part of this" — no "plan" in EN | `Twoja niespodzianka. To ma z tym związek.` ✔ |
| 589 | Ch11 | `w imieniu miasteczka, a nie nikogo konkretnego,` | grammar: double negation "a nie nikogo" | `w imieniu samego miasteczka, a nie kogokolwiek innego,` ✔ |
| 593 | Ch11 | `Ona miała pliki dokumentów i klucze.` | word choice: "files" ≠ pliki (computer files) | `Ona miała akta i klucze.` ✔ |
| 599 | Ch11 | `Kocioł grzewczy, dla którego była to ostatnia zima.` | term drift: boiler = piec (settled; Ch5) | `Piec, dla którego była to ostatnia zima.` ✔ |
| 641 | Ch11 | `z aktami własności Winter Wonderland Inn gdzieś` | clue term: "the deed" (singular) to the inn | `z aktem własności Winter Wonderland Inn gdzieś` ✔ |
| 648 | Ch12 | `że „Gazette” chciało widzieć` | consistency: Gazette bare elsewhere (no quotes); agreement gazeta (f.) | `że Gazette chciała widzieć` ✔ |
| 693 | Ch14 | `ze skwerem, ratuszem i całą resztą.` | term: Town Hall = Ratusz (capitalised, settled) | `ze skwerem, Ratuszem i całą resztą.` ✔ |
| 703 | Ch14 | `Na skwerze problem sprawiał Bram.` | reversed: "the trouble was Bram's" (he HAD the trouble), not "Bram was causing trouble" | `Na skwerze kłopot miał Bram.` ✔ |
| 707 | Ch14 | `Siedzi w fontannie,` | mistranslation: Prancer is standing (EN [515] "standing in the basin") | `Stoi w fontannie,` ✔ |
| 738 | Ch15 | `W wersji Ivy Prancer siedziała w fontannie od świtu,` | consistency: Prancer stood in the basin (Ch14) | `W wersji Ivy Prancer stała w fontannie od świtu,` ✔ |
| 757 | Ch15 | `Głowa Claire poszła w górę.` | calque: "Claire's head came up" | `Claire podniosła głowę.` ✔ |
| 767 | Ch15 | `tuż obok ciepłego boku pieca.` | term: woodstove = koza ([735], Ch5); piec is the boiler | `tuż obok ciepłego boku kozy.` ✔ |
| 791 | Ch16 | `to ten, kto napisał tę notatkę, nie tylko czytał papiery Blackburnów ogólnie. On trzymał w rękach dokładnie tamte listy.` | SPOILER-GENDER: EN "They had those exact letters in their hands" — emphatic masculine "On trzymał" named a male writer | `to osoba, która napisała tę notatkę, nie tylko czytała papiery Blackburnów ogólnie. Dokładnie tamte listy musiały być w jej rękach.` ✔ |
| 773 | Ch16 | `na oba, inaczej to nie był on.` | spoiler-gender (soft): EN "or it wasn't them" — "nie był on" | `na oba, inaczej to nie mogła być ta osoba.` ✔ |
| 790 | Ch16 | `Chcę, żeby Neil okazał się sprytnym szelmą,` | mistranslation: "clever villain" ≠ szelma (rascal) | `Chcę, żeby Neil okazał się sprytnym złoczyńcą,` ✔ |
| 822 | Ch17 | `niech pan zapamięta dla mnie jego twarz.` | spoiler-gender (soft): EN "remember their face" — masculine jego | `niech pan zapamięta dla mnie twarz tej osoby.` ✔ |
| 840 | Ch18 | `Szantażista handluje rozmiarem groźby.` | typo: szantażista → szantażysta | `Szantażysta handluje rozmiarem groźby.` ✔ |
| 844 | Ch18 | `podczas gdy rodzina, do której należała, kazała jej być wdzięczna.` | ambiguity: "the family that owned it" read as "the family she belonged to" | `podczas gdy rodzina, do której ta brosza należała, kazała jej być wdzięczna.` ✔ |
| 854 | Ch19 | `mosiężne spinacze w moim podajniku.` | word choice: "tray" ≠ podajnik (feeder) | `mosiężne spinacze na mojej tacce.` ✔ |
| 860 | Ch19 | `Powinnam je odłożyć bez czytania.` | tense: "I should have set them aside" (past conditional) | `Powinnam była je odłożyć bez czytania.` ✔ |
| 862 | Ch19 | `przez domową służbę;` | mistranslation: "a household servant" (one person), not "the household staff"; inside italic card run, italics kept | `przez kogoś ze służby domowej;` ✔ |
| 876 | Ch19 | `wyznać ze lśniącymi zmęczeniem oczami,` | mistranslation: "his tired eyes shining" ≠ "eyes shining with fatigue" | `wyznać, a jego zmęczone oczy lśniły,` ✔ |
| 900 | Ch19 | `W centrum pomieszczenia, tam gdzie niegdyś stało dawne palenisko Bieguna,` | mistranslation: "where the old hearth of the Pole would have stood" (hypothetical), not "where it once stood" | `W centrum pomieszczenia, w miejscu, w którym na Biegunie stałoby dawne palenisko,` ✔ |
| 900 | Ch19 | `dotarła wreszcie i tutaj, i zataczała` | omission: "had come, some of it, here" | `dotarła tutaj, przynajmniej jej część, i zataczała` ✔ |
| 957 | Ch20 | `Ktoś, kto poruszał się po tym miasteczku tak zwyczajnie, że niczyje oko się na nim nie zatrzymało;` | SPOILER-GENDER: the unknown courier — EN "no eye would ever snag on them"; "na nim" made them male | `Ktoś, kto poruszał się po tym miasteczku tak zwyczajnie, że niczyje oko nie miało się na czym zatrzymać;` ✔ |
| 933 | Ch20 | `a on musiał to wiedzieć, musiał, więc o co mu w ogóle chodzi?` | tense: "he must know that" (present), not "must have known" | `a on musi to wiedzieć, musi, więc o co mu w ogóle chodzi?` ✔ |
| 967 | Ch21 | `od czasu kradzieży kasetki Olivii.` | mistranslation: "since Olivia's cash box" = her Book 1 fundraising collection; the PL invented a THEFT | `od czasu zbiórki Olivii do blaszanej kasetki.` ✔ |
| 971 | Ch21 | `To było najbliższe starcie tego dnia.` | mistranslation: "That was the closest the day came" ≠ "closest clash" | `Do niczego bliższego tego dnia nie doszło.` ✔ |
| 975 | Ch21 | `To już dwoje z was pilnujących przedniej recepcji Fiony.` | calque: "front desk" ≠ "przednia recepcja" | `To już dwoje z was pilnujących recepcji Fiony.` ✔ |
| 981 | Ch21 | `Stojąc tak w śniegu, mój umysł stał się twardy` | grammar: dangling participle (stojąc ≠ subject umysł) | `Gdy tak stałam w śniegu, mój umysł stał się twardy` ✔ |
| 1019 | Ch22 | `Rano pójdę tam i upewnię się co do drugiej pary.` | tense: "In the morning I would go" (future-in-past, past narration) | `Rano miałam pójść i upewnić się co do drugiej pary.` ✔ |
| 1080 | Ch24 | `wyszeptać to wszystko i pozwolić` | mistranslation: "whisper it all away" (make it vanish), not "whisper it all" | `zażegnać to wszystko szeptem i pozwolić` ✔ |
| 1080 | Ch24 | `A zgnilizna zostaje w murach tam, gdzie jej nie widzę, i rośnie.` | tense/mood: hypothetical (if I do that…) | `A zgnilizna zostałaby w murach tam, gdzie jej nie widzę, i rosłaby dalej.` ✔ |
| 1082 | Ch24 | `i to ty sprowadziłaś na nich ten żal.` | tense: "you're the one who'll have brought the grief" (future) | `i to ty sprowadzisz na nich ten żal.` ✔ |
| 1183 | Ch26 | `w pani koszyku do ponownego porządkowania, dotknięty, na biurku` | mistranslation: "handled" ≠ dotknięty (touched/hurt) | `w pani koszyku do ponownego porządkowania, niedawno przeglądany, na biurku` ✔ |
| 1187 | Ch26 | `On nie przeszedłby przez miasteczko niezauważony choćby o życie,` | idiom: "to save his life" — "choćby o życie" is not Polish | `On nie przeszedłby przez miasteczko niezauważony, choćby od tego zależało jego życie,` ✔ |
| 1163 | Ch26 | `Jego twarz powoli skurczyła się jak stary papier.` | mistranslation: "crumpled" ≠ shrank | `Jego twarz powoli zmięła się jak stary papier.` ✔ |
| 1197 | Ch26 | `Spojrzała na Fionę, druzgocąco skruszona.` | word choice: "stricken" | `Spojrzała na Fionę, zdruzgotana.` ✔ |
| 1222 | Ch27 | `wykorzystując zbiory i papier firmowy Towarzystwa,` | clue-chain term drift: stationery = papeteria | `wykorzystując zbiory i papeterię Towarzystwa,` ✔ |
| 1226 | Ch27 | `a zamiast tego dostarczono mu długą, wyboistą drogę.` | word choice: "handed" ≠ dostarczono (delivered) | `a zamiast tego dano mu długą, wyboistą drogę.` ✔ |
| 1248 | Ch28 | `Kawałek mnie, stojący zmęczony` | calque: "Part of me" = część mnie | `Część mnie, stojącej zmęczonej` ✔ |
| 1256 | Ch28 | `i położyła w rękawiczce dłoń na ramieniu męża.` | word order: "her gloved hand" | `i położyła dłoń w rękawiczce na ramieniu męża.` ✔ |
| 1258 | Ch28 | `co czyniło ich położenie jeszcze bardziej ryzykownym` | agreement: refers to Towarzystwo (sg.) | `co czyniło jego położenie jeszcze bardziej ryzykownym` ✔ |
| 1263 | Ch28 | `Przekonamy się o tym przed nowym rokiem.` | tense: "We would know by the new year" (future-in-past); Nowy Rok capitalised as elsewhere | `Mieliśmy się o tym przekonać do Nowego Roku.` ✔ |
| 1275 | Ch29 | `Przygotowałam się na rolę outsiderki, która zniszczyła` | consistency: "the outsider who broke a good man" = obca (Ch24 [1084] [1092]); anglicism | `Przygotowałam się na rolę obcej, która zniszczyła` ✔ |
| 1291 | Ch30 | `To może być pierwsza porządna rzecz, w pobliżu której przyjdzie mu stanąć.` | omission: "stand near AGAIN" | `To może być pierwsza porządna rzecz, w pobliżu której znów przyjdzie mu stanąć.` ✔ |
| 1292 | Ch30 | `Nie otworzymy jej.` | tense: "We wouldn't open it" (past narration) | `Nie mieliśmy jej otwierać.` ✔ |
| 1295 | Ch30 | `— Ten zatrzask, pani Claus! —` | term drift: latch = zasuwa (Ch10 ×5) | `— Ta zasuwa, pani Claus! —` ✔ |
| 1299 | Ch30 | `W nowym roku miasteczko otworzy skrzynkę, a Theo będzie tam, żeby to zobaczyć.` | tense: future-in-past ("would open … would be there") | `W nowym roku miasteczko miało otworzyć skrzynkę, a Theo miał tam być, żeby to zobaczyć.` ✔ |
| 1327 | Ch31 | `Tylko tyle ktoś od ciebie wymaga.` | mistranslation: "That's all anyone's asking of you" | `Tylko tego wszyscy od ciebie oczekują.` ✔ |
| 1326 | Ch31 | `Szczera prawda, to w dużej mierze trzyma mnie przy życiu.` | mistranslation: "keeping me going" ≠ "keeping me alive" | `Szczera prawda, to w dużej mierze pozwala mi się trzymać.` ✔ |
| 1330 | Ch31 | `a magia unosiła się nad pustym paleniskiem w powolnych kręgach.` | term: "the empty grate" = ruszt (Ch19 [900]); palenisko twice in one sentence | `a magia unosiła się nad pustym rusztem w powolnych kręgach.` ✔ |
| 1332 | Ch31 | `— Kawałek po kawałku. Początek. —` | mistranslation: "A little of it. The beginning of it." ≠ "little by little" | `— Jej odrobina. Dopiero początek. —` ✔ |
| 1333 | Ch31 | `wciąż sypiąca iskrami wokół lamp i zamków w całym miasteczku.` | term drift: latches = zasuwy (Ch10), not zamki (locks) | `wciąż sypiąca iskrami wokół lamp i zasuw w całym miasteczku.` ✔ |
| 1337 | Ch31 | `Weszliśmy razem z zimnej nocy.` | mistranslation: "out of the gold night" | `Weszliśmy razem ze złotej nocy.` ✔ |
| 1248 | Ch28 | `na tym zimnym ganku, chciał chwycić tę ofertę` | agreement after the "Część mnie" fix | `na tym zimnym ganku, chciała chwycić tę ofertę` ✔ |
| 58 | Ch1 | `Jej sweter był zapięty o jeden guzik za wysoko.` | term/mistranslation: cardigan = kardigan (blurb, Ch2, Ch12); "buttoned wrong by one button", not "one button too high" | `Jej kardigan był zapięty krzywo, o jeden guzik.` ✔ |

## Regressions introduced by the first pass (all applied)
| Para | Ch | Polish (before) | Class | Fix |
|---|---|---|---|---|
| 185 | Ch2 | `zawiąż w jej miejsce czerwoną, żebym wiedział, że pieniądze tam są.` | SPOILER-GENDER: the note's "so I'll know" was masculine 1st person (żebym wiedział) — reveals a male writer; EN neutral | `zawiąż w jej miejsce czerwoną na znak, że pieniądze tam są.` ✔ |
| 1373 | excerpt | `Ludzie byli dla mnie życzliwi tak, jak miasto bywa życzliwe wobec gościa` | term: town = miasteczko (settled); FP PL [77] has the same — informational for FP | `Ludzie byli dla mnie życzliwi tak, jak miasteczko bywa życzliwe wobec gościa` ✔ |
| 1392 | excerpt | `nie chcesz, żeby miasto ci się gapiło na ręce.` | term: town = miasteczko; FP PL [110] same | `nie chcesz, żeby miasteczko ci się gapiło na ręce.` ✔ |
| 1399 | excerpt | `Uczniowie szkoły zbudowali wzdłuż niego rzędami bałwany` | mistranslation: "a row of snowmen" (three), not "snowmen in rows"; FP PL [124] same | `Uczniowie szkoły zbudowali wzdłuż niego rząd bałwanów` ✔ |

([185] is the blackmail note that the first pass translated from the English the MT had left; [1373] [1392] [1399] came in with the excerpt rebuild from corrected Flour Play PL, which has the same three lines — see PC-PL-ITF-2.)

## Today's targeted wording refined (all applied)
| Para | Ch | Polish (before) | Class | Fix |
|---|---|---|---|---|
| 1009 | Ch22 | `papeterię. Miał kradzież. Ale` | "Theo had the theft": literal "Miał kradzież" (targeted pass) reads oddly / can mean "had a theft done"; rendered by sense | `papeterię. Miał w ręku tajemnicę kradzieży. Ale` ✔ |
| 1045 | Ch23 | `Theo miał kradzież. Znalazł ją w listach Blackburnów,` | "Theo had the theft": literal "miał kradzież" rendered by sense (= Ch22 [1009]) | `Theo miał w ręku tajemnicę kradzieży. Znalazł ją w listach Blackburnów,` ✔ |
| 1183 | Ch26 | `— Pani Vero — powiedziałam. — Theo miał kradzież. Ale` | "Theo had the theft": literal "miał kradzież" (targeted pass) rendered by sense (= Ch22/23) | `— Pani Vero — powiedziałam. — Theo miał w ręku tajemnicę kradzieży. Ale` ✔ |
| 1187 | Ch26 | `— On miał kradzież. Pani miała akt własności.` | "He had the theft. You had the deed." — sense rendering, had/had parallel kept | `— On miał w ręku tajemnicę kradzieży. Pani miała w ręku akt własności.` ✔ |

## Ledger mismatches
Not re-sampled (done today by the targeted pass: 0 real mismatches).

## Re-checked decisions
IT-PL-1…7 (PROOFREAD_DECISIONS2) and PC-PL-IT-1 (PROOFCHECK_DECISIONS): quotes still accurate; nothing re-raised. PC-PL-IT-1 (pecan) is now applied in the file ([1377] `czekoladowo-pekanowych`).

## Decisions added (PROOFCHECK_DECISIONS.md, section "… — FULL PROOFCHECK (2026-10-28)")
- PC-PL-ITF-1 "Theo had the theft" wording (informational, applied).
- PC-PL-ITF-2 Flour Play PL follow-up: three excerpt lines and the blurb's gendered "whoever" (not applied to FP).
- PC-PL-ITF-3 Theo's declension is mixed (Theo / Thea / Theowi) + generic-masculine policy note.

## Refusals
None (96 edits, 96 applied, each matched exactly once inside its paragraph).

## Checks after the fixes
- looks_english: `[]`
- bt_anchors check: 8 spans (Inn Trouble, Frost and Found, Flour Play), 0 unpaired
- check_matter: 1 PASS, 0 FAIL
- preflight --verify: paragraphs 1416 → 1416 ok, scene breaks 3 → 3 ok; the same pre-existing FAIL as before this audit (first pass's +2 italic runs and −6 stray `<bt>`, ruling 5). Corrected vs my backup: 1416 = 1416 paragraphs, 24 = 24 italic runs in the same order (text changed only inside the italic runs of [185] the note and [862] the card), 8 = 8 `<bt>`, 3 = 3 scene breaks, 89 paragraphs changed.
- proofcheck re-run: A–G = 0, H = 19, I = 1, J = 0 (unchanged; all false positives).

## Verdict
**SIGNIFICANT.** The blackmail note itself announced a male writer (`żebym wiedział`), Ch16 named the letter-holder "On", and Ch20 gendered the unknown courier — three spoiler-gender giveaways; plus a reversed "the trouble was Bram's" (Ch14), "men who can wear a feeling" reversed (Ch8), an invented theft of Olivia's cash box (Ch21), and the literal "miał kradzież" ×4. All fixed. Rate: 96 edits / 31 chapters + front/back matter ≈ 2.9 per chapter (most are minor mistranslations, tense and term drift).
