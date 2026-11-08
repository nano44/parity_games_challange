#!/usr/bin/env python3
"""L-RED 60 R226: test the sharpening «#events <= |E_U| - 1» of LEAPFROG-ASC (units with PRIV + NODE) on random genomes,
with a correct max (leap225's rand aggregate starts max-keys at 0, which hides negative maxima). Freezes every genome with
maxexcess >= 0 to out/exwit_SEED_i.json. Usage: ex226.py SEED COUNT"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
import leap225, latch225
seed, cnt = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); hist = {}; wit = 0
for i in range(cnt):
    G = latch225.rgen(rng); c = leap225.census(G)
    if c["units_hyp"] == 0: continue
    e = c["maxexcess"]; hist[e] = hist.get(e, 0) + 1
    if e >= 0:
        wit += 1; json.dump(G, open(f"out/exwit_{seed}_{i}.json", "w")); print("WIT", i, c, flush=True)
    if i % 500 == 0: print("AT", i, sorted(hist.items()), flush=True)
print("RAND", seed, cnt, "hist(maxexcess per genome with hyp units)", sorted(hist.items()), "witnesses", wit, flush=True)
