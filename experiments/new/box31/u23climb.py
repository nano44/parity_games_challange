#!/usr/bin/env python3
"""Box 31 (b) climb on o-cyclic C^1O (SPEC). mode U2: fitness (U2 W-flat switches, longest W-flat run); mode U3: (U3 W-flat switches,
U3 events, longest run). Any CASC-U2 / CASC-U3 violation is printed and saved as <out>_viol.pg. Usage: u23climb.py mode seed secs out seed.pg"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from u23check import *
from climb_fix import mutate
from cascclimb import save

def fit(G, mode):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, -1, -1), 0
    g = pg.Game(*G); Y = split(g, odd[0])
    if not any(w in Y for w in G[2][odd[0]]): return (-1, -1, -1), 0
    acc = {}
    try: analyse(g, acc)
    except Exception: return (-1, -1, -1), 0
    vi = acc.get("U2_viol", 0) + acc.get("U3_violB", 0) + acc.get("U3_viol2R", 0)
    f = (acc.get("U2_sw", 0), acc.get("maxflat", 0), 0) if mode == "U2" else (acc.get("U3_sw", 0), acc.get("U3_events", 0), acc.get("maxflat", 0))
    return f, vi

if __name__ == "__main__":
    mode, seed, secs, out = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    g = load(sys.argv[5]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f, _ = fit(G, mode); t0 = time.time(); it = 0
    print("start", f, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh, vi = fit(H, mode)
        if vi: print(f"VIOLATION it {it} fit {fh}", flush=True); save(out + "_viol.pg", H)
        if fh >= f:
            if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); save(out + ".pg", H)
            G, f = H, fh
    print("FINAL", f, it, flush=True)
