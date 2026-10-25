#!/usr/bin/env python3
"""Box 39 (L-RED successor 16): hill-climb on 𝒞^1O, counter = rx16.analyse (own checker). Mutations: soclimb.mutate.
  rise: (RISE-LAST events rfb0, other failures, consecutive in-scope fallback pairs checked, fallbacks)
  rise2: (rfb0, other failures, θ-changes at S4a steps between consecutive in-scope fallbacks, pairs checked)
  tev : (TEV failures, post-rise states checked, pre-rise states whose threat meets Ev, fallback pairs)
  tevl: as tev for TEVLAST (k0 = the last fallback before t)
  conf: (TEVCONF, TEVLAST failures, fallback pairs, TEV-LAST states)
  xrun: (failures, max SN-prefix crossings of one fallback-free run − (n − 1), exit crossings, fallbacks)
  rst : (failures, max #(h)-runs − (1 + toggles + f) per phase, max #(h)-runs, fallback restarts)
A hit (rfb0 > 0, maxpre > n − 1, any failure) is saved as OUT_viol.pg. Invalid sentinel −10^9 (trap 1).
Usage: climb16.py mode seed secs OUT (seed.pg | --rand n)"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sox, rx16, pg
from soclimb import mutate, dump
NEG = (-10 ** 9,) * 4

def fit(G, mode):
    g = pg.Game(*G)
    if any(not s for s in G[2]) or len(sox.oddchoice(g)) != 1: return NEG, None
    try: r = rx16.analyse(g, cap=3000)
    except AssertionError: raise
    except Exception: return NEG, None
    fails = sum(v for k, v in r["C"].items() if k != "RISE")
    if mode == "rise": f = (r["rfb0"], fails, r["rfbchk"], r["fb"])
    elif mode == "rise2": f = (r["rfb0"], fails, r["thin"], r["rfbchk"])
    elif mode == "tev": f = (r["C"].get("TEV", 0), r["tev"], r["tevmeetpre"], r["rfbchk"])
    elif mode == "tevl": f = (r["C"].get("TEVLAST", 0), r["tevlast"], r["tevmeetpre"], r["rfbchk"])
    elif mode == "conf": f = (r["C"].get("TEVCONF", 0), r["tevlastfail"], r["rfbchk"], r["tevlast"])
    elif mode == "xrun": f = (fails + r["rfb0"], r["maxpre"] - (r["n"] - 1), r["exitx"], r["fb"])
    else: f = (fails + r["rfb0"], r["maxslack"], r["maxruns"], r["rst_fb"])
    return f, r

def hit(r): return bool(set(r["C"]) - {"TEV", "TEVLAST"}) or r["maxpre"] > r["n"] - 1   # TEV refuted: tev_cex_n40, tevlast_cex_n40

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
    t0 = time.time(); it = 0; nh = 0; print("start", f, "n", len(G[0]), flush=True); dump(G, out + ".pg")
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh, rh = fit(H, mode)
        if fh != NEG and hit(rh) and nh < 5: nh += 1; print(f"HIT it {it} fit {fh} C {rh['C']} ex {rh['ex']}", flush=True); dump(H, out + f"_viol{nh}.pg")
        if fh >= f:
            if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh} it/fb {rh['it']}/{rh['fb']} maxpre {rh['maxpre']} runs {rh['maxruns']}", flush=True); dump(H, out + ".pg")
            G, f = H, fh
    print("FINAL", f, it, flush=True)
