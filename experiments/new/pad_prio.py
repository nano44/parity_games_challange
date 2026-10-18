#!/usr/bin/env python3
"""Add one isolated dummy vertex per priority 0..max (self-loop, owner by parity), so priority compression (compress.py, N1m)
merges nothing. The dummies are separate components: regions and plays on the original vertices are unchanged.
Usage: pad_prio.py in.pg > out.pg"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
for p in range(max(g.prio) + 1):
    v = len(prio); prio.append(p); owner.append(p % 2); succ.append([v])
print(pg.dumps(pg.Game(prio, owner, succ)), end="")
