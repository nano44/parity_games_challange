#!/usr/bin/env python3
"""P-N5-QUIET §1 quote check (record tool, not in check.sh: it needs git objects). Every «…» in §1 must occur verbatim (whitespace
normalised) in trunk docs/RESULTS.md, docs/new/P-N5-XICYC.md, trunk docs/red/P-N5-REALIZE.md, or docs/new/P-N5-ASC.md + its line L-1.
Usage, from the repo root: python3 experiments/new/box194/quotes194.py TRUNK_SHA"""
import re, subprocess, sys
sha = sys.argv[1]
show = lambda path: subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True, check=True).stdout
norm = lambda t: re.sub(r"\s+", " ", t)
p = open("docs/new/P-N5-QUIET.md").read(); sec = p[p.index("## 1. Premises"):p.index("## 2. Lemma CN2")]
srcs = {"RESULTS": norm(show("docs/RESULTS.md")), "XICYC": norm(open("docs/new/P-N5-XICYC.md").read()),
        "REALIZE": norm(show("docs/red/P-N5-REALIZE.md")),
        "ASC": norm(open("docs/new/P-N5-ASC.md").read() + open("docs/new/P-N5-ASC-line-L1.txt").read())}
qs = re.findall(r"«(.*?)»", norm(sec)); miss = 0
for q in qs:
    hit = [k for k, v in srcs.items() if q in v]
    print(("OK   " + "/".join(hit)) if hit else "MISS", q[:100]); miss += not hit
print(f"quotes {len(qs)} missing {miss} (trunk {sha})")
