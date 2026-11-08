#!/usr/bin/env python3
"""L-SI P-ACYC fixes entry 3: prints the entry to append to docs/si/P-ACYC-fixes.md (entries 1-2 unchanged).
Usage: mkfix3.py REPO_ROOT L4_SHA1 L4_BYTES [ENTRIES12_FILE]   (default: docs/si/P-ACYC-fixes.md before entry 3 is appended)"""
import sys, os
R, S, B = sys.argv[1], sys.argv[2], sys.argv[3]
F = open(sys.argv[4] if len(sys.argv) > 4 else os.path.join(R, "docs", "si", "P-ACYC-fixes.md")).read()
assert "## Entry 2" in F and "## Entry 3" not in F
sys.stdout.write(f"""
## Entry 3 (CHECKER-class items on the R122 first fill, ruled in by the Lead 05:13Z; L-SI successor 45)
Items: the R122 first fill over L-3 (ff9b1639, sha1 03453361…) flags two FAIL-class items with CHECKER precedent (C135 E-1 / E-2 on R121).
Lead rulings (05:13Z): G-7 = L41 applies (the w* = K1 step of LAMBDA-CONST's proof is a REQUIRED referee-originated repair: REFEREE LC-1
and REFEREE-2 G-1 / W-1, found independently; restated in entry 1 F-1; the R119 precedent; AC-6 (F-9) is not L41's case); G-1 = the
source note must name the fixes entries and their author (C134 N-S / C135 E-1). G-4 is left to CHECKER. Line L-4 by
experiments/si/box81/fix3/mkL4.py (asserts L-3's sha1 and each Old string once, R-G first, then R-B); this text by fix3/mkfix3.py.
Citations checked against the reports: docs/referee/R-P-ACYC.md §4.2 «Lemma LAMBDA-CONST: SIGN WITH GAP LC-1»; docs/referee-2/R2-P-ACYC.md
§ «Lemma LAMBDA-CONST: SIGN WITH GAP (G-1; repair W-1)», and its Addendum 1 «REFEREE's LC-1 is my G-1».

### F-12 (G-7 = L41, required): the line names the referee-originated step
- L-3 Old (once): «not a TARGET.md claim); DATA (experiments/si/box81, check81.sh):» New: «not a TARGET.md claim); the step w* = K1 of
  LAMBDA-CONST's proof (σ̄(K2) toward K1 is Odd's unique optimum) is referee-originated (REFEREE R-P-ACYC §4.2 LC-1 and REFEREE-2
  R2-P-ACYC G-1 / W-1, found independently, restated in P-ACYC's fixes entry 1 F-1), signed by both referees; DATA (experiments/si/box81,
  check81.sh):»

### F-13 (G-1, required): the source note names the fixes entries and their authors
- L-3 Old (once): «(P-ACYC, docs/si/P-ACYC.md; L-SI successor 43)» New: «(P-ACYC, docs/si/P-ACYC.md with its fixes entries 1-2,
  docs/si/P-ACYC-fixes.md; L-SI successors 43-44)»

### Line L-4
docs/si/P-ACYC-line-L4.txt: sha1 {S}, {B} B = L-3 with F-12 then F-13 (the Lead's predicted sha1 and size, matched). L-1 to L-3 stay as they are.
""")
