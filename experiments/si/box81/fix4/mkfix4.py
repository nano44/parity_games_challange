#!/usr/bin/env python3
"""L-SI P-ACYC fixes entry 4: prints the entry to append to docs/si/P-ACYC-fixes.md (entries 1-3 unchanged).
Usage: mkfix4.py REPO_ROOT L5_SHA1 L5_BYTES [ENTRIES123_FILE]   (default: docs/si/P-ACYC-fixes.md before entry 4 is appended)"""
import sys, os
R, S, B = sys.argv[1], sys.argv[2], sys.argv[3]
F = open(sys.argv[4] if len(sys.argv) > 4 else os.path.join(R, "docs", "si", "P-ACYC-fixes.md")).read()
assert "## Entry 3" in F and "## Entry 4" not in F
sys.stdout.write(f"""
## Entry 4 (CHECKER C136 FAIL E-1, E-2 on the R122 second fill; line-only; routed by the Lead 15:52Z; L-SI successor 46)
Source: CHECKER successor 22, docs/checker/C136.md (claude/checker b2fe3440) §3 E-1, E-2 and §5 R1-R3, quoted here. Line L-5 by
experiments/si/box81/fix4/mkL5.py (asserts L-4's sha1 and each Old string once; R1, R2, R3 in that order); this text by fix4/mkfix4.py.
The packet P-ACYC.md and lines L-1 to L-4 are not edited.
- E-1 (C136 §3): «BETA-ACYC's signed clause quantifies over «every optimal counterstrategy of Odd». The proof compares values at the gate g,
  so it needs the POINTWISE sense (packet §1 l. 69: «σ̄ is an optimal counterstrategy: Ω_σ̄(v) ⊴ Ω_τ(v) for every Odd strategy τ and every
  v»).» … «Fix: R1, which defines the word.»
- E-2 (C136 §3): «pacyc81.py counts on states 0..k1−1 only (its docstring l. 4; l. 28 breaks at the first fallback). The packet states that
  set (§6 l. 171 «on states 0, …, T3 of N5′-xi», l. 180 «states 0, …, k1 − 1 that are non-standard»), and so do both referees» … «The line
  drops it.» … «Read on the whole run, the zeros are FALSE» (C136's whole-run counts on the four towers: σ̄ off the β-face 94 / 121 / 138 /
  150, non-standard states 3, C 2). «Fix: R2 and R3 state the set, «states 0, …, T3 before the first fallback».»

### F-14 (E-1, required): R1
- L-4 Old (once): «the order ⊴ and σ̄ of R118 [VJ];» New: «the order ⊴ and σ̄ of R118 [VJ], an optimal counterstrategy being pointwise
  optimal (at every vertex its play value is ⊴ the value under every Odd strategy; RESULTS R57 (b), [1E-N3], as landed in R104);»

### F-15 (E-2, required): R2 and R3
- R2, L-4 Old (once): «along N5′-xi on Γ3 from S3 (pacyc81.py; τ by fix1/pacyc81t.py), σ̄ off the β-face 0,» New: «along N5′-xi on Γ3
  from S3, on its states 0, …, T3 before the first fallback (pacyc81.py; τ by fix1/pacyc81t.py), σ̄ off the β-face 0,»
- R3, L-4 Old (once): «the same counts on IDEAL-CYC and along N5′-xi on Γ3;» New: «the same counts on IDEAL-CYC and on N5′-xi's states 0,
  …, T3 on Γ3;»
- (In the quoted strings a wrapped line is joined to the next with one space, as in C136 §5.)

### Line L-5
docs/si/P-ACYC-line-L5.txt: sha1 {S}, {B} B = L-4 with R1, R2, R3 (CHECKER C136's expected sha1 7a84e0944b0f33ce4d569604bec41d6e9236d82f
and 3,321 B, matched); one line, 43 «(» / 43 «)», 0 "|". L-1 to L-4 stay as they are.
""")
