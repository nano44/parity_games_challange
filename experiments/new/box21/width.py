#!/usr/bin/env python3
"""Box 21: gate-width histogram (|Iσ| at each Even move) along the N5 run (canonical, or from (sigma_0, tau*) with 'tstar'),
and the number of W-improving edges refused by the step (in the gate, W-improving, not taken). Usage: width.py game.pg [tstar]"""
import sys
from collections import Counter
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))  # box21 -I: find sibling modules
from n5x import *
from h1 import wvals
def main(path, mode=""):
    g = load(path); E = Engine(g); n = g.n
    st, _ = trace(g)
    if mode == "tstar":
        s0, ts = st[0][0], st[-1][1]
        st, _ = trace(g, ({v: s0[v] for v in range(n) if g.owner[v] == 0}, {v: ts[v] for v in range(n) if g.owner[v] == 1}))
    h = Counter(); ref = 0
    for k in range(len(st) - 1):
        s, t = st[k]; s2 = st[k + 1][0]
        if s == s2: continue
        X, _ = E.evaluate(s); I = E.improving(s, X); h[len(I)] += 1
        Eg, W = wvals(g, s, t)
        ref += sum(1 for v, w in I if Eg.key(W[w]) > Eg.key(W[s[v]]) and s2[v] != w)
    print(f"{path.split('/')[-1]} n={n} Even moves={sum(h.values())} width histogram={dict(sorted(h.items()))} refused W-improving gated edges={ref}")
if __name__ == "__main__": main(*sys.argv[1:])
