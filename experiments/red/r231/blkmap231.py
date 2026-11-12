#!/usr/bin/env python3
"""L-RED 65 R231 item 0: bit map of the top block (own engine) and the high/low split of a mover's block sequence.
Usage: blkmap231.py G.json mover [lowbits]"""
import sys, json
from blk231 import analyse, dedup
G = json.load(open(sys.argv[1])); A = analyse(G); x0 = int(sys.argv[2]); lowb = int(sys.argv[3]) if len(sys.argv) > 3 else 2
V, O, pos, p0 = A["V"], A["O"], A["pos"], A["p0"]
top_lev = max(G["lev"])
for q in sorted(O, key=lambda q: pos[V[("e", q)]]):
    if G["lev"][q[0]] == top_lev:
        wt, xt, br = G["opts"][q[0]][q[1]]
        print(f"bit {pos[V[('e', q)]] - p0}: e-pos {pos[V[('e', q)]]} option (mover {q[0]}, j {q[1]}) W-target {wt} Xi-target {xt} lev(x) {G['lev'][q[0]]}")
seq = dedup(A["blk"][x0]); hi = [s >> lowb for s in seq]
print("high parts (dedup over states):", dedup(hi)); print("popcount of high parts:", [bin(h).count("1") for h in dedup(hi)])
print("level-1 movers:", [x for x in range(G["N"]) if G["lev"][x] == top_lev])
