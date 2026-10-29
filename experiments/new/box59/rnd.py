#!/usr/bin/env python3
"""L-NEW box 59: random parity games (seeded), PGSolver format. Usage: rnd.py SEED N DEG > out.pg  (priorities 0..N-1 random, owners
fair coin, out-degree 1..DEG distinct successors, no self-loop requirement)."""
import sys, random
seed, n, deg = map(int, sys.argv[1:4]); r = random.Random(seed)
print(f"parity {n - 1};")
for v in range(n):
    k = r.randint(1, deg); s = r.sample(range(n), k)
    print(f"{v} {r.randrange(n)} {r.randrange(2)} {','.join(map(str, s))};")
