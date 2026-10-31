#!/usr/bin/env python3
"""L-NEW box 90 (SB-POLY, mechanism O): per W-run F of N5 (R89), SB_F = transitions at which sigmabar changes at some Odd vertex, and
SBV_F(o) = transitions at which sigmabar(o) changes, for each Odd o; also the number of distinct sigmabar(o) values and RET_F(o) = returns
of sigmabar(o) to a successor it held earlier in F. Prints max SB_F, SB_F / n, max SBV_F(o), max RET, the Odd out-degree max.
Usage: sbv.py GAME.pg [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); start = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); S = [tuple(s)]; TAU = [tuple(t)]; FB = []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
T = len(S) - 1; od = [v for v in range(n) if g.owner[v] == 1]
SB = [E.evaluate(x)[1] for x in S]
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
runs = []; cur = None
for k in range(T):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and S[k + 1] != S[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
    if not ok: cur = None; continue
    if cur is None: cur = [k, k]; runs.append(cur)
    cur[1] = k + 1
mx = dict(sb=0, sbv=0, ret=0, F=0); argo = None
for a, b in runs:
    sb = sum(1 for q in range(a, b) if SB[q + 1] != SB[q]); mx['sb'] = max(mx['sb'], sb); mx['F'] = max(mx['F'], b - a)
    for o in od:
        ch = [q for q in range(a, b) if SB[q + 1][o] != SB[q][o]]
        held = {SB[a][o]}; ret = 0
        for q in ch:
            if SB[q + 1][o] in held: ret += 1
            held.add(SB[q + 1][o])
        if len(ch) > mx['sbv']: mx['sbv'] = len(ch); argo = o
        mx['ret'] = max(mx['ret'], ret)
dmax = max([len(g.succ[o]) for o in od] + [0])
print(f"SBV n {n} runs {len(runs)} maxima {mx} sb/n {mx['sb'] / n:.2f} odd-outdeg {dmax} argmax-odd {argo}")
