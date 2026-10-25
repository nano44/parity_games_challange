#!/usr/bin/env python3
"""Box 38 (L-RED): climb against L-NEW's TOGGLE / L-MONO / Z-COUNT (counter = sox4.analyse). Mutations: soclimb.mutate.
Fitness: (failures, max H1-toggles in one phase, max Z-only toggles, max toggles − σ(c)-changes).
Usage: soclimb4.py seed secs OUT (seed.pg | --rand n)"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sox, sox4, pg
from soclimb import mutate, dump
NEG = (-10 ** 9,) * 4
def fit(G):
    g = pg.Game(*G)
    if any(not s for s in G[2]) or len(sox.oddchoice(g)) != 1: return NEG, None
    try: r = sox4.analyse(g, cap=3000)
    except AssertionError: raise
    except Exception: return NEG, None
    rs = r["rows"]; mx = lambda f: max((f(x) for x in rs), default=-10 ** 9)
    return (sum(r["C"].values()), mx(lambda x: x["tog"]), mx(lambda x: x["zonly"]), mx(lambda x: x["tog"] - x["cch"])), r
if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    g = sox.load(sys.argv[4]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f, r = fit(G)
    t0 = time.time(); it = 0; print("start", f, flush=True); dump(G, out + ".pg")
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh, rh = fit(H)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh} it/fb {rh['it']}/{rh['fb']} C {rh['C']} ex {rh['ex']}", flush=True); dump(H, out + ".pg")
            G, f = H, fh
    print("FINAL", f, it, flush=True)
