"""Pre-flight report and post-write integrity check.

  python _tools/preflight.py                 # one line per edition
  python _tools/preflight.py --current       # inspect corrected/ copies instead
  python _tools/preflight.py --verify STEM   # PASS/FAIL: corrected/STEM vs corrected/_baseline/STEM
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

UNITS = re.compile(r"\b(\d+\s*(ft|in|mi|yd|lb|lbs|oz)\b|°F|Fahrenheit|f[oø]t|tommer?|mijl|Meilen?|Zoll|pouces?|pieds?|milles?|pollici|piedi|miglia|pulgadas?|pies|millas|yardas?|libras?|onzas?|inch(es)?|feet|miles?|yards?|pounds?)\b", re.I)


def line(stem, where):
    p = stem_path(stem, where)
    if not os.path.exists(p):
        return f"{stem}: (no {where} copy)"
    s = stats(p)
    units = sum(len(UNITS.findall(t)) for t in s["text"])
    arts = "".join(c if os.path.exists(x) else "-" for c, x in [
        ("R", os.path.join(LEDGERS, stem + "_PROOFREAD.md")),
        ("C", stem_path(stem, "corrected")),
        ("A", os.path.join(LEDGERS, stem + "_APPLIED.md"))])
    return (f"{stem}: paras={s['paras']} nonempty={s['nonempty']} H1={s['heading1']} breaks={s['scene_breaks']} "
            f"asterisks={s['asterisks']} italics={len(s['italics'])} bt={s['bt_spans']} unit-tokens={units} [{arts}]")


def verify(stem):
    a, b = stats(stem_path(stem, "baseline")), stats(stem_path(stem, "corrected"))
    ok = True
    def chk(name, x, y):
        nonlocal ok
        good = x == y
        ok &= good
        print(f"  {'PASS' if good else 'FAIL'} {name}: baseline={x if not isinstance(x, list) else len(x)} now={y if not isinstance(y, list) else len(y)}")
    print(f"VERIFY {stem}")
    chk("paragraphs", a["paras"], b["paras"])
    chk("scene breaks", a["scene_breaks"], b["scene_breaks"])
    chk("bt spans", a["bt_spans"], b["bt_spans"])
    chk("italic runs (content+order)", a["italics"], b["italics"])
    if a["italics"] != b["italics"]:
        import difflib
        for d in difflib.unified_diff(a["italics"], b["italics"], lineterm="", n=0):
            print("     ", d)
    changed = [i for i, (x, y) in enumerate(zip(a["text"], b["text"])) if x != y]
    print(f"  INFO paragraphs changed vs baseline: {len(changed)}")
    print("RESULT:", "PASS" if ok else "FAIL (check that every difference is an intended, logged fix)")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[:1] == ["--verify"]:
        verify(args[1])
    else:
        where = "corrected" if "--current" in args else "translated"
        print("ENGLISH:", stats(ENGLISH)["paras"], "paras,", stats(ENGLISH)["heading1"], "H1")
        for s in editions():
            print(line(s, where))
