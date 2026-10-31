#!/usr/bin/env python3
"""L-COMP box 24: hill climbs on the root-map quantities of casc.py (engine n5b SPEC). Mutations and start handling as n5-box23/climb23.py
(start pair mutated; --s3 keeps the S3 start). Fitness over the run's W-runs, by --fit:
  (third key of every fitness: the W-run's number of returns, a gradient when the first two are 0)
  pxr     (max returns of one Even X per root, its W-run's |F|)          [Lead 22:17Z (1), CASC-EDGE]
  kidsret (max children of a RETURN node, max depth)                     [Lead 22:17Z (2), CONJECTURE NARROW]
  depth   (max root-chain depth, max children of a return node)          [Lead 22:17Z (2)]
  casc    (max returns per root, |F|)
A W-run with a NOEVEN / NORISE event (a failure of EVEN-ON-PLAY / WINDOW-RISE, box 100) stops the climb and is written to OUT_viol.
Usage: climb24.py N SEED --fit pxr|kidsret|depth|casc --secs S [--s3] [--seed-pg FILE.pg[:START]] --out OUTPREFIX"""
import argparse
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "n5-box23"))
import casc  # noqa: E402
import climb23 as C  # noqa: E402
import n5b  # noqa: E402
import pg  # noqa: E402
import rstar  # noqa: E402

KEY = {"pxr": ("pxr", "F", "returns"), "kidsret": ("kids_ret", "maxdepth", "returns"), "depth": ("maxdepth", "kids_ret", "returns"),
       "casc": ("casc", "F", "returns")}


def score(g, s, t, fit):
    try:
        states, runs = casc.analyse(g, (tuple(s), tuple(t)))
    except (n5b.RepeatedState, RecursionError, KeyError):
        return (-1, 0, 0), None
    if len(states) > C.CAP:
        return (-1, 0, 0), None
    if any(r["bad"] for r in runs):
        return (10 ** 9, 0, 0), [r for r in runs if r["bad"]]
    return max([tuple(r[k] for k in KEY[fit]) for r in runs], default=(0, 0, 0)), runs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int); ap.add_argument("seed", type=int); ap.add_argument("--fit", choices=list(KEY), required=True)
    ap.add_argument("--secs", type=float, default=600); ap.add_argument("--steps", type=int, default=10 ** 9)
    ap.add_argument("--s3", action="store_true"); ap.add_argument("--seed-pg"); ap.add_argument("--out", required=True)
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
    if a.s3:
        s, t = map(list, rstar.Eng(g).start())
    cur, _ = score(g, s, t, a.fit); best = (cur, g, s, t); t0 = time.time(); step = 0
    print(f"START fit {cur} n {g.n}", flush=True)
    while step < a.steps and time.time() - t0 < a.secs:
        step += 1
        h, hs, ht = C.mutate(g, s, t, rng)
        if a.s3:
            hs, ht = map(list, rstar.Eng(h).start())
        f, info = score(h, hs, ht, a.fit)
        if f[0] >= 10 ** 9:
            print("VIOLATION (NOEVEN / NORISE) during climb:", info[:2], flush=True); C.write(h, hs, ht, a.out + "_viol"); best = (f, h, hs, ht); break
        if f >= cur:
            if f > best[0]:
                print(f"BEST step {step} fit {f} t {time.time() - t0:.0f}s", flush=True); best = (f, h, hs, ht)
            g, s, t, cur = h, hs, ht, f
    f, g, s, t = best
    C.write(g, s, t, a.out)
    print(f"END steps {step} best {f} n {g.n} secs {time.time() - t0:.0f} -> {a.out}.pg", flush=True)


if __name__ == "__main__":
    main()
