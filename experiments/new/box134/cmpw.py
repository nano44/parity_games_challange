#!/usr/bin/env python3
"""L-NEW box 134 CMPW: classification of ORDER FLIPS behind FL moves. For every maximal FL run (box132/anchor.py detection), every
transition j >= a + 2 and every Even mover x (old option z = sigma_(j-1)(x), new option y = sigma_j(x)): a FLIP is Xi_(j-2)(y) not > Xi_(j-2)(z)
but Xi_(j-1)(y) > Xi_(j-1)(z) (the release behind the move). Each option's Xi-prefix at state s is the W-play (sigma_s at Even, tau at Odd)
from it up to the first anchor A in ODIFF_s u CN (Lemma PREFIX). Classes, first match:
  PREFIX  a prefix (vertex sequence) or anchor of y or z differs between j-2 and j-1;
  CROSS   anchors of y and z differ;
  INPREF  same anchor A, and the cycle node w of Xi_(j-1)(A) or of Xi_(j-2)(A) lies on one of the prefixes;
  CYCNODE same anchor, w changes between j-2 and j-1;
  SAMEW   same anchor, same prefixes, same w, w on neither prefix: Lemma COMPARE-W predicts 0.
Usage: cmpw.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "box132", "anchor.py")).read().split("R = dict(runs")[0]
exec(src.replace("os.path.dirname(os.path.abspath(__file__))", repr(os.path.join(HERE, "..", "box132"))))
C = dict(moves=0, flips=0, prefix=0, cross=0, inpref=0, cycnode=0, samew=0, nonflip=0); ex = []
for a, b in runs:
    tau = T[a]; W = wval(a); CN = {v for v in range(n) if W[v][2] == 0}
    XS = {j: E.evaluate(S[j]) for j in range(a, b + 1)}
    def pre(s, y):
        vs, sb = XS[s]; od = {o for o in range(n) if own[o] == 1 and sb[o] != tau[o]}
        p = []; u = y
        while u not in od and u not in CN and len(p) <= n:
            p.append(u); u = S[s][u] if own[u] == 0 else tau[u]
        return tuple(p), u
    for j in range(a + 1, b + 1):
        for x in range(n):
            if own[x] or S[j][x] == S[j - 1][x] or x in CN: continue
            C["moves"] += 1
            if j < a + 2: continue
            y, z = S[j][x], S[j - 1][x]
            k = lambda s, v: E.key(XS[s][0][v])
            if k(j - 2, y) > k(j - 2, z) or not k(j - 1, y) > k(j - 1, z): C["nonflip"] += 1; continue
            C["flips"] += 1
            P2y, A2y = pre(j - 2, y); P2z, A2z = pre(j - 2, z); P1y, A1y = pre(j - 1, y); P1z, A1z = pre(j - 1, z)
            if (P2y, A2y, P2z, A2z) != (P1y, A1y, P1z, A1z): cl = "prefix"
            elif A1y != A1z: cl = "cross"
            else:
                w1, w2 = XS[j - 1][0][A1y][0], XS[j - 2][0][A1y][0]
                if {w1, w2} & (set(P1y) | set(P1z)): cl = "inpref"
                elif w1 != w2: cl = "cycnode"
                else: cl = "samew"
            C[cl] += 1
            if cl == "samew" and len(ex) < 5: ex.append((a, j, x, z, y, A1y))
print(f"CMPW {os.path.basename(sys.argv[1])} n {n} " + " ".join(f"{k.upper()} {v}" for k, v in C.items()) + (f" EX {ex}" if ex else ""))
