#!/usr/bin/env python3
"""Box 41 (L-RED successor 17): hill-climb on 𝒞^1O into the post-freeze regimes of P-FREEZE (θ-run with > |U| − 1 fallbacks... i.e.
#fallbacks f ≥ |U| − 1, then states after f_{|U|−1}) and HAT-FREEZE (phase with g ≥ |U| − 2). Checker: pfz17.analyse.
Modes: pf  score (FAILS, maxU with pfz excess ≥ 0, best pfz excess over runs with |U| > that maxU (capped at 0), post states)
       hat score (FAILS, maxU with hat excess ≥ 0, best hat excess over phases with |U| > that maxU, HF post states)
       hath1 as hat but a phase counts as reached only with an H1 state after g_{|U|−2}.
Mutations: soclimb.mutate. Hits (FAILS > 0) saved as OUT_viol*.pg. Usage: climb17.py mode seed secs OUT (seed.pg | --rand n)"""
import sys, os, random, time, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import sox, pfz17, pg
from soclimb import mutate, dump
NEG = (-10 ** 9,) * 4

def fit(G, mode):
    g = pg.Game(*G)
    if any(not s for s in G[2]) or len(sox.oddchoice(g)) != 1: return NEG, None
    acc = {}
    try:
        with contextlib.redirect_stdout(io.StringIO()): pfz17.analyse(g, acc, "c")
    except AssertionError: raise
    except Exception: return NEG, None
    fails = sum(v for k, v in acc.items() if k.startswith("FAIL"))
    key = "max_pfz_excess_U" if mode in ("pf", "pftriv") else "max_hat_excess_U"
    ex = {int(k[len(key):]): v[0] for k, v in acc.items() if k.startswith(key)}
    pre = "PF_post_nontriv_U" if mode == "pf" else "HF_post_nontriv_U"
    reached = [int(k[len(pre):]) for k, v in acc.items() if k.startswith(pre) and v > 0]
    if mode == "pftriv": reached = [u for u, e in ex.items() if e >= 0]
    reached = [u for u in reached if u >= 3]
    mu = max(reached, default=2)
    nxt = max((min(e, 0) for u, e in ex.items() if u > mu), default=-99)
    post = sum(v for k, v in acc.items() if k.startswith("PF_tr_U" if mode in ("pf", "pftriv") else "HF_post_U") and int(k.split("_U")[1]) >= 3)
    return (fails, mu, nxt, post), acc

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
        if fh != NEG and fh[0] > 0 and nh < 5:
            nh += 1; print(f"HIT it {it} fit {fh}", {k: v for k, v in rh.items() if k.startswith("FAIL")}, flush=True); dump(H, out + f"_viol{nh}.pg")
        if fh >= f:
            if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); dump(H, out + ".pg")
            G, f = H, fh
    print("FINAL", f, it, flush=True)
