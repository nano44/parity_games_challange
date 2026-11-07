#!/usr/bin/env python3
"""L-COMP box 30: drop the top k levels of a text genome (rclimb format; option m = 2x+k): movers >= 2(d-k) removed; an option whose
Xi-target is removed now targets the exit X (-1); beta ranks re-numbered 0..M'-1 in the old order; gates, parities, start kept.
Usage: trunc.py in.txt k out.txt"""
import sys
D = {}
for ln in open(sys.argv[1]):
    w = ln.split()
    if w and w[0] in ("d", "xt", "br", "bp", "gate", "start"): D[w[0]] = list(map(int, w[1:]))
d = D["d"][0] - int(sys.argv[2]); N = 2 * d; M = 2 * N
xt = [(-1 if y >= N else y) for y in D["xt"][:M]]; br = D["br"][:M]; srt = sorted(br); br = [srt.index(b) for b in br]
with open(sys.argv[3], "w") as f:
    f.write(f"d {d}\n"); f.write("xt " + " ".join(map(str, xt)) + "\n"); f.write("br " + " ".join(map(str, br)) + "\n")
    for k, n in (("bp", M), ("gate", M), ("start", N)): f.write(k + " " + " ".join(map(str, D[k][:n])) + "\n")
