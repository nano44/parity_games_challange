#!/usr/bin/env python3
"""Write the pinned N9 instances: circ(n,1,2) for n = 3..10 and the peeling STUCK games r26, r90 (gaps.py/peeltest.py seeds)."""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
import pg, gen
from twoout import circ
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "instances")
for n in range(3, 11):
    pg.write(circ(n, 1, 2), os.path.join(d, f"circ12_n{n}.pg"))
for seed in (26, 90):
    rnd = random.Random(seed); n = rnd.randint(3, 12)
    pg.write(gen.random_game(n, rnd.randint(2, n + 1), 1, min(3, n), seed), os.path.join(d, f"peel_r{seed}.pg"))
for seed in (1147, 2136):  # peeltest.py random 1000 2000 3 14 (n range 3..14)
    rnd = random.Random(seed); n = rnd.randint(3, 14)
    pg.write(gen.random_game(n, rnd.randint(2, n + 1), 1, min(3, n), seed), os.path.join(d, f"peel_r{seed}.pg"))
