#!/usr/bin/env python3
"""L-RED 53 R215: per-iteration trace of N5'-xi (n5v.step @ acdbd28b): #Even switches, #Odd switches, #tie overrides (xi choice !=
SPEC's S4a choice), fallback flag, |Is|, |It|. Usage: trace.py GAME.pg [xi|spec]"""
import sys, os
WT = os.environ["WT"]
sys.path[:0] = [os.path.join(WT, "experiments/new/box190"), os.path.join(WT, "experiments/new/box21"), os.path.join(WT, "experiments/harness")]
import n5v, n5x, pg
from si import Engine
g = n5x.load(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else "xi"
E, Ed = Engine(g), Engine(n5v.dual(g)); s, t = n5x.start_pair(g, E, Ed, None); it = 0; tot = [0, 0, 0, 0]
while True:
    r = n5v.step(g, E, Ed, s, t, mode)
    if r is None: break
    ns, nt, Is, It, fb = r
    rs = n5v.step(g, E, Ed, s, t, "spec")
    ov = sum(1 for v in range(g.n) if g.owner[v] == 0 and ns[v] != rs[0][v]) if not fb else 0
    es = sum(a != b for a, b in zip(s, ns)); os_ = sum(a != b for a, b in zip(t, nt)); it += 1
    tot = [tot[0] + es, tot[1] + os_, tot[2] + ov, tot[3] + fb]
    print(f"{it:3d} Is {len(Is):3d} It {len(It):3d} Esw {es:3d} Osw {os_:3d} override {ov:3d} fb {fb}")
    s, t = ns, nt
print(f"TOTAL it {it} Esw {tot[0]} Osw {tot[1]} overrides {tot[2]} fallbacks {tot[3]}")
