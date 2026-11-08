"""REFEREE successor 30: P-ACYC L-5 = L-4 (85bb221f) + CHECKER 22's R1-R3 (C136, claude/checker b2fe3440 l. 84-89; wrapped lines joined
with one space), strings typed from C136, not from the lane's script. Usage: acyc_l5.py L4 OUT"""
import sys, hashlib
L = open(sys.argv[1], encoding="utf-8").read()
R = [("R1", "the order ⊴ and σ̄ of R118 [VJ];",
            "the order ⊴ and σ̄ of R118 [VJ], an optimal counterstrategy being pointwise optimal (at every vertex its play value is ⊴ the "
            "value under every Odd strategy; RESULTS R57 (b), [1E-N3], as landed in R104);"),
     ("R2", "along N5′-xi on Γ3 from S3 (pacyc81.py; τ by fix1/pacyc81t.py), σ̄ off the β-face 0,",
            "along N5′-xi on Γ3 from S3, on its states 0, …, T3 before the first fallback (pacyc81.py; τ by fix1/pacyc81t.py), σ̄ off the "
            "β-face 0,"),
     ("R3", "the same counts on IDEAL-CYC and along N5′-xi on Γ3;", "the same counts on IDEAL-CYC and on N5′-xi's states 0, …, T3 on Γ3;")]
X = L
for k, o, n in R:
    print(k, "old in L-4", L.count(o)); assert L.count(o) == 1 and X.count(o) == 1; X = X.replace(o, n)
b = X.encode(); d = m = 0
for c in X:
    d += (c == "(") - (c == ")"); m = min(m, d)
print("parens", X.count("("), X.count(")"), "min depth", m, "| newlines", X.count("\n"), "| bars", X.count("|"),
      "| predicted L-5 sha1", hashlib.sha1(b).hexdigest(), len(b), "B")
open(sys.argv[2], "w", encoding="utf-8").write(X)
