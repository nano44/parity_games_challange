#!/usr/bin/env python3
"""Box 37 (L-RED): hill-climb on 𝒞^1O against L-NEW's box-33 lemmas, counter = sox2.analyse. Mutations: soclimb.mutate.
  exr : (fails, max over phases of ε-transitions in one fallback-free segment − (d_o − 1), same count, ε in SN)
        (EXIT-R + ORX give <= d_o − 1 per segment; > 0 refutes the pair)
  xsn : (fails, max X_SN per phase, max X)        post: (fails, max crossings after the SN prefix of a run, max X)
Usage: soclimb2.py mode seed secs OUT (seed.pg | --rand n)"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sox, sox2, pg
from soclimb import mutate, dump
NEG = (-10 ** 9,) * 4

def fit(G, mode):
    g = pg.Game(*G)
    if any(not s for s in G[2]) or len(sox.oddchoice(g)) != 1: return NEG, None
    try: r = sox2.analyse(g, cap=3000)
    except AssertionError: raise
    except Exception: return NEG, None
    rs = r["rows"]; fails = sum(r["C"].values())
    mx = lambda f: max((f(x) for x in rs), default=-10 ** 9)
    if mode == "exr": f = (fails, max((x["maxseg"] - (x["d_o"] - 1) for x in rs if x["maxseg"] >= 1), default=-10 ** 9), mx(lambda x: x["maxseg"]), mx(lambda x: x["epsSN"]))
    elif mode == "xsn": f = (fails, mx(lambda x: x["XSN"]), mx(lambda x: x["X"]), 0)
    elif mode == "post": f = (fails, mx(lambda x: x["maxpost"]), mx(lambda x: x["X"]), 0)
    return f, r

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
    t0 = time.time(); it = 0; print("start", f, flush=True); dump(G, out + ".pg")
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh, rh = fit(H, mode)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh} it/fb {rh['it']}/{rh['fb']} C {rh['C']} ex {rh['ex']}", flush=True); dump(H, out + ".pg")
            G, f = H, fh
    print("FINAL", f, it, flush=True)
