# APPLIED — Inn Trouble - ASSEMBLED - FORMATTED_Spanish

## Verify (`python3 _tools/preflight.py --verify`)

- PASS paragraphs 1568 = 1568
- PASS scene breaks 5 = 5
- PASS bt spans 9 = 9
- italic runs 27 = 27; content differs in 5 runs, all deliberate text fixes inside italic runs (formatting untouched):
  - 134 (first note): `el zafiro en el corazón` → `el zafiro en su corazón` (match Theo's card)
  - 619 (drawer labels): English labels → `ESCRITURAS. LICENCIAS. PADRONES FISCALES. REGISTROS DE LA PROPIEDAD, 1900–1950.`
  - 911 (MISSING card): `al encontraras` → `al encontrarlas`
  - 1070 (quoted note): `I know how your family came by this inn,` → `Sé cómo consiguió tu familia esta posada,`
  - 1086 (folder tab): `PROPERTY — EVERGREEN AVE — WINTER WONDERLAND INN` → `PROPIEDAD — AVDA. EVERGREEN — WINTER WONDERLAND INN`
- Paragraphs changed vs baseline: 140. RESULT printed FAIL only because of the 5 intended italic-run text changes above.

## Applied fixes (154)

| Para | Was | Now | Why |
|---|---|---|---|
| 16 | identificación avec personas | identificación con personas | 1 Untranslated: French word 'avec' in the fiction disclaimer |
| 45 | Era un círculo grueso de perenne, | Era un círculo grueso de ramas de hoja perenne, | 3 Calque: 'evergreen' rendered as a bare adjective 'de perenne' |
| 49 | murmurro | murmullo | 6 Typo: nonword |
| 51 | Su cárdigan estaba abrochado con un botón de más. | Llevaba el cárdigan mal abrochado, desfasado en un botón. | 3 Mistranslation: EN 'buttoned wrong by one button'; 'con un botón de más' = one button too many |
| 53 | le tendí a cesta | le tendí la cesta | 6 Typo: missing letter |
| 72 | Miró a Sam de reojo | Señaló con la cabeza hacia donde se había ido Sam | 3 Mistranslation: EN 'He nodded after Sam', not 'glanced sideways at Sam' |
| 76 | pero me fiaba de ella tanto como habría podido lanzar la pantalla contra incendios | pero no me fiaba de ella más de lo lejos que habría podido lanzar la pantalla contra incendios | 5 Idiom: idiom garbled: said she trusted it as much as she could throw the screen (lost the negative sense) |
| 84 | a una pulgada de una pera | a dos o tres centímetros de una pera | 8 Units: SAFE rule: literal 'about an inch' -> 2–3 cm |
| 104 | —¿Diga? —sostuve | —¿Diga? —Sostuve | 6 Typography: narration after dialogue that is not a speech verb takes a capital |
| 134 | el que lleva el zafiro en el corazón | el que lleva el zafiro en su corazón | 3 Key clue: the note must use the same five words as Theo's card (915/917/919 'el zafiro en su corazón'); plot depends on verbatim match |
| 136 | El zafiro en el corazón. | El zafiro en su corazón. | 3 Key clue: same five words as the card (919) |
| 166 | —¿Pero es que no lo ves? —sacudió | —¿Pero es que no lo ves? —Sacudió | 6 Typography: capital after dialogue (not a speech verb) |
| 172 | Léeotra vez | Léela otra vez | 6 Typo: run-together words |
| 172 | El zafiro en el corazón, esas | El zafiro en su corazón, esas | 3 Key clue: 'those very words' must match the card |
| 206 | Pío y se puso a mi lado. | Pió y se puso a mi lado. | 6 Typo: 'Pío' (1st person / noun) for 'she chirped' |
| 213 | a un solo alma | a una sola alma | 6 Grammar: 'alma' is feminine; 'un' only directly before stressed a- |
| 220 | Eso es lo que hace que me siente tan frío por dentro. | Eso es lo que hace que se me quede tan frío por dentro. | 3 Mistranslation: 'sit cold in me' rendered with 'sentarse' (me siente = I sit) |
| 222 | había leído lo que no le importaba | había leído lo que no tenía por qué leer | 3 Mistranslation: EN 'had no business reading' |
| 223 | Theo has estado viviendo | Theo ha estado viviendo | 1 Untranslated: English/2nd-person 'has' for 3rd person |
| 238 | de forma lenta y compasiva | de forma lenta y acompasada | 3 Mistranslation: EN 'slow and even'; 'compasiva' = compassionate |
| 261 | a veces agitando ambas manos | a veces tendiendo ambas manos | 3 Mistranslation: EN 'both hands sometimes' (handshake), not waving |
| 287 | Veinte cartas y ni una sola | Veinte años de cartas y ni una sola | 3 Mistranslation: EN 'Twenty years of letters' |
| 307 | motivos para fijarse | motivos para fijarme | 6 Grammar: first person |
| 317 | Me enderezé | Me enderecé | 6 Typo: spelling |
| 317 | un cuarto de pulgada más | medio centímetro más | 8 Units: SAFE rule: literal 'a final quarter-inch' (~6 mm) |
| 324 | el corro había arrimado | el círculo había arrimado | 6 Term: the knitting circle is 'el círculo' everywhere else |
| 339 | Me lo contó el propio Theo el año pasado | Me lo contó el propio Theo la primavera pasada | 3 Mistranslation: EN 'last spring' (cf. 672 'la primavera pasada') |
| 345 | entre las cajas de Blackburn | entre las cajas de los Blackburn | 6 Term: family name needs article, as everywhere else |
| 353 | a si la nieve del primero de octubre presagiaba | a si una primera nevada en octubre presagiaba | 3 Mistranslation: EN 'an October first snow' = a first snowfall in October, not 1 October |
| 363 | Me lo contarás o no, y me da igual. | Me lo contarás o no, y las dos cosas están bien. | 3 Mistranslation: EN 'either's all right'; 'me da igual' = I don't care |
| 369 | a su manoplas | a su manopla | 6 Grammar: number agreement |
| 370 | mientras los nuevos hilos se tensaban en la oscuridad | mientras subían las nuevas tiras, todavía apagadas | 3 Mistranslation: EN 'the new strands going up dark' = unlit |
| 377 | el primer par de docenas de manoplas | la primera docena de manoplas | 3 Mistranslation: EN 'first dozen mittens' |
| 377 | «¿Ponlas a lo largo del frente del escenario, por favor? Cuidado con la blanda» | «Ponlas a lo largo del frente del escenario, ¿quieres? Cuidado con la blanda» | 6 Grammar: imperative wrapped in question marks |
| 378 | su pingüino se está comiendo | tu pingüino se está comiendo | 5 Register: Emma uses tú with Jessica (406, 408, 1381) |
| 382 | Todo el pueblo había salido a buscarla. | Todo el pueblo había salido a buscar. | 3 Mistranslation: 'buscarla' made the town search for Emma; EN neutral 'to search' |
| 393 | Cacerolas. | Cazuelas. | 6 Term: casseroles = dishes of food ('cazuela', 5:337); 'cacerola' = saucepan |
| 398 | Y sus renos no están | Y tus renos no están | 5 Register: Noriko uses tú with Jessica in the same speech (400) and in ch21/25 |
| 400 | a Cometa en Maple Street | a Comet en Maple Street | 4 Proper name: reindeer names kept in English (Dancer, Prancer, Vixen) |
| 403 | —Señora Claus. Mire. | —Señora Claus. Mira. | 5 Register: Emma uses tú with Jessica |
| 434 | Pase lo que pase, esto valía la pena: | Pasara lo que pasara, esto merecía protegerse: | 2 Omission: EN 'this was worth protecting' – 'protecting' dropped; tense |
| 456 | —Hizo la posada —dije, con naturalidad, dando vuelta el portavelas—. | —Usted hizo los trabajos de la posada —dije, con naturalidad, dándole la vuelta al portavelas—. | 3 Mistranslation: 'Hizo la posada' = built the inn; EN 'You did the inn' (the ironwork); 'dar vuelta' is not Peninsular |
| 484 | A un herrero le dejar un sitio | A un herrero le gusta dejar un sitio | 2 Omission: verb missing (EN 'A smith likes to leave') |
| 527 | hasta la última onza | hasta la última pizca | 8 Units/idiom: idiom 'every ounce' rendered with a literal ounce; not native |
| 535 | Cerrar el patrimonio. | Cerrar la herencia. | 6 Term: estate = 'herencia' (509) |
| 539 | Se rió, | Se rio, | 6 Orthography: RAE spelling; edition uses 'rio' (269) |
| 546 | a un eludito muy alterado | a un pequeño elfo muy alterado | 6 Typo: nonword; EN 'a small elf' |
| 548 | y ahora aquí la tienes comiéndose | y ahora aquí la tiene comiéndose | 5 Register: Bram uses usted with Jessica (same speech 'se lo digo yo', 552 'dígame usted') |
| 574 | doradas allí donde debieron ser anaranjadas | doradas allí donde deberían haber sido anaranjadas | 6 Grammar: 'debieron' = must have been; EN 'should have been' |
| 613 | no ara los campos en febrero | no quita la nieve de las carreteras en febrero | 3 Mistranslation: EN 'doesn't plow the roads' (snowplough), not plough fields |
| 619 | DEEDS. PERMITS. TAX ROLLS. PROPERTY RECORDS, 1900–1950. | ESCRITURAS. LICENCIAS. PADRONES FISCALES. REGISTROS DE LA PROPIEDAD, 1900–1950. | 1 Untranslated: drawer labels left in English (text inside italic run) |
| 627 | impuestos. Su pluma no dejó de moverse. | impuestos. —Su pluma no dejó de moverse. | 6 Punctuation: narration was inside Vera's speech |
| 658 | porque la Gaceta quería | porque el Gazette quería | 6 Term: newspaper is 'el Gazette' elsewhere (326, 340, 347, 1303) |
| 672 | La historia no abre los caminos con el arado. | La historia no quita la nieve de las carreteras. | 3 Mistranslation: EN 'History doesn't plow the roads' (echo of 613) |
| 680 | a través del año nuevo | hasta pasado el año nuevo | 3 Calque: EN 'through the new year' |
| 691 | —¡Sra. Claus! | —¡Señora Claus! | 1 Honorific: abbreviation used only by Jamal; 'señora Claus' spelled out everywhere else |
| 695 | Él rió | Él rio | 6 Orthography: RAE spelling |
| 705 | Sra. Claus | señora Claus | 1 Honorific: see 691 |
| 709 | su madre Aparentemente | su madre aparentemente | 6 Typo: stray capital |
| 709 | Sra. Claus | señora Claus | 1 Honorific: see 691 |
| 717 | —Rió | —Rio | 6 Orthography: RAE spelling |
| 717 | Sra. Claus, yo | Señora Claus, yo | 1 Honorific: see 691 |
| 738 | verde, con el ayuntamiento y todo | con su prado, su ayuntamiento y todo | 3 Mistranslation: EN 'green and Town Hall and all' = the town green, not the colour |
| 770 | su cara de papa gruñón | su cara de patata gruñona | 6 Variety: 'papa' is Latin American; edition uses 'patata' (548) |
| 797 | Es un tasador | Es un marchante | 3 Mistranslation: EN 'He's a dealer'; 'tasador' = appraiser |
| 822 | Házmelo en voz alta. | Razónalo en voz alta. | 3 Mistranslation: EN 'Talk it through out loud' |
| 824 | Toda su beca de historia | Toda su erudición histórica | 3 Mistranslation: 'history scholarship' = learning, not a grant |
| 825 | —De acuerdo —Nick dio un trago—. | —De acuerdo. —Nick dio un trago—. | 6 Punctuation: narration after speech needs full stop + capital |
| 826 | Golpecé | Golpeé | 6 Typo: spelling |
| 835 | son de las que se levantó ante todo el pueblo para anunciar que se habían extraviado | son precisamente las que, plantado ante todo el pueblo, anunció que se habían extraviado | 6 Grammar: ungrammatical relative clause |
| 839 | como debido | como es debido | 6 Grammar: fixed phrase |
| 841 | a quien sospechar | de quien sospechar | 6 Grammar: 'sospechar de' |
| 853 | como si le supiera mal | como si le dejara mal sabor de boca | 3 Mistranslation: 'saber mal' (Spain) = to feel sorry; EN 'as though it tasted foul' |
| 861 | que pudiera esperar limpiar | que pudiera esperar descartar | 3 Calque: 'clear' a suspect = descartar (as 1062) |
| 866 | —Muy sólido —dijo | —Es una firma de verdad —dijo | 3 Mistranslation: EN 'Real firm' = it is a real firm |
| 866 | Uno viejo, a dos estados de distancia, | Antigua, a dos estados de distancia, | 3 Mistranslation: agrees with 'firma' |
| 882 | Por algo que la ley ni puede tocar. | Por algo que la ley ya no puede tocar. | 6 Grammar: EN 'a thing the law can't touch' (anymore) |
| 888 | de su lindo pueblo | de su bonito pueblo | 6 Variety: 'lindo' is Latin American |
| 898 | son los a medias | son los que se cuentan a medias | 6 Grammar: elliptical, ungrammatical |
| 900 | a limpiar a Neil Carter. Lo había limpiado | a descartar a Neil Carter. Lo había descartado | 3 Calque: 'clear' a suspect |
| 900 | pase lo que pase: | pasara lo que pasara: | 6 Tense: past narrative |
| 911 | al encontraras | al encontrarlas | 6 Typo: card text (inside italic run) |
| 929 | a las apuradas | deprisa y corriendo | 6 Variety: 'a las apuradas' is Rioplatense |
| 933 | alrededor de los hombres | alrededor de los hombros | 6 Typo: 'hombres' = men; shoulders |
| 937 | —mi voz salió áspera—. | —Mi voz salió áspera—. | 6 Typography: capital after dialogue |
| 951 | Pip marchando en desgarbado tropel delante de nosotros | Pip anadeando delante de nosotros | 3 Mistranslation: 'tropel' = a throng; one penguin waddling |
| 992 | de cómo y de si estaba sola | de cómo y de si lo había hecho solo | 3 Mistranslation: EN 'how and whether-alone' = whether he acted alone, not whether Jessica was alone |
| 1019 | los empanadillos | las empanadillas | 6 Grammar: gender |
| 1019 | Ni un solo alma | Ni una sola alma | 6 Grammar: 'alma' feminine |
| 1025 | ve a su hija cumplir ocho años a viva voz | ve a su hija ser una niña de ocho años a viva voz | 3 Mistranslation: 'cumplir ocho años' = turn eight; EN 'be eight years old out loud' |
| 1027 | El segundo billete había dicho | La segunda nota había dicho | 3 Mistranslation: 'billete' = banknote/ticket; the blackmail note is 'nota' |
| 1027 | un tercer billete | una tercera nota | 3 Mistranslation: as above |
| 1039 | en el billete que le había llegado | en la nota que le había llegado | 3 Mistranslation: as above |
| 1049 | la mano enguantada de Emma | la mano de Emma, enfundada en una manopla, | 3 Mistranslation: EN 'mittened hand' (mittens are 'manoplas' throughout) |
| 1062 | con la verdad de la que me había estado sirviendo para evitarlos | con la verdad que había estado eludiendo sirviéndome de ellos | 3 Reversed meaning: EN 'the truth I'd been using them to avoid' (inverted) |
| 1064 | impresas en la nota de extorsión exactamente igual que en la tarjeta con la cuidadosa y ligera caligrafía de Theo | plasmadas en la nota de extorsión exactamente igual que en la ficha con la cuidadosa caligrafía inclinada de Theo | 3 Mistranslation: note is handwritten ('impresas' = printed); catalog card = 'ficha' (911–925); 'sloping' not 'light' |
| 1070 | I know how your family came by this inn, | Sé cómo consiguió tu familia esta posada, | 1 Untranslated: quotation of the first note left in English (italic run); wording from 134 |
| 1072 | Tenía el robo. | Tenía la parte del robo. | 3 Mistranslation: EN 'He had the theft' = held that half of the knowledge |
| 1075 | Subí a la cama | Subí a acostarme | 6 Idiom: 'went up to bed' |
| 1086 | PROPERTY — EVERGREEN AVE — WINTER WONDERLAND INN | PROPIEDAD — AVDA. EVERGREEN — WINTER WONDERLAND INN | 1 Untranslated: folder tab left in English (italic run) |
| 1090 | lo suficientemente reciente como para no haberlo guardado | tan recientemente que aún no lo había guardado | 6 Grammar: adjective for adverb, garbled |
| 1100 | un hombre al que respetaba | un hombre en quien confiaba | 3 Mistranslation: EN 'a man she trusted' |
| 1104 | Theo tenía el robo. | Theo tenía la parte del robo. | 3 Mistranslation: see 1072 |
| 1104 | por Evergreen Avenue desapercibido | por la avenida Evergreen desapercibido | 4 Proper name: street is 'la avenida Evergreen' everywhere else |
| 1121 | Paren ahora mismo | Parad ahora mismo | 5 Register: Jessica uses tú with both Theo and Vera; European plural is vosotros (cf. 672, 1306) |
| 1123 | en la Gazette | en el Gazette | 6 Term: see 658 |
| 1129 | en cualquier invierno desesperado con los años | en cualquier invierno desesperado a lo largo de los años | 6 Grammar: EN 'down the years' |
| 1143 | medio extranjera | medio forastera | 3 Mistranslation: outsider in town, not a foreigner (cf. 1309 'forastera') |
| 1143 | una búsqueda de perros por allá | la búsqueda de un perro por allá | 3 Mistranslation: one lost dog |
| 1145 | LLeves | Lleves | 6 Typo: double capital |
| 1162 | medio turno | media vuelta | 6 Term: 'half-turn' |
| 1174 | Nada de redadas. | Nada de operaciones encubiertas. | 3 Mistranslation: EN 'Not a sting'; 'redada' = raid |
| 1184 | Le quitó a quienes la habían robado primero | Se lo quitó a quienes le habían robado primero | 6 Grammar: laísmo with 'robar' |
| 1211 | El cartulina gruesa | La cartulina gruesa | 6 Grammar: gender |
| 1213 | Están en tu tarjeta de catálogo, de tu propia mano, la tarjeta de las cartas | Están en tu ficha de catálogo, de tu propia mano, la ficha de las cartas | 6 Term: catalog card = 'ficha' (911–925, 1063) |
| 1226 | Theo cometió el robo. | Theo tenía la parte del robo. | 3 Reversed meaning: EN 'Theo had the theft' (the knowledge of it); 'cometió el robo' says Theo committed the 1924 theft |
| 1228 | Él cometió el robo. | Él tenía la parte del robo. | 3 Reversed meaning: as above |
| 1230 | debí haber decir | debí haber dicho | 6 Grammar: participle |
| 1234 | en el dinero y en poder dormir | en el dinero y en las noches sin dormir | 3 Reversed meaning: EN 'the not-sleeping' |
| 1248 | lo daba vuelta | le daba vueltas | 6 Variety: Peninsular usage |
| 1254 | aceptó la dimisión y hablaba en serio | aceptó la dimisión, y en serio | 3 Mistranslation: 'and meant it'; 'hablaba' had no subject sense |
| 1272 | aquello mismo que Theo había arruinado intentando salvar | aquello mismo por cuya salvación Theo se había arruinado | 3 Reversed meaning: EN 'Theo had ruined himself trying to save' – TR said Theo ruined the Society |
| 1274 | Lo que había hecho mal para salvar seguía hundiéndose. | Aquello que había querido salvar obrando mal seguía hundiéndose. | 6 Grammar: garbled |
| 1278 | Nada de eso se quedaba callado | Nada parecido se quedaba callado | 3 Mistranslation: EN 'Nothing like that' |
| 1285 | que un rescate valía más que una mala acción | que un rescate bien valía una mala acción | 3 Mistranslation: EN 'a rescue was worth a wrong' (justified it), not 'worth more than' |
| 1285 | por un invitado generoso | por un huésped generoso | 6 Term: inn guest |
| 1292 | me preguntué | me pregunté | 6 Typo: spelling |
| 1294 | El juicio había terminado. | La rendición de cuentas había terminado. | 3 Mistranslation: there was no trial; EN 'The reckoning' |
| 1295 | nuestro callejón | nuestra calle | 3 Mistranslation: 'lane' up to the cottage; 'callejón' = alley |
| 1303 | una familia que la había robado primero | una familia que le había robado primero | 6 Grammar: laísmo |
| 1305 | en la tertulia | en el círculo | 6 Term: the knitting circle |
| 1307 | los mitones terminados amontonándose | las manoplas terminadas amontonándose | 6 Term: mittens = 'manoplas' throughout; 'mitones' = fingerless gloves |
| 1312 | me levantó el sombrero cruzando de un lado a otro de la avenida Evergreen | me saludó tocándose la gorra desde la otra acera de la avenida Evergreen | 3 Mistranslation: EN 'tipped his cap ... clear across' (cf. 1025) |
| 1313 | en la tertulia | en el círculo | 6 Term: the knitting circle |
| 1317 | a su mitón | a su manopla | 6 Term: mittens |
| 1318 | casi una extranjera | casi una forastera | 3 Mistranslation: outsider (cf. 1309) |
| 1319 | Pip iba waddleándose | Pip iba anadeando | 1 Untranslated: English 'waddle' hispanised |
| 1322 | buena mitad de Evergreen Avenue | buena mitad de la avenida Evergreen | 4 Proper name: street name form |
| 1342 | Puede que sea lo único bueno de lo que le toque estar cerca de nuevo. | Puede que sea lo primero bueno de lo que vuelva a estar cerca. | 3 Mistranslation: EN 'the first good thing he gets to stand near again' |
| 1350 | Danzarina esta vez | Dancer esta vez | 4 Proper name: the reindeer is 'Dancer' in ch10 (548–554) |
| 1354 | al cuello de Danzarina | al cuello de Dancer | 4 Proper name: as above |
| 1356 | bajo las narices de Danzarina | bajo las narices de Dancer | 4 Proper name: as above |
| 1356 | el hogar que él había encendido para la magia | el hogar que él había construido para la magia | 3 Mistranslation: EN 'built'; the hearth is unlit (953) |
| 1405 | si soy sincera | si soy sincero | 4 Gender: Theo is male |
| 1431 | ¿Qué sigue? | ¿Y ahora qué? | 6 Term: heading must match its TOC entry (24) |
| 1437 | una piedra atraviesa el cristal | un ladrillo atraviesa el cristal | 3 Mistranslation: EN 'a brick' |
| 1471 | Y tras el mío en el ochenta y pico. | Y tras el mío allá por mil novecientos ochenta y tantos. | 3 Mistranslation: EN 'in nineteen eighty-something'; 'el ochenta y pico' reads as an age/number |
| 1497 | la respuesta era todas ustedes, así que toma. | la respuesta era todas vosotras, así que tomad. | 5 Register/variety: informal plural in this European edition is vosotras (cf. 1306) |
| 1501 | Ustedes solas no lo van a hacer. | Vosotras solas no lo vais a hacer. | 5 Register/variety: as above |
| 1513 | ¿Por qué están todas haciendo coronas? | ¿Por qué estáis todas haciendo coronas? | 5 Register/variety: as above |
| 1545 | en dirección a los tiendas | en dirección a las tiendas | 6 Grammar: gender |
| 1545 | con los brazos de paleta | con los brazos de palo | 3 Mistranslation: EN 'stick arms' |
| 1561 | sus brazos de paleta | sus brazos de palo | 3 Mistranslation: EN 'stick arms' |
| 1563 | un muñeco de nieve vuelto del revés | un muñeco de nieve mirando hacia el lado equivocado | 3 Mistranslation: 'del revés' = inside out/upside down; EN 'turned the wrong way' |

## Decisions logged (13)

ES-D1 title localisation; ES-D2 truncated TOC; ES-D3 five `* * *` lines; ES-D4 key clue in English inside <bt> (1064, 1213); ES-D5 round-figure units (150, 1330); ES-D6 alphabetical B cards; ES-D7 green/paddock terms; ES-D8 gender of the inn's name; ES-D9 Sam↔Jessica register; ES-D10 translator-added italics; ES-D11 bittersweet; ES-D12 Martha's echoed line; ES-D13 banner kept in English.

## Refusals

None (0).

## Quoted but not found

None.
