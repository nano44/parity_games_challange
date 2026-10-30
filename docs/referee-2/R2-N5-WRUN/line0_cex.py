#!/usr/bin/env python3
r"""REFEREE-2 successor 23: independent re-check of REFEREE's G-WRUN-1 instance (wc_line_cex.pg) with my own N5 loop. Blocks under
(a) line 0faa5b80's wording (not improving; play from g reaches X; E0 iff X own cycle node and route below X) and (b) the packet §4.1
definition (also g != sigma_t(X); route avoids X's cycle when X is on it; route pairwise distinct). Reports REG blocks whose (X -> g,
pattern on the route) recurs at a later state (WAIT-CYCLE' fails) under each definition.
Usage: line0_cex.py game.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DUAL"))
import dual_check as DC
from si import Engine
import pg
g = pg.read(sys.argv[1]); n = g.n; E = Engine(g)
s, t = Engine(g).initial("best"), Engine(DC.dual(g)).initial("best")
states, fbs = DC.Runner(g).run(list(s), list(t))
info = []
for sg, tu in states:
    xi, sb = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
    nx = [sg[v] if g.owner[v] == 0 else sb[v] for v in range(n)]
    info.append((sg, xi, set(E.improving(tuple(sg), xi)), nx))
def route(nx, a, X):
    seen, p, x = set(), [], a
    while x != X:
        if x in seen: return None
        seen.add(x); p.append(x); x = nx[x]
    return p
def cyc(nx, v):
    seen, p, x = {}, [], v
    while x not in seen: seen[x] = len(p); p.append(x); x = nx[x]
    return set(p[seen[x]:])
print("states", len(states), "sigma(3) per state", [st[0][3] for st in states])
for mode in ("line0", "packet"):
    bad = []
    for t1, (sg, xi, Is, nx) in enumerate(info):
        for X in range(n):
            if g.owner[X] != 0: continue
            for gg in sorted(set(g.succ[X])):
                if (X, gg) in Is: continue
                if mode == "packet" and gg == sg[X]: continue
                pi = route(nx, gg, X)
                if pi is None: continue
                if mode == "packet" and X in cyc(nx, X) and any(u in cyc(nx, X) for u in pi): continue
                e0 = xi[X][0] == X and all(E.rank[u] < E.rank[X] for u in pi)
                if e0: continue
                pat = [(u, sg[u]) for u in pi if g.owner[u] == 0]
                for t2 in range(t1 + 1, len(info)):
                    s2 = info[t2][0]
                    if s2[X] == gg and all(s2[u] == w for u, w in pat): bad.append((t1, X, gg, pi, t2)); break
    print(mode, "REG-block recurrences", len(bad), bad[:3])
