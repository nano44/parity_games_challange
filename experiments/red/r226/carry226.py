#!/usr/bin/env python3
"""L-RED 60 R226: CARRY CHAIN on CX4_n21 (DS-TOPS test). CX4's carry is x8 (level 1; e8 -> x20, beta -> x18), reached from x7's option 1.
Add K clones x8_1..x8_K of x8 (same targets), their e's ranked above e8 in increasing order (gate ranks at the top), and give the carrier
(x7 by default) one extra option with Xi-target x8_j for each j.  Variants: carrier, beta ranks of the new options (top/bottom), clone
beta-target. Prints T, maxD, Hn17 and maxalt per K. Usage: carry226.py CX4.json KMAX"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
from compose226 import *
from altclimb226 import score as altscore
import own
def hn(G, x=17):
    out, V, O, ow = own.run(G, 3000); best = 0; t = 0
    while t < len(out):
        u = t
        while u + 1 < len(out) and out[u + 1][1][x][0] == out[t][1][x][0]: u += 1
        best = max(best, len({out[i][1][x][1] for i in range(t, u + 1)})); t = u + 1
    return best
def build(A, K, carrier=7, bpos="top", cbt=18, cbp=0):
    G = copy.deepcopy(A); N0 = G["N"]
    for j in range(K):
        x = G["N"]; G["N"] += 1; G["lev"].append(1); G["opts"].append([]); G["gate"].append([]); G["start"].append(0)
        M = len(G["br"]); G = add_opt(G, x, 20, cbt, M, (M if bpos == "top" else 0), cbp)
        M = len(G["br"]); G = add_opt(G, carrier, -1, x, j, (M if bpos == "top" else 0), 1)
    return G
if __name__ == "__main__":
    A = json.load(open(sys.argv[1])); KM = int(sys.argv[2])
    for carrier in (7, 9, 2):
        for bpos in ("top", "bot"):
            for cbt in (18, 17, 10):
                row = []
                for K in range(0, KM + 1):
                    G = build(A, K, carrier, bpos, cbt)
                    try: m = measure(G)
                    except AssertionError as e: row.append("bad"); continue
                    row.append("K%d:T%d/D%d/H%d/a%d" % (K, m["T"], m["maxD"], hn(G), altscore(G)[0]))
                print("carrier x%d beta %s clone-beta x%d:" % (carrier, bpos, cbt), " ".join(row), flush=True)
