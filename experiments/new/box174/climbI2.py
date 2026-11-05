#!/usr/bin/env python3
"""L-NEW box 173: hill-climb on R197 ladders (L^R_d: 2-wide, degree 2, option k of a level-l mover W-pointing to mover 2(l-1)+k) to
maximise I (number of maximal top-only runs), tie-break T; plateau moves accepted, worse moves with prob. 0.02.
Usage: climbR.py d iters restarts seed [seedfile.json]   (out/climbR_d<d>_s<seed>.json = best genome)"""
import os, sys, json, random, copy
H = os.path.dirname(os.path.abspath(__file__)); _H = H; H = os.path.join(_H, "..", "box165")
exec(open(os.path.join(H, "kill1.py")).read().split("\nif __name__")[0].replace('H = os.path.dirname(os.path.abspath(__file__)); ', ''))
H = _H; LR = os.environ.get("LR", "1") == "1"
def scI(G):
    try: S, _ = Gen(G).run(G["start"])
    except Exception: return (-1, 0, 0)
    top = max(G["lev"]); low = [v for v in range(G["N"]) if G["lev"][v] < top]
    k = "".join("L" if any(S[t][v] != S[t - 1][v] for v in low) else "T" for t in range(1, len(S)))
    return (sum(1 for i, c in enumerate(k) if c == "T" and (i == 0 or k[i - 1] == "L")), len(S) - 1, k.count("L"))
d, iters, restarts, seed = map(int, sys.argv[1:5]); sf = sys.argv[5] if len(sys.argv) > 5 else None
rng = random.Random(seed); best = None; out = os.path.join(H, "..", "box174", "out", "climbI2_d%d_%s_s%d.json" % (d, "LR" if LR else "L", seed))
for rs in range(restarts):
    if sf:
        G = json.load(open(sf))
        if "xorder" not in G: G["xorder"] = list(ns["topo"](G)) if "ns" in dir() else None
    else: G = gen(d, 2, rng, LR)
    s = scI(G); bs, bG = s, G
    for it in range(iters):
        G2 = mutate(G, rng, LR); s2 = scI(G2)
        if s2[:2] >= s[:2] or rng.random() < 0.02: G, s = G2, s2
        if s[:2] > bs[:2]: bs, bG = s, G
    if best is None or bs[:2] > best[:2]: best = bs; json.dump(bG, open(out, "w"))
    print("restart %d (I, T, lower) %s best %s" % (rs, bs, best), flush=True)
