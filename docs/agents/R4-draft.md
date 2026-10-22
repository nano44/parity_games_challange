# Draft RESULTS R4 (Lead, 2026-10-17 09:50Z; rev. 10:00Z per CHECKER C4 O-1..O-4, gap 3, optional) — LANDED as RESULTS R4 (2026-10-17 10:20Z, CHECKER PASS fd8e3eb; WM citation moved to §18k per N-3)

### R4 [refereed-only] GAP-C Step 5 for A_DTL: KT survives every depth-0 P piece, with (ACYC) as the only open hypothesis (2026-10-17) — partial step-4 lemma (not M3, not a step-4 pass)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). G' = the game at the
  start of a search(p); D = W_p(G'). A depth-0 P piece is, as in STEP5.md line 9, "the −1 branch with Q empty, dtl.cpp
  961-991" at depth 0 (best_vertices 643-776 returned −1); R is its context and Y_0 the set it removes. Packet: docs/alg/STEP5.md and docs/alg/GAP-C.md §18g-§18k at trunk 8f41be8.
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (1) KT(R) definitions; KT(G') holds when D ≠ ∅; KT(R_end) fails.
  (2) Lemma NT-f: the final pruning round of a −1 call accepts no stored tangle in its region loop.
  (3) FM (Z_f ⊆ Z^r for every round r of a −1 call) and WM (Z^r ⊆ A^r_t, GAP-C §18h), as consequences of NT-f.
  (4) The (YZ) reading of dtl.cpp 961-976, and (YZ) ⇐ (ACYC).
  (5) Lemma P-KT, given (YZ): at every depth-0 P piece with D ∩ R ≠ ∅, KT(R \ Y_0) holds (witnessed at level c1).
  Hence: at every depth-0 P piece with D ∩ R ≠ ∅, KT(R \ Y_0) holds, with (ACYC) as the only open hypothesis.
- Signatures: REFEREE docs/referee/R-STEP5.md (referee 8c2d012): (1)-(3) SIGN, (4) SIGN + SIGN WITH GAPS, (5) SIGN WITH GAPS.
  REFEREE-2 docs/referee-2/R2-STEP5.md (referee-2 ce37984, comparison §9 at a18e9e5): (1),(2),(4),(5) SIGN WITH GAPS, (3) SIGN.
  Independent (REFEREE-2 read docs/referee/ only after pushing ce37984). No REJECT.
- Gaps (union of both reports). G-S5-1..5 are closed in the reports and are to be imported into the author's text; G-S5-6 is
  OPEN; G-S5-7 lists dependencies checked only for this use:
  G-S5-1 NT-f (D) needs DTL-proof Lemma 1.5a (top ∈ t, tpr(t) = max pr(t)), re-derived by both referees (F2.1 / G2).
  G-S5-2 (YZ) ⇐ (ACYC) (iii): both inclusions, regions and Dom part as least fixed points with tangle retrial at escape pops,
         DTL-proof Lemma 1.2 (G4.1).
  G-S5-3 trigger case: a new opponent vertex whose R-edges all lie in earlier parts would have been taken there (G4.2 / G3).
  G-S5-4 P-KT case c1 = 0 (p Even): A^r_{−1} := Z^r, candidacy at dtl.cpp 714 (G5.1 / G4).
  G-S5-5 "all its edges" in A_c means edges of G' (REFEREE-2 G1; REFEREE wording note); whole-game edges make P-KT (4) false.
  G-S5-6 OPEN hypothesis (ACYC): the new part of a Dom(prevV) straddle contains no tangle-graph cycle. DATA only.
  G-S5-7 Lemmas 1.5a and 1.2 of DTL-proof.md checked by the referees only for this use; sorted indices (oink.cpp:35);
         O1 (index order follows priority) is an Oink order-datum fact; positional determinacy and D = W_p(G')
         (DTL-proof.md Lemma 1.4c; REFEREE §6.6, REFEREE-2 'standard parity-game facts named in (1)'), standard.
         Nothing Lean-checked.
- Scope: depth-0 P pieces of one search only. The S step ((S-LOW), data) and T step (CORE-PASS + REC, data), hence (K-in)
  and GAP-C as a whole, are NOT established. GAP-A untouched. Gauntlet step 4 stays open.
- Data (evidence, not part of the signed statement): REFEREE step5_probe.py (Python ref; 243 of the 254 corpus files: n > 80 and one unreadable file skipped; both orders):
  NT-f 0/8,323 and 0/8,145, YZ 0/4,476 and 0/4,377. REFEREE-2 instrumented pinned C++ (docs/referee-2/R2-STEP5/), 254 corpus
  + 3,000 random/unions + 9,000 climb mutants (each in 2 in-orders), 32,026 runs: 0 NT-f / FM / YZ / ACYC / tpr violations. In the corpus the only straddling Dom
  firing is strfam_S5_n46 stable order (both referees; Lead and CHECKER re-ran pinned Oink: 6 iterations, verified); REFEREE-2's
  climbs from it (18,000 runs) produce many straddling firings, none with a cyclic new part or a YZ failure (no total count
  kept). CHECKER C4 (checker 7d7c6fb) reproduced REFEREE's probe and REFEREE-2's corpus and random parts exactly.
