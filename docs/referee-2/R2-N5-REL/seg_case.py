#!/usr/bin/env python3
"""REFEREE-2 succ. 19: per run S (fallback-free, in-phase): n, |S|, SEG, G(S), CF(S) for named instances (own; uses rel_check)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rel_check as RC
R = RC.R
for pgf in sys.argv[1:]:
    gp = R.pg.read(pgf); g, n = gp, gp.n
    stf = pgf[:-3] + ".start"
    s, t = R.read_start(gp, stf) if os.path.exists(stf) else R.starts(gp, 0, None)
    states, fbs = R.DC.Runner(gp).run(s, t)
    ctx = R.Ctx(gp); st = R.Stats()
    I = [R.state_info(ctx, a, b, st, "x") for a, b in states]
    for k in range(len(I)): I[k]["cW"] = RC.cycles(I[k]["wn"]); I[k]["cH"] = RC.cycles(I[k]["hn"])
    key = [(I[k]["lamX"], I[k]["tu"]) for k in range(len(I))]
    k0 = 0
    while k0 < len(I):
        k1 = k0
        while k1 + 1 < len(I) and key[k1 + 1] == key[k0] and not fbs[k1]: k1 += 1
        if k1 - k0 >= 5:
            sets = {bb: RC.rel_sets(g, I[bb], n) for bb in range(k0, k1 + 1)}
            segs, bk = 0, k1
            while bk >= k0:
                ak = bk
                while ak - 1 >= k0 and RC.admissible(I, ak - 1, bk, sets[bk]): ak -= 1
                segs += 1; bk = ak - 1
            odd2 = [u for u in range(n) if g.owner[u] == 1 and len(set(g.succ[u])) >= 2]
            G = sum(1 for k in range(k0, k1) if any(I[k]["hn"][u] != I[k + 1]["hn"][u] for u in odd2))
            print(os.path.basename(pgf), f"run [{k0},{k1}] n {n} |S| {k1 - k0} SEG {segs} G {G}")
        k0 = k1 + 1
