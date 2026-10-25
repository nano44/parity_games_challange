#!/usr/bin/env python3
"""Box 36 climb for CONJECTURE OUT-POLY (docs/new/N5-SCOPE-box36.md §4): fallbacks at H1 ∧ ¬H2 or OTHER (H1 ∧ H2 ∧ ¬H3) states in one
phase. Fitness = (max such fallbacks in one phase, crossings in that phase). Usage: outclimb.py seed secs out seed.pg"""
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
    best = (0, 0); i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1]["ph"] == rows[i]["ph"]: j += 1
        c = sum(1 for k in range(i, j) if rows[k]["fb"] and rows[k]["h1"] and
                (not h2(rows[k]["nxt"], o) or rows[k]["Xi"][o][0] != rows[k]["W"][o][0]))
        X = sum(1 for k in range(i, j) if set(rows[k]["R"]) != set(rows[k + 1]["R"]))
        best = max(best, (c, X)); i = j + 1
    return best

if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    g = load(sys.argv[4]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G); t0 = time.time(); it = 0
    print("start", f, "n", g.n, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh >= f:
            if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); save(out + ".pg", H)
            G, f = H, fh
    print("FINAL", f, it, flush=True)
