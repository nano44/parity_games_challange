#!/usr/bin/env python3
"""Box 32 climb on C^1O (SPEC): fitness = (max over M-blocks of #KW transitions − |R|, max W-changes per vertex per block, max EV per
block). Tests the DATA hypothesis KW-M: #KW transitions per M-block of a U2/U3/U23 stretch ≤ |R| − 1. Saves the best as <out>.pg and
any candidate with KW per block ≥ |R| as <out>_viol.pg. Usage: mblockclimb.py seed secs out seed.pg"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21")); sys.path.insert(0, os.path.join(HERE, "..", "box31"))
from mblock import *
from climb_fix import mutate
from cascclimb import save

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-99, 0, 0), 0
    g = pg.Game(*G); acc = {}
    try: analyse(g, acc)
    except Exception: return (-99, 0, 0), 0
    kw = max([acc[k][0] - acc[k][1] for k in acc if k.startswith("max_") and k.endswith("KW_perblock")] or [-99])
    pv = max([acc[k][0] for k in acc if k.endswith("Wchanges_per_vertex_block")] or [0])
    ev = max([acc[k][0] for k in acc if k.endswith("EV_perblock")] or [0])
    return (kw, pv, ev), kw >= 0

if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    g = load(sys.argv[4]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f, _ = fit(G); t0 = time.time(); it = 0
    print("start", f, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh, vi = fit(H)
        if vi: print(f"VIOLATION it {it} fit {fh}", flush=True); save(out + "_viol.pg", H)
        if fh >= f:
            if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); save(out + ".pg", H)
            G, f = H, fh
    print("FINAL", f, it, flush=True)
