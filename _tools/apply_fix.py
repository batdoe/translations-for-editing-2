"""Run-safe, verified replacements in a corrected/ working copy.

    from apply_fix import Fixer
    fx = Fixer(STEM)                                   # opens corrected/STEM.docx
    fx.fix(idx, expected_full_paragraph_text, old, new, why)
    fx.save()                                          # writes the copy; returns log rows

fix() REFUSES (returns False, logs reason) when:
  - paragraph idx's full current text != expected_full_paragraph_text (no fuzzy matching)
  - `old` does not occur exactly once in that paragraph
  - `old` spans runs with different formatting (split it into smaller fixes, one per run)
  - the paragraph has non-text run content (drawings, breaks, fields, hyperlinks)
The replacement inherits the formatting of the run(s) it replaces; every other run is untouched,
so italic/bold runs elsewhere in the paragraph survive. Never call claude_translate.set_para_text().
"""
import os, sys, copy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
from docx.oxml import OxmlElement
from lxml import etree

TEXT_ONLY = {qn("w:rPr"), qn("w:t")}


def _key(rpr):
    return etree.tostring(rpr) if rpr is not None else b""


class Fixer:
    def __init__(self, stem):
        self.stem = stem
        self.path = stem_path(stem, "corrected")
        self.doc = Document(self.path)
        self.log = []

    def _refuse(self, idx, why, old, new):
        self.log.append(("REFUSED", idx, old, new, why))
        print(f"REFUSED para {idx}: {why}")
        return False

    def fix(self, idx, expected, old, new, why=""):
        p = self.doc.paragraphs[idx]
        if p.text != expected:
            return self._refuse(idx, "paragraph text does not match expected exactly", old, new)
        if p.text.count(old) != 1:
            return self._refuse(idx, f"'old' occurs {p.text.count(old)} times (need exactly 1)", old, new)
        runs = list(p._p.iter(qn("w:r")))
        if any(ch.tag not in TEXT_ONLY for r in runs for ch in r) or any(r.getparent() is not p._p for r in runs):
            return self._refuse(idx, "paragraph has non-text run content or nested runs", old, new)
        # map chars -> run index
        owner, pos = [], 0
        for k, r in enumerate(runs):
            t = "".join(x.text or "" for x in r.iter(qn("w:t")))
            owner += [k] * len(t)
        start = p.text.index(old); end = start + len(old)
        touched = sorted(set(owner[start:end])) if old else [owner[start] if start < len(owner) else owner[-1]]
        keys = {_key(runs[k].find(qn("w:rPr"))) for k in touched}
        if len(keys) > 1:
            return self._refuse(idx, "'old' crosses runs with different formatting; split the fix", old, new)
        # rewrite: put the whole new text of the touched runs into the first touched run, empty the rest
        first, last = touched[0], touched[-1]
        seg_start = owner.index(first)
        seg_end = len(owner) - owner[::-1].index(last)
        seg = p.text[seg_start:seg_end]
        new_seg = seg[: start - seg_start] + new + seg[end - seg_start:]
        for k in touched:
            for t in list(runs[k].iter(qn("w:t"))):
                runs[k].remove(t)
        tt = OxmlElement("w:t"); tt.text = new_seg
        tt.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        runs[first].append(tt)
        for k in touched[1:]:
            p._p.remove(runs[k])
        after = p.text
        if after != expected.replace(old, new, 1):
            raise RuntimeError(f"post-check failed on para {idx}")
        self.log.append(("APPLIED", idx, old, new, why))
        return True

    def save(self):
        self.doc.save(self.path)
        return self.log
