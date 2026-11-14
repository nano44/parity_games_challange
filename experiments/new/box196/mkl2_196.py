#!/usr/bin/env python3
# P-N5-CHAIN line L-2 generator (L-NEW successor 65). From the repo root: python3 experiments/new/box196/mkl2_196.py
# L-2 = L-1 + CL-1 (REFEREE 29, claude/referee 36d2932d, docs/referee/R-P-N5-CHAIN.md §5; Lead ruling: Form A, REFEREE 29's exact strings).
# Asserts: the frozen packet's sha1, L-1's sha1, each old string exactly once in L-1, one line, no «|», balanced parentheses.
import hashlib
pk = open("docs/new/P-N5-CHAIN.md", encoding="utf-8").read()
assert hashlib.sha1(pk.encode()).hexdigest() == "6e613ba762b6ecf67247ef6d8674b4c960013039", "frozen packet changed"
L1 = open("docs/new/P-N5-CHAIN-line-L1.txt", encoding="utf-8").read()
assert hashlib.sha1(L1.encode()).hexdigest() == "bd152dd9c71ea47dbc7fa6655a9a18a87908781a", "L-1 changed"
FIX = [("CL-1",
 "controls fire (every fail counter has one): ctrl1 (L3 := 0, U(G) := −1) wfail 32, Tfail 22, upfail 26,477 in 50 runs; ctrl2 "
 "(order reversed) locfail 3,320; ctrl3 (no excluded vertex) bonly 2,269; spec mode nohoward 599 (rand, 200 runs) and 911 (dense, 200 "
 "runs);",
 "controls fire (every fail counter except ties, NO-TIE3's counter, which has none): ctrl1 (L3 := 0, U(G) := −1) wfail 32, "
 "Tfail 22, upfail 26,477; ctrl2 (order reversed) locfail 3,320; ctrl3 (no excluded vertex) bonly 2,269 (each control on 50 runs, "
 "family rand, seed 1963, check196.out); spec mode, seed 1963 (data/sweep196.out), nohoward 599 (rand, 200 runs) and 911 (dense, 200 "
 "runs);")]
L = L1
for k, o, n in FIX:
    assert L1.count(o) == 1, (k, L1.count(o))
    L = L.replace(o, n)
assert L.endswith("\n") and L.count("\n") == 1 and "|" not in L and L.count("(") == L.count(")"), (L.count("("), L.count(")"))
open("docs/new/P-N5-CHAIN-line-L2.txt", "w", encoding="utf-8").write(L)
b = L.encode(); print("ok", len(b), hashlib.sha1(b).hexdigest(), "parens", L.count("("), L.count(")"))
