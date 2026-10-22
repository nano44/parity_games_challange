#!/usr/bin/env python3
"""Box 4: during every run of consecutive fallback iterations (a LOCK, τ frozen) check pointwise:
  Ξσ_k ⊴ V_{σ_k,τ} (stall lemma) and V_{σ_{k+1},τ} ⊴ V_{σ_k,τ} (Even's switch-all only takes edges that are not better against τ).
Usage: n5_sandwich.py game.pg ...   (prints per game: lock lengths, violations of each claim)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from n5_lock import step, play_val
from n5 import pg, Engine, dual
for path in sys.argv[1:]:
    g = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
    E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best"))
    locks, cur, bad_sand, bad_mono, steps = [], 0, 0, 0, 0
    while True:
        r = step(g, E, Ed, s, t)
        if r is None: break
        ns, nt, f, _, _ = r
        if f and nt == t and ns != s:
            V0 = play_val(E, g, s, t); V1 = play_val(E, g, ns, t); X1 = E.evaluate(tuple(ns))[0]; steps += 1
            bad_mono += sum(E.key(V1[v]) > E.key(V0[v]) for v in range(g.n))
            bad_sand += sum(E.key(X1[v]) > E.key(V1[v]) for v in range(g.n))
        cur = cur + 1 if f else 0
        if not f and cur: locks.append(cur); cur = 0
        s, t = ns, nt
    if cur: locks.append(cur)
    print(f"{os.path.basename(path)}: Even-fallback steps checked {steps}; V not monotone at {bad_mono} vertex-steps; "
          f"Xi above V after the step at {bad_sand} vertex-steps")
