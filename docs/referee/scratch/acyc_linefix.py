"""REFEREE successor 28: apply the required L-1 changes AC-L1..AC-L5 (R-P-ACYC §5) to P-ACYC-line-L1.txt; each old string must occur
exactly once in L-1 and the changes must not overlap; prints counts, parenthesis balance, and the sha1 / size of the predicted line.
Usage: acyc_linefix.py L1.txt OUT.txt"""
import sys, hashlib
L = open(sys.argv[1], encoding="utf-8").read()
CH = [
 ("AC-L1", "the order ⊴ and σ̄ of R118 [VJ]):",
  "the order ⊴ and σ̄ of R118 [VJ]; for the corollary's iterations and fallback, SPEC S4 and S4c, RESULTS R15's object):"),
 ("AC-L2", "PROVED-CONDITIONAL on R118's REACH3-CYC, whose premises RESULTS R117's entry signs for acyclic Ξ-graphs)",
  "PROVED-CONDITIONAL on R118's REACH3-CYC, whose [REACH-L] premises RESULTS R117's entry signs for acyclic Ξ-graphs, with Lemma K2-r and [1E-N3] as listed in R118 (k))"),
 ("AC-L3", "L6Z_KILL238_d28 (44 states), σ̄ off the β-face in 0 (state, gate) pairs, C 0, R 0, runs with T_CYC > N 0 (lemma81.py, IDEAL-CYC)",
  "L6Z_KILL238_d28 (44 states), each run from the genome's stored start (IDEAL-CYC) or from S3 (Γ3), σ̄ off the β-face in 0 (state, gate) pairs (BETA-ACYC's no-e-vertex clause: no separate DATA), C 0, R 0, runs with T_CYC > N 0 (lemma81.py, IDEAL-CYC; ACYC-LIN from other mover states: no separate DATA)"),
 ("AC-L4", "genomes with first fallback after iteration N + 1 0;",
  "genomes with no fallback 0, genomes with first fallback after iteration N + 1 0 (k = T3 + 1 is R118 (k)'s own clause, and N5's L(G) is R117's: no separate DATA);"),
 ("AC-L5", "control, five Ξ-cyclic genomes: σ̄ off the β-face 121, C 15, R 25",
  "control, five Ξ-cyclic genomes rd2_d3, rd2_d4, rd3_d3, rf_d4, RS2 (59 states; the same counts on IDEAL-CYC and along N5′-xi on Γ3): σ̄ off the β-face in 121 (state, gate) pairs, C 15, R 25"),
]
pos = []
for nm, o, n in CH:
    c = L.count(o); i = L.find(o); pos.append((i, i + len(o), nm)); print(nm, "old occurs", c, "at", i)
    assert c == 1
pos.sort()
assert all(a[1] <= b[0] for a, b in zip(pos, pos[1:])), "overlap"
N = L
for nm, o, n in CH: N = N.replace(o, n)
for nm, o, n in CH: print(nm, "new occurs in result", N.count(n))
print("L-1 parens", L.count("("), L.count(")"), "| predicted L-2 parens", N.count("("), N.count(")"))
open(sys.argv[2], "w", encoding="utf-8").write(N)
b = N.encode("utf-8"); print("predicted line: sha1", hashlib.sha1(b).hexdigest(), len(b), "bytes; L-1:", hashlib.sha1(L.encode()).hexdigest(), len(L.encode()), "bytes")
