#!/usr/bin/env python3
"""R172: per transition of the N5 run: fallback flag, W-changed vertex count, and the vertices whose lambda_W (cycle node of W, W := the
valuation in G_tau) changes, with names and old -> new cycle node names. Usage: lamtrace.py G.pg START"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]); nm = {}
for l in open(sys.argv[1]):
    mm = re.match(r'(\d+) .*"(\S+)"', l)
    if mm: nm[int(mm.group(1))] = mm.group(2)
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); k = 0
def W(s, t):
    e = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else g.succ[v] for v in range(g.n)])); return e.evaluate(tuple(s))[0]
w0 = W(s, t)
while True:
    r = step(g, E, Ed, s, t)
    if r is None: break
    ns, nt = r[0], r[1]; w1 = W(ns, nt)
    lc = [(nm.get(v, v), nm.get(w0[v][0], w0[v][0]), nm.get(w1[v][0], w1[v][0])) for v in range(g.n) if w0[v][0] != w1[v][0]]
    sw = [nm.get(v, v) + "->" + nm.get(ns[v], ns[v]) for v in range(g.n) if g.owner[v] == 0 and ns[v] != s[v]]
    print(f"{k} fb {r[4]} Wch {sum(1 for v in range(g.n) if w0[v] != w1[v])} sw {sw} lamch {lc[:6]}{' ...' if len(lc) > 6 else ''}")
    s, t, w0 = ns, nt, w1; k += 1
