#!/usr/bin/env python3
# P-N5-QN line L-2 generator (L-NEW successor 70). From the repo root: python3 experiments/new/box203/mkl2_qn.py
# L-2 = L-1 + R-D2 + R-S, in that order (CHECKER C140 §4, claude/checker 445372f9: E-1 = flag G-L43; Lead ruling R-D2a 02:30Z 2026-11-12:
# drop DEAD D2, carry its source into the DATA clause). Asserts the frozen packet's sha1, L-1's sha1, each old string exactly once,
# one line, no «|», balanced parentheses, «D2» absent, «406ef2fd» once, and the result sha1 C140 §4 gives (166e4695…, 7,187 B).
import hashlib
pk = open("docs/new/P-N5-QN.md", "rb").read()
assert hashlib.sha1(pk).hexdigest() == "97254bd2a97f28bb0c14ab5f4d236ee723821dd9", "frozen packet changed"
L1 = open("docs/new/P-N5-QN-line-L1.txt", encoding="utf-8").read()
assert hashlib.sha1(L1.encode()).hexdigest() == "28bf566bdf95d0708b3b80303bfa7311c8d5d8b1", "L-1 changed"
R = [("R-D2", "; D2 «at k = 1 every gate flips at most c·(lamch(g) + 1) times», every constant c (L-RED 63's MWR(n), claude/l-red "
              "406ef2fd, R229-box202 §2; copies experiments/new/box203/inst/MWR4_2.json sha1 856d369b, MWR8_2.json 918f1414, "
              "MWR16_2.json 2ccda9a9: gate (qz, 0) flips 2n + 1 times with lamch 0)", ""),
     ("R-S", "C = 0): MWR4/8/16_2 9 / 17 / 33,",
             "C = 0): MWR4/8/16_2 (L-RED 63's MWR(n), claude/l-red 406ef2fd; box203/inst/MWR4_2.json sha1 856d369b, MWR8_2.json "
             "918f1414, MWR16_2.json 2ccda9a9) 9 / 17 / 33,")]
L = L1
for k, o, n in R:
    assert L.count(o) == 1, (k, L.count(o))
    L = L.replace(o, n)
    print(k, "applied; sha1", hashlib.sha1(L.encode()).hexdigest()[:8], len(L.encode()), "B")
assert L.endswith("\n") and L.count("\n") == 1 and "|" not in L and L.count("(") == L.count(")"), (L.count("("), L.count(")"))
assert "D2" not in L and L.count("406ef2fd") == 1
b = L.encode(); h = hashlib.sha1(b).hexdigest()
assert (h, len(b)) == ("166e4695b07843ae73e2d23ac92802c256f31113", 7187), (h, len(b))
open("docs/new/P-N5-QN-line-L2.txt", "wb").write(b)
print("L-2 written: sha1", h, len(b), "B")
