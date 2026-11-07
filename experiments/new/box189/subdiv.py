#!/usr/bin/env python3
"""Box 189 SUBDIV test (CONJECTURE, data only): for a game G and ANY start pair (s0, t0), the game G^pad := G with every priority + 4
and EVERY edge a -> b subdivided by a single-successor Even pad p(a,b) (indices n, n+1, ... in (a, b) order; Om(p) = 2 if a is Even
and b = s0(a), 1 if a is Odd and b = t0(a), 0 otherwise) has S3's start = (s0, t0) transported, and N5 from S3 on G^pad runs state
for state as N5 from (s0, t0) on G (projection: choice p(a, b) -> b). Usage: subdiv.py SEED COUNT NMAX"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, "experiments/new/box21"), os.path.join(ROOT, "experiments/new"), os.path.join(ROOT, "experiments/si"), os.path.join(ROOT, "experiments/harness")]
import pg, n5x, n5
from si import Engine

def pad(g, s0, t0):
    n = g.n; E = sorted((a, b) for a in range(n) for b in g.succ[a]); P = {e: n + i for i, e in enumerate(E)}
    prio = [p + 4 for p in g.prio] + [0] * len(E); own = list(g.owner) + [0] * len(E); succ = [None] * (n + len(E))
    for a in range(n): succ[a] = sorted(P[(a, b)] for b in g.succ[a])
    for (a, b), p in P.items():
        succ[p] = [b]
        if g.owner[a] == 0 and s0[a] == b: prio[p] = 2
        if g.owner[a] == 1 and t0[a] == b: prio[p] = 1
    return pg.Game(prio, own, succ), P

def rgame(rng, n):
    prio = [rng.randint(0, n) for _ in range(n)]; own = [rng.randint(0, 1) for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), rng.randint(1, min(3, n))))) for _ in range(n)]
    return pg.Game(prio, own, succ)

if __name__ == "__main__":
    seed, cnt, nmax = map(int, sys.argv[1:4]); rng = random.Random(seed); ok = 0; its = []
    for i in range(cnt):
        g = rgame(rng, rng.randint(3, nmax))
        s0 = {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}; t0 = {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}
        A, fa = n5x.trace(g, (s0, t0), check=False)
        h, P = pad(g, s0, t0); B, fb = n5x.trace(h, None, check=False)
        inv = {p: b for (a, b), p in P.items()}
        Bp = [(tuple(inv[s[v]] if g.owner[v] == 0 else A[0][0][v] for v in range(g.n)), tuple(inv[t[v]] if g.owner[v] == 1 else A[0][1][v] for v in range(g.n))) for s, t in B]
        Ap = [(tuple(s[v] if g.owner[v] == 0 else A[0][0][v] for v in range(g.n)), tuple(t[v] if g.owner[v] == 1 else A[0][1][v] for v in range(g.n))) for s, t in A]
        same = Ap == Bp and fa == fb; ok += same; its.append(len(A) - 1)
        if not same:
            print(f"MISMATCH i {i} n {g.n} iters G {len(A) - 1} (fb {fa}) Gpad {len(B) - 1} (fb {fb}) first diff at",
                  next((j for j in range(min(len(Ap), len(Bp))) if Ap[j] != Bp[j]), min(len(Ap), len(Bp))))
    print(f"SUBDIV seed {seed} games {cnt} nmax {nmax}: identical runs {ok}/{cnt}; iterations max {max(its)}")
