#!/usr/bin/env python3
"""L-NEW box 52: graft a COMPARATOR onto a game: Odd u -> {a, b}, Even q -> {a, b}, Even z -> {u, q}, all three with priority PR (default
0, ranked below every old vertex of priority >= 0 with a larger index... ties go by index, so the new vertices rank above old priority-0
vertices only). No old vertex gets an edge into the new ones, so old plays never see them. tau(u) := a (TAU0), sigma(z) := u (SIGMA0), q takes SPEC S3.
MODE (8th argument): "q" (default) as above; "a": no q, z -> {u, a}; "b": no q, z -> {u, b}; "ab": two observers z1 -> {u, b},
z2 -> {u, a} (each sees the flips of sigma-bar(u) in one direction, since the true Xi(u) is never above the frozen one).
Usage: graft.py GAME.pg GAME.start a b OUT.pg OUT.start [PR [MODE]]"""
import sys
src, sst, a, b, out, ost = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5], sys.argv[6]
PR = int(sys.argv[7]) if len(sys.argv) > 7 else 0
MODE = sys.argv[8] if len(sys.argv) > 8 else "q"
L = [l for l in open(src) if l.strip() and not l.lstrip().startswith("%")]
body = [l for l in L if not l.startswith("parity")]; n = len(body); u, q, z = n, n + 1, n + 2
body = [l.rstrip("\n") for l in body]
if MODE == "q": body += ["%d %d 1 %d,%d;" % (u, PR, a, b), "%d %d 0 %d,%d;" % (q, PR, a, b), "%d %d 0 %d,%d;" % (z, PR, u, q)]
elif MODE == "ab":
    z = q + 1
    body += ["%d %d 1 %d,%d;" % (u, PR, a, b), "%d %d 0 %d,%d;" % (q, PR, *sorted((u, b))), "%d %d 0 %d,%d;" % (z, PR, *sorted((u, a)))]
else:
    z = q; y = a if MODE == "a" else b
    body += ["%d %d 1 %d,%d;" % (u, PR, a, b), "%d %d 0 %d,%d;" % (z, PR, *sorted((u, y)))]
open(out, "w").write("parity %d;\n" % (z) + "\n".join(body) + "\n")
S = open(sst).read().split("\n"); S = [s for s in S if s.strip()]
S = [s + (" %d:%d" % (u, a) if s.startswith("TAU0") else (" %d:%d" % (z, u) if s.startswith("SIGMA0") else "")) for s in S]
open(ost, "w").write("\n".join(S) + "\n")
