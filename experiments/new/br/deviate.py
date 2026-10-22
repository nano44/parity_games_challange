#!/usr/bin/env python3
"""Box 11 option (2): along N5's run, compare Even's actual step (optimum of the honestly gated arena against Odd's CURRENT tau_k) with the honest
switch-best step (optimum of the same arena against Odd's best reply sigma-bar_k = c). Counts DEVIATIONS (iterations where the two differ),
and whether sigma-bar stayed constant. A toggle-driven killer must make deviations frequent. Usage: deviate.py game.pg [...]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, ".."))
from n5_lock import step
from n5 import pg, Engine, dual
for p in sys.argv[1:]:
    g = pg.read(p); E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best")); n = g.n
    it = dev = em = 0; sbs = set(); devs = []
    while True:
        vs, sbar = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs); sbs.add(tuple(sbar[v] for v in range(n) if g.owner[v] == 1))
        r = step(g, E, Ed, s, t)
        if r is None: break
        if Is:
            opt = {v: {s[v]} for v in range(n) if g.owner[v] == 0}
            for v, w in Is: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 0 else [sbar[v]] for v in range(n)]
            _, best = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ))).evaluate(tuple(sbar[v] if g.owner[v] == 1 else -1 for v in range(n)))
            hon = [best[v] if g.owner[v] == 0 else -1 for v in range(n)]
            act = [r[0][v] if g.owner[v] == 0 else -1 for v in range(n)]
            if hon != act and not r[2]: dev += 1; devs.append(it)
        em += r[0] != s; s, t = r[0], r[1]; it += 1
    print(f"{os.path.basename(p)} n={n} iterations={it} Even-moving {em} | distinct σ̄ states {len(sbs)} | Even steps deviating from honest switch-best (against σ̄): {dev} at iterations {devs[:20]}")
