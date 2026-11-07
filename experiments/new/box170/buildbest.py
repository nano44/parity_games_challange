#!/usr/bin/env python3
"""rebuild a tower1 best (assignment + gadget + start) as one genome and re-run it plainly. Usage: buildbest.py clock.json best.json out.json"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(H, "tower1.py")).read()
pre = src.split("V = copy.deepcopy(V0)")[0]
cf, bf, of = sys.argv[1], sys.argv[2], sys.argv[3]
B = json.load(open(bf)); vtmp = os.path.join(H, "out", "_v.json"); json.dump(B["V"], open(vtmp, "w"))
sys.argv = ["tower1.py", cf, vtmp, "0", "0", "0", "0"]
exec(pre)
assign = [tuple([a[0], tuple(a[1])]) if a[0] == "s" else tuple(a) for a in B["assign"]]
for s in list(seq): pass
G = build(B["V"], assign, B["vs"]); json.dump(G, open(of, "w")); os.remove(vtmp)
r = measure(G); x = NC + top
print("built", of, "N", G["N"], "T", r["T"], "top", x, "moves", r["mv"][x], "desc", r["desc"][x], "KF", r["kf"][x])
