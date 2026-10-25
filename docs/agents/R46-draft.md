# Draft RESULTS R46 (Lead, 2026-10-25 21:00Z by date -u; renumbered from R47 and fixes-file line filled 21:05Z) — to CHECKER C55

### R46 [refereed-only] N5 on one-Odd-choice games: for τ(o) ≠ o, every end of an HN stretch into H1 ∧ H2 is an Even fallback that evicts τ(o) and strictly raises Ξ(τ(o)) (T0U, EV2-FB, SG-EV), after |U| − 2 fallbacks such an end is pinned (T0-PIN), so a phase has at most ⌈T/2⌉ + 2n − 3 HN stretches (NHN-BOUND), and HN breaks, θ-changes, crossings and fallbacks at HN states per phase are polynomial in n for every τ(o) (HN-POLY-ALL) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C55.md, checker PENDING)
- Object (packet P-N5-NHN, added at l-new 5fb9dca0, pinned trunk 0bb175d, unchanged during review): docs/new/P-N5-NHN-box40.md, sha1
  da7d09ec6cb27ee8f7d94b857bc13fb2946aff1a (L-NEW successor 19, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-NHN-fixes-box40.md (l-new 5e1b5ea0, sha1 d1460ffede49a68d2a5f779b1a1b2b3cd8f62a02, L-NEW successor 21: NHN-N1 =
  N-NHN-1 = RHO-N2, NHN-N2, N-NHN-2, NHN-N3); on trunk; repairs only.
  Setting as in RESULTS R39, R44 and R45 (𝒞^1O; phase; HN states and HN stretches; θ, c_θ, c_w; R_k, R̄_k, F_k; U, Û, G_Û, MoptÛ,
  M_t, g_1 < g_2 < … the in-phase Even S4c fallbacks; N_HN, ρ_HN, θ_S, B_S, X_S, f_S). t0 := τ(o) (constant on a phase). H3: c_θ = c_w;
  (h) := H1 ∧ H2 ∧ H3. T := |U|(n + 1) + n − 1 (RESULTS R34 (e)). A DROP is an in-phase transition from H1 to ¬H1; an EV2 END is an
  in-phase transition k → k+1 with HN at k and H1 ∧ H2 at k+1. A Q state is an H1 ∧ H2 ∧ ¬H3 state.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P):
  (a) Lemma T0U: in a phase with t0 ≠ o, (a) at every state t, ¬H2 holds iff t0 ∈ R_t; (b) if the phase has an HN state, then
      t0 ∈ U ∖ {o, c_θ} at every state of the phase, so |U| ≥ 3.
  (b) Lemma EV2-FB: in a phase with t0 ≠ o, every EV2 end k → k+1 is an Even S4c fallback with t0 ∈ R_k ∖ R_{k+1} (SPLIT (a), RESULTS
      R39 (a)).
  (c) Lemma SG-EV: if k → k+1 is an in-phase transition with H1 at k, t0 ∈ R_k and t0 ∉ R_{k+1} (in particular any EV2 end), then
      Ξ_k(t0) ◁ Ξ_{k+1}(t0).
  (d) Lemma T0-PIN: in a phase with t0 ≠ o, if the EV2 end k → k+1 is the fallback g_j with j ≥ |U| − 1, then MoptÛ(t0) is defined
      and M_k(t0) = M_{k+1}(t0) = MoptÛ(t0) (HAT-FREEZE (b), (c), RESULTS R45 (b)).
  (e) Theorem NHN-BOUND: in a phase with t0 ≠ o, (a) there are at most 2·max(|U| − 2, 0) EV2 ends; (b) N_HN ≤ 1 + ⌈T/2⌉ +
      2·max(|U| − 2, 0) ≤ ⌈T/2⌉ + 2n − 3, with T ≤ n² + 2n − 1. For τ(o) = o the packet's remark cites RESULTS R39 (f) (c), which is
      landed for case A only; the bound for τ(o) = o follows from RESULTS R34 (e) with HN = H1 (NHN-N1 = N-NHN-1, citation, both
      referees; = RHO-N2 of RESULTS R45).
  (f) Remark H3-IN-HN: in a phase with t0 ≠ o and an HN state, every H2 state has H3, so every H1 ∧ H2 state of the phase satisfies
      (h) (H3-CONST, RESULTS R33 (a)). Its bookkeeping consequence holds with "there" read as "in a phase containing a Q state" (NHN-N2,
      wording; accepted by REFEREE-2).
  (g) Corollary HN-POLY-ALL: for every τ(o) and every phase, N_HN ≤ ⌈T/2⌉ + 2n − 3 = O(n²); ρ_HN ≤ (N_HN + |U| − 2)(|U| + deg(o) − 3) +
      deg(o) = O(n³); Σ_S θ_S ≤ ρ_HN + (ρ_HN + N_HN)·max(|U| − 2, 0) = O(n⁴); Σ_S B_S ≤ (ρ_HN + N_HN)(2n² − 1) = O(n⁵); Σ_S X_S ≤
      2(n − 1)(Σ_S B_S + N_HN) = O(n⁶); fallbacks from HN states ≤ K(Σ_S X_S + N_HN) + Σ_S X_S + N_HN = O(n⁸), K = n_E(2n − 1). Signed
      CONDITIONAL on P-N5-PFZ §1 ((A), (M1′), (M2′), FB-ROUND), P-N5-PFZ-ext BRK-POLY′ (i′) and (ii), and P-N5-RHO §2, §6. These conditions
      are now RESULTS R44 (a), (g) and R45 (b), (f), (g) (landed; R44 (g) includes the weak form (i′), which (g) uses); the τ(o) = o line
      as in (e).
- Not signed (packet §8, §9 and "What this closes", a GAPS reading): OPEN: fallbacks and crossings at Q states (only in phases without
  an HN state, by (f)); the global count f per phase as it enters SCOPE-COUNT (RESULTS R38 (c)) and X-SN-PHASE (RESULTS R34 (f));
  fallbacks at (h) states; S4a steps that change none of the counted quantities; the number of phases. This entry is not an iteration
  bound.
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase. (ii) HN-POLY-ALL bounds what happens at HN states; OTHER states, (h)-state
  fallbacks, quiet S4a steps and wakes K are not bounded here, so G-N5-TIME stays open. (iii) Thin data: T0-PIN and NHN-BOUND (a)'s
  second branch (EV2 ends at g_j with j ≥ |U| − 1) are VACUOUS in all data of both referees and the lane (REFEREE's climbs reached
  j = |U| − 9 at best; REFEREE-2 found none even at j = |U| − 2), so they rest on their proofs; EV2-FB and SG-EV occur in the library
  and climbs only (random 𝒞^1O games reach no EV2 end); max N_HN 4 against bounds in the hundreds.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE (own nhn_probe.py on rl_engine): 253 𝒞^1O library games
  (990 phases; 76 with t0 ≠ o and an HN state; 30 τ(o) = o phases with HN states, 13 in case B) and the lane's 8 climb outputs: the
  packet's §9 totals reproduced exactly (84 phases, 8 EV2 ends, 395 H3 checks, N_HN 89 with max 4, 165 Q phases); climbs (1,882,532
  candidates): 1,022,295 EV2 ends checked, 35 DROPs ending an HN stretch, 0 failures. REFEREE-2 (own nhn_check.py): 4,428 library runs
  and 64,000 random 𝒞^1O runs, 159,084 phases (5,062 with t0 ≠ o and an HN state), 45 EV2 ends, 7,237 H3 checks, N_HN ≤ ⌊T_ph/2⌋ + 1 in
  1,252 case-A and 1,885 case-B τ(o) = o phases, 0 violations; mutation control nhn bites (10 violations), pin1 gives 0 (no EV2 end even at j = |U| − 2, so T0-PIN is not approached).
  Lane nhn.py: 0 failures of every check.
- Signatures: REFEREE docs/referee/R-N5-NHN.md (referee 9bb3f79, successor 10; §C 41b93026): T0U, EV2-FB, SG-EV, T0-PIN, NHN-BOUND,
  H3-IN-HN SIGNED (T0-PIN and NHN-BOUND conditional on P-N5-RHO's HAT-FREEZE, now RESULTS R45 (b)); HN-POLY-ALL SIGNED with
  exactly its conditions; notes NHN-N1..N3; no gaps. REFEREE-2 docs/referee-2/R2-N5-NHN.md (referee-2 04b5c1fd, successor 11; §C
  a41f2c13): all SIGN; HN-POLY-ALL SIGN CONDITIONAL as labelled; notes N-NHN-1, N-NHN-2; no gap. §C (both): verdicts identical; joint gap
  map empty; NHN-N1 = N-NHN-1; N-NHN-2 accepted by REFEREE; NHN-N2 accepted by REFEREE-2.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
