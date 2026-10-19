#!/usr/bin/env python3
"""R-N5K9 check 1: si.py's computed counter-strategy sigma-bar is OPTIMAL, i.e. Theta_{sigma, sbar} = Omega_sigma at every vertex
(VJ00 (11)), for every sigma, on G and on G^d built as n5.py's dual(). Omega from n5t_probe (VJ00 §4 brute force).
Run from the repo root: python3 -I docs/referee/scratch/n5k9_sbar.py [games] [nmax] [seed]"""
import sys, os, random, itertools
R = os.getcwd(); sys.path[:0] = [os.path.join(R, "experiments/si"), os.path.join(R, "experiments/harness"), os.path.join(R, "docs/referee/scratch")]
import pg
from si import Engine
from n5t_probe import omega, theta, from_pg
games = int(sys.argv[1]) if len(sys.argv) > 1 else 300; nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 6
rnd = random.Random(int(sys.argv[3]) if len(sys.argv) > 3 else 11)
cnt = bad = strat = 0
for _ in range(games):
    n = rnd.randint(2, nmax)
    prio = [rnd.randint(0, 4) for _ in range(n)]; owner = [rnd.randint(0, 1) for _ in range(n)]
    succ = [sorted(set(rnd.sample(range(n), rnd.randint(1, min(3, n))))) for _ in range(n)]
    for dual in (False, True):
        P = [p + 1 for p in prio] if dual else prio; O = [1 - o for o in owner] if dual else owner
        E = Engine(pg.Game(list(P), list(O), [list(s) for s in succ]))
        o2, s2, plus, r = from_pg(prio, owner, succ, dual)
        evens = [v for v in range(n) if O[v] == 0]
        for ch in itertools.product(*[succ[v] for v in evens]):
            sig = [-1] * n
            for v, w in zip(evens, ch): sig[v] = w
            _, sbar = E.evaluate(tuple(sig)); strat += 1
            nxt = {r[v]: r[sig[v]] if O[v] == 0 else r[sbar[v]] for v in range(n)}
            sig2 = [None] * n
            for v in evens: sig2[r[v]] = r[sig[v]]
            Om = omega(n, o2, s2, plus, sig2)
            for v in range(n):
                cnt += 1
                if theta(v, lambda x: nxt[x]) != Om[v]:
                    bad += 1
                    if bad <= 3: print("NOT OPTIMAL", prio, owner, succ, dual, sig, list(sbar), v)
print(f"strategies={strat} vertex plays compared={cnt} Theta(sigma,sbar) != Omega: {bad}")
