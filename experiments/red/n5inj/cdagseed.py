"""L-RED box 26/27 (produced on Opus 5.5): seed games for thetaclimb.py --from: L-NEW's CDAG_k (docs/new/N5-K9-Pstrict-counter.md:
vertex 0' sink (priority 0, self-loop), vertex v = 1..k priority 2(k+1-v), edges to every u < v; all Even) with ONE Odd choice
vertex o placed on top (C^1O): o (Odd, priority OP) has exits to the CDAG vertices in EXITS, and every CDAG vertex v >= 2 gets an
extra edge to o (so o lies on cycles; R58 §9 Corollary X1 says a C^1O kill needs that). Vertex ids: o = 0, sink = 1, CDAG v = v + 1.
Usage: cdagseed.py k OP EXITS(comma list of CDAG vertices) > game.pg"""
import sys
k, op = int(sys.argv[1]), int(sys.argv[2]); exits = [int(x) for x in sys.argv[3].split(",")]
n = k + 2
prio = [op, 0] + [2 * (k + 1 - v) for v in range(1, k + 1)]
owner = [1, 0] + [0] * k
succ = [sorted(e + 1 for e in exits), [1]] + [sorted([1] + [u + 1 for u in range(1, v)] + ([0] if v >= 2 else [])) for v in range(1, k + 1)]
print(f"parity {n - 1};")
for v in range(n): print(f"{v} {prio[v]} {owner[v]} {','.join(map(str, succ[v]))};")
