#!/usr/bin/env python3
"""REFEREE succ. 8: own engine's final regions (S5: Even wins v iff the cycle node of Xi_sigma(v) has even priority) against
Oink --zlk -p (pinned build tools/oink/build). Usage: rl_oink.py lib|named tmpdir"""
import sys, os, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P
ok = bad = 0
for f in (P.lib() if sys.argv[1] == "lib" else P.named()):
    g = RE.parse(f)
    st = RE.run(g)[-1]
    mine = [0 if g.prio[st["Xi"][v][0]] % 2 == 0 else 1 for v in range(g.n)]
    sol = os.path.join(sys.argv[2], "rl_oink.sol")
    subprocess.run([os.path.join(P.ROOT, "tools/oink/build/oink"), "--zlk", f, sol], capture_output=True, text=True, check=True)
    win = {}
    for l in open(sol):
        p = l.strip().rstrip(";").split()
        if len(p) >= 2 and p[0].isdigit(): win[int(p[0])] = int(p[1])
    if len(win) == g.n and all(win[v] == mine[v] for v in range(g.n)): ok += 1
    else: bad += 1; print("MISMATCH", f, len(win))
print("OINK_AGREE", ok, "MISMATCH", bad)
