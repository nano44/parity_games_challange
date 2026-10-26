#!/usr/bin/env python3
"""Box 48 DATA (N5-NCONF §8): split each configuration of the longest phase into (root value sigma-bar(r), relay sub-configuration R = sigma-bar on
Q - {r}), r := the vertex of Q whose sigma-bar changes most often. Prints the epoch sequence as (root value, R id), the distinct R, and for each R the
sequence of root values over the epochs with that R (MONO: no root value repeats within one R). Usage: rootrel.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../box43", "../box21"): sys.path.insert(0, os.path.join(HERE, p))
from multi import load, step, start_pair, Engine, dual
from n5x import readstart
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); rows = []
Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
while True:
    vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
    rows.append((tuple(x[0] for x in vs), tuple(t), tuple(sb[q] for q in Q), r[4] if r else 0))
    if r is None: break
    s, t = r[0], r[1]
ph = []; i = 0
while i < len(rows):
    j = i
    while j + 1 < len(rows) and rows[j + 1][:2] == rows[i][:2]: j += 1
    ph.append((i, j)); i = j + 1
a, b = max(ph, key=lambda p: p[1] - p[0])
eps = [rows[k][2] for k in range(a, b + 1) if k == a or rows[k][2] != rows[k - 1][2]]
chg = [sum(1 for x, y in zip(eps, eps[1:]) if x[i] != y[i]) for i in range(len(Q))]; ri = max(range(len(Q)), key=lambda i: chg[i])
Rid = {}; seq = []; perR = {}
for c in eps:
    R = c[:ri] + c[ri + 1:]; rid = Rid.setdefault(R, len(Rid)); seq.append((c[ri], rid)); perR.setdefault(rid, []).append(c[ri])
mono = all(len(v) == len(set(v)) for v in perR.values())
print(sys.argv[1].split("/")[-1], "root", Q[ri], "changes per Q vertex", dict(zip(Q, chg)), "N_ep", len(eps), "distinct R", len(Rid), "MONO", mono)
print("per R (root values in epoch order):", {k: v for k, v in perR.items()})
