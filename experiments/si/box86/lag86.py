#!/usr/bin/env python3
"""L-SI box 86: LAG TOWER (Lead 07:12Z; docs/si/box86-lagtower.md). Real bits B_1..B_h (B_l at level l; UP -> B_(l+1); RS2 lane of
length L_l exiting to B_(l+1); SET with W-target w_l), top T = B_(h+1). For each bit l a private LAGGING copy chain C_(l,j), j = l+1..h,
of the upper bits (C_(l,j) at level j, the same rule as B_j, lane length CL(l,j) = cfg a*j + b*(h-l) + c, its SET e at gate key
(9, cpos*(1+l), j): above the real e_j if cpos = +1, below if -1), which can MERGE into the real chain:
- w_l (level l-1): option -> C_(l,l+1) (T when l = h); plus -> B_(l+1) if cfg wreal.
- C_(l,j): UP -> C_(l,j+1) (T at j = h), plus UPR -> B_(j+1) if cfg merge; lanes exit -> cfg cexit ('C' next copy | 'B' real);
  SET W-target wc_(l,j) (level j-1) with option -> C_(l,j+1) and, if cfg merge, -> B_(j+1).
- H (level 0): beta -> B_1. Every non-SET e-face is dead (W-target a dummy), as in pair84 / two85.
So w_l's play can follow the copies (lagging) and merge into the real chain at any level above l: by SAME-E-MERGE (note §1) a play
that shows a real e_j passes B_j, so «the same upper e's, one count behind» must be a copy prefix followed by a merge.
cfg JSON: h, L (list), a, b, c, cpos (+1/-1), wreal (0/1), merge (0/1), cexit ('C'/'B'). Usage: lag86.py CFG.json OUT.json"""
import sys, os, json; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen83 import Gen, save
def build(c):
    h = c["h"]; g = Gen(); D = [g.mv(f"D{l}", l) for l in range(h + 1)]; cnt = [0]
    def bk(*a): cnt[0] += 1; return (a[0], cnt[0]) + a[1:]
    g.opt(D[0], None, D[0], (99, 0), 0, (0,), "dummy")
    for l in range(1, h + 1): g.opt(D[l], D[l - 1], D[l], (98, l), 0, (0,), "dummy")
    B = {l: g.mv(f"B{l}", l) for l in range(1, h + 1)}; B[h + 1] = g.mv("T", h + 1)
    g.opt(B[h + 1], D[h], None, (8, 0), 1, (0,), "top")
    H = g.mv("H", 0); g.opt(H, None, B[1], (7, 0), 1, (0,), "hub")
    C = {}
    for l in range(1, h + 1):
        for j in range(l + 1, h + 1): C[(l, j)] = g.mv(f"C{l}_{j}", j)
        C[(l, h + 1)] = B[h + 1]
    def bit(x, l, L, tag, gk, ups, ex, wv, wts):
        for kd, t in wts: g.opt(wv, D[l - 2] if l >= 2 else None, t, bk(6, tag, l), 1, (0,), kd)
        for kd, t in ups: g.opt(x, D[l - 1], t, bk(5, tag, l), 1, (1, tag, l, kd), kd)
        d = g.mv(f"d{tag}", 0); g.opt(d, None, None, bk(50, tag), 0, (0,), "bonus")
        a = [g.mv(f"a{tag}_{i}", 0) for i in range(L)]; b = [g.mv(f"b{tag}_{i}", 0) for i in range(L)]
        for i in range(L):
            g.opt(a[i], None, b[i], bk(30, tag, i), 0, (0,), "lane")
            g.opt(b[i], None, ex, bk(1, tag, i), 1, (0,), "exit")
            g.opt(b[i], None, b[i - 1] if i else d, bk(2, tag, i), 1, (0,), "chain")
            g.opt(x, D[l - 1], a[i], bk(3, tag, i), 0, (0, tag, i), f"lane{i}")
        g.opt(x, wv, x, bk(20, tag), 0, gk, "SET")
    for l in range(1, h + 1):
        w = g.mv(f"w{l}", l - 1); wts = [("cp", C[(l, l + 1)])] + ([("real", B[l + 1])] if c.get("wreal", 1) and l < h else [])
        bit(B[l], l, c["L"][l - 1], f"B{l}", (9, 0, l), [("UP", B[l + 1])], B[l + 1], w, wts)
        for j in range(l + 1, h + 1):
            nx = C[(l, j + 1)]; ups = [("UP", nx)] + ([("UPR", B[j + 1])] if c.get("merge", 1) and j < h else [])
            wc = g.mv(f"wc{l}_{j}", j - 1); wts = [("cp", nx)] + ([("real", B[j + 1])] if c.get("merge", 1) and j < h else [])
            Lc = max(1, c["a"] * j + c["b"] * (h - l) + c["c"])
            bit(C[(l, j)], j, Lc, f"C{l}_{j}", (9, c.get("cpos", 1) * (1 + l), j), ups, B[j + 1] if c.get("cexit", "C") == "B" else nx, wc, wts)
    return g.genome({})
if __name__ == "__main__":
    G, nm = build(json.load(open(sys.argv[1]))); save(G, nm, sys.argv[2])
