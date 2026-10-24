#!/usr/bin/env python3
"""Box 26 climb: smallest o-cyclic C^1O game (canonical start) with a THETA-class re-entry into R inside a (τ, joint-λ)-phase
(reentry.py's classes). Fitness = (THETA re-entries, THETA re-entries with (h) at leave and re-entry). Stops at the first hit
if --first. Usage: thetareclimb.py n seed secs out [--first]"""
from common import *
from climb_fix import mutate
from reentry import run
from collections import Counter
def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, -1)
    g = pg.Game(*G)
    if not any(w in split(g, odd[0]) for w in G[2][odd[0]]): return (-1, -1)
    c = Counter()
    try: run(g, None, c)
    except Exception: return (-1, -1)
    return (c["THETA"], c["THETA"] - c["THETA_noh"])
if __name__ == "__main__":
    n, seed, secs, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; first = "--first" in sys.argv
    rng = random.Random(seed)
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
        if first and f[1] > 0: break
    print("FINAL", f, it)
