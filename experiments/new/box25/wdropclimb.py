#!/usr/bin/env python3
"""Box 25 climb: o-cyclic C^1O, canonical N5. Fitness = number of Even fallback steps (τ fixed) at which W = V_{σ,τ} drops at some
vertex, inside ONE (τ, joint-λ)-phase (max over phases); ties broken by the total. Usage: wdropclimb.py n seed secs out"""
from common import *
from climb_fix import mutate
def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, -1)
    o = odd[0]; g = pg.Game(*G); Y = split(g, o)
    if not any(w in Y for w in G[2][o]): return (-1, -1)
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, None); per, tot, lam0, k = 0, 0, None, 0; best = 0
    try:
        while k < 400:
            Xi, _ = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); lam = (tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o])
            if lam != lam0: per, lam0 = 0, lam
            r = step(g, E, Ed, s, t)
            if r is None: break
            ns, nt, Is, It, fb, _, _ = r
            if fb and list(nt) == list(t):
                Eg, W0 = wvals(g, s, t); _, W1 = wvals(g, ns, t)
                if any(Eg.key(W1[v]) < Eg.key(W0[v]) for v in range(n)): per += 1; tot += 1; best = max(best, per)
            s, t = ns, nt; k += 1
    except Exception: return (-1, -1)
    return (best, tot)
if __name__ == "__main__":
    n, seed, secs, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
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
    print("FINAL", f, it)
