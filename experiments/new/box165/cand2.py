#!/usr/bin/env python3
"""C1D: moves(x) <= (deg(x) - 1) * (1 + desc(x)) on real IDEAL runs (deg(x) = number of options of x); reports violations split by
max genome degree, and the tightest ratio moves / ((deg-1)(1+desc)). Usage: cand2.py file.json ..."""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); exec(open(os.path.join(H, "permover.py")).read().split("\nif __name__")[0])
viol = {}; files = 0; best = (0, None)
for f in sys.argv[1:]:
    try: G = json.load(open(f)); assert "N" in G; r = measure(G)
    except Exception: continue
    files += 1
    for x in range(G["N"]):
        D = len(G["opts"][x]); b = (D - 1) * (1 + r["desc"][x])
        if r["mv"][x] / b > best[0]: best = (r["mv"][x] / b, (os.path.basename(f), x, D, r["desc"][x], r["mv"][x]))
        if r["mv"][x] > b:
            viol[r["deg"]] = viol.get(r["deg"], 0) + 1
            print("VIOL", os.path.basename(f), "x", x, "deg", D, "desc", r["desc"][x], "moves", r["mv"][x])
print("files", files, "violations by genome degree", viol, "tightest", best)
