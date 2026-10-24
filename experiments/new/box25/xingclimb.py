#!/usr/bin/env python3
"""Box 26 climb against (XING): o-cyclic C^1O, canonical start. Fitness = (max crossings of one vertex inside one
(τ, joint-λ, θ, w)-stretch with (h) and θ ◁ w (throttled; unthrottled stretches are R17-bounded), max crossing transitions per such stretch). Usage: xingclimb.py n seed secs out [--from g.pg]"""
from common import *
from climb_fix import mutate
from thtrace import Rset
from wdrop_h import oncycle
from collections import Counter
def measure(g):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, None); prev = None; per = Counter(); tot = bt = bv = 0; k = 0
    while k < 300:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        h = not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and Xi[o][0] == W[o][0] and E.key(Xi[o]) < E.key(W[o])
        cur = (((tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), E.key(Xi[o]), E.key(W[o])), h, Rset(g, s, t, o))
        if prev is not None:
            if prev[0] != cur[0] or not (prev[1] and cur[1]): per = Counter(); tot = 0
            else:
                d = prev[2] ^ cur[2]
                if d:
                    tot += 1; bt = max(bt, tot)
                    for x in d: per[x] += 1
                    bv = max(bv, max(per.values()))
        prev = cur
        r = step(g, E, Ed, s, t)
        if r is None: break
        s, t = list(r[0]), list(r[1]); k += 1
    return (bv, bt)
def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, -1)
    g = pg.Game(*G)
    if not any(w in split(g, odd[0]) for w in G[2][odd[0]]): return (-1, -1)
    try: return measure(g)
    except Exception: return (-1, -1)
if __name__ == "__main__":
    n, seed, secs, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    if "--from" in sys.argv:
        g = load(sys.argv[sys.argv.index("--from") + 1]); n = g.n; G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G)
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
    print("FINAL", f, it)
