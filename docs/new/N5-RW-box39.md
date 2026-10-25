# N5 on o-cyclic 𝒞^1O, box 39 (1): R̄-rises with θ fixed. Inside a block, the route part above max(c_θ, c_w) freezes in N − 1 transitions (Bellman-Ford dominance, Lemma BF-RW / Theorem FREEZE-M); every remaining rise is a length rise (polynomial) or, when c_w is above c_θ, a fallback, a W-length step (polynomial) or a W-TIE step (OPEN)
L-NEW successor 18 (Opus 5.5, D15/D18), session_01BhkSHzG2cPM2Rdbj5Y2NJV. Box 39 (1), the Lead's GO of 14:29Z (Lead's stamp): "RW_S, the
R̄-rises after c_w ≠ o evictions with θ fixed ... Look for a count of route improvements in R." Written 2026-10-25 14:4xZ onward by date -u.
- Setting and notation: docs/new/P-N5-OUT-box37.md §0 (sha1 9f032e61…), docs/new/N5-TAUW-box38.md (sha1 e194ffe4…). N5 = SPEC S1-S5 on
  𝒞^1O; HN := H1 ∧ ¬H2; c_θ := λ(o), c_w := λ_W(o) = the top of o's W-cycle C_W; R, R̄ = R ∪ {o}, F, routes π_z as there.
- Labels (D18/L40): PROVED (L-NEW succ. 18, unrefereed), CONJECTURE, FALSE, OPEN, DATA, READING. Nothing here is a running-time bound
  for N5, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN. Nothing uses (P).
- Names (Lead 15:01Z): Lemma BF-RW was "BF" in l-new 79322603 (clash with P-N5-ENT's BF); FB-ROUND was "FBF" in a29bd8ac (clash
  with box 27's FBF, P-N5-XA); W-TIE was "TIE". Script output keys keep the old names (FAIL_BFM, FAIL_BFX, FAIL_FBF, TIE_total).
- Cross-field idea (D18; READING, no source cited as a premise): with θ fixed, honest values on R̄ are ADDITIVE path weights to the target
  o (the route form), so N5 restricted to R̄ behaves like policy iteration for a deterministic longest-path problem. The Bellman-Ford
  argument (after m rounds every vertex is at least as good as its best path of ≤ m edges) is the tool. The fleet already used it for
  one-player games (RESULTS R17 (b) Lemma P). Here it is applied to the part of the route weight above T* := max(rank c_θ, rank c_w),
  which is the common major part of the honest order and the W order. That is why both N5 step kinds (S4a, which optimises W, and S4c,
  which is honest-greedy) obey it.

## Summary
1. **Lemma BF-RW (PROVED).** In a block (a maximal run of consecutive in-phase HN states with θ, R̄ and c_w constant), at every transition
   k → k+1 of the block, every v ∈ R and every successor x ∈ R̄ of v satisfy M_{k+1}(v) ≥ wt(v) + M_k(x). Here M is the signed weight of
   the route above T*.
2. **Theorem FREEZE-M (PROVED).** In a block [a, b] with N := |R̄|, M_t(z) = Mopt(z) (the best simple path weight in G[R̄]) for every
   z ∈ R̄ and every state t ≥ a + N − 1. So at most N − 1 transitions of a block have a rise at a level > T* (an "M-rise").
3. **Lemma ROUTE-LEN (PROVED).** In a block with rank(c_w) < rank(c_θ), at most (N − 1) + N(N − 1) transitions have an R̄-rise.
4. **Lemma W-POT (PROVED).** In a block with rank(c_w) > rank(c_θ), after the freeze, the S4a transitions that change W on R̄ number at
   most (f_B + 1)·N(n − 1), where f_B ≤ K = n_E(2n − 1) is the number of fallback transitions of the block (FB-INT, RESULTS R38 (d)).
5. **Corollary BLOCK-RED (PROVED).** In a block with rank(c_w) > rank(c_θ), the number of transitions with an R̄-rise is at most
   (N − 1) + K + (K + 1)·N(n − 1) + TIE_B. TIE_B counts the W-TIE steps of the block: S4a transitions with W unchanged on R̄ and an honest
   R̄-rise, which is always a band or length rise.
6. **Lemma CW-COUNT (PROVED).** In a run of consecutive in-phase HN states with f fallback transitions, c_w changes at most
   (f + 1)(n − 1) + f times.
7. **Theorem FREEZE-X (PROVED).** The M-freeze survives evictions. In a θ- and c_w-constant HN run, an M-rise is an entry or lies
   within n − 2 transitions after the last entry (or the run start). So a break whose eviction comes ≥ n − 1 transitions after the
   previous entry is charged by RISE to a band or length rise, and to a length rise when rank(c_w) < rank(c_θ).
8. **Obstruction (exact; why this does not bound RW_S yet).** Every count above is per reset (per entry), and every break is an entry.
   RISE's charging (B_S ≤ θ_S + RR_S) is therefore circular with these bounds: rise counting alone cannot bound breaks. An entry itself has
   to pay, for example through an EXIT-UP potential (§7, (E1)/(E2), OPEN).
9. **Theorem P-FREEZE and BRK-POLY (PROVED, §11; supersedes 7-8 for counting breaks).** In a θ-constant run of a phase, the
   fallbacks are Bellman-Ford rounds on U = λ^{-1}(c_θ), so P is frozen on U after |U| − 1 fallbacks. Every break consumes its own fallback (its
   eviction), so B_S ≤ θ_S + (θ_S + 1)(n² − 1) for every HN stretch, any τ(o), any c_w; in case A, B_S ≤ θ_S + (θ_S + 1)(|U| − 1). With EPOCH,
   crossings and fallbacks per HN stretch are polynomial in n and θ_S. OPEN as before: θ_S, HN stretches per phase (τ(o) ≠ o), OTHER states.
10. **DATA.** Lemma BF-RW (and BF-RWX across 177 crossings) is checked at every transition of every block (library, all box-37/38 instances, climbs): 0 failures. FREEZE: the
   last M-rise is always at an index < n − 1 (max 13 at n = 24). F1 monotonicity of W at S4a: 0 failures. W-TIE steps exist (library: 2;
   climb: 4 in one block at n = 24). Random 𝒞^1O games give no HN blocks (20,110 games, n 6..16).

## 0. Blocks and the M-part
- A BLOCK is a maximal run [a, b] of consecutive states of one phase, all HN, with θ, R̄ and c_w constant. Its transitions are k → k+1
  with a ≤ k < b. A block lies inside a crossing-free run of the phase (R̄ is constant), so it has ≤ K fallback transitions (FB-INT,
  RESULTS R38 (d)).
- T* := max(rank(c_θ), rank(c_w)) (c_θ ∈ F and c_w ∈ R̄ under H1 ∧ ¬H2 (P-N5-OUT §1 (a)), so c_θ ≠ c_w and the ranks differ).
- sgn(u) := +1 if Ω(u) is even, −1 if odd. wt(u) := sgn(u)·2^rank(u) if rank(u) > T*, else 0. For a set A of vertices, wt(A) := Σ_{u∈A} wt(u).
  - (O) For sets A, B: wt(A) > wt(B) iff A ∩ V_{>T*} ≠ B ∩ V_{>T*} and the top vertex of (A Δ B) ∩ V_{>T*} is even and lies in A
    (distinct powers of 2). wt(A) = wt(B) iff A ∩ V_{>T*} = B ∩ V_{>T*}.
- For z ∈ R̄_k: M_k(z) := wt(π_z^k). Routes are simple paths, so M_k(z) is a set weight; M_k(o) = 0 (π_o = ∅). For v ∈ R_k with
  successor y on its play, π_v = v · π_y, so M_k(v) = wt(v) + M_k(y).
- Facts used (all from the honest/W route forms; dependencies table in §8):
  - (RF) Route form (P-N5-OUT §4, proof of FREEZE-STEP): at an H1 state, for z ∈ R̄, Ξ_k(z) = π_z ⊕ θ_k, with P(Ξ_k z) =
    (π_z ∩ V_{>c_θ}) ⊔ P(θ_k), where P(θ_k) ⊆ {o} ∪ F_k is disjoint from the route (P-N5-OUT §5 BASE (ii)).
  - (M1) For y, z ∈ R̄_k at an H1 state: Ξ_k(y) ⊴ Ξ_k(z) ⇒ M_k(y) ≤ M_k(z); and M_k(y) < M_k(z) ⇒ Ξ_k(y) ◁ Ξ_k(z).
    Proof: same cycle node c_θ; P(Ξ y) Δ P(Ξ z) = (π_y Δ π_z) ∩ V_{>c_θ}. If its part above T* is nonempty, its top is the top of the
    whole difference (T* ≥ rank c_θ) and decides both the honest order and the sign of M_k(z) − M_k(y), by (O). Otherwise the M-values
    are equal. □
  - (M2) If θ_{k+1} = θ_k, both states are H1 and z ∈ R̄_k ∩ R̄_{k+1}, then M_{k+1}(z) ≥ M_k(z). Proof: R15 (a) Ξ_{k+1}(z) ⊵ Ξ_k(z);
    both values have the form π ⊕ θ with the same θ, and (M1)'s argument across the two states applies. □
  - (WF) W-form. At an HN state, for z ∈ R̄_k, W_k(z) has cycle node c_w and P(W_k z) = π_z ∩ V_{>c_w}.
    Proof: z's (σ_k, τ)-play follows π_z to o and then o's W-cycle C_W, whose top is c_w. So the cycle node is c_w, and P is the set of
    vertices of rank > rank(c_w) on the play before its first visit of c_w. That prefix lies in π_z ∪ C_W. Vertices of C_W have rank
    ≤ rank(c_w). If c_w ∈ π_z, the part of π_z after c_w is c_w's own route, which runs along C_W. So P = π_z ∩ V_{>c_w}. □
    Consequence (W1): for y, z ∈ R̄_k at an HN state, W_k(y) ⊴ W_k(z) ⇒ M_k(y) ≤ M_k(z) (T* ≥ rank c_w; as (M1)). (WF)'s argument
    applies to the value of any play that reaches o and then runs around C_W with cycle node c_w.
  - (F1) RESULTS R17 (a): the optimum of a one-player game dominates every strategy of that game pointwise. At an S4a step, σ_{k+1} is
    the optimum of Even's one-player game on the arena H_k against τ, so W_{k+1} ⊵ W_{σ''} pointwise for every strategy σ'' of the
    arena; in particular W_{k+1} ⊵ W_k (σ_k is an arena strategy).

## 1. Lemma BF-RW (PROVED, L-NEW succ. 18; 𝒞^1O)
Statement. Let k → k+1 be a transition of a block. Then:
- (a) for every Even v ∈ R and every successor x of v with x ∈ R̄: M_{k+1}(v) ≥ wt(v) + M_k(x);
- (b) for every Odd v ∈ R (forced, unique successor x): M_{k+1}(v) = wt(v) + M_{k+1}(x) ≥ wt(v) + M_k(x).
Proof.
- (b) v ∈ R_k ∩ R_{k+1} (R̄ constant), so π_v = v · π_x at both states. Then (M2). □
- (a) Write y := σ_k(v), so M_k(v) = wt(v) + M_k(y).
  - Case 1: M_k(x) ≤ M_k(y). Then wt(v) + M_k(x) ≤ M_k(v) ≤ M_{k+1}(v) by (M2).
  - Case 2: M_k(x) > M_k(y). By (M1), Ξ_k(x) ▷ Ξ_k(y), so (v, x) ∈ Iσ_k.
    - 2a, the transition is a fallback (S4c). v has an improving edge, so σ_{k+1}(v) = x* with Ξ_k(x*) ⊵ Ξ_k(x) (S4c maximises).
      v ∈ R_{k+1}, so π_v^{k+1} = v · π_{x*}^{k+1} and x* ∈ R̄_{k+1} = R̄_k. Hence
      M_{k+1}(v) = wt(v) + M_{k+1}(x*) ≥ wt(v) + M_k(x*) ≥ wt(v) + M_k(x), by (M2) and (M1).
    - 2b, the transition is an S4a step. x ∈ A_k(v) (an improving edge), so σ'' := σ_k with v ↦ x is a strategy of the arena H_k.
      By (F1), W_{k+1}(v) ⊵ W_{σ''}(v). By (WF) at k+1 (v ∈ R_{k+1}), W_{k+1}(v) has cycle node c_w. Three sub-cases.
      - (i) π_x^k passes v. Then π_x^k = q · v · π_y^k with q, {v}, π_y disjoint, and M_k(x) = wt(q) + wt(v) + M_k(y). Case 2 gives
        wt(q ∪ {v}) > 0. Under σ'', v's play is the cycle Z: v → x → q → v, with vertex set q ∪ {v}. By (O), Z has a vertex above T*,
        and the top of Z ∩ V_{>T*} is even; it is the top u of Z. So u is the cycle node of W_{σ''}(v), with reward(u) = p′(u) >
        p′(c_w) ≥ reward(c_w) (rank(u) > T* ≥ rank(c_w)). The order compares cycle-node rewards first, so W_{σ''}(v) ▷ W_{k+1}(v),
        against (F1). Impossible.
      - (ii) π_x^k avoids v and v ∈ C_W (at k).
        - Write C_W as o = c_0 → c_1 → … → c_m → o with v = c_i. v's route is c_i … c_m, inside C_W, so all its vertices have rank
          ≤ rank(c_w) ≤ T*: M_k(y) = 0, and Case 2 gives M_k(x) > 0. Let u be the top of π_x^k ∩ V_{>T*}; by (O) it is even.
        - π_x^k contains no c_j with j < i: from c_j the route runs along C_W through c_i = v.
        - So under σ'', o's play is c_0 … c_i, then x · π_x^k back to o: a cycle Z′ through v. Its vertices above T* are those of π_x^k,
          so its top is u.
        - Hence W_{σ''}(v) has cycle node u, and as in (i), W_{σ''}(v) ▷ W_{k+1}(v), against (F1). Impossible.
      - (iii) π_x^k avoids v and v ∉ C_W. Under σ'', o's play is still C_W (it does not visit v), and x's play is π_x^k followed by
        C_W, avoiding v. So v's play under σ'' is v · π_x^k followed by C_W. By (WF) for this play, W_{σ''}(v) has cycle node c_w and
        P ∩ V_{>T*} = ({v} ∪ π_x^k) ∩ V_{>T*}. W_{k+1}(v) ⊵ W_{σ''}(v) with the same cycle node, so the P-parts satisfy (W1):
        M_{k+1}(v) ≥ wt(v) + M_k(x). □
- Remark. In Case 2b the arena optimum may pick an edge other than x for v. The lemma bounds only the M-part of v's new route.

## 2. Theorem FREEZE-M (PROVED, L-NEW succ. 18; 𝒞^1O)
Statement. Let [a, b] be a block, N := |R̄|, and G[R̄] the graph on R̄ with all edges of G for Even vertices of R, the forced edge for
Odd vertices of R, and o as a sink. Mopt(z) := max{wt(p ∖ {o}) : p a simple path from z to o in G[R̄]}. Then:
- (a) for every m with a + m ≤ b, every z ∈ R̄ and every simple path p from z to o in G[R̄] with ≤ m edges: M_{a+m}(z) ≥ wt(p ∖ {o});
- (b) M_t(z) = Mopt(z) for every state t ∈ [a + N − 1, b] and every z ∈ R̄;
- (c) at most N − 1 transitions of the block have an M-rise (a rise of some z ∈ R̄ with lev > T*).
Proof.
- (a) By induction on m. For m = 0, p is the trivial path at z = o, and M(o) = 0. For m + 1, write p = z · p′, with p′ a simple path
  from the successor x ∈ R̄ of z, with ≤ m edges. Then wt(p ∖ {o}) = wt(z) + wt(p′ ∖ {o}) ≤ wt(z) + M_{a+m}(x) ≤ M_{a+m+1}(z), by the
  hypothesis and Lemma BF-RW (a) or (b) at the transition a+m → a+m+1.
- (b) A simple path in G[R̄] has ≤ N − 1 edges, so (a) gives M_t(z) ≥ Mopt(z). The route π_z^t followed by o is a simple path in
  G[R̄], so M_t(z) ≤ Mopt(z).
- (c) By (M1)/(M2), an M-rise of z at t → t+1 is M_{t+1}(z) > M_t(z). By (b) this needs t < a + N − 1. □
- Remark (no positive-cycle issue). Only simple paths enter (a), so cycles of positive M-weight inside R do not matter.

## 3. Lemma ROUTE-LEN (PROVED, L-NEW succ. 18) — blocks with rank(c_w) < rank(c_θ)
Statement. In a block [a, b] with rank(c_w) < rank(c_θ), at most (N − 1) + N(N − 1) transitions have an R̄-rise.
Proof.
- T* = rank(c_θ), so M_k(z) is the weight of the whole honest route part P(Ξ_k z) ∖ P(θ) (RF). Two values of R̄ with equal M differ
  only in length, |π_z| + ℓ(θ).
- s_θ := +1 if Ω(c_θ) is odd (longer is better for Even), −1 if even. Ψ_t := Σ_{z ∈ R̄} s_θ·|π_z^t|.
- For t ≥ a + N − 1, M is frozen (FREEZE-M (b)). By R15 (a), each z then has s_θ|π_z| non-decreasing, at fallbacks too. A transition
  with an R̄-rise raises Ψ by ≥ 1. Ψ ranges over an interval of length ≤ N(N − 1) (|π_z| ∈ [0, N − 1]).
- Before a + N − 1 there are ≤ N − 1 transitions. □

## 4. Lemma W-POT and Corollary BLOCK-RED (PROVED, L-NEW succ. 18) — blocks with rank(c_w) > rank(c_θ)
Statement (W-POT). Let [a, b] be a block with rank(c_w) > rank(c_θ), so T* = rank(c_w). s_w := +1 if Ω(c_w) is odd, −1 if even.
Φ_t := Σ_{z ∈ R̄} s_w·ℓ(W_t z), with ℓ(W z) the W-length (steps to the cycle node c_w), in [0, n − 1]. For an S4a transition
t → t+1 of the block with t ≥ a + N − 1: Φ_{t+1} ≥ Φ_t, with equality iff W_{t+1} = W_t on R̄. Hence, for t ≥ a + N − 1, the S4a
transitions that change W on R̄ number at most (f_B + 1)·N(n − 1), where f_B ≤ K.
Proof.
- By (WF), for z ∈ R̄ the value W_t(z) is (c_w, π_z ∩ V_{>T*}, ℓ). After the freeze the route sets above T* are constant (FREEZE-M (b)
  and (O)), so W_t and W_{t+1} differ on R̄ only in lengths.
- (F1) gives W_{t+1}(z) ⊵ W_t(z), i.e. s_w ℓ non-decreasing for each z, strictly for some z iff W changes on R̄.
- Fallback transitions split [a + N − 1, b] into ≤ f_B + 1 fallback-free pieces. On each, Φ only increases, by ≥ 1 at each counted
  transition, and its range has length ≤ N(n − 1). □
Corollary BLOCK-RED. In a block with rank(c_w) > rank(c_θ), the transitions with an R̄-rise are:
- M-rises: ≤ N − 1 (FREEZE-M (c));
- after the freeze, fallbacks: ≤ f_B ≤ K;
- S4a transitions changing W on R̄: ≤ (K + 1)·N(n − 1) (W-POT);
- W-TIE steps: S4a transitions with W unchanged on R̄ and an R̄-rise. Their rises are band rises (lev ∈ (rank c_θ, rank c_w]) or honest
  length rises, since an M-rise changes W (WF).
So in total ≤ (N − 1) + K + (K + 1)·N(n − 1) + TIE_B. □
- Structure of a W-TIE step (PROVED, from the above). W is unchanged on R̄, so σ_k and σ_{k+1} are both W-optimal for the arena H_k on
  R̄. Every R-vertex's options in both lie in Opt(v) := {x ∈ succ(v) ∩ R̄ : v ⊕ W(x) = W(v)}, a fixed set while W is fixed. The routes
  of a W-fixed stretch therefore live in the subgraph of W-optimal edges, layered by W-length (each edge lowers ℓ(W) by 1). On it the
  honest order is the band weight, then the honest length. A run of W-TIE steps is a sequence of honest-improving switches inside this
  fixed layered graph, with the switch chosen by the S1 procedure's tie-breaks (BFS discovery order or smallest index, docs/new/
  N5-ssi-global.md FIX 2, FIX 4). OPEN: a polynomial bound on TIE_B. On a layered DAG, arbitrary improving single switches can take
  many steps; N5's tie-break is not arbitrary, but nothing about it is proved here.

## 5. Lemma CW-COUNT (PROVED, L-NEW succ. 18)
Statement. In a run of consecutive in-phase HN states with f fallback transitions, c_w changes at ≤ (f + 1)(n − 1) + f transitions.
Proof. c_w is the cycle node of W(o). At an S4a transition, (F1) gives W_{t+1}(o) ⊵ W_t(o). The order compares cycle-node rewards
first, and rewards are injective, so a change of c_w at S4a strictly raises reward(c_w): ≤ n − 1 changes per fallback-free piece.
There are ≤ f + 1 pieces, plus ≤ f changes at the fallbacks themselves. □
- So a θ-constant crossing-free HN run of a phase splits into ≤ (K + 1)(n − 1) + K + 1 blocks.

## 6. Consequences, and the obstruction (exact)
- (PROVED) Let C be a crossing-free run of a phase whose states are all HN with θ constant. Its transitions with an R̄-rise number at
  most
  (#blocks of C)·(1 + (N − 1) + K + (K + 1)·N(n − 1)) + Σ_B TIE_B,
  with #blocks ≤ (K + 1)(n − 1) + K + 1. The leading "1" counts each block-boundary transition (a c_w change). Blocks with
  rank(c_w) < rank(c_θ) have TIE_B = 0 (ROUTE-LEN). So inside a crossing-free θ-constant HN run, R̄-rises are polynomial up to W-TIE steps.
- (Obstruction, first form; sharpened in §7) This does not bound RW_S or B_S.
  - A break's window [a, k] runs from an eviction (a crossing) to an entry (a crossing), so every window contains block boundaries.
  - RISE gives B_S ≤ θ_S + RR_S. The bound above gives RR_S ≤ (crossing-free runs of S)·poly + W-TIE.
  - Crossing-free runs of S number ≤ X_S + 1, and EPOCH gives only X_S ≤ 2(n − 1)(B_S + 1).
  - The chain B ≤ θ + (X + 1)·poly ≤ θ + (2(n − 1)(B + 1) + 1)·poly is circular: per-block freezing alone cannot exclude a run in which
    every block contributes one rise that feeds one break.
  - What is missing is FREEZE-M ACROSS crossings, i.e. Lemma BF-RW for the vertices that stay in R̄ through an eviction or an entry, plus a
    rule for re-entering vertices. §7 proves the across-evictions part (FREEZE-X); entries remain.

## 7. Theorem FREEZE-X: the M-freeze survives evictions (PROVED, L-NEW succ. 18; 𝒞^1O)
Setting. U = [a, b] is a run of consecutive in-phase HN states with θ and c_w constant; crossings are allowed. By SPLIT, every crossing
of U is an entry (at S4a) or an eviction (at a fallback), never both. A state s ∈ U is a RESET if s = a or s − 1 → s is an entry.
G[R̄_t] and Mopt_t are as in §2, for the set R̄_t.
- Lemma BF-RWX (PROVED). Lemma BF-RW (a), (b) hold at every transition k → k+1 of U, for every v ∈ R_k ∩ R_{k+1} and every successor
  x ∈ R̄_k of v.
  Proof: the proof of §1 word for word. It uses only v ∈ R_k ∩ R_{k+1} (route form of v at both states, (WF) at k+1 for v), x ∈ R̄_k
  (route form at k), and (M2) for v (Case 1) or for x* (Case 2a). In 2a, v ∈ R_{k+1} forces x* ∈ R̄_{k+1}. In (b), v's forced successor
  lies in R̄_{k+1}. □
- Theorem FREEZE-X. Let s ≤ t in U, with no entry among the transitions of [s, t).
  - (a) For every z ∈ R̄_t and every simple path p from z to o in G[R̄_t] with ≤ t − s edges: M_t(z) ≥ wt(p ∖ {o}).
  - (b) If t − s ≥ |R̄_t| − 1, then M_t = Mopt_t on R̄_t. For every t′ ≥ t with no entry in [t, t′), M_{t′} = M_t on R̄_{t′}.
  - (c) So a transition t → t+1 of U with an M-rise is an entry, or has t − s < |R̄_t| − 1 ≤ n − 2, where s is the last reset ≤ t.
    U has at most (n − 1)(E + 1) + E M-rise transitions, where E is its number of entries.
  Proof.
  - (a) Induction on t − s. If t = s, the only path with 0 edges is the one at z = o, and M(o) = 0.
  - For the step t → t+1 (not an entry), R̄_{t+1} ⊆ R̄_t (SPLIT). Write p = z · p′, a path in G[R̄_{t+1}], with p′ starting at x.
    - p′ is a path in G[R̄_t] with ≤ t − s edges, so the hypothesis gives M_t(x) ≥ wt(p′ ∖ {o}).
    - z ∈ R_{t+1} ⊆ R_t and x ∈ R̄_t, so BF-RWX gives M_{t+1}(z) ≥ wt(z) + M_t(x) ≥ wt(p ∖ {o}).
  - (b) Simple paths in G[R̄_t] have ≤ |R̄_t| − 1 edges, and routes are such paths, so Mopt_t ≤ M_t ≤ Mopt_t. For t → t+1 not an entry:
    - G[R̄_{t+1}] is a subgraph of G[R̄_t], so Mopt_{t+1} ≤ Mopt_t;
    - every z ∈ R̄_{t+1} is in R̄_t, so (M2) gives M_t(z) ≤ M_{t+1}(z);
    - hence M_{t+1}(z) ≤ Mopt_{t+1}(z) ≤ Mopt_t(z) = M_t(z) ≤ M_{t+1}(z), and t + 1 − s ≥ |R̄_{t+1}| − 1 again. Induction.
  - (c) An M-rise at a non-entry transition t → t+1 means M_{t+1}(z) > M_t(z) for some z ∈ R̄_t ∩ R̄_{t+1}, which (b) excludes when
    t − s ≥ |R̄_t| − 1. Each reset is followed by ≤ n − 1 such transitions, and there are ≤ E + 1 resets. □
- Consequences for breaks (PROVED). Take a break of an HN stretch whose window [a, k] (a the eviction, k the entry) lies in one θ- and
  c_w-constant run, and let e be the last entry before a (or the run start).
  - If a ≥ e + n − 1, no transition of [a, k) is an M-rise, by FREEZE-X (c).
  - So RISE's rise for this break is a band rise (rank(c_θ) < lev ≤ T*) or a length rise.
  - When rank(c_w) < rank(c_θ) there is no band, so it is a length rise.
- The obstruction, sharpened (exact). Inside the windows, R̄-rises are now polynomial between two entries, up to W-TIE steps:
  - M-rises by FREEZE-X;
  - length rises after the freeze by the Ψ-argument of ROUTE-LEN, applied between two resets (vertices only leave R̄ there, and each
    staying vertex's s_θ|π| only grows), giving ≤ n(n − 1) per reset;
  - fallbacks by FB-INT;
  - W-length steps by W-POT on each block.
  But every break is itself an entry, i.e. a reset. So all these counts are per reset, and the number of resets is the number of
  entries, which is what has to be bounded. Rise-counting alone cannot close RISE's charging. A bound on breaks needs a quantity that an
  entry itself must pay for. Candidates (OPEN):
  - (E1) EXIT-UP type: in case A, an entering vertex rises at level ≥ rank(o) (SEP-o), and an evicted vertex's value cannot fall
    (R15 (a)), so it rises at a level > rank(o). So each re-entry cycle of one vertex raises its value at a level ≥ rank(o) twice. A
    polynomial bound needs these levels to be above T* (then an M-type freeze argument over F ∪ R̄ applies) or a band structure.
  - (E2) A Bellman-Ford argument over the whole graph with o as the target, treating F-vertices through their W-values (G (a)).
- CONJECTURE M-CROSS (in the summary of the first draft) is the statement FREEZE-X (c); it is now PROVED.

## 8. Dependencies
| tag | statement used | location | status |
| --- | --- | --- | --- |
| R15 (a) | Ξ_k ⊴ Ξ_{k+1} pointwise | RESULTS R15 (a) | LANDED |
| F1 | one-player optimum dominates every arena strategy pointwise | RESULTS R17 (a) | LANDED, no (P) |
| RF | route form Ξ(z) = π_z ⊕ θ at H1 states; P(θ) ⊆ {o} ∪ F | P-N5-OUT §4, §5 BASE (ii) (sha1 9f032e61…) | both referees signed; R39 in landing |
| SPLIT (a) | c_w ∈ R̄, c_θ ∈ F at HN states | P-N5-OUT §1 | as RF |
| FB-INT | ≤ K fallbacks in a crossing-free run of a phase | RESULTS R38 (d) | LANDED |
| EPOCH, RISE | X_S ≤ 2(n − 1)(B + 1); B_S ≤ θ_S + RR_S | P-N5-OUT §2; docs/new/N5-TAUW-box38.md §1 | §6-§7 only (obstruction, consequences) |
| SPLIT | in an HN stretch every crossing is an entry (S4a) or an eviction (fallback) | P-N5-OUT §1 | as RF |
| Lemma P (idea) | Bellman-Ford dominance for switch-best on one-player games | RESULTS R17 (b) | idea only; not a premise |

## 9. Data and scripts (DATA; experiments/new/box39)
- rwcount.py: per θ-constant HN run, the transitions with an R̄-rise (fallback / S4a), rises per vertex, crossings, and runs with
  c_w ≠ o. Library (lib37.txt minus out/ dirs, 270 𝒞^1O files; plus box-37/38 instances): 56 runs, 496 transitions, 106 rise transitions
  (13 at fallbacks, 93 at S4a), at most 14 in one run (kwm_cex_n24, n 24, 0 crossings), at most 4 rises per vertex.
- rwclass.py: blocks; rise classes M / BAND / LEN by transition kind and by "W changed on R̄"; direct checks of Lemma BF-RW (every Even
  v ∈ R, every successor x ∈ R̄, every transition of every block), of FREEZE-M (no M-rise at index ≥ n − 1), and of (F1) monotonicity of W
  at S4a.
  - Library: 75 blocks, 328 transitions. Rise counts by class: M 68 (all S4a, W changed), BAND 4 (W changed) + 4 (W unchanged = W-TIE),
    LEN 5 (W changed). 0 rise transitions inside blocks at fallbacks (the 13 fallback rises of rwcount.py are at crossings or c_w changes).
    FAIL_BFM 0, FAIL_FREEZE 0, FAIL_F1_Wmono 0. Latest M-rise index 13 (kwm_cex_n24, n 24).
  - W-TIE steps in the library: 2 (experiments/new/box29/instances/wf0_cex_n16.pg, blocks [13, 17] and [20, 21]; each a single R-vertex
    switch, W unchanged everywhere).
  - `--rand N lo hi seed`, 4 × 6,000 tries at n 6..16 (20,110 𝒞^1O games): no HN block (as box 37 found: random 𝒞^1O games do not
    reach these states).
- tieclimb.py: hill climb toward many W-TIE steps in one block (canonical start, mutations of box38/nebclimb.py MODE=TAU). A failure of
  Lemma BF-RW, FREEZE-M or F1 in any candidate is scored at the maximum and so would be kept and reported.
  Logs: experiments/new/out/box39 (gitignored). Results: §10.
- rwcross.py: θ-, c_w-constant HN runs with crossings. It checks BF-RWX at every transition (Even v ∈ R_k ∩ R_{k+1}, x ∈ R̄_k) and
  FREEZE-X (c) (no M-rise at a non-entry transition ≥ |R̄| − 1 after the last reset). Library + box-37/38 instances + climb outputs:
  55 runs with crossings (177 crossings), 100 M-rise transitions; FAIL_BFX 0, FAIL_MCROSS 0.

## 10. Climb results (DATA; interim at 14:50Z by date -u, climbs still running)
- tieclimb.py, 4 climbs, 55 min each, canonical start; seeds wf0_cex_n16 (391), kwm_cex_n24 (392), tauw_A_cex_n24 (393),
  tauw_B_cex_n24 (394). Score (max W-TIE in one block, total W-TIE, block transitions):
  - 391 (1, 2, 19); 392 (0, 0, 17); 393 (4, 6, 18); 394 (1, 1, 14).
- No candidate in any climb failed Lemma BF-RW, FREEZE-M or F1 (a failure is scored at the maximum and would show as (1000000, 0, 0)).
- W-TIE steps do accumulate in one block (4 at n = 24). Whether they can grow superpolynomially is the OPEN W-TIE question of §4.

## 11. Theorem P-FREEZE: fallbacks are Bellman-Ford rounds on U = λ^{-1}(c_θ); breaks per HN stretch are polynomial in θ_S (PROVED, L-NEW succ. 18; 𝒞^1O; written 15:0xZ by date -u)
This section supersedes the obstruction of §6-§7 for B_S. The circularity there came from counting rises per entry. Here the clock is the
fallbacks, and every break consumes a fallback (its eviction, SPLIT (b)).
- Setting.
  - Θ = [a, b] is a run of consecutive states of one phase with θ constant. Nothing is assumed about H1, H2, c_w or τ(o).
  - U := λ^{-1}(c_θ), constant on the phase (λ is a phase constant), with o ∈ U and c_θ ∈ U.
  - Terminals: o and c_θ.
  - M_t(z) := the signed weight of P(Ξ_t z), the whole path set (P ⊆ V_{>c_θ} for values with cycle node c_θ).
  - wt(v) := sgn(v)·2^rank(v) if rank(v) > rank(c_θ), else 0.
  - G_U: vertex set U; every Even v ∈ U ∖ {c_θ} keeps all its edges into U; every Odd v ∈ U ∖ {o, c_θ} keeps its forced edge; o and
    c_θ are sinks.
  - Mopt(z) := max{wt(p ∖ {end}) + M(end) : p a simple path in G_U from z to a terminal}, with M(o) := wt(P(θ)) (constant on Θ) and
    M(c_θ) = 0.
- Facts (all LANDED; no (P)):
  - (A) Additivity. For z ∈ U ∖ {c_θ} and every state t, M_t(z) = wt(z) + M_t(next_t(z)), with next_t(z) ∈ U. Here next_t = σ_t at
    Even, the forced edge at Odd z ≠ o, and σ̄_t at o.
    Proof: (V1) (R17 (a)), since λ(z) = c_θ ≠ z. ⊕ adds z iff rank(z) > rank(c_θ); a vertex on c_θ's cycle has rank < rank(c_θ),
    so its weight is 0 and no double count arises. The successor has the same cycle node, so it is in U.
  - (M1′) For y, z ∈ U at one state, Ξ_t(y) ⊴ Ξ_t(z) ⇒ M_t(y) ≤ M_t(z). (Same cycle node c_θ; the order compares the signed weight of
    P next, §0 of P-N5-OUT.)
  - (M2′) For z ∈ U, M_{t+1}(z) ≥ M_t(z) at every transition of the phase (R15 (a), same cycle node).
  - (UB) M_t(z) ≤ Mopt(z). Proof: z's honest play, up to its first visit of a terminal, is a simple path in G_U. Before o, the honest
    play and the (σ_t, ·)-play agree, and Odd vertices other than o are forced (𝒞^1O). By (A), M_t(z) is that path's weight plus M of
    its end. (V1) at o gives M(o) = wt(P(θ)) when the path ends at o; P(c_θ) = ∅ when it ends at c_θ.
- **Lemma FB-ROUND (PROVED).** At every fallback transition k → k+1 of Θ, for every Even v ∈ U ∖ {c_θ} and every successor x ∈ U of v:
  M_{k+1}(v) ≥ wt(v) + M_k(x).
  Proof.
  - If Ξ_k(x) ⊴ Ξ_k(σ_k v): by (M1′) and (A), wt(v) + M_k(x) ≤ wt(v) + M_k(σ_k v) = M_k(v) ≤ M_{k+1}(v) (M2′).
  - Otherwise (v, x) ∈ Iσ_k. S4c sets σ_{k+1}(v) = x* with Ξ_k(x*) ⊵ Ξ_k(x).
    - The transition is in the phase, so λ_{k+1}(v) = c_θ ≠ v, and (A) at k+1 gives M_{k+1}(v) = wt(v) + M_{k+1}(x*), with x* ∈ U.
    - So M_{k+1}(v) ≥ wt(v) + M_k(x*) ≥ wt(v) + M_k(x), by (M2′) and (M1′). □
  - Remark. This is the fallback being a Howard (switch-all-to-best) round. S4a steps are not used, except that they never lower M (M2′).
- **Theorem P-FREEZE (PROVED).** Let f_1 < f_2 < … be the fallback transitions of Θ.
  - (a) For every j and every state t ∈ Θ with t > f_j (t ≥ a when j = 0), every z ∈ U and every simple path p in G_U from z to a
    terminal with ≤ j edges: M_t(z) ≥ wt(p ∖ {end}) + M(end).
  - (b) Hence M_t = Mopt on U, and P(Ξ_t z) is constant on U, for every state t > f_{|U|−1} of Θ. (When |U| = 1 this holds on all of Θ.)
  Proof.
  - (a) Induction on j. For j = 0, p has 0 edges, z is a terminal, and M_t(z) = M(end) (θ constant; P(c_θ) = ∅).
  - j − 1 → j. Write p = z · p′, with p′ from x, ≤ j − 1 edges.
    - Odd z: x is its forced successor. By (A), M_t(z) = wt(z) + M_t(x) ≥ wt(z) + wt(p′ ∖ {end}) + M(end), by the hypothesis at t.
    - Even z: put k := f_j < t. By FB-ROUND at k and the hypothesis at the state k > f_{j−1},
      M_{k+1}(z) ≥ wt(z) + M_k(x) ≥ wt(p ∖ {end}) + M(end). Then M_t(z) ≥ M_{k+1}(z) by (M2′).
  - (b) Simple paths in G_U have ≤ |U| − 1 edges, so (a) and (UB) give M_t = Mopt. The signed weight is injective on sets of vertices
    above c_θ (distinct powers of 2), so P is constant. □
- **Corollary LEN-TAIL (PROVED).** On the states of Θ after f_{|U|−1}, every U-rise (z ∈ U with Ξ_t(z) ◁ Ξ_{t+1}(z)) is a length rise.
  Put s_θ := +1 if Ω(c_θ) is odd, −1 if even, and Ψ_t := Σ_{z∈U} s_θ·ℓ(Ξ_t z), with ℓ ∈ [0, |U| − 1] the honest distance to c_θ. Then
  Ψ is non-decreasing there and rises at every transition with a U-rise. So at most |U|(|U| − 1) transitions of Θ after f_{|U|−1}
  carry a U-rise.
- **Corollary NO-CROSS-A (PROVED; case A).** If rank(o) > rank(c_θ), no transition of Θ between two H1 states after f_{|U|−1} is a
  crossing.
  Proof: under H1, R̄_t ⊆ U (SPLIT (a)'s proof). SEP-o (P-N5-OUT §5) gives, for z ∈ U, z ∈ R̄_t iff o ∈ P(Ξ_t z). P is frozen on U. □
- **Theorem BRK-POLY (PROVED).** For every HN stretch S of a phase on 𝒞^1O, for any τ(o) and any c_w:
  - B_S ≤ θ_S + (θ_S + 1)(|U| − 1 + |U|(|U| − 1)) ≤ θ_S + (θ_S + 1)(n² − 1);
  - in case A, B_S ≤ θ_S + (θ_S + 1)(|U| − 1).
  Proof.
  - Every break has a window [a, k]: a is its eviction, which is a fallback transition (SPLIT (b)), and k its entry. Windows of distinct
    breaks are disjoint. By RISE (N5-TAUW §1, in P-N5-NEB) each window has a θ-change in (a, k] or an R̄-rise at a transition of [a, k)
    with θ constant on [a, t + 1].
  - At most θ_S breaks are of the first kind.
  - Breaks of the second kind lie in one θ-run Θ of S each (S meets ≤ θ_S + 1 θ-runs). In Θ, those whose eviction is one of
    f_1, …, f_{|U|−1} number ≤ |U| − 1.
  - For every other break of Θ, a ≥ f_{|U|}, so its rise transition t → t+1 has t > f_{|U|−1}. By LEN-TAIL, at most |U|(|U| − 1)
    such transitions exist. In case A there are none, since such a break's eviction a > f_{|U|−1} would be a crossing after the freeze,
    against NO-CROSS-A.
  - Sum over the θ-runs. □
- Consequences (PROVED, with P-N5-OUT §2 EPOCH, corrected form):
  - X_S ≤ 2(n − 1)(B_S + 1) and f_S ≤ K(X_S + 1) + X_S. So the crossings and fallbacks of an HN stretch are O(n³·K·(θ_S + 1)), for
    every τ(o) and every c_w.
  - This removes the RW_S term of BRK-ALL (N5-TAUW §7) and makes BAND / NO-ENTRY for c_w ≠ o unnecessary for counting.
  - What stays OPEN in the N5-OUT programme:
    - (i) θ_S / θ_ph, the θ-changes per stretch / phase;
    - (ii) HN stretches per phase for τ(o) ≠ o;
    - (iii) OTHER states;
    - and of course the S4a steps between fallbacks (iterations, not fallbacks).
- What this theorem does NOT give.
  - No bound on S4a steps: before f_{|U|−1}, any number of S4a transitions can occur.
  - No bound on θ-changes: P-FREEZE restarts at every θ-change.
  - Not a running-time bound for N5. G-N5-TIME stays OPEN.
- DATA (pfreeze.py; library 270 𝒞^1O files + box-37/38 instances + box-39 climb outputs):
  - 714 θ-constant runs, 4,197 transitions, 674 fallbacks; FB-ROUND checked at every fallback for every Even v ∈ U ∖ {c_θ} and every
    successor x ∈ U: FAIL_FBF 0.
  - P-changes on U never after the (|U| − 1)-th fallback: FAIL_PFZ 0. Post-freeze crossings 0, post-freeze breaks 0.
  - Max fallbacks in one θ-run: 25 (experiments/red/so/instances/njb_reabs65_n48.pg, n 48, |U| 48).
  - pfzclimb.py (climb against the theorem; score = (failures, fallbacks before the last P-change, fallbacks per θ-run)): running, §12.
- Relation to earlier lane work.
  - NO-ENTRY-A′ / NE-COUNT (c_w = o, case A) give breaks ≤ θ-changes; BRK-POLY's case-A form is weaker by the factor |U| − 1 but needs
    no assumption on c_w.
  - LOW-RISE / BRK-B ((n − 2)² per θ-run, c_w = o) are of the same shape as LEN-TAIL.
  - FREEZE-M / FREEZE-X (§2, §7) are the S4a-side analogues on R̄ with threshold T*. P-FREEZE needs no S4a analysis at all.

## 12. P-epochs: P-FREEZE needs only P(θ) constant; θ-changes inside a P-epoch are length-only (PROVED, L-NEW succ. 18; written 15:2xZ by date -u)
- Definition. A P-EPOCH is a maximal run of consecutive states of one phase with P(θ) constant (θ's length may change). Since θ is
  monotone (R15 (a)) with a fixed cycle node c_θ, P(θ) changes only by strict increases of M(o) = wt(P(θ)).
- **Theorem P-FREEZE′ (PROVED).** §11's FB-ROUND, P-FREEZE (a)-(b), LEN-TAIL and NO-CROSS-A hold verbatim with "θ-run Θ" replaced by
  "P-epoch Θ".
  Proof: θ enters §11 only through the terminal value M(o) = wt(P(θ)) in (UB) and in the base of P-FREEZE (a). FB-ROUND does not use θ
  at all ((A), (M1′), (M2′) and S4c only). □
- **Lemma θ-LEN (PROVED).** A P-epoch has at most |U| − 2 θ-changes.
  Proof: inside it, θ = (c_θ, P, ℓ) with c_θ and P fixed. So θ's order is the order of ℓ (in the direction s_θ), and θ is monotone. So
  each θ-change moves ℓ strictly in one direction. ℓ(θ) is o's honest distance to c_θ, a simple path in U, so ℓ ∈ [1, |U| − 1]. □
- **Theorem BRK-POLY′ (PROVED).** For every HN stretch S of a phase on 𝒞^1O, with ρ_S := the number of P(θ)-changes at transitions of
  S, any τ(o), any c_w:
  - θ_S ≤ (ρ_S + 1)(|U| − 2);
  - B_S ≤ θ_S + (ρ_S + 1)(|U| − 1 + |U|(|U| − 1)) ≤ (ρ_S + 1)(2n² − 1);
  - in case A, B_S ≤ θ_S + (ρ_S + 1)(|U| − 1) ≤ (ρ_S + 1)(2n − 3).
  Proof.
  - θ_S: by θ-LEN, since S meets ≤ ρ_S + 1 P-epochs.
  - Breaks with a θ-change in their window: ≤ θ_S.
  - Every other break has θ constant on its window, so the window lies in one P-epoch. Count per P-epoch as in BRK-POLY (§11), with
    P-FREEZE′ and LEN-TAIL′. □
- So the residual for fallbacks and breaks inside HN stretches is ρ_S, the number of P(θ)-changes: only strict increases of the path set
  of θ, not its length. This is a sharper form of the residual core "θ-changes per phase" (PF-THETA: its linear form is FALSE,
  experiments/red/so/instances/pftheta_cex_n32.pg; the polynomial form is OPEN). OPEN: ρ per phase.
- DATA (pfreeze.py with PFZ_KEY=P; same library, instances and climb outputs as §11): 872 P-epochs (runs with > 1 state), 4,749
  transitions, 704 fallbacks. FAIL_FBF 0, FAIL_PFZ 0, FAIL_THLEN (θ-changes > |U| in a P-epoch) 0. Post-freeze crossings 0, breaks 0.
  Max θ-changes in one P-epoch: 11 (pftheta_cex_n32.pg, n 32, |U| 32).

## 13. Final climb results (DATA; stopped at 15:3xZ by date -u, at the handover)
- tieclimb.py (W-TIE): max W-TIE in one block 4 (seed 393 from tauw_A_cex_n24, 134,664 iterations); 3 (392, kwm_cex_n24); 1 (391,
  394). No Lemma BF-RW / FREEZE-M / F1 failure in any candidate.
- pfzclimb.py (against P-FREEZE; score (failures, fallbacks before the last P-change, fallbacks per θ-run)):
  - seed 3971 from fb32_inr2_final.pg reached (0, 26, 26): a P-change after 26 fallbacks of one θ-run at n 32, still ≤ |U| − 1;
  - seeds 3951 and 3952: 0 failures (their lastP score was inert, see the notebook pitfall).
  - PFZ_SCORE=excess (seeds 3961, 3962): stuck at −1, i.e. θ-runs with |U| ≥ 3 reach |U| − 2 fallbacks but never |U| − 1.
  - 0 failures in every climb.
- Climb outputs are in experiments/new/out/box39 (gitignored); they are lost with the container.
