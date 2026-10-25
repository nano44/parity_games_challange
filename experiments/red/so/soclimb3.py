#!/usr/bin/env python3
"""Box 38 (L-RED): climb against L-SI's CONJECTURE ENT / Lemma NO-RF-OLD (counter = sox3.analyse). Mutations: soclimb.mutate.
Fitness: (NORF + ENT failures, windows reaching the next fallback, any rise before a next fallback (0/1), gap, rfb, rfb0, longest window).
Usage: soclimb3.py seed secs OUT (seed.pg | --rand n)"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sox, sox3, pg
from soclimb import mutate, dump
NEG = (-10 ** 9,) * 7
def fit(G):
    g = pg.Game(*G)
    if any(not s for s in G[2]) or len(sox.oddchoice(g)) != 1: return NEG, None
    try: r = sox3.analyse(g, cap=3000)
    except AssertionError: raise
    except Exception: return NEG, None
    return (sum(r["C"].values()), r["reach"], r.get("rfb0", 0) and 1, r["gap"], r["rfb"], r.get("rfb0", 0), r["maxwin"]), r
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
