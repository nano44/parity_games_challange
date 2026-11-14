#!/usr/bin/env python3
"""L-RED R194 GCH: per maximal FL run of a REAL game (N5 run by r170/freeze.run from the default start pair), the number of gating
changes GCH and of epochs, exactly as L-NEW box132/anchor.py (gating data G_j = (sbar_j on Odd vertices, Xi_j on ODIFF_j, Xi_j on the
W-cycle nodes); epoch = maximal stretch of transitions with the same G); plus MOVMAX (max moves of one Even non-cycle-node vertex in
one run). analyse(g, st=None, cap) -> list of dicts (a, b, fl, gch, epochs, movmax, top) per run. Usage: gch.py G.pg [START|-]"""
import sys, os
H = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(H, "..", "..", "new", "box21"), os.path.join(H, "..", "r170")]
from n5x import load, start_pair, readstart, Engine, dual
import pg
from freeze import run
def analyse(g, st=None, cap=600):
    E0, Ed0 = Engine(g), Engine(dual(g)); s, t = start_pair(g, E0, Ed0, st)
    S, T, F, E = run(g, s, t, cap); n, own, pr = g.n, g.owner, g.prio; Wc = {}
    def weng(tau):
        if tau not in Wc: Wc[tau] = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)]))
        return Wc[tau]
    def wval(j): return weng(T[j]).evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0]
    runs = []; cur = None
    for j in range(1, len(S)):
        if not F[j] and T[j] == T[j - 1] and S[j] != S[j - 1] and wval(j) == wval(j - 1):
            if cur and cur[1] == j - 1: cur[1] = j
            else: cur = [j - 1, j]; runs.append(cur)
    out = []
    for a, b in runs:
        tau = T[a]; W = wval(a); lvl = [W[v][2] for v in range(n)]; CN = [v for v in range(n) if lvl[v] == 0]; gat = {}
        for j in range(a, b + 1):
            vs, sb = E.evaluate(S[j]); od = tuple(sorted(o for o in range(n) if own[o] == 1 and sb[o] != tau[o]))
            gat[j] = (tuple(sb[o] for o in range(n) if own[o] == 1), tuple((o, vs[o]) for o in od), tuple((c, vs[c]) for c in CN))
        s0 = a; nep = 1; ng = 0
        for j in range(a + 1, b + 1):
            if gat[j - 1] != gat[s0]: s0 = j - 1; nep += 1
            if gat[j - 1] != gat[j - 2 if j - 2 >= a else j - 1]: ng += 1
        mv = {}
        for j in range(a + 1, b + 1):
            for x in range(n):
                if own[x] == 0 and lvl[x] > 0 and S[j][x] != S[j - 1][x]: mv[x] = mv.get(x, 0) + 1
        top = max(mv, key=lambda x: (mv[x], lvl[x]), default=-1)
        out.append(dict(a=a, b=b, fl=b - a, gch=ng, epochs=nep, movmax=max(mv.values(), default=0), top=top))
    return out
if __name__ == "__main__":
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
    for r in analyse(g, st): print("GCH", os.path.basename(sys.argv[1]), r)
