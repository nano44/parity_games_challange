#!/usr/bin/env python3
# P-N5-QUIET line L-3 generator (L-NEW successor 65). From the repo root: python3 experiments/new/box194/mkl3_194.py
# L-3 = L-2 + R-L, R-U, R-B, R-Q, R-T, R-G (Lead rulings 12:21Z and 12:24Z (R-G, L41; REFEREE 30's reading of REFEREE 28's step), pre-CHECKER, by CHECKER precedents C118 E-1 / C132 E-1, C133 E-3 / C134 E-3,
# C135 E-4). Asserts the frozen packet's sha1, L-2's sha1, each old string exactly once in L-2, one line, no «|», balanced parentheses.
import hashlib
pk = open("docs/new/P-N5-QUIET.md", encoding="utf-8").read()
assert hashlib.sha1(pk.encode()).hexdigest().startswith("066dfc7d"), "frozen packet changed"
L2 = open("docs/new/P-N5-QUIET-line-L2.txt", encoding="utf-8").read()
assert hashlib.sha1(L2.encode()).hexdigest().startswith("fed89346"), "L-2 changed"
R = [("R-L", "with F′_B of RESULTS R121 (P-N5-ASC, to land first);", "with F′_B of RESULTS R121 (P-N5-ASC);"),
     ("R-U", "; G-N5-TIME stays OPEN; TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4: not M3, not M4, not a step-4 pass, not a TARGET.md claim (P-N5-QUIET",
             "; TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4, so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (P-N5-QUIET"),
     ("R-B", "(P-N5-QUIET, docs/new/P-N5-QUIET.md with fixes entry 1, docs/new/P-N5-QUIET-fixes.md; L-NEW successor 62)",
             "(P-N5-QUIET, docs/new/P-N5-QUIET.md with its fixes entries 1-2, docs/new/P-N5-QUIET-fixes.md; L-NEW successors 62 and 64)"),
     ("R-Q", "(Corollary ASC-T) if every seq_t(v) has at most B ascents for every vertex v,",
             "(Corollary ASC-T) with seq_t(v) and its ascents as in RESULTS R121, if every seq_t(v) has at most B ascents for every vertex v,"),
     ("R-T", "T-QUIET: Tfail 0 (unit: runs with T > Q + (Q + 1)L; same set as QUIET)",
             "T-QUIET: Tfail 0 (unit: runs with T_CYC > Q + (Q + 1)L, Q the number of loud steps; same set as QUIET)"),
     ("R-G", "changes movers after its first fallback); DATA, clause by clause (scope IDEAL-CYC",
             "changes movers after its first fallback); the step β_g ∉ Π(y) for boundary targets y in (Q5)'s F4′ (else E(y) ⊇ S, against y's class) is referee-originated (REFEREE R-P-N5-QUIET §3 (Q4), l. 118-120, REFEREE 28), signed by both referees; DATA, clause by clause (scope IDEAL-CYC")]
L = L2
for k, o, n in R:
    assert L2.count(o) == 1, (k, L2.count(o))
    L = L.replace(o, n)
assert L.endswith("\n") and L.count("\n") == 1 and "|" not in L and L.count("(") == L.count(")"), (L.count("("), L.count(")"))
open("docs/new/P-N5-QUIET-line-L3.txt", "w", encoding="utf-8").write(L)
b = L.encode(); print("R-L, R-U, R-B, R-Q, R-T, R-G old once each, applied; sha1", hashlib.sha1(b).hexdigest(), len(b), "bytes; parens", L.count("("), L.count(")"))
