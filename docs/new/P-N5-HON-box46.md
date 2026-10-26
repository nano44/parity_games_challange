# Packet P-N5-HON (box 46): in every phase of N5 the W-honest states (Ξ = W) number at most f_in + 4n² − 3n (Lemma HON, with SAT0 / HON-FB / HON′), so the D = ∅ part of a phase costs that many states (HON-0, the stronger form of the signed REC-0); and runs with D ⊆ {u} are N5^τ runs on a one-Odd-choice game (RESTRICT_u, REPRO_u), which reduces REC for |D| = 1 configurations to f, X_dir and X_big (EP-1u, REC-1, implications from (Στ)) — every game
L-NEW successor 25 (Opus 5.5), D14 / D18, Lead reading L40; Lead's GO 09:21Z / 09:46Z (Lead's stamps): "P-N5-HON: GO … freeze P-N5-HON with
everything lane-PROVED, EP-1u and REC-1 as implications, and HON-FF / IMM′ as PROVED or as an OPEN section … State HON-0's relation to the signed
REC-0." Written 2026-10-26 09:55Z onward (date -u). FROZEN at push: later text goes into a fixes file.
Source: docs/new/N5-REC1-box46.md §0-§6 (working doc, l-new 9443948e … 0b47b9ef; this packet governs). Tools: experiments/new/box46/.
Labels: PROVED (L-NEW 25, unrefereed) / IMPLICATION / OPEN / DEAD / DATA / READING. Not a TARGET.md claim. Nothing here bounds N5's running time
on any class beyond 𝒞^1O ∪ 𝒞^1E; HON is a count of one kind of state, REC-1 is a reduction. G-N5-TIME stays open.

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | Lemma HON (W-honest states per phase ≤ f + 4n² − 3n) | PROVED (to sign) |
| §2 | Lemma SAT0; Lemma HON-FB (a fallback at a W-honest state is flat, saturating, and the phase's last transition); Corollary HON′ (f → f_in); Corollary HON-0 (D = ∅ states, N_0, D = ∅-epoch transitions) and its relation to REC-0 | PROVED (to sign) |
| §3 | Lemma RESTRICT_u, Corollary REPRO_u | PROVED (to sign) |
| §3 | Corollary EP-1u | IMPLICATION from (Στ) (to sign as an implication) |
| §4 | Theorem REC-1 (a) | PROVED (to sign) |
| §4 | Theorem REC-1 (b)-(d) | IMPLICATION from (Στ) (to sign as an implication) |
| §5 | CONJECTURE HON-FF (no f term at all); three dead routes to it | OPEN (not to sign); DEAD items with instances |
| §6 | data and climbs | DATA (not to sign) |
- Premises (LANDED unless marked):
  - SPEC S1-S5 of docs/new/N5-ssi-global.md (FIX 1-4, Q1-Q4); in particular S2 (Iσ = Ξ-improving edges), S4a (arena: Even v restricted to
    {σ(v)} ∪ Iσ(v), Odd to τ), S4c with FIX 3 (an Even fallback leaves τ; Odd falls back only if Iσ = ∅). Standing premise 1E-N3 (RESULTS R57).
  - RESULTS R15 (a) (Ξ non-decreasing along a run) and R15 (d) (at most 4n(n − 1) consecutive iterations leave both Ωσ = Ξ and Ωτ unchanged).
  - RESULTS R17 (a) (V1)/(V2), (F1)/(F2); R17 (b) Lemma P, its INDUCTION STEP only (box 10 §2 cases A1, A2, B1, B2), with R17 (d) (every
    pointwise-optimal choice); R17 (c) Theorem PH's case split (box 10 §3). QUESTION FOR THE REFEREES (Q-R17, the same as P-N5-REC0's): §1 step 1
    applies Lemma P's induction step at a state of an N5 run, not inside a switch-best run from a phase start. As I read box 10 §2, the step
    k → k + 1 uses only: the hypothesis at k, that the step's strategy is an optimum of the switch-best arena H_k, (F1)/(F2), and that no vertex
    changes its cycle node from k to k + 1. Please confirm that nothing else is used.
  - RESULTS R18 (d) Lemma S (a) (S1's valuation is the pointwise minimum over Odd's strategies; game-general) and S (c) (S4a's output is a
    pointwise optimum of its arena against τ).
  - RESULTS R21 (a) Lemma XW (Ξ_k ⊴ W_k; game-general, = (VJ) at τ′ := τ_k, RESULTS R57).
  - RESULTS R23 (g) Lemma WM (W_{k+1} ⊵ W_k at every in-phase transition that is not an S4c fallback; game-general, P-N5-XEP fixes XEP-N2).
  - RESULTS R64 (a), (b) RESTRICT_E / REPRO with the repair EPR-1 (their proofs, read with G^u in place of G′_E), and R64 (e) for the form of EP-1.
  - For the IMPLICATIONS only: premise (Στ), as in RESULTS R64 (e): RESULTS R48 (i) and R50 (h), with their chains, hold for every phase of every
    N5^τ run on every 𝒞^1O game from every start pair (packet P-N5-STAU with its fixes file P-N5-STAU-fixes-box45, sha1 42d7b04c…, is its check;
    RESULTS R65 is at CHECKER). RESULTS R51 (a) for the per-phase bound T*.
- Context (not a premise): packet P-N5-REC0-box45 (sha1 343239b5…, Lemma REC-0, in the referee queue). §2 states how HON-0 relates to it.

## 0. Setting (every game)
- N5 = SPEC S1-S5. State k = (σ_k, τ_k); σ̄_k = S1's Odd counterstrategy to σ_k; Ξ_k := V_{σ_k,σ̄_k}; W_k := V_{σ_k,τ_k}, σ_k's valuation in the
  one-player game G_τ (every Odd vertex fixed to τ_k); λ := Ξ's cycle-node map, λ_W := W's. Values and ⊴ as in VJ00 (RESULTS R15). n := |V|,
  m := |E|, Δ := the maximum out-degree.
- A PHASE P: a maximal run of consecutive states with (λ, τ) constant (RESULTS R38 (a) Remark KEY); f := its in-phase S4c fallbacks. Inside P,
  G_τ and the set of cycle nodes of λ are fixed. Q := the Odd vertices of out-degree ≥ 2; D_k := {q ∈ Q : σ̄_k(q) ≠ τ(q)}; an EPOCH is a maximal
  run of consecutive states of P with σ̄|Q constant (RESULTS R64).
- A state k of P is W-HONEST if Ξ_k = W_k pointwise. Every D = ∅ state is W-honest (σ̄_k = τ: Odd vertices outside Q have one successor). At a
  W-honest state, λ_W = λ, and Iσ_k is exactly the set of W-improving edges of G_τ at σ_k (S2 with Ξ_k = W_k).
- LEV(k) := the largest j ≤ n − 1 such that Ξ_k(x) ⪰ value(r) for every vertex x and every simple path r of G_τ with ≤ j edges from x to a
  cycle node c of λ (λ(c) = c); value(r) := (c, P(r), |r|) with P(r) the vertices of r before c that are more relevant than c (R17 Lemma P).
  B(x) := the maximum of value(r) over all such simple paths from x (any length ≤ n − 1). A state with LEV = n − 1 is SATURATED.
- f_in := the in-phase fallbacks of P at states that are NOT W-honest and lie strictly between two W-honest states of P (f_in ≤ f).

## 1. Lemma HON (PROVED, every game)
Statement. In every phase P of N5, the W-honest states of P number at most f + 4n² − 3n.
Proof.
0. (Monotone.) LEV is non-decreasing along P: Ξ_{k+1} ⊵ Ξ_k (R15 (a)), and the paths r and the cycle nodes of λ do not depend on k inside P.
   LEV ≥ 0: for a cycle node c of λ, Ξ_k(c) = (c, ∅, 0), the value of the empty path.
1. (Rise across a fallback-free gap.) Let h < h′ be W-honest states of P with no W-honest state strictly between them, and suppose no
   transition h → … → h′ is an S4c fallback (all of them are in-phase, being inside P). Then LEV(h′) ≥ min(LEV(h) + 1, n − 1).
   - W along the gap: by WM, W_{h′} ⊵ W_{h′−1} ⊵ … ⊵ W_{h+1} ⊵ W_h.
   - Cycle nodes: W_h = Ξ_h and W_{h′} = Ξ_{h′} have cycle-node map λ. The order on valuations compares the cycle node's reward first, and
     rewards are injective, so for every v the sandwiched W_{h+1}(v) has cycle node λ(v). So λ_W = λ at h and at h + 1.
   - Lemma P's induction step at h → h + 1 in G_τ (Ω := W, ρ_h := σ_h, ρ_{h+1} := σ_{h+1}, u := a cycle node of λ): at h, Iσ_h = the W-improving
     edges of G_τ, so S4a's arena is the switch-best arena of G_τ at σ_h; h → h + 1 is not a fallback, so σ_{h+1} is S4a's output, a pointwise
     optimum of that arena (R18 (d) S (c)); τ is unchanged (in-phase); no vertex changes its W-cycle node from h to h + 1 (previous bullet),
     which is what cases B1 / B2 use when they conclude "the phase ended at step k + 1, contrary to the assumption". With the hypothesis
     W_h = Ξ_h ⪰ value(r′) for |r′| ≤ LEV(h), the step gives W_{h+1}(x) ⪰ value(r) for every x and every simple r with ≤ LEV(h) + 1 edges (Q-R17).
   - So Ξ_{h′} = W_{h′} ⊵ W_{h+1} ⪰ value(r) for all such r: LEV(h′) ≥ min(LEV(h) + 1, n − 1).
2. (Saturation.) At a W-honest state h, Ξ_h(x) = W_h(x) is the value of the (σ_h, τ)-play from x, which follows a simple path r_x of G_τ to
   λ_W(x) = λ(x), a cycle node of λ, and then that cycle; so Ξ_h(x) = value(r_x) ⊴ B(x). If LEV(h) = n − 1 then Ξ_h ⊵ B, so Ξ_h = B.
3. (Count.) Let h_1 < … < h_N be the W-honest states of P. If h_i is saturated, every later h_{i′} is (step 0). Let h_1, …, h_s be the
   unsaturated ones.
   - For i < s the gap (h_i, h_{i+1}) contains a fallback or has LEV(h_{i+1}) ≥ LEV(h_i) + 1 (step 1; LEV(h_i) ≤ n − 2). The gaps are disjoint
     sets of transitions, so at most f of them contain a fallback; 0 ≤ LEV(h_1) and LEV(h_s) ≤ n − 2, so at most n − 2 are fallback-free.
     Hence s − 1 ≤ f + n − 2.
   - If s < N, put t := h_{s+1}. For i > s, Ξ_{h_i} = B = Ξ_t (step 2), so Ξ is constant on the states t, …, h_N (R15 (a)); τ is constant on P,
     so Ωτ is too; R15 (d) gives h_N − t ≤ 4n(n − 1), hence N − s ≤ 4n(n − 1) + 1.
   - N ≤ (f + n − 1) + 4n(n − 1) + 1 = f + 4n² − 3n. □

## 2. SAT0, HON-FB, HON′, HON-0 (PROVED, every game) and the relation to REC-0
Lemma SAT0. If at a state k of P the strategy σ_k has no W-improving edge in G_τ, then W_k(x) ⪰ value(r) for every x and every simple path r of
G_τ from x to a W-cycle node c (λ_W(c) = c), of any length. If k is moreover W-honest, k is saturated.
Proof. Induction on |r|. |r| = 0: W_k(c) = (c, ∅, 0). |r| ≥ 1, r = x → z → r′, r′ simple and avoiding x; W_k(z) ⪰ value(r′) by induction.
- x Even: (x, z) is not W-improving, i.e. W_k(z) ⪯ W_k(σ_k(x)); Lemma P's Case A (A1, A2), which uses only this inequality, the induction
  hypothesis, (V1) and (V2), gives value(r) ⪯ W_k(x).
- x Odd: z = τ(x). If x is not its own W-cycle node, W_k(x) = x ⊕ W_k(z) ⪰ x ⊕ value(r′) = value(r) by (V1), (V2) (r′ and z's play avoid x).
  If x is its own W-cycle node, W_k(x) = (x, ∅, 0) and z's W-play returns to x, so W_k(z) has cycle node x, while value(r′) has cycle node
  c ≠ x; W_k(z) ⪰ value(r′) then forces x better than c, so W_k(x) ≻ value(r).
At a W-honest k the W-cycle nodes are those of λ and W_k = Ξ_k, so LEV(k) = n − 1. □
Lemma HON-FB. Let h be a W-honest state of P whose transition h → h + 1 is an in-phase S4c fallback. Then (i) every W-improving edge (x, z) of
G_τ at σ_h is FLAT: x is its own cycle node and z's W-play returns to x through vertices less relevant than x; (ii) W_{h+1} = W_h; (iii) σ_{h+1}
has no W-improving edge in G_τ; (iv) h + 1 is W-honest and saturated, and it is the last state of P.
Proof. In-phase, so τ is unchanged and the fallback is Even's (FIX 3); so Iσ_h ≠ ∅ and S4a returned σ_h, which is therefore a pointwise
optimum of S4a's arena (R18 (d) S (c)); that arena is G_τ's switch-best arena (W-honest).
(i) Let (x, z) be W-improving and ρ̂ := σ_h[x → z], a strategy of the arena; so W_h(x) ⪰ W_ρ̂(x) ((F1)). Theorem PH's case split (box 10 §3)
  with this inequality in place of Lemma P's bound: if x is neither on z's path π to c := λ(z) nor on c's cycle, W_ρ̂(x) = x ⊕ W_h(z) strictly
  exceeds W_h(x) (strict (V2) if x is not its own cycle node; a better cycle node if it is): impossible. Otherwise the switch closes a cycle Z
  and Lemma P's B1 / B2 leave three outcomes: W_ρ̂(x) has a better cycle node than W_h(x) (impossible), W_ρ̂(x) = x ⊕ W_h(z) ≻ W_h(x) (B1,
  second sub-case; impossible), or B2 with D = ∅ and top(Z) = x: x is its own cycle node and W_ρ̂(x) = (x, ∅, 0) = W_h(x). Only the last remains.
(ii) S4c switches exactly the vertices x with Iσ_h(x) ≠ ∅, each to z* := the (Ξ_h(w), w)-maximum of Iσ_h(x); all are flat by (i). Each switched
  x stays its own cycle node with value (x, ∅, 0) (its new cycle has top x). A switched x′ is not on the path from z* to x (x′ is its own cycle
  node, so a play reaching x′ ends in x′'s cycle, not at x). So every play keeps its path to its cycle node and its path set: W_{h+1} = W_h.
(iii) Values are unchanged, so the W-improving edges at σ_{h+1} are judged with the same W. An unswitched vertex had none at h and keeps its
  edge. A switched x has Iσ_{h+1}(x) = {w : W_h(w) ≻ W_h(z*)}; such a w would lie in Iσ_h(x) with a larger Ξ_h = W_h value than z*.
(iv) Ξ_h ⊴ Ξ_{h+1} (R15 (a)) ⊴ W_{h+1} (XW) = W_h = Ξ_h, so Ξ_{h+1} = W_{h+1}: h + 1 is W-honest, and saturated by (iii) and SAT0. At h + 1,
  Iσ = ∅ (W-honest, (iii)), so S4a returns σ_{h+1}; then S4b changes τ, or S4c fires for Odd (Iσ = ∅, FIX 3) and changes τ, or N5 stops. So h + 1
  is the last state of P. □
Corollary HON′. In every phase P, the W-honest states number at most f_in + 4n² − 3n.
Proof. §1 step 3, sharpened: a gap (h_i, h_{i+1}) with i < s that contains a fallback cannot have it at h_i (HON-FB (iv) would make h_{i+1} =
h_i + 1 saturated, against i + 1 ≤ s); so it contains a fallback at a non-W-honest state strictly inside the gap. The gaps are disjoint, so at most
f_in of them contain a fallback, and s − 1 ≤ f_in + n − 2. □
Corollary HON-0. In every phase P: (a) the D = ∅ states number ≤ f_in + 4n² − 3n; (b) so does N_0, the number of epochs with D_E = ∅; (c) so does the
number of in-phase transitions whose source lies in a D = ∅ epoch.
Proof. D = ∅ states are W-honest; epochs are disjoint and non-empty; a transition has one source state. □
Relation to Lemma REC-0 (packet P-N5-REC0-box45, sha1 343239b5…; it is in the referee queue and is expected to land as signed):
- REC-0 states N_0 ≤ (f + 1)(n + 1) + 4n(n − 1) + 1, and its corollary bounds the transitions out of D = ∅ epochs by that number times (n + m)
  (EP-0, RESULTS R64 (c)).
- HON-0 (b) gives N_0 ≤ f_in + 4n² − 3n ≤ f + 4n² − 3n, and (f + 1)(n + 1) + 4n(n − 1) + 1 − (f + 4n² − 3n) = f·n + 2 > 0. So HON-0 (b) implies
  REC-0's inequality for every f ≥ 0 and n ≥ 1, strictly. HON-0 (c) implies REC-0's corollary (it removes the factor n + m).
- The proofs are independent: HON does not use REC-0, SN-PREFIX_D or EP-0. Both use the same Lemma P step (Q-R17), WM, R15 (a), (d) and Lemma S
  (c); HON-FB adds XW and the Theorem PH case split. REC-0 needs to be signed for nothing here; if both are signed, HON-0 is the stronger form.
- The difference in mechanism (READING): REC-0 keeps its level in W inside each fallback-free run and restarts at every fallback (so f is
  multiplied by n + 1). HON keeps the level in Ξ, which never drops in a phase, and uses W only across the gap between two consecutive W-honest
  states; a fallback costs at most one rise (f additive), and a fallback AT a W-honest state costs nothing (HON-FB).

## 3. u-runs: Lemma RESTRICT_u, Corollary REPRO_u (PROVED, every game) and Corollary EP-1u (IMPLICATION from (Στ))
- For u ∈ Q let G^u := G with every Odd v ≠ u cut to its edge τ(v); u keeps ALL its edges. G^u ∈ 𝒞^1O with d_o = deg(u). (RESULTS R64's G′_E for
  D_E = {u} is G^u with u cut further to {τ(u), σ̄_E(u)}.)
- A u-RUN of P: a maximal run J = (x, …, y) of consecutive states of P with D_k ⊆ {u} for every k ∈ J; len(J) := the in-phase transitions with
  source in J. A u-run may contain D = ∅ states and several configurations with D = {u}.
Lemma RESTRICT_u. For every state k of P with D_k ⊆ {u}, statements (i)-(iv) of RESULTS R64 (a) hold with G′_E replaced by G^u.
Proof. R64 (a)'s proof (docs/new/P-N5-EPR-box45.md §1) verbatim. It uses the epoch only in (i): "σ̄_E is an Odd strategy of G′_E and σ̄_k = σ̄_E".
Here σ̄_k is an Odd strategy of G^u: σ̄_k(v) = τ(v) for v ∈ Q ∖ {u} (as D_k ⊆ {u}), Odd vertices outside Q have one successor, and u keeps all its
edges. (ii)-(iv) use only that G^u's edges are G's, that every τ(v) is an edge of G^u, and (i). □
Corollary REPRO_u. Let J = (x, …, y) be a u-run of P and y′ := x + len(J). Then N5^τ on G^u from (σ_x, τ) passes through (σ_x, τ), …, (σ_{y′}, τ)
with the same fallback / non-fallback type at each of its len(J) transitions as N5 on G, and x, …, y lie in ONE phase of that N5^τ run (the last
transition may leave it; R64's repair EPR-1).
Proof. R64 (b)'s induction (P-N5-EPR §2) verbatim, with RESTRICT_u at each k ∈ [x, y′ − 1] ⊆ J. □
Corollary EP-1u (IMPLICATION from (Στ)). Every u-run J has len(J) ≤ T*(G^u) + 1, where T*(G^u) is RESULTS R51 (a)'s per-phase bound (R50 (h) with
f := 2n²) at G^u's parameters (n, m^u ≤ m, Δ^u ≤ Δ, d_o = deg(u)), a polynomial.
Proof. As R64 (e): by REPRO_u the len(J) transitions are, except possibly the last, in-phase transitions of one phase of an N5^τ run on G^u ∈
𝒞^1O; under (Στ) that phase has at most T*(G^u) of them. □
- Size (READING, not a separate claim): R64 (e) reads T* at d_o = 2 as O(m·Δ·n¹¹); the same reading at d_o = deg(u) gives O(m·Δ·d_o·n¹¹).
- EP-1u contains R64's EP-1 (an epoch with D_E = {u} lies in one u-run) and covers a whole run of epochs whose configurations differ only at u,
  interleaved with D = ∅ epochs.

## 4. Theorem REC-1 (a PROVED; (b)-(d) IMPLICATIONS from (Στ); a REDUCTION)
Definitions (phase P). A {u}-INTERVAL: a maximal run of consecutive states of P with D_k = {u}. X_dir(P): the in-phase transitions k → k + 1 with
|D_k| = |D_{k+1}| = 1 and D_k ≠ D_{k+1}. X_big(P): the in-phase transitions with |D_k| ≥ 2 and |D_{k+1}| = 1. T*_Q := max over u ∈ Q of T*(G^u).
Statement. In every phase P of N5 on any game:
(a) the {u}-intervals of P, over all u ∈ Q, number at most 1 + (f_in + 4n² − 3n) + X_dir + X_big;
and, under (Στ):
(b) every {u}-interval has at most T*(G^u) + 2 states;
(c) the states with |D_k| = 1 number at most (1 + f_in + 4n² − 3n + X_dir + X_big)·(T*_Q + 2), and so do the epochs with |D_E| = 1; in particular,
    for every configuration C with |D_C| = 1, the C-epochs of P number at most that;
(d) if every state of P has |D_k| ≤ 1, then X_big = 0 and P has at most (f_in + 4n² − 3n) + (1 + f_in + 4n² − 3n + X_dir)·(T*_Q + 2) states.
Proof.
(a) A {u}-interval I that does not start at P's first state starts at the target k + 1 of an in-phase transition k → k + 1 with D_k ≠ {u}: either
    D_k = ∅ (k is a D = ∅ state; distinct intervals have distinct k; HON-0 (a) bounds these k), or |D_k| = 1 (a transition of X_dir), or |D_k| ≥ 2
    (X_big). One more interval may start at P's first state.
(b) A {u}-interval I lies in one u-run J. Every state of I except possibly the last state of P is the source of an in-phase transition with
    source in J, so |I| ≤ len(J) + 1 ≤ T*(G^u) + 2 (EP-1u).
(c) Every state with |D_k| = 1 lies in exactly one {u}-interval; (a) × (b). Epochs are disjoint and non-empty, and a |D_E| = 1 epoch consists of
    |D| = 1 states.
(d) No state has |D| ≥ 2, so X_big = 0. States of P = D = ∅ states (HON-0 (a)) + |D| = 1 states ((c)). □
- What REC-1 gives (READING). CONJECTURE REC (docs/new/N5-NEP-box45.md §2) for configurations with |D| = 1 is REDUCED to f_in, X_dir and X_big
  (under (Στ)). In the data the long phases are of type (d) with X_dir = 0, and the recurrences of a |D| = 1 configuration happen INSIDE one
  {u}-interval (lev_l_x: 49 epochs in one {u}-interval), where EP-1u bounds them as a whole.
- Not addressed: X_dir, X_big (D-changes into a singleton not via D = ∅; a special case of RESULTS R55's CONJECTURE Δ1), f on general games
  (RESULTS R56: ρ), epochs with |D| ≥ 2.

## 5. OPEN: CONJECTURE HON-FF (the f-free form) and three dead routes to it (not to sign)
- CONJECTURE HON-FF: across EVERY gap between consecutive W-honest states of a phase, LEV(h_{i+1}) ≥ min(LEV(h_i) + 1, n − 1), fallbacks inside
  the gap included. It would give: W-honest states per phase ≤ 4n² − 3n (no f term), hence HON-0 and REC-1 (a) without f_in.
- What is proved toward it: fallback-free gaps (§1 step 1) and gaps whose fallback is at the first state (HON-FB). OPEN: gaps containing a
  fallback at a non-W-honest state (f_in). Such a fallback fires only if every gated edge at that state is W-flat in S4a's arena.
- DATA: 0 failures. hon2.py: lib41 n ≤ 34 (1,689 gaps), random 3,000 𝒞^kO (2,984 gaps). THIN where it matters: only 3 gaps with an inside
  fallback exist in all the data (fbin.py over all of lib41: j10_n24 LEV 1 → 4, j7_n32 0 → 19, j8_n32 2 → 9; hon2's 2 at n ≤ 34 are among them;
  none in the random sample), all rise; ffclimb.py never produced a new one. Routed by the Lead to L-COMP 5 as a falsification add-on.
- DEAD routes (each with its instance; experiments/new/box46/, S3 start unless stated):
  - IMM, "LEV(h + 1) ≥ LEV(h) + 1 after a non-fallback in-phase step from a W-honest h": FALSE. instances/immfail_n14.pg (sha1
    db3fc2ca2ef48523166d93ce0eff072e1eb8d33e), h = 0 (LEV 3 → 3, split) and h = 2 (3 → 3); both h + 1 are the last state of their phase.
  - IMM′, "IMM whenever h + 1 is not the last state of its phase": FALSE. Hand-built instances/immp_cex_n11.pg (sha1
    1dd7f5853103bb0698cd7e3cbc220a70df5d24ee) with start instances/immp_cex_n11.start (sha1 18cf37667017b1f0244731e0719ac878568eb8fb): one cycle
    node (0, a self-loop), one Odd choice q = 3 with τ(3) = 4 Odd-optimal for the whole game (Iτ = ∅); x = 1 keeps σ(1) = 2 → q because W(4) rises
    through 4 → 8 (priority 30), while the honest reply at q switches to 5, whose potential 5 → 6 → 10 (priority 40) needs two steps; Ξ_1(1) =
    (0, {1, 2, 3, 5}, 4) is below value(1 → 7 → 0) = (0, {1, 7}, 2), so LEV 1 → 1 at a state that is not the last of its phase; state 2 is W-honest
    with LEV 10. In the library: exitr_cex_n16 (experiments/red/so/instances/, random start, h = 2, LEV 1 → 1). Obstruction: τ's value-optimality
    in S4b's arena binds Odd only on τ ∪ Iτ, and Iτ is read from Even's G_τ-OPTIMUM, not from σ.
  - FB-WLEV, "an in-phase fallback never lowers the W-level": FALSE. experiments/n5-exhaustive/instances/b5_o11.pg (sha1
    db4fe55a650236dfe1bc5030f0ca123c75754764), fallback 7 → 8, W-level 6 → 5 (14 of 166 fallbacks at non-honest states, lib41 n ≤ 24). On the same
    run the Ξ-level climbs through the non-honest stretch and the next honest state has LEV 9: HON-FF holds there, not by carrying W.
- Also DEAD (context for §4, not a route to HON-FF): the permanent Ξ-level in H_C as a REC potential for |D_C| = 1
  (experiments/si/orlens/instances/thclimb_n12_s11.pg, sha1 e3b47b6e…: inside one {u}-interval σ̄(u) moves 10 → 2 → 3 → 2 → 10 and LEV_C stays 1;
  133 of 453 fallback-free gaps between C-epochs do not rise, lib41 n ≤ 34); and "no in-phase fallback at a W-honest state"
  (experiments/n5-exhaustive/instances/b4_n5_other_0.pg, sha1 6115e60a…: the flat cycle-closing switch; replaced by HON-FB).

## 6. DATA (not to sign; experiments/new/box46/, README.md lists every run; outputs in out/)
- hon.py (HON, HON-FB): HON_V = 0, WMC_V = 0 (the WM chain of §1 step 1), D0NOTHON_V = 0, FBH_LAST_V = FBH_HON_V = FBH_FLAT_V = 0.
| sample | runs | phases | max W-honest states in a phase | fallbacks at W-honest states (all last, flat, honest target) | f_in (gaps) |
| --- | --- | --- | --- | --- | --- |
| lib41 (n ≤ 64), S3 + 2 random starts, seed 7 | 1,101 | 5,377 | 57 | 56 | 4 (3) |
| 3,000 random 𝒞^kO (k 2-4, n 5-18, games seed 111), S3 + 4 random, seed 8 | 15,000 | 40,203 | 4 | 546 | — |
- dint.py (REC-1 (a) and HON-0 (b) per phase): 0 violations on both samples; {u}-intervals 2,330 / 12,239, entered from D = ∅ 204 / 130, from {u′}
  (X_dir) 1 / 15, from |D| ≥ 2 (X_big) 12 / 32, at the phase start 2,113 / 12,062; max epochs in one {u}-interval 49 / 2; phases with all |D| ≤ 1:
  3,814 (max N_ep 50, max X_dir 0) / 30,360 (max N_ep 3, max X_dir 1).
- hon2.py (§1 step 1 and HON-FF): no gap without a rise, fallback-free or not (lib41 n ≤ 20: 472 gaps; n ≤ 34: 1,689; random: 2,984).
- imm.py (IMM, IMM′; the W-level rise of §1 step 1 at unsplit h + 1): WIMM UNSPLIT = 0 in every sample; IMM failures 0 / 5 / 3 (lib41 n ≤ 20 /
  random / lib41 n ≤ 34), IMM′ failures 0 / 0 / 2.
- Reproduce (from experiments/new/box46): `python3 hon.py 2 7 --list ../box41/lib41.txt`; `python3 hon.py 4 8 --rand 3000 5 18 111`; the same
  arguments for dint.py; `python3 hon2.py 2 7 --list ../box41/lib41.txt --nmax 34 --budget 3000000`; `python3 imm.py …` likewise.
