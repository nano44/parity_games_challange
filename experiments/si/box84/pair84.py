#!/usr/bin/env python3
"""L-SI box 84: HUB PAIR «MIRROR» (Lead GO 01:54Z, design (c)): a bit's SET continuation and its alternatives go into DIFFERENT higher
movers, breaking Lemma LOCK-UP's hypothesis «every option of B other than S has its Xi-target in Y u {X} u Z u {u}» with X = the
continuation's target. Real bits B_1..B_h (B_l at level l), mirrors M_2..M_h (M_l at level l, same decision rule as B_l, longer delay
lane, mirror e above the real e at its level), top T = B_(h+1) = M_(h+1).
- B_l (and M_l): UP (beta -> B_(l+1)), lanes (RS2 delay lane of length L_l for B_l, LM_l for M_l, exits -> B_(l+1)),
  SET (W-target w_l / wm_l at level l - 1, Xi-target itself, even beta). w_l: one option, beta -> M_(l+1) (the mirror; T at the top).
- H (level 0): beta -> B_1.
MUP=1: a mirror's UP goes to the next MIRROR M_(l+1) (its lanes still exit to the real B_(l+1)).
Usage: pair84.py h L1,..,Lh LM2,..,LMh OUT.json [MUP]"""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen83 import Gen, save
def build(h, Ls, LMs, mup=0):
    g = Gen(); D = [g.mv(f"D{l}", l) for l in range(h + 1)]
    g.opt(D[0], None, D[0], (99, 0), 0, (0,), "dummy")
    for l in range(1, h + 1): g.opt(D[l], D[l - 1], D[l], (98, l), 0, (0,), "dummy")
    B = {l: g.mv(f"B{l}", l) for l in range(1, h + 1)}; B[h + 1] = g.mv("T", h + 1)
    M = {l: g.mv(f"M{l}", l) for l in range(2, h + 1)}; M[h + 1] = B[h + 1]
    g.opt(B[h + 1], D[h], None, (8, 0), 1, (0,), "top")
    H = g.mv("H", 0); g.opt(H, None, B[1], (7, 0), 1, (0,), "hub")
    def bit(x, l, L, tag, gk):
        wl = D[l - 2] if l >= 2 else None
        w = g.mv(f"w{tag}{l}", l - 1); g.opt(w, wl, M[l + 1], (6, tag, l), 1, (0,), "cont")
        g.opt(x, D[l - 1], M[l + 1] if (mup and tag == "m") else B[l + 1], (5, tag, l), 1, (1, tag, l), "UP")
        d = g.mv(f"d{tag}{l}", 0); g.opt(d, None, None, (50, tag, l), 0, (0,), "bonus")
        a = [g.mv(f"a{tag}{l}_{j}", 0) for j in range(L)]; b = [g.mv(f"b{tag}{l}_{j}", 0) for j in range(L)]
        for j in range(L):
            g.opt(a[j], None, b[j], (30, tag, l, j), 0, (0,), "lane")
            g.opt(b[j], None, B[l + 1], (1, tag, l, j), 1, (0,), "exit")
            g.opt(b[j], None, b[j - 1] if j else d, (2, tag, l, j), 1, (0,), "chain")
            g.opt(x, D[l - 1], a[j], (3, tag, l, j), 0, (0, tag, l, j), f"lane{j}")
        g.opt(x, w, x, (20, tag, l), 0, gk, "SET")
    for l in range(1, h + 1): bit(B[l], l, Ls[l - 1], "b", (9, 0, l))
    for l in range(2, h + 1): bit(M[l], l, LMs[l - 2], "m", (9, 1, l))     # mirror e above the real e at level l
    return g.genome({})
if __name__ == "__main__":
    h = int(sys.argv[1]); Ls = [int(x) for x in sys.argv[2].split(",")]; LMs = [int(x) for x in sys.argv[3].split(",")] if sys.argv[3] != "-" else []
    mup = int(sys.argv[5]) if len(sys.argv) > 5 else 0
    G, nm = build(h, Ls, LMs, mup); save(G, nm, sys.argv[4])
