#!/usr/bin/env python3
# Box 210 (L-NEW successor 72): every «…» quote on a line of docs/new/N5-GENLEVEL-box210.md marked «[Q]» (and its continuation lines up to
# the next bullet), whitespace-normalised, searched in trunk docs/RESULTS.md; prints the trunk line(s) where each quote's first 6 words occur.
# Usage (needs git objects): python3 quotes210.py TRUNK_SHA   (run from experiments/new/box210)
import sys, subprocess, re
raw = subprocess.run(["git", "show", sys.argv[1] + ":docs/RESULTS.md"], capture_output=True, text=True, check=True).stdout
res = " ".join(raw.split()); lines = [" ".join(l.split()) for l in raw.splitlines()]
doc = open("../../../docs/new/N5-GENLEVEL-box210.md", encoding="utf-8").read().splitlines()
blocks, cur = [], None
for l in doc:
    if l.lstrip().startswith("- "):
        if cur is not None: blocks.append(cur)
        cur = l if "[Q]" in l else None
    elif cur is not None and l.startswith("  "): cur += " " + l
    else:
        if cur is not None: blocks.append(cur)
        cur = None
if cur is not None: blocks.append(cur)
qs = [" ".join(q.split()) for b in blocks for q in re.findall(r"«([^«»]*)»", b)]
miss = 0
for q in qs:
    ok = q in res; miss += not ok; w = " ".join(q.split()[:6])
    print("quote", repr(q[:60]), "lines", [i + 1 for i, l in enumerate(lines) if w in l][:3], "found", ok)
print("quotes", len(qs), "missing", miss, "trunk", sys.argv[1])
