#!/usr/bin/env python3
"""Box 41: hill-climb against N5-FBPOLY's THETA-AFTER / FREEZE-EXIT / FB-POLY and FB-CAP (fbpoly17.analyse).
Fitness = (FAILS, max THETA-AFTER slack (#θ-changes after g_{|U|−2} − (deg_U(o) + |U| − 2)), max FB-CAP slack, THAFTER phases at |U| ≥ 3).
START=1: start pair in the genome. Usage: fbpclimb17.py seed secs OUT seed.pg   (env OBJ=fx: fitness (FAILS, max FX slack X − (n(f + X_SN) + n − 1), max X, FB-PHASE slack))"""
import sys, os, random, time, json, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import sox, pg, fbpoly17
from soclimb import mutate, dump
NEG = (-10 ** 9,) * 4
def fit(G, st):
    if any(not s for s in G[2]): return NEG, None
    try:
        g = pg.Game(*G)
        if len(sox.oddchoice(g)) != 1: return NEG, None
        if st is not None and any(st[v] not in g.succ[v] for v in range(g.n)): return NEG, None
        acc = {}
        with contextlib.redirect_stdout(io.StringIO()): fbpoly17.analyse(g, acc, "c", st)
    except Exception: return NEG, None
    F = sum(v for k, v in acc.items() if k.startswith("FAIL"))
    if os.environ.get("OBJ") == "fx": return (F, acc.get("max_FX_slack", -10 ** 6), acc.get("max_X", 0), acc.get("max_FBPHASE_slack", -10 ** 6)), acc
    return (F, acc.get("max_THAFTER_slack", -99), acc.get("max_FBCAP_slack", -99), acc.get("THAFTER_phases_U3+", 0)), acc
if __name__ == "__main__":
    seed, secs, out, f0 = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3], sys.argv[4]; rng = random.Random(seed)
    g = sox.load(f0); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]
    st = [rng.choice(g.succ[v]) for v in range(g.n)] if os.environ.get("START") == "1" else None
    f, r = fit(G, st); print("start", f, flush=True); t0 = time.time(); it = 0; nh = 0
    while time.time() - t0 < secs:
        it += 1
        if st is not None and rng.random() < 1 / 3: H = G; st2 = list(st); v = rng.randrange(len(st2)); st2[v] = rng.choice(G[2][v])
        else:
            H = mutate(rng, G); st2 = None if st is None else [x if x in H[2][v] else rng.choice(H[2][v]) for v, x in enumerate(st)]
        fh, rh = fit(H, st2)
        if fh != NEG and fh[0] > 0 and nh < 6:
            nh += 1; dump(H, f"{out}_hit{nh}.pg"); json.dump(dict(start=st2, acc=rh), open(f"{out}_hit{nh}.json", "w")); print("HIT", nh, it, fh, rh, flush=True)
        if fh >= f:
            if fh > f: print(f"{time.time()-t0:6.0f}s it {it} fit {fh}", flush=True); dump(H, out + ".pg"); json.dump(dict(start=st2), open(out + ".json", "w"))
            G, f, st = H, fh, st2
    print("FINAL", f, it, flush=True)
