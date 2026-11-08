#!/usr/bin/env python3
"""Packet P-N5-CHAIN §1 quote check (record tool, not in check.sh: it needs git objects). Every «…» in docs/new/P-N5-CHAIN.md §1 must
occur verbatim (whitespace normalised; a quote containing « … » is checked part by part) in a TRUNK source read by git show
(docs/RESULTS.md, docs/new/N5-ssi-global.md, docs/new/P-N5-XICYC.md, docs/new/P-N5-REACH.md) or in a LANE packet, whose sha1 is asserted
(docs/new/P-N5-END.md 5cae845b, docs/new/P-N5-ASC.md, docs/new/P-N5-QUIET.md, their fixes files). Nested «…» are read outermost.
Usage, from the repo root: python3 experiments/new/box196/quotes_chain.py TRUNK_SHA"""
import re, subprocess, sys, hashlib
sha = sys.argv[1]
show = lambda p: subprocess.run(["git", "show", f"{sha}:{p}"], capture_output=True, text=True, check=True).stdout
norm = lambda t: re.sub(r"\s+", " ", t)
d = open("docs/new/P-N5-CHAIN.md", encoding="utf-8").read(); sec = norm(d[d.index("## 1. Premises"):d.index("## 2. The model")])
srcs = {k: norm(show(p)) for k, p in (("RESULTS", "docs/RESULTS.md"), ("SPEC", "docs/new/N5-ssi-global.md"),
        ("XICYC", "docs/new/P-N5-XICYC.md"), ("REACH", "docs/new/P-N5-REACH.md"))}
lane = {"END": ("docs/new/P-N5-END.md", "5cae845b1da1a1c40b52e73da6edae3d6aadbf29"), "ASC": ("docs/new/P-N5-ASC.md", None),
        "QUIET": ("docs/new/P-N5-QUIET.md", None), "QFIX": ("docs/new/P-N5-QUIET-fixes.md", None), "AFIX": ("docs/new/P-N5-ASC-fixes.md", None)}
for k, (p, h) in lane.items():
    t = open(p, encoding="utf-8").read(); hh = hashlib.sha1(t.encode()).hexdigest()
    if h: assert hh == h, (p, hh)
    srcs["LANE-" + k] = norm(t); print(f"lane {p} sha1 {hh}")
qs = []; depth = 0; cur = ""                      # outermost «…» only
for ch in sec:
    if ch == "«":
        depth += 1
        if depth == 1: cur = ""; continue
    if ch == "»":
        depth -= 1
        if depth == 0: qs.append(cur); continue
    if depth >= 1: cur += ch
miss = 0
for q in qs:
    parts = [x.strip() for x in q.split("…") if x.strip()]
    hit = sorted({k for k, v in srcs.items() if all(x in v for x in parts)})
    print(("OK   " + "/".join(hit)) if hit else "MISS", q[:110]); miss += not hit
print(f"quotes {len(qs)} missing {miss} (trunk sources from {sha}; lane packets by sha1)")
