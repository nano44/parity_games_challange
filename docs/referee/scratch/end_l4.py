"""REFEREE successor 30: P-N5-END L-4 = L-3 (d6afe92a) + R-U, then R-T0 (CHECKER 23 C138 §4, claude/checker 46905772; wrapped lines joined
with one space), strings typed from C138, not from the lane's script. Usage: end_l4.py L3 OUT"""
import sys, hashlib
L = open(sys.argv[1], encoding="utf-8").read()
M = "TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4"
R = [("R-U", "; G-N5-TIME stays OPEN, N5′-xi stays a CANDIDATE (D1); " + M + ": not M3, not M4, not a step-4 pass, not a TARGET.md claim (P-N5-END",
             "; N5′-xi stays a CANDIDATE (D1); " + M + ", so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (P-N5-END"),
     ("R-T0", "iterations 1, …, F − 1 being S4a steps with K-config κ0 and τ0;",
              "iterations 1, …, F − 1 being S4a steps with K-config κ0 and S3's τ;")]
X = L
for k, o, n in R:
    print(k, "old in L-3", L.count(o)); assert L.count(o) == 1 and X.count(o) == 1; X = X.replace(o, n)
b = X.encode(); d = m = 0
for c in X:
    d += (c == "(") - (c == ")"); m = min(m, d)
print("parens", X.count("("), X.count(")"), "min depth", m, "| newlines", X.count("\n"), "| bars", X.count("|"), "| τ0", X.count("τ0"),
      "| predicted L-4 sha1", hashlib.sha1(b).hexdigest(), len(b), "B")
open(sys.argv[2], "w", encoding="utf-8").write(X)
