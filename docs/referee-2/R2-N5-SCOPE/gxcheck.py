#!/usr/bin/env python3
"""REFEREE-2 succ. 8: validate my own GENERAL N5 (scope_check.run_general) against Oink --zlk (pinned 8fbf0a7): at termination Even wins
exactly where Xi(v) has an even cycle node. Usage: gxcheck.py file.pg ... (S3 start; deterministic and --rand)."""
import sys, os, subprocess, tempfile, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import scope_check as SC
RC = SC.RC; FC = SC.FC
OINK = os.path.join(HERE, "..", "..", "..", "tools", "oink", "build", "oink")
ok = bad = 0
for path in sys.argv[1:]:
    g = RC.parse(open(path).read())
    with tempfile.NamedTemporaryFile("w", suffix=".sol", delete=False) as tf: sol = tf.name
    subprocess.run([OINK, "--zlk", path, sol], capture_output=True, text=True)
    W0 = set()
    for line in open(sol):
        w = line.replace(";", " ").split()
        if len(w) >= 2 and w[0].isdigit() and w[1] in ("0", "1") and not line.startswith("paritysol"):
            if w[1] == "0": W0.add(int(w[0]))
    os.unlink(sol)
    for rand in (False, True):
        s, t = FC.s3_start(g); A, fbs = SC.run_general(g, s, t, random.Random(3), rand)
        mine = {v for v in range(g.n) if g.prio[A[-1]["Xi"][v][0]] % 2 == 0}
        if mine == W0 and not A[-1]["Is"] and not A[-1]["It"]: ok += 1
        else: bad += 1; print("MISMATCH", path, rand)
print("gxcheck ok", ok, "bad", bad)
