#!/usr/bin/env python3
"""Adversarial search for games maximizing a rule's iteration count (falsification step 3b).
Hill-climb with restarts over games with n vertices, priorities in 0..n, out-degree 1..n (self-loops allowed):
mutations = change a priority, flip an owner, add/remove an edge.  Objective = iterations (for randomized rules:
mean over --samples seeds).  Writes the best game per n to out/adv_<rule>_n<n>.pg and a summary line.
Usage: adversarial.py RULE --n 4,5,6 [--restarts 20] [--steps 400] [--samples 1] [--seed 0] [--start best]"""
import sys, os, random, argparse, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, si

ap = argparse.ArgumentParser()
ap.add_argument("rule"); ap.add_argument("--n", default="4,5,6,7,8"); ap.add_argument("--restarts", type=int, default=20)
ap.add_argument("--steps", type=int, default=400); ap.add_argument("--samples", type=int, default=1); ap.add_argument("--seed", type=int, default=0)
ap.add_argument("--start", default="best"); ap.add_argument("--budget", type=float, default=1e9, help="seconds per n")
a = ap.parse_args()


def score(g):
    tot = 0
    for s in range(a.samples):
        tot += si.solve(g, a.rule, seed=s, start=a.start)[2]
    return tot / a.samples


def mutate(g, rng, n):
    prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
    k = rng.randrange(4)
    v = rng.randrange(n)
    if k == 0:
        prio[v] = rng.randrange(n + 1)
    elif k == 1:
        owner[v] ^= 1
    elif k == 2:
        w = rng.randrange(n)
        if w not in succ[v]:
            succ[v].append(w)
    else:
        if len(succ[v]) > 1:
            succ[v].remove(rng.choice(succ[v]))
    return pg.Game(prio, owner, succ)


def rand_game(rng, n):
    return pg.Game([rng.randrange(n + 1) for _ in range(n)], [rng.randrange(2) for _ in range(n)],
                   [sorted(rng.sample(range(n), rng.randint(1, min(n, 3)))) for _ in range(n)])


os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
for n in [int(x) for x in a.n.split(",")]:
    rng = random.Random(a.seed * 1000 + n); t0 = time.time()
    best_g, best_s = None, -1
    for r in range(a.restarts):
        if time.time() - t0 > a.budget:
            break
        g = rand_game(rng, n); s = score(g)
        for step in range(a.steps):
            g2 = mutate(g, rng, n); s2 = score(g2)
            if s2 >= s:
                g, s = g2, s2
        if s > best_s:
            best_g, best_s = g, s
    path = os.path.join(HERE, "out", f"adv_{a.rule}_n{n}.pg"); pg.write(best_g, path)
    print(f"{a.rule} n={n}: max iterations {best_s} (m={best_g.m}, restarts {r + 1}, {time.time() - t0:.0f}s) -> {path}", flush=True)
