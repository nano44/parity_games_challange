#!/usr/bin/env python3
"""L-NEW box 128: witness for the failure of the per-h count STRICT_h <= LC_h (pcount.py LEADVIOL) on one game: the (stretch, h) with the
largest excess; prints h's move sequence (transition, old -> new, classes, W-strict) and the Xi-cycle-node changes of its classes.
Usage: witness.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "red", "r170")); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, start_pair, readstart, Engine, dual
import pg
from freeze import run, windows, frozen
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
E0, Ed0 = Engine(g), Engine(dual(g)); s, t = start_pair(g, E0, Ed0, st)
S, T, F, E = run(g, s, t); W, SB = windows(g, S, T, E); n, own, pr = g.n, g.owner, g.prio
best = None
for a, b in W:
    if b - a < 1: continue
    gf = frozen(g, SB[a], T[a]); tau = T[a]; sb = SB[a]
    EW = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)]))
    EX = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [sb[v]] for v in range(n)]))
    WV = {j: EW.evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0] for j in range(a, b + 1)}
    XV = {j: EX.evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0] for j in range(a, b + 1)}
    def cls(h, x):
        v, seen = x, {h}
        while len(gf.succ[v]) == 1:
            if v in seen: return None
            seen.add(v); v = gf.succ[v][0]
        return None if v in seen else v
    st_ = []; p = a
    for j in range(a + 1, b + 1):
        if F[j]: st_.append((p, j - 1)); p = j
    st_.append((p, b))
    for p, q in st_:
        for h in range(n):
            if own[h] != 0: continue
            L = [(j, S[j - 1][h], S[j][h]) for j in range(p + 1, q + 1) if S[j][h] != S[j - 1][h]]
            if not L: continue
            strict = sum(EW.key(WV[j][w]) > EW.key(WV[j][o]) for j, o, w in L)
            cl = {cls(h, x) for x in g.succ[h]}
            lam = {X: [k + 1 for k in range(p, q) if XV[k][X][0] != XV[k + 1][X][0]] for X in cl if X is not None}
            lc = sum(1 + len(v) for v in lam.values()) + (None in cl)
            if best is None or strict - lc > best[0]: best = (strict - lc, a, b, p, q, h, L, lam, lc, strict, {x: cls(h, x) for x in g.succ[h]}, WV, EW)
ex, a, b, p, q, h, L, lam, lc, strict, cmap, WV, EW = best
print(f"WITNESS {os.path.basename(sys.argv[1])} n {n} window [{a},{b}] stretch [{p},{q}] h {h} (prio {pr[h]}) STRICT {strict} LC {lc} EXCESS {ex}")
print(f"  successors -> class: {cmap}")
print(f"  Xi-cycle-node changes of each class X in the stretch (transitions): {lam}")
for j, o, w in L:
    print(f"  move @{j}: {o} (class {cmap[o]}) -> {w} (class {cmap[w]}) W-strict {EW.key(WV[j][w]) > EW.key(WV[j][o])}")
