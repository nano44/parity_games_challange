# Honest states, u-runs and REC for |D| = 1 configurations (box 46)
L-NEW successor 25 (Opus 5.5), D14 / D18, Lead reading L40; Lead's GO 08:32Z (Lead's stamp): "(c), then (b), as briefed"; (c) = REC for
epochs with |D_E| = 1, (b) = an f-free REC-0. Written 2026-10-26 08:57Z onward (date -u). Working doc, unrefereed.
Labels: PROVED (L-NEW 25, unrefereed) / IMPLICATION / CONJECTURE / OPEN / DATA / READING / DEAD. Not a TARGET.md claim; G-N5-TIME stays open.
Frozen packets P-N5-REC0-box45 (sha1 343239b5…) and P-N5-STAU-box45 (sha1 7446d9a9…) are not edited; this doc goes further than both.

## Summary
| § | item | label |
| --- | --- | --- |
| §1 | Lemma HON: the W-HONEST states (Ξ_k = W_k) of a phase number ≤ f + 4n² − 3n; Corollary HON-0: D = ∅ states, D = ∅ epochs (N_0) and the in-phase transitions out of D = ∅ epochs are ≤ f + 4n² − 3n | PROVED (every game) |
| §1a | Lemma SAT0, Lemma HON-FB (a fallback at a W-honest state is flat, saturating, and the phase's last transition); Corollary HON′ (f replaced by f_in, the fallbacks at non-honest states between two honest ones); CONJECTURE HON-FF (no f at all) | PROVED; HON-FF CONJECTURE |
| §2 | Lemma RESTRICT_u, Corollary REPRO_u (u-runs: maximal runs with D_k ⊆ {u} are runs of N5^τ on G^u ∈ 𝒞^1O); Corollary EP-1u | PROVED; EP-1u an IMPLICATION from (Στ) |
| §3 | Theorem REC-1: per phase, the |D| = 1 states (so the epochs of every |D| = 1 configuration) are ≤ (1 + f + 4n² − 3n + X_dir + X_big)(T*_Q + 2) | IMPLICATION from (Στ), a REDUCTION to f, X_dir, X_big |
| §4 | the permanent Ξ-level in H_C does not rise between C-epochs for |D_C| = 1 (thclimb_n12_s11); fallbacks do fire at W-honest states (b4_n5_other_0); IMM (immfail_n14), FB-WLEV (b5_o11), IMM′ (immp_cex_n11, exitr_cex_n16) | DEAD (instances) |
| §5 | data | DATA |
| §6 | what is open; (b) | OPEN / READING |
- What changed against P-N5-REC0 (READING): REC-0's bound (f + 1)(n + 1) + 4n(n − 1) + 1 on N_0 had f MULTIPLIED by n, because its level lived in W
  and was lost at every fallback. HON keeps the level in Ξ (permanent, R15 (a)) and carries it through W only across the gap between two
  consecutive W-honest states, where W is monotone (WM). A fallback now costs one level step, not a restart: f is ADDITIVE. HON also counts
  STATES, not epochs, so EP-0's factor n + m disappears from the transition count.

## 0. Setting (every game)
- N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md (FIX 1-4, Q1-Q4). State k = (σ_k, τ_k); σ̄_k = S1's Odd counterstrategy; Ξ_k = V_{σ_k,σ̄_k};
  W_k := V_{σ_k,τ_k}, σ_k's valuation in the one-player game G_τ (Odd fixed to τ_k); λ := Ξ's cycle-node map. A PHASE P: maximal run with (λ, τ)
  constant (RESULTS R38 (a)); f := its in-phase S4c fallbacks. Q := Odd vertices of out-degree ≥ 2; D_k := {q ∈ Q : σ̄_k(q) ≠ τ(q)}; epochs,
  configurations C = σ̄|Q, H_C := G with Odd fixed to σ̄_C, as in docs/new/N5-NEP-box45.md §0.
- A state k of P is W-HONEST if Ξ_k = W_k pointwise. Every D = ∅ state is W-honest (σ̄_k = τ, Odd vertices outside Q having one successor);
  the converse fails (DATA §5: up to 14 W-honest states with D ≠ ∅ in one phase).
- LEV(k) := the largest j ≤ n − 1 such that Ξ_k(x) ⪰ value(r) for every vertex x and every simple path r of G_τ with ≤ j edges from x to a
  cycle node c of λ (λ(c) = c); value(r) := (c, P(r), |r|) as in RESULTS R17 Lemma P (P(r) = the vertices of r before c more relevant than c).
  B(x) := the maximum of value(r) over all such simple paths from x. (Same objects as P-N5-REC0 §0, with Ξ in place of W.)

## 1. Lemma HON and Corollary HON-0 (PROVED, every game)
Statement. In every phase P of N5, the W-honest states of P number at most f + 4n² − 3n.
Corollary HON-0. In every phase P: (a) the D = ∅ states number ≤ f + 4n² − 3n; (b) so does N_0, the number of epochs with D_E = ∅; (c) so does
the number of in-phase transitions whose source lies in a D = ∅ epoch (each such transition has a D = ∅ source state, and a state has one
outgoing transition). (b) is below REC-0's (f + 1)(n + 1) + 4n(n − 1) + 1 for every f, n ≥ 1, and (c) is below REC-0's corollary N_0·(n + m).
Premises (LANDED unless marked): SPEC; RESULTS R15 (a) (Ξ non-decreasing along a run) and R15 (d) (at most 4n(n − 1) consecutive iterations
leave both Ωσ = Ξ and Ωτ unchanged); R17 (b) Lemma P, its INDUCTION STEP only, with R17 (F1)/(F2) and R17 (d) (every pointwise-optimal choice)
— the same use, and the same question Q-R17, as P-N5-REC0 §1 step 1; R18 (d) Lemma S (c) (S4a's output is a pointwise optimum of its arena
against τ); R23 (g) Lemma WM (W_{k+1} ⊵ W_k at every in-phase transition that is not an S4c fallback; game-general, P-N5-XEP fixes XEP-N2).
Proof.
0. (Monotone.) LEV is non-decreasing along P: Ξ_{k+1} ⊵ Ξ_k (R15 (a)), and the paths r and the cycle nodes of λ do not depend on k inside P
   (G_τ and λ are fixed). LEV ≥ 0 everywhere: for a cycle node c of λ, Ξ_k(c) = (c, ∅, 0) = value of the empty path.
1. (Rise across a fallback-free gap.) Let h < h′ be W-honest states of P with no W-honest state strictly between them, and suppose no
   transition h → … → h′ is an S4c fallback (all of them are in-phase, being inside P). Then LEV(h′) ≥ min(LEV(h) + 1, n − 1).
   - W along the gap: by WM, W_{h′} ⊵ W_{h′−1} ⊵ … ⊵ W_{h+1} ⊵ W_h.
   - Cycle nodes: W_h = Ξ_h and W_{h′} = Ξ_{h′} have cycle-node map λ. The order on valuations compares the reward of the cycle node first,
     and rewards are injective, so for every v the sandwiched W_{h+1}(v) has cycle node λ(v). So λ_W = λ at h and at h + 1.
   - Lemma P step at h → h + 1 in G_τ (Ω := W, ρ_h := σ_h, ρ_{h+1} := σ_{h+1}, u := a cycle node of λ): at h, Ξ_h = W_h, so the gates Iσ_h (S2,
     Ξ-improving edges) are exactly the W-improving edges of G_τ at σ_h, and S4a's arena (Even v: {σ_h(v)} ∪ Iσ_h(v); Odd: τ) is the
     switch-best arena of G_τ at σ_h; h → h + 1 is not a fallback, so σ_{h+1} is S4a's output, a pointwise optimum of that arena (R18 (d) S (c);
     if Iσ_h = ∅ the arena is {σ_h} and σ_{h+1} = σ_h, which is trivially its optimum); τ is unchanged (in-phase); no vertex changes its
     W-cycle node from h to h + 1 (previous bullet), which is what Lemma P's cases B1 / B2 use when they conclude "the phase ended at step
     k + 1, contrary to the assumption". With the hypothesis W_h = Ξ_h ⪰ value(r′) for |r′| ≤ LEV(h), the step gives W_{h+1}(x) ⪰ value(r)
     for every x and every simple r with ≤ LEV(h) + 1 edges (Q-R17).
   - So Ξ_{h′} = W_{h′} ⊵ W_{h+1} ⪰ value(r) for all such r: LEV(h′) ≥ min(LEV(h) + 1, n − 1).
2. (Saturation.) At a W-honest state h, Ξ_h(x) = W_h(x) is the value of the (σ_h, τ)-play from x, which follows a simple path r_x of G_τ to
   λ_W(x) = λ(x), a cycle node of λ, and then that cycle; so Ξ_h(x) = value(r_x) ⊴ B(x). If LEV(h) = n − 1 then Ξ_h ⊵ B (every simple path has
   ≤ n − 1 edges), so Ξ_h = B: call h SATURATED.
3. (Count.) Let h_1 < … < h_N be the W-honest states of P. If h_i is saturated, every later h_{i′} is: LEV(h_{i′}) ≥ LEV(h_i) = n − 1 (step 0).
   Let h_1, …, h_s be the unsaturated ones (LEV ≤ n − 2).
   - For i < s the gap (h_i, h_{i+1}) either contains a fallback, or LEV(h_{i+1}) ≥ LEV(h_i) + 1 (step 1, as LEV(h_i) + 1 ≤ n − 2 + 1). The gaps
     are disjoint sets of transitions, so at most f of them contain a fallback; and 0 ≤ LEV(h_1), LEV(h_s) ≤ n − 2, so at most n − 2 of them
     are fallback-free. Hence s − 1 ≤ f + n − 2.
   - If s < N, put t := h_{s+1}. For i > s, Ξ_{h_i} = B = Ξ_t (step 2), so Ξ is constant on the states t, …, h_N (R15 (a)); τ is constant on P,
     so Ωτ is too; R15 (d) gives h_N − t ≤ 4n(n − 1), hence N − s ≤ 4n(n − 1) + 1.
   - N ≤ (f + n − 1) + 4n(n − 1) + 1 = f + 4n² − 3n. □
- Proof of HON-0: (a), (b), (c) are immediate (D = ∅ states are W-honest; epochs are disjoint and non-empty). For the comparison:
  (f + 1)(n + 1) + 4n(n − 1) + 1 − (f + 4n² − 3n) = f·n + 2 > 0.
- What HON does NOT give (READING): it says nothing about states that are not W-honest, i.e. about epochs with Ξ ≠ W (all |D| ≥ 1 epochs in
  which some τ-play reaches D). Its f term is sharpened below (HON′).

### 1a. Fallbacks at W-honest states: Lemma SAT0, Lemma HON-FB, Corollary HON′ (PROVED, every game; added 09:0xZ by date -u)
"No in-phase fallback fires at a W-honest state" is FALSE (§4 (ii), b4_n5_other_0). What is true is that such a fallback is harmless:
Lemma SAT0. If at a state k of P the strategy σ_k has no W-improving edge in G_τ, then W_k(x) ⪰ value(r) for every x and every simple path r of
G_τ from x to a W-cycle node c (λ_W(c) = c), of any length. If k is moreover W-honest, LEV(k) = n − 1 (k is saturated).
Proof. Induction on |r|. |r| = 0: W_k(c) = (c, ∅, 0). |r| ≥ 1, r = x → z → r′, r′ simple, avoiding x; W_k(z) ⪰ value(r′) by induction.
x Even: (x, z) is not W-improving, i.e. W_k(z) ⪯ W_k(σ_k(x)), and R17 Lemma P's Case A (A1, A2) gives value(r) ⪯ W_k(x) (it uses only this
inequality, the induction hypothesis, (V1) and (V2)). x Odd: z = τ(x); if x is not its own W-cycle node, W_k(x) = x ⊕ W_k(z) ⪰ x ⊕ value(r′) =
value(r) by (V1), (V2) (r′ and z's play avoid x); if x is its own W-cycle node, W_k(x) = (x, ∅, 0), z's W-play returns to x so W_k(z) has cycle
node x, while value(r′) has cycle node c ≠ x; W_k(z) ⪰ value(r′) then forces x better than c, and W_k(x) ≻ value(r). At a W-honest k the
W-cycle nodes are those of λ, and W_k = Ξ_k, so LEV(k) = n − 1. □
Lemma HON-FB. Let h be a W-honest state of P whose transition h → h + 1 is an in-phase S4c fallback. Then (i) every W-improving edge (x, z) of
G_τ at σ_h is FLAT: x is its own cycle node and z's W-play returns to x through vertices less relevant than x; (ii) W_{h+1} = W_h;
(iii) σ_{h+1} has no W-improving edge in G_τ; (iv) h + 1 is W-honest and saturated, and it is the last state of P.
Proof. In-phase, so τ is unchanged and the fallback is Even's (FIX 3), so Iσ_h ≠ ∅ and S4a returned σ_h. At h, Iσ_h = the W-improving edges
(Ξ_h = W_h) and S4a's arena is G_τ's switch-best arena, of which σ_h is therefore a pointwise optimum ((F1) via R18 (d) S (c)).
(i) Let (x, z) be W-improving and ρ̂ := σ_h[x → z], a strategy of the arena, so W_h(x) ⪰ W_ρ̂(x). Run Theorem PH's case split (box 10 §3,
  R17 (c)) with this inequality in place of Lemma P's bound: if x is not on z's path π to c := λ(z) nor on c's cycle, W_ρ̂(x) = x ⊕ W_h(z)
  strictly exceeds W_h(x) (strict (V2) if x is not its own cycle node; a better cycle node if it is): impossible. Otherwise the switch
  closes a cycle Z, and Lemma P's B1 / B2 leave three outcomes: W_ρ̂(x) has a better cycle node than W_h(x) (impossible, as W_h(x) ⪰ W_ρ̂(x)),
  W_ρ̂(x) = x ⊕ W_h(z) ≻ W_h(x) (B1, second sub-case: impossible), or B2 with D = ∅ and top(Z) = x: x is its own cycle node and W_ρ̂(x) =
  (x, ∅, 0) = W_h(x). Only the last is possible.
(ii) S4c switches exactly the vertices x with Iσ_h(x) ≠ ∅, each to z* := the (Ξ_h(w), w)-maximum of Iσ_h(x); all are flat by (i). Each switched x
  stays its own cycle node with value (x, ∅, 0) (its new cycle has top x). A switched x′ is not on the path from z* to x: x′ is its own cycle
  node, so a play reaching x′ ends at x′'s cycle, not at x. So every play keeps its path to its cycle node and its path set: W_{h+1} = W_h.
(iii) Values are unchanged, so the W-improving edges at σ_{h+1} are judged with the same W. An unswitched vertex had none at h and its edge is
  unchanged. A switched x has Iσ_{h+1}(x) = {w : W_h(w) ≻ W_h(z*)}; such a w would lie in Iσ_h(x) with a larger Ξ_h = W_h value than z*. So
  there are none.
(iv) Ξ_h ⊴ Ξ_{h+1} (R15 (a)) ⊴ W_{h+1} (RESULTS R21 (a) XW) = W_h = Ξ_h, so Ξ_{h+1} = W_{h+1}: h + 1 is W-honest; by (iii) and SAT0 it is
  saturated. At h + 1, Iσ = the W-improving edges = ∅ (W-honest), so S4a returns σ_{h+1}; then either S4b changes τ, or S4c fires for Odd
  (Iσ = ∅, FIX 3), which changes τ, or N5 stops. So h + 1 is the last state of P. □
Corollary HON′ (sharpened HON). In every phase P, the W-honest states number at most f_in + 4n² − 3n, where f_in ≤ f is the number of in-phase
fallbacks of P at states that are NOT W-honest and lie strictly between two W-honest states of P.
Proof. HON's proof, step 3: a gap (h_i, h_{i+1}) with i < s that contains a fallback cannot have it at h_i (by HON-FB (iv) h_{i+1} = h_i + 1
would be saturated, against i + 1 ≤ s); so its fallback is at a non-W-honest state strictly inside the gap. The gaps are disjoint, so at most
f_in of them contain a fallback, and s − 1 ≤ f_in + n − 2. □
- So the D = ∅ part of a phase costs f_in + 4n² − 3n states (HON-0 with HON′). DATA (§5): f_in totals 4 (in 3 gaps) over all 5,377 lib41 phases.
- CONJECTURE HON-FF (f-free; DATA §5): across EVERY gap between consecutive W-honest states of a phase, LEV rises (LEV(h_{i+1}) ≥ min(LEV(h_i) + 1,
  n − 1)), fallbacks inside the gap included. It would give |H(P)| ≤ 4n² − 3n with no f term, i.e. (b) for D = ∅ in its strongest form.

## 2. u-runs: Lemma RESTRICT_u, Corollary REPRO_u (PROVED, every game) and Corollary EP-1u (IMPLICATION from (Στ))
- For u ∈ Q let G^u := G with every Odd v ≠ u cut to its edge τ(v); u keeps ALL its edges. So G^u ∈ 𝒞^1O with d_o = deg(u). (RESULTS R64's G′_E
  for D_E = {u} is G^u with u cut further to {τ(u), σ̄_E(u)}.)
- A u-RUN of P is a maximal run J = (x, …, y) of consecutive states of P with D_k ⊆ {u} for every k ∈ J; len(J) := the in-phase transitions
  with source in J. A u-run can contain several D = ∅ states and several configurations with D = {u} (σ̄(u) may take any successor of u ≠ τ(u)).
Lemma RESTRICT_u. For every state k of P with D_k ⊆ {u}, statements (i)-(iv) of RESULTS R64 (a) RESTRICT_E hold with G′_E replaced by G^u.
Proof. R64 (a)'s proof verbatim. The only place where it uses the epoch is (i): "σ̄_E is an Odd strategy of G′_E and σ̄_k = σ̄_E". Here σ̄_k
is an Odd strategy of G^u: σ̄_k(v) = τ(v) for v ∈ Q ∖ {u} (as D_k ⊆ {u}), Odd vertices outside Q have one successor, and u keeps all its edges.
(ii)-(iv) use only that G^u's edges are G's, that every τ(v) is an edge of G^u, and (i). □
Corollary REPRO_u. Let J = (x, …, y) be a u-run of P and y′ := x + len(J). Then N5^τ on G^u from (σ_x, τ) passes through (σ_x, τ), …, (σ_{y′}, τ)
with the same fallback / non-fallback type at each of its len(J) transitions as N5 on G, and x, …, y lie in ONE phase of that N5^τ run (the
last transition may leave it; R64's repair EPR-1).
Proof. R64 (b)'s induction verbatim, with RESTRICT_u at each k ∈ [x, y′ − 1] ⊆ J in place of RESTRICT_E. □
Corollary EP-1u (IMPLICATION). Under premise (Στ) (as in R64 (e): R48 (i) and R50 (h), with their chains, hold for every phase of every N5^τ run
on every 𝒞^1O game from every start pair; packet P-N5-STAU is its check), every u-run J has len(J) ≤ T*(G^u) + 1, where T*(G^u) is RESULTS R51
(a)'s per-phase bound (R50 (h) with f := 2n²) at G^u's parameters (n, m^u ≤ m, Δ^u ≤ Δ, d_o = deg(u) ≤ Δ), a polynomial.
Proof. As R64 (e): by REPRO_u, the len(J) transitions are, except possibly the last, in-phase transitions of one phase of an N5^τ run on G^u ∈
𝒞^1O; under (Στ) that phase has ≤ T*(G^u) of them. □
- Size (READING, not a separate claim): R64 (e) reads T* at d_o = 2 as O(m·Δ·n¹¹), and R51 (a)'s ITER = (n(n − 1) + d_o)(T* + 1) = O(m·Δ·d_o·n¹³)
  gives the same reading O(m·Δ·d_o·n¹¹) ⊆ O(m·Δ²·n¹¹) at d_o = deg(u).
- EP-1u contains R64's EP-1 (an epoch with D_E = {u} lies in one u-run) and is stronger: one bound covers a whole run of epochs whose
  configurations differ only at u, interleaved with D = ∅ epochs.

## 3. Theorem REC-1 (IMPLICATION from (Στ); a REDUCTION)
Definitions (phase P). A {u}-INTERVAL: a maximal run of consecutive states of P with D_k = {u}. X_dir(P): the in-phase transitions k → k + 1 with
|D_k| = |D_{k+1}| = 1 and D_k ≠ D_{k+1}. X_big(P): the in-phase transitions with |D_k| ≥ 2 and |D_{k+1}| = 1. T*_Q := max over u ∈ Q of T*(G^u).
Statement. In every phase P of N5 on any game, under (Στ):
(a) (PROVED, no (Στ)) the {u}-intervals of P, over all u ∈ Q, number ≤ 1 + (f + 4n² − 3n) + X_dir + X_big;
(b) every {u}-interval has ≤ T*(G^u) + 2 states;
(c) so the states with |D_k| = 1 number ≤ (1 + f + 4n² − 3n + X_dir + X_big)·(T*_Q + 2), and so do the epochs with |D_E| = 1; in particular, for
    every configuration C with |D_C| = 1, the C-epochs of P number at most that (CONJECTURE REC for such C is REDUCED to f, X_dir and X_big);
(d) if every state of P has |D_k| ≤ 1, then X_big = 0 and P has at most (f + 4n² − 3n) + (1 + f + 4n² − 3n + X_dir)·(T*_Q + 2) states, so N5's
    in-phase transitions in P are polynomial in n, m, f and X_dir.
Proof.
(a) A {u}-interval I that does not start at P's first state starts at the target k + 1 of an in-phase transition k → k + 1 with D_k ≠ {u}.
    Either D_k = ∅ (k is a D = ∅ state; distinct intervals have distinct k, and HON-0 (a) bounds these k), or |D_k| = 1 (a transition of
    X_dir), or |D_k| ≥ 2 (X_big). One more interval may start at P's first state.
(b) A {u}-interval I lies in one u-run J. Every state of I except possibly the last state of P is the source of an in-phase transition with
    source in J, so |I| ≤ len(J) + 1 ≤ T*(G^u) + 2 (EP-1u).
(c) Every state with |D_k| = 1 lies in exactly one {u}-interval; (a) × (b). Epochs are disjoint and non-empty, and a |D_E| = 1 epoch consists of
    |D| = 1 states.
(d) X_big = 0 since no state has |D| ≥ 2. States of P = D = ∅ states (HON-0 (a)) + |D| = 1 states ((c)). □
- Every f in (a)-(d) may be replaced by f_in ≤ f (Corollary HON′, §1a), since f enters only through HON-0 (a).
- What REC-1 gives (READING). The longest phases in the data (50 and 31 epochs; lev_l_x, so_th_n32) are of type (d), and in them X_dir = 0 (§5):
  the 49 epochs of lev_l_x's longest phase sit in ONE {u}-interval, i.e. one u-run, which EP-1u bounds as a whole. So the recurrences of a
  |D| = 1 configuration that the data shows (up to 10, N5-NEP §1) are recurrences INSIDE one u-run; across u-runs they are paid by D = ∅ states
  (HON), by fallbacks, or by X_dir / X_big.
- With FB-kT (RESULTS R61, conditional on R56 / R58): on 𝒞^kO, k fixed, f = O(n^{k+1}) per phase, so the D = ∅ part is O(n^{k+1} + n²) and the
  |D| = 1 part is O((n^{k+1} + X_dir + X_big)·m·Δ²·n¹¹) under (Στ) (with §2's size reading of T*). What remains open there: X_dir, X_big, and epochs with |D| ≥ 2.

## 4. DEAD (instances)
(i) The permanent Ξ-level in H_C for |D_C| = 1 (my first plan for (c), 08:40Z). For a configuration C, LEV_C(k) := LEV with G_τ replaced by H_C. It is
  non-decreasing along the whole phase (R15 (a)), and at C-states Ξ = V^{H_C}, so a rise of LEV_C between consecutive C-epochs on every
  fallback-free gap would bound the C-epochs exactly as HON bounds the D = ∅ states. For D_C = ∅ it is HON. For |D_C| = 1 it FAILS:
  - experiments/si/orlens/instances/thclimb_n12_s11.pg (sha1 e3b47b6e86ba881f7de64db3647f011fc0043878), S3 start, phase [2, 17], D = {1}, τ(1) = 11
    throughout the gaps: configuration u → 10 at states 2 and 6, gap 2 → 6 fallback-free, LEV_C 1 → 1 (also gaps 3 → 5 for u → 2 and 7 → 9 for
    u → 7). In the gap σ̄(1) moves 10 → 2 → 3 → 2 → 10: D never changes, only σ̄(u). The H_C-path 8 → 11 → 5 (cycle node 5) beats Ξ(8) at state 6.
    experiments/new/box46/norise.py prints it (out/norise_lib41_n20.txt).
  - Obstruction: S4a optimises against τ (u → 11 = τ(u)), not against σ̄_C(u). The gate (8, 11) is Ξ-improving, but S4a can prefer a W-better,
    Ξ-worse target, so V^{H_C} gains nothing from the step. DATA: lib41 (n ≤ 34), 133 of 453 fallback-free gaps between C-epochs with |D_C| = 1
    have no rise (levels.py; also with paths avoiding u: 133).
  - What survives: these recurrences are inside one u-run, and REC-1 handles them by EP-1u instead of a level.
(ii) "No in-phase fallback fires at a W-honest state" (my side claim, 09:0xZ; never used). FALSE: experiments/n5-exhaustive/instances/b4_n5_other_0.pg
  (sha1 6115e60a98150a4c6dc1643c4e2276a38075f8fa), S3 start, state 1: W-honest, Iσ = {(4, 0)}, σ(4) = 1, Ξ(0) = (4, ∅, 2) ▷ Ξ(1) = (4, ∅, 3),
  vertex 4 is its own cycle node with Ξ(4) = (4, ∅, 0): the flat cycle-closing switch (Lemma P case B2, N5-killer-box4.md §3); S4a returns σ and
  the Even fallback fires in-phase. hon.py: 56 such fallbacks on lib41, 546 on the random sample (FBH_V). So honest states do not exclude
  fallbacks. What replaces the claim: Lemma HON-FB (§1a), such a fallback is flat, saturating and the last transition of its phase.

(iii) CONJECTURE IMM, "the Ξ-level rises AT ONCE after a non-fallback in-phase step from a W-honest state: LEV(h + 1) ≥ min(LEV(h) + 1, n − 1)"
  (09:3xZ; it would have given HON-FF directly, since Ξ is monotone). DATA first: 0 failures on lib41 n ≤ 20 (481 steps, 27 of them split).
  FALSE: immclimb.py (seed 61, 𝒞^2O, n ≤ 14) found experiments/new/box46/instances/immfail_n14.pg (sha1 db3fc2ca2ef48523166d93ce0eff072e1eb8d33e),
  S3 start: h = 0 honest, LEV 3; state 1 has D = {0} and LEV 3 (W-level 6; W's cycle node moves to 10 at nine vertices, Ξ's stays 2: a split);
  again h = 2 → 3, LEV 3 → 3 with no split. Obstruction: S4a takes the W-best target into the region where Odd now deviates at q = 0 (σ̄(0) = 2 ≠
  τ(0) = 4), so Ξ_{h+1} lags W_{h+1}. In both failures h + 1 is the LAST state of its phase (W drops into the next state without a fallback, so
  the next transition leaves the phase), and HON-FF holds on the game (hon2.py: 2 gaps, both rise). Refined CONJECTURE IMM′ (would imply
  HON-FF): IMM holds whenever h + 1 is not the last state of its phase; FALSE too, see (v).

(iv) CONJECTURE FB-WLEV, "an in-phase fallback never lowers the W-level" (WLEV: W_k ⪰ value(r) for simple G_τ-paths r with ≤ j edges to cycle
  nodes of the phase's λ), 09:45Z, the W-carry route to HON-FF. FALSE: fbwlev.py, lib41 n ≤ 24, 14 of the 166 fallbacks at non-honest states
  lower it (none of the 39 at honest states, as HON-FB says). First: experiments/n5-exhaustive/instances/b5_o11.pg (sha1
  db4fe55a650236dfe1bc5030f0ca123c75754764), S3, fallback 7 → 8, WLEV 6 → 5. On the same run the Ξ-level itself climbs through the non-honest
  stretch (LEV 3, 4, 4, 5, 5, 6, 9 at states 5-11; gaptrace.py) and the next honest state 12 has LEV 9: HON-FF holds there, not by carrying W.
  So a proof of HON-FF cannot go through W alone; IMM′ (a rise in Ξ itself) is the remaining route.

(v) CONJECTURE IMM′ (IMM whenever h + 1 is not the last state of its phase), 09:3xZ. FALSE (09:5xZ, by date -u):
  - Hand construction experiments/new/box46/instances/immp_cex_n11.pg (sha1 1dd7f5853103bb0698cd7e3cbc220a70df5d24ee) with start
    instances/immp_cex_n11.start (sha1 18cf37667017b1f0244731e0719ac878568eb8fb). One cycle node (vertex 0, a self-loop), so λ never changes; one
    Odd choice q = 3 with τ(3) = 4 = a, alternative y = 5. x = 1 has σ(1) = 2 → q and an improving edge to Z = 7 (priority 20). At a = 4 the
    improving edge to E = 8 (priority 30); at y = 5 a two-step potential 5 → 6 → 10 (priority 40), of which only 6 → 10 is improving at the start,
    so τ(3) = 4 is Odd-optimal for the whole game (Iτ = ∅, and τ never moves). State 0 is W-honest with LEV 1. S4a keeps x at 2 (W(2) now goes
    through E), but at state 1 the honest reply at q is y (Ξ(4) rose through E, Ξ(5) did not yet), so Ξ_1(1) = (0, {1, 2, 3, 5}, 4) is below the
    value (0, {1, 7}, 2) of the path 1 → 7 → 0: LEV 1 → 1. State 1 is not the last of its phase (τ is constant, λ is constant), and state 2 is
    W-honest with LEV 10. The run (engine trace): states 0 (honest, LEV 1), 1 (D = {3}, LEV 1), 2 (honest, LEV 10), stop.
  - In the library too: imm.py on lib41 n ≤ 34 finds 2 IMM′ failures, first experiments/red/so/instances/exitr_cex_n16.pg (random start, h = 2,
    LEV 1 → 1).
  - Obstruction: τ's value-optimality in S4b's arena constrains Odd only on τ ∪ Iτ; Iτ is read from Even's G_τ-OPTIMUM, so an edge to a vertex
    with large latent potential (not yet realised by σ) is not in Iτ, and the honest reply may take it at once.
  - HON-FF survives on both (one fallback-free gap each, both rise): the rise comes at the next honest state, carried by W (HON step 1).

## 5. DATA (not proof; experiments/new/box46/, run from that directory; outputs in out/)
- hon.py (Lemma HON): HON_V = |H| > f + 4n² − 3n; WMC_V = the WM chain W_{h′} ⊵ W_{h+1} fails on a fallback-free gap between consecutive W-honest
  states; D0NOTHON_V = a D = ∅ state that is not W-honest; FBH_V (§4 (ii)).
| sample | runs | phases | HON_V | WMC_V (fallback-free pairs) | D0NOTHON_V | FBH_V | max W-honest states in a phase | max W-honest, D ≠ ∅ | max |H| / (f + n) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib41 (n ≤ 64), S3 + 2 random starts, seed 7 | 1,101 | 5,377 | 0 | 0 (3,380) | 0 | 56 | 57 | 14 | 0.94 |
| 3,000 random 𝒞^kO (k 2-4, n 5-18, games seed 111), S3 + 4 random, seed 8 | 15,000 | 40,203 | 0 | 0 (2,438) | 0 | 546 | 4 | 4 | 0.6 |
- dint.py (D-intervals, REC-1 (a)): R0P_V = N_0 > f + 4n² − 3n; REC1R_V = for some u, #{u}-intervals > N_0 + 1 + ENTDIR(u) + ENTBIG(u).
| sample | phases | R0P_V | REC1R_V | {u}-intervals | entered from D = ∅ / {u′} (X_dir) / |D| ≥ 2 (X_big) / phase start | max epochs in one {u}-interval | max states in one | max {u}-intervals of one u per phase | phases with all |D| ≤ 1: count, max N_ep, max X_dir |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib41, S3 + 2 random, seed 7 | 5,377 | 0 | 0 | 2,330 | 204 / 1 / 12 / 2,113 | 49 | 111 | 6 | 3,814, 50, 0 |
| 3,000 random 𝒞^kO, S3 + 4 random, seed 8 | 40,203 | 0 | 0 | 12,239 | 130 / 15 / 32 / 12,062 | 2 | 4 | 2 | 30,360, 3, 1 |
| lev_l_x, so_th_n32, lap_n6_s1_110421 (S3) | 6 | 0 | 0 | 11 | 6 / 0 / 0 / 5 | 49 | 54 | 6 | 6, 50, 0 |
- levels.py (the permanent level LEV_C at C-epoch ends, §4 (i)); gaps = between consecutive C-epochs of one phase; NORISE = no rise on a
  fallback-free gap; NORISE_FB = no rise on a gap with a fallback; UNK = level computation over the path budget (skipped).
| sample | |D_C| | gaps | fallback-free | NORISE | gaps with a fallback | NORISE_FB | UNK |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lib41 n ≤ 34, S3 + 2 random, seed 7, budget 3·10⁶ | 0 | 33 | 31 | 0 | 2 | 0 | 1 |
| lib41 n ≤ 34 (same) | 1 | 676 | 453 | 133 (also 133 for u-avoiding paths) | 223 | — | 36 |
| random 3,000 𝒞^kO, S3 + 4 random, seed 8, budget 10⁶ | 0 / 1 | 1 / 1 | 1 / 1 | 0 / 0 | 0 / 0 | — | 0 |
- hon2.py (LEV in G_τ at every W-honest state; gaps between consecutive ones; HON step 1 and HON-FF):
| sample | gaps | fallback-free gaps without a rise | gaps with the fallback at the first state (HON-FB) | without a rise | gaps with a fallback inside | without a rise | UNK |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lib41 n ≤ 20, S3 + 2 random, seed 7 | 472 | 0 | 27 | 0 | 0 | — | 3 |
| lib41 n ≤ 34, budget 3·10⁶ | 1,689 | 0 | 45 | 0 | 2 | 0 | 49 |
| random 3,000 𝒞^kO, S3 + 4 random, seed 8 | 2,984 | 0 | 546 | 0 | 0 | — | 0 |
- fbin.py, all lib41 gaps with an inside fallback (n ≤ 64, exact LEV): j10_n24 gap 1 → 24, fallback at 9, LEV 1 → 4; j7_n32 gap 1 → 46, fallback at
  22, LEV 0 → 19; j8_n32 gap 3 → 50, fallbacks at 22 and 29, LEV 2 → 9 (experiments/red/xing/instances/, S3 starts). All rise. On j10_n24
  (gaptrace.py) the Ξ-level already rises at state 2, one step after the honest state, and the fallback at 9 lowers W at nine vertices
  without lowering the W-level (3).
- imm.py (non-fallback in-phase steps h → h + 1 from a W-honest h; IMM and IMM′ failures; WIMM = the W-level at h + 1 does not rise):
| sample | steps | split steps (a W-cycle node ≠ λ at h + 1) | IMM failures (split / unsplit) | IMM′ failures (h + 1 not last in its phase) | WIMM split / UNSPLIT |
| --- | --- | --- | --- | --- | --- |
| lib41 n ≤ 20, S3 + 2 random, seed 7 | 481 | 27 | 0 / 0 | 0 | 11 / 0 |
| random 3,000 𝒞^kO, S3 + 4 random, seed 8 | 2,556 | 45 | 4 / 1 | 0 | 15 / 0 |
| lib41 n ≤ 34, budget 3·10⁶ (74 UNK) | 1,750 | 88 | 2 / 1 | 2 (exitr_cex_n16) | 62 / 0 |
  WIMM UNSPLIT = 0 is HON step 1's Lemma P rise of W (it needs no W-cycle-node change at h + 1); the split failures are allowed.
- Climbs (ffclimb.py against HON-FF, immclimb.py against IMM / IMM′; box43 climb.mutate, S3 start; best games in out/climb/, not kept):
  ffclimb seeded from j10_n24 (1,500 steps, seed 51): (0, 1); from random 𝒞^2O / 𝒞^3O / 𝒞^4O (4,000 steps, seeds 54-56): (0, 0, 0), i.e. the
  climber never produced a gap with an inside fallback. immclimb (IMM, seeds 61-63): IMM failures found at once (§4 (iii)); immclimb --prime
  (IMM′ first, seeds 71-74, 𝒞^2O-𝒞^4O, n ≤ 14-22, 3,000-4,000 steps): best (IMM′ failures, IMM failures, honest-to-dishonest steps) = (0, 1, 3),
  (0, 1, 4), (0, 2, 2), (0, 3, 4): no IMM′ failure.
- Reading of the data: X_dir and X_big are rare (≤ 1% of interval entries); most {u}-intervals start the phase; the per-phase number of
  {u}-intervals of one u is ≤ 6. Nothing here bounds X_dir or X_big.

## 6. Open, and (b)
- OPEN: X_dir, X_big per phase (D-changes into a singleton that do not pass through D = ∅; a special case of R55's CONJECTURE Δ1); f per phase on
  general games (R56: ρ); epochs with |D| ≥ 2; and (Στ) itself (P-N5-STAU in review).
- (b), the f-free form, where it stands. HON′ leaves f_in: fallbacks at NON-honest states strictly between two honest states. Two routes:
  - HON-FF directly (CONJECTURE; 0 failures, but only 3 gaps with an inside fallback exist in all the data (fbin.py; hon2's 2 at n ≤ 34 are among them), so the support is THIN). A proof
    must show that W's lower bound, carried from h + 1, survives a fallback at a dishonest k (W does drop there, j10_n24) until the next
    honest state.
  - IMM′ is FALSE (§4 (v)); IMM is FALSE (§4 (iii)). The rise of Ξ is not immediate; it arrives at the next honest state.
  - What a proof of HON-FF must handle (READING): a fallback at a non-honest k inside a gap fires only if every gated edge at k is W-flat in S4a's
    arena; W can drop there and the W-level can drop (§4 (iv)), yet in all 3 such gaps in the data Ξ's level has risen by the next honest state.
