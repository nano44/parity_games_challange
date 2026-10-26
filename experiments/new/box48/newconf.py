#!/usr/bin/env python3
"""Box 48 DATA (N5-NCONF §8): classify each NEW configuration (first visit in its phase) of the longest phase: NEWPAIR if it contains a pair
(q, sigma-bar(q)) not seen earlier in the phase, RECOMB otherwise (all pairs seen, new combination). For RECOMB: the changed vertices at its
boundary and whether their new values return to an earlier value. Usage: newconf.py GAME.pg [START]"""
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
a, b = max(ph, key=lambda p: p[1] - p[0]); seenp = set(); seenc = set(); cnt = {"NEWPAIR": 0, "RECOMB": 0}; rec = []
tau = rows[a][1]
for k in range(a, b + 1):
    c = rows[k][2]; pairs = {(Q[i], c[i]) for i in range(len(Q))}
    if c not in seenc:
        kind = "NEWPAIR" if pairs - seenp else "RECOMB"; cnt[kind] += 1
        if kind == "RECOMB" and k > a:
            ch = [Q[i] for i in range(len(Q)) if c[i] != rows[k - 1][2][i]]
            rec.append((k, ch, sum(1 for i in range(len(Q)) if c[i] != tau[Q[i]])))
        seenc.add(c)
    seenp |= pairs
print(sys.argv[1].split("/")[-1], "phase", (a, b), "NCONF", len(seenc), "pairs seen", len(seenp), cnt, "sumdeg", sum(len(g.succ[q]) for q in Q))
print("RECOMB (state, changed vertices, |D|):", rec)
