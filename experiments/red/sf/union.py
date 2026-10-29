#!/usr/bin/env python3
"""L-RED successor 29: disjoint union of two games with starts (B priorities shifted above A, parity kept).
Usage: union.py A.pg A.start B.pg B.start OUT.pg OUT.start"""
import sys, re
def rd(p):
    L = [l for l in open(p) if re.match(r"\s*\d", l)]
    return [re.match(r'\s*(\d+)\s+(\d+)\s+(\d+)\s+([\d,]+)(.*)', l).groups() for l in L]
A, B = rd(sys.argv[1]), rd(sys.argv[3]); na = len(A); off = max(int(x[1]) for x in A) + 2; off += off % 2
out = [f"parity {na + len(B) - 1};"]
for v, p, o, s, rest in A: out.append(f"{v} {p} {o} {s}{rest.rstrip()}")
for v, p, o, s, rest in B: out.append(f"{int(v) + na} {int(p) + off} {o} {','.join(str(int(x) + na) for x in s.split(','))}{rest.rstrip()}")
open(sys.argv[5], "w").write("\n".join(out) + "\n")
def st(p):
    d = {}
    for l in open(p):
        k, *xs = l.split(); d[k] = xs
    return d
sa, sb = st(sys.argv[2]), st(sys.argv[4])
with open(sys.argv[6], "w") as f:
    for k in ("SIGMA0", "TAU0"):
        f.write(k + " " + " ".join(sa.get(k, []) + [f"{int(a.split(':')[0]) + na}:{int(a.split(':')[1]) + na}" for a in sb.get(k, [])]) + "\n")
