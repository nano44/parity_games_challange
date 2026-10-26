#!/usr/bin/env python3
"""Box 44 DATA: per phase ((lambda_Xi, tau) constant), the number of in-phase S4c fallbacks and of cross-terminal switches among
them (x in R_D, z in R_D, u(z) != u(x), (hD) and (h3D) at the fallback state; = crd.py DIFFSW), and the phase length.
Usage: swphase.py FILE.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, HERE)
from multi import pg
from n5x import load, step, start_pair, Engine, dual
from f1d import hD
from crd import term
for f in sys.argv[1:]:
    g = load(f); E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, None); ph = []; cur = None; it = 0
    while True:
        vs, sb = E.evaluate(tuple(s)); D = frozenset(u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u]); U = term(g, s, t, D)
        gt = pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if g.owner[v] == 0 else [t[v]] for v in range(g.n)])
        W, _ = Engine(gt).evaluate(tuple(s[v] if g.owner[v] == 0 else -1 for v in range(g.n)))
        key = (tuple(x[0] for x in vs), tuple(t))
        if key != cur: ph.append([0, 0, 0]); cur = key
        r = step(g, E, Ed, s, t)
        if r is None: break
        vs2, _ = E.evaluate(tuple(r[0])); inph = (tuple(x[0] for x in vs2), tuple(r[1])) == key
        if inph: ph[-1][0] += 1
        if r[4] and inph:
            ph[-1][1] += 1
            if hD(g, s, t, sb, D) and all(vs[u][0] == W[u][0] for u in D):
                ph[-1][2] += sum(1 for x in range(g.n) if g.owner[x] == 0 and r[0][x] != s[x] and U[x] is not None and U[r[0][x]] is not None and U[r[0][x]] != U[x])
        s, t = r[0], r[1]; it += 1
    best = max(ph, key=lambda p: p[2])
    print(f"{os.path.basename(f)} n {g.n} iterations {it} phases {len(ph)}; max cross-terminal switches in one phase {best[2]} (that phase: {best[0]} transitions, {best[1]} fallbacks); total {sum(p[2] for p in ph)}; max fallbacks in a phase {max(p[1] for p in ph)}")
