#!/usr/bin/env python3
"""Box 27 climb for (CYC'): o-cyclic C^1O, canonical start. Fitness = max over joint λ-phases (τ fixed) of the number of (θ, w)-stretches
(1 + θ-changes + w-changes, counted as changes of the pair). Usage: stretchclimb.py n seed secs out [--from g.pg]"""
from common import *
from climb_fix import mutate
def measure(g):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, None); prev = None; cur = best = 0; k = 0
    while k < 400:
        Xi, _ = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        key = ((tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), E.key(Xi[o]), E.key(W[o]))
        if prev is None or key[0] != prev[0]: cur = 1
        elif key[1:] != prev[1:]: cur += 1
        best = max(best, cur); prev = key
        r = step(g, E, Ed, s, t)
        if r is None: break
        s, t = list(r[0]), list(r[1]); k += 1
    return best
def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return -1
    g = pg.Game(*G)
    if not any(w in split(g, odd[0]) for w in G[2][odd[0]]): return -1
    try: return measure(g)
    except Exception: return -1
if __name__ == "__main__":
    n, seed, secs, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    if "--from" in sys.argv:
        g = load(sys.argv[sys.argv.index("--from") + 1]); n = g.n; G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G)
    else:
        while True:
            g = rand_c1o(rng, n, n, forced=0.0)
            if g is None: continue
            G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G)
            if f >= 0: break
    t0 = time.time(); it = 0
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True)
                open(out + ".pg", "w").write(f"parity {n-1};\n" + "".join(f"{v} {H[0][v]} {H[1][v]} {','.join(map(str, H[2][v]))};\n" for v in range(n)))
            G, f = H, fh
    print("FINAL", f, it)
