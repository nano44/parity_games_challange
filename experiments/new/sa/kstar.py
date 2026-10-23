#!/usr/bin/env python3
"""k* of the gap queries listed in a gaps.py output file (random games): least k with SA_k infeasible, k up to KMAX."""
import os, sys, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
import gen
from gaps import queries
from sa import sa_feasible, acyc
src, kmax = sys.argv[1], int(sys.argv[2])
nmin, nmax = int(sys.argv[3]), int(sys.argv[4])
done = set()
for line in open(src):
    if not line.startswith("GAP"):
        continue
    _, _, name, q, _ = line.split()
    seed = int(name[1:]); rnd = random.Random(seed); n = rnd.randint(nmin, nmax)
    g = gen.random_game(n, rnd.randint(2, n + 1), 1, min(3, n), seed)
    h = dict((a, b) for a, b, c in queries(g))[q]
    res = []
    for k in range(1, kmax + 1):
        t = time.time(); f = sa_feasible(h, k); res.append(f"{k}:{'F' if f else 'I'}({time.time()-t:.0f}s)")
        if not f:
            break
    print(f"{name} {q} n={h.n} varedges={len(acyc(h)[0])} " + " ".join(res), flush=True)
