#!/usr/bin/env python3
"""L-NEW box 95 (docs/new/N5-HN-box95.md): which N5 feature kills Friedmann's H_n (PGSolver switchbestexp; LMCS 1106.0778 §8)?
One-sided Even loops from the best-reward start on L-SI's si.py Engine (as L-RED R140 hybrid.py), all with the SAME arena
A_t(v) = {sigma_t(v)} u I_sigma_t(v) (SPEC S2 offers):
  GLO: I^glo (Schewe / Friedmann [F11] p.7): sigma' = an optimal Even strategy of the two-player game restricted to A_t (Odd unrestricted),
       computed by switch-all VJ iterations inside A_t started at sigma_t (ties: larger index), i.e. values judged by Xi with Odd re-responding.
  V1:  sigma' = Even's pointwise optimum of A_t against Odd FIXED to sigma-bar_t (R140 V1; N5's S4a with tau := sigma-bar_t).
  V2:  sigma' = Even's pointwise optimum of A_t against Odd fixed to tau_0 forever (R140 V2; one never-ending W-run).
  SA:  switch-all (locally optimizing), for reference.
Prints iterations, and for GLO / V1 the number of iterations at which some stubborn closure was available (CLOSE: an Even vertex whose
arena optimum under V1 differs from GLO's choice). Usage: hn.py GAME.pg MODE [MAXIT]"""
import sys, os
EXP = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
for p in ("si", "harness", "new"): sys.path.insert(0, os.path.join(EXP, p))
import pg
from si import Engine
from n5 import dual
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); mode = sys.argv[2]; n = g.n
maxit = int(sys.argv[3]) if len(sys.argv) > 3 else 20000
E = Engine(g); Ed = Engine(dual(g)); sigma = list(E.initial("best")); tau0 = list(Ed.initial("best"))
def onep(sigma, A, oddfix):
    succ = [sorted(A[v]) if g.owner[v] == 0 else [oddfix[v]] for v in range(n)]
    Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
    _, best = Er.evaluate(tuple(oddfix[v] if g.owner[v] == 1 else -1 for v in range(n)))
    return [best[v] if g.owner[v] == 0 else -1 for v in range(n)]
def glo(sigma, A):
    succ = [sorted(A[v]) if g.owner[v] == 0 else list(g.succ[v]) for v in range(n)]
    Er = Engine(pg.Game(list(g.prio), list(g.owner), succ)); s = list(sigma)
    while True:
        vs, _ = Er.evaluate(tuple(s)); Is = Er.improving(tuple(s), vs)
        if not Is: return s
        bw = {}
        for v, w in Is:
            if v not in bw or (Er.key(vs[w]), w) > (Er.key(vs[bw[v]]), bw[v]): bw[v] = w
        for v, w in bw.items(): s[v] = w
it = 0; diff = 0
while it < maxit:
    vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
    if not Is: break
    A = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
    for v, w in Is: A[v].add(w)
    if mode == "SA":
        ns = list(sigma); bw = {}
        for v, w in Is:
            if v not in bw or (E.key(vs[w]), w) > (E.key(vs[bw[v]]), bw[v]): bw[v] = w
        for v, w in bw.items(): ns[v] = w
    elif mode == "GLO":
        ns = glo(sigma, A); diff += ns != onep(sigma, A, sbar)
    elif mode == "V1":
        ns = onep(sigma, A, sbar); diff += ns != glo(sigma, A)
    else:
        ns = onep(sigma, A, tau0)
    if ns == sigma: print("STALL"); break
    sigma = ns; it += 1
print(f"HN {os.path.basename(sys.argv[1])} n {n} {mode} iterations {it} differ_from_other {diff}")
