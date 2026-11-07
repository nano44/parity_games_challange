#!/usr/bin/env python3
"""L-RED 55 R218: H1 hub WITHOUT access edges. PROBE=1: S enters B_k only through a copy gate Q_k (e-face e_q(k) -> U_k with
e_k < e_q(k) < e_(k+1), so Odd ENTERS a set bit; beta-face -> B_k with the top odd beta 60, so an open bit's cycle S -> Q_k -> B_k -> lane -> S
is Odd-won and S avoids it). PROBE=0: S -> B_k directly. (Lead 20:01Z hint). Shared lane (2n), exits -> S; S (level 0): -> B_0 .. B_(n-1) or s
(it picks the lowest set bit, whose SET play runs up through every set bit via the upper selectors U_k). Bits: SET_k (e_k -> U_k), lane
options -> a_m (m < 2k + 2). No ACC options. Lane root d: bonus -> ROOT (s | S).  Usage: t4.py n ROOT OUT.json [PROBE]"""
import sys, json
from gdsl import Gen
def build(n, root, probe=0):
    g = Gen(); lab = {}
    def mv(nm, lv): lab[nm] = []; return g.mv(nm, lv)
    def opt(x, wt, xt, bk, par, gkey=(0,), L=""): lab[x].append(L); g.opt(x, wt, xt, bk, par, gkey)
    s = mv("s", 0); D = mv("DUMMY", 0); S = mv("S", 0); d = mv("d", 0)
    L = 2 * n; a = [mv(f"a{m}", 0) for m in range(L)]; b = [mv(f"b{m}", 0) for m in range(L)]
    B = [mv(f"B{k}", 1) for k in range(n)]; U = [mv(f"U{k}", 0) for k in range(n)]
    opt(s, None, None, (0, "sink"), 1, L="u"); opt(D, None, D, (99, "dummy"), 0, L="D")
    opt(d, None, s if root == "s" else S, (50, "bonus"), 0, L="root")
    opt(S, None, s, (1, "Ss"), 1, L="s")
    Q = [mv(f"Q{k}", 1) for k in range(n)] if probe else B
    for k in range(n): opt(S, None, Q[k], (1, "SB", k), 1, L=f"B{k}")
    if probe:
        for k in range(n): opt(Q[k], U[k], B[k], (60, "probe", k), 1, gkey=(10, k, 1), L="q")
    for m in range(L):
        opt(a[m], None, b[m], (30, m), 0, L="b")
        opt(b[m], None, S, (1, "bx", m), 1, L="X"); opt(b[m], None, b[m - 1] if m else d, (2, "bc", m), 1, L="c")
    for k in range(n):
        opt(U[k], None, s, (1, "Us", k), 1, L="s")
        for j in range(k + 1, n): opt(U[k], None, B[j], (1, "Ub", k, j), 1, L=f"B{j}")
    for k in range(n):
        for m in range(2 * k + 2): opt(B[k], D, a[m], (3, "lane", k, m), 0, gkey=(0, k, m), L=f"a{m}")
        opt(B[k], U[k], B[k], (20, "set", k), 0, gkey=(10, k, 0), L="SET")
    G, ix = g.genome(); return G, ix, lab
if __name__ == "__main__":
    n, root, out = int(sys.argv[1]), sys.argv[2], sys.argv[3]; G, ix, lab = build(n, root, int(sys.argv[4]) if len(sys.argv) > 4 else 0)
    json.dump(G, open(out, "w")); json.dump(ix, open(out[:-5] + ".names.json", "w")); json.dump(lab, open(out[:-5] + ".labels.json", "w"))
