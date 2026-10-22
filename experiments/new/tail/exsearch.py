#!/usr/bin/env python3
"""Box 10: search over EXPLOIT assignments on the gadgeted Odd-CDAG (tailsim.build). Each gadget e[x,u] gets an exploit set drawn from the
Odd vertices 0..n (upward targets allowed) and other gadgets. Fitness = frozen-sigma tail steps from tau0 = all -> sink, counted only
when sigma (gadgets direct) is Even-optimal (Isigma = empty); otherwise reported separately. Modes: exh1 (exhaustive, <= 1 target per
gadget, Odd targets only) or rand K (K random assignments, 0-2 targets per gadget, Odd + gadget targets). Usage: exsearch.py n exh1|rand K seed"""
import sys, itertools, random, hashlib
from tailsim import build, tail, tau_all_sink, cdag_target
import pg
n = int(sys.argv[1]); mode = sys.argv[2]
edges = [(x, u) for x in range(1, n + 1) for u in range(x)]
best = (0, None); best_nonopt = (0, None); seen = 0
def run(ex):
    global best, best_nonopt, seen
    g, sigma, gid = build(n, ex); r = tail(g, sigma, tau_all_sink(g, gid, n), cap=2000); seen += 1
    key = (r["steps"], ex)
    if r["optimal_sigma"]:
        if r["steps"] > best[0]: best = key; print("OPT  steps", r["steps"], "exploits", ex, flush=True)
    else:
        if r["steps"] > best_nonopt[0]: best_nonopt = key; print("NONOPT steps", r["steps"], "even_moves", r["even_moves"], "exploits", ex, flush=True)
if mode == "exh1":
    opts = [None] + list(range(n + 1))
    for choice in itertools.product(opts, repeat=len(edges)):
        ex = {e: [c] for e, c in zip(edges, choice) if c is not None and c != e[1]}
        run(ex)
else:
    K, seed = int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed)
    targets = list(range(n + 1)) + edges
    for _ in range(K):
        ex = {}
        for e in edges:
            k = rng.choice([0, 1, 1, 2])
            ts = [t for t in rng.sample(targets, k) if t != e[1] and t != e]
            if ts: ex[e] = ts
        run(ex)
print(f"DONE n={n} mode={mode} configs={seen} best optimal-sigma tail={best[0]} best non-optimal-sigma run={best_nonopt[0]}")
