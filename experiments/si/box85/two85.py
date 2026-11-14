#!/usr/bin/env python3
"""L-SI box 85: TWO COPIES PER LEVEL (Lead GO 05:06Z 2026-11-08). On MIRROR (box84 pair84.py, MUP=1) add per level l a LOW copy
L_l (mover at level l; its SET e has gate key (9, -1, l): at level l, BELOW e_SET_l = (9, 0, l), above every lower level), and make
B_l's SET W-target w_l a mover with several options (B_l's own WAITING HUB): cont -> M_(l+1) (as MIRROR) plus the options in cfg "w"
(targets by kind, relative to l). Optional extra B_l options cfg "wait" (beta -> target, dead e-face).
Kinds: "M+" = M_(l+1) (T at the top), "B+" = B_(l+1), "L" = L_l, "L-" = L_(l-1), "B-" = B_(l-1), "M-" = M_(l-1) (if it exists),
"Lw" = L_l's own W-target mover lw_l. Missing targets (below level 1 / no mirror) are skipped.
L_l: UP -> cfg lup (kind), RS2 lane of length LL_l exiting to cfg lexit, SET with W-target lw_l (one option per kind in cfg "lw",
default ["M+"]). cfg JSON keys: h, L, LM, LL, mup (1), lup, lexit, w, wait, lw, lmin (lowest level with a low copy, default 1).
Usage: two85.py CFG.json OUT.json   |  module: build(cfg) -> (G, names)"""
import sys, os, json; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen83 import Gen, save
def build(c):
    h = c["h"]; Ls, LMs, LLs = c["L"], c["LM"], c["LL"]; mup = c.get("mup", 1); lmin = c.get("lmin", 1)
    g = Gen(); D = [g.mv(f"D{l}", l) for l in range(h + 1)]
    g.opt(D[0], None, D[0], (99, 0), 0, (0,), "dummy")
    for l in range(1, h + 1): g.opt(D[l], D[l - 1], D[l], (98, l), 0, (0,), "dummy")
    B = {l: g.mv(f"B{l}", l) for l in range(1, h + 1)}; B[h + 1] = g.mv("T", h + 1)
    M = {l: g.mv(f"M{l}", l) for l in range(2, h + 1)}; M[h + 1] = B[h + 1]
    Lc = {l: g.mv(f"L{l}", l) for l in range(lmin, h + 1)}
    g.opt(B[h + 1], D[h], None, (8, 0), 1, (0,), "top")
    H = g.mv("H", 0); g.opt(H, None, B[1], (7, 0), 1, (0,), "hub")
    W = {}; LW = {}
    for l in range(1, h + 1): W[("b", l)] = g.mv(f"wb{l}", l - 1)
    for l in range(2, h + 1): W[("m", l)] = g.mv(f"wm{l}", l - 1)
    for l in Lc: LW[l] = g.mv(f"lw{l}", l - 1)
    def tgt(kind, l):
        return {"M+": M.get(l + 1), "B+": B.get(l + 1), "L": Lc.get(l), "L-": Lc.get(l - 1), "B-": B.get(l - 1), "M-": M.get(l - 1),
                "Lw": LW.get(l), "L+": Lc.get(l + 1)}[kind]
    def dead(l): return D[l - 1] if l >= 1 else None
    cnt = [0]
    def bkey(*a): cnt[0] += 1; return (a[0], cnt[0]) + a[1:]
    def wopts(wv, l, kinds):
        for kd in kinds:
            t = tgt(kd, l)
            if t is None: continue
            g.opt(wv, dead(l - 1), t, bkey(6, kd, l), 1, (0,), kd)
    def bit(x, l, L, tag, gk, up, ex, wv, wk):
        wopts(wv, l, wk)
        g.opt(x, D[l - 1], up, bkey(5, tag, l), 1, (1, tag, l), "UP")
        d = g.mv(f"d{tag}{l}", 0); g.opt(d, None, None, bkey(50, tag, l), 0, (0,), "bonus")
        a = [g.mv(f"a{tag}{l}_{j}", 0) for j in range(L)]; b = [g.mv(f"b{tag}{l}_{j}", 0) for j in range(L)]
        for j in range(L):
            g.opt(a[j], None, b[j], bkey(30, tag, l, j), 0, (0,), "lane")
            g.opt(b[j], None, ex, bkey(1, tag, l, j), 1, (0,), "exit")
            g.opt(b[j], None, b[j - 1] if j else d, bkey(2, tag, l, j), 1, (0,), "chain")
            g.opt(x, D[l - 1], a[j], bkey(3, tag, l, j), 0, (0, tag, l, j), f"lane{j}")
        g.opt(x, wv, x, bkey(20, tag, l), 0, gk, "SET")
    for l in range(1, h + 1):
        bit(B[l], l, Ls[l - 1], "b", (9, 0, l), B[l + 1], B[l + 1], W[("b", l)], ["M+"] + c.get("w", []))
        for kd in c.get("wait", []):
            t = tgt(kd, l)
            if t is not None: g.opt(B[l], D[l - 1], t, bkey(4, kd, l), 0, (0, "wait", l), "WAIT" + kd)
    for l in range(2, h + 1):
        bit(M[l], l, LMs[l - 2], "m", (9, 1, l), M[l + 1] if mup else B[l + 1], B[l + 1], W[("m", l)], ["M+"])
    for l in Lc:
        bit(Lc[l], l, LLs[l - lmin], "l", (9, -1, l), tgt(c.get("lup", "B+"), l), tgt(c.get("lexit", "B+"), l), LW[l], c.get("lw", ["M+"]))
    return g.genome({})
if __name__ == "__main__":
    G, nm = build(json.load(open(sys.argv[1]))); save(G, nm, sys.argv[2])
