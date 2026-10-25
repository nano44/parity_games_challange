#!/usr/bin/env python3
"""Sum the counters of logs/*.txt (keys containing 'max', 'U1_last', 'run_len' are maxima) and count RESULT lines."""
import glob, re, sys, collections
tot = collections.Counter(); mx = {}; res = collections.Counter()
for f in sorted(glob.glob(sys.argv[1] if len(sys.argv) > 1 else "logs/*.txt")):
    for line in open(f):
        m = re.match(r"^(.+): (-?\d+)$", line.strip())
        if m and not line.startswith("example"):
            k, v = m.group(1), int(m.group(2))
            if "max" in k or k.startswith("U1_last") or "run_len" in k: mx[k] = max(mx.get(k, -999), v)
            else: tot[k] += v
        if line.startswith("RESULT"): res[line.split()[1]] += 1
for k in sorted(tot): print(k, tot[k])
for k in sorted(mx): print("MAX", k, mx[k])
print("RESULTS", dict(res))
