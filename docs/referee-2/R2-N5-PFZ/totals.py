#!/usr/bin/env python3
"""Sum the counters of logs/*.txt per trace (own | rand | spec; inst files and random batches separately). Maxima are maxima."""
import glob, os, re
from collections import Counter, defaultdict
tot = defaultdict(Counter); mx = defaultdict(Counter); files = Counter()
for p in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs", "*.txt"))):
    b = os.path.basename(p)
    grp = "t123" if b.startswith("t123") else ("random_" if b.startswith("rnd_") else "library_") + b.split("_")[1 if b.startswith("rnd_") else 0]
    files[grp] += 1
    for line in open(p):
        m = re.match(r"^([^:]+): (-?\d+)$", line.strip())
        if not m: continue
        k, v = m.group(1), int(m.group(2))
        if k.startswith("max_"): mx[grp][k] = max(mx[grp][k], v)
        else: tot[grp][k] += v
for g in sorted(files):
    print(f"## {g} ({files[g]} logs)")
    for k in sorted(tot[g]): print(f"  {k}: {tot[g][k]}")
    for k in sorted(mx[g]): print(f"  {k}: {mx[g][k]}")
