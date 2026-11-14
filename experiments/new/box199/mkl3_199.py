#!/usr/bin/env python3
# P-N5-SPLIT line L-3 generator (L-NEW successor 71). From the repo root: python3 experiments/new/box199/mkl3_199.py
# L-3 = L-2 + R-U127 (Lead ruling R-U127 07:58Z 2026-11-12, DATA rule: every DATA clause names its counter): units (a), (b), (c) as
# proposed in fixes entry 3, and the source note «with fixes entries 1-2» -> «with fixes entries 1-4». Asserts the frozen packet's sha1,
# L-2's sha1 (d8888d0b…), each old string exactly once («max c_y ≤ 6» once: (a) goes into the FIRST «max c_y»), one line, no «|»,
# balanced parentheses, each new unit string exactly once.
import hashlib
pk = open("docs/new/P-N5-SPLIT.md", "rb").read()
assert hashlib.sha1(pk).hexdigest() == "5bc1b1f390ed81683fe5c93008c7ea0b338fe735", "frozen packet changed"
L2 = open("docs/new/P-N5-SPLIT-line-L2.txt", encoding="utf-8").read()
assert hashlib.sha1(L2.encode()).hexdigest() == "d8888d0b090339b80b4ce9b636a23461b476bf3f", "L-2 changed"
UA = " (unit: y-tops of one (v, I, y), max over (v, I, y); split199.out maxc)"
UB = " (unit: distinct split pairs (u, b) of the y-tops of one (v, I, y), max over (v, I, y); split199.out maxSPL)"
UC = "; unit: states of the HOW3 run, max over the 28 frozen instances, split199.out T3; 199 on MW32_2"
R = [("R-U127 (a)", "max c_y ≤ 6", "max c_y" + UA + " ≤ 6"),
     ("R-U127 (b)", "max split pairs 5 (FW6_4, FW8_4)", "max split pairs" + UB + " 5 (FW6_4, FW8_4)"),
     ("R-U127 (c)", "every run is short (T3 ≤ 199)", "every run is short (T3 ≤ 199" + UC + ")"),
     ("R-U127 (d)", "with fixes entries 1-2", "with fixes entries 1-4")]
L = L2
for k, o, n in R:
    assert L.count(o) == 1, (k, L.count(o))
    L = L.replace(o, n)
    print(k, "applied; sha1", hashlib.sha1(L.encode()).hexdigest()[:8], len(L.encode()), "B")
assert L.endswith("\n") and L.count("\n") == 1 and "|" not in L and L.count("(") == L.count(")"), (L.count("("), L.count(")"))
for s in (UA, UB, UC, "with fixes entries 1-4"): assert L.count(s) == 1, s
assert "with fixes entries 1-2" not in L
b = L.encode(); h = hashlib.sha1(b).hexdigest()
open("docs/new/P-N5-SPLIT-line-L3.txt", "wb").write(b)
print("L-3 written: sha1", h, len(b), "B")
