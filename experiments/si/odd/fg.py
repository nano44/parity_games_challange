#!/usr/bin/env python3
"""L-SI box 36 (docs/si/N5-PIVOT-box36.md §5): FIXED-GUIDE strategy improvement FG(tau). Even's step is N5's S4a with Odd's tau
frozen: sigma' := Even's optimal strategy against tau in G restricted to sigma ∪ I_sigma (the same construction as n5x.step). If
sigma' = sigma while I_sigma != ∅ (a STALL: no improving edge helps against tau), FG takes one switch-all step (counted as STALL).
Stops when I_sigma = ∅ (sigma optimal; checked against the switch-all fixed point's valuation). Reports iterations, stalls, and per
lambda-run the most P-changes / matched changes of one vertex. TAU: first | last | sbar0 (Odd's best reply to sigma_0) | rand:SEED.
Usage: fg.py GAME.pg [TAU ...]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "chg"))
from n5x import load, Engine, dual
import pg
from compose import matched, bits
g = load(sys.argv[1]); n = g.n; E = Engine(g)
rk2v = {E.rank[v]: v for v in range(n)}; odd = lambda r: E.par[rk2v[r]] == 1
def kind(a, b):
    if a == b or a[0] != b[0] or a[1] == b[1]: return None
    rc = E.rank[a[0]]; w = lambda r: (r - rc) if not odd(r) else -(r - rc)
    return "MAT" if matched(bits(a[1]), bits(b[1]), w, odd) else "CAR"
def br(sigma, imp, tau):
    opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
    for v, w in imp: opt[v].add(w)
    succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
    Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
    _, best = Er.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
    return tuple(best[v] if g.owner[v] == 0 else -1 for v in range(n))
s0 = E.initial("best")
for spec in (sys.argv[2:] or ["first", "last", "sbar0", "rand:1", "rand:2", "rand:3"]):
    if spec == "first": tau = [min(g.succ[v]) if g.owner[v] == 1 else -1 for v in range(n)]
    elif spec == "last": tau = [max(g.succ[v]) if g.owner[v] == 1 else -1 for v in range(n)]
    elif spec == "sbar0": tau = list(E.evaluate(s0)[1])
    else: r = random.Random(int(spec[5:])); tau = [r.choice(g.succ[v]) if g.owner[v] == 1 else -1 for v in range(n)]
    s = s0; S = [s]; stall = 0
    while True:
        val, _ = E.evaluate(s); imp = E.improving(s, val)
        if not imp: break
        s2 = br(s, imp, tau)
        if s2 == s: s2 = E.rule_switch_all(s, val, imp, None); stall += 1
        s = s2; S.append(s)
        if len(S) > 20000: break
    U = [E.evaluate(x)[0] for x in S]; T = len(S) - 1
    lam = [tuple(u[v][0] for v in range(n)) for u in U]; runs = [0] + [k + 1 for k in range(T) if lam[k + 1] != lam[k]]
    best = (0, 0, -1)
    for i, j in zip(runs, runs[1:] + [T + 1]):
        for x in range(n):
            ks = [kind(U[t][x], U[t + 1][x]) for t in range(i, j - 1)]
            best = max(best, (sum(1 for k in ks if k), sum(1 for k in ks if k == "MAT"), x))
    print(f"FG {os.path.basename(sys.argv[1])} n {n} tau {spec} iter {T} stalls {stall} lambda_runs {len(runs)} maxPCH {best[0]} maxMAT {best[1]} vertex {best[2]}"
          f" {'CAP' if T >= 20000 else 'DONE'}")
