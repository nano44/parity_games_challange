#!/usr/bin/env python3
"""L-NEW: bait transform (N1 killer route B, docs/new/N1-killer-sketch.md). Priorities +2; for every Even vertex v with >= 2
successors, the edge to its best-reward start successor sigma0(v) (L-SI's convention, computed on the input) is replaced by
a chain of k single-successor Odd vertices of priority 0 (winners unchanged: every cycle keeps an original vertex).
Usage: bait.py game.pg k > out.pg"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); k = int(sys.argv[2])
def rk(w):
    rr = g.prio[w] if g.prio[w] % 2 == 0 else -g.prio[w]
    return (rr, w if rr % 2 == 0 else -w)
prio = [p + 2 for p in g.prio]; owner = list(g.owner); succ = [sorted(set(s)) for s in g.succ]
for v in range(g.n):
    if g.owner[v] != 0 or len(succ[v]) < 2: continue
    w0 = max(succ[v], key=rk); first = len(prio)
    for i in range(k):
        prio.append(0); owner.append(1); succ.append([first + i + 1] if i < k - 1 else [w0])
    succ[v] = sorted(first if x == w0 else x for x in succ[v])
print(pg.dumps(pg.Game(prio, owner, succ)), end="")
