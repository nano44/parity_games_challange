#!/usr/bin/env python3
"""Box 6 (K8): along switch-best's run σ_0, σ_1, ... (arena optimum of H_σk, sb_tauvar.sbstep), let b_k = Odd's VJ best reply to σ_k
in G (Engine.evaluate counterstrategy) and τ_sb(k) = Odd's optimal strategy in H_σk. Checks (a) τ_sb(k) = b_{k+1} on Odd's vertices
(the saddle identification), (b) at each change of τ_sb (k -> k+1), the flip-back b_k = b_{k+2} that N5 needs to keep following
(τ_{k+1} = OddStep(σ_k, ·) answers σ_k; τ_sb(k+1) answers σ_{k+2}). Usage: sb_flipback.py game.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from n5 import pg, Engine, dual
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); E = Engine(g)
O = [v for v in range(g.n) if g.owner[v] == 1]
def sbstep(s):
    vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
    if not Is: return None, None
    A = {v: {s[v]} | {w for x, w in Is if x == v} for v in range(g.n) if g.owner[v] == 0}
    h = pg.Game(list(g.prio), list(g.owner), [sorted(A[v]) if g.owner[v] == 0 else list(g.succ[v]) for v in range(g.n)])
    Eh = Engine(h); sb, _ = Eh.run(Eh.rule_switch_all, tuple(s)); return list(sb), Eh.evaluate(sb)
sig = [list(E.initial("best"))]; tsb = []; vsb = []
while True:
    nx, ev = sbstep(sig[-1])
    if nx is None: break
    sig.append(nx); tsb.append(tuple(ev[1][v] for v in O)); vsb.append(ev[0])
b = [tuple(E.evaluate(tuple(s))[1][v] for v in O) for s in sig]
ident = sum(tsb[k] == b[k + 1] for k in range(len(tsb)))
# valuation-equivalence version of (a): Odd's strategy tsb(k) against σ_{k+1} in G gives the same valuation as b_{k+1}
ch = [k for k in range(len(tsb) - 1) if tsb[k] != tsb[k + 1]]
flip = sum(1 for k in ch if k + 2 < len(b) and b[k] == b[k + 2])
need = sum(1 for k in ch if k + 2 < len(b))
print(f"{os.path.basename(sys.argv[1])}: switch-best steps {len(tsb)}; τ_sb(k) = b_(k+1) at {ident}/{len(tsb)}; τ_sb changes {len(ch)}; "
      f"flip-back b_k = b_(k+2) at {flip}/{need} changes")
