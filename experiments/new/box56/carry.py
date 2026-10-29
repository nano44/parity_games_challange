#!/usr/bin/env python3
"""L-NEW box 57 probe: print, for orbit indices A..B of F on a game, the Even switches (label: old -> new), the sigma-bar changes, and
the CC bit pattern. Labels from the .pg names. Usage: carry.py GAME A B"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box54")); sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
import n5sf
from n5x import load
path, A, B = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
lab = {}
for l in open(path):
    m = re.match(r'\s*(\d+)\s+\d+\s+\d\s+[\d,]+\s+"([^"]*)"', l)
    if m: lab[int(m.group(1))] = m.group(2)
g = load(path); n = g.n
E, T = n5sf.trace(g, None); T = [x for x in T if "lam" in x]
seq = []
for x in T:
    s = [x["s"][v] if g.owner[v] == 0 else -1 for v in range(n)]
    if not seq or seq[-1] != s: seq.append(s)
VS = [E.evaluate(tuple(s)) for s in seq]
CH = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]
L = lambda v: lab.get(v, str(v))
for j in range(A, min(B, len(seq) - 1) + 1):
    sb = VS[j][1]; pat = "".join("1" if sb[u] == max(set(g.succ[u])) else "0" for u in reversed(CH))
    sw = [f"{L(v)}:{L(seq[j][v])}->{L(seq[j + 1][v])}" for v in range(n) if g.owner[v] == 0 and seq[j][v] != seq[j + 1][v]] if j + 1 < len(seq) else []
    bc = [f"{L(u)}:{L(VS[j][1][u])}->{L(VS[j + 1][1][u])}" for u in CH if j + 1 < len(seq) and VS[j][1][u] != VS[j + 1][1][u]]
    print(j, pat, "EVEN", " ".join(sw), "| ODD", " ".join(bc))
