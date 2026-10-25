# Referee packet P-N5-LV: in-scope THR fallbacks of level −1: gate shape, the CN-LAST exit, and a per-scope-run count (box 11)
L-SI successor 6 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~14:00Z (date -u). Lane default after the 13:42Z report (no
redirect received). Frozen at its commit: corrections go in a fixes file, never here.
- Source texts: docs/si/N5-LV-box11.md (sha1 407c5520) and docs/si/N5-LV2-box11.md (sha1 94ac2469). Where they differ, this packet
  governs. In particular, LV-PL here has NO "+1" (no straddling interval at level −1, §4) and is PROVED, not a reading.
- Status: L-SI successor 6's proofs, unrefereed. Labels: PROVED (L-SI succ. 6); PROVED CONDITIONAL on CN-LAST; CONJECTURE; OPEN; DATA.
- Everything is on 𝒞^1O: exactly one Odd vertex o with out-degree > 1. The script asserts it.
- Not a running-time bound, not a TARGET.md claim, not a step-4 pass. G-N5-TIME stays OPEN.
- Statements to sign:

| § | statement | label |
| --- | --- | --- |
| §1 | Proposition LV-SHAPE | PROVED (no (P)) |
| §2 | Corollary LV-CN, Corollary LV-COUNT | PROVED CONDITIONAL on CN-LAST |
| §3 | Lemma FLAT-ALL_{−1}, Lemma STRETCH_{−1} | PROVED |
| §4 | Theorem PL_{−1} (a)-(c) and Corollary LV-PL | PROVED |

- §5 is NOT TO SIGN. §6: data.

## 0. Objects and dependencies
- Objects: as in P-N5-FBW §0 (R31) and P-N5-RL §0: N5, S4a / S4c, Ξ, W, gates, gate levels, M_k, lev, COARSE_L for −1 ≤ L < ∞ (R25 §1),
  (C1)-(C7), b_k(y), θ, w, R̄ / R / F, (h), r, THR, u*, phase, scope run S, c, e*, x0 := σ̄_k(o).
  - λ(y) is the Ξ-cycle node of y.
  - Under (h), for y ∈ F the honest play and the (σ, τ)-play coincide (Odd is forced off o).
- LANDED, used:
  - R15 (a), (d);
  - R19 (a) Lemma G; R21 (a) XW;
  - R25 (e) OFF (at level M_k) and CAP-1; R25 (d) FB step (2);
  - R28 (a) U-loc (any level L);
  - R29 (a) Fact R, (b) TRANSFER, (c) OFFGATE, (d) CN, (e) NL (L < ∞, r_j > L);
  - R30 (a)-(b) Lemma OR, TC-SPLIT;
  - R31 FBW (b), FBW-S, P-OPT, CLS2, FLAT-ALL's proof, STRETCH's step (1), PL's proof;
  - R35 PL (c′)'s proof (N_x count);
  - R20 (b) FBL (u* ≠ none).
- SIGNED, in landing: P-N5-RL (R37): Lemma R-SAME (no (P)), and BL's proof Step 2a. Step 2a uses no (P): it is R31 FBW Step 2 with
  V := W_k, plus P-OPT.
- In landing: CN-LAST (docs/new/P-N5-SCOPE-box36.md §6, packet sha1 c3f5ed37; R38 per the Lead 13:48Z). Used only in §2.
- SETTING (LV): k is an in-scope S4c fallback (k → k+1 in S), THR at k (θ_k ◁ w_k under (h)), and M_k = −1. A fallback has a gate,
  and every gate level is ≥ −1, so every gate has level −1.

## 1. Proposition LV-SHAPE (PROVED, L-SI succ. 6)
In setting (LV), let (y, z) be a gate and s := σ_k(y). Exactly one of the following holds:
- (α) s, z ∈ F_k, and y is its own Ξ- and W-cycle node;
- (γ) s ∈ F_k, z ∈ R̄_k, r_k = −1, y = c, and P(W_k z) = ∅;
- (β) y ∈ R_k, z ∈ F_k, rank o < rank c, π^k_s ∩ V_{>c} = ∅ and P(Ξ_k z) = P(θ_k). If r_k ≥ 0, also W_k(s) ▷ W_k(z) at level r_k.
The case s, z ∈ R̄_k does not occur.
Proof. Put δ := max(lev(Ξ s, W s), lev(Ξ z, W z)).
- (F, F). Ξ = W at s and z (Lemma G), so δ = ⊥ < −1 = ℓ. FBW (b) makes y its own W- and Ξ-cycle node. This is (α).
- (R̄, R̄). By R-SAME, π_z ⊕ w ▷ π_s ⊕ w iff π_z ⊕ θ ▷ π_s ⊕ θ, and the symmetric difference of the path sets is the same. So (y, z) is
  a W-improving gate.
  - By BL Step 2a it is exceptional: y is its own W-cycle node.
  - y is Even (so y ≠ o), and y ∈ R̄_k (its successor s is). So y's (σ_k, τ)-play reaches o and returns to y, and o lies on a W-cycle,
    against H2. This case does not occur.
- (F, R̄). Ξ(z) = π_z ⊕ θ ▷ Ξ(s) = W(s) at level −1, and W(z) = π_z ⊕ w ⊵ π_z ⊕ θ (XW, (C7)). So W(z) ▷ W(s), and (y, z) is a
  W-improving gate. By Step 2a it is exceptional: y is its own W-cycle node, W(z) = (y, ∅, ·), and lev(W s, W z) = −1.
  - If r ≥ 0: lev(Ξ s, π_z ⊕ θ) = −1 and lev(π_z ⊕ θ, π_z ⊕ w) = r ((C7)). (C6), applied twice, gives lev(W s, W z) = r ≥ 0, against
    −1. So r = −1.
  - W(z) has cycle node c (z ∈ R̄ under (h)), so y = c.
  - y ∈ F_k, so its honest play is its W-play, and y is its own Ξ-cycle node. This is (γ).
- (R̄, F). y ∈ R_k. Level −1 gives P(Ξ z) = P(Ξ s) = P(π_s ⊕ θ) = (π_s ∩ V_{>c}) ⊔ P(θ) (Lemma G).
  - P(Ξ z) ⊆ F_k, since z's play avoids o. So π_s ∩ V_{>c} ⊆ F_k ∩ R_k = ∅, and o ∉ P(θ).
  - o is the first vertex of θ's play and is not its cycle node (H1). So o ∉ P(θ) means rank o < rank c.
  - If r ≥ 0: lev(π_s ⊕ θ, π_s ⊕ w) = r with w ▷ θ, and Ξ(z) = W(z) ≈_{−1} π_s ⊕ θ. So W(s) = π_s ⊕ w ▷ W(z) at level r ((C6), (C7)).
    This is (β). □

## 2. Corollaries LV-CN and LV-COUNT (PROVED CONDITIONAL on CN-LAST)
**LV-CN.** In setting (LV), if no gate at k is of kind (β), then Ξ_{k+1} = Ξ_k, Iσ_{k+1} = ∅, and k + 1 is the last state of its phase.
- Proof. Every gate is (α) or (γ), so every gate has λ_k(y) = y and level −1. S4c is Even's (Iσ_k ≠ ∅). These are CN-LAST's hypotheses;
  apply CN-LAST (i)-(iii). □
**LV-COUNT.** In each phase, the in-scope THR fallbacks with M = −1 number at most 1 + (those with a (β) gate). If rank o > rank c, none
has a (β) gate, so there is at most one, and it is the phase's last transition.

## 3. Lemma FLAT-ALL_{−1} and Lemma STRETCH_{−1} (PROVED)
**FLAT-ALL_{−1}.** Let k be a fallback of a scope run with M_k = −1, r_k ≥ 0, and (h) at k and k + 1. Then R31 FLAT-ALL (i)-(iv) hold with
M := −1: (i) F_k ⊆ F_{k+1}, and R̄_{k+1} keeps its routes; (ii) COARSE_{−1}(θ_{k+1}) = COARSE_{−1}(θ_k); (iii) COARSE_{−1}(Ξ_{k+1} v) =
COARSE_{−1}(Ξ_k v) for all v; (iv) M_{k+1} ≤ −1.
- Proof. R31's proof (P-N5-FBW §3) uses M ≥ 0 ONLY in its first line: "By FBW-S, r_k ≥ M ≥ 0, so k is THR with u* ≠ none". Here r_k ≥ 0
  is assumed, so k is THR with u* ≠ none, and FBL applies.
  - (i) uses only FBL and H2.
  - (ii) uses H1, Lemma S (a), R15 (a), OFF at level M_k = −1 (R25 (e), stated for COARSE_{M_k}), (C7), (C1) and (C3).
  - (iii) uses OFF, Lemma G, (C7) and (ii).
  - (iv) uses TRANSFER, which holds for every L < ∞.
  None of these steps uses M ≥ 0. □
**STRETCH_{−1}.** Let [s, e] be consecutive states of a scope run S with COARSE_{−1}(Ξ_t v) the same for all t ∈ [s, e] and every v. Then
each Even y is a level −1 tail at most n times among the fallbacks k of S with s ≤ k < e and M_k = −1.
- Proof.
  - Step (1) of R31 STRETCH holds with M = −1: COARSE_{−1}(b_t y) is constant on [s, e].
    - A switch of y along a gate of level > −1 would change COARSE_{−1}(Ξ y) if y is not a cycle node ((P2), (C7)). That is excluded.
    - At a cycle node every switch has level −1 (CN).
    - A switch along a gate of level ≤ −1 lands on a target with the same COARSE_{−1} value.
  - With (c_y, P_y) := COARSE_{−1}(b(y)) fixed, ⊴ among values with that coarse part is the length order: shorter is better if c_y is
    even, longer if c_y is odd. b(y) is ⊴-non-decreasing (R15 (a), (d)).
  - Take a level −1 tail event at k, with y's best target z (FB step (2)). Then b_{k+1}(y) = Ξ_{k+1}(z) ⊵ Ξ_k(z) ▷ b_k(y), with the same
    COARSE_{−1}. So the length of b(y) moves strictly in the better direction.
  - Lengths lie in {0, …, n − 1}, so there are at most n such events. □

## 4. Theorem PL_{−1} and Corollary LV-PL (PROVED)
Setting. S is a scope run. The LEVEL −1 BLOCK of S is the set of its fallbacks f_1 < … < f_N with M = −1 and r ≥ 0.
- They are consecutive among S's fallbacks: levels are non-increasing (CLS2), r is non-increasing (Fact R), and −1 is the least level a
  fallback can have.
- Every state of [f_1, f_N] has r ≥ 0, by Fact R and r_{f_N} ≥ 0. So, unlike levels ≥ 0, there is no straddling interval.
- DIRTY and D_{−1} are as in R31 PL, at level −1. REL_{−1} := the number of exits leaving R at f_1, …, f_{N−1}.
**Theorem PL_{−1}.**
- (a) N ≤ n·n_E·(1 + D_{−1}).
- (b) The first transition j of a dirty interval at which COARSE_{−1}(Ξ) changes is an S4a step with O_j > −1 ≥ E_j, lev(θ_j, θ_{j+1}) = O_j,
  and an absorption (σ̄_j(o) ∈ F_j ∩ R_{j+1}).
- (c) D_{−1} ≤ (d_o − 1) + REL_{−1}. Hence N ≤ n·n_E·(d_o + REL_{−1}).
Proof.
- (a) R31 PL (a)'s proof.
  - For i < N, S continues after f_i, so (h) holds at f_i + 1, and FLAT-ALL_{−1} (iii) applies at f_i (r_{f_i} ≥ 0). So no fallback of the
    block changes COARSE_{−1}(Ξ).
  - [f_1, f_N] splits into at most 1 + D_{−1} runs of constant COARSE_{−1}(Ξ). Every fallback of the block has a level −1 tail (FB step
    (2)). STRETCH_{−1} on each run gives at most n·n_E per run.
- (b) R31 PL (b)'s proof with M = −1.
  - M_{f_i+1} ≤ −1 by FLAT-ALL_{−1} (iv). While COARSE_{−1}(Ξ) is unchanged, M_t ≤ −1 persists by TRANSFER. So M_j ≤ −1.
  - Every relevant Even change at j has level ≤ −1 (R15 (d)), so E_j ≤ −1. The interval has no fallback, so j is an S4a step.
  - U-loc (R28 (a), stated for any level L) with L = −1 freezes COARSE_{−1} at every vertex whose path before its cycle node carries no
    relevant change above −1. So a change needs the relevant σ̄(o) change, with O_j > −1 ≥ E_j.
  - Lemma OR (c) / TC-SPLIT give lev(θ_j, θ_{j+1}) = O_j. Lemma OR (a)-(b), with H1 at j, give the absorption.
- (c) R35 PL (c′)'s proof (equivalently R31 PL (c)) with M = −1.
  - On each interval, (A_t) holds for L = −1: OFFGATE at f_i + 1 (gates into F have level ≤ M_{f_i} = −1), then NL (iii) at each S4a
    step. NL applies with L = −1, since r_t ≥ 0 > −1.
  - NL (ii): no exit leaves R at an S4a step. Each dirty interval contains its own first absorption (b), which raises N_x := #exits in R by
    1. N_x falls only at the block's fallbacks, by REL_{−1} in total. Under H1, 0 ≤ N_x ≤ d_o − 1.
  - Hence D_{−1} ≤ (d_o − 1) + REL_{−1}. With (a), N ≤ n·n_E·(d_o + REL_{−1}). □
**Corollary LV-PL.** Every scope run S has at most n·n_E·(d_o + REL(S)) THR fallbacks with M = −1 and r ≥ 0. With LV-COUNT (CONDITIONAL on
CN-LAST), all but at most one per phase are (β)-fallbacks.

## 5. NOT TO SIGN
- CONJECTURE "in scope, THR ⇒ M ≥ 0". DATA: 1,032 / 1,032 in-scope THR fallbacks have M ≥ 0. A counterexample relevant to counting is
  a (β)-fallback (§1). LV-PL bounds them anyway, up to REL(S).
- OPEN:
  - THR fallbacks with u* = none (r = −1). There NL at L = −1 is unavailable, and Fact R keeps r ≤ −1 for the rest of S. DATA: 0 in
    scope.
  - REL(S) at level −1. P-N5-ENT's ENT-X, which removes REL at levels ≥ 0, uses the rank-L bit (ENT-SHAPE (4)). A length-based analogue
    is OPEN.

## 6. DATA (DATA, not proof; experiments/si/tev/lvm1.py, log experiments/si/tev/logs/lvm1_all.txt)
- In-scope fallbacks over NAMED (coarse/named.txt + coarse/instances + box9 + riselast/instances) + experiments/red/so/instances + LIB
  (234):
  - THR with r ≥ 0: 1,032, all with M ≥ 0;
  - THR with r = −1: 0;
  - EQ: 15, all with M = −1.
- So the level −1 block is empty in all data, and §1-§4 have vacuous hypotheses there. They rest on the proofs.
