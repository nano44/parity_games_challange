#!/usr/bin/env python3
"""L-RED 56 R221: post221.post on random Xi-cyclic genomes (brute221.rgen); prints a tally of (#fallbacks, post-fallback iterations,
post-fallback mover changes) and saves genomes with >= 2 fallbacks or > 1 post-fallback mover change. Usage: rpost221.py SEED COUNT"""
import sys, os, json, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../r221q"))
import post221
from brute221 import rgen
seed, cnt = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); tally = collections.Counter()
for i in range(cnt):
    d = rng.randint(1, 5); w = rng.randint(1, 3); G = rgen(rng, d, w, rng.choice([2, 3]))
    r = post221.post(G); post = sum(r["phases"][1:]) + r["fb"]
    tally[(r["fb"], post, r["Mpost"])] += 1
    if r["fb"] >= 2 or r["Mpost"] > 1:
        json.dump(G, open(f"out/post_{seed}_{i}.json", "w")); print("HIT", i, r, flush=True)
print(f"seed {seed} genomes {cnt} tally (fallbacks, post-fallback iterations, post-fallback mover changes): {sorted(tally.items())}", flush=True)
