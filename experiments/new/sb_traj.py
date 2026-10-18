#!/usr/bin/env python3
"""Box 5: (1) switch-best SI's own run on a game (Even's σ_k; Odd = optimal reply), from best-reward start;
(2) N5's run; report the first iteration where N5's σ leaves switch-best's σ-trajectory, and per N5 iteration the flags
(N5 step = switch-best step from N5's σ) / (τ = Odd's optimal reply in H_σ to switch-best's σ). Usage: sb_traj.py game.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from n5_lock import step
from n5 import pg, Engine, dual
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
E, Ed = Engine(g), Engine(dual(g))
def sbstep(s):
    vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
    if not Is: return None, None
    A = {v: {s[v]} | {w for x, w in Is if x == v} for v in range(g.n) if g.owner[v] == 0}
    h = pg.Game(list(g.prio), list(g.owner), [sorted(A[v]) if g.owner[v] == 0 else list(g.succ[v]) for v in range(g.n)])
    Eh = Engine(h); sb, _ = Eh.run(Eh.rule_switch_all, tuple(s)); return list(sb), Eh.evaluate(sb)[1]
traj = [list(E.initial("best"))]
while True:
    nx, _ = sbstep(traj[-1])
    if nx is None: break
    traj.append(nx)
s, t = list(E.initial("best")), list(Ed.initial("best")); it = 0; left = None; flags = []
while True:
    sb, tsb = sbstep(s); r = step(g, E, Ed, s, t)
    if r is None: break
    it += 1
    a = sb is not None and all(r[0][v] == sb[v] for v in range(g.n) if g.owner[v] == 0) if sb else (r[0] == s)
    b = sb is not None and all(t[v] == tsb[v] for v in range(g.n) if g.owner[v] == 1)
    flags.append(("S" if a else "-") + ("t" if b else "."))
    s, t = r[0], r[1]
    if left is None and (it >= len(traj) or s != traj[it]): left = it
print(f"{os.path.basename(sys.argv[1])}: switch-best iterations {len(traj) - 1}; N5 iterations {it}; N5's σ leaves the switch-best trajectory at iteration {left}")
print("flags (S = step equals switch-best, t = τ is Odd's arena-optimal reply):", " ".join(flags))
