#!/usr/bin/env python3
"""L-NEW box 62: labelled trace of plain N5 (box21/n5x.trace, S3 start): per iteration the Even switches (label:old>new), Odd tau switches,
and changes of Odd's best reply sbar(sigma). Usage: n5trace.py GAME.pg [A B]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, HERE)
from n5x import load, trace, Engine
import flips
p = sys.argv[1]; A, B = (int(sys.argv[2]), int(sys.argv[3])) if len(sys.argv) > 3 else (0, 10 ** 9)
g = load(p); lab = flips.labels(p); L = lambda v: lab.get(v, str(v)); E = Engine(g)
st, fb = trace(g, check=False)
for k in range(len(st) - 1):
    if not A <= k <= B: continue
    (s, t), (s2, t2) = st[k], st[k + 1]
    sb, sb2 = E.evaluate(s)[1], E.evaluate(s2)[1]
    S = " ".join(f"{L(v)}:{L(s[v])}>{L(s2[v])}" for v in range(g.n) if g.owner[v] == 0 and s[v] != s2[v])
    T = " ".join(f"{L(v)}:{L(t[v])}>{L(t2[v])}" for v in range(g.n) if g.owner[v] == 1 and t[v] != t2[v])
    D = " ".join(f"{L(v)}:{L(sb[v])}>{L(sb2[v])}" for v in range(g.n) if g.owner[v] == 1 and sb[v] != sb2[v])
    H = " ".join(f"{L(v)}={L(t2[v])}" for v in range(g.n) if L(v).startswith("h"))
    print(f"{k+1:3d} S[{S}] T[{T}] SBAR[{D}] tau@h: {H}")
