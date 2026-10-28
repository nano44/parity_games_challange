#!/usr/bin/env python3
"""REFEREE succ. 16: search for READER counterexamples on random games (own engine). For each random game and run with a fallback, append
o (index n, priority 0, Odd, no predecessors) with S = two vertices of one class at the fallback state that stay in one class on that phase,
and every choice of tau0(o) in S; count: PHASE (phases differ), RUN (sigma/tau/fb on the old vertices differ), and save the first RUN case.
Usage: reader_search.py N nmin nmax kmax seed outprefix"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D
from collections import Counter
N, lo, hi, km, seed = map(int, sys.argv[1:6]); out = sys.argv[6]
r = random.Random(seed); cnt = Counter(); saved = False
def phases(st, nn):
    cut = []; k = 0
    key = lambda q: (tuple(v[0] for v in st[q]["Xi"][:nn]), tuple(st[q]["t"]))
    while k < len(st):
        j = k
        while j + 1 < len(st) and key(j + 1) == key(k): j += 1
        cut.append((k, j)); k = j + 1
    return cut
def write(g, s0, t0, path):
    with open(path + ".pg", "w") as f:
        f.write("parity %d;\n" % (g.n - 1))
        for v in range(g.n): f.write("%d %d %d %s;\n" % (v, g.prio[v], g.owner[v], ",".join(map(str, g.succ[v]))))
    with open(path + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join("%d:%d" % (v, s0[v]) for v in range(g.n) if g.owner[v] == 0) + "\n")
        f.write("TAU0 " + " ".join("%d:%d" % (v, t0[v]) for v in range(g.n) if g.owner[v] == 1) + "\n")
for i in range(N):
    n = r.randint(lo, hi); g = D.rand_ck(r, n, r.randint(1, min(km, n - 1)))
    g = RE.Game([p + 2 for p in g.prio], g.owner, g.succ)      # priorities >= 2, so o (priority 0) ranks below every old vertex
    s0, t0 = RE.best_reward_start(g); st = RE.run(g, (s0, t0)); cnt["games"] += 1
    fbs = [k for k in range(len(st) - 1) if st[k]["fb"] and st[k]["Is"]]
    if not fbs: continue
    cnt["with_even_fallback"] += 1
    k = fbs[0]; lam = [v[0] for v in st[k]["Xi"]]
    for c in set(lam):
        U = [v for v in range(n) if lam[v] == c]
        if len(U) < 2: continue
        S = sorted(r.sample(U, 2))
        go = RE.Game(list(g.prio) + [0], list(g.owner) + [1], [list(x) for x in g.succ] + [S])
        for y in S:
            so = list(s0) + [None]; to = list(t0) + [y]
            st2 = RE.run(go, (so, to)); cnt["readers"] += 1
            run_same = len(st) == len(st2) and all(st[q]["s"] == st2[q]["s"][:n] and st[q]["t"] == st2[q]["t"][:n] and st[q]["fb"] == st2[q]["fb"] for q in range(len(st)))
            ph_same = phases(st, n) == phases(st2, n + 1)
            if not ph_same: cnt["PHASE_differs"] += 1
            if not run_same:
                cnt["RUN_differs"] += 1
                if not saved:
                    saved = True; write(g, s0, t0, out + "_base"); write(go, so, to, out + "_reader")
                    print("saved", i, "n", n, "fallback state", k, "S", S, "tau0(o)", y)
        break
for k in sorted(cnt): print(k, cnt[k])
