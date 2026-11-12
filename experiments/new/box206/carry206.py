#!/usr/bin/env python3
"""Box 206 Addendum C (L-NEW successor 70): CARRY-wired variant of MWR(n) (box203/inst/MWR*_2.json with names): every high-bit mover
qh_k (k < n) gets a new level-0 W-target c_k (instead of the dead sink D) whose options have Xi-targets qh_j (j > k) and X, so that a play
can pass several high bits (qh_k -> e -> c_k -> beta-chain -> qh_j -> e -> ...). New beta ranks above all existing ones (parity PAR,
default 0 = even), new gate indices after all existing ones, start = the X option. Xi-feedback number stays 1 (no Xi-edge enters c_k).
Usage: carry206.py MWR.json OUT.json [PAR]"""
import sys, json, copy
src, out = sys.argv[1], sys.argv[2]; par = int(sys.argv[3]) if len(sys.argv) > 3 else 0
G = json.load(open(src)); nm = json.load(open(src.replace(".json", ".names.json"))); H = copy.deepcopy(G)
qh = sorted((int(k[2:]), v) for k, v in nm.items() if k.startswith("qh")); n = len(qh)
rk = max(H["br"]) + 1; gi = max(g for row in H["gate"] for g in row) + 1
for i, (k, x) in enumerate(qh[:-1]):
    c = H["N"]; H["N"] += 1; H["lev"].append(0); opts = []; gates = []
    for (k2, x2) in qh[i + 1:] + [(None, -1)]:
        b = len(H["br"]); H["br"].append(rk); H["bp"].append(par); rk += 1
        opts.append([-1, x2, b]); gates.append(gi); gi += 1
    H["opts"].append(opts); H["gate"].append(gates); H["start"].append(len(opts) - 1)
    H["opts"][x][0][0] = c
json.dump(H, open(out, "w")); print(out, "N", H["N"], "M", sum(len(o) for o in H["opts"]))
