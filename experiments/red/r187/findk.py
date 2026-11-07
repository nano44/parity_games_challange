#!/usr/bin/env python3
"""L-RED R187 FINDK: search tiny games for a STUCK pair (sigma, tau): an N5 state at which S4a keeps sigma and S4b keeps tau although
I_sigma u I_tau != {} (the state at which S4c would fire), with a vertex u whose Xi_sigma cycle node k_s (Odd's best reply to sigma)
and Xi_tau cycle node k_t (Even's best reply to tau) satisfy: k_t even, prio(k_t) > prio(k_s). Usage: findk.py n trials seed"""
import sys, os, random, itertools
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "..", "new", "box21")]
from n5x import step, Engine, dual
import pg
def search(n, trials, seed):
    rng = random.Random(seed)
    for t in range(trials):
        own = [rng.randint(0, 1) for _ in range(n)]; prio = rng.sample(range(2 * n), n)
        succ = [sorted(rng.sample(range(n), rng.randint(1, 2))) for _ in range(n)]
        g = pg.Game(prio, own, succ); E, Ed = Engine(g), Engine(dual(g))
        ch = [succ[v] if own[v] == 0 else [-1] for v in range(n)]; cht = [succ[v] if own[v] == 1 else [-1] for v in range(n)]
        for s in itertools.product(*ch):
            for tt in itertools.product(*cht):
                r = step(g, E, Ed, list(s), list(tt))
                if r is None or not r[4]: continue
                vs, vt = r[5], r[6]
                for u in range(n):
                    ks, kt = vs[u][0], vt[u][0]
                    if prio[kt] % 2 == 0 and prio[kt] > prio[ks]:
                        yield g, s, tt, u, ks, kt
if __name__ == "__main__":
    n, T, seed = map(int, sys.argv[1:4]); c = 0
    for g, s, t, u, ks, kt in search(n, T, seed):
        print("prio", g.prio, "own", g.owner, "succ", g.succ, "sigma", s, "tau", t, "u", u, "ks", ks, "kt", kt); c += 1
        if c >= 5: break
