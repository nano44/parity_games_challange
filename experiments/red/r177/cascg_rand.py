#!/usr/bin/env python3
"""L-RED R177: CASC-G on random abstract instances whose Xi-targets lie at strictly lower W-level (or X), so D is acyclic.
Writes each genome to a temp file and runs dcheck. Usage: cascg_rand.py trials seed"""
import sys, os, random, json, subprocess, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import abs177 as A, dcheck
T, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); tmp = tempfile.mkdtemp()
for t in range(T):
    N = rng.randint(4, 12); L = rng.randint(2, max(2, N // 2)); deg = rng.randint(2, 3)
    g = A.randgen(N, L, deg, rng)
    for i in range(N):
        low = [j for j in range(N) if g["levels"][j] < g["levels"][i]]
        g["opts"][i] = [[wt, rng.choice(["X"] + low)] for wt, xt in g["opts"][i]]
    if rng.random() < 0.5:
        g["bper"] = True; M = sum(len(o) for o in g["opts"]); br = list(range(M)); rng.shuffle(br); g["brank"] = br
        g["bpar"] = [rng.randint(0, 1) for _ in br]
    p = os.path.join(tmp, f"g{t}.json"); json.dump(g, open(p, "w")); dcheck.main(p)
