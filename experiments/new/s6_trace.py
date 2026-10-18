#!/usr/bin/env python3
"""Count switches per Even vertex in L-SI's cunningham/zadeh rule (si.py Engine, unmodified) on a game. Usage: s6_trace.py RULE game.pg"""
import sys, os, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "si")); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, si
g = pg.read(sys.argv[2]); e = si.Engine(g); rule = getattr(e, "rule_" + sys.argv[1]); cnt = collections.Counter()
def wrapped(strat, val, imp, rng):
    new = rule(strat, val, imp, rng)
    for v in range(g.n):
        if new[v] != strat[v]: cnt[v] += 1
    return new
strat, it = e.run(wrapped, e.initial("best"))
print("iterations", it); print("switch counts (vertex:count), descending:", sorted(cnt.items(), key=lambda x: -x[1])[:25])
