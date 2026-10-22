#!/usr/bin/env python3
"""Box 8: print switch-best's run (sb_2per_climb.sbrun) with Odd's best replies b_k, their distinct count, and N5's iterations on the
same game (n5.run, unmodified). Usage: sb_replies.py game.pg"""
import sys, os, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg, n5
from n5 import Engine
spec = importlib.util.spec_from_file_location('sb2', os.path.join(HERE, 'sb_2per_climb.py')); m = importlib.util.module_from_spec(spec)
path = sys.argv[1]; sys.argv = [sys.argv[0]]; spec.loader.exec_module(m)
g = pg.read(path); E = Engine(g); O = [v for v in range(g.n) if g.owner[v] == 1]
s = list(E.initial("best")); sig = [s]
while True:
    vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
    if not Is: break
    A = {v: {s[v]} | {w for x, w in Is if x == v} for v in range(g.n) if g.owner[v] == 0}
    h = pg.Game(list(g.prio), list(g.owner), [sorted(A[v]) if g.owner[v] == 0 else list(g.succ[v]) for v in range(g.n)])
    Eh = Engine(h); sb, _ = Eh.run(Eh.rule_switch_all, tuple(s)); s = list(sb); sig.append(s)
b = [tuple(E.evaluate(tuple(x))[1][v] for v in O) for x in sig]
print("switch-best steps", len(sig) - 1, "distinct Odd best replies", len(set(b)), "replies by step:", [sorted(set(b)).index(x) for x in b])
print("Even vertices switched per step:", [sum(a != c for a, c in zip(sig[k], sig[k + 1])) for k in range(len(sig) - 1)])
it, fb, win, ws, ev = n5.run(g, "n5"); print("N5 iterations", it, "fallback", fb)
