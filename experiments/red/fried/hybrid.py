#!/usr/bin/env python3
"""L-RED R140: which N5 feature defeats Friedmann's locally-optimizing counter (arXiv 0901.2731, PGSolver switchallexp)?
One-sided Even improvement loops on L-SI's si.py Engine (as experiments/new/n5.py uses it), same best-reward start:
  V0 switch-all: every Even v with an improving edge takes its Xi-best improving successor (locally optimizing, ties: larger index).
  V1 arena-vs-sigmabar: sigma' = Even's one-player optimum in the arena {sigma(v)} + I_sigma(v) against Odd FIXED to sigma-bar (N5's S4a
     step with tau := sigma-bar, i.e. feature (ii) without (i)).
  V2 arena-vs-fixed-tau: S4a's step against tau0 (Odd's best-reward start, never improved): N5 inside one never-ending W-run (features
     (i) + (ii)); stops when I_sigma is empty or the step does not move.
Usage: hybrid.py GAME.pg V0|V1|V2   (prints iterations)"""
import sys, os
EXP = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
for p in ("si", "harness", "new"): sys.path.insert(0, os.path.join(EXP, p))
import pg
from si import Engine
from n5 import dual
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); mode = sys.argv[2]; n = g.n
E, Ed = Engine(g), Engine(dual(g)); sigma = list(E.initial("best")); tau0 = list(Ed.initial("best"))
def arena(sigma, Is, oddfix):
    opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
    for v, w in Is: opt[v].add(w)
    succ = [sorted(opt[v]) if g.owner[v] == 0 else [oddfix[v]] for v in range(n)]
    Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
    _, best = Er.evaluate(tuple(oddfix[v] if g.owner[v] == 1 else -1 for v in range(n)))
    return [best[v] if g.owner[v] == 0 else -1 for v in range(n)]
NM = {}
for l in open(sys.argv[1]):
    a = l.strip().rstrip(";").split()
    if len(a) >= 5 and a[0].isdigit(): NM[int(a[0])] = a[4].strip('"')
it = 0
while it < 100000:
    vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
    if not Is: break
    if mode == "V0":
        ns = list(sigma); bestw = {}
        for v, w in Is:
            if v not in bestw or (E.key(vs[w]), w) > (E.key(vs[bestw[v]]), bestw[v]): bestw[v] = w
        for v, w in bestw.items(): ns[v] = w
    else:
        ns = arena(sigma, Is, sbar if mode == "V1" else tau0)
    if ns == sigma: print("STALL"); break
    if os.environ.get("TRACE"): print(it + 1, " ".join(f"{NM[v]}->{NM[ns[v]]}" for v in range(n) if ns[v] != sigma[v]))
    sigma = ns; it += 1
print(f"HYBRID {os.path.basename(sys.argv[1])} {mode} iterations {it}")
