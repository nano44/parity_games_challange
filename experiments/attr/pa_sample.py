#!/usr/bin/env python3
"""PA-only sampler (the PD predicate of hypotheses.py is slow at n >= 5): random canonical games with n vertices,
counts of PA against psolQ/psolB outcomes. Usage: pa_sample.py n K seed"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1lib, pg, hypotheses
n, K, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
rnd = random.Random(seed)
pats = list(a1lib.priority_patterns(n))
succsets = [list(s) for r in range(1, n + 1) for s in __import__("itertools").combinations(range(n), r)]
c = {}
for i in range(K):
    g = pg.Game(rnd.choice(pats), [rnd.randint(0, 1) for _ in range(n)], [rnd.choice(succsets) for _ in range(n)])
    r = a1lib.classify(g, others=True)
    WE = [v for v in range(n) if r["ref"][v] == 0]; WO = [v for v in range(n) if r["ref"][v] == 1]
    P = max(g.prio); dE = P if P % 2 == 0 else P + 1; dO = P if P % 2 == 1 else P + 1
    pa = hypotheses.closed_decomposition(g, WE, dE, 0, "A") and hypotheses.closed_decomposition(g, WO, dO, 1, "A")
    k = (pa, r["psolq"], r["psolb"]); c[k] = c.get(k, 0) + 1
    if pa and (r["psolq"] != "solved" or r["psolb"] != "solved"):
        print("COUNTEREXAMPLE", pg.dumps(g).replace("\n", " | "), r["psolq"], r["psolb"], flush=True)
print(f"n={n} K={K} seed={seed}:", dict(sorted(c.items())))
