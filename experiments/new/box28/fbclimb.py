#!/usr/bin/env python3
"""Box 28 (FB-run) climb: o-cyclic C^1O, canonical N5 start. Fitness = max over (w, u*)-runs (fbre.py definition, u* ≠ None) of the
number of NON-FLAT fallbacks (fallbacks that change Ξ or W), then FBRE in that run, then θ-changes.
With env FIT=p: re-entries of POST-freeze fallback evictees (CONJECTURE FBRE-F says 0), then post-freeze evictions, then run length.
With env FIT=v: max FBRE of one vertex in one run, then FBRE, then non-flat fallbacks. Usage: fbclimb.py n seed secs out [seed.pg]  (with seed.pg: start the climb from that game; n is then its size)"""
import sys, os, random, time
from fbre import *
from climb_fix import mutate

def fbfit(g, start=None):
    best = (0, 0, 0)
    for (k, j, rows) in runs_of(g, start):
        if rows[k]["u"] is None or j == k: continue
        nf = sum(1 for i in range(k, j) if rows[i]["fb"] and (rows[i]["Xk"] != rows[i + 1]["Xk"] or rows[i]["Wk"] != rows[i + 1]["Wk"]))
        s = stats(k, j, rows)
        post = s["FBRE"] - sum(v for kk, v in s.items() if kk.startswith("FBRE_") and kk.endswith("prefreeze"))
        if os.environ.get("FIT") == "p": best = max(best, (post, s.get("evict_postfreeze", 0), j - k))
        else: best = max(best, (s["maxFBREv"], s["FBRE"], nf) if os.environ.get("FIT") == "v" else (nf, s["FBRE"], s["tc"]))
    return best

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, -1, -1)
    o = odd[0]; g = pg.Game(*G); Y = split(g, o)
    if not any(w in Y for w in G[2][o]): return (-1, -1, -1)
    try: return fbfit(g)
    except Exception: return (-1, -1, -1)

if __name__ == "__main__":
    n, seed, secs, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    while len(sys.argv) > 5:
        g = load(sys.argv[5]); n = g.n; G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G); break
    while len(sys.argv) <= 5:
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
