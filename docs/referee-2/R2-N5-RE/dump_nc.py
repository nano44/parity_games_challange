#!/usr/bin/env python3
"""Reproduce one (NC)-failing leave from re_check.py's random stream and print it (game, states, values at L, L+1)."""
import sys, random
import re_check as rc
seed, idx = int(sys.argv[1]), int(sys.argv[2]); nmin, nmax = int(sys.argv[3]), int(sys.argv[4])
rng = random.Random(seed)
for i in range(idx + 1):
    g, o = rc.rand_game(rng, rng.randint(nmin, nmax)); s, t = rc.rand_start(rng, g)
    states, fbs = rc.n5_own(g, o, s, t, rng)
print("parity %d;" % (g.n - 1))
for v in range(g.n): print("%d %d %d %s;" % (v, g.prio[v], g.owner[v], ",".join(map(str, g.succ[v]))))
print("o =", o, "ranks", g.rank)
for k, (sg, tu) in enumerate(states):
    S = rc.analyse(g, o, sg, tu)
    print(f"k={k} f={S.f} sbar(o)={S.sbar} h={S.h} R={sorted(S.R)} theta={S.theta} w={S.w} fb={fbs[k] if k < len(fbs) else '-'}")
    for v in range(g.n): print(f"   v={v} Xi={tuple(S.Xi[v][:1]) + (sorted(S.Xi[v][1]), S.Xi[v][2])} W={tuple(S.W[v][:1]) + (sorted(S.W[v][1]), S.W[v][2])} lamU={S.lamU[v]}")
