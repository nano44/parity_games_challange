#!/usr/bin/env python3
"""Box 8 K10: masking load of gen(n) on CDAG_n. At each state of the chain, the number of Even vertices with a non-empty improving set
(si.py Engine.improving) other than the switched vertex = vertices N5's Even step must leave unmoved (each needs a local stall, K1).
Also: how often the designated switch is the arena optimum's choice when τ = σ̄ (one-player switch-best), i.e. no masking needed.
Usage: cdag_load.py n"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "si")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
from si import Engine
import pg
n = int(sys.argv[1])
sys.argv = [sys.argv[0], str(n)]
g = pg.Game([0] + [2 * (n + 1 - v) for v in range(1, n + 1)], [0] * (n + 1), [[0]] + [list(range(v)) for v in range(1, n + 1)]); E = Engine(g)
def gen(m):
    if m <= 1: return []
    out = [(m, m - 1)]
    for x, u in gen(m - 1): out += [(m, u), (m - 1, u), (m, m - 1)] if x == m - 1 else [(x, u)]
    return out
s = [0] * (n + 1); loads = []
for x, u in gen(n):
    val, _ = E.evaluate(tuple(s)); imp = E.improving(tuple(s), val); vs = {v for v, w in imp}
    loads.append(len(vs - {x})); s[x] = u
print(f"n={n} steps={len(loads)} masked vertices per step: min {min(loads)} mean {sum(loads)/len(loads):.2f} max {max(loads)}; steps with load 0: {loads.count(0)}")
