#!/usr/bin/env python3
"""Adapter: any solver that writes an Oink / PGSolver solution file ('paritysol N;' then 'v winner [strategy];') becomes a
battery engine. Usage: sol_adapter.py [--iter REGEX] [--steps REGEX] '<solver command with {in} and {out}>' GAME.pg
{in} is replaced by the game path, {out} by a temporary solution path (without {out} the solver's stdout is the solution).
--iter / --steps: a regular expression with one group, searched in the solver's stdout + stderr, e.g. --iter 'iterations (\\d+)'.
Example (L-COMP's second N5 implementation, which is NOT the battery's N5 row engine):
  sol_adapter.py --iter 'iterations (\\d+)' 'python3 -I experiments/n5-second/n5b.py {in} --mode spec {out}' GAME.pg"""
import sys, os, re, json, shlex, subprocess, tempfile
a = sys.argv[1:]; rx = {}
while a and a[0] in ("--iter", "--steps"): rx[a[0][2:]] = a[1]; a = a[2:]
cmd, game = a[0], a[1]
fd, sol = tempfile.mkstemp(suffix=".sol"); os.close(fd)
r = subprocess.run([x.replace("{in}", game).replace("{out}", sol) for x in shlex.split(cmd)], capture_output=True, text=True)
if r.returncode != 0: os.remove(sol); sys.exit("solver failed (exit %d): %s" % (r.returncode, (r.stdout + r.stderr)[-300:]))
text = open(sol).read() if "{out}" in cmd else r.stdout; os.remove(sol)
win, strat = {}, {}
for line in text.splitlines():
    p = line.strip().rstrip(";").split()
    if len(p) >= 2 and p[0].isdigit() and p[1] in ("0", "1"):
        win[int(p[0])] = int(p[1])
        if len(p) >= 3 and p[2].lstrip("-").isdigit() and int(p[2]) >= 0: strat[p[0]] = int(p[2])
if sorted(win) != list(range(len(win))): sys.exit("solution does not list every vertex 0..n-1")
def grab(k):
    m = re.search(rx[k], r.stdout + r.stderr) if k in rx else None
    return int(m.group(1)) if m else None
print(json.dumps({"winner": [win[v] for v in range(len(win))], "strategy": strat, "iterations": grab("iter"), "steps": grab("steps")}))
