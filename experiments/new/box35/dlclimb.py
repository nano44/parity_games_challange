#!/usr/bin/env python3
"""Box 35 (a) climb against CONJECTURE DROP-LEN (N5-REL-box34.md §13) and its weaker form. MODE (env):
 dl  = max number of H1 -> ¬H1 drops inside one stretch of a phase with theta constant (>= 2 refutes DROP-LEN);
 fr  = max drops inside one fallback-free run of a phase (>= 2 refutes the weaker form);
 tog = max H1-toggles in one phase (tests the size of Theorem TOGGLE's bound).
Fitness = (target, toggles per phase, ¬H1 states). Saves <out>.pg (best) and <out>_viol.pg (dl/fr >= 2).
Usage: MODE=dl dlclimb.py seed secs out seed.pg"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box34"))
sys.path.insert(0, os.path.join(HERE, "..", "box21")); sys.path.insert(0, os.path.join(HERE, "..", "box31"))
from relfr import *
from climb_fix import mutate
from cascclimb import save
MODE = os.environ.get("MODE", "dl")

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(set(G[2][v])) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, 0, 0)
    g = pg.Game(*G)
    try: rows, o = rows_w(g)
    except Exception: return (-1, 0, 0)
    best = bt = 0; nh = sum(1 for r in rows if not r["h1"]); i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1]["ph"] == rows[i]["ph"]: j += 1
        t = sum(1 for k in range(i, j) if rows[k]["h1"] != rows[k + 1]["h1"]); bt = max(bt, t)
        cur = 0
        for k in range(i, j):
            if MODE == "dl" and rows[k]["th"] != rows[k + 1]["th"] and not (rows[k]["h1"] and not rows[k + 1]["h1"]): cur = 0
            if MODE == "fr" and rows[k]["fb"]: cur = 0
            if rows[k]["h1"] and not rows[k + 1]["h1"]:
                cur += 1; best = max(best, cur)
                if MODE == "dl" and rows[k]["th"] != rows[k + 1]["th"]: cur = 1
        i = j + 1
    if MODE == "tog": best = bt
    return (best, bt, nh)

if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    g = load(sys.argv[4]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G); t0 = time.time(); it = 0
    print("start", MODE, f, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if MODE != "tog" and fh[0] >= 2 and fh[0] > f[0]: print(f"VIOLATION it {it} fit {fh}", flush=True); save(out + "_viol.pg", H)
        if fh >= f:
            if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); save(out + ".pg", H)
            G, f = H, fh
    print("FINAL", f, it, flush=True)
