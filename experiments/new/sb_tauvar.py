#!/usr/bin/env python3
"""Box 5: along switch-best's own run (sb_traj.sbstep), how often does Odd's arena-optimal reply τ_sb change, and does N5's Odd step
(Odd's restricted optimum against the OLD σ_k within Odd's improving edges) from τ_sb(k) give τ_sb(k+1), as N5 would need? Usage: sb_tauvar.py game.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.argv = [sys.argv[0], sys.argv[1]]
from n5 import pg, Engine, dual
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); E, Ed = Engine(g), Engine(dual(g))
def sbstep(s):
    vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
    if not Is: return None, None
    A = {v: {s[v]} | {w for x, w in Is if x == v} for v in range(g.n) if g.owner[v] == 0}
    h = pg.Game(list(g.prio), list(g.owner), [sorted(A[v]) if g.owner[v] == 0 else list(g.succ[v]) for v in range(g.n)])
    Eh = Engine(h); sb, _ = Eh.run(Eh.rule_switch_all, tuple(s)); return list(sb), list(Eh.evaluate(sb)[1])
def odd_step(s, t):
    vt, _ = Ed.evaluate(tuple(t)); It = Ed.improving(tuple(t), vt)
    if not It: return list(t)
    opt = {v: {t[v]} for v in range(g.n) if g.owner[v] == 1}
    for v, w in It: opt[v].add(w)
    succ = [sorted(opt[v]) if g.owner[v] == 1 else [s[v]] for v in range(g.n)]
    _, best = Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(tuple(s[v] if g.owner[v] == 0 else -1 for v in range(g.n)))
    return [best[v] if g.owner[v] == 1 else -1 for v in range(g.n)]
s = list(E.initial("best")); taus = []; sigmas = [s]
while True:
    sb, tsb = sbstep(sigmas[-1])
    if sb is None: break
    sigmas.append(sb); taus.append([tsb[v] if g.owner[v] == 1 else -1 for v in range(g.n)])
ch = sum(taus[k] != taus[k + 1] for k in range(len(taus) - 1))
# N5 needs τ_{k+1} = OddStep(σ_k, τ_k) = τ_sb(k+1) (Odd answers the OLD σ_k); misses vs change points
okk = [odd_step(sigmas[k], taus[k]) == taus[k + 1] for k in range(len(taus) - 1)]; odd_ok = sum(okk)
chg = [taus[k] != taus[k + 1] for k in range(len(taus) - 1)]
miss_at_change = sum(1 for a, c in zip(okk, chg) if not a and c); miss_elsewhere = sum(1 for a, c in zip(okk, chg) if not a and not c)
print(f"{os.path.basename(sys.argv[1])}: switch-best steps {len(taus)}; τ_sb changes {ch} times; distinct τ_sb {len(set(map(tuple, taus)))}; "
      f"OddStep(σ_k, τ_sb(k)) = τ_sb(k+1) at {odd_ok}/{len(taus) - 1}; misses at a change of τ_sb {miss_at_change}, elsewhere {miss_elsewhere}")
