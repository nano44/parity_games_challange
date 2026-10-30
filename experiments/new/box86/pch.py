#!/usr/bin/env python3
"""L-NEW box 86 (Theorem RSTAR-PCH, docs/new/N5-RSTAR-box86.md §3). Per W-run F of N5: for each vertex z, LCH_F(z) = transitions where
lambda(Xi(z)) changes, PCH_F(z) = transitions where the path set of Xi(z) changes with lambda unchanged, LEN_F(z) = transitions where only
the length changes, XICH_F(z) = their sum. Checks (i) the whole-run count of lambda(Xi(z)) values <= n per vertex; (ii) LEN changes inside
one (lambda, P) block <= n - 1; (iii) XICH_F(z) <= n (n + PCH_F(z)); (iv) R*_F <= m_E n (n + max_z PCH_F(z)) (R*_F as box86/rstar.py).
Prints maxima. Usage: pch.py GAME.pg [START]"""
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
T = len(S) - 1; ev = [v for v in range(n) if g.owner[v] == 0]; mE = sum(len(g.succ[v]) for v in ev)
XI = [E.evaluate(x)[0] for x in S]
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
c = dict(lam_viol=0, len_viol=0, xich_viol=0, rstar_viol=0)
for z in range(n):
    if len({XI[k][z][0] for k in range(T + 1)}) > n: c['lam_viol'] += 1
runs = []; cur = None
for k in range(T):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and S[k + 1] != S[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
    if not ok: cur = None; continue
    if cur is None: cur = [k, k]; runs.append(cur)
    cur[1] = k + 1
mx = dict(lch=0, pch=0, len=0, xich=0, rstar=0, n=n)
for a, b in runs:
    W = [Wv(q, TAU[a]) for q in range(a, b + 1)]; pchmax = 0
    for z in range(n):
        lch = pch = ln = 0; blk = 0
        for q in range(a, b):
            x0, x1 = XI[q][z], XI[q + 1][z]
            if x0 == x1: continue
            if x0[0] != x1[0]: lch += 1; blk = 0
            elif x0[1] != x1[1]: pch += 1; blk = 0
            else:
                ln += 1; blk += 1
                if blk > n - 1: c['len_viol'] += 1
        if lch + pch + ln > n * (n + pch): c['xich_viol'] += 1
        pchmax = max(pchmax, pch)
        mx['lch'] = max(mx['lch'], lch); mx['pch'] = max(mx['pch'], pch); mx['len'] = max(mx['len'], ln); mx['xich'] = max(mx['xich'], lch + pch + ln)
    Is = {q: set(E.improving(S[q], XI[q])) for q in range(a, b + 1)}; blocked = set(); rstar = 0
    for q in range(a, b):
        if any((y, S[q + 1][y]) in blocked for y in ev if S[q + 1][y] != S[q][y]): rstar += 1
        for y in ev:
            for z in g.succ[y]:
                if z != S[q][y] and E.key(W[q - a][z]) > E.key(W[q - a][S[q][y]]) and (y, z) not in Is[q]: blocked.add((y, z))
    if rstar > mE * n * (n + pchmax): c['rstar_viol'] += 1
    mx['rstar'] = max(mx['rstar'], rstar)
print(f"PCH n {n} runs {len(runs)} {c} maxima {mx}")
