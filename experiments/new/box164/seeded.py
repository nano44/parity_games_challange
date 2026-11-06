#!/usr/bin/env python3
"""climb from a seed genome file (same mutations/score as climb.py). Usage: seeded.py seed.json kind iters seed"""
import os, sys, json, random
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "climb.py")).read().split("\nif __name__")[0])
f, kind, iters, seed = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
rng = random.Random(seed); G = json.load(open(f)); d = G["N"] // 2
if "xorder" not in G or not G["xorder"]:
    print("no xorder"); sys.exit(1)
s, r = score(G, kind); print("seed", os.path.basename(f), "mult", s[0], "T", s[1], flush=True); best = s
for it in range(iters):
    G2 = mutate(G, rng); s2, r2 = score(G2, kind)
    if s2 >= s:
        G, s = G2, s2
        if s > best:
            best = s; json.dump(G, open(os.path.join(H, "out", "seed_%s_d%d_m%d_T%d.json" % (kind, d, s[0], s[1])), "w"))
            print("it %d mult %d T %d" % (it, s[0], s[1]), flush=True)
print("FINAL mult %d T %d" % best)
