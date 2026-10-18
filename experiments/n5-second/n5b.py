#!/usr/bin/env python3
"""N5 SSI-GLOBAL, second independent implementation (L-COMP, gauntlet step 2; Lead 2026-10-18 20:51Z).

Written from the TEXT ONLY: docs/new/N5-ssi-global.md on claude/l-new @ 8925171 ("Exact pseudocode" section).
experiments/new/n5.py and L-SI's engine (experiments/si/) were NOT opened. The Voege-Jurdziński (VJ00) valuations and
Odd's optimal counterstrategy come from L-COMP's own port of PGSolver's evaluate_strategy
(experiments/hard-families/pgsolver_si.py, class SI; REFEREE-checked, and identical to the PGSolver d3cd624 binary in
iteration counts and solutions: experiments/hard-families/pgsolver-binary-diff.md).

Readings of the spec (each an ambiguity, reported; see README.md "Ambiguities"):
 A1 injective rank: ties between equal priorities broken by vertex index (VJ order on (priority, index), as PGSolver).
 A2 "best-reward start": PGSolver's initial_strategy_by_best_reward (successor of maximal reward; ties by the reward
    order on (priority, index)); for Odd the same on the dual game.
 A3 dual game: owners swapped, priorities + 1, same vertex ids and successor order.
 A4 Iσ = {(v,w): v Even, Ξσ(w) strictly better for Even than Ξσ(σ(v))}; Iτ likewise on the dual.
 A5 "optimal strategy" in a restricted arena = PGSolver's optimal counterstrategy (per vertex, the successor of best
    valuation for its owner; ties broken by vertex index as in PGSolver's best/nvto). The spec does not fix ties.
 A6 Step 3 uses the OLD σ (the spec: "Odd's optimal counterstrategy to σ"; σ' is not yet assigned in step 5's sense).
 A7 Fallback "classical switch-all step": every Even vertex with an improving edge switches to its best successor under
    Ξσ (PGSolver switch-all, ties by index); for Odd the same on the dual.
 A8 Iteration count = number of passes through steps 2-5 (the final pass that finds Iσ = Iτ = ∅ is not counted);
    fallback count = number of passes that took step 4.
 A9 Output: regions from Ξσ at termination (winner = parity of the cycle vertex), Even's strategy σ on its region,
    Odd's strategy = its optimal counterstrategy σ̄ to σ on its region.
Usage: n5b.py GAME.pg [OUT.sol] [--start FILE]   (FILE: lines 'SIGMA0 v:w ...' and 'TAU0 v:w ...', as dlm_gen.py prints)
Prints 'n5b iterations K fallbacks F evals E'."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "hard-families")); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg
from pgsolver_si import SI

sys.setrecursionlimit(1000000)
EVEN, ODD = 0, 1


def dual(g, succ=None):
    return pg.Game([p + 1 for p in g.prio], [1 - o for o in g.owner], succ if succ is not None else g.succ)


def restrict(g, allowed):
    """Same game with succ(v) := allowed[v] where allowed[v] is not None."""
    return pg.Game(g.prio, g.owner, [sorted(set(allowed[v])) if allowed[v] is not None else g.succ[v] for v in range(g.n)])


class N5:
    def __init__(self, g):
        self.g, self.d = g, dual(g)
        self.SG, self.SD = SI(self.g), SI(self.d)
        self.evals = 0

    def ev(self, si, strat):
        self.evals += 1
        return si.evaluate(strat)

    @staticmethod
    def improving(si, strat, valu):
        """A4: for each vertex of si's Even player, the set of strictly improving successors."""
        I = {}
        for v in range(si.g.n):
            if strat[v] == -1:
                continue
            ws = [w for w in si.succ[v] if si.nvo(valu[strat[v]], valu[w]) < 0]
            if ws:
                I[v] = ws
        return I

    @staticmethod
    def counter(si, valu):
        """Optimal counterstrategy of si's Odd player (A5)."""
        return [si.best(valu, v) if si.pl[v] == ODD else -1 for v in range(si.g.n)]

    def run(self, sigma=None, tau=None, max_iter=100000):
        g = self.g
        sigma = sigma or self.SG.initial_strategy_by_best_reward()                  # Even vertices: successor, Odd: -1
        tau = tau or self.SD.initial_strategy_by_best_reward()                      # on the dual: original Odd vertices
        it = fb = 0
        while True:
            vs = self.ev(self.SG, sigma); vt = self.ev(self.SD, tau)
            Is, It = self.improving(self.SG, sigma, vs), self.improving(self.SD, tau, vt)
            if not Is and not It:                                                    # step 1
                break
            it += 1
            if it > max_iter:
                raise RuntimeError("iteration cap")
            # step 2: Even's optimum against fixed τ, Even restricted to A_σ, via Odd's counterstrategy on the dual arena
            allow = [None] * g.n
            for v in range(g.n):
                if g.owner[v] == EVEN:
                    allow[v] = [sigma[v]] + Is.get(v, [])
                else:
                    allow[v] = [tau[v]]
            d2 = dual(restrict(g, allow)); s2 = SI(d2)
            v2 = self.ev(s2, [tau[v] if g.owner[v] == ODD else -1 for v in range(g.n)])
            sigma2 = [s2.best(v2, v) if g.owner[v] == EVEN else -1 for v in range(g.n)]
            # step 3: Odd's optimum against σ (A6: old σ), Odd restricted to A_τ
            allow = [None] * g.n
            for v in range(g.n):
                if g.owner[v] == ODD:
                    allow[v] = [tau[v]] + It.get(v, [])
            s3 = SI(restrict(g, allow))
            v3 = self.ev(s3, sigma)
            tau2 = [s3.best(v3, v) if g.owner[v] == ODD else -1 for v in range(g.n)]
            # step 4: fallback
            if sigma2 == sigma and tau2 == tau:
                fb += 1
                if Is:
                    sigma2 = list(sigma)
                    for v in Is:
                        sigma2[v] = self.SG.best(vs, v)
                else:
                    tau2 = list(tau)
                    for v in It:
                        tau2[v] = self.SD.best(vt, v)
            sigma, tau = sigma2, tau2                                                 # step 5
        win = [g.prio[vs[v][0]] % 2 for v in range(g.n)]                             # A9
        sbar = self.counter(self.SG, vs)
        strat = [sigma[v] if g.owner[v] == EVEN else sbar[v] for v in range(g.n)]
        strat = [strat[v] if win[v] == g.owner[v] else None for v in range(g.n)]
        return win, strat, it, fb


def read_start(path, g):
    sigma = [-1] * g.n; tau = [-1] * g.n
    for line in open(path):
        parts = line.split()
        if parts and parts[0] in ("SIGMA0", "TAU0"):
            tgt = sigma if parts[0] == "SIGMA0" else tau
            for p in parts[1:]:
                a, b = map(int, p.split(":")); tgt[a] = b
    return sigma, tau


def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    start = sys.argv[sys.argv.index("--start") + 1] if "--start" in sys.argv else None
    a = [x for x in a if x != start]
    g = pg.read(a[0])
    s = N5(g)
    sigma, tau = read_start(start, g) if start else (None, None)
    win, strat, it, fb = s.run(sigma, tau)
    if len(a) > 1:
        pg.write_sol(win, a[1], strat)
    print(f"n5b iterations {it} fallbacks {fb} evals {s.evals}")


if __name__ == "__main__":
    main()
