# Draft RESULTS R12 (Lead, 2026-10-17 20:40Z by date -u) (rev. 20:40Z: REFEREE §C 3785d3f; rev. 20:45Z: L-ALG imports §23k; rev. 20:50Z: CHECKER C12 E-1, N-1, N-2) — NOT LANDED; awaiting CHECKER re-diff

### R12 [refereed-only] Packet 9 on A_DTL: R11 (d) with the factor k, Lemma CHARGE, and GAP-A ⇐ (CTX⁺) ∧ (STEAL-DEPTH_D, D constant) ∧ (FIRED-R) (2026-10-17) — partial step-4 reduction (not M3, not a step-4 pass)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). Packet pinned at
  trunk c5e2b4d, docs/alg/GAP-A-M.md §23f (line 2904) and §23g (line 2944) (L-ALG succ. 7), building on RESULTS R10, R11 and
  the R11 POST-LANDING NOTE ((STEAL-ONCE*) FALSE, DE20). A quadruple is q = (R, round, top τ, fired tangle t); k_q is the
  number of consecutive visit pairs of R at which q is a relevant steal (an EVENT of q); Q := (|R| + 1)·|R|·#fired(R) bounds
  the number of q with k_q > 0. A RE-STEAL is an event of q after an earlier event of q. P(τ⁺) is the round's prefix before τ.
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) F_R ≤ 3·N*_R ≤ 3·Σ_q k_q ≤ 3·k_R·Q (k_R = max_q k_q). Hence, given STR-DET and (CTX⁺) for the sum over contexts:
      GAP-A ⇐ (CTX⁺) ∧ (STEAL-POLY_sum), where (STEAL-POLY_sum): Σ_q k_q is polynomial per phase for every first-difference
      context R; and GAP-A ⇐ (CTX⁺) ∧ (STEAL-POLY_k) ∧ (FIRED-R), where (STEAL-POLY_k): k_R is polynomial.
  (b) Lemma CHARGE: every re-steal of q at pair i, with the previous event of q at pair j < i, has a CAUSE: an event at a pair m
      with j < m < i, at a step strictly earlier than (round, τ) in the step order (rounds ascending, tops descending).
      Distinct re-steals of one q have distinct causes (their open pair intervals are disjoint).
  (c) Depth: depth(first event) = 0; depth(re-steal) = 1 + min over its causes. If E_d is the number of events of depth d,
      E_0 ≤ Q and E_d ≤ Q·E_{d−1}; so (STEAL-DEPTH_D) "every event has depth ≤ D" gives Σ_q k_q ≤ 2Q^{D+1}. With (FIRED-R)
      (Q polynomial) this gives (STEAL-POLY_sum) for CONSTANT D only (D = O(log n) gives quasi-polynomial). Depth ≤ #steps − 1
      ≤ (|R|+1)|R| − 1 is proved, which gives only exp(Θ(n² log n)). Hence GAP-A ⇐ (CTX⁺) ∧ (STEAL-DEPTH_D, D constant)
      ∧ (FIRED-R), given STR-DET.
  (d) Data check on stealonce_viol_n76 (RESULTS DE20): one re-steal (stable order; tangle 7 at (round 4, top 18), k = 2, depth
      1, single cause: the depth-0 relevant steal of tangle 9 at (round 4, top 66)); none in the Oink order.
- Signatures: REFEREE docs/referee/R-P9.md (referee 72313f3 + a3e9566; comparison §C 3785d3f): (a) SIGN (its note N9-a1 WITHDRAWN in §C; accepts REFEREE-2 N9-a1); (b) SIGN
  WITH GAPS, closed (G9-b1, G9-b2; G23g-1/2 checked; N9-b1); (c) SIGN WITH GAPS, closed (G9-c1); (d) CONFIRMED (dtl_stealdepth
  unmodified + own probe p9charge.py). REFEREE-2 docs/referee-2/R2-P9.md (referee-2 2612634; comparison §5 19a94b8): (a) SIGN
  (N9-a1: name the form of STEAL-POLY); (b) SIGN WITH GAPS, closed (G9-b1, G9-b2 = REFEREE N9-b1); (c) SIGN (N9-c1); (d) own
  pinned-C++ probe an9.py. Independent (each read the other's P9 report only after pushing its own). No REJECT; full
  agreement after comparison.
- Gaps (union). G-R12-1..4 closed in the reports and imported by L-ALG (GAP-A-M §23k, l-alg 67b9e05; §23f-§23g not rewritten); G-R12-5..7 OPEN; G-R12-8 dependencies:
  G-R12-1 Notation: §23g's P_{j+1}(τ), P_i(τ) must read P(τ⁺) (the prefix before τ); as written "t ∩ P_i(τ) = ∅" is false
          since t fired inside region τ (REFEREE G9-b1 = REFEREE-2 G9-b1).
  G-R12-2 An intermediate visit may have fewer than r rounds: a "no candidates" stop (dtl.cpp 716/765) repeats its last round
          (virtual round, C3); a V′ = ∅ stop (768-771) forces an earlier-round steal (REFEREE G9-b2; REFEREE-2's rounds
          convention, R2-P7 §3).
  G-R12-3 The forms of (STEAL-POLY): the sum form needs no (FIRED-R) in (a); the k_R form and (c) need (FIRED-R) (REFEREE-2
          N9-a1, REFEREE G9-c1). Cite dtl.cpp 136-139, not dtl_pyref (REFEREE N9-b1 = REFEREE-2 G9-b2).
  G-R12-4 §23f's remark "the factor tightens to 2 given STR-DET (REFEREE-2 R2-P8 §7; one signature)": REFEREE N9-a1 called it
          misattributed; REFEREE-2 §5 and the Lead checked c2ac652:docs/referee-2/R2-P8.md §7 (line 139ff, "The same device
          tightens G-P7-c2 / G8-1 from 3 to 2, given STR-DET (optional)"); the citation is correct; the device is REFEREE's
          R-P7 §C2; REFEREE §C (3785d3f) WITHDRAWS N9-a1 (it had read R2-P8 at b8fdd76, before §7). Unused here.
  G-R12-5 OPEN (STEAL-DEPTH_D, D constant): DATA only. Every re-steal found has depth 1: 1 in the corpus (stable), 64 in 320
          random tie-break runs (REFEREE-2, all on stealonce_viol_n76, k_q ≤ 2); L-ALG: k max 1 on big unions (n ≤ 120,
          both orders); no re-steal elsewhere. Attack in progress (L-RED; L-ALG dtl_depthclimb).
  G-R12-6 OPEN (FIRED-R): DATA only, no route (L-ALG box 8 self-kills FIRED-STEP, FIRED-LAMINAR, FIRED-TOP-INJ, NO-RETURN).
  G-R12-7 OPEN (CTX⁺): DATA only (max 13). (CTX-LAMINAR) self-killed (GAP-A-M §23i).
  G-R12-8 Dependencies: R10 (EXACT, PREFIX-MONO-X and its Corollary incl. V alignment), R11 (a)-(c) (EXACT*, PREFIX-MONO-X*,
          F_R ≤ 3·N*_R), R8 (STR-DET), R9 (budget); also open, inherited: (ACYC) (G-S5-6, a GAP-C item).
          Nothing Lean-checked.
- Scope: a reduction, not a bound. CHARGE turns the steal count into a depth question but does not bound the depth. GAP-A
  stays OPEN on (CTX⁺), (FIRED-R) and (STEAL-DEPTH_D) (or directly (STEAL-POLY_sum)); all are DATA only, and only
  (STEAL-DEPTH) has a proof route. Not the L32 single-statement criterion. GAP-C is separate. Gauntlet step 4 stays open.
