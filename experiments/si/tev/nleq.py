#!/usr/bin/env python3
"""L-SI succ. 6, box 11: DATA for the straddling interval (docs/si/N5-TEV-box11.md §5). At every in-scope S4a step s -> s+1 of a scope run
that comes after a fallback k0 of S (the last one before s) with L := M_k0 >= 0 and r_s <= L (where R29 NL is NOT available): does NL's
conclusion still hold?  (nl1) COARSE_L(Ξ) unchanged at every v ∉ R̄_{s+1};  (nl2) R_s ⊆ R̄_{s+1} (no leave);  (A) every gate at s into F_s
has level <= L. Usage: nleq.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "coarse"))
from reltrace import *

def scan(g, name):
    o = odd_choice(g); assert o is not None
    assert sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) == 1
    runs, d_o, exits, out = runs_of(g, name); C = Counter(); ex = []
    for S in runs:
        L = None
        for e in S:
            if e["k"] == "F": L = e["M"]; continue
            if L is None or L < 0 or e["r"] > L: continue
            s = e["i"]; a, b = out[s], out[s + 1]; Rb1 = b["R"] | {o}
            C["steps"] += 1; C["r_eq_L" if e["r"] == L else "r_lt_L"] += 1
            if any(coarse(b["Xi"][v], L) != coarse(a["Xi"][v], L) for v in range(g.n) if v not in Rb1):
                C["nl1_fail"] += 1; ex.append((name, "nl1", s, L, e["r"]))
            if not a["R"] <= Rb1: C["nl2_fail"] += 1; ex.append((name, "nl2", s, L, e["r"]))
            if any(l > L for y, z, l in a["gl"] if z != o and z not in a["R"]): C["A_fail"] += 1
    return C, ex

if __name__ == "__main__":
    T = Counter(); X = []
    for p in sys.argv[1:]:
        c, e = scan(load(p), os.path.basename(p)); T.update(c); X += e
    print("TOTAL", dict(T))
    for e in X[:30]: print("  ", e)
