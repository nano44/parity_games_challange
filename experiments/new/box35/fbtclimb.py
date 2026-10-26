#!/usr/bin/env python3
"""Box 35 (b) climb: an in-phase S4c fallback at H1 ∧ ¬H2 with tau(o) != o after which tau(o) leaves R (N5-REL-box34 §12 item 2).
Fitness = (events, such fallbacks with a switch on o's W-cycle, such fallbacks). Saves <out>.pg and <out>_viol.pg.
Usage: fbtclimb.py seed secs out seed.pg"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "box21")); sys.path.insert(0, os.path.join(HERE, "..", "box31"))
from fbtau import *
from climb_fix import mutate
from cascclimb import save

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(set(G[2][v])) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, 0, 0)
    g = pg.Game(*G)
    try: rows, o = rows_w(g)
    except Exception: return (-1, 0, 0)
    ev = [e for e in events(g, rows, o) if not e["loop"]]
    return (sum(e["leave"] for e in ev), sum(1 for e in ev if e["sw"]), len(ev))

if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    g = load(sys.argv[4]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G); t0 = time.time(); it = 0
    print("start", f, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh[0] >= 1 and fh[0] > f[0]: print(f"VIOLATION it {it} fit {fh}", flush=True); save(out + "_viol.pg", H)
        if fh >= f:
            if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); save(out + ".pg", H)
            G, f = H, fh
    print("FINAL", f, it, flush=True)
