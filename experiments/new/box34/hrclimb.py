#!/usr/bin/env python3
"""Box 34 climb against CONJECTURE ONE-H (docs/new/N5-REL-box34.md §10): in a phase the (h) states form one consecutive run.
Fitness = (max number of maximal (h)-runs in one phase, fallbacks at ¬(h) states of phases that contain an (h) state, (h) states).
Saves the best as <out>.pg and any phase with >= 2 (h)-runs as <out>_viol.pg. Usage: hrclimb.py seed secs out seed.pg"""
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
    hh = [r["h1"] and h2(r["nxt"], o) and r["Xi"][o][0] == r["W"][o][0] for r in rows]
    best = 0; fbn = 0; nh = sum(hh); i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1]["ph"] == rows[i]["ph"]: j += 1
        runs = sum(1 for k in range(i, j + 1) if hh[k] and (k == i or not hh[k - 1]))
        best = max(best, runs)
        if any(hh[i:j + 1]): fbn += sum(1 for k in range(i, j) if rows[k]["fb"] and not hh[k])
        i = j + 1
    return (best, fbn, nh)

if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    g = load(sys.argv[4]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G); t0 = time.time(); it = 0
    print("start", f, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh[0] >= 2 and fh[0] > f[0]: print(f"VIOLATION it {it} fit {fh}", flush=True); save(out + "_viol.pg", H)
        if fh >= f:
            if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); save(out + ".pg", H)
            G, f = H, fh
    print("FINAL", f, it, flush=True)
