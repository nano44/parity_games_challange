#!/usr/bin/env python3
"""Box 28 (X): per phase ((λ_Ξ, λ_U, τ(o)) constant): transitions, crossing transitions (R = vertices whose (σ, τ)-play reaches o
changes), entries, leaves, OTHER-touching transitions ((h) fails and Ξ ≠ W at an endpoint), θ-changes, w-changes.
Usage: xcount.py game.pg [start]   (prints the phases with >= 4 transitions)"""
import sys
from fbre import *

def phases_x(g, start=None):
    rows, ph = profile(g, start); o = odd_choice(g); out = []
    for r in rows: r["R"] = reach_o(g, r["s"], r["t"], o); r["other"] = (not all(r["h"])) and r["Xk"] != r["Wk"]
    for (x, y) in ph:
        X = sum(rows[k]["R"] != rows[k + 1]["R"] for k in range(x, y))
        ent = sum(len(rows[k + 1]["R"] - rows[k]["R"]) for k in range(x, y)); lv = sum(len(rows[k]["R"] - rows[k + 1]["R"]) for k in range(x, y))
        O = sum(rows[k]["other"] or rows[k + 1]["other"] for k in range(x, y))
        tc = sum(rows[k]["th"] != rows[k + 1]["th"] for k in range(x, y)); wc = sum(rows[k]["w"] != rows[k + 1]["w"] for k in range(x, y))
        out.append(dict(phase=(x, y), it=y - x, X=X, entries=ent, leaves=lv, O=O, tc=tc, wc=wc))
    return out

if __name__ == "__main__":
    g = load(sys.argv[1])
    for p in phases_x(g, readstart(sys.argv[2]) if len(sys.argv) > 2 else None):
        if p["it"] >= 4: print(os.path.basename(sys.argv[1]), "n", g.n, p)
