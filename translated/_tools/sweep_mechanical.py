#!/usr/bin/env python3
r"""Run the MECHANICAL sweeps over many editions in one pass — no model needed.

Built 2026-08-12. On the Book-1 run these three jobs cost ~365k sub-agent tokens
because each was handed to a reasoning agent per edition. Two of them are pure
pattern work with a verification gate and do not need a model at all:

  asterisks : Markdown `*emphasis*` -> real italic runs (55 spans on Book 1)
  units     : report imperial tokens per edition so the units agent gets a
              worklist instead of discovering it (the CONVERSION itself stays
              with a model — it needs context to tell a measurement from an
              idiom, and to keep the fire-shelter arithmetic consistent)

⚑ WHAT THIS DELIBERATELY DOES NOT DO
Back matter and unit CONVERSION are NOT mechanical. Back matter is translated
prose in the author's voice; conversion requires judging "every foot of that
climb" (idiom, keep) against "sixty feet of crawl" (measurement, convert), and
requires moving linked numbers together. Those stay with sub-agents.

Scene-break markers (`* * *`) are protected: a paragraph that is entirely
asterisks and whitespace is structural and is never touched. The script aborts
on any edition whose scene-break count would change.

USAGE
    python sweep_mechanical.py --book KB_H1_2 --langs French,German,Italian
    python sweep_mechanical.py --book KB_H1_2 --apply
"""
import argparse
import re
import shutil
import sys
import zipfile
from datetime import datetime
import os
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(os.environ.get("SCRIPTS_ROOT") or r"C:\Users\User\Scripts")  # cloud: export SCRIPTS_ROOT=<repo root>
TRANSLATED = ROOT / "translated"
CORRECTED = TRANSLATED / "corrected"
PROOFREAD_DIR = ROOT / "proofread"
BACKUP = TRANSLATED / "_EditLedgers" / "_sweep_backups"
DOC = "word/document.xml"
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

SPAN = re.compile(r"\*([^*\n]+?)\*")
SCENE_ONLY = re.compile(r"^[\*\s\u2022\u00b7]+$")
IMPERIAL = re.compile(
    r"\b\d*\s*(pieds?|pouces?|livres?|milles?|Fuß|Zoll|Pfund|Meilen?|piedi|"
    r"pollic[ei]|libbr\w*|migli[ao]|acri|iarde)\b", re.I)


def load(p):
    with zipfile.ZipFile(p) as z:
        names = z.namelist()
        xml = z.read(DOC).decode("utf8")
        others = {n: z.read(n) for n in names if n != DOC}
    return xml, names, others


def save(p, xml, names, others):
    with zipfile.ZipFile(p, "w", zipfile.ZIP_DEFLATED) as z:
        for n in names:
            z.writestr(n, xml.encode("utf8") if n == DOC else others[n])


def unescape(s):
    return (s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
             .replace("&quot;", '"').replace("&apos;", "'"))


def escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def paras(xml):
    return list(re.finditer(r"<w:p[ >].*?</w:p>", xml, re.S))


def ptext(px):
    return unescape("".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", px, re.S)))


def italic_runs(path):
    """Parsed italic run text. NOT a string count of '<w:i/>' — writers emit
    '<w:i />' with a space and a raw count silently returns 0."""
    with zipfile.ZipFile(path) as z:
        x = ET.fromstring(z.read(DOC))
    out = []
    for r in x.iter(W + "r"):
        rpr = r.find(W + "rPr")
        if rpr is not None and rpr.find(W + "i") is not None:
            s = "".join(t.text or "" for t in r.iter(W + "t")).strip()
            if s:
                out.append(s)
    return out


def convert_asterisks(pxml):
    if SCENE_ONLY.match(ptext(pxml).strip()):
        return pxml, 0
    edits, n = [], 0
    for rm in re.finditer(r"<w:r[ >].*?</w:r>", pxml, re.S):
        run = rm.group(0)
        tm = re.search(r"(<w:t[^>]*>)(.*?)(</w:t>)", run, re.S)
        if not tm or "*" not in tm.group(2):
            continue
        text = unescape(tm.group(2))
        if not SPAN.search(text):
            continue
        rpr_m = re.search(r"<w:rPr>.*?</w:rPr>", run, re.S)
        rpr = rpr_m.group(0) if rpr_m else ""
        irpr = (rpr.replace("</w:rPr>", "<w:i/></w:rPr>") if rpr
                else "<w:rPr><w:i/></w:rPr>")
        pieces, last = [], 0
        for m in SPAN.finditer(text):
            if m.start() > last:
                pieces.append((rpr, text[last:m.start()]))
            pieces.append((irpr, m.group(1)))
            last = m.end()
            n += 1
        if last < len(text):
            pieces.append((rpr, text[last:]))
        edits.append((rm.start(), rm.end(), "".join(
            '<w:r>%s<w:t xml:space="preserve">%s</w:t></w:r>' % (pr, escape(s))
            for pr, s in pieces if s)))
    if not edits:
        return pxml, 0
    out = pxml
    for s, e, rep in sorted(edits, key=lambda x: -x[0]):
        out = out[:s] + rep + out[e:]
    return out, n


def source_for(stem):
    if (CORRECTED / f"{stem}.docx").exists():
        return CORRECTED / f"{stem}.docx"
    # " - FORMATTED" FIRST — that copy is the deliverable. Preferring the bare stem
    # swept the raw pre-format draft and left the shipping file untouched.
    for d in (PROOFREAD_DIR, TRANSLATED):
        for c in (d / f"{stem} - FORMATTED.docx", d / f"{stem}.docx"):
            if c.exists():
                return c
    return None


def sweep(stem, dry=True):
    src = source_for(stem)
    if not src:
        print(f"  {stem[:56]:56} NOT FOUND")
        return
    dst = CORRECTED / f"{stem}.docx"
    if src != dst:
        if not dry:
            CORRECTED.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        work = src
    else:
        work = dst

    xml, names, others = load(work)
    scene_before = sum(1 for p in paras(xml)
                       if ptext(p.group(0)).strip()
                       and SCENE_ONLY.match(ptext(p.group(0)).strip()))
    units = sum(len(IMPERIAL.findall(ptext(p.group(0)))) for p in paras(xml))

    total, new_xml, off = 0, xml, 0
    for pm in paras(xml):
        rebuilt, n = convert_asterisks(pm.group(0))
        if n:
            s, e = pm.start() + off, pm.end() + off
            new_xml = new_xml[:s] + rebuilt + new_xml[e:]
            off += len(rebuilt) - (pm.end() - pm.start())
            total += n

    scene_after = sum(1 for p in paras(new_xml)
                      if ptext(p.group(0)).strip()
                      and SCENE_ONLY.match(ptext(p.group(0)).strip()))
    lang = stem.rsplit("_", 1)[-1]
    if scene_before != scene_after:
        print(f"  {lang:10} SCENE BREAKS {scene_before}->{scene_after} — ABORTED")
        return
    print(f"  {lang:10} asterisk spans: {total:3}   scene breaks: {scene_after} (ok)   "
          f"imperial tokens remaining: {units}")

    if total and not dry:
        BACKUP.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        shutil.copy2(dst if dst.exists() else work,
                     BACKUP / f"{stem}.{stamp}.pre-sweep.docx")
        before = italic_runs(work)
        save(dst, new_xml, names, others)
        after = italic_runs(dst)
        if len(after) != len(before) + total:
            print(f"      ⚑ italic runs {len(before)} -> {len(after)}, "
                  f"expected +{total} — INSPECT")
        else:
            print(f"      written; italic runs {len(before)} -> {len(after)} (+{total})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", required=True)
    ap.add_argument("--langs")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    stems = set()
    for d in (PROOFREAD_DIR, TRANSLATED, CORRECTED):
        for p in d.glob("*.docx"):
            if p.name.startswith("~$"):
                continue
            s = p.stem
            if s.endswith(" - FORMATTED"):
                s = s[:-len(" - FORMATTED")]
            if s.startswith(a.book):
                stems.add(s)
    if a.langs:
        want = {x.strip() for x in a.langs.split(",")}
        stems = {s for s in stems if s.rsplit("_", 1)[-1] in want}

    print("DRY RUN (pass --apply to write)" if not a.apply else "APPLYING")
    for s in sorted(stems):
        sweep(s, not a.apply)


if __name__ == "__main__":
    main()
