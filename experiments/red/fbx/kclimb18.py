#!/usr/bin/env python3
"""Box 42: hill-climb on K (wakes per phase, k18.analyse). Fitness (max Kt per phase, total Kt, iterations): Kt = transitions with a wake (the quantity in ρ ≤ 2f + 2X + K).
Mutations: soclimb.mutate. Usage: kclimb18.py seed secs OUT seed.pg"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import sox, k18, pg
from soclimb import mutate, dump
NEG = (-1, -1, -10 ** 9)
def fit(G):
    try:
        g = pg.Game(*G)
        if any(not s for s in G[2]) or len(sox.oddchoice(g)) != 1: return NEG
        r = k18.analyse(g, cap=600); ph = r["phases"]
    except Exception: return NEG
    return (max((p["Kt"] for p in ph), default=0), sum(p["Kt"] for p in ph), r["it"])
seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
g = sox.load(sys.argv[4]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G)
t0 = time.time(); it = 0; print("start", f, flush=True); dump(G, out + ".pg")
while time.time() - t0 < secs:
    H = mutate(rng, G); it += 1; fh = fit(H)
    if fh >= f:
        if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); dump(H, out + ".pg")
        G, f = H, fh
print("FINAL", f, it, flush=True)
