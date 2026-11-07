#!/usr/bin/env python3
"""L-NEW box 122: per-transition trace of a TWO-FIX window [a, b] (tau, sbar fixed) with ODIFF = 1 at Odd vertex o (sbar(o) != tau(o)).
Columns: j, FB (S4c fallback), XO := Xi(o) changes, WO := W(o) changes, XCH / WCH := vertices whose Xi / W change, D := vertices whose
(sigma_j, sbar)-play passes through o, XDOUT := Xi-changes outside D_j u D_(j+1) (there Xi = W, so these are joint Xi = W rises),
GAP := vertices with Xi != W, WDN := vertices where W falls (expected 0 at non-fallback steps: F2).
Usage: odiff1.py G.pg START a b"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if sys.argv[2] != "-" else None; a0, b0 = int(sys.argv[3]), int(sys.argv[4])
n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g))
s, t = start_pair(g, E, Ed, st); S, T, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(T[-1]))
    if r is None: break
    S.append(tuple(r[0])); T.append(tuple(r[1])); FB.append(r[4])
sb = E.evaluate(S[a0])[1]; tau = T[a0]
O = [v for v in range(n) if own[v] == 1 and sb[v] != tau[v]]; assert len(O) == 1, O; o = O[0]
Wt = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
key = E.key
def through(j):
    f = lambda v: S[j][v] if own[v] == 0 else sb[v]
    D = set()
    for x in range(n):
        y = x; seen = set()
        while y not in seen:
            if y == o: D.add(x); break
            seen.add(y); y = f(y)
    return D
print(f"o {o} sbar(o) {sb[o]} tau(o) {tau[o]} window [{a0}, {b0}]")
tot = dict(fb=0, xo=0, wo=0, wflat=0, xdout=0, wdn=0)
for j in range(a0, b0):
    X0, X1 = E.evaluate(S[j])[0], E.evaluate(S[j + 1])[0]; W0, W1 = Wt.evaluate(S[j])[0], Wt.evaluate(S[j + 1])[0]
    assert E.evaluate(S[j])[1] == sb
    D0, D1 = through(j), through(j + 1)
    xc = [x for x in range(n) if X0[x] != X1[x]]; wc = [x for x in range(n) if W0[x] != W1[x]]
    xdout = [x for x in xc if x not in D0 | D1]; wdn = [x for x in range(n) if key(W1[x]) < key(W0[x])]
    gap = sum(X1[x] != W1[x] for x in range(n))
    tot["fb"] += FB[j]; tot["xo"] += X0[o] != X1[o]; tot["wo"] += W0[o] != W1[o]; tot["wflat"] += not wc; tot["xdout"] += bool(xdout); tot["wdn"] += bool(wdn)
    print(f"j {j} FB {FB[j]} XO {int(X0[o] != X1[o])} WO {int(W0[o] != W1[o])} XCH {len(xc)} WCH {len(wc)} |D| {len(D0)} XDOUT {len(xdout)} GAP {gap} WDN {len(wdn)} sw {[(v, S[j+1][v]) for v in range(n) if S[j][v] != S[j+1][v]]}")
print("TOT", tot)
