# R-N5-HON: REFEREE report on packet P-N5-HON (L-NEW box 46: Lemma HON, W-honest states per phase ≤ f + 4n² − 3n, with SAT0, HON-FB, HON′, HON-0; RESTRICT_u, REPRO_u; EP-1u and REC-1; every game)
Referee: REFEREE (successor 14, session_011gcqhgkUNYoFY7xCryrLff), Opus 5.5 (owner ruling D15). FIRST referee (Lead brief). Context at writing: about 300k tokens.
- Routing: the Lead's GO of 10:42Z (Lead's stamp), after the successor-14 handover check (fe90edbf, Lead 5/5).
- Object: docs/new/P-N5-HON-box46.md, sha1 07f8e767cfca12d29c8f6f2e3f03358326abbef1 (checked on the tree, with `git show 67a7b54d:… | sha1sum`
  (l-new freeze) and `git show 31835c4b:… | sha1sum` (trunk pin); identical), 211 lines. Author: L-NEW successor 25.
- Written 2026-10-26T10:45Z-11:08Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: trunk has docs/referee-2/R2-N5-HON.md and docs/referee-2/R2-N5-HON/ (`git ls-tree` on
  origin/claude/vibrant-johnson-nxvvxo); neither is on my tree and neither was opened before this report was pushed (re-listed in the same
  turns as each fetch). No lane code run
  (experiments/new/box46/*.py not executed or imported). D1.
- Premises read against their text: SPEC S1-S5 (docs/new/N5-ssi-global.md l. 24-60: S4 "both steps computed from the SAME (σ, τ)", S4c fires
  iff σ_new = σ and τ_new = τ, Even switch-all to the (Ξσ(w), w)-maximum, ties to the larger index; FIX 3 l. 88); RESULTS R15 (a), (d)
  (l. 637-647; Ωτ depends on τ alone); R17 (a)-(d) (l. 730-777) and the proof text docs/new/N5-phase-bound-box10.md §1-§3 (Lemma P cases
  A1, A2, B1, B2; Theorem PH's case split); R18 (d) Lemma S (a), (c) (l. 803-807, S (c) for S4a outputs only, G-1OA-6); R21 (a) XW;
  R23 (g) WM (l. 1041), game-general by RESULTS l. 3169 (XEP-N2); R64 (a)-(e) (l. 3206-3260) and the proof text docs/new/P-N5-EPR-box45.md
  §1-§2; R51 (a) (T*, 𝒞^1O := exactly one Odd vertex of out-degree > 1); P-N5-REC0-box45.md (sha1 343239b5…, re-measured) §0-§1; my lane's
  R-N5-REC0.md (Q-R17 answer).
- Tools: scratch/hon_probe.py (own engine rl_engine = SPEC from the text; epr_probe's gates / s4a / s4b_arena / wval / n5tau_step by REFEREE
  succ. 12): per phase every HON step (LEV exact by simple-path enumeration in G_τ for n ≤ LEVMAX), HON-FB (i)-(iv), HON′, HON-0, REC-1 (a)
  in its proof form, RESTRICT_u (i)-(iv) for every u with D_k ⊆ {u}, REPRO_u with N5^τ on G^u; controls MUT=1 (G^u cut at u as well),
  MUT=3 (STEP1 asks for a rise of 2), IMM / IMM′ and FB1 / FB2 controls. scratch/hon_climb.py (hill climb, every candidate fully checked).
  Logs scratch/hon_logs/.

## Verdicts
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | Lemma HON: W-honest states per phase ≤ f + 4n² − 3n, every game | SIGNED |
| §2 | Lemma SAT0 | SIGNED |
| §2 | Lemma HON-FB (i)-(iv) | SIGNED |
| §2 | Corollary HON′ (f → f_in) | SIGNED |
| §2 | Corollary HON-0 (a)-(c) | SIGNED |
| §2 | "HON-0 implies the signed REC-0" (inequality and corollary) | CHECKED: TRUE (strictly; difference f·n + 2) |
| §2 | "the proofs are independent" | CHECKED: TRUE in the sense "neither proof uses the other, nor SN-PREFIX_D or EP-0"; the premise sets overlap (note HON-N1) |
| §3 | Lemma RESTRICT_u, Corollary REPRO_u | SIGNED |
| §3 | Corollary EP-1u | SIGNED as an IMPLICATION from (Στ) |
| §4 | Theorem REC-1 (a) | SIGNED |
| §4 | Theorem REC-1 (b)-(d) | SIGNED as IMPLICATIONS from (Στ) |
| Q-R17 | in HON's own use, is R17 (b)'s step used only through the listed items? | YES (§5 below; three uses, each listed) |
| §5, §6 | CONJECTURE HON-FF, dead routes, data | not signed (as briefed); DEAD instances re-run (§6) |
No gap. Notes HON-N1..N4 (wording / citation). With RESULTS R65 ((Στ) at audit strength) EP-1u and REC-1 (b)-(d) hold at that same
strength; they are signed here as the packet states them (implications). HON is a count of one kind of state and REC-1 a reduction: no
running-time bound; not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. Lemma HON, step by step
- Setting ✓. A W-honest state has Ξ_k = W_k, so λ_W = λ and (S2 read from Ξ_k) Iσ_k = the W_k-improving Even edges of G_τ; S4a's arena
  (Even v: {σ_k(v)} ∪ Iσ_k(v), Odd v: τ(v)) is then R17's switch-best arena H_k of the one-player game G_τ. D = ∅ ⇒ σ̄_k = τ ⇒ W-honest ✓.
  LEV(k) is read from Ξ_k (not W_k); paths and cycle nodes of λ are fixed on P (G_τ fixed, λ fixed). LEV ≥ 0 since Ξ_k(c) = (c, ∅, 0) for
  λ(c) = c ✓.
- Step 0 ✓: R15 (a) with (d) (every iteration is Switch_I on σ with I ⊆ Iσ, or leaves σ and so Ξ unchanged) gives Ξ_{k+1} ⊵ Ξ_k.
- Step 1 ✓. (a) WM at every transition of the gap (all in-phase, none a fallback). (b) Sandwich: W_h ⊴ W_{h+1} ⊴ W_{h′} pointwise, both ends
  with cycle node λ(v) (honest, in P); the order compares the cycle node's reward first and rewards are injective (SPEC: p′ = 2·rank + parity,
  rank injective), so W_{h+1}(v) has cycle node λ(v): no W-cycle-node change h → h + 1. NOTE: honesty of h + 1 is NOT needed; this is how HON
  gets Lemma P's "phase still holds at k + 1" without REC-0's all-unsplit hypothesis at k + 1 (it pays with WM along the whole gap and
  honesty at h′). (c) The Lemma P step at h → h + 1 (§5 below for the item list): hypothesis "W_h ⪰ value(r′), |r′| ≤ LEV(h)" (W_h = Ξ_h);
  conclusion for |r| ≤ LEV(h) + 1. The step uses k only as the path-length bound, never as a step count, so j := LEV(h) in place of k is
  legitimate ✓. (d) Ξ_{h′} = W_{h′} ⊵ W_{h+1} (WM along the rest of the gap) ✓.
- Step 2 ✓. At an honest h the (σ_h, τ)-play from x follows a simple path r_x of G_τ (Odd vertices at τ, Even at σ_h: edges of G_τ) to its
  first visit of λ_W(x) = λ(x), and VJ00's valuation of the play is exactly value(r_x) = (c, P(r_x), |r_x|); so Ξ_h ⊴ B, and LEV = n − 1
  gives Ξ_h ⊵ B ✓ (order total).
- Step 3 ✓. Saturation persists (step 0, B fixed on P). Gaps between consecutive unsaturated honest states are disjoint transition sets: ≤ f
  contain a fallback; each fallback-free one raises LEV by ≥ 1 (LEV(h_i) ≤ n − 2 there), LEV never falls, 0 ≤ LEV(h_1), LEV(h_s) ≤ n − 2: ≤ n − 2
  such gaps; s − 1 ≤ f + n − 2. Saturated honest states: Ξ_{h_i} = B for i > s, so Ξ is constant on [t, h_N] (monotone, equal ends) and Ωτ is
  constant (τ fixed on P, Ωτ a function of τ, R15 (d)); R15 (d) bounds the h_N − t consecutive iterations by 4n(n − 1); the saturated honest
  states are distinct states of [t, h_N]: N − s ≤ 4n(n − 1) + 1. Sum (f + n − 1) + 4n(n − 1) + 1 = f + 4n² − 3n ✓ (s = 0 and s = N included).

## 2. SAT0, HON-FB, HON′, HON-0
- SAT0 ✓. Even x: R17's A1/A2 inequalities at the same state (A1: value(r) = x ⊕ value(r′) ⪯ x ⊕ W(σ(x)) = W(x) by (V1)/(V2); A2: cycle-node
  comparison), WITHOUT A1's final (F2) link, which is the only part of Case A that refers to a later strategy: the packet's "uses only this
  inequality, the induction hypothesis, (V1) and (V2)" is exact. Odd x (z = τ(x)): not its own W-cycle node ⇒ (V1) and z's play avoids x
  (true also when x lies on its cycle but is not its top: the arc from z to the top avoids x) ✓; own W-cycle node ⇒ W(z) has cycle node x and
  ⪰ value(r′) with cycle node c ≠ x forces reward(x) > reward(c) ✓. Last line: honest ⇒ W-cycle nodes = λ's and W = Ξ ⇒ LEV = n − 1 ✓.
- HON-FB ✓.
  - Premise: in-phase ⇒ τ_{h+1} = τ ⇒ the fallback is Even's (an Odd fallback switches τ on a non-empty Iτ: τ changes) ⇒ Iσ_h ≠ ∅ and S4a
    returned σ_h (S4c fires iff σ_new = σ and τ_new = τ) ⇒ σ_h is a pointwise optimum of S4a's arena (S (c): it IS S4a's output) ✓.
  - (i): I re-derived the case list independently before reading box 10's (ρ̂ := σ_h[x → z], W_h(x) ⪰ W_ρ̂(x)): x off π and off c's cycle:
    W_ρ̂(x) = x ⊕ W_h(z) ≻ W_h(x) (strict (V2), or a better cycle node c ≻ x when x is its own cycle node — c ≠ x because z's play avoids x);
    x on c's cycle, x ≠ c (B1, second sub-case): P(π) has an even top above c ⇒ top(Z) even and above c ⇒ better cycle node; P(π) = ∅ ⇒
    top(Z) = c and W_ρ̂(x) = x ⊕ W_h(z) ≻ x ⊕ W_h(σ_h(x)) = W_h(x); x ∈ π, x ≠ c (B2): D ≠ ∅ with even top ⇒ better cycle node; D = ∅ ⇒ c odd,
    top(Z) less relevant than c ⇒ better reward; x = c: P(π) ≠ ∅ with even top ⇒ better cycle node, P(π) = ∅ ⇒ W_ρ̂(x) = (x, ∅, 0) = W_h(x):
    flat. Only flat survives ✓ (same list as box 10 §3 with "the phase ends" replaced by "contradicts W_h(x) ⪰ W_ρ̂(x)").
  - (ii) ✓: S4c's targets are the (Ξ_h(w), w)-maxima of Iσ_h(x) = W-improving edges (honest); each switched x is its own cycle node and
    z*'s W-play reaches x through vertices below x; a σ_h-play that reaches a cycle node x′ stays on x′'s cycle, so z*'s path to x avoids every
    other switched x′, and every play's path to its first visit of its cycle node is unchanged: W_{h+1} = W_h.
  - (iii) ✓ (a new improving w at a switched x would be in Iσ_h(x) with a larger Ξ_h = W_h value than z*).
  - (iv) ✓: Ξ_h ⊴ Ξ_{h+1} (R15 (a): the fallback is Switch_I, I ⊆ Iσ) ⊴ W_{h+1} (XW) = W_h = Ξ_h; honest + no W-improving edge ⇒ saturated
    (SAT0); at h + 1, Iσ = ∅ ⇒ S4a returns σ; S4b moves τ, or S4c falls back for Odd (Iσ = ∅) and moves τ, or N5 stops (Iτ = ∅): last state.
- HON′ ✓. A gap (h_i, h_{i+1}), i < s, with its fallback at h_i would make h_{i+1} = h_i + 1 saturated (HON-FB (iv); no honest state lies
  strictly inside the gap), contradicting i + 1 ≤ s; so every fallback of such a gap is at a non-honest state strictly inside it, i.e. counted
  by f_in, and distinct gaps get distinct fallbacks.
- HON-0 ✓ (D = ∅ states are honest; a D_E = ∅ epoch is a non-empty set of D = ∅ states, epochs disjoint; one source per transition).
- Relation to REC-0 ✓ (definitions identical: P-N5-REC0 §0 has the same phase, f, epoch, D_E, N_0). Arithmetic re-done:
  (f + 1)(n + 1) + 4n(n − 1) + 1 − (f + 4n² − 3n) = f·n + 2 > 0, and f_in ≤ f; HON-0 (c) ≤ HON-0's bound ≤ REC-0's bound ≤ REC-0's bound ×
  (n + m). So HON-0 implies REC-0 and its corollary, strictly.
- Independence ✓, checked by script (scratch/hon_logs/independence.txt): the citations in HON §1-§2's proofs (everything before "Relation to
  Lemma REC-0") are (F1), (V1), (V2), Lemma P cases A1/A2/B1/B2, Theorem PH, FIX 3, R15 (a), R15 (d), R18 (d) S (c), WM, XW, Q-R17 and HON's
  own lemmas; "REC-0" occurs only in the §2 heading; SN-PREFIX_D and EP-0 do not occur. REC-0's proof cites neither HON nor XW by name. So
  neither proof uses the other. Note HON-N1 on the packet's sentence "HON-FB adds XW".

## 3. RESTRICT_u, REPRO_u, EP-1u
- RESTRICT_u ✓. I re-read R64 (a)'s proof (P-N5-EPR §1): the epoch enters only in (i), through "σ̄_E is an Odd strategy of G′_E and
  σ̄_k = σ̄_E", used in Lemma S (a) on the restricted game. With D_k ⊆ {u}, σ̄_k is an Odd strategy of G^u (Q ∖ {u} at τ, u keeps all its
  edges). (ii) needs only that S4a's arena is the same game (Even edges and τ unchanged) ✓; (iii) that S1 on G^d for τ sees the same graph
  (Odd at τ, Even with all edges) ✓; (iv) that G^u's S4b arena is a sub-arena of G's that contains τ (Iτ′ ⊆ Iτ by (iii)) ✓. The order's
  antisymmetry step in (i) uses injective rewards (SPEC) ✓. G^u ⊋ G′_E for D_E = {u}, so RESTRICT_u contains RESTRICT_E for those epochs
  and also covers D = ∅ states (for every u ∈ Q at once).
- REPRO_u ✓. R64 (b)'s induction uses RESTRICT at each source k ∈ [x, y′ − 1]; here [x, y′ − 1] ⊆ J because y′ − 1 ≤ y. The one-phase claim
  is stated for x, …, y only, with the exit transition allowed to leave: the EPR-1 repair is built in ✓ (my data: exits leaving the
  N5^τ phase occur, §6).
- EP-1u ✓ as an implication: same form as R64 (e). G^u ∈ 𝒞^1O (exactly one Odd vertex of out-degree > 1) with d_o = deg(u); (Στ) is stated
  for every 𝒞^1O game and every start pair, so it covers the run of N5^τ on G^u from (σ_x, τ); the len(J) − [y → y + 1 in-phase] transitions
  with source in [x, y − 1] are in-phase transitions of that N5^τ phase, so len(J) ≤ T*(G^u) + 1. T* is R51 (a)'s per-phase bound (R50 (h)
  with f := 2n²), polynomial in (n, m, Δ, d_o) ✓. The size line O(m·Δ·d_o·n¹¹) is labelled a reading; it is consistent with R51 (a)'s
  (n(n − 1) + d_o)(T* + 1) = O(m·Δ·d_o·n¹³); not signed.

## 4. Theorem REC-1
- (a) ✓ (no (Στ)). A {u}-interval not starting at P's first state starts at k + 1 with k → k + 1 in-phase and D_k ≠ {u} (maximality); the
  map interval ↦ k is injective; D_k = ∅ ⇒ k is a D = ∅ state (HON-0 (a) bounds them); |D_k| = 1 ⇒ X_dir; |D_k| ≥ 2 ⇒ X_big. Plus one at P's
  first state.
- (b) ✓ as an implication: a {u}-interval lies in one u-run (D = {u} ⊆ {u}); every state of I but P's last is a source with source in J;
  |I| ≤ len(J) + 1 ≤ T*(G^u) + 2.
- (c), (d) ✓ as implications (each |D| = 1 state lies in exactly one {u}-interval; epochs disjoint and non-empty; with no |D| ≥ 2 state,
  states = D = ∅ states + |D| = 1 states and X_big = 0).

## 5. Q-R17 in HON's own use (answer YES)
HON uses R17 three ways; in each, nothing beyond the listed items enters.
1. §1 step 1 (the full induction step at h → h + 1): (1) the hypothesis at k = W_h ⪰ value(r′), |r′| ≤ LEV(h) (from W_h = Ξ_h); (2) I_k read from
   Ω_k = W_h (honest at h, so S2's Iσ_h is W_h's improving set; nothing is required of h + 1's honesty); (3) ρ_{k+1} = σ_{h+1} an optimum of
   H_k (S (c); h → h + 1 is not a fallback), giving (F1) for ρ̂ in B1/B2 and (F2) W_{h+1} ⪰ W_h in A1 and B2's last line; (4) (V1)/(V2);
   (5) u a cycle node of λ_W(h) = λ; (6) no W-cycle-node change h → h + 1, from the sandwich (§1 step 1 (b)), used where B1/B2 conclude "the
   phase ended at step k + 1"; (7) G_τ one-player. Same list as my REC-0 answer (R-N5-REC0 §2), with (2) at a W-honest state and (6) obtained
   from the sandwich instead of all-unsplit at k + 1.
2. SAT0: Case A (A1, A2) at a single state, without (F2): only the non-improvement inequality, the induction hypothesis on r′, (V1), (V2).
3. HON-FB (i): Theorem PH's case split / B1-B2 outcome analysis with (F1) at the same strategy (σ_h is the optimum), "phase ends" replaced
   by "contradicts W_h(x) ⪰ W_ρ̂(x)"; re-derived independently in §2.

## 6. Data (own engine; DATA, not proof)
All runs: own engine, 0 failures of every signed check in every sample. Logs in scratch/hon_logs/. Starts: S3 + 2 random (seeded by path / fixed
seed), plus the packet's start file where given.
| sample | runs | phases | HON / HON′ / HON-0 / REC-1 (a) | LEV-step checks (STEP1 / GAPW / SAT / SAT0 / CNT) | HON-FB | RU / REPU (u-runs over ≥ 2 epochs) | failures |
| --- | --- | --- | --- | --- | --- | --- | --- |
| packet's named instances (immfail_n14, immp_cex_n11 + start, b5_o11, b4_n5_other_0, thclimb_n12_s11, exitr_cex_n16; LEVMAX 16) | 19 | 53 | 53 each | 7 / 7 / 21 / 12 / 18 | 2 | 118 / 56 (9) | 0 |
| lib41 (experiments/new/box41/lib41.txt, n ≤ 64; 45 skipped n > 64; LEV n ≤ 11) | 1,101 | 5,365 | 5,365 each; max 57 honest states in a phase, f_in 9, X_dir 2, X_big 17 | 53 / 53 / 312 / 219 / 342 | 64 | 20,473 / 7,702 (433) | 0 |
| random, own generator, n 4-11, ≤ 4 Odd choice vertices, seed 1414 (LEV all) | 9,000 | 20,910 | 20,910 each | 1,258 / 1,258 / 15,072 / 11,671 / 20,910 | 330 | 27,153 / 25,218 (74) | 0 |
| random, n 12-22, ≤ 5 Odd choice vertices, seed 1415 (no LEV) | 4,500 | 13,537 | 13,537 each | — | 251 | 21,466 / 18,439 (106) | 0 |
| hill climbs (hon_climb.py; fitness: inside-gap fallbacks, f_in, max honest, honest fallbacks): n 11 k ≤ 2 (20,000 steps), n 9 k ≤ 3 (20,000), n 12 k ≤ 3 LEVMAX 12 (10,000); every candidate fully checked | 48,751 candidates | — | 325,413 each | 235,399 STEP1 / 235,399 GAPW / 563,372 SAT / 150,253 SAT0 | 107,201 | 906,298 / 401,587 | 0 |
| hill climb n 12 k ≤ 3 at the default LEVMAX 11 (so NO LEV checks; non-LEV checks only) | 19,754 candidates | — | 138,666 each | — | 187 | 491,463 / 149,750 | 0 |
| lib41 games with n ≤ 20 (271 skipped), LEV exact for all (LEVMAX 20), RU off | 423 | 1,507 | 1,507 each; max 18 honest states | 422 / 422 / 1,152 / 602 / 1,507 | 28 (control: 142 non-honest fallbacks with non-flat edges and W change) | — | 0 |
- Controls (each bites): MUT=1 (G^u with u also cut to τ(u)) on the named instances: RU1 55, RU2 46, REPU 15 failures. MUT=3 (STEP1 demanding
  a rise of 2), random 200 games n 4-9: 5 of 70 fail. The DEAD claims of packet §5 are caught by my LEV: IMM fails 4 times on the named
  instances, and IMM′ reproduces exactly on immp_cex_n11 with its start file (state 0 honest, LEV 1 → 1, state 1 not the last of its
  phase, state 2 honest with LEV 10: packet §5's numbers). FB1 / FB2 tests applied to fallbacks at NON-honest states (not claimed): 5 non-flat
  and 5 W-changing on j10_n24, j7_n32, j8_n32 (the packet's inside-gap instances), so HON-FB's honesty hypothesis is needed and the tests
  discriminate.
- EPR-1-type exits: the exit transition of a u-run leaves the N5^τ phase on G^u in 51 of 244 exits (lib41) and 34 of 70 (random n ≤ 11):
  REPRO_u's one-phase claim is correctly limited to x, …, y. DIV (SPEC's S4b would move τ on G^u inside a u-run) = 0 in every sample.
- HON-FF (not signed): gaps with a fallback strictly inside, LEV computable: 1 in lib41 at n ≤ 11 (rose), 0 in random, 0 in every climb
  (the climbs did not produce one); none failed to rise. My data adds nothing beyond the packet's thin sample (its 3 instances are n ≥ 24).
- REC-1: {u}-intervals entered from D = ∅ / X_dir / X_big / phase start: lib41 214 / 2 / 17 / 2,077; random n ≤ 11 49 / 0 / 2 / 5,092. Max
  u-run length 112 (lib41), u-runs spanning ≥ 2 epochs 433 (lib41): RESTRICT_u / REPRO_u are exercised beyond R64's single epochs.

## 7. Notes (wording / citation; none affects a verdict)
- HON-N1 (§2, "HON-FB adds XW"). REC-0's chain also contains XW: it is in P-N5-REC0's premise list (l. 25) and in the proof of SN-PREFIX_D (a),
  which REC-0 step 3 uses (WM + XW; my R-N5-REC0 header). What HON adds over REC-0's premises is R17 (c)'s case split (HON-FB (i)), SAT0 and
  HON-FB (ii)-(iii); what it drops is SN-PREFIX_D and EP-0. The independence claim ("neither proof uses the other") is unaffected.
- HON-N2 (§2 / header, context line). "P-N5-REC0 … is in the referee queue and is expected to land as signed" is stale at the pin: both
  referees signed REC-0 (my R-N5-REC0, §C 981307c9; REFEREE-2 a0457eb0), RESULTS draft R66. So the packet's "HON-0 is the stronger form of
  the signed REC-0" is now literally true.
- HON-N3 (§1 step 1, remark for HON-FF). The fallback-free hypothesis is used twice: for the rise (Lemma P's step needs h → h + 1 to be an S4a
  step) and for the sandwich that keeps W's cycle-node map at h + 1 (WM at every transition of the gap). An inside fallback can lower W
  (FB-WLEV is DEAD, b5_o11), so a proof of HON-FF has to replace both, not only the first.
- HON-N4 (§6 DATA, comparison only). My lib41 run (different random starts) agrees with the packet on the maximum of 57 W-honest states in a
  phase; my f_in total is 9 against the packet's 4 (3 gaps), which is expected with other random starts.
