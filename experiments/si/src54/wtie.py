#!/usr/bin/env python3
"""L-SI box 54: the W-rank potential is blind at an Odd source. For Odd V with successors a < b, prints per state whether W(a) == W(b)
(W := val(sigma_k, tau)), and the number of sigmabar(V) changes. On sbq2_K8_m16 (V 260) with the INVALID start (non-edge 242:243): W(242) == W(259) at all 153 states, 128 changes; with the
repaired start sbq2_K8_m16_fix.start: at 0 states, 128 changes (P-N5-ODD fixes entry 4; the W-rank DEAD is withdrawn).
Usage: wtie.py GAME.pg START V"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]); V = int(sys.argv[3]); n = g.n; own = g.owner
sys.path.insert(0, os.path.join(HERE, "..")); from startcheck import check_start; check_start(g, st, sys.argv[2] if len(sys.argv) > 2 else "")  # P-N5-ODD fixes entry 4
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S, TAU = [tuple(s)], [tuple(t)]
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1]))
Wc = {}   # per-state tau_k (P-N5-ODD fixes entry 4: with a valid start tau changes once on sbq2)
def W(x, ta):
    if ta not in Wc: Wc[ta] = Engine(pg.Game(list(g.prio), list(own), [[ta[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[ta].evaluate(x)[0]
a, b = g.succ[V][0], g.succ[V][-1]
tie = sum(W(x, ta)[a] == W(x, ta)[b] for x, ta in zip(S, TAU))
sb = [E.evaluate(x)[1][V] for x in S]
print(f"WTIE {os.path.basename(sys.argv[1])} V {V} succ {a} {b} tau {TAU[0][V]} taus {len(set(TAU))} states {len(S)} Wtie {tie} sbflips {sum(sb[i] != sb[i + 1] for i in range(len(sb) - 1))}")
