#!/usr/bin/env python3
"""Box 4 killer attempt 4 (stall-gadget test): put an Odd dummy D on every edge (x, y) of an Even vertex x with >= 2 successors:
x -> D -> {y, g}; g = one shared gift vertex (Even self-loop) with priority GP. Dummies get priority DP (even, below everything).
Shifts the original priorities by +2 so 0/1 stay free. Usage: dummygift.py game.pg GP_mode(top|low) > out.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); mode = sys.argv[2]
prio = [p + 2 for p in g.prio]; owner = list(g.owner); succ = [list(s) for s in g.succ]
top = max(prio) + 2; top += top % 2
G = len(prio); prio.append(top if mode == "top" else 2 if False else 0); owner.append(0); succ.append([G])
for x in range(g.n):
    if g.owner[x] == 0 and len(g.succ[x]) >= 2:
        new = []
        for y in g.succ[x]:
            D = len(prio); prio.append(0); owner.append(1); succ.append([y, G]); new.append(D)
        succ[x] = new
sys.stdout.write(pg.dumps(pg.Game(prio, owner, succ)))
