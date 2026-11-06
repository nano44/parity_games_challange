#!/usr/bin/env python3
"""L-NEW box 184: RELAY-FREE test. For every non-ISO L^R_d genome file (d 3, 4) and every q in {0,1}^2, the frozen genome G_q (movers 0,
1 restricted to their options q, everything else unchanged, as in NONISO-FRAME): max over all starts with q at 0, 1 of T(G_q). Compared
with T_0(d - 1) (EXACT 4 at d 3 = m 2; at d 4 the lower bound 8). Usage: relayfree.py files..."""
import os, sys, json, itertools, copy
H = os.path.dirname(os.path.abspath(__file__)); P0 = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P0, "__name__": "lib"}; exec(open(P0).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
fl = {"__file__": os.path.join(H, "..", "box162", "flipcheck.py"), "__name__": "lib"}; exec(open(fl["__file__"]).read().split("\nif __name__")[0], fl)
T0 = {3: 4, 4: 8}; best = {}; cnt = {}
for f in sys.argv[1:]:
    try: G = json.load(open(f)); assert fl["is_lr"](G) and not fl["is_iso"](G) and G["N"] // 2 in T0
    except Exception: continue
    d = G["N"] // 2
    for q in itertools.product((0, 1), repeat=2):
        F = copy.deepcopy(G)
        for z in (0, 1):
            F["opts"][z] = [G["opts"][z][q[z]]]; F["gate"][z] = [G["gate"][z][q[z]]]
        g = Gen(F); m = 0
        for u in itertools.product((0, 1), repeat=G["N"] - 2):
            S, _ = g.run((0, 0) + u); m = max(m, len(S) - 1)
        cnt[d] = cnt.get(d, 0) + 1
        if m > best.get(d, (-1,))[0]: best[d] = (m, os.path.basename(f), q)
for d in sorted(best): print("d %d: frozen non-ISO frames %d, max T %d (T_0(%d) %s %d) at %s q %s" % (d, cnt[d], best[d][0], d - 1, "=" if d == 3 else ">=", T0[d], best[d][1], best[d][2]))
