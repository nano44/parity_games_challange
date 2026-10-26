#!/usr/bin/env python3
"""Box 34 climb for REL (exit releases at in-phase S4a steps). Fitness = (max releases of ONE exit in one fallback-free run, total
re-releases (releases beyond the first per exit and run), total releases). Saves the best as <out>.pg. Usage: relclimb.py seed secs out seed.pg"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "box21")); sys.path.insert(0, os.path.join(HERE, "..", "box31"))
from relfr import *
from climb_fix import mutate
from cascclimb import save

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(set(G[2][v])) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, 0, 0)
    g = pg.Game(*G)
    try: rows, o = rows_w(g)
    except Exception: return (-1, 0, 0)
    ex = set(g.succ[o]) - {o}; cnt = {}; run = 0; tot = 0
    for j in range(len(rows) - 1):
        a, b = rows[j], rows[j + 1]
        if a["ph"] != b["ph"] or a["fb"]: run += 1; continue
        R1 = set(b["R"]) | {o}
        for x in ex:
            if x in a["R"] and x not in R1: cnt[(run, x)] = cnt.get((run, x), 0) + 1; tot += 1
    return (max(cnt.values(), default=0), sum(v - 1 for v in cnt.values() if v >= 2), tot)

if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    g = load(sys.argv[4]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G); t0 = time.time(); it = 0
    print("start", f, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh >= f:
            if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); save(out + ".pg", H)
            G, f = H, fh
    print("FINAL", f, it, flush=True)
