#!/usr/bin/env python3
"""Add k levels on top of a text genome (xt/br/bp/gate/start): new options Xi-target X, ranks above all old ones (new top
level highest), parities even, gates fresh, start 0. Usage: lift.py in.txt k out.txt"""
import sys
def rd(p):
    D = {}
    for ln in open(p):
        w = ln.split()
        if w and w[0] in ("xt", "br", "bp", "gate", "start"): D[w[0]] = list(map(int, w[1:]))
    return D
D = rd(sys.argv[1]); k = int(sys.argv[2]); M = len(D["xt"]); N = M // 2; d = N // 2
g0 = max(D["gate"]) + 1
for j in range(k):
    for p in range(2):
        for kk in range(2):
            D["xt"].append(-1); D["br"].append(M + 4 * j + 2 * p + kk); D["bp"].append(0); D["gate"].append(g0 + 4 * j + 2 * kk + p)
        D["start"].append(0)
with open(sys.argv[3], "w") as f:
    f.write("d %d\n" % (d + k))
    for key in ("xt", "br", "bp", "gate", "start"): f.write(key + " " + " ".join(map(str, D[key])) + "\n")
