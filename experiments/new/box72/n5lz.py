#!/usr/bin/env python3
"""L-NEW box 72: N5-LZ = N5 (box21/n5x.step) with a LAZY S4a tie-break on Even's side: after S4a computes an optimum sigma* of H
against tau (W* := its valuation on G_tau), every Even v with W*(v) of length >= 1 keeps sigma(v) whenever sigma(v) is W*-consistent,
i.e. v (+) W*(sigma v) = W*(v) ([V1] form). Consistent choices decrease the length by 1 per step and reach the cycle node, so the
lazy strategy has valuation W* (it is another optimum of H; box 72 note §3). If the lazy strategy equals sigma, sigma_new = sigma and
S4c applies as in SPEC (if also tau_new = tau). Odd's side unchanged. Same signature as n5x.step.
--lzc (N5-LZC): also at a W*-cycle node v (W*(v) = (v, empty, 0)) keep sigma(v) when W*(sigma v) has cycle node v and empty path set
(the play v -> sigma(v) -> ... -> v is then a cycle with top v, every vertex keeps its W*-value)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import Engine, dual
import pg
CYC = '--lzc' in sys.argv   # also lazy at W*-cycle nodes v: keep sigma(v) if W*(sigma v) = (v, empty, l)
def step(g, E, Ed, sigma, tau):
    n = g.n
    vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
    vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
    if not Is and not It: return None
    ns, nt = list(sigma), list(tau)
    if Is:
        opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
        for v, w in Is: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
        Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
        _, best = Er.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 0: ns[v] = best[v]
        tk = tuple(tau); _wc = g.__dict__.setdefault("_n5lz_wc", {})   # per-game cache (L-RED R133 hazard: was keyed by tau only)
        if tk not in _wc: _wc[tk] = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
        Ew = _wc[tk]; Ws = Ew.evaluate(tuple(ns))[0]
        for v in range(n):
            if g.owner[v] == 0 and ns[v] != sigma[v] and Ws[v][2] >= 1 and Ew.extend(v, Ws[sigma[v]]) == Ws[v]: ns[v] = sigma[v]
            elif CYC and g.owner[v] == 0 and ns[v] != sigma[v] and Ws[v] == (v, 0, 0) and Ws[sigma[v]][0] == v and Ws[sigma[v]][1] == 0:
                ns[v] = sigma[v]
        assert Ew.evaluate(tuple(ns))[0] == Ws, "lazy strategy lost W*"
    if It:
        opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
        for v, w in It: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
        Er = Engine(pg.Game(list(g.prio), list(g.owner), succ))
        _, best = Er.evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 1: nt[v] = best[v]
    fb = 0
    if ns == sigma and nt == tau:
        fb = 1
        if Is:
            for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
        else:
            for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
    return ns, nt, Is, It, fb, vs, vt
