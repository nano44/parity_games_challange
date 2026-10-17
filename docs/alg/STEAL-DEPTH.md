# STEAL-DEPTH: Lemma CHARGE and the depth count (draft for a referee packet; L-ALG succ. 7, produced on Opus 5.5)
Status: packet 9 SIGNED (REFEREE R-P9, REFEREE-2 R2-P9, trunk 25111fa) with gaps G9-b1/G9-b2 closed; the imports are in
GAP-A-M §23k. Below, the prefix in CHARGE's proof is P(τ⁺) (the prefix BEFORE τ), per G9-b1. Originally a reading of dtl.cpp @ 8fbf0a7. Source of truth for the context is docs/alg/GAP-A-M.md §23f-§23g. This
file only restates them self-contained. Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every
order datum (L22/L26).

## Setting (as in RESULTS R10, R11)
- Fix one phase and a best_vertices context R. Its visits in the phase are 0, 1, 2, ...
- A step is σ = (r, τ): round r, processed top τ. Steps are ordered by rounds ascending, then tops descending (the
  processing order, dtl.cpp 691).
- P_i(σ) is the prefix before τ in round r at visit i, i.e. the union of the regions of the earlier tops of round r.
- F_σ(i) is the set of tangles that fire in the region step σ at visit i.
- An EVENT (i, q), with q = (σ, t), is a relevant steal: t ∈ F_σ(i), and t meets P_{i+1}(σ) without being contained in it.
- k_q is the number of events of q. Q is the number of q with k_q ≥ 1, so Q ≤ (|R| + 1)·|R|·#fired(R) (R11 (d); rounds
  ≤ |R| + 1, dtl.cpp 748-760).
- Signed facts used: Lemma EXACT and PREFIX-MONO-X* (R10 (a), R11 (b)), and the §22r Corollary.
- Proved here, as readings: the local form of PREFIX-MONO-X* and the V alignment.

## Lemma CHARGE
Let (i, q) be an event of q = ((r, τ), t) and let (j, q), j < i, be the previous event of q. Then there is an event (m, q′)
with j < m < i whose step σ′ is strictly earlier than (r, τ). Distinct such pairs (j, i) of the same q get distinct m.

Proof.
1. (All prefixes below are P(τ⁺) of round r, the prefix BEFORE τ; G9-b1.) At visit j+1, t ∩ P_{j+1}(r, τ⁺) ≠ ∅. This is the steal at pair j.
2. At visit i, t ∈ F_(r,τ)(i). A tangle fires only if each of its vertices is in CurZ or in CurR (dtl.cpp attractTangle
   131-137: `Z[v]` continue, `!R[v]` return false, with R = CurR and Z = CurZ at lines 700-701). CurR = R minus every
   vertex popped so far in this round (line 690, line 699). So t ∩ P_i(r, τ⁺) = ∅.
3. So some w ∈ t ∩ P_{j+1}(r, τ⁺) is not in P_i(r, τ⁺). With m the last visit in [j+1, i−1] holding w:
   P_m(r, τ⁺) ⊄ P_{m+1}(r, τ⁺). Visits with fewer than r rounds: G9-b2 (GAP-A-M §23k).
4. Local PREFIX-MONO-X*. Suppose that at pair m no step of round r above τ has an event, and V_r(m) ⊆ V_r(m+1). Then
   P_m(r, τ) ⊆ P_{m+1}(r, τ). This is the induction of R10's PREFIX-MONO-X proof (GAP-A-M §22r), "by induction over τ
   in decreasing order". Its three cases (τ not processed in run 1, processed in both, processed in run 1 only) use the
   (NS*) hypothesis only at the current step, plus the induction hypothesis P(τ⁺) ⊆ P′(τ⁺).
5. V alignment. If V_r(m) ⊄ V_r(m+1), then some round r′ < r has an event at pair m. This is the contrapositive of the
   §22r Corollary (rounds aligned inductively, C1-C4 of §22c). The threshold loop has no exclusions (tattr with
   consume = None, Gx = R, dtl.cpp 730), so it adds no case.
6. By 3-5, pair m has an event at a step earlier than (r, τ).
7. Distinctness. For consecutive events j < i < i′ of q, the m found lies in [j+1, i−1] and the next one in [i+1, i′−1].
   These intervals are disjoint. □

## Depth and the count
- depth(first event of q) = 0. depth(a later event of q) = 1 + min over its CHARGE causes of their depth.
- (i) depth ≤ (number of steps) − 1, since causes are strictly earlier steps.
- (ii) Let E_d be the number of events of depth d. Then E_0 ≤ Q and E_d ≤ Q·E_{d−1}.
  - Fix q. Its events of depth d ≥ 1 each choose a cause of depth exactly d − 1.
  - By the distinctness in CHARGE these causes are distinct events.
  - So q has at most E_{d−1} events of depth d. Summing over the at most Q values of q gives E_d ≤ Q·E_{d−1}.
- (STEAL-DEPTH_D): every event has depth ≤ D. Under it, Σ_q k_q = Σ_{d ≤ D} E_d ≤ Σ_{d ≤ D} Q^{d+1} ≤ 2·Q^{D+1}.
- With R11 (c) (F_R ≤ 3·N*_R ≤ 3·Σ_q k_q): F_R ≤ 6·Q^{D+1}.
- So GAP-A ⇐ (CTX⁺) ∧ (STEAL-DEPTH_D for a constant D) ∧ (FIRED-R), given STR-DET.

## Data (evidence only; GAP-A-M §23g)
- The only re-steal found: stealonce_viol_n76 (RESULTS DE20), stable order. Its depth is 1, k = 2, and the cause is the
  depth-0 steal of tangle 9 at (round 4, top 66).
- Elsewhere k = 1, so depth 0. This covers the corpus, cross unions s11 (both orders), mixed unions s1 (stable), and big
  unions with n ≤ 120 (both orders). No re-steal ever lacked a cause.
- Open: whether D is bounded. Bound (i) is exponential; nested R35 gadgets may give depth growing with n.
