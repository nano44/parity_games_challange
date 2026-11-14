#!/usr/bin/env python3
# P-N5-CHAIN line L-3 generator (L-NEW successor 65). From the repo root: python3 experiments/new/box196/mkl3_196.py
# L-3 = L-2 + R-1 + R-2 + R-4 (REQUIRED) + N-1 (optional, taken): REFEREE-2 35 second review, claude/referee-2 0e5c7c37,
# docs/referee-2/R2-P-N5-CHAIN.md «Line L-1» / «Line L-2», exact strings (Lead ruling 11:38Z: strings, not tool fixes). N-2 not taken.
# Asserts the frozen packet's sha1, L-2's sha1, each old string exactly once in L-2, one line, no «|», balanced parentheses.
import hashlib
pk = open("docs/new/P-N5-CHAIN.md", encoding="utf-8").read()
assert hashlib.sha1(pk.encode()).hexdigest() == "6e613ba762b6ecf67247ef6d8674b4c960013039", "frozen packet changed"
L2 = open("docs/new/P-N5-CHAIN-line-L2.txt", encoding="utf-8").read()
assert hashlib.sha1(L2.encode()).hexdigest() == "e481d260884807424c545bd3f3cdd7fbfb25f05c", "L-2 changed"
R = [("R-1", "QUIET3: wfail 0 (unit: quiet windows)", "QUIET3: wfail 0 (unit: quiet steps past the L3-th step of their window)"),
     ("R-2", "T-QUIET3: Tfail 0 (unit: runs)",
      "T-QUIET3: Tfail 0 (unit: runs with T3 > Q + (Q + 1)·L3, Q the number of loud steps; the Σ_v form is not counted)"),
     ("R-4", "LOC-K2-3: k2fail 0 (unit: states)",
      "LOC-K2-3: k2fail 0 (unit: states with σ̄_t(K2) ≠ r; the conjunct Ω_t(r) ◁ Ω_t(K2) is not counted)"),
     ("N-1", "spec on 100 runs and 5 pinned genomes, check196.out)", "spec on 100 runs, and 5 pinned genomes in xi mode, check196.out)")]
L = L2
for k, o, n in R:
    assert L2.count(o) == 1, (k, L2.count(o))
    L = L.replace(o, n)
assert L.endswith("\n") and L.count("\n") == 1 and "|" not in L and L.count("(") == L.count(")"), (L.count("("), L.count(")"))
open("docs/new/P-N5-CHAIN-line-L3.txt", "w", encoding="utf-8").write(L)
b = L.encode(); print("R-1, R-2, R-4, N-1 old once each, applied; sha1", hashlib.sha1(b).hexdigest(), len(b), "bytes; parens", L.count("("), L.count(")"))
