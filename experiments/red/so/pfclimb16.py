#!/usr/bin/env python3
"""Box 39 (L-RED): hill-climb on 𝒞^1O against PF-THETA (linear) and RISE-LAST, counter = pfx.analyse (own checker). Mutations: soclimb.mutate.
  pf  : (max θ-changes under one fallback level M in one scope run, same incl. the fallback step, fallbacks in that run)
  pfm : as pf, but only runs with >= 2 fallbacks count (the drain/refill loop, not one fallback-free run)
  rise: (rfb0 RISE-LAST events, consecutive fallback pairs checked, pf)
A count > n (pf) or rfb0 > 0 is saved as OUT_viol.pg. Invalid sentinel −10^9 (trap 1).
Usage: pfclimb16.py mode seed secs OUT (seed.pg | --rand n)"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sox, pfx, pg
from soclimb import mutate, dump
NEG = (-10 ** 9,) * 3

def fit(G, mode):
    g = pg.Game(*G)
    if any(not s for s in G[2]) or len(sox.oddchoice(g)) != 1: return NEG, None
    try: r = pfx.analyse(g, cap=3000)
    except AssertionError: raise
    except Exception: return NEG, None
    if mode == "pf": f = (r["pf"], r["pfi"], r["nfb"])
    elif mode == "pfm": f = (r["pf"] if r["nfb"] >= 2 else -10 ** 9, r["nfb"], r["pfi"])
    else: f = (r["rfb0"], r["rfbchk"], r["pf"])
    return f, r

def viol(r, mode): return r["rfb0"] > 0 if mode == "rise" else r["pf"] > r["n"]

if __name__ == "__main__":
    mode, seed, secs, out = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    if sys.argv[5] == "--rand":
        n = int(sys.argv[6])
        while True:
            prio = [rng.randrange(n) for _ in range(n)]; owner = [rng.randrange(2) for _ in range(n)]
            succ = [sorted(set(rng.sample(range(n), 1 if owner[v] else rng.choice((1, 2, 2, 3))))) for v in range(n)]
            o = rng.randrange(n); owner[o] = 1; succ[o] = sorted(set(rng.sample(range(n), max(2, n // 4))))
            G = [prio, owner, succ]; f, r = fit(G, mode)
            if f != NEG: break
    else:
        g = sox.load(sys.argv[5]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f, r = fit(G, mode)
    t0 = time.time(); it = 0; print("start", f, "n", len(G[0]), flush=True); dump(G, out + ".pg")
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh, rh = fit(H, mode)
        if fh != NEG and viol(rh, mode) and fh > f: print(f"VIOLATION it {it} fit {fh} {rh}", flush=True); dump(H, out + "_viol.pg")
        if fh >= f:
            if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh} it/fb {rh['it']}/{rh['fb']} M {rh['M']}", flush=True); dump(H, out + ".pg")
            G, f = H, fh
    print("FINAL", f, it, flush=True)
