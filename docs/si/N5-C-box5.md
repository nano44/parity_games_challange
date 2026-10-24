# N5 box 5 (b): carries per joint λ-phase, toward (C)
L-SI successor 2 (Opus 5.5, D15/D18). Lead GO 2026-10-24 20:2xZ (box 5: (a) packet P-N5-Z, then (b) here). Started 20:30Z (date -u).
Labels (L40): PROVED (by whom; unrefereed unless stated), CONJECTURE (with data), OPEN, DATA, READING.
Scope: N5 on 𝒞^1O inside one joint λ-phase (docs/si/P-N5-Z-box5.md §0 conventions). These are lemmas about the candidate N5 only.
They are not a bound, not a TARGET.md claim, and not a step-4 pass. G-N5-TIME stays OPEN.
ASSUMPTIONS (one line each):
- A1: 𝒞^1O (now asserted by experiments/si/xing/xclass.py).
- A2: one joint λ-phase, so τ is fixed.
- A3: (h) at the fallback states considered.

## 0. Results in short
- The target: (C) = the number of '+−' reversals at fallbacks per phase. A drain of consecutive evicting fallbacks counts once.
  - By LV′ (P-N5-Z §7), with Lemma EQ (R21 (b)) and R20 for the other pieces, (C) is the hard part of (X).
  - Data: Z ≤ 18 and '+−' fallback reversals ≤ 9 per phase at n 32 (zcl_fb2_n32). W-lowerings reach 19 (x32_waves48, L-RED).
- PROVED (L-SI succ. 2): **Lemma CLU** (§2). At a THR fallback with (h), every eviction target lies at most at the trust-gap level:
  lev(Ξ_k(σ_k y), Ξ_k(z)) ≤ rank(u*_k).
- CONJECTURE (CL) (§3). While w is constant, the CARRY LEVEL is non-increasing along the phase. Carry level := max over a carry's
  active leavers y of lev(Ξ_k(y), Ξ_{k+1}(y)).
  - DATA: 0 violations in 90 consecutive same-w pairs, over 118 carries on all in-class instances, climb bests and L-RED's x32 files.
  - The one apparent violation was on s_rt32_final, which is not in 𝒞^1O.
  - The adversarial climb against CL is in §5.
- FALSE (§4), with instances:
  - (H-VL): "with w constant, a vertex is evicted at most once per level". 13 repeats in 309 evictions.
  - The per-vertex version of CL: 23 increases.
  - So any carry potential must be global (the carry maximum), not per vertex.
- Shape (DATA, §3): carries form a counter digit. Levels go 30, 29, 26, 26, 26, … (zcl_fb2_n32) and 29, 28, 25, 25, … (fbref_cex_n32).
  Consecutive carries at one level are separated by θ-changes at lower levels, or by nothing (a drain).
- OPEN: (C); a proof of (CL); and, given (CL), a bound on the number of carries at one level. Data: ≤ 6 reversal-carries at level 26 on
  zcl_fb2_n32.

## 1. Setting
- Carry: a transition at which some W(v) decreases.
  - By WM (P-N5-Z §8) it is an S4c fallback. On every instance its active crossers are fallback leavers (LF).
  - '+−' carry: a carry whose sign is '−' or '±' and whose previous crossing transition had sign '+'.
  - A DRAIN: maximal runs of consecutive '−' carries.
- Levels: lev(a, b) is the rank of the top vertex of P(a) Δ P(b) when the cycle nodes agree; "length" (−1) if only the lengths differ.
  Lemma U (docs/si/N5-OR-lens.md §2, PROVED by L-SI succ. 1, unrefereed). (ii): a ◁ b ⊴ c ⇒ lev(a, b) ≤ lev(a, c).
- u*_k: the top vertex of P(θ_k) Δ P(w_k) (R20). Under (h), H3 gives equal cycle nodes, so lev(θ_k, w_k) = rank(u*_k).

## 2. Lemma CLU (PROVED, L-SI succ. 2)
Let k → k+1 be an S4c fallback inside a phase, with (h) at k and θ_k ◁ w_k. For every switched edge y → z with y ∈ R_k, z ∈ F_k:
    lev(Ξ_k(σ_k y), Ξ_k(z)) ≤ rank(u*_k).
Proof.
- GAP (P-N5-Z §6): π′ ⊕ θ_k = Ξ_k(σ_k y) ◁ Ξ_k(z) ⊴ W_k(σ_k y) = π′ ⊕ w_k.
- Lemma U (ii) gives lev(π′ ⊕ θ_k, Ξ_k(z)) ≤ lev(π′ ⊕ θ_k, π′ ⊕ w_k).
- π′'s vertices lie in R_k. θ_k's play avoids R_k (H1) and w_k's play avoids R_k (H2). So prepending π′ adds the same vertices to both
  path sets, and the same length to both: lev(π′ ⊕ θ_k, π′ ⊕ w_k) = lev(θ_k, w_k) = rank(u*_k). □
Remarks.
- If the target's value does not change at the fallback, Ξ_{k+1}(y) = y ⊕ Ξ_k(z). Then the eviction level of y equals the left side
  (F-pre).
- With w constant, rank(u*) is non-increasing (Lemma U (ii) with θ ◁ θ′ ⊴ w). So CLU gives carry levels ≤ the current u*. That is
  weaker than (CL): on fbref_cex_n32 u* stays at rank 30 while the carry levels fall 29 → 28 → 25.

## 3. CONJECTURE (CL) and the counter shape (DATA; experiments/si/xing/carries.py)
(CL): inside a phase, if carries k_1 < k_2 have no w-change between them, then carry level(k_2) ≤ carry level(k_1).

Checks (carries.cl_check; longest phase per instance):

| set | carries | consecutive same-w pairs | violations |
| --- | --- | --- | --- |
| 30 named in-class instances + 7 zcl climb bests + L-RED x32_* / u1t | 118 | 90 | 0 |
| s_rt32_final (out of class, two Odd choice vertices) | 6 | 5 | 1, not evidence |

Carry sequences (level, θ-change levels since the previous carry):
- zcl_fb2_n32 (sha1 b00b6b69), u* rank in parentheses:
  - 30 (30) after θ at 18, 29;
  - 29 (29) after θ at 28, 30, 23;
  - 26 (27) after θ at 29, 8, 17, 24;
  - then 26 after θ at 16, 19 / 16 / 8, 17 / 16, 6 / 14, 12;
  - then a drain of 26, 26, 26, 26, 26.
- fbref_cex_n32 (901674dc), u* at 30 throughout:
  - 29;
  - 28 after θ at 27, 29, 17;
  - 25 after θ at 25, 28, 24;
  - 25 after θ at 23;
  - then a drain of 25, 25, 25, 25.

READING:
- (CL) is the "carry digit only moves down" half of a counter.
- The other half, how often one level can carry, is paid in this data by θ-changes strictly below the carry level.
- If both halves held with polynomial constants, carries per w-value would be poly. #w-changes per phase is a separate question:
  w = o ⊕ Ξ(τ(o)) is one vertex's o-free value. Data: 0-4 w-changes per phase.

## 3b. Where a higher carry would have to come from (READING; each step PROVED where marked)
- PENDING LEVEL at state k: P_k := max lev(Ξ_k(σ_k y), Ξ_k(z)) over the honest-improving edges y → z with y ∈ R_k, z ∈ F_k.
- At a fallback every vertex with a gate edge switches. So a carry's level is P_k, provided the targets' values do not change at the
  fallback (the remark under CLU).
- (CL) says P_k, sampled at carries, never rises while w is constant. What can raise it between carries:
  - a θ-increase cannot (PROVED, L-SI succ. 2). For a fixed pair (y, z), with π′ and Ξ(z) fixed and π′ ⊕ θ ◁ π′ ⊕ θ′ ◁ Ξ(z),
    lev(π′ ⊕ θ′, Ξ(z)) ≤ lev(π′ ⊕ θ, Ξ(z)), since lev is an ultrametric (Lemma U). And pairs with π′ ⊕ θ′ ⊵ Ξ(z) leave the max.
  - o-free progress can: Ξ(z) rises for z ∈ F, e.g. at arena steps on the F side.
  - entries can: a new vertex of R brings its o-free options. It entered by an honest-improving edge over its OLD successor only, so
    its other o-free options are unconstrained.
- So a proof of (CL) must show that o-free progress and entries between two carries never push a trust-blocked option above the
  previous carry's level. The levers are WM (W never falls at arena steps) and GAP (every blocked option lies below π′ ⊕ w). I have
  no argument for this.

## 4. Refuted forms (DATA; experiments/si/xing/vlevel.py; all instances re-verified in box 4 / P-N5-Z §11)
- (H-VL): "while w is constant, a vertex is an active fallback leaver at most once per level". FALSE: 13 repeats in 309 active
  fallback evictions.
  - zcl_fb2_n32: vertex 16 at level 16, at k = 33, 37 and 48.
  - x32_waves32 (L-RED): vertex 6 at levels −1 and 22.
  - elim24_p52: vertex 11 at level 21, k = 13 and 36.
- Per-vertex (CL): "a vertex's successive eviction levels never increase". FALSE: 23 increases (zcl_fb2_n32 7, zcl_fb1_n32 6,
  fbref_cex_n32 4, x32_waves32 4).
- Consequence: per-vertex charging, of the kind "each (vertex, level) pays for one carry", does not work. Only the GLOBAL carry level
  is monotone in the data.

## 5. Adversarial climb against (CL) (clclimb.py; fitness (#CL violations, #carries); 25 min each from zcl_fb2_n32, x32_waves48,
fbref_cex_n32)
Three climbs, 25 min each, 20:37-21:02Z. Fitness was (#CL violations, #carries = W-lowerings). Bests pinned in
experiments/si/xing/instances/, each re-verified with reverify.sh (n5.py, Oink zlk OK, strategies verified).

| best (seed) | n | sha1 | n5 it/fb | T | X | Z | carries (W-lowerings) | CL violations | carry levels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ccl_fb2_n32 (zcl_fb2_n32) | 32 | 92f0a04b | 33/23 | 28 | 25 | 2 | 23 | 0 | 31, 31, 30, 28 ×5, 26 ×15 |
| ccl_fbx_n32 (fbref_cex_n32) | 32 | f5867fa6 | 31/24 | 27 | 25 | 2 | 24 | 0 | 31, 31, 28, 26 ×21 |
| ccl_w48_n48 (x32_waves48) | 48 | a7056dea | 46/33 | 41 | 35 | 2 | 33 | 0 | 46 ×8, 45 ×25 |

- (CL) survived: 0 violations in 3 × ~25,000-56,000 mutation steps (the first fitness component stayed 0).
- The secondary fitness pushed W-lowerings to 33 per phase at n 48. All of them sit in DRAINS (sign strings `--++------…`, Z = 2):
  consecutive fallbacks, each evicting a few vertices, with no re-entry in between.
- This confirms the redefinition of (C) (P-N5-Z fixes file §2). W-lowerings can be numerous (24 at n 32, 33 at n 48; both below n − 1 here,
  and a drain has ≤ n − 1 transitions because R strictly shrinks in it). The quantity
  LV′ needs, the reversals, stayed at 2.
- READING: the climb found no way to raise reversal-carries at the expense of (CL). That is weak evidence (the fitness did not target
  reversals), not a proof.

## 6. Box 6 (Lead GO 21:1xZ): the §3b gap. A reduction of (CL) to one jump statement
Data scripts: experiments/si/xing/pending.py, freeze.py, gatelev.py. In-class instance set as in P-N5-Z fixes §1, plus the zcl_* and
ccl_* climb bests. All runs are asserted equal to n5.run.

### 6.1 DATA: what holds between carries (w constant)
Notation: L is the level of the most recent carry. G(L) means "every gate edge (Ξ_k-improving Even edge) has level ≤ L".

| statement | checks | violations |
| --- | --- | --- |
| I(L): at every state after a carry and before the next one, every honest-improving R→F edge has level ≤ L (pending.py) | 784 states | 0 |
| A: a carry of level L changes every Ξ(v) only at levels ≤ L (freeze.py) | 198 carries | 0 |
| FREEZE(L): every transition from a carry up to the LAST carry of the phase changes every Ξ(v) only at levels ≤ L (freeze.py) | 638 transitions | 0 |
| G(L) at every state after a carry (gatelev.py) | 982 states | 11 states; all 13 offending edges are non-cycle-closing F→R entries |

- After the last carry, FREEZE(L) does fail: 20 transitions change some Ξ above L.
  - 19 of them land in a Ξ = W (θ = w) state.
  - 1 lands in a THR state.
  - None is followed by another carry at the same w.

### 6.2 READING: the argument, and where it breaks
- **Step 1 (COARSE-SI, READING).** Suppose G(L) holds at state k. Fix Odd to σ̄_k. In the one-player game G_{σ̄_k}, every Even edge's
  improvement over Ξ_k has level ≤ L. So Ξ_k is an "L-coarse super-solution": telescoping along a play gives
  COARSE_L(V(σ′, σ̄_k)) ⊴ COARSE_L(Ξ_k) for every Even σ′ whose (σ′, σ̄_k)-plays end in cycles of the (σ_k, σ̄_k)-graph.
  - Since Ξ_{σ′} ⊴ V(σ′, σ̄_k) (Odd's best reply), and with R15 (a), COARSE_L(Ξ) cannot change at k → k+1 unless σ_{k+1} closes a
    NEW cycle in G_{σ̄_k}.
  - COARSE_L(v) := (cycle node, path vertices of rank > L), so "level > L" means "COARSE_L differs".
  - Not refereed. The simple-path bookkeeping of the telescoping is not written out.
- **Step 2 (PROVED, L-SI succ. 2).** If COARSE_L(Ξ) is constant at k → k+1, then G(L) at k implies G(L) at k+1.
  - Take a gate edge (y, z) at k+1, and let u = σ_{k+1}(y). u is σ_k(y) or a gate target at k, so
    COARSE_L(Ξ_k(u)) ⊵ COARSE_L(Ξ_k(σ_k y)).
  - If COARSE_L(Ξ_k(z)) were above COARSE_L(Ξ_k(u)), then (y, z) would be a gate edge at k of level > L, against G(L).
  - Both coarse values are unchanged at k+1, so (y, z) has level ≤ L at k+1.
- **Step 3 (where it breaks; DATA, 4 of 4 first failures).** On fbref_cex_n32 (k 53), x31_lem_t32 (k 58), x32_waves48 (k 80) and
  run_x_inr2 (k 49), G(L) holds at k and fails at k+1.
  - At each, an INR happens: the argmin exit σ̄_k(o) enters R. So under σ̄_k the play from o closes a NEW cycle through o, the case
    Step 1 excludes.
  - Odd switches exits (24 → 9, 24 → 11, 3 → 34, 24 → 9), and θ jumps at level 30, 31, 47, 30, above L = 25, 28, 45, 24.
  - In all four the new state has θ = w (Ξ = W). With w constant, θ = w persists (R21 XW3), and NOFL-E (P-N5-Z §5) then forbids
    evictions at fallbacks. So no carry follows while w stays constant.
- **Reduction (READING).** (CL) ⟸ Step 1 (written out) + A + (JUMP-EQ), where:
  - CONJECTURE (JUMP-EQ): inside a phase with w constant, if an INR at k → k+1 raises θ at a level above the level of the most recent
    carry, then θ_{k+1} = w.
  - DATA: 4 of 4 first failures. Of the 20 post-carry above-L transitions, 19 land in θ = w. The one that lands in a THR state needs a
    look before (JUMP-EQ) is stated as the final form.
  - Why it might be true (heuristic only): after a carry all o-free exit values are coarse-frozen at level L, and w = o ⊕ Ξ(τ(o)) is
    one of those exits. A jump above L means every exit below w at the coarse level has been captured by R.
- What a proof of (C) would then need besides (CL): a bound on the carries at ONE level. In data these are separated by θ-changes
  strictly below the level (§3), and Step 1 says those are the only changes possible. This is the "lower digits refill" half of the
  counter. OPEN.

### 6.3 Status
- PROVED (L-SI succ. 2): Step 2 above; CLU (§2); the θ-monotonicity of pending levels (§3b).
- READING: Step 1 (COARSE-SI), and the reduction (CL) ⟸ Step 1 + A + (JUMP-EQ).
- CONJECTURE: (CL), A, FREEZE(L) (scoped), (JUMP-EQ). Data as in 6.1; 0 violations except where noted.
- OPEN: (C); carries per level. G-N5-TIME stays OPEN.
