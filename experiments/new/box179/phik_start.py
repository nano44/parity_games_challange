#!/usr/bin/env python3
"""L-NEW box 179: T against PHI_K(s_0) on the stored start of each L^R genome file (Theorem PHIK-DESCENT: T <= PHI_K(s_0)).
Usage: phik_start.py files..."""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); ns = {"__file__": os.path.join(H, "phik.py"), "__name__": "lib"}; exec(open(ns["__file__"]).read().split("\nC = dict")[0], ns)
Gen, is_lr, phik = ns["Gen"], ns["is_lr"], ns["phik"]; rows = []
for f in sys.argv[1:]:
    try: G = json.load(open(f)); assert is_lr(G)
    except Exception: continue
    g = Gen(G); d = G["N"] // 2; S, _ = g.run(G["start"]); T = len(S) - 1; P0 = phik(g, d, tuple(G["start"]))
    rows.append((d, T, P0, os.path.basename(f)))
viol = sum(1 for r in rows if r[1] > r[2])
for r in sorted(rows, key=lambda r: (r[0], -r[1]))[:400]:
    if r[1] >= 8: print("d %d T %d PHI_K(s0) %d max %d  %s" % (r[0], r[1], r[2], (1 << (r[0] + 2)) - 2 * r[0] - 4, r[3]))
print("files %d violations %d tight %d" % (len(rows), viol, sum(1 for r in rows if r[1] == r[2] and r[1] > 0)))
