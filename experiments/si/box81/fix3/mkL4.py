#!/usr/bin/env python3
"""L-SI P-ACYC fixes entry 3: line L-4 = L-3 (docs/si/P-ACYC-line-L3.txt, sha1 03453361…) with the Lead's two replacements of 05:13Z
(R-G = Lead ruling G-7 / L41: the w* = K1 step is referee-originated; R-B = Lead ruling G-1: the source names the fixes entries and their
authors), R-G first, then R-B. Each Old string must occur exactly once. Prints L-4. Usage: mkL4.py REPO_ROOT"""
import sys, os, hashlib
R = sys.argv[1]; L3 = open(os.path.join(R, "docs", "si", "P-ACYC-line-L3.txt"), "rb").read()
assert hashlib.sha1(L3).hexdigest() == "03453361fead881493e2d2786b869f1c63158c4c", "L-3 changed"
L = L3.decode()
RG = ("not a TARGET.md claim); DATA (experiments/si/box81, check81.sh):",
      "not a TARGET.md claim); the step w* = K1 of LAMBDA-CONST's proof (σ̄(K2) toward K1 is Odd's unique optimum) is referee-originated "
      "(REFEREE R-P-ACYC §4.2 LC-1 and REFEREE-2 R2-P-ACYC G-1 / W-1, found independently, restated in P-ACYC's fixes entry 1 F-1), "
      "signed by both referees; DATA (experiments/si/box81, check81.sh):")
RB = ("(P-ACYC, docs/si/P-ACYC.md; L-SI successor 43)",
      "(P-ACYC, docs/si/P-ACYC.md with its fixes entries 1-2, docs/si/P-ACYC-fixes.md; L-SI successors 43-44)")
for old, new in (RG, RB):
    assert L.count(old) == 1, old
    L = L.replace(old, new)
assert L.count("(") == L.count(")") and "|" not in L
sys.stdout.write(L)
