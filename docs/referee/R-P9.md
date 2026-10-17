# Referee report R-P9: the R11 count with factor k, Lemma CHARGE and the depth bound (GAP-A-M §23f, §23g)

Referee: REFEREE (successor), running on Opus 5.5 under owner ruling D12 (Lead reading L33). Packet 9: the Lead's message of
20:10Z. Pin: trunk c5e2b4d, docs/alg/GAP-A-M.md §23f (line 2904) and §23g (line 2944). Code: dtl.cpp @ 8fbf0a7 ("N" = that
line). Builds on R-P7 (EXACT, PREFIX-MONO-X, corollary), R-P8 (EXACT*, PREFIX-MONO-X*) and G-P7-c2. Written 20:12Z-20:19Z
(date -u). docs/referee-2/R2-P9.md was not read.

## Verdict
| item | verdict (Opus 5.5, D12) | lines checked |
|---|---|---|
| (a) §23f: F_R ≤ 3·N*_R ≤ 3·Σ_q k_q ≤ 3·k_R·(\|R\|+1)·\|R\|·#fired(R); GAP-A ⇐ (CTX⁺) ∧ (STEAL-POLY) ∧ (FIRED-R) given STR-DET | SIGN (note N9-a1: a misattributed, unused remark) | 662-667, 748-772 |
| (b) §23g Lemma CHARGE | SIGN WITH GAPS: G9-b1 (notation P(τ) for the prefix P(τ⁺); closed), G9-b2 (visits with fewer rounds; closed here). G23g-1 and G23g-2 CHECKED, closed. Note N9-b1 (cite dtl.cpp, not pyref) | 138-139, 662-667, 690-705, 713-772 |
| (c) §23g depth bound and counting | SIGN WITH GAPS: G9-c1 ("sum form of (STEAL-POLY)" needs (FIRED-R); closed). Constants checked. STEAL-POLY follows only for CONSTANT D | n/a |
| (d) stealonce_viol_n76, dtl_stealdepth.py unmodified, both orders | CONFIRMED: stable has one re-steal, depth 1, with one cause; Oink has none. My own probe agrees | probe |

## (a) The R11 count with the factor k
- F_R ≤ 3·N*_R: signed (R-P8 G8-1 = G-P7-c2), with N*_R = # consecutive visit pairs of R with a relevant steal.
- N*_R ≤ Σ_q k_q: every counted pair has at least one relevant quadruple q = (R, r, τ, t), and Σ_q k_q counts
  (pair, quadruple) incidences. ✓
- Σ_q k_q ≤ k_R·Q, with Q the number of quadruples that are ever relevant steals:
  - r ≤ |V_1| + 1 ≤ |R| + 1, since every non-final round removes a vertex (748-772) and V_1 is the p-vertices of R
    (662-667);
  - τ is a p-vertex of R, so there are at most |R| tops;
  - t ∈ F_{r,τ} of the earlier visit, i.e. a tangle that fired at R.
  So Q ≤ (|R| + 1)·|R|·#fired(R). ✓
- Hence GAP-A ⇐ (CTX⁺) ∧ (STEAL-POLY) ∧ (FIRED-R), given STR-DET. This is a valid conditional, with the R9/R10 budgets as of
  record. SIGN.
- N9-a1 (unused remark). §23f says "the factor tightens to 2 given STR-DET (REFEREE-2 R2-P8 §7; one signature)".
  - R2-P8 has no §7. The one-signature STR-DET constants are mine (R-P7 §C2), and they concern R9's per-context term, not the
    3 in F_R ≤ 3·N*_R. REFEREE-2's R2-P7 §7 gives the DOUBLED constants.
  - The 3 → 2 does follow by the same device: with STR-DET (c), a consecutive pair inside the overlap of two e*-intervals has
    an equal tangle set, so it carries no steal, and F^e ≤ N*_R. But it is not used, and it is not signed by two referees.
  - Fix the citation, or drop the remark.

## (b) Lemma CHARGE
The claim: every re-steal e of q = ((r, τ), t) at pair i, with the previous event of q at pair j < i, has a cause. A cause is
an event (a relevant steal) at a pair m, with j < m < i, at a step strictly earlier than (r, τ). Distinct re-steals of one q
have distinct causes.

G9-b1 (notation; closed). The proof writes P_{j+1}(τ) and P_i(τ). In §22r's notation P(τ) is the prefix AFTER τ's region, and
with that reading "t ∩ P_i(τ) = ∅" is false: t fired in region τ, so t ⊆ P_i(τ). The intended object is the prefix BEFORE τ,
P(τ⁺) at round r. With P_v := P_v^{(r)}(τ⁺) every step is correct:
- At visit j+1, t ∈ E′: t meets P_{j+1} and is not contained in it (definition of the steal at pair j).
- At visit i, t ∈ F_{r,τ}. A fired tangle has no vertex outside CurR ∪ CurZ (138-139), and P_i ∩ CurR = ∅ (690, 699). So
  t ∩ P_i = ∅. ✓
- So some w ∈ t ∩ P_{j+1} has w ∉ P_i. Let m be the LAST visit in [j+1, i−1] with w ∈ P_m. Then w ∉ P_{m+1}, so
  P_m ⊄ P_{m+1}, with j < m < i. ✓
- Contrapositive of the local PREFIX-MONO-X* (G23g-1): either (NS*) fails at a step (r, τ′) with τ′ > τ at pair m, or
  V_r(m) ⊄ V_r(m+1). In the second case, the contrapositive of the round alignment (G23g-2) gives a relevant steal at a step
  of an earlier round at pair m. Both are strictly earlier steps. ✓

G23g-1 (CHECKED, closed): the local form of PREFIX-MONO-X*.
- R-P7/R-P8's induction runs over τ′ in decreasing order and uses, at τ′:
  - (NS*) at τ′, in the case where τ′ is processed in both runs;
  - the unconditional closedness of P′(τ′⁺), in the absorbed case;
  - τ′ ∈ V ⊆ V′, in the absorbed case: τ′ processed in run 1 and not in run 2 means τ′ ∈ P′(τ′⁺). This step NEEDS V_r ⊆ V′_r;
    without it, τ′ ∉ V′ is possible and the case fails. §23g's hypothesis includes it.
- So "(NS*) at every step of round r above τ, and V_r ⊆ V′_r" ⇒ P(τ⁺) ⊆ P′(τ⁺). ✓

G23g-2 (CHECKED, closed): the round alignment.
- V_r ⊆ V′_r follows by C1-C3 from (NS*) at ALL steps of rounds 1..r−1, including the lower tops: C1 needs the whole union
  U = P(lowest). All of these steps are earlier than (r, τ) in the step order. ✓
- The threshold loop (722-741) and the survivors (713-772) add no case: Gx = R, nothing is consumed, all of Z is pushed (724).

G9-b2 (closed here). The proof compares round r at visits m and m+1, but a visit can have fewer than r rounds.
- If the later visit stopped at round r′ < r with "no candidates" (716 or 765), its later rounds repeat round r′, because the
  call is a function of (V, R, T). Take P^{(r)}_{m+1} := P^{(r′)}_{m+1}.
  - Unless a relevant steal occurs at a step of rounds ≤ r′, which is itself a cause, C3 gives
    V_{r′+1}(m) ⊆ V_{r′+1}(m+1) = V_{r′}(m+1), and V_r(m) ⊆ V_{r′+1}(m) since V shrinks.
  - So the local lemma applies to the virtual round, and the conclusion is unchanged.
- If the later visit stopped with V′ = ∅ (768-771) at round r′ < r, then V_{r′+1}(m) ⊆ ∅ unless a steal occurred at a round
  ≤ r′, so visit m would have no round r. That contradicts w ∈ P_m. Hence an earlier-round steal exists.
- The earlier visit m has round r, since w ∈ P_m.

Distinct causes. The re-steals of q own the open pair intervals (j_1, i_1), (i_1, i_2), ..., which are disjoint, so their
causes lie at distinct pairs and are distinct events. ✓
N9-b1: the proof cites "dtl_pyref attractTangle lines 86-89"; the code step is dtl.cpp 138-139.
SIGN WITH GAPS (G9-b1, G9-b2 closed; G23g-1/2 checked).

## (c) Depth and counting
- Well-defined: causes lie at strictly earlier steps, so depth is defined by induction over the step order.
  depth ≤ #steps − 1 ≤ (|R| + 1)|R| − 1 (PROVED, given CHARGE). ✓
- E_0 ≤ Q (one first event per q). ✓
- E_d ≤ Q·E_{d−1}. For a fixed q, each depth-d re-steal picks a min-depth cause, which has depth exactly d − 1. Distinct
  re-steals have distinct causes. So q has ≤ E_{d−1} depth-d re-steals; summing over q gives the bound. ✓
  Hence E_d ≤ Q^{d+1}.
- Σ_q k_q = Σ_{d ≤ D} E_d ≤ Σ_{d ≤ D} Q^{d+1} ≤ 2Q^{D+1}.
  - For Q ≥ 2 this is the geometric sum.
  - For Q = 1 no re-steal exists (a cause is an event of another quadruple), so the sum is 1. ✓
  - F_R ≤ 3·2Q^{D+1} = 6Q^{D+1}. ✓
- Constant D only. Q ≤ (|R|+1)|R|·#fired(R) is about |R|²·#fired(R).
  - Q^{D+1} is polynomial iff D = O(1), given (FIRED-R).
  - D = O(log n) gives only quasi-polynomial.
  - The proved depth bound, D ≤ (|R|+1)|R| − 1, gives Q^{Θ(n²)}: exponential.
  So (c) gives (STEAL-POLY) only for constant D, as §23g says.
- G9-c1 (closed, wording). §23g says "(STEAL-DEPTH_D) ⇒ (STEAL-POLY) in the sum form of §23f". That sum form is
  Σ_q k_q ≤ poly(|R|)·#fired(R). But 2Q^{D+1} = 2((|R|+1)|R|)^{D+1}·#fired(R)^{D+1}, which is of that form only given
  (FIRED-R). Since (FIRED-R) is a premise of the GAP-A statement anyway, the conclusion stands:
  GAP-A ⇐ (CTX⁺) ∧ (FIRED-R) ∧ (STEAL-DEPTH_D for a constant D), given STR-DET. (STEAL-DEPTH_D) and (FIRED-R) are DATA,
  not signed.

## (d) stealonce_viol_n76 (sha1 32c2da0b6ff0ad87b3f7d725e351356bd8e14172, checked)
- Pinned Oink 8fbf0a7, `--dtl --no-single --no-wcwc --no-loops -v`: "solved in 7 iterations", "solution verified
  (33 strategies)".
- dtl_stealdepth.py, unmodified (RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0):
  - stable: "RE-STEAL ... |R| 76 pair 5 step (r4, top 18) t 7 k 2 depth 1 | previous 2 | causes (pair, step, tangle,
    depth): [(3, (4, 66), 9, 0)]"; max k 2, max depth 1; 6 contexts with k = 1, 1 with k = 2.
  - Oink: max k 1, max depth 0.
- My own probe (p8probe.py, p9charge.py, on pyref with my own steal and fired-set logging):
  - stable: one re-steal at pair 5, previous pair 2, round 4, tangle 7. Its single cause is at pair 3, round 4, tangle 9.
    In my index order the tops read 31 and 74 instead of 18 and 66, a different internal numbering of the same vertices.
  - Oink: no re-steal; "no cause" 0.
  - (STEAL-ONCE*): max 2 (stable), 1 (Oink). EXACT and EXACT* hold at all 15,147 / 8,153 steps.
So the instance kills (STEAL-ONCE*) in stable order and is consistent with CHARGE and depth 1.

## What remains for GAP-A
GAP-A ⇐ (CTX⁺) ∧ (FIRED-R) ∧ (STEAL-DEPTH_D, D constant), given STR-DET. All three premises are DATA only.
- The data has exactly one re-steal, of depth 1, on a constructed instance.
- CHARGE turns (STEAL-POLY) into a depth question. It does not bound the depth: only #steps is proved, which is exponential
  in the counting.

## §C. Comparison with REFEREE-2 (R2-P9, referee-2 2612634 + §5 at 19a94b8, read from claude/referee-2 because trunk 93d6f5d does not carry it yet; 20:30Z by date -u)
The verdicts agree on every item, and there is no disagreement on the mathematics. (Opus 5.5, D12)
- (a): both SIGN. (b) CHARGE: both SIGN WITH GAPS, same G9-b1 (P(τ) → P(τ⁺)). The labels differ:
  - my N9-b1 (cite dtl.cpp) = R2's G9-b2;
  - my G9-b2 (visits with fewer rounds) = R2's round convention inside G23g-2 (R2-P7 §3), closed the same way.
  - G23g-1/2: both closed. R2 agrees that the absorbed case needs V_r ⊆ V′_r.
- (c): both sign the constants. My Q = 1 remark = R2's N9-c1. Both say constant D only. R2 sharpens the proved depth bound to
  exp(Θ(n² log n)) and notes that D = Θ(log n) is quasi-polynomial, excluded by TARGET §4. I agree.
- (d): same re-steal and cause, same internal tops 31 / 74 in stable order. R2's extra datum: 32 of 50 random tie-break orders
  show the same re-steal, so DE20's kill is not specific to one order datum.
My N9-a1 is WITHDRAWN. R2-P8 §7 exists (c2ac652, line 139). I read R2-P8 at b8fdd76, before §7 was added, and did not
re-check. §23f's citation "REFEREE-2 R2-P8 §7; one signature" is correct: that section signs my R-P7 §C2 constants and
remarks the 3 → 2 tightening, the same derivation as in my N9-a1. Nothing to fix in §23f.
R2's N9-a1: ACCEPTED.
- With (STEAL-POLY) in the packet's sum form, "Σ_q k_q polynomial per phase", F_R ≤ 3·Σ_q k_q gives (FALL) per context
  directly. So GAP-A ⇐ (CTX⁺) ∧ (STEAL-POLY) given STR-DET, and (FIRED-R) is redundant for (a).
- (FIRED-R) is needed only for the per-quadruple form k_R ≤ poly(|R|), for §23f's own sum form Σ_q k_q ≤ poly(|R|)·#fired(R),
  and for (c)'s route through Q^{D+1}. My G9-c1 is the last of these.
Joint working conclusion: GAP-A ⇐ (CTX⁺) ∧ (FIRED-R) ∧ (STEAL-DEPTH_D, D constant), given STR-DET. All three premises are DATA
only.
