#!/usr/bin/env python3
# P-N5-ASC line L-6 generator (L-NEW successor 65). From the repo root: python3 experiments/new/box193/mkl6_193.py
# L-6 = L-5 + R6 (CHECKER 22 C135 Add. 1, claude/checker 0ffde42c, docs/checker/C135.md: E-5 FAIL, R6 its exact replacement; routed by
# the Lead 10:25Z). Asserts L-5's sha1, the old string exactly once in L-5, one line, no «|», balanced parentheses, and the predicted
# sha1 a23c61d384036ce3fa771e27e175a8dbf2331658 (5,449 B).
import hashlib
R = [("R6", "(items 1..M compared by number, a run of forests with every chain lex-nondecreasing, an ascent a step to a larger item), a hub whose value has",
      "(items 1..M compared by number, a forest a map next from the items to the items and ⊥ without cycles, chain(x) := (x, next(x), "
      "next²(x), …) up to ⊥, compared as a set, a run of forests with every chain lex-nondecreasing, an ascent a step to a larger item), a hub "
      "(h_t an item or ⊥ at each time t, chain(⊥) := ∅, with chain_s(h_s) ≤ chain_t(h_t) for s < t) whose value chain_t(h_t) has")]
L = open("docs/new/P-N5-ASC-line-L5.txt", encoding="utf-8").read()
assert hashlib.sha1(L.encode()).hexdigest() == "fe4d3f902b6afde93384ebf625fa9bebcea0e1d0", "L-5 changed"
for name, old, new in R:
    assert L.count(old) == 1, (name, L.count(old)); L = L.replace(old, new)
assert L.endswith("\n") and L.count("\n") == 1 and "|" not in L and L.count("(") == L.count(")"), (L.count("("), L.count(")"))
b = L.encode(); h = hashlib.sha1(b).hexdigest()
open("docs/new/P-N5-ASC-line-L6.txt", "w", encoding="utf-8").write(L)
print("R6 old once, applied; sha1", h, len(b), "bytes; parens", L.count("("), L.count(")"))
assert h == "a23c61d384036ce3fa771e27e175a8dbf2331658", "prediction differs"
