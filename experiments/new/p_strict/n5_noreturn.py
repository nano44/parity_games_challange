#!/usr/bin/env python3
"""Box 8: check Lemma NR (docs/new/N5-K8-box8.md) along N5's own run (n5_lock.step = n5.py's loop): neither σ nor τ ever returns to a
strategy it held earlier (consecutive equal values allowed). Usage: n5_noreturn.py game.pg [...]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, ".."))
from n5_lock import step
from n5 import pg, Engine, dual
bad = runs = its = 0
for path in sys.argv[1:]:
    g = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%"))); E, Ed = Engine(g), Engine(dual(g))
    s, t = list(E.initial("best")), list(Ed.initial("best")); seenS, seenT = {tuple(s)}, {tuple(t)}; runs += 1
    while True:
        r = step(g, E, Ed, s, t)
        if r is None: break
        its += 1
        if r[0] != s:
            bad += tuple(r[0]) in seenS; seenS.add(tuple(r[0]))
        if r[1] != t:
            bad += tuple(r[1]) in seenT; seenT.add(tuple(r[1]))
        s, t = r[0], r[1]
print(f"runs={runs} iterations={its} returns of sigma or tau to an earlier strategy: {bad}")
