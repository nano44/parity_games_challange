#!/usr/bin/env python3
"""L-RED successor 38 (R164): for a given Odd s and its escape transitions u_1 < u_2 < ... (from platx.py), print W (valuation of sigma_k
against the run's fixed tau, desc2.py's W) of x = old choice and x2 = new choice at each u_i, and whether W(x) or W(x2) strictly rose
between consecutive escapes (L-SI box 58 §7 candidate (b)). Usage: wrise.py G.pg START s u1,u2,..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); s_, us = int(sys.argv[3]), [int(x) for x in sys.argv[4].split(",")]
sys.argv = sys.argv[:3]
src = open(os.path.join(HERE, "..", "desc", "desc2.py")).read(); src = src[:src.index("T = dict(")]
os.environ.setdefault("LNEW", os.path.join(HERE, "..", ".."))
exec(compile(src, "desc2.py", "exec"))
Bk = lambda k: E.evaluate(S[k])[1]
prev = None
for u in us:
    tau = TAU[u]; x, x2 = Bk(u)[s_], Bk(u + 1)[s_]; Wr = Wraw(u, tau)
    kx, kx2 = E.key(Wr[x]), E.key(Wr[x2])
    if prev: print(f"  rise since previous escape: W(x) {kx > prev[0]}  W(x2) {kx2 > prev[1]}  tau same {TAU[u] == prev[2]}")
    print(f"escape u {u}: x {x} x2 {x2}"); prev = (kx, kx2, TAU[u])
