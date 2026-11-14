"""REFEREE successor 30: P-N5-QUIET L-4 = L-2 (fed89346) + R-L, R-U, R-B2, R-Q, R-T, R-G (fixes entries 3-4, claude/l-new 87603d07,
table rows; R-U's «…» filled from L-2's own text between the table's fixed ends; not the lane's scripts). Usage: quiet_l4.py L2 OUT"""
import sys, hashlib
L = open(sys.argv[1], encoding="utf-8").read()
X_ = "for an algorithm polynomial on every parity game and §4 says a bound on a restricted class"
R = [("R-L", "with F′_B of RESULTS R121 (P-N5-ASC, to land first);", "with F′_B of RESULTS R121 (P-N5-ASC);"),
     ("R-U", "; G-N5-TIME stays OPEN; TARGET.md §2 (M4) asks " + X_ + " is not M4: not M3, not M4, not a step-4 pass, not a TARGET.md claim (P-N5-QUIET",
             "; TARGET.md §2 (M4) asks " + X_ + " is not M4, so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (P-N5-QUIET"),
     ("R-B2", "(P-N5-QUIET, docs/new/P-N5-QUIET.md with fixes entry 1, docs/new/P-N5-QUIET-fixes.md; L-NEW successor 62)",
              "(P-N5-QUIET, docs/new/P-N5-QUIET.md with its fixes entries 1-3, docs/new/P-N5-QUIET-fixes.md; L-NEW successors 62, 64 and 65)"),
     ("R-Q", "(Corollary ASC-T) if every seq_t(v) has at most B ascents for every vertex v,",
             "(Corollary ASC-T) with seq_t(v) and its ascents as in RESULTS R121, if every seq_t(v) has at most B ascents for every vertex v,"),
     ("R-T", "T-QUIET: Tfail 0 (unit: runs with T > Q + (Q + 1)L; same set as QUIET)",
             "T-QUIET: Tfail 0 (unit: runs with T_CYC > Q + (Q + 1)L, Q the number of loud steps; same set as QUIET)"),
     ("R-G", "changes movers after its first fallback); DATA, clause by clause (scope IDEAL-CYC",
             "changes movers after its first fallback); the step β_g ∉ Π(y) for boundary targets y in (Q5)'s F4′ (else E(y) ⊇ S, against y's "
             "class) is referee-originated (REFEREE R-P-N5-QUIET §3 (Q4), l. 118-120, REFEREE 28), signed by both referees; DATA, clause by "
             "clause (scope IDEAL-CYC")]
X = L
for k, o, n in R:
    print(k, "old in L-2", L.count(o)); assert L.count(o) == 1 and X.count(o) == 1; X = X.replace(o, n)
b = X.encode(); d = m = 0
for c in X:
    d += (c == "(") - (c == ")"); m = min(m, d)
print("parens", X.count("("), X.count(")"), "min depth", m, "| newlines", X.count("\n"), "| bars", X.count("|"),
      "| predicted L-4 sha1", hashlib.sha1(b).hexdigest(), len(b), "B")
open(sys.argv[2], "w", encoding="utf-8").write(X)
