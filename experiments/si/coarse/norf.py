#!/usr/bin/env python3
"""L-SI box 9: DATA for Lemma NO-RF-OLD and CONJECTURE NO-RF (docs/si/N5-C-box9.md §8). In a scope run (reltrace.py runs_of), after a
fallback k0 with L := M_k0, let j be the first S4a step with lev(θ_j, θ_{j+1}) > L and r_j > L. At every later state t of the run
before the next fallback with r > L on [k0+1, t]: (NO-RF-OLD) no gate (y, z) with y ∈ R_t ∩ R_j, z ∈ F_t; (NO-RF) none with y ∈ R_t at
all (entrants after j included). Also counts fallbacks after such a rise inside the scope run. Usage: norf.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reltrace import *

def scan_n(g, name):
    runs, d_o, exits, out = runs_of(g, name); o = odd_choice(g); C = Counter(); ex = []
    for S in runs:
        L = None; j = None; ok = True
        for t, e in enumerate(S):
            if e["k"] == "F":
                if j is not None: C["fb_after_rise"] += 1; ex.append((name, "fb-after-rise", e["i"], L, e["M"]))
                L = e["M"]; j = None; ok = True; continue
            if L is None: continue
            ok = ok and e["r"] > L
            a = out[e["i"]]
            if j is not None and ok:
                C["chk"] += 1
                for y, z, l in a["gl"]:
                    if y in a["R"] and z not in a["R"] and z != o:
                        if y in out[j]["R"]: C["old_viol"] += 1; ex.append((name, "NO-RF-OLD", e["i"], y, z, l, L))
                        else: C["new_viol"] += 1; ex.append((name, "NO-RF", e["i"], y, z, l, L))
            if j is None and ok and e["lt"] > L: j = e["i"]; C["rises"] += 1
    return C, ex

if __name__ == "__main__":
    T = Counter(); X = []
    for p in sys.argv[1:]:
        c, e = scan_n(load(p), os.path.basename(p)); T.update(c); X += e
    print("TOTAL", dict(T))
    for e in X[:20]: print("  ", e)
