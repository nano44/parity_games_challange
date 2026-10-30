#!/usr/bin/env python3
"""Sum wchpk_*.txt (N5 and LZC halves of each GAME line)."""
import re, sys, ast
from collections import Counter
tot = {"N5": Counter(), "LZC": Counter()}; mx = {"N5": [0, 0.0], "LZC": [0, 0.0]}; bad = 0; games = 0
for fn in sys.argv[1:]:
    for line in open(fn):
        if not line.startswith("GAME"): continue
        games += 1
        for eng, part in (("N5", line.split(" LZC ")[0]), ("LZC", line.split(" LZC ")[1])):
            m = re.search(r"WCHPK \S+ n \d+ wruns (\d+) (\{.*?\}) max-ret-per-edge (\d+) max\|F\|/bound ([0-9.]+)", part)
            if not m: bad += 1; continue
            d = ast.literal_eval(m.group(2)); tot[eng].update(d); tot[eng]["wruns"] += int(m.group(1))
            mx[eng][0] = max(mx[eng][0], int(m.group(3))); mx[eng][1] = max(mx[eng][1], float(m.group(4)))
print("games", games, "unparsed halves", bad)
for e in tot: print(e, dict(tot[e]), "max-ret-per-edge", mx[e][0], "max |F|/bound", mx[e][1])
