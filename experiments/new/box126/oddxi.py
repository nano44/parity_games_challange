#!/usr/bin/env python3
"""L-NEW box 126: Xi-changes at Odd vertices. For every transition k -> k+1 and Odd v with Xi_(k+1)(v) != Xi_k(v) (an XCH event of v):
MINRISE := Xi of v's current minimiser w0 := sbar_k(v) also changes at k (Xi_(k+1)(w0) != Xi_k(w0)); SBMOVE := sbar(v) moves at k;
for every sbar-move at v (with or without an Xi(v) change), OLDROSE := Xi(w0) changed at k (Lemma MIN-SWITCH predicts OLDROSE unless the
move is FLAT). CHAIN := the length of the charge chain x_0 = v, x_(i+1) := sbar_k(x_i) (Odd) or sigma_k(x_i) (Even), followed while
Xi(x_i) changes at k, until an Even vertex switched at k (END=SW) or a repeat (END=CYC: the change enters through the play's cycle).
Per Odd vertex: XCH, deg, and the number of distinct successors ever used as minimiser (USED).
Usage: oddxi.py G.pg [START|-] [TOP]   prints one ODDXI line, then the TOP (default 3) Odd vertices by XCH."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
TOP = int(sys.argv[3]) if len(sys.argv) > 3 else 3
n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g))
s, t = start_pair(g, E, Ed, st); S = [tuple(s)]; T = [tuple(t)]
while True:
    r = step(g, E, Ed, list(S[-1]), list(T[-1]))
    if r is None: break
    S.append(tuple(r[0])); T.append(tuple(r[1]))
K = len(S) - 1; EV = [E.evaluate(x) for x in S]
Odd = [v for v in range(n) if own[v] == 1]
xch = {v: 0 for v in Odd}; used = {v: set() for v in Odd}; tot = dict(ev=0, minrise=0, sbmove=0, moves=0, oldrose=0, flatmoves=0, sw=0, cyc=0, maxchain=0)
for k in range(K + 1):
    for v in Odd: used[v].add(EV[k][1][v])
for k in range(K):
    X0, X1 = EV[k][0], EV[k + 1][0]; sb0, sb1 = EV[k][1], EV[k + 1][1]
    sw = {v for v in range(n) if own[v] == 0 and S[k][v] != S[k + 1][v]}
    for v in Odd:
        w0 = sb0[v]; ch = X0[v] != X1[v]; mv = sb0[v] != sb1[v]
        if mv:
            tot["moves"] += 1; tot["oldrose"] += X0[w0] != X1[w0]; tot["flatmoves"] += not ch
        if not ch: continue
        xch[v] += 1; tot["ev"] += 1; tot["minrise"] += X0[w0] != X1[w0]; tot["sbmove"] += mv
        x = v; seen = []; L = 0; end = None
        while True:
            if x in sw: end = "sw"; break
            if x in seen: end = "cyc"; break
            seen.append(x); nx = S[k][x] if own[x] == 0 else sb0[x]
            if X0[nx] == X1[nx] and nx not in sw: end = "stop"; break
            x = nx; L += 1
        tot[end] = tot.get(end, 0) + 1; tot["maxchain"] = max(tot["maxchain"], L)
print(f"ODDXI {os.path.basename(sys.argv[1])} n {n} K {K} XCHodd {tot['ev']} MINRISE {tot['minrise']} SBMOVE {tot['sbmove']} MOVES {tot['moves']} "
      f"OLDROSE {tot['oldrose']} FLATMOVES {tot['flatmoves']} END sw {tot.get('sw', 0)} cyc {tot.get('cyc', 0)} stop {tot.get('stop', 0)} MAXCHAIN {tot['maxchain']}")
for v in sorted(Odd, key=lambda v: -xch[v])[:TOP]:
    print(f"  odd {v} deg {len(g.succ[v])} XCH {xch[v]} USED {len(used[v])}")
