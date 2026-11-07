#!/usr/bin/env python3
"""L-RED 53 R215 (2): per-instance totals for IDEAL-CYC (box191, env WT3): T, R, C, total gate-face flips of Odd's optimal
counterstrategy (si.Engine's choice), max flips at one gate, max switches of one mover. Usage: rflips.py G.json ..."""
import sys, os, json
sys.path.insert(0, os.path.join(os.environ["WT3"], "experiments/new/box191"))
import idealcyc, subrun191, gamma3
for f in sys.argv[1:]:
    G = json.load(open(f)); h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G); lab = subrun191.labels(G)
    _, _, _, V = gamma3.build(G, set()); Q = [(x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))]
    prev = None; fl = {q: 0 for q in Q}; mv = [0] * G["N"]
    for t, s in enumerate(st):
        cur = list(s0)
        for x in range(G["N"]): cur[movers[x]] = V[("g", (x, s[x]))]
        vs, sb = E.evaluate(tuple(cur)); face = {q: sb[V[("g", q)]] == V[("e", q)] for q in Q}
        if prev:
            for q in Q: fl[q] += face[q] != prev[1][q]
            for x in range(G["N"]): mv[x] += s[x] != prev[0][x]
        prev = (s, face)
    print(f"{os.path.basename(f)} d {max(G['lev']) + 1} N {G['N']} T {len(lab)} R {lab.count('R')} C {lab.count('C')} flips {sum(fl.values())} maxflip/gate {max(fl.values())} maxmoves/mover {max(mv)}", flush=True)
