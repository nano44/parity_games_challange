# R2-N5-NHN: second-referee check of packet P-N5-NHN (L-NEW box 40: T0U, EV2-FB, SG-EV, T0-PIN, NHN-BOUND, H3-IN-HN, HN-POLY-ALL). REFEREE-2 (successor 11), written 2026-10-25 19:3xZ-20:1xZ (date -u)
Signature: (Opus 5.5, D15). Lead queue (successor 10's handover; confirmed 18:27Z, Lead's stamp).
Object: docs/new/P-N5-NHN-box40.md, sha1 da7d09ec6cb27ee8f7d94b857bc13fb2946aff1a, the same at the pin 0bb175d and on my tree.
Author: L-NEW successor 19.
Background read: RESULTS R15 (a), (d), R17 (a), R33 (a) H3-CONST, (b) H2-STICK, R34 (e) TOGGLE-COUNT (text: "H1-toggles per phase ≤
T := |U|(n + 1) + n − 1 ≤ n² + 2n − 1, and drops ≤ ⌈T/2⌉"), R39 (a) SPLIT, (b) EPOCH, (f) NE-COUNT (headed "τ(o) = o, case A").
Also read: P-N5-RHO §0-§2, §6, P-N5-PFZ §1 and P-N5-PFZ-ext §3, all signed by this lane (R2-N5-RHO, R2-N5-PFZ incl. §X and §C).
Independence: nothing in docs/referee/ was read for this packet (`ls docs/referee | grep -i nhn` -> R-N5-NHN.md is on trunk, per the
Lead 18:51Z; NOT opened). No lane script (nhn.py, nhnclimb.py, qsurvey.py) was run or imported.
Tools (own code, docs/referee-2/R2-N5-NHN/): nhn_check.py (on R2-N5-OUT/out_check.py and R2-N5-RHO/rho_check.py's DFS), files.lst
(= R2-N5-FBPOLY/files.lst, 492 𝒞^1O files), run_all.sh, logs/, logs_mut/, totals_logs.txt.
Labels: PROVED (L-NEW succ. 19); §7 PROVED CONDITIONAL. This is not a running-time bound, not a TARGET.md claim and not a step-4 pass.
G-N5-TIME stays OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §1 Lemma T0U (a), (b) | SIGN | — |
| §2 Lemma EV2-FB | SIGN | — |
| §3 Lemma SG-EV | SIGN | — |
| §4 Lemma T0-PIN | SIGN (its premise HAT-FREEZE (a)-(c), P-N5-RHO §2, is signed by both referees) | — |
| §5 Theorem NHN-BOUND (a), (b) | SIGN | N-NHN-1 (citation): the τ(o) = o remark cites R39 (f) (c), which is landed for case A only (= RHO-N2) |
| §6 Remark H3-IN-HN (and its bookkeeping consequence) | SIGN | — |
| §7 Corollary HN-POLY-ALL | SIGN CONDITIONAL, as labelled: on P-N5-PFZ §1 (A), (M1′), (M2′), FB-ROUND; P-N5-PFZ-ext BRK-POLY′ (i′) and (ii); P-N5-RHO §2, §6 | N-NHN-1 for its τ(o) = o line; N-NHN-2 (statuses): all three conditions are now signed by both referees (PFZ: R2-N5-PFZ §1-§6 + §C; ext: §X + §C, (i) as stated now also signed with the PFZ-1 repair; RHO: R2-N5-RHO + §C) |
| §8, §9 | not signed (as briefed) | — |
No statement is NOT SIGNED, and no gap is open. No (P).
Thin spots (DATA; my data agree in kind with the packet's §9): T0-PIN and NHN-BOUND (a)'s second branch are VACUOUS (no EV2 end at
j ≥ |U| − 1, nor even at j ≥ |U| − 2). EV2-FB and SG-EV are exercised (45 EV2 ends, against the packet's 8). The NHN-BOUND (b) count is
far from its bound (max N_HN 4).

## 1. T0U: SIGN
- (a) o's (σ_t, τ)-play is o · (t0's play). o lies on its W-cycle iff that play returns to o, i.e. iff t0 ∈ R_t (t0 ≠ o). H2 is "o on
  no W-cycle". ✓
- (b) At an HN state, ¬H2 gives t0 ∈ R_s. Under H1, R_s ⊆ U (route form, (HP)) and c_θ ∈ F_s. λ is constant on the phase, so
  t0 ∈ U ∖ {o, c_θ} at every state. ✓

## 2. EV2-FB: SIGN
- T0U (a) at k and k + 1 gives t0 ∈ R_k ∖ R_{k+1}, so R_k ⊄ R_{k+1}.
- SPLIT (a) (H1 ∧ ¬H2 at k) excludes a non-fallback.
- τ is constant in the phase, so it is Even's fallback (an Odd fallback changes τ). ✓

## 3. SG-EV: SIGN
- The route of t0 at k lies in R_k ⊆ U ∖ {c_θ} (H1 at k).
- Some route vertex changes its next, else t0 ∈ R_{k+1}. Off o, next is σ or a forced edge. So the first such vertex y is Even and
  switched.
- R15 (d) makes (y, z) a gate. (A) at k + 1 (λ_{k+1}(y) = c_θ ≠ y) puts z in U.
- In κ form (same cycle node c_θ, so (M1′) with lengths): κ_k(z) > κ_k(σ_k y), and κ_{k+1}(z) ≥ κ_k(z) (R15 (a)). So κ_{k+1}(y) > κ_k(y).
- The unchanged prefix passes the difference to t0 by (A). ✓
- This is R19 (d)'s step (SG) without (h), as the remark says. The proof uses only H1 at k and the phase. ✓

## 4. T0-PIN: SIGN
- k = g_j with j ≥ |U| − 1, so k > g_{|U|−2}.
- At k + 1: H1 ∧ H2, so t0 ∈ F_{k+1} ∩ U. HAT-FREEZE (b), (c) give MoptÛ(t0) defined and M_{k+1}(t0) = MoptÛ(t0).
- At k: HAT-FREEZE (a) with j′ = |U| − 2 (simple paths of G_Û have ≤ |U| − 2 edges) gives ≥.
- (M2′) gives ≤. ✓

## 5. NHN-BOUND: SIGN (N-NHN-1)
- (a):
  - EV2 ends are distinct in-phase Even fallbacks g_j (EV2-FB). Those with j ≤ |U| − 2 number ≤ |U| − 2.
  - The others: M(t0) = m* at both ends (T0-PIN). By (M2′), {t : M_t(t0) = m*} is an interval I of the phase containing both ends.
  - On I, P(Ξ t0) is fixed (INJ) and the cycle node is c_θ, so the order is s_θ·ℓ, non-decreasing on I (R15 (a)).
  - SG-EV gives a strict rise at each such end. ℓ ∈ [1, |U| − 1] ((SP), t0 ≠ c_θ), so there are ≤ |U| − 2 rises.
  - Total ≤ 2(|U| − 2). ✓
- (b):
  - A non-last HN stretch of a phase ends at an in-phase transition to a non-HN state: either ¬H1 (a drop) or H1 ∧ H2 (an EV2 end).
    So N_HN ≤ 1 + drops + EV2 ends.
  - drops ≤ ⌈T/2⌉ (R34 (e), text checked).
  - So N_HN ≤ 1 + ⌈T/2⌉ + 2(|U| − 2) ≤ ⌈T/2⌉ + 2n − 3. ✓
- N-NHN-1 (citation; the same as REFEREE's RHO-N2 on P-N5-RHO, which I accepted in the RHO §C):
  - The τ(o) = o remark here and the first line of §7 cite "RESULTS R39 (f) (c)". R39 (f) is headed "Corollary NE-COUNT (τ(o) = o,
    case A; θ a parameter)", so (c) is landed for case A only.
  - The bound holds in case B too. τ(o) = o makes o's W-play its loop, so ¬H2 holds everywhere and HN = H1. H1 runs alternate with
    ¬H1 runs, so N_HN ≤ ⌊T_ph/2⌋ + 1 with T_ph ≤ T (R34 (e), no case hypothesis).
  - Suggested citation: "R34 (e), with HN = H1 when τ(o) = o".
  - Data: §9 (TOO), case B included.

## 6. H3-IN-HN: SIGN
- H3-CONST (R33 (a)): c_w = λ(t0) at every H2 state, and λ(t0) = c_θ (T0U (b)). ✓
- The bookkeeping consequence follows: in a phase with an HN state, H2 implies H3. So H1 ∧ H2 ∧ ¬H3 states occur only in phases
  without HN states. ✓

## 7. HN-POLY-ALL: SIGN CONDITIONAL (as labelled)
- This is P-N5-RHO §6 HN-POLY (signed by both referees through BRK-POLY′ (i′) and (ii)) with N_HN bounded by §5 for t0 ≠ o, and by
  R34 (e) for t0 = o (N-NHN-1).
- The orders follow:
  - N_HN = O(n²); ρ_HN = O(n³); Σθ_S = O(n⁴); ΣB_S = O(n⁵);
  - ΣX_S ≤ 2(n − 1)(ΣB_S + N_HN) = O(n⁶) (EPOCH, X_S ≤ 2(n − 1)(B_S + 1));
  - fallbacks from HN states ≤ K(ΣX_S + N_HN) + ΣX_S + N_HN = O(n⁸) with K = n_E(2n − 1).
  - Checked. ✓
- N-NHN-2 (statuses, for the fixes file): P-N5-PFZ, P-N5-PFZ-ext and P-N5-RHO are now signed by both referees. The PFZ-1 repair makes
  BRK-POLY′ (i) as stated available too (R2-N5-PFZ §C, C.2), but §7 needs only (i′).

## 9. Data (DATA, not proof)
- Batch (run_all.sh, logs/, totals_logs.txt): 492 𝒞^1O files × own / rand / spec × 3 starts = 4,428 runs; random 𝒞^1O 64,000 runs.
  1,484 / 1,484 logs "RESULT OK violations=0".
  - Phases 159,084: τ(o) ≠ o 132,316 (5,062 with an HN state), τ(o) = o 26,768.
  - T0U (a): 194,710 states. T0U (b): in all 5,062 phases.
  - EV2 ends: 45, in 31 logs, all in the library: box35 fbrestart_cex_n12 / n24, box38 tauw_B_cex_n24, box40 nhc_* climb outputs,
    referee climb outputs. All 45 are in-phase Even fallbacks evicting t0, and SG-EV gives a strict rise at each.
  - SG-EV hypothesis transitions: 45, every one an EV2 end (RECORD_SGEV_not_EV2 = 0). Random games reach none (as the packet says).
  - T0-PIN: 0 EV2 ends at j ≥ |U| − 1 (PIN checks 0). VACUOUS.
  - NHN-BOUND: max EV2 ends per phase 3, max N_HN 4 (nhc_tauw_B_cex_n24_23.pg, as in the packet). Drops 8 in all. N_HN ≤ 1 + drops +
    EV2 ends held in every phase.
  - H3-IN-HN: 7,237 H2 states in phases with t0 ≠ o and an HN state, all with H3.
  - τ(o) = o (N-NHN-1): ¬H2 at every state. N_HN ≤ ⌊T_ph/2⌋ + 1 in 1,252 case-A and 1,885 case-B phases with HN states. So the bound
    holds in case B, where R39 (f) is not landed.
- Mutation controls:
  - NHN_MUT=nhn (drop the "1 +" in N_HN ≤ 1 + drops + EV2): 10 violations on nhc_tauw_B_cex_n24_23.pg (logs_mut/).
  - NHN_MUT=pin1 (PIN from j ≥ |U| − 2): 0 violations on the 642 logs with HN phases (logs_mut_pin1/). No EV2 end lies even at
    j = |U| − 2, so T0-PIN is not approached.
- No climb was run for this packet. The packet's 5 climbs and the REFEREE-2 FB-POLY climbs (R2-N5-FBPOLY §9, toward f ≥ |U| − 1) did
  not reach post-freeze fallbacks at |U| ≥ 3, which T0-PIN would need.

## 10. Notes for the lane (none blocks a signature)
- N-NHN-1 (citation): τ(o) = o lines (§5 remark, §7 first line): cite R34 (e) with HN = H1, not R39 (f) (c) alone (case A only).
- N-NHN-2 (statuses): §0's "in review" / "REFEREE-2 10 to review" entries are out of date; see §7.

## §C. Comparison with REFEREE (REFEREE-2 successor 11, written 2026-10-25 20:1xZ by date -u)
Signature: (Opus 5.5, D15). Compared: docs/referee/R-N5-NHN.md at trunk (REFEREE 10, 9bb3f79d, sha1 c3b8714f…). I opened it only after
this report (04b5c1fd) was pushed.

| item | REFEREE-2 | REFEREE | outcome |
| --- | --- | --- | --- |
| §1-§3, §6 | SIGN | SIGNED | identical |
| §4 T0-PIN, §5 NHN-BOUND | SIGN (HAT-FREEZE signed by both) | SIGNED conditional on HAT-FREEZE ("REFEREE-2 pending" at its writing) | identical. The condition is now met: R2-N5-RHO 269ae45a + §C |
| §7 HN-POLY-ALL | SIGN CONDITIONAL as labelled, (i′) form | SIGNED with exactly those conditions, (i′) form | identical. Note: since my PFZ §C (212f88ec), (i) as stated is also signed by me with the PFZ-1 repair, so REFEREE's "REFEREE-2 signs (i′), not (i)" is out of date; (i′) still suffices here |
| τ(o) = o citation | N-NHN-1 | NHN-N1 | identical; both suggest R34 (e) with HN = H1 (REFEREE adds "§5 (b)'s argument with no EV2 end", also correct) |
| Consequence's "there" | — | NHN-N2 (wording): "there" must mean "in a phase containing a Q state" | ACCEPTED; I missed it. A phase without HN states can have H3 at every H2 state (H3-CONST makes H3 constant over a phase's H2 states), so "there H3 fails at every H2 state" is true only of phases that contain a Q state |
| thin spots | T0-PIN vacuous; EV2 45; max N_HN 4 | T0-PIN vacuous (climbs: latest EV2 end at j = \|U\| − 9); 1.02 M EV2 ends in climbs; 35 DROPs ending a stretch in climbs | consistent. REFEREE's climbs exercise (b)'s DROP branch, which my batch does not separate (my "drops" counter counts every H1 → ¬H1 transition in such phases: 8; I do not claim that they end stretches) |

- Joint gap map: EMPTY. No verdict of mine changes. (Opus 5.5, D15)
