#!/usr/bin/env python3
"""P-N5-QN §1 quote check (record tool, not in check.sh: it needs git objects). Every «…» in §1 must occur verbatim (whitespace
normalised) in trunk docs/RESULTS.md or in docs/new/P-N5-XICYC.md (the frozen packet RESULTS R118 cites). For each quote in RESULTS the
line number of the RESULTS entry (### Rnnn) holding it is printed.
Usage, from the repo root: python3 experiments/new/box203/quotesqn.py TRUNK_SHA"""
import re, subprocess, sys
sha = sys.argv[1]
res = subprocess.run(["git", "show", f"{sha}:docs/RESULTS.md"], capture_output=True, text=True, check=True).stdout
norm = lambda t: re.sub(r"\s+", " ", t)
p = open("docs/new/P-N5-QN.md", encoding="utf-8").read(); sec = p[p.index("## 1. Premises"):p.index("## 2. Theorem GATE-CLASS")]
xicyc = norm(open("docs/new/P-N5-XICYC.md", encoding="utf-8").read())
entries = []; cur = None
for i, line in enumerate(res.split("\n"), 1):
    m = re.match(r"### (R\d+) ", line)
    if m: cur = (m.group(1), i)
    entries.append((cur, line))
blocks = {}
for cur, line in entries:
    if cur: blocks.setdefault(cur, []).append(line)
nb = {k: norm("\n".join(v)) for k, v in blocks.items()}
qs = re.findall(r"«(.*?)»", norm(sec)); miss = 0
for q in qs:
    hit = [f"{k[0]} (l. {k[1]})" for k, v in nb.items() if q in v]
    if q in xicyc: hit.append("P-N5-XICYC")
    print(("OK   " + ", ".join(hit)) if hit else "MISS", q[:100]); miss += not hit
print(f"quotes {len(qs)} missing {miss} (trunk {sha})")
