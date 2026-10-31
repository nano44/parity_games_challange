#!/usr/bin/env python3
"""L-RED R147: srcsettle.check on random games with random starts. Sums the counters; writes the first violating game.
Usage: srcrand.py SEED GAMES NMIN NMAX"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import xcn, srcsettle
pg = xcn.pg
seed, G, a, b = map(int, sys.argv[1:5]); rng = random.Random(seed); tot = {}; bad = None
for i in range(G):
    n = rng.randint(a, b); pr = rng.sample(range(2 * n + 2), n); ow = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), rng.randint(1, 3)))) for _ in range(n)]
    g = pg.Game(pr, ow, succ)
    s0 = [rng.choice(succ[v]) if ow[v] == 0 else -1 for v in range(n)]; t0 = [rng.choice(succ[v]) if ow[v] == 1 else -1 for v in range(n)]
    try: tr, fb = xcn.trace(g, s0, t0, cap=400)
    except Exception: continue
    r = srcsettle.check(g, tr, fb)
    for k, v in r.items(): tot[k] = max(tot.get(k, 0), v) if k.startswith("max") else tot.get(k, 0) + v
    if bad is None and (r["VIOL"] or r["VIOL2"] or r["TAILV"] or r["BLKV"] or r["CNOX"]):
        bad = i; pg.write(g, f"/tmp/claude-0/srcbad_{seed}_{i}.pg")
        with open(f"/tmp/claude-0/srcbad_{seed}_{i}.start", "w") as f:
            f.write("SIGMA0 " + " ".join(f"{v}:{s0[v]}" for v in range(n) if ow[v] == 0) + "\nTAU0 " + " ".join(f"{v}:{t0[v]}" for v in range(n) if ow[v] == 1) + "\n")
print(f"SRCRAND seed {seed} games {G} n {a}-{b} " + " ".join(f"{k} {v}" for k, v in tot.items()) + f" firstbad {bad}")
