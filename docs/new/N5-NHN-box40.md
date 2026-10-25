# N5 on 𝒞^1O, box 40 (2): HN stretches per phase for τ(o) ≠ o. Every stretch end that keeps H1 is a fallback that evicts τ(o) and strictly raises Ξ(τ(o)); after |U| − 2 fallbacks these rises are length-only; so N_HN ≤ ⌈T/2⌉ + 2|U| − 3 and HN-POLY holds for every τ(o) (EV2-FB, SG-EV, T0-PIN, NHN-BOUND, HN-POLY-ALL)
L-NEW successor 19 (Opus 5.5, D15/D18), session_011reTXakSJCcwLhC4i9ZpkB. Working doc (not a packet). Started 2026-10-25 16:1xZ by date -u.
- Setting and notation: docs/new/P-N5-RHO-box40.md §0 (packet, which restates P-N5-PFZ §0-§1). t0 := τ(o), a phase constant (τ is).
  T := |U|(n + 1) + n − 1 (TOGGLE-COUNT's count, RESULTS R34 (e)). DROP: an in-phase transition from H1 to ¬H1.
- Labels: PROVED (L-NEW succ. 19, unrefereed), OPEN, DATA. Not a running-time bound; G-N5-TIME stays OPEN. No (P).
- Lead's question (16:05Z, Lead's stamp): "is the number of HN stretches ≤ H1-toggles (R34 (e)) + H2-changes (WCH, R38 (b)) + 1? ...
  If it holds, HN-POLY holds for every τ(o)."
  - Answer. The inequality itself is trivially true (a stretch that is not the phase's last ends at an in-phase transition at which H1 or
    H2 changes), but it does NOT by itself give a polynomial bound: WCH counts w-CHANGES between H2 states, not H2-TOGGLES, and an
    H2-toggle is a crossing (t0 enters or leaves R), whose count per phase is not bounded by landed results. What does work: the
    toggles that END a stretch while keeping H1 are fallbacks (SPLIT), each strictly raises Ξ(t0), and after the hat freeze the rise is
    length-only. That is NHN-BOUND below.

## Summary
1. **Lemma T0U (PROVED).** In a phase with t0 ≠ o and an HN state: t0 ∈ U ∖ {o, c_θ} (so |U| ≥ 3), and at every state of the phase,
   ¬H2 ⇔ t0 ∈ R.
2. **Lemma EV2-FB (PROVED).** Every in-phase transition k → k+1 with HN at k and H1 ∧ H2 at k+1 (an EV2 END) is an Even S4c fallback with
   t0 ∈ R_k ∖ R_{k+1}.
3. **Lemma SG-EV (PROVED).** At every EV2 end, Ξ_k(t0) ◁ Ξ_{k+1}(t0).
4. **Lemma T0-PIN (PROVED).** If an EV2 end is the fallback g_j with j ≥ |U| − 1, then M_k(t0) = M_{k+1}(t0) = MoptÛ(t0).
5. **Theorem NHN-BOUND (PROVED).** A phase with t0 ≠ o has ≤ 2(|U| − 2) EV2 ends, and N_HN ≤ 1 + ⌈T/2⌉ + 2(|U| − 2) ≤ ⌈T/2⌉ + 2n − 3.
6. **Corollary HN-POLY-ALL (PROVED, conditional on P-N5-PFZ / -ext / -RHO).** For every τ(o): ρ_HN, the HN breaks, θ-changes, crossings
   and fallbacks at HN states of a phase are polynomial in n.
7. **OPEN.** Non-HN states (SN, OTHER, ¬H1), the number of phases, S4a steps that change none of the counted quantities.

## 1. Lemma T0U (PROVED)
Proof.
- At any state t: o's (σ_t, τ)-play is o · (t0's play). o lies on its W-cycle (¬H2) iff t0's play returns to o, i.e. iff t0 ∈ R_t
  (t0 ≠ o). So ¬H2 ⇔ t0 ∈ R_t.
- At an HN state s: t0 ∈ R_s ⊆ U ((HP) of P-N5-RHO §0: route form under H1), and c_θ ∈ F_s, so t0 ≠ c_θ. λ is constant on the phase,
  so t0 ∈ U at every state. U ⊇ {o, c_θ, t0}, three distinct vertices. □

## 2. Lemma EV2-FB (PROVED)
Proof. t0 ∈ R_k (¬H2 at k, T0U) and t0 ∉ R_{k+1} (H2 at k+1), so R_k ⊄ R_{k+1}. By SPLIT (RESULTS R39 (a); H1 ∧ ¬H2 at k) the
transition is not a non-fallback, so it is an S4c fallback; in-phase, τ is unchanged, so it is Even's (SPEC S4c, FIX 3). □

## 3. Lemma SG-EV (PROVED)
Statement. At an EV2 end k → k+1: Ξ_k(t0) ◁ Ξ_{k+1}(t0). (Uses only: H1 at k, the transition in-phase, t0 ∈ R_k ∖ R_{k+1}.)
Proof. Write κ_t(z) := (M_t(z), s_θ·ℓ(Ξ_t z)) for z ∈ U; by (M1′), for z, z′ ∈ U, Ξ_t(z) ◁ Ξ_{t′}(z′) ⇔ κ_t(z) < κ_{t′}(z′)
lexicographically. By (A), κ_t(z) = (wt(z), s_θ) + κ_t(next_t z) for z ∈ U ∖ {c_θ} (componentwise sum).
- Let π := π_{t0}^k = (v_0 = t0, v_1, …, v_m), the route at k (o excluded). All v_i ∈ R_k ⊆ U ∖ {c_θ} ((HP)).
- t0 ∉ R_{k+1}, so some v_i has next_{k+1}(v_i) ≠ next_k(v_i) (otherwise π followed by o is still t0's (σ_{k+1}, τ)-path). Let
  y = v_i be the first. y ≠ o, so y is not Odd (Odd vertices other than o are forced): y is Even and switched, σ_{k+1}(y) = z.
- R15 (d): (y, z) ∈ Iσ_k, so Ξ_k(z) ▷ Ξ_k(σ_k y). λ_{k+1}(y) = λ_k(y) = c_θ ≠ y (phase), so by (A) at k+1, z = next_{k+1}(y) ∈ U.
  So κ_k(z) > κ_k(σ_k y), and κ_{k+1}(z) ≥ κ_k(z) (R15 (a), (M1′)). Hence
  κ_{k+1}(y) = (wt(y), s_θ) + κ_{k+1}(z) > (wt(y), s_θ) + κ_k(σ_k y) = κ_k(y).
- For i′ < i, next_{k+1}(v_{i′}) = next_k(v_{i′}) = v_{i′+1}, so κ_t(t0) = Σ_{i′<i} (wt(v_{i′}), s_θ) + κ_t(y) for t ∈ {k, k+1}, and
  κ_{k+1}(t0) − κ_k(t0) = κ_{k+1}(y) − κ_k(y) > 0. □
- Remark. This is the step (SG) of RESULTS R19 (d) (signed "on all games"), propagated along the unchanged route prefix as in R19 (d)
  step 3; it is re-proved here because R19 (d) assumes (h), which fails at HN states (o lies on its W-cycle). Only H1 is used.

## 4. Lemma T0-PIN (PROVED)
Proof. k = g_j with j ≥ |U| − 1, so k > g_{|U|−2} and k + 1 > g_{|U|−2}. At k+1: H1 and t0 ∈ F_{k+1} ∩ U (H2, T0U), so HAT-FREEZE (b),
(c) (P-N5-RHO §2) give that MoptÛ(t0) is defined and M_{k+1}(t0) = MoptÛ(t0). At k: HAT-FREEZE (a) with j′ = |U| − 2 (every simple path
of G_Û has ≤ |U| − 2 edges) gives M_k(t0) ≥ MoptÛ(t0). (M2′): M_k(t0) ≤ M_{k+1}(t0). □

## 5. Theorem NHN-BOUND (PROVED)
Statement. In a phase with t0 ≠ o: #EV2 ends ≤ 2(|U| − 2), and N_HN ≤ 1 + ⌈T/2⌉ + 2(|U| − 2).
Proof.
- (Stretch count.) An HN stretch that is not the last of the phase ends at an in-phase transition k → k+1 with HN at k and not at k+1:
  either ¬H1 at k+1 (a DROP) or H1 ∧ H2 at k+1 (an EV2 end). So N_HN ≤ 1 + #DROPs + #EV2. #DROPs ≤ ⌈T/2⌉ (RESULTS R34 (e)).
- (EV2 ends.) By EV2-FB they are distinct in-phase Even fallbacks g_j.
  - j ≤ |U| − 2: at most |U| − 2 of them.
  - j ≥ |U| − 1: by T0-PIN, M(t0) = m* := MoptÛ(t0) at both ends of each. The states with M_t(t0) = m* form an interval I of the
    phase ((M2′)). On I, P(Ξ_t t0) is constant ((INJ)), so Ξ(t0) is ordered by s_θ·ℓ(Ξ_t t0), which is non-decreasing (R15 (a)). By
    SG-EV each such end is a transition of I at which s_θ·ℓ(Ξ t0) strictly rises. ℓ(Ξ_t t0) ∈ [1, |U| − 1] ((SP), t0 ≠ c_θ), so at
    most |U| − 2 strict moves. So at most |U| − 2 of these ends.
- Hence #EV2 ≤ 2(|U| − 2), and N_HN ≤ 1 + ⌈T/2⌉ + 2(|U| − 2). With |U| ≤ n and T ≤ n² + 2n − 1: N_HN ≤ (n² + 2n)/2 + 2n − 3 = O(n²). □
- Remarks.
  - Nothing about c_w, case A/B or θ is assumed. For τ(o) = o, RESULTS R39 (f) (c) gives N_HN ≤ ⌊T/2⌋ + 1 (no EV2 ends: ¬H2 always).
  - The answer to the Lead's form: the stretch count needs only the H2-toggles that END a stretch (EV2 ends), and those are fallbacks;
    the H2-toggles that START a stretch (t0 enters R at a non-HN state) need no bound.

## 6. Corollary HN-POLY-ALL (PROVED; conditional on P-N5-PFZ, P-N5-PFZ-ext and P-N5-RHO, all in review or offered)
For every τ(o) and every phase: N_HN = O(n²) (NHN-BOUND, or R39 (f) for τ(o) = o), so by P-N5-RHO §6 (RHO-HN, HN-POLY):
- ρ_HN ≤ (N_HN + |U| − 2)(|U| + deg(o) − 3) + deg(o) = O(n³);
- Σ_S θ_S ≤ (ρ_HN + N_HN)(n − 2) = O(n⁴); Σ_S B_S ≤ (ρ_HN + N_HN)(2n² − 1) = O(n⁵);
- crossings at HN states Σ_S X_S + (stretch exits) = O(n⁶); fallbacks at HN states ≤ K(Σ_S X_S + N_HN) + Σ_S X_S + N_HN = O(n⁸)
  (K = n_E(2n − 1)).
This closes, conditionally, the out-of-SN fallbacks AT HN STATES ("HN stretches for τ(o) ≠ o" in G-N5-TIME's open list after R39).
- Remark H3-IN-HN (PROVED, L-NEW succ. 19, two lines). In a phase with t0 ≠ o and an HN state, every H2 state has H3 (c_w = c_θ):
  H3-CONST (RESULTS R33 (a)) gives c_w = λ(t0) at every H2 state, and λ(t0) = c_θ by T0U. So every H1 ∧ H2 state of such a phase
  satisfies (h) = H1 ∧ H2 ∧ H3. The out-of-SN fallbacks of R38's not-signed list (at H1 ∧ ¬H2 and at H1 ∧ H2 ∧ ¬H3 states) therefore
  split as: HN states (HN-POLY-ALL), and H1 ∧ H2 ∧ ¬H3 states only in phases WITHOUT an HN state (there H3 fails at every H2 state).
- Still OPEN: fallbacks and crossings at H1 ∧ H2 ∧ ¬H3 states in phases without an HN state; S4a-only stretches; the number of phases.
  (¬H1 fallbacks: RESULTS R38 (e) NH1-FB.)

## 7. DATA (experiments/new/box40/nhn.py; library + box-37/38 instances as in P-N5-RHO §8, canonical start)
- Run 16:2xZ (date -u), files: the 412-file list of P-N5-RHO §8 (253 𝒞^1O) plus experiments/new/box40/out/*.pg (box-40 climb outputs at
  that time): 259 𝒞^1O files, 77 phases with τ(o) ≠ o and an HN state. Failures: 0 of every check (T0U, SPLIT/EV2-FB, SG-EV, T0-PIN,
  MOPT, LEN, POST, NHN1, NHN).
- THIN: 4 EV2 ends in all (EV2-FB and SG-EV checked 4 times); 0 post-freeze EV2 ends, so T0-PIN and the length-only branch are
  VACUOUS in data so far; 0 drops; N_HN ≤ 2 per phase (max 2: experiments/new/box40/out/nhc_fbrestart_cex_n12_11.pg, climb output).
- Climb: experiments/new/box40/nhnclimb.py (score: failures, post-freeze EV2 ends, max N_HN, EV2 ends). Running.
