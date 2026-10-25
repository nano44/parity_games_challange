#!/usr/bin/env python3
"""L-SI box 8: DATA for Lemma EQ-STRETCH (docs/si/N5-C-box8.md §10). Inside a joint λ-phase on 𝒞^1O, an EQ run is a maximal run of
consecutive states with Ξ = W pointwise. Checks: transitions inside an EQ run < n + m (R17 (c) transfer); every transition inside an
EQ run equals one step of N5 on the one-player game G_τ from the same σ (recomputed with experiments/new/n5.py on G_τ). Counts EQ
runs per phase against 1 + #w-changes + #transitions with (h) failing at an endpoint. Usage: eqrun.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cls2 import *
from collections import Counter

def scan_e(g, name):
    E, out = states(g); n = g.n; m = sum(len(set(s)) for s in g.succ); o = odd_choice(g); assert o is not None, name
    Ed = n5.Engine(n5.dual(g)); C = Counter()
    for a in out:
        a["key"] = (tuple(x[0] for x in a["Xi"]), a["t"], tuple(x[0] for x in Ed.evaluate(tuple(a["t"]))[0]))
        _, W = wvals(g, a["s"], a["t"]); a["eq"] = all(tuple(a["Xi"][v]) == tuple(W[v]) for v in range(n)); a["W"] = W
        a["h"] = (not oncycle(g, a["s"], a["sb"], o)) and (not oncycle(g, a["s"], a["t"], o)) and a["Xi"][o][0] == W[o][0]
    j = 0
    while j < len(out) - 1:
        k = j
        while k + 1 < len(out) and out[k + 1]["key"] == out[j]["key"]: k += 1
        runs = 0; i = j; wch = sum(out[x]["W"][o] != out[x + 1]["W"][o] for x in range(j, k)); nh = sum(not (out[x]["h"] and out[x + 1]["h"]) for x in range(j, k))
        while i <= k:
            if not out[i]["eq"]: i += 1; continue
            r = i
            while r + 1 <= k and out[r + 1]["eq"]: r += 1
            runs += 1; C["eq_tr"] += r - i; C["max_eq_run"] = max(C["max_eq_run"], r - i)
            if r - i >= n + m: C["len_viol"] += 1
            # step equality with N5 on G_τ
            gt = pg.Game(list(g.prio), list(g.owner), [[out[i]["t"][v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)])
            st = ({v: out[i]["s"][v] for v in range(n) if g.owner[v] == 0}, {v: out[i]["t"][v] for v in range(n) if g.owner[v] == 1})
            _, o2 = states(gt, st)
            for q in range(i, r):
                C["step_chk"] += 1
                if q - i + 1 >= len(o2) or tuple(o2[q - i + 1]["s"]) != tuple(out[q + 1]["s"]): C["step_viol"] += 1
            i = r + 1
        C["phases"] += 1; C["eq_runs"] += runs
        if runs > 1 + wch + nh: C["runs_viol"] += 1
        j = k + 1
    return C

if __name__ == "__main__":
    T = Counter()
    for p in sys.argv[1:]:
        c = scan_e(load(p), os.path.basename(p))
        for kk, v in c.items(): T[kk] = max(T[kk], v) if kk.startswith("max") else T[kk] + v
    print("TOTAL", dict(T))
