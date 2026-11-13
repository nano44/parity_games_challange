#!/usr/bin/env python3
"""REFEREE-2 40: second-engine cross-check of box 212's T_key (N5 itself from S3 on Γ3(G), steps before its first fallback, the lane's
rfd212 RFD_MODE spec, engine n5v). Own engine: REFEREE-2's R2-P-N5-END/r2end.run (SPEC S1-S5 + FIX 1-4 from the texts; successor 34),
mode spec, e-order lev (the lane's gamma3 order). F := the iteration of the first fallback in r2end's count. Prints per genome F, the
lane's T (by column name from `git show COMMIT:experiments/new/box212/out/<FILE>`) and F − T; the claim checked: F − T is one constant.
Usage: r2tkey.py COMMIT LANEFILE GENOME_FILES..."""
import sys, os, json, subprocess
from collections import defaultdict, Counter
sys.path.insert(0, os.path.join(os.environ["R2DIR"], "R2-P-N5-END"))
import r2end
com, lf = sys.argv[1], sys.argv[2]
lane = {}
for l in subprocess.run(["git", "show", f"{com}:experiments/new/box212/out/{lf}"], capture_output=True, text=True, check=True).stdout.splitlines():
    t = l.split()
    if "RFD_MODE" in t and t[t.index("RFD_MODE") + 1] == "spec": lane[t[0]] = int(t[t.index("T") + 1])
diffs = Counter(); C = defaultdict(int)
for fn in sys.argv[3:]:
    G = json.load(open(fn)); G = G.get("genome", G)
    it, F, g = r2end.run(G, "spec", "lev", C)
    nm = os.path.basename(fn); T = lane.get(nm)
    d = None if (F is None or T is None) else F - T; diffs[d] += 1
    print(nm, "F", F, "iterations", it, "laneT", T, "F-T", d, flush=True)
print("F-T distribution", dict(diffs), "| r2end must-0:", {k: v for k, v in C.items() if k.endswith("fail") or k in ("nofb", "multifb", "capped")})
