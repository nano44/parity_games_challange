#!/usr/bin/env python3
"""L-NEW box 144: hill-climb U = unchained steps t >= 2 (chain.py ALL form) on 2-wide deg-2 IDEAL-ACYC ladders (box143/dclimb.py genomes and
mutations; UP=1 for strictly upward Xi-targets). Ties broken by steps. Usage: uclimb.py d iters seed out.json"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "box143", "dclimb.py")).read().split("def score(G):")[0]
ns = {"__file__": os.path.join(HERE, "..", "box143", "dclimb.py")}; exec(src, ns); rand, mut = ns["rand"], ns["mut"]
src2 = open(os.path.join(HERE, "chain.py")).read().split('\nif __name__ == "__main__":')[0]
ns2 = {"__file__": os.path.join(HERE, "chain.py")}; exec(src2, ns2); analyse = ns2["analyse"]
def score(G):
    r = analyse(G); return (r["au"], r["T"])
if __name__ == "__main__":
    d, iters, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed); random.seed(seed)
    G = rand(d, rng); bs = score(G); best = (bs, G)
    for it in range(iters):
        H = mut(G, rng); hs = score(H)
        if hs >= bs:
            G, bs = H, hs
            if bs > best[0]: best = (bs, G); print("IT", it, "UNCHAINED_ALL", bs[0], "STEPS", bs[1], flush=True); json.dump(G, open(out, "w"))
        if it % 4000 == 3999 and bs < best[0]: G, bs = json.loads(json.dumps(best[1])), best[0]
    print("BEST UNCHAINED_ALL", best[0][0], "STEPS", best[0][1], flush=True)
