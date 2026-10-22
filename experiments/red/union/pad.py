#!/usr/bin/env python3
"""L-RED (2026-10-16, produced on Opus 5.5): pad a PGSolver game with K source-only vertices (no incoming edges; random
priority <= max priority, random owner, 1-3 edges into the old game), as L-ALG did for its (H4) scaling (GAP-A-M 13b).
Usage: pad.py G.pg K SEED > out.pg"""
import sys, random
lines = [l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith(("parity", "start"))]
K, rng = int(sys.argv[2]), random.Random(int(sys.argv[3]))
vs = [l.rstrip(";").split()[:4] for l in lines]
n = len(vs); mp = max(int(v[1]) for v in vs)
print(f"parity {n + K - 1};")
for v in vs: print(f"{v[0]} {v[1]} {v[2]} {v[3]};")
for k in range(K):
    print(f"{n + k} {rng.randint(0, mp)} {rng.randint(0, 1)} {','.join(str(x) for x in sorted(rng.sample(range(n), rng.randint(1, 3))))};")
