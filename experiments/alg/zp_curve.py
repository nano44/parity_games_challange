#!/usr/bin/env python3
"""Evaluate an explicit tiled family: UNIT game tiled R = 1..RMAX times with template (step, edges) (zp_ladder2.build);
prints (R, n, ZP calls, plain Zielonka calls if n <= 40, time) and stops when a point exceeds --limit seconds.
Usage: zp_curve.py UNIT.jsonl 'STEP' 'EDGES_JSON' [--rmax 5] [--limit 900] [--write NAME]"""
import sys, os, json, time, signal
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import alglib, pg, zielonka, zp, zp_ladder2

unit = alglib.from_record(json.loads(open(sys.argv[1]).readline()))
step = int(sys.argv[2]); edges = [tuple(e) for e in json.loads(sys.argv[3])]
opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
rmax = int(opt("--rmax", 5)); limit = float(opt("--limit", 900)); name = opt("--write", "")
def alarm(s, f): raise TimeoutError()
signal.signal(signal.SIGALRM, alarm)
for R in range(1, rmax + 1):
    g = zp_ladder2.build(unit, (step, edges), R)
    if name:
        pg.write(g, os.path.join(HERE, "instances", f"{name}_R{R}_n{g.n}.pg"))
    t0 = time.time(); signal.alarm(int(limit))
    try:
        z = zp.ZP(g); win = z.run(); signal.alarm(0)
        assert win == zielonka.solve(g)
        print(f"R={R} n={g.n} m={g.m} d={len(set(g.prio))} ZP calls={z.calls} pruned={z.pruned} t={time.time()-t0:.1f}s", flush=True)
    except TimeoutError:
        print(f"R={R} n={g.n}: ZP did not finish in {limit:.0f}s (calls so far {z.calls if 'z' in dir() else '?'})", flush=True); break
