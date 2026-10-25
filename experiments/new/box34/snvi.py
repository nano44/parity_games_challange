#!/usr/bin/env python3
"""Box 34: the SN prefix as value iteration in G_τ (docs/new/N5-REL-box34.md). For each fallback-free run of a phase, its SN prefix =
the states with c_w = c_θ (a prefix, Corollary SN-PREFIX). Inside it, with H1 (so (h), Lemma H3H2), every S4a step has the W-improving
edges of G_τ in its arena except WITHHELD ones: F -> R̄ edges (y, z) with W(z) ▷ W(σ y) that are not gates. Per SN prefix: length,
W-changing transitions on U := λ^{-1}(c_θ), crossings, steps with a withheld edge, max W-changes. Usage: snvi.py game.pg ... | --rand"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from relfr import *

def bump(acc, k, d=1): acc[k] = acc.get(k, 0) + d

def check(g, acc, name):
    rows, o = rows_w(g); E = Engine(g); n = g.n
    runs = []; cur = []
    for k in range(len(rows) - 1):
        a, b = rows[k], rows[k + 1]
        if a["ph"] != b["ph"] or a["fb"]:
            if cur: runs.append(cur); cur = []
            continue
        cur.append(k)
    if cur: runs.append(cur)
    for run in runs:
        pre = []
        for k in run:
            a = rows[k]
            if a["Xi"][o][0] != a["W"][o][0]: break
            pre.append(k)
        if not pre: continue
        c = rows[pre[0]]["Xi"][o][0]; U = [v for v in range(n) if rows[pre[0]]["Xi"][v][0] == c]
        wchg = 0; xing = 0; wh = 0; allh1 = True; thr = 0
        for k in pre:
            a, b = rows[k], rows[k + 1]
            if not a["h1"]: allh1 = False
            if any(E.key(a["W"][v]) != E.key(b["W"][v]) for v in U): wchg += 1
            if set(a["R"]) != set(b["R"]): xing += 1
            if a["th"] != a["w"]: thr += 1
            Rb = set(a["R"]) | {o}; s = tuple(a["s"]); Xi, W = a["Xi"], a["W"]
            gates = set(E.improving(s, Xi)); found = False
            for y in range(n):
                if g.owner[y] != 0 or y in Rb: continue
                for z in g.succ[y]:
                    if z in Rb and E.key(W[z]) > E.key(W[s[y]]) and (y, z) not in gates: found = True
            if found: wh += 1
        key = "H1" if allh1 else "mixH1"
        bump(acc, key + "_prefixes"); bump(acc, key + "_steps", len(pre)); bump(acc, key + "_Wchg", wchg); bump(acc, key + "_xing", xing)
        bump(acc, key + "_withheld_steps", wh); bump(acc, key + "_thr_steps", thr)
        if wh == 0: bump(acc, key + "_prefixes_nowithheld")
        if wh == 0 and wchg > len(U) - 1: bump(acc, key + "_VI_FAIL"); acc.setdefault("ex_vi", (name, pre[0], wchg, len(U)))
        if wchg > acc.get("max_Wchg", (0,))[0]: acc["max_Wchg"] = (wchg, len(U), n, wh, name, pre[0])
        if xing > acc.get("max_xing", (0,))[0]: acc["max_xing"] = (xing, wchg, len(U), n, wh, name, pre[0])

if __name__ == "__main__":
    acc = {}; a = sys.argv[1:]
    if a and a[0] == "--rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); d = 0
        while d < N:
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            check(g, acc, f"rand{seed}_{d}"); d += 1
    else:
        for f in a:
            g = load(f)
            if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
            check(g, acc, os.path.basename(f))
    for k in sorted(acc): print(k, acc[k])
