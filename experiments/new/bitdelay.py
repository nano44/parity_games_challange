#!/usr/bin/env python3
"""L-NEW: bit-indexed delays for labelled switchallexp (pgsolver_port labels e<i>, f<i>, ... carry the bit index i).
Priorities +2; every edge out of an Even vertex with >= 2 successors whose label carries index i (a/b lanes: index i//2)
gets a chain of c*(i+1)^POW (REV: c*(N-i)^POW) single-successor Odd vertices of priority 0; other edges untouched.
Intent: reverse N1's top-down reveal order so low bits are revealed first.
Usage: bitdelay.py game.pg c [--pow P] [--rev] > out.pg"""
import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg
g = pg.parse(open(sys.argv[1]).read()); c = int(sys.argv[2])
P = int(sys.argv[sys.argv.index("--pow") + 1]) if "--pow" in sys.argv else 1; rev = "--rev" in sys.argv
idx = []
for v in range(g.n):
    m = re.fullmatch(r"([a-z])(\d+)", g.labels[v] or "")
    idx.append(None if not m else (int(m.group(2)) // 2 if m.group(1) in "ab" else int(m.group(2))))
N = max(i for i in idx if i is not None) + 1
prio = [p + 2 for p in g.prio]; owner = list(g.owner); succ = [sorted(set(s)) for s in g.succ]
for v in range(g.n):
    if g.owner[v] != 0 or len(succ[v]) < 2 or idx[v] is None: continue
    L = c * ((N - idx[v]) if rev else (idx[v] + 1)) ** P; new = []
    for w in succ[v]:
        first = len(prio)
        for i in range(L):
            prio.append(0); owner.append(1); succ.append([first + i + 1] if i < L - 1 else [w])
        new.append(first)
    succ[v] = new
print(pg.dumps(pg.Game(prio, owner, succ)), end="")
