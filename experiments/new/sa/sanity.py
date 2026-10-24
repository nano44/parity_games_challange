#!/usr/bin/env python3
"""Sanity: (i) the ACYC program itself (integral sigma enumeration) = Zielonka's "Even wins all"; (ii) SA at level
k = number of variable edges is exact; (iii) feasibility is monotone in k (SA_{k+1} feasible => SA_k feasible)."""
import itertools, os, sys, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pg, gen, zielonka
from sa import sa_feasible, acyc, even_wins_all


def mip_brute(g):
    succ = [sorted(set(s)) for s in g.succ]
    ev = [v for v in range(g.n) if g.owner[v] == 0]
    for ch in itertools.product(*[succ[v] for v in ev]):
        s = [list(x) for x in succ]
        for v, u in zip(ev, ch):
            s[v] = [u]
        if not zielonka._odd_wins_one_player(g.n, s, g.prio):
            return True
    return False


cnt = {"games": 0, "full_exact": 0, "mip_ok": 0, "gaps": {}}
for seed in range(int(sys.argv[1]) if len(sys.argv) > 1 else 200):
    rnd = random.Random(seed)
    n = rnd.randint(1, 6)
    g = gen.random_game(n, rnd.randint(1, 4), 1, min(3, n), seed)
    edges, _ = acyc(g)
    truth = even_wins_all(g)
    assert mip_brute(g) == truth, seed
    cnt["mip_ok"] += 1
    if len(edges) <= 8:
        kfull = len(edges)
        assert sa_feasible(g, kfull) == truth, (seed, "full level not exact")
        cnt["full_exact"] += 1
        prev = True
        for k in range(0, kfull + 1):
            f = sa_feasible(g, k)
            assert prev or not f, (seed, "not monotone")
            prev = f
            if f and not truth:
                cnt["gaps"][k] = cnt["gaps"].get(k, 0) + 1
    cnt["games"] += 1
print(cnt)
