#!/usr/bin/env python3
"""Packet P-N5-END §1 + §6 quote check (record tool, not in check.sh: it needs git objects). Every «…» in docs/new/P-N5-END.md §1 and §6
must occur verbatim (whitespace normalised) in trunk docs/RESULTS.md, docs/new/N5-ssi-global.md, docs/new/P-N5-XICYC.md,
docs/new/P-N5-REACH.md or docs/new/P-N5-QUIET-fixes.md (the Lead's Γ3 scope sentence), EVERY source read from the trunk SHA by
git show (P-N5-END fixes entry 1, T-1, L-RED 58 R223); the packet itself is the lane's frozen file (sha1 asserted).
Usage, from the repo root: python3 experiments/new/box195/quotes_end.py TRUNK_SHA"""
import re, subprocess, sys
sha = sys.argv[1]
show = lambda path: subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True, check=True).stdout
norm = lambda t: re.sub(r"\s+", " ", t)
import hashlib
d = open("docs/new/P-N5-END.md", encoding="utf-8").read()
assert hashlib.sha1(d.encode()).hexdigest() == "5cae845b1da1a1c40b52e73da6edae3d6aadbf29", "frozen packet changed"
sec = d[d.index("## 1. Premises"):d.index("## 2. Facts")] + d[d.index("## 6. Theorems"):d.index("## 7. DATA")]
srcs = {"RESULTS": norm(show("docs/RESULTS.md")), "SPEC": norm(show("docs/new/N5-ssi-global.md")),
        "XICYC": norm(show("docs/new/P-N5-XICYC.md")), "REACH": norm(show("docs/new/P-N5-REACH.md")),
        "QFIX": norm(show("docs/new/P-N5-QUIET-fixes.md"))}
qs = re.findall(r"«(.*?)»", norm(sec)); miss = 0
for q in qs:
    hit = [k for k, v in srcs.items() if q in v]
    print(("OK   " + "/".join(hit)) if hit else "MISS", q[:100]); miss += not hit
print(f"quotes {len(qs)} missing {miss} (every source from trunk {sha})")
