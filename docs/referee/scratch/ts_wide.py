#!/usr/bin/env python3
"""REFEREE succ. 17 (TOPSHAPE §C, N-TS-1): TOP-SHAPE (a), (b) and the strict weight rise at EVERY N5 transition (phase-leaving included) at which
v's cycle node is unchanged and P(Xi v) changes. Own engine. Usage: ts_wide.py files..."""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, core_probe as CP
cnt = Counter()
for path in sys.argv[1:]:
    if path.endswith(".start"): continue
    g = RE.parse(path)
    if g.n > 48: continue
    even = lambda r: g.prio[g.byrank[r]] % 2 == 0
    sp = path[:-3] + ".start"
    starts = ([CP.parse_start(g, sp)] if os.path.exists(sp) else []) + [RE.best_reward_start(g)]
    for s0 in starts:
        if s0 is None: continue
        st = RE.run(g, s0)
        for t in range(len(st) - 1):
            x0, x1 = st[t], st[t + 1]
            inph = x0["t"] == x1["t"] and [v[0] for v in x0["Xi"]] == [v[0] for v in x1["Xi"]]
            for v in range(g.n):
                (c0, A, _), (c1, B, _) = x0["Xi"][v], x1["Xi"][v]
                if c0 != c1 or A == B or inph: continue
                cnt["OFFPHASE_Pchg_same_c"] += 1
                if not g.weight(B) > g.weight(A): cnt["STRICT_FAIL"] += 1
                t0, t1 = A.bit_length() - 1, B.bit_length() - 1
                if t1 > t0 and not even(t1): cnt["A_FAIL"] += 1
                if t0 >= 0 and even(t0) and t1 < t0: cnt["B_FAIL"] += 1
for k in sorted(cnt): print(k, cnt[k])
