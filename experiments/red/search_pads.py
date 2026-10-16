#!/usr/bin/env python3
"""Random search over pad schemes for Friedmann's G_n under S7 (L-RED, R3). A scheme gives every vertex class
(d, g, k, s, r, c, t, a, e, f, h) pads = alpha + beta * (n + 1 - i) (i = the gate/lane index; alpha only for s, r, c).
Scores the number of S7 iterations with L-SI's vjfast at n = N0; re-scores the best schemes at larger n.
Usage: search_pads.py VJFAST [--samples 400] [--n0 3] [--seed 0] [--top 15]"""
import sys, os, random, subprocess, tempfile, argparse, math
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import gens_red
ap = argparse.ArgumentParser(); ap.add_argument("vjfast"); ap.add_argument("--samples", type=int, default=400)
ap.add_argument("--n0", type=int, default=3); ap.add_argument("--seed", type=int, default=0); ap.add_argument("--top", type=int, default=15)
ap.add_argument("--timeout", type=float, default=60); ap.add_argument("--climb", action="store_true"); a = ap.parse_args(); rng = random.Random(a.seed)
CLASSES = ["d", "g", "k", "s", "r", "c", "t", "a", "e", "f", "h"]
VALS = [0, 0, 0, 1, 2, 4, 8, 16, 32, 64, 128, 256]


def scheme_pads(sch, n):
    pads = {}
    for cls in CLASSES:
        al, be = sch[cls]
        if cls in ("s", "r", "c"):
            if al: pads[cls] = al
        else:
            rng_i = range(1, 2 * n + 1) if cls in ("t", "a") else range(1, n + 1)
            for i in rng_i:
                v = al + be * (n + 1 - i)
                if v > 0: pads[f"{cls}{i}"] = v
    return pads


def run(sch, n, start_iota=True):
    txt = gens_red.friedmann_Gn(n, pads=scheme_pads(sch, n))
    with tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False) as f: f.write(txt); p = f.name
    st = [l for l in txt.splitlines() if l.startswith("% start")][0].split("start")[1].strip()
    try:
        r = subprocess.run([a.vjfast, "most-improved", p] + (["--start", "spec:" + st] if start_iota else []), capture_output=True, text=True, timeout=a.timeout)
        line = [l for l in r.stderr.splitlines() if l.startswith("solved with")][0]; it = int(line.split()[2])
    except Exception:
        it = -1
    os.unlink(p); return it


results = []
for k in (range(a.samples) if not a.climb else []):
    sch = {cls: (rng.choice(VALS), rng.choice(VALS)) for cls in CLASSES}
    it = run(sch, a.n0); results.append((it, sch))
    if k % 50 == 0: print(f"sample {k}: best so far {max(r[0] for r in results)}", flush=True)
results.sort(key=lambda x: -x[0])
if not a.climb: print(f"n0={a.n0}: top schemes")
for it, sch in results[:a.top]:
    grow = [run(sch, n) for n in (a.n0 + 1, a.n0 + 2, a.n0 + 3)]
    print(f"  iters n={a.n0}: {it}; n={a.n0+1},{a.n0+2},{a.n0+3}: {grow}; scheme {sch}", flush=True)


def hillclimb(start, steps, n0, rng):
    cur = dict(start); best = run(cur, n0); print(f"hillclimb start {best} {cur}", flush=True)
    for k in range(steps):
        cand = dict(cur); cls = rng.choice(CLASSES); al, be = cand[cls]
        if rng.random() < 0.5: al = rng.choice(VALS + [al * 2, max(0, al // 2), al + 1, max(0, al - 1)])
        else: be = rng.choice(VALS + [be * 2, max(0, be // 2), be + 1, max(0, be - 1)])
        cand[cls] = (al, be); it = run(cand, n0)
        if it >= best:
            if it > best: print(f"step {k}: {it} {cand}", flush=True)
            cur, best = cand, it
    return best, cur


if __name__ == "__main__" and "--climb" in sys.argv:
    C = 4 * a.n0 + 3
    start = {"d": (0, C), "g": (-1, C), "k": (C * a.n0 + C, 0), "s": (10 * C * a.n0, 0), "r": (10 * C * a.n0, 0), "c": (0, 0),
             "t": (0, 0), "a": (0, 0), "e": (0, 0), "f": (0, 0), "h": (0, 0)}
    best, sch = hillclimb(start, a.samples, a.n0, rng)
    print("final", best, sch); print("growth", [run(sch, n) for n in (a.n0 + 1, a.n0 + 2, a.n0 + 3)])
