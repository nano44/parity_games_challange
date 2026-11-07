#!/usr/bin/env python3
"""L-RED 54 R217: 3-bit attempt with PER-BIT lanes (Lead 17:55Z test (2)). Extends rs2.py:
- B1 delay lane a1/b1 (L1), B2 delay lane a2/b2 (L2 > L1): e-free, bits hide there.
- B0: SET0 (e0 -> F0, F0 end -> B1), ACC1 (copy of B1, e1'), ACC2 (copy of B2, e2_0).
- B1: lane1 options, SET1 (e1 -> F1, F1 end -> B2), ACC2 (copy of B2, e2_1).
- B2: lane2 options, SET2 (e2 -> s).  F_j exits -> X_j (forced bit, e_x_j).
- e order (gate keys): e_x0 < e0 < e1' < e_x1 < e1 < e2_0 < e2_1 < e2.
Usage: rs3.py L1 L2 M0 M1 OUT.json"""
import sys, json
from gdsl import Gen
def lane(g, tag, L, bonus):
    a = [g.mv(f"{tag}a{j}", 0) for j in range(L)]; b = [g.mv(f"{tag}b{j}", 0) for j in range(L)]; d = g.mv(f"{tag}d", 0)
    g.opt(d, None, None, (50 + bonus, tag), 0)
    for j in range(L):
        g.opt(a[j], None, b[j], (30 + bonus, j), 0)
        g.opt(b[j], None, None, (1, tag + "x", j), 1)
        g.opt(b[j], None, b[j - 1] if j else d, (2, tag + "c", j), 1)
    return a
def build(L1, L2, M0, M1):
    g = Gen(); s = g.mv("s", 0); D = g.mv("DUMMY", 0); g.opt(s, None, None, (0, "sink"), 1); g.opt(D, None, D, (99, "dummy"), 0)
    a1 = lane(g, "L1", L1, 0); a2 = lane(g, "L2", L2, 5)
    B0, B1, B2 = g.mv("B0", 1), g.mv("B1", 1), g.mv("B2", 1)
    A1, A2a, A2b = g.mv("A1", 1), g.mv("A2a", 1), g.mv("A2b", 1); X0, X1 = g.mv("X0", 1), g.mv("X1", 1)
    f0 = [g.mv(f"f0_{i}", 0) for i in range(M0)]; f1 = [g.mv(f"f1_{i}", 0) for i in range(M1)]
    for X, k in ((X0, 1), (X1, 4)): g.opt(X, s, X, (20, "x", k), 0, gkey=(k, 0))
    for f, X, end, t in ((f0, X0, B1, 0), (f1, X1, B2, 1)):
        for i in range(len(f)):
            g.opt(f[i], None, X, (1, "fx", t, i), 1); g.opt(f[i], None, f[i + 1] if i + 1 < len(f) else end, (40, "fc", t, i), 1)
    for j in range(L1): g.opt(B1, D, a1[j], (3, "B1l", j), 0, gkey=(0, j))
    for j in range(L2): g.opt(B2, D, a2[j], (3, "B2l", j), 0, gkey=(0, 50 + j))
    g.opt(B0, f0[0], B0, (20, "s0"), 0, gkey=(2, 0)); g.opt(B0, D, A1, (3, "a01"), 0, gkey=(0, 98)); g.opt(B0, D, A2a, (3, "a02"), 0, gkey=(0, 99))
    g.opt(B1, f1[0], B1, (20, "s1"), 0, gkey=(5, 0)); g.opt(B1, D, A2b, (3, "a12"), 0, gkey=(0, 97))
    g.opt(B2, s, B2, (20, "s2"), 0, gkey=(8, 0))
    g.opt(A1, s, B1, (20, "c1"), 0, gkey=(3, 0)); g.opt(A2a, s, B2, (20, "c20"), 0, gkey=(6, 0)); g.opt(A2b, s, B2, (20, "c21"), 0, gkey=(7, 0))
    return g.genome({"B0": 1})
if __name__ == "__main__":
    G, ix = build(*map(int, sys.argv[1:5])); out = sys.argv[5]; json.dump(G, open(out, "w")); json.dump(ix, open(out[:-5] + ".names.json", "w"))
