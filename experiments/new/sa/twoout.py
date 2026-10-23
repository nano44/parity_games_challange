#!/usr/bin/env python3
"""One-player all-odd 2-out games (N9-screen.md §1(c)): n Even vertices, priority 1, two distinct successors, no
self-loops; every sigma is a functional graph, hence has a cycle: Odd wins everywhere. Families:
  circ n a b : v -> v+a, v+b (mod n);   rand n seed : two random successors.
Usage: twoout.py circ NMIN NMAX KMAX A B [--sym] (rotation-orbit reduction, exact) | twoout.py rand N COUNT KMAX SEED0"""
import os, sys, time, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
import pg
from sa import sa_feasible, even_wins_all


def circ(n, a, b):
    return pg.Game([1] * n, [0] * n, [[(v + a) % n, (v + b) % n] for v in range(n)])


def rand2(n, seed):
    r = random.Random(seed)
    return pg.Game([1] * n, [0] * n, [r.sample([w for w in range(n) if w != v], 2) for v in range(n)])


def rotations(n):
    return [[(v + r) % n for v in range(n)] for r in range(n)]


def kstar(g, kmax, group=None):
    assert not even_wins_all(g)
    for k in range(1, kmax + 1):
        if not sa_feasible(g, k, group=group):
            kstar.method = sa_feasible.last_method
            return k
    kstar.method = sa_feasible.last_method
    return None  # > kmax


if __name__ == "__main__":
    if sys.argv[1] == "circ":
        nmin, nmax, kmax, a, b = map(int, sys.argv[2:7])
        for n in range(nmin, nmax + 1):
            t = time.time(); ks = kstar(circ(n, a, b), kmax, rotations(n) if "--sym" in sys.argv else None)
            print(f"circ({n},{a},{b}) k*={ks if ks else '>' + str(kmax)} ({time.time()-t:.0f}s; infeasible verdict by {kstar.method})", flush=True)
    else:
        n, cnt, kmax, s0 = map(int, sys.argv[2:6])
        hist = {}
        for s in range(s0, s0 + cnt):
            ks = kstar(rand2(n, s), kmax); key = ks if ks else f">{kmax}"
            hist[key] = hist.get(key, 0) + 1
            if not ks or ks >= 3:
                print(f"rand2({n},{s}) k*={key}", flush=True)
        print(f"rand2 n={n} seeds {s0}..{s0+cnt-1}: k* histogram {hist}", flush=True)
