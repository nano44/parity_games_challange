# Draft RESULTS R42 (Lead, 2026-10-25 17:02Z by date -u) — to CHECKER C51

### R42 [refereed-only] N5 on one-Odd-choice games: after an HN fallback with θ constant, a new F → R̄ gate needs an R̄-rise (RISE; high in case A, HIGH-RISE), no vertex enters R when o tops its W-cycle in case A (NO-ENTRY-A′), case-B gates are length-only and their failures need a low rise (CASE-B-LEN′, LOW-RISE′), so every break of an HN stretch is paid by a θ-change or an R̄-rise (Theorem BRK), and for τ(o) = o the out-of-SN fallbacks per phase are polynomial in θ-changes and H1-toggles (OUT-1) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C51.md, checker PENDING)
- Object (packet P-N5-NEB, added at l-new 8ca3571, pinned trunk 314d220, unchanged during review): docs/new/P-N5-NEB-box38.md, sha1
  ba15e51fb02471207b11ecd64e9687a23fe8a744 (L-NEW successor 17, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-NEB-fixes-box38.md (l-new e535e61, sha1 15434c1ca9920b8254ce48834b07cd86f5946837, L-NEW successor 19: NEB-R1 =
  N-NEB-1, NEB-N1..N5, N-NEB-2, N-NEB-3, NEB-B1); on trunk; repairs only.
  Setting as in RESULTS R38 and R39 (𝒞^1O; phase = (λ_Ξ, τ)-phase; R_k, R̄_k, F_k, routes; H1, H2; θ, w, c_θ, c_w; HN states and HN
  stretches; crossings, entries, evictions; breaks; Iσ_k; case A: rank(o) > rank(c_θ), case B: rank(c_θ) > rank(o); K := n_E(2n − 1)).
  An R̄-RISE at t → t+1 is a strict rise of Ξ at some z ∈ R̄_t ∩ R̄_{t+1}; it is HIGH if its level is ≥ rank(o) and LOW if it is
  length-only. "o tops its W-cycle at a" means c_w(a) = o.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P):
  (a) Lemma RISE (any τ(o), cases A and B): if an in-phase Even fallback is taken at a ∈ S (S an HN stretch), θ is constant on [a, t+1],
      no state of [a, t] has an F → R̄ gate and t+1 has one, then there is an R̄-rise at t → t+1.
  (b) Lemma HIGH-RISE (case A, any τ(o), any c_w): in (a), the rise satisfies lev(Ξ_t z, Ξ_{t+1} z) ≥ rank(o).
  (c) Theorem NO-ENTRY-A′ (case A, c_w(a) = o, any τ(o)): with θ constant on [a, b] ⊆ S, the invariant INV(t) (no F → R̄ gate; every
      R → R̄ gate has lev < rank(o)) holds on [a, b], no transition of [a, b] is an entry, R̄ only shrinks, and Ξ_t(z) ≡_o Ξ_a(z) for
      z ∈ R̄_t; in particular no R̄-rise on [a, b] is high. For τ(o) = o this is RESULTS R39 (e) in the general form. The base cites
      FBL-N (i) (RESULTS R21 (c)) + F1 (RESULTS R17 (a)) in place of Step (K) (R23 (a), "inside a phase") (NEB-R1 = N-NEB-1, citation;
      as R39's OUT-R1).
  (d) Lemma CASE-B-LEN′ (case B, c_w(a) = o, any τ(o)): at an HN state a where an Even fallback is taken, every R → R̄ gate (v, z) has
      lev(Ξ_a(σ_a v), Ξ_a(z)) = −1 and z's route longer than σ_a(v)'s.
  (e) Lemma LOW-RISE′ (case B, c_w(a) = o, any τ(o)): INV_B(a) holds (no F → R̄ gate; every R → R̄ gate has level −1); if θ is
      constant on [a, t+1] and INV_B holds on [a, t], then (a) no transition of [a, t+1] is an entry and Ξ_{t+1}(z) ≡_B Ξ_t(z) for
      z ∈ R̄_{t+1}; (b) (ii_B) holds at t+1; (c) if (i) fails at t+1, there is a LOW rise at some z ∈ R̄_t ∩ R̄_{t+1} at t → t+1. (b)
      does not need (i) at t+1 (N-NEB-2, optional).
  (f) Theorem BRK (any τ(o)): for every break of an HN stretch S, with eviction state a and entry k → k+1: (a) in case A with
      c_w(a) = o there is a θ-change in (a, k]; (b) in case B with c_w(a) = o, a θ-change in (a, k] or a LOW rise in [a, k) with θ
      unchanged; (c) in general, a θ-change in (a, k] or an R̄-rise in [a, k) with θ unchanged, HIGH in case A; (d) B_S ≤ θ_S + LR_S + RW_S
      with LR_S ≤ (n − 2)²(θ_S + 1), and if o tops its W-cycle at every eviction state of S (always when τ(o) = o), B_S ≤ θ_S +
      (n − 2)²(θ_S + 1), and in case A B_S ≤ θ_S. The eviction a → a+1 is a fallback by SPLIT (a) (RESULTS R39 (a)) (NEB-N1; the packet's
      "SPLIT (b)"), and a itself has no F → R̄ gate by FBL-N (iii) + (iii+) (NEB-N2).
  (g) Corollary OUT-1 (τ(o) = o, cases A and B): with D := (n − 2)² + 1, X_HN ≤ 2(n − 1)·D·(θ_ph + N_HN) and
      f_HN ≤ (K + 1)(2(n − 1)·D·(θ_ph + N_HN) + N_HN), where N_HN ≤ ⌊T_ph/2⌋ + 1 and f_HN counts the in-phase fallbacks from HN states
      (premises RESULTS R39 (b) EPOCH, (f) NE-COUNT (c), R38 (a), (d), R34 (e)).
- Not signed (packet §8): NO-ENTRY-B FALSE and NO-ENTRY for c_w ≠ o FALSE (both recorded in RESULTS R39: nebc_cex_n14, tauw_A_cex_n24,
  tauw_B_cex_n24); the dead ends NO-RR-B, NO-RISE-B and "INV_B (i) propagates" (all killed on nebc_cex_n14: states 1, 1 → 2, 2; obstruction
  §5 (c), a low rise); CONJECTURE BAND is FALSE in three forms (NEB-B1): in the rises form on experiments/new/box38/instances/tauw_A_cex_n24.pg
  (sha1 e29908d5; the S4a step 12 → 13 raises Ξ(11) and Ξ(16) at level 23 > rank(c_w) = 21; L-NEW successor 17, Lead re-run of the
  lane's score (4, 5, 2)), in the gates form at a later state (tauw_A state 13, gates 3 → 11 and 7 → 16 at level 23), and in the gates
  form at the base at the boundary (docs/referee/R-N5-NEB/band_base_cex.pg, sha1 468edac8, n 24: base a = 2, gate 5 → 14 at level
  19 = rank(c_w = 2); REFEREE successor 9; Lead re-run: one Odd choice vertex, n5 6/1, Oink zlk OK strategies verified); OPEN: RW_S
  (rises after c_w ≠ o evictions), θ_S / θ_ph, HN stretches per phase for τ(o) ≠ o, OTHER states.
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase. (ii) BRK bounds breaks by θ-changes plus R̄-rises; RW_S and θ-changes per phase are
  not bounded here, so G-N5-TIME stays open; OUT-1 is polynomial GIVEN θ_ph for τ(o) = o only. (iii) On the library (lib37) the
  hypotheses of RISE, HIGH-RISE, CASE-B-LEN′ and LOW-RISE′ (c) never occur and every break is charged to a θ-change; they occur only on
  the box-38 instances and in climbs, where they occur many times (REFEREE's §9). (iv) The packet's §9 base totals (13 / 6 / 34 / 27,
  data/inv2_all.txt) came from an unnamed larger input; the stated command gives 75 / 9 / 4 / 20 / 8 (NEB-N5; the lane re-ran it and
  withdraws the old totals). (v) Status rows of the packet are stale: P-N5-OUT is RESULTS R39, KEY / FB-INT are RESULTS R38 (N-NEB-3,
  NEB-N4). (vi) Lane work after the pin (P-N5-PFZ, P-N5-RHO, N5-NHN) is not part of this entry.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE neb_probe.py (own engine; logs docs/referee/R-N5-NEB/):
  lib37 270 games, lane set 275, 6 named starts; 0 failures; NO-ENTRY-A′ 84 runs / 835 states on lib37; climbs from nebc_cex_n14,
  tauw_A_cex_n24, tauw_B_cex_n24, wd16_s2 (3,336,298 mutants): every hypothesis of §1, §2, §4, §5 (c) and the B= / B≠ charging of §6 occurs
  many times, 0 failures; case-A breaks with c_w = o occur only in the library (8, all θ-charged). REFEREE-2 (own checker; own / random
  / SPEC traces): 66,655 batch runs and climbs (501,892 runs), 0 violations; the new class (case A, c_w = o, τ(o) ≠ o) 26 / 20 / 28
  library bases and 18,324 in climbs; LOW-RISE′ (c) 31,951 first INV_B failures in climbs, each with a low rise; control: INV fails
  80k times outside the proved class, never inside.
- Signatures: REFEREE docs/referee/R-N5-NEB.md (referee 40adbf1, successor 9; §C 46a8030): RISE, HIGH-RISE, NO-ENTRY-A′, CASE-B-LEN′,
  LOW-RISE′, BRK (a)-(d), OUT-1 SIGNED; notes NEB-R1, NEB-N1..N5, NEB-B1; no gaps. REFEREE-2 docs/referee-2/R2-N5-NEB.md (referee-2
  a4516df, successor 9; §C a769ff5): RISE, HIGH-RISE, NO-ENTRY-A′ (with its Case 1′), CASE-B-LEN′, LOW-RISE′, BRK (a)-(d), OUT-1 SIGN;
  notes N-NEB-1..3; no gap. §C (both): verdicts identical; joint gap map empty; N-NEB-2 accepted by REFEREE (missed); NEB-N1..N3
  accepted by REFEREE-2.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
