#!/usr/bin/env python3
"""REFEREE-2 succ. 7: validate my own N5 (frz_check.run_n5) against Oink --zlk: at termination, Even wins exactly where W(v) has an even
cycle node (Xi = W at the end). Usage: oink_xcheck.py file.pg ... (each file: S3 start, deterministic and --rand)."""
import sys, os, subprocess, tempfile, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import frz_check as FC
RC = FC.RC
OINK = os.path.join(HERE, "..", "..", "..", "tools", "oink", "build", "oink")
ok = bad = 0
for path in sys.argv[1:]:
    g = RC.parse(open(path).read()); o = FC.odd_vertex(g)
    with tempfile.NamedTemporaryFile("w", suffix=".sol", delete=False) as tf: sol = tf.name
    r = subprocess.run([OINK, "--zlk", "-v", path, sol], capture_output=True, text=True)
    W0 = set()
    for line in open(sol):
        w = line.replace(";", " ").split()
        if len(w) >= 2 and w[0].isdigit() and w[1] in ("0", "1") and line.strip() and not line.startswith("paritysol"):
            if w[1] == "0": W0.add(int(w[0]))
    os.unlink(sol)
    for rand in (False, True):
        rng = random.Random(3)
        s, t = FC.s3_start(g)
        A, fbs = FC.run_n5(g, o, s, t, rng, rand)
        S = A[-1]
        mine = {v for v in range(g.n) if g.prio[S.W[v][0]] % 2 == 0}
        if mine == W0 and S.Xi == S.W: ok += 1
        else: bad += 1; print("MISMATCH", path, rand)
print("oink_xcheck ok", ok, "bad", bad)
