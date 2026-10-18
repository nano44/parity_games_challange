# Draft RESULTS R14 (Lead, 2026-10-18 01:16Z by date -u) (rev. 01:24Z: REFEREE §C abc5185; rev. 01:28Z: L-ALG imports §23v; rev. 01:38Z: CHECKER C14 E-1, N-1) — NOT LANDED; awaiting CHECKER re-diff

### R14 [refereed-only] Packet 11 on A_DTL: Lemma CHANGE-NEW, F_R ≤ 3·#fired⁺(R) unconditionally, and GAP-A ⇔ (CTX⁺) ∧ (FIRED⁺-R) (2026-10-18) — partial step-4 reformulation (not M3, not a step-4 pass)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). Packet pinned at
  trunk 5909724, docs/alg/GAP-A-M.md §23s (line 3313) (L-ALG succ. 7), building on RESULTS R10 (EXACT), R11 (EXACT*,
  F_R ≤ 3·N*_R), R9 (budget). For a context R in a phase, D_R is the number of consecutive visit pairs of R whose set-level
  traces differ; #fired⁺(R) is the number of distinct tangles that fire at R (in a region step or in the threshold loop) in
  the phase; ntv(x) is the number of stored tangles when visit x starts.
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) Lemma CHANGE-NEW: if two consecutive visits x < y of R differ at set level, then a tangle born between them (index in
      [ntv(x), ntv(y))) fires at R in visit y. Proof: within a phase the set-level trace of a best_vertices call is a function
      of (R, p, alive T, order datum) only (both referees' state inventories: V rebuilt from R 648/662-667; Candidates written
      at 714 before read at 735; Q empty on entry; str read only at 73; this->G read only at 132 and changed only at 1035;
      X, W, depth not read); tangles are only appended (stored 440/458-461; tpr = −1 only at 134; G changes only at 1035, ending
      the phase), so T_x ⊆ T_y; at the first differing tattr call the inputs agree; a region step is handled by EXACT/EXACT*
      (E_y ∩ T_x = E_x), the threshold step by DTL-proof Lemma 1.2 (all of Z pushed at 724, Gx = R).
  (b) Corollary: birth intervals of consecutive pairs are disjoint (ntv non-decreasing), so D_R ≤ #fired⁺(R); N*_R ≤ D_R; with
      R11's F_R ≤ 3·N*_R: F_R ≤ 3·#fired⁺(R) with NO premise. Hence GAP-A ⇐ (CTX⁺) ∧ (FIRED⁺-R), given STR-DET, where
      (FIRED⁺-R): #fired⁺(R) is polynomial per phase for every first-difference context R.
  (c) Honest limit: the bound is tight (spp_chain_up_n43: root D_R = #fired⁺ = 41, both orders), and over all contexts the
      conditional is an EQUIVALENCE: GAP-A ⇔ (CTX⁺) ∧ (FIRED⁺-R) up to polynomial factors, given STR-DET (GAP-A gives
      (FIRED⁺-R) via Lemma W, ≤ n·S tangles per phase, and (CTX⁺) via R5 (k)); a reformulation, not a reduction to something
      easier. At G′ alone (FIRED⁺-R) is implied by GAP-A but does not imply it; on chain families where every first
      difference is at the root (spp_chain_up_n43) it equals S − 1 (both referees). (L-ALG's unrefereed note at the end of
      GAP-A-M §23s relates the root case to (SPP); not part of R14.)
  (d) Data: CHANGE-NEW held at every differing pair checked: REFEREE p11probe.py (corpus 138 files, both orders, AT the first
      differing tattr) 1,160/1,160 and 1,231/1,231, and on spp_chain_up_n43 + stealonce_viol_n76 with dtl_changenew.py 89/89
      (stable) and 49/49 (Oink); REFEREE-2 (268 files, both orders) 3,028/3,028 and
      3,066/3,066; L-ALG dtl_changenew.py 37,361/37,361; D_R > #fired⁺(R) in 0 contexts.
- Signatures: REFEREE docs/referee/R-P11.md (referee fc86762; draft f953548; comparison §C abc5185): (a) SIGN WITH GAPS, closed
  (N11-a1, G11-a1); (b) SIGN; (c) CONFIRMED (equivalence); (d) CONFIRMED. REFEREE-2 docs/referee-2/R2-P11.md (referee-2
  aeedd00; comparison §5 bb8a625): (a) SIGN (N11-a1); (b) SIGN (N11-b1); (c) CONFIRMED (equivalence); (d) own probe, 0
  failures. Independent (each read the other's P11 report only after pushing its own). No REJECT; full agreement after comparison.
- Gaps (union). G-R14-1..3 closed in the reports and imported by L-ALG (GAP-A-M §23v, l-alg 510cb18, which marks N11-b1
  as one signature, written before REFEREE §C confirmed it; §23s not rewritten); G-R14-4..5 OPEN; G-R14-6 dependencies:
  G-R14-1 STR-DET is not needed for the determinism step: best_vertices reads str only at 73, to guard a str write (REFEREE
          N11-a1 = REFEREE-2 N11-a1). STR-DET remains a hypothesis of the GAP-A conditional through R9.
  G-R14-2 The threshold step follows from DTL-proof Lemma 1.2 directly (all of Z pushed at 724, Gx = R), not from "the §22r
          Corollary" (REFEREE G11-a1; REFEREE-2 §1 makes the same fix in substance).
  G-R14-3 Sharper use (REFEREE-2 N11-b1; CONFIRMED by REFEREE §C abc5185, so two signatures): an e*-at-R transition contains a differing
          consecutive pair and, given STR-DET (c), overlaps occur only where T is constant, so #(e*-at-R) ≤ D_R ≤ #fired⁺(R)
          (2·D_R without STR-DET); hence S − 1 ≤ Σ_R #fired⁺(R) + n(|C_T| + |C_Dom|) + 1, with no H and no F_R.
  G-R14-4 OPEN (FIRED⁺-R): DATA only; ≤ |R| on all data (tight: fired18_stable_n20 stable, #fired⁺ = |R|); at G′ it is necessary, not sufficient, and equals S − 1 on chain families;
          route via (EXIT_c) (GAP-A-M §23u, SKETCH, gap G23u, unrefereed).
  G-R14-5 OPEN (CTX⁺): DATA only; |C_bv| ≤ S − 1 per phase, best contexts/transitions ≈ 0.5 at n = 20, 30, 40 (L-RED box 9,
          unpinned, in progress).
  G-R14-6 Dependencies: R10 (EXACT), R11 (EXACT*, F_R ≤ 3·N*_R), R9 (budget), R8 (STR-DET), R5 (k), Lemma W (GAP-A-M), DTL-proof
          Lemma 1.2; also open, inherited: (ACYC) (G-S5-6, a GAP-C item). Nothing Lean-checked.
- Scope: an unconditional per-context bound (F_R ≤ 3·#fired⁺(R)) and a reformulation of GAP-A, not a bound. GAP-A stays OPEN on
  (CTX⁺) and (FIRED⁺-R) (the alternative sufficient pair (CTX⁺) and (EXIT_c) is RESULTS R13), all DATA only. Not the L32 single-statement
  criterion. GAP-C is separate. Gauntlet step 4 stays open.
