#!/usr/bin/env python3
"""L-SI box 54: the W-rank potential is blind at an Odd source. For Odd V with successors a < b, prints per state whether W(a) == W(b)
(W := val(sigma_k, tau)), and the number of sigmabar(V) changes. On sbq2_K8_m16 (V 260): W(242) == W(259) at all 153 states, 128 changes.
Usage: wtie.py GAME.pg START V"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]); V = int(sys.argv[3]); n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S, TAU = [tuple(s)], [tuple(t)]
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1]))
assert len(set(TAU)) == 1
We = Engine(pg.Game(list(g.prio), list(own), [[TAU[0][v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
a, b = g.succ[V][0], g.succ[V][-1]
tie = sum(We.evaluate(x)[0][a] == We.evaluate(x)[0][b] for x in S)
sb = [E.evaluate(x)[1][V] for x in S]
print(f"WTIE {os.path.basename(sys.argv[1])} V {V} succ {a} {b} tau {TAU[0][V]} states {len(S)} Wtie {tie} sbflips {sum(sb[i] != sb[i + 1] for i in range(len(sb) - 1))}")
