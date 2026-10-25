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

## 6. Lemma AL (PROVED under (A) and FRZ at the transition): arena-step leaves after a fallback need rank u* ≤ L
In a scope run, after a fallback (L as in §5), let j → j+1 be an S4a step at a THR state with u* ≠ none. Suppose (A) holds at j and
FRZ holds at j → j+1 (both follow from (H-B1), §5). If rank(u*_j) > L, then j → j+1 has no leave.
Proof.
- Under H1, every leave has an active leaver s ∈ R_j with t := σ_{j+1}(s) ∈ F_j (R23 (b), (c)). (s, t) is a gate at j (R15 (d)),
  so its level is ≤ L by (A).
- s ∉ R̄_{j+1}, so W_{j+1}(s) = s ⊕ W_{j+1}(t) (s is not a W-cycle node in a phase) and W_{j+1}(t) = Ξ_{j+1}(t) (R19 (a)).
- WM (R23 (g)): W_{j+1}(s) ⊵ W_j(s) = π_s ⊕ w = s ⊕ π′ ⊕ w, with π′ the route of σ_j(s). By (F-pre), Ξ_{j+1}(t) ⊵ π′ ⊕ w.
- FRZ: COARSE_L(Ξ_j t) = COARSE_L(Ξ_{j+1} t) ⊵_L COARSE_L(π′ ⊕ w).
- rank(u*) > L, so COARSE_L(π′ ⊕ θ) ◁_L COARSE_L(π′ ⊕ w): they differ at u* ∉ π′.
- Hence COARSE_L(Ξ_j t) ▷_L COARSE_L(Ξ_j σ_j s), so the gate (s, t) has level > L. Contradiction. □
DATA (rfinv.py): 4 arena leaves after a fallback in scope; all have rank(u*_j) ≤ L.

## 7. Item (2): the arena reversals of (Z) (DATA; scratch classification on the named set + pinned bests + j7_*)
Arena-step '−' and '±' reversals (Z's part beyond (C)), by regime:

| sign | scope | fallback earlier at the same w? | state | count |
| --- | --- | --- | --- | --- |
| ± | in scope | no | THR | 18 |
| ± | in scope | no | EQ | 10 |
| − | in scope | no | THR | 7 |
| − | in scope | no | EQ | 4 |
| − | w changes | no | EQ | 2 |
| ± | in scope | yes | THR | 2 |
| − | in scope | yes | THR | 2 |

- READING:
  - The arena reversals live almost entirely BEFORE the first fallback at the current w: 39 of 45. After a fallback, AL leaves room
    only once u* has dropped to the fallback level.
  - So the rest of (Z) is a fallback-free question: R-reversals driven by arena steps alone, i.e. o-free progress against trust. That
    is the regime of R21's F-intervals and R22's F1°.
  - No lemma for it this box. OPEN.

## 8. Independent check of L-NEW's P-N5-SO (Lead request 01:00Z), and what (CL-S) still adds
- Ran experiments/new/box32/socheck.py UNMODIFIED (trunk 1ef02bb2, merged into l-si) on:
  - all 12 pinned lane climb bests (experiments/si/coarse/instances/: jcl_*, rel_*, rel2_*, rel_j7_*, cls_rel_lev): 16 phases;
  - the 53-file named set plus the 6 box 8 climb outputs: 73 phases.
- Result (DATA): no failure key printed. That is: no J > S_o, no SO bound failure, no TH bound failure, and no TH_H1 / shape /
  SO-tiebreak failure.
  - Largest: J 18 ≤ S_o 19 ≤ d_o(Θ + 1) with Θ 19, X 20 (rel2_x31_rx48, n 48, d_o 28).
  - On the named set: max S_o 49, Θ 51 (lev_l_x, n 32, X 21).
- What (CL-S) adds (READING). SO with TH gives J ≤ poly(n)(1 + X), and through R25 FB the same bound on fallbacks and (C).
  - But X is what (C) is meant to bound: R23 LV′ gives X ≤ (n − 1)(Z + 1) + Z, and (C) is a part of Z. So for proving (X) the SO
    route to (C) is circular.
  - (CL-S) (box 7 §13; box 8 §5) bounds J, and so (C), by poly(n)(1 + N_out), with N_out ≤ O + #w-changes + …, and no X. It is the
    non-circular route for (C) inside (Z).
  - Recommendation: keep (CL-S) with its open (H-B1) at arena leaves. Its use is (Z), not (J-poly) as such.
- The rest of (Z), arena '−' and '±' reversals (§7), is the remaining core.

## 9. Adversarial climbs against (CL-S) and its invariants (DATA; experiments/si/coarse/jclimb.py, 40 min each, 00:3xZ-01:09Z)
- CLS2 mode. Fitness = ((CL-S) violations, the largest rise of the fallback level between two fallbacks of one scope run, fallbacks
  + MF rises). Seeds fbref_cex_n32 and zcl_fb2_n32: 36,230 and 35,360 steps. Final (0, 0, 23) and (0, 0, 25): equal levels
  repeated, never a rise.
- RF mode. Fitness = (violations of (CL-S), (A), FRZ, LV; high gates into R̄ after a fallback, plus 5 × arena leaves after a
  fallback; fallbacks). Seeds x32_waves48 and x31_lem_t32: 31,047 and 43,863 steps. Final (0, 20, 35) and (0, 20, 21): high gates
  into R̄ saturate the cap, and no arena leave after a fallback ever appeared.
- Earlier, a CLS climb in box 7 (cls_rel_lev): 0.
- READING: the open case of (H-B1), an arena leave whose target carries a gate above L, did not arise under direct pressure. Weak
  evidence: the climbs never reached the precondition "arena leave after a fallback" at all.

## 10. Lemma EQ-STRETCH (PROVED, from R17): the EQ part of (Z) is polynomial
EQ state: Ξ_k = W_k pointwise (R21 state types). An EQ RUN is a maximal run x..y of consecutive EQ states inside a phase on 𝒞^1O.
**Lemma EQ-STRETCH.** An EQ run has y − x < n + m transitions.
Proof.
- At an EQ state the gates Iσ_k (Ξ-improving edges) are exactly the VJ00 improving edges of σ_k in the one-player game G_τ (Odd fixed
  to τ, which is constant in the phase): the valuation of σ in G_τ is W.
- N5's Even step S4a is the arena optimum against τ, over {σ_k(v)} ∪ Iσ_k(v). This is the switch-best step of R17 on G_τ.
- An in-phase S4c is Even's (fixes2 G-FB-2) and switches by (Ξ-key, index) = (W-key, index). That is N5's fallback on G_τ (R17 (e)).
- So x..y is a segment of N5's run on the one-player game G_τ from σ_x. R17 (e) covers any start, since its bound is per λ-phase
  (R17 (c)).
- λ of that run is λ_W = λ_Ξ (EQ), which is constant in the phase. So the segment lies in one λ-phase of the one-player run, and
  R17 (c) gives fewer than n + m steps. □
**Lemma EQ-PERSIST (PROVED).** If k is EQ, (h) holds at k+1 and w_{k+1} = w_k, then k+1 is EQ.
- Proof: θ_{k+1} ⊴ w_{k+1} = w_k = θ_k ⊴ θ_{k+1} (R21 (a) XW; R15 (a)), so θ_{k+1} = w_{k+1}.
- R19 (a) Lemma G gives Ξ = π ⊕ θ = π ⊕ w = W on R_{k+1} under (h), and Ξ = W off R. □
**Corollary (PROVED).** Inside a phase, the crossing transitions with both endpoints EQ (in particular their reversals) number fewer
than (n + m)(1 + #w-changes + #transitions whose target lacks (h)).
- An EQ run ends only at a w-change, at a target lacking (h), or at the phase end (EQ-PERSIST).
- So with R23 LV′, the EQ part of (Z) is polynomial in n·(1 + w-changes + non-(h) transitions), with no X.
DATA (experiments/si/coarse/eqrun.py, the named set + every pinned climb best + L-RED j7_*; each EQ run recomputed with N5 on G_τ):
- 278 phases, 108 EQ runs, 287 in-run transitions, all 287 equal to N5's step on G_τ;
- longest EQ run 56 transitions (< n + m); 0 run-count violations.

## 11. Where (Z) stands after box 8
Each reversal of R is at one of four places.
- (i) A fallback. Bounded by Theorem FB (R25) by poly(1 + J). J is bounded non-circularly through (CL-S) (§5, OPEN at (H-B1) arena
  leaves), or through P-N5-SO by poly(1 + X), which is circular for (X).
- (ii) A transition inside an EQ run. PROVED poly(n)·(1 + w-changes + non-(h)) (§10).
- (iii) An out-of-scope transition: OTHER-touching or a w-change. These are R21's O and the w-changes, OPEN as (NH′).
- (iv) An arena transition at a THR state with (h), no fallback before it at that w: 25 of the 45 arena reversals (§7). OPEN.
  - This is R20's throttled regime. R20 bounds value changes per throttled stretch (O(n³)), but the stretch count is the θ-change
    count, and TH bounds it only via X.
- So the open core of (X) on 𝒞^1O: THR arena reversals (iv) per scope run, (H-B1) at arena leaves for (i), and O / w-changes (iii).
- DATA (scratch classification, same set): the 29 THR in-scope arena reversals all lie at a θ-change (12) or within n − 1 transitions
  after one (17). None is later.
  - READING: (iv) behaves like R20 CR ("coarse values change only in the first n − 1 transitions of a throttled stretch"). So
    (iv) ≲ n·(1 + Θ_scope), with Θ_scope = θ-changes in scope runs (up to 51 per phase on lev_l_x-type instances).
  - So (iv) is the θ-change count again. This is the circularity "θ-changes ↔ crossings" of box 3 and of L-NEW's TH. A
    non-circular bound on Θ per scope run is the single open quantity behind (iv).

## 12. Box 8b (Lead "go" 02:00Z): (H-B1) removed. The first half of (CL-S) at THR fallbacks, PROVED
Setting: a scope run S on 𝒞^1O (§0). Write r_j := rank(u*_j) when θ_j ◁ w_j with u* ≠ none; r_j := −1 when θ_j ◁ w_j with
u* = none; r_j := −2 at EQ (θ_j = w_j).
**Fact R (PROVED).** r is non-increasing along S. w is constant on S and θ is non-decreasing (R15 (a)), with θ ⊴ w (R21 (a)). For
θ ◁ θ′ ⊴ w, Lemma U (ii) (L-SI succ. 1) gives lev(θ′, w) ≤ lev(θ, w).

**Lemma NL (PROVED; no hypothesis beyond (A)).** Let j → j+1 be an S4a (non-fallback) transition of S, let L < ∞ satisfy r_j > L,
and assume (A) at j (every gate into F_j has level ≤ L). Then:
- (i) COARSE_L(Ξ_{j+1} v) = COARSE_L(Ξ_j v) for every v ∉ R̄_{j+1};
- (ii) the transition has no leave (R_j ⊆ R̄_{j+1});
- (iii) (A) holds at j+1.
Proof.
- (i) Suppose some v ∉ R̄_{j+1} violates (i). Choose one whose H_{j+1}-play p_0 = v, p_1, … reaches its cycle node c_v in the fewest
  steps.
  - The play avoids o, Odd is forced off o, and its cycle's top t has λ_j(t) = λ_{j+1}(t) = t (phase). If v = c_v, then
    Ξ(v) = (v, ∅, 0) at both states. So v ≠ c_v, and p_1 satisfies (i) by minimality.
  - The step "(T) (iii)" of R25 then gives (i) at v unless (E) fails at v: v switched to q := p_1 along a gate of level > L.
  - By (A) at j, q ∉ F_j. Since q ∉ R̄_{j+1} and q ≠ o, q ∈ R_j ∖ R̄_{j+1}: q is a LEAVER that satisfies (i).
  - Now R19 (a) Lemma G, for q ∈ R_j under (h) at j: Ξ_j(q) = π_q ⊕ θ_j and W_j(q) = π_q ⊕ w_j. π_q avoids the paths of θ_j and w_j
    (H1, H2), so lev(π_q ⊕ θ_j, π_q ⊕ w_j) = r_j > L. Hence COARSE_L(Ξ_j q) ◁_L COARSE_L(W_j q).
  - Off R̄_{j+1}, Lemma G (a) gives W_{j+1}(q) = Ξ_{j+1}(q). WM (R23 (g); an S4a step) gives W_{j+1}(q) ⊵ W_j(q).
  - Combining with (i) at q: COARSE_L(Ξ_j q) = COARSE_L(Ξ_{j+1} q) = COARSE_L(W_{j+1} q) ⊵_L COARSE_L(W_j q) ▷_L COARSE_L(Ξ_j q).
    Contradiction. So (i) holds everywhere off R̄_{j+1}.
- (ii) If q ∈ R_j ∖ R̄_{j+1} existed, (i) at q and the last three bullets give the same contradiction.
- (iii) Let (y, z) be a gate at j+1 with z ∈ F_{j+1}. By (ii) z ∈ F_j, and by (i) COARSE_L(Ξ z) is unchanged. If its level were > L,
  TRANSFER (§5) would make (y, z) a gate at j of level > L into F_j, against (A). □

**Theorem CLS1 (PROVED, L-SI succ. 3): the first half of (CL-S) without (H-B1).** Let k0 < k1 be S4c fallbacks of S, and let k1 be
THR with u* ≠ none. Then M_{k1} ≤ min{M_k : k a fallback of S, k ≤ k0}.
Proof. Induction on the fallbacks of S. Let k0 be the last fallback before k1 and L := M_{k0}; by induction L is the minimum so far,
and L < ∞ (R25 NOINF, fixes FB-1).
- Case r_{k1} ≤ L. FBL (R20 (b), THR with u* ≠ none) leaves only R → F switched edges and flat cycle-node switches.
  - CLU bounds the R → F levels by r_{k1} ≤ L. Cycle-node switches have level −1 ≤ L (CN).
  - So M_{k1} ≤ L.
- Case r_{k1} > L. By Fact R, r_j > L for all j ∈ [k0, k1]. So every state of [k0, k1] is THR with u* ≠ none, and every fallback in
  between is such a fallback. Show (A) for L at every j ∈ [k0+1, k1]:
  - j = k0 + 1: OFFGATE (§1), since M_{k0} = L.
  - j → j+1 an S4a step: Lemma NL (iii).
  - j → j+1 a fallback (k0 < j < k1): its M_j ≤ L by the induction, so OFFGATE gives (A) at j+1.
  - At k1, M_{k1} is attained by switched edges (R25 FB step (2)).
    - Those into F_{k1} have level ≤ L by (A).
    - Those into R̄_{k1} are excluded by FBL, except cycle-node switches (level −1).
    - So M_{k1} ≤ L. □
- Remarks.
  - (H-B1) is no longer needed for THR fallbacks with u* ≠ none. These are all 260 non-EQ in-scope fallbacks in the data.
  - For EQ and THR-with-u* = none fallbacks, Theorem CL-S-RED's (H-EQ) remains, now with the F → F case (§3 (e)) added: such fallbacks
    have R → F levels ≤ r ≤ −1 (CLU), and only their other switched edges need a hypothesis.
  - Lemma AL (§6) is now unconditional at THR states (it is NL (ii)).
  - DATA consistency: the 4 arena leaves after a fallback all had r_j ≤ L (§6).

**The second half (the per-level count) reduces to θ-changes (PROVED reduction; the bound itself OPEN).**
- For an Even y, b(y) := Ξ(σ_k(y)) is ⊴-non-decreasing along the whole run: σ moves along gates, and Ξ is monotone (R15 (a), (d)).
- At a fallback of level M, each tail with a level-M gate has b(y) rise at level exactly M (R25 FB step (2)). With COARSE_M(b(y)) fixed,
  the rank-M membership can flip upwards only once.
- So y is a level-M tail at two fallbacks only if COARSE_M(b(y)) strictly rose in between. Then
      #fallbacks of S at level M ≤ Σ_y (1 + #{changes of COARSE_M(Ξ(σ y)) on S}).
- For an R-tail, Ξ(σ y) = π′ ⊕ θ (Lemma G (b)). Its COARSE_M changes when θ changes above M, when the route of σ(y) changes above M,
  or when y switches above M. DATA (box 8 §5, R-ROUTE 10,293 / 0): route changes above L do not occur outside θ's own level.
- Hence, on the data's evidence (READING): fallbacks per level per scope run ≲ n_E(1 + Θ_{>M}(S)), with Θ_{>M}(S) = #θ-changes above
  level M on S. That is item 2 again.

## 13. Item 2 (Θ per scope run without X): where it stands (READING; no lemma this box)
Write T(≥ℓ) := #θ-changes on S at levels ≥ ℓ.
- A θ-change at level ℓ is tame (ℓ ≤ M_j) or a jump (ℓ > M_j; R25 J1).
- Jumps are bounded by Corollary JD (box 7 §9; PROVED) by |succ(o)| + the releases at evicting fallbacks.
- Fallbacks at level M are bounded by §12's reduction, ≤ n_E(1 + T(>M)).
- Tame changes at level ℓ ≤ M come from o-free progress below M (R25 MONO freezes everything above M).
- So the natural recursion is T(≥ℓ) ≤ poly(n)·(1 + T(>ℓ)). That is box 3's multiplicative counter (docs/si/N5-OR-lens-box3.md §3),
  now with the fallback and jump terms made explicit. It gives n^{O(depth)}, not a polynomial.
- What would break it: a lower-digit count that is additive, i.e. tame θ-changes below M bounded independently of T(>M). In the data the
  climbs never exceed 51 θ-changes per phase at n 32 (lev_l_x). OPEN.
