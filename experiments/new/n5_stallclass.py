#!/usr/bin/env python3
"""Box 4: classify every improving edge (v, w) ∈ Iσ at Even-stall iterations (σ' = σ) of N5 from the best-reward start:
  C = covered by the stall lemma; X = cycle-closing (w's (σ,τ)-play visits v); N = v is the cycle node of its own (σ,τ)-play.
Usage: n5_stallclass.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from n5_lock import step, play_val, on_play
from n5 import pg, Engine, dual
for path in sys.argv[1:]:
    g = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
    E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best")); cnt = {"C": 0, "X": 0, "N": 0}
    while True:
        r = step(g, E, Ed, s, t)
        if r is None: break
        if r[2]:
            vs, _ = E.evaluate(tuple(s)); V = play_val(E, g, s, t)
            for v, w in E.improving(tuple(s), vs):
                if on_play(g, s, t, w, v): cnt["X"] += 1
                elif V[v][0] == v: cnt["N"] += 1
                else: cnt["C"] += 1
        s, t = r[0], r[1]
    print(os.path.basename(path), cnt)
