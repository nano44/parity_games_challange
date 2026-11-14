#!/usr/bin/env python3
"""MUTUAL-FEEDBACK seed (L-SI 41 box 77 §9 design): tower = levels 0..h of a given tower genome; fuel block C on levels h+1..h+m:
(2l, k) -> 2(l-1) + (1 - k), (2l+1, k) -> 2(l-1) + k (crossed onto the C pair below), the bottom C pair -> X; every tower option
whose Xi-target is above level h is re-pointed to the top C pair (same q = target index parity). C ranks below all tower ranks,
parity of (x, k) even iff k = 0, gates fresh, starts 0. Usage: mutual.py tower.json h m out.txt"""
import sys, json
G = json.load(open(sys.argv[1])); h = int(sys.argv[2]); m = int(sys.argv[3]); out = sys.argv[4]
d = h + 1 + m; N = 2 * d; NT = 2 * (h + 1)
xt, br, bp, gt, st = [], [], [], [], []
for x in range(NT):
    for k in range(2):
        o = G["opts"][x][k]; t = o[1]
        if t >= NT: t = 2 * (d - 1) + (t % 2)
        xt.append(t); br.append(1000 + G["br"][o[2]]); bp.append(G["bp"][o[2]]); gt.append(G["gate"][x][k])
    st.append(G["start"][x])
for x in range(NT, N):
    l = x // 2; p = x % 2
    for k in range(2):
        xt.append(-1 if l == h + 1 else 2 * (l - 1) + ((1 - k) if p == 0 else k)); br.append(4 * l + 2 * p + k); bp.append(0 if k == 0 else 1)
        gt.append(5000 + 4 * l + 2 * k + p)
    st.append(0)
order = sorted(range(len(br)), key=lambda i: br[i]); rk = [0] * len(br)
for r, i in enumerate(order): rk[i] = r
with open(out, "w") as f:
    f.write(f"d {d}\n")
    for key, v in (("xt", xt), ("br", rk), ("bp", bp), ("gate", gt), ("start", st)): f.write(key + " " + " ".join(map(str, v)) + "\n")
