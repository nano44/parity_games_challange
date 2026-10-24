#!/usr/bin/env python3
"""Box 29: attack on CONJECTURES (NFB-O) and (WF0). Fitness = (violations: crossing-free S4c fallbacks at OTHER states + W-flat
honest-strict S4a steps, OTHER-touching transitions in the run). Usage: nfbclimb.py n seed secs out [seed.pg]"""
import sys, os, random, time
from otherx import *
from climb_fix import mutate

def vfit_g(g):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, None); viol = otr = 0; k = 0
    while k < 300:
        Xi, sb = E.evaluate(tuple(s)); _, W = wvals(g, s, t)
        Xk = [E.key(Xi[v]) for v in range(g.n)]; Wk = [E.key(W[v]) for v in range(g.n)]
        h = (not oncycle(g, s, sb, o), not oncycle(g, s, t, o), Xi[o][0] == W[o][0]); other = (not all(h)) and Xk != Wk
        r = step(g, E, Ed, s, t)
        if r is None: break
        ns, nt, fb = r[0], r[1], r[4]
        if tuple(nt) == tuple(t) and tuple(ns) != tuple(s):
            Xi2, _ = E.evaluate(tuple(ns)); _, W2 = wvals(g, ns, t)
            if fb and other and reach_o(g, s, t, o) == reach_o(g, ns, t, o): viol += 1
            if not fb and all(E.key(W2[v]) == Wk[v] for v in range(g.n)) and any(E.key(Xi2[v]) != Xk[v] for v in range(g.n)): viol += 1
        otr += other; s, t = ns, nt; k += 1
    return (viol, otr)

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, -1)
    o = odd[0]; g = pg.Game(*G); Y = split(g, o)
    if not any(w in Y for w in G[2][o]): return (-1, -1)
    try: return vfit_g(g)
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
    t0 = time.time(); it = 0; print("start", f, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True)
                open(out + ".pg", "w").write(f"parity {n-1};\n" + "".join(f"{v} {H[0][v]} {H[1][v]} {','.join(map(str, H[2][v]))};\n" for v in range(n)))
            G, f = H, fh
    print("FINAL", f, it, flush=True)
