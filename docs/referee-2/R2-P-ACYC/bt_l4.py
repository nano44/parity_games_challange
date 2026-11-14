# REFEREE-2 33: byte test of P-ACYC line L-4 (claude/l-si 0bc6f028) = L-3 (ff9b1639) + R-G + R-B (strings typed from the Lead's 05:24Z
# message to REFEREE-2; own code)
import subprocess, hashlib
S = "0bc6f0285c6fc042ebd446883b817fb38960cb08"
sh = lambda c, f: subprocess.run(["git", "show", f"{c}:{f}"], capture_output=True).stdout
L3, L4 = sh("ff9b1639", "docs/si/P-ACYC-line-L3.txt"), sh(S, "docs/si/P-ACYC-line-L4.txt")
CH = [("R-G", "not a TARGET.md claim); DATA (experiments/si/box81, check81.sh):",
       "not a TARGET.md claim); the step w* = K1 of LAMBDA-CONST's proof (σ̄(K2) toward K1 is Odd's unique optimum) is referee-originated (REFEREE R-P-ACYC §4.2 LC-1 and REFEREE-2 R2-P-ACYC G-1 / W-1, found independently, restated in P-ACYC's fixes entry 1 F-1), signed by both referees; DATA (experiments/si/box81, check81.sh):"),
      ("R-B", "(P-ACYC, docs/si/P-ACYC.md; L-SI successor 43)",
       "(P-ACYC, docs/si/P-ACYC.md with its fixes entries 1-2, docs/si/P-ACYC-fixes.md; L-SI successors 43-44)")]
t3, t4 = L3.decode(), L4.decode()
print("L-3", hashlib.sha1(L3).hexdigest(), len(L3), "| L-4", hashlib.sha1(L4).hexdigest(), len(L4))
X = t3
for k, o, n in CH:
    print(k, "old in L-3", t3.count(o), "| old in L-4", t4.count(o), "| new in L-3", t3.count(n), "| new in L-4", t4.count(n)); X = X.replace(o, n)
print("rebuild L-3 + R-G + R-B equal to L-4:", X.encode() == L4, hashlib.sha1(X.encode()).hexdigest(), len(X.encode()))
d = 0; neg = False
for c in t4: d += (c == "(") - (c == ")"); neg |= d < 0
print("L-4 newlines", t4.count("\n"), "parens", t4.count("("), t4.count(")"), "neg", neg, "pipes", t4.count("|"))
