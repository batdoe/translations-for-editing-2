# PROOFREAD — Flour Play - ASSEMBLED - FORMATTED_Turkish (2026-10-26 run, done 2026-10-27)

- Edition: Turkish, Frost Falls Book 3. Input `translated\Flour Play - ASSEMBLED - FORMATTED_Turkish.docx` (raw MT, never proofread). English: `translate_now\Flour Play - ASSEMBLED - FORMATTED.docx` (Oct 19 no-poison version). Output: `translated\corrected\Flour Play - ASSEMBLED - FORMATTED_Turkish.docx`.
- Starting copy: the existing `corrected\` file (= input + the pre-flight's 6 asterisk-to-italic conversions), backed up to `corrected\_bak\Flour Play - ASSEMBLED - FORMATTED_Turkish.pre-proofread-20261027.docx`.
- Prior report: none (0/0 not found).
- Dossier: **turkish_cozy.txt** (NOT turkish.txt). Dialogue = konuşma çizgisi "— " per turn, no closing mark, attribution after a comma ("— Dur, dedi, düşünmem lazım."), quoted words inside narration in "…"; narrative tense = -di past (checked every chapter: locked, no -miş narration); clean register. Rulings FF_DECISIONS_BRIEF_20261013 1–7 + FF_PROOFREAD_BRIEF_20261026 incl. all Lessons and the Flour Play section.
- Series sources: no Inn Trouble TR exists; Frost and Found TR (`translated\`, raw, unproofread) for circle / Snowball / place words / reindeer. Flour Play SV / NO / FR ledgers used for the clue-term CHOICES only.
- Coverage: front matter, blurb, Ch 1–27, back matter, Binder's Bequest excerpt — every paragraph read against the English, sequentially, no sub-agents. Body is 1:1 with the English (verified by alignment: every chapter's paragraph count matches; −25 vs English = the 27-line TOC collapsed to "Bölüm 27", the missing Ch10 heading, and the missing second sell line).
- Paragraph numbers = index of `<w:p>` in document.xml (= python-docx `document.paragraphs`).
- Input `bt_anchors check` (ruling 5): 6 spans, 0 unpaired — "The Binder's Bequest" ×5 (real title: kept) and **"Wendt's Bakehouse, Bridgton"** [941] (business name, not a title: markers removed).
- No published Turkish *The Binder's Bequest* exists (`2buploaded\`, `proofread\`, `translated\corrected\` checked) — excerpt proofread against the English instead.

## Worst defects
1. **The Joyce "cold room" / "Hobart sink" clue was erased.** Ch22 [1657] `Şikâyet dilekçesinde soğuk odadan soğuk oda diye, eviye için de Hobart eviyesi diye bahsedilmiş` ("called the cold room the cold room") and Ch23 [1731] `kendisinin soğuk odasını soğuk oda … olarak adlandırmışlar`; Greta's Ch20 explanation [1556] used **Pete's locker word** (`soğuk hava deposu`) for her own walk-in, and Ch9 [791] Varney called the walk-in `Soğuk hava deposu` too — so the slip vanished and the walk-in collided with Pete's locker. Now: walk-in = **soğutucu**; Joyce's word = **"soğuk oda"**; hand-sink = **el lavabosu**, her word = **"Hobart lavabosu"**; Pete's locker = **soğuk hava deposu** — identical at [791] [793] [1554] [1556] [1657] [1731] [1733] [1838].
2. **Poison wording in the no-poison edition:** Ch12 [893] `Zehrinizi dökerdiniz` ('Tip your powder') and Ch13 [958] `O zehirli tozu döken her kimse` — fixed to "Tozunuzu" / "O tozu". Grep zehir/toksik = 0 now.
3. **Reversed meanings:** Ch4 [309] 'If this comes out right' → `Eğer bu da düzgün çıkmazsa`; Ch15 [1194] 'Everything in me wanted to cross that hall' → `…istemiyordu`; Ch16 [1255] 'Between us' → `Aramızda kalmasın`; Ch17 [1295] 'I know it was you' → `Ben olduğunu biliyorum`; Ch18 [1458] 'be thanked by no one' → `kimseye teşekkür etmemeyi`; Ch19 [1495] 'if she's not changed it' → `Eğer plakayı değiştirdiyse`; Ch23 [1761] 'decided to stop wasting her time' → `…harcamaya karar vermiş`; Ch27 [2179] 'as though I might not have been there' → `sanki oradaymışım gibi`; Ch5 [556] 'decided it was not a fish' → `bir balık olduğuna karar veremeyip`.
4. **Dialogue: three systems mixed** — « » (361 paragraphs), straight "…" (Ch1), MT-dash chapters (Ch17–23, several with Spanish-raya closing dashes `— X — dedi Y` in Ch23). Converted 556 paragraphs to the dossier's dash system and rebuilt ~110 attributions by hand (Turkish pre-posed attributions `Dot, «…» dedi.` → `— …, dedi Dot.`; narration inside speech set off with dashes; overheard speech inside narration → "…").
5. **Foreign-script / garbage tokens and English left in:** Amharic `ነበር` [717], Tamil `பெரும்பாலான` [1687], Azerbaijani `kinə` [1021], `sig` [1676], `Varış.` [1602]; English `pumpkins` [42], `Evergreen Avenue` [42], `hardware` [750], `cite` [791], `roll` [1527], `Halloween` [1529], `shingle` ×4 (Ch26), `teal` [2245], `Mrs./Mr./Miss` ×9; graffiti left in corrupted English `DİRİTY / UNSAFE / DÖN'T EAT HERE` (Ch4) → PİS / TEHLİKELİ / BURADA YEMEK YEMEYİN (not a vulgarity; three words kept three).
6. **Chapter 10 heading missing** (body present, runs on under Bölüm 9 from [810]) — decision FP-TR-D1 (not renumbering: 11–27 are correct).

## Clue chain (brief §Flour Play): one rendering each
- sour base = **ekşitici baz** (MT had `ekşi maya` = sourdough starter ×8, `ekşi maya mayası` ×4, `ekşi baz`, `ekşitilmiş maya`, `ekşi maya tabanı`); starter itself = ekşi maya [864]. Doc's analysis, Pelkey's invoice [1661], the confrontation [1735] [1737], the charges [1834] all say ekşitici baz.
- "ten times" = "…miktarın on katı" / "on katı dozda" [864] [866]; 100 lb = 45 kg (FP-TR-D3).
- Doc's 'Nothing I can name' = "Adını koyabileceğim bir şey değil" [856]; 'Somebody put that there. And they knew exactly how much to put.' = "Biri bunu oraya koymuş. Ve tam olarak ne kadar koyacağını biliyormuş." — identical in the Ch15 echo [1206].
- Renée's 'Poor woman. Such a shame about her troubles just now.' = "Zavallı kadın. Şu sıralar başına gelen dertler ne yazık." [236] — quoted back identically [238] (`Başına gelen dertler mi?`) and in Ch15 [1210] (MT had three different wordings incl. `ne büyük utanç` = 'what a disgrace').
- Varney's 'A week. Maybe more, if the parts for the sink don't come.' = "Bir hafta. Lavabonun parçaları gelmezse belki daha uzun." identical [782] [1178].
- 'two degrees under code' = "yönetmeliğin iki derece altında" identical [778] [1255] [1259] (FP-TR-D2). Grout / weather-strip / hand-sink = **derz / rüzgârlık / el lavabosu** at [778] [791] [1255] [1259] [1343] [1371] [1540] [1565] (MT: derz dolgu, fuga, hava fitili, pencere fitili, eskitme şerit, hava sızdırmazlığı, eviye, evye, el yıkama lavabosu).
- old gate key: "Hiç değiştirmedim" [1561] / "Hiç değiştirmedin" [1755]; key cut = "yaptırmıştım" [1747] [1825]; key ring = anahtarlık (MT `halkamda` [1561]).
- order book = Şükran Günü sipariş defteri; Martha's order = "iki çikolatalı-cevizli turta ve bir düzine çörek" identical [1119] [1522] [1547] [1971] (MT: kek/ekmek/rulo/'roll' variants); pies = **turta** throughout (MT pasta/kek).
- flour bin = **un bidonu** (MT kutu / çuval / saklama kutusu / ambar); Joyce's white baker's coat = **fırıncı ceketi** (MT önlük); Pete's locker = **soğuk hava deposu** (MT dolap ×3); loading dock = **rampa** (MT rıhtım 'quay' ×7, iskele 'pier'); the van = minibüs (MT kamyonet ×2).
- The founder's line "Biline ki Frost Falls güçlüler tarafından kurulmadı. Komşulukla kuruldu." identical [591] [617] [2090] (MT Ch26 `Komşumsu olanlar tarafından kurulmuştur` — non-word).
- Renée's "sanki hep buradaymışım gibi" identical [1245] [1279].
- The gold carton / thin figure / van stay ungendered (MT made Danny's figure 'a man' [1494]).

## Lessons checklist (FF_PROOFREAD_BRIEF)
- Note vs letters: Book-2 plot, n/a here. Joyce's Ch27 letter = mektup; the August lawyer's letter = avukat mektubu; the complaint = şikâyet (dilekçesi).
- Units (SAFE unless stated): six inches ×2 already 15 cm; 'six inches' [688] `altı inçlik` → 15 cm; 'a foot high' [341] → 30 cm; 'A foot, perhaps two' [716] (MT `Bir karış`) → 30/60 cm; 'ten feet' [728] [1500] (MT `on adım`) → 3 m; 'a pinch in fifty pounds' [1383] → 23 kg; 'a pound of chocolate' [1767] → yarım kilo; '100 lb' [864] → 45 kg (FP-TR-D3); idioms 'an inch at a time' [625] → santim santim, 'not one inch nearer' [1267] → bir adım, 'by the mile' [1091] → metrelerce. 'A hundred feet' = FOOTPRINTS — MT already "Yüzlerce ayak izi" [905]. 'six clean feet' already iki metre. No imperial token left (grep inç/libre/pound/ons/mil/feet = 0).
- Currency: dollars/cents only (dolar, kuruş idiom "tek bir kuruş" = 'a dime', kept as idiom); no lira.
- Snowball = Snowball (as Frost and Found TR, 47×). Pip: Turkish ungendered; one wrong gendered noun fixed (`dedi Nick kıza` 'to the girl' [1470]); Jessica's forms OK. No masculinised narrator.
- Circle = **çember** (Frost and Found TR majority; MT mixed halka ×19). Historical Society = **Tarih Cemiyeti / Cemiyet** (FP-TR-D6). The green = **meydan** (Book 1 majority; MT yeşillik / yeşil alan / köy meydanı / park). Avenue = cadde (MT bulvar ×5, Avenue, Sokağı). Doc = **Doktor** (Book 1; MT Doc / Dok / Dr.). Chief = Şef Tanaka (MT `Tanaka Hanım`, `emniyet müdürü`). County = **ilçe** (MT eyalet/vilayet/bölge/**kontluk** = earldom); state = eyalet. Inn(s) = otel (MT han 'caravanserai'). Barrel = varil (MT fıçı). Balsam = köknar (MT balsam). Wreath frame/hoop = iskelet/kasnak (avoid the circle word). Brad = çivi (MT raptiye, tel zımba, kıskaç).
- Reindeer: "ren geyikleri" [739] (Book 1 form); none named. Cider: none in this book.
- Title page `Unun Oyunu` → `<bt>Flour Play</bt>` (Book 1 TR shows its English title anchored); series line `Kitap 3` → `3. Kitap` (Book 1 `1. Kitap`); series list anchored ×3.
- 'Very nearly' = "Neredeyse." [50] (not reversed). Blurb: no Sam/debtor content; blurb fixed ('reaches for the easy names', 'the thing that fits', 'That is a trade', funeral).
- Narrative tense: -di past in every chapter (checked); blurb present like the English.
- MT notes printed in prose: none found. English duplicate paragraphs: none.
- Words from other languages: Amharic, Tamil, Azerbaijani letters (see worst defect 5) — removed.
- Numbers: Joyce 65 [1842] ✓; partnership 15 yrs / split 25 yrs ago / started ~40 yrs ago ✓; 'the twentieth' [1202] [1544] ✓; 'two counties' fixed.
- Graffiti DIRTY → PİS (not a vulgarity).
- Final line "Start reading The Binder's Bequest today!" present [2275]. The **second** sell line (EN [1387]) is missing — FP-TR-D4.

## Dialogue conversion (ruling 1) — systemic finding
- Before: « » in 361 paragraphs (Ch2–16, 21, 22, excerpt), straight "…" (Ch1, parts of Ch16), em-dash turns in Ch17–23 (Ch23 in Spanish-raya form `— Elimden ne gelirse — dedi parkasını açarak. — Gerçekten.`).
- After: every spoken turn opens with "— ", no closing mark, attribution after a comma (`— Bileklerde, dedim`), "diye sordu" frames kept, mid-line continuation without a new dash (`— Kozalaklardaki püf nokta şu, dedim bir tanesini yukarı kaldırarak, yerleştirmeden önce…`), narration between turns set off by dashes (Frost and Found TR style), quoted words and overheard speech inside narration in "…".
- Converted paragraphs (556): see `_APPLIED.md`. Attribution rebuilt by hand in ~110 more (class DLG in the table).

## Findings table (every applied change; Turkish quoted verbatim)
| # | Para | Ch | Class | Turkish before (verbatim) | Why (English) | Turkish after |
|---|---|---|---|---|---|---|
| 1 | [0] | Front | TITLE | Unun Oyunu | title page translated title; Book 1 TR title page carries the anchored English title | <bt>Flour Play</bt> |
| 2 | [4] | Front | TERM | Kitap 3 | series line matches Book 1 '1. Kitap' | 3. Kitap |
| 3 | [16] | Front | TITLE | Frost and Found | series list title anchor (as Book 1) | <bt>Frost and Found</bt> |
| 4 | [17] | Front | TITLE | Inn Trouble | series list title anchor (as Book 1) | <bt>Inn Trouble</bt> |
| 5 | [18] | Front | TITLE | Flour Play | series list title anchor (as Book 1) | <bt>Flour Play</bt> |
| 6 | [29] | Front | MT | Kocası öldükten sonraki sabah | 'the morning after her husband's funeral' | Kocasının cenazesinden sonraki sabah |
| 7 | [33] | Front | TERM | Evergreen Sokağı'ndaki | Evergreen Avenue = Evergreen Caddesi (Book 1) | Evergreen Caddesi'ndeki |
| 8 | [35] | Front | MT | Kasaba kolaya kaçıp suçluyu hemen buluyor: | 'reaches for the easy names' — the town does not find the culprit | Kasaba en kolay isimlere uzanıyor: |
| 9 | [35] | Front | TYPO | çalınma boya kutusuyla | 'a stolen can' | çalıntı bir boya kutusuyla |
| 10 | [35] | Front | MT | Jessica ise gerçeği nokta atışı buluyor; | 'reaches for the thing that fits' — not 'finds the truth' | Jessica ise yerine tam oturan şeye uzanıyor; |
| 11 | [35] | Front | MT | Bu ustalık gerektiren bir iş. | 'That is a trade' — someone who knows the trade | Bu, işini bilen birinin işi. |
| 12 | [40] | Ch1 | TERM | Halkadaki her kadın kendi | circle = çember (Book 1 majority) | Çemberdeki her kadın kendi |
| 13 | [42] | Ch1 | EN | Evergreen Avenue boyunca | English street word left in | Evergreen Caddesi boyunca |
| 14 | [42] | Ch1 | MT | karlarını silkelenerek | 'came in stamping' | ayaklarını vura vura |
| 15 | [42] | Ch1 | TYPO | gıcırdayıyordu | typo | gıcırdıyordu |
| 16 | [42] | Ch1 | TYPO | balkabagi fenerlerini | missing Turkish letter ğ | balkabağı fenerlerini |
| 17 | [42] | Ch1 | EN | o sade pumpkins bal kabakları | English word 'pumpkins' left in | o sade bal kabakları |
| 18 | [46] | Ch1 | MT | İki dalı iskelete | 'three sprigs' — number | Üç dalı iskelete |
| 19 | [56] | Ch1 | TERM | ve kuru gülüşüyle halkanın öbür ucundan güldü. | circle = çember | ve kuru gülüşüyle çemberin öbür ucundan güldü. |
| 20 | [58] | Ch1 | TERM | bakanlar hariç bütün halka oradaydı. Olivia, dükkânının | circle = çember | bakanlar hariç bütün çember oradaydı. Olivia, dükkânının |
| 21 | [60] | Ch1 | TYPO | alınırırdı | typo | alınırdı |
| 22 | [60] | Ch1 | MT | kırmızı yün çilelerinden yaptığı yuvaya | 'a fallen skein of red wool' — one fallen skein | yere düşmüş kırmızı bir yün çilesinden yaptığı yuvaya |
| 23 | [60] | Ch1 | TERM | Ve Pip; halkadan biri değildi ama | circle = çember | Ve Pip; çemberden biri değildi ama |
| 24 | [80] | Ch1 | TYPO | O bir kez olmuşt, | truncated verb | O bir kez oldu, |
| 25 | [84] | Ch1 | MT | Martha’cım seninkini yiyeceğine söz verene kadar | narration turned into an address 'Martha dear, yours'; EN 'until Martha promised to eat hers' | Martha kendi kekini yiyeceğine söz verene kadar |
| 26 | [88] | Ch1 | TERM | bütün kuruşlar Tarih Derneği’nin çatı fonuna gidiyor. | Historical Society = Tarih Cemiyeti / Cemiyet (Book 1 majority; MT mixed Dernek/Cemiyet) | bütün kuruşlar Tarih Cemiyeti’nin çatı fonuna gidiyor. |
| 27 | [90] | Ch1 | TERM | işe koyulduk. Sohbet, halka sohbetlerine mahsus olduğu | circle = çember | işe koyulduk. Sohbet, çember sohbetlerine mahsus olduğu |
| 28 | [96] | Ch1 | TERM | Bu, halkanın dikkatini telden uzaklaştırdı. | circle = çember | Bu, çemberin dikkatini telden uzaklaştırdı. |
| 29 | [100] | Ch1 | MT | Hani bir yeri yerleştirirken | 'fitting a place out' | Hani bir yeri döşeyip hazırlarken |
| 30 | [104] | Ch1 | TERM | dalını çevirdim ve halkaya adını koyamayacağım bir | circle = çember | dalını çevirdim ve çembere adını koyamayacağım bir |
| 31 | [112] | Ch1 | TERM | Yeşillik, Yarn Tales’ın karşısında, tepesinde savaş anıtı ve uzak ucunda ulu karaağaç bulunan geniş ve beyaz bir meydandı. | the green = meydan (Book 1) | Meydan, Yarn Tales’ın karşısındaydı; tepesinde savaş anıtı, uzak ucunda ulu karaağaç bulunan geniş, bembeyaz bir açıklık. |
| 32 | [116] | Ch1 | TERM | dükkânlara doğru, yeşilliğe çevirmişti | 'pointed away up the green toward the shops'; the green = meydan | meydan boyunca dükkânlara doğru çevirmişti |
| 33 | [128] | Ch1 | TERM | buydu zaten ve halka bunu benimsedi; biri | circle = çember | buydu zaten ve çember bunu benimsedi; biri |
| 34 | [128] | Ch1 | TERM | yağmazdı dedi ve halka sohbetlerinin yapacağı gibi | circle = çember | yağmazdı dedi ve çember sohbetlerinin yapacağı gibi |
| 35 | [130] | Ch1 | MT | turuncudan alta çeviriyordu | 'from orange to gold' — 'alta' = 'to the bottom' | turuncudan altın rengine çeviriyordu |
| 36 | [134] | Ch1 | TERM | Kar, yeşilliğin üzerinde, | the green = meydan | Kar, meydanın üzerinde, |
| 37 | [134] | Ch1 | TERM | Ama bunların hiçbirini halkaya söylemedim. Bir zencefilli | circle = çember | Ama bunların hiçbirini çembere söylemedim. Bir zencefilli |
| 38 | [145] | Ch2 | MT | Havada belli belirsiz ama yanlışlığından sual olunmaz, hafifçe kesilmiş gibi bir tat. | 'a thin, curdled edge to the air, faint but unmistakable' — garbled | Havada ince, kesilmiş süt gibi bir keskinlik vardı; belli belirsiz ama şaşmaz. |
| 39 | [159] | Ch2 | MT | Onlardan önce bir posta çörek daha, fritözün aldığı kadar. | 'a run of doughnuts' (MT 'more rolls') | Onlardan önce bir posta donut, fritözün aldığı kadar. |
| 40 | [159] | Ch2 | MT | Hepsini mahvetmişti. | 'Every one of them was ruined' — Greta did not ruin them | Hepsi mahvolmuştu. |
| 41 | [159] | Ch2 | MT | Dün öğleden sonra ne pişirdimse. | 'Everything I've baked since yesterday noon' | Dün öğleden beri ne pişirdiysem. |
| 42 | [175] | Ch2 | TYPO | ayırtıttığı | typo | ayırttığı |
| 43 | [175] | Ch2 | TERM | Frost Falls’un yarısının ayırttığı pastalar ve ekmekler | pies = turta (Greta's Thanksgiving pies) | Frost Falls’un yarısının ayırttığı turtalar ve ekmekler |
| 44 | [177] | Ch2 | MT | isteyen bir sürü eşkıya. | 'Some outfit' — a company, not 'a bunch of bandits' | isteyen bir şirket. |
| 45 | [181] | Ch2 | MT | çörekler, halkalar ve ekmekler | 'the rolls, the doughnuts and the bread' (halka collides with the circle word) | çörekler, donutlar ve ekmekler |
| 46 | [193] | Ch2 | MT | kokusu bozulmuş bir mayıs balığına | herring = ringa (as elsewhere in the book) | kokusu bozulmuş bir ringa balığına |
| 47 | [197] | Ch2 | MT | Ama Greta’nın, penguenin açıklayamayacağım fikrinden başka dertleri de vardı zaten. | 'Greta had worries enough without a penguin's opinion I couldn't explain' | Ama Greta’nın derdi zaten başından aşkındı; bir de açıklayamayacağım bir penguen görüşüne ihtiyacı yoktu. |
| 48 | [216] | Ch3 | MT | Aralarında fark varmış, bana da söylerler muhtemelen, hepimize söylerler. | 'There's a difference, I'm told, and I expect we'll all be told again' | Aralarında fark varmış, öyle söylediler; eminim hepimize bir daha söylenecek. |
| 49 | [226] | Ch3 | EN | Mrs. Claus olmalısınız | English title 'Mrs.' | Bayan Claus olmalısınız |
| 50 | [228] | Ch3 | TYPO | Sabah beri | case suffix missing | Sabahtan beri |
| 51 | [236] | Ch3 | MT | Şu sıralar işlerinin kötü gitmesi ne büyük utanç. | 'Such a shame about her troubles just now' — 'utanç' = disgrace; line is quoted back later, wording fixed here | Şu sıralar başına gelen dertler ne yazık. |
| 52 | [238] | Ch3 | MT | — İşlerinin kötü gitmesi mi? dedim. | echo of Renée's 'her troubles' | — Başına gelen dertler mi? dedim. |
| 53 | [240] | Ch3 | TYPO | tam bir sempatikle | 'sempatikle' is not a word; 'all sympathy' | tam bir şefkatle |
| 54 | [240] | Ch3 | DLG | bir kez lekelendi mi, bana dürüst ve pişmanlık duyan bir ifadeyle, sanki bir sırrı dostuyla paylaşan bir meslektaş gibi baktı, insanlar konuşuyor, değil mi? | narration inside the speech not set off (dash system) | bir kez lekelendi mi — bana dürüst ve hayıflanan bir ifadeyle, sanki bir dostuna sır veren bir meslektaş gibi baktı — insanlar konuşuyor, değil mi? |
| 55 | [240] | Ch3 | TYPO | meraba | typo | merhaba |
| 56 | [244] | Ch3 | TYPO | Pip, gözü hala altın harflerde olacak | 'hala' (= aunt) for 'hâlâ' (still) | Pip, gözü hâlâ altın harflerde olacak |
| 57 | [248] | Ch3 | MT | onlarsız düzgün bir kabuk | 'without it' (the steam injection) | o olmadan düzgün bir kabuk |
| 58 | [248] | Ch3 | DLG | Aralık ayının ne olduğunu biliyorum, Jessica. — Pırıl pırıl odasının etrafına gülümseyerek baktı, — Frost Falls, Frost Falls bir dinlenme yeri olacak. | speech/narration order garbled; 'Frost Falls is going to be a rest' | Aralık ayının ne demek olduğunu bilirim, Jessica. Frost Falls — pırıl pırıl mutfağına gülümseyerek göz gezdirdi — Frost Falls bana tatil gibi gelecek. |
| 59 | [256] | Ch3 | DLG | — Kendine güldü. Beni bağışlamalısınız. | resumed speech after narration needs its dash | — Kendine güldü. — Beni bağışlamalısınız. |
| 60 | [258] | Ch3 | TYPO | işine duyduğu sevgi gerçektir | tense | işine duyduğu sevgi gerçekti |
| 61 | [258] | Ch3 | TYPO | küçük altın rengi bir financiers kutusu | English plural -s on a loan word | küçük, altın rengi bir kutu financier |
| 62 | [264] | Ch3 | TYPO | Financiers'ların kalanını | English plural -s on a loan word | Financier’lerin kalanını |
| 63 | [264] | Ch3 | OM | Onu hala tezgahında, Hal Thompson’ın getirdiği bir kağıt parçası üzerine başlarını eğmiş halde buldum. | Hal leaning on the counter / 'the two of them' dropped; 'hala' = aunt | Onu hâlâ tezgâhının başında buldum; Hal Thompson da tezgâha yaslanmıştı, ikisi Hal’in getirdiği bir kâğıdın üzerine baş başa eğilmişlerdi. |
| 64 | [270] | Ch3 | MT | Yeni komşu ve ben bölgecilik yapıyorum. | 'being territorial' | Yeni bir komşu, ben de kendi bölgemi kıskanıyorum. |
| 65 | [270] | Ch3 | MT | Ama bu caddede ne kadarlık tatil ticareti var ki zaten, ve o da bunun küçük bir dilimi için Montreal’den buraya kadar gelmemiştir. | 'holiday business' ('tatil' = vacation) | Ama bu caddede yılbaşı sezonunun getireceği iş sınırlı ve o, bunun küçük bir dilimi için ta Montreal’den buraya gelmedi. |
| 66 | [272] | Ch3 | TYPO | bir financiers alıp | loan-word plural | bir financier alıp |
| 67 | [282] | Ch3 | TYPO | Frost Falls’daki | suffix harmony (Book 1: Falls’ta) | Frost Falls’taki |
| 68 | [284] | Ch3 | MT | iyi fikrinin sıradan bulunmasından | 'thought soft' | iyi fikrinin fazla yufka yürekli bulunmasından |
| 69 | [284] | Ch3 | TYPO | bir kutu bıraktığını hala hatırlarım. Bu yıl | 'hala' (= aunt) for 'hâlâ' (still) | bir kutu bıraktığını hâlâ hatırlarım. Bu yıl |
| 70 | [294] | Ch3 | MT | daha iyisini düşünemeden ikinci bir financiers'a uzandı | calque of 'think better of it'; loan-word plural | kendini tutamadan ikinci bir financier’ye uzandı |
| 71 | [300] | Ch3 | MT | Greta adına bölgecilik yapmamdan | 'being territorial' | Greta adına kıskançlık etmemden |
| 72 | [304] | Ch3 | MT | Evergreen’e saptığım köşede | 'where I turned off Evergreen' | Evergreen’den saptığım köşede |
| 73 | [309] | Ch4 | MT | Kilomu Hal'den ödünç aldığım terazide her şeyi iki kez tarttım | garbled 'Kilomu' | Her şeyi Hal'den ödünç aldığım terazide iki kez tarttım |
| 74 | [309] | Ch4 | MT | Kutu değil. Eğer bu da düzgün çıkmazsa, geçen birkaç gün havadaki kötü bir büyüden ibarettir, | REVERSED: 'If this comes out right' (MT 'if this doesn't come out right'); bin = bidon | Bidondan değil. Eğer bu düzgün çıkarsa, geçen birkaç gün havadaki bir uğursuzluktan ibarettir, |
| 75 | [315] | Ch4 | MT | Harika görünmüşlerdi. Kabarmış ve düzgün, altı altın sarısı renginde kızarmış | tense; 'altı' (underside) not in EN | Harika görünüyorlardı. Kabarmış ve düzgün, altın sarısı kızarmış |
| 76 | [317] | Ch4 | MT | Umut, bulutun geçen güneşin tarladan çekilmesi gibi yüzünden silindi. | garbled simile | Bir bulut geçince tarladan çekilen güneş gibi, umut yüzünden silindi. |
| 77 | [319] | Ch4 | MT | Kırk yıl ve ellerim sonunda unutmayı başardı. | 'my hands have finally gone and forgot how' | Kırk yıl, ve ellerim sonunda nasıl yapıldığını unuttu. |
| 78 | [323] | Ch4 | TERM | un kutusundan | flour bin = un bidonu (one term) | un bidonundan |
| 79 | [329] | Ch4 | MT | ben kahvemi henüz bitirmişken | 'before I'd finished my coffee' | ben daha kahvemi bitirmeden |
| 80 | [333] | Ch4 | TERM | sert, soğuk ve çimlerden gelen keskin rüzgarın içinde | 'off the green' = meydan | meydandan esen sert, soğuk, ufak bir rüzgârın içinde |
| 81 | [337] | Ch4 | MT | dişli bir boşluk | 'a jagged hole' | sivri kenarlı bir delik |
| 82 | [341] | Ch4 | UNIT | kırmızı harflerle bir ayak yüksekliğinde iki kelime | 'a foot high' → 30 cm (SAFE, arithmetic) | kırmızı harflerle otuz santim boyunda iki kelime |
| 83 | [341] | Ch4 | R3 | İlk kelime DİRİTY idi. İkincisi UNSAFE idi. | graffiti left in corrupted English; translated (not a vulgarity) | İlk kelime PİS idi. İkincisi TEHLİKELİ. |
| 84 | [341] | Ch4 | R3 | üç kelime daha vardı: DÖN'T EAT HERE. | graffiti translated; three words kept as three | üç kelime daha vardı: BURADA YEMEK YEMEYİN. |
| 85 | [345] | Ch4 | MT | Ama gece yarısı içeri giren her kimdiyse | 'whoever came in the night' — nobody came inside | Ama gece gelen her kimdiyse |
| 86 | [347] | Ch4 | TYPO | geçirmiştirm | typo | geçirmiştim |
| 87 | [349] | Ch4 | R3 | üzerindeki DİRİTY kelimesine | graffiti word | üzerindeki PİS kelimesine |
| 88 | [349] | Ch4 | MT | Yüzü, kendisi hakkında söylenmiş bir yalanın yanında halkın önüne çıkmaya zorlanmış gururlu bir kadının omuzlarındaki ağırlıkla çökmüş ifadesine bürünmüştü. | 'the stripped look of a proud woman made to stand in public beside a lie' | Yüzünde, kendisi hakkında söylenmiş bir yalanın yanında herkesin önünde durmaya zorlanan gururlu bir kadının o çırılçıplak kalmış ifadesi vardı. |
| 89 | [353] | Ch4 | MT | Kırk yıldır bu caddedeki en temiz mutfağı işletti. | wrong person ('işletti' = he/she ran) | Kırk yıldır bu caddedeki en temiz mutfağı ben işletiyorum. |
| 90 | [353] | Ch4 | TYPO | ister izin versinler ister vermesin | agreement | ister izin versinler ister vermesinler |
| 91 | [353] | Ch4 | MT | Yemeklerimden kim korkmak ister ki? | 'Who wants people to be afraid of my food?' | İnsanların yemeklerimden korkmasını kim ister ki? |
| 92 | [355] | Ch4 | R3 | DİRİTY ve UNSAFE ile DÖN'T EAT HERE yazan | graffiti words translated | PİS ve TEHLİKELİ ve BURADA YEMEK YEMEYİN yazan |
| 93 | [355] | Ch4 | MT | Hayatının en kötü sabahında bunu ona söylemek için durum fazla hassastı ama bundan eminim. | 'too half-seen to put to her'; tense | Henüz yarım yamalak gördüğüm bir şeydi, hayatının en kötü sabahında ona söylenecek gibi değildi; ama bundan emindim. |
| 94 | [373] | Ch4 | MT | Pip'in bota sıkıca yaslandığı | 'my boot' | Pip'in botuma sıkıca yaslandığı |
| 95 | [375] | Ch4 | MT | herkes iyi bir kadının ve ona yapılanların karşısında dimdik durmaya kararlıydı | 'standing between a good woman and what had been done to her' | herkes iyi bir kadınla ona yapılan şeyin arasına girmeye kararlıydı |
| 96 | [377] | Ch4 | MT | Biri kasabanın konuşmasını kesinleştirmişti. | 'made sure the town would talk' | Biri, kasabanın bunu konuşmasını garantiye almıştı. |
| 97 | [383] | Ch4 | TYPO | kasti olarak | spelling | kasıtlı olarak |
| 98 | [391] | Ch4 | MT | Ivy, sırt tulumu ve bir kutu grafiti sökücü ile hırdavat dükkanından Tom'u da alarak bloktan yukarı geri döndü ve duvara çalışmaya koyuldu. | Tom (not Ivy) wore coveralls and carried the remover; 'sırt tulumu' wrong | Ivy, hırdavat dükkânından Tom'u da alarak bloktan yukarı geri döndü; iş tulumlu Tom'un elinde bir kutu grafiti sökücü vardı ve hemen duvara koyuldu. |
| 99 | [395] | Ch4 | TERM | beyaz fırıncı önlüğünün üzerine | Joyce's white baker's coat = fırıncı ceketi (one term; apron = önlük) | beyaz fırıncı ceketinin üzerine |
| 100 | [405] | Ch4 | MT | Şoförüm han seferini yapıyor | 'the inn run' — 'han' is archaic caravanserai | Şoförüm otelin teslimatını yapıyor |
| 101 | [405] | Ch4 | MT | Yardımımın dokunacağını düşündü. | 'Thought you'd want hands' | Yardıma ihtiyacın olur diye düşündü. |
| 102 | [409] | Ch4 | REG | — Sen tut, ben süpüreyim, dedi. Kuşunu buradan uzak tut. | Joyce and Jessica not yet introduced → siz (ruling 2); switch to sen after the first-name exchange | — Siz tutun, ben süpüreyim, dedi. Kuşunuzu buradan uzak tutun. |
| 103 | [411] | Ch4 | MT | tüylerini sımsıkı kabartarak | 'feathers drawn in tight' (opposite of ruffled) | tüylerini sımsıkı gövdesine yapıştırmış hâlde |
| 104 | [427] | Ch4 | OM | bakışıyla ön lastiğin yanında duruyordu. | 'studying the bright chrome hubcap' dropped | bakışıyla parlak krom jant kapağını inceleyerek ön lastiğin yanında duruyordu. |
| 105 | [431] | Ch4 | MT | yukarı bakmadan | 'without looking up' | başını kaldırmadan |
| 106 | [439] | Ch4 | TERM | parkasını beyaz önlüğün üzerine | white baker's coat | parkasını beyaz ceketin üzerine |
| 107 | [445] | Ch4 | MT | arabayı kaldırımdan aşağı, bloğun uzak ucuna doğru sürdü | 'pulled out, up the avenue' | arabayı çıkarıp caddeden yukarı, bloğun uzak ucuna doğru sürdü |
| 108 | [447] | Ch4 | R3 | DİRİTY yazısının | graffiti word | PİS yazısının |
| 109 | [452] | Ch5 | MT | Kapıdan içeri hırsla girdiğim an | 'came in stamping' (snow off boots), not 'angrily' | Ayaklarımdaki karı silkeleyerek içeri girdiğim an |
| 110 | [454] | Ch5 | DLG | Dot, küçük ve sert bir çıtırtıyla bir tel parçasını dişleriyle koparırken — Pencere de duvar da, dedi. Tom boyayı çıkardı. | dash turn must open the paragraph; attribution rebuilt | — Pencere de duvar da, dedi Dot, bir tel parçasını küçük ve sert bir çıtırtıyla dişleriyle koparırken. — Tom boyayı çıkardı. |
| 111 | [460] | Ch5 | DLG | Yalnızca benim duyabileceğim alçak bir sesle — Bunu araştırdığına sevindim, dedi. Hepimiz sevindik. | attribution rebuilt for the dash system | — Bunu araştırdığına sevindim, dedi yalnızca benim duyabileceğim alçak bir sesle. — Hepimiz sevindik. |
| 112 | [460] | Ch5 | MT | cesaretimi ne hale getirdiğini | 'my composure' | soğukkanlılığımı ne hâle getirdiğini |
| 113 | [462] | Ch5 | DLG | Olivia teli eline alarak ortaya doğru, — Bu sabah Joyce Wendt içeri girdiğinde Greta'nın yüzünü gören oldu mu? diye sordu. | attribution rebuilt | — Bu sabah Joyce Wendt içeri girdiğinde Greta'nın yüzünü gören oldu mu? diye sordu Olivia, teline uzanırken herkese hitaben. |
| 114 | [464] | Ch5 | DLG | Dot, — Herkes gördü, dedi. | attribution rebuilt | — Herkes gördü, dedi Dot. |
| 115 | [466] | Ch5 | MT | Joyce'u severdim. | 'I'd liked Joyce' (just met) | Joyce'u sevmiştim. |
| 116 | [470] | Ch5 | DLG | Ivy, — Annem Şükran Günü pastalarımızı ikisinden alırdı, dedi. | attribution rebuilt; pies = turta | — Annem Şükran Günü turtalarımızı ikisinden alırdı, dedi Ivy. |
| 117 | [472] | Ch5 | TERM | pastanın kime ait olduğu | pie = turta | turtanın kime ait olduğu |
| 118 | [474] | Ch5 | DLG | Ellie biraz hüzünlü bir sesle, — Çikolatalı-cevizli, dedi. Joyce o tarifin | attribution rebuilt; 'the chocolate-pecan' (pie) | — Çikolatalı-cevizli turta, dedi Ellie biraz hüzünlü bir sesle. — Joyce o tarifin |
| 119 | [476] | Ch5 | MT | Greta da hep kendisinin söylediğini iddia etti ve ikisi de bir adım bile geri adım atmadı. | garbled 'And Greta always said it was hers' | Greta da hep tarifin kendisine ait olduğunu söylerdi ve ikisi de bir milim bile geri adım atmazdı. |
| 120 | [476] | Ch5 | MT | Hanlar ve hastane için. | 'the inns' | Oteller ve hastane için. |
| 121 | [478] | Ch5 | DLG | Ivy, — Joyce'un gelmesi hoş bir davranıştı, dedi. | attribution rebuilt | — Joyce'un gelmesi hoş bir davranıştı, dedi Ivy. |
| 122 | [482] | Ch5 | DLG | Ivy'nin o koca kahkahası bugün içinde hiç yokmuş gibi, — Mesele şu ki, dedi, kim? | attribution rebuilt | — Asıl soru şu, dedi Ivy; o koca kahkahasından bu öğleden sonra eser yoktu. — Kim? |
| 123 | [484] | Ch5 | DLG | Claire, — Mesele tam da bu, dedi. | attribution rebuilt; echoes 'That's the question, all right' | — Asıl soru da bu işte, dedi Claire. |
| 124 | [486] | Ch5 | MT | hiçbirine karşı çıkmadım | 'gave none of it back' | hiçbirine bir şey eklemedim |
| 125 | [488] | Ch5 | DLG | Dot, — Kimsenin söylemek istemediği şeyi ben söyleyeyim, nasıl olsa yaşlandım ve umurumda değil, dedi. Pete Garcia. | attribution rebuilt | — Kimsenin söylemek istemediği şeyi ben söyleyeyim, dedi Dot, nasılsa yaşlandım, umurumda da değil. Pete Garcia. |
| 126 | [492] | Ch5 | DLG | Ellie yumuşak bir sesle, — Yapma, Dot, dedi. | attribution rebuilt | — Yapma, Dot, dedi Ellie yumuşak bir sesle. |
| 127 | [494] | Ch5 | MT | — Şimdi hiç de bile. | 'Now nothing' (answering 'Now, Dot') | — Yapması falan yok. |
| 128 | [496] | Ch5 | DLG | Claire, — Dükkânı meydanın karşısında ve içeri kamyon sokmanın hiçbir yolu yok, dedi, bu yüzden | attribution rebuilt | — Dükkânı meydanın karşısında ve içeri kamyon sokmanın hiçbir yolu yok, dedi Claire, bu yüzden |
| 129 | [498] | Ch5 | DLG | Dot, — Temmuz ayında zincire vurdu ki kadının unu içeri giremesin, dedi. Kadın belediyeyi şikâyet etti. O da çöplüğündeki fareler için belediyeyi aradı. | attribution rebuilt; 'rats at her bins' | — Temmuz ayında kadının unu içeri giremesin diye zincire vurdu, dedi Dot. Kadın onu belediyeye şikâyet etti. O da kadının çöp bidonlarındaki fareler yüzünden belediyeyi aradı. |
| 130 | [498] | Ch5 | MT | her saat başı o sokakta | 'at all hours' | saatli saatsiz o sokakta |
| 131 | [500] | Ch5 | DLG | Ivy bunu istemeye istemeye onaylayarak, — Öyleymiş, dedi. Bana | attribution rebuilt | — Öyleymiş, dedi Ivy, istemeye istemeye kabul ederek. — Bana |
| 132 | [502] | Ch5 | DLG | Dot, — Bir kapıya kilit vuracak kadar öfkeliyse, daha kötüsünü yapacak kadar da öfkelidir, dedi. | attribution rebuilt; 'chain a gate' | — Bir kapıya zincir vuracak kadar öfkeliyse, daha kötüsünü yapacak kadar da öfkelidir, dedi Dot. |
| 133 | [504] | Ch5 | MT | her sabah iskeledeki en iyi kemikleri | 'on his dock' (loading dock), not a pier | her sabah rampasına en iyi kemikleri |
| 134 | [506] | Ch5 | DLG | Yumuşak bir dille, — Bu bir, dedim. Başka | attribution rebuilt | — Bu bir, dedim yumuşak bir dille. Başka |
| 135 | [508] | Ch5 | DLG | Ellie üzgün bir sesle, — Kimse iyi bir şeyden bahsetmiyor, dedi. | attribution rebuilt; 'Nobody kind' | — Hoş isimler değil, dedi Ellie üzgün bir sesle. |
| 136 | [512] | Ch5 | DLG | Ivy sessizce, — Bundan nefret ediyorum, dedi. | attribution rebuilt | — Bundan nefret ediyorum, dedi Ivy sessizce. |
| 137 | [514] | Ch5 | DLG | Beklemediğim kadar sert bir tonla, — Bu hem zalimce hem de tembelce, dedim ve çemberdekiler başını kaldırdı. Yumuşatmak için devam ettim: — Özür dilerim. | attribution rebuilt | — Bu hem zalimce hem de tembelce, dedim, istediğimden daha sert bir sesle, ve çemberdekiler başını kaldırdı. Sözümü yumuşattım. — Özür dilerim. |
| 138 | [516] | Ch5 | DLG | Ellie, sanki birinin ona bunu taşımak zorunda olmadığını söylemesini bekliyormuş gibi rahatlamış ve sakin bir sesle, — Çıkarılmayacak, ben de çıkarmayacağım, dedi. Sadece | attribution rebuilt | — Çıkarılmayacak, ben de çıkarmayacağım, dedi Ellie; sesi sakin ve rahatlamıştı, sanki birinin ona bunu taşımak zorunda olmadığını söylemesini bekliyormuş gibi. — Sadece |
| 139 | [518] | Ch5 | DLG | Dot, — Söylenmiş ve utanılmış sayalım, dedi ve | attribution rebuilt | — Söylenmiş ve utanılmış sayalım, dedi Dot ve |
| 140 | [520] | Ch5 | DLG | Claire kalemini vurarak, — Ve üçüncüsü, dedi, editörümün | attribution rebuilt | — Ve üçüncüsü, dedi Claire kalemini vurarak, editörümün |
| 141 | [522] | Ch5 | DLG | Olivia, — Çocuklar, diye onayladı ve | attribution rebuilt | — Çocuklar, diye onayladı Olivia ve |
| 142 | [522] | Ch5 | TYPO | Çalınma bir kutu boyayla | 'stolen' | Çalıntı bir kutu boyayla |
| 143 | [524] | Ch5 | DLG | Ivy, — Festival bittikten sonra karanlıktan sonra meydanda gezinen bir sürü çocuk var artık, dedi. | attribution rebuilt; doubled 'sonra' | — Festival bittiğinden beri hava karardıktan sonra meydanda takılan bir sürü çocuk var, dedi Ivy. |
| 144 | [526] | Ch5 | DLG | Claire not alarak, — İşin ne kadar amatörce olduğunu açıklar, dedi. Harfler birbirine girmiş. Kim yaptıysa birbirine girmesini önemsememiş. | attribution rebuilt; 'the letters ran' (paint ran) | — İşin ne kadar kaba saba olduğunu da açıklar, dedi Claire not alarak. Harfler akmış. Kim yaptıysa akmasını önemsememiş. |
| 145 | [528] | Ch5 | MT | Yine de boyayla mahvedilen pastaların aynı kişinin marifeti olması gerekmiyordu: | 'the paint and the ruined batches' — not batches ruined with paint | Yine de boyanın ve mahvolan partilerin aynı elden çıkmış olması gerekmiyordu: |
| 146 | [532] | Ch5 | DLG | Olivia sevgi dolu bir sesle, — Sen aynen böylesin işte, dedi. İkimiz çaydanlık | attribution rebuilt; 'the rest of us' (not 'the two of us') | — Sen aynen böylesin işte, dedi Olivia sevgi dolu bir sesle. Biz çaydanlık |
| 147 | [536] | Ch5 | DLG | Martha, — Hak ediyor, dedi ve | attribution rebuilt | — Hak ediyor, dedi Martha ve |
| 148 | [538] | Ch5 | OM | Zil çaldı ve Emma Redfern, kulakları kıpkırmızı bir şekilde soğuktan kaçarak içeri girdi. | 'eight years old' dropped | Zil çaldı ve Emma Redfern soğuktan içeri girdi; sekiz yaşındaydı, kulaklarına kadar kızarmıştı. |
| 149 | [544] | Ch5 | REG | Saygılarınızı sunabilirsiniz. | Jessica to a child → sen (ruling 2) | Saygılarını sunabilirsin. |
| 150 | [548] | Ch5 | DLG | Martha çocuğa, — Kilisenin olduğu taraftaki buza dikkat et, dedi. | attribution rebuilt | — Kilisenin olduğu taraftaki buza dikkat et, dedi Martha çocuğa. |
| 151 | [550] | Ch5 | DLG | Emma, sekiz yaşındaki tüm ciddiyetiyle, — Hep öyle yapıyorum, dedi. | attribution rebuilt | — Hep öyle yapıyorum, dedi Emma, sekiz yaşının bütün ciddiyetiyle. |
| 152 | [556] | Ch5 | MT | Kapıda durup sundurma korkuluğundan düşmüş bir buz sarkıtını inceledi, bunun bir balık olduğuna karar veremeyip yola devam etti. | REVERSED-ish: 'decided it was not a fish'; 'at the gate' | Bahçe kapısında durup sundurma korkuluğundan düşmüş bir buz sarkıtını inceledi, bunun balık olmadığına karar verip yoluna devam etti. |
| 153 | [561] | Ch6 | TERM | Frost Falls Tarih Derneği, meydanda, yeşil kapısı | Society = Cemiyet | Frost Falls Tarih Cemiyeti, meydanda, yeşil kapısı |
| 154 | [567] | Ch6 | TERM | asitsiz kağıt şeritleri. Derneği her seferinde bir | Society = Cemiyet | asitsiz kağıt şeritleri. Cemiyeti her seferinde bir |
| 155 | [573] | Ch6 | NM | Tanaka Hanım, biri geldiğinde | Chief Tanaka = Şef Tanaka | Şef Tanaka, biri geldiğinde |
| 156 | [575] | Ch6 | MT | O yüzden ona göre yargılama. | 'don't judge her by them' | O yüzden onu bunlara bakarak yargılama. |
| 157 | [575] | Ch6 | REG | — Artık bir dükkân sahibinin değil, bir bekçinin kulağına sahipsin. | Jessica ↔ Theo siz both ways (ruling 2; Ch18 MT already siz) | — Artık bir dükkân sahibinin değil, bir bekçinin kulağına sahipsiniz. |
| 158 | [575] | Ch6 | REG | — Sana bunları getirdim. Greta'nın tarifi, benim ellerim. O yüzden onu bunlara bakarak yargılama. | Theo formal | — Size bunları getirdim. Greta'nın tarifi, benim ellerim. O yüzden onu bunlara bakarak yargılamayın. |
| 159 | [579] | Ch6 | REG | — Çok naziksin, dedi | Theo addresses Jessica as 'Bayan Claus' → siz | — Çok naziksiniz, dedi |
| 160 | [581] | Ch6 | REG | — Ne buldun? | Theo formal | — Ne buldunuz? |
| 161 | [583] | Ch6 | TERM | her gün arşivdeydi. Derneğin evrakları geçen ayki | Society = Cemiyet | her gün arşivdeydi. Cemiyetin evrakları geçen ayki |
| 162 | [585] | Ch6 | NM | — Tanaka Hanım onları yeniden sıraya koymamı emretti, dedi. | Chief Tanaka; 'set me to' | — Şef Tanaka onları yeniden düzene sokmakla beni görevlendirdi, dedi. |
| 163 | [585] | Ch6 | TYPO | Yüksek rafından | suffix | Yüksek raftan |
| 164 | [587] | Ch6 | MT | son çiviyi de boşa çıkarıp | 'easing the last brad free' | son çiviyi de gevşetip çıkarıp |
| 165 | [591] | Ch6 | MT | İlk kış neredeyse dayanamıyorduk. | 'The first winter we near did not keep' | İlk kışa az kalsın dayanamayacaktık. |
| 166 | [591] | Ch6 | TYPO | hiçbir kadının kiler de | possessive | hiçbir kadının kileri de |
| 167 | [593] | Ch6 | MT | Bunu ben kurdum değil. Birbirimizi hayatta tuttuk ve nasıl hatırlayacağınızı unutmayın diyordu. | 'Not I built this. But we kept each other alive, and mind you remember how.' | Bunu ben kurdum, demiyordu. Birbirimizi hayatta tuttuk, nasıl tuttuğumuzu da sakın unutmayın, diyordu. |
| 168 | [595] | Ch6 | MT | Tapularda adımız, | 'her name on the deeds' | Tapularda adı, |
| 169 | [601] | Ch6 | TERM | yeniden vardım. Arkamızda, Derneğin başköşeye oturttuğu ön | Society = Cemiyet | yeniden vardım. Arkamızda, Cemiyetin başköşeye oturttuğu ön |
| 170 | [603] | Ch6 | TERM | yeşilliklerin altındaki | the green = meydan | meydanın altındaki |
| 171 | [603] | Ch6 | TERM | bir balsam dalı | balsam = köknar elsewhere | bir köknar dalı |
| 172 | [605] | Ch6 | MT | ipi tutan iki sıra hâlâ kilise kadar sessiz, içinde kendilerine ait yüz yıllık bir kapalılık olduğunu bilerek. | garbled | ipe tutunmuş iki sıra hâlinde, kilisedeki gibi sessiz; içinde kendilerine ait yüz yılın kapalı durduğunu biliyorlardı. |
| 173 | [605] | Ch6 | MT | Ben değilim. | 'Not me.' | Ben değil. |
| 174 | [607] | Ch6 | REG | — Bu bulduğun cümle, | Theo formal | — Bu bulduğunuz cümle, |
| 175 | [611] | Ch6 | TERM | ona çok sevdiği Derneğin başındaki yerini mal | Society = Cemiyet | ona çok sevdiği Cemiyetin başındaki yerini mal |
| 176 | [617] | Ch6 | NM | Gazete'de | paper name Gazette (as Book 1) | Gazette'de |
| 177 | [617] | Ch6 | MT | Kelly, gazetenin kasasının yanındaki Starlight tezgâhının arkasına yapıştırmıştı; | 'taped hers behind the counter by the register' | Kelly kendi kupürünü Starlight tezgâhının arkasına, kasanın yanına yapıştırmıştı; |
| 178 | [617] | Ch6 | R3 | KİRLİ yazısı | graffiti word = PİS (as Ch4) | PİS yazısı |
| 179 | [619] | Ch6 | TERM | yavaş, insanlar akıllarını Derneğe çevirmeye başladılar. | Society = Cemiyet | yavaş, insanlar akıllarını Cemiyete çevirmeye başladılar. |
| 180 | [621] | Ch6 | TERM | vardı ve başlık Derneği Koru idi. | Society = Cemiyet | vardı ve başlık Cemiyeti Koru idi. |
| 181 | [623] | Ch6 | TERM | kaldırdı. — Yani. Dernek için bir varil. | Society = Cemiyet | kaldırdı. — Yani. Cemiyet için bir varil. |
| 182 | [625] | Ch6 | UNIT | inç inç onararak | 'an inch at a time' idiom → santim santim (SAFE) | santim santim onararak |
| 183 | [627] | Ch6 | MT | Kağıdı sevdiği gibi köşesinden katlayıp düzgünce katladım ve geri uzattım. | 'along its crease' | Kâğıdını, sevdiği gibi, kat yerinden düzgünce katlayıp geri uzattım. |
| 184 | [627] | Ch6 | TERM | geri uzattım. — Dernek hâlâ gerçek bir | Society = Cemiyet | geri uzattım. — Cemiyet hâlâ gerçek bir |
| 185 | [633] | Ch6 | MT | tam da duymaya en çok ihtiyaç duyduğumuz kış günü karşımıza çıkmıştı | 'the very winter' | tam da onu duymaya en çok ihtiyaç duyduğumuz kış ortaya çıkmıştı |
| 186 | [635] | Ch6 | TERM | Arkamda, Derneğin ön penceresinde tek | Society = Cemiyet | Arkamda, Cemiyetin ön penceresinde tek |
| 187 | [638] | Ch7 | TERM | Topluluk Merkezine gittiğim perşembe günü | the Society (not a 'community centre') | Cemiyete gittiğim perşembe günü |
| 188 | [640] | Ch7 | TERM | Evergreen Caddesi’nin karşısında, yeşil alanın öte yanında parka bakan dükkân sıralarının arasındaydı. | the green / the Park = meydan | Evergreen Caddesi’nin karşısında, meydanın öte yakasında, meydana karşıdan bakan dükkân sırasındaydı. |
| 189 | [640] | Ch7 | TYPO | karlan temizlenmiş | typo | karı temizlenmiş |
| 190 | [640] | Ch7 | MT | Kapının eşiğinde durduğumda, tepemdeki zil hâlâ sallanırken, o tek avlunun onun derdiyle Pete’inkini nasıl birbirine bağladığını gerektiği gibi hesaba katmamıştım. | 'until I stood on his mat' dropped | Kapının eşiğinde, tepemdeki zil hâlâ sallanırken durana kadar, o tek avlunun Pete’in derdini Greta’nınkine nasıl bağladığını gerektiği gibi hesaba katmamıştım. |
| 191 | [642] | Ch7 | REG | Buralarda pek sık göremeyiz seni. | Pete ↔ Jessica formal (ruling 2; he calls her Bayan Claus) | Buralarda pek sık göremeyiz sizi. |
| 192 | [644] | Ch7 | REG | Buralara düşüşüm sandığından daha sık olur | Pete formal | Buralara düşüşüm sandığınızdan daha sık olur |
| 193 | [644] | Ch7 | REG | içinde senin olduğun bir kasabada | Pete formal | içinde sizin olduğunuz bir kasabada |
| 194 | [644] | Ch7 | REG | bir aşçı için neyin var? | Pete formal | bir aşçı için neyiniz var? |
| 195 | [648] | Ch7 | REG | Kendi haline bırakacaksın ki duyduğuma göre senin için en zor kısmı bu zaten. | Pete formal | Kendi hâline bırakacaksınız ki duyduğuma göre sizin için en zor kısmı bu. |
| 196 | [648] | Ch7 | REG | Bana bir dakika ver. | Pete formal | Bana bir dakika verin. |
| 197 | [654] | Ch7 | REG | — Greta’yı duymuşsundur | Pete formal | — Greta’yı duymuşsunuzdur |
| 198 | [658] | Ch7 | REG | Hadi ama. Duymuşsundur. | Pete formal | Hadi ama. Duymuşsunuzdur. |
| 199 | [660] | Ch7 | MT | Kendi adıma buna hak verdiğimi duymazsın. | 'I haven't heard myself agree to it' (first person) | — Ama kendimi buna katılırken duymadım. |
| 200 | [662] | Ch7 | REG | Sana Greta’yla arkadaş olduğumuzu söyleyecek değilim. Değiliz, bunu sonradan yüzüme de vurdurmam. | Pete formal; 'won't have you catching me in it later' | Size Greta’yla arkadaş olduğumuzu söyleyecek değilim. Değiliz; sonradan beni bu yalanla yakalamanıza da izin vermem. |
| 201 | [662] | Ch7 | DLG | evet, kasabaya beni şikâyet etti ve evet, çenesi kasıldı, çöpleri ve fareler hakkında | narration inside speech set off; 'called the town on me' | evet, beni belediyeye şikâyet etti ve evet — çenesi kasıldı — çöp bidonları ve fareler hakkında |
| 202 | [668] | Ch7 | REG | — Tom bana ara saatlerde sokakta olduğunu söylüyor | Pete formal; 'at odd hours' | — Tom bana olmadık saatlerde sokakta olduğunuzu söylüyor |
| 203 | [668] | Ch7 | REG | Ondan yok satarmış gibi asma kilit alıyormuşsun. | Pete formal | Ondan yok satarmış gibi asma kilit alıyormuşsunuz. |
| 204 | [670] | Ch7 | MT | Aldığım tek şey bir horultu, | 'a snort' | Aldığım tek şey burnundan sert bir soluk, |
| 205 | [672] | Ch7 | TERM | dolabımı güvencesiz bırakacak değilim | Pete's locker = soğuk hava deposu (one term; kept distinct from the walk-in) | soğuk hava depomu güvencesiz bırakacak değilim |
| 206 | [672] | Ch7 | REG | Sana bunu uğursuz gösterme zahmetinden kurtarayım. | Pete formal; 'save you the trouble of finding it sinister' | Sizi bunu kötüye yorma zahmetinden kurtarayım. |
| 207 | [672] | Ch7 | MT | Kasap, dükkânlar açılmadan önce | 'the meat man' is the supplier, not the butcher | Et tedarikçisi, dükkânlar açılmadan önce |
| 208 | [676] | Ch7 | MT | — Bununla ilgili bana fısıldadılar, dedi, ekşi bir sesle. Ki bu da bir yenilikti. | 'It's been whispered at me. Which is a novelty.' (present) | — Arkamdan fısıldanıyor, dedi ekşi bir sesle. Bu da yeni bir şey. |
| 209 | [678] | Ch7 | TYPO | iki elinde bağlandığı rosto ile durdu | 'bağlandığı' | bağladığı rosto iki elinde, durdu |
| 210 | [678] | Ch7 | MT | dirseklerini kütüğe dayadı | 'leaned his knuckles on the block' | yumruklarını kütüğe dayadı |
| 211 | [680] | Ch7 | MT | — Sana bir şey söyleyeceğim, dedi, şimdi daha alçak sesle, öfkesi sesinden uçup gitmişti, ve bununla ne istersen yap, çünkü ben kendim bir anlam veremiyorum. Karanlıkta avluda olduğum o sabahlarda, orada tek başına olan sadece ben değildim. | Pete formal; speech/narration separated; 'I haven't been the only one down there' | — Size bir şey söyleyeceğim, dedi, şimdi daha alçak sesle; sesindeki sitem uçup gitmişti. — Bundan ne çıkarırsanız çıkarın, çünkü ben pek bir şey çıkaramıyorum. Karanlıkta avluda olduğum o sabahlarda, orada olan tek kişi ben değildim. |
| 212 | [680] | Ch7 | TERM | yeşil alanın karşısındaki Evergreen | the green = meydan | meydanın karşısındaki Evergreen |
| 213 | [680] | Ch7 | MT | Onunkinin arkalarında birileri vardı. | 'There's been somebody around the back of hers' | Onun dükkânının arkasında biri dolaşıyordu. |
| 214 | [680] | Ch7 | MT | Kasabınki değildi. | 'Not the meat man's' | Et tedarikçisininki değildi. |
| 215 | [684] | Ch7 | REG | — Bunu birine söyledin mi? | Pete formal | — Bunu birine söylediniz mi? |
| 216 | [686] | Ch7 | REG | Sana söylüyorum çünkü kasap dükkânına derimi yüzmeye değil, rosto almaya geldin. | Pete formal | Size söylüyorum, çünkü buraya derimi yüzmeye değil, rosto almaya geldiniz. |
| 217 | [686] | Ch7 | REG | Eğer gözün açık ortalıkta dolanan sensen, işte benim açık gözümün gördükleri. Bununla ne istersen yap. | Pete formal | Eğer gözünü açık tutup ortalıkta dolaşan sizseniz, işte benim açık gözümün gördükleri. Bununla ne isterseniz yapın. |
| 218 | [686] | Ch7 | TYPO | ipi muntazammış | typo | ipi muntazam |
| 219 | [688] | Ch7 | MT | — Parmak izleri vardır, dedim | 'There'd be prints' = footprints in the snow, not fingerprints | — Ayak izleri kalmıştır, dedim |
| 220 | [688] | Ch7 | UNIT | altı inçlik tertemiz bir tabaka | 'six inches' → 15 cm (SAFE; matches Ch1) | on beş santimlik tertemiz bir tabaka |
| 221 | [690] | Ch7 | MT | merdivenlerinin etrafında bot izleri | 'around her step' | basamağının etrafında bot izleri |
| 222 | [690] | Ch7 | REG | Ya da arkada dolabı olan, derisini kurtarmak için siluet uyduran kasap değilsen. | Pete formal; locker term | Ya da arkada soğuk hava deposu olan ve paçayı kurtarmak için siluet uyduran kasap değilseniz. |
| 223 | [696] | Ch7 | REG | Kısık ateş. Kendi haline bırak. | Pete formal | Kısık ateş. Kendi hâline bırakın. |
| 224 | [696] | Ch7 | REG | penceresine asla dokunmadığımı söylersin | Pete formal | penceresine asla dokunmadığımı söylersiniz |
| 225 | [704] | Ch7 | MT | Pete Garcia’yı elimde bir o yana bir bu yana tutup sakinleştiremiyordum. | 'could not get Pete Garcia to sit still in my hands one way or the other' | Pete Garcia’yı zihnimde bir türlü bir yere oturtamıyordum. |
| 226 | [706] | Ch7 | MT | Hediye paketine sarılmış ve ipiyle bağlanmış o çember için kolay bir etiket isteseydim: husumet, dolap, şafak vakti. | garbled: Pete is the gift-wrapped easy name for the circle | Çembere sunacak kolay bir isim isteseydim, o isim hediye paketi yapılmış, kendi ipiyle bağlanmış hazır duruyordu: husumet, soğuk hava deposu, şafaktan önceki saatler. |
| 227 | [706] | Ch7 | TYPO | Kavgasmda | typo | Kavgasında |
| 228 | [706] | Ch7 | MT | kasabın halihazırda sevmediği | 'somebody the town already disliked' (MT: 'the butcher') | kasabanın hâlihazırda sevmediği |
| 229 | [706] | Ch7 | TYPO | bir silüetti | spelling (siluet elsewhere) | bir siluetti |
| 230 | [708] | Ch7 | TYPO | derbimdi | typo | derdimdi |
| 231 | [715] | Ch8 | TYPO | Frost Falls’daki | suffix harmony | Frost Falls’taki |
| 232 | [716] | Ch8 | UNIT | Bir karış, belki iki. | 'A foot, perhaps two' → 30/60 cm (SAFE) | Otuz santim, belki altmış. |
| 233 | [716] | Ch8 | MT | Kiliseninkiler basamaklarından inmişlerdi. | 'The two by the church' | Kilisenin önündeki ikisi basamaklarından inmişti. |
| 234 | [717] | Ch8 | MT | Yeni bir insan gelip de etrafa bakana dek her seferinde kahkahaları kesen kısım da buydu. | 'each time a new soul came up the block and looked' | Bloğa her yeni biri gelip baktığında kahkahaları kesen de buydu. |
| 235 | [717] | Ch8 | EN | Üzerinde tek bir çizgi yok ነበር. | foreign-script (Amharic) word leaked into the prose | Üzerinde tek bir çizgi yoktu. |
| 236 | [717] | Ch8 | MT | Bir şakacının dikilip kar fırlatmak için turladığına dair bir bot izi yoktu. | 'where a prankster might have stood to heave' | Bir şakacının ittirmek için durmuş olabileceği yerin çevresinde dönen bir bot izi de yoktu. |
| 237 | [719] | Ch8 | TYPO | Ne var ki kasaba Hal’lerden ibaret değildir. | narrative tense | Ne var ki kasaba Hal’lerden ibaret değildi. |
| 238 | [719] | Ch8 | DLG | Biri, — Çözülme ve donma olayı, dedi. Kar eridikçe çöker. | attribution rebuilt | — Erime ve donma işi bu, dedi biri. Kar eridikçe çöker. |
| 239 | [728] | Ch8 | UNIT | on adım kadar uzağa yürümüştü | 'a good ten feet' → 3 m (SAFE) | üç metre kadar uzağa yürümüştü |
| 240 | [729] | Ch8 | TERM | Greta’nın un çuvalının yanında | flour bin = un bidonu | Greta’nın un bidonunun yanında |
| 241 | [732] | Ch8 | MT | Ve hepsinin altında, kibrit çöpü gibi, oda haftalardır o kokuyu taşıyordu; kesilmiş sedir ve adını koyamayacağınız sıcak bir şey. | garbled sentence | Ve hepsinin altında, odanın haftalardır taşıdığı o öbür koku vardı: çakılmış bir kibrit gibi, kesilmiş sedir ve adını koyamayacağınız sıcak bir şey. |
| 242 | [732] | Ch8 | TYPO | silişerek | typo | silerek |
| 243 | [735] | Ch8 | MT | Sıcak idi. Odanın dört bir yanına düşük ısı yayan odun sobasının sıcaklığı gibi değil. | 'the woodstove's heat, which was banked low across the room' | Sıcaktı. Odanın öbür ucunda kısık yanan odun sobasının sıcaklığıyla değil. |
| 244 | [735] | Ch8 | MT | bir çinekopu takip eder gibi | herring = ringa | bir ringa balığını takip eder gibi |
| 245 | [739] | Ch8 | MT | Bram kendinde değil. | 'beside himself' ('kendinde değil' = unconscious) | Bram fena hâlde bozuluyor. |
| 246 | [739] | Ch8 | MT | Elinden gelse geyiklerle birlikte çite kilitlerdi | 'locked in the paddock with the reindeer'; reindeer = ren geyiği (Book 1) | Elinden gelse onu ren geyikleriyle birlikte ağıla kapatırdı |
| 247 | [740] | Ch8 | MT | patates yuvarlağına dönmüş ve skandala uğramış yüzünü | 'potato-round and scandalized' | patates gibi yuvarlak, dehşete düşmüş yüzünü |
| 248 | [744] | Ch8 | MT | karda konuşan yaşlı bir kadın | 'talking to snow' | karla konuşan yaşlı bir kadın |
| 249 | [744] | Ch8 | MT | — Diğer herkesi bu yola aklını çektirip delirttin, kendini de buralara kadar atıp bir sokağın ağzına dikildin. Neden? | garbled 'You've got all the others mooning up the lane' | — Ötekilerin hepsi o yola doğru hayran hayran bakıyor, sen ise buraya çekilmiş bir ara sokağın ağzına bakıyorsun. Neden? |
| 250 | [747] | Ch8 | TYPO | Blokun yarısına | spelling | Bloğun yarısına |
| 251 | [750] | Ch9 | EN | Briket, cam ve altın varakli harflerin her ikisinin de –hardware dükkânındaki Tom tarafından dükkânın cephesine tekrar kazandırılmasından üç gün sonra Greta, penceresine yeniden kavuştu. | garbled sentence with English 'hardware' and 'briket' (cinder block) for the brick | Tuğla olayından üç gün sonra Greta penceresine yeniden kavuştu; hem camına hem de altın harflerine. Hırdavat dükkânından Tom, HOLLY JOLLY BAKERY yazısını cephe boyunca yeniden eksiksiz yazmıştı. |
| 252 | [750] | Ch9 | MT | O briket olayından beri hamur yoğururken arka kapısını | brick = tuğla | Tuğla olayından beri fırın başındayken arka kapısını |
| 253 | [750] | Ch9 | MT | o günden beri çıkardığı her parti zencefilli kurabiye kusursuzdu | 'every batch since had come out sweet' (not only gingersnaps) | o günden beri çıkardığı her parti ekşimeden, tatlı çıkmıştı |
| 254 | [752] | Ch9 | MT | Resmî bir eyalet paltosu, | 'County coat' — county = ilçe, not state (eyalet) | Bir ilçe memurunun paltosu, |
| 255 | [756] | Ch9 | REG | — Buldun. — | Greta to a stranger → siz | — Buldunuz. — |
| 256 | [758] | Ch9 | MT | Eyalet sağlık denetlemesi. | 'County health' — county, not state | İlçe sağlık müdürlüğü. |
| 257 | [760] | Ch9 | TYPO | bömülmüştü | typo | gömülmüştü |
| 258 | [770] | Ch9 | MT | çünkü kurallar, işini hisleriyle yapması ile yapmaması arasındaki tek engeldi | 'the book was the only thing standing between him and doing it by feeling' | çünkü kitap, onunla işi duygularına göre yapmak arasındaki tek engeldi |
| 259 | [770] | Ch9 | TERM | Soğuk hava deposuna bir derece soktu | 'cold-case' = refrigerated case (MT used Pete's locker word) | Soğutmalı vitrinine bir termometre soktu |
| 260 | [776] | Ch9 | MT | hepsini yazdı | 'He said all of it' | hepsini söyledi |
| 261 | [778] | Ch9 | TERM | Ve su standart derecenin iki derece altında akıyor. | clue figure 'two degrees under code' — fixed wording, identical at every echo | Ve bu, yönetmeliğin iki derece altında akıyor. |
| 262 | [780] | Ch9 | NM | Yeni İngiltere’deki | New England (as Ch10) | New England’daki |
| 263 | [782] | Ch9 | TERM | Lavabo parçaları gelmezse belki daha uzun. | echoed line; wording fixed | Lavabonun parçaları gelmezse belki daha uzun. |
| 264 | [784] | Ch9 | MT | Mevsimin daha başında beni kapatıyorsunuz. | 'You're closing me a week into the season' | Sezonun içinde beni bir haftalığına kapatıyorsunuz. |
| 265 | [786] | Ch9 | MT | eyalet mührü | county seal | ilçe mührü |
| 266 | [790] | Ch9 | TYPO | yaşlı bir kadınınylesine | typo | yaşlı bir kadının öylesine |
| 267 | [791] | Ch9 | REG | Yalnız sana şunu söyleyeceğim | Varney (stranger) → siz | Yalnız size şunu söyleyeceğim |
| 268 | [791] | Ch9 | EN | faslına ve bölümüne kadar bana cite etti. | English 'cite' left in | faslına ve bölümüne kadar tek tek sıraladı. |
| 269 | [791] | Ch9 | TERM | fugayı | grout = derz (as in his list) | derzi |
| 270 | [791] | Ch9 | TERM | Soğuk hava deposuna sanki özel bir ismi varmış gibi 'soğuk oda,' el lavabosuna da 'Hobart lavabosu' dedi. | CLUE: walk-in = soğutucu (kept distinct from Joyce's 'soğuk oda' and from Pete's soğuk hava deposu) | Soğutucuya, sanki özel bir adıymış gibi "soğuk oda", el lavabosuna da "Hobart lavabosu" demiş. |
| 271 | [791] | Ch9 | MT | yüz yıllık bir binanın | 'an old building' | eski bir binanın |
| 272 | [793] | Ch9 | TYPO | omuzunun | spelling | omzunun |
| 273 | [794] | Ch9 | R3 | KİRLİ yazan ve bildiği tek kelime KİRLİ olduğu için | graffiti word = PİS | PİS yazan ve bildiği tek kelime PİS olduğu için |
| 274 | [794] | Ch9 | TYPO | Bu, ekmeği pişen kişinin bilgisiydi. | 'pişen' → 'pişiren' (someone who baked it) | Bu, ekmeği pişiren kişinin bilgisiydi. |
| 275 | [795] | Ch9 | MT | Kadın çemberindekilerin | 'the women of the circle' | Çemberdeki kadınların |
| 276 | [795] | Ch9 | MT | ekşi mayanın | 'the sour flour' | ekşi unun |
| 277 | [795] | Ch9 | TYPO | silüetin | spelling | siluetin |
| 278 | [798] | Ch9 | TERM | yardım fıçısı için | barrel = varil (as Ch3) | yardım varili için |
| 279 | [798] | Ch9 | TERM | doldurması gereken bir fıçısı | barrel = varil | doldurması gereken bir varili |
| 280 | [800] | Ch9 | MT | Başsağlığı diler. | 'In sympathy' — 'başsağlığı' is condolence for a death | Geçmiş olsun dileğiyle. |
| 281 | [802] | Ch9 | DLG | Hiçbir şey gelmeyince, — Tamam. İyi akşamlar, dedi ve kendi kendine dışarı çıktı. | speech turn rebuilt | Hiçbir şey gelmedi. — Tamam. İyi akşamlar, dedi ve kendi kendine çıkıp gitti. |
| 282 | [806] | Ch9 | DLG | Hal, çörek kutusunu fıçı için aldı. Sessizce, en yakınında durana, — Bu iltçe genelinde bundan daha temiz bir mutfak yoktur, dedi. | attribution rebuilt; typo 'iltçe'; barrel term | Hal, çörek kutusunu varil için aldı. — Bu ilçede bundan daha temiz bir mutfak yoktur, dedi sessizce, en yakınında kim duruyorsa ona. |
| 283 | [807] | Ch9 | DLG | alçak sesle, — Şey, durduk yere kapatmazlar adamı, değil mi? dedi; diğeri de, Yok, sanmam, kapatmazlar herhalde, diye karşılık verdi. | overheard speech inside narration → quotation marks (dossier) | alçak sesle "Eh, durduk yere kapatmazlar, değil mi?" dedi; öteki de "Yok, herhalde kapatmazlar," diye karşılık verdi. |
| 284 | [810] | Ch10 | MT | sıvı yağın fiyatı üzerine | 'the price of oil' = heating oil | yakıt fiyatları üzerine |
| 285 | [810] | Ch10 | DLG | Diğeri, — Şey, bu yıl işleri çok geride kaldı ve çaresiz insanlar çaresiz şeyler yapar, dedi. İlki, Ben bir şey demiyorum, diye karşılık verdi. | overheard speech inside narration → quotation marks; 'so far behind' (on payments) | Diğeri "Eh, bu yıl borçları çok birikti, çaresiz insanlar da çaresiz şeyler yapar," dedi. İlki "Ben bir şey demiyorum," diye karşılık verdi. |
| 286 | [810] | Ch10 | TERM | Akşamüstü fıçı için | barrel = varil | Akşamüstü varil için |
| 287 | [812] | Ch10 | TERM | kapının yanındaki fıçıyı | barrel = varil | kapının yanındaki varili |
| 288 | [813] | Ch10 | DLG | Alçak sesle unumu bırakarak, — Bunu duydun, dedim. | attribution rebuilt | — Bunu duydun, dedim alçak sesle, unumu bırakırken. |
| 289 | [814] | Ch10 | MT | Hal hayatı hiçbir konuda asla rol yapmamıştı. | 'had never in his life pretended otherwise about anything' | Hal hayatında hiçbir konuda başka türlüymüş gibi davranmamıştı. |
| 290 | [814] | Ch10 | MT | Marc Doucette eylül ayında Miller's Creek'teki kereste fabrikasından çıkarıldı. Sandalye ayakları ve tahta çiviler üreten torna fabrikasından. | 'the plant… the turning plant' (MT 'lumber mill' then 'turning plant') | Marc Doucette eylül ayında fabrikadan çıkarıldı. Miller's Creek'teki torna fabrikasından; sandalye ayağı ve dübel üreten. |
| 291 | [814] | Ch10 | MT | yakacağı azalmış bir aile | 'a family behind on its heat' | yakıt borcu birikmiş bir aile |
| 292 | [816] | Ch10 | MT | — Sessiz. — | 'Quiet.' = quietly | — Sessizce. — |
| 293 | [816] | Ch10 | TERM | Fıçının bütün esprisi | barrel = varil | Varilin bütün esprisi |
| 294 | [816] | Ch10 | MT | o mahalleye haftada bir koli | 'that end of town' | kasabanın o ucuna haftada bir koli |
| 295 | [816] | Ch10 | MT | Bizimkilere kapısı kapalı olan evlere girebiliyorsun. | 'houses that stay shut to the rest of us' | Bize kapalı kalan evlere sen girebilirsin. |
| 296 | [817] | Ch10 | MT | bir demet çayla | 'a twist of tea' | bir külah çayla |
| 297 | [817] | Ch10 | TERM | fıçının içine herkes için koymadığı | barrel = varil | varile herkes için koymadığı |
| 298 | [821] | Ch10 | DLG | Kapının önünde, — Uslu dur, dedim ona. Bunlar | attribution rebuilt | — Uslu dur, dedim ona bahçe kapısında. Bunlar |
| 299 | [822] | Ch10 | TYPO | on yaşlarında kadar bir kız | typo | on yaşlarında bir kız |
| 300 | [823] | Ch10 | REG | onu kollarım alarak bana bir iyilik yapmış olursunuz | to a child → sen; typo 'kollarım' | onu kollarımdan alarak bana bir iyilik yapmış olursun |
| 301 | [827] | Ch10 | DLG | Çaylar doldurulduktan ve elinde bir kitapla Pip'e özlem dolu bir bakış fırlatarak diğer odaya çekilen kız da bardağını alıp gittikten sonra, — Marc dışarıda iş arıyor, dedi. Pip, bu evi kendine mesken tutmaya karar vermiş bir canavar edasıyla sobanın yanına yerleşmişti. | attribution rebuilt; 'canavar' (monster) → creature | — Marc iş aramaya çıktı, dedi, çaylar doldurulup kız da bardağıyla kitabını alarak diğer odaya çekildikten sonra; kız giderken Pip'e özlem dolu bir bakış atmıştı. Pip ise bu evin işini göreceğine karar vermiş bir yaratık edasıyla sobanın yanına yerleşmişti. |
| 302 | [827] | Ch10 | TYPO | Noelden sonra Bridgton taraflarında | apostrophe | Noel'den sonra Bridgton taraflarında |
| 303 | [827] | Ch10 | TYPO | Ama o Noelden sonra. | apostrophe | Ama o Noel'den sonra. |
| 304 | [827] | Ch10 | TYPO | darda olmak... — | ellipsis = single character … (dossier) | darda olmak… — |
| 305 | [828] | Ch10 | MT | Onda olanın üç katına sahip olup | 'three times what you have' | Sizdekinin üç katına sahip olup |
| 306 | [829] | Ch10 | DLG | Ciddi olup olmadığını anlamak için bana | « » dialogue converted by hand (interrupted speech); 'whether I meant it' | Ciddi olup olmadığımı anlamak için bana |
| 307 | [829] | Ch10 | DLG | tutan elleri gevşedi. Alçak sesle, «Benim için | « » dialogue converted by hand (interrupted speech); 'whether I meant it' | tutan elleri gevşedi. — Benim için önemli, |
| 308 | [829] | Ch10 | DLG | elleri gevşedi. Alçak sesle, «Benim için önemli,» dedi. | « » dialogue converted by hand (interrupted speech); 'whether I meant it' | elleri gevşedi. — Benim için önemli, dedi |
| 309 | [829] | Ch10 | DLG | sesle, «Benim için önemli,» dedi. «Temiz olması. | « » dialogue converted by hand (interrupted speech); 'whether I meant it' | — Benim için önemli, dedi alçak sesle. |
| 310 | [829] | Ch10 | DLG | «Benim için önemli,» dedi. «Temiz olması. Hakkımızda | « » dialogue converted by hand (interrupted speech); 'whether I meant it' | Benim için önemli, dedi alçak sesle. Temiz |
| 311 | [829] | Ch10 | DLG | için önemli,» dedi. «Temiz olması. Hakkımızda ne | « » dialogue converted by hand (interrupted speech); 'whether I meant it' | için önemli, dedi alçak sesle. Temiz olması. Hakkımızda ne |
| 312 | [829] | Ch10 | DLG | Hakkımızda ne söylerlerse söylesinler» —ve daha kendini | « » dialogue converted by hand (interrupted speech); 'whether I meant it' | Hakkımızda ne söylerlerse söylesinler — ve daha |
| 313 | [829] | Ch10 | DLG | ne söylerlerse söylesinler» —ve daha kendini durduramadan, | « » dialogue converted by hand (interrupted speech); 'whether I meant it' | ne söylerlerse söylesinler — ve daha kendini durduramadan, |
| 314 | [829] | Ch10 | DLG | alan o şey dökülüverdi— «ne söylüyorlarsa söylesinler, | « » dialogue converted by hand (interrupted speech); 'whether I meant it' | alan o şey dökülüverdi — ne söylüyorlarsa |
| 315 | [829] | Ch10 | DLG | o şey dökülüverdi— «ne söylüyorlarsa söylesinler, buraya | « » dialogue converted by hand (interrupted speech); 'whether I meant it' | o şey dökülüverdi — ne söylüyorlarsa söylesinler, buraya |
| 316 | [829] | Ch10 | DLG | herhangi biri girip bizim onların sandığı gibi | « » dialogue converted by hand (interrupted speech); 'whether I meant it' | herhangi biri girip onların sandığı gibi |
| 317 | [829] | Ch10 | DLG | sandığı gibi olmadığımızı görebilir.» | « » dialogue converted by hand (interrupted speech); 'whether I meant it' | sandığı gibi olmadığımızı görebilir. |
| 318 | [831] | Ch10 | MT | yokuşta yakacak yağı gecikmiş bir aile | 'behind on its oil' | yokuşta yakıt borcu birikmiş bir aile |
| 319 | [831] | Ch10 | MT | insanlar aritmetikten anlar, en iyileri bile | 'people have got arithmetic in them' | insanların içinde hesap kitap vardır, en iyilerinin bile |
| 320 | [831] | Ch10 | MT | Bir şeye bağırarak hiçbir şeyi temizleyemezsin. | 'You don't clear a thing by shouting at it' | Bağırarak kimse aklanmaz. |
| 321 | [833] | Ch10 | MT | sabahtan kendine nefret de duyabilir | 'hate himself by morning' | sabaha kendinden nefret edebilir |
| 322 | [834] | Ch10 | MT | Un oradaydı. | 'Under it sat the flour' | Onun altında un vardı. |
| 323 | [834] | Ch10 | MT | Her ne yaptıysa bunu bilerek yapmıştı: | 'Whatever did that had taken knowing' | Bunu her ne yaptıysa, bilgi gerektirmişti: |
| 324 | [834] | Ch10 | TERM | kilitli bir kapının arkasındaki bir kutuya | flour bin = bidon | kilitli bir kapının arkasındaki bir bidona |
| 325 | [838] | Ch10 | MT | Yabancı sayılmayacak bir adam | 'A man I knew slightly' | Şöyle böyle tanıdığım bir adam |
| 326 | [838] | Ch10 | TERM | fıçının başında | barrel = varil | varilin başında |
| 327 | [838] | Ch10 | TERM | Hal, fıçıyı | barrel = varil | Hal, varili |
| 328 | [839] | Ch10 | DLG | Ona, — Onlar iyi insanlar, dedim. Doucette'ler. Haklarında fısıldayan caddedeki insanların yarısından daha temiz ev sahipleri. | attribution rebuilt; 'better housekeepers' | — Onlar iyi insanlar, dedim ona. Doucette'ler. Evlerini, haklarında fısıldayan caddenin yarısından daha iyi çekip çeviriyorlar. |
| 329 | [841] | Ch10 | TERM | arkalarında fıçının içine | barrel = varil | arkalarında varilin içine |
| 330 | [841] | Ch10 | MT | Açlık olsa saldırırdı. | 'Hunger would have grabbed' | Açlık kapar geçerdi. |
| 331 | [843] | Ch10 | TERM | un kutusuna | flour bin | un bidonuna |
| 332 | [844] | Ch10 | DLG | Hal, — Bu oldukça dar bir çember, dedi. Hepsine birden sahip olan insanlar açısından. | attribution rebuilt | — Bu oldukça dar bir çember, dedi Hal. Üçüne birden sahip olanlar açısından. |
| 333 | [845] | Ch10 | TERM | fıçının arasında | barrel = varil | varilin arasında |
| 334 | [845] | Ch10 | MT | Ama ben ayakta dururken etrafımdaki çember daralmıştı. Konserve kutusu taşıyan bir çocuk değil. | 'the field had narrowed'; 'a boy with a can' (spray can) | Ama ben orada dururken şüpheliler alanı ayaklarımın altında daralmıştı. Boya kutulu bir oğlan değil. |
| 335 | [850] | Ch11 | MT | çünkü güvendiğim bir sezginin yaklaşmamı söyleyeceği şeyleri saklayacak kadar uzun yaşayıştım. | 'keep what a nose I trusted would not go near' (Pip's nose); typo | çünkü güvendiğim bir burnun yanına yaklaşmadığı şeyi saklayacak kadar uzun yaşamıştım. |
| 336 | [852] | Ch11 | TYPO | Greta'yı değil. | case | Greta değil. |
| 337 | [852] | Ch11 | TYPO | İlçesi de değil; | case | İlçe de değil; |
| 338 | [852] | Ch11 | NM | Doc Mitchell'ın muayenehanesinde | Doc = Doktor (Book 1) | Doktor Mitchell'ın muayenehanesinde |
| 339 | [853] | Ch11 | MT | Doc Mitchell kasabanın hayvan doktoruydu ki burası gibi bir yerde bu durum onu aynı zamanda kasabanın eczacısı da yapıyordu. | 'the town's chemist' (does the chemistry), not pharmacist; Doc = Doktor | Doktor Mitchell kasabanın hayvan doktoruydu ki burası gibi bir yerde bu durum onu aynı zamanda kasabanın kimyageri de yapıyordu. |
| 340 | [854] | Ch11 | DLG | Ceketimi daha çıkarmadan, — Greta'nın başı belada, dedi. | attribution rebuilt; 'Greta's trouble' | — Greta'nın derdi, dedi ben daha paltomu çıkarmadan. |
| 341 | [855] | Ch11 | MT | — Greta'nın başı belada. Bir kavanozun içinde. | echo of 'Greta's trouble' | — Greta'nın derdi. Bir kavanozun içinde. |
| 342 | [855] | Ch11 | REG | Bunun bozulma olduğunu söyle, Doc. Nemli bir deponun ve sıcak bir haftanın unu bu hale getirdiğini söyle de | Doc formal (ruling 2; MT mixed sen/siz in one scene); Doc = Doktor | Bunun bozulma olduğunu söyleyin, Doktor. Nemli bir deponun ve sıcak bir haftanın unu bu hâle getirdiğini söyleyin de |
| 343 | [858] | Ch11 | MT | bir bardak suya karıştırıp | 'a saucer of water' | bir fincan tabağındaki suya karıştırıp |
| 344 | [860] | Ch11 | REG | Eğer umudun buysa, bozulmuş değil. | Doc formal | Eğer umudunuz buysa, bozulmuş değil. |
| 345 | [860] | Ch11 | MT | Küf sana küflü bir koku ve cam altında pamuksu bir tabaka verir, burada ise hiçbiri yok. | 'a musty note and a fur under the glass' | Küf, rutubet kokusu ve cam altında tüylü bir tabaka bırakır; burada ikisi de yok. |
| 346 | [861] | Ch11 | TYPO | ki memnuniyetle... | ellipsis = single character … (dossier) | ki memnuniyetle… |
| 347 | [862] | Ch11 | TERM | kuru bir ambarda | 'dry in a bin' | kuru bir bidonda |
| 348 | [862] | Ch11 | MT | Dört temiz parti ve yeni bir maya çuvalı ile | 'a new bag of yeast' | Dört temiz parti ve yeni bir paket mayayla |
| 349 | [864] | Ch11 | MT | maya kullanmadan ekşi bir tat vermek için | 'without the starter' = sourdough starter | ekşi maya kullanmadan ekşi bir tat vermek için |
| 350 | [864] | Ch11 | UNIT | Yüz libre unu bilerek mahvetmek için kullanacağınız doz bu. Herhangi bir ekmek fırıncısının asla koymayacağı kadar, on katı. | 100 lb → 45 kg (accurate, per Lisa's 2026-08-11 ruling; logged); 'ten times' clue wording fixed | Kırk beş kilo unu bilerek mahvetmek için kullanacağınız doz bu. Hiçbir ekmek fırıncısının koymayacağı miktarın on katı. |
| 351 | [866] | Ch11 | TERM | — Sana bir zihni anlatamam, Jessica. İyi bir un çuvalının, Tanrı'nın veya havanın yarattığı herhangi bir tesadüfle, on katı dozda bir ekmek fırınının ekşi bazını bir gecede kendi kendine üretmeyeceğini söyleyebilirim. | Doc formal; 'a bin of good flour'; sour base = ekşitici baz (one term) | — Size kimsenin niyetini söyleyemem, Jessica. Ama iyi undan oluşan bir bidonun, Tanrı'nın ya da havanın yarattığı hiçbir tesadüfle, bir ekmek fırınının ekşitici bazını on katı dozda bir gecede kendi kendine üretmeyeceğini söyleyebilirim. |
| 352 | [869] | Ch11 | NM | alınmış bir toz. Doc'un merdiveninde durup Frosty'nin | Doc = Doktor (Book 1) | alınmış bir toz. Doktor'un merdiveninde durup Frosty'nin |
| 353 | [870] | Ch11 | TERM | Bir bakkal rafından çuvalla ekşi baz satın alamazdınız. | sour base = ekşitici baz | Bir bakkal rafından çuvalla ekşitici baz satın alamazdınız. |
| 354 | [870] | Ch11 | MT | taze bir maya çuvalıyla | 'a fresh bag of yeast' | taze bir paket mayayla |
| 355 | [870] | Ch11 | MT | el lavabosu kodunu ezbere bilen elle | 'the hand-sink code' | el lavabosu yönetmeliğini ezbere bilen elle |
| 356 | [870] | Ch11 | TYPO | fazla olsa ham un çuval açıldığı an | grammar | fazla olsa ham un, çuval açıldığı an |
| 357 | [871] | Ch11 | TERM | bu bulvarda | avenue = cadde | bu caddede |
| 358 | [871] | Ch11 | NM | yakıştırmadım. Yine de Doc'un merdiveninde dururken sorunun | Doc = Doktor (Book 1) | yakıştırmadım. Yine de Doktor'un merdiveninde dururken sorunun |
| 359 | [873] | Ch11 | MT | elini omzuma koydu | 'put its hand on my sleeve' | elini koluma koydu |
| 360 | [876] | Ch11 | MT | ve imlası yoktu | 'it couldn't spell' (as Ch8) | ve heceleyemezdi |
| 361 | [877] | Ch11 | TERM | o un çuvalından benden önce geri çekilen botumun dibindeki pengüene | flour bin; typo 'pengüen' | o un bidonundan benden önce geri çekilen, botumun dibindeki penguene |
| 362 | [879] | Ch11 | MT | diğer tüm hemşerilerinden uzağa | 'its fellows' | diğer tüm arkadaşlarından uzağa |
| 363 | [883] | Ch12 | TYPO | Ona kimin nefret ettiği değil. | case | Ondan kimin nefret ettiği değil. |
| 364 | [887] | Ch12 | MT | Pete’in kızartmam üzerine söylenip durduğu | 'had grumbled about over my roast' | Pete’in rostomu bağlarken söylenip durduğu |
| 365 | [887] | Ch12 | TERM | minibüsünü rıhtıma yanaştırır | loading dock = rampa (not a quay) | minibüsünü rampaya yanaştırır |
| 366 | [887] | Ch12 | TERM | Greta da sabah boyunca ihtiyacı oldukça bunları arka duvarındaki saklama kutularına taşırırdı. Un, o dokunulmasa da Holly Jolly’nin hiçbir müşterinin görmediği, hiçbir sokak lambasının erişmediği o tek odasında, arabayla kutu arasında, o kendisini kaldırana kadar öylece dururdu. | flour bin = bidon; garbled clause; typo 'taşırırdı' | Greta da sabah boyunca ihtiyacı oldukça bunları arka duvarındaki bidonlara taşırdı. Un, arabayla bidon arasında, Holly Jolly’nin hiçbir müşterinin görmediği, hiçbir sokak lambasının erişmediği o tek odasında, Greta onu kaldırana kadar öylece dururdu. |
| 367 | [889] | Ch12 | MT | Ve o tuğla örülene dek, | 'until the brick' = until the brick through the window (MT 'until bricked up') | Ve tuğla olayına kadar, |
| 368 | [891] | Ch12 | TYPO | dörütte | typo | dörtte |
| 369 | [891] | Ch12 | MT | Ne var ki tuğla örülene dek bu, | 'until the brick' | Ne var ki tuğla olayına kadar bu, |
| 370 | [891] | Ch12 | TERM | bir un kutusu | flour bin | bir un bidonu |
| 371 | [893] | Ch12 | MT | Zehrinizi dökerdiniz. Kendi küreğiyle iyice karıştırırdınız. | NO-POISON edition: 'Tip your powder' (MT 'your poison'); 'her scoop' | Tozunuzu dökerdiniz. Onun kepçesiyle iyice karıştırırdınız. |
| 372 | [893] | Ch12 | MT | İlaçlanmış unu kutularına | 'the doctored flour' (not 'medicated'); bin | İçine bir şey katılmış unu bidonlarına |
| 373 | [895] | Ch12 | MT | Bardağı masaya bıraktım. | 'the cup' | Fincanı masaya bıraktım. |
| 374 | [901] | Ch12 | TERM | İşte rıhtımı paylaşan o iki kapı. | dock = rampa | İşte rampayı paylaşan o iki kapı. |
| 375 | [905] | Ch12 | MT | Tuğla örülene dek her karanlık sabahın yarısında | 'until the brick' | Tuğla olayına kadar her karanlık sabahın yarısında |
| 376 | [907] | Ch12 | MT | — Demek, dedim alçak sesle, Pip’e bakarak. | 'I said, low, to Pip' | — Demek öyle, dedim alçak sesle Pip’e. |
| 377 | [907] | Ch12 | MT | Tuğla örülene dek her karanlık sabah | 'until the brick' | Tuğla olayına kadar her karanlık sabah |
| 378 | [915] | Ch12 | TERM | o çamurlu rıhtım boyunca | dock = rampa | o çamurlu rampa boyunca |
| 379 | [917] | Ch12 | TERM | Pete Garcia rıhtıma sahipti | dock = rampa | Rampa Pete Garcia’nındı |
| 380 | [917] | Ch12 | MT | Tom’un halkasından | 'off Tom's rack' | Tom’un rafından |
| 381 | [917] | Ch12 | TERM | Tam da bu rıhtım yüzünden içten içe | dock = rampa | Tam da bu rampa yüzünden içten içe |
| 382 | [921] | Ch12 | MT | Unun ilaçlandığını bilmeden evvel | 'the flour was doctored' | Una bir şey katıldığını bilmeden evvel |
| 383 | [929] | Ch12 | NM | doktorun tezgâhından | Doc | Doktor’un tezgâhından |
| 384 | [935] | Ch12 | MT | sürülmüş beyaz patika | 'churned white slot' | çiğnenmiş beyaz patika |
| 385 | [937] | Ch12 | MT | Rıhtımın soğuk boğazına, tuğla örülene dek | dock = rampa; 'until the brick' | Rampanın soğuk boğazına, tuğla olayına kadar |
| 386 | [937] | Ch12 | MT | Erişim ise bir adamın önünden yürütüp geçirmesi çok daha zor bir şey. | 'Access is a harder thing to walk a man past' | Erişim ise bir adamı aklayıp geçmek için çok daha zor bir engel. |
| 387 | [941] | Ch12 | R5 | Blok boyunca aşağıda, Holly Jolly’nin önündeki kaldırımda üzerinde <bt>Wendt's Bakehouse, Bridgton</bt> yazan | stray <bt> around a business name removed (ruling 5) | Bloğun aşağı ucunda, Holly Jolly’nin önündeki kaldırımda yan tarafında Wendt's Bakehouse, Bridgton yazan |
| 388 | [949] | Ch12 | MT | geçen hafta tezgahın üzerinden kendisine tek bir kelime edilmiş bir kadın için | 'a woman who'd given her one word across the counter' | geçen hafta tezgâhın üzerinden ona tek bir kelime etmiş bir kadın için |
| 389 | [951] | Ch12 | MT | caddenin karşısında onun peşinden yola koyuldu | 'set off down the sidewalk after it' | kaldırımdan aşağı onun peşine düştü |
| 390 | [954] | Ch13 | MT | Haritanın soğuk ucunda Pete'in adının yazdığı o kâğıtla gecenin | 'the map with Pete's name at the cold end of it' (no paper) | Haritanın soğuk ucunda Pete'in adıyla gecenin |
| 391 | [954] | Ch13 | TYPO | Pip da bel çukurumda | vowel harmony | Pip de bel çukurumda |
| 392 | [954] | Ch13 | MT | sokakta sormaya cesaret edemediğim soruyu | 'what I had refused to ask in the alley' | ara sokakta sormayı reddettiğim soruyu |
| 393 | [954] | Ch13 | MT | O pervazda dikilenin | 'that sill' | O eşikte dikilenin |
| 394 | [954] | Ch13 | MT | Onu neredeyse idama mahkûm eden kasaba dedikoducuları | 'who had all but tried him' | Onu neredeyse yargılamış olan kasaba dedikoducuları |
| 395 | [958] | Ch13 | DLG | Pip uykusunda olduğundan derdimi anlatamadığım çaydanlığa, — Şu husumeti bir düşün bakalım, dedim. Pete, ben biftek almaya gittiğim o gün, | not speech in the English (no quotes) — dash removed; 'roast' | Şu husumeti bir düşün, dedim çaydanlığa, çünkü Pip söz dinleyecek hâlde olmayacak kadar uykudaydı. Pete, ben rosto almaya gittiğim o gün, |
| 396 | [958] | Ch13 | MT | O zehirli tozu döken her kimse | NO-POISON edition: 'whoever poured that powder' (MT 'that poisonous powder') | O tozu döken her kimse |
| 397 | [960] | Ch13 | TERM | ekşitilmiş bir mayayı veya bir tutam tebeşir tozunu, benim bir danayı nasıl parçalayacağımı bilmediğimden daha iyi ayırt edemezdi | sour base = ekşitici baz (MT 'a soured yeast') | ekşitici bazı bir tutam tebeşir tozundan ayırt etmeyi, benim bir danayı parçalamayı bildiğimden daha iyi bilmezdi |
| 398 | [972] | Ch13 | REG | — Seni işinden alıkoymayacağım, dedim. Buraya seni suçladığımı söylemeye geldim. Greta'nın başına gelenler yüzünden. Sırf şafaktan önce o avluda bulunduğun ve senden başka orada bulunma hakkı kimsenin olmadığı açık gerçeğinden ötürü. | Pete formal; 'I had you down for it' = suspected, not accused | — Sizi işinizden alıkoymayacağım, dedim. Buraya sizden şüphelendiğimi söylemeye geldim. Greta'nın derdi yüzünden. Sırf şafaktan önce o avluda bulunduğunuz ve sizden başka kimsenin orada bulunmak için bir sebebi olmadığı açık gerçeğinden ötürü. |
| 399 | [972] | Ch13 | REG | — Ve seni akladığımı söylemeye geldim. Bunu her kim yaptıysa, karanlığa uygun bir öfkeye ve tozu kullanacak bir fırıncı ustalığına ihtiyaç duymuştu, sende ise ikisi de yok. Sen öğle vakti kavga edersin ve et kesersin. Bu sana uymuyor. | Pete formal; 'taken you back out' | — Ve sizi listeden çıkardığımı söylemeye geldim. Bunu her kim yaptıysa, karanlığa uygun bir mizaca ve tozu kullanacak bir fırıncı ustalığına ihtiyaç duymuştu, sizde ise ikisi de yok. Siz öğle vakti kavga edersiniz ve et kesersiniz. Bu size uymuyor. |
| 400 | [974] | Ch13 | REG | — Bütün bu yolu yaşlı bir huysuza dil dökmek için tepmedin herhalde. | Pete formal | — Bütün bu yolu yaşlı bir huysuza dil dökmek için tepmediniz herhalde. |
| 401 | [976] | Ch13 | REG | — Sana güvendiğimi söylemeye geldim. Ki bunun bir ilk olduğunu tahmin ediyorum. | Pete formal; echoes his 'Which is a novelty' | — Size güvendiğimi söylemeye geldim. Bu da yeni bir şey sanırım. |
| 402 | [978] | Ch13 | REG | Bunun tam tersini söylemeye gelen tek kişisin. | Pete formal | Bunun tam tersini söylemeye gelen tek kişi sizsiniz. |
| 403 | [978] | Ch13 | REG | — Öyle mi? Pekâlâ. O halde bir pirzola alacaksın. | Pete formal; 'Yeah. Well.' | — Evet. Neyse. O hâlde bir pirzola alacaksınız. |
| 404 | [982] | Ch13 | DLG | İstemediğim pirzolayı paketlerken, — Sana bahsettiğim o siluet, dedi. Karanlıkta arka kapısının önünde olan hani. Şimdi bana inandığına göre, bunun hepsini bilmek isteyeceksin. | attribution rebuilt; Pete formal | — Size bahsettiğim o siluet, dedi, istemediğim pirzolayı paketlerken. Karanlıkta arka kapısının önündeki hani. Şimdi bana inandığınıza göre, hepsini bilmek istersiniz. |
| 405 | [982] | Ch13 | TERM | köy meydanının karşısındaki | the green = meydan | meydanın karşısındaki |
| 406 | [982] | Ch13 | MT | kaçışarak değil | 'not a scramble' | telaşla kaçarak değil |
| 407 | [982] | Ch13 | MT | çalışkan bir siluet | 'a working shape' | iş başındaki bir siluet |
| 408 | [982] | Ch13 | TERM | — Şu kamyonet de bir sabah yine oradaydı. | van = minibüs (as Ch7) | — O minibüs de bir sabah yine oradaydı. |
| 409 | [982] | Ch13 | TERM | bir kamyonetin gereğinden de yüksek | van = minibüs | bir minibüsün gereğinden de yüksek |
| 410 | [984] | Ch13 | MT | bol soluk renkli bir iş önlüğü giymiş | 'a loose pale working coat' | bol, soluk renkli bir iş ceketi giymiş |
| 411 | [986] | Ch13 | REG | — Ve peşine düştün, dedim. O sabahlar. Sadece görmekle kalmadın. | Pete formal | — Ve peşine düştünüz, dedim. O sabahlar. Sadece görmekle kalmadınız. |
| 412 | [988] | Ch13 | REG | Onu sevdiğimden değil, yanlış anlama. | Pete formal | Onu sevdiğimden değil, yanlış anlamayın. |
| 413 | [992] | Ch13 | REG | — Kavganızın elverdiğinden çok daha iyi bir komşusun, dedim. | Pete formal; 'than your quarrel lets on' | — Kavganızın belli ettiğinden çok daha iyi bir komşusunuz, dedim. |
| 414 | [994] | Ch13 | DLG | Yüzü kızararak, — Bunu söylediğini, dedi, kimseye söyleme. | attribution rebuilt; Pete formal | — Bunu söylediğinizi, dedi kızararak, kimseye söylemeyin. |
| 415 | [1000] | Ch13 | MT | ortalıkta iyi bir insan daha eksilmişken | 'the field gone narrower by one good man' | şüpheliler alanı iyi bir adam eksilerek daralmışken |
| 416 | [1007] | Ch14 | MT | yokuştan yukarı, | 'came up my path' | bahçe yolumdan yukarı, |
| 417 | [1017] | Ch14 | MT | annesi için bir kutu bayat kek verdim | 'a box of day-olds' | annesi için bir kutu dünden kalma ekmek verdim |
| 418 | [1017] | Ch14 | R3 | duvara KİRLİ yazdığını | graffiti word = PİS; 'my wall' | duvarıma PİS yazdığını |
| 419 | [1017] | Ch14 | MT | sabah kutularımı yamuldukları için dümdüz dizecek kadar titizlenen o çocukla | 'because he couldn't stand them crooked' | sabah kutularımı yamuk durmalarına dayanamadığı için dümdüz dizen o çocukla |
| 420 | [1021] | Ch14 | EN | Kırgınlığın kinə dönüştüğü. Onu sevdiğim için bunu fark edemeyen son kişi olacağım. | foreign letter 'ə' (Azerbaijani) in 'kinə'; 'I'd be the last to see it' | Kırgınlığın kine dönüştüğünü. Onu sevdiğim için bunu en son ben görürmüşüm. |
| 421 | [1037] | Ch14 | MT | mezarlık vardiyasına | calque of 'graveyard shift' | gece vardiyasına |
| 422 | [1037] | Ch14 | MT | bir ateş ölçer | 'a thermometer' | bir termometre |
| 423 | [1037] | Ch14 | MT | yanlış ayrıntıları da sıraladı: sıcaklık derecesi, öksürük şurubunun aroması; | 'all the wrong details'; 'cough drops' | üstelik hep yersiz ayrıntılar: ateşin kaç derece olduğu, öksürük pastillerinin aroması; |
| 424 | [1041] | Ch14 | TYPO | insanlara bunu anlatmaya | capital after full stop | İnsanlara bunu anlatmaya |
| 425 | [1041] | Ch14 | MT | Sanki dükkânların içinden gidip onun duvarına bunu yazacakmışım gibi. | 'of all the shops' | Sanki onca dükkân varken gidip onun duvarına bunu yazacakmışım gibi. |
| 426 | [1043] | Ch14 | MT | İnsan gece vakti duvara spreyle kelimeler yazıp, aynı zamanda eczacı terazisiyle un tartamazdı. | 'dose flour by the scoop to a chemist's measure' | İnsan gece vakti duvara spreyle kelimeler yazıp, aynı zamanda una kepçe kepçe, kimyager hassasiyetiyle doz katamazdı. |
| 427 | [1047] | Ch14 | TYPO | değilti | typo | değildi |
| 428 | [1049] | Ch14 | MT | Ben sadece gürültülü kısmın peşindeyim. | 'I've been chasing the loud part' | Ben gürültülü kısmın peşine düşmüşüm. |
| 429 | [1053] | Ch14 | MT | Üzerinde çok fazla düşünme. | 'Don't polish it' | Süsleyip püsleme. |
| 430 | [1059] | Ch14 | MT | Kapısına kadar ona eşlik ettim. | 'as far as his gate' | Bahçe kapısına kadar ona eşlik ettim. |
| 431 | [1059] | Ch14 | MT | merdivenin başındaki paspası | 'the boot scraper' | basamağın yanındaki çamur sıyırıcıyı |
| 432 | [1059] | Ch14 | REG | — Senin Danny'n o duvarı boyamadı Bayan Ott. | Mrs. Ott (acquaintance) → siz | — Sizin Danny'niz o duvarı boyamadı, Bayan Ott. |
| 433 | [1067] | Ch14 | MT | Bu yüzden tezgâhlar arka odada | 'the frames' (wreath frames) | Bu yüzden çelenk iskeletleri arka odada |
| 434 | [1067] | Ch14 | MT | yedi kadın bizler şişlerimizle | 'the seven of us' | yedimiz şişlerimizle |
| 435 | [1071] | Ch14 | MT | o kocaman kahkahasını atarak buna izin verdi. | sentence garbled | o kocaman kahkahasını attı ve izin verdi. |
| 436 | [1091] | Ch14 | UNIT | Milde milde atkı ören | 'by the mile' idiom → metric idiom (SAFE) | Metrelerce atkı ören |
| 437 | [1119] | Ch14 | TERM | iki çikolatalı-cevizli kek ve bir düzine çörek | Martha's order (repeated later): pies = turta | iki çikolatalı-cevizli turta ve bir düzine çörek |
| 438 | [1130] | Ch15 | MT | ceketinin düğmelerini ilklemiş bir hâlde | 'in his good coat' | en iyi ceketini giymiş hâlde |
| 439 | [1130] | Ch15 | MT | bütün bir hamuru kabul etti | 'a whole ham' (MT 'a whole dough') | bütün bir jambonu kabul etti |
| 440 | [1130] | Ch15 | TERM | salonu, Hal'in ve Dernek'in kampanyaları için iki | Society = Cemiyet | salonu, Hal'in ve Cemiyet'in kampanyaları için iki |
| 441 | [1138] | Ch15 | MT | katıksız yuvarlak ekmekler | 'seeded rounds' | çekirdekli yuvarlak ekmekler |
| 442 | [1140] | Ch15 | MT | — Bunlar bayat, dedi, sesler kesildiğinde. Domuz çiftçisinden başka kime versem üç kuruş anca kazanırdım. | 'day-olds'; 'pennies off the pig farmer' | — Bunlar dünden kalma, dedi, sesler kesildiğinde. Domuz çiftliğine versem ancak üç kuruş alırdım. |
| 443 | [1142] | Ch15 | MT | Sonra hamur ve tenekeler gibi | 'the same as the ham' | Sonra jambon ve tenekeler gibi |
| 444 | [1156] | Ch15 | MT | dibinde ekim ayından kalma birkaç erken dönem sunusuyla birlikte ekim ayından beri | duplicated 'since October' | dibinde birkaç erken sunuyla ekim ayından beri |
| 445 | [1156] | Ch15 | TERM | için yeni değildi. Dernek'in sedir ağacından yapılma | Society = Cemiyet | için yeni değildi. Cemiyet'in sedir ağacından yapılma |
| 446 | [1160] | Ch15 | OM | mühürlü bir şekilde olduğu yerde kaldı. | sentence 'Everyone had drawn a clean line in their minds between the two…' dropped | mühürlü bir şekilde olduğu yerde kaldı. Kimsenin yüksek sesle söylemesine gerek kalmadan herkes ikisinin arasına zihninde net bir çizgi çekmişti. |
| 447 | [1160] | Ch15 | TERM | vakti gelene kadar Dernek'in ön odasında, kartının | Society = Cemiyet | vakti gelene kadar Cemiyet'in ön odasında, kartının |
| 448 | [1164] | Ch15 | TERM | pek inanamayarak. — Dernek. Kimse tek bir | Society = Cemiyet | pek inanamayarak. — Cemiyet. Kimse tek bir |
| 449 | [1166] | Ch15 | MT | Nick'in taş ocağından örülmüş şöminesinden | 'Nick's fieldstone hearth' | Nick'in tarla taşından örülmüş ocağından |
| 450 | [1170] | Ch15 | OM | Saban programları ve kilise yemekleri duyurularının arasında, Grange'ın ilan tahtasında askıdaydı; | 'plow schedules' (snow plow); 'glossy and pale gray' dropped | Kar küreme programları ve kilise yemekleri duyurularının arasında, Grange'ın ilan tahtasında asılıydı; parlak, soluk gri bir kâğıt, |
| 451 | [1178] | Ch15 | MT | unlu çöreklerin arasına | 'among the cocoa buns' | kakaolu çöreklerin arasına |
| 452 | [1178] | Ch15 | TERM | Lavabonun parçaları gelmezse belki daha fazla. | Varney's line quoted back — identical to Ch9 | Lavabonun parçaları gelmezse belki daha uzun. |
| 453 | [1178] | Ch15 | MT | Noellerin o en hareketli günlerinde | 'in the whole bright run to Christmas' | Noel'e uzanan o parlak dönemin tamamında |
| 454 | [1182] | Ch15 | TYPO | yılndaki | typo | yılındaki |
| 455 | [1190] | Ch15 | TERM | finansiyerin ne olduğunu | financier spelled as elsewhere | financier’nin ne olduğunu |
| 456 | [1194] | Ch15 | MT | İçimdeki her şey o salondan karşıya geçip broşürü havaya kaldırmalarını ve o haftayı yüzlerine vurup açıklamalarını istemiyordu. | REVERSED: 'Everything in me wanted to cross that hall…' (MT 'did not want') | İçimdeki her şey salonu geçip broşürü havaya kaldırmak ve ondan o haftayı herkesin yüzüne karşı açıklamasını istemek istiyordu. |
| 457 | [1198] | Ch15 | REG | işlerin üstesinden nasıl geliyorsun? | a farmer's wife to Renée (stranger) → siz | işlerin üstesinden nasıl geliyorsunuz? |
| 458 | [1202] | Ch15 | MT | Ama tatil dönemindeki sayılara ulaştığınızda | 'at holiday numbers' ('tatil' = vacation) | Ama yılbaşı yoğunluğunda |
| 459 | [1202] | Ch15 | MT | yoksa yirminci güne varana kadar bütün emekleriniz boşa gider. Bu yüzden insan bunu önceden hazırlar. | 'by the twentieth'; 'So one conditions it' | yoksa ayın yirmisine varmadan bütün düzeniniz çöker. Bu yüzden una iyileştirici katılır. |
| 460 | [1206] | Ch15 | NM | kahverengi şişeler arasındaki bankından Dr. Mitchell'ın sesi | Doc = Doktor; 'bench' (tezgâh, as Ch11) | kahverengi şişelerin arasındaki tezgâhından Doktor Mitchell'ın sesi |
| 461 | [1206] | Ch15 | MT | gıda varilinin etrafındaki kadın halkasına | 'a ring of women' (avoid the circle word) | gıda varilinin yanındaki bir grup kadına |
| 462 | [1208] | Ch15 | TERM | Greta'nın kutusundaki şeyin | flour bin | Greta'nın bidonundaki şeyin |
| 463 | [1208] | Ch15 | MT | sokaktaki tek eski tuğla yığını da dükkânının arkasındaki çöp konteynerinin arkasındaydı | 'the only heap of old brick on the block sat in the dumpster behind her shop' | bloktaki tek eski tuğla yığını da onun dükkânının arkasındaki çöp konteynerinin içindeydi |
| 464 | [1210] | Ch15 | TERM | Motif, ilk günden beri gözümün önündeydi; esmer tereyağı kokusuna bürünmüş, yazık kadına, bu aralar işlerinin bozulması ne kadar üzücü diyen bir kadının şahsında. O haftayı tahmin etmemişti. Bizzat kendisi örmüştü. | Renée's Ch3 line quoted back — wording now identical; 'motive'; 'She'd built it' | Sebep, ilk günden beri gözümün önündeydi; esmer tereyağı kokusuna bürünmüş, zavallı kadın, şu sıralar başına gelen dertler ne yazık diyen bir kadının şahsında. O haftayı tahmin etmemişti. O haftayı bizzat o kurmuştu. |
| 465 | [1220] | Ch15 | MT | Unla çalışırken ya da arka sokakta işleri yürütürken yavaş değildim. | 'Not slow to work the flour, or the alley' | Unu ya da ara sokağı çözmekte yavaş değildim. |
| 466 | [1220] | Ch15 | MT | Bütün hafta boyunca onu aklımda tutup durdum, bense | 'picked her up in my mind and set her down again' | Bütün hafta boyunca onu aklımda alıp alıp geri bırakmıştım; bu arada |
| 467 | [1231] | Ch16 | MT | bir tel çember ve bir planla | 'a hoop of wire' (avoid the circle word) | bir tel kasnak ve bir planla |
| 468 | [1233] | Ch16 | MT | kapısından sahte bir nota rastlamadan girmemi | 'without a false note' | altın kapısından hiçbir yapmacıklık sezdirmeden girmemi |
| 469 | [1233] | Ch16 | MT | Öyleyse ellerim balsamlardayken geldiğim diğer şeyi de yapardım. Onu yakından okumak. Büyünün neyin üzerine yapıldığını anlayacak kadar yakın olmak. Aynı şeyi balta kütüğü üzerindeki Pete ile de yapmıştım. | 'what the charm was laid over' = her charm, not magic; balsam = köknar | Öyleyse ellerim köknar dallarıyla meşgulken asıl geldiğim işi de yapardım. Onu yakından okumak. Cazibesinin neyin üzerine serildiğini görecek kadar yakın olmak. Aynısını Pete'le, kütüğünün başında da yapmıştım. |
| 470 | [1235] | Ch16 | TERM | kuş yok, sağlık kuralları | 'health code' (as Ch3) | kuş yok, sağlık yönetmeliği |
| 471 | [1239] | Ch16 | EN | — Mrs. Claus. — | English title 'Mrs.' | — Bayan Claus. — |
| 472 | [1239] | Ch16 | MT | Hâlimizi mazur görün, ancak yerleşebildik. | 'we're hardly settled' | Hâlimizi mazur görün, daha yerleşemedik bile. |
| 473 | [1239] | Ch16 | MT | — Süslemeye bakmaya geldiniz. Pencerede ticaretle daha güzel durmuyor mu? | 'You've come to see it dressed. Isn't it better with the trade in the window?' | — Donanmış hâlini görmeye geldiniz. Vitrin malla dolunca daha güzel değil mi? |
| 474 | [1241] | Ch16 | MT | Bloka bir hoş geldin. | 'A welcome to the block' | Bloğa hoş geldin hediyesi. |
| 475 | [1245] | Ch16 | TERM | — Balsam galiba, kır yeşili. | balsam = köknar | — Köknar galiba, kır yeşili. |
| 476 | [1245] | Ch16 | DLG | durmasını istiyorum. "Hep buradaymışım"ı düz ve kesin | narration after speech needs its dash | durmasını istiyorum. — "Hep buradaymışım" lafını düz ve kesin |
| 477 | [1251] | Ch16 | MT | tuttuğunuz bütün tatil takvimini. Bu kasabada Noel'de harcanacak, şimdiye kadar her zamankinden çok daha fazla tatlı ticareti var, çünkü harcayacak sadece bir tane eski fırını vardı. Köy fiyatlarıyla. Köy mallarıyla. "Bir tane eski fırını" dedi hoş bir şekilde, çoktan geçmişte kalmış bir şeyi adlandırarak. | garbled sentence; 'holiday calendar'; narration after speech needs its dash | tuttuğunuz bütün yılbaşı takvimini. Bu kasabada Noel'de, şimdiye kadar harcayacak yer bulabildiğinden çok daha fazla tatlı parası var; çünkü harcayabileceği tek bir eski fırın oldu hep. Köy fiyatlarıyla. Köy mallarıyla. — "Tek bir eski fırın" lafını hoş bir edayla, çoktan geçmişte kalmış bir şeyi adlandırır gibi söyledi. |
| 478 | [1255] | Ch16 | MT | Aramızda kalmasın, şaşırmadım. O bina bir günlükse bile yüz yıllık, ve bir tanesinde ticari bir mutfak çalıştırıp kontluğun sonsuza dek görmezden gelmesini bekleyemezsiniz. Derz bozulur. Hava fitili bozulur. El yıkama lavabonuz | REVERSED 'Between us' (MT 'let it not stay between us'); 'county' (MT 'kontluk' = earldom); weather-strip = rüzgârlık (Ch9) | Aramızda kalsın, şaşırmadım. O bina en az yüz yaşında ve böyle bir binada ticari mutfak çalıştırıp ilçenin sonsuza dek görmezden gelmesini bekleyemezsiniz. Derz bozulur. Rüzgârlık bozulur. El lavabonuz |
| 479 | [1259] | Ch16 | TERM | Derz. Hava fitili. Eski bir borudan iki derece mahrum kalan el yıkama lavabosu. | clue: same three trade words as Varney's list; 'two degrees under code' identical wording | Derz. Rüzgârlık. Eski bir borudan beslenen, yönetmeliğin iki derece altında akan el lavabosu. |
| 480 | [1261] | Ch16 | MT | Geçici durum Greta'nınkisiydi, Varney'ninkiydi ve benimki. | 'The provisional was Greta's, and Varney's, and mine' | Geçici kapatmanın ayrıntılarını Greta, Varney ve ben biliyorduk. |
| 481 | [1265] | Ch16 | EN | aynı üç kusur vardır, Mrs. Claus. | English title 'Mrs.' | aynı üç kusur vardır, Bayan Claus. |
| 482 | [1267] | Ch16 | UNIT | bir şeye bir inç bile yaklaşmamıştım | 'not one inch nearer' idiom | bir şeye bir adım bile yaklaşmamıştım |
| 483 | [1271] | Ch16 | DLG | Hiç tereddüt etmeden söyledi. Arabanızın | resumed speech needs its dash | Hiç tereddüt etmeden söyledi. — Arabanızın |
| 484 | [1271] | Ch16 | MT | zarif ve dışarısıyla bağı kopuk, altından çivi sokabileceğim tek bir dikişi olmadan | 'gracious and airtight, without a seam I could get a nail under' | zarif ve kusursuz; altına tırnağımı sokabileceğim tek bir dikiş yeri bile yoktu |
| 485 | [1275] | Ch16 | MT | Bana itirafı vermişti ama onunla ilgili yapabileceğim hiçbir şey vermemişti | 'given me the recognition' — not a confession | Bana o farkına varışı vermişti ama onunla yapabileceğim hiçbir şey vermemişti |
| 486 | [1279] | Ch16 | TERM | — Balsam ve altın sarısı bir kurdele, | balsam = köknar; 'a gold bow' | — Köknar ve altın sarısı bir fiyonk, |
| 487 | [1279] | Ch16 | TERM | Sanki hep buradayım gibi. | her repeated phrase — identical to [1245] | Sanki hep buradaymışım gibi. |
| 488 | [1287] | Ch16 | MT | Greta'nın düşüşüne yarı yarıya fazla sevinmiş ve tam olarak şeklini çok iyi biliyordu. Büyünün altında, | 'Too glad of Greta's fall by half'; 'the charm' = her charm | Greta'nın düşüşüne gereğinden fazla sevinmişti ve bu düşüşün şeklini fazlasıyla iyi biliyordu. Cazibesinin altında, |
| 489 | [1289] | Ch16 | MT | Evde balsamı araziden içeri getirdim ve çemberi mutfak masasına koydum. | 'from the shed'; balsam; hoop | Evde köknar dallarını kulübeden içeri getirdim ve kasnağı mutfak masasına koydum. |
| 490 | [1289] | Ch16 | TERM | Renée'nin kurdelesi için bir parça altın kurdele kestim ve kenara koydum, ve balsamın ilk demetini Sugarplum'ın kapısı için çembere bağlayıp | balsam; hoop; bow | Renée'nin fiyongu için bir parça altın kurdele kestim ve kenara koydum, sonra köknarın ilk demetini Sugarplum'ın kapısı için kasnağa bağlayıp |
| 491 | [1291] | Ch17 | MT | balsam dalları çemberin üçte biri kadarını ve sarkan teli kaplamıştı, kurdele için kestiğim altın rengi kurdele de hemen yanında bekliyordu. | 'balsam bound a third of the way around the ring and the wire hanging off the frame' | köknar dalları kasnağın üçte birine sarılmış, tel iskeletten sarkıyordu; fiyonk için kestiğim altın rengi kurdele de hemen yanında bekliyordu. |
| 492 | [1295] | Ch17 | MT | — Durdurdular, dedi ben sormaya fırsat bulamadan. Şu bakışları. | 'They've stopped. The looks.' | — Kesildi, dedi ben sormaya fırsat bulamadan. Şu bakışlar. |
| 493 | [1295] | Ch17 | MT | Bana değil, bal damlalarına baktı. Öyle işte. Teşekkürler. Ben olduğunu biliyorum. | REVERSED 'I know it was you' (MT 'I know it was me'); narration inside speech set off | — Bana değil, bal damlalarına baktı. — Öyle işte. Teşekkürler. Sizin sayenizde olduğunu biliyorum. |
| 494 | [1303] | Ch17 | DLG | Hızlıca başını kaldırdı. Eğer herkes | narration inside speech set off | — Hızlıca başını kaldırdı. — Eğer herkes |
| 495 | [1305] | Ch17 | MT | o ikisine huysuzluktan çok daha iyi gelecektir | 'than a fuss' | o ikisine yaygaradan çok daha iyi gelecektir |
| 496 | [1309] | Ch17 | DLG | Bana tutmamı söylediğin şey. Hafızam yerine geldi. Fincandan hiç ayırmadı gözlerini. Rosie ile nöbet tuttuğumuz o gecelerde, | Danny addresses Jessica as siz (as Ch14); narration set off | Bana aklımda tutmamı söylediğiniz şey. Hatırladım. — Gözlerini fincandan hiç ayırmadı. — Rosie'nin başında beklediğim o gecelerde, |
| 497 | [1309] | Ch17 | TERM | Pete’in dolabının üzerindeki ışık | Pete's locker = soğuk hava deposu | Pete’in soğuk hava deposunun üzerindeki ışık |
| 498 | [1313] | Ch17 | MT | Uzun bir önlük, diz kapaklarına kadar inenlerden, | 'the kind that goes down to your shins' | Uzun bir önlük, baldırlara kadar inenlerden, |
| 499 | [1313] | Ch17 | MT | sonra aradan uzaklaşarak uzak uca doğru gitti. | 'went up the alley toward the far end' | sonra ara sokaktan uzak uca doğru yürüdü. |
| 500 | [1313] | Ch17 | DLG | Kaşlarını çattı. Teslimat falan sandım. | narration inside speech set off | — Kaşlarını çattı. — Teslimat falan sandım. |
| 501 | [1317] | Ch17 | DLG | Üzerinde yazılar olan bir koliydi; üzerinde altın rengi yazılar olduğu için aklımda kalmış. Kenarında altın rengi yazılar vardı. Penceremizden okuyamadım. Sonra bana baktı. Tekrar baktığımda gitmişti. Hafızan yerine gelince bana getirirsin demiştin. | garbled/duplicated; narration set off; Danny → siz | Baskılı bir koliydi; üzerinde altın rengi vardı, o yüzden aklımda kalmış. Yan tarafında altın rengi yazılar. Penceremizden okuyamadım. — Sonra bana baktı. — Tekrar baktığımda gitmişti. Netleşince bana getir demiştiniz. |
| 502 | [1319] | Ch17 | TYPO | zayıf ve çevik bir suretinin | suffix | zayıf ve çevik bir suretin |
| 503 | [1327] | Ch17 | MT | Pip arkasından hüzünlü gözlerle baktı. | 'Pip watched it go with poor grace' (the bag of honey drops) | Pip torbanın gidişini pek hoş karşılamadan izledi. |
| 504 | [1335] | Ch17 | TERM | — Benimle caddeye gelmeni istiyorum, dedim. Sugarplum’a. Renée Duval’dan bana depolarını göstermesini isteyeceğim ve orada, ekşimiş bir mayayı gördüğünde bunu hemen anlayabilecek birinin yanımda olmasını istiyorum. Dürüst birinin, Doktor. Yanılıyor olmama ihtimaline karşı. | sour base = ekşitici baz (MT 'a soured yeast'); Doc formal | — Benimle caddeye gelmenizi istiyorum, dedim. Sugarplum’a. Renée Duval’dan bana depolarını göstermesini isteyeceğim ve orada ekşitici baz bulursa onu tanıyacak birinin yanımda olmasını istiyorum. Dürüst birinin, Doktor. Ne olur ne olmaz, yanılıyorsam diye. |
| 505 | [1337] | Ch17 | DLG | — İhtimaline karşı. Büyüteci bıraktı. Bunu onun yaptığını düşünüyorsun. | echo 'In case'; narration set off; Doc formal | — Ne olur ne olmaz. — Büyüteci bıraktı. — Bunu onun yaptığını düşünüyorsunuz. |
| 506 | [1343] | Ch17 | TERM | derzi, pencere fitilini ve lavaboyu | weather-strip = rüzgârlık (Varney's list) | derzi, rüzgârlığı ve lavaboyu |
| 507 | [1347] | Ch17 | REG | Polis değilim ve o da sana hiçbir şey göstermek zorunda değil. | Doc formal | Polis değilim ve o da size hiçbir şey göstermek zorunda değil. |
| 508 | [1359] | Ch17 | MT | Doktor botlarındaki karları silkelemek için bir an yanımda durdu, Pip ise birden | 'Doc stood beside her' (Pip) | Doktor botlarındaki karları silkelemek için bir an onun yanında durdu, Pip ise |
| 509 | [1371] | Ch17 | TERM | — Biri Greta’nın ununa ekşi maya katmış, dedim. Bir ekmek mutfağını mahvedecek asitlikte, fırınladığı her şeyi ekşitecek kadar çok. Bu sabah bana şikayet dilekçesinde müfettiş daha içeri adımını atmadan önce belirtilen üç kusuru, derzi, fitili ve lavaboyu tek tek saydın. Bu yüzden açıkça sormaya geldim. Bunu yapan sen miydin? | sour base (MT 'sour yeast'; 'enough to ruin a bread kitchen' mistranslated); Renée → siz (she uses siz) | — Biri Greta’nın ununa ekşitici baz katmış, dedim. Ekmek fırınlarının kullandığı bir asit; pişirdiği her şeyi ekşitmeye yetecek kadar. Bu sabah bana, müfettiş daha içeri adımını atmadan şikâyet dilekçesinde belirtilen üç kusuru, derzi, rüzgârlığı ve lavaboyu tek tek saydınız. Bu yüzden açıkça sormaya geldim. Bunu siz mi yaptınız? |
| 510 | [1379] | Ch17 | DLG | — Hayır. Yapmadım. Geçidin yanında asılı duran anahtarlardan birini alıp kuru gıda deposunun kilidini açtı. O hâlde bakın. | narration inside speech set off | — Hayır. Yapmadım. — Kemerin yanındaki çividen bir anahtar alıp kuru gıda deposunun kilidini açtı. — O hâlde bakın. |
| 511 | [1381] | Ch17 | MT | Portland’daki evden gelen un çuvalları | 'the Portland house' = the supplier | Portland’daki toptancıdan gelen un çuvalları |
| 512 | [1381] | Ch17 | TERM | Kilerde, kalıplar halinde tereyağı ve krema. | 'In the walk-in' = soğutucu (walk-in term); 'by the case' | Soğutucuda, koli koli tereyağı ve krema. |
| 513 | [1381] | Ch17 | TERM | bir kutu ekmek katkı maddesi | 'bread improver' | bir kutu ekmek iyileştirici |
| 514 | [1383] | Ch17 | UNIT | Elli pounda bir tutam. Hamur düzenleyici. Kapağını geri kapattı. Greta’nın ununun içindeki şey bu değil. Ekşi maya dolu bir kutunun | 'a pinch in fifty pounds' → 23 kg (SAFE); sour base term; narration set off | Yirmi üç kiloya bir tutam. Hamur düzenleyici. — Kapağını geri kapattı. — Greta’nın ununun içindeki şey bu değil. Ekşitici baz dolu bir kutunun |
| 515 | [1389] | Ch17 | OM | bekleyen yassılaştırılmış koli yığınlarının yanında | 'gold labels and all' dropped (clue: the gold carton) | bekleyen, altın etiketleriyle birlikte yassılaştırılmış koli yığınlarının yanında |
| 516 | [1391] | Ch17 | TERM | — Un, tereyağı, kuvertür, badem, katkı maddesi, dedi Doktor nihayet. Krema. Kutular. Klasörü kapattı. Ekşi maya yok. | sour base term; narration set off | — Un, tereyağı, kuvertür, badem, iyileştirici, dedi Doktor nihayet. Krema. Kutular. — Klasörü kapattı. — Ekşitici baz yok. |
| 517 | [1393] | Ch17 | MT | — İnsan kruvasanın içine ekşi maya koymaz, Doktor | 'One doesn't put sour in a croissant' | — İnsan kruvasana ekşilik katmaz, Doktor |
| 518 | [1399] | Ch17 | DLG | Klasörü Doktor’un elinden alıp mermerin üzerine düzgünce yerleştirdi. Eğer | narration inside speech set off | — Klasörü Doktor’un elinden alıp mermerin üzerine düzgünce yerleştirdi. — Eğer |
| 519 | [1405] | Ch17 | REG | — Bize gösterdiğin için teşekkürler, dedim. | Jessica ↔ Renée siz | — Bize gösterdiğiniz için teşekkürler, dedim. |
| 520 | [1407] | Ch17 | DLG | — Sanırım yine de çelenk getireceksiniz, dedi. Balsam dalları ve altın rengi kurdeleyle. İçeri girerken yaptığı gibi geçitte bize yol verdi. | echo of 'Balsam and a gold bow' (as Ch16); narration set off | — Sanırım çelengi yine de getireceksiniz, dedi. Köknar ve altın sarısı bir fiyonkla. — İçeri girerken yaptığı gibi kemerli geçidi bize açık tuttu. |
| 521 | [1419] | Ch17 | MT | — Emin miydin? | 'You were sure.' is a statement; Doc formal | — Emindiniz. |
| 522 | [1421] | Ch17 | MT | — Eminmişim. | 'I was.' | — Emindim. |
| 523 | [1425] | Ch17 | MT | Grange’dan beri eminim, o sabah içtiği kahvenin üzerinde ise daha da emindim. | 'surer that morning over her coffee' | Grange’dan beri emindim; o sabah onun kahvesini içerken daha da emin olmuştum. |
| 524 | [1425] | Ch17 | MT | Yani onun olmasını o kadar çok istemiştim ki. | 'So I had wanted it to be her' | Yani onun olmasını istemiştim. |
| 525 | [1435] | Ch17 | TERM | balsam dallarını halkadan birer birer, önümde çıplak çelik çerçeveden başka bir şey kalmayana kadar kaldırdım. | balsam; ring/frame (avoid circle word) | köknar dallarını kasnaktan birer birer, önümde çıplak çelik iskeletten başka bir şey kalmayana kadar söktüm. |
| 526 | [1435] | Ch17 | TERM | ilk dalı alıp çemberin üzerine yerleştirdim. | ring = kasnak | ilk dalı alıp kasnağın üzerine yerleştirdim. |
| 527 | [1438] | Ch18 | MT | adeta dikey düşen bir taş gibi | 'like a dropped stone' | elden bırakılmış bir taş gibi |
| 528 | [1438] | Ch18 | MT | Pencerelerin kenarları beyaza kesmiş, | 'windows ferned white to their corners' | Pencereler köşelerine kadar beyaz buz çiçekleriyle kaplanmış, |
| 529 | [1438] | Ch18 | TERM | düşünmeden önce, meydandaki Dernek’in dar tuğla binasını | Society = Cemiyet | düşünmeden önce, meydandaki Cemiyet’in dar tuğla binasını |
| 530 | [1441] | Ch18 | MT | — Dernek’in kazanı patladı, dedi kapı eşiğinde. Böğründen çatlamış. | 'gone… Cracked right down the side' (not exploded) | — Dernek’in kazanı gitti, dedi kapı eşiğinde. Yanından boydan boya çatlamış. |
| 531 | [1441] | Ch18 | TERM | — Dernek’in kazanı gitti, dedi | Society = Cemiyet | — Cemiyet’in kazanı gitti, dedi |
| 532 | [1443] | Ch18 | MT | hiçbir pervazda duraklamadı | 'didn't stop at any sill' (threshold) | hiçbir eşikte duraklamadı |
| 533 | [1444] | Ch18 | TYPO | gerekmüştü | typo | gerekmişti |
| 534 | [1445] | Ch18 | MT | — Ferris kazanı yenileyecekti, | 'was going to stand the boiler' = pay for it | — Ferris kazanın parasını karşılayacaktı, |
| 535 | [1445] | Ch18 | MT | çatının masrafı diğerinin nerdeyse iki katı | 'the bigger sum by half' = 1.5× | çatının masrafı diğerinin bir buçuk katı |
| 536 | [1447] | Ch18 | MT | Otomobil yolculuğunun o güzel hissi, Grange’da dolup taşan sedir kutusu, her pencerede kurucusunun soyu ve bunun utanç verici bir durum olacağını söyleyen dikkatli kadınlar... | 'the drive' = donation drive (MT 'car ride'); 'the founder's line' = her sentence (MT 'lineage') | Bağış kampanyasının o güzel havası, Grange’da dolup taşan sedir kutusu, her pencerede kurucunun o cümlesi ve bunun çok yazık olacağını söyleyen tutumlu kadınlar... |
| 537 | [1447] | Ch18 | EN | Mr. Worthington’ı düşündüm. Ondan bunu yedekte tutmasını istemiştim ve o da öyle yapmıştı. | English title 'Mr.'; 'and I left it there' | Bay Worthington’ı düşündüm. Ondan bunu yedekte tutmasını istemiştim ve öyle de bırakmıştım. |
| 538 | [1447] | Ch18 | TERM | tutunmasının zorlaşmasını seyrettim. Derneğin en eski bağışçısı | Society = Cemiyet | tutunmasının zorlaşmasını seyrettim. Cemiyetin en eski bağışçısı |
| 539 | [1447] | Ch18 | TYPO | tutumlu kadınlar... | ellipsis = single character … (dossier) | tutumlu kadınlar… |
| 540 | [1448] | Ch18 | TYPO | dününü de sırtımda taşıyordum | possessive | dünü de sırtımda taşıyordum |
| 541 | [1448] | Ch18 | TERM | Renée’nin dükkânındaki rafların, içinde en ufak bir ekşilik emaresi bile olmayan malzemelerle Doc’a açılışını, kesinlik hissemin | sour base term; Doc = Doktor; typo | Renée’nin, içinde zerre kadar ekşitici baz bulunmayan depolarının Doktor’a raf raf açılışını, kesinlik hissimin |
| 542 | [1448] | Ch18 | TERM | içine bir şeyler katılmış un çuvalı | flour bin | içine bir şeyler katılmış un bidonu |
| 543 | [1449] | Ch18 | TERM | döndüm. Nedenini söyleyemezdim. Derneğin, ilk soğuk gecesinde, | Society = Cemiyet | döndüm. Nedenini söyleyemezdim. Cemiyetin, ilk soğuk gecesinde, |
| 544 | [1452] | Ch18 | EN | Yönetim kurulundan Mrs. Pelletier, | English title 'Mrs.' | Yönetim kurulundan Bayan Pelletier, |
| 545 | [1452] | Ch18 | MT | Kıskaçlarıyla çalışırken izlediğim | 'his brads' (as Ch6) | Çivileriyle uğraşırken izlediğim |
| 546 | [1454] | Ch18 | MT | ıslak bir yaprağı bile tek tek kurtarıyordu | 'salvaging what would salvage, one wet leaf at a time' | kurtarılabilecek olanı, ıslak sayfaları birer birer kurtarıyordu |
| 547 | [1458] | Ch18 | MT | bunun için övgü almamayı, kimseye teşekkür etmemeyi amaçlamıştı | REVERSED 'be thanked by no one' (MT 'thank no one') | bunun için övgü almamayı, kimseden teşekkür duymamayı amaçlamıştı |
| 548 | [1460] | Ch18 | EN | — Mrs. Claus, dedi. | English title 'Mrs.' | — Bayan Claus, dedi. |
| 549 | [1463] | Ch18 | MT | Benden istemese de, bir kez olsun övülmemeyi istemişti | 'He had asked me once, without asking, not to be praised' | Bir keresinde, istemeden, benden övülmemeyi istemişti |
| 550 | [1463] | Ch18 | MT | Onu akladım da sayılmazdı. | 'I did not absolve him either' | Onu bağışlamadım da. |
| 551 | [1463] | Ch18 | TYPO | Ama paltoyu çıkarıp | possessive | Ama paltomu çıkarıp |
| 552 | [1470] | Ch19 | MT | — Bırak onu, dedi Nick kıza. | 'Nick told her' (Pip) — 'kıza' = to the girl | — Bırak onu, dedi Nick ona. |
| 553 | [1476] | Ch19 | TERM | sokak aralığını temsil etmesi için | alley = ara sokak | ara sokağı temsil etmesi için |
| 554 | [1477] | Ch19 | MT | Bütün sokakta eski tuğlalardan oluşan tek bir yığın var. | 'on the whole block' | Bütün blokta eski tuğlalardan oluşan tek bir yığın var. |
| 555 | [1479] | Ch19 | MT | Harcın üzerinde onun molozunu gördüm ve adını okudum. | 'I saw her rubble on that brick and read her name' | O tuğlanın üzerinde onun molozunu gördüm ve onun adını okudum. |
| 556 | [1484] | Ch19 | MT | Bunun üzerinde durdu ve | 'He let that stand' | Buna itiraz etmedi ve |
| 557 | [1487] | Ch19 | MT | Dükkânı dizdiğinden beri | 'since she fitted out' | Dükkânı döşediğinden beri |
| 558 | [1489] | Ch19 | MT | işi için gerekli pudrasını | 'her powder' | işi için gerekli tozunu |
| 559 | [1492] | Ch19 | MT | Bir kez kendi mahallesinde, senin etinin üzerinde. | 'Once at his block, over your roast' | Bir kez kütüğünün başında, senin rostonu bağlarken. |
| 560 | [1492] | Ch19 | MT | Kasabınki değil. | 'Not the meat man's' | Et tedarikçisininki değil. |
| 561 | [1494] | Ch19 | MT | — Önemli bir şey çıkmaz dedim. Şoför şekerleme yapmak için durmuştur. Ama Pete o avluya giren her kamyonu bilir; kasabınki olmadığını söyledi, ben de kimseninkini duymadım. | 'I made nothing of it'; 'not the meat man's, and I heard nobody's' | — Hiç üzerinde durmadım. Şoför şekerleme yapmak için durmuştur, dedim. Ama Pete o avluya giren her kamyonu bilir; et tedarikçisininki değil dedi, ben de bunu kimseninki değil diye duydum. |
| 562 | [1494] | Ch19 | MT | İnce ve çevik bir adam, fırınları yanmadan hemen önce Greta’nın penceresinin önündeydi | EN is ungendered ('figure') — MT made it 'a man'; 'sill' | İnce ve çevik bir siluet, fırınları yanmadan önce Greta’nın eşiğindeydi |
| 563 | [1495] | Ch19 | MT | Eğer plakayı değiştirdiyse, o da kasaba dışından bir plakadır. | REVERSED 'if she's not changed it' | Plakasını değiştirmediyse, o da kasaba dışından bir plaka demektir. |
| 564 | [1496] | Ch19 | MT | Kapısından çıkıp Greta’nın penceresinin önüne yürüyebilir | 'down to Greta's sill' | Kapısından çıkıp Greta’nın eşiğine yürüyebilir |
| 565 | [1498] | Ch19 | MT | Kardan adamı da aradan çıkaracaksın herhalde. | 'You'll want to do the snowman' | Kardan adamı da ele almak isteyeceksin. |
| 566 | [1500] | Ch19 | UNIT | diğerleri meydana gidip senin ocağına doğru sıraya dizildiler. O kardan adam diğer yöne gitti, sürülerinden on adım öteye, | 'leaned up the lane toward your hearth'; 'ten feet' → 3 m (SAFE) | diğerleri meydana gidip yoldan yukarı, senin ocağına doğru eğildi. O kardan adam diğer yöne gitti, arkadaşlarından üç metre öteye, |
| 567 | [1501] | Ch19 | DLG | — Bunu nazikçe söyledi. Sana hiçbir şey | narration inside speech set off | — Bunu nazikçe söyledi. — Sana hiçbir şey |
| 568 | [1509] | Ch19 | MT | Yani dükkânın kapanışı açılış saatine göre ayarlanmıştı. | 'timed to the opening' | Yani dükkânın kapanışı açılışa göre ayarlanmıştı. |
| 569 | [1510] | Ch19 | MT | Grange’ın basamağından beri bunu yanlış anlamışım. | 'I had it backward' | Grange’ın basamağından beri bunu tersinden okumuşum. |
| 570 | [1512] | Ch19 | TERM | içeride hiç ekşi maya tabanı olmadığını gördü, o da bana Greta’nın derz dolgusu hakkında | sour base = ekşitici baz; grout = derz | içeride hiç ekşitici baz olmadığını gördü, o da bana Greta’nın derzi hakkında |
| 571 | [1512] | Ch19 | MT | birisinin tezgâhının üzerinde kanıt olarak durur | 'A flyer's a proof' = printer's proof, not evidence | birisinin tezgâhının üzerinde prova baskısı olarak durur |
| 572 | [1522] | Ch20 | TERM | İki çikolatalı-cevizli ve bir düzine ekmek, Şükran Günü'nden önceki çarşamba hazır olacakmış. — Telefonu indirdi. — Siparişimin aynısı. Ekmek sayısı bile tutuyor. | Martha's order — identical to Ch14 ('two chocolate-pecans and a dozen rolls'); 'To the roll' | İki çikolatalı-cevizli turta ve bir düzine çörek, Şükran Günü'nden önceki çarşamba hazır olacakmış. — Telefonu indirdi. — Siparişimin aynısı. Çöreğine kadar. |
| 573 | [1525] | Ch20 | MT | Adım, numaram ve üç bal kabağım vardı kadında. Greta'dan ekmekleri fırına verilmemiş hamur halinde | 'my three pumpkin pies'; 'the rolls unbaked' | Adım, numaram ve üç bal kabaklı turtam kadında kayıtlıydı. Greta'dan çörekleri fırına verilmemiş hamur hâlinde |
| 574 | [1525] | Ch20 | MT | Joyce pazartesi günü kadına güveç götürmüş | 'Joyce took her a casserole' (Greta) | Joyce pazartesi günü Greta'ya güveç götürmüş |
| 575 | [1527] | Ch20 | EN | Ekmek yerine roll tercih edip etmediğimi teyit etmek için | English 'roll' left in | Ekmek değil de çörek istediğimden emin olmak için |
| 576 | [1529] | Ch20 | EN | Halloween'den önceki hafta | English 'Halloween' (book uses Cadılar Bayramı) | Cadılar Bayramı'ndan önceki hafta |
| 577 | [1538] | Ch20 | MT | Tom'un yeniden taktırdığı cam, eski kasaların yanında | 'beside the old frames' | Tom'un yeniden taktığı cam, eski çerçevelerin yanında |
| 578 | [1540] | Ch20 | TERM | — Tom perşembe günü hava sızdırmazlığını yaptı. Derz dolguyu kendi ellerimle çektim. Vilayet de lavabo tamamen düzelene kadar gelmeyecekmiş. | weather-strip = rüzgârlık; grout = derz; county = ilçe | — Tom perşembe günü rüzgârlığı yeniledi. Derzi kendi ellerimle doldurdum. İlçe de lavabo düzelene kadar gelmeyecekmiş. |
| 579 | [1544] | Ch20 | TERM | pastaları için başka bir yere | pies = turta | turtaları için başka bir yere |
| 580 | [1544] | Ch20 | MT | Çaydanlığı halkasının üzerine yerleştirdi. | 'set the kettle on its ring' (burner) | Çaydanlığı ocağın üzerine yerleştirdi. |
| 581 | [1547] | Ch20 | TERM | İki çikolatalı-cevizli ile bir düzine ekmek. Ivy'yi de aramışlar, onun üç bal kabağını da söylemişler. | Martha's order wording; 'her three pumpkins' (pies) | İki çikolatalı-cevizli turta ve bir düzine çörek. Ivy'yi de aramışlar, üç bal kabaklı turtasıyla birlikte. |
| 582 | [1553] | Ch20 | MT | en yakın koltuk olduğu için | 'the nearest seat' | en yakın oturacak yer olduğu için |
| 583 | [1554] | Ch20 | TERM | — Vilayetten gelen adam kapıdan çıkarken, dedi Greta, soğuk oda dedi. | CLUE word quoted; county = ilçe | — İlçeden gelen adam kapıdan çıkarken, dedi Greta, "soğuk oda" dedi. |
| 584 | [1556] | Ch20 | TERM | — Joyce'tan beri kimse buraya öyle denildiğini duymamıştı. — Bunu deftebe söylüyormuş gibi konuştu. — Soğuk hava deposu deriz biz. Harold'a göre, sevkiyatçılara göre, benim için çalışmış herkese göre burası hep soğuk hava deposuydu. Joyce buraya soğuk oda derdi. Soğuk odaya giriyorum Greta, ekmekleri yakma sakın derdi, sanki evin herhangi bir odasıymış gibi. | CLUE: walk-in = soğutucu, Joyce's word = soğuk oda (MT used Pete's 'soğuk hava deposu' for the walk-in); typo 'deftebe' | — Joyce'tan beri kimse ona öyle dememişti. — Bunu deftere söylüyormuş gibi konuştu. — O soğutucu. Harold için de, sevkiyatçılar için de, benim yanımda çalışmış herkes için de hep soğutucuydu. Joyce ise ona soğuk oda derdi. "Soğuk odaya giriyorum Greta, çörekleri yakma sakın," derdi, sanki evin bir odasıymış gibi. |
| 585 | [1556] | Ch20 | TERM | Soğuk hava deposu dedim. Kendimi zorladım. | CLUE: walk-in = soğutucu | Soğutucu dedim. Kendimi zorladım. |
| 586 | [1558] | Ch20 | REG | avlu kapınızdaki kilidin | Jessica ↔ Greta sen | avlu kapındaki kilidin |
| 587 | [1561] | Ch20 | MT | Biri benim halkamda. Diğeri Joyce'un üzerindeydi. | 'One's on my ring. The other one was on Joyce's' (key ring) | Biri benim anahtarlığımda. Diğeri Joyce'unkindeydi. |
| 588 | [1565] | Ch20 | TERM | kapının altındaki eskitme şeridin aşındığı ve karşı duvarın dibindeki derz harcının çatladığı | weather-strip = rüzgârlık; grout = derz (Varney's list) | kapının altındaki rüzgârlığın aşındığı ve uzak duvarın dibindeki derzin çatladığı |
| 589 | [1567] | Ch20 | MT | Gittiğinden beri hiç tadına bakmamıştı. | person: 'I hadn't tasted it' | Gittiğinden beri hiç tadına bakmamıştım. |
| 590 | [1569] | Ch20 | MT | Düğününde ayakta durdum. | 'I stood at her wedding' (as attendant), calque | Düğününde yanında durdum. |
| 591 | [1569] | Ch20 | MT | İki vilayetteki herkes | 'two counties' | İki ilçedeki herkes |
| 592 | [1586] | Ch21 | TERM | Bir ekmek fırını ekşi maya mayası almak istese | sour base = ekşitici baz (MT 'sourdough yeast-yeast') | Bir ekmek fırını ekşitici baz almak istese |
| 593 | [1587] | Ch21 | MT | giderken de yanına götürdü ve bunu değiştirmeyecektir. | 'she won't have changed it' | giderken de yanında götürdü ve değiştirmemiştir. |
| 594 | [1592] | Ch21 | MT | — İkisinin de takipçisi olacağım. | 'I'm holding you to both halves of that' | — Sözünün iki yarısını da tutmanı bekleyeceğim. |
| 595 | [1595] | Ch21 | MT | Maine Dışişleri Bakanlığı'nın işletme arama sayfasını | 'Maine Secretary of State' is a state office, not a foreign ministry | Maine Eyalet Sekreterliği'nin şirket arama sayfasını |
| 596 | [1599] | Ch21 | MT | Pencerenin kırıldığı sabah, Joyce içeriyi süpürürken çerçeveden cam parçalarını toplayarak caddede not defteriyle dolaşmış olan oydu. | garbled sentence | Pencerenin kırıldığı sabah o da not defteriyle caddedeydi; Joyce içeride süpürürken çerçeveden cam parçalarını toplamıştı. |
| 597 | [1602] | Ch21 | MT | Varış. Her sabah kapınıza taze yazısının altında | stray word 'Varış.' (= 'Arrival') added by the MT | Her sabah kapınıza taze yazısının altında |
| 598 | [1607] | Ch21 | TERM | Köy meydanını geçerken | the green = meydan | Meydanı geçerken |
| 599 | [1608] | Ch21 | MT | — Konu etse, iyilerinden kalmadı bende. | garbled 'If this is about a roast, I'm out of the good ones' | — Rosto içinse, iyilerinden kalmadı. |
| 600 | [1609] | Ch21 | REG | — Çıktıyı tezgahının üzerine koydum. — Bana eczanenin olduğu uzak köşede farları sönük park etmiş bir minibüs olduğunu söylemiştin. | Pete formal; 'his block' | — Çıktıyı kütüğünün üzerine koydum. — Bana eczanenin olduğu uzak köşede farları sönük park etmiş bir minibüs olduğunu söylemiştiniz. |
| 601 | [1610] | Ch21 | MT | Tezgahın üzerindeki lambanın altında | 'the light over the block' | Kütüğün üzerindeki lambanın altında |
| 602 | [1612] | Ch21 | REG | — Bunu şefe söyler misin peki? | Pete formal | — Bunu şefe söyler misiniz peki? |
| 603 | [1613] | Ch21 | TYPO | — Kimin ki bu? | typo | — Kimin bu? |
| 604 | [1614] | Ch21 | MT | — Şefin, herkesinkinden önce haberi olmasını tercih ederim. | 'I'd rather the chief had it before anyone else' | — Önce şefin haberi olsun isterim. |
| 605 | [1615] | Ch21 | MT | Hık dedi. — Adil. | 'He grunted. "Fair."' | Homurdandı. — Haklısınız. |
| 606 | [1615] | Ch21 | REG | Ona bunu daha yeni süpürdüğümü söyle. | Pete formal | Ona bunu daha yeni süpürdüğümü söyleyin. |
| 607 | [1617] | Ch21 | TYPO | Mantolomu bile çıkar-madım. | typo / stray hyphen | Mantomu bile çıkarmadım. |
| 608 | [1620] | Ch21 | TERM | — Doktor, Greta'nın ununun içinde bir ekşi maya mayası buldu, dedim. | sour base | — Doktor, Greta'nın ununun içinde ekşitici baz buldu, dedim. |
| 609 | [1620] | Ch21 | TERM | Wendt's Bakehouse'a bir ekşi maya mayası teslim edip etmediğini | sour base | Wendt's Bakehouse'a ekşitici baz teslim edip etmediğini |
| 610 | [1624] | Ch21 | NM | Dok'a götürdüğün un nerede? | Doc = Doktor | Doktor'a götürdüğün un nerede? |
| 611 | [1625] | Ch21 | NM | — Dok'ta. | Doc = Doktor | — Doktor'da. |
| 612 | [1628] | Ch21 | TERM | Wendt's Bakehouse yirmi beş yıldır onlardan hesap açtırmış. Haziran ayına kadar, hanlara pişirdiği çavdar ekmeği için her birkaç haftada bir bir çuval ekşi maya mayası. Sonra hiçbir şey yok. Yaz boyunca büyük han hesabını kaybettiğini, | sour base; 'the inns' (MT 'hans'); 'has had an account with them' | Wendt's Bakehouse'un yirmi beş yıldır orada hesabı varmış. Haziran ayına kadar, otellere pişirdiği çavdar ekmeği için birkaç haftada bir bir çuval ekşitici baz. Sonra hiçbir şey yok. Yaz boyunca büyük otel müşterisini kaybettiğini, |
| 613 | [1628] | Ch21 | MT | Sürücünün fişini J. Wendt olarak imzaladığını söylüyor. | 'the driver's ticket is signed J. Wendt' — J. Wendt signed, not the driver | Teslimat fişinde J. Wendt imzası varmış. |
| 614 | [1630] | Ch21 | NM | ben de Dok'a ilettim, dedi. Dok izlemek istersen | Doc = Doktor | ben de Doktor'a ilettim, dedi. Doktor izlemek istersen |
| 615 | [1632] | Ch21 | NM | Dok Mitchell'ın | Doc = Doktor | Doktor Mitchell'ın |
| 616 | [1634] | Ch21 | NM | dedi Dok. | Doc = Doktor | dedi Doktor. |
| 617 | [1634] | Ch21 | MT | Bir devlet laboratuvarı | 'A state lab' | Eyalet laboratuvarı |
| 618 | [1634] | Ch21 | MT | bu kağıda uyuyor | 'fits this sheet' (the product sheet) | bu ürün sayfasına uyuyor |
| 619 | [1643] | Ch22 | MT | Üstelik daha önce de böyle bir şeye kalkışmışlığım vardı. | 'And I'd been sure before.' | Üstelik daha önce de emin olmuştum. |
| 620 | [1643] | Ch22 | TYPO | Sugarplum’ın içeriğinden içeri girmiştim | garbled | Sugarplum’a girmiştim |
| 621 | [1644] | Ch22 | MT | Greta’nın adı temiz kâğıdıyla kendisine iade edilirdi | 'Greta's name would come back to her on paper' | Greta’nın adı da ona kâğıt üzerinde geri verilirdi |
| 622 | [1651] | Ch22 | TYPO | Beneri içeri girdiğimde | typo | Ben içeri girdiğimde |
| 623 | [1655] | Ch22 | MT | Bridgton’daki bir pastaneden aramışlar; Holly Jolly siparişlerini üstlenmeyi teklif etmişler. Pastalarına varıncaya dek. | 'a bakery'; 'Down to the pies' | Bridgton’daki bir fırından aramışlar; Holly Jolly siparişlerini üstlenmeyi teklif etmişler. Turtalarına varıncaya dek. |
| 624 | [1657] | Ch22 | TERM | — Şikâyet dilekçesinde soğuk odadan soğuk oda diye, eviye için de Hobart eviyesi diye bahsedilmiş. | CLUE: MT said 'called the cold room the cold room' — the slip vanished; walk-in = soğutucu, hand-sink = el lavabosu (as Ch9/Ch20) | — Şikâyet dilekçesinde soğutucuya "soğuk oda", el lavabosuna da "Hobart lavabosu" deniyormuş. |
| 625 | [1657] | Ch22 | TERM | Bahçe kapısının kilidi | 'the yard gate' | Avlu kapısının kilidi |
| 626 | [1657] | Ch22 | MT | Gün ağarmadan önce eczanenin oralarda farları sönük bir minibüs görmüş, etçinin arabası değilmiş. Dün Claire’in çıkardığı Wendt’lerin minibüsü fotoğrafına baktı ve ‘İşte bu,’ dedi. | subject 'He' = Pete made explicit; 'not the meat man's' | Pete gün ağarmadan önce eczanenin oralarda farları sönük bir minibüs görmüş, et tedarikçisininki değilmiş. Dün Claire’in çıktısını aldığı Wendt's minibüsünün fotoğrafına baktı ve "İşte bu," dedi. |
| 627 | [1659] | Ch22 | MT | — Danny Ott, sabahın köründe Greta’nın pencere pervazında ince, çevik bir siluet görmüş, uzaklara doğru seğirtiyormuş. Başka bir sabah kapısının önünde etiketinde altın yaldızlar olan bir koli bulmuş. | 'at Greta's sill'; 'going away toward the far end'; 'saw' (not 'found') | — Danny Ott, sabahın köründe Greta’nın eşiğinde ince, çevik bir siluet görmüş, uzak uca doğru gidiyormuş. Başka bir sabah kapısının önünde etiketinde altın yaldız olan bir koli görmüş. |
| 628 | [1659] | Ch22 | TERM | kavanozumdaki tozun ekşi mayayla birebir uyuştuğunu söylüyor, test üstüne test. | sour base | kavanozumdaki tozun ekşitici bazla her testte birebir uyuştuğunu söylüyor. |
| 629 | [1661] | Ch22 | TERM | Ekşi maya, bir çuval, Wendt’in Pastanesi’ne teslim edilmiş, Bridgton. Teslim alan: J. Wendt. | sour base; business name as elsewhere | Ekşitici baz, bir çuval, teslim yeri Wendt's Bakehouse, Bridgton. Teslim alan: J. Wendt. |
| 630 | [1672] | Ch22 | TYPO | beklemiyecek | spelling | beklemeyecek |
| 631 | [1676] | Ch22 | TYPO | Greta’nın haberi var sig? | garbage token 'sig' | Greta’nın haberi var mı? |
| 632 | [1687] | Ch22 | EN | Burada olmak zorunda değilsin. Senin yerinde ols பெரும்பாலான insan orada olmamayı tercih ederdi. | Tamil word leaked into the sentence; Chief ↔ Greta professional → siz | Burada olmak zorunda değilsiniz. Sizin yerinizde olan çoğu insan orada olmamayı tercih eder. |
| 633 | [1690] | Ch22 | MT | On beş yıl boyunca o kadının yanındaki bankta oturdum. | 'I sat at the next bench' (workbench) | On beş yıl boyunca o kadının yanındaki tezgâhta çalıştım. |
| 634 | [1692] | Ch22 | REG | İstemediğin sürece tek kelime etmek zorunda değilsin. | Chief ↔ Greta professional → siz | İstemediğiniz sürece tek kelime etmek zorunda değilsiniz. |
| 635 | [1694] | Ch22 | REG | — O zaman onun seni görebileceği bir yere otur, dedi Tanaka | Chief ↔ Greta professional → siz | — O zaman onun sizi görebileceği bir yere oturun, dedi Tanaka |
| 636 | [1696] | Ch22 | MT | ben Frost Falls emniyet müdürü Noriko Tanaka | 'chief of police' | ben Frost Falls polis şefi Noriko Tanaka |
| 637 | [1703] | Ch23 | MT | Kenara taşınan ezik su ısıtıcısı çalıştırılmıştı, havada buhar tütüyordu. | 'the dented kettle' (çaydanlık, as Ch22) | Göçük çaydanlık oraya getirilip köşede ocağa konmuştu, havada buhar vardı. |
| 638 | [1703] | Ch23 | TYPO | Greta iyi manttosuyla | typo | Greta iyi paltosuyla |
| 639 | [1711] | Ch23 | TYPO | — Kesânin yanındaki ağır pirinç ve çelik anahtarlığı masaya bırakırken aralarında minibüsün anahtarı da vardı. | typo 'Kesânin'; garbled sentence | — Anahtarlarını kesenin yanına, masaya bıraktı; aralarında minibüsün anahtarı da bulunan, pirinç ve çelikten ağır bir anahtarlıktı. |
| 640 | [1711] | Ch23 | DLG | — Elimden ne gelirse — dedi parkasını açarak. | closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier); resumed speech after a plain attribution takes no new dash (dossier) | — Elimden ne gelirse, dedi parkasını açarak. |
| 641 | [1711] | Ch23 | DLG | dedi parkasını açarak. — Gerçekten. Ona yardım | closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier); resumed speech after a plain attribution takes no new dash (dossier) | dedi parkasını açarak. Gerçekten. Ona yardım |
| 642 | [1719] | Ch23 | DLG | — Bayan Wendt — dedi Tanaka. — | closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier); resumed speech after a plain attribution takes no new dash (dossier) | — Bayan Wendt, dedi Tanaka. Tutuklu |
| 643 | [1719] | Ch23 | DLG | — dedi Tanaka. — Tutuklu değilsiniz. Kendi | closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier); resumed speech after a plain attribution takes no new dash (dossier) | Wendt, dedi Tanaka. Tutuklu değilsiniz. Kendi |
| 644 | [1721] | Ch23 | DLG | — Tabii ki — dedi Joyce ve | closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier) | — Tabii ki, dedi Joyce ve |
| 645 | [1723] | Ch23 | TERM | elinde itme süpürgesiyle | push broom (as Ch20) | elinde iterli süpürgesiyle |
| 646 | [1727] | Ch23 | DLG | — Fırınınız Cuma gecesi Greta’nın iki müşterisini aramış — dedi Tanaka, — Greta’nın defterindeki siparişleri kelimesi kelimesine doldurmayı teklif etmişsiniz. | attribution rebuilt (dash system); 'offering to fill their Holly Jolly orders, word for word out of Greta's book' | — Fırınınız cuma akşamı Greta’nın iki müşterisini aramış, dedi Tanaka. Holly Jolly siparişlerini, Greta’nın defterindekiyle kelimesi kelimesine aynı şekilde karşılamayı teklif etmiş. |
| 647 | [1731] | Ch23 | TERM | — İlçeye yapılan şikâyette kendisinin soğuk odasını soğuk oda, evyesini ise Hobart evyesi olarak adlandırmışlar. Greta, bunları senden başka kimsenin o şekilde adlandırmadığını söylüyor. | CLUE: MT 'called her cold room the cold room' erased the slip; walk-in = soğutucu; Chief → Joyce siz | — İlçeye yapılan şikâyette onun soğutucusuna "soğuk oda", el lavabosuna da "Hobart lavabosu" denmiş. Greta, sizden beri kimsenin onlara böyle demediğini söylüyor. |
| 648 | [1735] | Ch23 | TERM | — Dr. Mitchell, unundaki tozu ekşi mayayla eşleştirdi. Pelkey’ler, aylardır hiç almadıktan sonra, yirmi yedi Ekim’de size bundan bir çuval teslim etmiş. | sour base; Doc = Doktor; Pelkey's (company) | — Doktor Mitchell, unundaki tozu ekşitici bazla eşleştirdi. Pelkey's, aylardır hiç teslimat yapmamışken, yirmi yedi ekimde size bundan bir çuval teslim etmiş. |
| 649 | [1737] | Ch23 | TERM | New England’daki her çavdar fırıncısı ekşi maya alır. | sour base | New England’daki her çavdar fırıncısı ekşitici baz alır. |
| 650 | [1739] | Ch23 | MT | sabah uyanmadan önce birkaç kez eczanenin yanında park etmiş, farları kapalı bir minibüs | 'before light, more than one morning' | gün ağarmadan, birkaç sabah, eczanenin yanında park etmiş, farları sönük bir minibüs |
| 651 | [1741] | Ch23 | MT | Biri buna gülümsemedi. | 'That one got no smile' | Buna gülümseme gelmedi. |
| 652 | [1743] | Ch23 | MT | — Her kimse evimin arka bahçe kapısından içeri girmiş — dedi Greta. | 'my yard gate' (the shop's yard, not a house garden); attribution rebuilt | — Her kimse, avlu kapımdan girdi, dedi Greta. |
| 653 | [1747] | Ch23 | DLG | — Pete’in o kapıda zinciri var — dedi Greta. — Bir ucunda onun kilidi, diğer ucunda benimki. Benimkinde iki anahtar var. | attribution rebuilt; 'two keys to mine' | — Pete’in o kapıda zinciri var, dedi Greta. Bir ucunda onun kilidi, diğer ucunda benimki. Benimkinin iki anahtarı var. |
| 654 | [1755] | Ch23 | DLG | — Yirmi beş yıl — dedi Greta’ya bakarak. | closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier); resumed speech after a plain attribution takes no new dash (dossier) | — Yirmi beş yıl, dedi Greta’ya bakarak. |
| 655 | [1755] | Ch23 | DLG | dedi Greta’ya bakarak. — Hiç değiştirmedin. Tanrım, | closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier); resumed speech after a plain attribution takes no new dash (dossier) | dedi Greta’ya bakarak. Hiç değiştirmedin. Tanrım, |
| 656 | [1761] | Ch23 | MT | zamanını boşa harcamaya karar vermiş bir kadına benzedi | REVERSED 'decided to stop wasting her time' | zamanını boşa harcamayı bırakmaya karar vermiş bir kadına benzedi |
| 657 | [1763] | Ch23 | DLG | — Pekâlâ — dedi. — Nedenini | closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier); resumed speech after a plain attribution takes no new dash (dossier) | — Pekâlâ, dedi. Nedenini öğrenmek |
| 658 | [1763] | Ch23 | DLG | Pekâlâ — dedi. — Nedenini öğrenmek istiyorsunuz. | closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier); resumed speech after a plain attribution takes no new dash (dossier) | — Pekâlâ, dedi. Nedenini öğrenmek istiyorsunuz. |
| 659 | [1767] | Ch23 | UNIT | annemin pekan cevizli turtasıyla alamadığımız bir pound çikolatayla uğraşıp durdum. | 'a pound of chocolate' → yarım kilo (SAFE) | annemin cevizli turtası ve paramızın yetmediği yarım kilo çikolatayla uğraşıp durdum. |
| 660 | [1767] | Ch23 | MT | Ve o aldı. Kapının üstündeki ismi. Turtayı. | 'And she kept it' | Ve hepsini o tuttu. Kapının üstündeki ismi. Turtayı. |
| 661 | [1767] | Ch23 | TERM | Greta’nın çikolatalı-pekan cevizli turtası için | chocolate-pecan = çikolatalı-cevizli (one form) | Greta’nın çikolatalı-cevizli turtası için |
| 662 | [1771] | Ch23 | MT | mazot parasını ödemeden önce | 'the oil' (heating oil) | yakıt parasını ödemeden önce |
| 663 | [1771] | Ch23 | MT | fatura koçanları | 'the stubs' | makbuz koçanları |
| 664 | [1771] | Ch23 | MT | sabahın köründe turtadan ölümüne sıkıldığını | 'pie at four in the morning' | sabahın dördünde turtadan ölümüne bıktığını |
| 665 | [1771] | Ch23 | DLG | — Sana parasını ödedim — dedi. — Sana | closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier); resumed speech after a plain attribution takes no new dash (dossier) | — Sana parasını ödedim, dedi. Sana sekiz |
| 666 | [1771] | Ch23 | DLG | ödedim — dedi. — Sana sekiz yıl | closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier); resumed speech after a plain attribution takes no new dash (dossier) | parasını ödedim, dedi. Sana sekiz yıl |
| 667 | [1777] | Ch23 | TYPO | — Ve sonra seninki oldu. | 'And then it was yours' | — Ve sonra senin oldu. |
| 668 | [1781] | Ch23 | MT | Bunu sana vereceğim. | calque of 'I'll give you that' | Bu konuda hakkını vereyim. |
| 669 | [1781] | Ch23 | MT | Theo’nun bana konuya dahil edilecek bir şeyler sorması | 'Theo asking me for something to put in' | Theo’nun kutuya koymak için benden bir şey istemesi |
| 670 | [1781] | Ch23 | DLG | — Gitmene izin verdim — dedi sonunda Greta | closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier) | — Gitmene izin verdim, dedi sonunda Greta |
| 671 | [1785] | Ch23 | MT | — O kız buraya financier’ler gönderdi, Joyce; o kadın benden nefret eder ve buraya financier’ler gönderdi. Ve sen içeri bir süpürgeyle girdin. | 'She sent a girl over with financiers. That one can't stand me…' | — O kadın bir kızla buraya financier gönderdi, Joyce. Benden hiç hoşlanmayan o kadın, bir kızla financier gönderdi. Sen ise elinde süpürgeyle geldin. |
| 672 | [1785] | Ch23 | DLG | bunu turta için yapmadın — dedi Greta. — | closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier); resumed speech after a plain attribution takes no new dash (dossier) | bunu turta için yapmadın, dedi Greta. Yapmadığını |
| 673 | [1785] | Ch23 | DLG | — dedi Greta. — Yapmadığını söyleme bana. | closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier); resumed speech after a plain attribution takes no new dash (dossier) | yapmadın, dedi Greta. Yapmadığını söyleme bana. |
| 674 | [1789] | Ch23 | MT | — Ve ellerimin titrediğini sanmama izin verdin. | 'you let me think it was my hands' (not trembling) | — Ve suçun ellerimde olduğunu sanmama izin verdin. |
| 675 | [1789] | Ch23 | MT | parmaklarının tadı kaçtı ve bunu anlamak için çok yaşlısın dedim | 'it's gone out of your fingers and you're too old to know it' | o hüner parmaklarından gitti, sen de bunu fark edemeyecek kadar yaşlısın dedim |
| 676 | [1793] | Ch23 | DLG | — Gret — dedi. Sadece bu | closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier) | — Gret, dedi. Sadece bu |
| 677 | [1797] | Ch23 | MT | — Senin böyle bir şey yapacağını… — | 'I didn't think you'd…' | — Hiç düşünmemiştim ki sen… — |
| 678 | [1799] | Ch23 | DLG | — Turta hâlâ benimdi — dedi. | closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier) | — Turta hâlâ benimdi, dedi. |
| 679 | [1801] | Ch23 | MT | omuzlarını düzeltmeye başladı | 'began to preen her shoulder' | omzundaki tüyleri düzeltmeye başladı |
| 680 | [1803] | Ch23 | DLG | hiçbir zaman ellerim olmadı — dedi Greta. — | closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier); resumed speech after a plain attribution takes no new dash (dossier) | hiçbir zaman ellerim olmadı, dedi Greta. Sorun |
| 681 | [1803] | Ch23 | DLG | — dedi Greta. — Sorun sendin. — | closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier); resumed speech after a plain attribution takes no new dash (dossier) | olmadı, dedi Greta. Sorun sendin. — |
| 682 | [1809] | Ch23 | MT | bir kimyager eşleşmesi, bir devlet kaydı, | 'a chemist's match, a state registry' | bir kimyasal eşleşme, eyalet sicil kaydı, |
| 683 | [1809] | Ch23 | DLG | ihtiyacınız olacak, Bayan Wendt — dedi, kabalık etmeden. | closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier); resumed speech after a plain attribution takes no new dash (dossier) | ihtiyacınız olacak, Bayan Wendt, dedi, kabalık etmeden. |
| 684 | [1809] | Ch23 | DLG | dedi, kabalık etmeden. — Bu sizin hakkınız | closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier); resumed speech after a plain attribution takes no new dash (dossier) | dedi, kabalık etmeden. Bu sizin hakkınız |
| 685 | [1813] | Ch23 | DLG | — Şimdilik. Gitmeden önce — dedi Tanaka, — | attribution rebuilt; closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier) | — Şimdilik. Gitmeden önce, dedi Tanaka, Greta’nın |
| 686 | [1813] | Ch23 | DLG | — dedi Tanaka, — Greta’nın kilidinin anahtarını | attribution rebuilt; closing dash before attribution (Spanish-raya style) → Turkish comma + attribution (dossier) | önce, dedi Tanaka, Greta’nın kilidinin anahtarını |
| 687 | [1821] | Ch23 | TERM | Su ısıtıcısı tam o sırada kaynama noktasına ulaştı ve köşede buhar çıkardı. Tanaka kalkıp ısıtıcıyı ocaktan aldı. | kettle = çaydanlık | Çaydanlık tam o sırada kaynadı ve köşede buhar saldı. Tanaka kalkıp çaydanlığı ocaktan aldı. |
| 688 | [1834] | Ch24 | TERM | Tanaka, defterini kurutma kağıdının üzerinde açarak, — İki suçlama | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | — İki suçlama |
| 689 | [1834] | Ch24 | TERM | İki suçlama var, dedi. Suç kastıyla mala | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | İki suçlama var, dedi Tanaka, defterini kurutma |
| 690 | [1834] | Ch24 | TERM | suçlama var, dedi. Suç kastıyla mala zarar | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | suçlama var, dedi Tanaka, defterini kurutma kâğıdının |
| 691 | [1834] | Ch24 | TERM | var, dedi. Suç kastıyla mala zarar verme. | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | var, dedi Tanaka, defterini kurutma kâğıdının üzerinde açarak. Kasıtlı mala zarar verme. |
| 692 | [1834] | Ch24 | TERM | Greta’nın hamurunun dört partisinin mahvolmasına yol açan | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | Greta’nın hamurunun dört partisini mahvetmek için una |
| 693 | [1834] | Ch24 | TERM | hamurunun dört partisinin mahvolmasına yol açan ekşi | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | hamurunun dört partisini mahvetmek için una kattığı |
| 694 | [1834] | Ch24 | TERM | dört partisinin mahvolmasına yol açan ekşi maya. | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | dört partisini mahvetmek için una kattığı ekşitici |
| 695 | [1834] | Ch24 | TERM | partisinin mahvolmasına yol açan ekşi maya. Pencere | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | partisini mahvetmek için una kattığı ekşitici baz. |
| 696 | [1834] | Ch24 | TERM | mahvolmasına yol açan ekşi maya. Pencere de | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | mahvetmek için una kattığı ekşitici baz. Pencere |
| 697 | [1834] | Ch24 | TERM | yol açan ekşi maya. Pencere de bununla | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | için una kattığı ekşitici baz. Pencere de bunun |
| 698 | [1834] | Ch24 | TERM | maya. Pencere de bununla birlikte aradan çıkarılıyor. | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | baz. Pencere de bunun içine giriyor. — |
| 699 | [1834] | Ch24 | TERM | Pencere de bununla birlikte aradan çıkarılıyor. — | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | Pencere de bunun içine giriyor. — Tuğlayı |
| 700 | [1834] | Ch24 | TERM | de bununla birlikte aradan çıkarılıyor. — Kırık tuğlayı | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | de bunun içine giriyor. — Tuğlayı pazar |
| 701 | [1834] | Ch24 | TERM | aradan çıkarılıyor. — Kırık tuğlayı pazar günü Sugarplum’ın | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | içine giriyor. — Tuğlayı pazar günü Greta’nın |
| 702 | [1834] | Ch24 | TERM | tuğlayı pazar günü Sugarplum’ın arkasındaki çöp | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | Tuğlayı pazar günü Greta’nın arka odasındaki raftan alıp ara sokaktan kendisi taşımış ve Sugarplum’ın arkasındaki çöp |
| 703 | [1834] | Ch24 | TERM | Sugarplum’ın arkasındaki çöp konteynerinin dibinde hâlâ duran molozların | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | Sugarplum’ın arkasındaki çöp konteynerinde hâlâ yığılı duran |
| 704 | [1834] | Ch24 | TERM | konteynerinin dibinde hâlâ duran molozların üzerine | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | çöp konteynerinde hâlâ yığılı duran molozlarla yan |
| 705 | [1834] | Ch24 | TERM | dibinde hâlâ duran molozların üzerine kendisi taşıyıp | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | hâlâ yığılı duran molozlarla yan yana koymuştu. |
| 706 | [1834] | Ch24 | TERM | hâlâ duran molozların üzerine kendisi taşıyıp götürmüş | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | yığılı duran molozlarla yan yana koymuştu. |
| 707 | [1834] | Ch24 | TERM | duran molozların üzerine kendisi taşıyıp götürmüş ve | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | duran molozlarla yan yana koymuştu. |
| 708 | [1834] | Ch24 | TERM | molozların üzerine kendisi taşıyıp götürmüş ve oradaki kalıntılara dayamıştı. | attribution rebuilt; sour base (MT 'sour yeast'); 'from Greta's back-room shelf' dropped; 'held it against the rubble' | molozlarla yan yana koymuştu. |
| 709 | [1834] | Ch24 | MT | — Sprey boya ona ait değil. Onu sprey kutusu taşıyan ve daha küçük bir mesele olan çocuklar yapmış. | garbled: 'That's boys with a spray can, and it's a smaller matter' | — Boya onun işi değil. O, sprey kutulu oğlanların işi ve daha küçük bir mesele. |
| 710 | [1838] | Ch24 | TERM | Soğuk hava odası ile Hobart evyesine dair daktiloyla yazılıp kontluğa gönderilen, Alan Varney tertemiz bir mutfağı kapatsın diye verilen dilekçe. | CLUE wording; 'county' (MT 'kontluk' = earldom) | "Soğuk oda" ile "Hobart lavabosu"; daktiloyla yazılıp Alan Varney tertemiz bir mutfağı kapatsın diye ilçeye gönderilmiş. |
| 711 | [1842] | Ch24 | MT | bölge mahkemesinde | 'county court' | ilçe mahkemesinde |
| 712 | [1846] | Ch24 | REG | Makbuzlarını bulup hazırlamasını söyleyin. | Noriko ↔ Jessica sen (first names) | Makbuzlarını bulup hazırlamasını söyle. |
| 713 | [1852] | Ch24 | DLG | Tanaka, — İşin bir de diğer yüzü var, dedi. Wendt’in toptan ekmek satmak için devletten alınmış bir lisansı var. | attribution rebuilt; 'a state license' | — İşin bir de öbür yüzü var, dedi Tanaka. Wendt's'in toptan ekmek satmak için eyaletten aldığı bir ruhsatı var. |
| 714 | [1856] | Ch24 | TERM | Ekşi maya da bir gıdadır zaten. | sour base | Ekşitici baz da bir gıdadır zaten. |
| 715 | [1856] | Ch24 | MT | onlar da siparişi askıya almışlar. Müfettiş, minibüse yükleme bitmeden iki hanın şoförünü aradığını söyledi. | 'suspended the account'; 'two inns rang her driver' | o da hesabı askıya almış. Müfettiş, şoför minibüsü yüklemeyi bitirmeden iki otelin onu aradığını söyledi. |
| 716 | [1860] | Ch24 | DLG | Tanaka ona, — Teşekkür ederim, diyerek atacı cebine attı. | attribution rebuilt | — Teşekkür ederim, dedi Tanaka ona ve atacı cebine koydu. |
| 717 | [1864] | Ch24 | MT | penceresindeki sarı bölge idaresi ilanı | 'the county's yellow notice' | penceresindeki ilçenin sarı ilanı |
| 718 | [1868] | Ch24 | TERM | cuma günü kapıya astığım altın kurdeleli balsam çelenginin altında bekledi. Basamağın yanındaki taşın içine gömülmüş pirinçten bir çizmepaspas vardı, | balsam = köknar; gold bow; boot-scraper | cuma günü kapıya astığım altın fiyonklu köknar çelenginin altında bekledi. Basamağın yanındaki taşa gömülmüş pirinçten bir çamur sıyırıcı vardı, |
| 719 | [1880] | Ch24 | MT | Bunu sindirmesine izin verdim. Arkasında çırak, tepsideki finansiyer kurabiyelerini birbirine bakmadan teker teker vitrinine yerleştiriyordu. | 'She let it sit'; 'not looking at either of us' | Sözlerimin bir an havada kalmasına izin verdi. Arkasında çırak, tepsideki financier’leri ikimize de bakmadan teker teker vitrine yerleştiriyordu. |
| 720 | [1882] | Ch24 | DLG | Renée, — Evet, dedi. Haksızdınız. | attribution rebuilt; 'You were wrong' | — Evet, dedi Renée. Yanılmıştınız. |
| 721 | [1886] | Ch24 | MT | tuğla çöplüğümden bilerek alınmış | 'my dumpster' | tuğla çöp konteynerimden bilerek alınmış |
| 722 | [1892] | Ch24 | MT | Kilise çay toplantılarından kadınlar | 'Women from the church suppers' | Kilise yemeklerinden tanıdığım kadınlar |
| 723 | [1892] | Ch24 | TERM | Pip çizmepaspasa bir kez daha | boot-scraper | Pip çamur sıyırıcıya bir kez daha |
| 724 | [1896] | Ch24 | MT | şekil vermekte olduğu bir kızak kundağının yanındaki sehpaya da bir bardak çay koymuştu. Pip, kendisini bekleyen bir tabak çinekopun durduğu kesmetaş ocağa | 'a sleigh runner'; 'on the bench'; 'a pot of tea'; 'sprats'; 'fieldstone hearth' | şekil vermekte olduğu bir kızak ayağının yanına, tezgâha da bir demlik çay koymuştu. Pip, kendisini bekleyen bir tabak çaça balığının durduğu tarla taşından ocağa |
| 725 | [1902] | Ch24 | MT | Joyce ise en sonda, artık hiçbir şeyi değiştiremeyecek durumdayken işin içine biraz dahil olmuştu. | 'Joyce got there at the very end, a little' | Joyce ise ancak en sonda, hiçbir şeyi değiştiremeyeceği bir anda, azıcık kabullendi. |
| 726 | [1902] | Ch24 | MT | Hanlar da öyle. | 'The inns too' | Oteller de öyle. |
| 727 | [1910] | Ch24 | MT | Sönmüş ızgaranın üzerinde dans eden sarı alevleri izledim. | 'the gold turn over the empty grate' (the magic, not flames) | Boş ızgaranın üzerinde dönen altın ışıltıyı izledim. |
| 728 | [1912] | Ch24 | MT | Nick kundağı ellerinde | 'the runner' | Nick kızak ayağını ellerinde |
| 729 | [1918] | Ch24 | TYPO | Pip çinekopları bitirip boş tabağı gagasınyla | sprats; typo | Pip çaça balıklarını bitirip boş tabağı gagasıyla |
| 730 | [1918] | Ch24 | MT | Rendenin kızak tahtası üzerinde | 'the runner' | Rendenin kızak ayağı üzerinde |
| 731 | [1918] | Ch24 | TYPO | soluk renkli rontolar halinde | non-word 'rontolar' | soluk renkli talaş kıvrımları hâlinde |
| 732 | [1921] | Ch25 | MT | Ve bu kez buraya bir şeyler vermeye gelmişti. | 'to give something back' | Ve bu kez bir şeyi geri vermeye gelmişti. |
| 733 | [1923] | Ch25 | MT | düğümleri düğüm çözer gibi çözmüştü | 'unwound it knot by knot' | düğüm düğüm çözmüştü |
| 734 | [1923] | Ch25 | TERM | Evyenin yedek parçası | the sink part (lavabo, as Ch9) | Lavabonun parçası |
| 735 | [1925] | Ch25 | TYPO | Mutfaktınız | typo | Mutfağınız |
| 736 | [1925] | Ch25 | MT | Tamir edilmiş dosyasının üzerine | 'her mended case' (display case, not a file) | Onarılmış vitrinin üzerine |
| 737 | [1927] | Ch25 | MT | Sonra dosyasının altından uzanıp | 'under her case' | Sonra vitrinin altından uzanıp |
| 738 | [1931] | Ch25 | TYPO | Bridgeton'dan Joyce Wendt'ti | place name | Bridgton'dan Joyce Wendt'ti |
| 739 | [1935] | Ch25 | MT | Kakolu çörekler yarım saatte bitmişti. | 'gone by half past' (two); typo 'Kakolu' | Kakaolu çörekler iki buçukta bitmişti. |
| 740 | [1935] | Ch25 | TERM | tarçınlı rulo hamuru yoğurmaya başladı | cinnamon rolls = tarçınlı çörek (Ch2) | tarçınlı çörek hamuru yoğurmaya başladı |
| 741 | [1941] | Ch25 | DLG | Martha bir düzine kakolu çörek satın aldı. Sırada bekleyenlerden soran olmamasına rağmen, — Emma'nın sınıfı için, dedi. | attribution rebuilt; typo | Martha bir düzine kakaolu çörek satın aldı. — Emma'nın sınıfı için, dedi kuyruktakilere, kimse sormadığı hâlde. |
| 742 | [1945] | Ch25 | MT | — Kutular için, dedi ve parasını düzgün bir deste halinde dosyanın üzerine bıraktı. | 'For the barrels'; 'on the case' | — Variller için, dedi ve parasını düzgün bir deste hâlinde vitrinin üzerine bıraktı. |
| 743 | [1947] | Ch25 | TYPO | Bridgeton'a | place name | Bridgton'a |
| 744 | [1955] | Ch25 | DLG | Ferris çocuğu yere bakarak, — Özür dileriz, dedi. | attribution rebuilt | — Özür dileriz, dedi Ferris çocuğu yere bakarak. |
| 745 | [1957] | Ch25 | MT | Ardından her birine birer kakolu çörek verdi. — Noel'e kadar ön merdivenimi küreklersiniz, dedi. | 'shovel my front step'; typo | Ardından her birine birer kakaolu çörek verdi. — Noel'e kadar ön basamağımın karını siz küreyeceksiniz, dedi. |
| 746 | [1963] | Ch25 | DLG | Arkasındaki adamlardan biri, — Şey, Pete, o yükleme rampası hakkında… diye lafa başlayacak olduğunda | speech inside narration → quotation marks | Arkasındaki adamlardan biri "Şey, Pete, o yükleme rampası hakkında…" diye lafa başlayacak olduğunda |
| 747 | [1969] | Ch25 | MT | elindeki sarı kağıt tezgahta dururken | 'with the yellow paper sitting on her case' | sarı kâğıt tezgâhında dururken |
| 748 | [1969] | Ch25 | MT | mahvolduğu miktar neyse kuruşu kuruşuna ödeniyor | 'dollar for dollar of what she spoiled' | onun mahvettiğinin dolarına dolarına karşılığı |
| 749 | [1969] | Ch25 | MT | kimse de buna hayır demedi. Pazartesi dediler. | 'nobody called it charity. They called it Monday.' | kimse de buna sadaka demedi. Pazartesi dediler. |
| 750 | [1969] | Ch25 | TERM | — Hatta kendisinin yenilerini yoğurmaya başladığı tarçınlı rulolar için soğukta hala kuyrukta bekleyenleri buharlı camdan dışarı bakarak süzdü. | cinnamon rolls; garbled | — Şimdiden yenisini yoğurmaya başladığı tarçınlı çörekler için soğukta hâlâ kuyrukta bekleyenlere buğulu camdan baktı. |
| 751 | [1971] | Ch25 | TERM | Listede seni iki çikolatalı-cevizli ile bir düzine ruloyla kaydetmişim | Martha's order — identical to Ch14/Ch20 | Listede seni iki çikolatalı-cevizli turta ve bir düzine çörekle kaydetmişim |
| 752 | [1979] | Ch25 | MT | Pencereler fırın ışığıyla altın sarısı parlıyor, buhardan görünmez haldeki içerideki kuyruk hala sıcacığını koruyordu. | garbled | Pencereler fırın ışığıyla altın sarısıydı, buğulanmıştı; kuyruk hâlâ içeride, sıcaktaydı. |
| 753 | [1988] | Ch26 | TERM | Derneği ertesi gün kurtardık, | Society = Cemiyet | Cemiyeti ertesi gün kurtardık, |
| 754 | [1990] | Ch26 | NM | Haftalar önce Sn. Worthington | Mr. = Bay (as elsewhere) | Haftalar önce Bay Worthington |
| 755 | [1990] | Ch26 | TERM | ilk kızaklar ve el arabaları bulvar boyunca | avenue = cadde | ilk kızaklar ve el arabaları cadde boyunca |
| 756 | [1990] | Ch26 | TERM | arabaları cadde boyunca Derneğin yeşil kapısına doğru | Society = Cemiyet | arabaları cadde boyunca Cemiyetin yeşil kapısına doğru |
| 757 | [1994] | Ch26 | TERM | Bulvara tıpkı Hal'in varilleri için geldiğimiz gibi çıktık | avenue = cadde | Caddeden tıpkı Hal'in varilleri için geldiğimiz gibi yukarı çıktık |
| 758 | [1998] | Ch26 | TERM | Bulvarın alt ucundaki herkes | avenue = cadde | Caddenin alt ucundaki herkes |
| 759 | [1998] | Ch26 | TYPO | hem çatından aşağıya | typo | hem çatıdan aşağıya |
| 760 | [2006] | Ch26 | EN | yeni kaplamalar ve yeni shingle'larla örtülmüş | English 'shingle' left in | yeni kaplama tahtaları ve yeni kiremitlerle örtülmüş |
| 761 | [2008] | Ch26 | MT | İş için gereken dirsekleri | 'the brackets' | İş için gereken destekleri |
| 762 | [2014] | Ch26 | TERM | yemek kampanyası başladığından beri | food drive | gıda kampanyası başladığından beri |
| 763 | [2014] | Ch26 | TERM | Kadınlar grubu bir piyango düzenlemişti. | 'The circle' = çember | Çember bir piyango düzenlemişti. |
| 764 | [2020] | Ch26 | EN | O sırada Theo kollarını shingle'la doldurmuş merdivendeyken, orada kalmasına ses çıkarmadım. | English 'shingle' left in | O sırada Theo kucak dolusu kiremitle merdivendeydi; orada kalmasına ses çıkarmadım. |
| 765 | [2028] | Ch26 | EN | Buz tutmuş merdivenden yukarı shingle taşıdı | English 'shingle' | Buz tutmuş merdivenden yukarı kiremit taşıdı |
| 766 | [2028] | Ch26 | MT | dizlerinin üzerinde yaptığı düzeltme işini | 'the blotting-work' | dizlerinin üzerinde yaptığı kurutma işini |
| 767 | [2028] | Ch26 | EN | Ama shingle taşımasına izin vermişlerdi | English 'shingle' | Ama kiremit taşımasına izin vermişlerdi |
| 768 | [2040] | Ch26 | TERM | sırayla yeşillik üzerinde duruyor | the green = meydan | sıra sıra meydanda duruyor |
| 769 | [2040] | Ch26 | TERM | duruyor, kömürden gözleriyle Derneğe bakıyorlardı. | Society = Cemiyet | duruyor, kömürden gözleriyle Cemiyete bakıyorlardı. |
| 770 | [2046] | Ch26 | TERM | Dernek kapılarını bütün kasabaya | Society = Cemiyet | Cemiyet kapılarını bütün kasabaya |
| 771 | [2068] | Ch26 | OM | Kadınlar grubu, kurutulmuş balsam ve orman meyvesinden sarıp hazırladığımız küçük bir çelengi içeri bıraktı. | 'The circle'; balsam = köknar; 'the same green we'd hung in every window' dropped | Çember, kurutulmuş köknar ve orman meyvesinden sarıp hazırladığımız küçük bir çelengi içeri bıraktı; her pencereye astığımız yeşilin aynısı. |
| 772 | [2076] | Ch26 | MT | büyüttüğü elinden iki yıl daha küçük bir el için | 'a hand two years smaller than the hand she'd grown' | şimdiki elinden iki yaş küçük bir el için |
| 773 | [2078] | Ch26 | MT | — Artık olmuyor, dedi | 'It doesn't fit anymore' | — Artık elime olmuyor, dedi |
| 774 | [2078] | Ch26 | MT | ardından Martha'nın paltosunun arkasına doğru bir adım atıp geri çekildi. | 'stepped back into Martha's coat' | ardından geri çekilip Martha'nın paltosuna sokuldu. |
| 775 | [2084] | Ch26 | TERM | tek bir pirinç raptiyeyi kutunun içine bıraktı | brad = çivi (Ch6) | tek bir pirinç çiviyi kutunun içine bıraktı |
| 776 | [2084] | Ch26 | MT | aynı küçük parça eşliğinde ayakta tutuyor olacak | 'with the same small pieces' | aynı küçük parçalarla ayakta tutuyor olacak |
| 777 | [2084] | Ch26 | TERM | yıl sonra biri Dernek binasını aynı küçük | Society = Cemiyet | yıl sonra biri Cemiyet binasını aynı küçük |
| 778 | [2088] | Ch26 | MT | diğer tarafta Eliza Frost'un kahverengi eli vardı | 'Eliza Frost's brown hand' (handwriting) | diğer tarafta Eliza Frost'un kahverengileşmiş el yazısı vardı |
| 779 | [2090] | Ch26 | TERM | — Not düşülsün ki Frost Falls güçlüler tarafından kurulmamıştır. Komşumsu olanlar tarafından kurulmuştur. | founder's line — now identical to Ch6 [591]/[617] (MT 'Komşumsu' non-word) | — Biline ki Frost Falls güçlüler tarafından kurulmadı. Komşulukla kuruldu. |
| 780 | [2092] | Ch26 | TERM | kutunun içine konulmadı. Derneğin koleksiyonuna aitti. | Society = Cemiyet | kutunun içine konulmadı. Cemiyetin koleksiyonuna aitti. |
| 781 | [2106] | Ch26 | TERM | Onu eldivenlerin ve raptiyenin arasına bıraktı. | brad = çivi | Onu eldivenlerin ve çivinin arasına bıraktı. |
| 782 | [2110] | Ch26 | MT | Dışarıda, bulvardaki her kardan adam yeşillik boyunca ve yürüyüş yolu boyunca sıralanmıştı; aydınlık pencerelere dönmüşlerdi, çocukların bir avuç dolusu yaptığı düzinelerce kardan adam oradaydı. | 'dozens of them where the children had built a handful'; avenue/green terms | Dışarıda, caddedeki her kardan adam meydan boyunca ve kaldırım boyunca sıralanmıştı; aydınlık pencerelere dönmüşlerdi; çocukların topu topu birkaç tane yaptığı yerde şimdi düzinelercesi vardı. |
| 783 | [2117] | Ch27 | TERM | Çelenk halkası için yapılan daimi siparişi almak üzere | 'the wreath-circle's standing order' (circle = çember) | Çelenk çemberinin daimi siparişini almak üzere |
| 784 | [2119] | Ch27 | TYPO | paltolarının düğmelerini paketlerinin üstünde ilgeleyen | typo 'ilgeleyen' | paketlerinin üstüne paltolarını ilikleyen |
| 785 | [2121] | Ch27 | DLG | Greta başını kaldırmadan, tepsiyi fırına sürüp kapağını kalçasıyla kapatarak, — Erken geldin, dedi. Çelenk siparişi kutulanmadı. | attribution rebuilt | — Erken geldin, dedi Greta başını kaldırmadan, tepsiyi fırına sürüp kapağını kalçasıyla kapatırken. — Çelenk siparişi daha kutulanmadı. |
| 786 | [2129] | Ch27 | MT | doğruca başkana götürdüm | 'the chief' (police), not 'the mayor/president' | doğruca şefe götürdüm |
| 787 | [2131] | Ch27 | TYPO | çizgili birkâğıt | typo | çizgili bir kâğıt |
| 788 | [2135] | Ch27 | MT | Başkanın ofisinde sana ellerinin olduğuna inanacağını sanmadığımı söylemeye başladım. | 'the chief's office'; 'you'd believe it was your hands' | Şefin odasında sana, suçun ellerinde olduğuna inanacağını düşünmediğimi söylemeye başladım. |
| 789 | [2136] | Ch27 | TERM | Pastaya gelince. Yirmi beş yıldır kendime bunun benimki olduğuna inandırdım. Annemin pekan cevizleri, | pie = turta; grammar | Turtaya gelince. Yirmi beş yıldır kendimi onun benim olduğuna inandırdım. Annemin cevizleri, |
| 790 | [2145] | Ch27 | TERM | — Bir pastayla cevap ver, dedim. | pie = turta | — Bir turtayla cevap ver, dedim. |
| 791 | [2149] | Ch27 | TERM | Ama pastanın senin olduğunu söylemek için yazmış. | pie = turta | Ama turtanın senin olduğunu söylemek için yazmış. |
| 792 | [2155] | Ch27 | MT | kendisine kıdem tazminatı borçlu olduğunu | 'back-pay' (not severance) | kendisine birikmiş maaş borçlu olduğunu |
| 793 | [2161] | Ch27 | TYPO | ve sakın sağırlık edip sağlık müfettişine | garbled 'sağırlık edip' | ve sakın sağlık müfettişine |
| 794 | [2173] | Ch27 | TERM | başka bir tel zımbayı daha yavaşça çıkarıyordu | brad = çivi | başka bir çiviyi daha yavaşça çıkarıyordu |
| 795 | [2179] | Ch27 | EN | — Mrs. Claus! Pip bir hırsız yakaladı, diye duyurdu Emma, sanki oradaymışım gibi nefes nefese. — Gerçek bir tane. Miss Bennett gazeteye yazmış | English 'Mrs.'/'Miss'; REVERSED 'as though I might not have been there' | — Bayan Claus! Pip bir hırsız yakaladı, diye duyurdu Emma nefes nefese, sanki ben orada değilmişim gibi. — Gerçek bir tane. Bayan Bennett gazeteye yazmış |
| 796 | [2189] | Ch27 | MT | ve provadan önce midene sıcak bir kakaonun indirilmesi iyi olur | garbled | ve provadan önce sıcak bir kakao içsen iyi olur |
| 797 | [2195] | Ch27 | MT | soğuk mangalın önünde | 'the cold grate' | soğuk ızgaranın önünde |
| 798 | [2199] | Ch27 | MT | yuvarlak saha taşlarının | 'fieldstones' | yuvarlak tarla taşlarının |
| 799 | [2203] | Ch27 | TERM | Cemiyet’teki kutuların ve yeşillikteki kardan adamların | the green = meydan | Cemiyet’teki kutuların ve meydandaki kardan adamların |
| 800 | [2213] | Back | TERM | büyütecinden başka her şeyini kaybetti | dossier lock: loupe stays 'loupe' | loupe'u dışında her şeyini kaybetti |
| 801 | [2214] | Back | MT | kasabasına adını veren kadim çam ağaçlarına inat ressamları kıskandıracak kadar kusursuz Pinecrest kasabasında | MT interpolation; EN 'the picture-perfect town of Pinecrest' | kartpostal gibi kusursuz Pinecrest kasabasında |
| 802 | [2216] | Back | TERM | Açıklayamadığı ve kanıtlayamadığı bir hediyeyle | dossier lock: the gift = yetenek (not hediye) | Açıklayamadığı ve kanıtlayamadığı bir yetenekle |
| 803 | [2222] | Back | MT | bir son düşünceymiş gibi kıvrılıyordu | 'like an afterthought' | sonradan akla gelmiş bir şey gibi kıvrılıyordu |
| 804 | [2224] | Back | MT | tatlı ve floral, nereye koyamadığım bir şey | 'I couldn't place' | tatlı ve çiçeksi, adını koyamadığım bir şey |
| 805 | [2224] | Back | MT | Ta ki olamayana dek. | 'Until I wasn't' | Ta ki olmadığım güne dek. |
| 806 | [2226] | Back | DLG | Alışılmış, cenazeye mahsus bir sempatiyle yumuşak bir ses tonuyla, — Maeve bunu senin almanı istedi, dedi. Sizinle çok gurur duyuyordu Fiona. Şehir gazetelerindeki kariyerini her zaman takip etti. | attribution rebuilt; the lawyer addresses her as siz (MT mixed sen/siz) | — Maeve bunu sizin almanızı istedi, dedi; sesi alışılmış, cenazeye yakışır bir şefkatle yumuşaktı. — Sizinle çok gurur duyuyordu, Fiona. Şehir gazetelerindeki kariyerinizi hep takip etti. |
| 807 | [2227] | Back | DLG | Düz, nötr bir sesle, — Bunu söylediğiniz için naziksiniz, dedim. | attribution rebuilt | — Bunu söylemeniz çok nazik, dedim düz, nötr bir sesle. |
| 808 | [2228] | Back | REG | Hepsi senin. Temiz ve net. | lawyer → siz; 'Free and clear' | Hepsi sizin. Hiçbir yükü olmadan. |
| 809 | [2231] | Back | NM | Flanagan’ın İnce Ciltleme & Restorasyon dükkânı | dossier: business names stay as written | Flanagan's Fine Binding & Restoration |
| 810 | [2231] | Back | MT | büyük panjurlu pencerede | 'the large picture window' | büyük vitrin camında |
| 811 | [2233] | Back | MT | Solgun, temiz ve floral. | 'Faint, clean, and floral' | Hafif, temiz ve çiçeksi. |
| 812 | [2236] | Back | TERM | kemik katlayıcılar, bızlar, bıçaklar gibi | dossier: awl = biz (MT 'bızlar' misspelt); 'paring knives' | kemik katlayıcılar, ciltçi bizleri, sıyırma bıçakları gibi |
| 813 | [2240] | Back | MT | bir kafeterya vardı | 'a coffee shop' | bir kahve dükkânı vardı |
| 814 | [2245] | Back | TYPO | Ben durgun ve kontrollüleyken | typo | Ben durgun ve kontrollüyken |
| 815 | [2245] | Back | EN | parlak teal mavisi bir kanto | English 'teal'; typo 'kanto' | parlak petrol mavisi bir palto |
| 816 | [2246] | Back | DLG | Sıcak, taşkın bir aceleyle, — Buradasın! diye haykırdı. Arabayı gördüm! | attribution rebuilt | — Buradasın! diye haykırdı sıcak, taşkın bir telaşla. — Arabayı gördüm! |
| 817 | [2247] | Back | DLG | Gergin bir sesle, — Öyleyim, dedim. Ve sen kimsin? | attribution rebuilt; Fiona keeps her distance (later 'Ms. Donovan') → siz | — Öyleyim, dedim gergin bir sesle. Ya siz kimsiniz? |
| 818 | [2248] | Back | MT | Büyük halanla biz bir elmanın iki yarısıydık. | 'thick as thieves' | Büyük halanla can ciğer kuzu sarmasıydık. |
| 819 | [2249] | Back | TYPO | sıcak tı. | typo | sıcaktı. |
| 820 | [2250] | Back | DLG | Gözleri odaya huşu dolu bir ifadeyle tararken devam etti, — Seninle sonunda tanışmak inanılmaz. | attribution rebuilt | — Seninle sonunda tanışmak inanılmaz, diye devam etti, gözleri huşu dolu bir ifadeyle dükkânı tararken. — |
| 821 | [2251] | Back | DLG | Sözcük amaçladığımdan daha sert çıkarak, — Dağınık… dedim. | attribution rebuilt | — Burası… dağınık, dedim; kelime ağzımdan istediğimden sert çıkmıştı. |
| 822 | [2257] | Back | DLG | Telefonumla belirsiz bir hareket yaparak, — Bir sistemim var, dedim. | attribution rebuilt | — Bir sistemim var, dedim, telefonumla belli belirsiz bir hareket yaparak. |
| 823 | [2259] | Back | MT | Göz kırptım. | 'I blinked' (not winked) | Gözlerimi kırpıştırdım. |
| 824 | [2260] | Back | DLG | Sanki dünyadaki en aşikar şeymiş gibi, — Ay Işığı Maskeli Balo’suna! dedi. | attribution rebuilt | — Ay Işığı Maskeli Balosu’na! dedi, sanki dünyanın en bariz şeyiymiş gibi. |
| 825 | [2261] | Back | MT | Elimle odanın etrafında, kâğıt ve deri yığınlarında dolandım. | 'I swept a hand around the room' | Elimle odayı, sallanan kâğıt ve deri yığınlarını gösterdim. |
| 826 | [2262] | Back | DLG | Tavi umursamaz bir el hareketi yaparak, — Aman, bu eski toz yığını bir gece bekleyebilir, dedi. Hiçbir yere gitmiyor. Aydır seni bekliyor. | attribution rebuilt; 'for months' | — Aman, bu eski toz yığını bir gece bekleyebilir, dedi Tavi elini umursamazca sallayarak. Hiçbir yere gitmiyor. Aylardır seni bekliyor. |
| 827 | [2262] | Back | MT | Araziyi öğren. | 'Get the lay of the land' | Ortamı tanı. |
| 828 | [2263] | Back | DLG | Sabrım tükenerek, — Araziyi öğrenmeye çalışmıyorum, dedim. | attribution rebuilt | — Ortamı tanımaya çalışmıyorum, dedim, sabrım tükenirken. |
| 829 | [2264] | Back | DLG | Tavi otomatik olarak düzeltti, — Tavi. | attribution rebuilt | — Tavi, diye düzeltti otomatik olarak. |
| 830 | [2264] | Back | MT | Cemiyet’le uygulayıcılar olarak başa çıkmalısın. | 'deal with the Society as executors' | Vasiyeti yürüten taraf olarak Cemiyet’le muhatap olacaksın. |
| 831 | [2266] | Back | DLG | Umutsuz, son bir saman çöpüne sarılarak, — Maskeli balo için giyecek hiçbir şeyim yok, dedim. | attribution rebuilt | — Maskeli… balo için giyecek hiçbir şeyim yok, dedim, son bir umutla bir saman çöpüne tutunarak. |
| 832 | [2267] | Back | MT | Maeve’in eski seyahat sandığında yukarıda bir koleksiyon maskesi vardı. | 'a whole collection of masks upstairs in her old steamer trunk' | Maeve’in yukarıdaki eski seyahat sandığında koca bir maske koleksiyonu var. |
| 833 | [2270] | Back | TYPO | Yedibuçukta | spacing | Yedi buçukta |
