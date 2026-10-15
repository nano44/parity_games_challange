#!/usr/bin/env python3
"""Test of conjecture T-ALG1 (notes/L-ALG.md): NE'(k) (C2) solves completely every game of Strahler number <= k + 1.
Random walk inside the psolC-failure region (walk.mutate; n <= NMAX so the Strahler DP is affordable); for each accepted
game: Strahler number s (experiments/attr/strahler.py, DJT 2003.08627 section 2), and whether NE'(s-1) solves it
(conjecture: always) and whether NE'(s-2) solves it (not implied). Counterexamples to the conjecture are written to
out/strtest_cex_<tag>.jsonl. Usage: strtest.py STEPS SEED [--nmax 9] [--tag T]"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "attr"))
import alglib, pg, zielonka, ne, walk
from strahler import strahler


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    steps, seed = int(args[0]), int(args[1])
    opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
    nmax = int(opt("--nmax", 9)); tag = opt("--tag", f"s{seed}")
    ne.MODE = "h"
    rnd = random.Random(seed)
    seeds = [alglib.from_record(json.loads(l)) for l in open(os.path.join(HERE, "out", "psolc_fail_n4.jsonl"))]
    g = rnd.choice(seeds)
    stat, seen, t0 = {}, set(), time.time()
    out = open(os.path.join(HERE, "out", f"strtest_cex_{tag}.jsonl"), "a")
    for step in range(steps):
        if rnd.random() < 0.02:
            g = rnd.choice(seeds)
        h = walk.mutate(g, rnd, nmax)
        if walk.undec(h, 0) == 0:
            continue
        g = h
        key = pg.dumps(g)
        if key in seen:
            continue
        seen.add(key)
        ref = zielonka.solve(g)
        s, _ = strahler(g, win=ref)
        ok1 = walk.undec(g, s - 1) == 0
        ok2 = (s >= 2) and walk.undec(g, s - 2) == 0
        k = stat.setdefault(s, [0, 0, 0]); k[0] += 1; k[1] += ok1; k[2] += ok2
        if not ok1:
            rec = alglib.game_record(g, ref, strahler=s)
            out.write(json.dumps(rec) + "\n"); out.flush()
            print(f"COUNTEREXAMPLE: Strahler {s}, NE'({s-1}) incomplete: {key.strip()}", flush=True)
        if step % 5000 == 0:
            print(f"  step {step}, {time.time()-t0:.0f}s: " + "; ".join(f"Str {s}: {c[0]} games, NE'(s-1) solves {c[1]}, NE'(s-2) solves {c[2]}" for s, c in sorted(stat.items())), flush=True)
    print("done: " + "; ".join(f"Str {s}: {c[0]} games, NE'(s-1) solves {c[1]}, NE'(s-2) solves {c[2]}" for s, c in sorted(stat.items())))


if __name__ == "__main__":
    main()
