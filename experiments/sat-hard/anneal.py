#!/usr/bin/env python3
"""Simulated annealing for a k-state weak (n,d)-separator (convention E): cost = number of graphs (even + odd, from
graphs.family) the automaton violates (check.py). Finds upper bounds only; any 0-cost automaton is reported and must
be re-verified (check.py does that by construction; search.py --verify re-checks again).
Usage: anneal.py n d k [--seed S] [--steps N] [--t0 T]"""
import sys, os, random, math, json, time, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import graphs, check

ap = argparse.ArgumentParser()
ap.add_argument("n", type=int); ap.add_argument("d", type=int); ap.add_argument("k", type=int)
ap.add_argument("--seed", type=int, default=1); ap.add_argument("--steps", type=int, default=200000)
ap.add_argument("--t0", type=float, default=2.0)
a = ap.parse_args()
rnd = random.Random(a.seed)
evens, odds = graphs.family(a.n, a.d, 0), graphs.family(a.n, a.d, 1)
k, d = a.k, a.d


def cost(delta):
    return len(check.violations({"k": k, "d": d, "delta": delta}, evens, odds))


delta = [[rnd.choice(list(range(k)) + [None]) for _ in range(d)] for _ in range(k)]
c = cost(delta); best = c; t0 = time.time()
for step in range(a.steps):
    T = a.t0 * (1 - step / a.steps) + 1e-3
    q, p = rnd.randrange(k), rnd.randrange(d)
    old = delta[q][p]
    new = rnd.choice([x for x in list(range(k)) + [None] if x != old])
    delta[q][p] = new
    c2 = cost(delta)
    if c2 <= c or rnd.random() < math.exp((c - c2) / T):
        c = c2
        if c < best:
            best = c
            print(f"step {step} cost {c} ({time.time()-t0:.0f}s)", flush=True)
            if c == 0:
                print("FOUND", json.dumps({"k": k, "d": d, "delta": delta}), flush=True)
                break
    else:
        delta[q][p] = old
print(f"done best={best} {time.time()-t0:.0f}s")
