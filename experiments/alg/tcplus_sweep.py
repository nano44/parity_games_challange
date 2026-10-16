#!/usr/bin/env python3
"""DTL/idtl/tl work on tc+ variants (tcvar.tcplus knobs), N = 2..NMAX."""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import tcvar, oink_fit
nmax = int(sys.argv[sys.argv.index("--nmax") + 1]) if "--nmax" in sys.argv else 9
VARIANTS = [("plain+", {}), ("dd", dict(dd=True)), ("lane1", dict(lane=1)), ("lane2", dict(lane=2)), ("lane1_pr1", dict(lane=1, lane_pr=1)),
            ("gates2", dict(gates=2)), ("zshift-2", dict(zshift=-2)), ("zshift2", dict(zshift=2)), ("zk-2", dict(zk_shift=-2)), ("zk2", dict(zk_shift=2)),
            ("zk4", dict(zk_shift=4)), ("lane1_zk2", dict(lane=1, zk_shift=2)), ("dd_gates2", dict(dd=True, gates=2))]
for name, kw in VARIANTS:
    row = []
    for N in range(2, nmax + 1):
        g = tcvar.tcplus(N, **kw); t0 = time.time()
        w = {s: oink_fit.work(g, s, raw=True, timeout=120) for s in ("dtl", "idtl", "tl")}
        row.append(f"N={N}(n={g.n}):dtl={w['dtl']} idtl={w['idtl']} tl={w['tl']}")
        if w["dtl"] >= 10**9 or time.time() - t0 > 100: break
    print(f"{name}: " + "  ".join(row), flush=True)
