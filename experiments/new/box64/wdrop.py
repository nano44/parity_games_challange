#!/usr/bin/env python3
"""L-NEW box 64: inside tau-stretches of plain N5 (S3 start), count W-drop transitions (some vertex's W = val(sigma, tau)
decreases) split by fallback / arena step. Box 21 Lemma W: arena steps never drop. Usage: wdrop.py GAME.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, Engine, dual
import pg
g = load(sys.argv[1]); n = g.n; E, Ed = Engine(g), Engine(dual(g))
s, t = start_pair(g, E, Ed); Wc = {}
def W(s, t):
    t = tuple(t)
    if t not in Wc: Wc[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[t].evaluate(tuple(s))[0], Wc[t]
c = dict(fb=0, fbdrop=0, fbflat=0, arenadrop=0, lwfb=0)
while True:
    r = step(g, E, Ed, list(s), list(t))
    if r is None: break
    ns, nt, _, _, fb, _, _ = r
    if nt == list(t) and ns != list(s):
        w0, Ew = W(s, t); w1, _ = W(ns, t)
        drop = any(Ew.key(w1[x]) < Ew.key(w0[x]) for x in range(n))
        if fb:
            c["fb"] += 1; c["fbdrop"] += drop; c["fbflat"] += (w0 == w1); c["lwfb"] += any(w0[x][0] != w1[x][0] for x in range(n))
        else: c["arenadrop"] += drop
    s, t = ns, nt
print(f"WDROP {os.path.basename(sys.argv[1])} n {n} {c}")
