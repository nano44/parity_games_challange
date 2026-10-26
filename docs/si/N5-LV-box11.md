# N5 box 11, part 4 (L-SI successor 6): in-scope THR fallbacks of level −1: their gate shape, and when CN-LAST ends the phase
L-SI successor 6 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~13:40Z (date -u), Lead GO 13:13Z ("first prove or kill
'THR ⇒ M ≥ 0' in scope, then the per-scope-run count"). Lane write-up, unrefereed.
- Labels: PROVED (L-SI succ. 6); PROVED CONDITIONAL on CN-LAST (P-N5-SCOPE §6, in review); CONJECTURE; OPEN; DATA.
- Everything is on 𝒞^1O; the script asserts it. Not a running-time bound, not a TARGET.md claim, not a step-4 pass. G-N5-TIME stays OPEN.
- Result in one paragraph.
  - "THR ⇒ M ≥ 0" is neither proved nor killed.
  - PROVED: at an in-scope THR fallback with M_k = −1, every gate is of one of three kinds:
    - (α) an F → F gate at its tail's own cycle node;
    - (γ) an F → R̄ gate at the tail c itself, and only when r = −1 (u* = none);
    - (β) an R → F gate of level −1, which needs rank o < rank c and a route below c.
  - Without a (β) gate, L-NEW's CN-LAST applies: Ξ is unchanged, and the fallback is the last transition of its phase. So:
    - level −1 THR fallbacks in scope number ≤ 1 per phase + the (β)-fallbacks;
    - when rank o > rank c (no (β) possible), they number ≤ 1 per phase.
  - DATA: no in-scope THR fallback has M = −1 (1,032 THR, all M ≥ 0; 0 with u* = none). The 15 EQ fallbacks all have M = −1 (EQ-END).

## 0. Objects and dependencies
- As in P-N5-FBW §0 (R31) and P-N5-RL §0: N5, S4c, Ξ, W, gates, levels, M_k, R̄ / R / F, (h), r = lev(θ, w), THR (θ ◁ w under (h)), c, e*,
  x0 := σ̄_k(o). λ(y): the Ξ-cycle node of y. Under (h), for y ∈ F the honest play and the (σ, τ)-play coincide (Odd is forced off o).
- Used:
  - R19 (a) Lemma G; R21 (a) XW; (C1)-(C7) (R25, R29 (a));
  - R31 Lemma FBW (b) (ℓ = −1 > δ ⇒ the tail is its own W- and Ξ-cycle node) and P-OPT;
  - P-N5-RL Lemma R-SAME (signed by both, no (P)) and BL's proof Step 2a (no (P): R31 FBW Step 2 with V := W_k, and P-OPT);
  - H2;
  - CN-LAST: docs/new/P-N5-SCOPE-box36.md §6 (L-NEW succ. 15; packet sha1 c3f5ed37), in review. REFEREE signed it in R-N5-SCOPE.
- Setting (LV): k is an in-scope S4c fallback (S a scope run, k → k+1 in S), THR at k, and M_k = −1. Every gate then has level −1, since a
  fallback has a gate and gate levels are ≥ −1.

## 1. Proposition LV-SHAPE (PROVED, L-SI succ. 6)
In setting (LV), let (y, z) be a gate with s := σ_k(y). Then exactly one of the following holds:
- (α) s, z ∈ F_k, and y is its own Ξ- and W-cycle node (λ(y) = y);
- (γ) s ∈ F_k, z ∈ R̄_k, r_k = −1, y = λ(y) is its own W- and Ξ-cycle node, and P(W_k z) = ∅;
- (β) y ∈ R_k, z ∈ F_k, rank o < rank c, π^k_s ∩ V_{>c} = ∅, P(Ξ_k z) = P(θ_k), and W_k(s) ▷ W_k(z) at level r_k (when r_k ≥ 0).
The case s, z ∈ R̄_k never occurs.
Proof. Put δ := max(lev(Ξ s, W s), lev(Ξ z, W z)), as in FBW. Four cases on (s, z).
- (F, F): Ξ = W at both (Lemma G), so δ = ⊥ < −1 = ℓ. FBW (b): y is its own W- and Ξ-cycle node. This is (α).
- (R̄, R̄): by R-SAME, π_z ⊕ w ▷ π_s ⊕ w iff π_z ⊕ θ ▷ π_s ⊕ θ, with the same symmetric difference, hence the same level. So (y, z) is a
  W-improving gate. By BL Step 2a (P-OPT + FBW Step 2) it is EXCEPTIONAL: y is its own W-cycle node.
  - y ∈ R̄_k (its successor s is in R̄_k, and y is Even, so y ≠ o). y's (σ_k, τ)-play reaches o, and y lies on that play's cycle. So
    the cycle contains o: o is on a W-cycle, against H2. This case does not occur.
- (F, R̄): Ξ(z) = π_z ⊕ θ ▷ Ξ(s) = W(s) at level −1, and W(z) = π_z ⊕ w ⊵ π_z ⊕ θ (XW, (C7)). So W(z) ▷ W(s): a W-improving gate,
  hence exceptional (Step 2a): y is its own W-cycle node, P(W z) = ∅, and lev(W s, W z) = −1.
  - If r ≥ 0: lev(Ξ s, π_z ⊕ θ) = −1 and lev(π_z ⊕ θ, π_z ⊕ w) = r ((C7)). (C6) twice gives lev(W s, W z) = lev(Ξ s, π_z ⊕ w) = r ≥ 0,
    against −1. So r = −1.
  - Exceptional also gives W(z) = (y, ∅, ·) (Step 2a / 2b). W(z) has cycle node c (z ∈ R̄, under (h)), so y = c.
  - y ∈ F_k (s ∈ F_k), so y's honest play is its W-play, and y is also its own Ξ-cycle node. This is (γ), with y = c.
- (R̄, F): y ∈ R_k. Level −1 gives P(Ξ z) = P(Ξ s) = P(π_s ⊕ θ) = (π_s ∩ V_{>c}) ⊔ P(θ) (Lemma G; the cycle node is c).
  - P(Ξ z) ⊆ F_k, since z's play avoids o. So π_s ∩ V_{>c} ⊆ F_k ∩ R_k = ∅, and o ∉ P(θ).
  - o is the first vertex of θ's play and is not its cycle node (H1), so o ∉ P(θ) means rank o < rank c.
  - If r ≥ 0: W(s) = π_s ⊕ w and Ξ(z) = W(z) ≈_{−1} π_s ⊕ θ. lev(π_s ⊕ θ, π_s ⊕ w) = r ≥ 0 with w ▷ θ, so W(s) ▷ W(z) at level r
    ((C6), (C7)). This is (β). □
- Reading: (β) gates are W-WORSENING. Even's robust valuation prefers z by length only, while its nominal valuation prefers the route
  through o at level r.

## 2. Corollary LV-CN (PROVED CONDITIONAL on CN-LAST, L-SI succ. 6)
In setting (LV), if no gate at k is of kind (β), then Ξ_{k+1} = Ξ_k, Iσ_{k+1} = ∅, and k + 1 is the last state of its phase.
- Proof. Every gate is (α) or (γ), so every gate has λ_k(y) = y and level −1. That is CN-LAST's hypothesis, and S4c is Even's
  (Iσ_k ≠ ∅). CN-LAST (i)-(iii). □
**Corollary LV-COUNT (CONDITIONAL on CN-LAST).** In each phase, the in-scope THR fallbacks with M = −1 number at most 1 + #(those with a
(β) gate). If rank o > rank c along S, a (β) gate is impossible (LV-SHAPE), so there is at most 1 per phase, and it is the phase's last
transition.
- This sharpens P-N5-SCOPE §6's READING, "level −1 fallbacks of a phase ≤ 1 + (level −1 fallbacks with a gate at a non-cycle node)",
  inside scope: the non-cycle-node gates are exactly the (β) gates, and they need rank o < rank c.
- EQ fallbacks in scope: EQ-END (P-N5-RL §4, signed CONDITIONAL on CN-LAST): at most one per scope run after θ = w, and it is the last
  transition of its phase.

## 3. What is left (OPEN), and the kill shape for "THR ⇒ M ≥ 0"
- OPEN: "THR ⇒ M ≥ 0" in scope (CONJECTURE, DATA below). By LV-SHAPE, a counterexample is an in-scope THR fallback whose gates are all
  of kinds (α) / (γ) / (β), all of level −1.
  - With no (β) gate, it ends its phase (LV-CN). That is harmless for counting.
  - So the counting-relevant kill shape is a (β)-fallback:
    - rank o < rank c;
    - an R → F level −1 gate (y, z) with σ_k(y)'s route below c and P(Ξ z) = P(θ_k), i.e. z free with the threat's path set and a better
      length;
    - and no gate of level ≥ 0 anywhere.
- OPEN: the per-scope-run count of (β)-fallbacks.
  - By CLS2, once a fallback of S has M = −1, every later fallback of S has M ≤ −1. So the (β)-fallbacks of S form a final run of
    level −1 fallbacks (with EQ / CN-LAST ones).
  - Between two of them, OFFGATE gives (A) at level −1 at k0 + 1 (gates into F of level ≤ −1). While r ≥ 0, NL with L = −1 applies:
    COARSE_{−1}(Ξ) is frozen off R̄, and there is no leave.
  - A PL-type count at level −1 needs a level −1 STRETCH. A (β) tail's b(y) rises by length only, so a tail repeats at most n times per
    constant-COARSE_{−1} stretch. It also needs a level −1 FLAT-ALL across a (β)-fallback, which R31 states only for M ≥ 0.
  - Not attempted further in this box.

## 4. DATA (DATA, not proof; experiments/si/tev/lvm1.py, log experiments/si/tev/logs/lvm1_all.txt)
- Every in-scope fallback (reltrace.runs_of) over NAMED (coarse/named.txt + coarse/instances + box9 + riselast/instances) +
  experiments/red/so/instances + LIB (234):
  - THR with u* ≠ none (r ≥ 0): 1,032, all with M ≥ 0;
  - THR with u* = none (r = −1): 0;
  - EQ: 15, all with M = −1.
- So the setting (LV) never occurs in data. LV-SHAPE and LV-CN rest on their proofs, as P-N5-FBW §6's "DATA FINDING" already noted for
  u* = none.
