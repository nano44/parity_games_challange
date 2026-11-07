#!/usr/bin/env python3
"""L-RED R177: climb abs177's idealised dynamics with W = ladder (laddergen), restarts. Usage: climbl.py d iters restarts seed"""
import sys, os, random, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import abs177 as A
d, iters, rs, seed = (int(a) for a in sys.argv[1:5]); rng = random.Random(seed); gbest, gbs = None, -1
for r in range(rs):
    best = A.laddergen(d, rng)
    if os.environ.get("BPER"):
        best["bper"] = True; br = list(range(4 * d)); rng.shuffle(br); best["brank"] = br; best["bpar"] = [rng.randint(0, 1) for _ in br]
    bs = A.score(best)
    for it in range(iters):
        c = A.mutate(best, rng, 2)
        c["opts"] = [[[best["opts"][i][k][0], c["opts"][i][k][1]] for k in range(2)] for i in range(len(c["opts"]))]  # keep W ladder
        cs = A.score(c)
        if cs >= bs: best, bs = c, cs
    print("RESTART", r, "FL", bs, flush=True)
    if bs > gbs: gbest, gbs = best, bs; json.dump(gbest, open(os.environ.get("OUT", "/dev/null"), "w"))
print("BEST", d, gbs)
