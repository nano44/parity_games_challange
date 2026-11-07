#!/usr/bin/env python3
"""L-SI box 79: replays of the DEAD items of packet P-IDEAL-DBL (§6); every printed number is asserted. Simulator box76/tw.py Sim;
XCHK=<l-new box150/check.py> also replays each run with L-NEW's Gen (identical states required)."""
import sys, os, json, copy
H = os.path.dirname(os.path.abspath(__file__)); B76 = os.path.join(H, "..", "box76"); sys.path.insert(0, B76)
from tw import Sim, analyse, is_lr
from climb77 import acyclic
Gen = None
if os.environ.get("XCHK"):
    ns = {"__file__": os.environ["XCHK"], "__name__": "lib"}; exec(open(os.environ["XCHK"]).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
def run(rel, start=None):
    G = json.load(open(os.path.join(B76, "inst", rel))); assert is_lr(G) and acyclic(G)
    s0 = tuple(int(c) for c in start) if start else tuple(G["start"]); sim = Sim(G); S = sim.run(s0)
    if Gen is not None:
        S2, _ = Gen(G).run(s0); assert [tuple(x) for x in S2] == S
    a = analyse(sim, S); T = a["T"]; N = G["N"]
    mv = [sum(1 for t in range(1, T + 1) if y in a["Mv"][t]) for y in range(N)]
    F = [sum(1 for t in range(1, T + 1) if a["flip"][t][j]) for j in range(N // 2)]
    return G, T, mv, F, a
# D1 MAXPLUS (SUM-COUPLE)
G, T, mv, F, a = run("dense_d5_l3_H10.json", "1100110110")
desc = set(); stack = [6]
while stack:
    x = stack.pop()
    for k in range(2):
        y = G["opts"][x][k][1]
        if y >= 0 and y not in desc: desc.add(y); stack.append(y)
assert T == 10 and mv[6] == 10 and max(mv[:6]) == 4 and max(mv[y] for y in desc) == 4 and 6 not in desc
assert [G["opts"][6][k][1] for k in range(2)] == [5, 4] and mv[4] == 4 and mv[5] == 4
print("D1 dense_d5_l3_H10 start 1100110110: T 10, moves(6) 10 (level 3), max moves over levels 0-2 = 4, over strict Xi-descendants = 4")
# D2 DBL-GAP
G, T, mv, F, a = run("lower/REC_d10_tower_mu30.json")
assert T == 35 and F[:4] == [2, 6, 14, 30] and all(F[l] == 2 * F[l - 1] + 2 for l in (1, 2, 3))
print("D2 REC_d10_tower_mu30 stored start: T 35, F(0..3) = 2 6 14 30, levels 1, 2, 3 doubling with F(0) = 2")
# D3 PASS-THROUGH DECAY
G, T, mv, F, a = run("passfreeze77_d5.json")
up4 = [(x, k) for x in (8, 9) for k in range(2) if G["opts"][x][k][1] >= 0 and G["lev"][G["opts"][x][k][1]] > 4]
assert T == 10 and F == [2, 2, 2, 6, 6] and mv[8] == mv[9] == 0 and up4 == [] and G["N"] == 10
print("D3 passfreeze77_d5 stored start: T 10, F = 2 2 2 6 6 (level 3 doubling), pair 4 never moves, no upward option, F(4) = F(3)")
# D4 RE-ENTRY (static)
G = json.load(open(os.path.join(B76, "inst", "lower", "REC_d10_tower_mu30.json")))
assert G["lev"][11] == 5 and G["lev"][3] == 1 and 3 in [G["opts"][11][k][1] for k in range(2)]
assert any(G["opts"][x][k][1] == 11 and G["lev"][x] <= 1 for x in range(G["N"]) for k in range(2))
G = json.load(open(os.path.join(B76, "inst", "lower", "KILL_M2D_d6_mu13.json")))
assert G["lev"][5] == 2 and 3 in [G["opts"][5][k][1] for k in range(2)]
assert any(G["opts"][x][k][1] == 5 and G["lev"][x] <= 1 for x in range(G["N"]) for k in range(2))
print("D4 REC_d10_tower_mu30: fuel target 11 (level 5, upward target of a level <= 1 mover) has an option with Xi-target 3 (level 1);"
      " KILL_M2D_d6_mu13: fuel target 5 (level 2) -> 3 (level 1)")
print("dead79: all assertions PASS" + (" (Gen cross-check on)" if Gen else ""))
