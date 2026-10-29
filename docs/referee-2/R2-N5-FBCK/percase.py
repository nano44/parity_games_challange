#!/usr/bin/env python3
"""REFEREE-2 succ. 19: per phase with fallbacks: n, n_K, f, |C_f|, |C^K_f| (own; for the packet's §2 (ii) / §3 / §4 instances)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND"))
import rund_check as R, fbck_check as F
for pgf in sys.argv[1:]:
    gp = R.pg.read(pgf); g, n = gp, gp.n
    st0 = pgf[:-3] + ".start"
    s, t = R.read_start(gp, st0) if os.path.exists(st0) else R.starts(gp, 0, None)
    states, fbs = R.DC.Runner(gp).run(s, t)
    E = R.DC.Engine(gp)
    K = F.frame_K(g); Q = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    lam = []; sb = []
    for sg, tu in states:
        vs, tf = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        lam.append(tuple(x[0] for x in vs)); sb.append(tf)
    key = [(lam[k], states[k][1]) for k in range(len(states))]
    k0 = 0
    while k0 < len(states):
        k1 = k0
        while k1 + 1 < len(states) and key[k1 + 1] == key[k0]: k1 += 1
        fb = [k for k in range(k0, k1) if fbs[k]]
        if fb:
            Cf = {tuple(sb[k][q] for q in Q) for k in fb}; CK = {tuple(sb[k][q] for q in Q if q in K) for k in fb}
            print(os.path.basename(pgf), f"phase [{k0},{k1}] n {n} n_K {len(K)} |Q| {len(Q)} |Q_K| {sum(1 for q in Q if q in K)} f {len(fb)} |C_f| {len(Cf)} |C^K_f| {len(CK)} bound n_K|C^K_f| {len(K) * len(CK)}")
        k0 = k1 + 1
