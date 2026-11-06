#!/usr/bin/env python3
"""L-NEW box 175: gain' recomputed with L-RED's simulator r187/ideal.py (independent of box150 Gen). Usage: xgain.py LREDDIR files..."""
import os, sys, json, itertools
LR = sys.argv[1]; sys.path[:0] = [os.path.join(LR, "r187"), os.path.join(LR, "r178")]
import ideal
H = os.path.dirname(os.path.abspath(__file__))
g = {"__file__": os.path.join(H, "gain.py"), "__name__": "lib"}; exec(open(g["__file__"]).read().split("\nif __name__")[0], g)
for f in sys.argv[2:]:
    G = json.load(open(f)); tau, top, cp = g["couplings"](G); low = [x for x in range(G["N"]) if x not in top]
    S, _ = ideal.traj(G); res = []
    for choice in itertools.product(*[[-1] + low for _ in cp]):
        H_ = g["lower"](G, top, dict(zip(cp, choice)))
        if not g["acyc"](H_["N"], H_["opts"]): continue
        S2, _ = ideal.traj(H_); res.append((len(S2) - 1, choice))
    best = max(res)
    print("%s C %d couplings %s T(G) %d reroutings %d T(lower) values %s best %s gain' %d" % (os.path.basename(f), len(cp), cp, len(S) - 1,
          len(res), sorted(set(r[0] for r in res)), best, len(S) - 1 - best[0]))
