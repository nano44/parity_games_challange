#!/usr/bin/env python3
"""L-RED successor 27: named trace. Per transition t: Even switches (sigma) and Odd switches (tau) as v:old->new by label.
Usage: trn.py GAME.pg START|S3 [maxlines]"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cpl, n5b
g = n5b.pg.read(sys.argv[1]); lab = cpl.labels(sys.argv[1]); L = lambda v: lab.get(v, str(v))
s0, t0 = (None, None) if sys.argv[2] == "S3" else n5b.read_start(sys.argv[2], g)
N, tr, fb = cpl.run(g, s0, t0)
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 9
for t in range(min(len(tr) - 1, mx)):
    (s, u), (s2, u2) = tr[t], tr[t + 1]
    es = [f"{L(v)}:{L(s[v])}->{L(s2[v])}" for v in range(g.n) if s[v] != s2[v]]
    os_ = [f"{L(v)}:{L(u[v])}->{L(u2[v])}" for v in range(g.n) if u[v] != u2[v]]
    print(t, "FB" if fb[t] else "  ", "S[" + " ".join(es) + "]", "T[" + " ".join(os_) + "]")
