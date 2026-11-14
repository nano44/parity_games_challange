#!/usr/bin/env python3
"""REFEREE-2 successor 35: byte test of P-N5-END line L-3 (claude/l-new 8b67d40e) against L-2 (2fcee038, e8a8ac51…). Own code.
Strings: L-R1, N-1, N-2 from R2-P-N5-END.md «Line L-2» (claude/referee-2 9b3cc9b6); EL-1, EL-2 from REFEREE 29's R-P-N5-END.md §C
(claude/referee 407f4a21 l. 212-215; EL-1's parenthesis placed after «is NOT proved», EL-2 «§4 (A), (B)»). Usage: bt_l3.py (repo root)"""
import subprocess, hashlib, difflib
def show(rev, p): return subprocess.run(["git", "show", f"{rev}:{p}"], capture_output=True, check=True).stdout.decode("utf-8")
L2 = show("2fcee038", "docs/new/P-N5-END-line-L2.txt"); L3 = show("8b67d40e", "docs/new/P-N5-END-line-L3.txt")
h = lambda s: hashlib.sha1(s.encode()).hexdigest()
print("L-2", h(L2), len(L2.encode()), "B;  L-3", h(L3), len(L3.encode()), "B")
R2 = show("9b3cc9b6", "docs/referee-2/R2-P-N5-END.md"); R29 = show("407f4a21", "docs/referee/R-P-N5-END.md")
norm = lambda s: " ".join(s.split())
S = [("L-R1", "so the K-config changes only at a fallback and the run cannot stop before one",
              "so the K-config leaves κ0 only at a fallback and the run cannot stop before one", R2),
     ("N-1", "has L(G) = 1 and N5 makes 3 iterations (F = 1)",
             "has L(G) = 1 (IDEAL run read with B_s the set of β-ids on its eventually periodic X-chain; R104's IDEAL run is defined on IDEAL-ACYC) and N5 makes 3 iterations (F = 1)", R2),
     ("N-2", "ctrl2 e0fail 200 and e1fail 200 (unit: states)",
             "ctrl2 e0fail 200 (unit: states) and e1fail 200 (unit: iterations before the first fallback)", R2),
     ("EL-1", "their transfer to the Γ3 run (equal runs at exact VJ ties) is NOT proved",
              "their transfer to the Γ3 run is NOT proved (the Γ3 run can differ from the IDEAL-CYC run at exact VJ ties, R118's DATA)", R29),
     ("EL-2", "REFEREE 29 R-P-N5-END §4 (claude/referee e4cb208a)", "REFEREE 29 R-P-N5-END §4 (A), (B) (claude/referee e4cb208a)", R29)]
exp = L2
for k, o, n, src in S:
    # the referee-side pieces must be in the referee's text (whitespace-normalised)
    piece = {"L-R1": n, "N-1": "(IDEAL run read with B_s the set of β-ids on its eventually periodic X-chain; R104's IDEAL run is defined on IDEAL-ACYC)",
             "N-2": "e1fail 200 (unit: iterations before the first fallback)", "EL-1": "(the Γ3 run can differ from the IDEAL-CYC run at exact VJ ties, R118's DATA)",
             "EL-2": "§4 (A), (B)"}[k]
    print(f"{k}: old in L-2 {L2.count(o)}, old in L-3 {L3.count(o)}, new in L-2 {L2.count(n)}, new in L-3 {L3.count(n)}, referee text has its piece {norm(piece) in norm(src)}")
    exp = exp.replace(o, n)
print("L-3 == L-2 + S1-S5:", L3 == exp, "; parens", L3.count("("), L3.count(")"), "; pipes", L3.count("|"), "; lines", L3.count("\n"))
d = [l for l in difflib.ndiff(L2.split(" "), L3.split(" ")) if l[:1] in "+-"]
print("word-level diff tokens:", len(d))
