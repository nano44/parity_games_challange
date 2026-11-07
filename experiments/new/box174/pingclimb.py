#!/usr/bin/env python3
"""L-NEW box 174: kill-candidate climb for RENEW-COUNT_2 on L^R_d: start from a clock genome (seed file), mutate only (i) every field of
the movers of the top two levels and (ii) Xi-targets of any option (acyclic via xorder); objective (I, T); annealing-style acceptance.
Usage: pingclimb.py seed.json iters restarts seed [temp]"""
import os, sys, json, random, copy
H = os.path.dirname(os.path.abspath(__file__)); _H = H; H = os.path.join(_H, "..", "box165")
exec(open(os.path.join(H, "kill1.py")).read().split("\nif __name__")[0].replace('H = os.path.dirname(os.path.abspath(__file__)); ', ''))
H = _H
def scI(G):
    try: S, _ = Gen(G).run(G["start"])
    except Exception: return (-1, 0)
    top = max(G["lev"]); low = [v for v in range(G["N"]) if G["lev"][v] < top]
    k = "".join("L" if any(S[t][v] != S[t - 1][v] for v in low) else "T" for t in range(1, len(S)))
    return (sum(1 for i, c in enumerate(k) if c == "T" and (i == 0 or k[i - 1] == "L")), len(S) - 1)
def frozen_ok(G0, G):
    tau = max(G0["lev"])
    for x in range(G0["N"]):
        if G0["lev"][x] >= tau - 1: continue
        for k in range(2):
            m = G0["opts"][x][k][2]
            if G["gate"][x][k] != G0["gate"][x][k] or G["br"][m] != G0["br"][m] or G["bp"][m] != G0["bp"][m]: return False
    return True
sf, iters, restarts, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); temp = float(sys.argv[5]) if len(sys.argv) > 5 else 0.03
rng = random.Random(seed); G0 = json.load(open(sf)); best = None; d = max(G0["lev"]) + 1
out = os.path.join(H, "out", "ping_%s_s%d.json" % (os.path.basename(sf)[:-5], seed))
for rs in range(restarts):
    G = copy.deepcopy(G0); s = scI(G); bs, bG = s, G
    for it in range(iters):
        G2 = mutate(G, rng, True)
        if not frozen_ok(G0, G2): continue
        s2 = scI(G2)
        if s2 >= s or rng.random() < temp: G, s = G2, s2
        if s > bs: bs, bG = s, G
    if best is None or bs > best: best = bs; json.dump(bG, open(out, "w"))
    print("restart %d best-in-restart %s best %s (d %d, d+1 = %d)" % (rs, bs, best, d, d + 1), flush=True)
