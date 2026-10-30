#!/usr/bin/env python3
"""L-COMP box 23 (c): hill climbs MAXIMISING R*_F per W-run of N5 (rstar.py definitions; engine n5b SPEC).
Individual = (game on n vertices, start pair). Mutation (one per step, as experiments/n5-epoch/climb.py): change one priority (0..n),
flip one owner, replace / add / remove one edge (every vertex keeps >= 1 successor), or change one start entry; the start pair is
repaired after owner / edge changes. Accept if fitness >= current (sideways moves allowed).
Fitness = (max over the run's W-runs of R*_F, sum over W-runs of R*_F, |F| of the argmax run). Runs with > 5,000 iterations score -1.
A FREE-RED violation (|F| > (n-1)(R*_F+1) + FL_F) or an incl != strict W-run stops the climb and is written to OUT_viol.
Start: random game (out-degree 1..3, owners and priorities 0..n uniform) with S3 start, or --seed-pg FILE.pg[:START] padded with
Even self-loop vertices to n. Budget --secs and/or --steps. Output: OUT.pg + OUT.start of the best; log 'BEST step fit', 'END ...'.
Usage: climb23.py N SEED --secs S [--steps K] [--seed-pg FILE.pg[:START]] --out OUTPREFIX"""
import argparse
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rstar  # noqa: E402
import n5b  # noqa: E402
import pg  # noqa: E402
from n5b import EVEN  # noqa: E402

CAP = 5000


class Cap(Exception):
    pass


def score(g, s, t):
    e = rstar.Eng(g); x = (tuple(s), tuple(t)); states, fbs, data = [], [], []; seen = set()
    try:
        while True:
            if x in seen or len(states) > CAP:
                raise Cap()
            seen.add(x); states.append(x); data.append(e.sdata(*x)); nx = e.step(*x)
            if nx is None:
                break
            fbs.append(nx[2]); x = (nx[0], nx[1])
    except (Cap, n5b.RepeatedState, RecursionError):
        return (-1, 0, 0), None
    runs = [rstar.measure(e, states, data, a, b) for a, b in rstar.wruns(e, states, fbs, data)]
    bad = [r for r in runs if r["F"] > (g.n - 1) * (r["rs"] + 1) + r["fl"] or r["ri"] != r["rs"]]
    if bad:
        return (10 ** 9, 0, 0), bad
    if not runs:
        return (0, 0, 0), runs
    top = max(runs, key=lambda r: (r["rs"], r["F"]))
    return (top["rs"], sum(r["rs"] for r in runs), top["F"]), runs


def mutate(g, s, t, rng):
    n = g.n; prio, owner, succ = list(g.prio), list(g.owner), [list(x) for x in g.succ]; s, t = list(s), list(t)
    r = rng.randrange(6); v = rng.randrange(n)
    if r == 0:
        prio[v] = rng.randrange(n + 1)
    elif r == 1:
        owner[v] = 1 - owner[v]
    elif r == 2:
        succ[v][rng.randrange(len(succ[v]))] = rng.randrange(n)
    elif r == 3:
        succ[v].append(rng.randrange(n))
    elif r == 4 and len(succ[v]) > 1:
        succ[v].pop(rng.randrange(len(succ[v])))
    succ = [sorted(set(x)) for x in succ]
    h = pg.Game(prio, owner, succ)
    for x in range(n):
        if owner[x] == EVEN:
            t[x] = -1
            if s[x] not in succ[x]:
                s[x] = succ[x][0]
        else:
            s[x] = -1
            if t[x] not in succ[x]:
                t[x] = succ[x][0]
    if r == 5:
        x = rng.randrange(n)
        (s if owner[x] == EVEN else t)[x] = rng.choice(succ[x])
    return h, s, t


def write(g, s, t, out):
    pg.write(g, out + ".pg")
    with open(out + ".start", "w") as fh:
        fh.write("SIGMA0 " + " ".join(f"{v}:{s[v]}" for v in range(g.n) if g.owner[v] == EVEN) + "\n")
        fh.write("TAU0 " + " ".join(f"{v}:{t[v]}" for v in range(g.n) if g.owner[v] != EVEN) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int); ap.add_argument("seed", type=int); ap.add_argument("--secs", type=float, default=600)
    ap.add_argument("--steps", type=int, default=10 ** 9); ap.add_argument("--seed-pg"); ap.add_argument("--out", required=True)
    a = ap.parse_args(); rng = random.Random(a.seed)
    if a.seed_pg:
        path, _, st = a.seed_pg.partition(":")
        g0 = pg.read(path); e0 = rstar.Eng(g0)
        s, t = rstar.overlay(g0, e0.start(), n5b.read_start(st, g0)) if st else e0.start()
        n = max(a.n, g0.n); s, t = list(s), list(t)
        g = pg.Game(list(g0.prio) + [0] * (n - g0.n), list(g0.owner) + [0] * (n - g0.n),
                    [list(x) for x in g0.succ] + [[v] for v in range(g0.n, n)])
        s += list(range(g0.n, n)); t += [-1] * (n - g0.n)
    else:
        n = a.n
        g = pg.Game([rng.randrange(n + 1) for _ in range(n)], [rng.randrange(2) for _ in range(n)],
                    [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 3)))) for _ in range(n)])
        s, t = map(list, rstar.Eng(g).start())
    cur, _ = score(g, s, t); best = (cur, g, s, t); t0 = time.time(); step = 0
    print(f"START fit {cur} n {g.n}", flush=True)
    while step < a.steps and time.time() - t0 < a.secs:
        step += 1
        h, hs, ht = mutate(g, s, t, rng)
        f, info = score(h, hs, ht)
        if f[0] >= 10 ** 9:
            print("VIOLATION during climb:", info[:3], flush=True); write(h, hs, ht, a.out + "_viol"); best = (f, h, hs, ht); break
        if f >= cur:
            if f > best[0]:
                print(f"BEST step {step} fit {f} t {time.time() - t0:.0f}s", flush=True); best = (f, h, hs, ht)
            g, s, t, cur = h, hs, ht, f
    f, g, s, t = best
    write(g, s, t, a.out)
    print(f"END steps {step} best {f} n {g.n} secs {time.time() - t0:.0f} -> {a.out}.pg", flush=True)


if __name__ == "__main__":
    main()
