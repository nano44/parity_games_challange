#!/usr/bin/env python3
"""Run gaps.analyse on a list of instances (path[:start]) and print one row per instance: n, iterations, longest phase,
and for that phase: transitions, level drops, flat transitions, longest flat run, returns, E-violations."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gaps
for spec in sys.argv[1:]:
    p, _, s = spec.partition(":")
    t = time.time()
    r = gaps.analyse(p, s or None)
    ph = max(r["phases"], key=lambda q: q["trans"])
    viol = sum(q["E1"] + q["E2"] + q["E2o"] for q in r["phases"])
    tf = sum(q["flat"] for q in r["phases"]); td = sum(q["drops"] for q in r["phases"])
    print(f"{os.path.basename(p):24s} n={r['n']:3d} it={r['it']:4d} fb={r['fb']:3d} | longest phase trans={ph['trans']:3d} "
          f"drops={ph['drops']:4d} flat={ph['flat']:3d} flatrun={ph['flatrun']:3d} gmaxrun={ph['gmaxrun']:3d} returns={ph['returns']:3d}"
          f" | all phases flat={tf} drops={td} viol={viol} ({time.time()-t:.0f}s)", flush=True)
