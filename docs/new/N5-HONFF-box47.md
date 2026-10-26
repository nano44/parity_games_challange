# HON-FF: an Even fallback is a Bellman-Ford step for Ξ (box 47)
L-NEW successor 26 (Opus 5.5), D14 / D18, Lead reading L40; queue item (2) of the Lead's GO 10:57Z ("(2) HON-FF"). Written 2026-10-26 11:30Z
onward (date -u). Working doc, unrefereed. Not a TARGET.md claim; G-N5-TIME stays open.
Labels: PROVED (L-NEW 26, unrefereed) / CONJECTURE / OPEN / DATA / READING.
Builds on docs/new/N5-REC1-box46.md §0, §1, §1a (Lemma HON, SAT0, HON-FB, HON′, CONJECTURE HON-FF) = docs/new/P-N5-HON-box46.md (frozen, sha1
07f8e767…; not edited; REFEREE-2 16 signed it, REFEREE 14 pending). Uses REFEREE-2's wording N-HON-1 for SAT0's Odd case.

## Summary
| item | statement | label |
| --- | --- | --- |
| Lemma FB-RISE | at an in-phase S4c fallback t → t+1 at or after a W-honest state h of the phase, LEV(t + 1) ≥ min(LEV(h) + 1, n − 1) | PROVED (every game) |
| Lemma FB-RISE (general form) | at every in-phase S4c fallback, LEV(t + 1) ≥ min(LEV(t) + 1, LEV_odd(t), n − 1) | PROVED (every game) |
| Theorem HON-FF | the W-honest states of a phase number at most 4n² − 3n: no f term | PROVED (every game); was CONJECTURE HON-FF |
| Corollary HON-0-FF | D = ∅ states, N_0, and in-phase transitions out of D = ∅ epochs are each ≤ 4n² − 3n per phase | PROVED (every game) |
| Corollary REC-1-FF | REC-1 (a)-(d) with f deleted: {u}-intervals ≤ 1 + 4n² − 3n + X_dir + X_big; (d) with f deleted | (a) PROVED; (b)-(d) IMPLICATIONS from (Στ), as REC-1 |
| data | FB-RISE (general): 0 failures; its control (no Odd term) fails 79 times, always where the Odd term binds | DATA |

## 0. Setting (every game)
As docs/new/N5-REC1-box46.md §0: N5 = SPEC S1-S5 (FIX 1-4, Q1-Q4); state k = (σ_k, τ_k), σ̄_k, Ξ_k = V_{σ_k,σ̄_k}, W_k = V_{σ_k,τ_k}; a phase P =
a maximal run with (λ, τ) constant (RESULTS R38 (a)); f = its in-phase S4c fallbacks. A state k is W-HONEST if Ξ_k = W_k. G_τ: Odd fixed to
τ. For a cycle node u of λ (λ(u) = u) and a simple path r of G_τ from x to u, value(r) := (u, P(r), |r|) (R17 Lemma P; box 10 §2). LEV(k) :=
the largest j ≤ n − 1 with Ξ_k(x) ⪰ value(r) for every vertex x and every such r with ≤ j edges. LEV_odd(k): the same with x ranging over
the Odd vertices only (the paths r still pass through every vertex). So LEV(k) ≤ LEV_odd(k).
Facts used, with sources (all LANDED or signed):
- (MON) Ξ_{k+1} ⊵ Ξ_k at every transition of N5, S4c fallbacks included (RESULTS R15 (a), (d); as HON step 0 and N-HON's premise list).
- (V1), (V2) (RESULTS R17 (a); box 10 §1). (V1) is a property of a play: if x is not its own cycle node, the value of x's play is x ⊕ (the value
  of the play from its successor), and that successor's path to the cycle node avoids x. It applies to Ξ_k (the value of the honest play,
  which follows σ_k at Even vertices). (V2) is order algebra on values.
- Lemma P's Case A (A1, A2) (box 10 §2; RESULTS R17 (b)), with Ω := Ξ_t, ρ := σ_t and "improving" := S2's Iσ_t. Case A uses only "Ω(z) ⪯
  Ω(ρ(x))", the bound Ω(z) ⪰ value(r′), (V1) and (V2) for Ω; it does not use that Ω comes from a one-player game (as SAT0 already uses it
  with Ω := W).
- SAT0's Odd case (N5-REC1 §1a; signed by REFEREE-2 16 with wording N-HON-1): at a state k and an Odd x with z := τ(x), r = x → z → r′:
  if W_k(z) ⪰ value(r′) then W_k(x) ⪰ value(r) (x not its own W-cycle node: (V1), (V2), with r′ avoiding x and z's play avoiding x or passing
  it only as a cycle vertex ranked below its cycle node; x its own W-cycle node: W_k(x) = (x, ∅, 0) ≻ value(r)).
- SPEC S2, S4c and FIX 3: an in-phase fallback is Even's (an Odd fallback changes τ); it switches exactly the Even x with Iσ_t(x) ≠ ∅, each to
  z*(x) := the (Ξ_t(w), w)-maximum of Iσ_t(x); Iσ_t(x) = {w ∈ succ(x) : Ξ_t(w) ≻ Ξ_t(σ_t(x))}.

## 1. Lemma FB-RISE (PROVED, every game)
Statement (general form). Let t → t + 1 be an in-phase S4c fallback of a phase P, and j := min(LEV(t) + 1, LEV_odd(t), n − 1). Then
LEV(t + 1) ≥ j.
Statement (honest form). If moreover h ≤ t is a W-honest state of P, then LEV(t + 1) ≥ min(LEV(h) + 1, n − 1).
Proof (general form). Let x be a vertex, u a cycle node of λ, r a simple path of G_τ from x to u with |r| ≤ j. We show Ξ_{t+1}(x) ⪰ value(r).
If |r| = 0, x = u and Ξ_{t+1}(u) = (u, ∅, 0) = value(r). Otherwise r = x → z → r′, with r′ simple from z to u, avoiding x, |r′| ≤ j − 1 ≤ LEV(t),
so Ξ_t(z) ⪰ value(r′).
- x Odd. |r| ≤ LEV_odd(t), so Ξ_t(x) ⪰ value(r); by (MON) Ξ_{t+1}(x) ⪰ value(r).
- x Even, z ∉ Iσ_t(x), i.e. Ξ_t(z) ⪯ Ξ_t(σ_t(x)). Lemma P's Case A at t with Ω = Ξ_t gives value(r) ⪯ Ξ_t(x); then (MON). (This covers every
  Even x that S4c leaves alone, and the non-improving edges of a switched x.)
- x Even, z ∈ Iσ_t(x). S4c sets σ_{t+1}(x) = z* := z*(x), and Ξ_t(z*) ⪰ Ξ_t(z) ⪰ value(r′) (z* is the Ξ_t-maximum of Iσ_t(x) ∋ z). By (MON),
  Ξ_{t+1}(z*) ⪰ value(r′). Both t and t + 1 lie in P, so λ_{t+1} = λ_t = λ.
  - λ(x) ≠ x: by (V1) at t + 1, Ξ_{t+1}(x) = x ⊕ Ξ_{t+1}(z*), and the honest path from z* to λ(x) at t + 1 avoids x; r′ avoids x. By (V2),
    Ξ_{t+1}(x) ⪰ x ⊕ value(r′) = value(r).
  - λ(x) = x: Ξ_{t+1}(x) = (x, ∅, 0). Since σ_{t+1}(x) = z* and x is its own cycle node at t + 1, z*'s honest play at t + 1 returns to x, so
    λ(z*) = x, and Ξ_t(z*) has cycle node x (λ_t = λ). value(r′) has cycle node u ≠ x (r is simple with |r| ≥ 1). Ξ_t(z*) ⪰ value(r′) then
    says x is better than u, so (x, ∅, 0) ≻ value(r). □
Proof (honest form). If LEV(h) = n − 1, LEV(t + 1) ≥ LEV(h) by (MON) (HON step 0). Let L := LEV(h) ≤ n − 2. By (MON), LEV(t) ≥ L. Odd part: let
x be Odd, r = x → τ(x) → r′ with |r′| ≤ L. At the W-honest h, W_h(τ(x)) = Ξ_h(τ(x)) ⪰ value(r′) (LEV(h) = L), and the W-cycle nodes at h are
those of λ. SAT0's Odd case at h gives W_h(x) ⪰ value(r), so Ξ_t(x) ⪰ Ξ_h(x) = W_h(x) ⪰ value(r): LEV_odd(t) ≥ L + 1. The general form gives
LEV(t + 1) ≥ min(LEV(t) + 1, LEV_odd(t), n − 1) ≥ min(L + 1, n − 1). □
- READING (the idea). S4c is a "switch every improving vertex to its Ξ-best improving successor" step: in the Ξ frame it is exactly a
  Bellman-Ford relaxation at Even vertices (Lemma P's induction step with Ω = Ξ, where Case B needs only Ξ_t(z*) ⪰ Ξ_t(z) and (MON)). An S4a
  step is not (it optimises W over the Ξ-gated arena), which is why IMM and IMM′ are false (N5-REC1 §4 (iii), (v)). Odd vertices cannot be
  relaxed by Even's move; at a W-honest state they are already one step ahead (SAT0), and Ξ keeps that.
- What the general form does NOT give: a rise at every fallback. When LEV_odd(t) ≤ LEV(t) (an Odd vertex of D undercuts its τ-path), a
  fallback need not raise LEV. DATA §3: this happens (79 of 269 non-honest fallbacks), always with LEV_odd(t) ≤ LEV(t).

## 2. Theorem HON-FF and corollaries (PROVED, every game)
Theorem HON-FF. In every phase P of N5 on every game, the W-honest states of P number at most 4n² − 3n.
Proof. Lemma HON's proof (N5-REC1 §1) with step 3's fallback clause removed. Let h_1 < … < h_N be the W-honest states of P and h_1, …, h_s the
unsaturated ones. For i < s, the gap h_i → … → h_{i+1} consists of in-phase transitions. If none is an S4c fallback, step 1 gives LEV(h_{i+1})
≥ LEV(h_i) + 1. Otherwise let t ∈ [h_i, h_{i+1} − 1] be the source of one of its fallbacks: FB-RISE (honest form, h := h_i) gives LEV(t + 1) ≥
min(LEV(h_i) + 1, n − 1), and LEV(h_{i+1}) ≥ LEV(t + 1) by step 0. As LEV(h_i) ≤ n − 2, either way LEV(h_{i+1}) ≥ LEV(h_i) + 1. With 0 ≤ LEV(h_1)
and LEV(h_s) ≤ n − 2, s − 1 ≤ n − 2. The saturated tail is as in step 3: N − s ≤ 4n(n − 1) + 1. So N ≤ (n − 1) + 4n(n − 1) + 1 = 4n² − 3n. □
- This is CONJECTURE HON-FF of N5-REC1 §1a, proved; it supersedes Corollary HON′ (f_in no longer appears).
- REFEREE 14's note HON-N3 (relayed by the Lead 11:27Z; report 59121877, not opened by me): an HON-FF proof must replace BOTH uses of the
  fallback-free hypothesis in step 1, the rise (Lemma P's step at h → h + 1, carried by WM) and the sandwich (λ_W = λ at h + 1). Here a gap
  WITH a fallback does not use step 1 at all: FB-RISE uses neither W after h, nor WM, nor any W-cycle node after h (only Ξ_h = W_h and λ_W = λ AT
  the honest h, both from honesty), and its Even part is read in the Ξ frame, whose cycle nodes are λ on the whole phase. Fallback-free gaps
  use step 1 unchanged, with both of its hypotheses in force.
Corollary HON-0-FF. In every phase P: the D = ∅ states, N_0 (the epochs with D_E = ∅) and the in-phase transitions whose source lies in a D = ∅
epoch each number at most 4n² − 3n. □ (HON-0's proof with HON-FF in place of HON.)
Corollary REC-1-FF. Theorem REC-1 (N5-REC1 §3) holds with f deleted: (a) the {u}-intervals of P, over all u ∈ Q, number ≤ 1 + (4n² − 3n) + X_dir
+ X_big (PROVED, no (Στ)); (c) the |D| = 1 states number ≤ (1 + 4n² − 3n + X_dir + X_big)(T*_Q + 2); (d) if every state of P has |D_k| ≤ 1, P has
≤ (4n² − 3n) + (1 + 4n² − 3n + X_dir)(T*_Q + 2) states. (c), (d) are IMPLICATIONS from (Στ) through EP-1u, as in REC-1 (since RESULTS R65, (Στ)
holds at audit strength). □ (f entered REC-1 only through HON-0 (a).)
- READING. For phases whose states all have |D| ≤ 1, the only quantity left open is X_dir, and by docs/new/N5-XDIR-box47.md Corollary XD-ρ,
  X_dir ≤ Σ_u ρ_u^exit + FLAT. The D = ∅ part of every phase, on every game, is now O(n²) states with no condition.
- Against P-N5-REC0 (frozen): REC-0's N_0 ≤ (f + 1)(n + 1) + 4n(n − 1) + 1; HON-0-FF's N_0 ≤ 4n² − 3n, smaller for every f ≥ 0, n ≥ 1
  ((f + 1)(n + 1) + 4n² − 4n + 1 − 4n² + 3n = f(n + 1) + 2 > 0).

## 3. DATA (experiments/new/box47/ffdeep.py; not proof)
Per non-honest in-phase fallback t: GEN_V = the general form fails (must be 0); CTRL_T = the rise from LEV(t) WITHOUT the Odd term fails (a
control: FB-RISE does not claim it); GEN_ODDBIND = LEV_odd(t) ≤ LEV(t). After a W-honest state h (h → h + 1 a non-fallback): FBRISE_V = the
honest form fails (must be 0); XI_AT = LEV(t) ≥ LEV(h) + 1 already at t; DEEP = the W-carry bound WLEV ≥ LEV(h) + 1 is lost at the fallback
(FB-WLEV-type); STEP_V = HON step 1's W-rise at h + 1 fails (must be 0). Exact levels by simple-path DFS (box 46 fbwlev.wlev), UNK = budget hit.
| sample | runs | non-honest in-phase fallbacks | GEN_V | CTRL_T (control) | GEN_ODDBIND | after a W-honest state | FBRISE_V | XI_AT | DEEP | STEP_V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all pinned instances of experiments/ and docs/referee*/ (735 files, out/liball.txt), n ≤ 20, S3 + 6 random, seed 5 | 2,128 | 269 | 0 | 79 | 79 | 0 | — | — | — | 0 |
| random 3,000 𝒞^kO (n 5-18, gseed 111), S3 + 4 random, seed 8 | 15,000 | 7 | 0 | 4 | 4 | 0 | — | — | — | 0 |
| random 3,000 𝒞^kO (n 6-24, gseed 222), S3 + 4 random, seed 9 | 15,000 | 3 | 0 | 2 | 2 | 0 | — | — | — | 0 |
| L-COMP 5's pinned gaps (l-comp 15bcfa06, experiments/n5-epoch/instances): ffin12_n32 (sha1 6bae375b…), ffin5_n32 (d20ea0f2…), ffin4_n24 (e1c4043c…), each with its .start, budget 3·10⁷ | 3 | 21 | 0 | 20 | 20 | 21 | 0 | 21 | 0 | 0 |
| experiments/red/xing/instances j10_n24, j7_n32, j8_n32, S3 (GEN not yet in the script for this row) | 3 | 4 | — | — | — | 4 | 0 | 4 | 0 | 0 |
- Library runs at n ≤ 34 (lib41 and the 735-file list, exact LEV, budget 3·10⁶) are running at this commit; their rows will be added.
- On the three known gaps with an inside fallback (experiments/red/xing/instances/j10_n24, j7_n32, j8_n32, S3; budget 3·10⁷ for n = 32): 4
  fallbacks, FBRISE_V 0, and XI_AT 4 (the Ξ-level had already reached LEV(h) + 1 before each fallback).
- Reading: the control fails often (CTRL_T 79), and only where the Odd term binds (GEN_ODDBIND 79 on n ≤ 20), so the checker can see a failed
  rise; the general form never fails.

## 4. What is left, and what this changes
- f itself per phase on general games (RESULTS R56: ρ) is NOT bounded by this: a fallback raises LEV only when LEV_odd(t) > LEV(t), i.e.
  away from Odd undercutting. CONJECTURE (not tested beyond §3): between two consecutive W-honest states, at most one fallback is needed to
  pay a level step, and the others are "Odd-bound" (LEV_odd(t) ≤ LEV(t)). OPEN.
- The P-N5-HON packet stands as signed; HON-FF is a strengthening for a new packet (P-N5-HONFF, if the Lead routes it): FB-RISE (both forms),
  Theorem HON-FF, Corollaries HON-0-FF and REC-1-FF (a). Its premises are the HON packet's plus S4c's exact rule (z* = the Ξ-best improving
  successor) and FIX 3.
