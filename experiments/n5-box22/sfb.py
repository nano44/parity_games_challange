#!/usr/bin/env python3
"""L-COMP box 22: N5-SF on L-COMP's engine n5b (second implementation; L-NEW's n5sf.py is the first). Definition from
docs/new/N5-SF-box54.md §1 (l-new 56a42d4f): N5's step with S4a's opponent τ replaced by σ̄ = Odd's best reply to σ (SPEC S1 choice) and
S4b's opponent σ replaced by τ̄ = Even's best reply to τ on G^d; S4c, S4d, S5 unchanged. Implemented as n5b's step body (box17.Eng.step)
with exactly those two substitutions. Usage: sfb.py GAME.pg [START]  -> 'sfb iterations I fallbacks F sbc_sigma S sbc_tau T'"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(EXP, "n5-box17")); sys.path.insert(0, os.path.join(EXP, "n5-box18"))
import box17 as B  # noqa: E402
from box17 import SpecSI, dual, restrict, EVEN, ODD  # noqa: E402


class SFEng(B.Eng):
    def replies(self, sigma, tau):
        _, sb = self.N.SG.evaluate_choice(list(sigma)); _, tb = self.N.SD.evaluate_choice(list(tau))
        return tuple(sb), tuple(tb)          # sb on Odd vertices; tb on the dual's Odd = original Even vertices

    def step(self, sigma, tau):
        N, g = self.N, self.g; sigma, tau = list(sigma), list(tau)
        vs = N.ev(N.SG, sigma); vt = N.ev(N.SD, tau)
        Is, It = N.improving(N.SG, sigma, vs), N.improving(N.SD, tau, vt)
        if not Is and not It:
            return None
        sb, tb = self.replies(sigma, tau)
        allow = [None] * g.n
        for v in range(g.n):
            allow[v] = [sigma[v]] + Is.get(v, []) if g.owner[v] == EVEN else [sb[v]]          # SF: Odd keeps σ̄(v), not τ(v)
        _, c2 = N.opt(SpecSI(dual(restrict(g, allow))), [sb[v] if g.owner[v] == ODD else -1 for v in range(g.n)])
        sigma2 = [c2[v] if g.owner[v] == EVEN else -1 for v in range(g.n)]
        allow = [None] * g.n
        for v in range(g.n):
            if g.owner[v] == ODD:
                allow[v] = [tau[v]] + It.get(v, [])
            else:
                allow[v] = [tb[v]]                                                           # SF: Even keeps τ̄(v), not σ(v)
        _, c3 = N.opt(SpecSI(restrict(g, allow)), [tb[v] if g.owner[v] == EVEN else -1 for v in range(g.n)])
        tau2 = [c3[v] if g.owner[v] == ODD else -1 for v in range(g.n)]
        isfb = sigma2 == sigma and tau2 == tau
        if isfb:
            if Is:
                sigma2 = list(sigma)
                for v in Is:
                    sigma2[v] = N.SG.best(vs, v)
            else:
                tau2 = list(tau)
                for v in It:
                    tau2[v] = N.SD.best(vt, v)
        return tuple(sigma2), tuple(tau2), int(isfb)


def run(g, st=None):
    e = SFEng(g); x = st or e.start(); states = [x]; fb = 0; seen = {x}
    while True:
        r = e.step(*x)
        if r is None:
            break
        x = (r[0], r[1]); fb += r[2]
        if x in seen:
            raise RuntimeError("SF state repeated")
        seen.add(x); states.append(x)
    rep = [e.replies(*s) for s in states]
    sbs = sum(rep[i][0] != rep[i + 1][0] for i in range(len(rep) - 1)); sbt = sum(rep[i][1] != rep[i + 1][1] for i in range(len(rep) - 1))
    vs, _ = e.N.SG.evaluate_choice(list(x[0])); win = [g.prio[vs[v][0]] % 2 for v in range(g.n)]
    return dict(states=states, it=len(states) - 1, fb=fb, sbc_sigma=sbs, sbc_tau=sbt, win=win)


if __name__ == "__main__":
    import nm
    g = nm.load(sys.argv[1]); e = B.Eng(g); st = nm.startof(g, e, sys.argv[2]) if len(sys.argv) > 2 else None
    r = run(g, st); print(f"sfb iterations {r['it']} fallbacks {r['fb']} sbc_sigma {r['sbc_sigma']} sbc_tau {r['sbc_tau']}")
