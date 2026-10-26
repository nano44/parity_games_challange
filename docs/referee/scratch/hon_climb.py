#!/usr/bin/env python3
"""REFEREE succ. 14: hill climb for packet P-N5-HON. Every candidate is checked by hon_probe.analyse (all checks, LEV exact, n <= LEVMAX).
Fitness = (gaps with a fallback strictly inside (f_in gaps), max W-honest states in a phase, fallbacks at honest states). Mutations: redirect
an edge, add / drop an edge, flip an owner, swap two priorities. Own engine only.
Usage: hon_climb.py n kmax steps seed [out.pg]"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D, hon_probe as HP


def evaluate(g, rng):
    cnt = Counter()
    for s0 in [RE.best_reward_start(g)] + [D.rand_start(g, random.Random(i)) for i in range(2)]:
        HP.analyse(g, s0, cnt, "climb")
    fails = sum(v for k, v in cnt.items() if k.endswith("_FAIL"))
    return (cnt["FFGAP_inside"], cnt["f_in_total"], cnt["MAX_HONEST"], cnt["fb_at_honest"]), fails, cnt


def mutate(g, rng):
    prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
    n = g.n; r = rng.random()
    v = rng.randrange(n)
    if r < 0.35: succ[v][rng.randrange(len(succ[v]))] = rng.randrange(n)
    elif r < 0.55: succ[v].append(rng.randrange(n))
    elif r < 0.7 and len(succ[v]) > 1: succ[v].pop(rng.randrange(len(succ[v])))
    elif r < 0.8: owner[v] = 1 - owner[v]
    else:
        w = rng.randrange(n); prio[v], prio[w] = prio[w], prio[v]
    return RE.Game(prio, owner, succ)


def nodd(g): return sum(1 for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1)


def main(a):
    n, km, steps, seed = map(int, a[:4]); rng = random.Random(seed)
    g = D.rand_ck(rng, n, min(km, n - 1)); fit, fails, cnt = evaluate(g, rng)
    tot = Counter(); bad = []
    for it in range(steps):
        h = mutate(g, rng)
        if nodd(h) > km or nodd(h) == 0: continue
        try: f2, fl2, c2 = evaluate(h, rng)
        except RecursionError: continue
        tot["CANDIDATES"] += 1
        for k, v in c2.items():
            if k.endswith("_FAIL") or k.endswith("_chk"): tot[k] += v
        if fl2: bad.append((it, c2)); print("FAIL at", it, {k: v for k, v in c2.items() if k.endswith("_FAIL")}, HP.EX[-3:], flush=True)
        if f2 >= fit: g, fit = h, f2
    print("BEST", fit, "n", g.n, "k", nodd(g))
    for k in sorted(tot): print(k, tot[k])
    if len(a) > 4:
        with open(a[4], "w") as f:
            f.write("parity %d;\n" % (g.n - 1))
            for v in range(g.n): f.write("%d %d %d %s;\n" % (v, g.prio[v], g.owner[v], ",".join(map(str, g.succ[v]))))


if __name__ == "__main__":
    main(sys.argv[1:])
