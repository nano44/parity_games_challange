#!/usr/bin/env python3
"""Box 195 §1 + §6 quote check (record tool, not in check.sh: it needs git objects). Every «…» in docs/new/N5-END-box195.md §1 and §6
must occur verbatim (whitespace normalised) in trunk docs/RESULTS.md, docs/new/N5-ssi-global.md, docs/new/P-N5-XICYC.md,
docs/new/P-N5-REACH.md or docs/new/P-N5-QUIET-fixes.md (the Lead's Γ3 scope sentence).
Usage, from the repo root: python3 experiments/new/box195/quotes195.py TRUNK_SHA"""
import re, subprocess, sys
sha = sys.argv[1]
show = lambda path: subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True, check=True).stdout
norm = lambda t: re.sub(r"\s+", " ", t)
d = open("docs/new/N5-END-box195.md").read()
sec = d[d.index("## 1. Premises"):d.index("## 2. Facts")] + d[d.index("## 6. Theorems"):d.index("## 7. What")]
srcs = {"RESULTS": norm(show("docs/RESULTS.md")), "SPEC": norm(open("docs/new/N5-ssi-global.md").read()),
        "XICYC": norm(open("docs/new/P-N5-XICYC.md").read()), "REACH": norm(open("docs/new/P-N5-REACH.md").read()),
        "QFIX": norm(open("docs/new/P-N5-QUIET-fixes.md").read())}
qs = re.findall(r"«(.*?)»", norm(sec)); miss = 0
for q in qs:
    hit = [k for k, v in srcs.items() if q in v]
    print(("OK   " + "/".join(hit)) if hit else "MISS", q[:100]); miss += not hit
print(f"quotes {len(qs)} missing {miss} (trunk {sha})")
