#!/usr/bin/env python3
"""Trace N10c on instances/cond_stuck_r1569_YE.pg: after each accepted fixing, the TRUE answer (Zielonka) of the restricted game.
The first accepted fixing with true answer NO is an N10b gap; that restricted game is written to instances/."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sa"))
import pg, zielonka
from cond import oracle
g = pg.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), "instances", "cond_stuck_r1569_YE.pg"))
succ = [sorted(set(x)) for x in g.succ]
truth = lambda sc: all(w == 0 for w in zielonka.solve(pg.Game(g.prio, g.owner, sc)))
written = False
ok, s = oracle(g); print("start oracle", ok, "truth", truth(succ))
for v in range(g.n):
    if g.owner[v] != 0 or len(succ[v]) < 2:
        continue
    order = sorted(succ[v], key=lambda u: (-s.get((v, u), 0.0), u))
    acc = None
    for u in order:
        trial = [list(x) for x in succ]; trial[v] = [u]
        ok2, s2 = oracle(pg.Game(g.prio, g.owner, trial))
        print(f"  v={v} try u={u} (s={s.get((v, u), 0.0):.3f}): oracle {ok2}, truth {truth(trial)}")
        if ok2:
            acc = (u, trial, s2); break
    if acc is None:
        print(f"STUCK at v={v}"); break
    u, succ, s = acc
    if not truth(succ) and not written:
        written = True
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "instances", "esc_gap_from_r1569.pg")
        pg.write(pg.Game(g.prio, g.owner, succ), out); print(f"FIRST WRONG ACCEPT at v={v} u={u}: N10b gap written to {out}")
