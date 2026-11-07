#!/usr/bin/env python3
"""REFEREE-2 succ. 25: N5 (my R2-N5-LATEP loop) final regions vs Oink 8fbf0a7 --zlk (with -v verify). Usage: oink_pins.py OINK prefix list"""
import sys, os, subprocess, tempfile
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D + "/../R2-N5-LATEP"); sys.path.insert(0, D + "/../R2-N5-WRUN")
import latep_check as L, wrun_check as WR
oink, pre, lst = sys.argv[1:4]
for line in [l.split() for l in open(lst) if l.strip()]:
    g = L.pg.read(pre + line[0]); s, t, ok = WR.read_start(g, pre + line[1])
    states, fbs = L.DC.Runner(g).run(list(s), list(t), cap=5000)
    sg = states[-1][0]; E = L.Engine(g)
    xe, sb = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(g.n)))
    n5 = [0 if E.par[tuple(xe[v])[0]] == 0 else 1 for v in range(g.n)]
    with tempfile.NamedTemporaryFile(suffix=".sol") as f:
        r = subprocess.run([oink, "--zlk", "-v", pre + line[0], f.name], capture_output=True, text=True)
        sol = {}
        for l in open(f.name):
            p = l.replace(";", " ").split()
            if len(p) >= 2 and p[0].isdigit(): sol[int(p[0])] = int(p[1])
    ver = "verified" in (r.stdout + r.stderr).lower()
    same = all(sol.get(v) == n5[v] for v in range(g.n))
    print(line[0], "n", g.n, "start_ok", ok, "N5_iters", len(states) - 1, "oink_exit", r.returncode, "oink_verified", ver,
          "regions_equal", same, "evenwins", n5.count(0), flush=True)
