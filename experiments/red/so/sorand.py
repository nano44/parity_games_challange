#!/usr/bin/env python3
"""Box 36 (L-RED): sox.analyse on random 𝒞^1O games (one Odd vertex o with out-degree > 1, o's out-degree n//4..n//2).
Usage: sorand.py count nmin nmax seed  -> failure totals and maxima"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import sox, pg
cnt, a, b, seed = map(int, sys.argv[1:5]); rng = random.Random(seed); tot = {}; mx = {}; ph = 0
for i in range(cnt):
    n = rng.randint(a, b); prio = [rng.randrange(n) for _ in range(n)]; owner = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), 1 if owner[v] else rng.choice((1, 2, 2, 3))))) for v in range(n)]
    o = rng.randrange(n); owner[o] = 1; succ[o] = sorted(rng.sample(range(n), rng.randint(max(2, n // 4), max(2, n // 2))))
    r = sox.analyse(pg.Game(prio, owner, succ)); ph += len(r["rows"])
    for k, v in r["C"].items(): tot[k] = tot.get(k, 0) + v
    for x in r["rows"]:
        for k in ("Th", "So", "X", "J", "K", "maxrun", "nruns2"): mx[k] = max(mx.get(k, 0), x[k])
print("games", cnt, "phases", ph, "FAILS", tot or 0, "max", mx)
