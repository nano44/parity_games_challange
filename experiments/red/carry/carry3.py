#!/usr/bin/env python3
"""Two-level counter attempt with a DEFICIT gate (L-RED CARRY box, produced on Opus 5.5). carry3.py mA mB out.pg
Layout per search (R10 (F)): piece 0 domfirst x0 | C_A (seed sA) | P1 stable (slow frontier learns iff the stealer sig is
pruned) | C_B (seed sB) | P2 stable (fast chain step). Gate module = L-ALG's synthetic deficit shape (GAP-A-M.md section 4)
with t = {m->k, k->o, o} (escape tau2) and the straddler = the complete fast chain pulled into tau's pruning region, which
then takes k (k -> b_mB). sig -> x needs x lifted by t into tau2's region; under the straddle x is lost and sig is pruned."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gadget import Game
mA, mB, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
L = mA + mB + 12                                    # clock length for x0
pa = lambda j: 4 + 2 * j
psig = pa(mA) + 2; px = psig + 1
pb = lambda i: px + 1 + 2 * i
ptau2 = pb(mB) + 2; tB = ptau2 + 1; ptau = ptau2 + 2
ph = lambda j: ptau + 1 + 2 * j
tA = ph(mA) + 2
G = Game()
G.v("z", 1, 1, ["z"])
G.v("x0", 2, 0, ["qx0"]); G.v("qx0", 1, 0, [f"kap{L}"])
for i in range(1, L + 1):
    G.v(f"kap{i}", 2, 1, ["z" if i == 1 else f"kap{i-1}"])
G.v("sA", tA, 0, ["x0"])
G.v("sB", tB, 0, ["tau", "m"])
G.v("zeta", 2, 0, ["z"])
G.v("tau", ptau, 0, ["q"]); G.v("q", 1, 1, ["tau", "zeta"])
G.v("tau2", ptau2, 0, ["q2"]); G.v("q2", 1, 1, ["tau2", "sA", "m"])
G.v("m", 4, 0, ["k"]); G.v("k", 2, 0, ["o", f"b{mB}"]); G.v("o", 1, 1, ["m", "tau2"])
G.v("x", px, 0, ["o"]); G.v("sig", psig, 0, ["x"])
for j in range(1, mA + 1):
    G.v(f"a{j}", pa(j), 0, [f"p1_{j}"])
    G.v(f"p1_{j}", 1, 0, [f"p2_{j}", "sig"])
    G.v(f"p2_{j}", 1, 1, [f"a{j}", "sA" if j == 1 else f"a{j-1}"])
    G.v(f"h{j}", ph(j), 0, [f"a{j}"])
for i in range(1, mB + 1):
    G.v(f"b{i}", pb(i), 1, [])
    G.v(f"w{i}_0", 1, 0, [f"b{i}"]); G.e(f"b{i}", f"w{i}_0")
    for j in range(1, mA + 1):
        G.v(f"w{i}_{j}", 1, 0, [f"b{i}", f"h{j}"]); G.e(f"b{i}", f"w{i}_{j}")
    G.e(f"b{i}", "sB" if i == 1 else f"b{i-1}")
G.dump(out)
