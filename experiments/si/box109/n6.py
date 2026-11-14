#!/usr/bin/env python3
"""L-SI box 109 (design day): ONE step function for every improvement rule of the box, on L-SI's VJ engine (si.Engine) and
L-NEW's N5 step (box 190 n5v.step: modes spec = N5, xi = N5'-xi). Every rule applies, per iteration, a non-empty set of
improving switches of Even's sigma (on G) and / or of Odd's tau (on G^d) whenever one exists, so RESULTS R15 (c), (d) apply:
no state repeats, the run terminates, and at the stop (I_sigma = empty for one-sided rules; I_sigma = I_tau = empty for
two-sided ones) sigma is optimal (classical SI); output = SPEC S5 (regions and strategies of the final sigma and sigma-bar).

Rules (mode):
  spec     N5 (SPEC S1-S5)                                              two-sided
  xi       N5'-xi (RESULTS R118)                                        two-sided
  h1       alternate: odd iterations spec, even iterations xi           two-sided
  h3       Even: the Xi_sigma-best element of A(v) = {sigma(v)} + I_sigma(v) at every Even v (so every improvable Even vertex
           switches to a best improving edge); ties among Xi_sigma-best: SPEC's S4a choice if it is one of them, then the larger
           index. Odd: SPEC S4b; SPEC S4c for Odd when I_sigma is empty.     two-sided
  howard   classical switch-best for Even only (ties: larger index); tau is not used     one-sided
  h4       SCC-ordered Howard: switch-best only at the improvable Even vertices of the game-graph SCCs from which no other
           SCC holding an improvable Even vertex is reachable                one-sided
  nh       NO-HOLD N5: SPEC's S4a / S4b choice where it moves; every improvable vertex that SPEC holds (sigma_new(v) = sigma(v)
           although I_sigma(v) is non-empty; the same for Odd on G^d) switches to its best improving edge (ties: larger index)
  nhxi     the same with N5'-xi's S4a
  rf       ROOT-FIRST = candidate S8 (rf109.py's rf_select; the same function), one-sided: play graph of (sigma, sigma-bar); an improvable Even vertex v DEPENDS
           on an improvable u != v iff u lies on the play from sigma(v) or on the play from one of v's improving targets;
           switch-best exactly at the improvable vertices in the SINK strongly connected components of the dependency digraph
  rf2      rf on both sides at once (Odd on G^d); stop when I_sigma is empty OR I_tau is empty (either strategy optimal)
run(g, mode, start=None, cap) -> dict(its, fb, win, strat, capped, sw)   (sw = number of (vertex, iteration) switches of Even)
Usage: n6.py GAME.pg MODE [cap]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.environ.get("ROOT109") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [HERE] + [os.path.join(ROOT, p) for p in ("experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import pg, n5, n5x, n5v
from si import Engine
from rf109 import sccs, rf_select
dual = n5.dual
ONE = ("howard", "h4", "rf")


def best_imp(E, vs, cands):
    return max(cands, key=lambda w: (E.key(vs[w]), w))


class Runner:
    def __init__(self, g, mode):
        self.g, self.mode, self.n = g, mode, g.n
        self.E, self.Ed = Engine(g), Engine(dual(g))
        if mode == "h4":
            self.comp, self.nc = sccs(g.n, [sorted(s) for s in g.succ])
            # reach[c] = set of comps reachable from c (ids are reverse topological: successors have smaller ids)
            self.reach = [None] * self.nc
            members = [[] for _ in range(self.nc)]
            for v in range(g.n): members[self.comp[v]].append(v)
            for c in range(self.nc):
                r = 1 << c
                for v in members[c]:
                    for w in g.succ[v]:
                        if self.comp[w] != c: r |= self.reach[self.comp[w]]
                self.reach[c] = r

    def step(self, sigma, tau, it):
        g, n, E, Ed, mode = self.g, self.n, self.E, self.Ed, self.mode
        if mode in ("spec", "xi"): r = n5v.step(g, E, Ed, sigma, tau, mode); return None if r is None else (r[0], r[1], r[4])
        if mode == "h1": r = n5v.step(g, E, Ed, sigma, tau, "spec" if it % 2 == 1 else "xi"); return None if r is None else (r[0], r[1], r[4])
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        if mode in ONE:
            if not Is: return None
            imp = {}
            for v, w in Is: imp.setdefault(v, []).append(w)
            ns = list(sigma)
            if mode == "howard":
                for v in imp: ns[v] = best_imp(E, vs, imp[v])
            elif mode == "h4":
                cs = 0
                for v in imp: cs |= 1 << self.comp[v]
                for v in imp:
                    c = self.comp[v]
                    if (self.reach[c] & cs) == (1 << c): ns[v] = best_imp(E, vs, imp[v])
            else:
                for v, w in rf_select(n, g.owner, E, sigma, vs, sbar, Is).items(): ns[v] = w
            return ns, list(tau), 0
        vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        if mode == "rf2":
            if not Is or not It: return None
            ns, nt = list(sigma), list(tau)
            for v, w in rf_select(n, g.owner, E, sigma, vs, sbar, Is).items(): ns[v] = w
            for v, w in rf_select(n, Ed.g.owner, Ed, tau, vt, tbar, It).items(): nt[v] = w
            return ns, nt, 0
        if not Is and not It: return None
        base = "xi" if mode == "nhxi" else "spec"
        r = n5v.step(g, E, Ed, sigma, tau, base); ns, nt, fb = list(r[0]), list(r[1]), r[4]
        impS, impT = {}, {}
        for v, w in Is: impS.setdefault(v, []).append(w)
        for v, w in It: impT.setdefault(v, []).append(w)
        if mode == "h3":
            if Is:
                if fb: nt = list(tau)
                fb = 0
                for v in impS: ns[v] = max(impS[v], key=lambda w: (E.key(vs[w]), w == r[0][v], w))
            return ns, nt, fb
        if mode in ("nh", "nhxi"):
            if fb: return ns, nt, fb
            for v in impS:
                if ns[v] == sigma[v]: ns[v] = best_imp(E, vs, impS[v])
            for v in impT:
                if nt[v] == tau[v]: nt[v] = best_imp(Ed, vt, impT[v])
            return ns, nt, 0
        raise ValueError(mode)


def run(g, mode, start=None, cap=10 ** 6, start_pair=None):
    R = Runner(g, mode)
    sigma, tau = start_pair if start_pair else n5x.start_pair(g, R.E, R.Ed, start)
    sigma, tau = list(sigma), list(tau); its = fb = sw = 0
    while its < cap:
        r = R.step(sigma, tau, its + 1)
        if r is None: break
        ns, nt, f = r
        assert ns != sigma or nt != tau, "rule made no switch"
        sw += sum(1 for v in range(g.n) if ns[v] != sigma[v]); sigma, tau = ns, nt; its += 1; fb += f
    capped = int(its >= cap and R.step(sigma, tau, its + 1) is not None)
    E = R.E
    if mode == "rf2" and not capped:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        if Is:      # tau is optimal: read the solution from tau on the dual (winner flipped back)
            vt, tbar = R.Ed.evaluate(tuple(tau))
            win = [1 if R.Ed.g.prio[vt[v][0]] % 2 == 0 else 0 for v in range(g.n)]
            strat = [tau[v] if g.owner[v] == 1 else tbar[v] for v in range(g.n)]
            return dict(its=its, fb=fb, win=win, strat=strat, capped=capped, sw=sw)
    vs, sbar = E.evaluate(tuple(sigma))
    win = [0 if g.prio[vs[v][0]] % 2 == 0 else 1 for v in range(g.n)]
    strat = [sigma[v] if g.owner[v] == 0 else sbar[v] for v in range(g.n)]
    return dict(its=its, fb=fb, win=win, strat=strat, capped=capped, sw=sw)


if __name__ == "__main__":
    g = n5x.load(sys.argv[1]); cap = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 6
    r = run(g, sys.argv[2], cap=cap)
    print(f"n6 mode {sys.argv[2]} n {g.n} iterations {r['its']} fallbacks {r['fb']} capped {r['capped']} switches {r['sw']}")
