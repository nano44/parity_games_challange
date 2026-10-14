#!/usr/bin/env python3
"""Comparison only (not used for the verdict): REFEREE-2's psolB / psolQ / PA** against L-ATTR's psolb.py, psolq.py and
peeling.pa2 (claude/l-attr d5d6396) on the same games.  Usage: compare_lane.py <path to a checkout of experiments/> n K seed"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r2lib import *
lane = sys.argv[1]
sys.path.insert(0, os.path.join(lane, "attr")); sys.path.insert(0, os.path.join(lane, "harness"))
import pg as lpg, peeling as lpeel
from psolb import PsolB
from psolq import PsolQ
n, K, seed = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
rnd = random.Random(seed)
games = list(all_games(n)) if K == 0 else [random_game(rnd, n, n, [1, 2, 3]) for _ in range(K)]
dB = dQ = dP = 0
for g in games:
    lg = lpg.Game(g.pr, g.owner, g.succ)
    WE, WO = zielonka(g)
    ref = [0 if v in WE else 1 for v in range(g.n)]
    _, _, resB, _ = PsolB(lg).run()
    _, _, resQ, _ = PsolQ(lg).run()
    lp = lpeel.both(lg, ref, lpeel.pa2)
    mB, mQ, mP = psolB_hkp(g)[1], psolQ_hkp(g)[1], pa2(g, WE, WO)
    if set(resB) != set(mB):
        dB += 1; print("psolB residual differs:", g.oneline(), sorted(resB), sorted(mB))
    if set(resQ) != set(mQ):
        dQ += 1; print("psolQ residual differs:", g.oneline(), sorted(resQ), sorted(mQ))
    if lp != mP:
        dP += 1; print("PA** differs:", g.oneline(), lp, mP)
print(f"compared {len(games)} games (n={n}, {'exhaustive' if K == 0 else 'random seed %d' % seed}): psolB residual differs on {dB}, psolQ on {dQ}, PA** on {dP}")
