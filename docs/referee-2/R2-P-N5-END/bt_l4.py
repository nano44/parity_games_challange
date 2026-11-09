#!/usr/bin/env python3
"""REFEREE-2 successor 35: byte test of P-N5-END line L-4 (claude/l-new b7faeebe) = L-3 (8b67d40e, d6afe92a…) + CHECKER 23's R-U, then
R-T0 (claude/checker 46905772 docs/checker/C138.md §4 l. 52-57, wrapped lines joined with one space). Own code. Usage: bt_l4.py (repo root)"""
import subprocess, hashlib
def show(rev, p): return subprocess.run(["git", "show", f"{rev}:{p}"], capture_output=True, check=True).stdout.decode("utf-8")
L3 = show("8b67d40e", "docs/new/P-N5-END-line-L3.txt"); L4 = show("b7faeebe", "docs/new/P-N5-END-line-L4.txt")
h = lambda s: hashlib.sha1(s.encode()).hexdigest()
print("L-3", h(L3), len(L3.encode()), "B; L-4", h(L4), len(L4.encode()), "B; parens", L4.count("("), L4.count(")"), "pipes", L4.count("|"), "lines", L4.count("\n"), "τ0", L4.count("τ0"))
C = " ".join(show("46905772", "docs/checker/C138.md").split())
R = [("R-U", "; G-N5-TIME stays OPEN, N5′-xi stays a CANDIDATE (D1); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4: not M3, not M4, not a step-4 pass, not a TARGET.md claim (P-N5-END",
      "; N5′-xi stays a CANDIDATE (D1); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4, so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (P-N5-END"),
     ("R-T0", "iterations 1, …, F − 1 being S4a steps with K-config κ0 and τ0;", "iterations 1, …, F − 1 being S4a steps with K-config κ0 and S3's τ;")]
exp = L3
for k, o, n in R:
    print(f"{k}: old in current {exp.count(o)} / L-4 {L4.count(o)}; new in L-3 {L3.count(n)} / L-4 {L4.count(n)}; both verbatim in C138 {('«'+o+'»') in C and ('«'+n+'»') in C}")
    exp = exp.replace(o, n)
print("L-4 == L-3 + R-U + R-T0:", L4 == exp)
for s in ["PROVED-CONDITIONAL", "REACH3-CYC"]: print(f"«{s}» in L-3 {L3.count(s)}, in L-4 {L4.count(s)}")
