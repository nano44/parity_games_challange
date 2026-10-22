# Draft RESULTS R17 (Lead, 2026-10-22 00:40Z by date -u) — awaits CHECKER C20 re-diff (rev. 01:00Z: C20 E-1, E-2, N-1, N-2; rev. 01:03Z: REFEREE follow-up 708b996 closes G-1P-7)

### R17 [refereed-only] N5 (switch-best) on one-player games: a λ-phase has at most n − 1 value-changing steps, so N5 makes fewer than (n² − n + 1)(n + m) iterations on one-player games (2026-10-22) — a bound on the candidate N5 itself on a subclass that is polynomial by other means (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open)
- Object: docs/new/N5-phase-bound-box10.md §1-§4 (L-NEW successor 4, Fable 5.1), packet P-N5-1P pinned at trunk 26905f0, with addendum A1
  = the SCOPE line and §6 (VJ00 dependency list) at trunk 0f899f3 (29 inserted lines, 0 deleted; §1-§4 unchanged). N5 as specified in
  docs/new/N5-ssi-global.md (SPEC S1-S5; RESULTS R15). Source: Vöge-Jurdziński, BRICS RS-00-48 (pdf sha256 485a12de…). Setting: H a
  one-player game (one player has out-degree 1 everywhere), injective priorities, VJ00 valuation Ω = (cycle node, P, length) with VJ00's
  order; switch-best: ρ_{k+1} = an optimal strategy of the arena H_k in which every vertex x may use {ρ_k(x)} ∪ I_k(x) (VJ00 improving
  edges, §4.4 eq. (2)); λ-phase = a maximal run of steps in which no vertex changes its cycle node.
- Claims signed (both referees, both labelled "(Fable 5.1)"; first signatures after the D12 Opus period, Lead reading L36):
  (a) (V1)/(V2) (prefix equation and prefix monotonicity of values) and (F1)/(F2) (the optimum of a one-player game dominates every strategy
      of that game pointwise; hence Ω_{k+1} ⪰ Ω_k). (F1) has two independent derivations: REFEREE via the dual of VJ00 Lemma 5.5's proof,
      REFEREE-2 via VJ00 (11) in the dual game plus the "⊵" halves of (4)/(6), which VJ00 asserts and REFEREE-2 derived.
  (b) Lemma P (phase progress): in a λ-phase, after k steps every vertex x satisfies Ω_k(x) ⪰ value(r) for every simple path r of at most k
      edges from x to a cycle node of ρ_0 (all four cases, including the cycle-closing cases B1/B2).
  (c) Theorem PH: in a λ-phase, after n − 1 steps every further in-phase step is value-flat, and there are fewer than m such steps; so a
      phase has fewer than n + m steps.
  (d) Corollary 1: switch-best on one-player games makes fewer than (n² − n + 1)(n + m) steps, O(n²·m), at most n³ − n² + n of them
      value-changing. The arena optimum is not unique; the bound holds for every pointwise-optimal choice (step counts depend on the tie-break).
  (e) Corollary 2: on a game in which one player has out-degree 1 everywhere, N5's step for the other player is switch-best, N5's fallback
      (S4c) fires only in the value-flat situation and then leaves no improving edge; so N5 makes fewer than (n² − n + 1)(n + m) iterations on
      one-player games. This closes K8's constant case (τ constant; Even's steps = switch-best on G_c) for every G_c, cyclic or not.
  (f) Corollary 3 (signed as a reading): VJ00 Prop. 7.4's O(n³) holds for the arena-optimum rule; for arbitrary single switches the statement
      is false (CDAG_n, L-NEW). Not an attribution claim about VJ00's intended rule.
  (g) §6 (A1): the proof uses VJ00 §4.2/§4.5 (the order), §5.1 (6)-(10) (path values), (11) on the dual (F1) and §4.4 eq. (2) (improving
      edges); it does NOT use VJ00 Lemma 5.5, 5.7, 5.8, postulates P1/P2/I1/I2, §5.6. So it does not rest on Lemma 5.8 "2 ⇒ 1" or I1/I2, which
      fail at cycle nodes (RESULTS R15 side finding).
- Honest limits: (i) SUBCLASS that is already polynomial: one-player parity games are solvable in polynomial time by other means; the value
  is a bound on N5 itself. (ii) Two-player N5 is NOT covered: Lemma P's statement is FALSE for N5's Even moves inside a σ̄-segment
  (seg_r16, seg_n24: stalls against τ_k), and the count bound does not transfer (vc_g25, sha1 243f890d…: 26 value-changing Even moves in one segment-phase at
  n = 25, one-player bound 24) (docs/new/N5-phase-bound-box10.md §5, DATA). G-N5-TIME stays OPEN; so do the best-reply-change factor of K9
  (three candidate invariants false, docs/new/N5-brchanges-box11.md) and SB1' (O(n)). (iii) Code link (G-N1 = G-N5T-1 = G-1P-6): N5's code
  experiments/new/n5.py agrees with the referees' definitions on all tested runs (REFEREE-2: 34,601 iterations, 522 fallbacks all value-flat;
  REFEREE: 7,224 runs, every iteration the exhaustive arena optimum or S4c), DATA not proof. (iv) G-N5T-3 (R15) untouched: the output
  correctness at S5 still rests on VJ00 Lemma 5.8 "1 ⇒ 2"; the bounds here do not depend on it.
- Data (DATA, not proof): REFEREE (own probe from VJ00 §4, exhaustive arena optimum, three tie-breaks): F1 462,110 strategy comparisons,
  Lemma P 30,958 checks, Theorem PH/phase count/fallback on 21,224 runs (R-N5-1P §6, all nine rows), "no improving edge ⇒ maximum" exhaustively on 7,945 games n ≤ 6,
  0 violations; Lemma P on n5.py's own ph_n48 sequence (45-step phase) over all simple paths of ≤ 8/11/16 edges, 13,325/18,078/24,987
  checks, and over EVERY simple path at every step (n5.py's 47 iterations, the 45-step phase included): 43,781 checks, 0 violations (referee 708b996). REFEREE-2 (own code from the definitions): 8,500 random one-player games (17,000
  runs, 4 tie-breaks), Lemma P 58,534 checks at every in-phase step, arena optimum verified by brute force over 170,544 arena strategies,
  0 violations. Tightness: in-phase n − 1 value-changing steps attained at n = 12 (rel_g12, sbstep rule; n5.py takes 10 from the same start);
  at n = 16 and n = 48 the longest in-phase counts are 14 and 45 (phase_vc.py counts the closing λ-step as well: N-2).
- Signatures: REFEREE docs/referee/R-N5-1P.md (referee dfa87d0; §C 492ad6d; follow-up 708b996): SIGNED WITH GAPS G1-G9. REFEREE-2 docs/referee-2/R2-N5-1P.md
  (referee-2 f954070; §7 addendum 857ce07; §C 498b8c9; stamp correction ec8d7a7): (V1)/(V2), Lemma P and Corollary 1 SIGN; (F1)/(F2), Theorem PH, Corollary 2 and §6 SIGN WITH GAPS; Corollary 3 SIGN as a remark. Both §C: identical
  verdicts, no disagreement; joint gap map G1 = G-1P-4, G2 = G-1P-1, G3 = G-1P-3, G4 = G-1P-5, G5 = N-1, G6 = N-3, G-N1 = G-1P-6, G-1P-2
  separate; all closed or DATA except G7-G9 (= N-4..N-6, citation slips in §6: Improve is §4.4 eq. (2) p. 11; the switch-all fixpoint rule
  relies on Lemma 5.8 "1 ⇒ 2"; Prop. 7.4 is on printed p. 27), corrected by L-NEW in the new §7 (l-new a300339, merged trunk ace3841; §1-§4 and §6 unchanged: 0 deleted lines against 0f899f3); G-1P-7 (Lemma P on ph_n48)
  CLOSED as DATA by REFEREE's full enumeration (referee 708b996; earlier partial checks by REFEREE and L-NEW §7 (lemmaP_paths.py: on ph_n48 the Lemma P instances Theorem PH's proof uses, 111 checks, and all paths x, π^j_z, 166,608 checks, 0 violations, both rules); with it the full statement over all simple paths is checked on every pinned instance up to n = 18 and on ph_n48 (n = 48).
- TARGET.md diff: not a claim of TARGET.md section 1 (one-player games; no statement about general parity games). Gauntlet: partial step-4
  lemma for N5 on a subclass. GAPS G-N5-TIME: K8's constant case closed by this entry on landing; G-N5-TIME open.
