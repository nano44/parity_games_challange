#!/usr/bin/env python3
"""L-RED R212 LIFT (inverse of FROZEN-EMBED): a genome L of L^R_m (R197 convention, JSON) -> an ISO genome G of L^R_(m+1) (fk text)
with Lad_1(G) = L up to relabelling the options of a level-0 mover of L, so T_0(G) >= T(L). Needs: the two smallest level-0 gates
of L belong to different movers (otherwise exit 2). Level 0 of G: gates 0,3 / 1,2 (both bits realisable); new ranks of the four
level-0 options of G are placed below every old rank. Usage: lift.py L.json out.txt"""
import sys, json
L = json.load(open(sys.argv[1])); n = L["N"]; lev = L["lev"]; m = max(lev) + 1
assert n == 2 * m and all(lev[v] == v // 2 for v in range(n)), "not 2-wide"
for v in range(n):
    assert len(L["opts"][v]) == 2
    for k in range(2): assert L["opts"][v][k][0] == (2 * (lev[v] - 1) + k if lev[v] else -1), "not R197 convention"
g4 = sorted((L["gate"][x][k], x, k) for x in (0, 1) for k in (0, 1))
if g4[0][1] == g4[1][1]: print("NOT LIFTABLE: the two smallest level-0 gates are on one mover"); sys.exit(2)
# relabel options of level-0 movers so that the low class is option 0 of both (c = 1: kappa = 0 for option 0)
flip = {x: (1 if (g4[0][1] == x and g4[0][2] == 1) or (g4[1][1] == x and g4[1][2] == 1) else 0) for x in (0, 1)}
opts = [list(map(list, o)) for o in L["opts"]]; gate = [list(g) for g in L["gate"]]; start = list(L["start"])
for x in (0, 1):
    if flip[x]: opts[x] = opts[x][::-1]; gate[x] = gate[x][::-1]; start[x] = 1 - start[x]
N = n + 2; M = 2 * N
xt = [-1] * (2 * N); br = [0] * M; bp = [0] * M; gt = [0] * M
# beta records: L's option record o[2] indexes br/bp; build G's option ids 2x+k
oldbr = sorted(range(len(L["br"])), key=lambda i: L["br"][i])
for x in range(n):
    for k in range(2):
        o = opts[x][k]; X = x + 2
        xt[2 * X + k] = o[1] + 2 if o[1] >= 0 else -1
        br[2 * X + k] = 4 + L["br"][o[2]]; bp[2 * X + k] = L["bp"][o[2]]
# compress ranks to 0..M-1 keeping order
for i, k in enumerate((0, 1, 2, 3)): br[k] = i
order = sorted(range(M), key=lambda i: br[i]); 
for r, i in enumerate(order): br[i] = r
# gates: level 0 of G: 0,3 / 1,2 ; old gates shifted by 4, order kept (level-1 gates already encode the class order: low class = option 0)
gt[0], gt[1], gt[2], gt[3] = 0, 3, 1, 2
for x in range(n):
    for k in range(2): gt[2 * (x + 2) + k] = 4 + gate[x][k]
order = sorted(range(M), key=lambda i: gt[i])
for r, i in enumerate(order): gt[i] = r
open(sys.argv[2], "w").write("m %d\nxt %s\nbr %s\nbp %s\ngate %s\n" % (m, " ".join(map(str, xt)), " ".join(map(str, br)), " ".join(map(str, bp)), " ".join(map(str, gt))))
print("lifted m", m, "flip", flip, "start (levels >= 1)", "".join(map(str, start)))
