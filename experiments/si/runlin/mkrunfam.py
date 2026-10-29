#!/usr/bin/env python3
"""L-SI box 24 (successor 20): the RUN-LIN kill family (docs/si/N5-RUNLIN-box24.md §7). Base: instances/runfam_base_n39 (= stretchiter
round 5 from best62_n34). Step: subdivide the two-way Even pair (25, last) by a new Even vertex x of priority 0 (25: last -> x,
last: 25 -> x, x: {25, last}); last := x. Start: sigma0 as in the base, a held edge 25->last or last->25 is redirected to x, sigma0(x) = Y
(env Y = "u" for 25 or "w" for last; default u). Prints n and the longest fallback-free run; writes OUT.pg / OUT.start.
Usage: mkrunfam.py K OUT"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from stretchall import run, sub
from growclimb import save
from common import load, readstart
K, out = int(sys.argv[1]), sys.argv[2]; Y = os.environ.get("Y", "u")
g = load(os.path.join(HERE, "instances", "runfam_base_n39.pg")); s0, t0 = readstart(os.path.join(HERE, "instances", "runfam_base_n39.start"))
U = 25; last = 38
for k in range(K):
    g, s0 = sub(g, s0, U, last, 0, U if Y == "u" else last); last = g.n - 1
save(out, g, [s0.get(v, t0.get(v)) for v in range(g.n)])
r = run(g, (s0, t0)); print("K %d n %d run %d run-2n %d" % (K, g.n, r, r - 2 * g.n))
