#!/usr/bin/env python3
"""L-RED 55 R218 test (2) v1: hierarchical (prefix / Fenwick-style) hubs. Bit k has its own deceleration lane (length 2k+2) whose
exits go to P^k = a probe chain over the LOWER bits j < k (copy k): probe P^k_j is a level-1 copy gate, e-face e_m(k,j) -> P^k_(j-1)
(-> s at j = 0), beta-face -> B_j (odd beta, top band). Mirror e's rank below every bit e, ordered by (j, k). So Omega(P^k) encodes
the full lower state (up to 2^k values). Lane root d_k: bonus even beta -> ROOT (s | P = P^k).
Bits, upper selectors U_k, access movers A_kj (resets) and F_k lanes as in t1.py (F exits -> P^k).
Usage: t2.py n M ROOT OUT.json"""
import sys, json
from gdsl import Gen
def build(n, M, root):
    g = Gen(); lab = {}
    def mv(nm, lv): lab[nm] = []; return g.mv(nm, lv)
    def opt(x, wt, xt, bk, par, gkey=(0,), L=""): lab[x].append(L); g.opt(x, wt, xt, bk, par, gkey)
    s = mv("s", 0); D = mv("DUMMY", 0)
    B = [mv(f"B{k}", 1) for k in range(n)]; U = [mv(f"U{k}", 0) for k in range(n)]
    P = {(k, j): mv(f"P{k}_{j}", 1) for k in range(n) for j in range(k)}
    top = lambda k: P[(k, k - 1)] if k else s
    a = {k: [mv(f"a{k}_{m}", 0) for m in range(2 * k + 2)] for k in range(1, n)}
    b = {k: [mv(f"b{k}_{m}", 0) for m in range(2 * k + 2)] for k in range(1, n)}
    d = {k: mv(f"d{k}", 0) for k in range(1, n)}
    F = [[mv(f"f{k}_{i}", 0) for i in range(M)] for k in range(n)]
    A = {(k, j): mv(f"A{k}_{j}", 1) for k in range(n) for j in range(k + 1, n)}
    opt(s, None, None, (0, "sink"), 1, L="u"); opt(D, None, D, (99, "dummy"), 0, L="D")
    for (k, j), p in P.items(): opt(p, P[(k, j - 1)] if j else s, B[j], (60, "probe", k, j), 1, gkey=(1, j, k), L="p")
    for k in range(1, n):
        opt(d[k], None, s if root == "s" else top(k), (50, "bonus", k), 0, L="root")
        for m in range(2 * k + 2):
            opt(a[k][m], None, b[k][m], (30, m, k), 0, L="b")
            opt(b[k][m], None, top(k), (1, "bx", k, m), 1, L="X"); opt(b[k][m], None, b[k][m - 1] if m else d[k], (2, "bc", k, m), 1, L="c")
    for k in range(n):
        for i in range(M):
            opt(F[k][i], None, top(k), (1, "fx", k, i), 1, L="X"); opt(F[k][i], None, F[k][i + 1] if i + 1 < M else U[k], (40, "fc", k, i), 1, L="c")
        opt(U[k], None, s, (1, "Us", k), 1, L="s")
        for j in range(k + 1, n): opt(U[k], None, B[j], (1, "Ub", k, j), 1, L=f"B{j}")
    for k in range(n):
        if k:
            for m in range(2 * k + 2): opt(B[k], D, a[k][m], (3, "lane", k, m), 0, gkey=(0, k, m), L=f"a{m}")
        else: opt(B[k], D, s, (3, "open0"), 0, gkey=(0, 0), L="o")
        opt(B[k], F[k][0] if M else U[k], B[k], (20, "set", k), 0, gkey=(10, 3 * k + 2), L="SET")
        for j in range(k + 1, n):
            opt(B[k], D, A[(k, j)], (3, "acc", k, j), 0, gkey=(0, 99, k, j), L=f"ACC{j}")
            opt(A[(k, j)], U[j], B[j], (20, "copy", k, j), 0, gkey=(10, 3 * j + 1, k), L="cp")
    G, ix = g.genome(); return G, ix, lab
if __name__ == "__main__":
    n, M, root, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]; G, ix, lab = build(n, M, root)
    json.dump(G, open(out, "w")); json.dump(ix, open(out[:-5] + ".names.json", "w")); json.dump(lab, open(out[:-5] + ".labels.json", "w"))
