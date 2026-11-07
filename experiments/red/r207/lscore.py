#!/usr/bin/env python3
"""L-RED R207: print N, levels, degree profile, T (IDEAL run length under r187/ideal.py from the stored start) and the stop reason
for each genome file. Usage: lscore.py file.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal
for f in sys.argv[1:]:
    try: G = json.load(open(f)); S, why = ideal.traj(G, cap=200000)
    except Exception as e: print(f, "ERR", e); continue
    d = max(G["lev"]) + 1; two = sum(len(o) == 2 for o in G["opts"]); one = sum(len(o) == 1 for o in G["opts"])
    print(f"{os.path.basename(f):40s} d {d} N {G['N']} deg2 {two} deg1 {one} T {len(S) - 1} {why}")
