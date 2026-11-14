#!/usr/bin/env python3
"""L-SI box 109: prints the table rows of docs/si/box109-design.md §3 from out/*.out (one row per family and rule):
| family | rule | args | iterations | fallbacks (sum) | wrong + badstrat + capped (sum) |
Usage: tab109.py   (run in experiments/si/box109)"""
import re, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
ORDER = ["spec", "xi", "h1", "h3", "howard", "h4", "nh", "rf", "rf2"]
for fam in ("gk", "wl", "du", "fr", "sae", "sbe", "ports"):
    rows = collections.OrderedDict()
    for line in open(os.path.join(HERE, "out", fam + ".out")):
        m = re.match(r"T109 (\w+) (\d+) mode (\w+) n (\d+) m (\d+) iterations (\d+) fallbacks (\d+) switches (\d+) capped (\d+) wrong (\d+) badstrat (\d+)", line)
        assert m, line
        f, a, mode = m.group(1), int(m.group(2)), m.group(3)
        rows.setdefault((f, mode), []).append((a, int(m.group(6)), int(m.group(7)), int(m.group(9)) + int(m.group(10)) + int(m.group(11))))
    for (f, mode) in sorted(rows, key=lambda k: (k[0], ORDER.index(k[1]))):
        r = sorted(rows[(f, mode)])
        print(f"| {f} | {mode} | {', '.join(str(x[0]) for x in r)} | {', '.join(str(x[1]) for x in r)} | {sum(x[2] for x in r)} | {sum(x[3] for x in r)} |")
