"""REFEREE successor 30: P-N5-CHAIN L-4 = L-3 (c484795c) + R-G3, R-W, R-B3 in that order (fixes entry 3 table, claude/l-new 87603d07;
typed from the table, not the lane's script). Usage: chain_l4.py L3 OUT"""
import sys, hashlib
L = open(sys.argv[1], encoding="utf-8").read()
R = [("R-G3", "is a separate gauntlet step-4 item; DATA, clause by clause (unit:",
              "is a separate gauntlet step-4 item; the step β_g ∉ Π(y) for the boundary points y in QUIET3's (Q5) F4′ (an e-face target y of "
              "class (w, S ∖ {e}): else S = E(β_g) ⊆ E(y); the pb exit: Π = {K0, K3}; w: Π = ∅) is referee-originated (REFEREE R-P-N5-QUIET §3 "
              "(Q4), l. 118-120, REFEREE 28, for P-N5-QUIET's form; REFEREE 30 and REFEREE-2 35, R2-P-N5-CHAIN Addendum 3, for the Γ3 form), "
              "signed by both referees; DATA, clause by clause (unit:"),
     ("R-W", "signed by both referees; DATA, clause by clause (unit:",
             "signed by both referees; (F-cls3)'s convexity and E-MON3's reason hold for non-core vertices, the eight core vertices being "
             "constant (referee-originated: REFEREE-2 R2-P-N5-CHAIN W-1, signed by both referees); DATA, clause by clause (unit:"),
     ("R-B3", "frozen at l-new 93531b03, sha1 6e613ba7; source box 196, docs/new/N5-CHAIN-box196.md; L-NEW successor 64;",
              "frozen at l-new 93531b03, sha1 6e613ba7, with its fixes entries 1-3, docs/new/P-N5-CHAIN-fixes.md; source box 196, "
              "docs/new/N5-CHAIN-box196.md; L-NEW successors 64-65;")]
X = L
for k, o, n in R:
    print(k, "old in L-3", L.count(o), "| in current", X.count(o)); assert X.count(o) == 1; X = X.replace(o, n)
b = X.encode(); d = m = 0
for c in X:
    d += (c == "(") - (c == ")"); m = min(m, d)
print("parens", X.count("("), X.count(")"), "min depth", m, "| newlines", X.count("\n"), "| bars", X.count("|"),
      "| predicted L-4 sha1", hashlib.sha1(b).hexdigest(), len(b), "B")
open(sys.argv[2], "w", encoding="utf-8").write(X)
