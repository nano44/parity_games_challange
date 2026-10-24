#!/usr/bin/env python3
"""Box 26 climb against (ROUTE-BF): o-cyclic C^1O, canonical start. Fitness = max over Even x of the number of strict increases of
x's route value (path to o, Lemma G (c) comparison) inside ONE θ-constant stretch of a (τ, joint-λ)-phase, counted across x's
stays in R (re-entries included), at states satisfying (h) and, with THR (default), θ ◁ w (throttled; unthrottled stretches are R17-bounded via box 21 Lemma PT). Usage: routeclimb.py n seed secs out [--from game.pg]"""
from common import *
from climb_fix import mutate
from thtrace import Rset
from wdrop_h import oncycle
from reentry import path
from collections import Counter
THR = True
def measure(g):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, None); best = 0; key0 = None; last = {}; inc = Counter(); k = 0
    while k < 400:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        h = not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and Xi[o][0] == W[o][0]
        key = ((tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), E.key(Xi[o]))
        if key != key0: last, inc, key0 = {}, Counter(), key
        if h and (THR is False or E.key(Xi[o]) < E.key(W[o])):
            R = Rset(g, s, t, o)
            for x in R:
                if g.owner[x] != 0 or x == o: continue
                p = path(g, s, t, x, o)
                if p is None: continue
                v = W[o]
                for u in reversed(p): v = E.extend(u, v)
                # compare with a common terminal: re-extend the previous path on the current W(o)
                if x in last:
                    v0 = W[o]
                    for u in reversed(last[x]): v0 = E.extend(u, v0)
                    if E.key(v) > E.key(v0): inc[x] += 1; best = max(best, inc[x])
                last[x] = p
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
        g = load(sys.argv[sys.argv.index("--from") + 1]); n = g.n
        G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G)
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
