#!/usr/bin/env python3
"""L-COMP box 47: a random UPWARD LADDER (Lead 12:12Z, L-SI 55's class) of depth d: movers 2l, 2l + 1 at level l, two options each with
W-targets 2l − 2 and 2l − 1 (random order; X at level 0); Ξ-target a uniform mover of a strictly higher level or X (prob 1 / (#higher + 1));
β ranks 4l .. 4l + 3 on level l (random within the level), β parity uniform; gate order uniform; start uniform; no eperm (ε = gate).
Usage: up47.py D SEED out.json"""
import sys, json, random
d, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); N = 2 * d; lev = [x // 2 for x in range(N)]; M = 2 * N
opts = []; br = [0] * M; i = 0
for x in range(N):
    l = lev[x]; w = [2 * l - 2, 2 * l - 1] if l else [-1, -1]; rng.shuffle(w); oo = []
    for k in range(2):
        hi = [y for y in range(N) if lev[y] > l]; xt = rng.choice(hi + [-1]) if hi else -1
        oo.append([w[k], xt, i]); i += 1
    opts.append(oo)
for l in range(d):
    r = list(range(4 * l, 4 * l + 4)); rng.shuffle(r)
    for j, b in enumerate(range(4 * l, 4 * l + 4)): br[b] = r[j]
g = list(range(M)); rng.shuffle(g)
G = dict(N=N, lev=lev, opts=opts, gate=[[g[2 * x], g[2 * x + 1]] for x in range(N)], br=br, bp=[rng.randrange(2) for _ in range(M)], start=[rng.randrange(2) for _ in range(N)])
json.dump(G, open(sys.argv[3], "w"), sort_keys=True)
