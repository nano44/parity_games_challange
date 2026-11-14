"""REFEREE successor 27: unit counts for the DATA-rule texts of R-P-TOWER-FUEL (own replay, tf_replay.R on t3r_sim).
E3 units = (step, doubling level) pairs; E5 levels with F(j-1) >= 1; DFa units = (consecutive-state pair, mover) with equal deciders."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tf_replay import load, R
e3 = e5h = lv = dfa = dfa_all = 0
for f in sys.argv[1:]:
    r = R(load(f))
    for t in range(1, r.T + 1):
        for x in range(r.N):
            dfa_all += 1; dfa += r.dec(r.S[t - 1], x) == r.dec(r.S[t], x)
    for j in range(1, r.d):
        if r.dbl[j]:
            lv += 1; e3 += r.T; e5h += r.F[j - 1] >= 1
print("doubling levels", lv, "E3 units (step, doubling level)", e3, "E5 levels with F(j-1)>=1", e5h,
      "DFa equal-decider (consecutive-state pair, mover)", dfa, "of", dfa_all)
