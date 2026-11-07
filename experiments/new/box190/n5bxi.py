#!/usr/bin/env python3
"""Box 190: SECOND implementation of N5'-xi (gauntlet step 2), on L-COMP's independent N5 (experiments/n5-second/n5b.py, SPEC mode;
valuations from experiments/hard-families/pgsolver_si.py, a port of PGSolver's evaluate_strategy). Shares no valuation, improving-edge
or arena code with n5v.py (si.py Engine). The ONE rule changed (docs/new/N5-DETOWER-box190.md §2.1): after S4a, at every Even v with
|A(v)| >= 2 that is not its own cycle node in the arena, sigma_new(v) := the Xi_sigma-best element of TIE(v) = {w in A(v) :
val_H(v) = v (+) val_H(w)}, ties: S4a's own choice first, then the larger index. Valuations here are (cycle node u, frozenset P,
length e); v (+) (u, P, e) := (u, P + {v} if (prio(v), v) > (prio(u), u) else P, e + 1) (rank by (priority, index), n5b A1).
Usage: n5bxi.py GAME.pg   -> 'n5bxi iterations K fallbacks F'"""
import sys, os, functools
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, "experiments/n5-second")]
import n5b
from n5b import N5, SpecSI, dual, restrict, RepeatedState, EVEN, ODD

class N5xi(N5):
    def ext(self, v, val):
        u, P, e = val; pr = self.g.prio
        return (u, P | {v} if (pr[v], v) > (pr[u], u) else P, e + 1)

    def run(self, sigma=None, tau=None, max_iter=100000):
        g = self.g
        sigma = sigma or self.SG.initial_strategy_by_best_reward()
        tau = tau or self.SD.initial_strategy_by_best_reward()
        it = fb = 0; seen = set()
        while True:
            key = (tuple(sigma), tuple(tau))
            if key in seen: raise RepeatedState(f"(sigma, tau) repeated at iteration {it}")
            seen.add(key)
            vs = self.ev(self.SG, sigma); vt = self.ev(self.SD, tau)
            Is, It = self.improving(self.SG, sigma, vs), self.improving(self.SD, tau, vt)
            if not Is and not It: break
            it += 1
            if it > max_iter: raise RuntimeError("iteration cap")
            allow = [[sigma[v]] + Is.get(v, []) if g.owner[v] == EVEN else [tau[v]] for v in range(g.n)]
            s2 = SpecSI(dual(restrict(g, allow)))
            val2, c2 = self.opt(s2, [tau[v] if g.owner[v] == ODD else -1 for v in range(g.n)])
            sigma2 = [c2[v] if g.owner[v] == EVEN else -1 for v in range(g.n)]
            if Is:   # the changed rule (only meaningful when S4a ran, i.e. Is non-empty, as in SPEC S4a)
                for v in range(g.n):
                    if g.owner[v] != EVEN or len(set(allow[v])) < 2 or val2[v][0] == v: continue
                    tie = [w for w in sorted(set(allow[v])) if self.ext(v, val2[w]) == val2[v]]
                    if not tie: continue
                    def cmpw(a, b):
                        c = self.SG.nvo(vs[a], vs[b])           # nvo(x, y) < 0: y better for Even, so a < b
                        if c: return c
                        if (a == c2[v]) != (b == c2[v]): return 1 if a == c2[v] else -1
                        return (a > b) - (a < b)
                    sigma2[v] = max(tie, key=functools.cmp_to_key(cmpw))
            else:
                sigma2 = list(sigma)
            allow3 = [[tau[v]] + It.get(v, []) if g.owner[v] == ODD else None for v in range(g.n)]
            if It:
                s3 = SpecSI(restrict(g, allow3)); _, c3 = self.opt(s3, sigma)
                tau2 = [c3[v] if g.owner[v] == ODD else -1 for v in range(g.n)]
            else:
                tau2 = list(tau)
            if sigma2 == sigma and tau2 == tau:
                fb += 1
                if Is:
                    sigma2 = list(sigma)
                    for v in Is: sigma2[v] = self.SG.best(vs, v)
                else:
                    tau2 = list(tau)
                    for v in It: tau2[v] = self.SD.best(vt, v)
            sigma, tau = sigma2, tau2
        win = [g.prio[vs[v][0]] % 2 for v in range(g.n)]
        _, sbar = self.opt(self.SG, sigma)
        strat = [sigma[v] if g.owner[v] == EVEN else sbar[v] for v in range(g.n)]
        return win, [strat[v] if win[v] == g.owner[v] else None for v in range(g.n)], it, fb

if __name__ == "__main__":
    import pg
    g = pg.read(sys.argv[1]); win, strat, it, fb = N5xi(g, mode="spec").run(); print(f"n5bxi iterations {it} fallbacks {fb}")
