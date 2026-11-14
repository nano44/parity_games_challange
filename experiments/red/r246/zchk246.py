#!/usr/bin/env python3
"""L-RED 71 R246: winners of the scheme's run (own engine n5s237, mode spec / xi) against Oink (zlk and tl) on a game.
wrong_zlk / wrong_tl := number of vertices whose winner (SPEC S5: parity of the cycle node of Xi_sigma at the stop) differs from Oink's
solution file; must be 0. ZCHK246_CTRL=1 flips the engine's answer at vertex 0 (both must fire).
Usage: zchk246.py OINK MODE GAME.pg ..."""
import sys, os, subprocess, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "r237")]
import n5s237
oink, mode = sys.argv[1], sys.argv[2]
def oink_win(fn, flag):
    with tempfile.TemporaryDirectory() as td:
        sol = os.path.join(td, "o.sol")
        r = subprocess.run([oink, flag, "-v", fn, sol], capture_output=True, text=True)
        assert r.returncode == 0, (flag, r.returncode, r.stdout[-300:], r.stderr[-300:])
        w = {}
        for line in open(sol):
            p = line.strip().rstrip(";").split()
            if len(p) >= 2 and p[0].isdigit(): w[int(p[0])] = int(p[1])
        return w, ("verified" in r.stdout or "verified" in r.stderr)
for fn in sys.argv[3:]:
    prio, owner, succ = n5s237.parse(fn); it, fb, win, s, sb = n5s237.run(prio, owner, succ, mode)
    mine = [0 if e else 1 for e in win]
    if os.environ.get("ZCHK246_CTRL") == "1": mine[0] = 1 - mine[0]
    out = []
    for flag in ("--zlk", "--tl"):
        w, ver = oink_win(fn, flag); out.append(f"wrong_{flag[2:]} {sum(1 for v in range(len(prio)) if w.get(v) != mine[v])} oink_verified {int(ver)}")
    print("ZCHK246", os.path.basename(fn), "n", len(prio), "mode", mode, "its", it, "fb", fb, "even_wins", sum(win), " ".join(out), flush=True)
