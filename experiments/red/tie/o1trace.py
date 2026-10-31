#!/usr/bin/env python3
"""L-RED R152: trace one Even X through the longest W-run: per state sigma(X), W(X), and for every successor w of X: Xi(w) (n5b
evaluate_choice), W(w), key(w) (o1key.key), and whether w is in Iσ(X) (Xi(w) strictly better than Xi(sigma(X))). Usage: o1trace.py GAME.pg START X"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xcn")); sys.path.insert(0, HERE)
import xcn, n5b, o1key
pg = xcn.pg
g = pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g); X = int(sys.argv[3])
tr, fb = xcn.trace(g, s0, t0); runs, W = xcn.wruns(g, tr, fb); F = max(runs, key=len); t = tr[F[0]][1]; SG = n5b.SpecSI(g)
f = lambda x: (x[0], sorted(x[1]), x[2])
print("X", X, "owner", g.owner[X], "prio", g.prio[X], "succ", g.succ[X], "run", F[0], "-", F[-1])
for k in F:
    s = tr[k][0]; w = W(s, t); xi, _ = SG.evaluate_choice(list(s)); c = w[X][0]
    print(f"state {k} sigma(X) {s[X]} W(X) {f(w[X])}")
    for y in g.succ[X]:
        imp = SG.nvo(xi[s[X]], xi[y]) < 0
        print(f"   succ {y}: Xi {f(xi[y])} W {f(w[y])} key {o1key.key(g, s, t, y, c)} {'IMPROVING' if imp else ''}")
