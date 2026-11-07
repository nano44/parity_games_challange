#!/usr/bin/env python3
"""climb a seed genome to raise moves(x0) - (deg-1)(1+desc(x0)) for ONE named mover x0 (structure of x0's Xi-descendant set may
change only through mutations that keep desc(x0) <= its seed size). Usage: target.py seed.json x0 iters seed"""
import os, sys, json, random
H = os.path.dirname(os.path.abspath(__file__)); exec(open(os.path.join(H, "seedpm.py")).read().split("\nif __name__")[0])
f, x0, iters, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed)
G = json.load(open(f)); G["xorder"] = topo(G); D0 = len(reach(G)[x0])
def sc(G):
    try: r = measure(G)
    except RuntimeError: return (-99, 0)
    if r["desc"][x0] > D0: return (-99, 0)
    return (r["mv"][x0] - (len(G["opts"][x0]) - 1) * (1 + r["desc"][x0]), r["T"])
s = sc(G); best = s; print("seed", os.path.basename(f), "x0", x0, "desc", D0, s, flush=True)
for it in range(iters):
    G2 = mutate(G, rng); s2 = sc(G2)
    if s2 >= s:
        G, s = G2, s2
        if s > best:
            best = s; print("it", it, s, flush=True)
            if s[0] > 0:
                json.dump(G, open(os.path.join(H, "out", "KILL_PM_target_%s_x%d_s%d.json" % (os.path.basename(f)[:-5], x0, seed)), "w")); print("KILL", flush=True); break
print("FINAL", best)
