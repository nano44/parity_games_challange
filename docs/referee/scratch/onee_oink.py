#!/usr/bin/env python3
"""REFEREE succ. 12: own Zielonka (onecheck.zielonka) vs Oink 8fbf0a7 --zlk (solution file, as rl_oink.py) on given .pg files.
Usage: onee_oink.py tmpdir files..."""
import sys, os, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, onecheck as OC
OINK = os.path.join(P.ROOT, "tools/oink/build/oink")
tmp = sys.argv[1]; sol = os.path.join(tmp, "onee_oink.sol")
for f in sys.argv[2:]:
    g = RE.parse(f); ZE, _ = OC.zielonka(g, set(range(g.n)))
    subprocess.run([OINK, "--zlk", f, sol], capture_output=True, text=True, check=True)
    win = {}
    for l in open(sol):
        p = l.strip().rstrip(";").split()
        if len(p) >= 2 and p[0].isdigit() and p[1] in ("0", "1"): win[int(p[0])] = int(p[1])
    oe = {v for v, w in win.items() if w == 0}
    print(os.path.relpath(f, P.ROOT), "n", g.n, "oink_vertices", len(win), "AGREE" if (oe == ZE and len(win) == g.n) else "DIFFER")
