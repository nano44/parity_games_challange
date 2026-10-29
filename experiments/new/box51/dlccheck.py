#!/usr/bin/env python3
"""L-NEW box 51: check Proposition DLC on DLC_d (vcgad.py d): the N5 run (n5x via common.rows) is ONE phase (lambda_Xi, tau constant) of
2^(d+1) - 1 transitions, no fallback, |D| = 0; n = 1 + 2^d (2^(d+1) - 2 - d) + 2d + 2^(d+1) - 2; at every state t >= 1, x_i is on hA_i iff
bit i+1 of t - 1 is 1 (x_0 at state 0 on hB_0, the S3 tie to the larger index); the d edges (x_i, hA_i) are shattered (2^d traces),
and the phase VC (vcrun.vc) is printed. Usage: dlccheck.py d"""
import sys, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root")); sys.path.insert(0, os.path.join(HERE, "..", "box50"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "runlin"))
from common import rows, load, phases, Dset
from vcrun import vc
d = int(sys.argv[1]); f = os.path.join(HERE, "out", "dlc_d%d.pg" % d)
open(f, "w").write(subprocess.run([sys.executable, "-I", os.path.join(HERE, "vcgad.py"), str(d)], capture_output=True, text=True).stdout)
g = load(f); E, R = rows(g); n = g.n; T = 1 << d; bad = []
nexp = 1 + T * (2 * T - 2 - d) + 2 * d + 2 * T - 2
xs = [v for v in range(n) if sorted(set(g.succ[v])) == [v + 1, v + 2] and all(0 in g.succ[w] and g.prio[w] == 0 for w in (v + 1, v + 2))]
if n != nexp: bad.append(("n", n, nexp))
if len(xs) != d: bad.append(("gadgets", len(xs)))
P = list(phases(R))
if P != [(0, len(R) - 1)] or len(R) - 1 != 2 * T - 1: bad.append(("phase", P, len(R) - 1))
if any(A["fb"] for A in R): bad.append("fallback")
if any(Dset(g, A) for A in R) or any(g.owner[v] for v in range(n)): bad.append("D or Odd vertex")
for i, x in enumerate(xs):
    hA = x + 1
    for t, A in enumerate(R):
        want = (t >= 1 and ((t - 1) >> (i + 1)) & 1 == 1)
        if (A["s"][x] == hA) != want: bad.append(("trace", i, t)); break
pat = {tuple(A["s"][x] == x + 1 for x in xs) for A in R}
ev = [v for v in range(n) if g.owner[v] == 0 and len(set(g.succ[v])) >= 2]
dv = vc([frozenset((v, A["s"][v]) for v in ev) for A in R])[0]
print("DLC d=%d n=%d len=%d traces on the %d x-edges=%d phase_VC=%d" % (d, n, len(R) - 1, d, len(pat), dv), "DLC PASS" if not bad and len(pat) == T else "DLC FAIL %r" % bad[:5])
