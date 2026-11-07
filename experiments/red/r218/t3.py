#!/usr/bin/env python3
"""L-RED 55 R218 test (2) v2: hub PAIR per lane, bottom-up trailing-ones reading (R218 §4).
- Global bottom-up mirror chain C_0..C_(n-1): C_j copy gate, e-face m_j -> C_(j+1) (-> s), beta-face -> B_j (top odd beta).
- Bit k >= 1: own lane (2k+2); lane nodes: CHAIN, EXIT_A -> XA_k, EXIT_B -> XB_k, EXIT_U -> C_(k+1) (UP=1 only); root d_k -> T_k
  (selector -> XA_k | XB_k).  B_0: option o -> C_1 (its hidden route goes up).
- XA_k / XB_k: private bottom-up probes over bits 0..k-1, copy A / copy B (B ranked above A at every level), then -> C_(k+1)
  (TAIL=C) or -> s (TAIL=s). Odd diverts at the lowest open bit into its hidden route.
- Bits: SET (e_k -> U_k), ACC_kj copies (resets), U_k upper selectors, as t1.py; no F lanes.
Usage: t3.py n UP TAIL OUT.json"""
import sys, json
from gdsl import Gen
def build(n, up, tail):
    g = Gen(); lab = {}
    def mv(nm, lv): lab[nm] = []; return g.mv(nm, lv)
    def opt(x, wt, xt, bk, par, gkey=(0,), L=""): lab[x].append(L); g.opt(x, wt, xt, bk, par, gkey)
    s = mv("s", 0); D = mv("DUMMY", 0)
    B = [mv(f"B{k}", 1) for k in range(n)]; U = [mv(f"U{k}", 0) for k in range(n)]; C = [mv(f"C{j}", 1) for j in range(n)]
    Cn = lambda j: C[j] if j < n else s
    PA = {(k, i): mv(f"PA{k}_{i}", 1) for k in range(1, n) for i in range(k)}; PB = {(k, i): mv(f"PB{k}_{i}", 1) for k in range(1, n) for i in range(k)}
    T = {k: mv(f"T{k}", 0) for k in range(1, n)}; d = {k: mv(f"d{k}", 0) for k in range(1, n)}
    a = {k: [mv(f"a{k}_{m}", 0) for m in range(2 * k + 2)] for k in range(1, n)}; b = {k: [mv(f"b{k}_{m}", 0) for m in range(2 * k + 2)] for k in range(1, n)}
    A = {(k, j): mv(f"A{k}_{j}", 1) for k in range(n) for j in range(k + 1, n)}
    opt(s, None, None, (0, "sink"), 1, L="u"); opt(D, None, D, (99, "dummy"), 0, L="D")
    for j in range(n): opt(C[j], Cn(j + 1), B[j], (60, "C", j), 1, gkey=(1, j, 0), L="p")
    for k in range(1, n):
        end = Cn(k + 1) if tail == "C" else s
        for i in range(k):
            opt(PA[(k, i)], PA[(k, i + 1)] if i + 1 < k else end, B[i], (61, "PA", k, i), 1, gkey=(1, i, 1, k), L="p")
            opt(PB[(k, i)], PB[(k, i + 1)] if i + 1 < k else end, B[i], (62, "PB", k, i), 1, gkey=(1, i, 2, k), L="p")
        opt(T[k], None, PA[(k, 0)], (1, "TA", k), 1, L="A"); opt(T[k], None, PB[(k, 0)], (1, "TB", k), 1, L="B")
        opt(d[k], None, T[k], (50, "bonus", k), 0, L="root")
        for m in range(2 * k + 2):
            opt(a[k][m], None, b[k][m], (30, m, k), 0, L="b")
            if up: opt(b[k][m], None, Cn(k + 1), (1, "bxu", k, m), 1, L="X")
            opt(b[k][m], None, PA[(k, 0)], (1, "bxa", k, m), 1, L="X"); opt(b[k][m], None, PB[(k, 0)], (1, "bxb", k, m), 1, L="X")
            opt(b[k][m], None, b[k][m - 1] if m else d[k], (2, "bc", k, m), 1, L="c")
    for k in range(n):
        opt(U[k], None, s, (1, "Us", k), 1, L="s")
        for j in range(k + 1, n): opt(U[k], None, B[j], (1, "Ub", k, j), 1, L=f"B{j}")
    for k in range(n):
        if k:
            for m in range(2 * k + 2): opt(B[k], D, a[k][m], (3, "lane", k, m), 0, gkey=(0, k, m), L=f"a{m}")
        else: opt(B[k], D, Cn(1), (3, "open0"), 0, gkey=(0, 0), L="o")
        opt(B[k], U[k], B[k], (20, "set", k), 0, gkey=(10, 3 * k + 2), L="SET")
        for j in range(k + 1, n):
            opt(B[k], D, A[(k, j)], (3, "acc", k, j), 0, gkey=(0, 99, k, j), L=f"ACC{j}")
            opt(A[(k, j)], U[j], B[j], (20, "copy", k, j), 0, gkey=(10, 3 * j + 1, k), L="cp")
    G, ix = g.genome(); return G, ix, lab
if __name__ == "__main__":
    n, up, tail, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]; G, ix, lab = build(n, up, tail)
    json.dump(G, open(out, "w")); json.dump(ix, open(out[:-5] + ".names.json", "w")); json.dump(lab, open(out[:-5] + ".labels.json", "w"))
