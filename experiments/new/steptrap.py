#!/usr/bin/env python3
"""Box 3 (N3 scoping): deep traps with DISTINCT gaps, so trap releases are generic (one trap per breakpoint). As alltrap.py, but
the i-th trapped Even vertex (in index order, or reversed with --rev) gets t_v priority P0 + 2i, P0 = B + 2 + 2k, cycle q = B + 1.
Usage: steptrap.py game.pg k [--rev] > out.pg"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); k = int(sys.argv[2])
B = max(g.prio); B += B % 2; P0 = B + 2 + 2 * k
prio = list(g.prio); owner = list(g.owner); succ = [sorted(set(s)) for s in g.succ]
vs = [v for v in range(g.n) if g.owner[v] == 0 and len(succ[v]) >= 2]
if "--rev" in sys.argv: vs = vs[::-1]
for i, v in enumerate(vs):
    t, c = len(prio), len(prio) + 1
    prio += [P0 + 2 * i, B + 1]; owner += [1, 1]; succ += [[c], [c]]; succ[v] = sorted(succ[v] + [t])
print(pg.dumps(pg.Game(prio, owner, succ)), end="")
