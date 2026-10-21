#!/usr/bin/env python3
"""Box 9: the frozen-σ tail of N5's run (iterations after Even's last move). Reports tail length, Odd moves in the tail, and at how many
tail iterations Even's best reply τ̄ to τ (on Even's vertices) equals the frozen σ (then Odd's step is switch-best on G_σ).
Usage: n5_tail.py game.pg [...]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, ".."))
from n5_lock import step
from n5 import pg, Engine, dual
for p in sys.argv[1:]:
    g = pg.read(p); E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best"))
    V0 = [v for v in range(g.n) if g.owner[v] == 0]; hist = []
    while True:
        r = step(g, E, Ed, s, t)
        if r is None: break
        tbar = Ed.evaluate(tuple(t))[1]
        hist.append((r[0] != s, r[1] != t, all(tbar[v] == s[v] for v in V0), bool(r[2]))); s, t = r[0], r[1]
    last = max([i for i, h in enumerate(hist) if h[0]], default=-1); tail = hist[last + 1:]
    print(f"{os.path.basename(p)} n={g.n} iterations={len(hist)} tail={len(tail)} (after Even's last move at {last}); "
          f"tail iterations with τ̄ = σ: {sum(h[2] for h in tail)}; fallback iterations in the tail: {sum(h[3] for h in tail)} (whole run: {sum(h[3] for h in hist)})")
