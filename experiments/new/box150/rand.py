#!/usr/bin/env python3
"""L-NEW box 150: random IDEAL-ACYC genomes in the box 139-149 JSON format (any width, degree 1..DMAX), for the P-IDEAL-RED checks.
Movers 0..N-1 with levels; W-target of option (x,k): a random mover of level lev(x)-1 (none at level 0); Xi-target: X or a random
mover later in a random topological order; distinct beta ranks with random parities; distinct gate indices; random start.
Usage: rand.py SEED COUNT OUTDIR"""
import sys, json, random, os
seed, cnt, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; os.makedirs(out, exist_ok=True); rng = random.Random(seed)
for i in range(cnt):
    d = rng.randint(1, 4); wid = rng.randint(1, 3); DMAX = rng.choice([2, 2, 3, 4])
    lev = [l for l in range(d) for _ in range(rng.randint(1, wid))]; N = len(lev)
    xorder = list(range(N)); rng.shuffle(xorder); pos = {v: j for j, v in enumerate(xorder)}
    opts, M = [], 0
    for x in range(N):
        D = rng.randint(1, DMAX) if rng.random() < 0.2 else min(2, DMAX) if DMAX == 2 else rng.randint(2, DMAX); o = []
        for k in range(D):
            lower = [v for v in range(N) if lev[v] == lev[x] - 1]; wt = rng.choice(lower) if lev[x] > 0 else -1
            later = [v for v in range(N) if pos[v] > pos[x]]; xt = rng.choice(later) if later and rng.random() < 0.75 else -1
            o.append([wt, xt, M]); M += 1
        opts.append(o)
    gates = list(range(M)); rng.shuffle(gates); it = iter(gates); gate = [[next(it) for _ in o] for o in opts]
    br = list(range(M)); rng.shuffle(br); bp = [rng.randint(0, 1) for _ in range(M)]
    start = [rng.randrange(len(o)) for o in opts]
    G = {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": start, "xorder": xorder}
    json.dump(G, open(os.path.join(out, f"r{seed}_{i:03d}.json"), "w"))
