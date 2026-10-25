#!/usr/bin/env python3
"""L-SI succ. 5, box 10: DATA for the premise of Proposition EV+ (docs/si/N5-RL-box10.md §5). For every in-scope THR fallback k0 of a
scope run with L := M_k0 >= 0, Ev := F_{k0+1} \\ F_k0 (the region evicted at k0), and every later state t of the scope run with r > L on
[k0+1, t]: does the threat's play (the σ_t-play of x0_t = σ̄_t(o)) meet Ev?  (THR-EV) counts such states; (THR-EV-RISE) counts those after a
COARSE_L(θ) rise. Usage: threv.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffreeze import *

def scan2(g, name):
    o = odd_choice(g); assert o is not None
    assert sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) == 1
    runs, d_o, exits, out = runs_of(g, name); C = Counter(); ex = []
    for S in runs:
        for p, e in enumerate(S):
            if e["k"] != "F" or e["M"] < 0 or e["r"] < 0: continue
            k0 = e["i"]; L = e["M"]; A, A1 = out[k0], out[k0 + 1]
            F0 = {v for v in range(g.n) if v != o and v not in A["R"]}
            Ev = {v for v in range(g.n) if v != o and v not in A1["R"] and v not in F0}
            C["fb"] += 1; C["ev_size"] += len(Ev); risen = False
            for q in S[p + 1:]:
                t = q["i"]
                if q["r"] <= L: break
                B = out[t]; pl = play(g, B["s"], B["t"], B["sb"][o]); C["states"] += 1
                if risen: C["post_rise"] += 1
                if set(pl) & Ev:
                    C["thr_ev"] += 1
                    if risen: C["thr_ev_rise"] += 1; ex.append((name, k0, t, L))
                if q["k"] == "S" and q["lt"] > L: risen = True
                if q["k"] == "F": break
    return C, ex

if __name__ == "__main__":
    T = Counter(); X = []
    for p in sys.argv[1:]:
        c, e = scan2(load(p), os.path.basename(p)); T.update(c); X += e
    print("TOTAL", dict(T))
    for e in X[:20]: print("  ", e)
