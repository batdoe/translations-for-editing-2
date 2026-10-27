#!/usr/bin/env python3
"""check_matter.py — structural front/back-matter gate for translated editions.

HOUSE RULE (Lisa, 2026-08-11): every translated edition must have LOCALIZED back
matter. This is a STRUCTURAL check, not a proofread: it asks "is the back matter
present, and is it in the target language?" — never "is the prose any good?"

WHY A SEPARATE GATE FROM PROOFREAD
The two biggest untranslated-English runs in the corpus (Snapshot_French 279w,
Power Play_Italian 239w) were NOT prose defects — they were the blurb / also-by
sections left in English at position >92% of the book. That is a formatter
localization miss with a deterministic fix. Paying a model to re-read a whole
book to find it is the wrong tool. This finds it for free.

WHAT IT CHECKS, per deliverable
  1. PRESENT   — is there any back matter after the last story paragraph?
  2. LOCALIZED — is that back matter in the target language, not English?
  3. FRONT     — is the title/copyright page localized?

The three failures are reported separately because they have different fixes:
missing back matter = the formatter never built it; English back matter = it was
built from the English source and never translated.

DETECTION
Back matter is identified by localized section markers (about-the-author, also-by,
and the vendor/series-page headings the formatter emits) in the tail of the book,
per language. A book whose tail holds only story prose has NO back matter.

Language of the tail reuses claude_translate.looks_english() so the "is it still
English" verdict matches langcheck exactly rather than being a second opinion.

USAGE
  python check_matter.py                       # scan translated + 2buploaded
  python check_matter.py --dir translated
  python check_matter.py --xlsx                # write Matter_Check_<date>.xlsx
  python check_matter.py --file "<path.docx>"
"""

from __future__ import annotations

import argparse
import collections
import sys
import unicodedata
from datetime import date
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from claude_translate import paras, looks_english, lang_of, CHAP_WORDS

ROOT = Path(os.environ.get("SCRIPTS_ROOT") or r"C:\Users\User\Scripts")  # cloud: export SCRIPTS_ROOT=<repo root>

# Localized markers for the sections the formatter emits as back matter.
# Deliberately generous: a false "present" is safer here than a false "missing",
# because a missing-back-matter report sends Lisa to look at the file anyway.
BACK_MARKERS = {
    "English":  ["about the author", "also by", "other books", "books in this series",
                 "coming soon", "join", "newsletter", "read more", "up next", "click here", "get", "today", "thank you for reading"],
    "German":   ["über die autorin", "über den autor", "weitere bücher", "mehr von",
                 "in dieser reihe", "demnächst", "newsletter", "leseprobe", "klicken sie", "holen sie sich", "hol dir", "hol dir", "noch heute", "danke, dass sie"],
    "French":   ["à propos de l'auteur", "à propos de l’auteur", "de la même autrice",
                 "du même auteur", "autres livres", "dans cette série", "à paraître",
                 "newsletter", "bientôt", "cliquez ici", "procurez-vous", "obtenez", "procurez-vous", "dès aujourd’hui", "merci d'avoir lu", "merci d’avoir lu"],
    "Italian":  ["sull'autrice", "sull’autrice", "sull'autore", "sull’autore",
                 "altri libri", "della stessa autrice", "in questa serie",
                 "prossimamente", "newsletter", "clicca qui", "acquista", "acquistate",
                 # "prendi" — the imperative the KB_H1 Italian buy-lines actually use
                 # ("Prendi Il denaro non può comprare oggi!"). Its absence falsely
                 # blocked a fully localized edition as NO BACK MATTER.
                 "prendi", "scarica", "prendi", "oggi stesso", "grazie per aver letto"],
    "Spanish":  ["sobre la autora", "sobre el autor", "otros libros",
                 "de la misma autora", "en esta serie", "próximamente", "boletín", "haga clic", "consigue", "hazte con", "consigue", "hoy mismo", "gracias por leer"],
    "Brazilian Portuguese": ["sobre a autora", "sobre o autor", "outros livros",
                             "da mesma autora", "nesta série", "em breve", "clique aqui", "garanta", "adquira", "garanta", "hoje mesmo", "obrigada por ler"],
    "Romanian": ["despre autoare", "despre autor", "alte cărți", "în această serie",
                 "în curând", "buletin", "apăsați aici", "obține", "procură", "astăzi", "mulțumesc că"],
    "Dutch":    ["over de auteur", "over de schrijfster", "andere boeken",
                 "meer van", "in deze serie", "binnenkort", "nieuwsbrief", "klik hier", "haal ", "vandaag nog", "bedankt voor het lezen"],
    "Norwegian": ["om forfatteren", "andre bøker", "mer av", "i denne serien",
                  "kommer snart", "nyhetsbrev", "klikk her", "hent ", "skaff deg", "i dag", "takk for at du leste"],
    "Swedish":  ["om författaren", "andra böcker", "mer av", "i denna serie",
                 "kommer snart", "nyhetsbrev", "klicka här", "skaffa", "hämta", "skaffa", "idag", "tack för att du läste"],
    "Danish":   ["om forfatteren", "andre bøger", "mere af", "i denne serie",
                 "udkommer snart", "nyhedsbrev", "klik her"],
    "Polish":   ["o autorce", "o autorze", "inne książki", "w tej serii",
                 "wkrótce", "newsletter", "pozostałe książki", "kliknij", "zdobądź", "kup ", "zdobądź", "już dziś", "dziękuję, że"],
    "Czech":    ["o autorce", "o autorovi", "další knihy", "v této sérii",
                 "již brzy", "newsletter", "klikněte", "pořiďte", "získejte", "získejte", "ještě dnes", "děkuji, že jste"],
    "Greek":    ["σχετικά με τη συγγραφέα", "για τη συγγραφέα", "άλλα βιβλία",
                 "σε αυτή τη σειρά", "προσεχώς", "πατήστε", "αποκτήστε", "πάρτε",
                 # the house shape's own headings + the finale close (2026-08-26)
                 "τι ακολουθεί", "απόσπασμα από", "σχετικά με αυτό το βιβλίο",
                 "ευχαριστώ που διαβάσατε", "η σειρά", "αποκτήστε το", "σήμερα"],
    "Turkish":  ["yazar hakkında", "diğer kitaplar", "bu seride", "yakında",
                 "bülten", "tıklayın", "edinin", "kitabını bugün edinin", "okuduğunuz için teşekkür"],
    # ⚑ The list below predated the Filipino house shape and named none of the
    # phrases the formatter actually emits, so six fully-built Isabella Proctor
    # editions gated as NO BACK MATTER while three passed by luck on "sa seryeng
    # ito". Same failure as the Italian "prendi" note above. (2026-08-26.)
    "Filipino": ["tungkol sa may-akda", "iba pang libro", "sa seryeng ito",
                 "malapit na", "iba pang aklat", "i-click",
                 "ano ang susunod", "sipi mula sa", "kunin ang",
                 "tungkol sa aklat", "salamat sa pagbabasa", "bisitahin ang", "kunin ang", "ngayon"],
    "Tagalog":  ["tungkol sa may-akda", "iba pang libro", "sa seryeng ito",
                 "malapit na", "i-click",
                 "ano ang susunod", "sipi mula sa", "kunin ang",
                 "tungkol sa aklat", "salamat sa pagbabasa", "bisitahin ang"],
}

# The formatter's most common back-matter element is not an "About the author"
# heading at all — it is a one-line localized series-continuation teaser, e.g.
#   Dutch:   "Het verhaal van Fiora en Ciro gaat verder in Het Partnerschap"
#   Turkish: "Fiora ve Ciro'nun hikâyesi Ortaklık ile devam ediyor."
#   Greek:   "Η ιστορία της Φιόρα και του Τσίρο συνεχίζεται στο βιβλίο ..."
# A first version of this check missed every one of them and reported 50/51 books
# broken. These verbs/nouns are what those lines actually key on, per language.
CONTINUES = {
    "English":  ["story continues", "continues in", "available now", "up next"],
    "German":   ["geht weiter", "fortsetzung", "jetzt erhältlich", "fortgesetzt", "geht in", "wird fortgesetzt"],
    "French":   ["se poursuit", "l'histoire de", "l’histoire de", "disponible", "l'histoire continue", "l’histoire continue", "s'achève", "s’achève"],
    "Italian":  ["continua in", "la storia di", "disponibile", "prosegue", "si conclude", "inizia i misteri"],
    "Spanish":  ["continúa en", "la historia de", "ya disponible", "concluye"],
    "Brazilian Portuguese": ["continua em", "a história de", "já disponível", "conclui"],
    "Romanian": ["continuă în", "povestea", "se încheie în", "disponibil"],
    "Dutch":    ["gaat verder in", "het verhaal van", "nu verkrijgbaar", "wordt vervolgd", "wordt afgesloten"],
    "Norwegian": ["fortsetter i", "historien om", "avsluttes i", "tilgjengelig"],
    "Swedish":  ["fortsätter i", "berättelsen om", "tillgänglig", "avslutas"],
    "Danish":   ["fortsætter i", "historien om", "tilgængelig"],
    "Polish":   ["toczy się dalej", "historia", "dostępna", "kończy się", "ciąg dalszy"],
    "Czech":    ["pokračuje v", "příběh", "dostupné", "pokračování", "završuje"],
    "Greek":    ["συνεχίζεται", "η ιστορία", "διαθέσιμο", "ολοκληρώνεται"],
    "Turkish":  ["devam ediyor", "hikâyesi", "hikayesi", "mevcut", "sona eriyor"],
    "Filipino": ["nagpapatuloy ang kuwento", "ang kuwento nina", "available na", "nagtatapos"],
    "Tagalog":  ["nagpapatuloy ang kuwento", "ang kuwento nina", "nagtatapos"],
}

# ⚑ 2026-09-07: was 30, which predates the full back-matter block. That block now
# ends with the next book's SAMPLE CHAPTER (Lisa's spec, MATTER_SPEC.md), so the
# "series continues"/"What's Next?" markers sit 58-157 paragraphs above the end —
# far outside a 30-paragraph window. Five correctly-built Isabella Norwegian
# editions gated as NO BACK MATTER while four passed only because their excerpt
# happened to be short. The checker table lagged the format; the books were right.
# 400 comfortably clears the longest sample chapter (~200 paras) with headroom.
TAIL_PARAS = 400         # how far back to look for back matter
HEAD_PARAS = 12          # front matter window
SCENE_TOKENS = {"* * *", "***", "* * * *"}


def find_back_matter(body: list[str], lang: str) -> tuple[int | None, str]:
    """-> (index where back matter starts, which marker matched)."""
    tail_start = max(0, len(body) - TAIL_PARAS)
    own = [m.lower() for m in BACK_MARKERS.get(lang, [])]
    cont = [m.lower() for m in CONTINUES.get(lang, [])]
    eng = [m.lower() for m in BACK_MARKERS["English"]]
    eng_cont = [m.lower() for m in CONTINUES["English"]]
    for i in range(tail_start, len(body)):
        low = body[i].lower()
        for m in own:
            if m in low:
                return i, f"localized section: {m!r}"
        for m in cont:
            if m in low:
                return i, f"localized teaser: {m!r}"
        # Only call it English back matter if the marker is English AND the
        # paragraph is not simply a localized line that happens to share a word.
        for m in eng + eng_cont:
            if m in low and looks_english(body[i], min_words=6):
                return i, f"ENGLISH: {m!r}"
    return None, ""


# The three FRONT-matter blocks the formatter builds from the Book Catalogue.
# Added 2026-08-11: the first live proofread found a Norwegian edition whose front
# matter was missing its catalogue pages entirely, and this checker PASSED it —
# because it only asked "is the front matter English?", never "is it THERE?".
SERIES_PAGE = {
    "English": ["books in this series"],
    "German": ["bücher in dieser reihe", "in dieser reihe", "bücher dieser reihe"],
    "French": ["livres de cette série", "dans cette série"],
    "Italian": ["libri di questa serie", "in questa serie"],
    "Spanish": ["libros de esta serie", "en esta serie"],
    "Brazilian Portuguese": ["livros desta série", "nesta série"],
    "Romanian": ["cărți din această serie", "în această serie"],
    "Dutch": ["boeken in deze serie", "in deze serie"],
    "Norwegian": ["bøker i denne serien", "i denne serien"],
    "Swedish": ["böcker i denna serie", "i denna serie", "böcker i den här serien"],
    "Danish": ["bøger i denne serie", "i denne serie"],
    "Polish": ["książki z tej serii", "w tej serii"],
    "Czech": ["knihy z této série", "v této sérii"],
    "Greek": ["βιβλία αυτής της σειράς", "σε αυτή τη σειρά"],
    "Turkish": ["bu serideki kitaplar", "bu seride"],
    "Filipino": ["mga libro sa seryeng ito", "sa seryeng ito", "mga aklat sa seryeng ito"],
    "Tagalog": ["mga libro sa seryeng ito", "sa seryeng ito"],
}
OTHER_BOOKS = {
    "English": ["other books by"],
    "German": ["weitere bücher von", "andere bücher von"],
    "French": ["autres livres de", "du même auteur", "de la même autrice"],
    "Italian": ["altri libri di"],
    "Spanish": ["otros libros de"],
    "Brazilian Portuguese": ["outros livros de"],
    "Romanian": ["alte cărți de"],
    "Dutch": ["andere boeken van"],
    "Norwegian": ["andre bøker av"],
    "Swedish": ["andra böcker av"],
    "Danish": ["andre bøger af"],
    "Polish": ["inne książki", "pozostałe książki"],
    "Czech": ["další knihy", "další knihy od"],
    "Greek": ["άλλα βιβλία", "άλλα βιβλία της"],
    "Turkish": ["diğer kitaplar", "imzalı diğer kitaplar"],
    "Filipino": ["iba pang libro", "iba pang aklat ni"],
    "Tagalog": ["iba pang libro"],
}
TOC_HEAD = {
    "English": ["table of contents", "contents"],
    "German": ["inhaltsverzeichnis", "inhalt"],
    "French": ["table des matières", "sommaire"],
    "Italian": ["indice"],
    "Spanish": ["índice", "tabla de contenido"],
    "Brazilian Portuguese": ["sumário", "índice"],
    "Romanian": ["cuprins"],
    "Dutch": ["inhoudsopgave", "inhoud"],
    "Norwegian": ["innholdsfortegnelse", "innhold"],
    "Swedish": ["innehållsförteckning", "innehåll"],
    "Danish": ["indholdsfortegnelse", "indhold"],
    "Polish": ["spis treści"],
    "Czech": ["obsah"],
    "Greek": ["πίνακας περιεχομένων", "περιεχόμενα"],
    "Turkish": ["içindekiler"],
    "Filipino": ["talaan ng nilalaman", "nilalaman"],
    "Tagalog": ["talaan ng nilalaman", "nilalaman"],
}

# How far into the book the front matter can reasonably run. The catalogue pages
# plus a full chapter TOC push this well past a dozen paragraphs.
FRONT_WINDOW = 90
MIN_TOC_CHAPTERS = 5


def _fold(s: str) -> str:
    """Lowercase for comparison, surviving Turkish dotted-I.

    Python lowercases 'İ' (U+0130) to 'i' + U+0307 COMBINING DOT ABOVE, so
    'İçindekiler'.lower() != 'içindekiler' and every Turkish marker silently
    missed — which read as three missing pages in a book that had all of them.
    Strip combining marks so the comparison is about letters, not accents.
    """
    return "".join(c for c in unicodedata.normalize("NFD", s.lower())
                   if not unicodedata.combining(c))


def _first_hit(body: list[str], needles: list[str], limit: int) -> int | None:
    for i, t in enumerate(body[:limit]):
        low = _fold(t).strip()
        for n in needles:
            # `in`, not startswith: several languages prefix the author name
            # ("Meg Shannon imzalı diğer kitaplar"), so the marker sits mid-line.
            if _fold(n) in low:
                return i
    return None


def check_catalogue_pages(body: list[str], lang: str) -> dict:
    """Are the catalogue front-matter pages PRESENT and localized?

    Checks presence, not correctness — whether the catalogue's own local titles are
    filled in is a Book Catalogue question (promote/gap tooling), not a docx one.
    """
    sp = _first_hit(body, [m.lower() for m in SERIES_PAGE.get(lang, [])], FRONT_WINDOW)
    ob = _first_hit(body, [m.lower() for m in OTHER_BOOKS.get(lang, [])], FRONT_WINDOW)
    tc = _first_hit(body, [m.lower() for m in TOC_HEAD.get(lang, [])], FRONT_WINDOW)

    # Count chapter lines after the TOC heading: a one-entry TOC means the chapter
    # list was never built (seen live — a TOC holding only "About this Book").
    chap_word = CHAP_WORDS.get(lang, "Chapter").lower()
    n_chaps = 0
    if tc is not None:
        for t in body[tc + 1:min(tc + 1 + 250, len(body))]:
            low = t.lower().strip()
            if low.startswith(chap_word):
                n_chaps += 1
            elif n_chaps and not low:
                break

    problems = []
    if sp is None:
        problems.append("NO SERIES PAGE")
    # ⚑ Lisa's ruling 2026-08-26: the "Other books by <author>" page is NO LONGER part of
    # the house back matter. The book now ends on a single call to action — the
    # "What's Next?" blurb for the next book plus its Chapter 1 excerpt — and a catalogue
    # of every other series competed with that. format_book.py stopped emitting the page
    # on the same date; this check was still demanding it, which blocked promotion of a
    # correctly-built book. Its absence is now expected, not a defect.
    #   (Presence is still reported in the returned dict, so a caller can inspect it.)
    if tc is None:
        problems.append("NO TOC")
    elif n_chaps < MIN_TOC_CHAPTERS:
        problems.append(f"TOC HAS NO CHAPTER LIST ({n_chaps})")

    return {"series_page": sp, "otherbooks_page": ob, "toc": tc,
            "toc_chapters": n_chaps, "problems": problems}


def check(path: Path) -> dict:
    lang = lang_of(path)
    try:
        body = [t for t in paras(path) if t.strip()]
    except Exception as exc:
        return {"path": path, "lang": lang, "error": str(exc)}

    idx, marker = find_back_matter(body, lang)
    tail = body[idx:] if idx is not None else body[-8:]
    tail_txt = " ".join(tail)

    # Is the tail still English? Reuse the shipped detector on the joined tail so
    # a short English blurb split over several paragraphs is still caught.
    tail_english = looks_english(tail_txt, min_words=12)

    head_txt = " ".join(body[:HEAD_PARAS])
    front_english = looks_english(head_txt, min_words=12)

    cat = check_catalogue_pages(body, lang)

    problems = []
    if idx is None:
        problems.append("NO BACK MATTER")
    elif marker.startswith("ENGLISH") or tail_english:
        problems.append("BACK MATTER NOT LOCALIZED")
    if front_english:
        problems.append("FRONT MATTER NOT LOCALIZED")
    problems += cat["problems"]

    return {
        "path": path, "lang": lang, "paras": len(body),
        "back_at": idx, "back_pct": round(100.0 * idx / len(body), 1) if idx else None,
        "marker": marker, "tail_english": tail_english,
        "front_english": front_english,
        "series_page": cat["series_page"], "otherbooks_page": cat["otherbooks_page"],
        "toc": cat["toc"], "toc_chapters": cat["toc_chapters"],
        "problems": problems, "ok": not problems,
    }


def targets(args) -> list[Path]:
    if args.file:
        return [Path(args.file)]
    dirs = [ROOT / d for d in (args.dir.split(",") if args.dir
                               else ["translated", "2buploaded", "proofread"])]
    out = []
    for d in dirs:
        if not d.exists():
            continue
        for p in sorted(d.glob("* - FORMATTED.docx")):
            if p.name.startswith("~$") or lang_of(p) is None:
                continue
            out.append(p)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="", help="comma list under Scripts\\")
    ap.add_argument("--file")
    ap.add_argument("--xlsx", action="store_true")
    ap.add_argument("--show", type=int, default=25)
    args = ap.parse_args()

    files = targets(args)
    print(f"checking {len(files)} deliverable(s) ...\n")
    rows, errs = [], []
    for p in files:
        r = check(p)
        (errs if "error" in r else rows).append(r)

    bad = [r for r in rows if not r["ok"]]
    good = [r for r in rows if r["ok"]]

    tally = collections.Counter(pr for r in bad for pr in r["problems"])
    print(f"{len(good)} PASS   {len(bad)} FAIL   {len(errs)} unreadable\n")
    for why, n in tally.most_common():
        print(f"   {n:>4}  {why}")

    if bad:
        print(f"\nfailures (first {args.show}):")
        for r in bad[:args.show]:
            print(f"   {'; '.join(r['problems']):<46} [{r['lang']}] "
                  f"{r['path'].name[:56]}")
        if len(bad) > args.show:
            print(f"   ... +{len(bad)-args.show} more")

    if args.xlsx:
        import openpyxl
        from openpyxl.styles import Font, PatternFill
        from openpyxl.utils import get_column_letter
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Matter Check"
        hdr = PatternFill("solid", fgColor="1F3864")
        hf = Font(bold=True, color="FFFFFF")
        BADF = PatternFill("solid", fgColor="FFC7CE")
        OKF = PatternFill("solid", fgColor="C6EFCE")
        cols = ["File", "Language", "Status", "Problems", "Back matter at para",
                "Back matter at %", "Marker matched", "Tail still English?",
                "Front still English?", "Series page", "Other-books page",
                "TOC", "TOC chapters", "Total paras", "Folder"]
        for c, h in enumerate(cols, 1):
            cell = ws.cell(1, c, h)
            cell.fill, cell.font = hdr, hf
        for i, r in enumerate(bad + good, start=2):
            vals = [r["path"].name, r["lang"],
                    "PASS" if r["ok"] else "FAIL", "; ".join(r["problems"]),
                    r["back_at"] if r["back_at"] is not None else "none",
                    r["back_pct"] if r["back_pct"] is not None else "",
                    r["marker"], "yes" if r["tail_english"] else "no",
                    "yes" if r["front_english"] else "no",
                    "yes" if r.get("series_page") is not None else "MISSING",
                    "yes" if r.get("otherbooks_page") is not None else "MISSING",
                    "yes" if r.get("toc") is not None else "MISSING",
                    r.get("toc_chapters", 0),
                    r["paras"], r["path"].parent.name]
            for c, v in enumerate(vals, 1):
                ws.cell(i, c, v)
            ws.cell(i, 3).fill = OKF if r["ok"] else BADF
        ws.freeze_panes = "A2"
        ws.auto_filter.ref = f"A1:O{max(2, len(rows)+1)}"
        for c, w in enumerate([62, 14, 9, 46, 18, 16, 30, 18, 20, 13, 17, 9, 13, 12, 14], 1):
            ws.column_dimensions[get_column_letter(c)].width = w
        out = ROOT / f"Matter_Check_{date.today()}.xlsx"
        wb.save(out)
        print(f"\nwrote {out}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
