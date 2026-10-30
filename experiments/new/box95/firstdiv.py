#!/usr/bin/env python3
"""L-NEW box 95: first iteration at which N5's Even strategy sequence (experiments/new/box21/n5x.py, best-reward start pair) departs from the
I^glo run (box95/hn.py GLO) and from the V1 run (arena optimum against sigma-bar_t), and the tau-changes of N5 before that point.
Usage: firstdiv.py GAME.pg"""
import sys, os
EXP = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
for p in ("si", "harness", "new", "new/box21"): sys.path.insert(0, os.path.join(EXP, p))
import pg
from si import Engine
from n5 import dual
from n5x import load, step, start_pair
g = load(sys.argv[1]); n = g.n; E = Engine(g); Ed = Engine(dual(g))
def onep(sigma, A, oddfix):
    succ = [sorted(A[v]) if g.owner[v] == 0 else [oddfix[v]] for v in range(n)]
    Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
    _, best = Er.evaluate(tuple(oddfix[v] if g.owner[v] == 1 else -1 for v in range(n)))
    return [best[v] if g.owner[v] == 0 else -1 for v in range(n)]
def glo(sigma, A):
    succ = [sorted(A[v]) if g.owner[v] == 0 else list(g.succ[v]) for v in range(n)]
    Er = Engine(pg.Game(list(g.prio), list(g.owner), succ)); s = list(sigma)
    while True:
        vs, _ = Er.evaluate(tuple(s)); Is = Er.improving(tuple(s), vs)
        if not Is: return s
        bw = {}
        for v, w in Is:
            if v not in bw or (Er.key(vs[w]), w) > (Er.key(vs[bw[v]]), bw[v]): bw[v] = w
        for v, w in bw.items(): s[v] = w
def run(mode, cap):
    sigma = list(E.initial("best")); out = [tuple(sigma)]
    while len(out) <= cap:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        if not Is: break
        A = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
        for v, w in Is: A[v].add(w)
        sigma = glo(sigma, A) if mode == "GLO" else onep(sigma, A, sbar); out.append(tuple(sigma))
    return out
s, t = start_pair(g, E, Ed, None); S = [tuple(s)]; TAU = [tuple(t)]
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1]))
ev = [v for v in range(n) if g.owner[v] == 0]
SN = [tuple(x[v] for v in ev) for x in S]
res = {}
for mode in ("GLO", "V1"):
    R = [tuple(x[v] for v in ev) for x in run(mode, len(SN) + 5)]
    k = next((i for i in range(min(len(R), len(SN))) if R[i] != SN[i]), min(len(R), len(SN)))
    res[mode] = k
tch = [i for i in range(len(TAU) - 1) if TAU[i + 1] != TAU[i]]
print(f"FIRSTDIV {os.path.basename(sys.argv[1])} n {n} N5_iter {len(S) - 1} first_div_GLO {res['GLO']} first_div_V1 {res['V1']} N5_tau_changes {len(tch)} first_tau_change {tch[0] + 1 if tch else None}")
