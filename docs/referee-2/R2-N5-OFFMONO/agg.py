#!/usr/bin/env python3
"""Sum the integer counters of offmono_check.py logs (every 'key: int' line); max lines listed per file."""
import sys, re, collections
tot = collections.Counter(); res = collections.Counter()
for f in sys.argv[1:]:
    for line in open(f):
        m = re.match(r"^([A-Za-z_0-9]+): (\d+)$", line.strip())
        if m: tot[m.group(1)] += int(m.group(2))
        if line.startswith("RESULT"): res[line.split()[1]] += 1
for k in sorted(tot): print(f"{k}: {tot[k]}")
print("RESULT lines:", dict(res))
