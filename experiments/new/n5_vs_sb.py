#!/usr/bin/env python3
"""Box 5: along N5's run, compare N5's Even step with SWITCH-BEST's step (Friedmann 1106.0778 §8 / Schewe: the optimal strategy of
the improvement arena H_σ = Even restricted to {σ(v)} ∪ Iσ(v), Odd FREE), computed by switch-all SI (si.py Engine.run) on H_σ from σ.
Also tests whether Odd's current τ equals Odd's optimal reply inside H_σ to switch-best's strategy (the coincidence a switch-best-type
forcing needs). Usage: n5_vs_sb.py game.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "si"))
from n5_lock import step
from n5 import pg, Engine, dual
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best")); it = same = tau_ok = even_moves = 0
while True:
    vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
    if Is:
        A = {v: {s[v]} | {w for x, w in Is if x == v} for v in range(g.n) if g.owner[v] == 0}
        h = pg.Game(list(g.prio), list(g.owner), [sorted(A[v]) if g.owner[v] == 0 else list(g.succ[v]) for v in range(g.n)])
        Eh = Engine(h); sb, _ = Eh.run(Eh.rule_switch_all, tuple(s))
        tau_sb = Eh.evaluate(sb)[1]
    r = step(g, E, Ed, s, t)
    if r is None: break
    it += 1
    if Is and r[0] != s:
        even_moves += 1
        same += all(r[0][v] == sb[v] for v in range(g.n) if g.owner[v] == 0)
        tau_ok += all(t[v] == tau_sb[v] for v in range(g.n) if g.owner[v] == 1)
    s, t = r[0], r[1]
print(f"{os.path.basename(sys.argv[1])}: N5 iterations {it}; Even moves {even_moves}; N5 Even step = switch-best step at {same}; "
      f"τ = Odd's optimal reply in H_σ to switch-best's σ at {tau_ok}")
