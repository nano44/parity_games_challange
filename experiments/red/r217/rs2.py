#!/usr/bin/env python3
"""L-RED 54 R217: SET -> RESET -> re-SET under E-DOM (d 2), no odd penalty, no tap e's.
- B1's delay: an e-free deceleration lane (Friedmann style): helpers a_j (even beta p_j, increasing) -> lane movers b_j; b_j: EXIT
  (-> s) or CHAIN (-> b_(j-1); b_0 -> bonus helper d with the top even beta). Chaining runs b_0, b_1, ... one per step; B1 follows the
  newest chained a_j, then SETS (escape e1 -> s).
- B0: SET0 (escape e0 -> W0 = f_0, the start of lane F0) or ACC1 (access mover A1: copy gate of B1, escape e1' -> s).
- F0: movers f_0..f_(M-1): EXIT (-> TOPX: a forced-escape bit with e_x, then s) or CHAIN (-> f_(i+1); f_(M-1) -> B1), odd chain betas.
  Before B1 sets, F0's chain carries no e (B1's route is e-free), EXIT carries e_x: no discovery. After B1 sets, CHAIN carries e1 > e_x:
  discovery wave from f_(M-1) back to f_0; when it reaches f_0, SET0 = e0 + e1-route beats ACC1 = e1' -> B0 re-SETS.
- e order: e_x < e0 < e1' < e1. Prediction: B0 SET (step 1), RESET one step after B1 sets, re-SET about M steps later.
Usage: rs2.py L M OUT.json"""
import sys, json
from gdsl import Gen
def build(L, M):
    g = Gen(); s = g.mv("s", 0); D = g.mv("DUMMY", 0); d = g.mv("d", 0)
    a = [g.mv(f"a{j}", 0) for j in range(L)]; b = [g.mv(f"b{j}", 0) for j in range(L)]
    f = [g.mv(f"f{i}", 0) for i in range(M)]; X = g.mv("TOPX", 1)
    B1 = g.mv("B1", 1); B0 = g.mv("B0", 1); A1 = g.mv("A1", 1)
    g.opt(s, None, None, (0, "sink"), 1); g.opt(D, None, D, (99, "dummy"), 0)
    g.opt(d, None, None, (50, "bonus"), 0)                                   # bonus: top even beta below the dummy
    for j in range(L):
        g.opt(a[j], None, b[j], (30, j), 0)                                  # lane priorities p_j, even, increasing
        g.opt(b[j], None, None, (1, "bexit", j), 1)
        g.opt(b[j], None, b[j - 1] if j else d, (2, "bchain", j), 1)
    for j in range(L): g.opt(B1, D, a[j], (3, "b1lane", j), 0, gkey=(0, j))
    g.opt(B1, s, B1, (20, "set1"), 0, gkey=(9, 0))
    g.opt(X, s, X, (20, "x"), 0, gkey=(5, 0))
    for i in range(M):
        g.opt(f[i], None, X, (1, "fexit", i), 1)
        g.opt(f[i], None, f[i + 1] if i + 1 < M else B1, (40, "fchain", i), 1)
    g.opt(B0, f[0], B0, (20, "set0"), 0, gkey=(6, 0))
    g.opt(B0, D, A1, (3, "acc"), 0, gkey=(0, 99))
    g.opt(A1, s, B1, (20, "copy1"), 0, gkey=(8, 0))
    return g.genome({"B0": 1})
if __name__ == "__main__":
    L, M = int(sys.argv[1]), int(sys.argv[2]); G, ix = build(L, M); out = sys.argv[3]
    json.dump(G, open(out, "w")); json.dump(ix, open(out[:-5] + ".names.json", "w"))
