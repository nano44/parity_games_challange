#!/usr/bin/env python3
"""REFEREE-2 successor 35: byte test of P-ACYC line L-5 (claude/l-si 358ede16) = L-4 (0bc6f028, 85bb221f…) + CHECKER 22's R1-R3
(claude/checker b2fe3440 docs/checker/C136.md l. 84-89, wrapped lines joined with one space). Own code. Usage: bt_l5.py (repo root)"""
import subprocess, hashlib
def show(rev, p): return subprocess.run(["git", "show", f"{rev}:{p}"], capture_output=True, check=True).stdout.decode("utf-8")
L4 = show("0bc6f028", "docs/si/P-ACYC-line-L4.txt"); L5 = show("358ede16", "docs/si/P-ACYC-line-L5.txt")
h = lambda s: hashlib.sha1(s.encode()).hexdigest()
print("L-4", h(L4), len(L4.encode()), "B; L-5", h(L5), len(L5.encode()), "B; parens", L5.count("("), L5.count(")"), "pipes", L5.count("|"), "lines", L5.count("\n"))
C = " ".join(show("b2fe3440", "docs/checker/C136.md").split())
R = [("R1", "the order ⊴ and σ̄ of R118 [VJ];",
      "the order ⊴ and σ̄ of R118 [VJ], an optimal counterstrategy being pointwise optimal (at every vertex its play value is ⊴ the value under every Odd strategy; RESULTS R57 (b), [1E-N3], as landed in R104);"),
     ("R2", "along N5′-xi on Γ3 from S3 (pacyc81.py; τ by fix1/pacyc81t.py), σ̄ off the β-face 0,",
      "along N5′-xi on Γ3 from S3, on its states 0, …, T3 before the first fallback (pacyc81.py; τ by fix1/pacyc81t.py), σ̄ off the β-face 0,"),
     ("R3", "the same counts on IDEAL-CYC and along N5′-xi on Γ3;", "the same counts on IDEAL-CYC and on N5′-xi's states 0, …, T3 on Γ3;")]
exp = L4
for k, o, n in R:
    print(f"{k}: old in L-4 {L4.count(o)} / L-5 {L5.count(o)}; new in L-4 {L4.count(n)} / L-5 {L5.count(n)}; both verbatim in C136 {('«'+o+'»') in C and ('«'+n+'»') in C}")
    exp = exp.replace(o, n)
print("L-5 == L-4 + R1 + R2 + R3:", L5 == exp)
