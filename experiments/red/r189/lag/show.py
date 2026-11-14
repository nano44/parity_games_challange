#!/usr/bin/env python3
"""L-RED R189 SHOW: IDEAL trajectory of a genome (r187/ideal.traj): per step the movers that move, and the key order of each level pair."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "..", "r187"), os.path.join(H, "..", "..", "r178")]
import ideal
G = json.load(open(sys.argv[1])); S, why = ideal.traj(G); N = G["N"]; lev = G["lev"]
def keys(s):
    key = [None] * N
    for v in sorted(range(N), key=lambda v: lev[v]):
        wt = G["opts"][v][s[v]][0]; key[v] = ((G["gate"][v][s[v]],) if wt < 0 else key[wt] + (G["gate"][v][s[v]],))
    return key
mv = [0] * N
for j in range(1, len(S)):
    m = [v for v in range(N) if S[j][v] != S[j - 1][v]]
    for v in m: mv[v] += 1
    if "-q" not in sys.argv: print(f"step {j}: moves {m}  state {S[j]}")
print(f"L {len(S) - 1} {why} moves per mover {mv} per level {[sum(mv[v] for v in range(N) if lev[v] == l) for l in range(max(lev) + 1)]}")
