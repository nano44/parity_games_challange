#!/usr/bin/env python3
"""Box 21 probe H1: along N5 runs from (sigma_0, tau*) (tau* honest-optimal for Odd), is every edge that is improving for Even in
the one-player game G_tau* (play values W against tau*) also honest-improving (Iσ)? Counts violations.
Usage: h1.py NGAMES nmin nmax seed"""
import sys, random
from n5x import *
def wvals(g, sigma, tau):
    """W = Even-order valuation of the play under (sigma, tau): the S1 valuation in the arena where both are fixed."""
    succ = [[sigma[v]] if g.owner[v] == 0 else [tau[v]] for v in range(g.n)]
    Eg = Engine(pg.Game(list(g.prio), list(g.owner), succ))
    val, _ = Eg.evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(g.n)))
    return Eg, val
def main(N, nmin, nmax, seed):
    rng = random.Random(seed); viol = checks = games = 0; ex = None
    for _ in range(N):
        n = rng.randint(nmin, nmax)
        prio = [rng.randrange(n) for _ in range(n)]; owner = [rng.randrange(2) for _ in range(n)]
        succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for _ in range(n)]
        g = pg.Game(prio, owner, succ); E = Engine(g)
        states, _ = trace(g, check=False); s0, ts = states[0][0], states[-1][1]
        st = ({v: s0[v] for v in range(n) if owner[v] == 0}, {v: ts[v] for v in range(n) if owner[v] == 1})
        fs, _ = trace(g, st, check=False); games += 1
        for s, t in fs:
            vs, _ = E.evaluate(s); Is = set(E.improving(s, vs))
            Eg, W = wvals(g, s, t)
            for v in range(n):
                if owner[v] != 0: continue
                for w in succ[v]:
                    if w == s[v]: continue
                    # W-improving: the play value through w beats the current one (same comparison as si.py improving, on W)
                    if Eg.key(W[w]) > Eg.key(W[s[v]]):
                        checks += 1
                        if (v, w) not in Is:
                            viol += 1
                            if ex is None: ex = (g, s, t, v, w)
    print(f"games {games} W-improving edges {checks} not honest-improving {viol}")
    if ex:
        g, s, t, v, w = ex
        print("example n", g.n, "prio", g.prio, "owner", g.owner, "succ", g.succ, "sigma", s, "tau", t, "edge", (v, w))
if __name__ == "__main__": main(*map(int, sys.argv[1:]))
