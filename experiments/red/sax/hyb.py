#!/usr/bin/env python3
"""L-RED successor 38 (R164): which N5 feature kills the switch-all counter (switchallexp, L-SI box 58)? Hybrids of N5 (n5.py, l-new) and
classical switch-all SI, all on si.py's engine, best-reward start, from the SAME (sigma, tau) per iteration as n5.py:
  sa   : classical SI. Even switch-all on Is (per vertex the improving target of best Xi, ties larger index); Odd = sigma-bar (no tau).
  n5   : n5.py's rule, reimplemented here (Even S4a vs tau, Odd S4b vs sigma, fallback = switch-all); must equal n5.py's counts.
  H1   : Even SWITCH-ALL on Is (as sa), Odd S4b (tau moves as in N5). Tests: is S4a's one-player optimum needed?
  H2   : Even S4a, but Odd's vertices in the arena keep sigma-bar(v) (Odd's best response to the CURRENT sigma) instead of tau; no tau.
         Tests: is the separately evolving tau needed? (Fallback: switch-all.)
  H3   : Even S4a against the START tau, tau never moves (one W-world). Stops when Is is empty. Tests: S4a alone, one W-world.
  H4   : Even switch-all on Is restricted to edges that are ALSO W-improving against tau (W = valuation of sigma vs fixed tau), Odd S4b.
Env WMON=1: also count, per iteration, vertices whose W (valuation of sigma vs the CURRENT tau, Odd fixed) DROPS from sigma_k to
sigma_(k+1) while tau stays (WDROP) and the iterations with a drop (WDROPIT).
Prints iterations, fallbacks, and the W-runs (maximal stretches with tau constant). Usage: hyb.py MODE G.pg [--cap K]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "si")); sys.path.insert(0, os.path.join(ROOT, "harness"))
import pg
from si import Engine
def dual(h): return pg.Game([p + 1 for p in h.prio], [1 - o for o in h.owner], [list(s) for s in h.succ])
def s4a(g, sigma, Is, oddsucc):
    n = g.n; opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
    for v, w in Is: opt[v].add(w)
    succ = [sorted(opt[v]) if g.owner[v] == 0 else [oddsucc[v]] for v in range(n)]
    _, best = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ))).evaluate(tuple(oddsucc[v] if g.owner[v] == 1 else -1 for v in range(n)))
    return [best[v] if g.owner[v] == 0 else sigma[v] for v in range(n)]
def s4b(g, tau, It, sigma):
    n = g.n; opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
    for v, w in It: opt[v].add(w)
    succ = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
    _, best = Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
    return [best[v] if g.owner[v] == 1 else tau[v] for v in range(n)]
def sa(E, sigma, Is, vs):
    ns = list(sigma)
    for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
    return ns
def run(g, mode, cap=10 ** 5):
    n = g.n; E, Ed = Engine(g), Engine(dual(g)); sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
    it = fb = 0; taus = [tuple(tau)]; WD = [0, 0]
    while it < cap:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        if mode in ("sa", "H2", "H3"): It = []
        if not Is and not It: break
        it += 1; ns, nt = list(sigma), list(tau)
        if mode == "sa": ns = sa(E, sigma, Is, vs)
        elif mode in ("n5", "H3"):
            if Is: ns = s4a(g, sigma, Is, tau)
            if It and mode == "n5": nt = s4b(g, tau, It, sigma)
        elif mode == "H1":
            if Is: ns = sa(E, sigma, Is, vs)
            if It: nt = s4b(g, tau, It, sigma)
        elif mode == "H2":
            if Is: ns = s4a(g, sigma, Is, list(sbar))
        elif mode == "H4":
            if Is:
                Wg = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
                wv, _ = Wg.evaluate(tuple(sigma)); Wi = set(Wg.improving(tuple(sigma), wv))
                J = [(v, w) for v, w in Is if (v, w) in Wi]
                if J: ns = sa(E, sigma, J, vs)
            if It: nt = s4b(g, tau, It, sigma)
        if ns == sigma and nt == tau:
            fb += 1
            if Is: ns = sa(E, sigma, Is, vs)
            else:
                for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
        if os.environ.get("WMON") == "1" and nt == tau and mode != "sa":
            Wg = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
            a, _ = Wg.evaluate(tuple(sigma)); b, _ = Wg.evaluate(tuple(ns))
            d = sum(1 for v in range(n) if Wg.key(b[v]) < Wg.key(a[v])); WD[0] += d; WD[1] += d > 0
        sigma, tau = ns, nt; taus.append(tuple(tau))
    runs, cur = [], 1
    for a, b in zip(taus, taus[1:]):
        if a == b: cur += 1
        else: runs.append(cur); cur = 1
    runs.append(cur)
    win, _ = E.regions(tuple(sigma))
    run.WD = WD
    return it, fb, max(runs) - 1, len(runs), win
if __name__ == "__main__":
    mode, path = sys.argv[1], sys.argv[2]; cap = int(sys.argv[sys.argv.index("--cap") + 1]) if "--cap" in sys.argv else 10 ** 5
    g = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
    it, fb, L, R, win = run(g, mode, cap)
    print(f"HYB {mode} {os.path.basename(path)} n {g.n} iterations {it} fallbacks {fb} tau-runs {R} longest-tau-run {L} win_even {sum(1 for x in win if x == 0)}" + (f" WDROP {run.WD[0]} WDROPIT {run.WD[1]}" if os.environ.get("WMON") == "1" else ""))
