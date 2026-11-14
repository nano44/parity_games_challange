#!/usr/bin/env python3
# REFEREE-2 successor 37: byte test of P-N5-SPLIT line L-1 against R-1..R-6 (R2-P-N5-SPLIT.md «For the line» + Addendum 1).
# Usage (repo root): python3 -I docs/referee-2/R2-P-N5-SPLIT/bt_l1.py L1.txt PACKET.md FIXES.md CHAIN_L5.txt
# Own code; the lane's generator is not imported. Prints one line per check, then «FAILS n».
import sys, hashlib, re
L1, PK, FX, L5 = (open(p, encoding="utf-8").read() for p in sys.argv[1:5])
raw = open(sys.argv[1], "rb").read()
L = L1.rstrip("\n"); ws = lambda s: " ".join(s.split()); PKw, FXw = ws(PK), ws(FX)
fails = 0
def ck(name, ok, info=""):
    global fails
    fails += (not ok); print(("PASS " if ok else "FAIL ") + name + (" :: " + info if info else ""))
ck("sha1 634b2fdf", hashlib.sha1(raw).hexdigest().startswith("634b2fdf"), hashlib.sha1(raw).hexdigest() + " " + str(len(raw)))
ck("one line, no |", L.count("\n") == 0 and "|" not in L)
# R-1
for frag in ["passes K0 iff", "iff it passes K3", "cycle node is in the closed core"]:
    ck("R-1 false sentence absent: " + frag, frag not in L)
LS2 = "(LEX-Λ) is applied only to non-core vertices (pads), where P-N5-CHAIN's W-1 repair holds"
ck("R-1 LS-2 string (accepted for R-1 in Add. 1)", L.count(LS2) == 1)
ck("R-1 my parenthetical: pads of movers and gates; fixes entry 3, R-W", "(pads of movers and gates; P-N5-CHAIN fixes entry 3, R-W" in L)
ck("R-1 credit", L.count("referee-originated: REFEREE-2 R2-P-N5-SPLIT W-1") == 1)
ck("R-1 (LEX-Λ) named only once", L.count("LEX-Λ") == 1, str(L.count("LEX-Λ")))
# R-2
ck("R-2 CONDITIONAL string", "each statement PROVED and CONDITIONAL on RESULTS R125 (P-N5-CHAIN)" in L)
# fix 1 (first run): every later «PROVED» must be a back-reference to the lemmas, not a new claim
refs = ["every PROVED-lemma counter 0", "all PROVED statements SURVIVE"]
ck("R-2 every other PROVED is a back-reference", L.count("PROVED") == 1 + sum(L.count(r) for r in refs), str([m.start() for m in re.finditer("PROVED", L)]))
# R-3
pos = [m.start() for m in re.finditer(r"\[E-LEV\]", L)]
a0 = L.index("(Lemmas ASC-WIT, ASC-ROOT, under HYPOTHESIS [E-LEV]"); a1 = L.index("(premises:")
ok3 = len(pos) == 2 and pos[0] > a0 and pos[0] < a1 and L.startswith("[E-LEV] only in ASC-WIT and ASC-ROOT", pos[1])  # fix 2: slice length was 32, string is 37
ck("R-3 [E-LEV] only at ASC-WIT/ASC-ROOT + the 'only in' clause", ok3, str(pos))
ck("R-3 HYPOTHESIS once", L.count("HYPOTHESIS") == 1)
# R-4
ck("R-4 run name", L.startswith("On HOW3(G), i.e. N5′-xi from S3 on Γ3(G) until its first fallback"))
ck("R-4 reduction direction", "so C polynomial ⇐ max over y, b, J of Dhi_y(b, J) polynomial (a reduction, not an equivalence)" in L)
ck("R-4 SPLIT-COUNT never called equivalence", "SPLIT-COUNT is a reduction" in L and "SPLIT-COUNT are equivalences" not in L)
ck("R-4 G-N5-TIME stays OPEN", L.count("G-N5-TIME stays OPEN") == 1)
ck("R-4 nothing for N5 / outside Γ3", "nothing is claimed for N5 (SPEC S4a), outside Γ3(G)" in L)
# R-5
for s in ["unit: (v, I, y); SPLIT-COUNT's first inequality with Dhi_y(b, J_b) replaced by the number of distinct values of E(b) ∩ U_y at the pair's own y-tops, a lower bound",
          "rh2fail (unit: same-pair couples, all pairs t < t′; PAIR-SPLIT)",
          "playfail, kindfail, trfail and wlamfail are definition checks without a firing control",
          "on the 28 frozen instances max c_y ≤ 6", "large zero counts are DATA, not evidence"]:
    ck("R-5 " + s[:48], s in L)
# R-6: none of F2,(Core),(E-DOM),[G3],[DEF],(R),(P),CYC inside the R125 list
r0 = L.index("(premises: RESULTS R125 (P-N5-CHAIN): "); r1 = L.index("; [DEF] = RESULTS R104", r0)
r125 = L[r0+len("(premises: RESULTS R125 (P-N5-CHAIN): "):r1].split(", ")
bad6 = [x for x in r125 if x in ("F2", "(Core)", "(E-DOM)", "[G3]", "[DEF]", "(R)", "(P)", "CYC", "[OPT]")]
ck("R-6 R125 list free of non-R125 facts", not bad6, str(r125))
ck("R-6 frozen-text citation", "(R), (P), (E-DOM), (Core) in its W-1-repaired reading (the only edge into the eight-vertex core from outside is pb_g → K0), F2 and CYC: P-N5-CHAIN's frozen text (l-new 93531b03, sha1 6e613ba7, §2 and §4)" in L)
ck("R-6 landed sources", "[DEF] = RESULTS R104's" in L and "[G3] = RESULTS R117's" in L and "[OPT] = RESULTS R118 (b) and RESULTS R21 (a)" in L)
# each R125-list name must occur in CHAIN's L-5 (the R125 line)
L5w = ws(L5); miss = [x for x in r125 if (x.replace("T-QUIET3 with L3", "T-QUIET3")) not in L5w]
ck("R-6 every R125-list name occurs in CHAIN L-5", not miss, str(miss))
# meaning: formulas against packet + fixes (whitespace-normalised)
for f in ["T3 ≤ (1 + n3·((2M + 3)(M + 1) − 1) + Rtop)·(L3 + 1)", "Rtop ≤ n3·T3",
          "(1 + n3·((2M + 3)(1 + M·C) − 1))·(L3 + 1)", "3M", "C(M, 2)", "max(0, A_xy − 1)", "2·Dhi_y + 1", "A ≤ max(1, T3)", "C ≤ max(1, T3)"]:
    ck("formula in packet/fixes: " + f, f in L and (f in PKw or f in FXw))
print("FAILS", fails)
