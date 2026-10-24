#!/usr/bin/env python3
"""Box 31 (b) climb: W-flat switches outside route form (U2/U3). Fitness = (switches in W-flat runs of U2/U3 stretches, cycle
switches, U2/U3 stretches). Any CASC-C violation is printed and saved as <out>_viol.pg. Usage: nrclimb.py seed secs out seed.pg"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from nrcheck import *
from climb_fix import mutate
from cascclimb import save

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, -1, -1), 0
    g = pg.Game(*G); Y = split(g, odd[0])
    if not any(w in Y for w in G[2][odd[0]]): return (-1, -1, -1), 0
    acc = {}
    try: analyse(g, acc)
    except Exception: return (-1, -1, -1), 0
    sw = sum(v for k, v in acc.items() if k.startswith("sw_")); runs = sum(v for k, v in acc.items() if k.endswith("_runs"))
    return (sw, acc.get("cyc_sw", 0), runs), acc.get("cascC_viol", 0) + acc.get("wcyc_viol", 0)

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
