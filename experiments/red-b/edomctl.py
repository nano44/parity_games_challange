#!/usr/bin/env python3
"""CONTROL for (E-DOM3) (L-RED-B, B2): random genomes with the beta of 1-3 random options raised above every e-vertex
(eng3 test key "edomx"; not R104's game). Which counters of lev3 fire when E-DOM3 fails? Usage: edomctl.py SEED COUNT NMAX MMAX"""
import sys, random, eng3, gen, lev3, mut
seed, cnt, Nmax, Mmax = map(int, sys.argv[1:5]); rng = random.Random(seed)
tot = {k: 0 for k in lev3.CNT}; fired = {k: 0 for k in lev3.CNT}; n = 0; Tmax = 0
while n < cnt:
    G = gen.shaped(rng, rng.randint(1, Nmax), "mix"); G.pop("eorder", None)
    M = mut.M_of(G)
    if M > Mmax: continue
    G["edomx"] = rng.sample(range(M), min(M, rng.randint(1, 3)))
    g = eng3.build3(G); h = eng3.how3_run(g, tie=rng.choice(["keep-low", "high"]), cap=20000)
    c, d = lev3.check3(g, h, refs="all"); n += 1; Tmax = max(Tmax, d["T"])
    for k in lev3.CNT:
        tot[k] += c[k]; fired[k] += int(c[k] > 0)
print("EDOMCTL seed %d genomes %d Tmax %d | fired (genomes): %s | units: %s" % (seed, n, Tmax,
      " ".join("%s %d" % (k, fired[k]) for k in lev3.CNT if fired[k]), " ".join("%s %d" % (k, tot[k]) for k in lev3.CNT if tot[k])))
