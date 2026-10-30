#!/usr/bin/env python3
"""L-RED successor 32 (R133): second engine for the VARIANT N5-LZC (L-NEW box 72, l-new 909be5eb, docs/new/N5-LZ-box72.md; box72/n5lz.py
--lzc), written from the box-72 docstring on L-COMP's n5b SPEC loop and PGSolver-port valuations (not from n5lz.py's code).
S4a lazy rule: after Even's optimum sigma2 of the arena against tau, with W* := val(sigma2, tau) on G_tau, every Even v with
sigma2(v) != sigma(v) keeps sigma(v) if (i) len W*(v) >= 1 and v (+) W*(sigma v) = W*(v), or (ii) (N5-LZC) W*(v) = (v, {}, 0) and
W*(sigma v) has cycle node v and empty path set. Asserts that the lazy strategy keeps W*. Everything else is n5b SPEC.
Usage: n5lzb.py GAME.pg [SOL] [--start START] [--plain]   (--plain = plain N5, same loop, for the comparison)
Prints: n5lzb iterations I fallbacks F (and writes SOL)."""
import sys, os
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
for p in ("experiments/n5-second", "experiments/hard-families", "experiments/harness"): sys.path.insert(0, os.path.join(R, p))
import n5b, pg
from n5b import N5, SpecSI, restrict, dual, EVEN, ODD

def ext(si, v, val):
    u, P, e = val
    return (u, P | {v} if si.rel(v, u) > 0 else P, e + 1)

def run(g, sigma=None, tau=None, lazy=True, max_iter=10 ** 6, trace=None):
    N = N5(g, mode="spec"); SG, SD = N.SG, N.SD
    sigma = sigma or SG.initial_strategy_by_best_reward(); tau = tau or SD.initial_strategy_by_best_reward()
    it = fb = 0; WC = {}
    while True:
        if trace is not None: trace.append((tuple(sigma), tuple(tau)))
        vs = SG.evaluate(sigma); vt = SD.evaluate(tau)
        Is, It = N.improving(SG, sigma, vs), N.improving(SD, tau, vt)
        if not Is and not It: break
        it += 1
        if it > max_iter: raise RuntimeError("cap")
        allow = [[sigma[v]] + Is.get(v, []) if g.owner[v] == EVEN else [tau[v]] for v in range(g.n)]
        _, c2 = N.opt(SpecSI(dual(restrict(g, allow))), [tau[v] if g.owner[v] == ODD else -1 for v in range(g.n)])
        sigma2 = [c2[v] if g.owner[v] == EVEN else -1 for v in range(g.n)]
        if lazy and Is:
            tk = tuple(tau)
            if tk not in WC: WC[tk] = SpecSI(pg.Game(g.prio, g.owner, [g.succ[v] if g.owner[v] == EVEN else [tau[v]] for v in range(g.n)]))
            Ew = WC[tk]; Ws = Ew.evaluate(sigma2); lz = list(sigma2)
            for v in range(g.n):
                if g.owner[v] != EVEN or sigma2[v] == sigma[v]: continue
                d = sigma[v]
                if Ws[v][2] >= 1 and ext(Ew, v, Ws[d]) == Ws[v]: lz[v] = d
                elif Ws[v] == (v, frozenset(), 0) and Ws[d][0] == v and not Ws[d][1]: lz[v] = d
            assert Ew.evaluate(lz) == Ws, "lazy strategy lost W*"
            sigma2 = lz
        allow = [[tau[v]] + It.get(v, []) if g.owner[v] == ODD else None for v in range(g.n)]
        _, c3 = N.opt(SpecSI(restrict(g, allow)), sigma)
        tau2 = [c3[v] if g.owner[v] == ODD else -1 for v in range(g.n)]
        if sigma2 == sigma and tau2 == tau:
            fb += 1
            if Is:
                sigma2 = list(sigma)
                for v in Is: sigma2[v] = SG.best(vs, v)
            else:
                tau2 = list(tau)
                for v in It: tau2[v] = SD.best(vt, v)
        sigma, tau = sigma2, tau2
    win = [g.prio[vs[v][0]] % 2 for v in range(g.n)]
    _, sbar = N.opt(SG, sigma)
    strat = [sigma[v] if g.owner[v] == EVEN else sbar[v] for v in range(g.n)]
    strat = [strat[v] if win[v] == g.owner[v] else None for v in range(g.n)]
    return win, strat, it, fb

if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    st = sys.argv[sys.argv.index("--start") + 1] if "--start" in sys.argv else None
    a = [x for x in a if x != st]
    g = pg.read(a[0]); s0, t0 = n5b.read_start(st, g) if st else (None, None)
    win, strat, it, fb = run(g, s0, t0, lazy="--plain" not in sys.argv)
    if len(a) > 1: pg.write_sol(win, a[1], strat)
    print(f"n5lzb{'(plain)' if '--plain' in sys.argv else ''} iterations {it} fallbacks {fb}")
