#!/usr/bin/env python3
"""L-RED R199 CUBES: cube-and-conquer for r199/xbmc.py. Cubes = all move / stay patterns of the given movers at the given steps (complete
case split, so: every cube UNSAT => EXACT UNSAT; any cube SAT => genome). Runs J cubes in parallel, each with TMO; an UNKNOWN cube leaves
the answer UNKNOWN. Usage: cubes.py target.json aux steps(comma) movers(comma) J TMO prefix"""
import sys, os, json, itertools, subprocess, time
H = os.path.dirname(os.path.abspath(__file__))
tg, aux, steps, movers, J, TMO, pre = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3].split(",")], [int(x) for x in sys.argv[4].split(",")], int(sys.argv[5]), sys.argv[6], sys.argv[7]
lits = [(t, v) for t in steps for v in movers]; cubes = list(itertools.product((0, 1), repeat=len(lits)))
todo = list(enumerate(cubes)); run = {}; res = {}
while todo or run:
    while todo and len(run) < J:
        i, c = todo.pop(0); cube = ",".join(f"{t}:{v}:{b}" for (t, v), b in zip(lits, c))
        lf = f"{pre}_c{i}.log"; run[i] = (subprocess.Popen([sys.executable, os.path.join(H, "xbmc.py"), tg, aux, f"{pre}_c{i}.json"], env=dict(os.environ, CUBE=cube, TMO=TMO),
                                                         stdout=open(lf, "w"), stderr=subprocess.STDOUT), lf)
    time.sleep(5)
    for i in list(run):
        p, lf = run[i]
        if p.poll() is not None:
            out = open(lf).read(); r = "sat" if "-> sat" in out else "unsat" if "-> unsat" in out else "unknown"; res[i] = r; del run[i]
            print(f"cube {i}/{len(cubes)}: {r}", flush=True)
            if r == "sat":
                for q, _ in run.values(): q.kill()
                print("CUBES SAT (cube", i, ")", f"{pre}_c{i}.json"); sys.exit(0)
n = {k: sum(1 for v in res.values() if v == k) for k in ("unsat", "unknown")}
print("CUBES done:", n, "-> EXACT UNSAT" if n["unknown"] == 0 else "-> UNKNOWN (some cubes timed out)")
