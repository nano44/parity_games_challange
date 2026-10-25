#!/usr/bin/env python3
"""REFEREE succ. 11: own-engine re-check of REFEREE-2's N-NEEDB-5 (R2-N5-NEEDB §5, referee-2 ef433d32): the CONJECTURE
"in scope, THR => M >= 0" on block_9501.pg from its saved start pair, and from SPEC S3's start. rl_engine / rl_probe only."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P
f = sys.argv[1]; g = RE.parse(f)
s0 = [9, 2, 9, 1, 0, 5, 2, 8, 3, 5, 7]; t0 = [9, 2, 9, 1, 0, 5, 2, 5, 0, 5, 3]
for label, start in (("saved start pair", (s0, t0)), ("SPEC S3 start", None)):
    orig = RE.best_reward_start
    if start: RE.best_reward_start = lambda h: ([start[0][v] if h.owner[v] == 0 else None for v in range(h.n)],
                                                [start[1][v] if h.owner[v] == 1 else None for v in range(h.n)])
    o, st = P.states(g); RE.best_reward_start = orig
    print("==", label, "| o", o, "| states", len(st), "| fallbacks", [k for k, a in enumerate(st) if a["fb"]])
    viol = 0
    for k, a in enumerate(st[:-1]):
        b = st[k + 1]
        inph = a["key"] == b["key"]; scope = inph and a["h"] and b["H2"] and a["W"][o] == b["W"][o]
        thr = a["h"] and a["Xi"][o] != a["W"][o]
        if not (a["fb"] and scope and thr): continue
        th, w = a["Xi"][o], a["W"][o]
        gates = [(y, z, P.lev(a["Xi"][a["s"][y]], a["Xi"][z])) for (y, z) in a["Is"]]
        r = a["r"]; M = a["M"]
        print(" k %d: (h) %s, theta %s, w %s, r %s, M %s, H2 at k+1 %s, w_{k+1} = w_k %s" % (k, a["h"], th, w, r, M, b["H2"], a["W"][o] == b["W"][o]))
        for (y, z, L) in gates:
            al = a["Xi"][y][0] == y and a["Xi"][a["s"][y]][0] == y and a["Xi"][a["s"][y]][1] == 0
            be = y in a["Rb"] and z in a["F"]
            print("   gate (%d, %d) level %s  y in R %s  z in F %s  kind %s" % (y, z, L, y in a["Rb"], z in a["F"], "(beta)" if be else ("(alpha)" if al else "other")))
        print("   rank o %d, cycle node c = %d rank %d" % (g.rank[o], w[0], g.rank[w[0]]))
        if r >= 0 and M < 0: viol += 1
    print(" in-scope THR fallbacks with r >= 0 and M < 0:", viol)
