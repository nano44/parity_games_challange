"""REFEREE successor 30: P-N5-CHAIN L-3 = L-2 + REFEREE-2 35's R-1, R-2, R-4 (docs/referee-2/R2-P-N5-CHAIN.md, claude/referee-2
0e5c7c37), plus its optional N-1 (taken by the lane), strings typed from that report. Usage: chain_l3.py L2 OUT"""
import sys, hashlib
L = open(sys.argv[1], encoding="utf-8").read()
R = [("R-1", "QUIET3: wfail 0 (unit: quiet windows)",
              "QUIET3: wfail 0 (unit: quiet steps past the L3-th step of their window)"),
     ("R-2", "T-QUIET3: Tfail 0 (unit: runs)",
              "T-QUIET3: Tfail 0 (unit: runs with T3 > Q + (Q + 1)·L3, Q the number of loud steps; the Σ_v form is not counted)"),
     ("R-4", "LOC-K2-3: k2fail 0 (unit: states)",
              "LOC-K2-3: k2fail 0 (unit: states with σ̄_t(K2) ≠ r; the conjunct Ω_t(r) ◁ Ω_t(K2) is not counted)"),
     ("N-1", "spec on 100 runs and 5 pinned genomes, check196.out)", "spec on 100 runs, and 5 pinned genomes in xi mode, check196.out)")]
X = L
for k, o, n in R:
    print(k, "old in L-2", L.count(o)); assert L.count(o) == 1 and X.count(o) == 1; X = X.replace(o, n)
b = X.encode(); d = m = 0
for c in X:
    d += (c == "(") - (c == ")"); m = min(m, d)
print("parens", X.count("("), X.count(")"), "min depth", m, "| newlines", X.count("\n"), "| bars", X.count("|"),
      "| predicted L-3 sha1", hashlib.sha1(b).hexdigest(), len(b), "B")
open(sys.argv[2], "w", encoding="utf-8").write(X)
