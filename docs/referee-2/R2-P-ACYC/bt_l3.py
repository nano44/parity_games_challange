# REFEREE-2 32: byte test of P-ACYC line L-3 (claude/l-si ff9b1639) = L-2 + D-5 (own code)
import subprocess, hashlib
S = "ff9b16396129de30cca6d10a67285c3ed558d14a"
sh = lambda f: subprocess.run(["git", "show", f"{S}:{f}"], capture_output=True).stdout
L2, L3 = sh("docs/si/P-ACYC-line-L2.txt"), sh("docs/si/P-ACYC-line-L3.txt"); F = sh("docs/si/P-ACYC-fixes.md").decode()
o = "along N5′-xi on Γ3 from S3 (pacyc81.py),"; n = "along N5′-xi on Γ3 from S3 (pacyc81.py; τ by fix1/pacyc81t.py),"
t2, t3 = L2.decode(), L3.decode()
print("L-2", hashlib.sha1(L2).hexdigest(), len(L2), "| L-3", hashlib.sha1(L3).hexdigest(), len(L3))
print("old in L-2", t2.count(o), "| old in L-3", t3.count(o), "| new in L-3", t3.count(n))
rb = t2.replace(o, n).encode(); print("rebuild L-2 + D-5 equal to L-3:", rb == L3, hashlib.sha1(rb).hexdigest())
d = 0; neg = False
for c in t3: d += (c == "(") - (c == ")"); neg |= d < 0
print("L-3 newlines", t3.count("\n"), "parens", t3.count("("), t3.count(")"), "neg", neg, "pipes", t3.count("|"))
print("F-11 parenthesis strings in entry 2:", F.count("(its first N + 1 iterations)"), F.count("(at most N iterations; its first fallback comes by\n  iteration N + 1)"))
print("entry 1 unchanged (prefix of entry-2 file equals 01a68edc's file):",
      F.encode().startswith(subprocess.run(["git", "show", "01a68edc:docs/si/P-ACYC-fixes.md"], capture_output=True).stdout))
