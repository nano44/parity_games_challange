#!/usr/bin/env python3
"""L-SI box 68: hill-climb max T_k(G) (k external flips, box 64 flipdp.py) on ISO R197 ladders with m levels above level 0, optionally
seeded. Lower bounds on T_k(m). Live outputs in outdir (NOT pinned).  Usage: kclimb.py m k seed iters outdir [seed_genome.json]"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box64"))
from flipdp import analyse
from climb import rand_iso, mutate
m, k, seed, iters, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
rng = random.Random(seed); os.makedirs(out, exist_ok=True)
def sc(G):
    try: r = analyse(G, K=k, check=False)
    except AssertionError: return None
    return (r["T"][k], r["T"][0])
cur = json.load(open(sys.argv[6])) if len(sys.argv) > 6 else None
cs = sc(cur) if cur else None
while cur is None:
    G = rand_iso(m + 1, rng); s = sc(G)
    if s: cur, cs = G, s
best = cs; stale = 0
for it in range(iters):
    H = mutate(cur, rng); s = sc(H)
    if s is None: continue
    if s >= cs: stale = 0 if s > cs else stale; cur, cs = H, s
    else: stale += 1
    if cs > best:
        best = cs; json.dump(cur, open(os.path.join(out, "k%d_m%d_s%d.json" % (k, m, seed)), "w"))
        print("it", it, "T_%d" % k, best[0], "T_0", best[1], flush=True)
    if stale > 3000:
        G = rand_iso(m + 1, rng); s = sc(G)
        if s: cur, cs, stale = G, s, 0
print("FINAL m", m, "k", k, "best", best)
