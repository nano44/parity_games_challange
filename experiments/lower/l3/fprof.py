#!/usr/bin/env python3
"""F-profile of a run on L^R_d: F(l) = flips of the key order of pair (2l, 2l+1); moves per level; T. Usage: fprof.py g.json ..."""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sim import run, moves
from trace import info
for p in sys.argv[1:]:
    G = json.load(open(p)); S = run(G, G["start"]); d = G["N"] // 2; O = [info(G, s)[0] for s in S]
    F = [sum(1 for t in range(1, len(S)) if O[t][l] != O[t - 1][l]) for l in range(d)]
    m = moves(S, G["N"]); Z = {o[1] for x in range(G["N"]) for o in G["opts"][x]} - {-1}
    print(os.path.basename(p), "d", d, "T", len(S) - 1, "F", F, "moves", m, "muZ", max(m[z] for z in Z if G["lev"][z] >= 1))
