#!/usr/bin/env python3
"""L-SI succ. 5, box 10: per-state trace around the scope runs of one 𝒞^1O game (DATA). Columns: state i, F (fallback) or S, in-scope
flag, r = lev(θ, w), lt = lev(θ_i, θ_{i+1}), M = max gate level, #gates, #RF = gates R -> F (window gates), #Wimp = gates that are
W-improving (nominal), x0 = σ̄(o), e = τ(o), |R ∩ exits|. Usage: rltrace.py game.pg"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "coarse"))
from reltrace import *

def main(p):
    g = load(p); o = odd_choice(g); assert o is not None
    assert sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) == 1
    runs, d_o, exits, out = runs_of(g, p); E = n5.Engine(g)
    inscope = {e["i"] for S in runs for e in S}
    for i, a in enumerate(out):
        R = a["R"]; W = a["W"]
        rf = sum(1 for y, z in a["Is"] if y in R and z not in R and z != o)
        wimp = sum(1 for y, z in a["Is"] if E.key(W[z]) > E.key(W[a["s"][y]]))
        lt = lev(a["Xi"][o], out[i + 1]["Xi"][o]) if i + 1 < len(out) else None
        print(i, "F" if a["fb"] else "S", "in" if i in inscope else "--", "r", lev(a["Xi"][o], W[o]), "lt", lt, "M", a["M"],
              "gates", len(a["Is"]), "RF", rf, "Wimp", wimp, "x0", a["sb"][o], "e", a["t"][o], "Rex", sum(1 for x in exits if x in R), "h", int(a["h"]))

if __name__ == "__main__": main(sys.argv[1])
