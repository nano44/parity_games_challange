#!/usr/bin/env python3
"""L-SI box 69: hill-climb max T_0(G) + T_1(G) (box 64 flipdp.py) on ISO R197 ladders with m levels above level 0, optionally seeded.
Lower bounds for CONJECTURE SUM_1 (T_0(G) + T_1(G) <= 2 T^R(m) + 1). Live outputs (NOT pinned).  Usage: sumclimb.py m seed iters out [seed.json]"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box64"))
from flipdp import analyse
from climb import rand_iso, mutate
m, seed, iters, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed); os.makedirs(out, exist_ok=True)
def sc(G):
    try: T = analyse(G, K=1, check=False)["T"]
    except AssertionError: return None
    return (T[0] + T[1], T[1])
cur = json.load(open(sys.argv[5])) if len(sys.argv) > 5 else None
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
        best = cs; json.dump(cur, open(os.path.join(out, "sum_m%d_s%d.json" % (m, seed)), "w")); print("it", it, "T0+T1", best[0], "T1", best[1], flush=True)
    if stale > 3000:
        G = rand_iso(m + 1, rng); s = sc(G)
        if s: cur, cs, stale = G, s, 0
print("FINAL m", m, "best", best)
