#!/usr/bin/env python3
"""DTL (and idtl, tl for contrast) work counts on tc variants (tcvar.tc knobs) at N = 2..NMAX. Usage: tcvar_sweep.py [--nmax 10]"""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import tcvar, oink_fit, pg
nmax = int(sys.argv[sys.argv.index("--nmax") + 1]) if "--nmax" in sys.argv else 10
VARIANTS = [("plain", {}), ("dd", dict(dd=True)), ("lane1", dict(lane=1)), ("lane2", dict(lane=2)), ("lane3", dict(lane=3)),
            ("lane1_pr1", dict(lane=1, lane_pr=1)), ("lane2_pr1", dict(lane=2, lane_pr=1)), ("gates2", dict(gates=2)), ("gates3", dict(gates=3)),
            ("zshift2", dict(zshift=2)), ("zshift4", dict(zshift=4)), ("dd_lane2", dict(dd=True, lane=2)), ("gates2_zshift2", dict(gates=2, zshift=2)),
            ("lane2_zshift2", dict(lane=2, zshift=2)), ("tprio3", dict(tprio=3)), ("gap4", dict(hprio_gap=4))]
for name, kw in VARIANTS:
    row = []
    for N in range(2, nmax + 1):
        g = tcvar.tc(N, **kw); t0 = time.time()
        w = {s: oink_fit.work(g, s, raw=True, timeout=120) for s in ("dtl", "idtl", "tl")}
        row.append(f"N={N}(n={g.n}):dtl={w['dtl']} idtl={w['idtl']} tl={w['tl']}")
        if w["dtl"] >= 10**9 or time.time() - t0 > 100: break
    print(f"{name}: " + "  ".join(row), flush=True)
