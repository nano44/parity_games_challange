# R119: the mixed frame adds no gating power. Lemma MG: an Odd lock on Even's improving set that matters for N5's choice must read an Even vertex that is not at τ̄(τ), or use an Odd deviation inside Iτ, or close a loop; R117 §4's CDAG obstruction holds in the mixed frame for any nesting of Odd deviations outside Iτ. READING (lane proof) + DATA; G-N5-TIME untouched
L-RED successor 30 (Opus 5.5; D1/D18; Lead 19:51Z STEP 1 (b): "a super-polynomial fixed-τ stretch under the mixed frame, the (FO*)
question"). Written 2026-10-29 from 20:13Z (date -u). Labels: READING / DATA / OPEN / DEAD. Not a TARGET.md claim, unrefereed.
Engine: L-COMP's n5b.py SPEC mode. Order ⊴ = SPEC S1's order, Even's view.

## 0. The question and the loophole tested
- In a fixed-τ stretch, N5's Even step (S4a) is σ_new = the W_τ-optimum over the arena {σ(v)} ∪ Iσ(v), where W_τ = values against
  the FIXED τ. Iσ is computed against Odd's FREE best reply σ̄(σ) (S1, S2). Write T := τ̄(τ), Even's optimal counter to τ (S1 on
  G^d), and Ξτ(v) = the value of v under (T, τ). On G^d the order is exactly reversed (reward^d = −reward − 1, P-weights flip sign,
  the length rule flips), so Ξτ is also the primal value of the (T, τ)-play.
- The masks of R117 §3-§4 lock an Even switch x → u by an Odd choice that Odd's best reply takes and τ does not. R117 §4 killed single
  masks with τ = τ*. The mixed frame seemed to leave a loophole: τ need not be optimal; a mask can lock through Odd options that are
  OUTSIDE Iτ, so N5's Odd step can never take them, while σ̄(σ) uses them freely.
- Result: the loophole is closed by additivity of S1's valuations.

## 1. Lemma MG (READING; elementary proof)
Setting: any state (σ, τ). Let u be a vertex and π the (σ, σ̄)-play from u. Let p_1, …, p_r be the Odd vertices on π, in order, with
σ̄(p) ≠ τ(p) (the DEVIATIONS).
Hypotheses:
- (i) every Even vertex w on π has σ(w) = T(w);
- (ii) every deviation has (p, σ̄(p)) ∉ Iτ;
- (iii) no deviation lies on π's cycle, and for each i the (T, τ)-play from τ(p_i) avoids π's prefix up to p_i.
Claim: Ξσ(u) = val_(σ,τ)(u) = Ξτ(u). Odd's free reply gains nothing at u over τ, and u already has its G_τ-optimal value.
Proof.
- (Prepend.) If s is a path segment and A, B are plays that both avoid s, then A ⊴ B implies s·A ⊴ s·B.
  - With the same cycle node, the same vertices of s are added to both P-sets and |s| to both lengths.
  - With different cycle nodes, the cycle comparison does not change.
- Let B_i be the (T, τ)-play from τ(p_i), and A_i the (T, τ)-play from σ̄(p_i).
  - By (i) and (iii), A_i follows π from σ̄(p_i) up to p_(i+1) and then continues as B_(i+1).
  - A_r is π's remainder after p_r.
- By (ii), Ξτ(σ̄(p_i)) ⊵ Ξτ(τ(p_i)), i.e. A_i ⊵ B_i.
- Let Π_i = (π up to p_i)·A_i. Then:
  - Π_r = π;
  - (π up to p_i)·B_i = Π_(i−1);
  - Π_0 = the (T, τ)-play from u.
- Prepend gives Π_i ⊵ Π_(i−1). Hence Ξσ(u) = val(π) ⊵ Ξτ(u).
- Conversely, Ξσ(u) ⊴ val_(σ,τ)(u), because σ̄ is Odd's pointwise optimum. And val_(σ,τ)(u) ⊴ Ξτ(u), because T is Even's pointwise
  optimum in G_τ. So all three are equal. □
Consequence (READING). Let (x, u) ∉ Iσ be a lock, i.e. Ξσ(u) ⊴ Ξσ(σ(x)), with MG's hypotheses at u. Then:
- Ξτ(u) = Ξσ(u) ⊴ Ξσ(σ(x)) ⊴ val_(σ,τ)(σ(x)) ⊴ W_new(σ(x)).
- The last step holds because σ lies in the arena and S4a's optimum is pointwise.
- So x → u is not W-better than keeping σ(x) at the next state, and the lock is inert, up to ties and to loops through x.
A lock that changes N5's choice must therefore read an Even vertex w ≠ T(w) (fail (i)), or deviate inside Iτ (fail (ii)), or close a
loop (fail (iii)).
- Value form (remark, not checked): (i) can be weakened to "every Even w on π is DONE, i.e. val_(σ,τ)(w) = Ξτ(w)". The DONE set is
  closed under (σ, τ)-successors, so σ is G_τ-optimal on it and can replace T there.

## 2. What it gives for (FO*) and FRAME-STRETCH-P (READING + DATA)
- (DONE-MONO, elementary.) Inside a fixed-τ stretch W_k := val_(σ_k,τ) never decreases, because σ_k is in the arena. So the set DONE_k
  = {v : W_k(v) = Ξτ(v)} only grows, and the stretch is (≤ n DONE-additions) × (runs of W-rises among undone vertices).
- By §1 every lock that matters in a stretch either reads an undone (lagging) Even vertex or uses an Odd deviation that N5's Odd step
  could take but does not (fail (ii)).
- CDAG at m = 3 in the mixed frame (R117 §4 extended). At S1 the only Even vertex with σ ≠ T is the gated vertex 2 itself. A lock on
  (2, 1) through deviations outside Iτ, nested to any depth, is excluded by the same telescoping: the play from the gate passes 2.
  - Write seg := (gate … 2).
  - At S1, closed means seg·Y ⊴ Y, with Y = sink.
  - Under (T, τ), T(2) = the gate, and (ii) chained gives seg·B_1 ⊵ B_1, with B_1 = the τ-play from 1.
  - Additivity forces weight(seg) ≤ 0 and > 0 together (equal weights are broken by length, and here longer is worse for Even), a
    contradiction.
  So plan (b) on CDAG is DEAD in the mixed frame too, not only at τ = τ*.
- DATA (experiments/red/mix/):
  | check | games / states | hits | violations | notes |
  | --- | --- | --- | --- | --- |
  | mgcheck.py, corpus sbcg.lst (L-SI's copy of L-NEW box59, 719 games, S3) | see addendum | | 0 so far | every lock fails (i), (ii) or (iii) |
  | mgcheck.py dw_3 | 42 states | 1145 | 0 | 288 locks: all fail (i); control (only (i) fails, claim false) 2383 |
  | mgcheck.py runquad_K8_m30_n192 (mkr, explicit start) | 265 | 1512 | 0 | 40392 locks, all fail (i); control 37682 |
  | mgcheck.py d_hntop_n8 (dual, Odd's long τ-run) | 292 | 5661 | 0 | 43395 locks, all fail (ii): Even's locks use Odd's own improving switches |
  The control row shows that (i) is needed and that the test can fire.
- Sampler mixgate.py: CDAG_n with two-level gates o → {u, b}, b → p (Odd) → {z, q}, q → z2. Random priorities and readers, σ_0 = all
  → sink, τ_0 RANDOM (not τ*).
  | n | samples (seeds) | longest τ-stretch | histogram | chain 2^n − n − 1 |
  | --- | --- | --- | --- | --- |
  | 3 | 200 000 (1, 2) | 3 | 0: 16 537, 1: 171 729, 2: 11 255, 3: 479 | 4 |
  | 4 | 50 000 (1) | 4 | 1: 45 250, 2: 4174, 3: 299, 4: 13 | 11 |
  | 5 | 20 000 (1) | 4 | 1: 18 050, 2: 1814, 3: 125, 4: 11 | 26 |
  The sampler has the same ceiling as R117's single masks with τ = τ* (3 at n = 3). Random sampling at n ≥ 4 is weak evidence.
- DONE profile (done.py):
  - runquad_K8_m30_n192: one stretch of 264 σ-changes, DONE 22 → 192, with only 16 adding steps. The quadratic stretch is long runs of
    W-rises among undone vertices.
  - dw_5: 38-step stretch, 36 adding steps.
  - mk_20_80: addendum.

## 3. What is left (OPEN) and where it points
- A super-polynomial fixed-τ stretch needs exponentially many W-rises among undone vertices. Each lock that matters reads a lagging Even
  vertex (one with σ ≠ T, on the lock's free play, other than the locked vertex x itself, unless the Case-2 telescoping is escaped by a
  cycle change), or rides an Odd deviation in Iτ that N5's Odd step leaves untaken.
  - The first kind is Even's own lag. A chain must keep a supply of lagging vertices that the locks read, and those vertices must
    themselves be held lagging by further locks or by their T-plays.
  - The second kind is the mixed frame proper: Odd improving switches that are W-worse for Odd against the current σ (S4b). On the
    dualised families every lock is of this kind (d_hntop_n8: 43395 of 43395).
- Mirror (by P-N5-DUAL, not re-proved): an Odd lock that matters reads an Odd vertex with τ ≠ σ̄(σ), or an Even deviation in Iσ.
  For route (a) this says that a cross-released step of one side is a lock of the OTHER kind: it rides the opponent's untaken
  improving switches. This is consistent with L-SI box 33 (class X, re-entries charged to U(e)-rises), but nothing is composed here.
- Not done in this box: route (a) (coupled counters with class-X Odd options).

## DONE / FINDINGS / NEEDS
- DONE: mix/mgcheck.py (exact per-state Lemma MG check + control), mix/mixgate.py (two-level gate sampler, random τ_0), mix/done.py
  (DONE profile), check.sh gate (mgcheck dw_3; mixgate 3 300 1).
- FINDINGS:
  1. READING (lane proof): Lemma MG. Odd's free best reply cannot lower a value below the G_τ optimum along plays that follow τ̄(τ) and
     deviate only outside Iτ. Locks that matter read lagging Even vertices or Odd deviations inside Iτ.
  2. DEAD: plan (b) on CDAG in the mixed frame (any nesting of Odd deviations outside Iτ), not only at τ = τ*.
  3. DATA: 0 violations of MG (dw_3, runquad_K8, d_hntop_n8; corpus in the addendum); the sampler ceiling is 3 / 4 / 4 at n = 3 / 4 / 5.
  4. READING: DONE-MONO. A stretch is at most n DONE-additions apart from W-rise runs among undone vertices (runquad_K8: 16 additions
     in 264 steps).
- NEEDS: none from the owner.
