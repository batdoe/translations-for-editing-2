# Flour Play - ASSEMBLED - FORMATTED_Czech — APPLIED (2026-10-27)

Output: `translated\corrected\Flour Play - ASSEMBLED - FORMATTED_Czech.docx`
Backup of the pre-proofread corrected copy (identical to the input): `translated\corrected\_bak\Flour Play - ASSEMBLED - FORMATTED_Czech.pre-proofread-20261027.docx`
Method: lxml, run-level edits of `<w:t>` nodes only. Each fix verified that the paragraph's COMPLETE current text equalled the expected text (input + earlier fixes in the same paragraph) and that the quoted span occurred exactly once; the edit was narrowed to the minimal changed span and refused if that span crossed runs with different formatting (6 such fixes were split per run and re-applied so italics stay where they were). No `set_para_text()`. Excerpt paragraphs rebuilt from the published edition's runs (text + italic/bold), base rPr cloned from each paragraph's original first run.

- Text fixes applied: 637 (refused: 0, not found: 0)
- Excerpt paragraphs replaced from the published *Knihařův odkaz*: 50 ([1323]–[1372] ← published ¶53–102)
- Stray `<bt>` removed: 11 (ruling 5); title anchors added: 4 ([0] title page, [9]–[11] series list, matching Book 1)
- Dialogue: the edition already used „…“ throughout (quote balance checked per paragraph: 0 unbalanced). 1 dialogue paragraph converted ([955] spoken line set as `*…*` → „…“); 2 interruptions → em dash ([1043], [1074]); 4 ellipses '...' → '…'.
- Paragraph [381] (stray 'Kapitola 3' inside Ch8) emptied, paragraph kept (count unchanged).
- Italic runs: 43 → 43; sequence differs ONLY where the italic text itself was translated/corrected in place: capsule card Ch15 [651] and Ch26 [1259] (made identical), flyer 'Týden velkého otevření' [659], Varney's quoted line [662], Doc's quoted words [676], Renée's echoed words [678], Joyce's letter [1273] [1274] [1275], sell lines [1313] [1321] (English → Czech).

## Checks on the corrected file
1. Untranslated English: `[]`
2. `bt_anchors.py check`: 9 spans, 0 unpaired; only Flour Play / Frost and Found / Inn Trouble / The Binder's Bequest (BB = a real title, kept per the Book-3 brief)
3. `check_matter.py`: OK, 1/1 clean
4. `preflight.py --verify`: paragraphs 2013 → 2013 ok; italic runs 43 → 43 ok (sequence differs only at the in-place translations listed above); scene breaks 60 → 60 ok; bt 16 → 9 = ruling-5 removals (−11) + Book-1 title anchors (+4) — reports FAIL by design of the check, which predates ruling 5.

## Applied (para · was → now · why)

| ¶ | was | now | why |
|---|---|---|---|
| 0 | `Moučné hrátky` | `<bt>Flour Play</bt>` | consistency: title page: Book 1 Czech carries the title anchor on its title page (stamped later with the catalogue Czech title); MT had its own invented title |
| 6 | `v jakékoli formě nebo jakýmkoli způsobem, včetně fotokopírování, záznamu či jiných elektronických nebo mechanických metod, bez předchozího písemného souhlasu vydavatele, s výjimkou případů povolených autorským zákonem USA.` | `v jakékoli formě či jakýmikoli prostředky, včetně fotokopírování, záznamu nebo jiných elektronických či mechanických metod, bez předchozího písemného souhlasu vydavatele, s výjimkou případů povolených autorským zákonem.` | consistency: ruling 7: rights paragraph matched to Book 1 Czech verbatim |
| 7 | `jsou zcela fiktivní. Jakákoli podoba se skutečnými osobami (žijícími či zesnulými), místy, budovami a výrobky` | `jsou čistě fiktivní. Jakákoli podoba se skutečnými osobami (žijícími či zesnulými), místy, budovami a produkty` | consistency: ruling 7: disclaimer matched to Book 1 Czech verbatim |
| 9 | `Frost and Found` | `<bt>Frost and Found</bt>` | consistency: title anchor: Book 1 Czech anchors its series list; restored so stamp localises the title |
| 10 | `Inn Trouble` | `<bt>Inn Trouble</bt>` | consistency: title anchor (as Book 1) |
| 11 | `Flour Play` | `<bt>Flour Play</bt>` | consistency: title anchor (as Book 1) |
| 21 | `Tohle nebyl výbuch vzteku. Tohle byl chladný kalkul.` | `Tohle nebyl výbuch vzteku. Tohle bylo řemeslo.` | mistranslation: EN 'That is not a temper. That is a trade.' — the clue is that the culprit is IN THE TRADE (a baker); 'cold calculation' loses it |
| 22 | `kdy bude v Holly Jolly zataženo` | `kdy bude Holly Jolly zavřené` | mistranslation: 'will be dark' = closed; 'zataženo' means overcast |
| 24 | `Každá žena v kruhu si přinesla vlastní jedli a já přinesla severopolský způsob jejího vázání,` | `Každá žena v kroužku si přinesla vlastní jedli a já přinesla způsob jejího vázání ze severního pólu,` | mistranslation: 'severopolský' = North-Polish; 'the North Pole's way'; circle = kroužek (Book 1) |
| 25 | `který začal o Hallowenu a měl ležet` | `který začal o Halloweenu a měl ležet` | typo: Halloween spelling |
| 25 | `a vydrží až do Díkůvzdání. Ulice po Hallowenu ztichla` | `a vydržely až do Díkůvzdání. Ulice po Halloweenu ztichla` | typo: tense (narrative past) + Halloween spelling |
| 32 | `Dot se zasmála svým krátkým, suchým smíchem z druhého konce kruhu,` | `Dot se zasmála svým krátkým, suchým smíchem z druhého konce kroužku,` | consistency: circle = kroužek (Book 1) |
| 32 | `„Ta tvojí fintě nadbíhá od dne, kdy jsi sem vkročila. Mně nadbíhala v roce osmdesát něco.“` | `„Jde po tvé fintě ode dne, kdy jsi sem vkročila. Po té mojí šla v roce devatenáct set osmdesát něco.“` | grammar: garbled ('tvojí fintě nadbíhá'); 'She's been after your trick… after mine in nineteen eighty-something' |
| 32 | `Nikdy se nezastavily a nikdy nezablbly.` | `Nikdy se nezastavily a nikdy nezaváhaly.` | register: 'nezablbly' is not a word in this sense; 'never fumbled' |
| 33 | `Celý kruh, když zrovna` | `Celý kroužek, když zrovna` | consistency: circle = kroužek |
| 34 | `nepatřila do kruhu,` | `nepatřila do kroužku,` | consistency: circle = kroužek |
| 34 | `v hnízdě, které si postarala uplést ze spadlého přadene červené vlny, jíž se Olivia, jak jsem si všimla, nepokoušela nijak zvlášť urputně získat zpět.` | `v hnízdě, které si postavila ze spadlého přadena červené vlny, o jehož navrácení se Olivia, jak jsem si všimla, nijak zvlášť urputně nesnažila.` | grammar: 'si postarala uplést' garbled ('she'd built'); relative clause ungrammatical; přadena |
| 37 | `„Nemá žádnou hrdost,“` | `„Ta se vůbec nestydí,“` | mistranslation: 'She's got no shame' — hrdost = pride |
| 38 | `„Má velké hrdosti dost,“ řekla jsem. „Jen si ji schovává pro příležitosti, kdy jí k něčemu bude.` | `„Stydět se umí až dost,“ řekla jsem. „Jen si to schovává pro příležitosti, kdy jí to k něčemu bude.` | mistranslation: garbled; 'She has a great deal of shame' |
| 39 | `mi došlo, jakou dálku jsem uvrhla, abych tu mohla sedět. Ne ty míle. Těch bylo opravdu hodně, ale nemyslela jsem tím míle. Ne tak dávno jsem byla v Frost Falls tou novou.` | `mi došlo, jakou dálku jsem urazila, abych tu mohla sedět. Ne ty kilometry. Těch bylo opravdu hodně, ale nemyslela jsem tím kilometry. Ne tak dávno jsem byla ve Frost Falls tou novou.` | units: 'uvrhla' wrong verb (urazila); figurative 'miles' → kilometry (safe, idiomatic); 've Frost Falls' |
| 41 | `„Ať nikdo nevstává,“ oznámila, což nejevilo sebemenší známky toho, že by se kdokoli chystal udělat.` | `„Ať nikdo nevstává,“ oznámila, ačkoli nikdo nejevil sebemenší známky, že by se k tomu chystal.` | grammar: garbled relative clause |
| 41 | `Greta vlastní Holly Jolly Bakery dole v ulici` | `Greta vlastnila Holly Jolly Bakery dole v ulici` | tense: narrative past (dossier lock) |
| 41 | `„Ne víc než před hodinou mi z trouby` | `„Ani ne před hodinou mi z trouby` | grammar: 'not one hour ago' |
| 49 | `jak už to v kruhu chodí,` | `jak už to v kroužku chodí,` | consistency: circle = kroužek |
| 52 | `To odvedlo pozornost kruhu od drátů.` | `To odvedlo pozornost kroužku od drátů.` | consistency: circle = kroužek |
| 56 | `který bych kruhu nedokázala pojmenovat` | `který bych kroužku nedokázala pojmenovat` | consistency: circle = kroužek |
| 60 | `Zelená plocha se rozprostírala naproti Yarn Tales, široký bílý parčík s válečným pomníkem` | `Náves se rozprostírala naproti Yarn Tales, široké bílé prostranství s válečným pomníkem` | consistency: the green = náves (Book 1 Czech, 35×) |
| 62 | `namířená pryč nahoru přes parčík k obchodům` | `namířená pryč nahoru přes náves k obchodům` | consistency: the green = náves |
| 67 | `Stačilo někomu přesunout obličej na druhou stranu,` | `Stačilo, aby někdo přesunul obličej na druhou stranu,` | grammar: ungrammatical |
| 68 | `A to byl ten rozumný pohled, kruh ho přijal a někdo prohlásil, že dnešní děti, a někdo jiný poznamenal, že za jeho mladých let takhle nikdy sníh nepadal, a hovor plynul dál, jak už to v kruhu bývá,` | `A to byl ten rozumný pohled, kroužek ho přijal a někdo prohlásil, že dnešní děti, a někdo jiný poznamenal, že za jejích mladých let takhle nikdy sníh nepadal, a hovor plynul dál, jak už to v kroužku bývá,` | gender: 'when I was a girl' — speaker is a woman (jejích); circle = kroužek |
| 69 | `Kouzlo se v Frost Falls utrhlo ze řetězu.` | `Kouzlo se ve Frost Falls utrhlo ze řetězu.` | grammar: ve Frost Falls |
| 69 | `Můj manžel ho stavěl.` | `Můj manžel mu jeden stavěl.` | mistranslation: 'My husband was building it one [a home]' — not building the magic |
| 69 | `Měnilo slavnostní světla z oranžových na zlatou. A teď, jak se zdálo, v noci procházelo dětského sněhuláka, aby čelil čemukoliv, co upoutalo jeho toulavou pozornost.` | `Měnilo slavnostní světla z oranžových na zlatá. A teď, jak se zdálo, v noci otáčelo dětského sněhuláka, aby se díval k čemukoli, co upoutalo jeho toulavou pozornost.` | mistranslation: garbled ('procházelo sněhuláka'); 'walking a snowman around… to face'; agreement |
| 71 | `Ale nic z toho jsem kruhu neřekla.` | `Ale nic z toho jsem kroužku neřekla.` | consistency: circle = kroužek |
| 71 | `Sníh zářil na parčíku` | `Sníh zářil na návsi` | consistency: the green = náves |
| 76 | `koho jsem v Frost Falls potkala` | `koho jsem ve Frost Falls potkala` | grammar: ve Frost Falls |
| 78 | `celá tucet` | `celý tucet` | grammar: agreement |
| 80 | `Chci, aby mi někdo jiný řekl, že neměknu v mozku.“` | `Chci, aby mi někdo jiný řekl, že mi nezměkl mozek.“` | grammar: garbled idiom 'going soft in the head' |
| 84 | `kde hnědoKůrkové, pohledné bochníky stále odpočívaly` | `kde hnědokůrkové, pohledné bochníky stále odpočívaly` | typo: capital K mid-word |
| 84 | `Celý den mé nejrušnější sezóny, Jessico. V pryč.“` | `Celý den mé nejrušnější sezóny, Jessico. Pryč.“` | typo: stray 'V' |
| 85 | `jen se otřásla a pak se tomu zasmála` | `jen sykla a pak se tomu zasmála` | mistranslation: 'wince' (otřásla = shuddered) |
| 87 | `Nechala to být, což mi prozradilo` | `Nechala mě, což mi prozradilo` | mistranslation: 'She let me' (not 'let it be') |
| 89 | `„Mé recepty se přece nezkazí,“ pronesla Greta do podlahy. „Tohle skořicové těsto jsem dělala deset tisíckrát, jestli vůbec jednou.` | `„Mé recepty nezklamou,“ pronesla Greta do podlahy. „Toho skořicového šneka jsem dělala snad desettisíckrát.` | mistranslation: literal idiom 'ten thousand times if I've made it once' read as doubt; 'don't fail' |
| 95 | `Jeden plech se mohl ošklivě povést na špatném ranním úsvitu kvůli uklouznuté ruce nebo chladnému průvanu.` | `Jeden plech se mohl za špatného rána nepovést kvůli uklouznuté ruce nebo chladnému průvanu.` | mistranslation: 'ošklivě povést' garbled; 'go wrong on a bad morning' |
| 101 | `a udělala krátké, pohoršené zatřesení. Couvala dva kroky přes dlaždice` | `a krátce a pohoršeně se otřepala. Couvla o dva kroky přes dlaždice` | grammar: calque; aspect |
| 101 | `kterým častovala sledě, jenž už to měl za sebou.` | `kterým častovala zkaženého sledě.` | mistranslation: 'a herring that had gone off' (not 'that had had it') |
| 103 | `Podívala se na obyčejnou světlou mouku a na tu svou tučňáčí společnici stojící v uctivé vzdálenosti s peřím nahoře.` | `Podívala jsem se na obyčejnou světlou mouku a na svou tučňačici stojící v uctivé vzdálenosti s naježeným peřím.` | grammar: first-person narrator dropped ('Podívala se'); 'feathers up' |
| 107 | `Uvnitř Greta otočila tabulkou na dveřích na ZAVŘENO` | `Uvnitř Greta otočila tabulku na dveřích na ZAVŘENO` | grammar: case |
| 109 | `Hnědý papír šel z oken starého Fenwicku dolů` | `Hnědý papír šel z oken starého Fenwickova domu dolů` | grammar: 'starého Fenwicku' — the place is 'Fenwickův dům' everywhere else |
| 109 | `že jde o nové pekařství <bt>Sugarplum Patisserie</bt>.` | `že jde o nové pekařství Sugarplum Patisserie.` | bt: ruling 5: shop name is not a book title |
| 110 | `a vtáhla mě dovnitř před chladem.` | `a vtáhla mě dovnitř z chladu.` | grammar: 'drew me in out of the cold' |
| 111 | `„Už jsi to viděla?“ řekla. Nebyla to otázka. „Za lékárnou. Už mají hotovou výlohu.“` | `„Už jsi to viděla,“ řekla. Nebyla to otázka. „Za lékárnou. Už mají nápis.“` | mistranslation: a question mark on a line the narration says was NOT a question; 'They've done the sign' |
| 113 | `Je v tom rozdíl, jak jsem sechala poučit, a předpokládám,` | `Je v tom rozdíl, jak jsem se nechala poučit, a předpokládám,` | typo: 'sechala' |
| 113 | `Řekla to lehce, ale usmát se odmítla.` | `Řekla to lehce, ale neusmála se.` | mistranslation: 'she didn't smile' (not 'refused to') |
| 115 | `které jsme vyráběly v <bt>Yarn Tales</bt>,` | `které jsme vyráběly v Yarn Tales,` | bt: ruling 5: shop name |
| 118 | `Já jsem ta, která vaši chudinku smutnou koutnou proměňuje v místo, kam má smysl vážit cestu.“` | `Já jsem ta, která váš chudičký smutný kout proměňuje v místo, kam má smysl vážit cestu.“` | typo: 'koutnou' non-word; agreement |
| 125 | `„Ještě neměla dopoledne otevřeno a lidé od chleba říkají, že má špatné období. Zkažené těsto, takové ty neřízené věci.` | `„Celé dopoledne má zavřeno a lidé od chleba říkají, že má špatné období. Zkažené várky, takové ty nepříjemnosti.` | mistranslation: 'door's been shut all morning'; 'neřízené' = uncontrolled ('unpleasantness') |
| 125 | `podívala se na mě s upřímným a lítostivým pohledem, jako by byla profesionálkou důvěřující své přítelkyni,` | `podívala se na mě upřímně a lítostivě, jako profesionálka, která se svěřuje přítelkyni,` | mistranslation: 'one professional confiding in a friend' (důvěřující = trusting) |
| 126 | `„Hygienické předpisy. Jistě to chápeš.“` | `„Hygienické předpisy. Jistě to chápete.“` | address: ruling 2: Renée formal (the paragraph before uses vy) |
| 129 | `Přejela rukou po kovu. „Vyučila se v Lyonu.` | `Přejela rukou po kovu. „Vyučila jsem se v Lyonu.` | grammar: Renée speaks in first person ('I trained in Lyon') |
| 131 | `posílají mouku, máslo a čokoládovou polevu po paletách,` | `posílají mouku, máslo a kuverturu po paletách,` | mistranslation: couverture = kuvertura (čokoládová poleva = cheap glaze, the opposite) |
| 131 | `Pokračovala dál k té polevě, pomalu,` | `Pokračovala dál ke kuvertuře, pomalu,` | mistranslation: couverture = kuvertura |
| 132 | `Věděla jsem, že čokoládová poleva slouží k namáčení` | `Věděla jsem, že kuvertura slouží k namáčení` | mistranslation: couverture = kuvertura |
| 133 | `V Bridgtonu peče jeden velkoobchodní pekař, který mi chce chléb dodávat. Má obrovský zájem.` | `V Bridgtonu peče jedna velkoobchodní pekařka, která mi chce chléb dodávat. Má obrovský zájem.` | gender: the Bridgton wholesale baker is a woman (Joyce, the culprit) — EN 'She's very keen' |
| 135 | `pochybnost o jediném pekaři na třídě,` | `pochybnost o jediné pekařce na třídě,` | gender: Greta is a woman |
| 137 | `Zbytek financierů jsem odnesla zpátky do <bt>Starlight Café</bt>,` | `Zbytek financierů jsem odnesla zpátky do Starlight Café,` | bt: ruling 5: café name |
| 140 | `„To nepochybně vím. A to je právě to, co mě znepokojuje.“ Vzhůru pohlédla.` | `„To určitě ví. A to je právě to, co mě znepokojuje.“ Vzhlédla.` | mistranslation: 'I'm sure she does' (= she knows), not 'I know' |
| 140 | `a já se tu chovám jak nějaký pes si hájící teritorium.` | `a já se tu chovám jako pes, co si hájí teritorium.` | grammar: garbled |
| 146 | `Hal vedl <bt>Frosty's Groceries</bt> na bližším konci třídy` | `Hal vedl Frosty's Groceries na bližším konci třídy` | bt: ruling 5: shop name |
| 146 | `Plechovky měl srovnané popředím dopředu` | `Plechovky měl srovnané etiketou dopředu` | mistranslation: 'cans faced front' — garbled |
| 147 | `Vzhůru pohlédl, zase tak plaše,` | `Vzhlédl, zase tak plaše,` | grammar: calque |
| 147 | `„Jednou jsem zažil zkoušku v podobě zlé zimy, ještě než jsem měl obchod.` | `„Jednou jsem zažil zlou zimu, ještě než jsem měl obchod.` | register: padded calque |
| 151 | `Hal složil papír přesně podél okraje,` | `Hal složil papír přesně v přehybu,` | mistranslation: 'along its crease' |
| 155 | `Věřila jsem tomu většinově.` | `Většině z toho jsem věřila.` | grammar: 'většinově' calque |
| 157 | `Na rohu, kde jsem odbočovala na Evergreenovou, jsem se ohlédla. Nahoře na třídě zářila nová výloha obchodu <bt>Sugarplum Patisserie</bt> zlatým světlem, jasněji než kterýkoliv jiný obchod v ulici. Dole na spodním konci zůstávala <bt>Holly Jolly Bakery</bt> temná.` | `Na rohu, kde jsem odbočovala z Evergreen Avenue, jsem se ohlédla. Nahoře na třídě zářila nová výloha cukrárny Sugarplum zlatým světlem, jasněji než kterýkoliv jiný obchod v ulici. Dole na spodním konci zůstávalo Holly Jolly potemnělé.` | bt: ruling 5: two shop-name spans removed; 'turned OFF Evergreen' (not onto); street name as elsewhere |
| 160 | `kdyby ta moje proměřovala.` | `kdyby ta moje vážila špatně.` | mistranslation: 'in case mine was off' |
| 161 | `Časovači zbývalo deset minut. Posadila se a Pip` | `Časovači zbývalo deset minut. Posadila jsem se a Pip` | grammar: first-person narrator dropped |
| 164 | `Roztrhla ji a vyvalil se bílý dým.` | `Roztrhla ji a vyvalila se bílá pára.` | mistranslation: steam, not smoke |
| 166 | `„Vaše ruce to nejsou.“` | `„Tvoje ruce to nejsou.“` | address: ruling 2: Jessica ↔ Greta informal (ty) everywhere else |
| 166 | `co ještě nevidím, a říkám vám, že vy to nejste.“` | `co ještě nevidím, a říkám ti, že ty to nejsi.“` | address: ruling 2: Jessica ↔ Greta informal |
| 172 | `proti studenému a ostrému větru vanoucímu od parku.` | `proti studenému a ostrému větru vanoucímu od návsi.` | consistency: the green = náves |
| 173 | `Před pekárnou stála asi dvacítka lidí` | `Před pekárnou stál asi tucet lidí` | mistranslation: 'a dozen or so' (dvacítka = twenty) |
| 176 | `červenou barvou dvě slova vysoká stopu.` | `červenou barvou dvě slova vysoká třicet centimetrů.` | units: a foot → 30 cm (safe arithmetic) |
| 177 | `Přečetla jsem si to a udělalo se mi zle.` | `Přečetla jsem si to a zamrazilo mě.` | mistranslation: 'went cold' (not 'felt sick') |
| 189 | `s Marií, Ellie a Dot,` | `s Olivií, Ellie a Dot,` | names: EN 'Olivia and Ellie and Dot' — no Marie in the book |
| 197 | `Někdo chce, aby Frost Falls přestal důvěřovat Holly Jolly.` | `Někdo chce, aby Frost Falls přestalo důvěřovat Holly Jolly.` | grammar: Frost Falls is neuter in this edition |
| 197 | `a pak jim zařídíme, že je zatraceně mrzet, že si vybrali` | `a pak jim zařídíme, že jich bude zatraceně mrzet, že si vybrali` | grammar: ungrammatical |
| 201 | `a Ellie s andělskou trpělivostí šly za ní,` | `a Ellie a já jsme šly za ní,` | mistranslation: EN 'Ellie and I followed her' — narrator dropped, 'angelic patience' invented |
| 203 | `v parkách rozepnutých přes bílý pekařský plášť.` | `v parce rozepnuté přes bílý pekařský plášť.` | grammar: parka is singular |
| 210 | `„Ty drž, já budu metst,“ řekla. „A drž toho svýho ptáka odsud dál. Tyhle věci se dostávají do spárů.“` | `„Vy držte, já budu mést,“ řekla. „A toho svýho ptáka držte odsud dál. Tohle se zadře do nohou.“` | address: ruling 2: Joyce formal before the first-name exchange; 'metst' typo; 'gets in feet' |
| 212 | `a poprvé, odkud vešla dovnitř, se jí uvolnily rysy.` | `a poprvé od chvíle, kdy vešla dovnitř, se jí uvolnily rysy.` | grammar: garbled |
| 214 | `„Ty budeš paní Clausová.“` | `„Vy budete paní Clausová.“` | address: ruling 2: before introductions → formal |
| 217 | `knihy objednávek na Díkuvzdání,` | `knihy objednávek na Díkůvzdání,` | typo: Díkůvzdání |
| 223 | `„Sklenař, kterého používám. Vystřihne tabuli takové velikosti` | `„Sklenář, kterého používám. Uřízne tabuli takové velikosti` | typo: sklenář; glass is cut, not snipped |
| 223 | `Zastrčila vizitku za pokladnu.` | `Opřela vizitku o pokladnu.` | mistranslation: 'propped the card against the register' |
| 228 | `vyjela nahoru po třídě ke konci bloku a byla pryč.` | `vyjela nahoru po třídě ke vzdálenému konci bloku a byla pryč.` | omission: 'toward the far end of the block' (the Sugarplum end) |
| 231 | `sešel v krámku <bt>Yarn Tales</bt> na druhý den věnců` | `sešel v krámku Yarn Tales na druhý den věnců` | bt: ruling 5: shop name |
| 234 | `jednu přes druhou, všechny směrem dovnitř, a poslouchala jsem.` | `jednu přes druhou, všechny směřující domů, a poslouchala jsem.` | consistency: echo of Ch1 'all of them pointing home' (Všechny směřují domů) |
| 235 | `Sněhulák pod Marthiným křeslem tvrdě spal.` | `Snowball pod Marthiným křeslem tvrdě spal.` | names: Snowball (the dog) rendered 'Sněhulák' (= snowman) — Book 1 Czech and Ch1 use Snowball |
| 236 | `Každé z nás se spí klidněji, když ví, že na to to město dohlížíš.` | `Každá z nás spí klidněji, když ví, že na tohle město dohlížíš.` | grammar: garbled |
| 240 | `Před čtyřmi desítkami let zhruba. Nebo patnácti. Stály tam v té kuchyni bok po boku.` | `Zhruba před čtyřiceti lety. Patnáct let. Stály v té kuchyni bok po boku.` | mistranslation: number drift: EN 'Forty years ago, about. Fifteen years [together]' — MT made it 'forty or fifteen years ago' |
| 241 | `„Moje máma kupovala naše sváteční koláče od nich obou,“ přidal se Ivy.` | `„Moje máma kupovala naše koláče na Díkůvzdání od nich obou,“ přidala se Ivy.` | gender: Ivy is a woman; 'Thanksgiving pies' |
| 242 | `panovala spousta zlé krev.` | `panovala spousta zlé krve.` | grammar: case |
| 243 | `„Ořechovo-čokoládový,“` | `„Ten čokoládovo-pekanový,“` | consistency: the chocolate-pecan pie — one rendering (Ch1 čokoládově-pekanové) |
| 247 | `a nevzala si za něj ani korunu.“` | `a nevzala si za něj ani cent.“` | currency: dollars/cents only ('a dime') |
| 248 | `protože pachatel je pouhý dohad a dohadovat se tiskem je nejlepší cesta k žalobě.“` | `protože pachatel je pouhý dohad a dohady v tisku jsou nejlepší cesta k žalobě.“` | mistranslation: 'guessing in print' (dohadovat se = to argue) |
| 249 | `Skládala jsem větvičky, poslouchala a nic z toho si nenechávala pro sebe.` | `Skládala jsem větvičky, poslouchala a sama jsem k tomu nic nepřidala.` | reversed: EN 'gave none of it back' = she shared nothing; MT said she kept none of it to herself |
| 253 | `„Pete s Gretou se kvůli té zadní rampě hádají už od léta.“` | `„Pete s Gretou se kvůli té zadní uličce hádají už od léta.“` | mistranslation: 'that back alley' (the clue alley), not a ramp |
| 255 | `„Hnusná věc, co může člověk o pekaři říct.` | `„Hnusná věc, co může člověk o pekařce říct.` | gender: Greta |
| 256 | `Nechlap, co hází cihlou.“` | `Ne chlap, co hází cihlou.“` | typo: spacing |
| 258 | `Tohohle jsem si na něm všimla kvůli Sněhulákovi, když se ukázalo, že Walterovu psovi nechával každé ráno na molu ty nejlepší kosti.` | `Tohohle jsem si na něm všimla kvůli Snowballovi, když se ukázalo, že Walterovu psovi nechával každé ráno na rampě ty nejlepší kosti.` | names: Snowball; dock = rampa (molo = pier) |
| 262 | `Hal plní sudy zbytečně.` | `Hal neplní sudy jen tak pro nic za nic.` | reversed: EN 'Hal's not filling his barrels for nothing' — MT said he fills them pointlessly |
| 262 | `a pomyslet si: hle, hle, vrhač cihel.“` | `a pomyslet si: tady je ten, kdo hází cihly.“` | register: odd calque |
| 263 | `Kdokoliv tenhle měsíc počítá každou korunu na olej,` | `Kdokoliv tenhle měsíc počítá každý dolar na olej,` | currency: dollars only |
| 270 | `Barva a zničené dávky ovšem nemusely` | `Barva a zničené várky ovšem nemusely` | consistency: batches = várky |
| 273 | `Zvedla jsem hotový věnec; každá větvička směřovala dovnitř.` | `Zvedla jsem hotový věnec; každá větvička směřovala domů.` | consistency: echo 'pointing home' |
| 274 | `pohladila Sněhuláka za uchem.` | `pohladila Snowballa za uchem.` | names: Snowball |
| 275 | `V rukavici už svírala Sněhulákovo vodítko, přestože Sněhulák seděl přímo v krámku,` | `V rukavici už svírala Snowballovo vodítko, přestože Snowball seděl přímo v krámku,` | names: Snowball |
| 279 | `a nevrhala se na ni, protože to tak měla odnaučené.` | `a nevrhala se na ni, protože ji to naučili.` | mistranslation: 'having been taught' |
| 279 | `Sněhulák se probudil, přišel se opřít Emmě do klína,` | `Snowball se probudil, přišel se opřít o Emmino koleno,` | names: Snowball; 'knee' |
| 285 | `Nikdo v kroužku nevyslovil Renèeino jméno.` | `Nikdo v kroužku nevyslovil Renéeino jméno.` | typo: accent (Renée) |
| 254 | `tak si pronajímá starý mrazírenský box ve dvoře` | `tak si pronajímá starý mrazírenský sklad ve dvoře` | consistency: Pete's cold-storage locker = sklad; 'box' is reserved for the walk-in (chladicí box) so Joyce's 'chladírna' slip stays distinct |
| 287 | `a ráno po věncovém večírku, když jsem vystoupala po schodech ze sněhu, vypadala, jako by sesedla o další palec.` | `a ráno po věncovém odpoledni kroužku, když jsem vystoupala po schodech ze sněhu, vypadala, jako by zase o kousek sesedla.` | units: 'another inch' figurative → idiom; it was the wreath circle, not a party |
| 288 | `upečených v mé troubě, protože Greta ji měla pořád zavřenou. Pipa jsem nechala doma` | `upečených v mé troubě, protože Gretina pekárna byla pořád zavřená. Pip jsem nechala doma` | gender: Pip is female (Pipa = masculine accusative); 'Greta's was still shut' |
| 292 | `Potom opatrná, obezřetná úleva.` | `Potom opatrná, obezřetná radost.` | mistranslation: 'pleasure', not relief |
| 293 | `„Slyšel jsem zvonek. Náčelnice Tanaková` | `„Neslyšel jsem zvonek. Náčelnice Tanaková` | reversed: EN 'I didn't hear the bell' |
| 294 | `„Teď máš uši správce, ne hokynáře.“` | `„Teď máte uši správce, ne obchodníka.“` | address: ruling 2: Theo ↔ Jessica formal (he says vy; her one-sided ty fixed) |
| 294 | `„Přinesla jsem ti tohle. Gretin recept, mé ruce. Takže ji za to nesbuď.“` | `„Přinesla jsem vám tohle. Gretin recept, mé ruce. Takže ji podle nich nesuďte.“` | address: ruling 2; 'nesbuď' non-word ('don't judge her by them') |
| 297 | `„Na co jsi přišel?“` | `„Na co jste přišel?“` | address: ruling 2 (Theo formal) |
| 298 | `Chvíli neodpovídal a odpověď brala velkou obklikou.` | `Chvíli neodpovídal a odpověď přišla velkou oklikou.` | typo: 'obklikou' |
| 300 | `„Člověk třídí daňové matriky,` | `„Člověk třídí daňové soupisy,` | mistranslation: tax rolls (matriky = parish registers) |
| 300 | `„A pak něco otočíte.“` | `„A pak něco obrátí.“` | grammar: person agreement with 'Člověk třídí…' |
| 301 | `nakreslená někým s větším  přehledem než umem.` | `nakreslená někým s větší trpělivostí než umem.` | mistranslation: 'more patience than skill' |
| 304 | `A tady nám zčistajasna říká, k čemu podle ní město mělo sloužit.“` | `A tady nám prostě a jasně říká, k čemu podle ní město mělo sloužit.“` | mistranslation: 'telling us plain' (zčistajasna = out of the blue) |
| 305 | `„V roce, kdy město málem nepřežilo,“ namítla jsem.` | `„V roce, kdy město málem nepřežilo,“ řekla jsem.` | mistranslation: not an objection |
| 308 | `ze zmrzlé půdy pod návsi,` | `ze zmrzlé půdy pod návsí,` | typo: case |
| 309 | `dvě řady dětí držící se provazu,` | `dvě řady dětí držících se provazu,` | grammar: agreement |
| 310 | `„To, cos dokázal, totiž že jsi našel ten vzkaz, není maličkost.“` | `„To, že jste našel ten řádek, není maličkost.“` | address: ruling 2 (Theo formal) |
| 312 | `Viděla jsem však, že neustoupí ani o centimetr, pokud to nebylo čistě jeho.` | `Viděla jsem však, že si nevezme ani píď, která nebyla jasně jeho.` | reversed: EN 'wouldn't take one inch of ground that wasn't plainly his' — MT said 'wouldn't yield' |
| 312 | `Přešla jsem to bez chvály. O nic takového nežádal.` | `Přešla jsem to bez chvály. Aniž to vyslovil, požádal mě, abych ho nechválila.` | reversed: EN 'He'd asked, without asking, not to be' |
| 315 | `Zrovna tam, kde předtím z prken smyli nápis ŠPÍNA.` | `Zrovna tam, kde předtím z prken smyli nápis ŠPINAVÉ.` | consistency: graffiti word = ŠPINAVÉ (Ch4) |
| 318 | `které obvykle obrací každý dolar,` | `které obvykle obracejí každý dolar,` | grammar: agreement |
| 319 | `jak palec po palci spravuje budovu,` | `jak kousek po kousku spravuje budovu,` | units: figurative inch → idiom |
| 319 | `A na Elizy Frostovou, jak píše,` | `A na Elizu Frostovou, jak píše,` | grammar: case |
| 320 | `a přitáhnu Nika, aby ho odnesl.` | `a přitáhnu Nicka, aby ho odnesl.` | consistency: Nick declines Nicka elsewhere |
| 326 | `V čtvrtek, když jsem byla u Spolku, pozdě odpoledne a ještě před zavíračkou, vydala jsem se k Peteu Garciovi s úmyslem koupit pečeně` | `Ve čtvrtek, když jsem byla ve Společnosti, pozdě odpoledne a ještě před zavíračkou, vydala jsem se k Peteu Garciovi s úmyslem koupit pečeni` | consistency: Historical Society = Společnost elsewhere; 've čtvrtek'; accusative pečeni |
| 327 | `Peteovo řeznictví sídlilo naprosto přes náves u Evergreen Avenue, v řadě obchůdků, které shlížely do parku z protější strany.` | `Peteovo řeznictví sídlilo na druhé straně návsi naproti Evergreen Avenue, v řadě obchůdků, které shlížely na náves z protější strany.` | mistranslation: Pete's shop is ACROSS the green from Evergreen (not on it) — the yard clue depends on it; the green = náves |
| 327 | `a pod tím všem byl cítit` | `a pod tím vším byl cítit` | typo: case |
| 329 | `„Přišla jsem pro pečeně.` | `„Přišla jsem pro pečeni.` | grammar: accusative |
| 333 | `Svázal pečeně na špalku` | `Svázal pečeni na špalku` | grammar: accusative |
| 336 | `Tomu chlapíkovi přes náves, co má nápis nade dřevem.“` | `Tomu chlapíkovi přes náves, co má nade dveřmi své jméno.“` | mistranslation: 'with my name over it' — garbled |
| 338 | `Otočil pečeně a začal novou smyčku.` | `Otočil pečeni a začal novou smyčku.` | grammar: accusative |
| 338 | `a ona dluží omluvu, kterou dostane, až mě přejde vztek, dřív ne.“` | `a dlužím jí omluvu, kterou dostane, až mě přejde vztek, dřív ne.“` | reversed: EN 'she's owed an apology' — MT said SHE owes one |
| 343 | `Nenechám svou skříňku nezabezpečenou` | `Nenechám svůj sklad nezabezpečený` | consistency: Pete's cold-storage locker = sklad (one term; walk-in = chladicí box, kept distinct) |
| 343 | `Řezník jezdí svou trasu za brzkých ranních hodin,` | `Dodavatel masa jezdí svou trasu za brzkých ranních hodin,` | mistranslation: 'the meat man' is the supplier, not a butcher |
| 343 | `Chlap, který je venku vzadu neustále před světlem, je záhada, nad kterou se vyplatí špinit si ústa šeptem.“` | `Chlap, který je vzadu venku pořád ještě před rozedněním, je najednou záhada, o které stojí za to si šeptat.“` | grammar: garbled ('špinit si ústa šeptem') |
| 347 | `„Něco vám povím,“ řekl teď tíživěji,` | `„Něco vám povím,“ řekl teď tišeji,` | mistranslation: 'lower now' |
| 347 | `„Někdo se motal za tou její.` | `„Někdo se motal vzadu za jejím obchodem.` | grammar: garbled |
| 347 | `a hned to zmizí, jakmile mi za rohem zajásají dálková světla.` | `a hned to zmizí, jakmile se za rohem objeví moje světla.` | mistranslation: 'zajásají' (rejoice) nonsense; 'when my headlamps come around the corner' |
| 348 | `Cítila jsem, jak to dolehlo, ale na tváři nedala nic znát.` | `Cítila jsem, jak to dolehlo, ale na tváři jsem nedala nic znát.` | grammar: auxiliary dropped |
| 350 | `Strčil pečeně přes pult,` | `Strčil pečeni přes pult,` | grammar: accusative |
| 350 | `protože jste přišla pro pečeně a ne pro moji kůži.` | `protože jste přišla pro pečeni a ne pro moji kůži.` | grammar: accusative |
| 351 | `šest palců čistého sněhu jako všude jindy v tuto roční dobu.` | `patnáct centimetrů čistého sněhu jako všude jindy v tuto roční dobu.` | units: six inches → 15 cm (safe; matches Ch1) |
| 352 | `anebo moje, co jsem tam našel.` | `anebo moje, co jsem tam našlapal.` | mistranslation: 'mine tracked over' |
| 352 | `„Nebo ledaže byste byl řezník se skříní vzadu` | `„Nebo ledaže byste byl řezník se skladem vzadu` | consistency: locker = sklad |
| 355 | `„Neděli,“ utrousil Pete` | `„V neděli,“ utrousil Pete` | grammar: case |
| 357 | `Vzala jsem pečeně i tučňáka` | `Vzala jsem pečeni i tučňáka` | grammar: accusative |
| 360 | `Kdybych chtěla jednoduché obvinění pro kruh, v němž se točil omotaný provázkem: spor, skříňka, předbřezenové hodiny.` | `Kdybych pro kroužek chtěla snadné jméno, měla bych ho jako dárek převázaný jeho vlastním provázkem: spor, sklad, hodiny před rozedněním.` | mistranslation: garbled; 'předbřezenové' = pre-March (!); circle = kroužek |
| 361 | `Přinesla jsem pečeně dovnitř` | `Přinesla jsem pečeni dovnitř` | grammar: accusative |
| 364 | `„Musíš se jít podívat na náves. Jsou pryč. Každý jeden sněhulák v aleji se v noci zvedl a šel na procházku.“` | `„Musíš se jít podívat na náves. Pohnuli se. Každý jeden sněhulák na třídě se v noci zvedl a šel na procházku.“` | mistranslation: 'They've moved' (not 'gone'); avenue = třída (alej = tree-lined alley) |
| 366 | `Stála jsem nahoře na Evergreen Avenue a vedle mě poskakovoval Pip,` | `Stála jsem nahoře na Evergreen Avenue a vedle mě stála Pip,` | gender: Pip is female; 'beside me' (no hopping) |
| 368 | `O stopu, možná o dvě.` | `O třicet centimetrů, možná o šedesát.` | units: a foot, perhaps two → 30/60 cm (safe arithmetic) |
| 369 | `kde mohl stát nějaký vtipálek a sníh uplácat.` | `kde mohl stát nějaký vtipálek a postrkovat je.` | mistranslation: 'stood to heave' (push them), not pack snow |
| 370 | `který vykoukl z Frosty's ve ztuhlé zástěře,` | `který vykoukl z Frosty's v zástěře,` | mistranslation: 'ztuhlé' (stiffened) invented |
| 372 | `Fakt, že od Halloweenu ani o stupeň roztálo, byl velkoryse přecházen.` | `Fakt, že od Halloweenu neroztálo ani o stupeň, byl velkoryse přecházen.` | reversed: negation missing ('had not thawed a degree') |
| 375 | `A tak se na tom všichni v aleji shodli.` | `A tak se na tom všichni na třídě shodli.` | consistency: avenue = třída |
| 378 | `prošla jsem pomalu náves s Pipem za patou` | `prošla jsem pomalu náves s Pip za patou` | gender: Pip female (indeclinable) |
| 378 | `Ne směrem k aleji, ke kostelu ani jeden k druhému.` | `Ne směrem ke třídě, ke kostelu ani jeden k druhému.` | consistency: avenue = třída |
| 378 | `které sicec cítili,` | `které sice cítili,` | typo: 'sicec' |
| 380 | `Na návses vůbec neodešel. Vydal se opačným směrem, ven k obchodům na vzdáleném konci, zády k uličce, ke které se všichni ostatní nakláněli, a svou hroudovitou tvář měl otočenou k ústí průjezdu, jenž se táhl za nimi. Ušel dobrých deset stop mimo společnost` | `Na náves vůbec nešel. Vydal se opačným směrem, ven k obchodům na vzdáleném konci, zády k cestě, ke které se všichni ostatní nakláněli, a svou hroudovitou tvář měl otočenou k ústí uličky, která se táhla za nimi. Ušel dobré tři metry mimo společnost` | mistranslation: lane/alley SWAPPED: the clue ALLEY (ulička, as Ch1/Ch5) was 'průjezd' and the lane got 'ulička'; 'návses' typo; ten feet → 3 m |
| 381 | `Kapitola 3` | `(emptied)` | structure: stray 'Kapitola 3' heading in the middle of Ch8 (not in EN) — emptied, paragraph kept |
| 382 | `Sněhulák, který se v uličce ocitl na špatném místě.` | `Sněhulák na špatném místě u uličky.` | mistranslation: 'out of place by an alley' |
| 388 | `Postavila se vedle něj.` | `Postavila jsem se k němu.` | grammar: first-person narrator dropped |
| 388 | `v řídkých zlatých nitích, nííž, než jsem si pamatovala,` | `v řídkých zlatých nitích, níž, než jsem si pamatovala,` | typo: 'nííž' |
| 388 | `a stála s zobákem zvednutým vzhůru, přičemž sledovala zlaté nitě, jako by sledovala sleďa na talíři.` | `a stála se zobákem zvednutým vzhůru, přičemž sledovala zlaté nitě, jako by sledovala sledě na talíři.` | typo: se zobákem; sledě |
| 392 | `aby to přestalo vyžírat sněhuláky.“` | `aby si to přestalo půjčovat sněhuláky.“` | mistranslation: 'stops borrowing the snowmen' (vyžírat = devour) |
| 392 | `Kdyby mohl, zavřel by ji do ohrady k sobům, a měl by asi takové štěstí, že by ji udržel.“` | `Kdyby mohl, zavřel by ji do ohrady k sobům – a udržel by ji tam asi stejně úspěšně jako je.“` | mistranslation: irony lost ('about as much luck holding it') |
| 394 | `na krb zářící trpělým vnitřním teplem,` | `na krb zářící trpělivým vnitřním teplem,` | typo: 'trpělým' |
| 397 | `„Všichni ostatní ti tady zamilovaně civí do ulice a ty ses postavil sem dolů` | `„Všichni ostatní zasněně civí nahoru k Hollyhock Lane a ty ses postavil sem dolů` | mistranslation: 'mooning up the lane' — lane vs alley must stay distinct |
| 402 | `a každý další bochánek vyjel ven sladký jako med. Stála za opravenou vitrínou poprášenou moukou a zářila na všechny strany.` | `a každá další várka vyšla sladká jako med. Stála za opravenou vitrínou, poprášená moukou, a zářila na všechny strany.` | mistranslation: 'every batch'; it is Greta who is dusted with flour, not the case |
| 403 | `Byla jsem ve frontě třetí od konce a Pip zkoumal drobky pod vitrínou, když zacinkal zvonek a do chladného vzduchu vešel muž. Už podle toho, jak měl ještě klobouk na hlavě, jsem poznala, že je cizí.` | `Byla jsem ve frontě třetí od konce a Pip zkoumala drobky pod vitrínou, když zacinkal zvonek a s chladem dovnitř vešel muž. Ještě než si sundal klobouk, poznala jsem, že je cizí.` | gender: Pip female; 'came in with the cold'; 'before he had his hat off' |
| 412 | `Pip se držel drobků pod vitrínou a nechal ho dělat jeho práci.` | `Pip se držela drobků pod vitrínou a nechala ho dělat jeho práci.` | gender: Pip female |
| 414 | `Hrdá žena, která se připravuje na to, že jí veřejně vytknou přesně to, čím strávila život tím, že nebyla.` | `Hrdá žena, která se připravuje na to, že jí veřejně řeknou, že je přesně tím, čím celý život nebyla.` | grammar: garbled |
| 416 | `Meziprostor pod zadními dveřmi, kde je opotřebované těsnění. Podle předpisů to může přilákat hlodavce.“` | `Mezera pod zadními dveřmi, kde je opotřebované těsnění. Podle předpisů tudy můžou dovnitř škůdci.“` | consistency: door-gap = mezera (one term); 'admit vermin' |
| 416 | `„A tohle teď ukazuje o dva stupně pod limitem.` | `„A tohle teče o dva stupně pod normou.` | clue: 'runs two degrees under code' — the °F clue figure; one wording at all three places |
| 419 | `„Zavíráte mě uprostřed sezóny.“` | `„Zavíráte mě na týden v hlavní sezóně.“` | omission: 'a week into the season' — the week dropped |
| 420 | `„Pozastavuji provoz do zjednání nápravy,“ opravil ji slovy, která mu umožňovala klidně spát,` | `„Pozastavuji provoz do zjednání nápravy,“ řekl, což bylo totéž, jen slovy, která mu umožňovala klidně spát,` | omission: 'the same thing said in the words that let him sleep' — the point dropped |
| 422 | `a Pip mu šlapal v patách a ostříhal mosaznou přezku na tašce.` | `a Pip nám šlapala v patách a pokukovala po mosazné přezce jeho tašky.` | gender: Pip female; 'ostříhal' nonsense ('with her eye on the brass clasp') |
| 426 | `a odborný výraz pro škvíru pod dveřmi.` | `a odborný výraz pro mezeru pod dveřmi.` | consistency: door-gap = mezera |
| 427 | `čistý a pronikavý jako úder do zvonu ve špatné tůni.` | `čistý a pronikavý jako úder do zvonu ve špatné tónině.` | mistranslation: tůň = pool; key = tónina |
| 427 | `vedle zatuchlé mouky` | `vedle zkyslé mouky` | mistranslation: 'sour flour' (zatuchlá = musty) |
| 429 | `dokud se nesmrtilo,` | `dokud se nesetmělo,` | typo: 'nesmrtilo' |
| 432 | `Pip se batolil přes podlahu, aby jí zkontroloval boty.` | `Pip se batolila přes podlahu, aby jí zkontrolovala boty.` | gender: Pip female |
| 434 | `Greta položenou zlatou krabičku usadila na pult vedle žlutého papíru. Neotevřela ho.` | `Greta položila zlatou krabičku na pult vedle žlutého papíru. Neotevřela ji.` | grammar: garbled; pronoun agreement |
| 434 | `Pip chvíli zůstal u dveří a díval se ven` | `Pip chvíli zůstala u dveří a dívala se ven` | gender: Pip female |
| 435 | `Pak jsme s Pipem vyšli na Evergreen Avenue` | `Pak jsme s Pip vyšly na Evergreen Avenue` | gender: Pip female; narrator female |
| 437 | `s obličejem zvrásněným jako počasí,` | `s obličejem zachmuřeným jako bouřka,` | mistranslation: 'a face like weather' (stormy) |
| 439 | `Pip mi šlapal těsně za patami.` | `Pip mi šlapala těsně za patami.` | gender: Pip female |
| 412 | `Strčil teploměr do chladicího boxu a zapsal naměřenou hodnotu.` | `Strčil teploměr do chladicí vitríny a zapsal naměřenou hodnotu.` | consistency: EN 'cold-case' (display cooler) — 'chladicí box' is reserved for the walk-in, the clue word |
| 442 | `daly hlavy dohromady nad cenou oleje.` | `daly hlavy dohromady nad cenou topného oleje.` | mistranslation: heating oil |
| 448 | `„Celý smysl toho sudu spočívá v tom, že nikdo nemusí stát na světle a prosit. Ale krabice odchází na tenhle konec města jednou týdně` | `„Celý smysl toho sudu spočívá v tom, že nikdo nemusí stát na světle a prosit. Ale krabice odchází na ten konec města jednou týdně` | mistranslation: 'that end of town' |
| 448 | `jedna krabice potřebuje odnést a já to vzít nemůžu.` | `je tu krabice, kterou je potřeba odnést, a já ji vzít nemůžu.` | grammar: garbled |
| 449 | `A zastrčené straně, kde by to pyšné oko hned nenašlo,` | `A zastrčené po straně, kde by to pyšné oko hned nenašlo,` | omission: word dropped |
| 451 | `Doucettova hromada byla nízká a ubohá pod celtou. Na dva týdny topení tam, kde by ho měly být čtyři měsíce.` | `Doucettovic hromada byla nízká a ubohá pod celtou. Na dva týdny topení tam, kde ho mělo být na čtyři měsíce.` | grammar: garbled |
| 463 | `„V ulici je obchod s rozbitým okem` | `„V ulici je obchod s rozbitým oknem` | typo: okem = eye |
| 466 | `i když Greta umyla kuchyň a otevřela nové kvasnice.` | `i když Greta vydrhla kuchyni a otevřela nové droždí.` | consistency: 'scrubbed'; yeast = droždí (Ch2) |
| 470 | `Hal sestrojil sud tak,` | `Hal vymyslel sud tak,` | mistranslation: 'built' in the sense of designed the scheme |
| 471 | `Větší pořádkové než polovina ulice,` | `Pořádnější hospodyně než polovina ulice,` | grammar: 'pořádkové' non-word |
| 472 | `„Nenašla jmenovitě žádného sabotéra nahoře v kopci.“` | `„Nahoře v kopci jsi žádného sabotéra nenašla.“` | grammar: garbled ('jmenovitě') |
| 475 | `„Vyžaduje to všechno dohromady, jestli se v té mouce mýlím.` | `„Vyžaduje to všechno dohromady, jestli mám s tou moukou pravdu.` | reversed: EN 'if I'm right about the flour' |
| 477 | `zatímco se sud u dveří plnila,` | `zatímco se sud u dveří plnil,` | grammar: agreement |
| 477 | `a draze za to zaplatila v městech,` | `a draze za to zaplatila ve městech,` | grammar: ve městech |
| 481 | `abych si schovala to, od čeho mě můj nos, kterému jsem věřila, zrazoval.` | `abych si schovala to, k čemu se nos, kterému jsem věřila, odmítal přiblížit.` | reversed: EN 'keep what a nose I trusted would not go near' (Pip's nose) — MT made it Jessica's own nose dissuading her |
| 483 | `Ani nikoho z kraje, jejichž člověka už poslali,` | `Ani nikoho z okresu, jehož člověka už poslali,` | consistency: county = okres (Ch3, Ch9) |
| 483 | `na konci uličky odbočující z Maple Street,` | `na konci cestičky odbočující z Maple Street,` | consistency: a lane, not the clue alley (ulička) |
| 484 | `znamenalo, že byl i místním lékárníkem.` | `znamenalo, že byl i místním chemikem.` | mistranslation: 'chemist' = analyst here (lékárník = pharmacist) |
| 486 | `zatlučeme její stěny prkny, otevřeme dveře` | `utěsníme jí stěny, otevřeme dveře` | mistranslation: 'seal her walls' (the grout), not board them up |
| 487 | `Odstrouhal víčko` | `Odšrouboval víčko` | typo: 'odstrouhal' = planed off |
| 490 | `Vypadal jako člověk, který našel odpověď, v kterou doufal, že ji neobjeví.` | `Vypadal jako člověk, který našel odpověď, o které doufal, že ji nenajde.` | grammar: garbled |
| 493 | `Když z tohohle umícháte těsto, zkvasí to celou dávku` | `Když z tohohle umícháte těsto, zkysne celá várka` | mistranslation: 'sours the whole batch' (zkvasit = ferment) |
| 493 | `Právě proto to pronásledovalo čtyři čisté várky a nový pytel kvasnic a ona na to nikdy nepřišla.` | `Právě proto to honila přes čtyři čisté várky a nové droždí a nikdy to nechytila.` | mistranslation: subject reversed ('she chased it'); yeast = droždí |
| 495 | `aby žitným a lahůdkovým chlebům dodaly chlebovou kyselost bez kvásku.` | `aby žitným a lahůdkovým chlebům dodaly kváskovou kyselost bez kvásku.` | mistranslation: 'a sourdough tang' |
| 495 | `Tohle je dávka, kterou použijete, když chcete úmyslně zničit sto liber mouky.` | `Tohle je dávka, kterou použijete, když chcete úmyslně zničit pětačtyřicet kilo mouky.` | units: a hundred pounds → 45 kg (accurate per Lisa's 2026-08-11 ruling, logged) |
| 501 | `čtyřikrát prošla čistými várkami a čerstvým pytlem kvasnic,` | `čtyřikrát přes čisté várky a čerstvé droždí,` | consistency: yeast = droždí; grammar |
| 501 | `Mělo to stejný rukopis jako to sepsané udání s citacemi podparagrafů, ruka, která dokonale znala kód k umyvadlu pro personál.` | `Mělo to stejný rukopis jako ta na stroji psaná stížnost s citacemi pododstavců, ruka, která dokonale znala předpis o umyvadle.` | consistency: sub-clauses = pododstavce (blurb, Ch9); hand-sink = umyvadlo |
| 502 | `Půda pod touto otázkou se však mezitím zhroutila,` | `Půda pod touto otázkou se však mezitím posunula,` | mistranslation: 'had shifted' |
| 504 | `A vtom se ta věc, která se potulovala městem, dotkla mé rukou.` | `A vtom se ta věc, která se potulovala městem, dotkla mého rukávu.` | grammar: garbled ('put its hand on my sleeve') |
| 505 | `Velké shromáždění na mýtině se stále` | `Velké shromáždění na návsi se stále` | consistency: the common/green = náves (mýtina = forest clearing) |
| 505 | `jeho uhlíkový obličej a celá jeho bezvládná váha` | `jeho uhlíkový obličej a celá jeho hroudovitá váha` | mistranslation: 'lumpen' (bezvládná = limp/lifeless) |
| 507 | `a dívala se tam, kam se dívala ona,` | `a dívala se tam, kam se díval on,` | grammar: the snowman is masculine |
| 507 | `Stála tam dva dny otočená čelem k té uličce` | `Stál tam dva dny otočený čelem k té uličce` | grammar: the snowman (masc.) |
| 508 | `promluvila jsem tiše k tučňákovi u mé boty, který couvl od bedny s moukou a naježil peří` | `promluvila jsem tiše k tučňačici u mé boty, která couvla od nádoby s moukou a naježila peří` | gender: Pip is female |
| 513 | `jako když člověk nosí moc dlouho v kapsi kámen,` | `jako když člověk nosí moc dlouho v kapse kámen,` | typo: kapse |
| 515 | `místa tak akorát pro jednu dodávku a zášti až nad hlavu.` | `místa tak akorát pro jednu dodávku a zášti dost pro dva.` | mistranslation: 'grudge enough for two' |
| 518 | `Člověk by tam ani musel chodit dovnitř.` | `Člověk by tam ani nemusel chodit dovnitř.` | reversed: negation missing |
| 518 | `Donutila by se odnést otrávenou mouku do nádob sama a ještě by poděkovala chladu za průvan.` | `Tu upravenou mouku by do nádob odnesla sama a ještě by poděkovala chladu za průvan.` | no-poison: EN 'doctored flour' — MT said 'poisoned'; also 'Donutila by se' (would force herself) is wrong |
| 522 | `mezi zadními traktem obchodů` | `mezi zadními trakty obchodů` | grammar: case |
| 522 | `Peteův mrazicí box, stará místnost z tvárnic s těžkou západkou, a druhý visací zámek, který si koupil od Toma, zářivě nový na brance.` | `Peteův mrazírenský sklad, stará místnost z tvárnic s těžkou západkou, a druhý visací zámek, který si koupil od Toma, zářivě nový na bráně.` | consistency: locker = sklad (walk-in = chladicí box kept distinct); gate = brána (Ch5, Ch7 — the gate-key clue) |
| 526 | `na nový zářivý visací zámek na řezníkově brance.` | `na nový zářivý visací zámek na řezníkově bráně.` | consistency: gate = brána |
| 530 | `Pete Garcia měl rampu a dvacet zimy skládání zboží na ní,` | `Pete Garcia měl rampu a dvacet zim skládání zboží na ní,` | grammar: genitive plural |
| 530 | `Měl klíč ke sdílené brance,` | `Měl klíč ke sdílené bráně,` | consistency: gate = brána |
| 531 | `a končila u jeho branky` | `a končila u jeho brány` | consistency: gate = brána |
| 532 | `dřív, než jsem vůbec věděla, že mouka byla otrávená.` | `dřív, než jsem vůbec věděla, že s moukou někdo něco provedl.` | no-poison: EN 'the flour was doctored' — no poison in this edition |
| 536 | `Dosáhnout na mouku byla jen jedna polovina. Peníze a znalost věci byly ty další dvě,` | `Dosáhnout na mouku byla jen jedna noha trojnožky. Peníze a znalost věci byly ty další dvě,` | mistranslation: 'one leg of it' — three legs, not halves |
| 537 | `Byla to brána, a to pořádně široká, a spousta poctivých lidí jí procházela každé ráno,` | `Byl to vchod, a to pořádně široký, a spousta poctivých lidí jím procházela každé ráno,` | consistency: metaphorical 'doorway' must not reuse the literal gate word (brána) |
| 538 | `Ale Petic brána to byla ze všech nejvíc.` | `Ale ze všech nejvíc to byl Peteův vchod.` | typo: 'Petic' non-word; doorway metaphor |
| 540 | `a o tři dál na řezníkovu branku,` | `a o tři dál na řezníkovu bránu,` | consistency: gate = brána |
| 542 | `pekařská dodávka s nápisem <bt>Wendt's Bakehouse, Bridgton</bt> na boku.` | `pekařská dodávka s nápisem Wendt's Bakehouse, Bridgton na boku.` | bt: ruling 5: van lettering is not a book title |
| 542 | `a přecházela přes utuavený sníh` | `a přecházela přes udusaný sníh` | typo: 'utuavený' |
| 549 | `nad tou mapou s Petrovým jménem na chladném konci,` | `nad tou mapou s Peteovým jménem na chladném konci,` | names: Pete rendered 'Petr' in Ch13 |
| 549 | `Ne, kdo mohl stát na té římse,` | `Ne, kdo mohl stát na tom prahu,` | consistency: sill = práh (Ch12) |
| 551 | `Petr mi ten den, co jsem přišla pro pečeni,` | `Pete mi ten den, co jsem přišla pro pečeni,` | names: Pete |
| 551 | `a Petr si založil život na tom, že je obojí.` | `a Pete si založil život na tom, že je obojí.` | names: Pete |
| 552 | `A Petr Garcia byl řezník. Znal kus hovězího do posledního vlákna a o kyselém základu nebo špetce křídy věděl stejné nic jako já o bourání bejka.` | `A Pete Garcia byl řezník. Znal kus hovězího do posledního vlákna a kyselý základ by od poprášení křídou rozeznal asi tak, jako bych já dokázala rozporcovat býka.` | names: Pete; garbled comparison |
| 553 | `K té chladné čáře vedoucí k jeho brance jsem dospěla pouhou dostupností, a dostupnost, jak jsem si v uličce opakovala, znamená jen dveře, ne rozsudek.` | `K té chladné čáře vedoucí k jeho bráně jsem dospěla jen na základě přístupu, a přístup, jak jsem si v uličce opakovala, je jen vchod, ne rozsudek.` | consistency: access = přístup, doorway = vchod (Ch12); gate = brána |
| 556 | `což byla ta nejtěžší pochůzka.` | `což byla těžší pochůzka než většina jiných.` | mistranslation: 'a harder errand than most' |
| 559 | `„Kvůli takové blbosti sem nechodíš mazat starému bručounovi med kolem huby.“` | `„Kvůli tomuhle jste sem přece nešla mazat starému bručounovi med kolem huby.“` | address: ruling 2: Pete ↔ Jessica formal (she says vy throughout) |
| 561 | `Cuknul s bradou.` | `Cuklo mu v čelisti.` | mistranslation: 'His jaw worked' |
| 561 | `pustil se raději do hovězího než do mě.` | `obracel se raději k hovězímu než ke mně.` | mistranslation: 'addressed the beef rather than me' (MT: 'set about the beef rather than me') |
| 561 | `Ty jsi jediný člověk, co přišel tvrdit opak.“` | `Vy jste jediný člověk, co přišel tvrdit opak.“` | address: ruling 2 (Pete formal) |
| 561 | `Tak si vezmeš kotletu. Bez diskusí. Nezaplatím ani korunu, a tím to končí.“` | `Tak si vezmete kotletu. Bez diskusí. Platit mi nebudete, a tím to končí.“` | reversed: EN 'I'm not letting you pay' — MT 'I won't pay a crown' (reversed + wrong currency); ruling 2 |
| 563 | `„Ta postava, o které jsem ti říkal,“` | `„Ta postava, o které jsem vám říkal,“` | address: ruling 2 |
| 563 | `Určitě to chceš vědět celé, když už mi věříš.“` | `Určitě to budete chtít slyšet celé, když už mi věříte.“` | address: ruling 2 |
| 563 | `a zahleděl se z okna na výlohy Evergreen protilehlé návsi,` | `a zahleděl se z okna na výlohy Evergreen Avenue na druhé straně návsi,` | grammar: garbled |
| 566 | `„A nevěř, že kvůli tomu, že ji mám rád.` | `„A nevěřte, že kvůli tomu, že ji mám rád.` | address: ruling 2 |
| 566 | `má lubem něco nekalého,` | `má za lubem něco nekalého,` | typo: idiom 'mít za lubem' |
| 569 | `„to nikomu neříkej.“` | `„to nikomu neříkejte.“` | address: ruling 2 |
| 41 | `plech čokoládově-pekanových košíčků` | `plech čokoládovo-pekanových košíčků` | consistency: chocolate-pecan = čokoládovo-pekanový (one form) |
| 576 | `přišla po cestičce naproti s notesem` | `přišla po mé cestičce s notesem` | mistranslation: 'came up my path' |
| 577 | `Pracoval pro Gretu. Loni. Zametání,` | `Celý poslední rok pracoval pro Gretu. Zametání,` | mistranslation: 'this past year' (not 'last year') |
| 581 | `dala jsem mu plat na dva týdny dopředu, aniž by pro něj hnul prstom, a k tomu krabici` | `dala jsem mu výplatu za dva týdny, které už neodpracoval, a k tomu krabici` | typo: 'prstom'; garbled ('two weeks' pay he hadn't worked for') |
| 581 | `Hlas se jí zatvrdil.` | `Hlas se jí zadrhl.` | mistranslation: 'Her voice thickened' (with emotion) |
| 581 | `A teď mi na zeď namalovali ŠPÍNU a já to nedokážu spojit` | `A teď z něj dělají toho, kdo mi na zeď namaloval ŠPINAVÉ, a já to nedokážu spojit` | mistranslation: 'now they've got him painting DIRTY'; graffiti word = ŠPINAVÉ |
| 583 | `„Byl zraněný, ne zlý.“ Žmoulala zástěru. „Zlý kluk vám práskne dveřmi. Danny mi potiskl ruku.` | `„Byl smutný, ne naštvaný.“ Žmoulala zástěru. „Naštvaný kluk vám práskne dveřmi. Danny mi potřásl rukou.` | mistranslation: 'Hurt, not sore' (zraněný = injured); 'potiskl' non-word |
| 583 | `Že to zranění přeteklo.` | `Že se ten smutek zvrhl ve zlost.` | mistranslation: 'That the hurt turned' |
| 591 | `Jeho otec měl tu týdenní hřbitovní směnu v továrně` | `Jeho otec měl ten týden noční směnu v továrně` | mistranslation: 'graveyard shift' calque |
| 593 | `Je to jediná duše tady dole, která mi kdy zaplatila na dřívko a nikdy mě neošidila.“` | `Je to jediná duše tady dole, která mi vždycky zaplatila přesně a nikdy mě neošidila.“` | mistranslation: 'na dřívko' = on credit (reversed sense) |
| 597 | `Já akorát honila to nejhlasitější křovisko.“` | `Já jsem honila tu nejhlasitější část.“` | mistranslation: garbled ('the loud part') |
| 602 | `s utěrkou sevřenou v obou douškách rukou.` | `s utěrkou sevřenou v obou rukou.` | typo: 'douškách' |
| 602 | `„Tvůj Danny tu zeď nepomaloval, paní Ottová.` | `„Váš Danny tu zeď nepomaloval, paní Ottová.` | address: ruling 2: Mrs Ott formal |
| 603 | `Položila ruku na zárubně` | `Položila ruku na zárubeň` | grammar: case |
| 606 | `Takže rámy na vyšívání zůstalo naskládané` | `Takže rámy na věnce zůstaly naskládané` | mistranslation: the frames are wreath frames; agreement |
| 615 | `„Jeho matka nakrmila obědem každé dítě v tomhle městě už před dvaceti lety,“` | `„Jeho matka už dvacet let krmí obědy každé dítě v tomhle městě,“` | mistranslation: 'for twenty years' (not twenty years ago) |
| 616 | `a to byl konec jména Dannyho Otta v kruhu.` | `a to byl konec jména Dannyho Otta v kroužku.` | consistency: circle = kroužek |
| 619 | `„Děláte, že to nic není,“ řekla.` | `„U tebe to vypadá, jako by to nic nebylo,“ řekla.` | address: ruling 2: Ellie ↔ Jessica informal (circle) |
| 622 | `„Byla jsem na obědě v <bt>Sugarplum Patisserie</bt>,“` | `„Byla jsem přes oběd v Sugarplum,“` | bt: ruling 5: shop name; EN 'into Sugarplum on my lunch' |
| 628 | `Sledovala jsem dál Elliečinu čepici.` | `Sledovala jsem dál Elliinu čepici.` | grammar: possessive of Ellie |
| 632 | `ty svoje dva čokoládovopekanové koláče` | `ty svoje dva čokoládovo-pekanové koláče` | consistency: one form |
| 43 | `viděla jsem tě to udělat v sále a nezapomněla jsem na to.“` | `viděla jsem tě to udělat ve spolkovém domě a nezapomněla jsem na to.“` | consistency: the Grange = spolkový dům (one rendering; Ch15–23) |
| 123 | `„Chudinka žena. S těmi jejími nedávnými potížemi je to taková škoda.“` | `„Chudák žena. Taková škoda, ty její potíže zrovna teď.“` | clue: Renée's line is echoed in Ch15/17 — one wording; 'just now' restored |
| 638 | `Spolkový dům byl dokořán pro obě sbírky najednou, Halovu i spolkovou,` | `Spolkový dům byl dokořán pro obě sbírky najednou, Halovu i tu pro Společnost,` | consistency: Historical Society = Společnost (Spolek ≠ Society) |
| 638 | `v dobrém kabátě, ztuzený studem z toho, kolik se toho sešlo.` | `v dobrém kabátě a ostýchal se nad tím, kolik lidí přišlo.` | grammar: 'ztuzený' non-word |
| 638 | `odkdy Grety provázejí potíže,` | `od chvíle, kdy začaly Gretiny potíže,` | grammar: garbled |
| 641 | `a Joyce Wendt z ní vystoupila s rozepnutou bundou přes pekařský ráz.` | `a Joyce Wendtová z ní vystoupila s rozepnutou bundou přes pekařský plášť.` | typo: 'ráz'; surname form as elsewhere |
| 643 | `„Jsou ze včerejška,“ řekla, když tichost nastala zpátky. „Od chovatele prasat bych za ně dostala leda pár haléřů. Líp udělají, když poputují na kopci.“` | `„Jsou ze včerejška,“ řekla, když potlesk utichl. „Od chovatele prasat bych za ně dostala leda pár centů. Líp udělají, když poputují na kopec.“` | currency: pennies → centy (no haléře); garbled; case |
| 646 | `Nehadala jsem se.` | `Nehádala jsem se.` | typo: diacritic |
| 647 | `„Dole ve své kuchyni drhla podlahu, do které nesmí vstoupit s těstem.“` | `„Je dole a drhne kuchyň, ve které nesmí péct.“` | mistranslation: garbled ('scrubbing a kitchen she isn't allowed to bake in') |
| 649 | `kde v bledé vlně stála Renée Duval mezi` | `kde v bledé vlně stála Renée Duvalová mezi` | consistency: surname form |
| 651 | `Pro koho jiného než pro všechny. Cestou podložená cedrová krabice Spolku stála na bočním stolku na šířku už od října` | `Nová ve skutečnosti nebyla. Cedrem vyložená krabice Společnosti stála otevřená na bočním stolku už od října` | mistranslation: 'It wasn't new to anyone' garbled; 'cedar-lined'; 'open on its side table' |
| 651 | `Gretin lístek s receptem na čokoládově-pekanové sušenky, Bramovy dvoje palčáky velké tak akorát pro palec. Toho rána ji Theo snnesl dolů` | `Gretin lístek s receptem na čokoládovo-pekanový koláč, Bramovy dva palčáčky velké jako palec. Toho rána ji Theo snesl dolů` | mistranslation: the recipe card is for the chocolate-pecan PIE (Ch27 payoff), not cookies; typo |
| 652 | `Vložila jsem tam svou červenou rukavičku, tu malou, kterou jsem pro ni v říjnu upletla a schovala na ten správný den. Zapadla hned vedle Bramovy.` | `Vložila jsem tam svůj červený palčáček, ten malý, který jsem pro ni v říjnu upletla a schovala na ten správný den. Zapadl hned vedle Bramových.` | mistranslation: craft word: mitten = palčák (rukavička = glove) |
| 653 | `v přední místnosti Spolku až do své hodiny. Každý v sobě nosil jasnou hranici mezi oběma, aniž by kdokoli musela cokoli pronést nahlas. Stará se měla otevřít na nový rok, ve společnosti, jak předkové zamýšleli.` | `v přední místnosti Společnosti až do své hodiny. Každý v sobě nosil jasnou hranici mezi oběma, aniž by kdokoli musel cokoli pronést nahlas. Stará se měla otevřít o novém roce, ve společnosti, jak zamýšleli předkové.` | consistency: Society = Společnost; agreement; echo of the Ch6 card wording |
| 655 | `„Bude to stačit,“ pronesl tiše, sotva těm slovům věře. „Spolek.` | `„Bude to stačit,“ pronesl tiše, sotva těm slovům věřil. „Společnost.` | consistency: Society = Společnost |
| 656 | `že na mé třídě žije někdo, kdo Gretě přináší zmar.` | `že na mé třídě žije někdo, kdo chce Gretě ublížit.` | mistranslation: 'meant Greta harm' |
| 658 | `mezi rozpisy orby a církevními hostinami,` | `mezi rozpisy odklízení sněhu a kostelními večeřemi,` | mistranslation: plow schedules = snow-plough rota (orba = ploughing fields) |
| 659 | `Sugarplum. Patisserie & Confiserie. Velké slavnostní otevření.` | `Sugarplum. Patisserie & Confiserie. Týden velkého otevření.` | consistency: 'Grand Opening Week' — as Ivy calls it in Ch14; the WEEK is the clue |
| 661 | `Teplý sál kolem mě tak trochu oněměl.` | `Teplý sál se kolem mě tak trochu vzdálil.` | mistranslation: 'went a little distant' |
| 662 | `mezi kakaovými bochánky, a slyšela` | `mezi kakaovými šneky, a slyšela` | consistency: cocoa buns = kakaoví šneci (Ch9) |
| 662 | `Týden. Možná víc, jestli díly na dřez nedorazí.` | `Týden. Možná déle, jestli nedodají díly k tomu umyvadlu.` | clue: Varney's quoted line must match Ch9; 'the sink' is the hand-sink (umyvadlo) — 'dřez' is reserved for Joyce's 'Hobart sink' (italic run kept) |
| 662 | `kdy nejstarší pekařství na Evergreen Avenue osleplo.` | `kdy nejstarší pekařství na Evergreen Avenue zhasne.` | mistranslation: 'would go dark' |
| 663 | `který si Renée Duval vybrala` | `který si Renée Duvalová vybrala` | consistency: surname form |
| 668 | `že za sto let bude tady někdo pořád ještě vědět, co je to finančník.“` | `že za sto let bude tady někdo pořád ještě vědět, co je to financier.“` | mistranslation: the cake (financier), not 'a financier' (banker) |
| 673 | `Renédina tvář se rozzářila prostou radostí ze svého obchodu.` | `Renéeina tvář se rozzářila prostou radostí ze svého řemesla.` | typo: name form; 'her trade' |
| 674 | `jinak vám celá řada do dvacátého dne přijde niva.` | `jinak vám celá řada do dvacátého přijde vniveč.` | typo: 'niva' |
| 676 | `hlas doktora Mitchella z lavice mezi hnědými lahvemi. ` | `hlas doktora Mitchella od pracovního stolu mezi hnědými lahvičkami. ` | mistranslation: bench = pracovní stůl |
| 676 | `Sušená kyselina. Někdo ji tam dal. A přesně věděl kolik.` | `Sušená kyselina. Někdo to tam dal. A přesně věděl, kolik toho má přidat.` | clue: Doc's words echoed verbatim from Ch11 (italic run kept) |
| 677 | `Doktor říkal, že pekařství by pro ten sajrajt v Gretině nádobě nemělo uplatnění.` | `Doktor říkal, že cukrárna by pro tu věc v Gretině nádobě neměla žádné využití.` | clue: Doc said a PASTRY kitchen (cukrárna, Ch11) — 'pekařství' reverses the point that Renée is pastry |
| 678 | `přepuštěného másla, pronášející slova o ` | `přepuštěného másla, která říkala: ` | clue: echo of Renée's Ch3 line |
| 678 | `chudince, jaká je to škoda s těmi jejími potížemi` | `chudák žena, taková škoda, ty její potíže zrovna teď` | clue: echo of Renée's Ch3 line — same words (italic run kept) |
| 678 | `Neuhádla ten týden. Sestavila ho.` | `Ten týden neuhádla. Naplánovala ho.` | mistranslation: 'She'd built it' |
| 680 | `protože v tom horku se mi už nedokázalo přemýšlet.` | `protože v tom horku se nedalo přemýšlet.` | grammar: ungrammatical |
| 687 | `a vůbec se na ni nepodívala.` | `a vůbec jsem se na ni nepodívala.` | grammar: auxiliary dropped |
| 689 | `Přešla jsem k ní hned následující ráno` | `Šla jsem za ní hned následující ráno` | grammar: calque |
| 689 | `která lidi četla se stejnou lehkostí jako stránky místnosti.` | `která lidi četla se stejnou lehkostí jako místnost.` | mistranslation: 'read a room' |
| 690 | `Obruč jsem v tichu domova přichystala už za tmy, zatímco Nick spal, jako jedinou záminku,` | `Na věnci jsem se rozhodla už za tmy, zatímco Nick spal – byl to jediná záminka,` | mistranslation: 'I had settled on the wreath' = decided |
| 690 | `vyzdobily na svátky celou třídu, každý jeden výkladní skříň,` | `vyzdobily na svátky celou třídu, dveře každého obchodu,` | grammar: garbled agreement |
| 701 | `„Chudinka ženská. Tak strašně blbá náhoda,` | `„Chudák žena. Tak nešťastné načasování,` | register: Renée is polished; 'Poor woman' as in her Ch3 line |
| 701 | `Dřez odpadní vody je napojený na staré potrubí a jste dvě stupnice pod limitem, aniž byste o tom věděl,` | `Umyvadlo je napojené na staré potrubí a teče vám o dva stupně pod normou, aniž byste o tom věděla,` | clue: hand-sink = umyvadlo (not dřez — reserved for 'the Hobart sink'); 'two degrees under code' = the identical clue figure 'o dva stupně pod normou' (Ch9); 'dvě stupnice' = two scales |
| 703 | `Spáry. Těsnění. Dřez dvě stupnice pod limitem na starém potrubí.` | `Spáry. Těsnění. Umyvadlo o dva stupně pod normou na starém potrubí.` | clue: same clue figure, same sink word |
| 703 | `Přesně tak, jak to stálo v úřední stížnosti,` | `Přesně tak, jak to stálo v té na stroji psané stížnosti,` | mistranslation: 'the typed complaint' |
| 705 | `„O Gretině dřezu se toho ví už tolik?“` | `„O Gretině umyvadle se toho ví už tolik?“` | clue: hand-sink = umyvadlo |
| 706 | `„V téhle branži se leccos doneslo.“` | `„V téhle branži se leccos donese.“` | mistranslation: 'One hears things' (present, general) |
| 707 | `Doneslo se. Otáčela jsem` | `Donese se. Otáčela jsem` | consistency: echo |
| 710 | `Byla to prostě tvrdá podnikatelka, která sice soucítí s cizím neúspěchem, ale v celém rozsahu tak, jak se sluší a patří.` | `Byla to prostě tvrdá podnikatelka, která má radost z klopýtnutí konkurentky a lituje přesně tam, kde se to sluší.` | reversed: EN 'glad of a rival's stumble and sorry in all the correct places' — MT made her sympathetic |
| 711 | `Znalost stavu spár ještě neznamená, že sypala mouku do větráků. Poskytla mi jen to, co věděla, a nic víc,` | `Znát spáry ještě neznamená sypat prášek. Dala mi jistotu a nic, s čím by se dalo něco dělat,` | mistranslation: garbled ('pouring flour into vents'); 'the recognition and nothing whatever to do with it' |
| 713 | `„Zelenočervený se zlatou mašlí, jestli by to šlo,“` | `„Jedlový se zlatou mašlí, jestli by to šlo,“` | mistranslation: 'Balsam and a gold bow' |
| 715 | `položeným přesně mezi tlapkami.` | `položeným přesně mezi nohama.` | mistranslation: a penguin has feet, not paws |
| 718 | `na Renéeninu mašli` | `na Renéeinu mašli` | typo: name form |
| 720 | `a u každé snítky jsem myslela na spárovací hmotu.` | `a u každé snítky jsem myslela na ty spáry.` | consistency: grout = spáry (Ch9, Ch16 — one term) |
| 722 | `Vím, že to byly vy.“` | `Vím, že jste to byla vy.“` | grammar: garbled |
| 724 | `otočila hlavu za papírovým sáňkem s medovými bonbóny.` | `otočila hlavu za papírovým sáčkem s medovými bonbóny.` | typo: sáňkem = sled |
| 729 | `když svítí světlo nad Petrovou kůlnou.“` | `když svítí světlo nad Peteovým skladem.“` | names: Pete (not Petr); locker = sklad |
| 731 | `„Jednoho rána jsem u zadku Gretina obchodu někoho viděl.` | `„Jednoho rána jsem vzadu u Gretina obchodu někoho viděl.` | mistranslation: 'u zadku' = at the backside (crude) |
| 731 | `Dlouhá zástěra, taková ta až ke kolenům, světlá, pod ní kabát. Stála u jejích zadních schodů a pak zamířila` | `Dlouhá zástěra, taková ta až po holeně, světlá, pod ní kabát. Chvíli stála u jejího zadního schodu a pak zamířila` | mistranslation: 'down to your shins'; 'a minute' dropped |
| 731 | `„Myslel jsem, že je to dovoza.“` | `„Myslel jsem, že je to nějaký rozvoz.“` | typo: 'dovoza' non-word |
| 734 | `Na Evergreen Street balil do zlata jen jeden obchod. Zlaté písmo na krabicích, zlatá stuha na finančerech. A stál na vzdáleném konci bloku, za lékárnou, kudy tou uličkou v tmu prošla` | `Na Evergreen Avenue balil do zlata jen jeden obchod. Zlaté písmo na krabicích, zlatá stuha na financierech. A stál na vzdáleném konci bloku, za lékárnou, kam tou uličkou ve tmě prošla` | consistency: street name; financier; 've tmě' |
| 739 | `se svým papírovým sáćkem plným sirupu` | `se svým papírovým sáčkem plným sirupu` | typo: 'sáćkem' |
| 742 | `a chci, aby tam byl někdo, kdo pozná zkažený základ, když ho uvidí.` | `a chci, aby tam byl někdo, kdo pozná kyselý základ, když ho uvidí.` | clue: sour base = kyselý základ (Ch11); 'zkažený' = spoiled — the whole point is that it is NOT spoilage |
| 743 | `„Myslíš, že to udělala ona.“` | `„Myslíte, že to udělala ona.“` | address: ruling 2: Doc ↔ Jessica formal (as Ch11 and the rest of Ch17) |
| 746 | `„Jejich zahajovací týden byl vytištěný` | `„Její zahajovací týden byl vytištěný` | grammar: 'Her opening week' |
| 746 | `A dnes ráno mi vyjmenovala spárovací hmotu, těsnění a dřez, což byly ty tři věci ve stížnosti. Nikdo na třídě kromě Gretry a inspektora je neznal.“` | `A dnes ráno mi vyjmenovala spáry, těsnění a umyvadlo, což byly ty tři věci ve stížnosti. Nikdo na třídě kromě Grety a inspektora je neznal.“` | clue: grout/hand-sink terms as Ch9/Ch16; 'Gretry' typo |
| 754 | `kde podle Renéina pravidla čekala` | `kde podle Renéeina pravidla čekala` | typo: name form |
| 760 | `„Někdo dal do Gretiny mouky zkažený základ,“ řekla jsem. „Kyselkavý chlebový základ, dost silný na to, aby zkvasilo všechno, co upekla. Dnes ráno jste mi jmenovala spárovací hmotu, těsnění a dřez` | `„Někdo dal do Gretiny mouky kyselý základ,“ řekla jsem. „Kyselinu, jakou používají pekárny chleba, dost na to, aby zkyslo všechno, co upekla. Dnes ráno jste mi jmenovala spáry, těsnění a umyvadlo` | clue: sour base = kyselý základ; 'a bread kitchen's acid'; grout/hand-sink terms |
| 761 | `Chvíli se ani pohnula.` | `Chvíli se ani nepohnula.` | reversed: negation missing |
| 761 | `To, co zbylo, bylo tvrdší a otoč víc upřímné.` | `To, co zbylo, bylo tvrdší a o dost upřímnější.` | typo: 'otoč' |
| 764 | `A pak vypadněte.“` | `A pak odejdete.“` | register: 'And then you'll leave' — Renée doesn't say 'get out' |
| 765 | `Zatímco doktor procházel dovnitř, stála s překříženýma rukama u dveří. Dělala to, jako by procházel stájí:` | `Zatímco to doktor procházel, stála s překříženýma rukama u dveří. Dělal to, jako by procházel stáj:` | grammar: subject confusion (Doc does it) |
| 765 | `Pytle mouky z portlandského mlýna,` | `Pytle mouky z portlandského velkoobchodu,` | mistranslation: 'the Portland house' = the bulk house (Ch3) |
| 765 | `Polotovar polevy v sáčcích plných lesklých kapiček.` | `Kuvertura v sáčcích plných lesklých kapiček.` | consistency: couverture = kuvertura (Ch3) |
| 766 | `„Špetka na padesát liber.` | `„Špetka na třiadvacet kilo.` | units: fifty pounds → 23 kg (safe arithmetic) |
| 766 | `Kdyby to byl kbelík se zkaženým základem, ucítil byste ho v okamžiku, kdy byste nadzvedl víko.` | `Kdyby to byl kbelík kyselého základu, ucítil by ho člověk v okamžiku, kdy by nadzvedl víko.` | clue: sour base = kyselý základ |
| 770 | `„Mouka, máslo, poleva, mandle, zlepšovač,“` | `„Mouka, máslo, kuvertura, mandle, zlepšovač,“` | consistency: couverture |
| 770 | `„Žádný zkažený základ. Na žádné stránce.“` | `„Žádný kyselý základ. Na žádné stránce.“` | clue: sour base = kyselý základ |
| 772 | `„A spárovací hmota?“ řekla jsem.` | `„A ty spáry?“ řekla jsem.` | consistency: grout = spáry |
| 774 | `„Spárovací hmota? To mi řekla Joyce Wendtová.` | `„Spáry? O těch mi řekla Joyce Wendtová.` | consistency: grout = spáry |
| 778 | `„Jalovec a zlatou mašli.“` | `„Jedlový se zlatou mašlí.“` | mistranslation: balsam (jalovec = juniper); echo of Ch16 wording |
| 784 | `„Byla sis jistá.“` | `„Byla jste si jistá.“` | address: ruling 2: Doc formal |
| 787 | `Jistá jsem si byla už od spolku,` | `Jistá jsem si byla už od spolkového domu,` | consistency: the Grange = spolkový dům |
| 787 | `Měla jsem leták a spárovací hmotu,` | `Měla jsem leták a ty spáry,` | consistency: grout = spáry |
| 787 | `Vysvětlovala mi čokoládovou polevu, jako bych nikdy nerozpouštěla čokoládu, dotkla se mého rukávu a s tím svým úsměvem litovala „chudinku Greet“.` | `Vysvětlovala mi kuverturu, jako bych nikdy nerozpouštěla čokoládu, dotkla se mého rukávu a s tím svým úsměvem o Gretě řekla chudák žena.` | clue: couverture; Renée's echoed words 'poor woman' (Ch3) — 'Greet' typo |
| 788 | `A když vyslovila Joyceino jméno, hodila jsem na Joyce jedním dechem to, co jsem Renée odepírala celý týden. Joyce tu spárovací hmotu samozřejmě znala. Pekařila hned vedle ní léta.` | `A když vyslovila Joyceino jméno, dopřála jsem Joyce jedním dechem to, co jsem Renée celý týden upírala. Joyce ty spáry samozřejmě znala. Pekla hned vedle nich léta.` | reversed: EN 'I had GIVEN Joyce in a breath what I had refused Renée' (the benefit of the doubt) — MT 'threw at Joyce' made it blame |
| 789 | `Viděla jsem je, jak to dělají Petrovi kvůli řetězu na brance` | `Viděla jsem je, jak to dělají Peteovi kvůli řetězu na bráně` | names: Pete; gate = brána |
| 789 | `Přivedla jsem ho, protože jsem si byla tak jistá, že mi to vyvrátí.` | `Přivedla jsem ho, protože jsem si byla tak jistá, že mi to neřekne.` | reversed: EN 'because I had been so certain he would not' |
| 790 | `a uličkou v tmu kráčela štíhlá postava.` | `a uličkou ve tmě kráčela štíhlá postava.` | grammar: ve tmě |
| 796 | `notes zapomenutý v rukavici.` | `notes zapomenutý v palčáku.` | mistranslation: craft word: mitten = palčák |
| 798 | `Dovnitř nepršela déšť, ale tál sníh z předchozího dne,` | `Dovnitř nepršelo, ale tekl roztátý sníh z předchozího dne,` | grammar: ungrammatical |
| 800 | `a připomínalo to kárný pohřeb, kde tělo ještě ani nevychladlo.` | `a připomínalo to tryznu, kde tělo ještě ani nevychladlo.` | mistranslation: 'kárný' = disciplinary; 'a wake' |
| 800 | `zatímco na podlaze stála čtvrt palce hnědé vody` | `zatímco na podlaze stál půl centimetru hnědé vody` | units: a quarter-inch → ~0.5 cm (safe) |
| 801 | `„Nenapoví hned rázné ne.` | `„Rovnou ne neřekne.` | grammar: garbled |
| 802 | `a prosak byl od ní daleko. Díky šesti čistým stopám a čisté milosti byla v bezpečí.` | `a průsak byl od ní daleko. Díky dvěma metrům a čiré milosti byla v bezpečí.` | units: six feet → 2 m (safe); 'prosak' typo |
| 803 | `Ten hřejivý pocit z jízdy, cédrová krabice plnící se na faře, zakladatelova linie v každém okně` | `Ten hřejivý pocit ze sbírky, cedrová krabice plnící se ve spolkovém domě, věta zakladatelky v každém okně` | mistranslation: 'the drive' (sbírka, not a ride); Grange = spolkový dům (not a rectory); the founder's LINE = věta |
| 804 | `Renéiny zásoby otevřené doktorovi police po polici,` | `Renéeiny zásoby otevřené doktorovi police po polici,` | typo: name form |
| 804 | `Přiotrávená bedna mouky a anonymní stížnost,` | `Nadávkovaná nádoba s moukou a na stroji psaná stížnost,` | no-poison: EN 'A dosed flour bin and a typed complaint' — MT 'slightly poisoned'; bin = nádoba |
| 808 | `kterou jsem ho dřív pozorovala dělat s jeho kovovými sponami,` | `kterou jsem ho dřív pozorovala dělat s jeho hřebíčky,` | consistency: brads = hřebíčky (Ch6) |
| 810 | `církevní zápis rozměklý ve skladu,` | `církevní zápis rozměklý v přehybu,` | mistranslation: 'gone to pulp at the fold' |
| 813 | `O dvě města dál žil hodinář, který takové věci vykupoval.` | `O dvě města dál žil klenotník, který takové věci vykupoval.` | mistranslation: jeweler (Ch26 payoff) |
| 817 | `„Sám tyhle do příchodu vlhka a plísně nedokončíš.“` | `„Sám tohle nestihnete, než se do toho vlhka dá plíseň.“` | address: ruling 2: Theo formal |
| 819 | `Było to to jediné, co jsem měla` | `Bylo to to jediné, co jsem měla` | leak: Polish spelling 'Było' |
| 828 | `„Tak spust‘.“` | `„Tak spusť.“` | typo: apostrophe for háček |
| 829 | `Nikdo mě nenechal zatlačit do kouta od chvíle, kdy to celé začalo. Všechna rozhodnutí jsem udělala nejdřív a fakta si pak ohla podle toho.` | `Od chvíle, kdy to celé začalo, jsem nikomu nedovolila, aby mě tlačil. Všechno jsem rozhodla nejdřív a fakta jsem si pak ohnula podle toho.` | reversed: EN 'I haven't let anyone push me' (her doing, not others'); 'ohla' typo |
| 832 | `„V kontejneru za Fenwickovic domem, kde to vybydlela, aby si tam mohla nechat postavit pece.“` | `„V kontejneru za Fenwickovic domem, kde to vybourala, aby si tam mohla postavit pece.“` | mistranslation: 'gutted it' (vybydlet = to make derelict) |
| 836 | `„Kdokoliv tu cihlu hodil, vznětlivý nebyl.` | `„Kdokoliv tu cihlu hodil, nejednal ve vzteku.` | mistranslation: 'wasn't in a temper' |
| 836 | `A Renée mě usadila a spočítala mi městské kostelní bály.` | `A Renée mě usadila a spočítala mi městské kostelní večeře.` | mistranslation: church suppers (not balls) |
| 837 | `„Nebo si myslela, že se po maltě nikdo dvakrát ohlížet nebude.“` | `„Nebo si myslela, že se na maltu nikdo dvakrát nepodívá.“` | mistranslation: 'look twice' |
| 838 | `„Já se ohlédla dvakrát,“` | `„Já se podívala dvakrát,“` | mistranslation: 'I looked twice' |
| 844 | `„To mohla. Žena, která nepustí tučňáka přes prášek, a nosí si pudr do práce v krabici se jménem obchodu na boku.“` | `„To mohla. Žena, která nepustí tučňáka přes svůj práh, a nosila by si prášek do práce v krabici se jménem svého obchodu na boku.“` | mistranslation: garbled ('over her step' → 'over the powder'; 'pudr' = face powder) |
| 847 | `„Petova dodávka,“ řekla jsem. „Řekl mi to dvakrát. Poprvé u jeho bloku, nad tvojí pečení. Dodávka nahoře u lékárny před rozedněním. Zhasnutá světla. Ne od řezníka.` | `„Ta dodávka, co viděl Pete,“ řekla jsem. „Řekl mi to dvakrát. Poprvé u jeho špalku, nad tvojí pečení. Dodávka nahoře u lékárny před rozedněním. Zhasnutá světla. Ne od dodavatele masa.` | mistranslation: 'Pete's van' = the van Pete saw; 'block' = chopping block; 'the meat man' = the supplier |
| 849 | `a říkal, že to nebylo řezníkovo, a já neslyšela nikoho.“` | `a říkal, že to nebyl dodavatel masa, a já to vzala jako ničí.“` | mistranslation: 'and I heard nobody's' |
| 849 | `Štíhlá a rychlá, u Gretina okenního parapetu, než se rozhořely pece, a pryč nahoru ke vzdálenému konci. Slyšela jsem o zlatém obchodě.` | `Štíhlá a rychlá, na Gretině prahu, než se rozhořely pece, a pryč nahoru ke vzdálenému konci. Já v tom slyšela ten zlatý obchod.` | mistranslation: sill = práh (door sill, Ch12); 'I heard the gold shop' = she read it in |
| 851 | `Mohla vyjít ze dveří, dolů ke Gretinu oknu a zase zpátky domů,` | `Mohla vyjít ze dveří, dolů ke Gretinu prahu a zase zpátky domů,` | consistency: sill = práh |
| 855 | `zbytek zamířil na náves a naklonil se v uličce směrem k tvému ohništi. Tenhle se vydal na druhou stranu, deset stop od jejich společnosti,` | `zbytek zamířil na náves a naklonil se nahoru k Hollyhock Lane, k tvému krbu. Tenhle se vydal na druhou stranu, tři metry od jejich společnosti,` | mistranslation: lane vs alley (the clue alley is ulička); ten feet → 3 m |
| 855 | `kde by mohla dodávka zastavit z třídy` | `kde mohla dodávka sjet z třídy` | grammar: garbled |
| 861 | `Strčila jsem do misky. „V cechu jsem to četla tak, že věděla o blížícím se uzavření. Nemůžeš přece vytisknout zahájení něčeho, co se ještě neuzavřelo.“` | `Odstrčila jsem misku. „Ve spolkovém domě jsem to četla tak, že věděla o blížícím se uzavření. Nemůžeš přece načasovat otevření na uzavření, které se ještě nestalo.“` | mistranslation: Grange = spolkový dům (cech = guild); the logic sentence was garbled |
| 865 | `„A ne naopak. Měla jsem to od schodů v cechu obráceně.“` | `„A ne naopak. Měla jsem to od schodů spolkového domu obráceně.“` | consistency: Grange = spolkový dům |
| 867 | `Pak se doktor ve čtvrtek podíval do jejího skladu a nezbyl tam ani kousek kvásku a ona mi řekla, kdo jí to vykládal o Gretině spáře.“` | `Pak se doktor ve čtvrtek podíval do jejího skladu a nebylo tam ani zrnko kyselého základu a ona mi řekla, kdo jí vykládal o Gretiných spárách.“` | clue: sour base = kyselý základ (kvásek = sourdough starter, the very thing it replaces); grout = spáry |
| 867 | `a napsal na kraj stížnost, aby do toho spadla.“` | `a napsal na okres stížnost, aby do něj spadla.“` | consistency: county = okres |
| 873 | `a s konvicí na plotě pro každého,` | `a s konvicí na plotně pro každého,` | typo: plot = fence |
| 875 | `„Jessica. Výborně,“ řekla Olivia. „Pojď Mařtě vysvětlit, že se nezbláznila.“` | `„Jessiko. Výborně,“ řekla Olivia. „Pojď Marthě vysvětlit, že se nezbláznila.“` | names: Martha rendered 'Marta/Maří' in Ch20; vocative |
| 876 | `„Nikdy jsem neřekla, že se zbláznila,“` | `„Nikdy jsem neřekla, že jsem se zbláznila,“` | grammar: person |
| 876 | `„Včera mi někdo volal, zrovna když jsme večeřeli.` | `„Včera mi někdo volal, zrovna při večeři.` | mistranslation: Martha is a widow living alone |
| 876 | `Dva čokoládově pekanové koláče a tucet housek,` | `Dva čokoládovo-pekanové koláče a tucet housek,` | consistency: one form |
| 877 | `Pip došla až k Mařiným kolenům. Natáhla krk a dvakrát ťukla zobákem do rozsvíceného displeje, dokud nezatměvl.` | `Pip došla až k Marthiným kolenům. Natáhla krk a dvakrát ťukla zobákem do rozsvíceného displeje, dokud nezhasl.` | names: Martha; 'nezatměvl' non-word |
| 879 | `„Hned po Mařině.` | `„Hned po Marthině.` | names: Martha |
| 883 | `týden před Hallowenem.“` | `týden před Halloweenem.“` | typo: Halloween |
| 884 | `Posadila se do křesla, které mi Olivia přisunula,` | `Posadila jsem se do křesla, které mi Olivia přisunula,` | grammar: first-person narrator dropped |
| 885 | `Říkala, že vyřizuje řidiče.` | `Prý odpovídala řidiči.` | consistency: echo of Ch4 'Odpovídám řidiči' |
| 890 | `ještě jednou se ohlédla po Mařině klíně.` | `ještě jednou se ohlédla po Marthině klíně.` | names: Martha |
| 894 | `„Ten dřez pořád ještě nedorazil,“ spustila dřív, než jsem stačila pozdravit. „Tom dělal těsnění ve čtvrtek. Spáry jsem zaspárovala sama. A krajští nepřijdou, dokud nebude dřez v pořádku.“` | `„Ten díl k umyvadlu pořád ještě nedorazil,“ spustila dřív, než jsem stačila pozdravit. „Tom dělal těsnění ve čtvrtek. Spáry jsem zaspárovala sama. A z okresu nepřijdou, dokud nebude umyvadlo v pořádku.“` | clue: 'the sink part' — hand-sink = umyvadlo (dřez is Joyce's 'Hobart sink'); county = okres |
| 901 | `Dva čokoládově pekanové koláče a tucet housek.` | `Dva čokoládovo-pekanové koláče a tucet housek.` | consistency: one form |
| 903 | `„Odkud začaly chodit objednávky na Díkůvzdání.` | `„Od té doby, co začaly chodit objednávky na Díkůvzdání.` | grammar: garbled |
| 904 | `a krev se jí vyhrnula z tváře.` | `a z tváře se jí vytratila barva.` | reversed: 'the color went out of her face' (MT: blood rushed out/up) |
| 910 | `„Je to mrazicí box. Odjakživa to byl mrazicí box pro Harolda,` | `„Je to chladicí box. Odjakživa to byl chladicí box pro Harolda,` | clue: walk-in = chladicí box everywhere (Ch9 Varney, Ch17 Renée's) — 'mrazicí' (freezer) broke the one-word rule |
| 910 | `A ten dřez u zadních dveří. Starý mixér Hobart stál vedle něj léta, dokud neodešel motor, takže tomu říkala hobartský dřez,` | `A to umyvadlo u zadních dveří. Starý mixér Hobart stál vedle něj léta, dokud neodešel motor, takže mu říkala hobartský dřez,` | clue: hand-sink = umyvadlo; Joyce's own word = hobartský dřez (kept distinct) |
| 910 | `Říkala jsem mrazicí box. Donutila jsem se k tomu.“` | `Říkala jsem chladicí box. Donutila jsem se k tomu.“` | clue: walk-in = chladicí box |
| 912 | `„Pete říká, že ti zase vyskakuje zámek od branky,“` | `„Pete říká, že ti pořád padá zámek z brány,“` | clue: gate = brána (the gate-key clue); 'keeps coming off' |
| 913 | `Sundává ho, aby dělal ramena kvůli mé závuře.“` | `Sundává ho, aby mi ukázal, co si myslí o mé petlici.“` | mistranslation: hasp = petlice (Ch7); 'to make a point' |
| 915 | `a mě o tom klíči od branky ani nenapadlo přemýšlet. Je to stejný zámek, jaký na té brance visel, odkud ho Harold pověsil.` | `a mě o tom klíči od brány ani nenapadlo přemýšlet. Je to stejný zámek, který na té bráně visí od té doby, co ho tam pověsil Harold.` | clue: the gate key — gate = brána; garbled clause |
| 915 | `Co by proboha chtěla s mojí brankou?“` | `Co by proboha chtěla s mojí bránou?“` | clue: gate = brána |
| 919 | `kousek od místa, kde se prodřela lišta a kde na konci protější stěny popraskaly spáry.` | `kousek od místa, kde se prodřelo těsnění pod dveřmi a kde u paty protější stěny popraskaly spáry.` | clue: weather-strip = těsnění (complaint item) |
| 921 | `„V pondělí mi přinesla tuňákové nudle.` | `„V pondělí mi přinesla těstoviny s tuňákem.` | consistency: Ch12 'Těstoviny s tuňákem' |
| 923 | `Pochovala mého prvního potomka dřív než Harold,` | `Chovala moje první miminko dřív než Harold,` | mistranslation: 'pochovala' also reads as 'buried' — EN 'held my first baby' |
| 244 | `Velkoobchod. Pro hostince a nemocnici.` | `Velkoobchod. Pro penziony a nemocnici.` | consistency: inns = penziony (Ch4 'do penzionu', Ch21) |
| 938 | `a tlapkou plácala do smyčky kabelu,` | `a ploutví plácala do smyčky kabelu,` | mistranslation: a penguin has flippers |
| 939 | `Gretiin hlas byl plochý a unavený,` | `Gretin hlas byl plochý a unavený,` | typo: possessive form |
| 940 | `Kdyby si nějaká pekárna chtěla obstarat surový základ na kvásek, kam by si pro něj poslala?“` | `Kdyby si nějaká pekárna chleba chtěla obstarat kyselý základ, kam by si pro něj poslala?“` | clue: sour base = kyselý základ (MT 'raw base for a starter') |
| 944 | `která stála na taburetku` | `která stála na taburetu` | typo: case |
| 953 | `To ráno po rozbitém výkladním skříni stála na třídě` | `To ráno po rozbité výloze stála na třídě` | grammar: agreement |
| 954 | `„To je přece Gretiina Joyce.“` | `„To je přece Gretina Joyce.“` | typo: possessive form |
| 955 | `*Má její webovka fotku té dodávky?*` | `„Má její webovka fotku té dodávky?“` | dialogue: Jessica's spoken line was set as an asterisk span instead of „…“ dialogue (EN quotes it) |
| 956 | `takže přímo zezadu by Petr v tmy nikdy nezahlédl ani písmenko.` | `takže přímo zezadu by Pete ve tmě nikdy nezahlédl ani písmenko.` | names: Pete; 've tmě' |
| 961 | `Petr zametal piliny ke dveřím, tabule s nápisem už byla otočená a poslední zákazník odcházel` | `Pete zametal piliny ke dveřím, tabulka na dveřích už byla otočená a poslední zákaznice odcházela` | names: Pete; the last customer is a woman ('under her arm') |
| 963 | `„Říkal jsi, že tam nahoře u lékárny` | `„Říkal jste, že tam nahoře u lékárny` | address: ruling 2: Jessica ↔ Pete formal |
| 965 | `„To je ona,“ řekl Petr.` | `„To je ona,“ řekl Pete.` | names: Pete |
| 966 | `„Řekl bys to náčelnici?“` | `„Řekl byste to náčelnici?“` | address: ruling 2 |
| 969 | `„Řekni jí, že jsem to zrovna zametl.“` | `„Řekněte jí, že jsem to zrovna zametl.“` | address: ruling 2 |
| 974 | `„Doktor našel v Gretiině mouce kvásek,“ řekla jsem. „Takový ten druh, co si pekárny kupují na žitný chléb. Jedna pekárna v Bridgtonu obvolávala Gretiiny zákazníky` | `„Doktor našel v Gretině mouce kyselý základ,“ řekla jsem. „Takový ten druh, co si pekárny kupují na žitný chléb. Jedna pekárna v Bridgtonu obvolávala Gretiny zákazníky` | clue: sour base = kyselý základ (kvásek = starter); possessive form |
| 974 | `dodal na podzim kvásek do Wendt's Bakehouse?“` | `dodal na podzim kyselý základ do Wendt's Bakehouse?“` | clue: sour base = kyselý základ |
| 981 | `s Pip spící u nohou na dodávce.` | `s Pip spící u jeho nohou na papíru s dodávkou.` | mistranslation: Pip sleeps on the printed van page |
| 982 | `„Našla to na notebooku u kuchyňského stolu.` | `„Našel to na notebooku u kuchyňského stolu.` | gender: Bob Pelkey is a man |
| 982 | `Jedno pytel jejich kvásku každých pár týdnů, na žitný chléb, který pekl pro hotely, hezky až do června. Pak nic. Říká, že o tu velkou zakázku pro hotel přes léto přišla,` | `Jeden pytel jejich kyselého základu každých pár týdnů, na žitný chléb, který pekla pro penziony, hezky až do června. Pak nic. Říká, že o tu velkou zakázku pro penzion přes léto přišla,` | clue: sour base = kyselý základ; Joyce baked (pekla); inns = penziony |
| 984 | `„List s výrobkem mi už poslala e-mailem` | `„List s výrobkem mi už poslal e-mailem` | gender: Pelkey (male) sent it |
| 988 | `Nemůžu ti zaručit, že to vypadlo zrovna z toho pytle.` | `Nemůžu vám zaručit, že to vypadlo zrovna z toho pytle.` | address: ruling 2: Doc formal |
| 989 | `pak stránku otrhl a podal mi ji.` | `pak stránku utrhl a podal mi ji.` | typo: otrhl |
| 972 | `Noriko Tanaka zvedla telefon a řekla své příjmení.` | `Noriko Tanaková zvedla telefon a řekla své příjmení.` | consistency: surname form Tanaková (Ch6, Ch22+) |
| 982 | `řekla Tanaka.` | `řekla Tanaková.` | consistency: surname form |
| 994 | `Vedle něj ležel Docův lístek,` | `Vedle něj ležel doktorův lístek,` | consistency: Doc = doktor everywhere else |
| 994 | `a v kamenech ještě dohoříval` | `a v kamnech ještě dohoříval` | typo: kamenech = stones |
| 997 | `Kdybych toho týdne vyslovila Renéino jméno v sále,` | `Kdybych toho týdne vyslovila Renéeino jméno v sále,` | typo: name form |
| 999 | `Nick sesšel dolů v ponožkách,` | `Nick sešel dolů v ponožkách,` | typo: 'sesšel' |
| 1000 | `„Tanaka,“ řekla jsem.` | `„Tanaková,“ řekl.` | mistranslation: EN: Nick says it ('he said') — speaker swapped |
| 1001 | `„Tanaka. Žádný sál.“` | `„Tanaková. Žádný sál.“` | consistency: surname form |
| 1006 | `„Jessiko,“ řekla Tanaková. „Sedněte si.“` | `„Jessiko,“ řekla Tanaková. „Sedni si.“` | address: ruling 2: Noriko ↔ Jessica informal (first names since Inn Trouble; Ch21 phone already ty) |
| 1007 | `Nepísala, když právě rozhodovala,` | `Nepsala, když právě rozhodovala,` | typo: 'Nepísala' (Slovak) |
| 1009 | `ležela otevřená na pultě ráno, co vzali výlohu,“` | `ležela otevřená na pultě to ráno, kdy rozbili výlohu,“` | mistranslation: 'the morning the window went' |
| 1011 | `„Ve stížnosti označili chladicí box za chladírnu a dřez na nádobí za Hobartův dřez. Greta říká, že takhle tomu nikdo neříkal od dob Joyce. Zámek na brance do dvora se nikdy neměnil a Pete říká, že pořád vyskakuje. A kysnutí přestalo ráno potom, co Greta začala po tom kamenu zamykat zadní dveře západkou, takže ten, kdo to dělal, chodil tudy. Viděl před rozedněním dodávku u lékárny, bez světel, a nebyl to řezníkův chlap.` | `„Stížnost nazvala chladicí box chladírnou a umyvadlo hobartským dřezem. Greta říká, že takhle tomu nikdo neříkal od dob Joyce. Zámek na bráně do dvora se nikdy neměnil a Pete říká, že pořád padá. A kysnutí přestalo ráno potom, co Greta začala po té cihle zamykat zadní dveře na závoru, takže ten, kdo to dělal, chodil tudy. Pete viděl před rozedněním dodávku u lékárny, bez světel, a nebyl to dodavatel masa.` | clue: the Ch22 recap: walk-in = chladicí box / Joyce's 'chladírna'; hand-sink = umyvadlo / 'hobartský dřez' (MT 'dish sink'); gate = brána; 'kamenu' = stone (it was the brick); subject Pete restored; meat man = supplier |
| 1012 | `„Mluvte dál.“` | `„Pokračuj.“` | address: ruling 2: Noriko ↔ Jessica informal |
| 1013 | `„Danny Ott viděl před rozedněním u Gretina parapetu štíhlou,` | `„Danny Ott viděl před rozedněním na Gretině prahu štíhlou,` | consistency: sill = práh |
| 1013 | `Dotkla se složeného papíru v mém klíně. „Renéin leták` | `Dotkla jsem se složeného papíru v klíně. „Renéein leták` | grammar: first-person; name form |
| 1013 | `Leták se na nástěnku spolku dostal až třicátého.` | `Leták se na nástěnku spolkového domu dostal až třicátého.` | consistency: Grange = spolkový dům |
| 1013 | `A Docova poznámka říká, že prášek v mé sklenici odpovídá kyslému základu, test za testem.“` | `A doktorova poznámka říká, že prášek v mé sklenici odpovídá kyselému základu, test za testem.“` | clue: sour base = kyselý základ ('kyslému' typo); Doc = doktor |
| 1019 | `„Řekl.“` | `„Řekl by.“` | grammar: conditional |
| 1022 | `Zlatá na etiketě, říkala jste.“` | `Zlatá na etiketě, říkala jsi.“` | address: ruling 2 |
| 1023 | `„Myslím, že z popelnice za Sugarplum,` | `„Myslím, že z kontejneru za Sugarplum,` | consistency: dumpster = kontejner (Ch1, Ch15, Ch19) |
| 1023 | `protože ve čtvrtek bych to už neučinila.` | `protože ve čtvrtek bych to neudělala.` | mistranslation: 'on Thursday I wouldn't have' |
| 1025 | `„Jak to provedete?“` | `„Jak to uděláš?“` | address: ruling 2 |
| 1028 | `„Seděla jsem s vámi minulý měsíc ve Fionině obývacím pokoji. Vím, jak tyhle věci ráda děláte.` | `„Seděla jsem s tebou minulý měsíc ve Fionině obývacím pokoji. Vím, jak tyhle věci ráda děláš.` | address: ruling 2 |
| 1031 | `Neví, že to dokážeme dokázat.“` | `Neví, že to umíme dokázat.“` | grammar: tautology |
| 1040 | `Pip ustoupila o krok zpět před hlubokým žárem a hluboce, formálně se uklonila zkřivenému ptákovi na jejím boku` | `Pip ustoupila o krok zpět před žárem a hluboce, formálně se uklonila zkřivenému ptákovi na boku konvice` | grammar: garbled |
| 1043 | `„Greto –“` | `„Greto—“` | dialogue: dossier: interruption = em dash, no space |
| 1044 | `„Seděla jsem s tou ženou patnáct let v sousední lavici.“` | `„Patnáct let jsem s tou ženou pracovala u vedlejšího stolu.“` | mistranslation: a baker's bench, not a pew |
| 1050 | `tady je Noriko Tanaková, vedoucí policie ve Frost Falls.` | `tady je Noriko Tanaková, náčelnice policie ve Frost Falls.` | consistency: chief = náčelnice (Ch6) |
| 1058 | `Gretičiny` | `Gretiny` | consistency: Greta's possessive rendered 'Gretičin-' (garbled diminutive) → Gretin- |
| 1067 | `Gretičiny` | `Gretiny` | consistency: Greta's possessive rendered 'Gretičin-' (garbled diminutive) → Gretin- |
| 1088 | `Gretičiny` | `Gretiny` | consistency: Greta's possessive rendered 'Gretičin-' (garbled diminutive) → Gretin- |
| 1099 | `Gretičiny` | `Gretiny` | consistency: Greta's possessive rendered 'Gretičin-' (garbled diminutive) → Gretin- |
| 1104 | `Gretičiny` | `Gretiny` | consistency: Greta's possessive rendered 'Gretičin-' (garbled diminutive) → Gretin- |
| 1065 | `Gretičině` | `Gretině` | consistency: Greta's possessive rendered 'Gretičin-' (garbled diminutive) → Gretin- |
| 1067 | `Gretičiným` | `Gretiným` | consistency: Greta's possessive rendered 'Gretičin-' (garbled diminutive) → Gretin- |
| 1087 | `Gretičinu` | `Gretinu` | consistency: Greta's possessive rendered 'Gretičin-' (garbled diminutive) → Gretin- |
| 1110 | `Gretičina` | `Gretina` | consistency: Greta's possessive rendered 'Gretičin-' (garbled diminutive) → Gretin- |
| 1098 | `Gretičin ` | `Gretin ` | consistency: Greta's possessive rendered 'Gretičin-' (garbled diminutive) → Gretin- |
| 1087 | `Gretičin.` | `Gretin.` | consistency: Greta's possessive rendered 'Gretičin-' (garbled diminutive) → Gretin- |
| 1055 | `a nikdo ji nenapadlo odmítnout.` | `a nikoho nenapadlo ji odmítnout.` | grammar: case |
| 1065 | `a měla jsem ji ráda v besedním sále s náručí chleba` | `a měla jsem ji ráda ve spolkovém domě s náručí chleba` | consistency: the Grange = spolkový dům |
| 1067 | `přesně slovo od slova podle Gretiny knížky. Vy jste tou knížkou seděla ráno po výloze s telefonem v ruce.“` | `přesně slovo od slova podle Gretiny knihy. Vy jste u té knihy seděla to ráno, kdy rozbili výlohu, s telefonem v ruce.“` | clue: the order book = kniha objednávek; 'sat beside that book' (garbled) |
| 1069 | `„Stížnost na úřadě označovala její chladírnu za mrazírnu a její dřez za dřez značky Hobart. Greta říká, že tomu tak nikdo neříká od té doby, co vy.“` | `„Stížnost na okres nazvala její chladicí box chladírnou a její umyvadlo hobartským dřezem. Greta říká, že tak tomu nikdo neříká od té doby, co jste odešla vy.“` | clue: REVERSED: MT had the walk-in called 'chladírna' and the slip-word as 'mrazírna' — Joyce's word must be 'chladírna' (as she answers in the next line) and the hand-sink 'hobartský dřez' |
| 1071 | `„Doktor Mitchell našel v jejím moučném základu stopové množství kyselého základu. Pelkey's vám ho doručil v pytli sedmadvacátého října, potom co ho měsíce neměli.` | `„Doktor Mitchell určil, že prášek v její mouce je kyselý základ. Pelkey's vám pytel doručil sedmadvacátého října, po měsících, kdy jste žádný neodebírala.` | mistranslation: 'matched the powder in her flour to a sour base' (MT: 'trace amount in her flour base'); 'after months of none' = Joyce had bought none |
| 1072 | `„Peču žitný, šéfe.“` | `„Peču žitný chleba, náčelnice.“` | consistency: Chief = náčelnice |
| 1074 | `„Pete Garcia má na ten krám pifku už od chvíle, kdy –“` | `„Pete Garcia má na ten krám pifku už od chvíle, kdy—“` | dialogue: interruption = em dash, no space (dossier) |
| 1075 | `„Kdo to byl, vnikl dovnitř přes branku mého dvorku,“` | `„Ať to byl kdokoli, vnikl dovnitř přes bránu mého dvora,“` | clue: gate = brána |
| 1077 | `„Pete má na té brance svůj řetěz,“` | `„Pete má na té bráně svůj řetěz,“` | clue: gate = brána |
| 1077 | `Druhý jsem nechala udělat pro vás v roce, kdy jsme otevřely, a nikdy jsem ho nechtěla zpátky.“` | `Druhý jsem nechala udělat pro tebe v roce, kdy jsme otevřely, a nikdy jsem si o něj neřekla zpátky.“` | address: ruling 2: Greta ↔ Joyce informal (both say ty elsewhere in the scene) |
| 1078 | `Joyce ruka sjela ke klíčům a zakryla je.` | `Joyceina ruka sjela ke klíčům a zakryla je.` | grammar: possessive |
| 1079 | `zobák popojel o palec nahoru` | `zobák se zvedl o kousek výš` | units: an inch → idiom |
| 1087 | `s receptem na pekanový koláč mé matky a librou čokolády, kterou jsme si nemohly dovolit.` | `s receptem na pekanový koláč mé matky a půl kilem čokolády, které jsme si nemohly dovolit.` | units: a pound of chocolate → ½ kg (safe) |
| 1087 | `na Gretinu čokoládovo-pekanovou dobrotu. V té krabici v besedním sále je kartička s receptem.` | `na Gretin čokoládovo-pekanový koláč. V té krabici ve spolkovém domě je kartička s receptem.` | consistency: the pie; Grange = spolkový dům |
| 1088 | `Gretiny ruce se na stole spojené.` | `Gretiny ruce se na stole sepjaly.` | grammar: no verb |
| 1089 | `a pořád mám ty útržky v krabici od bot, jestli si je chceš pročíst.` | `a pořád mám ty útržky v krabici od bot, jestli si je náčelnice bude chtít přečíst.` | mistranslation: EN 'if the chief wants to read them' |
| 1096 | `Zavolala jsi Martě. Chtěla jsi mít můj Den díkůvzdání na mém vlastním pultu, každé jméno v té knize.` | `Zavolala jsi Marthě. Chtěla jsi mi vzít můj Den díkůvzdání z mého vlastního pultu, každé jméno v té knize.` | names: Martha; 'had my Thanksgiving off my own counter' |
| 1098 | `Gretin hlas ztišil.` | `Gretin hlas se ztišil.` | grammar: reflexive missing |
| 1099 | `Joyce se otevřela ústa.` | `Joyce otevřela ústa.` | grammar: ungrammatical |
| 1111 | `bez přemýšlení našla správný klíč` | `aniž se podívala, našla správný klíč` | mistranslation: 'without looking' |
| 1116 | `schovala ho do kapsy kabátu a přitlačila patku knoflíkem, aby zůstal na místě.` | `schovala ho do kapsy kabátu a zapnula přes něj klopu kapsy.` | mistranslation: 'buttoned the flap down over it' |
| 1118 | `Náčelnice Tanaka měla obvinění sepsaná` | `Náčelnice Tanaková měla obvinění sepsaná` | consistency: surname form |
| 1119 | `Žádná chodba. Žádný dav. Můj pohár s moukou si z doktorovy uzamčené skříňky` | `Žádný sál. Žádný dav. Moji sklenici s moukou si z doktorovy uzamčené skříňky` | mistranslation: 'No hall' (echo of Ch22 'Žádný sál'); the preserving jar, not a goblet |
| 1121 | `„Dva body obvinění,“ pronesla Tanaka a otevřela zápisník na podložce na stůl. „Poškozování cizí věci. To je ta mouka, ten zkažený kvásek, kterým zničila čtyři várky Gretina těsta.` | `„Dva body obvinění,“ pronesla Tanaková a otevřela zápisník na psací podložce. „Poškozování cizí věci. To je ta mouka, ten kyselý základ, kterým zničila čtyři várky Gretina těsta.` | clue: sour base = kyselý základ (MT 'spoiled starter' in the charge itself) |
| 1123 | `„Křivé obvinění nahlášené zdravotnickému úřadu. Ta stížnost. Chladicí místnost a dřez Hobart, úředně sepsané a odeslané na kraj,` | `„Křivé oznámení hygienickému úřadu. Ta stížnost. Chladírna a hobartský dřez, napsané na stroji a odeslané na okres,` | clue: Joyce's two words as in Ch9/20/22/23 (chladírna / hobartský dřez); 'typed up'; county = okres |
| 1125 | `Tanaka obrátila stránku.` | `Tanaková obrátila stránku.` | consistency: surname form |
| 1127 | `Řekněte jí, ať si připraví účtenky.` | `Řekni jí, ať si připraví účtenky.` | address: ruling 2: Noriko ↔ Jessica informal |
| 1129 | `Podívala se na Joyce přes náčelnici a to jí stačilo.` | `Podívala se na Joyce přes náčelničin stůl a to jí stačilo.` | mistranslation: 'across the chief's table' |
| 1130 | `řekla Tanaka. „Wendtovi mají státní licenci` | `řekla Tanaková. „Wendt's má státní licenci` | consistency: surname form; the business, not a family |
| 1132 | `„To nenašel. Kvásek je potravina. Zkazí akorát nesprávné těsto.“` | `„To nenašel. Kyselý základ je potravina. Zkazí akorát nesprávné těsto.“` | clue: sour base = kyselý základ |
| 1132 | `a odběr zrušila. Inspektor říká, že řidiči volaly dvě hostince` | `a odběr pozastavila. Inspektor říká, že řidiči volaly dva penziony` | mistranslation: 'suspended the account'; inns = penziony |
| 1133 | `položila ji na stůl vedle Tanakina zápisníku.` | `položila ji na stůl vedle zápisníku Tanakové.` | consistency: surname form |
| 1134 | `„Děkuji,“ řekla jí Tanaka` | `„Děkuji,“ řekla jí Tanaková` | consistency: surname form |
| 1136 | `Vracela jsem se Evergreenovou ulicí kolem Holly Jolly. Pořád ještě měla zavřeno, žlutá výstražná cedule kraje visela ve výloze,` | `Vracela jsem se po Evergreen Avenue kolem Holly Jolly. Pořád ještě měla zavřeno, žlutá vyhláška okresu visela ve výloze,` | consistency: street name; county = okres |
| 1138 | `pod větví balzámové jedle se zlatou mašlí, kterou jsem na dveře pověsila v pátek.` | `pod jedlovým věncem se zlatou mašlí, který jsem na dveře pověsila v pátek.` | mistranslation: the balsam WREATH (Ch16/17 payoff), not a branch |
| 1143 | `a obvinila vás, že jste zkazila Gretino těsto.` | `a obvinila vás, že jste Gretě zkazila mouku.` | mistranslation: 'soured Greta's flour' |
| 1144 | `rovnala do vitríny z tácku jednoho finančníka za druhým` | `rovnala do vitríny z tácku jeden financier za druhým` | mistranslation: financier = the cake |
| 1147 | `„Člověk by řekl, že ta cihla se z mého popelnice objevila úmyslně.` | `„Jak jsem pochopila, ta cihla pocházela z mého kontejneru úmyslně.` | mistranslation: 'One gathers'; dumpster = kontejner; 'popelnice' gender error |
| 1152 | `Pip zamířila rovnou k cihlovému krbu,` | `Pip zamířila rovnou ke krbu z polních kamenů,` | mistranslation: fieldstone hearth (Ch8) |
| 1154 | `„Zní to jinak než ten předchozí případ,“ podotkl.` | `„Tohle je jiný pocit než minule,“ podotkl.` | mistranslation: 'Feels different than the last one' |
| 1155 | `„Theo k tomu všemu přišel, jakmile ho našli,“` | `„Theo se k tomu přiznal, jakmile na něj přišli,“` | reversed: 'Theo owned it the minute he was found' = confessed |
| 1155 | `„Nemocnice s ní ukončila spolupráci. Hostince taky.“` | `„Nemocnice s ní ukončila spolupráci. Penziony taky.“` | consistency: inns = penziony |
| 1160 | `„Nabídla vám tentokrát kávu?“` | `„Nabídla ti tentokrát kávu?“` | address: Nick ↔ Jessica informal |
| 1166 | `Tanaka odnesla sklenici i falešné udání na kraj` | `Tanaková odnesla sklenici i křivou stížnost na okres` | consistency: surname; county = okres |
| 1166 | `Díl do dřezu dorazil toho rána` | `Díl k umyvadlu dorazil toho rána` | clue: hand-sink = umyvadlo |
| 1166 | `Ty tři prodřené spáry v Gretině kuchyni byly přesně takové,` | `Ta tři opotřebovaná místa v Gretině kuchyni byla přesně taková,` | mistranslation: 'three worn seams' = grout, weather-strip, sink — not three grout joints |
| 1167 | `v den, kdy jsem jí prošel,` | `v den, kdy jsem ji prošel,` | grammar: case |
| 1167 | `Položil na její spravenou pokladnu jediný čistý list papíru` | `Položil na její opravenou vitrínu jediný čistý list papíru` | mistranslation: 'her mended case' (the display case), not the till |
| 1168 | `Ten předchozí od kraje byl žlutý. Pak sáhla pod pokladnu, uřízla mu roh čokoládově-pekanového koláče` | `Ten předchozí od okresu byl žlutý. Pak sáhla pod vitrínu, uřízla mu roh čokoládovo-pekanového koláče` | consistency: county = okres; case; pie form |
| 1170 | `ta, co nosívala chléb do farmářského spolku.` | `ta, co nosívala chléb do spolkového domu.` | consistency: the Grange = spolkový dům |
| 1170 | `Než to dorazilo na samý konec Evergreen Street, předváděl Pip kousky, které bych sama stěží uvěřila.` | `Než to dorazilo na samý konec Evergreen Avenue, předváděla Pip kousky, kterým bych sama stěží uvěřila.` | gender: Pip female; street name |
| 1172 | `a v půlce bloku dupala v mrazu.` | `až do půlky bloku a dupala v mrazu.` | mistranslation: 'out the door and halfway down the block' |
| 1172 | `že z ulice nebylo přes ni vidět <bt>HOLLY JOLLY</bt>. Kakaové bochánky byly pryč v půl třetí.` | `že z ulice nebylo přes ni vidět HOLLY JOLLY. Kakaoví šneci byli pryč v půl třetí.` | bt: ruling 5: the window lettering is not a book title; cocoa buns = kakaoví šneci (Ch9) |
| 1172 | `přestože neměla v úmyslu začínat takhle pozdě,` | `i když na to už bylo pozdě,` | mistranslation: 'that she had no business starting so late' |
| 1175 | `Martha koupila tuctu kakaových bochánků. „Pro Emlinu třídu,“` | `Martha koupila tucet kakaových šneků. „Pro Emminu třídu,“` | names: Emma; tucet; cocoa buns term |
| 1177 | `a úhledně naskládal peníze na pokladnu.` | `a úhledně naskládal peníze na vitrínu.` | mistranslation: 'on the case' |
| 1180 | `Byli u pobité dřevěné stěny hned za svítání,` | `Byli u palubek hned za svítání,` | consistency: clapboard = palubky (Ch4) |
| 1183 | `Pak každému z nich dala kakaový bochánek.` | `Pak každému z nich dala kakaového šneka.` | consistency: cocoa bun term |
| 1184 | `Greta vzhlédla od pokladny a spatřila ho.` | `Greta vzhlédla od vitríny a spatřila ho.` | mistranslation: 'her case' |
| 1185 | `„Pustíte dovnitř chlad a vy ze všech lidí` | `„Pouštíte ven teplo a vy ze všech lidí` | reversed: 'You're letting the heat out' |
| 1186 | `Přistoupil k pokladně, koupil si čokoládově-pekanový koláč, který očividně vůbec nechtěl, a s řeznickou opatrností ho stál sníst u okna.` | `Přistoupil k vitríně, koupil si čokoládovo-pekanový koláč, který očividně vůbec nechtěl, a s řeznickou pečlivostí ho vstoje snědl u okna.` | grammar: garbled; pie form |
| 1188 | `Pozdním odpoledním byly ztráty smazány` | `Pozdě odpoledne byly ztráty vynahrazeny` | grammar: case |
| 1189 | `a dívala se, jak jí jedna várka za druhou kazí, zatímco na pokladně ležel ten žlutý papír,` | `a dívala se, jak se jí jedna várka za druhou kazí, zatímco na vitríně ležel ten žlutý papír,` | grammar: reflexive; case |
| 1190 | `Mám tě zapsanou na dva čokoládově-pekanové koláče a tuctu rohlíků,` | `Mám tě zapsanou na dva čokoládovo-pekanové koláče a tucet housek,` | consistency: Martha's order exactly as Ch14/20 (housky) |
| 1192 | `Nebyla jsem si o něj řekla a ani bych to neudělala, ale zabalila celý čokoládově-pekanový do krabice,` | `Neřekla jsem si o něj a ani bych to neudělala, ale zabalila celý čokoládovo-pekanový do krabice,` | grammar: tense; pie form |
| 1194 | `a ohlédla se na <bt>Holly Jolly</bt>.` | `a ohlédla se na Holly Jolly.` | bt: ruling 5: shop name |
| 651 | `Co jim pošleme za sto let? K zapečetění, až se stará otevře, na nový rok.` | `Co jim pošleme za sto let? K zapečetění, až se otevře ta stará, o novém roce.` | clue: capsule card wording made identical to its Ch26 repeat |
| 1199 | `Zachránili jsme Spolek hned následující den,` | `Zachránili jsme Společnost hned následující den,` | consistency: Historical Society = Společnost |
| 1200 | `směrem k zeleným dveřím Spolku se blížily` | `směrem k zeleným dveřím Společnosti se blížily` | consistency: Society |
| 1202 | `s čerstvě narýsovaným archem na podložce a v malých čtverečcích psal úhledným písmem sloupce:` | `s čerstvě nalinkovaným archem na podložce, na kterém měl svým drobným hranatým písmem sloupce:` | mistranslation: 'in his small square hand' (not 'in small squares') |
| 1203 | `„Pozor na žebříky, namrzají. Kellyová má celý den v Hvězdě připravenou kávu. Donese se vám.` | `„Pozor na žebříky, namrzají. Kelly má celý den ve Starlightu připravenou kávu. Donesou vám ji.` | consistency: the café is 'Starlight' everywhere (MT translated it 'Hvězda' in Ch26 only); Kelly undeclined as elsewhere |
| 1208 | `utěsněný proti zimu poprvé` | `utěsněný proti zimě poprvé` | grammar: case |
| 1208 | `kteří nikdy nestřežili nic jiného než vlastní domy,` | `kteří nikdy nepokrývali nic jiného než vlastní domy,` | mistranslation: 'never roofed anything' (střežit = guard) |
| 1212 | `Na pultu v Hvězdě stála sklenice,` | `Na pultu ve Starlightu stála sklenice,` | consistency: Starlight |
| 1212 | `Svou troškou přispěla i sbírka tobolek. Lidé, kteří nosili své ústřižky do cedrové krabičky,` | `Svou troškou přispěla i sbírka do časové schránky. Lidé, kteří nosili své drobnosti do cedrové krabice,` | mistranslation: 'the capsule drive' (tobolky = pill capsules!) |
| 1212 | `Kruh uspořádal tombolu.` | `Kroužek uspořádal tombolu.` | consistency: circle = kroužek |
| 1213 | `dokud neviděla, že do ní peníze vkládá a nic si bere.` | `dokud neviděla, že do ní peníze vkládá a nic si nebere.` | reversed: negation missing |
| 1214 | `a pod tím pohledem vhodila pětikorunu.` | `a pod tím pohledem vhodila pětidolarovku.` | currency: dollars only |
| 1215 | `co zlaté hodinky v dobrém stavu vynesou u hodináře o dvě města dál.` | `co zlaté hodinky v dobrém stavu vynesou u klenotníka o dvě města dál.` | consistency: jeweler = klenotník (Ch18) |
| 1216 | `poslal Hal do Hvězdy pro druhou` | `poslal Hal do Starlightu pro druhou` | consistency: Starlight |
| 1218 | `Nikdo ho ničím pověřil.` | `Nikdo ho ničím nepověřil.` | reversed: negation missing |
| 1219 | `Nebyl vzat na milost. A ani nebyl, ne touhle zimou, a přijal to tak tiše, jako když v chladné zadní místnosti seděl nad papíry s kancelářskou sponou na klíně.` | `Do funkce ho nevrátili. A ani nevrátí, ne touhle zimou, a přijal to tak tiše jako tu práci se savým papírem na kolenou v chladné zadní místnosti.` | mistranslation: 'He wasn't reinstated'; garbled image (Ch18 blotting work) |
| 1224 | `Greta vnutila střešní partě poslední kakaové bulky, a když Hal otevřel ústa ohledně peněz, které věnovala, nacpala mu jednu buchtu rovnou do nich.` | `Greta vnutila střešní partě poslední kakaové šneky, a když Hal otevřel ústa ohledně peněz, které věnovala, nacpala mu jednoho rovnou do nich.` | consistency: cocoa buns = kakaoví šneci |
| 1225 | `Za sklem stála na trávníku řada dětských sněhuláků otočených tváří ke Spolku` | `Za sklem stála na návsi řada dětských sněhuláků otočených tváří ke Společnosti` | consistency: the green = náves; Society |
| 1228 | `Spolek otevřel své dveře celému městu. Lidé vcházeli ze sněhové vánice,` | `Společnost otevřela své dveře celému městu. Lidé vcházeli z padajícího sněhu,` | consistency: Society; 'falling snow' (not a blizzard) |
| 1228 | `Na jejím dně stále ležely první oběti: dětská kresba hodinové věže, lisovaný javorový list, Gretin recept na čokoládové sušenky a dvě Bramovy prťavé rukavičky, ne větší než palec. Nad ní na zdi Claire připíchla lístek ze sjezdu Grange.` | `Na jejím dně stále ležely první příspěvky: dětská kresba hodinové věže, lisovaný javorový list, Gretin lístek s receptem na čokoládovo-pekanový koláč a Bramovy dva drobounké palčáčky, ne větší než palec. Nad ní na zdi Claire připíchla kartičku ze sbírky ve spolkovém domě.` | clue: Greta's chocolate-pecan PIE recipe card (Ch15/Ch23 motive) — MT 'chocolate cookies'; mittens = palčáky; 'oběti' = sacrifices; 'the Grange drive' (MT: 'a Grange convention') |
| 1229 | `Její lístek se nezměnil a ani se nezmění, dokud neuplyne nový rok.` | `Její kartička se nezměnila a ani se nezmění, dokud nepřijde nový rok.` | mistranslation: 'not this side of the new year' |
| 1230 | `Náčelnice Tanaka pronesla pár prostých slov.` | `Náčelnice Tanaková pronesla pár prostých slov.` | consistency: surname form |
| 1236 | `Kelly přinesla papírek z Hvězdy, s celým menu napsaným kolem dokola jejím rukopisem,` | `Kelly přinesla papírový kelímek ze Starlightu, s celou nabídkou napsanou kolem dokola jejím rukopisem,` | mistranslation: 'a paper cup' (not a slip); Starlight |
| 1239 | `Kruh vložil malý věneček spletený ze sušeného balzámu a bobulí,` | `Kroužek vložil malý věneček spletený ze sušené jedle a bobulí,` | consistency: circle = kroužek; balsam = jedle |
| 1243 | `Měla rukavici. Jenom jednu. Červenou, z nějaké zimy předtím, než jsem ji znala, upletenou na ruku o dva roky menší, než jakou dorostla. Druhá byla dávno pryč.` | `Měla palčák. Jenom jeden. Červený, z nějaké zimy předtím, než jsem ji znala, upletený na ruku o dva roky menší, než jakou dorostla. Druhý byl dávno pryč.` | mistranslation: craft word: mitten = palčák |
| 1244 | `„Takže ji může mít holka za sto let. Ta bude mít taky studené ruce. Tady je má každý.“ Vložila ji tam, malou a červenou proti cedru, vedle Bramových dvou prťavých a té, kterou jsem položila v Grange,` | `„Takže ho může mít holka za sto let. Ta bude mít taky studené ruce. Tady je má každý.“ Vložila ho tam, malý a červený proti cedru, vedle Bramových dvou drobounkých a toho, který jsem vložila ve spolkovém domě,` | mistranslation: mitten (masc.); Grange = spolkový dům (English 'Grange' left in) |
| 1246 | `Theo Hussein se přiřítil ke konci.` | `Theo Hussein přišel až ke konci.` | mistranslation: 'came near the end' (not 'rushed') |
| 1247 | `Do krabičky položil jediný mosazný nýtek, jakým celý měsíc spravoval archiv. „Není to moc,“ pronesl tiše, spíše Tanace než celé místnosti. „Ale za sto let bude někdo držet budovu Spolku pohromadě` | `Do krabičky položil jediný mosazný hřebíček, jakými celý měsíc spravoval archiv. „Není to moc,“ pronesl tiše, spíše Tanakové než celé místnosti. „Ale za sto let bude někdo držet budovu Společnosti pohromadě` | consistency: brad = hřebíček (Ch6/18); surname; Society |
| 1248 | `Pak Hal nahlas přečetl slova zakladatele.` | `Pak Hal nahlas přečetl slova zakladatelky.` | gender: Eliza Frost |
| 1250 | `„Kéž je zaznamenáno, že Frost Falls nepostavili silní. Postavili ho sousedé.“` | `„Nechť je zaznamenáno, že Frost Falls nepostavili silní. Postavili ho sousedé.“` | clue: the founder's line identical to Ch6 |
| 1251 | `Patřila do sbírky Spolku.` | `Patřila do sbírky Společnosti.` | consistency: Society |
| 1253 | `Ne své kakaové bulky. Ty už měl celý měsíc v paměti.` | `Ne své kakaové šneky. Ty už celé město znalo nazpaměť.` | mistranslation: 'Those the town had by heart already' (MT: 'the whole month') |
| 1258 | `Vložil ho mezi rukavice a nýtek.` | `Vložil ho mezi palčáky a hřebíček.` | consistency: mittens; brad |
| 1259 | `Potom Tanaka přiklopila víko a nezajistila ho, a Claire rychlou rukou přišpendlila k cedru čerstvou kartu: ` | `Potom Tanaková přiklopila víko a nezajistila ho, a Claire rychlou rukou přišpendlila k cedru čerstvou kartičku: ` | consistency: surname form |
| 1259 | `Zapečetit, až se otevře stará, o novém roce.` | `K zapečetění, až se otevře ta stará, o novém roce.` | clue: capsule card identical to Ch15 (italic run kept) |
| 1260 | `Venku stál každý sněhulák na třídě seřazený napříč travnatou plochou až k chodníku, otočený tváří k osvětleným oknům, desítky z nich, kde děti nakupily hromadu.` | `Venku stál každý sněhulák z třídy seřazený napříč návsí a nahoru podél cesty, otočený tváří k osvětleným oknům, desítky jich, ačkoli děti jich postavily jen hrstku.` | reversed: EN 'dozens of them where the children had built a handful' — MT 'where children had heaped a pile' kills the magic; the green = náves |
| 226 | `„Joyce, moc děkuju za...“` | `„Joyce, moc děkuju za…“` | dialogue: dossier: single-glyph ellipsis |
| 261 | `„...a vylil si vztek` | `„…a vylil si vztek` | dialogue: single-glyph ellipsis |
| 275 | `V rukavici už svírala Snowballovo vodítko,` | `V palčáku už svírala Snowballovo vodítko,` | mistranslation: craft word: mitten = palčák |
| 492 | `a ráda...“` | `a ráda…“` | dialogue: single-glyph ellipsis |
| 507 | `a teď se nakláněla k zadním částem obchodů,` | `a teď se nakláněl k zadním částem obchodů,` | grammar: the snowman (masc.) |
| 561 | `protože Petr potřeboval zaměstnat ruce` | `protože Pete potřeboval zaměstnat ruce` | names: Pete |
| 1102 | `„Nemyslela jsem si, že ty...“` | `„Nemyslela jsem si, že ty…“` | dialogue: single-glyph ellipsis |
| 1266 | `„Jdeš brzy,“ prohodila Greta,` | `„Jsi tu brzy,“ prohodila Greta,` | mistranslation: 'You're early' |
| 1270 | `„Zanesla jsem to šéfové, než jsem to otevřela,` | `„Zanesla jsem to náčelnici, než jsem to otevřela,` | consistency: Chief = náčelnice |
| 1273 | `Půjdu k soudu a zaplatím, co mi určí, a taky by mě to mělo mrzet.` | `Půjdu k soudu a zaplatím, co mi určí, a tak to má být.` | mistranslation: EN 'and I should [pay]' — not 'I should be sorry' |
| 1274 | `V kanceláři šéfové jsem ti začala vykládat,` | `V kanceláři náčelnice jsem ti začala vykládat,` | consistency: Chief = náčelnice |
| 1275 | `Nech svou vizitku v krabici.` | `Nech svou kartičku v krabici.` | mistranslation: Greta's RECIPE card in the capsule (Ch15/23) — 'vizitka' = business card |
| 1278 | `a odškrtávala si mé zákazníky podle mých záznamů.“` | `a opisovala si mé zákazníky z mé knihy.“` | clue: 'read my customers off my book' (the order book) |
| 1282 | `„Ne proto, abychom tvrdili, že je jí odpuštěno.` | `„Ne proto, abys tvrdila, že je jí odpuštěno.` | grammar: person |
| 1283 | `a zastrčila na konec svého objednávkového bloku na Den díkůvzdání.` | `a zastrčila ho dozadu do své knihy objednávek na Den díkůvzdání.` | consistency: order book = kniha objednávek |
| 1284 | `Mám plný sešit objednávek, které musím vyřídit nejdřív,` | `Mám plnou knihu objednávek, které musím vyřídit nejdřív,` | consistency: order book = kniha objednávek |
| 1288 | `Přesto sáhla pod pult,` | `Přesto sáhla pod vitrínu,` | mistranslation: 'under the case' |
| 1291 | `a nesla objednávku věnců po třídě směrem ke Spolku.` | `a nesla jsem objednávku věnců po třídě směrem ke Společnosti.` | consistency: Society = Společnost; narrator |
| 1292 | `Spolek teď působil jinak a trvalo mi krok nebo dva, než jsem přišla na to proč. Budova Spolku byla prohřátá` | `Společnost teď působila jinak a trvalo mi krok nebo dva, než jsem přišla na to proč. Budova Společnosti byla prohřátá` | consistency: Society |
| 1293 | `cedrová krabice se sklopeným víkem a čerstvou vizitkou ukrývala` | `cedrová krabice se sklopeným víkem a čerstvou kartičkou ukrývala` | mistranslation: the capsule card (not a business card) |
| 1294 | `opatrně uvolňoval další špendlík z dalšího popraskaného starého kousku.` | `opatrně uvolňoval další hřebíček z dalšího popraskaného starého kousku.` | consistency: brad = hřebíček |
| 1296 | `Sněhulák se jí motal kolem kotníků` | `Snowball se jí motal kolem kotníků` | names: Snowball (MT 'snowman') |
| 1302 | `a chvíli stála a dívala se, jak odcházejí.` | `a chvíli jsem stála a dívala se, jak odcházejí.` | grammar: narrator |
| 1309 | `tiše sněžilo na dvůr a úzkou uličku. Sníh musel padat i na město, na krabice ve Spolku` | `tiše sněžilo na dvůr a na cestu. Sníh musel padat i na město, na krabice ve Společnosti` | consistency: the lane (not the clue alley); Society |
| 1313 | `Looking for another mystery? Start the Spine and Spells series with ` | `Hledáte další záhadu? Začněte sérii Záhady na hřbetu i v kouzlech knihou ` | untranslated: sell line left in English — translated (italic run kept); series name from the published Czech edition (Záhady na hřbetu i v kouzlech); title anchor kept |
| 1313 | ` today.` | ` ještě dnes.` | untranslated: sell line, end |
| 1315 | `soudní grafoložka, která dokázala` | `forenzní expertka na zkoumání dokumentů, která dokázala` | consistency: Fiona's profession as the published Czech edition names it |
| 1316 | `Odkaz zesnulé pratetice nabízí východisko` | `Odkaz zesnulé pratety nabízí východisko` | typo: 'pratetice' |
| 1316 | `zkolabuje na měsíčním maškarním blesku,` | `zkolabuje na Maškarním plese v měsíčním svitu,` | mistranslation: 'blesk' = lightning; the ball's name as in the published Czech edition |
| 1319 | `Začněte záhady ze série Spine & Spells knihou <bt>The Binder's Bequest</bt>.` | `Začněte sérii Záhady na hřbetu i v kouzlech knihou <bt>The Binder's Bequest</bt>.` | untranslated: series name left in English; published Czech series name |
| 1321 | `Looking for another mystery? Start the Spine and Spells series with ` | `Hledáte další záhadu? Začněte sérii Záhady na hřbetu i v kouzlech knihou ` | untranslated: sell line left in English — translated (italic run kept); series name from the published Czech edition (Záhady na hřbetu i v kouzlech); title anchor kept |
| 1321 | ` today.` | ` ještě dnes.` | untranslated: sell line, end |
| 1273 | `abych se z něčeho vyvlečila.` | `abych se z něčeho vyvlékla.` | typo: 'vyvlečila' non-word (Joyce's letter, italic run kept) |

## Excerpt paragraphs replaced

- [1323] ← published ¶53: `Silnice do Pinecrestu se vinula kolem kopců jako dodatečný nápad, stužka asfaltu…`
- [1324] ← published ¶54: `Moje pronajaté auto, fádní stříbrný sedan, který páchl syntetickou vanilkou, byl…`
- [1325] ← published ¶55: `Už jsem tu kdysi byla, ale moje vzpomínky byly útržkovité a nespolehlivé, jako v…`
- [1326] ← published ¶56: `Advokátova kancelář se tísnila mezi pekařstvím, které do vzduchu pumpovalo vůni …`
- [1327] ← published ¶57: `Pan Hartwell, muž, jehož kulatý obličej a ještě kulatější brýle dělaly z dobrosr…`
- [1328] ← published ¶58: `Zmínka o mé kariéře dopadla jako olověné závaží. Měl na mysli její velmi veřejný…`
- [1329] ← published ¶59: `„Všechno je v té obálce,“ řekl a pokynul k tlusté manilové obálce na svém stole.…`
- [1330] ← published ¶60: `Žádný odkaz jsem nechtěla. Chtěla jsem čistou účetní knihu. Chtěla jsem inventar…`
- [1331] ← published ¶61: `„Děkuji, pane Hartwelle.“ Strčila jsem klíč do kapsy, vzala obálku a vyšla ven d…`
- [1332] ← published ¶62: `Flanagan’s Fine Binding & Restoration stálo přímo přes ulici, vedle železářství.…`
- [1333] ← published ¶63: `Když jsem strkala železný klíč do zámku, ruka se mi třásla. Zámek se otočil s dr…`
- [1334] ← published ¶64: `Vzduch, který se mi vyvalil vstříc, byl hmatatelnou přítomností, hustou tkání vů…`
- [1335] ← published ¶65: `Na okraji mého vědomí se zatřepetal přízrak vzpomínky. Tichý broukavý zvuk, žens…`
- [1336] ← published ¶66: `Vešla jsem dovnitř a nechala dveře za sebou cvaknout. Zvonek vydal jedno posledn…`
- [1337] ← published ¶67: `Obchod byl pohromou nahromaděné historie. Knihy se vršily v nejistých věžích na …`
- [1338] ← published ¶68: `Sluneční světlo se prodíralo zaneřáděným předním oknem a osvětlovalo celý vesmír…`
- [1339] ← published ¶69: `Můj plán, úhledný a uspořádaný seznam, který jsem sestavila cestou sem, mi teď p…`
- [1340] ← published ¶70: `Zátylkem mi probleskl pocit, že mě někdo pozoruje. Standardní reakce. Nové prost…`
- [1341] ← published ¶71: `Naproti přes cestu, zasazená do výlohy z bohatého, tmavého dřeva, byla kavárna. …`
- [1342] ← published ¶72: `A za pultem, leštící sklenici bílým hadříkem, stál muž. Byl vysoký, s rozcuchaný…`
- [1343] ← published ¶73: `Můj profesní skepticismus byl štítem a já ho zvedla. Byl proměnnou, zařazenou po…`
- [1344] ← published ¶74: `Potřebovala jsem systematický přístup. Mřížkové prohledávání. Začnu u předních d…`
- [1345] ← published ¶75: `Veselé cinknutí zvonku za mnou mě tak prudce vylekalo, že jsem málem upustila te…`
- [1346] ← published ¶76: `Žena, která vtrhla dveřmi dovnitř, byla mým pravým opakem ve všech myslitelných …`
- [1347] ← published ¶77: `„Vy jste tady!“ zvolala hlasem plným vřelého, překypujícího nadšení. „Viděla jse…`
- [1348] ← published ¶78: `Zírala jsem na ni, moje vystavěná analytická bublina propíchnutá. „Jsem,“ řekla …`
- [1349] ← published ¶79: `„Panebože, kde mám způsoby? Nejspíš v té druhé kabelce.“ Zasmála se hlasitě a up…`
- [1350] ← published ¶80: `Stiskla jsem jí ruku. Měla pevný a teplý stisk. „Je… milé vás poznat.“ Moje vnit…`
- [1351] ← published ¶81: `„Je tak neuvěřitelné konečně vás poznat,“ pokračovala a očima přejížděla obchod …`
- [1352] ← published ¶82: `„Je tu… nepořádek,“ řekla jsem a to slovo vyšlo ostřeji, než jsem zamýšlela.…`
- [1353] ← published ¶83: `Tavi si toho zřejmě nevšimla. „Je to obydlené! Maeve vždycky říkala, že knihkupe…`
- [1354] ← published ¶84: `Její vnímavost mě odzbrojovala. Zaškatulkovala jsem si ji jako bublinkavou extro…`
- [1355] ← published ¶85: `„Už jste se seznámila s Bindym?“ zeptala se.…`
- [1356] ← published ¶86: `„Ne, opravdu jsem tu zatím moc lidí nepotkala,“ řekla jsem.…`
- [1357] ← published ¶87: `Tavi se zasmála. „Ne, Bindy je kocour. Bindings Midnight Flanagan. Kočka vaší te…`
- [1358] ← published ¶88: `„Mám systém,“ řekla jsem a neurčitě mávla telefonem. „Zvládnu tohle místo dát do…`
- [1359] ← published ¶89: `„Samozřejmě že zvládnete. Maeve říkala, že jste ten nejorganizovanější, nejlogič…`
- [1360] ← published ¶90: `Zamrkala jsem. Z té prudké zatáčky v rozhovoru mi cuklo v krku. „Přijít kam?“…`
- [1361] ← published ¶91: `„Na Maškarní v měsíčním svitu!“ řekla, jako by to bylo to nejsamozřejmější na sv…`
- [1362] ← published ¶92: `Ples. Maškarní ples. Ta představa byla tak monumentálně nelákavá, že jsem se mál…`
- [1363] ← published ¶93: `„Ale tahle stará hromada prachu může jeden večer počkat,“ řekla Tavi a odmítavě …`
- [1364] ← published ¶94: `„Já se v terénu orientovat nepotřebuji,“ řekla jsem, trpělivost se mi začínala t…`
- [1365] ← published ¶95: `„Tavi,“ opravila mě automaticky. „A vypořádání pozůstalosti v Pinecrestu znamená…`
- [1366] ← published ¶96: `Našla skulinu v mé zbroji. Byl to rozumný, logický argument. Až k vzteku. Setkat…`
- [1367] ← published ¶97: `„Nemám si co vzít na… maškarní ples,“ řekla jsem a chytala se posledního, zoufal…`
- [1368] ← published ¶98: `Tavi se rozzářila, jako bych jí právě podala výherní los. „S tím si vůbec neděle…`
- [1369] ← published ¶99: `Neptala se. Velela. Připadala jsem si jako exemplář napíchnutý na desce, jehož z…`
- [1370] ← published ¶100: `Ale to, co vyšlo, k mé hluboké hrůze, bylo jediné poražené slovo. „Tak dobře.“…`
- [1371] ← published ¶101: `Tavi tleskla rukama, ostrým, vítězoslavným zvukem. „Skvěle! Začíná to v osm. Sta…`
- [1372] ← published ¶102: `A s tím byla pryč, zvonek za ní cinkal, a mě nechala v tichu, které tížilo ještě…`

## Needs a decision
See `PROOFREAD_DECISIONS.md`, section `## Flour Play - ASSEMBLED - FORMATTED_Czech (2026-10-26)` (FP-CS-1 … FP-CS-10).

## Refused by verification
None in the final run. (First run: 6 fixes crossing italic/plain run boundaries were refused by the run-format guard; each was split into per-run pieces and re-applied from the clean backup.)

## Quoted but not found
None (no prior report existed).