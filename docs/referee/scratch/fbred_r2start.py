#!/usr/bin/env python3
"""REFEREE succ. 12: replay REFEREE-2's start-pair RNG (fbred_check.py 'files', random.Random(5151), runs=3, r = 1, 2 random) over
experiments/new/box41/lib41.txt with succ lists from experiments/harness/pg.read (the reader R2's
code uses; only to reproduce the start pair; 46 of 412 lib41 files order succ differently from my parser), then run MY probe (fbred_probe.run_check) on TARGET at its start #R. Read-only use of
R2's published seed convention; no R2 code imported. Usage: fbred_r2start.py TARGET_RELPATH R"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, fbred_probe as F
sys.path.insert(0, os.path.join(P.ROOT, "experiments/harness")); import pg
target, R = sys.argv[1], int(sys.argv[2])
rng = random.Random(5151)
for path in [l.strip() for l in open(os.path.join(P.ROOT, "experiments/new/box41/lib41.txt")) if l.strip()]:
    g = RE.parse(os.path.join(P.ROOT, path))
    succ = [list(x) for x in pg.read(os.path.join(P.ROOT, path)).succ]
    for r in range(1, 3):
        s = [rng.choice(succ[v]) for v in range(g.n)]; t = [rng.choice(succ[v]) for v in range(g.n)]
        if path == target and r == R:
            st = ([s[v] if g.owner[v] == 0 else None for v in range(g.n)], [t[v] if g.owner[v] == 1 else None for v in range(g.n)])
            c = Counter(); F.run_check(g, st, c, path + "#%d" % r)
            print(path, "#%d" % r, " ".join("%s=%d" % kv for kv in sorted(c.items()) if kv[0].startswith("max") or kv[0].endswith("FAIL") or kv[0] == "phases"))
            sys.exit(0)
