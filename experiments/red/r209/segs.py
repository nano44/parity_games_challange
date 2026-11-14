#!/usr/bin/env python3
"""L-RED R209 SEGS: TOP-SPLIT anatomy of a run: steps that move a top mover (m of them) cut the run into segments; prints per segment
the number of steps moving a lower mover, and which coupled lower movers move. Usage: segs.py file.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal
for f in sys.argv[1:]:
    G = json.load(open(f)); top = max(G["lev"]); U = [v for v in range(G["N"]) if G["lev"][v] == top]; S, why = ideal.traj(G)
    cx = sorted({v for v in range(G["N"]) if G["lev"][v] < top for o in G["opts"][v] if o[1] in U})
    cuts = [t for t in range(1, len(S)) if any(S[t][u] != S[t - 1][u] for u in U)]; segs = []; a = 0
    for b in cuts + ([len(S) - 1] if not cuts or cuts[-1] != len(S) - 1 else []):
        low = sum(1 for t in range(a + 1, b + 1) if any(S[t][v] != S[t - 1][v] for v in range(G["N"]) if v not in U))
        cm = [t for t in range(a + 1, b + 1) for v in cx if S[t][v] != S[t - 1][v]]
        segs.append((low, len(cm))); a = b
    print(f"{os.path.basename(f)}: d {top + 1} T {len(S) - 1} m {len(cuts)} segments (lower steps, coupled-mover moves) {segs}")
