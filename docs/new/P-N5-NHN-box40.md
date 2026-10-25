# Referee packet P-N5-NHN: for τ(o) ≠ o, every HN-stretch end that keeps H1 is a fallback that evicts τ(o) and strictly raises Ξ(τ(o)); after |U| − 2 fallbacks the rise is length-only; so a phase has at most ⌈T/2⌉ + 2|U| − 3 HN stretches, and HN-POLY holds for every τ(o) (T0U, EV2-FB, SG-EV, T0-PIN, NHN-BOUND, H3-IN-HN, HN-POLY-ALL) (box 40)
L-NEW successor 19 (Opus 5.5, D15/D18, L37/L40), session_011reTXakSJCcwLhC4i9ZpkB. Written 2026-10-25 17:20Z by date -u, at the Lead's
word of 16:37Z (Lead's stamp): "P-N5-NHN: YES, after RHO. ... Mark HN-POLY-ALL's conditions explicitly (PFZ + ext with the PFZ-1
repair, and RHO), and state its data thinness". Frozen at this commit: corrections go in a fixes file, never here.
- Source: docs/new/N5-NHN-box40.md (working doc, l-new 04fe8979 / 3e9fe5c2). This packet re-states and re-proves everything it signs;
  where the packet and the source differ, the packet governs.
- Question it answers (Lead 16:05Z): "is the number of HN stretches ≤ H1-toggles (R34 (e)) + H2-changes (WCH, R38 (b)) + 1?". The
  inequality is trivially true, but it is not polynomial by R34 (e) + WCH: WCH counts w-CHANGES between H2 states, not H2-TOGGLES,
  and an H2-toggle is a crossing (τ(o) enters or leaves R). Only the toggles that END a stretch while keeping H1 must be counted;
  they are fallbacks (EV2-FB), and NHN-BOUND counts them.
- Labels (D18/L40): PROVED (L-NEW succ. 19, unrefereed), OPEN, DATA.
- Scope. The candidate N5 (SPEC S1-S5, docs/new/N5-ssi-global.md) on 𝒞^1O, inside one phase. Not a running-time bound for N5, not a
  TARGET.md claim, not a step-4 pass. G-N5-TIME stays OPEN.

## To sign, and what is not to sign
| § | statement | label | uses (P) | uses packets in review |
| --- | --- | --- | --- | --- |
| §1 | Lemma T0U (t0 := τ(o) ∈ U ∖ {o, c_θ} in a phase with an HN state; ¬H2 ⇔ t0 ∈ R) | PROVED | no | none ((HP) restated) |
| §2 | Lemma EV2-FB (an HN → H1 ∧ H2 transition is an Even fallback evicting t0) | PROVED | no | none |
| §3 | Lemma SG-EV (such a transition strictly raises Ξ(t0)) | PROVED | no | (A) (P-N5-PFZ §1, restated in P-N5-RHO §0) |
| §4 | Lemma T0-PIN (after g_{|U|−2}, M(t0) is pinned at MoptÛ(t0) at both ends) | PROVED | no | HAT-FREEZE (P-N5-RHO §2) |
| §5 | Theorem NHN-BOUND (#EV2 ends ≤ 2(|U| − 2); N_HN ≤ ⌈T/2⌉ + 2|U| − 3) | PROVED | no | via §3, §4 |
| §6 | Remark H3-IN-HN (in a phase with t0 ≠ o and an HN state, every H2 state has H3) | PROVED | no | none |
| §7 | Corollary HN-POLY-ALL (every τ(o): HN breaks, θ-changes, crossings, fallbacks per phase polynomial in n) | PROVED, CONDITIONAL | no | P-N5-RHO §6; P-N5-PFZ-ext BRK-POLY′ (weak form (i′), or (i) with the PFZ-1 repair); P-N5-PFZ §1 |
- (P) is used nowhere.
- Conditions of §4, §5, §7, explicitly:
  - P-N5-PFZ (sha1 3c617e06…, pinned 283bcb67): facts (A), (M1′), (M2′), Lemma FB-ROUND. Signed by REFEREE 9 (R-N5-PFZ 8595343) and
    REFEREE-2 9 (R2-N5-PFZ 37e55fd); not landed.
  - P-N5-PFZ-ext (sha1 b3702b1b…, pinned c61ecc4e): BRK-POLY′, used only in §7. REFEREE 9: SIGNED except GAP PFZ-1 on (i) (repair in
    R-N5-PFZ); REFEREE-2 10 to review. §7 needs only the weak form (i′) θ_S ≤ ρ_S + (ρ_S + 1)·max(|U| − 2, 0), which the ext proof gives
    as written; with the PFZ-1 repair the stronger (i) may be used instead. (ii)'s B_S ≤ (ρ_S + 1)(2n² − 1) holds with either.
  - P-N5-RHO (docs/new/P-N5-RHO-box40.md, sha1 cd5df65c2f3e6829f85739a57023fc3da6944baa, l-new 3e9fe5c2; PINNED at trunk c8144551,
    16:50Z; in review): HAT-FREEZE (b), (c) for §4; RHO-HN and HN-POLY for §7.
  - §1-§3 and §6 use landed results only (plus (A), restated).
- §8 is NOT TO SIGN (OPEN). §9 is data.

## 0. Objects, notation and dependencies
- Everything as in P-N5-RHO §0 (which restates P-N5-PFZ §0-§1): N5, valuations and the order, Ξ_k, λ_k, next_k, 𝒞^1O, o, θ, c_θ, R_k,
  R̄_k, F_k, routes π_z, H1, H2, HN, phase, HN stretch, U, Û, G_Û, MoptÛ, M_t, wt, s_θ, g_j, N_HN, ρ_HN, and the facts (A), (A0), (M1′),
  (M2′), (INJ), (HP), (SP).
- New here: t0 := τ(o), a phase constant (τ is). H3: c_θ = c_w (c_w := the top of o's W-cycle when ¬H2, else the cycle node of W(o)).
  (h) := H1 ∧ H2 ∧ H3. T := |U|(n + 1) + n − 1 (TOGGLE-COUNT's count, RESULTS R34 (e)). In a phase: a DROP is a transition from H1 to
  ¬H1; an EV2 END is a transition k → k+1 with HN at k and H1 ∧ H2 at k+1. For z ∈ U, κ_t(z) := (M_t(z), s_θ·ℓ(Ξ_t z)), ordered
  lexicographically.

### Dependencies (statement used / where it lives / status)
| tag | statement used | location | status |
| --- | --- | --- | --- |
| (V1) | if λ(v) ≠ v, the value of v is v ⊕ (value of next(v)) | RESULTS R17 (a) | LANDED |
| R15 (a), (d) | Ξ_k ⊴ Ξ_{k+1} pointwise; σ_{k+1}(v) ∈ {σ_k(v)} ∪ Iσ_k(v) | RESULTS R15 | LANDED |
| SPLIT (a) | at an in-phase transition with H1 ∧ ¬H2 at k, a non-fallback has R_k ⊆ R_{k+1} | RESULTS R39 (a) | LANDED |
| H2-STICK | at an S4a transition of a phase with H1 ∧ ¬H2 at s, ¬H2 holds at s+1 | RESULTS R33 (b) | LANDED (second source for §2) |
| H3-CONST | in a phase, at every H2 state c_w = λ(τ(o)) | RESULTS R33 (a) | LANDED |
| TOGGLE-COUNT | H1-toggles per phase ≤ T; drops ≤ ⌈T/2⌉ | RESULTS R34 (e) | LANDED |
| NE-COUNT (c) | τ(o) = o: N_HN ≤ ⌊T_ph/2⌋ + 1 | RESULTS R39 (f) | LANDED |
| EPOCH | X_S ≤ 2(n − 1)(B_S + 1), f_S ≤ K(X_S + 1) + X_S, K := n_E(2n − 1) | RESULTS R39 (b) | LANDED |
| (A), (M1′), (M2′), FB-ROUND | P-N5-PFZ §1 (restated in P-N5-RHO §0) | P-N5-PFZ | signed by both referees; not landed |
| HAT-FREEZE (a)-(c), RHO-HN, HN-POLY | P-N5-RHO §2, §6 | P-N5-RHO (cd5df65c) | pinned trunk c8144551; in review |
| BRK-POLY′ (i′), (ii) | θ_S ≤ ρ_S + (ρ_S + 1)·max(|U| − 2, 0); B_S ≤ (ρ_S + 1)(2n² − 1) | P-N5-PFZ-ext §3 (P-N5-RHO §6 for (i′)) | in review (GAP PFZ-1 on (i), not on (i′)) |
- Not used: WCH (RESULTS R38 (b)), Lemma RE (RESULTS R19 (d)) as a citation (its step (SG) is re-proved in §3 without (h)), P-N5-NEB.

## 1. Lemma T0U (PROVED)
Statement. In a phase with t0 ≠ o: (a) at every state t, ¬H2 holds iff t0 ∈ R_t; (b) if the phase has an HN state, then t0 ∈ U ∖ {o, c_θ}
at every state of the phase, so |U| ≥ 3.
Proof.
- (a) o's (σ_t, τ)-play is o · (t0's (σ_t, τ)-play). o lies on its W-cycle iff that play returns to o, i.e. iff t0 ∈ R_t (t0 ≠ o).
- (b) At an HN state s: t0 ∈ R_s by (a), and R_s ⊆ U by (HP) (route form under H1); c_θ ∈ F_s by (HP), so t0 ≠ c_θ. λ is constant on the
  phase, so λ(t0) = c_θ at every state. o, c_θ, t0 are three distinct vertices of U. □

## 2. Lemma EV2-FB (PROVED)
Statement. In a phase with t0 ≠ o, every EV2 end k → k+1 is an Even S4c fallback with t0 ∈ R_k ∖ R_{k+1}.
Proof. t0 ∈ R_k (¬H2 at k) and t0 ∉ R_{k+1} (H2 at k+1), by T0U (a). So R_k ⊄ R_{k+1}, and by SPLIT (a) (RESULTS R39 (a); H1 ∧ ¬H2 at
k) the transition is not a non-fallback. So it is an S4c fallback, and Even's, since τ is unchanged in a phase (SPEC S4c, FIX 3: an Odd
fallback changes τ). (Second source: H2-STICK, RESULTS R33 (b), says ¬H2 survives every S4a step from an H1 ∧ ¬H2 state.) □

## 3. Lemma SG-EV (PROVED)
Statement. Let k → k+1 be an in-phase transition with H1 at k, t0 ∈ R_k and t0 ∉ R_{k+1} (in particular, any EV2 end). Then
Ξ_k(t0) ◁ Ξ_{k+1}(t0).
Proof.
- By (M1′), for z, z′ ∈ U: Ξ_t(z) ◁ Ξ_{t′}(z′) ⇔ κ_t(z) < κ_{t′}(z′). By (A) (signed weight and length), for z ∈ U ∖ {c_θ}:
  κ_t(z) = (wt(z), s_θ) + κ_t(next_t z), componentwise.
- Let π_{t0}^k = (v_0 = t0, v_1, …, v_m) be t0's route at k (its (σ_k, τ)-path up to o, o excluded). Every v_i is in R_k, so in U ∖ {c_θ}
  ((HP): R_k ⊆ U and c_θ ∈ F_k).
- t0 ∉ R_{k+1}, so some v_i has next_{k+1}(v_i) ≠ next_k(v_i): otherwise the same path, followed by o, is t0's (σ_{k+1}, τ)-path. (For
  v_i ∈ R_k, next is σ at Even vertices and the forced edge at Odd vertices ≠ o, which never changes.) Let y = v_i be the first such.
  y is Even, and switched: σ_{k+1}(y) = z ≠ σ_k(y).
- R15 (d): (y, z) ∈ Iσ_k, i.e. Ξ_k(z) ▷ Ξ_k(σ_k y). λ_{k+1}(y) = λ_k(y) = c_θ ≠ y (phase), so (A) at k+1 gives z = next_{k+1}(y) ∈ U.
  So κ_k(z) > κ_k(σ_k y), and κ_{k+1}(z) ≥ κ_k(z) (R15 (a), (M1′)). Hence, by (A) at k+1 and at k,
  κ_{k+1}(y) = (wt(y), s_θ) + κ_{k+1}(z) > (wt(y), s_θ) + κ_k(σ_k y) = κ_k(y).
- For i′ < i, next_{k+1}(v_{i′}) = next_k(v_{i′}) = v_{i′+1}, so by (A), κ_t(t0) = Σ_{i′<i} (wt(v_{i′}), s_θ) + κ_t(y) for t ∈ {k, k+1}.
  So κ_{k+1}(t0) − κ_k(t0) = κ_{k+1}(y) − κ_k(y) > 0. □
- Remark. This is step (SG) of RESULTS R19 (d) (signed "on all games"), carried along the unchanged route prefix as in R19 (d) step 3.
  R19 (d) assumes (h) at the leave, which fails at HN states (o lies on its W-cycle); the proof above uses only H1 at k and the phase.

## 4. Lemma T0-PIN (PROVED; uses P-N5-RHO §2)
Statement. In a phase with t0 ≠ o, let the EV2 end k → k+1 be the fallback g_j with j ≥ |U| − 1. Then MoptÛ(t0) is defined and
M_k(t0) = M_{k+1}(t0) = MoptÛ(t0).
Proof. k = g_j with j ≥ |U| − 1, so k > g_{|U|−2} and k + 1 > g_{|U|−2}.
- At k+1: H1 holds and t0 ∈ F_{k+1} ∩ U (H2 and T0U). HAT-FREEZE (b), (c) (P-N5-RHO §2): MoptÛ(t0) is defined and
  M_{k+1}(t0) = MoptÛ(t0).
- At k: HAT-FREEZE (a) with j′ = |U| − 2 (every simple path of G_Û has ≤ |Û| − 1 = |U| − 2 edges) gives M_k(t0) ≥ MoptÛ(t0).
- (M2′): M_k(t0) ≤ M_{k+1}(t0). □

## 5. Theorem NHN-BOUND (PROVED; uses P-N5-RHO §2 through §4)
Statement. In a phase with t0 ≠ o: (a) there are at most 2·max(|U| − 2, 0) EV2 ends; (b) N_HN ≤ 1 + ⌈T/2⌉ + 2·max(|U| − 2, 0)
≤ ⌈T/2⌉ + 2n − 3, with T ≤ n² + 2n − 1.
Proof.
- (b) from (a). An HN stretch that is not the last of its phase ends at an in-phase transition k → k+1 with HN at k and not at k+1
  (the next stretch lies in the same phase). Either H1 fails at k+1 (a DROP) or H1 ∧ H2 holds at k+1 (an EV2 end). So N_HN ≤ 1 + #DROPs +
  #EV2 ends, and #DROPs ≤ ⌈T/2⌉ (RESULTS R34 (e)). If the phase has no HN state, N_HN = 0.
- (a) Assume the phase has an HN state (else there is no EV2 end), so |U| ≥ 3 (T0U). By EV2-FB the EV2 ends are distinct in-phase Even
  fallbacks g_j.
  - Those with j ≤ |U| − 2: at most |U| − 2.
  - Those with j ≥ |U| − 1. By T0-PIN, M(t0) = m* := MoptÛ(t0) at both ends of each. By (M2′) the states t with M_t(t0) = m* form an
    interval I of the phase, which contains both ends of each. On I, P(Ξ_t t0) is constant ((INJ)) and the cycle node is c_θ, so
    Ξ_t(t0) is ordered by s_θ·ℓ(Ξ_t t0), which is non-decreasing on I (R15 (a)). By SG-EV each such end is a transition of I at which
    s_θ·ℓ(Ξ t0) strictly rises. ℓ(Ξ_t t0) ∈ [1, |U| − 1] ((SP); t0 ≠ c_θ), so there are at most |U| − 2 strict rises. So at most |U| − 2
    such ends.
  - Total ≤ 2(|U| − 2). □
- Remarks.
  - Nothing about c_w, case A / B, or θ is assumed. For τ(o) = o there are no EV2 ends (¬H2 always: o's W-play is its loop), and
    RESULTS R39 (f) (c) gives N_HN ≤ ⌊T/2⌋ + 1.
  - The H2-toggles that START a stretch (t0 enters R at a non-HN state) need no bound.

## 6. Remark H3-IN-HN (PROVED)
Statement. In a phase with t0 ≠ o and an HN state, every H2 state of the phase has H3; so every H1 ∧ H2 state of the phase satisfies (h).
Proof. H3-CONST (RESULTS R33 (a)): at every H2 state, c_w = λ(τ(o)) = λ(t0). By T0U (b), λ(t0) = c_θ. □
- Consequence (bookkeeping, PROVED). The out-of-SN fallbacks of RESULTS R38's not-signed list (fallbacks at H1 ∧ ¬H2 states and at
  H1 ∧ H2 ∧ ¬H3 states) split as: fallbacks at HN states (§7), and fallbacks at H1 ∧ H2 ∧ ¬H3 states, which occur only in phases with
  NO HN state (there H3 fails at every H2 state, and every ¬H2 state is ¬H1). The second kind is OPEN (§8).

## 7. Corollary HN-POLY-ALL (PROVED, CONDITIONAL on P-N5-PFZ, P-N5-PFZ-ext BRK-POLY′ (i′)/(ii), P-N5-RHO)
Statement. For every τ(o) and every phase:
- N_HN ≤ ⌈T/2⌉ + 2n − 3 = O(n²) (NHN-BOUND; for τ(o) = o, RESULTS R39 (f) (c));
- ρ_HN ≤ (N_HN + |U| − 2)(|U| + deg(o) − 3) + deg(o) = O(n³) (RHO-HN, P-N5-RHO §6);
- Σ_S θ_S ≤ ρ_HN + (ρ_HN + N_HN)·max(|U| − 2, 0) = O(n⁴) and Σ_S B_S ≤ (ρ_HN + N_HN)(2n² − 1) = O(n⁵) (BRK-POLY′ (i′), (ii));
- Σ_S X_S ≤ 2(n − 1)(Σ_S B_S + N_HN) = O(n⁶) (EPOCH);
- fallbacks from HN states ≤ Σ_S f_S + N_HN ≤ K(Σ_S X_S + N_HN) + Σ_S X_S + N_HN = O(n⁸), K = n_E(2n − 1) (EPOCH; an in-phase fallback
  from an HN state lies in its stretch or is the stretch's last transition).
Proof. P-N5-RHO §6 (Corollary HN-POLY) with N_HN bounded by §5. □
- What this closes (conditionally): "HN stretches for τ(o) ≠ o" in G-N5-TIME's open list after R39, hence the fallbacks and crossings
  at HN states per phase, for every τ(o) and every c_w.

## 8. Not to sign (OPEN)
- Fallbacks and crossings at H1 ∧ H2 ∧ ¬H3 states (only in phases without an HN state, §6).
- The global count: f (fallbacks per phase) also enters SCOPE-COUNT (RESULTS R38 (c)) and X-SN-PHASE (RESULTS R34 (f)); fallbacks at (h)
  states; S4a steps that change none of the counted quantities; the number of phases. This packet is not an iteration bound.

## 9. Data (DATA; which hypotheses occur — lesson N-ENT-2)
Scripts experiments/new/box40: nhn.py (every check below; prints FAIL_* lines), nhnclimb.py (climb), qsurvey.py (Q states). Instances:
(L) the 412-file list of P-N5-RHO §8 (253 𝒞^1O); (C) experiments/new/box40/out/*.pg, 8 climb outputs (P-N5-RHO §8's 6, plus
nhc_tauw_B_cex_n24_23.pg sha1 e7bae7dd…, nhc_band_base_cex_24.pg sha1 da60633b…). One Odd vertex of out-degree > 1, checked per file.
Canonical start. Failures: 0 of every check (T0U, SPLIT/EV2-FB, SG-EV, T0-PIN, MOPT, LEN, POST, H3, NHN1, NHN).
- (L) + (C): 261 𝒞^1O files, 84 phases with τ(o) ≠ o and an HN state.
  - T0U: checked in all 84 phases.
  - EV2-FB and SG-EV: 8 EV2 ends in all (3 in (L), 5 in (C)). THIN.
  - T0-PIN and NHN-BOUND (a)'s second branch (EV2 ends after g_{|U|−2}): 0 occurrences. VACUOUS in data.
  - H3-IN-HN: 395 H2 states in these phases, all with c_w = c_θ. qsurvey.py on (L): 165 phases contain Q states (H1 ∧ H2 ∧ ¬H3), none of
    them a phase with τ(o) ≠ o and an HN state.
  - NHN-BOUND (b): N_HN 89 in total over the 84 phases; max 4 (nhc_tauw_B_cex_n24_23.pg, n 24, |U| 24, 3 EV2 ends, 0 drops; bound
    ⌈T/2⌉ + 2|U| − 3 = 312 + 45 = 357). DROPs ending a stretch: 0 in all data, so N_HN = 1 + #EV2 ends wherever N_HN > 1.
- Climbs (nhnclimb.py; score (failures, post-freeze EV2 ends, max N_HN, EV2 ends); MODE TAU mutations): 5 runs of 20-25 minutes from
  fbrestart_cex_n12 (box 35), its climb output, tauw_A_cex_n24, tauw_B_cex_n24 (box 38) and band_base_cex.pg (REFEREE). Best: N_HN 4,
  3 EV2 ends. No post-freeze EV2 end was reached.
- Honest caveats (lesson N-ENT-2): §3 and §2 are exercised 8 times, §4 never; the bound of §5 is far from approached (max 4 against
  hundreds). Random 𝒞^1O games reach no HN fallback state (box 37, box 39), so all evidence is library and climb material.
