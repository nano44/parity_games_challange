#!/usr/bin/env python3
"""tightness of the static PM' form S over movers with desc + |W| >= 3, and the run-level sum check T <= sum_x (deg-1)(1+desc+|W|),
with the ratio T / sum. Usage: tight.py file.json ..."""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); exec(open(os.path.join(H, "pmprime.py")).read().split("\nif __name__")[0])
best = []; sums = []
for f in sys.argv[1:]:
    try: G = json.load(open(f)); assert "N" in G; T, out = analyse(G)
    except Exception: continue
    for o in out:
        if o["desc"] + o["W"] >= 3: best.append((o["mv"] - o["D"] * (1 + o["desc"] + o["W"]), o["mv"], o["desc"], o["W"], os.path.basename(f), o["x"]))
    s = sum(o["D"] * (1 + o["desc"] + o["W"]) for o in out); sums.append((T / s, T, s, len(out), os.path.basename(f)))
best.sort(reverse=True); sums.sort(reverse=True)
print("closest movers (excess, moves, desc, |W|, file, x):"); [print("  ", b) for b in best[:6]]
print("largest T / sum-bound:"); [print("  ", s) for s in sums[:5]]
