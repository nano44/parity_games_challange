# Draft RESULTS R39 (Lead, 2026-10-25 14:22Z by date -u) (rev. 14:39Z: REFEREE-2 OUT §C 2a9e8db0 filled in) (rev. 14:54Z: C48 E-1, E-2, E-3) — to CHECKER C48 — LANDED in RESULTS Results 15:09Z (CHECKER C48 3d6dcbc8 + Addendum 1 d22ddb69 PASS), after R38

### R39 [refereed-only] N5 on one-Odd-choice games: fallbacks at H1 ∧ ¬H2 states are evictions and θ-flat (SPLIT, F-FLAT), crossings and fallbacks per HN stretch are bounded by breaks (EPOCH), Ξ freezes on R̄ once no gate enters it (FREEZE-STEP, TAIL), and for τ(o) = o in case A no vertex enters R after a fallback while θ is constant (NO-ENTRY-A), so out-of-SN fallbacks per phase are polynomial in θ-changes (NE-COUNT); in case B every R → R̄ gate at a fallback is length-only (CASE-B-LEN) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C48.md, checker PENDING)
- Object (packet P-N5-OUT, added at l-new b1a43578, pinned trunk 719ce66, unchanged during review): docs/new/P-N5-OUT-box37.md, sha1
  9f032e616b515d703da4939cc1b0de89eb658aba (L-NEW successors 16 (proofs) and 17 (packet, filled-in steps), Opus 5.5). The referees'
  notes are collected by the lane in docs/new/P-N5-OUT-fixes-box37.md (l-new dd3f780b, sha1 640a5db215e7d5e2bcdc3b335ae5e4972fed1fb2,
  L-NEW successor 17: OUT-R1 = N-OUT-2, OUT-N1 = N-OUT-3, N-OUT-1, N-OUT-4); on trunk; repairs only.
  Setting as in RESULTS R21 and R38 (𝒞^1O; phase = (λ_Ξ, τ)-phase = joint λ-phase (R38 (a)); R_k, R̄_k, F_k, routes π_z; H1, H2; θ, w,
  c_θ; crossings, entries, evictions; Iσ_k; n_E; K := n_E(2n − 1)). An HN STATE has H1 ∧ ¬H2; an HN STRETCH is a maximal run of
  consecutive HN states of one phase. A BREAK of S is an entry preceded in S by an eviction with no entry in between; B, X_S, f_S are
  the numbers of breaks, crossings and fallback transitions of S. For τ(o) = o with an H1 state, CASE A: rank(o) > rank(c_θ); CASE B:
  rank(c_θ) > rank(o).
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P):
  (a) Lemma SPLIT: at an in-phase transition with H1 ∧ ¬H2 at k, a non-fallback has R_k ⊆ R_{k+1} and an Even S4c fallback has
      R̄_{k+1} ⊆ R̄_k; so inside an HN stretch every crossing is an entry at an S4a step or an eviction at a fallback, never both.
  (b) Corollary EPOCH (corrected form): X_S ≤ 2(n − 1)(B + 1) and f_S ≤ K(X_S + 1) + X_S (premise FB-INT, RESULTS R38 (d)). The
      "+ X_S" is needed: an evicting fallback is a crossing and lies in no crossing-free run (REFEREE-2's O-1 on P-N5-SCOPE; both
      referees). The superseded successor-16 forms without it are NOT signed.
  (c) Lemma F-FLAT: at an in-phase Even S4c fallback with H1 ∧ ¬H2 at k, Ξ_{k+1} = Ξ_k on F_k and θ_{k+1} = θ_k; inside an HN stretch θ
      changes only at S4a steps.
  (d) Lemma FREEZE-STEP: at an in-phase transition with H1 ∧ ¬H2 at t, H1 at t+1, θ_{t+1} = θ_t and no gate (y, z) ∈ Iσ_t with
      z ∈ R̄_t: (i) R̄_{t+1} ⊆ R̄_t with routes unchanged; (ii) Ξ_{t+1} = Ξ_t on R̄_{t+1}; (iii) no gate into R̄_{t+1}. Corollary TAIL: from
      such a state to the end of the stretch or the first θ-change, nothing enters R, R̄ only shrinks and Ξ is frozen on R̄.
  (e) Theorem NO-ENTRY-A (τ(o) = o, case A): if an Even fallback a → a+1 is taken at a ∈ S and θ is constant on [a, b] ⊆ S, then the
      invariant INV(t) (no F → R̄ gate; every R → R̄ gate has lev < rank(o)) holds on [a, b], no transition of [a, b] is an entry, R̄ only
      shrinks, and Ξ_t(z) ≡ Ξ_a(z) for t ∈ [a, b] and z ∈ R̄_t (the same cycle node, and P agrees on vertices of rank ≥ rank(o)). The base cites FBL-N (i) (RESULTS R21 (c)) + F1 (RESULTS R17 (a)) in
      place of Step (K) (R23 (a), "inside a phase"), so b = a with a phase-exiting fallback is covered (OUT-R1 = N-OUT-2, citation).
  (f) Corollary NE-COUNT (τ(o) = o, case A; θ a parameter): (a) every break has a θ-change at an S4a step after its eviction and no
      later than its entry, so B ≤ θ_S; (b) X_S ≤ 2(n − 1)(θ_S + 1), f_S ≤ K(X_S + 1) + X_S; (c) over the phase, N_HN ≤ ⌊T_ph/2⌋ + 1 ≤
      ⌊T*/2⌋ + 1 (TOGGLE-COUNT, RESULTS R34 (e)), f_HN ≤ (K + 1)(2(n − 1)·θ_ph + (2n − 1)·N_HN) and X_HN ≤ 2(n − 1)(θ_ph + N_HN).
  (g) Lemma CASE-B-LEN (τ(o) = o, case B): at an HN state a where an Even fallback is taken, every R → R̄ gate (v, z) has
      lev(Ξ_a(σ_a v), Ξ_a(z)) = −1 and z's route longer than σ_a(v)'s (same citation repair as (e), N-OUT-2). Remark W-SIDE (same
      setting): if z's route avoids v (Case 1), the W-difference of the gate is W-unfavourable to z, or empty with Ω(o) even; if
      π_z = q · v · π_{σ_a v} (Case 2), the top t of q ∪ {v} has reward(t) ≤ reward(o); its "Consequence" paragraph is a
      READING and is not signed.
- Not signed (packet §7): CONJECTURE NO-ENTRY in general; CONJECTURE NO-ENTRY-B (τ(o) = o, case B) is FALSE
  (experiments/new/box38/instances/nebc_cex_n14.pg, sha1 399119af; the HN fallback 1 → 2 makes a length-only R → R̄ switch and S4a
  2 → 3 enters 4 with θ = (12, ∅, 2) constant; Lead re-run n5 9/5, Oink zlk OK strategies verified, one Odd choice vertex);
  CONJECTURE NO-ENTRY for τ(o) ≠ o is FALSE when c_w ≠ o, in both cases (experiments/new/box38/instances/tauw_A_cex_n24.pg, sha1
  e29908d5, n5 16/3; tauw_B_cex_n24.pg, sha1 c0ad4f0c, n5 10/4; Lead re-runs, Oink OK, one Odd choice vertex) (L-NEW successor 17,
  after the pin; N-OUT-4: REFEREE-2 reproduces a break with no θ-change between eviction and entry on all three; REFEREE's probe finds
  every signed check holding on them); the dead end
  ROUTE-FROZEN FALSE (experiments/new/box37/instances/rfroz_cex_n16.pg, sha1 a9b40395; Lead re-run); the OPEN core: θ-changes per HN
  stretch (θ_S, θ_ph), HN stretches per phase for τ(o) ≠ o, OTHER states (H1 ∧ H2 ∧ ¬H3). §7's reduction "given NO-ENTRY" is valid only
  in case A with c_w = o.
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase. (ii) NE-COUNT is polynomial GIVEN θ_ph (and T_ph ≤ T*); θ_ph is OPEN, so the
  out-of-SN fallbacks per phase and G-N5-TIME stay open; NO-ENTRY-A covers τ(o) = o in case A only. (iii) FB-INT's per-run term is never
  used in data: every fallback with both ends in an HN stretch is a crossing (library 107 / 107 in the lane's count, 103 / 103 in
  REFEREE's); CASE-B-LEN's hypothesis occurs in the batches only on the counterexample nebc_cex_n14 (4 gates). (iv) N-OUT-1: the
  filled-in "target o" step of SPLIT (b) / F-FLAT is correct and redundant (landed FBL-N has o ∈ R). (v) Lane work after the pin
  (P-N5-NEB: NO-ENTRY-A′ for c_w = o, any τ(o); RISE; Theorem BRK; OUT-1) is not part of this entry.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE out_probe.py (own code on its rl_engine; logs
  rl_logs/out_lib37.txt, out_named.txt): lib37 270 𝒞^1O games plus 3 named, SPLIT 521 + 6 S4a / 105 + 22 fallbacks, F-FLAT 127,
  FREEZE-STEP 391 transitions, 121 HN stretches, NO-ENTRY-A 88 runs / 889 states, CASE-B-LEN 4 gates, 0 failures. REFEREE-2 (own
  checker; own / random / SPEC traces): 66,655 batch runs and 4 climbs (741,432 runs), 0 violations; CASE-B-LEN's hypothesis 4 gates in
  the batch and 1,291,962 in climbs, both W-SIDE cases; NO-ENTRY-A 2.35 M (a, b) pairs; mutation controls (drop "θ constant", case B
  read as case A, drop FREEZE-STEP's gate hypothesis) fail as expected; the lane's fbsplit numbers reproduced (115 HN stretches,
  107 / 107 crossing fallbacks, breaks 8 + 3); NE-COUNT (c)'s per-phase bounds (N_HN, f_HN, X_HN, T_ph ≤ T*) 0 violations (max f_HN 12
  on wd16_s2, max θ_ph 11; REFEREE checked (c) as arithmetic only). Lane: fbsplit.py library 115 stretches, 20,000 random games, 0 failures. Lead re-ran
  wd16_s2 (n5 19/14, Oink OK).
- Signatures: REFEREE docs/referee/R-N5-OUT.md (referee fa08687, successor 8; §C a8b8ef3): SPLIT, EPOCH, F-FLAT, FREEZE-STEP, TAIL,
  NO-ENTRY-A, NE-COUNT (a)-(c), CASE-B-LEN, W-SIDE SIGNED; notes OUT-R1, OUT-N1; no gaps. REFEREE-2 docs/referee-2/R2-N5-OUT.md
  (referee-2 dfcaae67, successor 9; §C 2a9e8db0): SPLIT, EPOCH (corrected), F-FLAT, FREEZE-STEP, TAIL, NO-ENTRY-A, NE-COUNT (a)-(c),
  CASE-B-LEN, W-SIDE SIGN; notes N-OUT-1..4; no gap. §C (both): verdicts identical; joint gap map empty; N-OUT-1..4 ACCEPTED
  (N-OUT-2 = OUT-R1, extended to CASE-B-LEN; N-OUT-3 = OUT-N1); REFEREE-2's §C checks the fixes file 640a5db2 item by item (all
  correct) and the c_w ≠ o qualification of N-OUT-4 on its own traces.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
