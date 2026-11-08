#!/usr/bin/env python3
# P-N5-QUIET line L-2 generator (L-NEW successor 64). From the repo root: python3 experiments/new/box194/mkl2_194.py
# L-2 = L-1 + QT-L1..QT-L6 exactly (Lead ruling 06:39Z; REFEREE 28 R-P-N5-QUIET §5, strings copied verbatim from REFEREE's
# docs/referee/scratch/quiet_linefix.py at claude/referee a233f356; REFEREE-2 33 Addendum 1, claude/referee-2 11a7a911, withdraws its
# W-1..W-3 in favour of QT-L4, QT-L1, QT-L3). Asserts L-1's sha1, each old string once in L-1, no overlap, and the predicted sha1
# fed893462811ea10d0b99622dcbb31f7b50b6d47 (5,131 B) reproduced by both referees.
import hashlib
L = open("docs/new/P-N5-QUIET-line-L1.txt", encoding="utf-8").read()
assert hashlib.sha1(L.encode()).hexdigest().startswith("62de9075"), "L-1 changed"
CH = [
 ("QT-L1", "[OPT] = RESULTS R57 (b)'s standing SPEC premise as landed in R104 («that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance», «used in two forms: S1's σ̄, and τ̄ on the dual game, are pointwise optima»; Lead reading 00:36Z that this covers IDEAL-CYC's σ̄_t, for the referees), optionally RESULTS R21 (a);",
  "[OPT] (σ̄_t is optimal at every vertex at once against σ_t) = RESULTS R118's σ̄, Odd's optimal counterstrategy for the order ⊴, as used in R118 (b) (F3's proof in the frozen P-N5-XICYC §3, l. 75: «σ̄_t is optimal at every vertex at once ([VJ])»), and RESULTS R21 (a) («(Odd's best reply σ̄_k is pointwise optimal in G_{σ_k})»); RESULTS R57 (b) concerns the output of SPEC's S1 procedure and is not used;"),
 ("QT-L2", "(b) F1, F3 and F4′'s stated clause", "(b) F1, F2, F3 and F4′'s stated clause"),
 ("QT-L3", "[E-LEV] is R104 (vi)'s packet §3.1 order (docs/red/P-N5-REALIZE.md l. 88) by Lead reading 23:54Z, else a hypothesis;",
  "[E-LEV] is a hypothesis (the e-priorities of R104's packet §3.1, docs/red/P-N5-REALIZE.md l. 88, satisfy it, but R104 (vi) leaves them to that packet as immaterial to its own results, so R104's line does not fix them);"),
 ("QT-L4", "«T bounds IDEAL-CYC iterations; on Γ3 this bounds N5′-xi only up to its first fallback, and only under REACH3-CYC; nothing is claimed about post-fallback iterations, N5′-xi's total count, N5 or general games»",
  "T bounds IDEAL-CYC iterations only; nothing is proved on Γ3: by RESULTS R118 (k) and (l), under REACH3-CYC's premises, N5′-xi from S3 on Γ3(G) makes Howard steps on Γ3 up to its first fallback, a run that can differ from the IDEAL-CYC run at exact VJ ties (R118's DATA), and a Γ3 form of this proof (not given here) would bound N5′-xi only up to its first fallback; nothing is claimed about post-fallback iterations, N5′-xi's total count, N5 or general games"),
 ("QT-L5", "1,000 random genomes rand191.rgen seed 2):", "1,000 random genomes rand191.rgen seed 2, d 1-6, w 1-3, degree 2-3):"),
 ("QT-L6", "CN2: cnlow 0 (unit: (state, vertex) pairs; same runs)",
  "CN2: cnlow 0 (unit: (state, vertex) pairs under (σ_t, σ̄_t); other positional pairs: no separate DATA; same runs)"),
]
pos = []
for nm, o, n in CH:
    assert L.count(o) == 1, (nm, L.count(o)); i = L.find(o); pos.append((i, i + len(o), nm))
pos.sort(); assert all(a[1] <= b[0] for a, b in zip(pos, pos[1:])), "overlap"
for nm, o, n in CH: L = L.replace(o, n)
b = L.encode("utf-8"); h = hashlib.sha1(b).hexdigest()
assert L.count("\n") == 1 and "|" not in L and L.count("(") == L.count(")")
print("QT-L1..QT-L6 old once each, applied; sha1", h, len(b), "bytes")
assert h == "fed893462811ea10d0b99622dcbb31f7b50b6d47" and len(b) == 5131, "differs from the prediction"
open("docs/new/P-N5-QUIET-line-L2.txt", "w", encoding="utf-8").write(L)
