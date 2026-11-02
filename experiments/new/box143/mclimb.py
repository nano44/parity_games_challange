#!/usr/bin/env python3
"""L-NEW box 143: hill-climb MAXMOVES_X = max moves of one mover on 2-wide deg-2 IDEAL-ACYC ladders (dclimb.py genomes and mutations;
UP=1 restricts to Xi-targets of strictly higher level). Ties broken by total moves. Usage: mclimb.py d iters seed out.json"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
src = open(os.path.join(HERE, "dclimb.py")).read().split("def score(G):")[0]
ns = {"__file__": os.path.join(HERE, "dclimb.py")}; exec(src, ns); rand, mut = ns["rand"], ns["mut"]
src2 = open(os.path.join(HERE, "..", "box139", "paths.py")).read().split("def vx(G):")[0]
ns2 = {"__file__": os.path.join(HERE, "..", "box139", "paths.py")}; exec(src2, ns2); run = ns2["run"]
def score(G):
    S = run(G, cap=5000)[0]; N = G["N"]; mv = [sum(S[t][x] != S[t - 1][x] for t in range(1, len(S))) for x in range(N)]
    return (max(mv), sum(mv))
if __name__ == "__main__":
    d, iters, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed); random.seed(seed)
    G = rand(d, rng); bs = score(G); best = (bs, G)
    for it in range(iters):
        H = mut(G, rng); hs = score(H)
        if hs >= bs:
            G, bs = H, hs
            if bs > best[0]: best = (bs, G); print("IT", it, "MAXMOVES", bs[0], "MOVES", bs[1], flush=True); json.dump(G, open(out, "w"))
        if it % 4000 == 3999 and bs < best[0]: G, bs = json.loads(json.dumps(best[1])), best[0]
    print("BEST MAXMOVES", best[0][0], "MOVES", best[0][1], flush=True)
