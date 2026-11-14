#!/usr/bin/env python3
# P-N5-CHAIN line L-4 generator (L-NEW successor 65). From the repo root: python3 experiments/new/box196/mkl4_196.py
# L-4 = L-3 + R-G3 + R-W + R-B3, in that order (Lead rulings 13:02Z and 13:12Z (R-W: REFEREE-2 35's W-1 repair, re-derived and signed by REFEREE 30), under L41, as P-N5-QUIET's R-G: REFEREE-2 35 R2-P-N5-CHAIN.md Addendum 3, claude/referee-2
# 09ce14fc, the boundary step of QUIET3's (Q5) on Γ3; the source note names fixes entries 1-3, entry 3 carrying that proof step).
# Asserts the frozen packet's sha1, L-3's sha1, each old string exactly once in L-3, one line, no «|», balanced parentheses.
import hashlib
pk = open("docs/new/P-N5-CHAIN.md", encoding="utf-8").read()
assert hashlib.sha1(pk.encode()).hexdigest() == "6e613ba762b6ecf67247ef6d8674b4c960013039", "frozen packet changed"
L3 = open("docs/new/P-N5-CHAIN-line-L3.txt", encoding="utf-8").read()
assert hashlib.sha1(L3.encode()).hexdigest() == "c484795c888ab46cee07038094368ba28da0055d", "L-3 changed"
R = [("R-G3", "is a separate gauntlet step-4 item; DATA, clause by clause (unit:",
      "is a separate gauntlet step-4 item; the step β_g ∉ Π(y) for the boundary points y in QUIET3's (Q5) F4′ (an e-face target y of class "
      "(w, S ∖ {e}): else S = E(β_g) ⊆ E(y); the pb exit: Π = {K0, K3}; w: Π = ∅) is referee-originated (REFEREE R-P-N5-QUIET §3 (Q4), "
      "l. 118-120, REFEREE 28, for P-N5-QUIET's form; REFEREE 30 and REFEREE-2 35, R2-P-N5-CHAIN Addendum 3, for the Γ3 form), signed by "
      "both referees; DATA, clause by clause (unit:"),
     ("R-W", "signed by both referees; DATA, clause by clause (unit:",
      "signed by both referees; (F-cls3)'s convexity and E-MON3's reason hold for non-core vertices, the eight core vertices being constant "
      "(referee-originated: REFEREE-2 R2-P-N5-CHAIN W-1, signed by both referees); DATA, clause by clause (unit:"),
     ("R-B3", "frozen at l-new 93531b03, sha1 6e613ba7; source box 196, docs/new/N5-CHAIN-box196.md; L-NEW successor 64;",
      "frozen at l-new 93531b03, sha1 6e613ba7, with its fixes entries 1-3, docs/new/P-N5-CHAIN-fixes.md; source box 196, "
      "docs/new/N5-CHAIN-box196.md; L-NEW successors 64-65;")]
L = L3
for k, o, n in R:                         # applied in order; R-W's old string is created by R-G3 (once in L-3 + R-G3, absent from L-3)
    assert L.count(o) == 1, (k, L.count(o))
    if k != "R-W": assert L3.count(o) == 1, (k, "not once in L-3")
    else: assert L3.count(o) == 0, (k, "unexpectedly in L-3")
    L = L.replace(o, n)
assert L.endswith("\n") and L.count("\n") == 1 and "|" not in L and L.count("(") == L.count(")"), (L.count("("), L.count(")"))
open("docs/new/P-N5-CHAIN-line-L4.txt", "w", encoding="utf-8").write(L)
b = L.encode(); print("R-G3, R-W, R-B3 old once each, applied; sha1", hashlib.sha1(b).hexdigest(), len(b), "bytes; parens", L.count("("), L.count(")"))
