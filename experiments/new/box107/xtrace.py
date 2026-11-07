#!/usr/bin/env python3
"""L-NEW box 107: state-by-state trace of a run: per transition, tau-change / fallback, W-cycle constancy, and every vertex whose Xi or
W changes, with the coordinate of change: C (cycle node), M<r> (highest differing rank r of the path set), L (length).
Usage: xtrace.py GAME.pg [START] [K0 K1]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); a = sys.argv[2:]; st = readstart(a[0]) if a and a[0].endswith(".start") else None
if a and a[0].endswith(".start"): a = a[1:]
k0, k1 = (int(a[0]), int(a[1])) if len(a) >= 2 else (0, 10 ** 9)
n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S, TAU, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
def coord(x, y):
    if x[0] != y[0]: return "C"
    if x[1] != y[1]: return "M%d" % (x[1] ^ y[1]).bit_length()
    return "L"
for k in range(max(0, k0), min(len(S) - 1, k1)):
    tau = TAU[k]; X0, sb0 = E.evaluate(S[k]); X1, sb1 = E.evaluate(S[k + 1]); W0 = Wv(k, tau); W1 = Wv(k + 1, tau)
    wr = TAU[k + 1] == tau and not FB[k] and [x[0] for x in W0] == [x[0] for x in W1]
    sw = [v for v in range(n) if S[k][v] != S[k + 1][v]]
    xc = ["%d:%s" % (v, coord(X0[v], X1[v])) for v in range(n) if X0[v] != X1[v]]
    wc = ["%d:%s" % (v, coord(W0[v], W1[v])) for v in range(n) if W0[v] != W1[v]]
    eqv = sum(1 for v in range(n) if X1[v] == W1[v]); samec = sum(1 for v in range(n) if X1[v][0] == W1[v][0])
    D = [o for o in range(n) if own[o] == 1 and sb1[o] != tau[o]]
    print(f"{k}->{k+1} WRUN {int(wr)} tauchg {int(TAU[k+1] != tau)} fb {FB[k]} sw {sw} XEQW {eqv} SAMEC {samec} D {D}\n   XI {' '.join(xc)}\n   W  {' '.join(wc)}")
