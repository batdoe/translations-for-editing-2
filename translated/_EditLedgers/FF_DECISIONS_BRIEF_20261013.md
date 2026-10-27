# Brief: resolve the Frost Falls translation decisions (Lisa's rulings 2026-10-13)

You handle ONE language, BOTH books: `C:\Users\User\Scripts\translated\corrected\Frost and Found - ASSEMBLED - FORMATTED_<Lang>.docx`
and `...\Inn Trouble - ASSEMBLED - FORMATTED_<Lang>.docx`. Back each up to `corrected\_bak\<stem>.pre-decisions-20261013.docx` first.
English sources: `C:\Users\User\Scripts\translate_now\<Book> - ASSEMBLED - FORMATTED.docx`.
Your open decisions: `C:\Users\User\Scripts\translated\_EditLedgers\PROOFREAD_DECISIONS.md`, sections FF1-<XX> and IT2-<XX>
(FR/IT/DE/ES). Also read the dossier `C:\Users\User\OneDrive\Documents\Claude\Projects\Multi-Book Translations\_kit\dossiers\<language>.txt`.
Edit only these two files. Do NOT use the Agent/Task tool. Edit at the run level (never collapse a paragraph's runs; keep italics).
Useful existing tools in `translated\_tools\`: `normalise_dialogue.py`, `strip_spurious_bt.py`, `preflight.py --verify`, and
`C:\Users\User\Scripts\bt_anchors.py check`. Read a tool before trusting it; if it doesn't fit, do the edit yourself.

## Lisa's rulings
1. **DIALOGUE PUNCTUATION: one system per language, identical in both books** (Lisa: "each language internally consistent with
   itself"). Convert every dialogue paragraph, including attribution punctuation (the systems place the speech verb
   differently — rebuild the incise correctly, don't just swap the opening mark):
   - **French: guillemets per turn** « … » with the attribution inside per French convention (« Bonjour, dit-elle. »), NBSP after «
     and before », NBSP before ; : ! ?, typographic apostrophe ’ throughout, single-glyph … . Inline quoted speech in narration
     also « ». No em-dash turns.
   - **Italian: caporali** «…» per the dossier (attribution outside, lowercase verb; mid-line: «Aspetta» disse lei, «devo pensare.»).
     Convert the em-dash chapters (FF1 Ch7, IT2 Ch3, any others).
   - **German: »…«** (nested ›…‹), per the dossier. Should already be uniform — verify and fix stragglers.
   - **Spanish: raya** —, per the dossier (no space after the opening raya; incises —dijo ella—; inline quotes « »). Verify and fix stragglers.
2. **Formal/informal "you": decide and make consistent across BOTH books**, using what the relationships are in the English:
   Jessica and the circle women (Olivia, Dot, Claire, Ivy, Martha, Ellie) are close friends → informal. Jessica and Nick → informal.
   Bram (elf foreman, centuries with the Clauses) ↔ Jessica → informal both ways (German Book 1 already du). Children (Emma) are
   addressed informally and address adults formally unless the English shows otherwise. Shopkeepers/acquaintances Jessica has just
   met (Theo at first, Vera, Neil, Sam, Jamal, Pete, Hal, Doc, Mayor) → formal, unless the text has them become friends (then switch at
   a clear moment, once). Chief Noriko Tanaka ↔ Jessica: formal at first meeting (Inn Trouble Ch6), first names/informal from the
   point the English has them on first names (Inn Trouble Ch24–26: "Noriko" / "Jessica"). Professional scenes (Noriko with Theo and
   Vera) stay formal. Whatever you choose, apply it in BOTH books, verb endings/clitics/possessives included (Spanish: vosotros for
   informal plural). Log the address table you used.
3. **English sign/label text: translate it** (e.g. THE WOOLLY HOUR, EMBRACE THE SEASON, CENTENNIAL, TIME CAPSULE, PROPERTY, drawer
   labels, the Ch19 "B" archive index — keep the alphabetical joke working with target-language words starting with the same letter
   if possible, otherwise translate plainly). Keep the italics on the translated text.
4. **"Fifty miles"**: leave as is (Lisa: fine). Mark resolved.
5. **Stray `<bt>` title markers** around things that are NOT book titles (Yarn Tales, Gazette, Winter Wonderland Inn, "twenty-nine",
   TIME CAPSULE, the 2124 flyer line, etc.): remove the markers, keep (and translate where needed) the text. Real book-title anchors
   (Frost and Found / Inn Trouble / Flour Play in front/back matter and sell lines) STAY. `bt_anchors.py check` must show 0 unpaired.
6. **Cider must be NON-alcoholic** (it's served to children at the festival and the cocoa stands): German "Apfelwein" → heißer Apfelsaft /
   Apfelpunsch (alkoholfrei); Spanish already "zumo de manzana (caliente)" — confirm. French/Italian: if the text uses "cidre"/"sidro"
   (alcoholic in France/Italy), change to a non-alcoholic hot apple drink too (jus de pomme chaud / succo di mela caldo) and log it.
7. **Everything else in your FF1-XX / IT2-XX decision entries** that is a straightforward consistency fix (term variants such as
   festival/fiesta, city/town, gate/cottage words; surname plurals; copyright "by/de" matching between the two books; title-page
   series line; the duplicated "green… park" sentence — rephrase so the same word doesn't sit twice awkwardly): fix it.
   **Leave alone (formatter's job):** chapter headings, TOC, front-matter order, `* * *` back-matter separators, missing chapter
   heading lines, Heading styles. Just confirm them in your log.
8. Mark each decision you resolved as `RESOLVED 2026-10-13: <what you did>` in PROOFREAD_DECISIONS.md (back it up first as
   `PROOFREAD_DECISIONS.md.bak-<lang>-decisions-20261013`; APPEND/EDIT only your own sections — other agents edit theirs in parallel,
   so re-read the file immediately before each write and change only your lines).

## Verify
Run `preflight.py --verify "<stem>"` on both files (expect paragraph counts unchanged; italic changes only where you translated
italic text) and `bt_anchors.py check`. Log every change category with counts to `_EditLedgers\<stem>_DECISIONS_APPLIED.md`.
Return: per book — dialogue paragraphs converted, address-table summary, signs translated, bt markers removed, cider changes,
verify result, anything left for Lisa.
