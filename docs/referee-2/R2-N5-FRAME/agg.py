#!/usr/bin/env python3
"""sum counters / max values over frame_check logs: agg.py log1 [log2 ...]"""
import sys
c, mx, res = {}, {}, []
for f in sys.argv[1:]:
    for l in open(f):
        l = l.strip()
        if l.startswith("max ") and ": " in l:
            k, v = l[4:].split(": "); mx[k] = max(mx.get(k, -1), int(v))
        elif l.startswith("RESULT"): res.append(l)
        elif ": " in l and not l.startswith(("MODE", "VIOLATION", "DONE", "WRUN", "STRETCH")):
            k, v = l.split(": ", 1)
            if v.isdigit(): c[k] = c.get(k, 0) + int(v)
print("logs", len(sys.argv) - 1, "RESULT lines", len(res), "all PASS" if res and all("PASS" in r for r in res) else res)
for k in sorted(c): print(f"{k}: {c[k]}")
for k in sorted(mx): print(f"max {k}: {mx[k]}")
