#!/usr/bin/env python3
"""L-COMP box 25: hill climbs on INS (ins.py; engine n5b SPEC). Mutations and start handling as n5-box23/climb23.py (start pair mutated).
Fitness = (max INS_I(c) over the run's W-constant intervals and even cycle nodes, |I| of that (I, c), the run's longest W-run).
Any LTX / TSX / NOVT / KB violation (a failure of LEX-TREE / TREE-STABLE / OVERTAKE / KEYCH <= 1 + INS) stops the climb (OUT_viol).
Usage: climb25.py N SEED --secs S [--seed-pg FILE.pg[:START]] --out OUTPREFIX"""
import argparse
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "n5-box23"))
import ins  # noqa: E402
import climb23 as C  # noqa: E402
import n5b  # noqa: E402
import pg  # noqa: E402
import rstar  # noqa: E402


def score(g, s, t):
    try:
        states, r = ins.analyse(g, (tuple(s), tuple(t)))
    except (n5b.RepeatedState, RecursionError, KeyError, ValueError):
        return (-1, 0, 0), None
    if len(states) > C.CAP:
        return (-1, 0, 0), None
    if r["LTX"] or r["TSX"] or r["NOVT"] or r["KB"]:
        return (10 ** 9, 0, 0), r
    b = r["best"]
    return ((b[0], b[1], b[2]) if b else (0, 0, 0)), r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int); ap.add_argument("seed", type=int); ap.add_argument("--secs", type=float, default=900)
    ap.add_argument("--seed-pg"); ap.add_argument("--out", required=True)
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
    while time.time() - t0 < a.secs:
        step += 1
        h, hs, ht = C.mutate(g, s, t, rng)
        f, info = score(h, hs, ht)
        if f[0] >= 10 ** 9:
            print("VIOLATION during climb:", info, flush=True); C.write(h, hs, ht, a.out + "_viol"); best = (f, h, hs, ht); break
        if f >= cur:
            if f > best[0]:
                print(f"BEST step {step} fit {f} t {time.time() - t0:.0f}s", flush=True); best = (f, h, hs, ht)
            g, s, t, cur = h, hs, ht, f
    f, g, s, t = best
    C.write(g, s, t, a.out)
    print(f"END steps {step} best {f} n {g.n} secs {time.time() - t0:.0f} -> {a.out}.pg", flush=True)


if __name__ == "__main__":
    main()
