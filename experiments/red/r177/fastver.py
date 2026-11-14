#!/usr/bin/env python3
"""L-RED R177: fastabs <-> abs177 (si.py engine) equivalence on random genomes and on given champion files.
Usage: fastver.py trials seed [champion.json ...]"""
import sys, os, random, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fastabs as F, abs177 as A
def conv(G):
    N = G["N"]; deg = G["deg"]
    levels = [l + 1 for l in G["lev"]]
    opts = [[["W" if o[0] < 0 else o[0], "X" if o[1] < 0 else o[1]] for o in G["opts"][v]] for v in range(N)]
    perm = list(range(N)) + [N + G["gate"][v][k] for v in range(N) for k in range(deg)]
    return dict(levels=levels, opts=opts, perm=perm, brank=G["br"], bpar=G["bp"], start=G["start"], bper=True)
T, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); bad = 0; tot = 0
Gs = [F.randG(rng.randint(2, 4), rng.randint(2, 3), rng, rng.choice([1, 2, 3])) for _ in range(T)] + [json.load(open(p)) for p in sys.argv[3:]]
for G in Gs:
    a = F.simulate(G); b = A.simulate(conv(G)); tot += 1
    if a[0] != b[0] or a[1] != b[2]: bad += 1; print("MISMATCH", a, b[:3])
print("FASTVER", tot, "genomes, mismatches", bad)
