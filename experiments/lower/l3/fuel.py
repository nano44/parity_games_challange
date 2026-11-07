#!/usr/bin/env python3
"""For each pi-change of mover x (pi_s_t(x) != pi_s_(t-1)(x)): the option b that became preferred, its chain under s_(t-1), and the
movers of that chain (other than x) that moved at step t (the cause of the rise, P-IDEAL-MOVES SEG-WINDOW (e) / AND-GATE (c)).
Usage: fuel.py g.json x [x ...]"""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sim import run, val
G = json.load(open(sys.argv[1])); S = run(G, G["start"]); N = G["N"]
def chain(s, x, k):
    out = []; y = G["opts"][x][k][1]
    while y >= 0: out.append(y); y = G["opts"][y][s[y]][1]
    return out
def pi(s, x): return max(range(2), key=lambda k: val(G, s, x, k))
for x in map(int, sys.argv[2:]):
    ev = []
    for t in range(1, len(S)):
        if pi(S[t], x) != pi(S[t - 1], x):
            b = pi(S[t], x); ch = chain(S[t - 1], x, b); mv = [y for y in ch if S[t][y] != S[t - 1][y]]
            ev.append(f"t{t}:->{b} via {mv}")
    print(f"x {x} (lev {G['lev'][x]}) targets {[o[1] for o in G['opts'][x]]}: " + "; ".join(ev))
