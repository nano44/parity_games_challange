#!/usr/bin/env python3
"""Box 37 (b): candidate invariant SEP (docs/new/N5-OUT-box37.md §7). At HN states t after a fallback of the current θ-constant run
(and at the fallback states themselves), check for every Even y ∈ F_t ∩ U and every z ∈ R̄_t: Ξ_t(z) ⊴ Ξ_t(σ_t y) (U := λ^{-1}(c_θ)).
Also the weaker SEP-θ: θ_t ⊴ Ξ_t(σ_t y) for those y. Counts states checked and failures. Usage: sep.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from outsn import *

def run(g, acc, name):
    assert sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1
    rows, o = rows_w(g); N = len(rows); H2 = [h2(r["nxt"], o) for r in rows]; E = Engine(g); seen = False
    for t in range(N):
        a = rows[t]
        if t and (rows[t - 1]["ph"] != a["ph"] or rows[t - 1]["th"] != a["th"] or not rows[t - 1]["h1"] or H2[t - 1]): seen = False
        if not a["h1"] or H2[t]: seen = False; continue
        if a["fb"]: seen = True
        if not seen: continue
        Xi = a["Xi"]; ct = Xi[o][0]; Rb = set(a["R"]) | {o}
        Fy = [y for y in range(g.n) if g.owner[y] == 0 and y not in Rb and Xi[y][0] == ct]
        if not Fy: continue
        lo = min(E.key(Xi[a["s"][y]]) for y in Fy); hi = max(E.key(Xi[z]) for z in Rb)
        bump(acc, "states"); 
        if hi > lo: bump(acc, "SEP_fail"); mx(acc, "ex_SEP_fail", 1, g.n, name, t)
        if E.key(Xi[o]) > lo: bump(acc, "SEPtheta_fail"); mx(acc, "ex_SEPtheta_fail", 1, g.n, name, t)

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        g = load(f)
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
        run(g, acc, f)
    for key in sorted(acc): print(key, acc[key])
