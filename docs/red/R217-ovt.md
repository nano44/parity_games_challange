# R217 OVT gadget vs CANDIDATE N5′-xi (L-RED successor 54; Lead GO 14:37Z 2026-11-07)
Labels: PROVED (lane, unrefereed) / PROVED-CONDITIONAL (named premise) / DATA (unit, set, scope) / DEAD (instance) / READING (not to sign).
Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1). Setting, notation and premises ([VJ], [LOC],
F1-F6, IDEAL-CYC, MERGE) are those of L-NEW's frozen packet docs/new/P-N5-XICYC.md and docs/new/N5-RPOT-box192.md (claude/l-new a2db977d).
Tools: experiments/red/r217/ (own.py = my independent implementation; leap.py = the construction; xcheck.py = cross-checks).

## 0. Answers (milestone 1, 15:0xZ)
- Interleaving is cheap. LEAP(k) is a hand-built d 2 genome with N = 4k + 5 movers in which one gate g flips 2k times. Each overtake
  costs O(1) size: one fuse mover (2 options) plus one tap bit (1 option) plus one option at Y or X′. At k = 64 (N 261) g flips 128
  times, against ≤ 15 at one gate in every search (R215 §53.1-§53.2, box 192). So the «flat ≤ 15» pattern was a search artifact.
  DATA exact for k = 1-64, from four independent routes (§3).
- R grows only linearly: R = 2k = (N − 5)/2, C = 0, L = 0, R_mov = R, T = 2k + 1. On Γ3(LEAP(k)), N5′-xi (n5v xi = n5bxi) takes T + 3
  iterations, and the regions equal Oink's. No superlinear R.
- Why flips at one gate cannot beat the face values (Lemma OVT-DV, §2, PROVED-CONDITIONAL on [LOC]): on a tie-free stretch, the
  flips at g are ≤ 2·min(D(e_g), D(β_g)) − 1, where D(v) is the number of distinct values of Ω(v). LEAP meets this bound with
  equality up to 1 (flips 2k, D(Y) = k + 1). So OVT-POLY ⇐ «every vertex takes polynomially many distinct values». The OVT question is
  exactly as hard as making ONE vertex's value change superlinearly often. Two monotone sequences interleaving adds nothing and costs
  nothing.
- The real obstruction (READING, §5): LEAP's values change only while a fuse is first discovered (BR-SEG's PATH mechanism). After
  that, carriers reach every chained mover in the same step, so a fuse fires once. Repeated firing needs a RESET (exit ▷ chain), and
  monotonicity forces each reset to bring a new, higher value. My two self-triggered round designs (leapr v0 / v1) did not re-fire
  (instances in §5).

## 1. Lemma TOP-DEC (PROVED, lane; the decision part PROVED-CONDITIONAL on [LOC])
This is the «MERGE reading» from my 14:35Z message, stated and proved as the Lead asked.
Setting: a state of IDEAL-CYC(G) for any genome G; a gate g with Λ(e_g) = Λ(β_g) = w, where w is less relevant than e_g; A′, B′, m as
in MERGE (box 192 §2). Write top(S) for the most relevant vertex of S.
Statement:
(a) Every vertex of A′ ∪ B′ that is at least as relevant as e_g is an e-vertex. Its priority is therefore even.
(b) e_g ∈ A′, so a* := top(A′) is an e-vertex at least as relevant as e_g.
(c) If B′ ∩ U_w = ∅, or top(B′ ∩ U_w) is less relevant than a*, then Ω(e_g) ▷ Ω(β_g). Otherwise Ω(β_g) ▷ Ω(e_g).
(d) [LOC] σ̄(g) = e iff B′ contains an e-vertex more relevant than every vertex of A′.
Proof.
- Priorities in Γ(G) (P-N5-XICYC [DEF], gamma3.build): movers 0, gates 1, cX 2, K2 3, K1 5, β's in [6, bmax], e's above bmax, even and
  ordered by (level, gate index), cW = top (above every e), K0 = top + 2, K3 = top + 3. So the vertices at least as relevant as e_g are:
  e_g; the e-vertices of higher (level, index); cW, K0, K3.
- cW has only its self-loop. If cW is on a play, the play ends in that loop and Λ = cW. Then w = cW is more relevant than e_g,
  contrary to the hypothesis. So cW is on neither play.
- K0 and K3: in IDEAL-CYC the only edges into {K1, K2} come from K3 (frozen K3 → K2), and the only edge into K3 is K0 → K3 (frozen).
  K0 leads only to K3. If w ∉ {K1, K2}, neither play reaches K0, hence neither reaches K3. If w ∈ {K1, K2}, both plays pass K0 and
  then K3. Then m comes at or before K0 on P_A, and the plays coincide after m, so K0 and K3 lie in the common suffix, not in
  A′ ∪ B′. This proves (a).
- (b): MERGE gives e_g ∈ A′. e_g is more relevant than w, so e_g ∈ U_w; top(A′) is at least as relevant as e_g, and by (a) it is an
  e-vertex.
- (c): MERGE says the order is decided by z := top((A′ ∪ B′) ∩ U_w), and the face containing z is the ⊴-larger one iff z is even.
  If B′ ∩ U_w is empty or its top is less relevant than a*, then z = a*, which lies in A′ and is even: e is better for Even.
  Otherwise z = top(B′ ∩ U_w) is more relevant than a*, hence than e_g; by (a) it is an e-vertex, so it is even: β is better for Even.
  The two faces never tie, because z exists.
- (d): [LOC] (box 192 Corollary MERGE-CHOICE) makes Odd take the ⊴-smaller face. ∎
READING: at a gate whose cycle node lies below e_g, Odd compares only the «e-heads» of the two pre-merge segments. Every vertex that
matters is even, so in effect two binary numbers on the e-vertices above e_g are compared. LEAP (§3) drives exactly this comparison.

## 2. Lemma OVT-DV (PROVED-CONDITIONAL on [LOC], lane)
For a vertex v and a set I of consecutive states, let D_I(v) := |{Ω_t(v) : t ∈ I}|.
Statement: let g be any gate and I = [a, b] consecutive states with Ω_t(e_g) ≠ Ω_t(β_g) for every t ∈ I. Let F be the number of
t ∈ (a, b] with σ̄_t(g) ≠ σ̄_(t−1)(g). Then F ≤ 2·min(D_I(e_g), D_I(β_g)) − 1.
Moreover D_I(e_g) ≤ D_I(y) + 1 for the W-target y (or c_W). Likewise D_I(β_g) ≤ D_I(x′) + 1 for the Ξ-target x′, while D_I(β_g) = 1
when xt = X.
Proof.
- [LOC]: with no tie, σ̄_t(g) is the face of ⊴-smaller value. Write A_t := Ω_t(e_g) and B_t := Ω_t(β_g). Both are ⊴-non-decreasing
  in t (F1).
- A flip e → β at step t means A_(t−1) ◁ B_(t−1) and B_t ◁ A_t, so A_t ▷ B_t ⊵ B_(t−1) ▷ A_(t−1): A increases strictly at step t.
  Symmetrically, a flip β → e means B increases strictly at step t.
- So the e → β flips are at most D_I(e_g) − 1, and the β → e flips at most D_I(β_g) − 1. The directions alternate, so
  F ≤ 2·min(D_I(e_g) − 1, D_I(β_g) − 1) + 1.
- If e_g is not a cycle node at t, F3 gives A_t = ext(e_g, Ω_t(y)), and ext is injective (F4). If e_g is a cycle node,
  A_t = (e_g, ∅, 0), one value. Hence D_I(e_g) ≤ D_I(y) + 1. The β-face is the same (β → u is fixed when xt = X: box 192 X-GATE). ∎
Remarks.
- Ties (L_g states) split the run into tie-free intervals. Each tie state adds at most 2 flips. L_g = 0 in all data (box 192; §3).
- Tightness: in LEAP(k), D_I(Y) = k + 1 (Y takes k + 1 values: start and k taps) and F = 2k. The bound is met up to 1.
- Consequence: CONJECTURE OVT-POLY ⇐ «D(v) polynomial for every vertex v». The converse is NOT claimed. Since D(v) ≤ T + 1, OVT reduces
  to the growth of single values, i.e. to the length of the run itself.

## 3. Construction LEAP(k) and DATA
Construction (experiments/red/r217/leap.py; d = 2, i.e. levels 0 and 1; every mover starts on option 0):
- FUSE: level-0 movers c_0 … c_(L−1), L = 2k. Option 0 = EXIT (β odd, low, → u). Option 1 = CHAIN (β odd, highest band, → c_(i+1);
  c_(L−1)'s CHAIN goes to TOP).
- TOP: a level-1 self-loop bit (one option: gate with Ξ-target TOP itself, β even). Odd must escape through e(TOP), the highest e, to a
  level-0 sink s → u.
- TAPS: level-1 self-loop bits T_0 … T_(2k−1). T_j's W-target is c_(L−1−j), and its e has rank j among the taps.
- Y (level 0) has options → T_0, T_2, …; X′ has options → T_1, T_3, …. Z (level 1) has one option, the measured gate g: W-target Y,
  Ξ-target X′, and e_g is the lowest level-1 e.
- β order: exit < tap < sink < g < bit < chain.
- Mechanism (READING; the data below is exact). Every play ends u → K0 → K3 → K2 → K1, so Λ = K1 throughout and C = 0.
  - An unchained CHAIN is worse than EXIT (odd, highest β), so the fuse is discovered one mover per step from c_(L−1)
    (BR-SEG / PATH). Tap T_j is «activated» (its play carries e(TOP)) at step j + 1.
  - Y and X′ each follow their best activated tap. By TOP-DEC, g's choice is decided by which side has the higher tap e.
  - The activations alternate sides, so the two face values overtake each other at every step.
- DATA. Unit: steps / σ̄-changes at g. Set: LEAP(k), k ∈ {1, 2, 3, 4, 6, 8, 16, 32, 64}. Scope: IDEAL-CYC and Γ3.
  File: experiments/red/r217/out/verify_leap.txt.

| k | N | T | C | R (R-steps) | R_mov | L | flips at g (= max at one gate) | Γ3 n | N5′-xi iterations n5v xi / n5bxi (= T + 3) | regions = Oink |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 9 | 2 | 0 | 2 | 2 | 0 | 2 | 96 | 5 / 5 | yes |
| 2 | 13 | 5 | 0 | 4 | 4 | 0 | 4 | 156 | 8 / 8 | yes |
| 3 | 17 | 7 | 0 | 6 | 6 | 0 | 6 | 216 | 10 / 10 | yes |
| 4 | 21 | 9 | 0 | 8 | 8 | 0 | 8 | 276 | 12 / 12 | yes |
| 6 | 29 | 13 | 0 | 12 | 12 | 0 | 12 | 396 | 16 / 16 | yes |
| 8 | 37 | 17 | 0 | 16 | 16 | 0 | 16 | 516 | 20 / 20 | yes |
| 16 | 69 | 33 | 0 | 32 | 32 | 0 | 32 | 996 | 36 / 36 | yes |
| 32 | 133 | 65 | 0 | 64 | 64 | 0 | 64 | 1956 | 68 / 68 | yes |
| 64 | 261 | 129 | 0 | 128 | 128 | 0 | 128 | 3876 | 132 / 132 | yes |

- Four routes agree on every row:
  - (1) My own implementation own.py: Γ(G) built from R104's text, its own VJ valuation and order, Odd's optimal counterstrategy by
    one-player strategy iteration, Howard at the movers. No code shared with si.py, idealcyc or gamma3. Its trajectory equals box191
    idealcyc.run state by state.
  - (2) box191 subrun191.labels gives the same C / R / p.
  - (3) My R215 labeller rmov.py (on idealcyc + si.Engine) gives R, R_mov, L and flips.
  - (4) On Γ3(G) (box189 gamma3.build with all pads), Oink 8fbf0a7 --zlk regions = n5v xi regions = n5bxi regions, and harness
    verify.check passes both strategy outputs. N5′-xi spec mode takes 3 iterations; xi takes T + 3.
- Frozen: experiments/red/r217/inst/LEAP_k{1,2,3,4,6,8,16,32,64}.json, plus Γ3 files LEAP_k3_g3.pg and LEAP_k8_g3.pg (sha1 in
  inst/SHA1SUMS; e.g. LEAP_k64.json b09b2745…, LEAP_k8.json 37f0350e…).
- DEAD (pattern, not a conjecture of record): «max flips at one gate stay ≤ 15 / do not grow with width» (R215 §53.2 DATA reading;
  box 192 A7 «per-gate flips stay ≤ 10 in all data»). Instance: LEAP_k64.json, 128 flips at one gate. CONJECTURE OVT-POLY is untouched:
  128 is linear in N.

## 4. Size per overtake (the box's question)
Each extra pair of overtakes (k → k + 1) adds 4 movers (2 fuse movers, 2 tap bits) and 6 options (2·2 fuse + 2 taps) to the genome,
plus 2 options at Y / X′. Constant. Flips at g = (N − 5)/2: super-constant, linear, NOT faster than size.

## 5. Superlinear: what is needed and what failed (READING; two DEAD designs with instances)
- By OVT-DV, a gate flips superlinearly often only if one face's value takes superlinearly many values. That requires a long run.
- In LEAP every value change is a fuse discovery step. Once c_i is chained, a better carrier at the fuse end reaches every chained
  mover in the same step, because valuations are exact for the current strategy. So a fuse yields one wave.
- A second wave needs every c_i to go back to EXIT (a reset: Ω(exit) ▷ Ω(chain)). By F1 that needs the exit target to gain a value
  above the current carrier, timed to the end of the wave. A wave's end can be read only through a play that passes c_0, and a reset
  breaks that play. Two attempts (experiments/red/r217/leapr.py, k 3, W 1-3; files out/leapr_k3_W*_v*.json):
  - v0 (Q_w closes a loop Q_w → c_0 → … → TOP_w → e(TOP_w) → Q_w): Q_w switches to c_0 already at step 1 (its β is even and high).
    When the fuse completes (step 6), the loop makes every self-loop bit's β-face Odd's choice: a C-step with no re-firing. T 7, R 4,
    C 2 for W = 1, 2, 3.
  - v1 (H routes to TOP_w): the cycle closes at step 1. T 1.
  These are design failures, not obstructions. No lemma excludes re-firing.
- Side search (DATA, running): R-scored climbs (r215 rclimb.py, box191 mutation) seeded with LEAP(4) + 10 spare movers (N 31) and
  LEAP(8) + 16 spare (N 53). At 14:50Z: R 15 at N 31 (seed R 8); R 17 at N 53 (seed 16). Unit: R-steps. Scope: IDEAL-CYC.

## 6. Next
1. A self-timed reset: a hub whose value rises above the carrier exactly when c_0 chains, without a play through c_0 after the reset.
   Candidate: read c_0 through an Odd gate (β → c_0), so that the reading play leaves the fuse once Odd takes e.
2. Inspect the climb bests from the LEAP seeds for any re-firing mechanism (ntrace.py).
3. If re-firing works, W rounds would give R ≈ W·2k at size O(k + W), i.e. quadratic R (still polynomial: CYC-COUNT allows
   C ≤ n(2M + 2) rounds).
