#!/usr/bin/env python3
"""L-LOWER 7 (BOX L7) §7: random small genomes (d = 2, 3, 4): how many leading capped levels occur? Random acyclic wiring (random topological order, each option's target
a later mover or exit), ranks (a random permutation), signs, gates (level 0 free permutation of 4 values; level l a random permutation of its 4),
start bits. Usage: rnd_small.py d samples seed"""
import sys, os, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, '..', 'l6'))
from sim6 import run, Fprof, caps, topo
from collections import Counter
d, n, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); N = 2 * d; c = Counter(); best = {}
for i in range(n):
    order = rng.sample(range(N), N); pos = {x: i for i, x in enumerate(order)}
    xt = [rng.choice([-1] + order[pos[m // 2] + 1:]) for m in range(2 * N)]
    D = {'d': d, 'xt': xt, 'br': rng.sample(range(2 * N), 2 * N), 'bp': [rng.randrange(2) for _ in range(2 * N)],
         'gate': [v for l in range(d) for v in rng.sample(range(4 * l, 4 * l + 4), 4)], 'start': [rng.randrange(2) for _ in range(N)]}
    if any(D['xt'][m] == m // 2 for m in range(2 * N)) or topo(D) is None: continue
    S, O = run(D, cap=5000); F = Fprof(D, O); h = caps(F); c[h] += 1
    if h not in best: best[h] = F
print('d', d, 'samples', n, 'acyclic', sum(c.values()), 'leading capped levels -> count', dict(sorted(c.items())), 'example F per h', best)
