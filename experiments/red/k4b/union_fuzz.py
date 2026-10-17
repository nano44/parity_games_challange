#!/usr/bin/env python3
"""L-RED box 6 (produced on Opus 5.5): disjoint union of a gadget with small random games; reports games where the
(K4-B)/(K-first)/(K-in)/completeness checks of carry/kfuzz.py fail. Usage: union_fuzz.py GADGET.pg SEED COUNT OUTDIR [nmax] [deg]"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "carry"))
import kfuzz, pg
gad = pg.read(sys.argv[1]); seed, cnt, out = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
nmax = int(sys.argv[5]) if len(sys.argv) > 5 else 8; deg = int(sys.argv[6]) if len(sys.argv) > 6 else 3
rng = random.Random(seed); os.makedirs(out, exist_ok=True); tot = {}
for i in range(cnt):
    n = rng.randint(2, nmax); q = kfuzz.rgame(rng, n, deg, rng.randint(1, n + 3))
    k = gad.n
    g = pg.Game(gad.prio + q.prio, gad.owner + q.owner, gad.succ + [[w + k for w in s] for s in q.succ])
    for order in ("oink", "stable"):
        bad = kfuzz.check(g, order)
        for b in set(bad):
            tot[b] = tot.get(b, 0) + 1
            if b.startswith("_"): continue
            fn = os.path.join(out, f"u_{seed}_{i}_{order}_{b}.pg")
            open(fn, "w").write(pg.dumps(g))
print(tot)
