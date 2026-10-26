#!/usr/bin/env python3
"""REFEREE-2 succ. 14: base ⊎ {u, x}: u Odd with successors {u, x}, x Odd forced to u; u ranked above x, so both of u's cycles (u self-loop,
u -> x -> u) have cycle node u: (h3_D) holds at u, u lies on its own honest cycle (so (NC) and (h_D) fail) once tau(u) != sbar(u).
Writes out.pg and, for each choice of tau(u), out_t<w>.start (S3 starts of the union with tau(u) := w). Usage: make_h3_union.py base.pg P out"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-N5-DUAL"))
import dual_check as DC
pg, Engine = DC.pg, DC.Engine
base, P, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
g = pg.read(base); n = g.n; u, x = n, n + 1
h = pg.Game(list(g.prio) + [P, 0], list(g.owner) + [1, 1], [list(s) for s in g.succ] + [[u, x], [u]])
open(out + ".pg", "w").write(pg.dumps(h))
s = list(Engine(h).initial("best")); t = list(Engine(DC.dual(h)).initial("best"))
for w in (u, x):
    t2 = list(t); t2[u] = w
    open(f"{out}_t{w}.start", "w").write("SIGMA0 " + " ".join(f"{v}:{s[v]}" for v in range(h.n) if h.owner[v] == 0) +
                                        "\nTAU0 " + " ".join(f"{v}:{t2[v]}" for v in range(h.n) if h.owner[v] == 1) + "\n")
print(out, "n", h.n, "u", u, "x", x)
