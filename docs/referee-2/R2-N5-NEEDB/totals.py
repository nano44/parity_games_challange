#!/usr/bin/env python3
"""sum counters over logs (regex ^([^:]+): (-?\\d+)$); list violations and nonzero exits. Usage: totals.py logdir..."""
import sys, re, glob
from collections import Counter
for d in sys.argv[1:]:
    c = Counter(); bad = []; ex = []
    for p in glob.glob(d + "/*.log"):
        for line in open(p):
            line = line.rstrip("\n")
            m = re.match(r"^([^:]+): (-?\d+)$", line)
            if m: c[m.group(1)] += int(m.group(2))
            if line.startswith("VIOLATION "): bad.append(p + ": " + line)
            m2 = re.match(r"^(\S+) exit (\d+)$", line)
            if m2 and m2.group(2) != "0": ex.append(line)
    print(f"== {d}: {len(glob.glob(d + '/*.log'))} logs")
    for k, v in sorted(c.items()): print(f"{k}: {v}")
    print("nonzero exits:", len(ex), ex[:5]); print("violation lines:", len(bad)); [print(b) for b in bad[:10]]
