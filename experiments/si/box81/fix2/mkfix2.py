#!/usr/bin/env python3
"""L-SI P-ACYC fixes entry 2: prints the entry to append to docs/si/P-ACYC-fixes.md (entry 1 = fix1/mkfix1.py's output, unchanged).
Asserts N-2's Old string occurs once in entry 1's F-3 (a) New text (whitespace normalised). Usage: mkfix2.py REPO_ROOT L3_SHA1 L3_BYTES [ENTRY1_FILE]   (default: docs/si/P-ACYC-fixes.md before entry 2 is appended)"""
import sys, os, re
R, S, B = sys.argv[1], sys.argv[2], sys.argv[3]
F = open(sys.argv[4] if len(sys.argv) > 4 else os.path.join(R, "docs", "si", "P-ACYC-fixes.md")).read()
assert "## Entry 2" not in F, "entry 2 already appended"
assert re.sub(r"\s+", " ", F).count("(its first N + 1 iterations)") == 1
sys.stdout.write(f"""
## Entry 2 (fix round 2; L-SI successor 44; Lead 03:06Z)
Items: REFEREE 28 §C (claude/referee c865da81): entry 1 CORRECT, L-2 MATCHES; AC-7 (optional) = REFEREE-2 N-2. REFEREE-2 32 Addendum 2
(claude/referee-2 d7ca68f4): entry 1 CORRECT, all statements SIGN; L-2 NOT YET on D-5 (required, one string); N-2 (recommended).
Line L-3 by experiments/si/box81/fix2/mkL3.py (asserts L-2's sha1 and the Old string once); this text by fix2/mkfix2.py.

### F-10 (D-5, required): the Γ3 clause names the tool of its τ test
- L-2 Old (once): «along N5′-xi on Γ3 from S3 (pacyc81.py),» New: «along N5′-xi on Γ3 from S3 (pacyc81.py; τ by fix1/pacyc81t.py),»
  (the Lead's routed form of REFEREE-2's plain-words variant). pacyc81.py is unchanged and counts σ only; the τ half of «states that are
  not standard (σ off the movers and τ) 0» is fix1/pacyc81t.py's taubad (F-5).

### F-11 (N-2 = AC-7, recommended, taken; packet text only): the header's parenthesis
- In F-3 (a)'s New header text, replace «(its first N + 1 iterations)» by «(at most N iterations; its first fallback comes by
  iteration N + 1)»: the mover phase has at most N iterations (Corollary ACYC-XI), and the first fallback is iteration T3 + 1 ≤ N + 1.

### Line L-3
docs/si/P-ACYC-line-L3.txt: sha1 {S}, {B} B = L-2 with F-10 only. L-1 and L-2 stay as they are.
""")
