#!/usr/bin/env python3
"""REFEREE-2 32: own Ξ-acyclic genome generator (wider than lemma81.agen): d 1-8, w 1-4, degree 2-4, pX in {0.05, 0.2, 0.5}, Ξ-targets
to movers earlier in a random topological order (any level), W-targets one level down; distinct gate indices drawn from a sparse range
(as in the tower files), distinct β-ranks, random parities and starts. Usage: r2gen.py COUNT SEED > SET.jsonl"""
import sys, random, json
cnt, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed)
for _ in range(cnt):
    d, w, D, pX = rng.randint(1, 8), rng.randint(1, 4), rng.randint(2, 4), rng.choice([0.05, 0.2, 0.5])
    N = d * w; lev = [v // w for v in range(N)]; order = list(range(N)); rng.shuffle(order); pos = {x: i for i, x in enumerate(order)}
    opts = []; M = 0
    for v in range(N):
        o = []
        for k in range(rng.randint(2, D)):
            wt = rng.choice([y for y in range(N) if lev[y] == lev[v] - 1]) if lev[v] else -1
            cand = [y for y in range(N) if pos[y] < pos[v]]
            xt = -1 if (not cand or rng.random() < pX) else rng.choice(cand)
            o.append([wt, xt, M]); M += 1
        opts.append(o)
    br = list(range(M)); rng.shuffle(br); bp = [rng.randrange(2) for _ in range(M)]
    gidx = rng.sample(range(5 * M + 10), M); it = iter(gidx); gate = [[next(it) for _ in o] for o in opts]
    print(json.dumps(dict(N=N, lev=lev, opts=opts, gate=gate, br=br, bp=bp, start=[rng.randrange(len(o)) for o in opts])))
