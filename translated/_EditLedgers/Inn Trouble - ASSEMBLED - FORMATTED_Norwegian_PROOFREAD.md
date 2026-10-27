# PROOFREAD — Inn Trouble - ASSEMBLED - FORMATTED_Norwegian (2026-10-26, second pass)

- Edition: Norwegian Bokmål. Input `translated\Inn Trouble - ASSEMBLED - FORMATTED_Norwegian.docx` (web-proofread earlier today); output `translated\corrected\Inn Trouble - ASSEMBLED - FORMATTED_Norwegian.docx` (pre-pass backup: `corrected\_bak\Inn Trouble - ASSEMBLED - FORMATTED_Norwegian.pre-proofread2-20261026.docx`).
- English source: `translate_now\Inn Trouble - ASSEMBLED - FORMATTED.docx`. Dossier: norwegian.txt. Rulings: FF_DECISIONS_BRIEF_20261013 1–7 + FF_PROOFREAD_BRIEF_20261026.
- Coverage: front matter, blurb, Ch 1–31, What's Next?, Flour Play excerpt. Every chapter read bilingually against the English, sequentially, no sub-agents.
- Prior report: 0/420 findings not found (0%). Every 'Corrected' string of the web session's 420 applied fixes is present in the input; none were undone.
- Findings this pass: 130 targeted fixes + 37 dialogue paragraphs converted to the dash system. All APPLIED, 0 refused. 1 decision logged (cross-book term), plus notes.
- Worst defect: the blackmail NOTE was called 'brevet' (letter) in the very chapters where 'Blackburn-brevene' (the letters) drive the deduction. Ch26 [773] 'Men brevene visste at vertshuset var kjøpt…' and Ch22 [692] 'Brevet visste ikke bare…' read as the Blackburn letters knowing about the inn purchase, the opposite of the reveal's logic. The note is now 'lappen' throughout (about 35 places, pronouns agreed); 'brev' is reserved for letters.

## Clue phrase (ruling 5)
'the sapphire at its heart' = **«safiren i hjertet»**, identical in the note [101], Jessica's reading [102] [119], the catalogue card [608] (in parentheses), the plain line [609] 'Safiren i hjertet.', [610] (×2), [686], [713], [768]. 'five words' is rendered 'tre ord' ([610] [617] [686]) because the Norwegian phrase is three words. The blurb [19] paraphrases ('safiren i hjertet av brosjen') as the English blurb does ('the stone at the brooch's heart').

## Address table used (ruling 2)
Norwegian dossier: **du for everyone**; formal De/Dem/Deres reads archaic and is only a satirical/period marker. The FR/IT/DE/ES formal/informal table therefore collapses to **du** for every pair in this edition (Jessica with the circle, Nick, Bram, Theo, Noriko, Neil, Sam, Jamal, Vera, the mayor, the Worthingtons, Emma). Courtesy titles carry the register: 'fru Claus', 'herr Carter', 'herr/fru Worthington'; Noriko moves from 'Fru Claus' (Ch6 [274], Ch21) to 'Jessica' (Ch25 [743] on) as the English does. Checked: 0 formal De/Dem/Deres.

## Book-wide changes
- Dialogue (ruling 1; house rule 'Norwegian = dash'): the four guillemet chapters (Ch6, Ch12, Ch18, Ch27) converted to the book's dash system. A turn opens with '– ', the attribution follows a comma, and speech resumed after the attribution opens with a new '– ' (the convention of the other 341 dash paragraphs and of FF1 NO). 37 paragraphs: 255, 257, 261, 262, 264, 265, 269, 270, 271, 272, 274, 275, 276, 279, 282, 283, 284, 285, 289, 290, 456, 457, 463, 584, 586, 587, 589, 591, 593, 594, 596, 598, 599, 783, 789, 790, 793. Words quoted inside narration keep « » per the dossier ([198] [204] [254] [455] [461] [548] [665] [781]). The glyph stays '–' because the whole book and FF1 NO use it uniformly (dossier: '–' acceptable if uniform; format_book.py treats –/— alike).
- Stray <bt> (ruling 5): 6 removed. Gazette [217] [231] [237], Winter Wonderland Inn [446] [697], The Holly Jolly Bakery [490] (now the edition's own form 'Holly Jolly Bakery', as [936]). Real anchors added to match IT2 FR: title page [0], series list [10] [11]. Spans now: Inn Trouble, Frost and Found, Flour Play only.
- Cider (ruling 6): 10 alcoholic 'eplesider/sider/cider' changed to 'varm eplemost' / 'eplemost' ([179] [181] [196] [202] [207] [211] [662] [665]×2 [668] [671]). It is served to children and to the on-duty police chief.
- The note vs the letters (ruling 7): blackmail note = 'lappen'/'lappene' throughout (was brev/lapp about 50/50). The set compound 'utpressingsbrev' is kept. 'brev' now only means letters.
- Term consistency (ruling 7, matching the IT2 FR choices): the green = 'allmenningen' ([273] 'gressletten' fixed); the square = 'torget' (unchanged, 2×); the inn lobby = 'foajeen' (6 'lobby' in Ch1 aligned to the 18 'foaje'); the Gazette = 'Gazette' (generic 'Lokalaviskontoret' / 'lokalavisens' / 'Avisen' / 'avisa' fixed where the English names the paper); hearth = 'ildsted', grate = 'rist' (Ch14, Ch19, Ch31 mixed peis/arne/ildsted); dog = 'Snowball' (5 'Snøball' fixed; names stay English like Pip); circle = 'syklubben' ([84] 'syforeningen' fixed).
- Units (spelled out, missed by the token sweep): 7 imperial idioms with 'tomme' (inch) at [183] [394] [476] [715] [733] [889] [897], rendered idiomatically (idiom rule). 'fem mil' [109] left as is (ruling 4).
- Currency: 7 krone/øre idioms in a dollar-economy book ([233] [302] [321] [554] [596] [620] [946]) changed to cent.

## Targeted findings (all APPLIED)
| # | Class | Para | Norwegian (verbatim, before) | Why (English) | Corrected |
|---|---|---|---|---|---|
| 1 | 1 Title page | 0 | Kapittel 1 | title page carried a chapter label instead of the book title (EN 'Inn Trouble', web NO-D1); anchored as in IT2 FR / FF1 so bt_anchors stamp localises it | <bt>Inn Trouble</bt> |
| 2 | Ruling 5 | 10 | Frost and Found | series-page title anchored (real book title; matches IT2 FR) | <bt>Frost and Found</bt> |
| 3 | Ruling 5 | 11 | Inn Trouble | series-page title anchored (real book title; matches IT2 FR) | <bt>Inn Trouble</bt> |
| 4 | 6 Term | 19 | Brevet krever en halv million dollar. Det vet hva oldemoren | the note = 'lappen' (blurb) | Lappen krever en halv million dollar. Den vet hva oldemoren |
| 5 | 6 Term | 19 | og det nevner safiren i hjertet av brosjen | agreement with 'lappen' | og den nevner safiren i hjertet av brosjen |
| 6 | 3 Reversed meaning | 20 | En smed skyldte tjue dollar og nektet å gi et rett svar. | EN 'A blacksmith owed twenty dollars and refused a straight answer' = Sam is OWED the money and is refused an answer; NO made him the debtor who refuses to answer | En smed som har tjue dollar til gode og ikke får et rett svar. |
| 7 | 6 Term | 28 | Lokalaviskontoret hadde | EN 'The Gazette office'; paper's name is Gazette (FF1 NO 'lokalspalten for Gazette') | Gazette-kontoret hadde |
| 8 | 3 Mistranslation | 30 | med en enslig kvist bitterhet for sesongens oransje farge | EN 'a sprig of bittersweet' (orange-berried vine); 'bitterhet' = bitterness (web NO-D9) | med en enslig kvist med oransje bær for sesongens oransje farge |
| 9 | 6 Term | 34 | Lobbyen var god og gjennomvarm | the inn lobby = 'foajeen' (18x elsewhere vs 6x 'lobby', all in Ch1; web NO-D11) | Foajeen var god og gjennomvarm |
| 10 | 3 Mistranslation | 36 | som en kvinne som tar på seg en kappe hun | EN 'coat'; 'kappe' = cape | som en kvinne som tar på seg en kåpe hun |
| 11 | 6 Term | 49 | akkurat der i lobbyen | lobby = 'foajeen' | akkurat der i foajeen |
| 12 | 6 Term | 51 | i en stille lobby | lobby = 'foajé' | i en stille foajé |
| 13 | 6 Term | 57 | ta inn lobbyen | lobby = 'foajeen' | ta inn foajeen |
| 14 | 6 Term | 69 | tvers over lobbyen | lobby = 'foajeen' | tvers over foajeen |
| 15 | 6 Term | 72 | uroen inne i lobbyen | lobby = 'foajeen' | uroen inne i foajeen |
| 16 | 6 Term | 78 | forbi lokalavisens avislesende skjelett | EN 'the Gazette's newspaper-reading skeleton' | forbi Gazettes avislesende skjelett |
| 17 | 6 Term | 84 | hvilken ettermiddag syforeningen møttes | the circle = 'syklubben' throughout this edition (31x) | hvilken ettermiddag syklubben møttes |
| 18 | 6 Term | 101 | Det var et brev. Håndskriften | the blackmail note = 'lappen' (book alternated brev/lapp, web NO-D11); 'brev' is reserved for the 1924 letters | Det var en lapp. Håndskriften |
| 19 | 6 Term | 101 | for den som hadde skrevet det, ville | pronoun agreement with 'lappen' | for den som hadde skrevet den, ville |
| 20 | 6 Term | 102 | Jeg leste det gjennom to ganger. | pronoun agreement with 'lappen' | Jeg leste den gjennom to ganger. |
| 21 | 6 Term | 104 | Jeg har lest det tre hundre ganger. | pronoun agreement with 'lappen' | Jeg har lest den tre hundre ganger. |
| 22 | 6 Term | 112 | og brevet i den andre | the note = 'lappen' | og lappen i den andre |
| 23 | 6 Term | 119 | senket brevet. – Les det igjen. Det nevner safiren. | the note = 'lappen' + agreement | senket lappen. – Les den igjen. Den nevner safiren. |
| 24 | 6 Term | 119 | Og det nevner Ridgeline | pronoun agreement with 'lappen' | Og den nevner Ridgeline |
| 25 | 4 Proper name | 124 | Theo har esker med ting fra Blackburn. | EN 'Blackburn things' = the family's papers, not a place | Theo har esker med ting fra Blackburn-familien. |
| 26 | 6 Typo | 126 | og Worthingtons’ gode uke | wrong genitive apostrophe; edition uses 'Worthington-ekteparet' | og Worthington-ekteparets gode uke |
| 27 | 3 Mistranslation | 137 | Nick holdt suppen varm da jeg kom hjem, noe han pleide å gjøre når verden hadde kjølnet og blitt urolig. | EN 'had soup on ... when the world had gone uneasy'; 'kjølnet' is an addition, 'holdt suppen varm' wrong | Nick hadde suppe på komfyren da jeg kom hjem, noe han pleide å gjøre når verden hadde blitt urolig. |
| 28 | 6 Term | 139 | Brevet, det røde båndet | the note = 'lappen' | Lappen, det røde båndet |
| 29 | 6 Term | 140 | Da jeg la brevet på bordet | the note = 'lappen' | Da jeg la lappen på bordet |
| 30 | 6 Term | 141 | og brevet foldet mot hjertet mitt | the note = 'lappen' | og lappen foldet mot hjertet mitt |
| 31 | 6 Grammar | 143 | Du må nesten tro på henne hvis du hadde sett ansiktet hennes. | EN 'You'd have to believe her, if you'd seen her face'; tense mismatch | Du ville også ha trodd henne, hvis du hadde sett ansiktet hennes. |
| 32 | Ruling 6 | 179 | et bord med eplesider og ingefærkaker | cider must be non-alcoholic (served to children); 'eplesider' is alcoholic | et bord med varm eplemost og ingefærkaker |
| 33 | Ruling 6 | 181 | merket eplesideren også | cider non-alcoholic | merket eplemosten også |
| 34 | 8 Units | 183 | trekke seg unna tomme for tomme | idiomatic 'by inches' -> imperial token removed (idiom rule) | trekke seg unna, litt etter litt |
| 35 | Ruling 6 | 196 | ved siderbordet i stad | cider non-alcoholic | ved eplemostbordet i stad |
| 36 | Ruling 6 | 202 | invitere alle sammen til cideren | cider non-alcoholic; 'cider' was English spelling | invitere alle sammen til eplemosten |
| 37 | Ruling 6 | 207 | gikk videre mot cideren | cider non-alcoholic | gikk videre mot eplemosten |
| 38 | 6 Grammar | 208 | fra en girlander med granbar | 'girlander' is plural after 'en' | fra en girlande med granbar |
| 39 | 6 Term | 209 | den eksakte rødfargen brevet hadde bedt Fiona | the note = 'lappen' | den eksakte rødfargen lappen hadde bedt Fiona |
| 40 | 6 Term | 211 | ved siden av brevet. | the note = 'lappen' | ved siden av lappen. |
| 41 | Ruling 6 + 3 | 211 | som nå stod bøyd ved siderbordet og fortalte en liten gutt om grunnleggelsen av byen av hele sitt trette hjerte, med store øyne av undring. | cider non-alcoholic; EN 'the boy's eyes wide' (NO gave the wide eyes to Theo) | som nå stod bøyd ved eplemostbordet og fortalte en liten gutt om grunnleggelsen av byen av hele sitt trette hjerte, mens gutten lyttet med store øyne. |
| 42 | 3 Mistranslation | 215 | som lo av ting før de nesten var ferdig med å være morsomme | EN 'before they were quite finished being funny'; 'nesten' = almost | som lo av ting før de helt var ferdige med å være morsomme |
| 43 | Ruling 5 | 217 | en uke før det sto å lese i <bt>Gazette</bt>. | stray <bt> on the newspaper name removed | en uke før det sto å lese i Gazette. |
| 44 | Ruling 5 | 231 | for jeg spurte ham for <bt>Gazette</bt> sin del | stray <bt> removed; 'X sin' genitive replaced by idiomatic 'på vegne av' | for jeg spurte ham på vegne av Gazette |
| 45 | Currency | 233 | gi en eneste rød øre for å holde lysene på | EN 'one thin dime'; 'rød øre' relocates the dollar economy | gi en eneste cent for å holde lysene på |
| 46 | 6 Term | 235 | alene blant boksene til Blackburn | EN 'the Blackburn boxes' = 'Blackburn-eskene' elsewhere | alene blant Blackburn-eskene |
| 47 | Ruling 5 | 237 | Theo har bedt <bt>Gazette</bt> om å sende noen. | stray <bt> removed | Theo har bedt Gazette om å sende noen. |
| 48 | 3 Mistranslation | 256 | av en lykt som noen hadde skåret ut tidligere | EN 'jack-o'-lantern'; 'lykt' alone = lantern | av en gresskarlykt som noen hadde skåret ut tidligere |
| 49 | 4 Proper name | 260 | Snøball satt ved Emmas føtter | dog's name rendered Snøball 5x / Snowball 7x; unified to Snowball (names stay English, cf. Pip; web NO-D10) | Snowball satt ved Emmas føtter |
| 50 | 4 Proper name | 267 | at Snøball nesten hadde lært seg | dog's name unified to Snowball | at Snowball nesten hadde lært seg |
| 51 | 4 Proper name | 269 | mellom Snøball og et gresskar | dog's name unified to Snowball | mellom Snowball og et gresskar |
| 52 | 6 Term | 273 | Noriko Tanaka stod midt på gressletten | the green = 'allmenningen' | Noriko Tanaka stod midt på allmenningen |
| 53 | 3 Mistranslation | 279 | Hun hadde gått tilbake til lykten Pip hadde herjet med | EN 'jack-o'-lantern' | Hun hadde gått tilbake til gresskarlykten Pip hadde herjet med |
| 54 | Currency | 302 | krevde aldri en øre for det | EN 'never charged a cent' | krevde aldri en cent for det |
| 55 | 3 Mistranslation | 310 | hva i all verden det var jeg kjempet for | EN 'what, exactly, I was fighting for'; 'i all verden' adds exasperation | hva det egentlig var jeg kjempet for |
| 56 | 6 Grammar/Term | 313 | Jeg hadde holdt utpressingsbrevet opp til nesen | 'brevet ... ga den' gender clash; the note = 'lappen' | Jeg hadde holdt utpressingslappen opp til nesen |
| 57 | 6 Term | 319 | Den var på brevet, og den var her. | the note = 'lappen' | Den var på lappen, og den var her. |
| 58 | Currency | 321 | Ikke det at jeg har sett snurten av en krone for den siste biten. | EN 'a penny'; 'krone' relocates the book's (dollar) economy | Ikke det at jeg har sett snurten av en cent for den siste biten. |
| 59 | 6 Term | 325 | og lukten var på brevet. | the note = 'lappen' | og lukten var på lappen. |
| 60 | 6 Idiom | 327 | Sam, ting er i en knipe, gi meg frist til våren | EN 'things are tight'; 'ting er i en knipe' unidiomatic | Sam, det er trangt for tiden, gi meg frist til våren |
| 61 | 6 Term | 335 | Brevet luktet av smia. Men luktet det av smia fordi Sam Patel hadde bøyd seg over det med en penn, eller fordi det hadde vært et sted | the note = 'lappen' + agreement | Lappen luktet av smia. Men luktet den av smia fordi Sam Patel hadde bøyd seg over den med en penn, eller fordi den hadde vært et sted |
| 62 | 6 Term | 339 | lukten på brevet markerte hvor det hadde vært | the note = 'lappen' + agreement | lukten på lappen markerte hvor den hadde vært |
| 63 | 6 Term | 373 | Den som hadde skrevet det brevet, arbeidet i mørket. | the note = 'lappen' | Den som hadde skrevet den lappen, arbeidet i mørket. |
| 64 | 8 Units | 394 | Hun lot seg ikke rikke en tomme av Bram | idiom 'not one inch' -> imperial token removed (idiom rule) | Hun lot seg ikke rikke en millimeter av Bram |
| 65 | 6 Term | 409 | større enn en brosje og et brev. | the note = 'lappen' | større enn en brosje og en lapp. |
| 66 | 6 Term | 410 | Jeg hadde brevet i kåpelommen, og nå gjorde hun det hun hadde begynt med hver gang brevet var i nærheten. | the note = 'lappen' | Jeg hadde lappen i kåpelommen, og nå gjorde hun det hun hadde begynt med hver gang lappen var i nærheten. |
| 67 | 3 Mistranslation | 410 | så opp på meg og sa et enkelt, skarpt og bestemt lite kvek, som en pekende finger. | EN 'chirped'; Pip 'kvitrer' everywhere else, 'kvek' = croak | så opp på meg og kvitret én gang, skarpt og bestemt, som en pekende finger. |
| 68 | 6 Term | 412 | – Brevet lukter smie, | the note = 'lappen' | – Lappen lukter smie, |
| 69 | 6 Term | 412 | Uansett hvor det brevet har vært, | the note = 'lappen' | Uansett hvor den lappen har vært, |
| 70 | 6 Typo | 417 | som et stykke familie-sølv | compound written with stray hyphen | som et stykke familiesølv |
| 71 | Ruling 5 | 446 | skjøtet til <bt>Winter Wonderland Inn</bt> et sted | stray <bt> on the inn's name removed | skjøtet til Winter Wonderland Inn et sted |
| 72 | 6 Term | 450 | halvt fordi Avisen ville ha et vennlig ansikt | EN 'the Gazette'; paper's name rendered as generic 'Avisen' (web NO-D5) | halvt fordi Gazette ville ha et vennlig ansikt |
| 73 | 8 Units | 476 | på den ærlige, slitsomme, tomme-for-tomme-måten | idiom 'inch-by-inch' -> imperial token removed (idiom rule) | på den ærlige, slitsomme, skritt-for-skritt-måten |
| 74 | 3 Mistranslation | 480 | Han hadde båret esken med blikket festet på føttene. | EN 'carried the boxes' (plural) | Han hadde båret eskene med blikket festet på føttene. |
| 75 | 6 Grammar | 482 | hvor jeg skulle plassere en montre, | 'montre' is the plural; singular 'en monter' | hvor jeg skulle plassere en monter, |
| 76 | Ruling 5 | 490 | stående på disken i <bt>The Holly Jolly Bakery</bt>, en sånn | stray <bt> removed; shop name matched to the edition's own form 'Holly Jolly Bakery' (para 803) | stående på disken i Holly Jolly Bakery, en sånn |
| 77 | 3 Mistranslation | 498 | med den nøysomme tilfredsheten til en som ser på et godt show | EN 'satisfaction of a man at a good show'; 'nøysom' = frugal | med den dype tilfredsheten til en som ser på et godt show |
| 78 | 3 Mistranslation | 502 | Lenge etterpå sto hun og speidet oppover stien | EN 'For a long moment after that she looked'; 'Lenge etterpå' = long afterwards | Så ble hun stående en lang stund og speide oppover stien |
| 79 | 6 Term | 507 | til en peis hun aldri hadde sett | EN 'a hearth she'd never seen'; hearth = 'ildsted' | til et ildsted hun aldri hadde sett |
| 80 | 3 Mistranslation | 519 | Theo fortsatte å beklage seg over taket, | EN 'kept apologizing for the roof'; 'beklage seg over' = complain about | Theo ba om unnskyldning for taket gang på gang, |
| 81 | Currency | 554 | for å presse henne for en krone. | EN 'a dime'; 'krone' relocates the dollar economy | for å presse henne for en eneste cent. |
| 82 | 3 Mistranslation | 577 | Jeg hadde lest den baklengs. Nå kunne jeg lese den riktig vei, | EN 'I'd been reading it backward' = the clue ('sporet', neuter), not the note | Jeg hadde lest det baklengs. Nå kunne jeg lese det riktig vei, |
| 83 | 6 Term | 595 | Den sa mer enn brevet, og den sa det snillere. | the note = 'lappen' (here next to Constance's real letter) | Den sa mer enn lappen, og den sa det snillere. |
| 84 | Currency | 596 | det fantes ikke penger til lege, ikke et øre. | EN 'none'; 'øre' relocates the dollar economy | det fantes ikke penger til lege, ikke en cent. |
| 85 | 6 Term | 596 | på den enkle måten brevet vil ha venninnen din til å tro | the note = 'lappen'; 'brevet' here collides with Constance's letter in the same speech | på den enkle måten lappen vil ha venninnen din til å tro |
| 86 | Currency | 620 | Theo ville aldri stjålet en øre for sin egen del. | EN 'a penny'; 'øre' relocates the dollar economy | Theo ville aldri stjålet en eneste cent for sin egen del. |
| 87 | 6 Term | 627 | der den gamle peisen på Nordpolen ville ha stått | EN 'the old hearth of the Pole'; hearth = 'ildsted' (Ch10 [404] [408]) | der det gamle ildstedet på Nordpolen ville ha stått |
| 88 | 6 Term | 628 | – En peis, sa jeg, | EN 'A hearth' — echoes Nick's 'Et ildsted' in Ch10 | – Et ildsted, sa jeg, |
| 89 | 6 Term | 629 | – En peis. Armen hans la seg rundt meg. – Den er ikke ferdig. Den kan ikke holde på den ennå, | hearth = 'ildsted' + agreement | – Et ildsted. Armen hans la seg rundt meg. – Det er ikke ferdig. Det kan ikke holde på den ennå, |
| 90 | 6 Term | 641 | hun holdt brevet ut på utstrakt arm, klemt fast mellom to fingre, som om det kunne snu seg og bite henne. | the note = 'lappen' (same chapter calls it 'den andre lappen'); also fixes 'Den lå...'/'brevet' gender clash | hun holdt lappen ut på utstrakt arm, klemt fast mellom to fingre, som om den kunne snu seg og bite henne. |
| 91 | Ruling 6 | 662 | Boder med eplesider og stekte kastanjer | cider non-alcoholic | Boder med varm eplemost og stekte kastanjer |
| 92 | Ruling 6 | 665 | Emma Redfern fant meg ved sideren | cider non-alcoholic (served to an 8-year-old) | Emma Redfern fant meg ved eplemosten |
| 93 | Ruling 6 | 665 | med to kopper sider og | cider non-alcoholic | med to kopper eplemost og |
| 94 | Ruling 6 | 668 | Hun stod ved siderboden | cider non-alcoholic | Hun stod ved eplemostboden |
| 95 | Ruling 6 | 671 | Hun tok en slurk av sideren. | cider non-alcoholic (the police chief on duty) | Hun tok en slurk av eplemosten. |
| 96 | 4 Proper name | 676 | siden uken da vi fant Snøball. | dog's name unified to Snowball | siden uken da vi fant Snowball. |
| 97 | 6 Term | 685 | de to brevene, kopien jeg hadde laget | the notes = 'lappene'; chapter otherwise collides with the Blackburn letters | de to lappene, kopien jeg hadde laget |
| 98 | 6 Term | 686 | Brevet siterte Theos egne ord. | the note = 'lappen' | Lappen siterte Theos egne ord. |
| 99 | 6 Term | 686 | Brevet var skrevet på Historielagets kremfargede brevpapir | the note = 'lappen' | Lappen var skrevet på Historielagets kremfargede brevpapir |
| 100 | 6 Term | 688 | Jeg tok det andre brevet og et ark | the note = 'lappen' | Jeg tok den andre lappen og et ark |
| 101 | 6 Term | 688 | Brevet var skrevet på papir fra Theos eget lager | the note = 'lappen' | Lappen var skrevet på papir fra Theos eget lager |
| 102 | 6 Term | 691 | Theo hadde skrevet brevene. Men Theo kunne ikke ha båret det andre brevet inn i en foajé full av festivalgjester og gått igjen uten at et menneske la merke til det. Noen andre hadde levert det til vertshuset. | the notes = 'lappene' + agreement | Theo hadde skrevet lappene. Men Theo kunne ikke ha båret den andre lappen inn i en foajé full av festivalgjester og gått igjen uten at et menneske la merke til det. Noen andre hadde levert den til vertshuset. |
| 103 | 6 Term | 692 | Brevet visste ikke bare at brosjen var stjålet. Det visste at vertshuset var kjøpt for pengene. | the note = 'lappen' + agreement; 'Brevet' here sits beside 'Blackburn-brevene' and misleads | Lappen visste ikke bare at brosjen var stjålet. Den visste at vertshuset var kjøpt for pengene. |
| 104 | 6 Term | 692 | hadde det første brevet stått. | the note = 'lappen' | hadde det stått i den første lappen. |
| 105 | 6 Term | 695 | og Theo kunne ikke ha båret brevene til vertshuset. | the notes = 'lappene' | og Theo kunne ikke ha båret lappene til vertshuset. |
| 106 | Ruling 5 | 697 | med skjøtet til <bt>Winter Wonderland Inn</bt> liggende | stray <bt> removed | med skjøtet til Winter Wonderland Inn liggende |
| 107 | 3 Mistranslation | 704 | og den maskinskrevne lappen på permen, | EN 'typed tab'; 'lappen' is the blackmail note's word | og den maskinskrevne etiketten på permen, |
| 108 | 6 Term | 713 | Og han kunne ikke ha båret brevene tvers over byen | the notes = 'lappene' (sentence follows 'Blackburn-brevene') | Og han kunne ikke ha båret lappene tvers over byen |
| 109 | 6 Term | 714 | den morgenen det andre brevet kom, | the note = 'lappen' | den morgenen den andre lappen kom, |
| 110 | 8 Units | 715 | Theo for Historielaget han så dø tomme for tomme. | idiom 'die by inches' -> imperial token removed (idiom rule) | Theo for Historielaget han så dø litt etter litt. |
| 111 | 6 Term | 722 | Brevene ville slutte, og Fiona ville være trygg. | the notes = 'lappene' | Lappene ville slutte, og Fiona ville være trygg. |
| 112 | 8 Units | 733 | jeg hadde arbeidet meg inn tomme for tomme, | idiom 'an inch at a time' -> imperial token removed (idiom rule) | jeg hadde arbeidet meg inn bit for bit, |
| 113 | 6 Term | 741 | De to brevene. Theos katalogkort | the notes = 'lappene' | De to lappene. Theos katalogkort |
| 114 | 6 Term | 743 | To brev, krav om penger, | the notes = 'lappene' | To lapper, krav om penger, |
| 115 | 6 Term | 773 | Men brevene visste at vertshuset var kjøpt for brosjepengene, | the notes = 'lappene'; 'brevene' reads as the Blackburn letters, reversing the logic of the reveal | Men lappene visste at vertshuset var kjøpt for brosjepengene, |
| 116 | 6 Term | 781 | De to brevene ble til bevis, | the notes = 'lappene' | De to lappene ble til bevis, |
| 117 | 6 Term | 795 | Brevene hadde stanset. | the notes = 'lappene' | Lappene hadde stanset. |
| 118 | 6 Grammar | 811 | Den eneste måten stedet noen gang er trygg på, | adjective agreement with neuter 'stedet' | Den eneste måten stedet noen gang blir trygt på, |
| 119 | 6 Term | 828 | Hun lot Claire skrive den for avisen, | EN 'for the Gazette'; paper's name | Hun lot Claire skrive den for Gazette, |
| 120 | 4 Proper name | 846 | Snøball hadde på seg gevirhatten. | dog's name unified to Snowball | Snowball hadde på seg gevirhatten. |
| 121 | 8 Units | 889 | – Fortsett da å holde det gående, sa jeg. – En tomme av gangen. | idiom 'An inch at a time' -> imperial token removed (idiom rule) | – Fortsett da å holde det gående, sa jeg. – Ett skritt av gangen. |
| 122 | 6 Term | 892 | Arnen han hadde bygd glødet midt i rommet, de runde marksteinene var varme og gyldne, og magien hang over det tomme ildstedet i langsomme sirkler. | hearth = 'ildsted' (Ch10/19/30), grate = 'rist' (Ch19); NO had hearth/grate swapped | Ildstedet han hadde bygd, glødet midt i rommet, de runde marksteinene var varme og gyldne, og magien hang over den tomme risten i langsomme sirkler. |
| 123 | 6 Term | 897 | så på hvordan gullet snurret i langsomme sirkler over ildstedet, | EN 'over the grate' | så på hvordan gullet snurret i langsomme sirkler over risten, |
| 124 | 8 Units | 897 | gikk sine lange veier tilbake, tomme for hard tomme. | idiom 'inch by hard inch' -> imperial token removed (idiom rule) | gikk sine lange veier tilbake, tungt skritt for tungt skritt. |
| 125 | 6 Term | 901 | fortsatte arnen å gløde inne i verkstedet. | EN 'the hearth glowed on'; hearth = 'ildsted' | fortsatte ildstedet å gløde inne i verkstedet. |
| 126 | 3 Mistranslation | 914 | byttet ut skjelettene og lyktene med maisstengler | EN 'jack-o'-lanterns' | byttet ut skjelettene og gresskarlyktene med maisstengler |
| 127 | 3 Reversed meaning | 920 | – Så absolutt. | EN 'Very nearly.' (then 'where's the North Pole in it?'); 'Så absolutt' = absolutely | – Nesten. |
| 128 | 6 Term | 926 | Claire Bennett, som skrev for avisa, | EN 'who wrote for the Gazette' | Claire Bennett, som skrev for Gazette, |
| 129 | 3 Mistranslation | 941 | jeg så du gjorde det på Bedehuset, | EN 'at the Grange' (community hall); 'Bedehuset' = a prayer house | jeg så du gjorde det på grendehuset, |
| 130 | Currency | 946 | og hver eneste øre går til Historielagets takfond. | EN 'every penny'; 'øre' relocates the dollar economy | og hver eneste cent går til Historielagets takfond. |

## Decision logged (PROOFREAD_DECISIONS.md)
- **NO2-D1: the circle's name across the series.** This edition calls the knitting circle 'syklubben' (31×, set by the web pass); FF1 NO calls it 'sirkelen' (28×) / 'strikkeklubben' (2×). Pick one for the series. Not changed here.

## Notes (not changed: formatter's job or another book)
- Formatter: 0 Heading 1 paragraphs. TOC [12]–[16] lists only 'Om denne boken / Kapittel 31 / Hva blir det neste? / Utdrag fra'. TOC 'Hva blir det neste?' differs from the back-matter heading [904] 'Hva skjer videre?'. '* * *' at [902] [910] [974] where the English has none. The pre-flight 'chapter 1 detected twice' came from the title page [0] 'Kapittel 1' (now the title); 'chapter 31 twice' comes from TOC line [14].
- Dash convention: most speech-to-narration transitions run on without a closing dash ('– Jessica. Til og med stemmen…'); a few close with one ([492] [497] [504] [506]). Both are accepted Norwegian practice; not normalised.
- Translator-added italics (web NO-D6) left; the italic sequence is unchanged by this pass.
- FF1 NO (Frost and Found, not edited here) needs the same series fixes: 'sider' 8× (ruling 6), Snowball/Snøball mixed 29/20, title page still in English ('Book 1', 'Copyright 2026 by', 'Second Edition', 'All rights reserved.'), and 118 guillemet-opening paragraphs.
