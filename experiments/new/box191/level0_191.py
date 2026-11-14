#!/usr/bin/env python3
"""Box 191 / P-N5-XICYC fixes entry 1: LEVEL0 data. Along IDEAL-CYC runs of random genomes (rand191.rgen), count (state, level-0 gate)
pairs where sigma-bar takes the e-face (the successor of larger priority). Usage: level0_191.py COUNT SEED"""
import sys, random
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import idealcyc, rand191
cnt, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); states = viol = gates0 = 0
for i in range(cnt):
    G = rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3))
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); gi = {}
    for x in range(G["N"]):
        for v in h.succ[movers[x]]: gi[(x, inv[v])] = v
    lv0 = [gi[(x, k)] for x in range(G["N"]) if G["lev"][x] == 0 for k in range(len(G["opts"][x]))]
    for s in idealcyc.run(G):
        cur = list(s0)
        for x in range(G["N"]): cur[movers[x]] = gi[(x, s[x])]
        vs, sb = E.evaluate(tuple(cur)); states += 1; gates0 += len(lv0)
        # beta-face of gate g = the successor that is a beta vertex: e-face successor has even priority > all betas; identify e-face as succ with larger priority
        for g in lv0:
            e = max(h.succ[g], key=lambda w: h.prio[w])
            viol += sb[g] == e
print(f"LEVEL0 count {cnt} seed {seed}: states {states}, (state, level-0 gate) pairs {gates0}, sigma-bar on the e-face {viol}")
