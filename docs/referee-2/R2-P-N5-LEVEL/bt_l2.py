#!/usr/bin/env python3
"""REFEREE-2 successor 39: own byte test of P-N5-LEVEL line L-2 (claude/l-new 366a38ab). Own parser (not mkl2_211.py): the pairs are read
from the two referee reports at their pinned commits, wrapped lines joined with ONE space (both reports' rule):
  REFEREE 34 (claude/referee 4c8d6c4f, docs/referee/R-P-N5-LEVEL.md §5): the bullets «- LT-1 …», «- LT-2 …», «- LT-3 …»: «old» → «new»;
  «LO-1, after «X»: add «Y»» (insert « Y» right after X);
  REFEREE-2 (claude/referee-2 43824abc, docs/referee-2/R2-P-N5-LEVEL.md 5.4): «- R-1 …» and «- R-2 …», «Old …: «old» New: «new»».
Applied to L-1 (l-new 1e6df499) in the order LT-1, LT-2, LT-3 (checkpoint), R-1, R-2, LO-1; every old string asserted to occur exactly once.
Usage: bt_l2.py L1 R34.md R2.md L2"""
import sys, re, hashlib
L1, R34, R2, L2 = sys.argv[1:5]
def bal(s, i):
    d = 0; j = i
    while j < len(s):
        d += (s[j] == "«") - (s[j] == "»")
        if d == 0: return s[i + 1:j], j + 1
        j += 1
    raise ValueError("unbalanced")
def bullet(text, head):
    L = text.split("\n"); out = None
    for k, l in enumerate(L):
        if re.match(r"^\s*- " + re.escape(head), l):
            ind = len(l) - len(l.lstrip()); out = [l.strip()]
            for m in L[k + 1:]:
                if not m.strip() or (len(m) - len(m.lstrip()) <= ind and m.lstrip().startswith("- ")) or m.startswith("#"): break
                out.append(m.strip())
            return " ".join(out)
    raise KeyError(head)
def quotes(s):
    out = []; i = 0
    while True:
        i = s.find("«", i)
        if i < 0: return out
        q, i = bal(s, i); out.append(q)
r34 = open(R34, encoding="utf-8").read(); r2 = open(R2, encoding="utf-8").read()
pairs = []
for h in ("LT-1", "LT-2", "LT-3"):
    q = quotes(bullet(r34, h)); pairs.append((h, q[0], q[1]))
q = quotes(bullet(r2, "R-1 (requested")); pairs.append(("R-1", q[0], q[1]))
q = quotes(bullet(r2, "R-2 (optional)")); pairs.append(("R-2", q[0], q[1]))
lo = bullet(r34, "OPTIONAL (the Lead's call)"); q = quotes(lo[lo.index("LO-1"):]); pairs.append(("LO-1", q[0], q[0] + " " + q[1]))
s = open(L1, encoding="utf-8").read(); print("L-1 sha1", hashlib.sha1(s.encode()).hexdigest(), len(s.encode()), "B")
for k, (h, old, new) in enumerate(pairs):
    c = s.count(old); print(f"{h}: old occurs {c}×; old {len(old)} chars, new {len(new)} chars"); assert c == 1, h
    s = s.replace(old, new)
    if h == "LT-3": print("after LT-1..LT-3: sha1", hashlib.sha1(s.encode()).hexdigest(), len(s.encode()), "B")
b = s.encode(); print("rebuilt L-2: sha1", hashlib.sha1(b).hexdigest(), len(b), "B; lines", s.count("\n"), "; «|»", s.count("|"),
      "; ( ", s.count("("), " ) ", s.count(")"))
lane = open(L2, "rb").read(); print("lane L-2: sha1", hashlib.sha1(lane).hexdigest(), len(lane), "B;", "EQUAL" if lane == b else "DIFFERENT")
for h, old, new in pairs: print(f"{h} new string present once in lane L-2:", lane.decode().count(new))
