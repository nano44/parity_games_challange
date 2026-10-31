#!/usr/bin/env python3
"""L-RED: second-engine check. Runs L-NEW's experiments/new/n5.py (driver) on L-SI's experiments/si/si.py (valuations), records the
(sigma, tau) state sequence by wrapping Engine.evaluate on the game and its dual, and compares it with L-COMP's n5b SPEC trace.
Usage: xeng.py GAME.pg START"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new")); sys.path.insert(0, os.path.join(ROOT, "experiments", "n5-second"))
import n5, n5b, si
sys.path.insert(0, os.path.join(HERE, "..", "startck")); import startck   # D-ODD-1 (succ. 38): reject non-edges in the start
if startck.check(sys.argv[1], sys.argv[2]) and os.environ.get("ALLOW_BAD_START") != "1":
    sys.exit(f"BAD START {sys.argv[2]}: {startck.check(sys.argv[1], sys.argv[2])[:3]} (set ALLOW_BAD_START=1 to run anyway)")
g5 = n5b.pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g5)
N = n5b.N5(g5); N.mode = "spec"; tr, fb = [], []; N.run(s0, t0, trace=tr, fbtrace=fb)
g = n5.pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
log = {"s": [], "t": []}; orig = si.Engine.evaluate; ids = {}
def ev(self, strat):
    if getattr(self, "_tag", None) is None:
        self._tag = "s" if not ids else ("t" if len(ids) == 1 else "x"); ids[id(self)] = self._tag
    if self._tag in "st": log[self._tag].append(tuple(strat))
    return orig(self, strat)
si.Engine.evaluate = ev
st = ({v: w for v, w in enumerate(s0) if w >= 0}, {v: w for v, w in enumerate(t0) if w >= 0})
it, f, win, ws, _ = n5.run(g, "n5", st)
A = [(tuple(x if x >= 0 else None for x in s), tuple(x if x >= 0 else None for x in t)) for s, t in tr]
B = [(tuple(x if g.owner[v] == 0 and x >= 0 else None for v, x in enumerate(s)), tuple(x if g.owner[v] == 1 and x >= 0 else None for v, x in enumerate(t)))
     for s, t in zip(log["s"], log["t"])]
A = [(tuple(x if g.owner[v] == 0 else None for v, x in enumerate(s)), tuple(x if g.owner[v] == 1 else None for v, x in enumerate(t))) for s, t in A]
print(f"n5b: states {len(A)} iterations {len(A) - 1} fallbacks {sum(fb)} | n5.py (si.py engine): iterations {it} fallbacks {f} states logged {len(B)}")
print("state sequences identical:", A == B[:len(A)] and len(A) == len(B))
