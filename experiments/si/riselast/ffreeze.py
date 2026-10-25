#!/usr/bin/env python3
"""L-SI succ. 5, box 10: DATA for Lemma FREE-FREEZE (docs/si/N5-RL-box10.md §2b). For every in-scope THR fallback k0 of a scope run
(reltrace.runs_of) and every later state t of the same scope run: every z ∈ F_t whose (σ_t, τ)-play lies inside F_k0 has
Ξ_t(z) = Ξ_k0(z) exactly. Also counts the vertices of F_t whose play leaves F_k0 (the only ones that may change).
Usage: ffreeze.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "coarse"))
from reltrace import *

def play(g, s, t, z):
    seen = []
    while z not in seen:
        seen.append(z); z = s[z] if g.owner[z] == 0 else t[z]
    return seen

def scan(g, name):
    o = odd_choice(g); assert o is not None
    assert sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) == 1
    runs, d_o, exits, out = runs_of(g, name); C = Counter(); ex = []
    for S in runs:
        idx = [e["i"] for e in S] + [S[-1]["i"] + 1]
        for p, e in enumerate(S):
            if e["k"] != "F" or e["r"] < -1: continue
            k0 = e["i"]; A = out[k0]; F0 = {v for v in range(g.n) if v != o and v not in A["R"]}
            for t in idx[p + 1:]:
                B = out[t]; Ft = [v for v in range(g.n) if v != o and v not in B["R"]]
                for z in Ft:
                    if set(play(g, B["s"], B["t"], z)) <= F0:
                        C["chk"] += 1
                        if B["Xi"][z] != A["Xi"][z]: C["viol"] += 1; ex.append((name, k0, t, z))
                    else: C["leaves_F0"] += 1
    return C, ex

if __name__ == "__main__":
    T = Counter(); X = []
    for p in sys.argv[1:]:
        c, e = scan(load(p), os.path.basename(p)); T.update(c); X += e
    print("TOTAL", dict(T))
    for e in X[:20]: print("  ", e)
