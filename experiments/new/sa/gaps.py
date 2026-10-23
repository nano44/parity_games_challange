#!/usr/bin/env python3
"""Gap search for SA_k (N9-screen.md §1(c)). For each game G: four queries, each with a known answer:
  Q1 Even-wins-all on G; Q2 Even-wins-all on G[W_O] (answer no unless W_O empty); Q3, Q4 the same on the dual (owners
  swapped, priorities + 1), i.e. Odd-wins-all on G and on G[W_E]. A gap = SA_k feasible where the answer is no.
Usage: gaps.py random SEED0 COUNT NMIN NMAX K   |   gaps.py files K f1.pg f2.pg ..."""
import os, sys, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
import pg, gen, zielonka
from sa import sa_feasible


def sub(g, keep):
    keep = sorted(keep); ix = {v: i for i, v in enumerate(keep)}
    return pg.Game([g.prio[v] for v in keep], [g.owner[v] for v in keep],
                   [[ix[w] for w in g.succ[v] if w in ix] for v in keep])


def dual(g):
    return pg.Game([p + 1 for p in g.prio], [1 - o for o in g.owner], g.succ)


def queries(g):
    win = zielonka.solve(g)
    WE = {v for v in range(g.n) if win[v] == 0}; WO = set(range(g.n)) - WE
    qs = [("Q1", g, not WO)]
    if WO and WE:
        qs.append(("Q2", sub(g, WO), False))
    d = dual(g)
    qs.append(("Q3", d, not WE))
    if WO and WE:
        qs.append(("Q4", sub(d, WE), False))
    return qs


def run(games, k, tag):
    gaps, nq, t0 = [], 0, time.time()
    for name, g in games:
        for q, h, truth in queries(g):
            f = sa_feasible(h, k)
            nq += 1
            if truth:
                assert f, (name, q, "SA infeasible on a yes-instance: bug")
            elif f:
                gaps.append((name, q, h.n))
                print(f"GAP k={k} {name} {q} n={h.n}", flush=True)
    print(f"{tag} k={k}: {len(games)} games, {nq} queries, {len(gaps)} gaps, {time.time()-t0:.0f}s", flush=True)
    return gaps


if __name__ == "__main__":
    if sys.argv[1] == "random":
        s0, cnt, nmin, nmax, k = map(int, sys.argv[2:7])
        games = []
        for seed in range(s0, s0 + cnt):
            rnd = random.Random(seed)
            n = rnd.randint(nmin, nmax)
            games.append((f"r{seed}", gen.random_game(n, rnd.randint(2, n + 1), 1, min(3, n), seed)))
        run(games, k, f"random seeds {s0}..{s0+cnt-1} n {nmin}-{nmax}")
    else:
        k = int(sys.argv[2])
        run([(os.path.basename(f), pg.read(f)) for f in sys.argv[3:]], k, "files")
