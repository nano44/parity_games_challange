#!/usr/bin/env python3
"""Oink's ptl / spptl / tl / dtl work counters on the 13 M1 families at growing sizes plus S_s and T_R (raw: no preprocessing).
Usage: ptl_sweep.py [--solvers ptl,spptl,tl,dtl] [--timeout 120]"""
import sys, os, subprocess, tempfile, shlex, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, strfam, oink_fit
from families import FAM
opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
solvers = opt("--solvers", "ptl,spptl,tl,dtl").split(","); timeout = float(opt("--timeout", 120))
SIZES = {"tc": [2, 4, 6, 8, 10, 12, 16, 20, 24, 32], "tc+": [2, 4, 6, 8, 10, 12, 16, 20], "counter_symsi": [2, 4, 8, 12, 16, 24, 32, 40],
         "counter_rr": [2, 4, 8, 12, 16, 24, 32, 40], "counter_dp": [2, 4, 8, 12, 16, 24, 32, 40], "counter_m": [2, 4, 8, 12, 16, 24, 32, 40],
         "counter_core": [2, 4, 8, 12, 16, 24, 32, 40], "counter_rob": [2, 4, 8, 12, 16, 24, 32], "counter_ortl": [2, 4, 8, 12, 16, 24, 32, 40],
         "counter_qpt": [2, 4, 8, 16, 32, 64, 128], "recursiveladder": [2, 4, 8, 12, 16, 24, 32, 40], "switchallexp": [1, 2, 4, 8, 16, 32],
         "switchbestexp": [1, 2, 4, 8, 16, 32]}
with tempfile.TemporaryDirectory() as td:
    fams = [(n, g, SIZES.get(n, s)) for (n, g, s, r) in FAM] + [("strfam", None, [2, 3, 4, 5, 6, 7, 8, 9]), ("T_R", None, [1, 2, 3, 4])]
    for name, gen, sizes in fams:
        for N in sizes:
            if name == "strfam": g = strfam.S(N)
            elif name == "T_R": g = pg.read(os.path.join(HERE, "instances", f"zp_tile8_R{N}_n{32*N}.pg"))
            else:
                gp = os.path.join(td, "g.pg")
                with open(gp, "w") as f: subprocess.run(shlex.split(gen.replace("{N}", str(N))), stdout=f, check=True, timeout=600)
                g = pg.read(gp)
            row = []
            for s in solvers:
                t0 = time.time(); w = oink_fit.work(g, s, raw=True, timeout=timeout); row.append(f"{s}={w if w < 10**9 else 'TIMEOUT'}({time.time()-t0:.1f}s)")
            print(f"{name} N={N} n={g.n} d={len(set(g.prio))}: " + " ".join(row), flush=True)
