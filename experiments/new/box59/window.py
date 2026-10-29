#!/usr/bin/env python3
"""L-NEW box 59: print, for transitions A..B of the distinct-sigma sequence, sigma at the named Even vertices and the top-K
non-sink path vertices of Xi at the named vertices. Usage: window.py GAME.pg A B SIGMA_LABELS XI_LABELS [K]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import flips
path, A, B = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); SL = sys.argv[4].split(","); XL = sys.argv[5].split(",")
K = int(sys.argv[6]) if len(sys.argv) > 6 else 6
g, E, seq, ev = flips.run(path); lab = flips.labels(path); inv = {v: k for k, v in lab.items()}; L = lambda v: lab.get(v, str(v))
sink = {inv[x] for x in ("p", "q") if x in inv}
for j in range(A, B + 1):
    vs, _ = E.evaluate(tuple(seq[j]["s"]))
    def top(x):
        m = vs[inv[x]][1]; vv = sorted((v for v in range(g.n) if E.bit[v] & m and v not in sink), key=lambda v: -E.rank[v])[:K]
        return " ".join(L(v) for v in vv)
    fl = " ".join(f"{L(e['u'])}:{L(e['a'])}>{L(e['b'])}" for e in ev if e["j"] == j - 1)
    print(f"j {j} {('['+fl+']') if fl else ''} " + " ".join(f"{x}>{L(seq[j]['s'][inv[x]])}" for x in SL) + " || " +
          " | ".join(f"{x}: {top(x)}" for x in XL))
