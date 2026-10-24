#!/usr/bin/env python3
"""Box 25 climb against (FB-H): o-cyclic C^1O, random start pair (part of the genome). Fitness = (number of fallbacks at states
satisfying (h) that LOWER W, number of fallbacks at (h)-throttled states). A first component > 0 refutes (FB-H).
Usage: fbhclimb.py n seed secs out"""
from common import *
from climb_fix import mutate
from wdrop_h import oncycle
from abovefind import write
def fit(G, S):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, -1)
    o = odd[0]; g = pg.Game(*G)
    if not any(w in split(g, o) for w in G[2][o]): return (-1, -1)
    st = ({v: (S[v] if S[v] in G[2][v] else G[2][v][0]) for v in range(n) if G[1][v] == 0}, {o: S[o] if S[o] in G[2][o] else G[2][o][0]})
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); d = th = 0; k = 0
    try:
        while k < 300:
            r = step(g, E, Ed, s, t)
            if r is None: break
            ns, nt, Is, It, fb, vs, _ = r
            if fb and list(nt) == list(t):
                _, sb = E.evaluate(tuple(s)); Eg, W0 = wvals(g, s, t)
                if not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and vs[o][0] == W0[o][0] and E.key(vs[o]) < Eg.key(W0[o]):
                    th += 1; _, W1 = wvals(g, ns, t)
                    if any(Eg.key(W1[v]) < Eg.key(W0[v]) for v in range(n)): d += 1
            s, t = ns, nt; k += 1
    except Exception: return (-1, -1)
    return (d, th), st
if __name__ == "__main__":
    n, seed, secs, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    def F(G, S):
        r = fit(G, S); return r if len(r) == 2 and isinstance(r[0], tuple) else ((-1, -1), None)
    while True:
        g = rand_c1o(rng, n, n, forced=0.0)
        if g is None: continue
        G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; S = [rng.choice(x) for x in G[2]]; f, st = F(G, S)
        if f[0] >= 0: break
    t0 = time.time(); it = 0
    while time.time() - t0 < secs:
        if rng.random() < 0.3:
            H = G; T = list(S); v = rng.randrange(n); T[v] = rng.choice(G[2][v])
        else:
            H = mutate(rng, G); T = S
        it += 1; fh, sth = F(H, T)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); write(pg.Game(*H), sth, out)
            G, S, f = H, T, fh
        if f[0] > 0: break
    print("FINAL", f, it)
