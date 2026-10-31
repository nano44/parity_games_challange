#!/usr/bin/env python3
"""L-RED successor 38 (D-ODD-1): run n5b SPEC from two start files and compare the (sigma, tau) state sequences, ignoring the vertices
whose start entries differ at state 0 only if they never change. Prints iterations, fallbacks and the first differing state (or IDENTICAL
up to the repaired entries). Usage: trcmp.py G.pg START_A START_B"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "n5-second"))
import n5b
g = n5b.pg.read(sys.argv[1]); R = []
for sp in sys.argv[2:4]:
    s0, t0 = n5b.read_start(sp, g); N = n5b.N5(g); N.mode = "spec"; tr, fb = [], []; N.run(s0, t0, trace=tr, fbtrace=fb)
    R.append((tr, fb))
(A, fa), (B, fbb) = R
diffv = {v for v in range(g.n) if A[0][0][v] != B[0][0][v] or A[0][1][v] != B[0][1][v]}
first = None
for k in range(max(len(A), len(B))):
    if k >= len(A) or k >= len(B): first = k; break
    d = {v for v in range(g.n) if A[k][0][v] != B[k][0][v] or A[k][1][v] != B[k][1][v]}
    if d - diffv: first = k; break
print(f"A iters {len(A) - 1} fb {sum(fa)} | B iters {len(B) - 1} fb {sum(fbb)} | start-diff vertices {sorted(diffv)} | " + ("IDENTICAL up to them" if first is None else f"FIRST DIFFERENT STATE {first}"))
