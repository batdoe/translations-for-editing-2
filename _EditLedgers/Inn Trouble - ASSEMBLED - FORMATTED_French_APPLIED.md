# APPLIED — Inn Trouble - ASSEMBLED - FORMATTED_French

## Verify (`python3 _tools/preflight.py --verify`)
- PASS paragraphs 1491 = 1491
- PASS scene breaks 3 = 3
- PASS bt spans 8 = 8
- italic runs: count and order unchanged (26 = 26); text differs in 12 runs, every one a deliberate text fix inside an existing italic run:
  - 311 exhibit card translated from English
  - 903 'à reclassement' → 'à reclasser'
  - 905 'du broche' → 'de la broche'
  - 948 second blackmail note: tu → vous (matches first note)
  - 1017 quoted first note translated from English
  - 1033 'PROPERTY' → 'PROPRIÉTÉ'
  - 1273 time-capsule inscription: restored dropped 'nous'
  - 1372, 1388 (×2 runs each), 1490: 'There are more mysteries afoot… / is coming soon' translated
- Result printed FAIL only because of these intended italic-text changes; 183 paragraphs changed vs baseline, all and only the paragraphs listed below.

## Applied fixes (217)

| Para | Was → Now | Why |
|---|---|---|
| 8 | Copyright 2026 by Lisa Bouchard. → Copyright © 2026 Lisa Bouchard. | 1 Untranslated: English 'by' in copyright line; standard French form |
| 10 | Second Edition → Deuxième édition | 1 Untranslated: front matter boilerplate |
| 12 | All rights reserved. → Tous droits réservés. | 1 Untranslated: front matter boilerplate |
| 14 | No part of this publication may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without the prior … → Aucune partie de cette publication ne peut être reproduite, distribuée ou transmise sous quelque forme ou par quelque moyen que ce soit, y compris la photocopie, l'enregistrement ou tout autre procédé… | 1 Untranslated: copyright notice left in English |
| 16 | The story, all names, characters, and incidents portrayed in this production are fictitious. No identification with actual persons (living or deceased), places, buildings, and products is intended or … → Cette histoire, ainsi que tous les noms, personnages et événements qui y sont décrits, sont fictifs. Toute ressemblance avec des personnes réelles (vivantes ou décédées), des lieux, des bâtiments ou d… | 1 Untranslated: fiction disclaimer left in English |
| 17 | Books in This Series → Dans la même série | 1 Untranslated: front matter heading |
| 20 | Table of Contents → Table des matières | 1 Untranslated: front matter heading |
| 21 | About this Book → À propos de ce livre | 1 Untranslated: TOC entry; matches para 28 heading |
| 45 | a dandiné sur le perron → s'est dandinée jusque sur le perron | 6 Grammar: 'se dandiner' is pronominal |
| 49 | M. Kim had sculpté → M. Kim avait sculpté | 1 Untranslated: English auxiliary 'had' left in French sentence |
| 61 | le grand pare-étincelles de l'îlot de la cheminée → le grand pare-étincelles devant l'âtre | 5 Idiom: 'at the hearth'; 'îlot de la cheminée' is not French |
| 87 | pourboirent le personnel avec largesse → laissent au personnel des pourboires généreux | 6 Typo/nonword: 'pourboirent' is not a French verb ('tipped the staff generously') |
| 87 | qui a fabriqué les édredons → qui a confectionné les courtepointes | 6 Term: quilts = 'courtepointes' two paragraphs earlier (81, 83) |
| 107 | approchant la cinquantaine → dans les cinquante-cinq ans | 3 Mistranslation: EN 'middle fifties', not 'approaching fifty' |
| 115 | je lui faisais à peu près autant confiance que j'aurais pu lancer le pare-étincelles → je ne m'y fiais pas plus loin que je n'aurais pu lancer le pare-étincelles | 5 Idiom: garbled rendering of 'trusted it about as far as I could have thrown the fire screen' |
| 117 | ce mot, <it>broche</it>, entre nous → ce mot, broche, entre nous | 6 Markup: literal <it> tags printed in text (EN not italic here; italic option logged as decision) |
| 131 | à environ un pouce d'une poire → à deux ou trois centimètres d'une poire | 8 Units: SAFE rule: literal 'about an inch' -> 2-3 cm |
| 160 | ou vous croyaient au marché → ou vous croisaient au marché | 3 Mistranslation: EN 'caught you at the market'; 'croyaient' = believed (typo) |
| 161 | de sa cachette près de la fenêtre → de son coin près de la fenêtre | 3 Mistranslation: EN 'her spot', not a hiding place |
| 178 | une tournure de phrase de parrain → une tournure de phrase d'inconnu | 3 Mistranslation: EN 'a stranger's turn of phrase'; 'parrain' = godfather |
| 190 | Quelques autres bric-a-brac. → Quelques autres objets. | 6 Typo/grammar: 'bric-a-brac' misspelt and cannot be pluralised with 'quelques autres'; EN 'A few other things' |
| 190 | pas un seul d'entre nous → pas une seule d'entre nous | 4 Agreement: mother, grandmother, Fiona: all women |
| 190 | Il y avait une valise dans le grenier, une vieille cantine, fermée à clé → Il y avait un coffre dans le grenier, une vieille malle de voyage, fermé à clé | 6 Term: trunk = 'coffre' everywhere else (11x); 'valise' = suitcase |
| 192 | cette cantine est fermée à clé → ce coffre est fermé à clé | 6 Term: trunk = 'coffre' |
| 196 | sur le reçu dans ma cantine → sur le reçu dans mon coffre | 6 Term: trunk = 'coffre' |
| 196 | dans la cantine aussi → dans le coffre aussi | 6 Term: trunk = 'coffre' |
| 197 | dans cette cantine verrouillée → dans ce coffre verrouillé | 6 Term: trunk = 'coffre' |
| 197 | dans ta cantine → dans ton coffre | 6 Term: trunk = 'coffre' |
| 200 | depuis des ans → depuis des années | 6 Typo: 'des ans' is not idiomatic; EN 'for years' |
| 200 | « La Société Historique. » → « La Société historique. » | 6 Typography: 'Société historique' |
| 201 | une cantine que toi seule → un coffre que toi seule | 6 Term: trunk = 'coffre' |
| 210 | On va à la Société Historique. → On va à la Société historique. | 6 Typography: 'Société historique' |
| 216 | Il a servi deux louches d'un bouillon → Il a servi deux bols d'un bouillon | 3 Mistranslation: EN 'ladled out two bowls'; 'les a posés' then agrees |
| 228 | La Société Historique. » → La Société historique. » | 6 Typography: 'Société historique' |
| 252 | Il y passait des semaines → Il y travaillait depuis des semaines | 3 Mistranslation: EN 'He'd been at it for weeks now' (ongoing) |
| 297 | La Société d’histoire de Frost Falls → La Société historique de Frost Falls | 6 Term: Historical Society = 'Société historique' elsewhere |
| 311 | From the Blackburn Family Papers, 1910–1930. On loan to the people of Frost Falls. → Extrait des papiers de la famille Blackburn, 1910–1930. Prêté aux habitants de Frost Falls. | 1 Untranslated: exhibit card left in English (text inside existing italic run) |
| 312 | « Mrs. Claus. » → « Madame Claus. » | 1 Untranslated: English honorific 'Mrs.' |
| 312 | Votre Mr. Hussein → Votre M. Hussein | 1 Untranslated: English honorific 'Mr.' |
| 312 | Regarde ça. → Regardez ça. | 5 Register: Neil and Jessica use vous (ch1, 'Votre' same para) |
| 313 | « Tu cours toujours après ta broche, ai-je dit. » → « Vous courez toujours après votre broche, ai-je dit. » | 5 Register: Jessica/Neil are on vous terms |
| 314 | Tu savais ça ? → Vous saviez ça ? | 5 Register: Neil/Jessica vous |
| 316 | une Mrs. Pelletier → une certaine Mme Pelletier | 1 Untranslated: English honorific 'Mrs.' |
| 317 | une écharde sous un onglet → une écharde sous un ongle | 6 Typo: 'onglet' is wrong word; EN 'under a nail' |
| 325 | qui m’préoccupait → qui me préoccupait | 6 Typo: elision typo |
| 329 | d’un dernier quart de pouce → d’un dernier demi-centimètre | 8 Units: SAFE rule: literal 'a final quarter-inch' (~6 mm) |
| 338 | a-t-elle dit, non sans humour, en → a-t-elle dit, sans s'en désoler, en | 3 Mistranslation: EN 'not unhappily', not 'with humour' |
| 341 | Tu tricotages → Tu tricotes | 6 Typo: nonword |
| 347 | « Il ne dort pas, a dit Martha, et → « Il ne dort pas », a dit Martha, et | 6 Punctuation: narration was inside Martha's quotation |
| 347 | sans fioritures. Je lui ai apporté → sans fioritures. « Je lui ai apporté | 6 Punctuation: reopen quotation after narration |
| 349 | l'été dernier → au printemps dernier | 3 Mistranslation: EN 'last spring' |
| 364 | Cela m'a poignée en plein cœur. → Cela m'a prise à la gorge. | 6 Typo/idiom: 'poignée' is not a verb form; EN 'caught me square in the throat' |
| 367 | les nouveaux fils s'élevant dans l'obscurité → les nouvelles guirlandes montant encore éteintes | 3 Mistranslation: EN 'the new strands going up dark' = unlit, not into darkness |
| 374 | le grand terrain vague au sud d'Evergreen qui descendait depuis le carré → le grand pré communal au sud d'Evergreen qui descendait depuis le square | 3 Mistranslation: EN 'the big common ... from the square'; 'terrain vague' = wasteland, 'le carré' is not a place |
| 374 | un comité allait s'en formaliser pendant une heure → un comité allait le peaufiner pendant une heure | 3 Mistranslation: EN 'fussed over for an hour by committee'; 's'en formaliser' = take offence |
| 374 | « Tu me poserais ça le long de l'estrade, s'il te plaît ? Fais attention à celle qui est molle. » → « Vous me poseriez ça le long de l'estrade, s'il vous plaît ? Faites attention à celle qui est molle. » | 5 Register: a stranger addressing Jessica: vous |
| 398 | C'est à ça qu'sert une ville → C'est à ça que sert une ville | 6 Typo: elision typo |
| 400 | un presse-papiers dans une main → un porte-bloc dans une main | 3 False friend: clipboard = porte-bloc; presse-papiers = paperweight |
| 408 | inspecter le clip brillant du presse-papiers → inspecter la pince brillante du porte-bloc | 3 False friend: clipboard = porte-bloc |
| 429 | munie d'un sous-main à pince → munie d'un porte-bloc | 6 Term: clipboard = 'porte-bloc' (cf. ch6); 'sous-main' = desk blotter |
| 433 | « C'comique, non ? → « C'est comique, non ? | 6 Typo: elision typo |
| 436 | Il y a avait beaucoup → Il y avait beaucoup | 6 Typo: doubled 'a' |
| 448 | là où l'avenue Evergreen cessait → là où Evergreen Avenue cessait | 4 Proper name: street name kept as 'Evergreen Avenue' everywhere else |
| 460 | Le festival donne du fil à retordre à un forgeron. → Le festival donne du travail à un forgeron. | 3 Mistranslation: EN 'keeps a smith busy'; 'donner du fil à retordre' = cause trouble |
| 464 | l'écran pare-feu → le pare-étincelles | 6 Term: fire screen = 'pare-étincelles' in ch1 |
| 466 | Je sais ce que ça a l'air. → Je sais de quoi ça a l'air. | 6 Grammar: anglicism; correct idiom 'de quoi ça a l'air' |
| 478 | en lui diciendo de n'y plus repenser → en lui disant de n'y plus repenser | 1 Untranslated: Spanish word 'diciendo' in French text |
| 480 | Mais s'en faut de peu n'est pas certitude → Mais à peu de chose près n'est pas certitude | 6 Grammar: ungrammatical; EN 'near enough is not the same as sure' |
| 494 | elle avait séjouné là → elle avait séjourné là | 6 Typo: missing r |
| 496 | pour vous être enquéri d'elle → pour vous être enquis d'elle | 6 Typo: past participle of s'enquérir is 'enquis' |
| 521 | De près, pourtant. → J'en suis proche, pourtant. | 6 Grammar: EN 'Close, though.'; 'De près' is not a sentence here |
| 545 | Il had ri → Il avait ri | 1 Untranslated: English auxiliary 'had' left in French |
| 554 | en se tordant son bonnet entre les mains → en tordant son bonnet entre ses mains | 6 Grammar: reflexive + possessive doubled |
| 560 | par-dessus la lisière supérieure → par-dessus la traverse supérieure | 3 Mistranslation: EN 'top rail' (of the fence); 'lisière' = edge of a wood/fabric |
| 592 | Pip had been nosing along the bottom rail of the paddock fence the whole while. I had the note in my coat pocket, and now she did what she'd taken to doing whenever it was near. She came to the pocket… → Pip avait fureté tout ce temps le long de la traverse inférieure de la clôture du paddock. J’avais le mot dans la poche de mon manteau, et elle a fait alors ce qu’elle avait pris l’habitude de faire c… | 1 Untranslated: whole paragraph left in English; translated from the English source |
| 603 | pour la Société d'histoire avant → pour la Société historique avant | 6 Term: Historical Society = 'Société historique' |
| 613 | ne déridaient pas les cordons de la bourse → ne déliaient pas les cordons de la bourse | 6 Idiom: idiom is 'délier les cordons de la bourse' |
| 617 | Théo fait du bon travail → Theo fait du bon travail | 4 Proper name: name is 'Theo' everywhere else |
| 617 | elle l'a toujours fait. Il a esquissé → elle l'a toujours fait. » Il a esquissé | 6 Punctuation: narration was inside the mayor's quotation |
| 617 | prêté l'oreille. Peut-être → prêté l'oreille. « Peut-être | 6 Punctuation: reopen quotation |
| 629 | aussi vite apparu qu'disparu → aussi vite apparu que disparu | 6 Typo: bad elision |
| 631 | a-t-elle répondu. Sa plume n'a pas cessé d'avancer. Surtout → a-t-elle répondu. » Sa plume n'a pas cessé d'avancer. « Surtout | 6 Punctuation: narration inside quotation |
| 639 | La Société d'histoire. → La Société historique. | 6 Term: Historical Society = 'Société historique' |
| 639 | C'est le rayon de Théo. → C'est le rayon de Theo. | 4 Proper name: name is 'Theo' everywhere else |
| 639 | « Je ne connais rien aux Blackburn, a-t-elle déclaré, ce qui → « Je ne connais rien aux Blackburn », a-t-elle déclaré, ce qui | 6 Punctuation: narration inside quotation |
| 639 | dans son dos. C'est le rayon → dans son dos. « C'est le rayon | 6 Punctuation: reopen quotation |
| 655 | l'acte de propriété de l'auberge Winter Wonderland → l'acte de propriété du Winter Wonderland Inn | 4 Proper name: inn name kept as 'Winter Wonderland Inn' elsewhere |
| 657 | dont je ne pouvais plus entendre le nom de Blackburn sans penser à elles → auxquelles je ne pouvais plus m'empêcher de penser en entendant le nom de Blackburn | 3 Mistranslation: garbled: said I couldn't hear their name 'Blackburn'; EN 'couldn't hear the name Blackburn without thinking of' |
| 662 | de la Société d'histoire s'est réuni → de la Société historique s'est réuni | 6 Term: Historical Society = 'Société historique' |
| 674 | l'homme que je venais de soupçonner → l'homme que j'avais commencé à soupçonner | 3 Mistranslation: EN 'had begun to suspect' (not 'had just suspected') |
| 682 | « Mrs. Claus ! Et Pip ! » → « Madame Claus ! Et Pip ! » | 1 Untranslated: English honorific 'Mrs.' |
| 694 | Je ne vais pas vous mentir, Mrs. Claus, → Je ne vais pas vous mentir, madame Claus, | 1 Untranslated: English honorific 'Mrs.' |
| 698 | en se contentant de formuler des vœux, Mrs. Claus. → en se contentant de formuler des vœux, madame Claus. | 1 Untranslated: English honorific 'Mrs.' |
| 700 | Jamal Washington had le moindre moyen → Jamal Washington avait le moindre moyen | 1 Untranslated: English 'had' left in French |
| 706 | « Mrs. Claus, je portais → « Madame Claus, je portais | 1 Untranslated: English honorific 'Mrs.' |
| 706 | de ne pas poser mon pied sur une chaise centenaire → de ne pas passer le pied à travers une chaise centenaire | 3 Mistranslation: EN 'put my foot through' |
| 708 | n'avait jamais had tout cela → n'avait jamais eu tout cela | 1 Untranslated: English 'had' left in French |
| 712 | pour fixer la trace d'humidité → et se mettait à fixer la trace d'humidité | 3 Mistranslation: 'pour' made staring the purpose of placing a case; EN 'just stare' |
| 727 | avec le vert de la mairie et le reste → avec la place, la mairie et tout le reste | 3 Mistranslation: EN 'green and Town Hall and all' (the green = la place) |
| 731 | — Bonjour, Mrs. Claus, → — Bonjour, madame Claus, | 1 Untranslated: English honorific |
| 737 | avec de l’eau jusqu’aux paturons dans les feuilles mortes → enfoncée jusqu’aux paturons dans les feuilles mortes | 3 Mistranslation: fountain is dry (shut off); EN 'ankle-deep in fallen leaves' |
| 741 | — Mrs. Claus ! — → — Madame Claus ! — | 1 Untranslated: English honorific |
| 743 | le vieux Mr. Kim → le vieux M. Kim | 1 Untranslated: English honorific |
| 755 | aller à l’atelier, Mrs. Claus ? → aller à l’atelier, madame Claus ? | 1 Untranslated: English honorific |
| 763 | et Mr. Kim a replié → et M. Kim a replié | 1 Untranslated: English honorific |
| 767 | Il y a vait un maître chanteur → Il y avait un maître chanteur | 6 Typo: split word |
| 771 | sans faire sauter une seule mailles → sans faire sauter une seule maille | 6 Typo: agreement |
| 771 | posés sur le sol entre eux → posés sur le sol entre elles | 4 Agreement: the circle are all women |
| 779 | Théo n'arrêtait pas → Theo n'arrêtait pas | 4 Proper name: 'Theo' elsewhere |
| 780 | un autre gratin à Théo → un autre gratin à Theo | 4 Proper name: 'Theo' elsewhere |
| 794 | la table des tourtes → la table des tartes | 6 Term: pie = 'tarte' (ch1 apple pie); 'tourte' = covered savoury pie |
| 795 | la table des tourtes → la table des tartes | 6 Term: pie = 'tarte' |
| 811 | « Sam n'a eu aucune chance. → « Sam n'en a jamais eu l'occasion. | 3 Mistranslation: EN 'had no chance' = opportunity, not luck |
| 814 | Et ton grand dadais de monsieur Carter. → Et ton bruyant monsieur Carter. | 3 Mistranslation: EN 'your loud Mr. Carter'; 'dadais' = oaf |
| 823 | tous les deux partis pour de bon → tous les deux écartés pour de bon | 3 Mistranslation: EN 'gone' = off the suspect list |
| 844 | « Tu ne savais pas, ai-je dit. Comment aurais-tu pu ? C'est pour cette raison exacte que je te l'ai dit maintenant. » → « Vous ne saviez pas, ai-je dit. Comment auriez-vous pu ? C'est pour cette raison exacte que je vous l'ai dit maintenant. » | 5 Register: Jessica uses vous with Sam in the same scene (834, 852) and ch8 |
| 848 | bien que j'étais venue → bien que je sois venue | 6 Grammar: 'bien que' takes the subjunctive |
| 850 | Un forgeur finit le fer → Un forgeron finit le fer | 6 Typo: smith = forgeron |
| 850 | l'écran de cheminée → le pare-étincelles | 6 Term: fire screen = 'pare-étincelles' (ch1) |
| 852 | Juste vous souvenir du visage. → Souvenez-vous juste du visage. | 6 Grammar: infinitive where imperative needed |
| 867 | et observez votre visage pendant que je le dirai → et observer votre visage pendant que je le dirai | 3 Mistranslation: imperative made Carter watch his own face; EN 'and watch your face while I tell it' (Jessica watches) |
| 871 | en l'admirant dedans → pour s'y admirer | 3 Mistranslation: EN 'admiring herself in it' |
| 877 | « Un demi-million. Il s'est rejeté en arrière et a poussé un sifflement étouffé. Bon sang. → « Un demi-million. » Il s'est rejeté en arrière et a poussé un sifflement étouffé. « Bon sang. | 6 Punctuation: narration inside quotation |
| 877 | C'est cruel, M<sup>me</sup> Claus, → C'est cruel, madame Claus, | 6 Markup: literal <sup> HTML tags in text |
| 887 | une lettre, M<sup>me</sup> Claus, → une lettre, madame Claus, | 6 Markup: literal <sup> HTML tags in text |
| 887 | qui ont pli bagage → qui ont plié bagage | 6 Typo: plié |
| 889 | s'était à moitié tuer à garder → s'était à moitié tuée à garder | 6 Typo: participle agreement |
| 903 | à reclassement une fois retrouvé → à reclasser une fois retrouvé | 6 Grammar: EN 'refile when found' |
| 905 | le vol du broche de famille → le vol de la broche de famille | 4 Gender: broche is feminine |
| 907 | décrire un broche → décrire une broche | 4 Gender: broche is feminine |
| 908 | cette note had lu cette fiche → cette note avait lu cette fiche | 1 Untranslated: English 'had' left in French |
| 923 | Pip dandinant des fesses devant nous → Pip se dandinant devant nous | 6 Grammar: 'se dandiner' is pronominal |
| 934 | et un presse-papiers sous le bras → et un porte-bloc sous le bras | 3 False friend: clipboard = porte-bloc |
| 936 | et elle a levé le presse-papiers → et elle a levé le porte-bloc | 3 False friend: clipboard = porte-bloc |
| 948 | Aie l'argent prêt d'ici là, ou toute la ville sera au courant pour ta famille dès lundi matin. → Ayez l'argent prêt d'ici là, ou toute la ville sera au courant pour votre famille dès lundi matin. | 5 Register: first blackmail note (177) addresses Fiona as vous |
| 948 | Ne fais pas l'idiote avec ça. → Ne faites pas l'idiote avec ça. | 5 Register: blackmailer uses vous |
| 952 | je ne l'aurais pas en trois ans → je ne l'aurai pas en trois ans | 6 Typo: future, not conditional |
| 960 | au fait d'agir seule → à la question de savoir s'il avait agi seul | 3 Mistranslation: EN 'whether-alone' = whether he acted alone; 'seule' made it Jessica |
| 964 | pour portes ouvertes de l'auberge → pour les portes ouvertes de l'auberge | 6 Typo: missing article |
| 976 | celle qui les avaient portées → celle qui les avait portées | 6 Typo: agreement |
| 982 | avec Pip d'un pas canardeur tout près de mon talon → avec Pip qui se dandinait tout près de mon talon | 6 Typo/nonword: 'canardeur' is not a word; EN 'waddling' |
| 986 | les tourtes de Greta → les tartes de Greta | 6 Term: pie = 'tarte' |
| 993 | « On aurait dit que tu t'apprêtais à plaquer → « On aurait dit que vous vous apprêtiez à plaquer | 5 Register: Noriko and Jessica are on vous terms (ch6, same para 995) |
| 995 | Il y a quelque chose que je devrais savoir, Mme Claus ? → Il y a quelque chose que je devrais savoir, madame Claus ? | 6 Typography: address form spelled out, as elsewhere in dialogue |
| 998 | « Tu sais où se trouve le poste. → « Vous savez où se trouve le poste. | 5 Register: Noriko/Jessica vous |
| 998 | « Ton manchot a rapporté → « Votre manchot a rapporté | 5 Register: Noriko/Jessica vous |
| 999 | « Ne lui dis pas », ai-je dit. → « Ne le lui dites pas », ai-je dit. | 5 Register: Noriko/Jessica vous |
| 1000 | nous avions trouvé Boule de Neige → nous avions trouvé Snowball | 4 Proper name: dog is 'Snowball' everywhere else |
| 1009 | la vérité que j'avais employée ces hommes à fuir → la vérité que je m'étais servie d'eux pour fuir | 6 Grammar: garbled construction; EN 'the truth I'd been using them to avoid' |
| 1013 | que laisse la forme du cirié → que laisse la forme du papetier | 6 Typo/nonword: 'cirié' is not a word; EN 'a papermaker's screen' |
| 1015 | Un homme bon venait de commettre un acte terrible → Un homme bon avait commis un acte terrible | 3 Mistranslation: EN 'had done', not 'had just done' |
| 1017 | I know how your family came by this inn, → Je sais comment votre famille a mis la main sur cette auberge, | 1 Untranslated: quotation of the first note left in English (italic run); wording matched to para 177 |
| 1029 | une corvée de plus en fin de journée → une corvée de plus par une longue journée | 3 Mistranslation: it is morning; EN 'on a long day' |
| 1033 | PROPERTY — EVERGREEN AVE → PROPRIÉTÉ — EVERGREEN AVE | 1 Untranslated: file tab label word left in English (italic run) |
| 1047 | ou qu'elle pitiérait, ou les deux → ou qui lui faisait pitié, ou les deux | 6 Typo/nonword: 'pitiérait' is not a word; EN 'pitied' |
| 1051 | <hi>le saphir en son cœur</hi> → le saphir en son cœur | 6 Markup: literal <hi> tags printed in text |
| 1051 | descendre l'avenue Evergreen incognito → descendre Evergreen Avenue incognito | 4 Proper name: 'Evergreen Avenue' elsewhere |
| 1055 | Elles l'avaient fait ensemble. → Ils l'avaient fait ensemble. | 4 Agreement: Theo + Vera: masculine plural |
| 1057 | Je les tenais toutes les deux. → Je les tenais tous les deux. | 4 Agreement: Theo + Vera |
| 1057 | une amie qu'elles avaient broyée entre elles → une amie qu'ils avaient broyée entre eux | 4 Agreement: Theo + Vera |
| 1061 | Maintenant, je dois choisir comment cela va se terminer. → Maintenant, il me fallait choisir comment cela se terminerait. | 6 Tense: drift into present; EN past |
| 1068 | dans sa valise au grenier → dans son coffre au grenier | 6 Term: trunk = 'coffre' |
| 1068 | Les lettres cesseraient → Les notes cesseraient | 3 Ambiguity: EN 'The notes would stop'; 'lettres' reads as the Blackburn letters |
| 1076 | cette valise de grenier → ce coffre du grenier | 6 Term: trunk = 'coffre' |
| 1086 | ronger les murs en cachettes → ronger les murs en cachette | 6 Typo: invariable 'en cachette' |
| 1088 | certains regretteront que tu n'aies rien dit → certains regretteront que tu n'aies pas laissé les choses en l'état | 3 Reversed meaning: EN 'wish you'd left it alone' — she DID speak; 'n'aies rien dit' inverts it |
| 1098 | qui a brisék un homme bon → qui a brisé un homme bon | 6 Typo: stray k |
| 1137 | qu'il a essayée de blesser → qu'il a essayé de blesser | 6 Grammar: participle before infinitive does not agree here |
| 1160 | Le papier vélin épais aux vergures marquées. → Le papier vergé épais aux vergures marquées. | 3 Mistranslation: EN 'laid' paper; 'vélin' is wove paper (no laid lines) — contradicts the clue |
| 1164 | j'étais déjà engrené → j'étais déjà pris dans l'engrenage | 6 Idiom: 'engrené' is not idiomatic here; EN 'already in it' |
| 1164 | Je l'ai vue grisonner. → Je l'ai vue blêmir. | 3 Mistranslation: EN 'go gray' (pallor), not hair greying |
| 1168 | Je me suis alors tourné vers Vera → Je me suis alors tournée vers Vera | 4 Agreement: narrator is female |
| 1170 | « Theo a commis le vol. → « Theo détenait le vol. | 3 Mistranslation: EN 'Theo had the theft' = had the knowledge of it (cf. 1051 'Theo détenait le vol'); he did not commit it |
| 1170 | « Il a commis le vol. Tu avais l'acte. → « Il détenait le vol. Tu avais l'acte. | 3 Mistranslation: EN 'He had the theft. You had the deed.' |
| 1174 | tellement dans le pétrin, Mme Claus. → tellement dans le pétrin, madame Claus. | 6 Typography: address form spelled out in dialogue |
| 1189 | « La justice réparatrice, → « La justice restaurative, | 6 Term: term introduced as 'justice restaurative' in ch25 (1115) |
| 1207 | son bureau à l'hôtel de ville → son bureau à la mairie | 6 Term: Town Hall = 'la mairie' everywhere else |
| 1213 | il n'avait plus aucune mordant → il n'avait plus aucun mordant | 4 Gender: mordant is masculine |
| 1215 | la chose même que Theo avait ruiné sa santé à essayer de sauver → la chose même que Theo s'était perdu à vouloir sauver | 3 Mistranslation: EN 'ruined himself trying to save' (not his health) |
| 1221 | que la Société Historique traversait → que la Société historique traversait | 6 Typography: 'Société historique' (lower-case h) is the dominant spelling |
| 1222 | que la Société Historique traverse → que la Société historique traverse | 6 Typography: 'Société historique' |
| 1226 | vous l'entendrez telle qu'elle est pensée → vous l'entendrez dans l'esprit où je le dis | 6 Grammar: 'telle qu'elle' has no feminine antecedent ('quelque chose') |
| 1246 | Pip s'est approchée du poêle pour inspecter le dossier → Pip a quitté le poêle pour venir inspecter le dossier | 3 Mistranslation: EN 'came over from the stove' (direction reversed) |
| 1248 | Pas la version mondaine → Pas la version des commérages | 3 Mistranslation: EN 'the gossip version'; 'mondaine' = society/high-life |
| 1252 | lors de l'atelier, → au cercle, | 6 Term: the knitting circle = 'le cercle'; 'atelier' is Nick's workshop |
| 1254 | Foutez-lui la paix. → Laissez-la reposer en paix. | 5 Register: vulgar and off-meaning; EN 'Let her rest' (Constance is dead) |
| 1260 | qu'elle se rappelerait → qu'elle se rappellerait | 6 Typo: spelling |
| 1260 | jeté l'opprobre sur l'endroit → plongé l'endroit dans le chagrin | 3 Mistranslation: EN 'grieved the place' (caused grief), not shame |
| 1264 | Martha m'a attrapé la main à l'atelier un après-midi gris → Martha m'a attrapé la main au cercle un après-midi gris | 6 Term: the knitting circle = 'le cercle' |
| 1264 | comme si elle ne venait pas de me détruire complètement → comme si elle ne venait pas de me bouleverser complètement | 3 Mistranslation: EN 'undone me' = moved to tears, not destroyed |
| 1273 | afin que ceux qui viendront après nous connaissent et sachent → afin que ceux qui viendront après nous nous connaissent et sachent | 2 Omission: object 'us' dropped; EN 'may know us and know we thought of them' |
| 1283 | Boule de Neige portait son chapeau → Snowball portait son chapeau | 4 Proper name: dog is 'Snowball' |
| 1283 | Pip se blottissait, chaud, contre ma botte → Pip se blottissait, chaude, contre ma botte | 4 Agreement: Pip is female |
| 1299 | le long des plus petites branches de l'orme → le long des plus basses branches de l'orme | 3 Mistranslation: EN 'lowest twigs' (cf. 1311) |
| 1301 | Danseuse cette fois-ci → Dancer cette fois-ci | 4 Proper name: reindeer is 'Dancer' in ch10 |
| 1305 | autour du cou de Danseuse → autour du cou de Dancer | 4 Proper name: 'Dancer' |
| 1307 | Pip était allé se placer juste sous le nez de Danseuse → Pip était allée se placer juste sous le nez de Dancer | 4 Proper name/agreement: 'Dancer'; Pip female |
| 1307 | quelle part de celle-ci tournait encore autour lorsque nous serions rentrés → quelle part de plus de celle-ci y tournerait lorsque nous serions rentrés | 3 Mistranslation: EN 'how much more of it would be circling there' |
| 1316 | être tout près de devant quand → être tout devant quand | 6 Grammar: 'tout près de devant' ungrammatical; EN 'near the front' |
| 1332 | trempant dans un pouce d'eau → trempant dans deux ou trois centimètres d'eau | 8 Units: SAFE rule: literal 'an inch of water' -> 2-3 cm |
| 1372 | There are more mysteries afoot for Jessica Claus!  → D'autres mystères attendent Jessica Claus !  | 1 Untranslated: end-of-book line left in English (text in existing italic run; <bt> untouched) |
| 1372 |  is coming soon. →  paraîtra bientôt. | 1 Untranslated: end-of-book line left in English (italic run) |
| 1374 | What's Next? → Et ensuite ? | 1 Untranslated: back-matter heading left in English; TOC (para 24) already has 'Et ensuite ?' |
| 1376 | Greta a préparé le même roulé à la cannelle depuis quarante ans. → Greta prépare le même roulé à la cannelle depuis quarante ans. | 6 Tense: 'depuis' + duration requires present; EN 'has made ... for forty years' |
| 1380 | tous les enfants de l'avenue Evergreen → tous les enfants d'Evergreen Avenue | 4 Proper name: 'Evergreen Avenue' elsewhere |
| 1384 | And at the bright end of the avenue, a new patisserie has dated its grand opening to the one week the Holly Jolly will be dark. → Et, au bout illuminé de l'avenue, une nouvelle pâtisserie a fixé son inauguration à l'unique semaine où le Holly Jolly restera fermé. | 1 Untranslated: back-cover blurb paragraph left in English; translated from the English source |
| 1388 | There are more mysteries afoot for Jessica Claus!  → D'autres mystères attendent Jessica Claus !  | 1 Untranslated: line left in English (italic run) |
| 1388 |  is coming soon. →  paraîtra bientôt. | 1 Untranslated: line left in English (italic run) |
| 1394 | Elle recouvrait désormais l'avenue Evergreen d'une → Elle recouvrait désormais Evergreen Avenue d'une | 4 Proper name: 'Evergreen Avenue' elsewhere |
| 1406 | et elle a fronçé les sourcils → et elle a froncé les sourcils | 6 Typo: cedilla before e |
| 1412 | Pip had already been spoken to about both. Twice. → Pip s'était déjà fait gronder pour l'un comme pour l'autre. Deux fois. | 1 Untranslated: sentence left in English |
| 1422 | Non pas les miles. Il y en avait eu un bon paquet, mais je ne parlais pas des miles. → Non pas les kilomètres. Il y en avait eu un bon paquet, mais je ne parlais pas des kilomètres. | 8 Units (idiom): idiom 'not the miles': 'miles' does not read natively; idiomatic equivalent |
| 1458 | Je leur apporterai une tourte le jour → Je leur apporterai une tarte le jour | 6 Term: pie = 'tarte' |
| 1464 | un large terrain vague engazonné doté → une large étendue communale toute blanche dotée | 3 Mistranslation: EN 'a wide white common'; 'terrain vague' = wasteland |
| 1482 | comme un pas sur mon propre perchoir → comme un pas dans mon propre escalier | 3 Mistranslation: EN 'a footstep on my own stair'; 'perchoir' = perch |
| 1486 | et je me suis rassis pour terminer → et je me suis rassise pour terminer | 4 Agreement: narrator female |
| 1490 |  is coming soon! →  paraîtra bientôt ! | 1 Untranslated: line left in English (italic run) |

## Decisions logged

- FR-D1: 7 Scene breaks (para 1370, 1386, 1488)
- FR-D2: 5 Dialogue punctuation (para whole book)
- FR-D3: 1 Untranslated (front matter) (para 4)
- FR-D4: 2 Omission (TOC) (para 22)
- FR-D5: Book title / <bt> markers (para 727, 1011, 1248)
- FR-D6: Italics added by translator (para 655, 662, 974, 1160, 1420 (+117, 1051))
- FR-D7: 1 Untranslated (in-world sign) (para 297)
- FR-D8: 5 Register tu/vous (para Vera 645 vs 1041/1170/1209; Jamal 684 vs 704/710/714; Mark 387 vs 396/398)
- FR-D9: 6 Term (penguin) (para 306, 328, 375, 385, 386, 421, 682, 745, 895, 1307)
- FR-D10: 3 False friend (mittens) (para 337 + 12 more)
- FR-D11: 8 Units (round figure — ESCALATE) (para 185)
- FR-D12: 6 Tense drift (para ch9 (507–549), ch22 (1009–1022); scattered passé simple (137, 448, 1172))
- FR-D13: 6 Term (the green / the note) (para e.g. 53, 170, 266, 374, 934, 1029, 1148, 1464)

## Refusals

- First pass refused 1017 and 1033 ('old' crossed an italic/roman run boundary); re-applied as single-run fixes inside the italic run — both now APPLIED. No outstanding refusals.

## Quoted but not found

- None.
