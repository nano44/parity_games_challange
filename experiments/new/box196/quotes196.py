#!/usr/bin/env python3
"""Box 196 record tool (needs git objects; run from the repo root): python3 experiments/new/box196/quotes196.py TRUNK_SHA
Extracts Lemma ESC3 (P-N5-REACH §6.5) and Lemma W3 (§6.6) VERBATIM from trunk's docs/new/P-N5-REACH.md (the packet RESULTS R117 lands),
splits them into steps (one per sentence or bullet), and flags every token through which a step could use the Xi-graph:
  'Ξ', 'xt(', 'X-chain', 'PLAY3', 'SBAR3', 'KEY3', 'Fact X', 'acycl', 'ACYC', 'β_g →', '→ β'.
Also prints R117's and R118's labels of ESC3 / W3 (verbatim, from trunk docs/RESULTS.md). Output: each step with its flags; box 196 §2
reads every flagged step by hand."""
import re, subprocess, sys
sha = sys.argv[1]
show = lambda p: subprocess.run(["git", "show", f"{sha}:{p}"], capture_output=True, text=True, check=True).stdout
R = show("docs/new/P-N5-REACH.md"); RES = show("docs/RESULTS.md")
TOK = ["Ξ", "xt(", "X-chain", "PLAY3", "SBAR3", "KEY3", "Fact X", "acycl", "ACYC", "β_g →", "→ β"]
for name, a, b in (("ESC3", "### 6.5 Lemma ESC3", "### 6.6 Lemma W3"), ("W3", "### 6.6 Lemma W3", "### 6.7 Lemma KEY3")):
    sec = R[R.index(a):R.index(b)]; flat = " ".join(sec.split())
    steps = [s.strip() for s in re.split(r"(?<=[.;∎])\s+(?=[A-Z(-])|\s+- ", flat) if s.strip()]
    print(f"== {name}: {len(steps)} steps, {len(flat)} chars, verbatim from trunk {sha} docs/new/P-N5-REACH.md")
    for i, s in enumerate(steps, 1):
        hits = [t for t in TOK if t in s]
        print(f"{name}.{i} [{','.join(hits) if hits else '-'}] {s}")
for q in ("[IDEAL-ACYC; K3 and TAU3 every genome]", "RESULTS R117's entry signs S3-START, PAD, K3 and TAU3 for every genome and ESC3, W3 for acyclic Ξ-graphs",
          "P-N5-XICYC §7 reads ESC3's and W3's proofs for every genome"):
    print(("OK   " if q in " ".join(RES.split()) else "MISS ") + q)
