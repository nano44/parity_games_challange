#!/usr/bin/env python3
"""Box 46 DATA: trace one gap between W-honest states: per state k, honest?, D_k, fallback?, LEV(k) (Xi-level, G_tau paths), WLEV(k)
(the same with W_k in place of Xi_k; W-cycle nodes), and at a fallback the vertices where W drops. Usage: gaptrace.py FILE.pg A B"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import levels as L, hon
from levels import load, step, start_pair, Engine, dual
g = load(sys.argv[1]); A, B = int(sys.argv[2]), int(sys.argv[3])
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, None)
Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]; k = 0; prevw = None
while k <= B:
    vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t); w = hon.wvals(g, s, t)
    if k >= A:
        frame = [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)]
        lv = L.level(E, g, frame, vs, (), 10 ** 8); wl = L.level(E, g, frame, w, (), 10 ** 8)
        drop = [v for v in range(g.n) if prevw and E.key(w[v]) < E.key(prevw[v])]
        D = [q for q in Q if sb[q] != t[q]]
        print(f"state {k}: honest {tuple(vs) == tuple(w)} D {D} fb-out {r[4] if r else '-'} LEV {lv} WLEV {wl} W-drops-at-entry {drop}")
    prevw = w
    if r is None: break
    s, t = r[0], r[1]; k += 1
