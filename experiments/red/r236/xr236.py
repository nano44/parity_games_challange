#!/usr/bin/env python3
"""L-RED 66 R236: n5x236 self-check on random games: regions vs harness Zielonka (must-0: regfail); iteration counts vs L-NEW's n5v
mode xi (env N5V=1 and LNEW = an archive of claude/l-new fcba92fc experiments/new + experiments/si/si.py; descriptive: cntdiff, the readings R1-R3 change tie-breaks). Usage: xr236.py SEED COUNT NMAX"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [HERE, os.path.join(ROOT, "experiments/harness")]
import n5x236, gen, zielonka
seed, cnt, nmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
tot = dict(games=0, regfail=0, cntdiff=0, maxit=0)
if os.environ.get("N5V") == "1":
    sys.path.insert(0, os.path.join(os.environ["LNEW"], "experiments/new/box190")); import n5v
for i in range(cnt):
    n = 2 + (i % (nmax - 1)); g = gen.random_game(n, max(2, n // 2), 1, 3, seed * 100000 + i)
    it, fb, win, s, sb = n5x236.run(list(g.prio), list(g.owner), [list(x) for x in g.succ])
    z = zielonka.solve(g); tot["games"] += 1; tot["maxit"] = max(tot["maxit"], it)
    if any((0 if win[v] else 1) != z[v] for v in range(n)): tot["regfail"] += 1
    if os.environ.get("N5V") == "1":
        st, fbs, _E = n5v.run(g, "xi"); tot["cntdiff"] += (len(st) - 1) != it; tot["fbdiff"] = tot.get("fbdiff", 0) + (fbs != fb)
print("TOTAL", tot, flush=True)
