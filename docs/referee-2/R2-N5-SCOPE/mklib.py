#!/usr/bin/env python3
"""List every tracked experiments/**/*.pg that is C^1O (exactly one Odd vertex with out-degree > 1) with n <= 64. Inputs only."""
import subprocess, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-N5-RE"))
import re_check as RC
root = sys.argv[1]
fs = subprocess.run(["git", "-C", root, "ls-files", "experiments/*.pg"], capture_output=True, text=True).stdout.split()
for f in sorted(fs):
    try: g = RC.parse(open(os.path.join(root, f)).read())
    except Exception: continue
    if g.n > 64: continue
    if len([v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]) == 1: print(f)
