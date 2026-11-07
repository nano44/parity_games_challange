#!/usr/bin/env python3
"""L-RED R177 BIDIR: abstract model, W-ladder with Xi-faces pointing one level UP (option k: W -> vertex (k xor wflip) of level l-1,
Xi -> vertex (k xor xflip) of level l+1; top level Xi -> X). Topology fixed; climb over gates (perm), beta ranks / parities
(per option), start, and the flips. Usage: bidir.py d iters restarts seed"""
import sys, os, random, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import abs177 as A
def gen(d, rng, xfl):
    N = 2 * d; levels = [1 + i // 2 for i in range(N)]; opts = []
    for i in range(N):
        l = levels[i]; o = []
        for k in range(2):
            wt = "W" if l == 1 else 2 * (l - 2) + k
            xt = "X" if l == d else 2 * l + (k ^ xfl[i])
            o.append([wt, xt])
        opts.append(o)
    return opts
d, iters, rs, seed = (int(a) for a in sys.argv[1:5]); rng = random.Random(seed); gb, gbs = None, -1
for r in range(rs):
    xfl = [rng.randint(0, 1) for _ in range(2 * d)]
    g = A.laddergen(d, rng); g["opts"] = gen(d, rng, xfl); g["bper"] = True
    br = list(range(4 * d)); rng.shuffle(br); g["brank"] = br; g["bpar"] = [rng.randint(0, 1) for _ in br]; g["xfl"] = xfl
    bs = A.score(g)
    for it in range(iters):
        c = A.mutate(g, rng, 2)
        if rng.random() < 0.15:
            i = rng.randrange(2 * d); c["xfl"][i] ^= 1
        c["opts"] = gen(d, rng, c["xfl"])
        cs = A.score(c)
        if cs >= bs: g, bs = c, cs
    print("RESTART", r, "FL", bs, flush=True)
    if bs > gbs: gb, gbs = g, bs; json.dump(gb, open(os.environ.get("OUT", "/dev/null"), "w"))
print("BIDIR BEST", d, gbs)
