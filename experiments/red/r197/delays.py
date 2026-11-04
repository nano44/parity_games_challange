#!/usr/bin/env python3
"""L-RED R197 DELAYS: for every DELAYED move (level l >= 1, no carry of level l-1 at t) of a width-2 ladder run, its offset
delta = t - (last carry step of level l-1 before t; 0 if none), histogram over genomes. Usage: delays.py genome.json ..."""
import sys, os, json, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal
hist = collections.Counter(); nodel = 0
for f in sys.argv[1:]:
    G = json.load(open(f)); S, _ = ideal.traj(G, cap=20000); N = G["N"]; O = G["opts"]; lev = G["lev"]; d = max(lev) + 1
    def keys(s):
        key = [None] * N
        for v in sorted(range(N), key=lambda v: lev[v]):
            wt = O[v][s[v]][0]; key[v] = ((G["gate"][v][s[v]],) if wt < 0 else key[wt] + (G["gate"][v][s[v]],))
        return key
    R = [[tuple(sorted((2 * l, 2 * l + 1), key=lambda v: k[v])) for l in range(d)] for k in (keys(s) for s in S)]
    for t in range(1, len(S)):
        for v in range(N):
            l = lev[v]
            if S[t][v] == S[t - 1][v] or l == 0 or R[t][l - 1] != R[t - 1][l - 1]: continue
            c = max([u for u in range(1, t) if R[u][l - 1] != R[u - 1][l - 1]] + [0]); hist[t - c] += 1
print("DELAYS offset histogram", dict(sorted(hist.items())))
