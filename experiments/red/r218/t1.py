#!/usr/bin/env python3
"""L-RED 55 R218 test (1): n-bit E-DOM counter attempt whose shared deceleration lane exits to a hub H that tracks ONLY the highest
set bit (probe gates C_k: e-face e_ck -> s, beta-face -> B_k with a high odd beta; e_c0 < ... < e_c(n-1) < every bit e).
- Bits B_k (level 1): SET_k (escape e_k -> F_k lane -> U_k), lane options -> a_m for m < 2k + 2 (bits hide there),
  ACC_kj (j > k): access mover A_kj, copy gate (e_acc_kj -> U_j, beta -> B_j); e order e_(j-1) < e_acc_*j < e_j.
- Upper selector U_k (level 0): -> B_(k+1) .. B_(n-1) or -> s.  F_k: M movers, EXIT -> H, CHAIN -> next (end -> U_k).
- Lane a_m (even beta, increasing) -> b_m; b_m: EXIT -> H, CHAIN -> b_(m-1) (b_0 -> d); d: bonus even beta -> ROOT (s or H).
Usage: t1.py n M ROOT(s|H) OUT.json  (writes OUT.names.json, OUT.labels.json)"""
import sys, json
from gdsl import Gen
def build(n, M, root):
    g = Gen(); lab = {}
    def mv(nm, lv): lab[nm] = []; return g.mv(nm, lv)
    def opt(x, wt, xt, bk, par, gkey=(0,), L=""):
        lab[x].append(L); g.opt(x, wt, xt, bk, par, gkey)
    s = mv("s", 0); D = mv("DUMMY", 0); H = mv("H", 0); d = mv("d", 0)
    L = 2 * n; a = [mv(f"a{m}", 0) for m in range(L)]; b = [mv(f"b{m}", 0) for m in range(L)]
    B = [mv(f"B{k}", 1) for k in range(n)]; U = [mv(f"U{k}", 0) for k in range(n)]; C = [mv(f"C{k}", 1) for k in range(n)]
    F = [[mv(f"f{k}_{i}", 0) for i in range(M)] for k in range(n)]
    A = {(k, j): mv(f"A{k}_{j}", 1) for k in range(n) for j in range(k + 1, n)}
    opt(s, None, None, (0, "sink"), 1, L="u"); opt(D, None, D, (99, "dummy"), 0, L="D")
    opt(d, None, s if root == "s" else H, (50, "bonus"), 0, L="root")
    for m in range(L):
        opt(a[m], None, b[m], (30, m), 0, L="b")
        opt(b[m], None, H, (1, "bx", m), 1, L="X"); opt(b[m], None, b[m - 1] if m else d, (2, "bc", m), 1, L="c")
    opt(H, None, s, (1, "Hs"), 1, L="s")
    for k in range(n): opt(H, None, C[k], (1, "Hc", k), 1, L=f"C{k}")
    for k in range(n): opt(C[k], s, B[k], (60, "probe", k), 1, gkey=(1, k), L="p")
    for k in range(n):
        for i in range(M):
            opt(F[k][i], None, H, (1, "fx", k, i), 1, L="X"); opt(F[k][i], None, F[k][i + 1] if i + 1 < M else U[k], (40, "fc", k, i), 1, L="c")
        opt(U[k], None, s, (1, "Us", k), 1, L="s")
        for j in range(k + 1, n): opt(U[k], None, B[j], (1, "Ub", k, j), 1, L=f"B{j}")
    for k in range(n):
        for m in range(2 * k + 2): opt(B[k], D, a[m], (3, "lane", k, m), 0, gkey=(0, k, m), L=f"a{m}")
        opt(B[k], F[k][0] if M else U[k], B[k], (20, "set", k), 0, gkey=(10, 3 * k + 2), L="SET")
        for j in range(k + 1, n):
            opt(B[k], D, A[(k, j)], (3, "acc", k, j), 0, gkey=(0, 99, k, j), L=f"ACC{j}")
            opt(A[(k, j)], U[j], B[j], (20, "copy", k, j), 0, gkey=(10, 3 * j + 1, k), L="cp")
    G, ix = g.genome(); return G, ix, lab
if __name__ == "__main__":
    n, M, root, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]; G, ix, lab = build(n, M, root)
    json.dump(G, open(out, "w")); json.dump(ix, open(out[:-5] + ".names.json", "w")); json.dump(lab, open(out[:-5] + ".labels.json", "w"))
