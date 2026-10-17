#!/usr/bin/env python3
"""L-RED CARRY box (Opus 5.5): test of the support obstruction's case (iv) (R10). liftmod.py d out.pg
Skeleton: piece 0 = domfirst x0 (clock kap), slow cut C_A with seed sA -> x0. Module behind it: a chain of tops
Y_d > ... > Y_1, each Y_{i+1} forgiven through l_{i+1} -> v_i (v_i sits in Y_i's region, l_{i+1} has priority above Y_i's
cap); the bottom top Y_1 closes with q1 -> {Y_1, Y_2.., sA}. Prediction (lift cascade): the module stays alive in P1 for
about d+1 searches and then the cut eats it."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gadget import Game
d, out = int(sys.argv[1]), sys.argv[2]
G = Game(); L = 3 * d + 8
G.v("z", 1, 1, ["z"]); G.v("x0", 2, 0, ["qx0"]); G.v("qx0", 1, 0, [f"kap{L}"])
for i in range(1, L + 1): G.v(f"kap{i}", 2, 1, ["z" if i == 1 else f"kap{i-1}"])
pY = lambda i: 4 * i + 2                       # Y_i: 6, 10, 14, ..
tA = pY(d) + 3
G.v("sA", tA, 0, ["x0"])
G.v("Y1", pY(1), 0, ["q1"]); G.v("q1", 1, 1, ["Y1", "sA"] + [f"Y{j}" for j in range(2, d + 1)])
for i in range(1, d + 1):
    G.v(f"v{i}", 1, 0, [f"Y{i}"])
for i in range(2, d + 1):
    G.v(f"l{i}", pY(i - 1) + 1, 0, [f"v{i-1}"])          # odd priority above Y_{i-1}'s cap, below Y_i
    G.v(f"Y{i}", pY(i), 0, [f"l{i}"])
G.dump(out)
