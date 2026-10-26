"""Mechanical sweep: copy each edition to corrected/, convert Markdown *emphasis* to real italic runs.

  python _tools/sweep_mechanical.py            # dry run
  python _tools/sweep_mechanical.py --apply    # writes corrected/<stem>.docx and corrected/_baseline/<stem>.docx

Scene-break lines (* * *) are protected; the run aborts an edition if their count would change.
Never touches the originals.
"""
import os, re, sys, copy, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
from docx.oxml import OxmlElement

SPAN = re.compile(r"\*([^*\n]+?)\*")
TEXT_ONLY = {qn("w:rPr"), qn("w:t")}


def sweep_para(p):
    """Return list of converted spans, or None if paragraph is untouched/skipped."""
    t = p.text
    if "*" not in t or SCENE_BREAK.match(t):
        return None
    runs = list(p._p.iter(qn("w:r")))
    if any(ch.tag not in TEXT_ONLY for r in runs for ch in r):
        return ("SKIP: non-text run content", t)
    if any(r.getparent() is not p._p for r in runs):
        return ("SKIP: runs inside hyperlink/field", t)
    # char -> (rPr, italic flag)
    chars = []
    for r in runs:
        rpr = r.find(qn("w:rPr"))
        for c in "".join(x.text or "" for x in r.iter(qn("w:t"))):
            chars.append([c, rpr, is_italic(r)])
    full = "".join(c[0] for c in chars)
    spans = list(SPAN.finditer(full))
    if not spans:
        return ("SKIP: unpaired asterisk", t)
    drop = set()
    for m in spans:
        drop.update([m.start(), m.end() - 1])
        for i in range(m.start() + 1, m.end() - 1):
            chars[i][2] = True
    keep = [c for i, c in enumerate(chars) if i not in drop]
    # group consecutive chars sharing the same source rPr + italic flag
    groups = []
    for c, rpr, it in keep:
        if groups and groups[-1][1] is rpr and groups[-1][2] == it:
            groups[-1][0] += c
        else:
            groups.append([c, rpr, it])
    anchor = runs[0].getprevious()
    parent = p._p
    for r in runs:
        parent.remove(r)
    idx = list(parent).index(anchor) + 1 if anchor is not None else len([e for e in parent if e.tag == qn("w:pPr")])
    for text, rpr, it in groups:
        r = OxmlElement("w:r")
        new_rpr = copy.deepcopy(rpr) if rpr is not None else OxmlElement("w:rPr")
        if it and new_rpr.find(qn("w:i")) is None:
            new_rpr.append(OxmlElement("w:i"))
        if len(new_rpr):
            r.append(new_rpr)
        tt = OxmlElement("w:t")
        tt.text = text
        tt.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        r.append(tt)
        parent.insert(idx, r)
        idx += 1
    return [m.group(1) for m in spans]


def run(apply):
    os.makedirs(BASELINE, exist_ok=True)
    for stem in editions():
        src = stem_path(stem)
        before = stats(src)
        d = Document(src)
        conv, skipped = [], []
        for p in d.paragraphs:
            res = sweep_para(p)
            if res is None:
                continue
            if isinstance(res, tuple):
                skipped.append(res)
            else:
                conv.extend(res)
        print(f"{stem}: converted {len(conv)} spans, skipped {len(skipped)}")
        for s in conv:
            print("    *", s[:70])
        for why, t in skipped:
            print("    !", why, "|", t[:80])
        if apply:
            out = stem_path(stem, "corrected")
            if os.path.exists(out):
                print("    corrected copy already exists - not overwriting")
                continue
            d.save(out)
            after = stats(out)
            if after["scene_breaks"] != before["scene_breaks"] or after["paras"] != before["paras"]:
                os.remove(out)
                print("    ABORT: scene-break/paragraph count changed")
                continue
            shutil.copy(out, stem_path(stem, "baseline"))
            print(f"    wrote corrected copy; asterisks left={after['asterisks']} italics {len(before['italics'])}->{len(after['italics'])}")


if __name__ == "__main__":
    run("--apply" in sys.argv)
