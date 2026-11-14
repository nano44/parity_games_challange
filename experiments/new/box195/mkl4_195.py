#!/usr/bin/env python3
# P-N5-END line L-4 generator (L-NEW successor 68). From the repo root: python3 experiments/new/box195/mkl4_195.py
# L-4 = L-3 + R-U, then R-T0 (fixes entry 4: CHECKER 23 C138 E-1, E-2, claude/checker 46905772, docs/checker/C138.md §4; strings verbatim).
# Asserts the frozen packet's sha1, L-3's sha1, each old string exactly once, one line, no «|», balanced parentheses, no «τ0»,
# and CHECKER's expected result (sha1 5f88c297…, 7,230 B).
import hashlib
pk = open("docs/new/P-N5-END.md", encoding="utf-8").read()
assert hashlib.sha1(pk.encode()).hexdigest().startswith("5cae845b"), "frozen packet changed"
L3 = open("docs/new/P-N5-END-line-L3.txt", encoding="utf-8").read()
assert hashlib.sha1(L3.encode()).hexdigest() == "d6afe92ae0d2c0021743c99d2bd10f16cad27c73", "L-3 changed"
R = [
 ("R-U (C138 E-1)",
  "; G-N5-TIME stays OPEN, N5′-xi stays a CANDIDATE (D1); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4: not M3, not M4, not a step-4 pass, not a TARGET.md claim (P-N5-END",
  "; N5′-xi stays a CANDIDATE (D1); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4, so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (P-N5-END"),
 ("R-T0 (C138 E-2)",
  "iterations 1, …, F − 1 being S4a steps with K-config κ0 and τ0;",
  "iterations 1, …, F − 1 being S4a steps with K-config κ0 and S3's τ;"),
]
L = L3
for k, o, n in R:
    assert L.count(o) == 1, (k, L.count(o))
    L = L.replace(o, n)
assert L.endswith("\n") and L.count("\n") == 1 and "|" not in L and L.count("(") == L.count(")") and "τ0" not in L, (L.count("("), L.count(")"))
b = L.encode(); h = hashlib.sha1(b).hexdigest()
assert h == "5f88c2971718522027ae267754814c6ba401b829" and len(b) == 7230, (h, len(b))
open("docs/new/P-N5-END-line-L4.txt", "w", encoding="utf-8").write(L)
print("R-U, R-T0 old once each, applied; sha1", h, len(b), "bytes; parens", L.count("("), L.count(")"), "; tau0", L.count("τ0"))
