#!/usr/bin/env python3
"""L-RED R187 CLIMB: hill climb in the DOWN class on the IDEAL simulator (= the real STAB+K run, t2.py). SCORE=T (run length) or
SCORE=top (moves at the top level) or SCORE=d2 (sum of D2). Accepts >=. Writes the best genome to OUT.json at every improvement.
Usage: climb.py d W deg iters seed OUT"""
import sys, os, json, random
sys.path[:0] = [os.path.dirname(os.path.abspath(__file__))]
import downgen, ideal, rel
RG, MU = (downgen.randacyc, downgen.mutacyc) if os.environ.get("CLASS") == "acyc" else (downgen.randdown, downgen.mutdown)
d, W, deg, iters, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
SC = os.environ.get("SCORE", "T")
def score(G):
    S, why = ideal.traj(G, cap=5000); st = rel.stats(G, S)
    return (st["T"] if SC == "T" else st["M"][-1] if SC == "top" else sum(st["D2"]) * 1000 + st["T"]), st
rng = random.Random(seed); best = None
for r in range(5):
    G = RG(d, deg, rng, W); s, st = score(G)
    for i in range(iters // 5):
        H = MU(G, rng); t, sh = score(H)
        if t >= s:
            if t > s: print("restart", r, "it", i, "score", t, sh, flush=True)
            G, s, st = H, t, sh
    if best is None or s > best[0]:
        best = (s, G, st); json.dump(G, open(out, "w"))
print("BEST", best[0], best[2])
