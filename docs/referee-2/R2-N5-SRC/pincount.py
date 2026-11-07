#!/usr/bin/env python3
"""REFEREE-2 successor 24: per-W-run one-vertex counts for the SRC pins, own code (my LATEP state loop; lane xcn.py not imported).
OWNFLIP(o): transitions of F at which sbar changes at Odd o with lambda_Xi(o) = o at k and at k + 1.  CN(c): switches of Even c in C.
Usage: pincount.py files list.txt 0"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-LATEP")); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-WRUN"))
import latep_check as L
import wrun_check as WR
def wrun(g, E, info, a, b, st, name, *rest):
    n = g.n; C = {v for v in range(n) if info[a]["lamW"][v] == v}; own = {}; cn = {}
    for k in range(a, b):
        A, B = info[k], info[k + 1]
        for o in range(n):
            if g.owner[o] == 1 and A["sbar"][o] != B["sbar"][o] and A["lam"][o] == o and B["lam"][o] == o: own[o] = own.get(o, 0) + 1
        for c in C:
            if g.owner[c] == 0 and A["sg"][c] != B["sg"][c]: cn[c] = cn.get(c, 0) + 1
    print("PIN", os.path.basename(name), "F", (a, b), "|F|", b - a, "OWNFLIP", own, "CN", cn, flush=True)
_orig = WR._orig_run_game
def run_game(g, s, t, st, name):
    o = L.wrun; L.wrun = wrun
    try: _orig(g, s, t, st, name)
    finally: L.wrun = o
L.run_game = run_game; L.read_start = WR.read_start
if __name__ == "__main__": L.main()
