#!/usr/bin/env python3
# P-N5-END line L-3 generator (L-NEW successor 65). From the repo root: python3 experiments/new/box195/mkl3_195.py
# L-3 = L-2 + S1-S5 below (fixes entry 3: REFEREE-2 34 R2-P-N5-END.md «Line L-2» L-R1 (required), N-1, N-2 (claude/referee-2 9b3cc9b6,
# Add. 1 0f82f03b); REFEREE 29 R-P-N5-END.md §C EL-1, EL-2 (claude/referee e4cb208a / 407f4a21)). S6 (fixes entries 1-3) dropped by Lead ruling 10:18Z.
# Asserts the frozen packet's sha1, L-2's sha1, each old string exactly once in L-2, one line, no «|», balanced parentheses.
import hashlib
pk = open("docs/new/P-N5-END.md", encoding="utf-8").read()
assert hashlib.sha1(pk.encode()).hexdigest().startswith("5cae845b"), "frozen packet changed"
L2 = open("docs/new/P-N5-END-line-L2.txt", encoding="utf-8").read()
assert hashlib.sha1(L2.encode()).hexdigest() == "e8a8ac51cc79c9de4000749899e7f0b860eeebe5", "L-2 changed"
R = [
 ("S1 L-R1", "so the K-config changes only at a fallback and the run cannot stop before one",
             "so the K-config leaves κ0 only at a fallback and the run cannot stop before one"),
 ("S2 N-1", "has L(G) = 1 and N5 makes 3 iterations (F = 1)",
            "has L(G) = 1 (IDEAL run read with B_s the set of β-ids on its eventually periodic X-chain; R104's IDEAL run is defined on IDEAL-ACYC) and N5 makes 3 iterations (F = 1)"),
 ("S3 N-2", "ctrl2 e0fail 200 and e1fail 200 (unit: states)",
            "ctrl2 e0fail 200 (unit: states) and e1fail 200 (unit: iterations before the first fallback)"),
 ("S4 EL-1", "their transfer to the Γ3 run (equal runs at exact VJ ties) is NOT proved",
             "their transfer to the Γ3 run is NOT proved (the Γ3 run can differ from the IDEAL-CYC run at exact VJ ties, R118's DATA)"),
 ("S5 EL-2", "REFEREE 29 R-P-N5-END §4 (claude/referee e4cb208a)", "REFEREE 29 R-P-N5-END §4 (A), (B) (claude/referee e4cb208a)"),
]
L = L2
for k, o, n in R:
    assert L2.count(o) == 1, (k, L2.count(o))
    L = L.replace(o, n)
assert L.endswith("\n") and L.count("\n") == 1 and "|" not in L and L.count("(") == L.count(")"), (L.count("("), L.count(")"))
open("docs/new/P-N5-END-line-L3.txt", "w", encoding="utf-8").write(L)
b = L.encode(); print("S1-S5 old once each, applied; sha1", hashlib.sha1(b).hexdigest(), len(b), "bytes; parens", L.count("("), L.count(")"))
