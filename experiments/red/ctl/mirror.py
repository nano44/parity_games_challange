#!/usr/bin/env python3
"""L-RED successor 26 (R111): is N5 on G^d the mirror of N5 on G? Runs n5b SPEC on (G, START) and (GD, DSTART) and checks
sigma_G = tau_GD and tau_G = sigma_GD at every state. Usage: mirror.py G.pg START GD.pg DSTART"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "n5-second"))
import n5b
def run(p, s):
    g = n5b.pg.read(p); s0, t0 = n5b.read_start(s, g); N = n5b.N5(g); N.mode = "spec"; tr = []; N.run(s0, t0, trace=tr); return g, tr
g, A = run(sys.argv[1], sys.argv[2]); gd, B = run(sys.argv[3], sys.argv[4])
own = lambda gg, x, p: tuple(y if gg.owner[v] == p else -1 for v, y in enumerate(x))
ok = len(A) == len(B) and all(own(g, sa, 0) == own(gd, tb, 1) and own(g, ta, 1) == own(gd, sb, 0) for (sa, ta), (sb, tb) in zip(A, B))
print(f"states {len(A)} {len(B)} mirror {ok}")
