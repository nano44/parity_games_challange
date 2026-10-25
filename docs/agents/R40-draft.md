# Draft RESULTS R40 (Lead, 2026-10-25 15:20Z by date -u) (rev. 15:40Z: C49 E-1, N-1, N-2) — to CHECKER C49 — LANDED in RESULTS Results 15:55Z (CHECKER C49 2b540583 + Addendum 1 cc26fd23 PASS), after R39

### R40 [refereed-only] N5 on one-Odd-choice games: between consecutive fallbacks of a scope run with r above the fallback level, coarse values freeze and routes walk back (FZ, BF, RB, WALK), no evicted vertex lies on the threat's cycle and the threat's play avoids the evicted set after a rise (CYC-EV, TEV-FB), so the ENT setting is empty (ENT-X) and every level-M block has at most one dirty interval, giving at most 2·n·n_E fallbacks of level ≥ 0 per scope run (NJB-A, D1, PL-S″) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C49.md, checker PENDING)
- Object (packet P-N5-ENT, added at l-si 3126857, pinned trunk 765e893, unchanged during review): docs/si/P-N5-ENT-box11.md, sha1
  4fd22be79f7050a7f466288c76eea8bfe2f669d0 (L-SI successor 6, Opus 5.5). The referees' notes are collected by the lane in
  docs/si/P-N5-ENT-fixes-box11.md (l-si b6b8f85b, sha1 72d052b5bc24ef57752924d61ec1b46fd8fc6452, L-SI successor 7: joint verdicts,
  N-ENT-1..3, the R36 status line); on trunk; repairs only.
  Setting as in RESULTS R31, R35 and R37 (𝒞^1O; scope run S; fallbacks, gates, gate levels, M_k; COARSE_L, (C1)-(C7); b_k(y); θ, w, r;
  R̄ / R / F; (h); THR; blocks, intervals, D_M). SETTING (Σ): k0 < k are consecutive fallbacks of S, L := M_{k0} ≥ 0, and r_s > L for
  every s ∈ [k0+1, k]; c is the common cycle node of θ and w on S; H := V_{>max(L, rank c)}; Ev := F_{k0+1} ∖ F_{k0}; A := P(θ_{k0}) ∩ H,
  B := P(θ_k) ∩ H; a RISE is an S4a step in (k0, k) that changes COARSE_L(θ); the ENT setting is (Σ), a rise and M_k = L (R37 (f)).
  (P) := for one-player games, a positional Even strategy with no improving edge is optimal (R18's premise; RESULTS R36).
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Facts (Σ1)-(Σ6) (from landed results): no fallback and τ constant in (k0, k); (h) and (A_s) on [k0, k]; no leave (F_k ⊆ F_s for
      s ∈ [k0+1, k], Ev ∩ F_k = R_{k0} ∩ F_k); M_k ≤ L (CLS2); c ∈ F_{k0} ∩ F_k; after a rise B ≠ A.
  (b) Lemma FZ: if v ∈ F_k, then v ∈ F_s for s ∈ [k0+1, k] and COARSE_L(Ξ_k v) = COARSE_L(Ξ_{k0} v). Lemma BF: if v is Even,
      v ∈ R_{k0} ∩ F_k and a := σ_{k0}(v), then COARSE_L(b_k v) = COARSE_L(Ξ_{k0} a), both with cycle node c.
  (c) Lemma RB: if moreover a ∈ R̄_k, then COARSE_L(Ξ_k a) = COARSE_L(Ξ_{k0} a). Corollary WALK (a)-(c): along the k0-route of
      v0 ∈ R_{k0} ∩ F_k, the first vertex a_j back in R̄_k has COARSE_L(Ξ_k a_j) = COARSE_L(Ξ_{k0} a_j); if the k0-route after v0 is low,
      then (π_{a_j}^k ∩ H) ⊔ B = A.
  (d) Lemma CYC-EV ((Σ) and a rise; M_k = L not assumed): no vertex of Ev ∩ F_k lies on C_k, the σ_k-cycle of c. This form implies the
      CYC-EV of docs/si/P-N5-RL-fixes-box10.md (fixes ac027458, signed in REFEREE A2 and REFEREE-2 Addendum A, not landed under RESULTS
      R37 by the Lead ruling of 12:58Z): its proof uses only M_k ≤ L (N-ENT-1, both referees).
  (e) Proposition TEV-FB ((Σ) and a rise): the σ_k-play of the threat x_k := σ̄_k(o) avoids Ev. (This is the dead CONJECTURE TEV at the
      single state t = k; at S4a states TEV is FALSE, RESULTS R37.)
  (f) Theorem ENT-X, signed CONDITIONAL on (P) by both referees: the ENT setting is empty; equivalently, if k0 < k are consecutive
      fallbacks of a scope run with M_{k0} = M_k = L ≥ 0 and r > L on [k0+1, k], then COARSE_L(θ) does not change in (k0, k). Proof: R37
      (f) EV+ against (e). Corollaries, signed CONDITIONAL on (P) by both: NJB-A (an interval of a level-M block, M ≥ 0, with r > M on
      [f_i + 1, f_{i+1}] is clean), D1 (every level-M block has D_M ≤ 1: only the straddling interval can be dirty), PL-S″ (every scope run
      has at most Σ_{M≥0} n_E(1 + D_M) ≤ 2·n·n_E fallbacks of level ≥ 0, without REL(S); compare R35 PL-S′). (P) enters only through
      EV+ ⇐ FREE-FREEZE ⇐ BL (c), i.e. (P) on G_τ[F_k]; REFEREE's §C records that RESULTS R36 (d) states P1 for exactly G[X], G_τ and
      G_τ[F_k], so given R36 (landed) ENT-X, NJB-A, D1 and PL-S″ hold without condition (as R37 records for EV, EV+, TEV-RED′). REFEREE-2's
      §C (C.1) records the same conclusion: with P1 landed, §4-§5 become unconditional; the check that R36 (d) names G_τ[F_k] is
      REFEREE's.
- Not signed (packet §6): CONJECTURE NJB in full (open only for the straddling interval, where r reaches M and NL and FZ are
  unavailable; straddling intervals occur 0 times in the data); TEV at S4a states (FALSE, RESULTS R37: tev_cex_n40, tevlast_cex_n40);
  the level −1 fallbacks per scope run (OPEN here; lane work after the pin, P-N5-LV pinned 601df6e and N5-LV4 / N5-LV5, in the referee
  queue).
- Honest limits: (i) SUBCLASS 𝒞^1O. (ii) PL-S″ bounds fallbacks of level ≥ 0 per scope run only; level −1 fallbacks, scope runs per
  phase beyond R38 SCOPE-COUNT, out-of-scope fallbacks, S4a steps and phases are OPEN, so G-N5-TIME stays open. (iii) The hypotheses of
  CYC-EV, TEV-FB and ENT-X ((Σ) with a rise) occur in NO data of either referee or the lane; they rest on their proofs. The packet's
  "vacuous everywhere" is too strong for the corollaries: NJB-A's hypothesis (an interval with r > M throughout) occurs, always clean
  (REFEREE-2 698 / 601 / 701 library (Σ)-pairs with M_k = L; REFEREE 654, all of its (Σ)-pairs) (N-ENT-2, both referees). (iv) The packet's §0 status of the
  RL report and of P-N5-P1 is stale: R36 and R37 have landed (N-ENT-3). (v) Lane work after the pin (N5-STR, N5-STR2: NL=, CONJECTURE)
  is not part of this entry.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE cyc_probe.py (own engine; logs rl_logs/cyc_*.txt):
  NAMED 262 + LIB 377 + tev_cex_n40 15 (Σ)-pairs (the tev_cex_n40 row is report text, no committed log;
  CHECKER's re-run and REFEREE-2's engine agree); FZ 17,116, BF 1,614, RB 938, WALK 1,669 checks; 0 failures (FZ, BF, RB, WALK,
  M_k ≤ L, Ev on C_k); 0 pairs with a rise; pair / RB / WALK counts equal the lane's. REFEREE-2 (own code; own / random / SPEC traces):
  66,655 batch runs and 4 climbs (62,036 runs, seeded with L-RED's TEV instances), 0 violations; (Σ)-pairs 756 / 660 / 760 library and
  134,200 in climbs, none with a rise; control: without a rise the threat's play meets Ev in 64 / 60 / 65 library pairs; after a rise
  following a fallback with r > L the scope run has no further fallback (62 library rises: r drops to ≤ L 38, N5 stops 13, the λ-phase
  ends 6, H2 fails 5; 26,665 in climbs). On tev_cex_n40 the two engines agree (15 pairs; FZ 414, BF 19, RB 16, WALK 19). Lane rb.py,
  straddle.py: 0 violations.
- Signatures: REFEREE docs/referee/R-N5-ENT.md (referee 55a3f6f, successor 8; §C d6b8aef): FZ, BF, RB, WALK, CYC-EV, TEV-FB SIGNED;
  ENT-X, NJB-A, D1, PL-S″ SIGNED CONDITIONAL ON (P); no gaps; in §C: R36 lifts the condition. REFEREE-2 docs/referee-2/R2-N5-ENT.md
  (referee-2 b7df84b, successor 9; §C f33884e): FZ, BF, RB, WALK (a)-(c), CYC-EV, TEV-FB and (Σ1)-(Σ6) SIGN; ENT-X, NJB-A, D1, PL-S″ SIGN
  CONDITIONAL ON (P); notes N-ENT-1..3; no gap. §C: verdicts identical; joint gap map empty; N-ENT-1..3 ACCEPTED (N-ENT-2 missed by
  REFEREE); one wording difference ("vacuous"), not a verdict.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
