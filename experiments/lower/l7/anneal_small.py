#!/usr/bin/env python3
"""L-LOWER 7 (BOX L7) §7: simulated annealing over whole genomes of a small d (wiring acyclic, ranks, signs, gates, start), score =
(leading capped levels, F of the next level), to measure how many levels d an h-capped tower needs. Usage: anneal_small.py d steps seed"""
import sys, os, random, math
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, '..', 'l6'))
from sim6 import run, Fprof, caps, topo, wr
d, steps, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); N = 2 * d
def sc(D):
    if topo(D) is None: return None
    S, O = run(D, cap=4000); F = Fprof(D, O); h = caps(F); return h * 1000 + (F[h] if h < d else 0), F
D = {'d': d, 'xt': [-1] * (2 * N), 'br': rng.sample(range(2 * N), 2 * N), 'bp': [rng.randrange(2) for _ in range(2 * N)],
     'gate': [0, 2, 1, 3] + [v for l in range(1, d) for v in (4 * l, 4 * l + 2, 4 * l + 1, 4 * l + 3)], 'start': [1, 1] + [rng.randrange(2) for _ in range(N - 2)]}
cur = sc(D); best = (cur[0], cur[1], {k: list(v) if isinstance(v, list) else v for k, v in D.items()}); temp = 30.0
for it in range(steps):
    E = {k: list(v) if isinstance(v, list) else v for k, v in D.items()}; r = rng.random()
    if r < 0.4: m = rng.randrange(2 * N); E['xt'][m] = rng.randrange(-1, N)
    elif r < 0.7: i, j = rng.sample(range(2 * N), 2); E['br'][i], E['br'][j] = E['br'][j], E['br'][i]
    elif r < 0.85: m = rng.randrange(2 * N); E['bp'][m] ^= 1
    elif r < 0.95: l = rng.randrange(1, d); g = E['gate'][4 * l:4 * l + 4]; rng.shuffle(g); E['gate'][4 * l:4 * l + 4] = g
    else: x = rng.randrange(2, N); E['start'][x] ^= 1
    if any(E['xt'][m] == m // 2 for m in range(2 * N)): continue
    ns = sc(E)
    if ns is None: continue
    if ns[0] >= cur[0] or rng.random() < math.exp((ns[0] - cur[0]) / temp): D, cur = E, ns
    if cur[0] > best[0]: best = (cur[0], cur[1], {k: list(v) if isinstance(v, list) else v for k, v in D.items()})
    temp = max(0.5, temp * 0.9997)
print('d', d, 'seed', seed, 'best caps', best[0] // 1000, 'F', best[1])
wr(best[2], os.path.join(H, 'out', 'anneal_d%d_s%d.txt' % (d, seed)))
