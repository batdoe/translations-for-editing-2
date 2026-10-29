# PROOFCHECK (FULL) — Inn Trouble - ASSEMBLED - FORMATTED_French (2026-10-28)

- **Mode:** FULL. I read the whole book sentence by sentence, with each English paragraph next to its French paragraph(s), in order: front matter, blurb, Ch1–Ch31, the sell lines, What's Next? and the Flour Play excerpt. This pass follows the same day's targeted pass (`…_PROOFCHECK.md`, 22 fixes) and a follow-up backup (`.followup.docx`).
- **Files:** I edited `translated/corrected/Inn Trouble - ASSEMBLED - FORMATTED_French.docx` in place. The English is `translate_now/Inn Trouble - ASSEMBLED - FORMATTED.docx`. The raw file `_superseded/…_French.docx` was read-only and used only to sort each defect into miss or regression. The excerpt reference was `translated/corrected/Flour Play - ASSEMBLED - FORMATTED_French.docx` Ch1.
- **Backup:** `_EditLedgers/_proofcheck_backups/Inn Trouble - ASSEMBLED - FORMATTED_French.20261028-234847.full.docx`
- **Chapters read in full:** 31 of 31, plus the front matter, the blurb and all of the back matter.
- **Skipped per the brief:** the step-2 diff audit and the 20-row ledger sample, which the targeted pass already did.
- **Flags (step 1):** the re-run shows A=0 B=0 C=0 D=0 E=0 F=0 G=0 H=20 I=0 J=0. These are the same 20 H flags the targeted report judged as false positives (livre, mille, pouce, once, pied, and centime = PC-FR2-1). No flag was left unjudged.
- **Totals:** 64 text edits in 59 paragraphs: 62 misses (already in the raw file) plus 2 edits fixing one regression in [547]. Refusals: 0. Every match fell inside a single `<w:t>`, so no run was merged.

## Targeted checks for today (all ✓ after this pass)
- **The note is never *lettre*.** I grepped every *lettre(s)* in the book (60+ hits). All of them are the 1924 letters, Jessica's Pole mail, Fiona's mail ([946]/[974], where the English also says "letters"), or grant letters. None is the blackmail note. The note is *mot*/*note*; the mix is Lisa's open style choice (IT2-FR-26-1).
- **Theft wording:** « avait / détenait le secret du vol » appears at [1019], [1051], [1170] ×2. There is no bare « avait le vol », and nothing says Theo committed the theft.
- **Porch = *porche*:** there is no *véranda* left. The 3 *perron* are all "stoop" ([47], [169], [1394]), which is correct. The porch **brackets** had three names (*ferrures* [93], *consoles* [95] [490], *supports* [830] [850] [856]). They are now *consoles* in all six places.
- **Paddock:** always *paddock*. There is no *enclos* left.
- **Spoiler-gender:** before the Ch26 reveal I checked every reference to the unknown writer or courier: quiconque, quelqu'un, cette personne, l'auteur, maître chanteur, la silhouette, and generic *il*/*lui*. I found one real slip, [177] « quiconque l'avait **écrite** », where the feminine participle can be read as the writer being a woman (see the table). Everything else is either faithful to an English "he" (Jessica's and Fiona's own assumption at [533], [946], [954], [966], [1001]) or the standard French generic masculine (see decision PC-FR2F-1). Ch21's « une silhouette … autour d'elle » is grammatical agreement, and the figure turns out to be Mrs. Pelletier, so it gives nothing away.
- **The run's lessons:** Ch19 « C'est l'amour qui le lui permet » ✓ · Ch27 « s'était perdu à vouloir sauver » ✓ · the Ch19 card is « la fiche était de la main de Theo » ✓ · « à sa sœur » ✓ · papers/archives vs *acte* ✓ (the one stray *titre de propriété* is fixed) · « ton homme » ✓ · the green = *parc* ✓ · the clue phrase « le saphir en son cœur » is identical at all 9 places, and the three "five words" lines are ✓ · *jus de pomme* ✓ · Sam is owed the money ✓ · "six letters" kept as in the English ✓ · the narration is passé composé + imparfait throughout (I scanned for passé simple and found 0).

## Missed by the first pass (all APPLIED)
| Para | Ch | French (was) | English | Class | Fix |
|---|---|---|---|---|---|
| 32 | blurb | « il nomme le saphir au cœur de la broche » | "names the stone at the brooch's heart" | addition (the blurb deliberately says "stone") | « la pierre » |
| 65 | 1 | « n'avait point masqués » | — | register (literary *point*) | « pas » |
| 71 | 1 | « Par-dessus, son regard a glissé par-dessus mon épaule » | "Over the top of it her eyes went past my shoulder" | doubled phrase | « Par-dessus le panier, son regard a glissé au-delà de mon épaule » |
| 93 | 1 | « les ferrures de porche » · « cette zénitude tranquille » | "porch brackets" · "a craftsman's easy calm" | term drift · register (slang) | « consoles de porche » · « ce calme tranquille » |
| 137 | 1 | « semblait par moments n'être » | "seemed for a moment" | mistranslation | « a semblé un instant » |
| 149 | 1 | « Un fil desserré. » | "A loose wire." (repeats the earlier « Un faux contact ») | term drift | « Un faux contact. » |
| 157 | 1 | « je n'ai point tourné » | — | register | « pas » |
| 177 | 2 | « quiconque l'avait **écrite** » | "whoever had written it" (it = the note, *mot*, masc.) | agreement + **spoiler-gender** (can be read as a woman writer) | « l'avait écrit » |
| 197 | 2 | « une boîte fermée à clé que toi seule as ouverte » | "a locked trunk that only you have opened" | term drift (trunk = *coffre*) | « un coffre fermé à clé … ouvert » |
| 248 | 3 | « j'ai laissé le temps suspendu à cela » | "I let it be only that" | garbled | « je n'en ai pas demandé davantage » |
| 307, 354 | 4, 5 | « les boîtes des Blackburn » | "the Blackburn boxes" | term drift (*cartons* ×3) | « les cartons des Blackburn » |
| 347 | 5 | « la platitude de sa voix » | "the flatness of her voice" | false friend (*platitude* = banality) | « le ton monocorde » |
| 359 | 5 | « une neige de début octobre » | "an October first snow" | mistranslation | « une première neige en octobre » |
| 374, 388 | 6 | « petits cucurbitacés », « des cucurbitacés » | gourds | gender/spelling (the noun is feminine, as at [49]) | « petites cucurbitacées », « des cucurbitacées » |
| 376 | 6 | « dans le couvercle arraché d'une lanterne » | "the torn-open top of a jack-o'-lantern" | mistranslation | « dans le haut éventré » |
| 391 | 6 | « une citrouille qui l'avait offensé » | "a gourd that had offended him" | term (gourd ≠ pumpkin) | « une cucurbitacée » |
| 414 | 6 | « Autour de chez nous, Noël arrive en avance » | "Around our house, Christmas comes early" | calque | « Chez nous » |
| 432 | 7 | « selon qu'elle se rappelle ou non le goût de sa nourriture » | "whether they remember to taste their food" | mistranslation | « selon qu'elle pense ou non à goûter ce qu'elle mange » |
| 472 | 8 | « les hommes qui savent exprimer un sentiment » | "men who can **wear** a feeling" (fake one) | reversed sense | « porter un sentiment comme un masque » |
| 554 | 10 | « je ne te le fais pas dire » (= "you said it") | "I don't mind telling you" | mistranslated idiom | « je ne te le cache pas » |
| 627 | 11 | « ne pas laisser peser le silence qu'on n'entendait que gratter la plume » | "to fill the pen-scratching quiet" | garbled | « meubler un silence que seul troublait le grattement de la plume » |
| 649 | 11 | « Pas pour grand monde cette année. » | "Not for anyone this year." | weakened | « Pour personne, cette année. » |
| 669 | 12 | « une fondation en ville » | "a foundation in the city" | mistranslation (*en ville* = in town) | « de la grande ville » |
| 671 | 12 | « Je ne lui ai pas pardonné. Mais j'ai compris » | "I didn't forgive it. But I understood it" (a hypothetical act; Jessica only suspects) | mistranslation (states Theo's guilt as a fact) | « Je ne l'excusais pas. Mais je le comprenais » |
| 743 | 14 | « de l'atelier mécanique » | "the auto shop" (Ch1 says *garage*; *atelier* is Nick's workshop) | term drift | « du garage » |
| 765 | 14 | « un renne rentrant de lui-même … qu'elle » | "a reindeer walking herself home" | gender clash | « rentrant seul » |
| 812 | 16 | « À l'entendre, Pip » | "At her name" | mistranslation | « En entendant son nom » |
| 817 | 16 | « registres de propriété » | "property records" (Ch11 = *registres fonciers*) | term drift | « registres fonciers » |
| 823 | 16 | « ne pas porter mes soupçons sur lui **tant qu'il ne restera personne** d'autre à suspecter » | "not to settle on him until there's no one else left to suspect" | **reversed logic** | « avant qu'il ne reste plus personne d'autre » |
| 830, 850, 856 | 17 | « supports » | porch brackets | term drift | « consoles » (agreement fixed) |
| 910 | 19 | « avait écrit les **mots** qui terrorisaient Fiona » | "had written the notes" | ambiguity (in the five-words chapter, *mots* reads as "words") | « les notes » |
| 913 | 19 | « la marche du chemin du retour » | "the walk home" | redundant phrase | « du chemin du retour » |
| 995 | 21 | « Ça fait deux d'entre vous à surveiller » | "That's two of you watching" | calque | « Vous êtes donc deux à surveiller » |
| 1001 | 21 | « la main gantée d'Emma » | "Emma's mittened hand" | mistranslation (gloved; mittens are a book motif) | « la petite main d'Emma, dans sa moufle, » |
| 1068 | 24 | « le titre de propriété de l'auberge » | "the inn's deed" (settled word *acte*) | term drift (deed chain) | « l'acte de propriété » |
| 1096 | 24 | « C'est une nécessité. » | "There has to be." (a way) | mistranslation | « Il faut que ce soit possible. » |
| 1100 | 24 | « les guirlandes de fêtes » | "festival lights" | term drift | « du festival » |
| 1148 | 26 | « sans savoir l'un et l'autre qu'ils venaient » | "neither knowing the other was coming" | mistranslation | « sans que l'un sache que l'autre venait aussi » |
| 1160 | 26 | « Le papier vergé épais aux vergures marquées. » | "The heavy **cream** stock with the laid lines." | omission, in the clue chain | « Le papier vergé épais, couleur crème. » |
| 1176 | 26 | « **Elles** l'avaient saisie » | "They had taken it" (Theo + Vera) | pronoun (feminine from a distant *personnes*) | « Ils » |
| 1197 | 27 | « faire chanter un voisin » | "extort a neighbor" (= Fiona) | gender | « une voisine » |
| 1203 | 27 | « la marcher » (a road) | "walk it" | non-idiomatic | « la parcourir » |
| 1211 | 27 | « raide et coincée » | "stiff buttoned" | mistranslation (echoes « boutonnée jusqu'au menton ») | « raide et boutonnée » |
| 1233 | 28 | « Venais-je de dissuader …? Durant quelques blocs glacés » | "I'd just talked a kind man out of… there were a few cold blocks" | statement turned into a question; calque | « Je venais de dissuader …, et durant quelques pâtés de maisons glacés » |
| 1235 | 28 | « de quel bois Frost Falls se chauffait » · « La guérison des gens d'ici » | "what Frost Falls was made of" · "the healing of the people in it" | mistranslated idiom (a threat idiom) · mistranslation | « de quoi Frost Falls était capable » · « des personnes concernées » |
| 1250 | 29 | « Surtout, ils ont intégré cela » | "Mostly they folded it in" | mistranslation (*surtout* = above all) | « Pour l'essentiel » |
| 1260 | 29 | « J'étais persuadée à plus de moitié » | "I'd more than half expected" | calque | « J'étais plus qu'à moitié persuadée » |
| 1273 | 30 | « par un bel après-midi froid » | "one cold afternoon" | addition | « par un après-midi froid » |
| 1316, 1360 | 31 | « la boîte en cuivre » | the copper box (*coffret* ×9 in Ch30) | term drift | « le coffret en cuivre » (agreement fixed) |
| 1362 | 31 | « rediscutait de trésors » | "was chattering again" | non-word or wrong verb | « bavardait de nouveau » |
| 1394 | excerpt | « les simples courges » | "the plain pumpkins" (FP FR: « citrouilles ordinaires ») | mistranslation | « les citrouilles ordinaires » |
| 1466 | excerpt | « avait fait un pivot complet » | "had turned clean around" (FP FR: « avait fait demi-tour ») | **clue risk**: can be read as a 360° turn, which would undo the clue (the Czech lesson) | « avait fait demi-tour » |
| 1472 | excerpt | « L'idée d'une blague de quelqu'un » | "Somebody's idea of a joke" (FP FR wording) | calque | « L'idée de quelqu'un qui veut faire une blague » |

## Regressions introduced by the first pass
| Para | Ch | French (was) | Raw | English | Fix |
|---|---|---|---|---|---|
| 547 | 9 | « Je suis allée à la bibliothèque … et j'y ai trouvé » | « J'étais allée … j'y avais trouvé » | "I had gone … and found instead" | The tense conversion flattened the pluperfect. Restored to « J'étais allée … j'y avais trouvé » (2 edits). |

## Ledger mismatches
Not re-sampled (done in the targeted pass, 20/20).

## Excerpt (Flour Play Ch1) against the policy
- The meaning now matches Inn Trouble's own English line by line. "Very nearly" = « À très peu de choses près » ✓. The snowmen question is not inverted ✓. *chocolat-pécan* ✓. FP-only details follow IT's English: weekend, Sunday, war memorial ✓. The paragraph count matches ✓.
- The wording still differs a lot from corrected FP FR Ch1 (similarity about 0.55–0.8 per paragraph), even where the two English texts are identical. It is the same meaning in different words. I applied FP's wording only where the IT French was wrong or a calque ([1394], [1466], [1472]). I did not rewrite the remaining ~45 paragraphs, because a rewrite would be a re-translation, not a one-answer fix. Policy PC-FIL2-1 already covers this, so it is not re-raised. If Lisa wants word-for-word parity, she could paste the FP FR Ch1 paragraphs into the matching places and keep IT's own English deltas (weekend, Sunday, war memorial).

## Open decisions re-checked
IT2-FR-26-1 (mot/note style), IT2-FR-26-2 (added italics) and IT2-FR-26-3 (formatter) are unchanged, and their quotes are still accurate. PC-FR2-1 (centime) and PC-FR2-2 are unchanged. Ruling 4 « cinquante kilomètres » ([185]) is left as ruled.

## Decisions added (PROOFCHECK_DECISIONS.md)
- PC-FR2F-1: generic masculine for the unknown writer or courier before the reveal (informational; recommend leaving it).

## Checks after the fixes
- looks_english: [] (empty)
- bt_anchors check: 8 spans, 0 unpaired; the spans are Inn Trouble, Frost and Found and Flour Play
- check_matter --file: 1 PASS 0 FAIL
- preflight --verify: "source or corrected copy missing" (the raw is in `_superseded/`). I compared by hand against the `.full` backup instead: paragraphs 1491 → 1491 · runs 991 → 991 · italic runs 26 → 26, same sequence · `<bt>` 8 → 8 · scene breaks 3 → 3 · 59 paragraphs changed, and they are exactly the ones listed above.
- proofcheck.py re-run: A–G, I, J = 0; H = 20 (all false positives, unchanged)

## Verdict
**SIGNIFICANT.** The full read found defects that change who did what or reverse a meaning, all missed by both earlier passes:
- [823] makes Jessica's fairness rule say the opposite.
- [671] states Theo's guilt as a fact while it is still only a suspicion.
- [472] reverses "wear a feeling".
- [1466] lets the excerpt's snowman clue read as a full 360° turn.
- [177] has a feminine participle that can hint at the writer's sex.
- [1160] drops "cream" from the paper evidence in the confrontation.

The rest are minor: term drift (brackets, boxes, deed, records, copper box), calques and register.
**Rate:** 64 edits in 59 paragraphs across 34 units read (31 chapters + front + blurb + back) ≈ 1.9 per unit.
