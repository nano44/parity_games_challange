#!/usr/bin/env python3
"""L-COMP box 30: independent replay of an rclimb text genome (option m = 2x+k, beta id m) with MY simulator box27/sim.py (R104 rules,
written from R104's text; not rclimb's code): T and stop reason, and F(l) = the number of steps t = 1..T at which the order of the
R104 keys of the two movers 2l, 2l+1 under s_t differs from that under s_(t-1) (key(x) = key of the W-target of x's current option,
followed by that option's gate; level 0: the gate). Writes the genome as box150/box27 JSON if a second path is given.
Usage: replay30.py genome.txt [out.json]"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box27")); import sim
D = {}
for ln in open(sys.argv[1]):
    w = ln.split()
    if w and w[0] in ("d", "xt", "br", "bp", "gate", "start"): D[w[0]] = list(map(int, w[1:]))
d = D["d"][0]; N = 2 * d
G = {"N": N, "lev": [x // 2 for x in range(N)], "deg": 2,
     "opts": [[[(-1 if x < 2 else 2 * (x // 2 - 1) + k), D["xt"][2 * x + k], 2 * x + k] for k in range(2)] for x in range(N)],
     "gate": [[D["gate"][2 * x + k] for k in range(2)] for x in range(N)], "br": D["br"], "bp": D["bp"], "start": D["start"]}
S, why = sim.run(G); T = len(S) - 1
def keys(s):
    K = [None] * N
    for x in range(N):
        w = G["opts"][x][s[x]][0]; K[x] = (K[w] if w >= 0 else ()) + (G["gate"][x][s[x]],)
    return K
o = [[keys(s)[2 * l] > keys(s)[2 * l + 1] for l in range(d)] for s in S]
F = [sum(1 for t in range(1, T + 1) if o[t][l] != o[t - 1][l]) for l in range(d)]
if len(sys.argv) > 2: json.dump(G, open(sys.argv[2], "w"))
print(f"{os.path.basename(sys.argv[1])}: replay (box27/sim.py) d {d} T {T} stop {why} F {' '.join(map(str, F))}")
