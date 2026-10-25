#!/usr/bin/env python3
"""Box 34 climb: w-changes inside SN prefixes under (h) (the quantity X_SN reduces to, docs/new/N5-REL-box34.md). Fitness = (max number
of w-changing transitions k -> k+1 with (h) at k and k+1 inside one phase, max in one fallback-free run, total). Usage: wsnclimb.py seed
secs out seed.pg"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "box21")); sys.path.insert(0, os.path.join(HERE, "..", "box31"))
from relfr import *
from climb_fix import mutate
from cascclimb import save

def wcount(g):
    rows, o = rows_w(g)
    hh = [r["h1"] and h2(r["nxt"], o) and r["Xi"][o][0] == r["W"][o][0] for r in rows]
    per = {}; prun = {}; run = 0; tot = 0
    for k in range(len(rows) - 1):
        a, b = rows[k], rows[k + 1]
        if a["ph"] != b["ph"]: run += 1; continue
        if hh[k] and hh[k + 1] and a["w"] != b["w"]:
            per[a["ph"]] = per.get(a["ph"], 0) + 1; prun[run] = prun.get(run, 0) + 1; tot += 1
        if a["fb"]: run += 1
    return (max(per.values(), default=0), max(prun.values(), default=0), tot)

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(set(G[2][v])) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, 0, 0)
    try: return wcount(pg.Game(*G))
    except Exception: return (-1, 0, 0)

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
