#!/usr/bin/env python3
"""N1 adversarial search (L-SI's adversarial.py scheme, own code): hill climb with restarts over games with n vertices,
priorities 0..n, out-degree >= 1; mutations: priority, owner, add/remove edge. Objective: N1 total Even iterations
(--obj even) or the largest single phase (--obj phase). Every best game is re-checked against Zielonka.
Usage: anneal_adv.py --n 6,8,10 [--restarts R] [--steps S] [--seed X] [--obj even|phase]; writes out/adv/adv_<obj>_n<n>.pg"""
import sys, os, random, argparse
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "harness")); sys.path.insert(0, HERE)
import pg, zielonka, verify, anneal
anneal.COMPRESS = False   # N1 as specified: no priority merging
ap = argparse.ArgumentParser(); ap.add_argument("--n", default="6,8"); ap.add_argument("--restarts", type=int, default=10)
ap.add_argument("--steps", type=int, default=300); ap.add_argument("--seed", type=int, default=0); ap.add_argument("--obj", default="even")
a = ap.parse_args(); rng = random.Random(a.seed); os.makedirs(os.path.join(HERE, "out", "adv"), exist_ok=True)
def score(g):
    (win, strat), J, E, O, per = anneal.solve(g)
    return E if a.obj == "even" else max(per)
def rand_game(n):
    succ = [sorted(rng.sample(range(n), rng.randint(1, min(3, n)))) for _ in range(n)]
    return pg.Game([rng.randint(0, n) for _ in range(n)], [rng.randint(0, 1) for _ in range(n)], succ)
def mutate(g):
    n = g.n; pr, ow, sc = list(g.prio), list(g.owner), [list(s) for s in g.succ]; k = rng.randint(0, 2); v = rng.randrange(n)
    if k == 0: pr[v] = rng.randint(0, n)
    elif k == 1: ow[v] = 1 - ow[v]
    else:
        w = rng.randrange(n)
        if w in sc[v]:
            if len(sc[v]) > 1: sc[v].remove(w)
        else: sc[v] = sorted(sc[v] + [w])
    return pg.Game(pr, ow, sc)
for n in map(int, a.n.split(",")):
    best, bs = None, -1
    for r in range(a.restarts):
        g = rand_game(n); s = score(g)
        for t in range(a.steps):
            h = mutate(g); hs = score(h)
            if hs >= s: g, s = h, hs
        if s > bs: best, bs = g, s
    (win, strat), J, E, O, per = anneal.solve(best)
    ok = win == zielonka.solve(best) and not verify.check(best, win, strat)
    pg.write(best, os.path.join(HERE, "out", "adv", f"adv_{a.obj}_n{n}.pg"))
    print(f"n={n} obj={a.obj} best={bs} even={E} odd={O} phases={J} per_nonzero={[p for p in per if p]} check={'OK' if ok else 'FAIL'}", flush=True)
