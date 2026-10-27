#!/usr/bin/env python3
r"""PROOFCHECK flags — the no-model half of /proofcheck (second-pass audit).

Scope: Frost Falls Book 2 (Inn Trouble) and Book 3 (Flour Play) ONLY, every language.
Reads the CORRECTED edition, the raw input it came from, and the English, and writes a
flag list for the recheck agent to judge. Every flag is a HINT, not a defect: the agent
confirms each one against the English before touching anything. This script never
edits a manuscript.

What it flags (per edition):
  A  English left in the text (long paragraphs AND short runs of 4+ English words)
  B  Letters from another alphabet / language (Cyrillic, Vietnamese, Hebrew, Arabic,
     CJK, zero-width chars, mixed-script words, accented letters foreign to the language)
  C  MT debris: translator notes, brackets, Markdown, stray tags, "Correction:", etc.
  D  MT loops (a word or short phrase repeated 3+ times in a row)
  E  Chapter length vs English (big gap = omission or duplication)
  F  Numbers in a chapter that the English chapter doesn't have (age/year/price drift)
  G  Names: English chapter names a character, the translation's chapter never does
  H  Watch-words: imperial units, foreign currency, alcoholic cider, poison words
  I  Dialogue system: mixed quote/dash systems, unbalanced quote marks
  J  The FIRST PASS's own edits: paragraphs it emptied or cut by more than half
  K  Book-specific clue chain: per-chapter counts of the English clue terms, so the
     agent can trace each one through the translation
  L  The four standard checks (looks_english, bt_anchors, check_matter, preflight --verify)
  M  Change density per chapter (where the first pass touched least = read first)

USAGE  (from the Scripts root / repo root)
    python translated\_tools\proofcheck.py --book "Inn Trouble" --langs Polish,Greek
    python translated\_tools\proofcheck.py --book "Flour Play"            # all languages
    python translated\_tools\proofcheck.py --all                          # both books
Output: translated\_EditLedgers\<stem>_PROOFCHECK_FLAGS.md + one summary line each.
"""
import argparse
import io as _io
import os
import re
import statistics
import subprocess
import sys
import unicodedata
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

if hasattr(sys.stdout, "buffer"):
    sys.stdout = _io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = Path(os.environ.get("SCRIPTS_ROOT") or r"C:\Users\User\Scripts")
TRANSLATED = ROOT / "translated"
CORRECTED = TRANSLATED / "corrected"
LEDGERS = TRANSLATED / "_EditLedgers"
sys.path.insert(0, str(ROOT))
from claude_translate import looks_english, _EN_WORDS  # noqa: E402

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
BOOKS = {
    "Inn Trouble": "Inn Trouble - ASSEMBLED - FORMATTED",
    "Flour Play": "Flour Play - ASSEMBLED - FORMATTED",
}
LANGS = ["French", "German", "Italian", "Spanish", "Dutch", "Norwegian", "Filipino",
         "Polish", "Romanian", "Czech", "Swedish", "Turkish", "Greek",
         "Brazilian Portuguese"]

# ── the clue chain each book's plot rests on (English side) ────────────────────────
CLUES = {
    "Inn Trouble": {
        "clue phrase 'sapphire at its heart'": r"sapphire at its heart",
        "'five words' claim": r"five words",
        "blackmail note(s)": r"\bnotes?\b",
        "letters (1924 Blackburn)": r"\bletters?\b",
        "catalogue card / index card": r"\b(catalog(ue)? card|index card|card)\b",
        "deed": r"\bdeed\b",
        "twenty dollars (Sam is OWED)": r"twenty dollars|\$20",
        "Snowball": r"\bSnowball\b",
        "cider": r"\bcider\b",
        "the green": r"\bthe green\b",
        "porch": r"\bporch\b",
        "Very nearly (excerpt)": r"\bVery nearly\b",
    },
    "Flour Play": {
        "sour base": r"sour base",
        "acidulant": r"acidulant",
        "walk-in (cooler)": r"walk-in",
        "cold room (Joyce's slip)": r"cold room",
        "ten times": r"ten times",
        "rye": r"\brye\b",
        "gate key": r"gate key|\bkey\b",
        "order book": r"order book",
        "'nothing I can name' (Greta)": r"nothing I can name",
        "two degrees below": r"two degrees",
        "poison* (must stay absent/as English)": r"poison|toxic",
        "flour": r"\bflour\b",
        "pounds": r"\bpounds?\b",
        "DIRTY graffiti": r"DIRTY",
        "Grange": r"\bGrange\b",
        "Pip": r"\bPip\b",
        "Joyce": r"\bJoyce\b",
        "Start reading The Binder's Bequest": r"Start reading",
        "cider": r"\bcider\b",
    },
}

# ── per-language watch-words ─────────────────────────────────────────────────────────
# units_num: words that ALSO mean something ordinary (foot/feet as body part, thumb,
#            Swedish/Norwegian "mil" = 10 km) — flagged only right after a number.
# units:     unambiguous imperial words — always flagged.
NUMW = {
    "French": r"un|une|deux|trois|quatre|cinq|six|sept|huit|neuf|dix|onze|douze|quinze|vingt|trente|quarante|cinquante|soixante|cent|mille|quelques|demi",
    "German": r"ein\w*|zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|elf|zwölf|zwanzig|dreißig|vierzig|fünfzig|hundert|tausend|paar|halb\w*",
    "Italian": r"un\w*|due|tre|quattro|cinque|sei|sette|otto|nove|dieci|venti|trenta|cinquanta|cento|mille|qualche|mezz\w*",
    "Spanish": r"un\w*|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|veinte|treinta|cincuenta|cien\w*|mil|unos|unas|medi\w*",
    "Dutch": r"een|twee|drie|vier|vijf|zes|zeven|acht|negen|tien|twintig|dertig|veertig|vijftig|honderd|paar|half|halve",
    "Norwegian": r"en|ei|et|to|tre|fire|fem|seks|sju|syv|åtte|ni|ti|tjue|tretti|førti|femti|hundre|noen|par|halv\w*",
    "Swedish": r"en|ett|två|tre|fyra|fem|sex|sju|åtta|nio|tio|tjugo|trettio|fyrtio|femtio|hundra|några|par|halv\w*",
    "Polish": r"jed\w*|dw\w*|trz\w*|czter\w*|pięć\w*|pięci\w*|sześ\w*|siedem\w*|siedmi\w*|osiem\w*|ośmi\w*|dziewię\w*|dziesię\w*|kilk\w*|pół|stu|sto",
    "Romanian": r"un|o|unu|doi|două|trei|patru|cinci|șase|şase|șapte|opt|nouă|zece|douăzeci|treizeci|cincizeci|sută|sute|câțiva|câteva|jumătate",
    "Czech": r"jed\w*|dv\w*|tř\w*|čtyř\w*|pět\w*|šest\w*|sedm\w*|osm\w*|devět\w*|deset\w*|dvacet\w*|padesát\w*|sto|pár|několik\w*|půl",
    "Turkish": r"bir|iki|üç|dört|beş|altı|yedi|sekiz|dokuz|on|yirmi|otuz|elli|yüz|birkaç|yarım",
    "Greek": r"ένα|ενός|μία|μια|δύο|τρία|τρεις|τέσσερ\w*|πέντε|έξι|επτά|εφτά|οχτώ|οκτώ|εννιά|δέκα|είκοσι|τριάντα|πενήντα|εκατό|μερικ\w*|μισ\w*",
    "Brazilian Portuguese": r"um|uma|dois|duas|três|quatro|cinco|seis|sete|oito|nove|dez|vinte|trinta|cinquenta|cem|cento|mil|alguns|algumas|meio|meia",
    "Filipino": r"isa|isang|dalawa\w*|tatlo\w*|apat\w*|lima\w*|anim\w*|pito\w*|walo\w*|siyam\w*|sampu\w*|ilang|kalahati|a|one|two|three|four|five|six|ten|twenty|fifty|hundred",
}
_EN_STRICT = r"inch(es)?|yards?|miles?|pounds?|ounces?|gallons?|acres?|Fahrenheit"
WATCH = {
    "French": {"units": r"\b(pouces?|milles?|livres? de|yards?|onces?|gallons?|acres?)\b", "units_num": r"pieds?",
               "currency": r"\b(euros?|centimes?)\b|€", "cider": r"\bcidre\b", "poison": r"\b(poison\w*|empoisonn\w*|toxique\w*)"},
    "German": {"units": r"\b(Zoll|Meilen?|Pfund|Unzen?|Gallonen?|Yards?)\b", "units_num": r"Fuß",
               "currency": r"\b(Euro|Cent)\b|€", "cider": r"\b(Apfelwein|Cidre)\b", "poison": r"\b(Gift\b|Gifte?s\b|vergift\w*|giftig\w*)"},
    "Italian": {"units": r"\b(pollic[ei]|miglia|miglio|libbr\w*|galloni|iard\w*|acri)\b", "units_num": r"piedi|piede|once",
                "currency": r"\b(euro|centesimi)\b|€", "cider": r"\bsidro\b", "poison": r"\b(velen\w*|avvelen\w*|tossic\w*)"},
    "Spanish": {"units": r"\b(pulgadas?|millas?|libras?|onzas?|galones|yardas?|acres?)\b", "units_num": r"pies?",
                "currency": r"\b(euros?|céntimos?|pesetas?)\b|€", "cider": r"\bsidra\b", "poison": r"\b(venen\w*|envenen\w*|tóxic\w*)"},
    "Dutch": {"units": r"\b(inch(es)?|mijl(en)?|gallons?|yards?|acres?)\b", "units_num": r"voet|duim|pond|ons",
              "currency": r"\b(euro|gulden)\b|€", "cider": r"\b(appelwijn)\b", "poison": r"\b(gif\b|giftig\w*|vergiftig\w*)"},
    "Norwegian": {"units": r"\b(tomm\w*|pund|unse\w*|gallon\w*|yard\w*|acre\w*)\b", "units_num": r"fot|mil",
                  "currency": r"\b(kroner?|øre)\b|\bkr\b", "cider": r"\bsider\b", "poison": r"\b(gift\b|forgift\w*|giftig\w*)"},
    "Filipino": {"units": rf"\b({_EN_STRICT}|talampakan|pulgada|milya|libra|onsa|galon|yarda)\b", "units_num": r"feet|foot",
                 "currency": r"\b(piso|sentimo)\b|₱", "cider": r"\b(alak)\b", "poison": r"\b(lason\w*|nilason|poison\w*)"},
    "Polish": {"units": r"\b(cal[ie]?|cali|funt\w*|uncj\w*|galon\w*|jard\w*|akr\w*)\b", "units_num": r"st[oó]p\w*|mil\w*",
               "currency": r"\b(złotych|złotówk\w*|groszy|zł)\b", "cider": r"\b(cydr\w*|jabłecznik\w*)\b", "poison": r"\b(trucizn\w*|otru\w*|toksyczn\w*)"},
    "Romanian": {"units": r"\b(inci|țoli|livre|livră|uncii|galoane|iarzi|acri)\b", "units_num": r"picioare|picior|mile|mil[ăe]",
                 "currency": r"\b(lei|euro)\b", "cider": r"\bcidru\w*", "poison": r"\b(otrav\w*|otrăv\w*|toxic\w*)"},
    "Czech": {"units": r"\b(libr\w*|unc\w*|galon\w*|yard\w*|akr\w*)\b", "units_num": r"stop\w*|palc\w*|míl\w*",
              "currency": r"\b(korun\w*|Kč|halé\w*|euro)\b", "cider": r"\b(cidr\w*|jablečné víno)\b", "poison": r"\b(jed\b|jedu|jedem|otráv\w*|otrav\w*|toxick\w*)"},
    "Swedish": {"units": r"\b(tum|pund|uns|gallon\w*|yard\w*|tunnland)\b", "units_num": r"fot|mil",
                "currency": r"\b(kronor|krona|öre)\b|\bkr\b", "cider": r"\b(äppelvin|cider)\b", "poison": r"\b(gift\b|förgift\w*|giftig\w*)"},
    "Turkish": {"units": r"\b(inç\w*|libre\w*|pound\w*|galon\w*|yarda\w*)", "units_num": r"fit\w*|mil\w*|ayak\w*|ons\w*",
                "currency": r"\b(lira\w*|kuruş\w*|TL|euro)\b|₺", "cider": r"\b(elma şarabı\w*|sider\w*)", "poison": r"\b(zehir\w*|zehirl\w*|toksik\w*)"},
    "Greek": {"units": r"(ίντσ\w*|λίβρ\w*|ουγγι\w*|γαλόν\w*|γιάρδ\w*)", "units_num": r"πόδι\w*|πόδ\w*|μίλι\w*|μίλ\w*",
              "currency": r"(ευρώ|δραχμ\w*|€)", "cider": r"(μηλίτη\w*)", "poison": r"(δηλητήρι\w*|δηλητηρι\w*|τοξικ\w*)"},
    "Brazilian Portuguese": {"units": r"\b(polegadas?|milhas?|libras?|onças?|galões|galão|jardas?|acres?)\b", "units_num": r"pés|pé",
                             "currency": r"\b(reais|centavos?|euros?)\b|R\$|€", "cider": r"\bsidra\b", "poison": r"\b(venen\w*|envenen\w*|tóxic\w*)"},
}
for _l, _w in WATCH.items():
    _w["units_num"] = rf"(?<!\w)(\d+(?:[.,]\d+)?|{NUMW[_l]})[\s -]+({_w['units_num']})\b"
    _w.setdefault("fahrenheit", r"Fahrenheit|°F|Φαρενάιτ|Fahrenhayt")

# Accented letters that belong to each language (plain ASCII is always allowed).
ALPHA = {
    "French": "àâæçéèêëîïôœùûüÿ", "German": "äöüß", "Italian": "àèéìíîòóùú",
    "Spanish": "áéíñóúü", "Dutch": "áéëïóöüèàç", "Norwegian": "æøåéèóòàô",
    "Filipino": "ñáéíóúàèìòù", "Polish": "ąćęłńóśźż", "Romanian": "ăâîșțşţ",
    "Czech": "áčďéěíňóřšťúůýž", "Swedish": "åäöéà", "Turkish": "çğıöşüâîûİ",
    "Brazilian Portuguese": "áâãàçéêíóôõúü", "Greek": "",
}
SHARED_OK = "éè"  # café, José-style loans — not worth flagging

CHAP = re.compile(r"^(Chapter|Chapitre|Kapitel|Capitolo|Capítulo|Hoofdstuk|Kapittel|Kapitola|"
                  r"Rozdział|Capitolul|Κεφάλαιο|Kabanata|Bölüm)\s+(\d+)\s*$", re.I)
SPELLED = re.compile(r"^(\w+(\s+\w+)?\s+(Bölüm|Kapitel|Κεφάλαιο|Chapter)|(Bölüm|Kabanata|Ikalawang|Ika-\w+)\s+\w+)\s*$", re.I)

DEBRIS = re.compile(
    r"(\[[^\]]{0,80}\]|\bnote:|\bN\.B\.|\bcorrection:|\btranslat(or|ion) note|(?-i:\bTODO\b)|"
    r"\blet'?s (use|keep|translate)|\bto preserve\b|\bsource text\b|\boriginal:|"
    r"\*\*|__|^#+\s|<(?!/?bt>)[a-z/][^>]{0,30}>|\(sic\)|\{|\}|(?-i:\bNOTE\b))", re.I)
LOOP = re.compile(r"\b(\w+(?:\s+\w+){0,3})(?:[\s,]+\1\b){2,}", re.I | re.U)
ZW = re.compile(r"[\u200b-\u200f\u2060\ufeff\u00ad]")
FOREIGN_SCRIPT = [
    ("Cyrillic", re.compile(r"[\u0400-\u04ff]")),
    ("Hebrew", re.compile(r"[\u0590-\u05ff]")), ("Arabic", re.compile(r"[\u0600-\u06ff]")),
    ("Armenian", re.compile(r"[\u0530-\u058f]")), ("CJK/Kana/Hangul", re.compile(r"[\u3040-\u30ff\u3400-\u9fff\uac00-\ud7af]")),
    ("Thai", re.compile(r"[\u0e00-\u0e7f]")), ("Devanagari", re.compile(r"[\u0900-\u097f]")),
    ("Vietnamese", re.compile(r"[ơưạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹđĐƠƯ]")),
]
GREEK = re.compile(r"[\u0370-\u03ff\u1f00-\u1fff]")
LATIN = re.compile(r"[A-Za-z]")
NUM = re.compile(r"(?<![\w.,])\d+(?:[.,]\d+)?")
OPENERS = ["«", "»", "„", "“", "”", '"', "—", "–", "-", "‚", "'", "‹"]


def paras(path):
    with zipfile.ZipFile(path) as z:
        x = ET.fromstring(z.read("word/document.xml"))
    return ["".join(t.text or "" for t in p.iter(W + "t")) for p in x.iter(W + "p")]


def chapter_index(P):
    """Map paragraph index -> chapter number (0 = front matter).
    Returns (index, accepted sequence, oddities). Skips the TOC (body starts at the
    heading that is followed by a '2'), ignores stray out-of-sequence headings, and
    folds a chapter whose heading is missing into the previous one. Every skipped or
    renumbered heading is reported in `odd` — those are real formatter/Lisa items."""
    heads = []
    for i, t in enumerate(P):
        s = t.strip()
        m = CHAP.match(s)
        if m:
            heads.append((i, int(m.group(2)), s))
        elif SPELLED.match(s) and len(s) < 40:
            heads.append((i, None, s))
    odd, body = [], []
    start = None
    for k, (i, n, s) in enumerate(heads):           # last heading followed by a '2'
        nxt = [h[1] for h in heads[k + 1:k + 4]]
        if 2 in nxt[:2] and (n in (1, None) or start is None or heads[start][1] != 1):
            start = k
    if start is None:
        return [0] * len(P), [], ["no chapter headings recognised"]
    i0, n0, s0 = heads[start]
    if n0 != 1:
        odd.append(f"[{i0}] Chapter 1 heading reads “{s0}”")
    body.append((i0, 1))
    prev = 1
    rest = heads[start + 1:]
    for k, (i, n, s) in enumerate(rest):
        if n is None:
            n = prev + 1
        if n == prev + 1:
            body.append((i, n)); prev = n
        elif prev + 1 < n <= prev + 3 and not any(h[1] == prev + 1 for h in rest[k + 1:k + 5]):
            odd.append(f"[{i}] heading “{s}” follows Ch{prev} — Ch{prev+1}..{n-1} heading(s) missing")
            body.append((i, n)); prev = n
        else:
            odd.append(f"[{i}] stray heading “{s}” inside Ch{prev}")
    ch, out, k = 0, [], 0
    for i in range(len(P)):
        while k < len(body) and body[k][0] == i:
            ch = body[k][1]
            k += 1
        out.append(ch)
    return out, [n for _, n in body], odd


def back_matter_start(P, chidx):
    # English and translations both end with "What's Next" / excerpt; find the first
    # heading-like short line after the last chapter that names an excerpt/what's-next.
    last = max(chidx) if chidx else 0
    pat = re.compile(r"(What.s Next|Excerpt|Extrait|Auszug|Estratto|Fragment|Fragmento|Utdrag|"
                     r"Uittreksel|Απόσπασμα|Ukázka|Úryvek|Sipi|Ano ang|Co dalej|Ce urmează|"
                     r"Vad händer|Sırada|Τι ακολουθεί|O que vem|Wie geht|Et ensuite|E adesso|"
                     r"Qué sigue|Hva skjer|Wat nu|Książki|Books in)", re.I)
    for i, (t, c) in enumerate(zip(P, chidx)):
        if c == last and pat.search(t) and len(t) < 80 and i > len(P) * 0.85:
            return i
    return len(P)


def names_from_english(EN):
    words = Counter()
    lower = set()
    for t in EN:
        for j, w in enumerate(re.findall(r"[A-Za-z']+", t)):
            if w[0].isupper() and j > 0:
                words[w] += 1
            else:
                lower.add(w.lower())
    return sorted(w for w, c in words.items()
                  if c >= 8 and len(w) >= 3 and w.lower() not in lower
                  and w.lower() not in _EN_WORDS and w not in {"Mrs", "Mr", "Ms", "Chapter", "Inn"})


def run(cmd):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                           errors="replace", cwd=str(ROOT), env={**os.environ, "SCRIPTS_ROOT": str(ROOT)})
        return (r.stdout + r.stderr).strip()
    except Exception as e:  # noqa: BLE001
        return f"(could not run: {e})"


def clip(s, a=0, b=None, w=70):
    b = len(s) if b is None else b
    lo, hi = max(0, a - w), min(len(s), b + w)
    return ("…" if lo else "") + s[lo:hi].replace("\n", " ") + ("…" if hi < len(s) else "")


def check(book, lang, cap=40):
    stem = f"{BOOKS[book]}_{lang}"
    cor = CORRECTED / f"{stem}.docx"
    if not cor.exists():
        print(f"  {lang:22} no corrected copy — not proofread yet, skipped")
        return None
    raw = next((p for p in (TRANSLATED / f"{stem}.docx", ROOT / "_superseded" / f"{stem}.docx")
                if p.exists()), None)
    en_path = next(p for p in (ROOT / "translate_now" / f"{BOOKS[book]}.docx",
                               ROOT / "translate" / f"{BOOKS[book]}.docx") if p.exists())
    EN, T = paras(en_path), paras(cor)
    R = paras(raw) if raw else None
    if R is not None and len(R) != len(T):
        R = None  # not the same paragraph grid → cannot diff safely
    en_ch, en_seq, _ = chapter_index(EN)
    sec, n = {}, Counter()
    t_ch, t_seq, t_odd = chapter_index(T)
    for o in t_odd:
        n['E'] += 1; sec.setdefault('E', []).append('heading: ' + o)
    t_bm = back_matter_start(T, t_ch)

    def add(key, line):
        n[key] += 1
        if n[key] <= cap:
            sec.setdefault(key, []).append(line)

    def tag(i):
        c = t_ch[i]
        return f"[{i}] " + ("front" if c == 0 else ("back" if i >= t_bm else f"Ch{c}"))

    latin_words = Counter()
    allowed = set(ALPHA[lang] + ALPHA[lang].upper() + SHARED_OK + SHARED_OK.upper())
    for i, t in enumerate(T):
        if not t.strip():
            continue
        # A — English
        if looks_english(t):
            add("A", f"{tag(i)} long English paragraph: {t[:120]}")
        else:
            toks = re.findall(r"[A-Za-z']+|[^\sA-Za-z']+", t)
            run_w, start = [], 0
            for tok in toks + ["#"]:
                if re.fullmatch(r"[A-Za-z']+", tok) and tok.lower() in _EN_WORDS:
                    run_w.append(tok)
                elif re.fullmatch(r"[A-Za-z']+", tok) and run_w and tok[0].isupper():
                    run_w.append(tok)  # names inside an English run
                else:
                    if len([w for w in run_w if w.lower() in _EN_WORDS]) >= 4:
                        add("A", f"{tag(i)} English run: “{' '.join(run_w)}”")
                    run_w = []
        # B — scripts / letters
        for name, rx in FOREIGN_SCRIPT:
            m = rx.search(t)
            if m:
                add("B", f"{tag(i)} {name}: {clip(t, m.start(), m.end(), 40)}")
        if ZW.search(t):
            add("B", f"{tag(i)} zero-width/soft-hyphen char(s): {len(ZW.findall(t))}")
        for w in re.findall(r"\w+", t):
            if lang == "Greek":
                if GREEK.search(w) and LATIN.search(w):
                    add("B", f"{tag(i)} mixed Greek+Latin word: {w}")
                elif LATIN.search(w) and len(w) > 2 and i < t_bm:
                    latin_words[w] += 1
            else:
                if GREEK.search(w):
                    add("B", f"{tag(i)} Greek letter in word: {w}")
                bad = {c for c in w if not c.isascii() and c.isalpha() and c not in allowed}
                if bad and not GREEK.search(w):
                    add("B", f"{tag(i)} letter(s) {''.join(sorted(bad))} foreign to {lang}: {w}")
        # C — debris (scene-break lines like *** are fine)
        for m in ([] if re.fullmatch(r"[\s*•·#~-]+", t) else DEBRIS.finditer(t)):
            if "<bt>" in m.group(0):
                continue
            add("C", f"{tag(i)} {m.group(0)!r}: {clip(t, m.start(), m.end(), 50)}")
        # D — loops
        m = LOOP.search(t)
        if m and len(m.group(0)) > 8 and not re.fullmatch(r"[\W\d_]+", m.group(1)):
            add("D", f"{tag(i)} repeated “{m.group(1)}”: {clip(t, m.start(), m.end(), 30)[:200]}")
        # H — watch-words
        for kind, rx in WATCH[lang].items():
            for m in re.finditer(rx, t, re.I):
                add("H", f"{tag(i)} {kind} “{m.group(0)}”: {clip(t, m.start(), m.end(), 45)}")
    if latin_words:
        add("B", "Latin-script words in the Greek text (check each is a deliberate kept name): "
                 + ", ".join(f"{w}×{c}" for w, c in latin_words.most_common(60)))
    # E/F/G — per chapter
    chapters = sorted(set(c for c in en_ch if c > 0))
    en_bm = back_matter_start(EN, en_ch)

    def chtext(P, idx, c, bm):
        return [t for i, t in enumerate(P) if idx[i] == c and i < bm
                and not CHAP.match(t.strip()) and not SPELLED.match(t.strip())]

    ratios = {}
    for c in chapters:
        e, t = chtext(EN, en_ch, c, en_bm), chtext(T, t_ch, c, t_bm)
        le, lt = sum(map(len, e)), sum(map(len, t))
        ratios[c] = (lt / le) if le else 0
    med = statistics.median([r for r in ratios.values() if r]) if any(ratios.values()) else 1
    for c, r in ratios.items():
        if r == 0:
            add("E", f"Ch{c}: NO text found under this chapter number (heading missing → folded "
                     f"into Ch{c-1}? or chapter omitted)")
        elif abs(r / med - 1) > 0.22:
            add("E", f"Ch{c}: length {r/med:.0%} of this edition's normal EN ratio "
                     f"({'LONGER' if r > med else 'SHORTER'} — duplication/omission/heading drift?)")
    whole = " ".join(T)
    names = [nm for nm in names_from_english(EN)
             if len(re.findall(rf"\b{re.escape(nm[:max(3, len(nm) - 2)])}", whole)) >= 5]
    for c in chapters:
        e = " ".join(chtext(EN, en_ch, c, en_bm))
        t = " ".join(chtext(T, t_ch, c, t_bm))
        if not t:
            continue
        en_nums = set(x.replace(",", "").replace(".", "") for x in NUM.findall(e))
        extra = sorted(set(x for x in NUM.findall(t)
                           if x.replace(",", "").replace(".", "") not in en_nums and x != str(c)))
        if extra:
            add("F", f"Ch{c}: numbers not in the English chapter: {', '.join(extra[:12])}")
        if lang != "Greek":
            for nm in names:
                ce = len(re.findall(rf"\b{nm}\b", e))
                stem_ = nm[:max(3, len(nm) - 2)]
                ct = len(re.findall(rf"\b{re.escape(stem_)}", t))
                if ce >= 2 and ct == 0:
                    add("G", f"Ch{c}: '{nm}' ×{ce} in English, ×0 here (renamed? passage dropped?)")
                elif ce >= 6 and ct < ce * 0.4:
                    add("G", f"Ch{c}: '{nm}' ×{ce} in English, only ×{ct} here")
    # I — dialogue system
    opens = Counter()
    for t in T[:t_bm]:
        s = t.strip()
        if s and s[0] in OPENERS:
            opens[s[0]] += 1
    if opens:
        major = opens.most_common(1)[0][0]
        pair = {"«": "»", "„": "“”", "“": "”", '"': '"', "»": "«"}
        sec["I_sum"] = [f"paragraph openers: " + ", ".join(f"{k!r}×{v}" for k, v in opens.most_common())]
        for i, t in enumerate(T[:t_bm]):
            s = t.strip()
            if s and s[0] in OPENERS and s[0] != major and opens[s[0]] < opens[major] * 0.2 \
                    and s[0] not in "-'":
                add("I", f"{tag(i)} opens with {s[0]!r} (book mostly {major!r}): {s[:90]}")
            for o, cl in (("«", "»"), ("„", "“”")):
                if s.count(o) != sum(s.count(x) for x in cl) and o in s:
                    add("I", f"{tag(i)} unbalanced {o}…{cl}: {s[:90]}")
            if s.count('"') % 2:
                add("I", f"{tag(i)} odd number of \" marks: {s[:90]}")
    # J — first pass's own edits
    density = Counter()
    totals = Counter(c for c in t_ch)
    if R is not None:
        for i, (r, t) in enumerate(zip(R, T)):
            if r != t:
                density[t_ch[i]] += 1
                if r.strip() and not t.strip():
                    add("J", f"{tag(i)} EMPTIED by first pass (was: {r[:110]})")
                elif len(r) > 60 and len(t) < len(r) * 0.5:
                    add("J", f"{tag(i)} cut to {len(t)/len(r):.0%} (was: {r[:80]} → now: {t[:80]})")
    # K — clue map (English side) + L standard checks
    clue_rows = []
    for label, rx in CLUES[book].items():
        per = Counter(en_ch[i] if i < en_bm else -1 for i, t in enumerate(EN)
                      for _ in re.finditer(rx, t, re.I))
        if per:
            where = ", ".join(("back" if c == -1 else ("front" if c == 0 else f"Ch{c}")) + f"×{k}"
                              for c, k in sorted(per.items()))
            clue_rows.append(f"{label}: {sum(per.values())} — {where}")
    std = {
        "looks_english": str([p[:90] for p in T if looks_english(p)]),
        "bt_anchors check": run([sys.executable, "bt_anchors.py", "check", str(cor)])[-400:],
        "check_matter": run([sys.executable, "check_matter.py", "--file", str(cor)]).splitlines()[-1:],
        "preflight --verify": "\n".join(l for l in run([sys.executable, str(TRANSLATED / "_tools" / "preflight.py"),
                                                      "--verify", stem]).splitlines()
                                        if re.search(r"paragraphs|italic runs|scene|bt |=>", l)),
    }
    # write
    titles = {"A": "English left in the text", "B": "Other alphabets / letters foreign to the language",
              "C": "MT debris (notes, brackets, markup)", "D": "MT loops", "E": "Chapter length vs English",
              "F": "Numbers not in the English chapter", "G": "Names missing from a chapter",
              "H": "Watch-words (units, currency, cider, poison)", "I": "Dialogue system",
              "J": "First pass's own deletions / big cuts"}
    out = [f"# PROOFCHECK FLAGS — {stem}", "",
           f"Corrected: `translated/corrected/{stem}.docx` · raw for diff: "
           f"`{raw.relative_to(ROOT) if raw and R is not None else 'NONE (no matching raw)'}` · "
           f"English: `{en_path.relative_to(ROOT)}`",
           f"Chapters detected: EN {len(en_seq)} · this edition {len(t_seq)} (sequence {t_seq[:3]}…{t_seq[-3:]})",
           "", "⚑ Every line is a HINT. Confirm against the English before acting. Expect false positives "
           "(body-part 'foot', 'free' = livre, names, loanwords).", ""]
    for k in "ABCDEFGHIJ":
        out.append(f"## {k} — {titles[k]} ({n[k]})")
        if k == "I" and "I_sum" in sec:
            out += sec["I_sum"]
        out += [f"- {x}" for x in sec.get(k, [])] or ["- none"]
        if n[k] > cap:
            out.append(f"- … {n[k]-cap} more not listed (re-run with --cap)")
        out.append("")
    out += ["## K — Clue chain, English side (trace each in the translation)", ""]
    out += [f"- {x}" for x in clue_rows] + [""]
    out += ["## L — Standard checks", ""] + [f"- **{k}:** {v}" for k, v in std.items()] + [""]
    out += ["## M — First-pass change density per chapter (lowest first = least re-read)", ""]
    if density or R is not None:
        rows = sorted(((density[c] / totals[c] if totals[c] else 0), c) for c in set(t_ch) if c > 0)
        out.append(", ".join(f"Ch{c} {d:.0%}" for d, c in rows))
    else:
        out.append("no raw file with a matching paragraph grid — cannot compute")
    LEDGERS.mkdir(parents=True, exist_ok=True)
    dest = LEDGERS / f"{stem}_PROOFCHECK_FLAGS.md"
    dest.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"  {lang:22} " + " ".join(f"{k}={n[k]}" for k in "ABCDEFGHIJ") + f"  → {dest.name}")
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", choices=list(BOOKS))
    ap.add_argument("--all", action="store_true", help="both books, every language")
    ap.add_argument("--langs", help="comma-separated (default: all 14)")
    ap.add_argument("--cap", type=int, default=40, help="max lines listed per section")
    a = ap.parse_args()
    if not a.book and not a.all:
        ap.error("give --book or --all")
    langs = [x.strip() for x in a.langs.split(",")] if a.langs else LANGS
    for l in langs:
        if l not in LANGS:
            ap.error(f"unknown language {l!r}; choose from {LANGS}")
    for book in (BOOKS if a.all else [a.book]):
        print(book)
        for l in langs:
            check(book, l, a.cap)


if __name__ == "__main__":
    main()
