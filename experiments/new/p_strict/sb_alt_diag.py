#!/usr/bin/env python3
"""Box 8 item (3): why N5 leaves a 2-periodic switch-best run. Runs N5 (n5_lock.step, = n5.py's loop) and, at each iteration k
while N5's σ_k still equals switch-best's σ_k, reports: τ_k = b_{k+1}? (needed for the coincidence lemma, K8 (b)); b_k (Odd's best
reply to σ_k) and the Odd vertices where the next needed reply b_{k+2} differs from τ_k; which of those edges are in Iτ_k (Odd's
improving set w.r.t. Even's best reply τ̄_k); and N5's actual τ_{k+1}. Usage: sb_alt_diag.py game.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, ".."))
from n5_lock import step
from n5 import pg, Engine, dual
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); E, Ed = Engine(g), Engine(dual(g))
O = [v for v in range(g.n) if g.owner[v] == 1]
def sbstep(s):
    vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
    if not Is: return None
    A = {v: {s[v]} | {w for x, w in Is if x == v} for v in range(g.n) if g.owner[v] == 0}
    h = pg.Game(list(g.prio), list(g.owner), [sorted(A[v]) if g.owner[v] == 0 else list(g.succ[v]) for v in range(g.n)])
    Eh = Engine(h); sb, _ = Eh.run(Eh.rule_switch_all, tuple(s)); return list(sb)
sig = [list(E.initial("best"))]
while True:
    x = sbstep(sig[-1])
    if x is None: break
    sig.append(x)
b = [E.evaluate(tuple(x))[1] for x in sig]
s, t = list(E.initial("best")), list(Ed.initial("best")); k = 0
while k + 2 < len(sig) and s == sig[k]:
    vt, _ = Ed.evaluate(tuple(t)); It = set(Ed.improving(tuple(t), vt))
    need = {o: b[k + 2][o] for o in O if b[k + 2][o] != t[o]}
    print(f"k={k}: tau_k = b_(k+1) on Odd: {all(t[o] == b[k + 1][o] for o in O)}; b_k = b_(k+2): {all(b[k][o] == b[k + 2][o] for o in O)}; "
          f"needed Odd changes for tau_(k+1) = b_(k+2): {need}; of these in I_tau: {[o for o in need if (o, need[o]) in It]}")
    r = step(g, E, Ed, s, t)
    if r is None: break
    print(f"      N5 tau_(k+1) = b_(k+2) on Odd: {all(r[1][o] == b[k + 2][o] for o in O)}; N5 sigma_(k+1) = sb sigma_(k+1): {r[0] == sig[k + 1]}")
    s, t = r[0], r[1]; k += 1
