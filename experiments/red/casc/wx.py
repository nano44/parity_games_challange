#!/usr/bin/env python3
"""L-RED R151: W(X) before / after every switch of Even X in the longest W-run (n5b SPEC). Run from experiments/. Usage: wx.py GAME.pg START X"""
import sys; sys.path.insert(0, "red/xcn"); import xcn, n5b
pg = xcn.pg
g = pg.read(sys.argv[1]); X = int(sys.argv[3]); s0, t0 = n5b.read_start(sys.argv[2], g); tr, fb = xcn.trace(g, s0, t0)
runs, W = xcn.wruns(g, tr, fb); F = max(runs, key=len); t = tr[F[0]][1]
sw = same = 0
for k in F[:-1]:
    if tr[k][0][X] != tr[k + 1][0][X]:
        sw += 1; a, b = W(tr[k][0], t)[X], W(tr[k + 1][0], t)[X]
        same += (a == b); print(k, tr[k][0][X], "->", tr[k + 1][0][X], "W(X)", (a[0], sorted(a[1]), a[2]), "->", (b[0], sorted(b[1]), b[2]))
print("switches", sw, "with W(X) unchanged", same)
