#!/usr/bin/env python3
"""L-SI box 67: hill-climb max T_1(G) subject to T_0(G) = tau on ISO R197 ladders with m levels above level 0 (lower bounds on
D(m, tau) := max T_1(G) over genomes with T_0(G) = tau; T_0, T_1 = max over starts of the run with <= 0 / <= 1 external flip, box 64
flipdp.py). Score = (-|T_0 - tau|, T_1). Live outputs in outdir (NOT pinned).  Usage: tauclimb.py m tau seed iters outdir [seed_genome.json]"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box64"))
from flipdp import analyse
from climb import rand_iso, mutate
m, tau, seed, iters, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
rng = random.Random(seed); os.makedirs(out, exist_ok=True)
def sc(G):
    try: r = analyse(G, K=1, check=False)
    except AssertionError: return None
    return (-abs(r["T"][0] - tau), r["T"][1])
cur = None
if len(sys.argv) > 6:  # optional seed genome
    cur = json.load(open(sys.argv[6])); cs = sc(cur)
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
        best = cs; json.dump(cur, open(os.path.join(out, "tau_m%d_t%d_s%d.json" % (m, tau, seed)), "w"))
        print("it", it, "T0 dev", -best[0], "T1", best[1], flush=True)
    if stale > 3000:
        G = rand_iso(m + 1, rng); s = sc(G)
        if s: cur, cs, stale = G, s, 0
print("FINAL m", m, "tau", tau, "best", best)
