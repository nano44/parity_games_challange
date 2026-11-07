#!/usr/bin/env python3
"""screen per-mover candidate bounds on real IDEAL runs: C1 moves(x) <= 1 + desc(x); C2 KF_x <= 1 + desc(x); C3 moves(x) <= 1 + desc(x)
counted only over descendants that move in the run (movdesc). Usage: cand.py file.json ..."""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); exec(open(os.path.join(H, "permover.py")).read().split("\nif __name__")[0])
tot = {"C1": 0, "C2": 0, "C3": 0}; files = 0
for f in sys.argv[1:]:
    try: G = json.load(open(f)); assert "N" in G; r = measure(G)
    except Exception: continue
    files += 1; R = reach(G); N = G["N"]
    for x in range(N):
        md = sum(1 for y in R[x] if r["mv"][y] > 0)
        for c, ok in (("C1", r["mv"][x] <= 1 + r["desc"][x]), ("C2", r["kf"][x] <= 1 + r["desc"][x]), ("C3", r["mv"][x] <= 1 + md)):
            if not ok:
                tot[c] += 1
                if tot[c] <= 4: print(c, "VIOL", os.path.basename(f), "deg", r["deg"], "x", x, "lev", r["lev"][x], "desc", r["desc"][x], "movdesc", md, "moves", r["mv"][x], "KF", r["kf"][x])
print("files", files, "violations", tot)
