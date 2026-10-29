#!/usr/bin/env python3
"""L-RED successor 28: SECOND engine for L-NEW's N5-SF (docs/new/N5-SF-box54.md §1 on claude/l-new), written from the text:
  S4a': Even v keeps {sigma(v)} + I_sigma(v); Odd v keeps ONLY sigma-bar(v) (Odd's optimal counter to sigma, S1);
        sigma_new = Even's one-player optimum of that arena.  S4b' mirror (Odd vs tau-bar on the dual).  S4c/S4d/S5 as N5's SPEC.
Valuations from L-COMP's PGSolver port (experiments/hard-families/pgsolver_si.py via experiments/n5-second/n5b.py), NOT L-SI's si.py
that n5sf.py uses. MODE=spec uses n5b's SpecSI choice rule (should reproduce n5sf.py counts exactly); MODE=orig uses PGSolver's
counterstrategy rule (per vertex best valuation, ties by index) everywhere: regions must agree, counts may differ.
Usage: sf2.py GAME.pg [--start FILE] [--mode spec|orig] [--trace]
Prints iterations, fallbacks, sigma-changes, SBC_sigma (sigma-changes at which sigma-bar changes), tau-changes, SBC_tau, LAM."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "n5-second"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "hard-families")); sys.path.insert(0, os.path.join(ROOT, "experiments", "harness"))
import pg
import n5b
from n5b import N5, SpecSI, dual, restrict, read_start, EVEN, ODD
sys.setrecursionlimit(1000000)


class SF(N5):
    def run_sf(self, sigma=None, tau=None, max_iter=10 ** 6, rec=None):
        g = self.g
        # a start file may give only one side (all -1): the other side then takes the S3 default
        sigma = sigma if sigma and any(x != -1 for x in sigma) else self.SG.initial_strategy_by_best_reward()
        tau = tau if tau and any(x != -1 for x in tau) else self.SD.initial_strategy_by_best_reward()
        it = fb = 0; seen = set()
        while True:
            key = (tuple(sigma), tuple(tau))
            if key in seen:
                raise n5b.RepeatedState(f"repeated at {it}")
            seen.add(key)
            vs, sbar = self.opt(self.SG, sigma)          # Xi_sigma and sigma-bar
            vt, tbar = self.opt(self.SD, tau)            # Xi_tau (dual) and tau-bar
            Is, It = self.improving(self.SG, sigma, vs), self.improving(self.SD, tau, vt)
            if rec is not None:
                rec.append(dict(s=tuple(sigma), t=tuple(tau), sb=tuple(sbar), tb=tuple(tbar),
                                lam=tuple(x[0] for x in vs), lamt=tuple(x[0] for x in vt), nIs=len(Is), nIt=len(It)))
            if not Is and not It:
                break
            it += 1
            if it > max_iter:
                raise RuntimeError("cap")
            sigma2 = list(sigma)
            if Is:
                allow = [None] * g.n
                for v in range(g.n):
                    allow[v] = [sigma[v]] + Is.get(v, []) if g.owner[v] == EVEN else [sbar[v]]
                s2 = SpecSI(dual(restrict(g, allow)))
                _, c2 = self.opt(s2, [sbar[v] if g.owner[v] == ODD else -1 for v in range(g.n)])
                sigma2 = [c2[v] if g.owner[v] == EVEN else -1 for v in range(g.n)]
            tau2 = list(tau)
            if It:
                allow = [None] * g.n
                for v in range(g.n):
                    allow[v] = [tau[v]] + It.get(v, []) if g.owner[v] == ODD else [tbar[v]]
                s3 = SpecSI(restrict(g, allow))
                _, c3 = self.opt(s3, [tbar[v] if g.owner[v] == EVEN else -1 for v in range(g.n)])
                tau2 = [c3[v] if g.owner[v] == ODD else -1 for v in range(g.n)]
            if sigma2 == sigma and tau2 == tau:
                fb += 1
                if Is:
                    for v in Is: sigma2[v] = self.SG.best(vs, v)
                else:
                    for v in It: tau2[v] = self.SD.best(vt, v)
            sigma, tau = sigma2, tau2
        win = [g.prio[vs[v][0]] % 2 for v in range(g.n)]
        return win, sigma, sbar, it, fb


def stats(rec):
    sc = sbc = tc = tbc = lam = 0
    for a, b in zip(rec, rec[1:]):
        if a["s"] != b["s"]:
            sc += 1; sbc += a["sb"] != b["sb"]; lam += a["lam"] != b["lam"]
        if a["t"] != b["t"]:
            tc += 1; tbc += a["tb"] != b["tb"]
    return sc, sbc, tc, tbc, lam


def main():
    a = sys.argv[1:]
    mode = a[a.index("--mode") + 1] if "--mode" in a else "spec"
    start = a[a.index("--start") + 1] if "--start" in a else None
    g = pg.read(a[0]); n5b.MODE = mode
    s = SF(g, mode=mode)
    sig, tau = read_start(start, g) if start else (None, None)
    rec = []
    win, sigma, sbar, it, fb = s.run_sf(sig, tau, rec=rec)
    sc, sbc, tc, tbc, lam = stats(rec)
    print(f"sf2 mode {mode} n {g.n} iterations {it} fallbacks {fb} sigma_changes {sc} SBC_sigma {sbc} tau_changes {tc} SBC_tau {tbc} LAM {lam}")
    if "--sol" in a:
        strat = [sigma[v] if g.owner[v] == EVEN else sbar[v] for v in range(g.n)]
        strat = [strat[v] if win[v] == g.owner[v] else None for v in range(g.n)]
        pg.write_sol(win, a[a.index("--sol") + 1], strat)


if __name__ == "__main__":
    main()
