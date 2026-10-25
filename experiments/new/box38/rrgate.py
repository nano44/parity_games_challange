#!/usr/bin/env python3
"""Box 38 (c): R -> R̄ gates at HN fallback states (H1 ∧ ¬H2, in-phase Even fallback k -> k+1), by τ(o) = o / ≠ o and case
(A: rank(o) > rank(c_θ); B otherwise). Per gate (v, z): lev(Ξ(σ v), Ξ(z)) and whether z's route passes v. Also counts the same at
post-fallback states of a θ-constant run (as inva.py). One Odd choice vertex asserted. Usage: rrgate.py game.pg ... | --rand N lo hi seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); B37 = os.path.join(HERE, "..", "box37")
sys.path.insert(0, B37); sys.path.insert(0, os.path.join(HERE, "..", "..", "si", "coarse"))
from outsn import *
from mono import lev

def run(g, acc, name):
    assert sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1
    rows, o = rows_w(g); N = len(rows); H2 = [h2(r["nxt"], o) for r in rows]; E = Engine(g); ro = E.rank[o]
    for t in range(N - 1):
        r = rows[t]
        if not (r["h1"] and not H2[t] and r["fb"] and rows[t + 1]["ph"] == r["ph"]): continue
        Xi = r["Xi"]; s = r["s"]; too = r["nxt"][o] == o
        case = "A" if ro > E.rank[Xi[o][0]] else "B"; key = f"{case}_tauo{'=o' if too else '!=o'}"
        bump(acc, key + "_fb_states"); Rb = set(r["R"]) | {o}; cnt = 0
        for y, z in E.improving(tuple(s), Xi):
            if y in Rb and z in Rb:
                cnt += 1; L = lev(Xi[s[y]], Xi[z]); bump(acc, key + f"_RRgate_lev{'-1' if L == -1 else ('<ro' if L < ro else '>=ro')}")
                mx(acc, "ex_" + key + "_RRgate", 1, g.n, name, t, y, z, L)
        if cnt: bump(acc, key + "_fb_states_with_RRgate")

if __name__ == "__main__":
    acc = {}; a = sys.argv[1:]
    if a and a[0] == "--rand":
        Nn, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for d in range(Nn):
            g = rand_c1o(rng, lo, hi)
            if g is not None: run(g, acc, f"rand{seed}_{d}")
    else:
        for f in a:
            g = load(f)
            if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: bump(acc, "skipped_not_C1O"); continue
            run(g, acc, f)
    for key in sorted(acc): print(key, acc[key])
