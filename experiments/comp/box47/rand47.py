#!/usr/bin/env python3
"""L-COMP box 47: a random Ξ-acyclic genome with w movers per level, d levels, degree D (seeds for the min-d ladder lanes): W-targets uniform
one level down; Ξ-targets: a mover earlier in a random order of all movers (prob. 0.8) or X; gate order, β ranks uniform permutations; β
parity and start uniform. Usage: rand47.py W D DEG SEED out.json"""
import sys, json, random
w, d, D, seed = map(int, sys.argv[1:5]); rng = random.Random(seed); N = w * d; lev = [x // w for x in range(N)]; M = N * D
perm = list(range(N)); rng.shuffle(perm); pos = {x: p for p, x in enumerate(perm)}; opts = []; i = 0
for x in range(N):
    oo = []
    for _ in range(D):
        wt = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1
        lower = [y for y in range(N) if pos[y] < pos[x]]
        oo.append([wt, rng.choice(lower) if lower and rng.random() < 0.8 else -1, i]); i += 1
    opts.append(oo)
g = list(range(M)); rng.shuffle(g); br = list(range(M)); rng.shuffle(br)
G = dict(N=N, lev=lev, opts=opts, gate=[[g[x * D + k] for k in range(D)] for x in range(N)], br=br, bp=[rng.randrange(2) for _ in range(M)], start=[rng.randrange(D) for _ in range(N)])
json.dump(G, open(sys.argv[5], "w"), sort_keys=True)
