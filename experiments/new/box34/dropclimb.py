#!/usr/bin/env python3
"""Box 34 climb against CONJECTURE ONE-DROP (N5-REL-box34.md §11): at most one H1 -> ¬H1 transition per phase. Fitness = (max drops in one
phase, max H1-toggles in one phase, ¬H1 states). Saves <out>.pg and <out>_viol.pg (>= 2 drops). Usage: dropclimb.py seed secs out seed.pg"""
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
    bd = bt = 0; nh = sum(1 for r in rows if not r["h1"]); i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1]["ph"] == rows[i]["ph"]: j += 1
        d = sum(1 for k in range(i, j) if rows[k]["h1"] and not rows[k + 1]["h1"])
        t = sum(1 for k in range(i, j) if rows[k]["h1"] != rows[k + 1]["h1"])
        bd = max(bd, d); bt = max(bt, t); i = j + 1
    return (bd, bt, nh)

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
