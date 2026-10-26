#!/usr/bin/env python3
"""N5^tau ("keep tau on ties"), L-COMP box 10 (Lead 2026-10-26 06:48Z), from the text of L-NEW's packet P-N5-EPR §0
(docs/new/P-N5-EPR-box45.md, sha1 8fecca79): SPEC N5 with S4b replaced by S4b^tau: "if I_tau != {} and tau is VALUE-OPTIMAL against sigma
in S4b's arena H' (that is, V_{sigma,tau} on H' equals S1's valuation on H' against sigma, pointwise), then tau_new := tau; otherwise
tau_new := SPEC's S4b output. S1, S2, S3, S4a, S4c, S4d, S5 are SPEC's."
Built on n5b.py (L-COMP's SPEC second implementation, written from the spec text only); this file copies n5b.N5.run and changes step 3
(S4b) only. V_{sigma,tau} on H' = the valuation of sigma in H' with every Odd vertex fixed to tau (SpecSI on restrict(H', tau)); S1's
valuation on H' against sigma = the valuation returned with SPEC's S4b output. Sanity assert: whenever SPEC's S4b output equals tau, the
two valuations are equal (so the test is the packet's, not a representation artefact).
API: N5tau(g).run(sigma, tau, trace=list, fbtrace=list) -> (win, strat, iterations, fallbacks); diverge counter self.kept = number of
iterations where S4b^tau kept tau while SPEC's S4b output differs."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n5b  # noqa: E402
from n5b import EVEN, ODD, SpecSI, dual, restrict  # noqa: E402


class N5tau(n5b.N5):
    def __init__(self, g):
        super().__init__(g, mode="spec"); self.kept = 0

    def run(self, sigma=None, tau=None, max_iter=100000, trace=None, fbtrace=None):
        g = self.g
        sigma = sigma or self.SG.initial_strategy_by_best_reward()
        tau = tau or self.SD.initial_strategy_by_best_reward()
        it = fb = 0; seen = set()
        while True:
            key = (tuple(sigma), tuple(tau))
            if key in seen:
                raise n5b.RepeatedState(f"(sigma, tau) repeated at iteration {it}")
            seen.add(key)
            if trace is not None:
                trace.append(key)
            vs = self.ev(self.SG, sigma); vt = self.ev(self.SD, tau)
            Is, It = self.improving(self.SG, sigma, vs), self.improving(self.SD, tau, vt)
            if not Is and not It:
                break
            it += 1
            if it > max_iter:
                raise RuntimeError("iteration cap")
            allow = [None] * g.n
            for v in range(g.n):
                allow[v] = [sigma[v]] + Is.get(v, []) if g.owner[v] == EVEN else [tau[v]]
            d2 = dual(restrict(g, allow)); s2 = SpecSI(d2)
            _, c2 = self.opt(s2, [tau[v] if g.owner[v] == ODD else -1 for v in range(g.n)])
            sigma2 = [c2[v] if g.owner[v] == EVEN else -1 for v in range(g.n)]
            # step 3 = S4b^tau
            allow = [None] * g.n
            for v in range(g.n):
                if g.owner[v] == ODD:
                    allow[v] = [tau[v]] + It.get(v, [])
            H = restrict(g, allow); s3 = SpecSI(H)
            val3, c3 = self.opt(s3, sigma)
            tau2 = [c3[v] if g.owner[v] == ODD else -1 for v in range(g.n)]
            if It:
                fixed = [None] * g.n
                for v in range(g.n):
                    if g.owner[v] == ODD:
                        fixed[v] = [tau[v]]
                vtau = SpecSI(restrict(H, fixed)).evaluate(sigma)
                value_opt = all(vtau[v] == val3[v] for v in range(g.n))
                if tau2 == tau and not value_opt:
                    raise AssertionError("S4b returned tau but V_{sigma,tau} != S1's valuation on H'")
                if value_opt and tau2 != tau:
                    tau2 = list(tau); self.kept += 1
            isfb = sigma2 == sigma and tau2 == tau
            if isfb:
                fb += 1
                if Is:
                    sigma2 = list(sigma)
                    for v in Is:
                        sigma2[v] = self.SG.best(vs, v)
                else:
                    tau2 = list(tau)
                    for v in It:
                        tau2[v] = self.SD.best(vt, v)
            if fbtrace is not None:
                fbtrace.append(int(isfb))
            sigma, tau = sigma2, tau2
        win = [g.prio[vs[v][0]] % 2 for v in range(g.n)]
        _, sbar = self.opt(self.SG, sigma)
        strat = [sigma[v] if g.owner[v] == EVEN else sbar[v] for v in range(g.n)]
        strat = [strat[v] if win[v] == g.owner[v] else None for v in range(g.n)]
        return win, strat, it, fb
