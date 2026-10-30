#!/usr/bin/env python3
"""L-NEW box 92 (P-N5-WRUN §3, Theorem XI-RUN): in every W-run F of N5, |F| <= m_E + sum_c d_E(c) * XICH_F(c), XICH_F(c) the transitions of F
at which Xi(c) changes (RESULTS R86 SW-RETURN on the stretch F, plus: every transition of a W-run switches some Even vertex). Also checks
the switch-count form |F| <= sum_v SW_F(v) and per Even edge ENT_F(v, c) <= 1 + XICH_F(c). W-run segmentation as box85/xirise.py.
Usage: xirun.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); start = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); S = [tuple(s)]; TAU = [tuple(t)]; FB = []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
T = len(S) - 1; ev = [v for v in range(n) if g.owner[v] == 0]
mE = sum(len(g.succ[v]) for v in ev); dE = [0] * n
for v in ev:
    for c in g.succ[v]: dE[c] += 1
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
runs = []; cur = None
for k in range(T):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
    if not ok: cur = None; continue
    if cur is None: cur = [k, k]; runs.append(cur)
    cur[1] = k + 1
XI = [E.evaluate(x)[0] for x in S]
c = dict(noswitch=0, viol_sw=0, viol_ent=0, viol_xirun=0); mx = dict(F=0, xich=0, bound=0, ratio=0.0)
for a, b in runs:
    xich = [sum(1 for q in range(a, b) if XI[q + 1][e] != XI[q][e]) for e in range(n)]
    sw = 0; ent = {}
    for q in range(a, b):
        moved = [y for y in ev if S[q + 1][y] != S[q][y]]
        if not moved: c['noswitch'] += 1
        sw += len(moved)
        for y in moved: ent[(y, S[q + 1][y])] = ent.get((y, S[q + 1][y]), 0) + 1
    F = b - a; bound = mE + sum(dE[e] * xich[e] for e in range(n))
    if F > sw: c['viol_sw'] += 1
    c['viol_ent'] += sum(1 for (y, z), k in ent.items() if k > 1 + xich[z])
    if F > bound: c['viol_xirun'] += 1
    mx['F'] = max(mx['F'], F); mx['xich'] = max([mx['xich']] + xich); mx['bound'] = max(mx['bound'], bound)
    mx['ratio'] = max(mx['ratio'], round(F / bound, 3))
print(f"XIRUN n {n} mE {mE} runs {len(runs)} {c} maxima {mx}")
