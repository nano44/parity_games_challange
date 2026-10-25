#!/usr/bin/env python3
"""L-SI succ. 6, box 11: DATA for "THR => M >= 0 in scope". For every in-scope fallback (reltrace.runs_of; (h) at k, H2 and w kept at k+1):
the kind (EQ: r = ⊥; THR u* = none: r = -1; THR u* ≠ none: r >= 0), M_k, whether an R -> F gate of level >= 0 exists, and rank o vs rank c.
Usage: lvm1.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "coarse"))
from reltrace import *

def scan(g, name):
    o = odd_choice(g); assert o is not None
    assert sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) == 1
    runs, d_o, exits, out = runs_of(g, name); C = Counter(); ex = []
    for S in runs:
        for e in S:
            if e["k"] != "F": continue
            a = out[e["i"]]; r, M = e["r"], e["M"]
            kind = "EQ" if r <= -2 else ("THR_none" if r == -1 else "THR")
            C[kind] += 1; C[f"{kind}_M{'>=0' if M >= 0 else M}"] += 1
            if kind != "EQ" and M < 0: ex.append((name, e["i"], kind, r, M))
    return C, ex

if __name__ == "__main__":
    T = Counter(); X = []
    for p in sys.argv[1:]:
        c, e = scan(load(p), os.path.basename(p)); T.update(c); X += e
    print("TOTAL", dict(T))
    for e in X[:30]: print("  ", e)
