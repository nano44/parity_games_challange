#!/usr/bin/env python3
"""REFEREE-2 succ. 17: longest fallback-free S4a run inside one phase (own SPEC loop), per game of a list, S3 start. Usage: s4a_runs.py list"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND"))
import rund_check as R
DC = R.DC
out = []
for path in [l.strip() for l in open(sys.argv[1]) if l.strip()]:
    gp = R.pg.read(os.path.join(DC.ROOT, path))
    if gp.n > 70: continue
    s, t = R.starts(gp, 0, None)
    states, fbs = DC.Runner(gp).run(s, t)
    ctx = R.Ctx(gp); st = R.Stats()
    I = [R.state_info(ctx, a, b, st, "x") for a, b in states]
    key = [(I[k]["lamX"], tuple(I[k]["tu"])) for k in range(len(I))]
    best = 0; k = 0
    while k < len(I) - 1:
        e = k
        while e < len(I) - 1 and key[e + 1] == key[k] and not fbs[e]: e += 1
        best = max(best, e - k); k = e + 1 if e > k else k + 1
    out.append((best, gp.n, path))
for b, n, p in sorted(out, reverse=True)[:15]: print(b, n, p)
