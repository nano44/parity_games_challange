#!/usr/bin/env python3
"""L-LOWER 4: export levels 1..d-1 of an L^R_d genome as a DRIVEN BLOCK (drv.c GEN format) and the c_1 sequence of its run.
Usage: blk.py genome.json out.gen  -> prints the e-sequence (c_1 at each step t >= 1, computed on s_t)."""
import sys, json, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l3'))
from sim import load, run
from trace import info
G = load(sys.argv[1]); N = G["N"]; d = N // 2
for v in range(N):
    for o in G["opts"][v]:
        assert o[1] not in (0, 1), "level-0 mover is a Xi-target: block export not exact"
S = run(G, G["start"])
mp = lambda y: -1 if y < 0 else y - 2
# topological order of block movers
xt = {v: [G["opts"][v][k][1] for k in range(2)] for v in range(2, N)}
order = []; seen = set()
def visit(v):
    if v in seen or v < 2: return
    seen.add(v)
    for y in xt[v]: visit(y)
    order.append(v)
for v in range(2, N): visit(v)
lines = [str(d - 1)]
for v in range(2, N):
    o = G["opts"][v]
    lines.append(" ".join(map(str, [mp(o[0][1]), mp(o[1][1]), G["br"][o[0][2]], G["br"][o[1][2]], G["bp"][o[0][2]], G["bp"][o[1][2]]])))
for l in range(1, d):
    lines.append(" ".join(str(int(G["gate"][2*l][j] > G["gate"][2*l+1][j])) for j in range(2)))
lines.append(" ".join(str(mp(v)) for v in order))
lines.append("".join(map(str, S[0][2:])))
open(sys.argv[2], "w").write("\n".join(lines) + "\n")
e = "".join(str(info(G, S[t])[1][1]) for t in range(1, len(S)))
print(e)
