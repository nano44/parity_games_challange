#!/usr/bin/env python3
"""L-RED R188 MIDCLIMB (L-NEW box 140 score): ACYC genomes (W 2, deg 2; r187 downgen.randacyc / mutacyc), score = moves at the middle
level floor(d / 2) (ties: run length). 10 restarts. Usage: midclimb.py d iters seed OUT"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal, rel, downgen
d, iters, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed); mid = d // 2
def score(G):
    S, _ = ideal.traj(G, cap=3000); st = rel.stats(G, S); return (st["M"][mid], st["T"])
best = None
for r in range(10):
    G = downgen.randacyc(d, 2, rng); s = score(G)
    for it in range(iters // 10):
        H_ = downgen.mutacyc(G, rng); t = score(H_)
        if t >= s: G, s = H_, t
    if best is None or s > best[0]: best = (s, G); json.dump(G, open(out, "w"))
S, _ = ideal.traj(best[1]); print("MID d", d, "level", mid, "BEST", best[0], rel.stats(best[1], S))
