#!/usr/bin/env python3
# P-N5-QUIET line L-4 generator (L-NEW successor 65). From the repo root: python3 experiments/new/box194/mkl4_194.py
# L-4 = L-3 + R-B2 (Lead ruling 12:47Z, by CHECKER's C134 N-S / C135 E-1 rule: fixes entry 3 carries a proof step (R-G), so the source note
# names it). Asserts the frozen packet's sha1, L-3's sha1, the old string exactly once in L-3, one line, no «|», balanced parentheses.
import hashlib
pk = open("docs/new/P-N5-QUIET.md", encoding="utf-8").read()
assert hashlib.sha1(pk.encode()).hexdigest().startswith("066dfc7d"), "frozen packet changed"
L3 = open("docs/new/P-N5-QUIET-line-L3.txt", encoding="utf-8").read()
assert hashlib.sha1(L3.encode()).hexdigest() == "d9b5e610300927fd0e8c1ec8567ee1fb68758df7", "L-3 changed"
R = [("R-B2", "(P-N5-QUIET, docs/new/P-N5-QUIET.md with its fixes entries 1-2, docs/new/P-N5-QUIET-fixes.md; L-NEW successors 62 and 64)",
              "(P-N5-QUIET, docs/new/P-N5-QUIET.md with its fixes entries 1-3, docs/new/P-N5-QUIET-fixes.md; L-NEW successors 62, 64 and 65)")]
L = L3
for k, o, n in R:
    assert L3.count(o) == 1, (k, L3.count(o))
    L = L.replace(o, n)
assert L.endswith("\n") and L.count("\n") == 1 and "|" not in L and L.count("(") == L.count(")"), (L.count("("), L.count(")"))
open("docs/new/P-N5-QUIET-line-L4.txt", "w", encoding="utf-8").write(L)
b = L.encode(); print("R-B2 old once, applied; sha1", hashlib.sha1(b).hexdigest(), len(b), "bytes; parens", L.count("("), L.count(")"))
