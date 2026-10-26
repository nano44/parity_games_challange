#!/usr/bin/env python3
"""Delta-reduce a game: delete edges (out-degree stays >= 1) while the longest phase stays >= THR. The start pair keeps only valid
entries (start_pair fills the rest by best reward). Usage: shrink.py GAME START THR OUT"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n3x, pg
from phclimb import fit, save
g = n3x.load(sys.argv[1]); st = n3x.readstart(sys.argv[2]); thr = int(sys.argv[3]); out = sys.argv[4]
def ok(h, s):
    f = fit(h, s, 10 ** 9); return f is not None and f[0] >= thr
changed = True
while changed:
    changed = False
    for v in range(g.n):
        for w in list(g.succ[v]):
            if len(g.succ[v]) == 1: break
            succ = [list(x) for x in g.succ]; succ[v] = [x for x in succ[v] if x != w]
            h = pg.Game(list(g.prio), list(g.owner), succ)
            s = ({a: b for a, b in st[0].items() if b in h.succ[a]}, {a: b for a, b in st[1].items() if b in h.succ[a]})
            if ok(h, s): g, st, changed = h, s, True
print("edges", sum(len(s) for s in g.succ), "n", g.n, "fit", fit(g, st, 10 ** 9)); save(g, st, out)
