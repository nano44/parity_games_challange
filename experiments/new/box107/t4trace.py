#!/usr/bin/env python3
"""L-NEW box 107: trace the T4 transitions of finpot.py (W changes, BW flat, A does not fall). Per W-changed vertex v: b = lcp(CS W_k v,
CS W_q v), i = first position where W_k(v), W_(k+1)(v) differ (0 = cycle reward, 1..n = ranks top-down, n+1 = length), and
a0/a1 = lcp(CS Xi, CS W) before/after. Usage: t4trace.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S, TAU, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
def cs(v):
    c, m, l = v
    return (E.rew[c],) + tuple(((1 if E.rankpar[r] == 0 else -1) if (m >> r) & 1 else 0) for r in range(n - 1, -1, -1)) + ((l if E.par[c] == 1 else -l),)
def lcp(a, b):
    i = 0
    while i < len(a) and a[i] == b[i]: i += 1
    return i
runs = []
for k in range(len(S) - 1):
    if TAU[k + 1] != TAU[k] or FB[k] or [x[0] for x in Wv(k, TAU[k])] != [x[0] for x in Wv(k + 1, TAU[k])]: continue
    if runs and runs[-1][-1] == k - 1: runs[-1].append(k)
    else: runs.append([k])
for run in runs:
    tau = TAU[run[0]]; q = run[-1] + 1; WQ = [cs(x) for x in Wv(q, tau)]
    print(f"RUN {run[0]}..{q}")
    for k in run:
        X0 = [cs(x) for x in E.evaluate(S[k])[0]]; X1 = [cs(x) for x in E.evaluate(S[k + 1])[0]]
        W0 = [cs(x) for x in Wv(k, tau)]; W1 = [cs(x) for x in Wv(k + 1, tau)]
        A0 = sum(lcp(X0[v], W0[v]) for v in range(n)); A1 = sum(lcp(X1[v], W1[v]) for v in range(n))
        B0 = sum(lcp(W0[v], WQ[v]) for v in range(n)); B1 = sum(lcp(W1[v], WQ[v]) for v in range(n))
        cat = "T1" if W0 == W1 else "T2" if B1 > B0 else "T3" if A1 < A0 else "T4"
        line = f" {k}->{k+1} {cat} A {A0}->{A1} BW {B0}->{B1} sw {[v for v in range(n) if S[k][v] != S[k+1][v]]}"
        if cat == "T4":
            det = [f"{v}:b{lcp(W0[v], WQ[v])},i{lcp(W0[v], W1[v])},a{lcp(X0[v], W0[v])}>{lcp(X1[v], W1[v])}" for v in range(n) if W0[v] != W1[v]]
            xd = [f"{v}:i{lcp(X0[v], X1[v])}" for v in range(n) if X0[v] != X1[v]]
            line += "\n    W " + " ".join(det) + "\n    XI " + " ".join(xd)
        print(line)
