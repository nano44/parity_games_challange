#!/usr/bin/env python3
"""Box 35 (c) climb against CONJECTURE PF-THETA (N5-DROP-box35.md §8): in a scope run, while the last fallback level is M, theta changes
at most n times. Fitness = (max theta-changes under one fallback level in one scope run, fallbacks in that run). Saves <out>.pg, and
<out>_viol.pg when the count exceeds n. Usage: pfclimb.py seed secs out seed.pg"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "box21")); sys.path.insert(0, os.path.join(HERE, "..", "box31"))
from thcls import *
from climb_fix import mutate
from cascclimb import save

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(set(G[2][v])) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, 0)
    g = pg.Game(*G)
    try: rows, o = rows_w(g)
    except Exception: return (-1, 0)
    best = (0, 0)
    for (k0, k1) in scope_runs(g, rows, o):
        Lf = None; per = {}; nf = 0
        for k in range(k0, k1 + 1):
            a, b = rows[k], rows[k + 1]
            if a["th"] != b["th"] and Lf is not None: per[Lf] = per.get(Lf, 0) + 1
            if a["fb"]: Lf = a["M"]; nf += 1
        if per: best = max(best, (max(per.values()), nf))
    return best

if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    g = load(sys.argv[4]); n = g.n; G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G); t0 = time.time(); it = 0
    print("start", f, "n", n, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh[0] > n and fh[0] > f[0]: print(f"VIOLATION it {it} fit {fh}", flush=True); save(out + "_viol.pg", H)
        if fh >= f:
            if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); save(out + ".pg", H)
            G, f = H, fh
    print("FINAL", f, it, flush=True)
