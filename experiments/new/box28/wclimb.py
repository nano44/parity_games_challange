#!/usr/bin/env python3
"""Box 28 (W) climb: o-cyclic C^1O, canonical N5 start. Fitness = max over phases (λ_Ξ, λ_U, τ(o) constant) of the number of
w-changes (w = W(o)) at transitions with (h) at both endpoints and a THROTTLED endpoint (θ ≠ w; w-changes inside Ξ = W runs are
harmless by Lemma EQ), then θ-changes in that phase. Usage: wclimb.py n seed secs out [seed.pg]"""
import sys, os, random, time
from nhprof import *
from climb_fix import mutate

def wfit_g(g):
    rows, ph = profile(g); best = (0, 0)
    for (x, y) in ph:
        thr = lambda r: all(r["h"]) and r["th"] != r["w"]
        wc = sum(1 for k in range(x, y) if all(rows[k]["h"]) and all(rows[k + 1]["h"]) and rows[k]["w"] != rows[k + 1]["w"]
                 and (thr(rows[k]) or thr(rows[k + 1])))
        tc = sum(1 for k in range(x, y) if rows[k]["th"] != rows[k + 1]["th"])
        best = max(best, (wc, tc))
    return best

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, -1)
    o = odd[0]; g = pg.Game(*G); Y = split(g, o)
    if not any(w in Y for w in G[2][o]): return (-1, -1)
    try: return wfit_g(g)
    except Exception: return (-1, -1)

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
    t0 = time.time(); it = 0
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True)
                open(out + ".pg", "w").write(f"parity {n-1};\n" + "".join(f"{v} {H[0][v]} {H[1][v]} {','.join(map(str, H[2][v]))};\n" for v in range(n)))
            G, f = H, fh
    print("FINAL", f, it, flush=True)
