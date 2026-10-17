#!/usr/bin/env python3
"""Two-level reset+replay attempt for DTL (L-RED CARRY box, produced on Opus 5.5). carry2.py mA mB out.pg
Level B (fast): chain b_1..b_mB eaten one per search by the B-cut (seed sB); tangle T_{i,c} = {b_i} + witnesses g_{i,j}
present at A-state c. Level A (slow): chain a_1..a_mA eaten one per A-step by the earlier A-cut (seed sA); eating a_j also
eats the witnesses g_{.,j}, killing every B-tangle of earlier states (f1). Carry gate: p1_k (Even) is stolen by the high top
sigma while sigma is alive in the stable piece; sigma lives while b_mB is in R (sigma -> qs -> b_mB). No gate escape."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gadget import Game
mA, mB, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
G = Game()
pa = lambda k: 2 + 2 * k                 # a_k: 4, 6, ..
tA = pa(mA) + 1                          # A-cut seed priority
pb = lambda i: tA + 1 + 2 * i            # b_i above tA
tB = pb(mB) + 1
psig = tB + 1
G.v("x", 2, 0, ["qx"])                   # piece-0 argmax, Dom(x) = {x}
G.v("qx", 1, 0, [f"a{mA}"])              # x survives while a_mA does
G.v("sA", tA, 0, ["x"])
G.v("sB", tB, 0, ["x"])
G.v("sig", psig, 0, ["qs"])              # stealer
G.v("qs", 1, 0, [f"b{mB}"])
for k in range(1, mA + 1):
    G.v(f"a{k}", pa(k), 1, [f"p1_{k}"])
    G.v(f"p1_{k}", 1, 0, [f"p2_{k}", "sig"])
    G.v(f"p2_{k}", 1, 1, [f"a{k}", "sA" if k == 1 else f"a{k-1}"])
for i in range(1, mB + 1):
    G.v(f"b{i}", pb(i), 1, [])
    G.v(f"g{i}_0", 1, 0, [f"b{i}"]); G.e(f"b{i}", f"g{i}_0")
    for j in range(1, mA + 1):
        G.v(f"g{i}_{j}", 1, 0, [f"b{i}", f"a{j}"]); G.e(f"b{i}", f"g{i}_{j}")
    G.e(f"b{i}", "sB" if i == 1 else f"b{i-1}")
idx = G.dump(out)
print(" ".join(f"{k}={v}" for k, v in idx.items()), file=sys.stderr)
