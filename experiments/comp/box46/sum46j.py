#!/usr/bin/env python3
"""L-COMP box 46, successor 22: summary of run46j.sh (L-NEW keymu213 / keyside215, unchanged, l-new cd4f7f4d) on box 46's genomes.
Must-0 counters as named in the tools' headers: keymu213 tau3 kp kpn muinc muflat mukappa; keyside215 lkp pkf pkfa kflip casc ftt ladder.
Per (tool, mode): rows, FAIL rows, the sum of each must-0 counter over all rows, the genomes where it is > 0, and the full row of the
target genome BEST_B3_WU151_NM163_e934d333.json. Usage: sum46j.py  (reads out/key46_*.out)"""
import os, re, glob
H = os.path.dirname(os.path.abspath(__file__)); TGT = "BEST_B3_WU151_NM163_e934d333.json"
MUST = {"keymu213": "tau3 kp kpn muinc muflat mukappa".split(), "keyside215": "lkp pkf pkfa kflip casc ftt ladder".split()}
for tool in ("keymu213", "keyside215"):
    for mode in ("spec", "xi", "ctrl1", "ctrl2"):
        p = os.path.join(H, "out", "key46_%s_%s.out" % (tool, mode))
        if not os.path.exists(p): continue
        L = [l.split() for l in open(p) if l.strip()]; fails = [l for l in L if l[0] == "FAIL"]; R = [l for l in L if l[0] != "FAIL"]
        tot = {k: 0 for k in MUST[tool]}; who = {k: [] for k in MUST[tool]}
        for l in R:
            for k in MUST[tool]:
                v = int(l[l.index(k) + 1]); tot[k] += v
                if v: who[k].append("%s:%d" % (l[0], v))
        print("%s %s: rows %d FAIL %d | must-0 sums %s" % (tool, mode, len(R), len(fails), " ".join("%s %d" % kv for kv in tot.items())))
        for k in MUST[tool]:
            if who[k]: print("    %s > 0 on %d genomes: %s" % (k, len(who[k]), " ".join(who[k][:6]) + (" ..." if len(who[k]) > 6 else "")))
        t = [l for l in R if l[0] == TGT]
        print("    target: %s" % (" ".join(t[0][1:]) if t else "MISSING"))
