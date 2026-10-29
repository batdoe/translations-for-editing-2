# PROOFCHECK (FULL) — Flour Play - ASSEMBLED - FORMATTED_Romanian (2026-10-29)

- **Mode:** FULL. A sentence-by-sentence bilingual read (EN paragraphs beside the RO paragraphs, in order) of the front matter and blurb, **Ch1–Ch27 (all 27 chapters)**, the sell lines, the What's Next blurb, and the frame and closing CTA of the excerpt. The *Binder's Bequest* excerpt is the published Romanian text (FP-RO-5): it was skimmed, not edited.
- **Edition:** `translated/corrected/Flour Play - ASSEMBLED - FORMATTED_Romanian.docx`, edited in place. Backup: `translated/_EditLedgers/_proofcheck_backups/Flour Play - ASSEMBLED - FORMATTED_Romanian.20261029-003001.full.docx`.
- **Targeted report kept:** `…_Romanian_PROOFCHECK.md` (2026-10-28, 55 edits) was not overwritten. The step 2 diff audit and the 20-row ledger sample were skipped, since the targeted pass did them. The 62 edits made here were each checked against the raw `_superseded` copy to tell a first-pass regression from an older miss.
- **Paragraph grid:** the python-docx grid of 2,499 paragraphs, empty ones included.
- **Flags (step 1):** a fresh run gives A0 B2 E0 H1 I1 J1. The targeted report already judged every one of them: B Bûches/Noël = false positive, H „o milă” = false positive, I [847] = the intended inline quote, J [1691] = correct. No new flags to judge. The re-run after the fixes is unchanged.

## Summary
- **62 one-answer fixes in 58 paragraphs**, 0 refusals. **59 were misses** (the defect was already in the raw MT and survived both passes). **3 were first-pass regressions**: [557], [2321], [2436].
- **Rate:** 62 defects over 27 chapters plus front and back matter, about **2.2 per chapter**. The chapters the targeted pass had not read (Ch2–8, 10, 15, 16, 26) gave 31 of the 62.
- **Worst finds:**
  - Ch5 [557]: Ellie's „N-o să iasă…” (correct in the raw) had been turned into „Nu depinde de tine” ("it's not up to you"). This was a first-pass reversal.
  - Ch23 [2021]: Greta's twice-repeated "That one's mine" (= that fault is mine) was „Asta e a mea”. In the middle of the quarrel over whose pie it is, that reads as Greta claiming the pie. It now reads „vina mea”.
  - Ch23 [2036]: Tanaka's "What I have is…" was „Tot ce am” ("all I have is…"), which plays down the evidence.
  - Ch23 [2016]: "buy you out" was rendered as „să te cumpăr” (buy *you*).
  - Ch7 [684]/[698]: Pete slipped into „tu” twice, although the address table makes him formal both ways.
  - Ch9 [827]/[832]: the clue "hand-sink" had become a plain „chiuveta”.
  - Ch27 [2321]/[2325]/[2383]: the wreath circle's standing order (baked goods) had become „comanda de coronițe”, an order of wreaths placed at a bakery.
- **Spoiler-gender check (Ch7, 9, 11, 12, 13, 17, 19, 22, before the Ch20 reveal):**
  - Every reference to the saboteur / complainant / "whoever" is neutral: *cineva*, *oricine*, *cine a făcut-o*, *silueta*, *mâna care…*, plural *au umblat*, *știau*.
  - The shape at Greta's door (Ch13 [1083]/[1087]: „Un om în toată firea… acoperit… Fără grabă în el… având grijă să nu fie văzut”, „siluetă de muncitor”) and Danny's figure (Ch17 [1461] „Un adult… L-am pierdut din vedere”) take Romanian's default masculine-generic agreement.
  - This is not a giveaway: it is the language's neutral default, it points *away* from Joyce, and the English itself uses generic "he/himself" in Ch12 [994]. Logged as PC-FP-RO-F2 in case Lisa wants it rephrased around *silueta*.
  - No feminine form appears anywhere before the Ch20 reveal.
- **Lines found wrong in other languages, re-checked:**
  - Ch13 [1055]/[1065] *temperament* (= disposition) ✓
  - Ch17 [1461]/[1475]: the FIGURE goes past the pharmacy light ✓
  - Ch19 [1678]: Jessica supplies the gold shop ✓
  - Ch19 [1697]: *șpalt* ✓
  - Ch23 [2008]: *lacătul* ✓
  - Ch23 [2023]: who would have been robbed ✓
  - Ch24 [2050]: Danny's *declarația* ✓
  - Ch1 [62]: *cu jumătate mai mare* ✓
  - Ch1 [88]: bakery box = *cutie de prăjituri* ✓
  - Ch22: Tanaka's split turns read as Tanaka, and Greta's turn [1965]–[1969] stays with Greta ✓
- **Rename spill check:**
  - walk-in *camera frigorifică* and Joyce's „camera rece” are still two words (Ch20 [1778], Ch22 [1913], Ch23 [1995]–[1996]) ✓
  - *bază acră* is never *maia* (the only *maia* is Doc's "without the starter" [951]) ✓
  - *caietul de comenzi* has not spilled onto Tanaka's *carnețel* ✓
  - gate key / lock ✓
  - the bakery box ≠ *patiserie* ✓
  - Three *cofetărie* variants for the rival Sugarplum ([1315] [1521] [2054]) were unified to the book's form.
- **Term drift fixed:**
  - batch *tranșă* → *șarjă* ([180] [189])
  - wreath *coroană* → *coroniță* [297]
  - balsam rendered *balsam* (= balm) → *brad / cetină* ([1412] [1422]×2 [2288])
  - weather-strip *banda* → *garnitura* [1796]
  - gingersnaps [2160]
  - plant *uzină* → *fabrică* [1297]
  - browned butter *unt ars* (burnt) → *unt brun* [1343]
  - the capsule-card echo in Ch15 [1293] now matches the Ch6 card wording
- **Clue chain (recount):**
  - *bază acră* ×20 ✓
  - „cu două grade sub normă” identical at [809] [1388] [1392] ✓
  - „Nimic ce aș putea numi” [941] ✓
  - "ten times" [951] [953] ✓
  - Joyce 65 [2062], 25 yrs / 15 together ✓, „pe douăzeci” ✓
  - MURDAR / PERICULOS / NU MÂNCAȚI AICI ✓
  - căminul cultural ✓
  - dollars only ✓
  - no poison/toxic ✓
  - Pip: no masculine agreement found ✓
  - founder's line identical [625] [638] [2302] ✓
  - capsule card identical [1289] = [2315] ✓
  - *Binder's Bequest* anchors and the CTA [2498] ✓
- **Blurbs:** the front blurb is in the present tense ✓. What's Next is in the present tense ✓, with the great-aunt fixed.
- **Tense:** perfect compus narration holds. Three pluperfect-for-main-action slips were fixed ([1521] [2367] [2383]). The published excerpt's perfect simplu stays (FP-RO-5).
- **Address:** Pete [684] [698] and Mrs Ott [1180] slips fixed. The rest of the table holds.

## Missed by the first pass (59, all APPLIED)
| ¶ | Ch | Target (was) | English | Class | Now (applied) |
|---|---|---|---|---|---|
| 180 | 2 | „Două tranșe de rulouri” | Two batches of the rolls | term drift (batch = șarjă) | „Două șarje de rulouri” |
| 189 | 2 | „o tranșă curată” | I mixed a clean batch | term drift (batch = șarjă) | „o șarjă curată” |
| 237 | 3 | „îi purta cu mândrie” | she wore it well | mistranslation | „îi purta cu grație” |
| 269 | 3 | „Există un brutar en gros tocmai în Bridgton” | There's a wholesale bread baker over in Bridgton who wants to sell me my bread. She's very keen. | gender agreement (EN: She's very keen; RO 'un brutar … pâinea ei … entuziasmată') | „Există o brutăreasă en gros tocmai în Bridgton” |
| 281 | 3 | „a condus o casă mare în Montreal” | ran a big house in Montreal | mistranslation ('o casă mare' = a big household; = the pastry house of [261]) | „a condus o cofetărie mare la Montreal” |
| 297 | 3 | „o coroană pe ușă” | a wreath on the door | term drift (wreath = coroniță) | „o coroniță pe ușă” |
| 469 | 5 | „mușcând dintr-o bucată de sârmă cu un sunet scurt și sec” | biting off a length of wire with a small hard snap | calque ('biting off' = snipping; RO = biting into the wire) | „tăind o bucată de sârmă cu un pocnet scurt și sec” |
| 632 | 6 | „știind că în ea este închisă o sută de ani care le aparțin” | knowing there's a hundred years shut up in it that belongs to them | agreement | „știind că în ea sunt închiși o sută de ani care le aparțin” |
| 643 | 6 | „și Greta o să coacă pentru ea în ziua” | I'd bet Greta bakes for it too | agreement (pentru el = the barrel, butoiul) | „și Greta o să coacă pentru el în ziua” |
| 670 | 7 | „Și toată strada a decis a cui ușă s-o încarce.” | And the whole street's decided whose door to lay it at. | garbled idiom | „Și toată strada a decis la ușa cui s-o lase.” |
| 672 | 7 | „N-am auzit să fi dat vreo adeziune.” | I haven't heard myself agree to it. | mistranslation (lost 'myself': Jessica has not agreed) | „Nu m-am auzit însă și pe mine fiind de acord.” |
| 684 | 7 | „A mușcat din sfoară.” | He bit off the twine. | calque ('bit off the twine') | „A rupt sfoara cu dinții.” |
| 684 | 7 | „Îți scutesc osteneala” | I'll save you the trouble of finding it sinister. | address (Pete ↔ Jessica formal; one 'tu' slip) | „Vă scutesc de osteneala” |
| 698 | 7 | „Fă ce vrei cu asta.” | Do what you like with it. | address (Pete formal; 'tu' slip in the same speech) | „Faceți ce vreți cu asta.” |
| 741 | 8 | „spre prăvăliile de la marginea orașului” | out to the far-end shops | mistranslation (far-end shops of the avenue, not the edge of town) | „spre prăvăliile din capătul celălalt al bulevardului” |
| 760 | 8 | „lucrul căruia i s-a dăruit cu tot trupul” | a man touching the thing he'd given himself to | mistranslation ('given himself to' ≠ 'with his whole body') | „lucrul căruia i se dăruise cu totul” |
| 781 | 9 | „nu se îndoise nicio secundă de spiritul sezonului” | she'd never doubted the season for a minute | mistranslation (her trading season, not 'the spirit of the season') | „nu se îndoise nicio secundă de sezonul ei” |
| 827 | 9 | „codul exact privind temperatura chiuvetei, capitol” | the exact code on hand-sink temperature | clue term (hand-sink dropped; settled 'chiuveta de spălat mâini') | „codul exact privind temperatura apei la chiuveta de spălat mâini, capitol” |
| 832 | 9 | „codul exact pentru temperatura chiuvetei și” | the exact code on hand-sink temperature | clue term (hand-sink) | „codul exact pentru temperatura apei la chiuveta de spălat mâini și” |
| 879 | 10 | „înainte să-mi scap ceaiul în zăpadă” | before I drop your tea in the snow | mistranslation ('your tea' rendered 'my tea') | „înainte să vă scap ceaiul în zăpadă” |
| 903 | 10 | „Stricase trei rânduri de aluat la fel” | It had soured three doughs the same way | mistranslation ('three doughs' = three different doughs, cf. Ch2) | „Stricase trei aluaturi diferite în același fel” |
| 998 | 12 | „Deschisă în bătaia vântului cu spatele la ea,” | Open to the air with her back to it | pronoun reference (read as the door having its back to her) | „Deschisă în bătaia vântului, cu Greta întoarsă cu spatele la ea,” |
| 1095 | 13 | „N-ați doar văzut-o.” | You didn't only see it. | ungrammatical word order | „Nu v-ați mulțumit doar s-o vedeți.” |
| 1180 | 14 | „— Danny al tău n-a vopsit” | Your Danny didn't paint that wall, Mrs. Ott. | address (Mrs Ott formal per the table; 'al tău' slip beside 'doamnă Ott') | „— Danny al dumneavoastră n-a vopsit” |
| 1196 | 14 | „Mama lui o să recunoască, și la fel și ei.” | His mother will say so, and so will they. | mistranslation ('recunoască' = admit/confess) | „Mama lui o să confirme, și la fel și ei.” |
| 1293 | 15 | „Cea veche trebuia deschisă de an nou, în adunare, așa cum intenționaseră înaintașii.” | The old was to be opened at the new year, in company, as the forebears intended. | echo drift (the capsule card wording, Ch6 [631] „De deschis la noul an, în obște, așa cum au intenționat strămoșii noștri”) | „Cea veche trebuia deschisă la noul an, în obște, așa cum intenționaseră strămoșii.” |
| 1297 | 15 | „pensionat de la uzină” | retired from the plant | term drift (the plant = fabrica, Ch10) | „pensionat de la fabrică” |
| 1315 | 15 | „o cofetărie nouă și lucioasă, cu ușile luminate în aur deschise larg ca să prindă fiecare suflet din ele. Tipărită, prinsă în ace și plătită cu” | a glossy new patisserie with its gold-lit doors thrown wide to catch every soul of it. Printed and pinned and paid for a full week before | term (rival = patiserie) + agreement ('din ele'; 'Tipărită…' attached to the shop, EN = the flyer/opening) | „o patiserie nouă și lucioasă, cu ușile luminate în aur deschise larg ca să prindă fiecare suflet din el. Totul tipărit, prins în ace și plătit cu” |
| 1343 | 15 | „învelită în unt ars” | a woman wrapped in browned butter | mistranslation (browned butter, = Ch3 'unt brun'; 'ars' = burnt) | „învelită în unt brun” |
| 1366 | 16 | „fiecare ușă de magazin de pe ea,” | every shop door on it | agreement (bulevardul) | „fiecare ușă de magazin de pe el,” |
| 1412 | 16 | „— Din cetină de balsam și cu” | Balsam and a gold bow | term drift (balsam = brad/cetină de brad throughout; RO 'balsam' = balm) | „— Din cetină de brad și cu” |
| 1422 | 16 | „am adus cetina de balsam din șopron” | I brought the balsam in from the shed | term drift (balsam) | „am adus cetina de brad din șopron” |
| 1422 | 16 | „primul mănunchi de cetină de balsam de cerc” | I bound the first bunch of balsam to the hoop | term drift (balsam) | „primul mănunchi de cetină de brad de cerc” |
| 1521 | 17 | „pe treapta măturată a cofetăriei Sugarplum, unde a așteptat și în dimineața aceea,” | Pip stopped on Sugarplum's swept step, where she had waited that morning and the first day both | term (rival = patiserie, not cofetărie) + tense (pluperfect for the earlier wait) | „pe treapta măturată de la Sugarplum, unde așteptase și în dimineața aceea,” |
| 1634 | 18 | „un reșou cu kerosen care își ticăia” | a kerosene heater ticking its small orange warmth | mistranslation (reșou = cooking ring; a kerosene heater) | „o sobiță cu kerosen care își ticăia” |
| 1634 | 18 | „mica lui căldură portocalie într-un colț, împrumutat sau cumpărat,” | borrowed or bought I did not ask | agreement after the heater fix | „mica ei căldură portocalie într-un colț, împrumutată sau cumpărată,” |
| 1647 | 18 | „Nu era treaba mea să o dau și el n-o ceruse,” | It was not mine to give and he had not asked it | dangling pronoun ('o' with no antecedent after 'absolvit') | „Iertarea nu era a mea s-o dau, și el n-o ceruse,” |
| 1648 | 18 | „cu reșoul ticăind” | the heater ticking | mistranslation (heater) | „cu sobița ticăind” |
| 1694 | 19 | „Deci închiderea a fost cronometrată în funcție de deschidere.” | So the closure was timed to the opening. | calque ('timed to' ≠ stopwatch 'cronometrată') | „Deci închiderea a fost potrivită după deschidere.” |
| 1746 | 20 | „— Partea cu chiuveta tot n-a sosit,” | The sink part still hasn't come | mistranslation ('the sink part' = the spare part, cf. Varney's 'the parts for the sink') | „— Piesa pentru chiuvetă tot n-a sosit,” |
| 1796 | 20 | „unde banda de sub ușă se tocise” | where the strip under the door had worn | clue term drift (weather-strip = garnitura, settled) | „unde garnitura de sub ușă se tocise” |
| 1834 | 21 | „și n-are de gând să-l schimbe.” | and she won't have changed it | mistranslation ('she won't have changed it' = she certainly hasn't; RO = she doesn't intend to) | „și sigur nu l-a schimbat de atunci.” |
| 1899 | 22 | „iar numele Gretei avea să i se facă dreptate tot pe hârtie, unde nimeni nu putea să-l conteste peste tejghea.” | Greta's name would come back to her on paper, where nobody could argue it away over a counter | ungrammatical ('numele … avea să i se facă dreptate') | „iar Greta avea să-și primească numele înapoi tot pe hârtie, unde nimeni nu putea să-l conteste peste tejghea.” |
| 2016 | 23 | „M-ai rugat să te cumpăr.” | You asked me to buy you out. | mistranslation ('buy you out' rendered 'buy you') | „M-ai rugat să-ți cumpăr partea.” |
| 2021 | 23 | „N-am făcut-o. Asta e a mea.” | I didn't. That one's mine. | ambiguity in the pie-ownership quarrel ('Asta e a mea' reads 'this is mine'; EN 'That one's mine' = that fault is mine) | „N-am făcut-o. Asta e vina mea.” |
| 2021 | 23 | „Nu m-am gândit la tine. Și asta e a mea.” | I didn't think of you. That's mine too. | same ambiguity | „Nu m-am gândit la tine. Și asta e vina mea.” |
| 2035 | 23 | „A cântărit fiecare faptă de două ori” | She measured each fact twice | wrong word (faptă = deed; fapt = fact) | „A cântărit fiecare fapt de două ori” |
| 2036 | 23 | „Tot ce am este un registru” | What I have is a supplier's record | meaning shift ('Tot ce am' = 'all I have', belittling the evidence; EN 'What I have is') | „Ce am eu este un registru” |
| 2054 | 24 | „în containerul din spatele cofetăriei Sugarplum” | the dumpster behind Sugarplum | term (rival = patiserie; 'cofetăria' variant) | „în containerul din spatele lui Sugarplum” |
| 2072 | 24 | „Wendt deține o licență de stat” | Wendt's has a state license to sell bread wholesale | reference ('Wendt's' = the business; RO read as the woman) | „Brutăria Wendt deține o licență de stat” |
| 2156 | 25 | „la capătul celălalt al străzii Evergreen” | By the time it reached the far end of Evergreen | term (Evergreen Avenue = Bulevardul Evergreen ×10) | „la capătul celălalt al Bulevardului Evergreen” |
| 2160 | 25 | „Fursecurile cu ghimbir s-au dus” | Gingersnaps to the bottom of the jar. | term drift (gingersnaps = biscuiți cu ghimbir, Ch1/Ch9) | „Biscuiții cu ghimbir s-au dus” |
| 2269 | 26 | „Greta a îndesat ultimele chifle cu cacao în gura echipei de pe acoperiș, iar când Hal a deschis gura despre banii pe care îi dăduse, i-a îndesat o chiflă și lui.” | Greta pressed the last of the cocoa buns on the roof crew, and when Hal opened his mouth about the money she'd given, she put a bun in it. | mistranslation (she pressed buns ON the crew; only Hal gets one put in his mouth) | „Greta le-a împărțit cu de-a sila celor din echipa de pe acoperiș ultimele chifle cu cacao, iar când Hal a deschis gura despre banii pe care îi dăduse, i-a îndesat una în gură.” |
| 2288 | 26 | „din balsam uscat și boabe” | a small wreath we'd wound of dried balsam and berry | term drift (balsam = brad/cetină; RO 'balsam' = balm) | „din cetină uscată și boabe” |
| 2293 | 26 | „— Nu mai vine, i-a spus” | It doesn't fit anymore | unclear ('Nu mai vine' = it isn't coming any more) | „— Nu-mi mai vine, i-a spus” |
| 2306 | 26 | „Fiind o familie sau găsind-o” | By being family, or by finding it in a box. | mistranslation ('by being family' = being one of the family) | „Fiind din familie sau găsind-o” |
| 2325 | 27 | „Comanda de coronițe nu e împachetată.” | The wreath order's not boxed. | same (Greta boxes baked goods for the circle) | „Comanda pentru cerc nu e împachetată.” |
| 2367 | 27 | „Pip intrase de acolo de unde supraveghease zăpada prin geamul jos și se așezase la picioarele Gretei” | Pip came in from where she'd been supervising the snow … and stationed herself at Greta's feet | tense (pluperfect for a main-line action; perfect compus lock) | „Pip a venit de acolo de unde supraveghease zăpada prin geamul jos și s-a așezat la picioarele Gretei” |
| 2383 | 27 | „O lăsasem pe Pip sub scaun cu ultima bucată din sardină, să aibă grijă de ea însăși când termina, și am dus comanda de coronițe pe bulevard” | I left Pip under the chair with the last of her sardine, to see herself home when she was done, and carried the wreath order up the avenue | same + tense (pluperfect in sequence) + 'to see herself home' mistranslated as 'take care of herself' | „Am lăsat-o pe Pip sub scaun cu ultima bucată din sardină, să-și vadă singură de drum spre casă când termina, și am dus comanda cercului pe bulevard” |

## Regressions introduced by the first pass (3, all APPLIED)
| ¶ | Ch | Target (was) | English | Class | Now (applied) |
|---|---|---|---|---|---|
| 557 | 5 | „— Nu depinde de tine, și n-o s-o las eu” | "It won't be, and I won't," Ellie said | mistranslation ('It won't be [let out], and I won't' rendered 'It's not up to you') | „— N-o să iasă, iar eu n-o să-l las” |
| 2321 | 27 | „după comanda obișnuită de coronițe a cercului” | for the wreath-circle's standing order | mistranslation (the wreath circle's standing order of baked goods, not an order of wreaths from a bakery) | „după comanda obișnuită a cercului de coronițe” |
| 2436 | back | „Moștenirea unei străbunici răposate” | A dead great-aunt's bequest | mistranslation in the What's Next blurb (great-aunt ≠ great-grandmother; the published excerpt has 'mătușa bunică' [2459][2471]) | „Moștenirea unei mătuși bunice răposate” |

- [557]: the raw had „N-o să iasă, și n-am s-o fac niciunul”, which is close to right. The first pass rewrote it to „Nu depinde de tine…”.
- [2321]: the raw „comanda regulată a cercului de coroane” was right in sense. The first pass reordered it into „comanda … de coronițe a cercului”. The targeted pass then carried *coronițe* into [2325] and [2383].
- [2436]: the What's Next blurb was translated fresh by the first pass, with *străbunică* (great-grandmother) for great-aunt. The published excerpt has „mătușa bunică”.

## Ledger mismatches
Not re-sampled (done in the targeted pass: 20/20).

## Decisions added (PROOFCHECK_DECISIONS.md, section "… — FULL PROOFCHECK (2026-10-29)")
- PC-FP-RO-F1: shop-sign text is still English (HOLLY JOLLY BAKERY ×3, "Patisserie & Confiserie" ×2), against ruling 3.
- PC-FP-RO-F2: masculine-generic agreement for the pre-reveal shape/figure (Ch13, Ch17). Informational; the recommendation is to keep it.
- PC-FP-RO-1 and PC-FP-RO-2 (the dash pass and the Ch25 split turn) are still open and are not re-raised.

## Refusals
None (62 of 62).

## Checks (after the fixes)
- **looks_english:** `[]`.
- **bt_anchors check:** 10 spans, 0 unpaired. Only Flour Play / Frost and Found / Inn Trouble / The Binder's Bequest.
- **check_matter:** 1 PASS, 0 FAIL.
- **preflight --verify:** "source or corrected copy missing" (the raw is in `_superseded/`). Manual check against the backup instead:
  - paragraphs 2,499 = 2,499;
  - italic runs 43 = 43, identical and in order (no edit touched an italic run);
  - `<bt>` 10 = 10;
  - `* * *` 61 = 61;
  - 58 paragraphs changed, every one matching its expected text exactly.
- **proofcheck re-run:** A0 B2 C0 D0 E0 F0 G0 H1 I1 J1. Unchanged, all known false positives or intended.

## Verdict
**SIGNIFICANT.** No clue-chain term was broken. But reversed-meaning defects in the confrontation chapter were missed:
- Ch23 [2021] „Asta e a mea” read as Greta claiming the pie;
- [2036] „Tot ce am” plays down Tanaka's evidence;
- [2016] "buy you out".

There was also a first-pass reversal in Ch5 [557]. Rate: about 2.2 real defects per chapter read.
