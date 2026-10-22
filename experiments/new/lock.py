#!/usr/bin/env python3
"""L-NEW lock attempt (Lead 11:40Z item 3) on labelled switchallexp/switchbestexp (pgsolver_port labels q = FinalCycle,
p = FinalSink, s = StartEven). Variant --mode p0: p's priority -> 0 (p lies on every play into q, so VJ comparisons do not
change). Variant --mode loop: additionally q's self-loop is replaced by q -> L, L a fresh Odd vertex with L -> s (priority 0),
so every play reaching q returns to s and Even wins s iff the top priority on the path from s is even.
Variant --mode loop2: loop, and s loses its direct edge to p (the cycle from s must pass a bit's access vertex k_i).
Usage: lock.py game.pg --mode p0|loop|loop2 > out.pg"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg
g = pg.parse(open(sys.argv[1]).read()); mode = sys.argv[sys.argv.index("--mode") + 1]
lab = {g.labels[v]: v for v in range(g.n)}; q, p, s = lab["q"], lab["p"], lab["s"]
prio = list(g.prio); owner = list(g.owner); succ = [list(x) for x in g.succ]
prio[p] = 0
if mode in ("loop", "loop2"):
    L = len(prio); prio.append(0); owner.append(1); succ.append([s]); succ[q] = [L]
    if mode == "loop2":
        succ[s] = [w for w in succ[s] if w != p]
print(pg.dumps(pg.Game(prio, owner, succ)), end="")
