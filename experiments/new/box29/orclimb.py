#!/usr/bin/env python3
"""Box 29 (NH') climb on the part Lemma F1-ext does not bound: max over phases of R-ONLY O' transitions (OTHER-touching,
non-crossing, values change on R ∪ {o} only), then their excess over |R|. Usage: orclimb.py n seed secs out [seed.pg]"""
import sys, os, random, time
from rsplit import *
from climb_fix import mutate

def rfit_g(g):
    return max([(r["Ronly"], r["Ronly"] - r["R"]) for r in rsplit(g)] or [(0, -99)])

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, -99)
    o = odd[0]; g = pg.Game(*G); Y = split(g, o)
    if not any(w in Y for w in G[2][o]): return (-1, -99)
    try: return rfit_g(g)
    except Exception: return (-1, -99)

if __name__ == "__main__":
    n, seed, secs, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    if len(sys.argv) > 5:
        g = load(sys.argv[5]); n = g.n; G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G)
    else:
        while True:
            g = rand_c1o(rng, n, n, forced=0.0)
            if g is None: continue
            G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G)
            if f[0] >= 0: break
    t0 = time.time(); it = 0; print("start", f, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True)
                open(out + ".pg", "w").write(f"parity {n-1};\n" + "".join(f"{v} {H[0][v]} {H[1][v]} {','.join(map(str, H[2][v]))};\n" for v in range(n)))
            G, f = H, fh
    print("FINAL", f, it, flush=True)
