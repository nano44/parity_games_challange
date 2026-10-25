# N5 box 8: toward (CL-S): fallback levels across a scope run
L-SI successor 3 (Opus 5.5, D18/L40). Lead GO 2026-10-25 00:18Z. Started 00:20Z (date -u).
Labels (L40): PROVED (L-SI succ. 3, unrefereed unless stated), CONJECTURE, OPEN, DATA, READING, FALSE.
- Scope: 𝒞^1O (exactly one Odd choice vertex o; asserted by every script), inside one PHASE (joint λ-phase, τ constant).
- These are lemmas about the candidate N5, not a running-time bound. G-N5-TIME stays OPEN.
- Notation as in RESULTS R25 / packet P-N5-FB (docs/si/P-N5-FB-box7.md §0-§1): levels lev, COARSE_L, gate levels, M_k, TAME, R̄,
  and (T), OFF, CAP.
- SCOPE RUN (box 7 §9, §13): a maximal run of in-phase transitions k → k+1 with (h) at k, H2 at k+1 and w_{k+1} = w_k.
- Dependencies are cited by RESULTS item. R25 = P-N5-FB as landed, scoped by CHECKER C34: the W-lowering bound holds on every game,
  (C) on 𝒞^1O.

## 1. Lemma OFFGATE (PROVED): gates into F never exceed the previous max gate level
Inside a phase on 𝒞^1O, at every transition k → k+1 (tame or not): every gate edge (y, z) at k+1 with z ∉ R̄_{k+1} has level ≤ M_k.
Proof.
- If M_k = ∞ there is nothing to show. If M_k = ⊥, then σ, Ξ and the gates are unchanged.
- Otherwise write M := M_k, and let u := σ_{k+1}(y).
- (i) COARSE_M(Ξ_k u) = COARSE_M(Ξ_k σ_k y). u is σ_k(y), or a gate target at k of level ≤ M (R15 (d), (C2)).
- (ii) COARSE_M(Ξ_{k+1} u) ⊵_M COARSE_M(Ξ_k u), by R15 (a) and (C1).
- (iii) COARSE_M(Ξ_{k+1} z) = COARSE_M(Ξ_k z), by OFF (R25), since z ∉ R̄_{k+1}.
- Suppose the level of (y, z) at k+1 is > M. Then COARSE_M(Ξ_{k+1} z) ▷_M COARSE_M(Ξ_{k+1} u): the gate is strict, so (C1) gives ⊵,
  and (C2) gives ≠.
- With (i)-(iii): COARSE_M(Ξ_k z) ▷_M COARSE_M(Ξ_k σ_k y). So z ≠ σ_k(y), and (y, z) ∈ Iσ_k has level > M = M_k. Contradiction. □
Remarks.
- OFFGATE is MONO (R25) for targets off R̄, without tameness. At a non-tame jump, only gates INTO R̄_{k+1} can rise above M_k.
- The stronger form with MF_k := max level of the gates at k whose target is off R̄_k is FALSE (DATA; OG′).
  - Instance: x31_re24 (L-RED, sha1 49eaf50e), transition 1 → 2: MF_1 = −1, while gate (4, 8) at state 2 has level 22.
  - At state 1 vertices 4 and 8 are in R, and the level-22 gate is (8, 14), from R into R. At 1 → 2, R collapses from 21 vertices to
    {12} at an arena step, and the high level moves into F.
DATA (experiments/si/coarse/cls2.py, the named set + all pinned climb bests + L-RED j7_*): OFFGATE 7,134 gate checks, 0 violations.

## 2. Lemma CN (PROVED): switches at cycle nodes are length-only inside a phase
If λ_{k+1} = λ_k and y with λ_k(y) = y switches to z at k → k+1, then the gate level of (y, z) at k is −1.
Proof.
- λ_{k+1}(y) = y, so y's H_{k+1}-play is a cycle with top y through z = σ_{k+1}(y). The path from z to y is an arc of that cycle, so
  all its vertices have rank < rank y. By Lemma 5.2 (VJ00 p. 15; ENG-1), P(Ξ_{k+1} z) = ∅.
- λ_k(z) = λ_{k+1}(z) = y. R15 (a) gives Ξ_k(z) ⊴ Ξ_{k+1}(z), with the same cycle node, so the signed weight of P(Ξ_k z) is ≤ 0.
- σ_k(y) lies on y's H_k-cycle, whose top is y, so P(Ξ_k σ_k y) = ∅. The gate Ξ_k(z) ▷ Ξ_k(σ_k y) gives weight(P(Ξ_k z)) ≥ 0.
- So the weight is 0, and P(Ξ_k z) = ∅ (the weight is injective on sets). The cycle nodes and path sets agree and the gate is strict,
  so the level is −1. □
DATA (cls2.py): 7 in-phase cycle-node switches, all of level −1.

## 3. Switched edges at in-scope fallbacks (PROVED parts; the rest OPEN)
Let k → k+1 be an S4c fallback inside a phase, with (h) at k. By R25 FB step (2), M_k is attained by switched edges (every tail
switches to its best target, whose level is the max over its gate edges). Classify the switched edges y → z* by memberships at k.
- (a) y a cycle node: level −1 (CN).
- (b) y ∈ F_k, z* ∈ R̄_k: y is a W-cycle node on o's W-play (R23 (d) with R21 (c) FBL-N (ii)). y ∈ F, so its H_k-play is its
  W-play (it avoids o, and Odd is forced off o). So λ_k(y) = y, and by (a) the level is −1.
- (c) y ∈ R_k, z* ∈ R̄_k:
  - none at a THR state with u* ≠ none (R20 (b), FBL strong form; R20 puts o in R, so "no R → R gate edge" covers R̄);
  - at THR states with u* = none (FBL unproved there, G-XA-1 (b)) and at EQ states: OPEN. A cycle-closing R → R edge whose cycle
    is broken by a simultaneous switch is not excluded.
- (d) y ∈ R_k, z* ∈ F_k (evictions): level ≤ rank(u*_k) (CLU, box 5, PROVED by L-SI succ. 2 on GAP = R23 (f)). At u* = none
  the level is −1.
- (e) y ∈ F_k, z* ∈ F_k, y not a cycle node: OPEN in general.
  - By R23 (a) Step (K), z*'s W-play must pass through y (cycle-closing). Otherwise the single switch raises W at y.
  - Inside a phase the cycle y → z* → … → y must then be broken at k+1 by a simultaneous switch, or have top λ_k(y). The latter
    forces level −1 by the argument of (a).
DATA (cls2.py): at in-phase fallbacks with (h), gates with a target in R̄_k: 1 case, at an EQ state, level ≤ −1. 0 non-flat.

## 4. What (CL-S) needs, and the obstruction (READING)
- Releases into D happen only at fallbacks with a leave (box 7 §9 NOREL-A). Under H1 these have an active R → F leaver (R23 (b),
  (c)), so they are exactly the evicting fallbacks. For Corollary JD it is enough to bound EVICTING fallbacks per scope run. Call
  that form (CL-E):
  - the max level E_k of the switched R → F edges is non-increasing along the evicting fallbacks of a scope run;
  - each level occurs at ≤ n_E of them.
- OFFGATE controls gates INTO F across every transition, but only by M_k. That includes gates INTO R̄, which rise at jumps, and also
  at arena steps (entries).
  - The x31_re24 mechanism (§1) shows a high gate into R becoming a high gate into F when R collapses at an arena leave.
  - So a proof of (CL-E) must show that such a high F-target gate cannot survive, as an R → F gate, until the next evicting fallback
    of the same scope run.
  - At that fallback, arena optimality (Step (K)) and GAP put every R → F gate in the window π′ ⊕ θ ◁ Ξ(z) ⊴ π′ ⊕ w.
- Adversarial climbs against (CL-S) in this form: §5.

## 5. The invariant behind (CL-S), and a reduction to one leave condition
Fix a scope run S and an in-scope S4c fallback k0 in it. For a later state j of S, let L_j := the least M over the fallbacks of S up to
j. (Under (CL-S) this is the most recent fallback level.) Write L for L_j.
Statements:
- **(A) [gates into F]:** every gate (y, z) at j with z ∈ F_j has level ≤ L. (This is RF-INV ∪ FF-INV.)
- **(B1) [no high gate into a leaver]:** at a transition j → j+1 of S after k0, no gate at j of level > L has its target in
  R_j ∖ R̄_{j+1} (a vertex leaving R).
- **(FRZ) [F frozen]:** z ∈ F_j ∩ F_{j+1} keeps COARSE_L(Ξ). **(LV) [leavers]:** z ∈ R_j ∖ R̄_{j+1} keeps COARSE_L(Ξ).

**Lemma TRANSFER (PROVED).** Let j → j+1 be in-phase, let L < ∞, and let z satisfy COARSE_L(Ξ_{j+1} z) = COARSE_L(Ξ_j z). If (y, z) is
a gate at j+1 of level > L, then (y, z) is a gate at j of level > L.
- Proof: let u := σ_{j+1}(y). Ξ_j(u) ⊵ Ξ_j(σ_j y) (R15 (d)) and Ξ_{j+1}(u) ⊵ Ξ_j(u) (R15 (a)). So by (C1)
  COARSE_L(Ξ_j z) = COARSE_L(Ξ_{j+1} z) ▷_L COARSE_L(Ξ_{j+1} u) ⊵_L COARSE_L(Ξ_j σ_j y). □

**Lemma FRZ/LV from (A) and (B1) (PROVED).** If (A) holds at j and (B1) at j → j+1, then (FRZ) and (LV) hold at j → j+1.
- Proof: let z ∉ R̄_{j+1}. Its H_{j+1}-play avoids o (𝒞^1O), and the play's cycle has a top t with λ_j(t) = λ_{j+1}(t) = t (phase).
- Run (T) (R25) at level L along that play. Take a switched vertex p on it, with q := σ_{j+1}(p) ∉ R̄_{j+1}; (p, q) is a gate at j.
  - If q ∈ F_j, its level is ≤ L by (A).
  - If q ∈ R̄_j, then q ∈ R_j ∖ R̄_{j+1} (q ≠ o, since q ∉ R̄_{j+1}), and its level is ≤ L by (B1).
- So (E) holds at level L, and (T) gives COARSE_L(Ξ_{j+1} z) = COARSE_L(Ξ_j z). □

**Lemma (A)-step (PROVED).** If (A) holds at j and (B1) at j → j+1 (both in S), then (A) holds at j+1.
- Take a gate (y, z) at j+1 with z ∈ F_{j+1} and level > L.
- z ∉ R̄_{j+1}, so COARSE_L(Ξ(z)) is unchanged (FRZ or LV). TRANSFER then makes (y, z) a gate at j of level > L.
- If z ∈ F_j, this contradicts (A). If z ∈ R_j, then z leaves R, against (B1).
- Base, at j = k0 + 1: OFFGATE (§1), since L = M_{k0}. If a later fallback lowers L, (A) at that fallback's successor is again
  OFFGATE with its own M. □

**Theorem CL-S-RED (PROVED: the first half of (CL-S) under explicit hypotheses).** Let S be a scope run. Assume:
- (H-B1) (B1) holds at every transition of S after its first fallback;
- (H-KIND) every in-scope fallback of S is THR with u* ≠ none, or EQ;
- (H-EQ) at an EQ fallback of S, every switched edge from R into R̄ has level ≤ L (in fact −1 suffices).
Then the fallback levels M along S are non-increasing.
- Proof: let k1 be a fallback after k0. M_{k1} is attained by switched edges (R25 FB step (2)).
  - Switched edges into F_{k1} have level ≤ L, by (A), which holds at k1 by induction (Lemma (A)-step and (H-B1)).
  - Switched edges into R̄_{k1}:
    - level −1 when the tail is a cycle node (§3 (a)) or in F (§3 (b));
    - from R: none at THR with u* ≠ none (§3 (c)); at EQ, level ≤ L by (H-EQ).
  - So M_{k1} ≤ L. Then L_{k1} = M_{k1}, and the induction continues from k1 with the smaller L. □
- DATA for the hypotheses: (H-KIND) 264 / 264 in-scope fallbacks; (H-EQ) 1 such edge in total, of level ≤ −1; (H-B1) 588 / 0.

**Where (B1) is PROVED.**
- At a THR fallback with u* ≠ none, R20 (b) FBL allows no gate into R at all, so (B1) is vacuous.
- At an EQ fallback with H1 ∧ H2 there is no leave (R23 (e) Corollary), so (B1) is vacuous.
- OPEN: (B1) at arena-step (S4a) leaves, and at THR fallbacks with u* = none.

**What is not covered.** The second half of (CL-S) (≤ n_E fallbacks per level across jumps) is OPEN.
- FB's β count resets at every jump.
- A partial argument (READING): after a θ-jump above L, an R-tail whose route did not change has no R → F gate at all. Its successor
  value rose at a level > L, and a target above the new value would, by TRANSFER, have been a gate above L at the earlier state,
  against (A).

DATA (experiments/si/coarse/rfinv.py, the named set + every pinned climb best + L-RED j7_*):
- (A) RF/FF 0 violations; FRZ 28,311 / 0; R-ROUTE 10,293 / 0; LV 588 / 0.
- (B1) 588 leaves checked, 0 violations: 584 leaves at fallbacks, 4 at arena steps.
- In-scope fallbacks by kind: 260 THR with u* ≠ none, 4 EQ, 0 THR with u* = none.
- Gates into R̄ of level > L after a fallback ("highRbar"): 15 states. None of their targets left R while the gate stood.
