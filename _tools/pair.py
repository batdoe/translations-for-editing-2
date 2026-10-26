"""Print English + translation for one section, with paragraph indices (empty paragraphs omitted).

  python _tools/pair.py STEM --ch N        # chapter N
  python _tools/pair.py STEM --front       # everything before chapter 1
  python _tools/pair.py STEM --back        # everything after the last chapter's body
  python _tools/pair.py STEM --map         # chapter heading indices in both files
Reads the corrected/ working copy by default; add --orig to read the untouched original.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

LABEL = re.compile(r"^\s*(Chapter|Hoofdstuk|Chapitre|Kapitel|Capitolo|Kapittel|Capítulo)\s+(\d+)\s*$")


def chapter_starts(texts):
    hits = [(i, int(m.group(2))) for i, t in enumerate(texts) if (m := LABEL.match(t))]
    # the body run is the longest increasing 1..N chain beginning at the LAST "1" that is followed by "2"
    best = []
    for k, (i, n) in enumerate(hits):
        if n != 1:
            continue
        chain = [(i, n)]
        for j, m in hits[k + 1:]:
            if m == chain[-1][1] + 1:
                chain.append((j, m))
        if len(chain) >= len(best):
            best = chain
    # a mislabelled heading breaks the chain (e.g. Dutch chapter 1 printed as "Hoofdstuk 3"):
    # if no chain starts at 1, take the longest chain from any start and back-fill by position
    if len(best) < 20:
        for k, (i, n) in enumerate(hits):
            chain = [(i, n)]
            for j, m in hits[k + 1:]:
                if m == chain[-1][1] + 1:
                    chain.append((j, m))
            if len(chain) > len(best):
                best = chain
        while best and best[0][1] > 1:
            prev = [h for h in hits if h[0] < best[0][0]]
            if not prev:
                break
            print(f"!! WARNING: heading at para {prev[-1][0]} reads {texts[prev[-1][0]]!r}, treated as chapter {best[0][1]-1} by position", file=sys.stderr)
            best.insert(0, (prev[-1][0], best[0][1] - 1))
    return best


def sections(texts, back_marker_count):
    st = chapter_starts(texts)
    return st


def show(label, texts, lo, hi):
    print(f"----- {label} [{lo}:{hi}]")
    for i in range(lo, hi):
        if texts[i].strip():
            print(f"{i}: {texts[i]}")


if __name__ == "__main__":
    stem, mode = sys.argv[1], sys.argv[2]
    tpath = stem_path(stem, "translated" if "--orig" in sys.argv else "corrected")
    en = [p.text for p in Document(ENGLISH).paragraphs]
    tr = [p.text for p in Document(tpath).paragraphs]
    se, stt = chapter_starts(en), chapter_starts(tr)
    if mode == "--map":
        print("EN:", se); print("TR:", stt); sys.exit()
    # English back matter starts at the first Heading after chapter 31 ("What's Next?")
    en_back = next(i for i, t in enumerate(en) if t.strip() == "What's Next?" and i > se[-1][0])
    if mode == "--front":
        show("EN front", en, 0, se[0][0]); show("TR front", tr, 0, stt[0][0] if stt else len(tr))
    elif mode == "--back":
        show("EN back", en, en_back, len(en)); show("TR back (from last chapter start)", tr, stt[-1][0], len(tr))
        print("(note: TR back matter is inside the last chapter span above; match it against EN back)")
    elif mode == "--ch":
        n = int(sys.argv[3])
        def rng(starts, total, end_override=None):
            d = dict((num, i) for i, num in starts)
            lo = d[n]
            hi = d.get(n + 1, end_override or total)
            return lo, hi
        lo, hi = rng(se, len(en), en_back)
        show(f"EN chapter {n}", en, lo, hi)
        if n in dict((num, i) for i, num in stt):
            lo, hi = rng(stt, len(tr))
            show(f"TR chapter {n}", tr, lo, hi)
        else:
            print(f"!! chapter {n} heading not found in translation; use --map")
