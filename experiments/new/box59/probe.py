#!/usr/bin/env python3
"""L-NEW box 59: at every SBC event of N5-SF print the flips and the top-K vertices (by relevance) of the path set of Xi at the named
vertices, before and after. Usage: probe.py GAME.pg LABEL[,LABEL..] [K]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import flips
path = sys.argv[1]; names = sys.argv[2].split(","); K = int(sys.argv[3]) if len(sys.argv) > 3 else 6
g, E, seq, ev = flips.run(path); lab = flips.labels(path); inv = {v: k for k, v in lab.items()}
L = lambda v: lab.get(v, str(v))
def top(val):
    vs = sorted((v for v in range(g.n) if E.bit[v] & val[1]), key=lambda v: -E.rank[v])[:K]
    return " ".join(L(v) for v in vs)
for j in sorted({e["j"] for e in ev}):
    va, _ = E.evaluate(tuple(seq[j]["s"])); vb, _ = E.evaluate(tuple(seq[j + 1]["s"]))
    fl = " ".join(f"{L(e['u'])}:{L(e['a'])}>{L(e['b'])}" for e in ev if e["j"] == j)
    print(f"j {j} [{fl}] " + " | ".join(f"{x}: {top(va[inv[x]])} -> {top(vb[inv[x]])}" for x in names))
