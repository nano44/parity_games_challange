"""REFEREE successor 29: P-ACYC byte test L-3 -> L-4 (R-G = F-12, R-B = F-13; strings from the Lead's 06:30Z relay = fixes entry 3).
Usage: acyc_l4.py L3 L4"""
import sys, hashlib
L3 = open(sys.argv[1], encoding="utf-8").read(); L4 = open(sys.argv[2], encoding="utf-8").read()
R = [("R-G", "not a TARGET.md claim); DATA (experiments/si/box81, check81.sh):",
      "not a TARGET.md claim); the step w* = K1 of LAMBDA-CONST's proof (σ̄(K2) toward K1 is Odd's unique optimum) is referee-originated (REFEREE R-P-ACYC §4.2 LC-1 and REFEREE-2 R2-P-ACYC G-1 / W-1, found independently, restated in P-ACYC's fixes entry 1 F-1), signed by both referees; DATA (experiments/si/box81, check81.sh):"),
     ("R-B", "(P-ACYC, docs/si/P-ACYC.md; L-SI successor 43)",
      "(P-ACYC, docs/si/P-ACYC.md with its fixes entries 1-2, docs/si/P-ACYC-fixes.md; L-SI successors 43-44)")]
X = L3
for nm, o, n in R:
    print(nm, "old in L-3:", L3.count(o), "| new in L-3:", L3.count(n), "| new in L-4:", L4.count(n), "| old in L-4:", L4.count(o)); X = X.replace(o, n)
h = lambda t: (hashlib.sha1(t.encode()).hexdigest(), len(t.encode()), t.count("("), t.count(")"), t.count("\n"))
print("L-3 + R-G + R-B == L-4:", X == L4, h(X), "| L-4", h(L4))
