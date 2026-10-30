#!/usr/bin/env python3
"""L-NEW box 85 (Lemma RET-XIRISE and Theorem FREE-RED, docs/new/N5-FREE-box85.md §2): in every W-run F, the returns of Even X to g are at most XICH_F(g),
the transitions of F at which Xi(g) changes. Checks per (F, X, g) RET <= XICH and that each return interval [s, k] has a strict Xi(g)
rise; prints maxima of RET, XICH_F(e), WCH_F(e). FREE-RED check (R88/R89): RSTAR_F = transitions of F at which some Even y adopts
an edge (y, z) BLOCKED at an earlier state q of F (W_q(z) > W_q(sigma_q y), (y, z) not in I_sigma_q); FL_F = transitions with W unchanged;
violation if |F| > (n - 1)(RSTAR_F + 1) + FL_F. Usage: xirise.py GAME.pg [START]"""
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
XI = [E.evaluate(x)[0] for x in S]
c = dict(ret=0, viol_edge=0, viol_rise=0, viol_fr=0); mx = dict(ret=0, xich=0, wch=0, rstar=0, fl=0, F=0)
IS = {}
def Isig(q):
    if q not in IS: IS[q] = set(E.improving(S[q], XI[q]))
    return IS[q]
for a, b in runs:
    xich = [sum(1 for q in range(a, b) if XI[q + 1][e] != XI[q][e]) for e in range(n)]
    W = [Wv(x, TAU[a]) for x in range(a, b + 1)]
    mx['xich'] = max([mx['xich']] + xich); mx['wch'] = max([mx['wch']] + [sum(1 for i in range(b - a) if W[i + 1][e] != W[i][e]) for e in range(n)])
    blocked = set(); rstar = 0
    for q in range(a, b):
        adopt = any((y, S[q + 1][y]) in blocked for y in ev if S[q + 1][y] != S[q][y])
        rstar += adopt
        for y in ev:
            for z in g.succ[y]:
                if z != S[q][y] and E.key(W[q - a][z]) > E.key(W[q - a][S[q][y]]) and (y, z) not in Isig(q): blocked.add((y, z))
    fl = sum(1 for i in range(b - a) if W[i + 1] == W[i])
    if b - a > (n - 1) * (rstar + 1) + fl: c['viol_fr'] += 1
    mx['rstar'] = max(mx['rstar'], rstar); mx['fl'] = max(mx['fl'], fl); mx['F'] = max(mx['F'], b - a)
    for X in ev:
        held = {S[a][X]}; last = {}; ret = {}
        for k in range(a, b):
            if S[k + 1][X] == S[k][X]: continue
            old, new = S[k][X], S[k + 1][X]; last[old] = k
            if new in held and new in last:
                c['ret'] += 1; ret[new] = ret.get(new, 0) + 1
                if not E.key(XI[k + 1][new]) > E.key(XI[last[new]][new]): c['viol_rise'] += 1
            held.add(new)
        for e, v in ret.items():
            mx['ret'] = max(mx['ret'], v)
            if v > xich[e]: c['viol_edge'] += 1
print(f"XIRISE n {n} runs {len(runs)} {c} maxima {mx}")
