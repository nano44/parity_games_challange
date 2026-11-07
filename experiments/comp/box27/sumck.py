#!/usr/bin/env python3
"""Replay a FREE0 genome (cnf.py decode JSON or any genome with level-0 movers 0, 1): V_k(G) = max over all starts of the longest
forced run with <= k b_0 flips (free0.py's DP, sim.py's rules). Usage: sumck.py f.json [kmax]"""
import sys, json
import free0
for f in sys.argv[1:2]:
    G = json.load(open(f)); kmax = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    Lr = free0.longest(G, kmax); N = G["N"]
    V = [max(Lr(tuple((s >> x) & 1 for x in range(N)), k) for s in range(1 << N)) for k in range(kmax + 1)]
    print(f, "V_k for k = 0..%d:" % kmax, V, "V0+V1 =", V[0] + V[1])
