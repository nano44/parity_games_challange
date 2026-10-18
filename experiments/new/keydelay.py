#!/usr/bin/env python3
"""L-NEW: route (A) of N1-killer-sketch.md on labelled switchallexp: delay ONLY bit i's cycle-closing edge e_i -> h_i
(pgsolver_port labels) by a chain of c*(i+1)^P (or c*(N-i)^P with --rev) single-successor Odd vertices of priority 0;
all original priorities +2. Usage: keydelay.py game.pg c [--pow P] [--rev] > out.pg"""
import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg
g = pg.parse(open(sys.argv[1]).read()); c = int(sys.argv[2])
P = int(sys.argv[sys.argv.index("--pow") + 1]) if "--pow" in sys.argv else 1; rev = "--rev" in sys.argv
lab = {g.labels[v]: v for v in range(g.n)}; N = sum(1 for l in lab if re.fullmatch(r"e\d+", l or ""))
prio = [p + 2 for p in g.prio]; owner = list(g.owner); succ = [sorted(set(s)) for s in g.succ]
for i in range(N):
    e, h = lab[f"e{i}"], lab[f"h{i}"]; L = c * ((N - i) if rev else (i + 1)) ** P; first = len(prio)
    for k in range(L):
        prio.append(0); owner.append(1); succ.append([first + k + 1] if k < L - 1 else [h])
    succ[e] = sorted(first if x == h else x for x in succ[e])
print(pg.dumps(pg.Game(prio, owner, succ)), end="")
