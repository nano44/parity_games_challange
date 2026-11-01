# R183 Growing FVCH (iterating odxi_n37's cross-anchor overtake): no family. Obstruction: Lemma OVT-KEY (PROVED, lane). Inside one FL run, a vertex can re-enter an option it left only after a σ-change below it on the W-plays of its tight options. So gates whose W-faces go straight to the W-cycle node (odxi_n37's shape) release at most |T_x| − 1 moves of x per FL run, however often their Ξ-values overtake each other. Corollary DEPTH: FL moves of non-cycle-node vertices ≤ n(Δn)^(ℓ*−1), whatever Ξ does (L-RED successor 43)
Started 2026-11-01 17:50Z (Lead brief, STEP 1 = R183; date -u). Brief: «iterate odxi_n37's cross-anchor overtake. Build two gates read by
W-tied siblings whose Ξ-values rise past each other repeatedly inside one FL run … A family with FVCH and L_FL growing super-linearly is
the target. Otherwise give the exact obstruction as a lemma L-NEW can use.»
Labels: PROVED (lane), DATA, READING. Premises and notation are those of the frozen packet P-N5-ANCHOR (f009a9a1) §1-§2: FL run, W,
level ℓ, CN, T_x, [RULE] with κ_j, FL-TIGHT, bridge B. Not a TARGET.md claim. G-N5-TIME stays OPEN. No kill.

## 0. Answer
- No family with growing FVCH or L_FL was found. Best FL run in the iterated-gadget search: L_FL 8, FVCH 8 at n 81-129. That is the
  same as the core's own run (§3), and it is flat in the number k of gadgets.
- The obstruction is not on the Ξ side; it is TB's key. Lemma OVT-KEY (§1, PROVED, lane):
  - Inside one FL run, take a stretch of states on which σ is constant on B_x. B_x is the set of Even vertices below x on the
    W-tight plays of x's options.
  - Every move of x in that stretch strictly lowers a FIXED key of x's option.
  - So x moves at most |T_x| − 1 times per stretch and never re-enters an option it left in the stretch. Ξ, anchors and FV play no
    role.
- Corollary GATE-SINK. In odxi_n37 the two gates' W-faces go straight to the W-cycle node (τ(33) = τ(34) = 32, the sink), so B_x = ∅.
  The gadget's x = 35 therefore moves at most |T_x| − 1 = 1 time per FL run, however often Ξ(33) and Ξ(34) rise past each other.
  - Iterating the gadget makes FVCH events (anchor-value changes) but no moves. The chained gadget movers move ≤ deg − 1 = 1 time
    per run (DATA §3: ≤ 2 over the whole N5 run).
- Corollary KEY-CHARGE: moves_run(x) ≤ (|T_x| − 1)(1 + KCH_x). KCH_x counts the transitions of the run that change σ on B_x.
- Corollary DEPTH: per FL run, the moves of Even vertices ∉ CN number ≤ n(Δn)^(ℓ*−1) (Δ = max out-degree).
  - This is polynomial for bounded W-depth ℓ*. It does not bound FL transitions at which only W-cycle nodes move (CNONLY).
  - It is exponential in ℓ*. R177 LADDERBF (TB alone: 2(2^(d+1) − d − 2)) shows that an exponential in the depth is the truth for TB
    with adversarial availability, so DEPTH is the right shape for a Ξ-free bound.
- What this means for L-NEW box 135 (READING):
  - FVCH is the wrong currency for releases. An FV change can release a RE-move of x only after a key change in B_x, i.e., a move
    strictly below x in W-level.
  - A growing family must put choice vertices on the gates' W-faces (graded W-faces). That is the shape of R178's IDEAL model, where
    every option is an ODIFF gate with empty prefix, so every comparison is CROSS. There the best runs are linear (2.7 n_E, R178; z3
    max 4 at d = 2, R180), with σ̄ and τ fixed by fiat.
  - A proof of «FVCH ≤ poly × (1 + cycle-node changes + WCH)» must cover the IDEAL model, where cycle-node changes = WCH = 0. So it
    either proves IDEAL-POLY or uses σ̄-optimality / τ-stability, which the IDEAL model drops.
  - Read per FL run (where WCH = 0), the «1 +» is needed: odxi_n37 has FVCH 5 with CNCH = SBCH = 0 inside its FL run (§3).

## 1. Lemma OVT-KEY (PROVED, lane)
Setting: an FL run [a, b] (packet §1); W, ℓ, CN, T_x are constant on it. Even x ∉ CN.
- B_x := the Even vertices v ∉ CN, v ≠ x, reachable from T_x by W-tight steps: T_v at Even v ∉ CN, τ_a at Odd; stop at CN.
  - Every v ∈ B_x has ℓ(v) < ℓ(x): tight steps lower the level by one.
- A KEY-STRETCH of x is a maximal interval [j0, j1] ⊆ [a, b] of states on which σ_j restricted to B_x is constant.
- A move of x at transition j (σ_j(x) ≠ σ_(j−1)(x)) BELONGS to the stretch that contains its new state j.

Statement. The options σ_(j0−1)(x) (when j0 > a), σ_(j0)(x), …, σ_(j1)(x) strictly decrease in one fixed injective key κ* on T_x at every
move of x that belongs to [j0, j1]. Hence:
- (a) at most |T_x| − 1 moves of x belong to one key-stretch;
- (b) x never moves back to an option it left by a move of the same stretch.

Proof.
1. Keys are frozen on the stretch.
   - By [RULE], κ_j(y) (y ∈ T_x) is either the index of y (x's W′-cycle node c odd; W′ = W*_j = W, so the case is fixed on the run),
     or the vertex sequence of the σ_j / τ_(j−1) play from y to c, read root-first (c even).
   - τ_(j−1) = τ_a on the run.
   - By FL-TIGHT, σ_j(v) ∈ T_v at every Even v ∉ CN, so that play follows W-tight steps from y until it reaches c.
   - x ∉ CN is not on it (V1, packet bridge B).
   - So all its Even vertices other than c lie in B_x, and κ_j(y) depends only on σ_j|B_x, τ_a and indices.
   - On [j0, j1] these are constant, so κ_j = κ* there.
2. One move lowers κ*. Let x move at j ∈ [j0, j1], from z = σ_(j−1)(x) to y = σ_j(x).
   - Bridge B: z, y ∈ TIE_j(x).
   - [RULE]: y is the κ_j-least element of TIE_j(x).
   - κ_j is injective: indices are distinct, and distinct options give distinct root-first sequences, since the last vertex is the
     option itself.
   - y ≠ z, so κ*(y) = κ_j(y) < κ_j(z) = κ*(z).
3. The value κ*(σ(x)) along the moves of the stretch is therefore strictly decreasing, and all values lie in κ*(T_x) (FL-TIGHT).
   This gives (a) and (b). ∎
- Only movers are used, so (R1) is not needed. No Ξ, anchor, σ̄ or FV hypothesis is used. The odd case is FL-IDX (R177).

Corollary KEY-CHARGE. moves_run(x) ≤ (|T_x| − 1)(1 + KCH_x), with KCH_x := #{j ∈ (a, b] : σ_j|B_x ≠ σ_(j−1)|B_x}
≤ Σ_(v ∈ B_x) moves_run(v).
- Proof: the stretches number 1 + KCH_x, and every move belongs to exactly one of them. Apply (a). ∎

Corollary GATE-SINK. If no v ∈ B_x has |T_v| ≥ 2 (in particular B_x = ∅), x moves at most |T_x| − 1 times in the run.
- Proof: FL-TIGHT fixes σ on B_x, so KCH_x = 0. ∎
- odxi_n37: T_35 = {33, 34}, both gates have τ → 32 (CN), so B_35 = ∅ and x = 35 moves ≤ 1 time per FL run.

Corollary DEPTH. Let μ_ℓ be the maximum of moves_run(x) over Even x ∉ CN with ℓ(x) ≤ ℓ. Then:
- μ_1 = 0: T_x = {c}.
- μ_ℓ ≤ (Δ − 1)(1 + n·μ_(ℓ−1)), so μ_ℓ ≤ (Δn)^(ℓ−1).
- The FL transitions at which some Even vertex ∉ CN moves number ≤ Σ_x moves_run(x) ≤ n(Δn)^(ℓ*−1).
- Proof: KEY-CHARGE, with |B_x| ≤ n and B_x of lower level; induction on ℓ. ∎
- The remaining FL transitions move only W-cycle nodes (CNONLY). Their moves strictly raise ξ among T_c inside an epoch (packet §4
  (ii)), which is still gating-circular. DATA: CNONLY 2 / 1 on fl_s48 / fl_s64, 0 on odxi_n37. Corpus: §3.

## 2. Why iterating odxi_n37 does not grow (READING, on §1)
- In odxi_n37, x = 35 compares two ODIFF gates 33 → {2, 32} and 34 → {32, 36 → 9}. Their τ-faces both go to the sink 32 (CN); their
  σ̄-faces go into the random core.
  - Ξ(33), Ξ(34) follow Ξ(2), Ξ(9), so the gates can overtake each other as often as the core lets them (FVCH 5 in the run).
  - But B_35 = ∅: κ is frozen for the whole run, so x moves once. The one CROSS flip seen anywhere (box 134 §2) is that single move.
- To make x move again, a choice vertex below x on a gate's W-face must move between x's moves (KEY-CHARGE).
  - Such a gate's W-face then reads lower movers. That is the graded two-face gate of R178's IDEAL model, together with R177 §5's
    stabiliser problem: σ̄ must stay the Ξ-face against every σ of the run, and τ must stay the W-face.
- Chains and rings of gadgets (§3) add anchor-value changes but no FL transitions. The core's run (L 7-8) is the run.

## 3. DATA
Tools (experiments/red/r183/):
- fvch.py: per FL run, FVCH / FVMAX / FVU / CNCH / SBCH / FLIPS / CROSS / CAP / FL-ANCHOR′ BOUND. Its run detection is that of box 132
  anchor.py. Its FLIPS / CROSS are cmpw.py's.
- ovtkey.py: the checker of §1: returns, returns inside a stretch, over-full stretches, KEY-CHARGE, CNONLY.
- chain.py / climbs.py: iterated gadgets on odxi_n37's core.
- climb183.py: free climb, score FVCH.
- kclimb.py: adversarial climb against OVT-KEY.
- krand.py: random games.
- mkstart.py: writes default-S3 START files.

| set | runs | FL | FVCH (sum / max per run) | CROSS | flips | returns | in-stretch returns / over-full / KEY-CHARGE viol. | CNONLY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| corpus, 813 distinct pairs (E-1) | 20 | 42 | 2 / 1 | 0 | 94 | 39 | 0 / 0 / 0 | 13 |
| odxi_n37 (L-NEW, own start) | 1 | 8 | 5 / 5 | 1 | 45 | 31 | 0 / 0 / 0 | 0 |
| fl_s48 ; fl_s64 (R181) | 3 ; 2 | 10 ; 8 | 6 / 6 ; 0 / 0 | 0 ; 0 | 12 ; 16 | 7 ; 9 | 0 / 0 / 0 | 2 ; 1 |
| odxi_many_n32 (R179) | 3 | 8 | 4 / 3 | 0 | 7 | 2 | 0 / 0 / 0 | – |
| 14 r15x-r18x pins | – | – | – | – | – | 49 | 0 / 0 / 0 | – |
| ovk_n37 (adversarial climb, pin) | 1 | 7 | – | – | – | 37 | 0 / 0 / 0 | 0 |
| k48 (adversarial climb from fl_s48) | 1 | – | – | – | – | 10 | 0 / 0 / 0 | – |
| 3,000 random games n 6-30 | 10 | – | – | – | – | 0 | 0 / 0 / 0 | – |
- The corpus counts reproduce box 134 exactly: 168 FL moves of non-cycle-node vertices, 94 flips, CROSS 0.
- Iterated gadgets (climbs.py; k 1-2: 3,000 mutations; k 4-32: the climbs were stopped by pid after ~40 min, last improvements at
  mutations 5,061 / 13,212 / 7,072 / 4,987; outputs re-checked intact; free gate targets among the core, the sink and any mover, i.e. chains, rings
  and feedback; free priorities):

| k (gadgets) | n | best L_FL | its FVCH | CROSS (all runs) |
| --- | --- | --- | --- | --- |
| 1 (odxi_n37 shape, default start) | 36 | 7 | 7 | 1 |
| 2 | 39 | 8 | 8 | 2 |
| 4 | 45 | 8 | 8 | 4 |
| 8 | 57 | 7 | 7 | 7 |
| 16 | 81 | 7 | 7 | 14 |
| 32 | 129 | 7 | 7 | 11 |
- CROSS grows with k (anchor overtakes are cheap: 14 at k 16), but L_FL and FVCH do not. The free climb climb183.py from
  odxi_n37 reached FVCH 6, L 7 (4,000 mutations, 2 seeds); from random n 24, FVCH 0.
- chain_k16_n81 (pin): L 7, FVCH 7, CROSS 3, SBCH 6, BOUND 154. Over the whole N5 run each of its 16 gadget movers moves ≤ 2 times.

Pins (experiments/red/r183/instances, pins.sha1; START files are the default S3 start written out by mkstart.py, except odxi_n37's
own): chain_k16_n81, ovk_n37, odxi_n37 (copy of L-NEW box 133's, sha1 83f263c1a4d0). Each passes startck.py, Oink --zlk + verify
(oinkcmp.sh: OINK OK), Oink --tl + verify (exit 0), and xeng (state sequences identical).

## 4. Next (Lead decides)
- Proof side (L-NEW): replace FVCH in FL-ANCHOR′ by key changes. KEY-CHARGE is well-founded (downward in W-level) where FVCH is
  circular. The open part is the multiplication per level (DEPTH's base Δn). A polynomial bound needs Ξ to cap how often a level-ℓ
  key change can re-release level ℓ + 1: a Ξ-side «release once per key change» statement.
- Attack side (me): the only route left for a super-linear FL run at unbounded ℓ* is a graded structure. Gates' W-faces read lower
  choice vertices whose moves re-order the keys above, AND gates whose Ξ-faces re-release above. That is LADDERBF's TB ladder driven
  by real (stabilised) gates. Concretely: realise R178's best IDEAL genome (d 4, 32 FL) as a real game with R177 §5's (τ)/(σ̄)
  checks, and measure how much of the run survives.
- Queue unchanged after that: NR-CYC (R182 §2), faster exact IDEAL d = 3, two-level replay, super-linear D at ODIFF ≥ 1.
