#!/usr/bin/env python3
"""L-RED 60 R226: TOWER HIGH, variant 2: ALL options of GROW7's High source x17 rewired into the tower (option k -> tower mover y + k*step),
so the tower is the only High. Every y, step in {0, 1}, gate placement below / above. Score (A, #tops, T) as tower226.ascore.
Usage: tower2_226.py GROW7.json HP.json TAG"""
import sys, os, json, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H]
from ascore226 import ascore
from compose226 import union, rewire, check
A = json.load(open(sys.argv[1])); B = json.load(open(sys.argv[2])); TAG = sys.argv[3]; NA = A["N"]; best = None; hist = collections.Counter()
for gm in ("below", "above"):
    G0 = union(A, B, gm)
    for step in (0, 1):
        for y in range(NA, G0["N"]):
            G = G0
            for k in range(len(G0["opts"][17])): G = rewire(G, 17, k, 1, min(G0["N"] - 1, y + k * step))
            try: check(G); a = ascore(G)
            except Exception: continue
            hist[a[0]] += 1
            if best is None or a > best[0]: best = (a, gm, step, y); json.dump(G, open(f"out/tower2_{TAG}.json", "w")); print("NEW", best, flush=True)
print("A hist", sorted(hist.items())); print("BEST", best, flush=True)
