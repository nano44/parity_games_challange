#!/usr/bin/env python3
"""L-NEW: priority spreading (candidate N1 killer K1). p -> K*p (K odd keeps parity and order), optionally adding isolated
self-loop dummy vertices so that every value 0..K*max(p) is used (then TARGET-style compression to {0..n} keeps the gaps).
Usage: spread.py game.pg K [--dummies] > out.pg"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); K = int(sys.argv[2]); assert K % 2 == 1
prio = [K * p for p in g.prio]; owner = list(g.owner); succ = [list(s) for s in g.succ]
if "--dummies" in sys.argv:
    used = set(prio)
    for q in range(max(prio) + 1):
        if q not in used:
            v = len(prio); prio.append(q); owner.append(0); succ.append([v])
print(pg.dumps(pg.Game(prio, owner, succ)), end="")
