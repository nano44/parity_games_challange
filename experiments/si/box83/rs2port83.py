#!/usr/bin/env python3
"""L-SI box 83: port of L-RED R217 rs2.py (claude/l-red experiments/red/r217/rs2.py) to gen83 with labels; DSL check: the genome
must equal box81/inst/RS2.json (L 4, M 3). Usage: rs2port83.py L M OUT.json"""
import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen83 import Gen, save
def build(L, M):
    g = Gen(); s = g.mv("s", 0); D = g.mv("DUMMY", 0); d = g.mv("d", 0)
    a = [g.mv(f"a{j}", 0) for j in range(L)]; b = [g.mv(f"b{j}", 0) for j in range(L)]
    f = [g.mv(f"f{i}", 0) for i in range(M)]; X = g.mv("TOPX", 1)
    B1 = g.mv("B1", 1); B0 = g.mv("B0", 1); A1 = g.mv("A1", 1)
    gk = iter(range(10 ** 6))
    g.opt(s, None, None, (0, "sink"), 1, (0,), "sink"); g.opt(D, None, D, (99, "dummy"), 0, (0,), "dummy")
    g.opt(d, None, None, (50, "bonus"), 0, (0,), "bonus")
    for j in range(L):
        g.opt(a[j], None, b[j], (30, j), 0, (0,), "lane")
        g.opt(b[j], None, None, (1, "bexit", j), 1, (0,), "exit")
        g.opt(b[j], None, b[j - 1] if j else d, (2, "bchain", j), 1, (0,), "chain")
    for j in range(L): g.opt(B1, D, a[j], (3, "b1lane", j), 0, (0, 0, j), f"lane{j}")
    g.opt(B1, s, B1, (20, "set1"), 0, (9, 0), "SET")
    g.opt(X, s, X, (20, "x"), 0, (5, 0), "x")
    for i in range(M):
        g.opt(f[i], None, X, (1, "fexit", i), 1, (0,), "exit")
        g.opt(f[i], None, f[i + 1] if i + 1 < M else B1, (40, "fchain", i), 1, (0,), "chain")
    g.opt(B0, f[0], B0, (20, "set0"), 0, (6, 0), "SET")
    g.opt(B0, D, A1, (3, "acc"), 0, (0, 99), "ACC")
    g.opt(A1, s, B1, (20, "copy1"), 0, (8, 0), "copy")
    return g.genome({"B0": 1})
if __name__ == "__main__":
    G, nm = build(int(sys.argv[1]), int(sys.argv[2])); save(G, nm, sys.argv[3])
