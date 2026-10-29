#!/usr/bin/env python3
"""Box 17 cross-check, L-SI side (read-only use of L-SI's tools on trunk): for GAME [START] print one JSON line with L-SI's state
sequence, fallback flags, REL segments (lwp/seglast.segs), per-segment SEG-COUNT excess (lay/segsw.py's formula), SEG max
(grun/relseg.segcount), L-WAVE' max gap - (n - 1) (grun/lwave.maxgap, PMODE=1) and f per phase (root/common.phases + fb)."""
import json, os, sys
os.environ["PMODE"] = "1"; os.environ.pop("MODE", None)
HERE = os.path.dirname(os.path.abspath(__file__)); SI = os.path.join(HERE, "..", "si")
for p in ("grun", "lwp", "lay"):
    sys.path.insert(0, os.path.join(SI, p))
import seglast, lwave, relseg  # noqa: E402
from common import rows, load, readstart, phases  # noqa: E402
from trace import runs  # noqa: E402
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None
E, R = rows(g, st, cap=100000); n = g.n
segs = [(a, b) for a, b in seglast.segs(g, R)]
exc = []
for a, b in segs:
    if b <= a: continue
    sw = {v for t in range(a, b) for v in range(n) if g.owner[v] == 0 and R[t]["s"][v] != R[t + 1]["s"][v]}
    exc.append((a, b, (b - a) - len(sw)))
f = [(i, j, sum(R[k]["fb"] for k in range(i, j))) for i, j in phases(R)]
rr = [(s, e) for s, e, i, j in runs(R)]
print(json.dumps(dict(n=n, states=[[[R[k]["s"][v] for v in range(n) if g.owner[v] == 0], [R[k]["t"][v] for v in range(n) if g.owner[v] == 1]] for k in range(len(R))],
      fb=[R[k]["fb"] for k in range(len(R) - 1)], sb=[list(R[k]["sb"]) for k in range(len(R))], runs=rr, segs=segs, exc=exc,
      segmax=relseg.segcount(g, R), lwgap_minus_n1=lwave.maxgap(g, R), f=f)))
