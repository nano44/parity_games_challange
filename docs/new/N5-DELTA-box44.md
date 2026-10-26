# Route Δ, step 2: the R20 coarse machinery in set form (box 44)
L-NEW successor 23 (Opus 5.5), D14 / D18, Lead reading L40; Lead's direction (2), 01:05Z (Lead's stamp). Written 2026-10-26 01:14Z-01:31Z
(date -u); §8 refutation and §7b added 01:29Z-01:31Z. Working doc, not a packet, unrefereed. Labels: PROVED (L-NEW 23, unrefereed) / CONJECTURE / OPEN / DATA / READING.
TARGET.md diff: nothing here is a claim of TARGET.md §1. No polynomial bound for N5 is proved, on 𝒞^1O or beyond. G-N5-TIME open.

## 0. Setting
Notation and hypotheses as in docs/new/P-N5-GD-box43.md §0 (D_k, u(v), R_D, F_D, π_v, W_k, (h_D), (h3_D), lev, COARSE_L, M_D,
(HP_D)); the lemmas G_D (a)-(c), F1°_D and Wo_D of that packet are used as stated there. Landed sources ported: R20 = P-N5-XA-box27
§1-§6 with its repairs P-N5-XA-fixes-box28 §1-§3 (FBL replaced, FBF step 1 replaced, XA-3, XA-4, N-XA-1).
- An L-RUN (−1 ≤ L < ∞) is a run S = k_0, …, k_1 of consecutive states inside one phase ((λ, τ) constant) with (h_D) and (h3_D) at
  every state and M_D(k) ≤ L at every state. Nothing else is fixed: D_k, R_D, Ξ(u) and W(u) may change along S.
- A D-STRETCH is an L-run on which D_k = D is constant and Ξ_k(u), W_k(u) are constant for every u ∈ D (the R20 analogue: "τ, θ, w
  constant" becomes "τ constant, D and the terminal values constant"). For u ∈ D, lev_u := lev(Ξ(u), W(u)); u is a TOP TERMINAL of S
  if lev_u = L ≥ 0.
- Coarse facts. For a fixed threshold L, R20 §1's (Cmono) a ⊴ b ⇒ COARSE_L(a) ⪯_L COARSE_L(b), (Cstrict) COARSE_L(a) ≺_L
  COARSE_L(b) ⇒ a ◁ b, and (V1c), (V2c) hold with R20's V* replaced by V_{>L}. R20 proves them for V* = V_{>rank(u*)} by a case split
  on which key decides; the proof never uses which vertex u* is, so it holds for every threshold (READING of the landed proof; for
  L = −1 it is R20's Remark after CR). (Cmono) is R25 (C1); (Cstrict) is its contrapositive (⊴ is total).

## 1. Lemma LAM_D (PROVED, every game)
Under (h_D) ∧ (h3_D) at k: λ_W(v) = λ_Ξ(v) for every v ∈ V. Hence on an L-run, λ_W is constant (it equals λ_Ξ, which is constant on
the phase).
Proof. v ∈ F_D: Ξ_k(v) = W_k(v) (G_D (a)). v ∈ R_D, u := u(v): both plays from v are π_v followed by u's play, whose cycle lies off
π_v (G_D (b)); so λ_Ξ(v) = λ_Ξ(u) and λ_W(v) = λ_W(u), equal by (h3_D). ∎
(R20 §1 "W's cycle-node map is constant on S" is this statement on 𝒞^1O with D = {o}.)

## 2. Lemma C_D (PROVED, every game)
On an L-run S: (i) COARSE_L(Ξ_k(v)) = COARSE_L(W_k(v)) for every v and every k ∈ S; (ii) COARSE_L(Ξ_{k+1}(v)) ⪰_L COARSE_L(Ξ_k(v))
and the same for W, for every transition k → k+1 of S, fallbacks included.
Proof. (i) is G_D (c2) at each state (M_D(k) ≤ L). (ii) R15 (a) gives Ξ_{k+1} ⊵ Ξ_k; apply (Cmono); W follows by (i) at k and k+1. ∎
Port (R20 (a) Lemma C): the one-terminal route form Ξ = π ⊕ θ, W = π ⊕ w on R (RT) is replaced by G_D (b) at each terminal, and the
fixed threshold u* (θ, w constant) by a uniform bound L ≥ M_D(k). No constancy of D, R_D or terminal values is needed.

## 3. Lemma CR_D (PROVED, every game): coarse R17 on an L-run
On an L-run S from k_0, for t ≥ k_0 + n − 1 in S: COARSE_L(W_t) = COARSE_L(W_{k_0+n−1}) (and the same for Ξ, by C_D (i)). So
COARSE_L(Ξ) changes at most at the first n − 1 transitions of S.
Proof. R20 §5 (Lemma P^c, Lemma CR) as repaired (fixes §3), with three substitutions, and nothing else changed:
- Lemma C → Lemma C_D (both halves, at the two ends of each transition of S);
- "W's cycle-node map is constant on S" (R20 §1) → Lemma LAM_D (used in A2, B1 (α), B2 and the final step, λ_t(x) = λ_{k_0}(x));
- case B-fallback: VACUOUS, by N-XA-1 in set form. At an S4c step of S, σ_k is the pointwise optimum of S4a's arena in G_τ (FBL-N (i),
  R18 (d) Lemma S (c)), so by R18 (c) every W-improving gate edge is flat, and a flat edge is coarse-equal (same cycle node x, empty
  path sets on both sides; fixes §3 N-XA-1). In Case B_c, (x, z) is coarse-strict, so W-improving by (Cstrict) (and in Iσ_k by
  (Cstrict) with C_D (i)); hence it cannot exist at a fallback.
Odd vertices x (XA-4): z = τ(x) = x's only G_τ successor, so Case A_c applies with equality. Every other step (A1, A2, B-arena with
(F1) in G_τ, B1 (α)/(β)/(γ), B2) is a statement about one-player valuations in G_τ and uses no route form and no Odd-choice property. ∎
- Port note: R20's CR is signed for throttled stretches (θ, w constant, θ ◁ w). CR_D needs only a uniform coarse threshold. On
  𝒞^1O it reads: on any run of a phase with (h) at every state and lev(θ_k, w_k) ≤ L, COARSE_L freezes after n − 1 transitions;
  R21's (w, u*)-run table already records that CR survives θ-changes.
- Limit (DATA, §7): CR_D is only as strong as L. At the two Δ-RT states found (dch16_n44, k = 28, 30), M_D = 43 = n − 1, so COARSE_L
  keeps only the cycle node, and CR_D says nothing there beyond λ being constant.

## 4. Lemma FBL_D (PROVED, every game): what a fallback's gate contains
Let k → k+1 be an S4c fallback inside one phase. Then:
- (a) (no hypothesis) every gate edge (x, z) with x ∈ F_D is flat for W_k: x = λ_W(x), λ_W(z) = x (P-N5-GD F1°_D step 4).
- (b) under (h_D) at k: no gate edge (x, z) with x ∈ R_D is W-improving. Under (h_D) ∧ (h3_D) at k, such an edge is
  - a LEAVE (z ∈ F_D), or
  - a CROSS-TERMINAL edge (z ∈ R_D, u(z) ≠ u(x)) whose ends are COARSE_{M_D}-equal: COARSE_{M_D}(Ξ_k(z)) = COARSE_{M_D}(Ξ_k(σ_k x)).
  There is no same-terminal R_D → R_D gate edge.
- (c) under (h_D) ∧ (h3_D) at k: if (x, z) is a gate edge with x ∈ F_D and z ∈ R_D, then x = c_u := λ_W(u) for u := u(z), and u has lev_u ≤ −1 (P(Ξ(u)) = P(W(u))
  = ∅). So if lev_u ≥ 0 for every u ∈ D_k, there is no F_D → R_D gate edge.
Proof.
- (a) is F1°_D step 4 (it uses no (h_D), and no crossing-freeness before its last sentence).
- (b) σ_k is the arena optimum (as in §3), so a W-improving gate edge is flat (R18 (c)) and needs x = λ_W(x). For x ∈ R_D (x is Even,
  so x ∉ D_k and u(x) ≠ x), x's W-play is π_x followed by u(x)'s W-play, which avoids π_x (G_D (b)); so x is not on its own cycle, a
  contradiction. Now let the edge be Ξ-improving and not W-improving. If z ∈ R_D with u(z) = u(x) = u(σ_k x), G_D (c1) (both routes end
  at the same terminal) makes it W-improving: excluded. If the coarse values differed, they would differ in Ξ's favour of z ((Cmono)
  on Ξ_k(z) ▷ Ξ_k(σ_k x)), hence in W's (G_D (c2) at L = M_D; if M_D = ⊥, Ξ_k = W_k everywhere and the edge is W-improving), and (Cstrict) would make it W-improving: excluded.
- (c) (R20 FBL as repaired, fixes §1 step 3, per terminal.) By (a) the edge is flat: x = λ_W(x) and λ_W(z) = x. z's W-play is π_z,
  then u's W-play, so λ_W(z) = λ_W(u) = x, and by (h3_D) λ_Ξ(u) = x. Flatness gives P(W_k(z)) = ∅ (R17 B2: the cycle x → z → … → x
  has no vertex more relevant than x), and P(W_k(z)) = A_z ∪ P(W(u)) (G_D (b)), so A_z = P(W(u)) = ∅. The edge is a gate edge:
  Ξ_k(z) = (x, P(Ξ(u)), ·) ▷ Ξ_k(σ_k x) = W_k(σ_k x) = (x, ∅, ·) (σ_k x ∈ F_D; G_D (a)). So P(Ξ(u)) = ∅ or its top is even. An even
  top would give Ξ(u) ▷ W(u) (P(W(u)) = ∅), against XW. So P(Ξ(u)) = P(W(u)) = ∅: lev_u ≤ −1. ∎
On 𝒞^1O with D = {o}: (b) is R20's "no R → R gate edge" (one terminal, so no cross-terminal edge), (c) is R20's repaired F → R case
(u* ≠ none ⇔ lev_o ≥ 0). CROSS-TERMINAL edges are new: they are the fallback face of Δ-RT.

## 5. Lemma FBF_D (PROVED, every game, under the hypothesis CT-FREE)
Let S be a D-stretch, and let L → L+1 be an S4c fallback in S whose gate at L has no cross-terminal edge (CT-FREE at L). No
hypothesis on lev_u (as R20's FBF, which holds for every u*). Then for every state t ≥ L+1 of S: R_t ⊆ R_{L+1}, every v ∈ R_t has its L-path (hence its L-terminal and its
L-values, Ξ_t(v) = Ξ_L(v)); no vertex enters R_D after L inside S.
Proof (fixes §2, per terminal).
0. For u ∈ D, c_u := λ_W(u) ∉ R_D at every state of S: c_u lies on u's W-play after u; if c_u ∈ R_D, u's W-play would reach D again
   after leaving u, against (h_D).
1. At L, by FBL_D (b) and CT-FREE, R_D-sourced gate edges are leaves; by FBL_D (c)'s first part (no lev hypothesis), an F_D → R_D
   gate edge (x, z) starts at x = c_{u(z)}. Let v ∈ R_{L+1} with (L+1)-path p_0, …, p_m ∈ D, and let p_i be the largest switched
   vertex on it (fixes §2 step 1). Then p_{i+1} ∈ R_L ∪ D, so p_i switched along a gate edge into R_L ∪ D; p_i is Even (τ is
   fixed), so p_i = c_{u′} for some u′ ∈ D. But p_i ∈ R_{L+1}, against step 0 at L+1 (c_{u′} = λ_W(u′) is the same at L and L+1: LAM_D
   and the phase). So no p_i switched, and R_{L+1} ⊆ R_L with unchanged paths.
2. Best-key fact (fixes §2 step 2): verbatim (it is about S4c's choice only).
3. Induction (fixes §2 step 3): for z ∈ R_t with its L-path, Ξ_t(z) = π_z ⊕ Ξ(u(z)) = Ξ_L(z) (G_D (b) at t; the terminal values are
   constant on S). For every Even y, Ξ_t(σ_t y) ⊵ Ξ_L(z) as in fixes §2 step 3 (R15 (a) and step 2). So no gate edge at t points into
   R_t; S4a and S4c switch only gate edges, and the largest-switched-vertex argument gives R_{t+1} ⊆ R_t with unchanged paths. ∎
- Without CT-FREE: OPEN, and the hypothesis is not vacuous. A cross-terminal gate edge (x, z) at a fallback is coarse-flat and can be
  S4c's best Ξ-key choice (rtf_cex_inj.pg, §8); switching it moves x into z's route region with a W-loss, and the R20 induction has
  no base.

## 6. Theorem XA_D (PROVED, every game; same top terminal only)
Let S be a D-stretch with threshold L ≥ 0. Let x leave R_D at an S4a step L′ → L′+1 and next re-enter at E > L′, with L′, …, E+1 in
S, and u(x) = u at L′ and at E+1, where u is a top terminal (lev_u = L). Then COARSE_L(Ξ_{E+1}(x)) ≻_L COARSE_L(Ξ_{L′}(x)).
Proof (R20 §6 with u for o).
1. W_{L′+1}(x) ⊵ W_{L′}(x): σ_{L′} is a strategy of its own S4a arena, so (F1) in G_τ gives W_{L′+1} ⊵ W_{L′} pointwise (this is
   R20's Lemma W; τ is fixed).
2. x ∈ F_D at L′+1: W_{L′+1}(x) = Ξ_{L′+1}(x) (G_D (a)). x ∈ R_D at L′: W_{L′}(x) = π^{L′} ⊕ W(u) (G_D (b)).
3. R15 (a): Ξ_{E+1}(x) ⊵ Ξ_{L′+1}(x); x ∈ R_D at E+1 with terminal u: Ξ_{E+1}(x) = π^{E+1} ⊕ Ξ(u). So π^{E+1} ⊕ Ξ(u) ⊵ π^{L′} ⊕ W(u).
4. Let u*_u := the most relevant vertex of P(Ξ(u)) Δ P(W(u)) (rank L, since lev_u = L ≥ 0). By XW, Ξ(u) ◁ W(u), decided at u*_u in
   W(u)'s favour. u*_u lies on u's honest or W-play, so on no route π (G_D (b)); u ∉ P(Ξ(u)) Δ P(W(u)) (u is on both plays). Suppose
   the two values of step 3 had equal COARSE_L parts. Both have cycle node c := λ(u) ((h3_D)), so their path-set symmetric difference
   lies in V_{≤L}, contains u*_u (rank L), and its top is u*_u, where W(u)'s side is better: π^{L′} ⊕ W(u) ▷ π^{E+1} ⊕ Ξ(u), against
   step 3.
5. So the coarse parts differ, and by (Cmono) on step 3: COARSE_L(Ξ_{E+1}(x)) ≻_L COARSE_L(π^{L′} ⊕ W(u)) = COARSE_L(W_{L′}(x)) =
   COARSE_L(Ξ_{L′}(x)) (C_D (i)). ∎
Count: for one x the intervals (L′, E+1] are disjoint and each holds a strict coarse increase of x; by CR_D all coarse increases lie in
the first n − 1 transitions of S. So such re-entries number ≤ n − 1 per vertex and ≤ n(n − 1) per D-stretch.
- OPEN (Δ-RT): re-entries to a different terminal, or to a terminal with lev_u < L. Step 4 needs the full-value difference's top to be
  a vertex where W is better; with two terminals, or with lev_u < L, a route difference in ranks (lev_u, L] can decide either way.

## 7. Single-terminal stretches (PROVED by port, every game)
If S is a D-stretch with D = {u} (one disagreement vertex; other Odd choice vertices may exist, agreeing with σ̄ at every state of S),
then R_D's routes all end at u, there is no cross-terminal edge, and R20 (a)-(e) hold on S verbatim with o := u, θ := Ξ(u), w := W(u),
u* := u*_u: C (§2), FBL for u* ≠ none (§4 (b), (c)), FBF for every u* (§5; CT-FREE holds automatically with one terminal), CR (§3), XA
(§6; with one terminal, a top terminal is u itself whenever L = lev_u ≥ 0). The proof is the substitution table of P-N5-GD §2 plus
§1-§6 here.

### 7b. Lemma PIECE_D (PROVED by port, every game; |D| = 1)
Let a run k_0 → … → k_1 lie in one phase with D_k = {u}, W(u) constant, R_D constant, (h_D) ∧ (h3_D) at every state, and no S4c
fallback. Then it has at most (|R_D| − 1) + (|F_D| − 1) transitions at which some Ξ_k(v) or W_k(v) changes, counted as in R21 (i)
(W on R_D, so Ξ(u) may vary).
Proof: P-N5-RE §5 (R19 (f)) steps 1-5 with o := u, read in G_τ:
- step 1 (closure): every vertex of π_v reaches u, so lies in R_D; F_D-plays avoid D (definition);
- step 2: the route game 𝓡 on R_D ∪ K (K := u's W-continuation, a path in F_D by (h_D)); its Odd vertices other than u keep τ (in
  𝒞^1O they were "forced"; here they are fixed by G_τ, with σ̄ = τ there by (HP_D)); W_k|R_D is 𝓡's valuation by G_D (b); 𝓕 := G_τ[F_D]
  as in F1°_D;
- step 3 (gates): G_D (c1) (one terminal) for R_D, G_D (a) for F_D;
- steps 4-5 verbatim (S4a arena optimum against τ; (F1); R17 Theorem PH from any start; 𝓡 has one λ-phase since every play ends at
  the terminal; 𝓕's cycle nodes are λ_Ξ's).
The R21 (i) reading (θ free) carries over: a change of Ξ(u) at a transition with R_D constant changes W on F_D or nothing (READING of
R21 (i)'s proof, X-1 / Lemma TF, with u for o; not re-derived here). ∎
READING: R21-R24's remaining one-Odd uses (per the ledger: FO steps inside proofs, e.g. NF, OE, TC-SPLIT) are not checked for |D| = 1.

## 8. Δ-RT, sharpened (OPEN), and one refuted conjecture
What blocks every multi-terminal port is the CROSS-TERMINAL DISAGREEMENT, in two directions, at a state with (h_D) ∧ (h3_D):
- FORWARD: an edge (x, z) inside R_D with u(σ_k x) ≠ u(z), Ξ-improving but not W-improving. It is in Iσ_k and in S4a's arena;
  S4a (a W-optimum) does not take it, but S4c (best Ξ-key) can, with a W-loss at x. By G_D (c2) and (Cstrict) its ends agree above
  M_D (FBL_D (b)).
- REVERSE: an edge (x, z) inside R_D, cross-terminal, W-improving but NOT in Iσ_k. S4a's arena then lacks a W-improving edge of the
  route game, so S4a is not R17's switch-best step on R_D and Lemma P's Case B has no arena edge to use. This is what blocks a
  multi-terminal PIECE (§7b needs |D| = 1 exactly for this).
Both are excluded for same-terminal pairs by G_D (c1); RTREV1 = 0 in all data (§9) is that check.
- (Δ-RT-F) "no cross-terminal edge is switched at a fallback inside a phase": **FALSE** (DATA, refuted).
  Instance experiments/new/box44/instances/rtf_cex_inj.pg (n 11, injective priorities, sha1 9b55eee6b55df9328018fdb0a70ec974d302bd47;
  rank-equivalent to rtf_cex.pg, sha1 2203e77f…, tied priorities, the shrinker's output; found by rtclimb.py seed 13 then shrinksw.py).
  N5 from the S3 start: 4 iterations, 2 fallbacks. At k = 1 → 2 (an S4c fallback, λ and τ unchanged): D_1 = {0, 1}, (h_D) and (h3_D)
  hold, M_D = 10 = n − 1. S4c switches Even 3 from 5 (terminal u(5) = 1) to 10 (terminal u(10) = 0):
  Ξ_1(10) = (6, {4}, 4) ▷ Ξ_1(5) = (6, ∅, 3) (vertex 4 even, rank 9), but W_1(10) = (6, {4}, 4) ◁ W_1(5) = (6, {8}, 4) (vertex 8
  even, rank 10). So W drops at 3 at this fallback. A second one at k = 2 → 3: Even 5 switches from 1 (terminal 1) to 3 (terminal 0).
  Checks: n5x.trace equals n5.py's counts (asserted); n5.py's output passes Oink `verify` (8fbf0a7) and experiments/harness/verify.py,
  and its winning regions equal Oink `--zlk`'s (both files).
  Obstruction: S4c chooses by the honest key; with two terminals whose gaps (Ξ(u), W(u)) differ below M_D, the honest key and the
  W-key order the two routes differently. Consequence: FBF_D's CT-FREE hypothesis is needed, and a multi-terminal FBF has no
  "fallbacks only evict" base.
- (Δ-RT-C) CONJECTURE (still open): inside a D-stretch, the transitions with a cross-terminal disagreement (either direction) number
  ≤ poly(n). DATA: largest climbed (experiments/new/box44/instances/rtdis_k4_n24.pg, n 24, k = 4 Odd choice vertices, sha1 00529ed5…; N5 output verified as for
  rtf_cex_inj): 12 states with a reverse
  disagreement, 6 with a forward one, 10 cross-terminal fallback switches, over the whole run (not per stretch).
- (Δ-RT-W) the weighting idea of the previous version (a potential monotone at fallbacks "if Δ-RT-F holds") is void with Δ-RT-F false.
  What remains (PROVED pieces, READING as a route): S4a steps never lower W (R20's Lemma W, (F1)), so W drops only at fallback
  transitions; there, F_D-sourced switches are W-flat (FBL_D (a)) and every R_D-sourced switch (a leave or a cross-terminal edge) is
  W-non-improving (FBL_D (b)), so both kinds can lower W. A W-potential argument therefore needs a frontier bound on fallbacks per
  phase (R48 FB-POLY is 𝒞^1O-only; ledger verdict FI) times a bound on the loss per fallback; cross-terminal switches are not the
  only W-losses. (Correction 01:36Z of my 01:35Z message to the Lead, which said they were.)

## 9. Data (DATA, not proof): experiments/new/box44/crd.py, rtdump.py, fbldump.py, rtclimb.py, shrinksw.py
crd.py checks LAM_D, CR_D (per maximal (h_D) ∧ (h3_D) run of a phase, L := max(−1, max M_D); latest coarse change index ≤ n − 2),
C_D (ii) (COARSE_L(Ξ) never decreases), FBL_D (b) (R_D-sourced gate edges at fallbacks with (h_D): never W-improving; with (h3_D) also,
never same-terminal; LEAVE, NOH3 (no (h3_D): no claim), cross-terminal DIFF and DIFFSW (switched by S4c) counted; DIFF must be
coarse-equal), FBL_D (c) / FBF base (switched F_D → R_D edges at fallbacks with (h_D) at both ends), and at states with
(h_D) ∧ (h3_D): forward (RTDIS, |D| ≥ 2) and reverse (RTREV, |D| ≥ 2; RTREV1 at |D| ≤ 1, must be 0) disagreements. Canonical S3
start only. A first version of the FBL_D (b) check counted same-terminal edges also at states without (h3_D) and reported false
"violations" on two climbed games; the statement needs (h3_D), the check was corrected, and the table is from the corrected script.
| sample | runs | trans. | LAM_D states / viol. | CR_D runs (> n) / viol. | C_D (ii) checks / viol. | fallback R_D gate edges (h_D): LEAVE / NOH3 / same-term. viol. / DIFF / DIFFSW | F_D→R_D switches / viol. | states |D| ≥ 2 / RTDIS (states) / RTREV (states) / RTREV1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `--list ../box41/lib41.txt` | 412 | 8,477 | 6,310 / 0 | 879 (58) / 0 | 204,735 / 0 | 1,730 / 0 / 0 / 0 / 0 | 25 / 0 | 77 / 0 (0) / 3 (3) / 0 |
| `--rand 2000 5 14 31` | 2,000 | 2,480 | 2,912 / 0 | 2,688 (0) / 0 | 2,359 / 0 | 0 / 0 / 0 / 0 / 0 | 46 / 0 | 18 / 0 (0) / 0 (0) / 0 |
| `--rand 1000 10 24 32` | 1,000 | 1,831 | 1,910 / 0 | 1,648 (0) / 0 | 4,737 / 0 | 2 / 0 / 0 / 0 / 0 | 45 / 0 | 40 / 1 (1) / 4 (3) / 0 |
| `--rand 3000 8 20 41` | 3,000 | 4,966 | 5,277 / 0 | 4,683 (0) / 0 | 9,030 / 0 | 0 / 0 / 0 / 0 / 0 | 108 / 0 | 85 / 0 (0) / 0 (0) / 0 |
| `--rand 1500 15 30 42` | 1,500 | 3,337 | 3,325 / 0 | 2,764 (0) / 0 | 13,341 / 0 | 0 / 0 / 0 / 0 / 0 | 76 / 0 | 112 / 3 (3) / 0 (0) / 0 |
| `../box43/instances/*.pg` | 5 | 87 | 39 / 0 | 20 (0) / 0 | 736 / 0 | 2 / 0 / 0 / 0 / 0 | 0 / 0 | 8 / 5 (2) / 2 (1) / 0 |
| `instances/rtf_cex_inj.pg` | 1 | 4 | 4 / 0 | 2 (0) / 0 | 22 / 0 | 0 / 0 / 0 / 2 / **2** | 0 / 0 | 4 / 2 (2) / 2 (2) / 0 |
| `instances/rtdis_k4_n24.pg` (climbed, rtclimb.py 4 24 20000 12) | 1 | — | — | — | — | 15 / 0 / 0 / 80 / **10** | 0 / 0 | 13 / 287 (6) / 104 (12) / 0 |
Reading of the data (DATA):
- 0 violations of every PROVED statement (LAM_D, CR_D, C_D (ii), FBL_D (b), (c)). CR_D is non-vacuous only on lib41 (58 runs longer
  than n; latest coarse change at index 54, ≤ n − 2 in each run). Random runs are short (latest change index ≤ 3).
- Random sampling never found a cross-terminal fallback switch (DIFFSW 0 in 7,912 runs); climbs scored on (DIFF, RTDIS, ST2) found
  them at once (seeds 11-14: DIFFSW 3-10 per game), and the shrinker reduced one to n 11.
- Forward disagreements at S4a states: rtdump.py on dch16_n44 (k = 28, 30, D = {9, 23}, M_D = 43 = n − 1; e.g. edge (38, 9), u(σ 38) =
  23, u(9) = 9, coarse-equal; S4a switched 38 to 29, a W-better arena edge).
- Thin: every multi-terminal statement rests on short phases (random) or on climbed games; no long frontier phase is in the data.
Runs 2026-10-26 01:13Z-01:30Z (date -u), from experiments/new/box44; Oink built at 8fbf0a7 by scripts/setup_oink.sh at ~01:27Z.
