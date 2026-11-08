#!/usr/bin/env python3
# P-N5-ASC line L-5 generator (L-NEW successor 64). From the repo root: python3 experiments/new/box193/mkl5_193.py
# L-5 = L-4 + R-A (REQUIRED) + R-I (optional, taken by Lead ruling 06:33Z), REFEREE 29 R-P-N5-ASC §F + §F addendum 1 (claude/referee
# 52e6e77b, 055758ba). Asserts each old string occurs once in L-4, and the predicted sha1 fe4d3f902b6afde93384ebf625fa9bebcea0e1d0 (5,192 B).
import hashlib
R = [("R-A", "(items 1..M, a run of forests with every chain lex-nondecreasing)",
             "(items 1..M compared by number, a run of forests with every chain lex-nondecreasing, an ascent a step to a larger item)"),
     ("R-I", "(f, …), i.e. the first e-vertex on v's play is f and f ∈ Π_t(v), then", "(f, …), then")]
L = open("docs/new/P-N5-ASC-line-L4.txt", encoding="utf-8").read()
assert hashlib.sha1(L.encode()).hexdigest() == "4017305a34eac21615ba8f172a9b899544d25659", "L-4 changed"
for name, old, new in R:
    assert L.count(old) == 1, (name, L.count(old)); L = L.replace(old, new)
b = L.encode("utf-8"); h = hashlib.sha1(b).hexdigest()
print("R-A, R-I old once each, applied; sha1", h, len(b), "bytes; parens", L.count("("), L.count(")"))
assert L.count("\n") == 1 and "|" not in L and L.count("(") == L.count(")")
assert h == "fe4d3f902b6afde93384ebf625fa9bebcea0e1d0" and len(b) == 5192, "differs from the prediction"
open("docs/new/P-N5-ASC-line-L5.txt", "w", encoding="utf-8").write(L)
