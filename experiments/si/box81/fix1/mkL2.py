#!/usr/bin/env python3
"""L-SI P-ACYC fixes entry 1: build line L-2 from the frozen line L-1 (docs/si/P-ACYC-line-L1.txt, frozen at e3ac4b06) by exact string
replacements; every Old string must occur exactly once; every new count is asserted against the fix1 outputs. Prints L-2.
Usage: mkL2.py REPO_ROOT"""
import sys, os, re
R = sys.argv[1]; F = os.path.join(R, "experiments", "si", "box81", "fix1")
L1 = open(os.path.join(R, "docs", "si", "P-ACYC-line-L1.txt")).read()
def last(f): return open(os.path.join(F, f)).read().strip().splitlines()[-1]
def kv(line): return dict(re.findall(r"(\w+) ([\d.]+)", line.split(":", 1)[1]))
A, B, CT = kv(last("pacyc81t_agen_300_7.out")), kv(last("pacyc81t_towers.out")), kv(last("pacyc81t_cyclic_control.out"))
for d, st in ((A, "768"), (B, "44")):
    assert d["states"] == st and d["taubad"] == "0" and d["nonstd"] == "0" and d["nofallback"] == "0" and d["bigT"] == "0" and d["notbeta"] == "0", d
assert (CT["states"], CT["notbeta"], CT["C"], CT["R"], CT["taubad"], CT["nonstd"]) == ("59", "121", "15", "25", "0", "0"), CT
LC = open(os.path.join(R, "experiments", "si", "box81", "out", "lemma81_cyclic_control.out")).read()
assert "states 59 notbeta 121 nonstrict 121 C 15 R 25" in LC
RES = open(os.path.join(R, "docs", "RESULTS.md")).read()
assert RES.count("S1's σ̄, and τ̄ on the dual game, are pointwise optima") >= 1
REP = [
    # AC-L1 (REFEREE 28), verbatim
    ("the order ⊴ and σ̄ of R118 [VJ]):",
     "the order ⊴ and σ̄ of R118 [VJ]; for the corollary's iterations and fallback, SPEC S4 and S4c, RESULTS R15's object):"),
    # AC-L2 (REFEREE 28), verbatim
    ("PROVED-CONDITIONAL on R118's REACH3-CYC, whose premises RESULTS R117's entry signs for acyclic Ξ-graphs)",
     "PROVED-CONDITIONAL on R118's REACH3-CYC, whose [REACH-L] premises RESULTS R117's entry signs for acyclic Ξ-graphs, with Lemma "
     "K2-r and [1E-N3] as listed in R118 (k))"),
    # AC-L3 (REFEREE 28), form A, verbatim
    ("L6Z_KILL238_d28 (44 states), σ̄ off the β-face in 0 (state, gate) pairs, C 0, R 0, runs with T_CYC > N 0 (lemma81.py, IDEAL-CYC)",
     "L6Z_KILL238_d28 (44 states), each run from the genome's stored start (IDEAL-CYC) or from S3 (Γ3), σ̄ off the β-face in 0 "
     "(state, gate) pairs (BETA-ACYC's no-e-vertex clause: no separate DATA), C 0, R 0, runs with T_CYC > N 0 (lemma81.py, IDEAL-CYC; "
     "ACYC-LIN from other mover states: no separate DATA)"),
    # W-3 fix (a) + D-1 (REFEREE-2 32) ⊃ AC-L4 (REFEREE 28): ONE replacement, REFEREE-2 Add. 1's combined string (6c937bc6), fix (a) form
    ("σ̄ off the β-face 0, non-standard states 0, genomes with first fallback after iteration N + 1 0;",
     "σ̄ off the β-face 0, states that are not standard (σ off the movers and τ) 0, genomes with no fallback 0, genomes with first "
     "fallback after iteration N + 1 0 (k = T3 + 1 is R118 (k)'s own clause, and N5's L(G) is R117's: no separate DATA);"),
    # AC-L5 (REFEREE 28) = D-2 (REFEREE-2 accepts AC-L5's string, Add. 1) + D-3 (REFEREE-2's insertion before «)»)
    ("control, five Ξ-cyclic genomes: σ̄ off the β-face 121, C 15, R 25",
     "control, five Ξ-cyclic genomes rd2_d3, rd2_d4, rd3_d3, rf_d4, RS2 (59 states; the same counts on IDEAL-CYC and along N5′-xi on "
     "Γ3; e-priorities ordered by (lev, gate index), as in ref gamma3.build): σ̄ off the β-face in 121 (state, gate) pairs, C 15, R 25"),
]
L2 = L1
for old, new in REP:
    assert L2.count(old) == 1, ("old string not unique", old)
    L2 = L2.replace(old, new)
assert L2.count("(") == L2.count(")"), "parens"
sys.stdout.write(L2)
