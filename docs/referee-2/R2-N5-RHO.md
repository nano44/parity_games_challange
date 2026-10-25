# R2-N5-RHO: second-referee check of packet P-N5-RHO (L-NEW box 40: Y-FORM, HAT-FREEZE, RHO-TAIL, BF-F, FREEZE-F, RHO-HN, HN-POLY). REFEREE-2 (successor 10), written 2026-10-25 17:2xZ-18:0xZ (date -u)
Signature: (Opus 5.5, D15). Lead queue 16:54Z (Lead's stamp). Object: docs/new/P-N5-RHO-box40.md, sha1
cd5df65c2f3e6829f85739a57023fc3da6944baa; the same at the pin c814455 and on my tree.
Background read: SPEC S1-S5 (A_σ(v) = {σ(v)} ∪ improving targets, S4a); RESULTS R15 (a), (d), R17 (a) ((V1), (F1)), R19 (a), R21 (a),
R39 (a)-(c), (f); P-N5-PFZ §0-§6 and P-N5-PFZ-ext (R2-N5-PFZ, both sections).
Independence: nothing in docs/referee/ read for this packet; REFEREE 10's report is not opened. The packet quotes "REFEREE's GAP PFZ-1"
and its repair (P-N5-RHO l. 10-11, 213-214); I read only that quotation, in the packet. No lane script (rhodata.py, rhoclimb.py,
box39/rho.py) run or imported.
Tools: docs/referee-2/R2-N5-RHO/ (own code on R2-N5-OUT/out_check.py, conventions of R2-N5-PFZ/pfz_check.py): rho_check.py,
rho_climb.py, files.lst, run_all.sh, run_climbs.sh, totals.py, logs/, climb/, totals_logs.txt, totals_climb.txt.
Traces own / rand / spec. Every game asserts exactly one Odd vertex with out-degree > 1.
Labels: PROVED (L-NEW succ. 18 / 19). Not a running-time bound, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN, and N_HN is
a parameter.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §0 facts (A), (A0), (M1′), (M2′), (INJ), (HP), (SP) | correct | — |
| §1 Lemma Y-FORM | SIGN | — |
| §2 Lemma HAT-FREEZE (a)-(c) | SIGN | — |
| §3 Theorem RHO-TAIL | SIGN | — |
| §4 Lemma BF-F | SIGN | — |
| §5 Theorem FREEZE-F (a)-(c) | SIGN | — |
| §6 Theorem RHO-HN | SIGN | N-RHO-1 (wording): the proof gives (N_HN + |U| − 3)(…) + deg(o); the stated bound is weaker |
| §6 Corollary HN-POLY | SIGN (its BRK-POLY′ inputs are the forms I signed: (i′) and (ii)'s first inequality, R2-N5-PFZ §X) | — |
| §7, §8 | not signed (as briefed) | — |
No statement is NOT SIGNED, and no gap is open. 0 violations in 68,131 batch runs and in 1,545,712 climb runs.
Thin spots, as the packet's §8 says:
- FREEZE-F (b) is vacuous in all my data (0 states with t ≥ s + |U| − 2).
- HAT-FREEZE (c) / RHO-TAIL are exercised past the freeze only at |U| = 3 (133,889 phases in all), never at |U| ≥ 4.
- RHO-TAIL's count there is always 0.

## 1. Y-FORM: SIGN
- (a) Under H1, λ(o) = c_θ ≠ o, and (A) gives M(o) = wt(o) + M(σ̄ o). σ̄(o)'s honest play is the rest of o's, which never returns to o, so
  σ̄(o) ∈ F by (HP). Hence σ̄(o) ∈ Y and M(o) ≥ wt(o) + min_Y M.
- For the other inequality, take y ∈ Y and τ′ with τ′(o) = y. y's play avoids o and is the same under τ and τ′, so V_{σ,τ′}(y) = W(y) =
  Ξ(y) (G (a)) and V_{σ,τ′}(o) = o ⊕ Ξ(y). Lemma S (a) / XW give Ξ(o) ⊴ o ⊕ Ξ(y). Both values have cycle node c_θ (y ∈ U), and o ∉ P(Ξ y).
  (M1′) then gives M(o) ≤ wt(o) + M(y). ✓
- (b) o lies on its honest cycle, which is topped by c_θ. Every vertex of o's path to c_θ is on that cycle, so it has rank < rank c_θ,
  and P(θ) = ∅. ✓

## 2. HAT-FREEZE: SIGN
- (a) is P-FREEZE (a)'s induction (signed, R2-N5-PFZ §2) on G_Û. The only terminal is c_θ, and o is not a vertex.
  - An Odd z ∈ Û has an edge only if its forced successor is in Û. So an Odd vertex forced into o is a dead end, and nothing reads o's
    value.
  - The Even step is FB-ROUND at g_j (x ∈ Û ⊆ U) and then (M2′). θ, H1, H2 and τ(o) are not used. ✓
- (b) For z ∈ F_t ∩ U: its honest play avoids o (HP), and up to c_θ it is a simple path in U (SP), hence in Û. Its Even steps are σ_t-edges
  into Û, and its Odd steps are forced edges into Û. So it is a path of G_Û, and (A) along it gives M_t(z) = wt(p ∖ {c_θ}) ≤ MoptÛ(z). ✓
- (c) Simple paths in G_Û have ≤ |U| − 2 edges, so (a) at j = |U| − 2 and (b) meet. ✓

## 3. RHO-TAIL: SIGN
- After g_{|U|−2}:
  - at an H1 state, M(o) = wt(o) + MoptÛ(y) for the minimising y ∈ Y_t ⊆ succ(o) ∩ U, by Y-FORM (a) and HAT-FREEZE (c) (Y_t ⊆ F_t ∩ U);
  - at a ¬H1 state, M(o) = 0.
- So M(o) takes ≤ deg(o) + 1 values. It is non-decreasing ((M2′) at o; λ(o) = c_θ holds on the whole phase, H1 or not). So it changes at
  ≤ deg(o) transitions, and (INJ) identifies those with the P(θ)-changes. ✓

## 4. BF-F: SIGN
- v ∈ F_{k+1} ⊆ F_k (SPLIT at the non-fallback k with H1 ∧ ¬H2). Case 1 is (A) + (M2′).
- Case 2: M_k(x) > M_k(σ_k v) with both values on c_θ. (M1′) and totality give Ξ_k(x) ▷ Ξ_k(σ_k v). So x ∈ A_σ(v) (SPEC S4a: σ(v) and
  the improving targets), and σ″ is a strategy of the S4a arena. (F1) gives W_{k+1} ⊵ W_{σ″}, and W_{k+1}(v) = Ξ_{k+1}(v) (G (a), v ∉ R̄_{k+1}).
  - x ∈ R̄_k: under ¬H2, o's W-cycle C_W ⊆ R̄_k. x's play (π_x, then C_W) avoids v and is unchanged under σ″. So W_{σ″}(v) has cycle node c_w.
    c_θ ∈ F_k (HP) and c_w ∈ R̄_k, so c_θ ≠ c_w. XW at o with distinct cycle nodes gives reward(c_θ) < reward(c_w) (ranks are distinct, so
    distinct nodes have distinct rewards). Against (F1). ✓
  - x's play passes v: the prefix q before v is simple. (A) / (A0) along q · v give M_k(x) − M_k(σ_k v) = wt(q ∪ {v}) > 0. Under σ″, v
    lies on the cycle C = q ∪ {v}, which avoids o. The top-rank vertex u of C's high part dominates the signed sum, so it is even. Every
    other vertex of C has rank ≤ rank c_θ < rank u, so u tops C. reward(u) > reward(c_θ), against (F1). ✓
  - Otherwise: W_{σ″}(v) = v ⊕ Ξ_k(x) on c_θ, with v ∉ P(Ξ_k x). (F1) and (M1′) give the claim. ✓
- The three sub-cases are exhaustive (x ∈ R̄_k, or x ∈ F_k with its play passing v or not).

## 5. FREEZE-F: SIGN
- Every transition of [s, e] is S4a, so F_t shrinks (SPLIT) and c_θ ∈ F_t (HP). Paths of G[F_{t+1} ∩ U] are paths of G[F_t ∩ U].
- (a): induction on t − s, with BF-F for Even z (z ∈ U ∩ F_{t+1}, x ∈ U) and (A) + (M2′) for Odd z. ✓
- (b): |F_t ∩ U| − 1 ≤ |U| − 2 (o ∉ F_t). The honest play of z ∈ F_t ∩ U is a path of G[F_t ∩ U]: its vertices' plays are suffixes of z's,
  so they lie in F_t. So M_t = MoptF_t from s + |U| − 2 on. Then MoptF_{t′} ≤ MoptF_t (fewer paths) together with (M2′) gives equality. ✓
- (c): ≤ |U| − 2 changes before t*. After t*, H1 holds (HN), M(o) = wt(o) + min_{Y_t} of frozen numbers, and Y_t shrinks and is never
  empty (σ̄(o) ∈ Y_t). So the minimum is non-decreasing and takes ≤ |Y_{t*}| ≤ deg(o) values: ≤ deg(o) − 1 changes. |U| ≥ 2 under H1. ✓

## 6. RHO-HN and HN-POLY: SIGN (N-RHO-1)
- F-FLAT removes the HN → HN fallbacks; RHO-TAIL takes t > g_{|U|−2}. Each remaining S4a change lies in a maximal fallback-free HN run that
  starts at an HN-stretch start or at g_j + 1 with j ≤ |U| − 3. That gives ≤ N_HN + |U| − 3 runs, each with ≤ |U| + deg(o) − 3 changes. ✓
  - The count is right also when the phase has fewer than |U| − 2 fallbacks (then j ≤ #fallbacks ≤ |U| − 3) and when |U| = 2 (the rest is
    empty).
  - N-RHO-1: the proof gives (N_HN + |U| − 3)(|U| + deg(o) − 3) + deg(o). The statement's N_HN + |U| − 2 is weaker and right.
- HN-POLY:
  - Σ_S (ρ_S + 1) ≤ ρ_HN + N_HN: every HN → HN transition of the phase lies in exactly one stretch.
  - It uses BRK-POLY′ in the form (i′) θ_S ≤ ρ_S + (ρ_S + 1)·max(|U| − 2, 0) and (ii)'s first inequality, plus the arithmetic
    θ_S + (ρ_S + 1)(|U|² − 1) ≤ (ρ_S + 1)(|U|² + |U| − 2) ≤ (ρ_S + 1)(2n² − 1). These are exactly the forms I signed in R2-N5-PFZ §X
    (G-PFX-1). ✓
  - EPOCH sums ✓.
  - The orders: ρ_HN = O(n(N_HN + n)), Σ B_S = O(n⁴ N_HN), Σ X_S = O(n⁵ N_HN), fallbacks O(n⁷ N_HN), using N_HN ≥ 1 whenever there is
    an HN state. ✓ For τ(o) = o they are polynomial via R39 (f) (c). ✓

## 7. Data (DATA, not proof)
- Batch (R2-N5-RHO/run_all.sh, logs/, totals_logs.txt): 459 𝒞^1O files (R2-N5-PFZ/filesx.lst + the 6 tracked experiments/new/box40/out/*.pg)
  × 3 traces × 3 starts = 4,131 runs; random 𝒞^1O 64,000 runs. 1,385 / 1,385 logs end "RESULT OK violations=0".
  - Library (all traces):
    - 17,012 phases, 1,798 with HN states; exact-optimum checks skipped (and counted) in 10,182 phases with |U| > 12.
    - Y-FORM (a) 58,579 states, (b) 8,870.
    - HAT-FREEZE (a) 3,342, (b) 27,186, (c) 15 checks; 15 phases past g_{|U|−2} with |U| = 3 and an H1 state.
    - RHO-TAIL: 527 phases past the freeze, max 0 changes.
    - BF-F: 174,890 checks, 2,636 in Case 2.
    - FREEZE-F: 2,646 runs, (a) 364 checks, (b) 0 states, (c) max 16 changes (bound max(|U| − 2, 0) + deg(o) − 1).
    - ρ_HN: 892 in total, max 16 in one phase. Σ θ_S max 16, Σ B_S max 2.
  - Random: 140,491 phases, 6,447 with HN states; ρ_HN 1 in total; 18 phases past the freeze at |U| = 3. As the packet says, random games
    give almost no HN material.
- Climbs (run_climbs.sh, climb/, totals_climb.txt), FIT rho, three × 1,200 s:
  - seeds: 9701 random n 6-10; 9702 and 9703 seeded with the lane's box-40 climb outputs rhc_rhc_oneodd_c16_2_5.pg and
    rhc_rhc_block_bk20_3_4.pg (inputs only);
  - 386,428 evaluations, 1,545,712 runs, 0 violations;
  - 133,856 phases past g_{|U|−2} with |U| = 3 and an H1 state (HAT-FREEZE (c) 3,867 exact checks, RHO-TAIL max 0 changes), never
    |U| ≥ 4. FREEZE-F (b) 0 states. BF-F 6,337 checks (227 in Case 2).
- Mutation controls:
  - RHO_MUT=hatall (HAT-FREEZE (c) at every state, not only after g_{|U|−2}): 701 violations on 3,000 random games.
  - RHO_MUT=frzb0 (FREEZE-F (b) from s): 0 violations on the same games and on epsseg_cex_n48.pg. So M on F ∩ U was already constant from
    s in the runs tested, and this control does not show that the (b) check can fail. (b) is vacuous anyway.

## 8. Notes for the lane (none blocks a signature)
- N-RHO-1 (wording): RHO-HN's proof gives the sharper (N_HN + |U| − 3)(|U| + deg(o) − 3) + deg(o).
- N-RHO-2 (DATA): FREEZE-F (b) and the post-freeze regime at |U| ≥ 4 are reached by no data, the lane's or mine. A target for L-RED.

## §C. Comparison with REFEREE (REFEREE-2 successor 11, written 2026-10-25 18:5xZ by date -u)
Signature: (Opus 5.5, D15). Lead GO 18:27Z (Lead's stamp). Compared: docs/referee/R-N5-RHO.md at trunk 42d8c3a9 (sha1 5a8ec11d…): REFEREE
10's report 59278313 and its §C 06d6e6d, against this file's report 269ae45a (successor 10). I opened R-N5-RHO only after 269ae45a was
on the branch and on trunk. Object unchanged: P-N5-RHO sha1 cd5df65c….

### Verdicts
| item | REFEREE-2 | REFEREE | outcome |
| --- | --- | --- | --- |
| Y-FORM, HAT-FREEZE (a)-(c), RHO-TAIL, BF-F, FREEZE-F (a)-(c), RHO-HN | SIGN | SIGNED | identical |
| HN-POLY | SIGN through BRK-POLY′ (i′) and (ii)'s first inequality | SIGNED conditional on the same two forms | identical. My PFZ §C (C.2) now also signs BRK-POLY′ (i) as stated with REFEREE's repair; HN-POLY does not need it |
| §7, §8 | not signed | not signed | identical |
- Joint gap map: EMPTY. I agree with REFEREE's §C table except where I add to it below.

### Notes
- N-RHO-1 = REFEREE's §6 sharper count: identical.
- RHO-N1 (o = c_θ with |U| ≥ 2: 89/990 library phases; covered vacuously). I accept it and its suggested wording.
- RHO-N2 (citation). I ACCEPT it: successor 10 MISSED it.
  - P-N5-RHO's HN-POLY τ(o) = o line (l. 89, l. 222) cites NE-COUNT (c), RESULTS R39 (f).
  - RESULTS R39 (f) is headed "Corollary NE-COUNT (τ(o) = o, case A; θ a parameter)" (`grep` RESULTS.md). Its (c) is landed for case A only.
  - REFEREE's case-B argument, re-derived:
    - τ(o) = o makes o's (σ, τ)-play the loop o → o, so o lies on its own W-cycle at every state. So ¬H2 holds everywhere and HN = H1.
    - An HN stretch is then a maximal H1 run of the phase. H1 runs and ¬H1 runs alternate, separated by H1-toggles. So
      N_HN ≤ ⌊T_ph/2⌋ + 1.
    - TOGGLE-COUNT (RESULTS R34 (e): "H1-toggles per phase ≤ T := |U|(n + 1) + n − 1 ≤ n² + 2n − 1", no case hypothesis) bounds T_ph.
  - So the claim holds in case B as well. Only the citation changes: "R34 (e), with HN = H1 when τ(o) = o".
- RHO-N3 / N-RHO-2 (data): the same thin spots on both engines. Post-freeze occurs only at |U| ≤ 3, never at |U| ≥ 4. FREEZE-F (b) is
  vacuous. RHO-TAIL has 0 changes past the freeze. Both name these as targets for L-RED.
- No verdict of mine changes. (Opus 5.5, D15)
