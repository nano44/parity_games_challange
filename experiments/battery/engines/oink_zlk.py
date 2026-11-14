#!/usr/bin/env python3
"""Reference engine: Oink (pinned 8fbf0a7, tools/oink/build/oink) with --zlk, wrapped to the battery interface.
Usage: oink_zlk.py [--SOLVER] GAME.pg    (default --zlk; e.g. --tl, --npp) -> one JSON line."""
import sys, os, json, subprocess, tempfile, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
solver = next((x for x in sys.argv[1:] if x.startswith("--")), "--zlk"); game = sys.argv[-1]
fd, sol = tempfile.mkstemp(suffix=".sol"); os.close(fd)
r = subprocess.run([os.path.join(ROOT, "tools", "oink", "build", "oink"), solver, game, sol], capture_output=True, text=True)
if r.returncode != 0: sys.exit("oink %s failed (exit %d): %s" % (solver, r.returncode, (r.stdout + r.stderr)[-300:]))
win, strat = {}, {}
for line in open(sol):
    p = line.strip().rstrip(";").split()
    if len(p) >= 2 and p[0].isdigit():
        win[int(p[0])] = int(p[1])
        if len(p) >= 3: strat[p[0]] = int(p[2])
os.remove(sol)
it = re.search(r"solved with (\d+) iterations", r.stdout + r.stderr)
print(json.dumps({"winner": [win[v] for v in range(len(win))], "strategy": strat, "iterations": int(it.group(1)) if it else None, "steps": None}))
