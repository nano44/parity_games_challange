#!/usr/bin/env python3
"""L-SI box 51b §12 (Lead 14:46Z / 16:10Z, the §9 charge form): at every W-changing transition q -> q+1 of a W-run (as deepint.py), for
every vertex v with a path-set change of depth >= 4 (box 87 definition) or any Xi-change (ALL): ON if some vertex of v's Xi-play at
q (sigma_q, sbar_q) or at q+1 changes W at q (W read with tau), else OFF. Also ONSELF: W(v) itself changes. Prints counts.
Usage: charge.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
a = sys.argv[1:]; g = load(a[0]); n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, readstart(a[1]) if len(a) > 1 else None)
S, TAU, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
T = len(S) - 1; EV = [E.evaluate(x) for x in S]
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
def play(k, v):
    sig, sb = S[k], EV[k][1]; out, x = [], v
    while x not in out: out.append(x); x = sig[x] if own[x] == 0 else sb[x]
    return out
c = dict(D4_ON=0, D4_OFF=0, D4_SELF=0, ALL_ON=0, ALL_OFF=0, ALL_SELF=0)
for k in range(T):
    if not (TAU[k + 1] == TAU[k] and not FB[k] and S[k + 1] != S[k]): continue
    w0, w1 = Wv(k, TAU[k]), Wv(k + 1, TAU[k])
    if [x[0] for x in w0] != [x[0] for x in w1] or w0 == w1: continue
    wch = {u for u in range(n) if w0[u] != w1[u]}
    for v in range(n):
        x0, x1 = EV[k][0][v], EV[k + 1][0][v]
        if x0 == x1: continue
        deep = x0[0] == x1[0] and x0[1] != x1[1] and bin((x0[1] & x1[1]) >> ((x0[1] ^ x1[1]).bit_length())).count("1") >= 4
        on = bool(wch & (set(play(k, v)) | set(play(k + 1, v)))); key = 'SELF' if v in wch else ('ON' if on else 'OFF')
        c['ALL_' + key] += 1
        if deep: c['D4_' + key] += 1
print(f"CHARGE {os.path.basename(a[0])} n {n} " + " ".join(f"{k} {v}" for k, v in c.items()))
