#!/usr/bin/env python3
"""Box 37 (b): checks Theorem NO-ENTRY-A's invariant (docs/new/N5-OUT-box37.md §9). In a phase with τ(o) = o, at HN states t of a
θ-constant run from a fallback state a on (a included): CASE = A if rank(o) > rank(c_θ) else B. Checks (i) no gate F_t -> R̄_t;
(ii) every gate R_t -> R̄_t has lev < rank(o); (iii) for z ∈ R̄_t, Ξ_t(z) agrees with Ξ_a(z) above rank(o) (z ∈ R̄_a, by SPLIT and (i)).
Counts failures per case. One Odd choice vertex asserted. Usage: inva.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "si", "coarse"))
from outsn import *
from mono import lev

def run(g, acc, name):
    assert sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1
    rows, o = rows_w(g); N = len(rows); H2 = [h2(r["nxt"], o) for r in rows]; E = Engine(g); ro = E.rank[o]; base = None
    for t in range(N):
        r = rows[t]; Xi = r["Xi"]; s = r["s"]
        ok = r["h1"] and not H2[t] and r["nxt"][o] == o
        if base is not None and (not ok or rows[base]["ph"] != r["ph"] or rows[base]["th"] != r["th"]): base = None
        if not ok: continue
        if base is None and r["fb"]: base = t
        if base is None: continue
        case = "A" if ro > E.rank[Xi[o][0]] else "B"; bump(acc, case + "_states")
        Rb = set(r["R"]) | {o}
        for y, z in E.improving(tuple(s), Xi):
            if z in Rb and y not in Rb: bump(acc, case + "_FAIL_i"); mx(acc, "ex_" + case + "_i", 1, g.n, name, t)
            if z in Rb and y in Rb and lev(Xi[s[y]], Xi[z]) >= ro: bump(acc, case + "_FAIL_ii"); mx(acc, "ex_" + case + "_ii", 1, g.n, name, t)
        Xa = rows[base]["Xi"]
        for z in Rb:
            if lev(Xa[z], Xi[z]) >= ro: bump(acc, case + "_FAIL_iii"); mx(acc, "ex_" + case + "_iii", 1, g.n, name, t)
        if r["fb"] and t != base: bump(acc, case + "_later_fallbacks")

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        g = load(f)
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
        run(g, acc, f)
    for key in sorted(acc): print(key, acc[key])
