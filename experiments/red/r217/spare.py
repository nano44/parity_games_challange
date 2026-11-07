#!/usr/bin/env python3
"""L-RED 54 R217: add S spare movers (2 options each, random targets) to a genome; levels alternate 0 / 1. Usage: spare.py G.json S seed OUT"""
import sys, json, random
G = json.load(open(sys.argv[1])); S, seed = int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); N = G["N"]
M = sum(len(o) for o in G["opts"]); l0 = [x for x in range(N) if G["lev"][x] == 0]
for i in range(S):
    lv = i % 2; x = N + i; G["lev"].append(lv); G["opts"].append([]); G["gate"].append([]); G["start"].append(0)
    for k in range(2):
        wt = rng.choice(l0) if lv else -1; xt = rng.randrange(N + S)
        G["opts"][x].append([wt, xt, M]); G["gate"][x].append(M); G["br"].append(M); G["bp"].append(rng.randrange(2)); M += 1
G["N"] = N + S; json.dump(G, open(sys.argv[4], "w"))
