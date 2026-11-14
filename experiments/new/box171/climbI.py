#!/usr/bin/env python3
"""hill-climb degree-2 ladders (box165 kill1.py generator/mutations) to maximize the number of top-only intervals I, tie T.
Usage: climbI.py d w iters restarts seed [LR]"""
import os, sys, json, random
H = os.path.dirname(os.path.abspath(__file__))
_H = H; H = os.path.join(_H, "..", "box165")
exec(open(os.path.join(H, "kill1.py")).read().split("\nif __name__")[0].replace('H = os.path.dirname(os.path.abspath(__file__)); ', ''))
H = _H
def scI(G):
    try: S, _ = Gen(G).run(G["start"])
    except RuntimeError: return (-1, 0, 0)
    top = max(G["lev"]); low = [v for v in range(G["N"]) if G["lev"][v] < top]
    k = "".join("L" if any(S[t][v] != S[t - 1][v] for v in low) else "T" for t in range(1, len(S)))
    return (sum(1 for i, c in enumerate(k) if c == "T" and (i == 0 or k[i - 1] == "L")), len(S) - 1, k.count("L"))
d, w, iters, restarts, seed = map(int, sys.argv[1:6]); lr = len(sys.argv) > 6; rng = random.Random(seed); best = None
for rs in range(restarts):
    G = gen(d, w, rng, lr); s = scI(G)
    for it in range(iters):
        G2 = mutate(G, rng, lr); s2 = scI(G2)
        if s2[:2] >= s[:2]: G, s = G2, s2
    if best is None or s[:2] > best[:2]: best = s; json.dump(G, open(os.path.join(H, "out", "climbI_d%d_w%d_%s_s%d.json" % (d, w, "LR" if lr else "gen", seed)), "w"))
    print("restart %d (I, T, lower) %s best %s" % (rs, s, best), flush=True)
