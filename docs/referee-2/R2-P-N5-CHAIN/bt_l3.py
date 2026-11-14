#!/usr/bin/env python3
"""REFEREE-2 successor 35: byte test of P-N5-CHAIN line L-3 (claude/l-new 219e3933) against L-2 (8b67d40e, e481d260…) + my R-1, R-2,
R-4, N-1 (strings from R2-P-N5-CHAIN.md at claude/referee-2 0e5c7c37). Own code. Usage: bt_l3.py (repo root)"""
import subprocess, hashlib
def show(rev, p): return subprocess.run(["git", "show", f"{rev}:{p}"], capture_output=True, check=True).stdout.decode("utf-8")
L2 = show("8b67d40e", "docs/new/P-N5-CHAIN-line-L2.txt"); L3 = show("219e3933", "docs/new/P-N5-CHAIN-line-L3.txt")
rep = " ".join(show("0e5c7c37", "docs/referee-2/R2-P-N5-CHAIN.md").split())
h = lambda s: hashlib.sha1(s.encode()).hexdigest()
print("L-2", h(L2), len(L2.encode()), "B;  L-3", h(L3), len(L3.encode()), "B; parens", L3.count("("), L3.count(")"), "pipes", L3.count("|"), "lines", L3.count("\n"))
S = [("R-1", "QUIET3: wfail 0 (unit: quiet windows)", "QUIET3: wfail 0 (unit: quiet steps past the L3-th step of their window)"),
     ("R-2", "T-QUIET3: Tfail 0 (unit: runs)", "T-QUIET3: Tfail 0 (unit: runs with T3 > Q + (Q + 1)·L3, Q the number of loud steps; the Σ_v form is not counted)"),
     ("R-4", "LOC-K2-3: k2fail 0 (unit: states)", "LOC-K2-3: k2fail 0 (unit: states with σ̄_t(K2) ≠ r; the conjunct Ω_t(r) ◁ Ω_t(K2) is not counted)"),
     ("N-1", "spec on 100 runs and 5 pinned genomes, check196.out)", "spec on 100 runs, and 5 pinned genomes in xi mode, check196.out)")]
exp = L2
for k, o, n in S:
    print(f"{k}: old in L-2 {L2.count(o)} / L-3 {L3.count(o)}; new in L-2 {L2.count(n)} / L-3 {L3.count(n)}; old and new verbatim in my report {f'«{o}»' in rep and f'«{n}»' in rep}")
    exp = exp.replace(o, n)
print("L-3 == L-2 + R-1 + R-2 + R-4 + N-1:", L3 == exp)
