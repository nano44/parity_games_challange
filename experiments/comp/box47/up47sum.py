#!/usr/bin/env python3
"""L-COMP box 47: summary of the upward-ladder multi-start (run47e.sh; out/up/U<d>_<r>.log, SCORE=KR): per depth d, runs finished (DONE) /
started, the best k_A6 and its T, and how many runs reached that k; the best genome's file. Usage: up47sum.py"""
import os, glob, re
H = os.path.dirname(os.path.abspath(__file__)); by = {}
for f in glob.glob(os.path.join(H, "out", "up", "U*_*.log")):
    d = int(re.match(r"U(\d+)_", os.path.basename(f)).group(1)); L = open(f).read().splitlines()
    dn = [l for l in L if l.startswith("DONE")]; b = by.setdefault(d, dict(runs=0, done=0, best=(-1, -1), at=None, nk={}))
    b["runs"] += 1
    if not dn: continue
    b["done"] += 1; m = re.search(r"\(k (\d+) T (\d+)\)", dn[0]); k, T = int(m.group(1)), int(m.group(2)); b["nk"][k] = b["nk"].get(k, 0) + 1
    if (k, T) > b["best"]: b["best"] = (k, T); b["at"] = os.path.basename(f)
for d in sorted(by):
    b = by[d]; print("d %d (N %d, M %d): runs %d done %d | best k_A6 %d T %d (%s) | runs per final k: %s" % (d, 2 * d, 4 * d, b["runs"], b["done"], b["best"][0], b["best"][1], b["at"], " ".join("k%d:%d" % kv for kv in sorted(b["nk"].items()))))
