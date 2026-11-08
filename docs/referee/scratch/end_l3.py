"""REFEREE successor 30: L-3 = L-2 + S1 (REFEREE-2 34 L-R1) + S2 N-1 + S3 N-2 (claude/referee-2 9b3cc9b6) + S4 EL-1 + S5 EL-2
(R-P-N5-END.md §C), strings typed from the referee reports, not from the lane's script. Usage: end_l3.py L2 OUT"""
import sys, hashlib
L = open(sys.argv[1], encoding="utf-8").read()
R = [("S1", "so the K-config changes only at a fallback and the run cannot stop before one",
             "so the K-config leaves κ0 only at a fallback and the run cannot stop before one"),
     ("S2", "has L(G) = 1 and N5 makes 3 iterations (F = 1)",
             "has L(G) = 1 (IDEAL run read with B_s the set of β-ids on its eventually periodic X-chain; R104's IDEAL run is defined on "
             "IDEAL-ACYC) and N5 makes 3 iterations (F = 1)"),
     ("S3", "ctrl2 e0fail 200 and e1fail 200 (unit: states)",
             "ctrl2 e0fail 200 (unit: states) and e1fail 200 (unit: iterations before the first fallback)"),
     ("S4", "their transfer to the Γ3 run (equal runs at exact VJ ties) is NOT proved",
             "their transfer to the Γ3 run is NOT proved (the Γ3 run can differ from the IDEAL-CYC run at exact VJ ties, R118's DATA)"),
     ("S5", "REFEREE 29 R-P-N5-END §4 (claude/referee e4cb208a)", "REFEREE 29 R-P-N5-END §4 (A), (B) (claude/referee e4cb208a)")]
X = L
for k, o, n in R:
    print(k, "old in L-2", L.count(o)); assert L.count(o) == 1 and X.count(o) == 1; X = X.replace(o, n)
b = X.encode(); d = m = 0
for c in X:
    d += (c == "(") - (c == ")"); m = min(m, d)
print("parens", X.count("("), X.count(")"), "min depth", m, "| newlines", X.count("\n"), "| bars", X.count("|"),
      "| predicted L-3 sha1", hashlib.sha1(b).hexdigest(), len(b), "B")
open(sys.argv[2], "w", encoding="utf-8").write(X)
