#!/usr/bin/env python3
"""VR(x) := #{t : V_(s_t)(x) > V_(s_(t-1))(x)} on real IDEAL runs (V = current Xi-value, ENC integer). Screens CONJECTURE PMV:
VR(x) <= (deg(x)-1)(1 + desc(x)) (implies PM since every move raises V(x)). Usage: vr.py file.json ..."""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "..", "box165", "permover.py")).read().split("\nif __name__")[0])
files = 0; viol = 0; tight = 0; worst = (-99, None)
for f in sys.argv[1:]:
    try:
        G = json.load(open(f)); assert "N" in G; g = Gen(G); S, _ = g.run(G["start"])
    except Exception: continue
    files += 1; R = reach(G)
    for x in range(G["N"]):
        vr = sum(g.face(S[t], x, S[t][x]) > g.face(S[t - 1], x, S[t - 1][x]) for t in range(1, len(S)))
        b = (len(G["opts"][x]) - 1) * (1 + len(R[x])); ex = vr - b
        if ex > worst[0]: worst = (ex, (os.path.basename(f), x, len(R[x]), vr))
        if ex > 0:
            viol += 1
            if viol <= 5: print("VIOL", os.path.basename(f), "x", x, "deg", len(G["opts"][x]), "desc", len(R[x]), "VR", vr)
        tight += ex == 0
print("files", files, "PMV violations", viol, "tight movers", tight, "worst excess", worst)
