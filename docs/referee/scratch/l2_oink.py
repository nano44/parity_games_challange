#!/usr/bin/env python3
"""REFEREE: N5's final regions (own trace, u1_probe) vs Oink --zlk -v (pinned 8fbf0a7); one Odd choice vertex asserted.
Usage: l2_oink.py game.pg ..."""
import sys, os, subprocess, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U
OINK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tools", "oink", "build", "oink")
for p in sys.argv[1:]:
    g = U.load(p); o = U.assert_c1o(g); E, Ed, out, it, fb = U.trace(g)
    Xi, _ = E.evaluate(out[-1][0]); n5win = [E.par[Xi[v][0]] for v in range(g.n)]   # 0 = Even wins
    with tempfile.TemporaryDirectory() as d:
        sol = os.path.join(d, "s.sol")
        r = subprocess.run([OINK, "--zlk", "-v", p, sol], capture_output=True, text=True)
        win = {}
        for line in open(sol):
            f = line.replace(";", " ").split()
            if len(f) >= 2 and f[0].isdigit(): win[int(f[0])] = int(f[1])
    ok = all(win[v] == n5win[v] for v in range(g.n))
    print(os.path.basename(p), "o", o, "iterations", it, "fallbacks", fb, "oink exit", r.returncode,
          "verified" if "verified" in (r.stdout + r.stderr).lower() else "NOT-VERIFIED", "regions", "AGREE" if ok else "DISAGREE")
