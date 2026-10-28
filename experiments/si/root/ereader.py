#!/usr/bin/env python3
"""L-SI box 23 (successor 19): DATA for docs/si/N5-ALT-box23.md §10-§11 (Even READERS against SW-LIN / SW-RUN). Appends an Even vertex e
(index n, priority 0, no predecessors) with edges to S inside one class, start SIGMA0 e:Y, runs N5 on base and base + e, checks that the run on
the old vertices is unchanged (SAME: sigma, tau, sigma-bar, fallback flags), and counts e's switches per phase and per fallback-free run.
--search K STEPS SEED: local search over S (subsets of the class of the longest phase; Y = the Xi-best of S at the phase start) maximising e's
switches in one phase subject to SAME.
Usage: ereader.py BASE.pg BASE.start S1,S2,.. Y | ereader.py BASE.pg BASE.start --search K STEPS SEED"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from common import rows, phases, load, readstart
import n5x; pg = n5x.pg
g0 = load(sys.argv[1]); st0 = readstart(sys.argv[2]); n0 = g0.n
E0, R0 = rows(g0, st0)

def build(S, y):
    prio = list(g0.prio) + [0]; owner = list(g0.owner) + [0]; succ = [list(x) for x in g0.succ] + [sorted(S)]
    g = pg.Game(prio, owner, succ); s0, t0 = dict(st0[0]), dict(st0[1]); s0[n0] = y
    return g, (s0, t0)

def test(S, y):
    g, st = build(S, y); E, R = rows(g, st)
    if len(R) != len(R0): return False, None, g, st
    for k in range(len(R0)):
        if R[k]["s"][:n0] != R0[k]["s"] or [R[k]["t"][v] for v in range(n0) if g0.owner[v]] != [R0[k]["t"][v] for v in range(n0) if g0.owner[v]] \
           or R[k]["fb"] != R0[k]["fb"] or [R[k]["sb"][v] for v in range(n0) if g0.owner[v]] != [R0[k]["sb"][v] for v in range(n0) if g0.owner[v]]:
            return False, None, g, st
    best = (0, 0, (0, 0))
    for i, j in phases(R):
        c = sum(R[k]["s"][n0] != R[k + 1]["s"][n0] for k in range(i, j)); s = i; rmax = 0
        for k in range(i, j + 1):
            if k == j or R[k]["fb"]:
                rmax = max(rmax, sum(R[m]["s"][n0] != R[m + 1]["s"][n0] for m in range(s, k))); s = k + 1
        best = max(best, (c, rmax, (i, j)))
    return True, best, g, st

if sys.argv[3] == "--search":
    K, steps, seed = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]); rng = random.Random(seed)
    i, j = max(phases(R0), key=lambda p: p[1] - p[0]); c = R0[i]["vs"][0][0]
    U = [v for v in range(n0) if R0[i]["vs"][v][0] == c]
    yb = lambda S: max(S, key=lambda v: (E0.key(R0[i]["vs"][v]), v))
    S = set(rng.sample(U, min(K, len(U)))); ok, cur, _, _ = test(S, yb(S)); cur = cur if ok else (0, 0, (0, 0))
    for it in range(steps):
        S2 = S ^ {rng.choice(U)}
        if not S2: continue
        ok, sc, _, _ = test(S2, yb(S2))
        if ok and sc[0] >= cur[0]:
            if sc[0] > cur[0]: print("step", it, "switches", sc, "S", ",".join(map(str, sorted(S2))), "Y", yb(S2), flush=True)
            S, cur = S2, sc
    print("final", cur, "S", ",".join(map(str, sorted(S))), "Y", yb(S), "n", n0 + 1)
else:
    S = [int(x) for x in sys.argv[3].split(",")]; ok, sc, g, st = test(S, int(sys.argv[4]))
    print("SAME" if ok else "DIFFERENT", "reader switches (max per phase, max per fallback-free run, phase)", sc, "n", n0 + 1)
