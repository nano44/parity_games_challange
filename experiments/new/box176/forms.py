#!/usr/bin/env python3
"""L-NEW box 176: test repaired TOP-C forms on genomes (degree <= 2, stored start). n2 := #two-option top movers (TOP-ADD's constant).
 FA: gain' <= n2 + C        (TOP-C with TOP-ADD's exact constant)
 FB: gain' <= n2 + mc       (one step per change of a coupled top mover = per proxy change)
 FC: gain' <= n2 + c * mc   reports the smallest c that fits each file: (gain' - n2) / mc
 FD: gain' <= n2 + sum over couplings of (1 + moves of its target)
Usage: forms.py files..."""
import os, sys, json, itertools
H = os.path.dirname(os.path.abspath(__file__))
r = {"__file__": os.path.join(H, "repair.py"), "__name__": "lib"}; exec(open(r["__file__"]).read().split("\nif __name__")[0], r)
g = r["g"]; Gen = g["Gen"]; C_ = dict(files=0, FA=0, FB=0, FD=0); worst = []
for f in sys.argv[1:]:
    try: G = json.load(open(f)); assert "opts" in G and "start" in G and max(len(o) for o in G["opts"]) <= 2
    except Exception: continue
    try: M = r["metrics"](G)
    except Exception: continue
    if not M: continue
    tau, top, cp = g["couplings"](G); n2 = sum(1 for u in top if len(G["opts"][u]) == 2)
    S, _ = Gen(G).run(G["start"]); T = len(S) - 1
    mv = {u: sum(1 for t in range(1, T + 1) if S[t][u] != S[t - 1][u]) for u in top}
    fd = n2 + sum(1 + mv[G["opts"][x][k][1]] for x, k in cp)
    C_["files"] += 1; gp = M["gain"]
    if gp > fd: print("FD-VIOL", os.path.basename(f), "gain", gp, "n2", n2, "bound", fd, "C", M["C"], "moves", mv, "T", T)
    C_["FA"] += gp > n2 + M["C"]; C_["FB"] += gp > n2 + M["mc"]; C_["FD"] += gp > fd
    if M["mc"]: worst.append(((gp - n2) / M["mc"], os.path.basename(f), gp, n2, M["mc"], M["C"], T))
print(" ".join("%s %d" % kv for kv in C_.items()))
worst.sort(reverse=True); print("largest (gain'-n2)/mc:", worst[:6])
