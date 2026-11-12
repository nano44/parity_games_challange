#!/usr/bin/env python3
"""L-RED 65 R231 item (b) design 1: GATED RE-ARM for CW(n) (adversary vs CONJECTURE DEEP-k1, box 206). Built from CW(n) (carry231.py):
a new level-0 exit mover z0 (one option: W -1, Xi X) and level-1 mover(s) y with one option (W-target z0, Xi-target R); every carry
chooser c_k gets one more option (before X) with Xi-target y. At y's gate Odd may leave the race (e-face: e_y -> z0 -> X) or follow it
(beta-face -> R). MODE 1: one shared y; MODE 2: one y_k per c_k. MODE 3 / 4: as 1 / 2 with y's W-target hv (DYNAMIC exit; y = a copy of Q). No new Xi-cycle (c_k is entered only by W-edges): k stays 1.
Usage: gate231.py CW.json NAMES.json OUT.json MODE"""
import sys, json
G = json.load(open(sys.argv[1])); nm = json.load(open(sys.argv[2])); mode = int(sys.argv[4]); R = nm["R"]
qh = sorted((int(k[2:]), v) for k, v in nm.items() if k.startswith("qh") and k[2:].isdigit())
cks = [G["opts"][x][0][0] for _, x in qh[:-1]]
nbr = max(G["br"]) + 1; ngate = max(g for row in G["gate"] for g in row) + 1
def mover(lev, opts):
    global nbr, ngate
    x = G["N"]; G["N"] += 1; G["lev"].append(lev); G["opts"].append([]); G["gate"].append([]); G["start"].append(0)
    for wt, xt in opts:
        G["opts"][x].append([wt, xt, len(G["br"])]); G["br"].append(nbr); nbr += 1; G["bp"].append(0); G["gate"][x].append(ngate); ngate += 1
    return x
z0 = mover(0, [(-1, -1)])
ex = z0 if mode in (1, 2) else nm["hv"]                 # MODE 3 / 4: dynamic exit, y's W-target = hv (y = a copy of the race's Q)
ys = [mover(1, [(ex, R)])] * len(cks) if mode in (1, 3) else [mover(1, [(ex, R)]) for _ in cks]
for c, y in zip(cks, ys):
    G["opts"][c].insert(len(G["opts"][c]) - 1, [-1, y, len(G["br"])]); G["br"].append(nbr); nbr += 1; G["bp"].append(0)
    G["gate"][c].insert(len(G["gate"][c]) - 1, ngate); ngate += 1; G["start"][c] = len(G["opts"][c]) - 1
json.dump(G, open(sys.argv[3], "w"))
