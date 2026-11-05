#!/usr/bin/env python3
"""L-NEW box 161, DATA: along external-flip runs (random ISO ladders, random level-0 schedules with <= K changes of b_0), record the
frozen remainders R_c(s_t) for both values c of b_0 and test candidate potentials. Prints counts.
Usage: psi.py d count seed K"""
import sys, os, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from ext import *
d, cnt, seed, K = map(int, sys.argv[1:5]); rng = random.Random(seed)
stat = dict(runs=0, maxT=0, psi_up=0, psi_up_max_per_run=0, maxexcess=-99)
for i in range(cnt):
    G = rand_iso(d, rng); g = Gen(G)
    # representative level-0 configurations for b_0 = 0 / 1
    rep = {}
    for q0 in itertools.product([0, 1], repeat=2):
        s = tuple(list(q0) + G["start"][2:]); rep.setdefault(b0(g, s), q0)
    if len(rep) < 2: continue
    # random schedule: start config, flip times
    c0 = rng.randint(0, 1); flips = sorted(rng.sample(range(1, 12), rng.randint(0, K)))
    cur = tuple(list(rep[c0]) + G["start"][2:]); c = c0; T = 0; ups = 0; t = 0
    psi = lambda s: max(frozen_R(G, g, s, list(rep[0]) + [0] * (g.N - 2)), frozen_R(G, g, s, list(rep[1]) + [0] * (g.N - 2)))
    P0 = psi(cur); prev = P0
    while t < 200:
        t += 1
        if t in flips: c = 1 - c
        q = list(rep[c]) + [0] * (g.N - 2); nw = step_forced(g, cur, q)
        if all(nw[v] == cur[v] for v in range(2, g.N)):
            if not any(f > t for f in flips): break
            cur = nw; continue
        T += 1; cur = nw; p = psi(cur)
        if p >= prev: ups += 1
        prev = p
    stat["runs"] += 1; stat["maxT"] = max(stat["maxT"], T); stat["psi_up"] += ups
    stat["psi_up_max_per_run"] = max(stat["psi_up_max_per_run"], ups); stat["maxexcess"] = max(stat["maxexcess"], T - P0)
print(stat)
