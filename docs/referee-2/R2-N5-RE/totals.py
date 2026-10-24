#!/usr/bin/env python3
"""Sum the counters of re_check.py / sg_check.py logs given on the command line (max for PIECE_max_*)."""
import sys
from collections import Counter
c, m = Counter(), Counter()
for p in sys.argv[1:]:
    for line in open(p):
        if ": " not in line or line.startswith(("example", "VIOLATION", "RESULT")): continue
        k, v = line.rsplit(": ", 1)
        try: v = int(v)
        except ValueError: continue
        if k.startswith(("PIECE_max", "CR_last", "S_max", "XA_max")) or "_max" in k: m[k] = max(m[k], v)
        else: c[k] += v
for k in sorted(c): print(f"{k}: {c[k]}")
for k in sorted(m): print(f"{k}: {m[k]}")
