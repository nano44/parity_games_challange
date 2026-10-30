#!/usr/bin/env python3
"""L-SI box 52: model BI1P ("two one-player games"), the W-run of N5 with sbar FROZEN at a fixed Odd strategy rho and tau fixed, with
the two N5 constraints dropped (rho need not stay Odd's best reply, tau need not stay Odd's arena optimum). One step from sigma:
  Xi := val(sigma, rho) (one-player arena G_rho), Is := Xi-improving Even edges (si.Engine.improving on G_rho);
  if Is is empty: stop; sigma' := S4a's arena optimum against tau over {sigma} + Is (as n5x.step); if sigma' == sigma: stop (S4c).
run(g, rho, tau, sigma) -> list of states. A model run is an upper envelope only for sbar-frozen W-runs: every such W-run of N5 is a
BI1P run (same S2 / S4a code), not conversely.  CLI: bi1p.py N SEED TRIES  (random search, prints the longest run found)."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import Engine, dual
import pg

def fixodd(g, strat):
    return pg.Game(list(g.prio), list(g.owner), [[strat[v]] if g.owner[v] == 1 else g.succ[v] for v in range(g.n)])

def run(g, rho, tau, sigma, cap=10 ** 4):
    n = g.n; Er = Engine(fixodd(g, rho)); sigma = tuple(sigma); out = [sigma]
    while len(out) <= cap:
        xi, _ = Er.evaluate(sigma); Is = Er.improving(sigma, xi)
        if not Is: break
        opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
        for v, w in Is: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
        Ea = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
        _, best = Ea.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
        ns = tuple(best[v] if g.owner[v] == 0 else -1 for v in range(n))
        if ns == sigma: break
        sigma = ns; out.append(sigma)
    return out

def rgame(n, rng, deg=3):
    prio = rng.sample(range(n), n); owner = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(set(rng.choice(range(n)) for _ in range(rng.randint(1, deg)))) for _ in range(n)]
    return pg.Game(prio, owner, succ)

if __name__ == "__main__":
    N, seed, tries = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); best = (0, None)
    for _ in range(tries):
        g = rgame(N, rng); rho = [rng.choice(g.succ[v]) if g.owner[v] == 1 else -1 for v in range(N)]
        tau = [rng.choice(g.succ[v]) if g.owner[v] == 1 else -1 for v in range(N)]
        sig = [rng.choice(g.succ[v]) if g.owner[v] == 0 else -1 for v in range(N)]
        L = len(run(g, rho, tau, sig)) - 1
        if L > best[0]: best = (L, (g.prio, g.owner, g.succ, rho, tau, sig))
    print("BI1P N", N, "seed", seed, "longest", best[0]); print(best[1])
