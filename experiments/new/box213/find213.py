#!/usr/bin/env python3
"""Box 213: regenerate key213.py --rand SEED COUNT MODE's genomes in order and save the first one with undef > 0 (a window step with
Y != V where some Odd vertex of Y leaves Y under tau) as inst/<NAME>.json; prints its key213 line. Usage: find213.py SEED COUNT MODE NAME"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import key213, eg195
seed, cnt, mode, name = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]; rng = random.Random(seed); k = 0
while k < cnt:
    G = eg195.gen(rng, mode)
    if G is None or G["N"] < 2: continue
    k += 1; c = key213.one(G)
    if c["undef"] > 0:
        os.makedirs(os.path.join(HERE, "inst"), exist_ok=True); json.dump(G, open(os.path.join(HERE, "inst", name + ".json"), "w"), sort_keys=True)
        print(name, "genome", k, "of seed", seed, mode, key213.fmt(c)); break
