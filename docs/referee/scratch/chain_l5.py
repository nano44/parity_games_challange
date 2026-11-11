"""REFEREE successor 30: P-N5-CHAIN L-5 = L-4 (a69c8aa9) + R-U, R-L1, R-L2 in that order (CHECKER C139 §4, claude/checker 389d19f8;
wrapped lines joined with one space), strings typed from C139, not from the lane's script. Usage: chain_l5.py L4 OUT"""
import sys, hashlib
L = open(sys.argv[1], encoding="utf-8").read()
M = "TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4"
R = [("R-U", "; G-N5-TIME stays OPEN, N5′-xi stays a CANDIDATE (D1); " + M + ": not M3, not M4, not a step-4 pass, not a TARGET.md claim (P-N5-CHAIN",
             "; N5′-xi stays a CANDIDATE (D1); " + M + ", so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (P-N5-CHAIN"),
     ("R-L1", "CONDITIONAL on the unlanded lane packets P-N5-END (ENDGAME-3) and P-N5-ASC §4 (its abstract core and F′; RESULTS R121 when landed))",
              "CONDITIONAL on P-N5-END's Theorem ENDGAME-3 (RESULTS R124) and P-N5-ASC §4 (its abstract core and F′; RESULTS R121))"),
     ("R-L2", "lane packets, not landed: P-N5-END's Theorem ENDGAME-3 (frozen at l-new 131b4c1c, REFEREE 29 SIGN) for CHAIN3, P-N5-ASC §4's "
              "game-free abstract core CS(M) and its constants F′_B (RESULTS R121 when landed) for HUB-ASC-G3 and CHAIN3;",
              "RESULTS R124's Theorem ENDGAME-3 (P-N5-END) for CHAIN3, RESULTS R121's game-free abstract core CS(M) (Lemma SKELETON, Theorem "
              "HUB-ASC(B); P-N5-ASC §4) and its constants F′_B for HUB-ASC-G3 and CHAIN3;")]
X = L
for k, o, n in R:
    print(k, "old in L-4", L.count(o)); assert L.count(o) == 1 and X.count(o) == 1; X = X.replace(o, n)
b = X.encode(); d = m = 0
for c in X:
    d += (c == "(") - (c == ")"); m = min(m, d)
print("parens", X.count("("), X.count(")"), "min depth", m, "| newlines", X.count("\n"), "| bars", X.count("|"),
      "| stale words", sum(X.count(w) for w in ("unlanded", "not landed", "when landed", "to land")),
      "| predicted L-5 sha1", hashlib.sha1(b).hexdigest(), len(b), "B")
open(sys.argv[2], "w", encoding="utf-8").write(X)
