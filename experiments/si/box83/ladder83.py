#!/usr/bin/env python3
"""L-SI box 83: LADDER-R (docs/si/box82-cyctower.md §5.2) as an IDEAL genome (R104 format: W-targets one level down, none at level 0;
[E-LEV] e-order by (level, gate)). Bits B_1..B_h (B_l at level l); T = top mover at level h + 1 (B_(h+1) := T).
- B_l options: UP_l (beta -> B_(l+1), e-face -> dummy D_(l-1): Odd never takes it), lane_(l,j) (beta -> helper a_(l,j); e-face -> dummy),
  SET_l (W-target w_l, Xi-target B_l itself, even beta). Start: UP_l.
- Carry = the hub play's own upward Xi-edge: w_l (level l - 1) has one option, beta -> B_(l+1) (e-face -> dummy). NO access options (K5).
- RS2-style delay lane per level: helpers a_(l,j) (level 0, even beta rising with j) -> lane movers b_(l,j) (level 0) with EXIT (beta ->
  B_(l+1), odd) or CHAIN (beta -> b_(l,j-1), b_(l,0) -> bonus d_l with a top even beta; odd). Start EXIT.
- Hub H (level 0): beta -> B_1.
- Variant flag UPE=1: UP_l's e-face goes to a level-(l-1) mover y_l (beta -> B_(l+1)) instead of the dummy (an Odd choice at UP_l).
- FL (continuation lane F_l of SET_l, M_l movers f_(l,i) at level l - 1; SET_l's W-target = f_(l,0) instead of w_l):
  FL=none: the literal design (w_l -> B_(l+1));
  FL=exitup: f EXIT (beta -> B_(l+1)) or CHAIN (beta -> f_(l,i+1); last -> bonus c_l, top even beta, then u);
  FL=chainup (RS2's F0): f EXIT (beta -> X_l: a forced-escape SET-type mover of level l whose e_x is below e_l) or CHAIN (beta ->
  f_(l,i+1); last -> B_(l+1)).
Usage: ladder83.py h L1,L2,... OUT.json [UPE] [FL] [M1,M2,...]"""
import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen83 import Gen, save
def build(h, Ls, upe=0, fl="none", Ms=None):
    g = Gen(); D = [g.mv(f"D{l}", l) for l in range(h + 1)]
    g.opt(D[0], None, D[0], (99, 0), 0, (0,), "dummy")
    for l in range(1, h + 1): g.opt(D[l], D[l - 1], D[l], (98, l), 0, (0,), "dummy")
    B = {l: g.mv(f"B{l}", l) for l in range(1, h + 1)}; B[h + 1] = g.mv("T", h + 1)
    g.opt(B[h + 1], D[h], None, (8, 0), 1, (0,), "top")
    H = g.mv("H", 0); g.opt(H, None, B[1], (7, 0), 1, (0,), "hub")
    for l in range(1, h + 1):
        wl = D[l - 2] if l >= 2 else None
        if fl == "none":
            w = g.mv(f"w{l}", l - 1); g.opt(w, wl, B[l + 1], (6, l), 1, (0,), "carry")
        else:
            M = Ms[l - 1]; f = [g.mv(f"f{l}_{i}", l - 1) for i in range(M)]; w = f[0]
            if fl == "exitup":
                c = g.mv(f"c{l}", 0); g.opt(c, None, None, (51, l), 0, (0,), "bonus")
                ex, ce = B[l + 1], c
            else:
                X = g.mv(f"X{l}", l); sk = g.mv(f"s{l}", l - 1); g.opt(sk, wl, None, (0, l), 1, (0,), "sink")
                g.opt(X, sk, X, (21, l), 0, (8, l), "x"); ex, ce = X, B[l + 1]
            for i in range(M):
                g.opt(f[i], wl, ex, (1, l, 100 + i), 1, (0,), "exit")
                g.opt(f[i], wl, f[i + 1] if i + 1 < M else ce, (40, l, i), 1, (0,), "chain")
        if upe:
            y = g.mv(f"y{l}", l - 1); g.opt(y, D[l - 2] if l >= 2 else None, B[l + 1], (6, l, 1), 1, (0,), "y")
        g.opt(B[l], y if upe else D[l - 1], B[l + 1], (5, l), 1, (1, l), "UP")
        d = g.mv(f"d{l}", 0); g.opt(d, None, None, (50, l), 0, (0,), "bonus")
        L = Ls[l - 1]; a = [g.mv(f"a{l}_{j}", 0) for j in range(L)]; b = [g.mv(f"b{l}_{j}", 0) for j in range(L)]
        for j in range(L):
            g.opt(a[j], None, b[j], (30, l, j), 0, (0,), "lane")
            g.opt(b[j], None, B[l + 1], (1, l, j), 1, (0,), "exit")
            g.opt(b[j], None, b[j - 1] if j else d, (2, l, j), 1, (0,), "chain")
            g.opt(B[l], D[l - 1], a[j], (3, l, j), 0, (0, l, j), f"lane{j}")
        g.opt(B[l], w, B[l], (20, l), 0, (9, l), "SET")
    return g.genome({})
if __name__ == "__main__":
    h = int(sys.argv[1]); Ls = [int(x) for x in sys.argv[2].split(",")]; upe = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    fl = sys.argv[5] if len(sys.argv) > 5 else "none"; Ms = [int(x) for x in sys.argv[6].split(",")] if len(sys.argv) > 6 else None
    G, nm = build(h, Ls, upe, fl, Ms); save(G, nm, sys.argv[3])
