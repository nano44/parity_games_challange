"""REFEREE s31: P-N5-SPLIT line L-1 checks (strings typed from R-P-N5-SPLIT §2/§7 and fixes entry 2; no lane code).
Usage: split_l1.py L1.txt CHAIN_L5.txt RESULTS.md"""
import sys, re
L = open(sys.argv[1], encoding="utf-8").read(); C5 = open(sys.argv[2], encoding="utf-8").read(); R = open(sys.argv[3], encoding="utf-8").read()
n = lambda s: re.sub(r"\s+", " ", s)
print("lines", L.count("\n"), "bars", L.count("|"), "open", L.count("("), "close", L.count(")"))
d = 0; neg = False
for ch in L:
    d += ch == "("; d -= ch == ")"; neg |= d < 0
print("paren depth never negative:", not neg)
must = ["(LEX-Λ) is applied only to non-core vertices (pads), where P-N5-CHAIN's W-1 repair holds",
        "[DEF] = RESULTS R104's definitions of the genome and of Γ(G)", "[G3] = RESULTS R117's definition of Γ3(G)",
        "[OPT] = RESULTS R118 (b) and RESULTS R21 (a)", "(Core) in its W-1-repaired reading", "P-N5-CHAIN's frozen text (l-new 93531b03, sha1 6e613ba7, §2 and §4)",
        "each statement PROVED and CONDITIONAL on RESULTS R125 (P-N5-CHAIN)", "under HYPOTHESIS [E-LEV]", "large zero counts are DATA, not evidence",
        "the open core is max over y, b, J of Dhi_y(b, J)", "a reduction, not an equivalence", "G-N5-TIME stays OPEN",
        "sha1 5bc1b1f3, with fixes entries 1-2", "L-NEW successors 65-67 and 69", "L-RED 60-62"]
for m in must: print(L.count(m), "MUST", m[:70])
bad = ["a play passes K0 iff it passes K3", "iff its cycle node is in the closed core"]
for b in bad: print(L.count(b), "ABSENT", b)
# R125 items cited as RESULTS R125: each must be named in R125's line L-5
for it in ["HOW3", "REACH3-ALL", "F1", "F3", "F4′", "F5", "F6", "DOM", "STRICT", "CN2-3", "LOC-GATE3", "LOC-K2-3", "B-ONLY3", "NO-TIE3", "T-QUIET3", "L3", "E-MON3", "CHAIN-DECOMP3"]:
    print("R125-L5", it, len(re.findall(r"(?<![\w-])" + re.escape(it) + r"(?![\w′-])", C5)))
for it in ["F2", "(Core)", "(E-DOM)", "CYC"]:
    print("R125-L5 (should be cited from frozen text)", it, C5.count(it))
tail = "TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4, so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim"
print("tail in L1", L.count(tail), "in trunk RESULTS", n(R).count(tail))
for q in re.findall(r"«([^»]*)»", L): print("quote", q[:60])
