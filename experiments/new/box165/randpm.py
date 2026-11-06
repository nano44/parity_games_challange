#!/usr/bin/env python3
"""random screen of CONJECTURE PM (moves(x) <= (deg-1)(1+desc(x))) over every start of random degree-2 genomes. Usage: randpm.py d w count seed [LR]"""
import os, sys, json, random, itertools
H = os.path.dirname(os.path.abspath(__file__)); exec(open(os.path.join(H, "kill1.py")).read().split("\nif __name__")[0])
d, w, cnt, seed = map(int, sys.argv[1:5]); lr = len(sys.argv) > 5; rng = random.Random(seed); runs = 0; kills = 0; maxT = 0
for i in range(cnt):
    G = gen(d, w, rng, lr); N = G["N"]
    for st in itertools.product((0, 1), repeat=N):
        r = measure(G, list(st)); runs += 1; maxT = max(maxT, r["T"])
        if any(r["mv"][x] > 1 + r["desc"][x] for x in range(N)):
            kills += 1; G["start"] = list(st); json.dump(G, open(os.path.join(H, "out", "KILL_PMrand_d%d_w%d.json" % (d, w)), "w"))
print("RANDPM d %d w %d genomes %d runs %d maxT %d kills %d" % (d, w, cnt, runs, maxT, kills))
