#!/usr/bin/env python3
"""L-SI P-ACYC fixes entry 4: line L-5 = L-4 (docs/si/P-ACYC-line-L4.txt, sha1 85bb221f…) with CHECKER C136's replacements R1, R2, R3
(claude/checker b2fe3440, docs/checker/C136.md §5; routed by the Lead 15:52Z), in that order. Each Old string must occur exactly once.
Prints L-5. Usage: mkL5.py REPO_ROOT"""
import sys, os, hashlib
R = sys.argv[1]; L4 = open(os.path.join(R, "docs", "si", "P-ACYC-line-L4.txt"), "rb").read()
assert hashlib.sha1(L4).hexdigest() == "85bb221f19ca457655c954f570552bc0f4d8095d", "L-4 changed"
L = L4.decode()
R1 = ("the order ⊴ and σ̄ of R118 [VJ];",
      "the order ⊴ and σ̄ of R118 [VJ], an optimal counterstrategy being pointwise optimal (at every vertex its play value is ⊴ the value "
      "under every Odd strategy; RESULTS R57 (b), [1E-N3], as landed in R104);")
R2 = ("along N5′-xi on Γ3 from S3 (pacyc81.py; τ by fix1/pacyc81t.py), σ̄ off the β-face 0,",
      "along N5′-xi on Γ3 from S3, on its states 0, …, T3 before the first fallback (pacyc81.py; τ by fix1/pacyc81t.py), σ̄ off the β-face 0,")
R3 = ("the same counts on IDEAL-CYC and along N5′-xi on Γ3;",
      "the same counts on IDEAL-CYC and on N5′-xi's states 0, …, T3 on Γ3;")
for old, new in (R1, R2, R3):
    assert L.count(old) == 1, old
    L = L.replace(old, new)
assert L.count("(") == L.count(")") and "|" not in L
sys.stdout.write(L)
