# K8 revisited (box 8): the 2-periodic case is closed; the constant case is open for cyclic G_c (L-NEW successor 3)
Opus 5.5 (D8). 2026-10-19, first commit 98770e2 at 01:23Z (commit time; an earlier stamp "01:35Z" was an estimate and is corrected here). Status: L-NEW READING, unrefereed, with DATA. Builds on N5-K8-box6.md (K8)
and N5-K9-Pstrict-counter.md §5.

## 1. Lemma NR (non-returning), from R15
Along N5's run, neither σ nor τ ever returns to a strategy it held earlier.
Proof:
- RESULTS R15 (d): every N5 iteration changes τ only by Switch_I with ∅ ≠ I ⊆ Iτ, on G^d (S4b or the S4c fallback).
- So the successive distinct values of τ form a VJ00 strategy-improvement run of Odd's player in G^d.
- R15 (c): "no strategy repeats in any VJ00 strategy-improvement run with any non-empty selection rule".
- The same holds for σ on G. □
Check: experiments/new/p_strict/n5_noreturn.py on 329 runs (lane instances, the box-8 climb instances, 300 of rand2k), 1,471
iterations: 0 returns.

## 2. K8's 2-periodic case is closed
- K8's route (N5-K8-box6.md §1 (b)) needs τ_k = b_{k+1} for every k along the followed stretch, where b_k is Odd's best reply to σ_k.
- Suppose b changes at step k (b_{k+1} ≠ b_k) and returns (b_{k+2} = b_k), as K8 (c) forces when Odd's step returns its full
  best reply.
- Then τ_{k−1} = b_k = b_{k+2} = τ_{k+1}, while τ_k = b_{k+1} differs from both. That is a return, which Lemma NR forbids.
- So along any stretch that N5 follows by K8's route, Odd's best replies form a NON-RETURNING sequence: each value occupies one
  contiguous block.
- With full-best-reply Odd steps, K8 (c)'s (*) then allows no reply change, except one at the very start of the stretch (where
  τ_{k−1} does not exist).
- So the followed stretch is the constant case. The 2-periodic case cannot occur beyond that edge effect.
Instance (DATA; climb p_strict/sb_alt_climb.py, fitness = reply changes inside the 2-periodic prefix):
- instances/sbalt/sbalt_n16_seed1016.pg. Switch-best's Odd replies alternate at each of its first 6 steps (11 switch-best steps).
- N5 follows for 2 iterations, then leaves (sb_traj.py).
- p_strict/sb_alt_diag.py shows why: at k = 1 the flip-back edge (Odd vertex 8 → 7) is not in Iτ_1, so N5's Odd step cannot
  return. N5 takes 8 iterations, switch-best 11.
Regions and strategies are checked (zielonka + verify.py) for every improved best in the climb logs.

## 3. The constant case
- Box 7's closure used the any-policy premise, which CDAG refutes; it is withdrawn (N5-K9-Pstrict-counter.md §5).
- Lemma S re-closes the constant case when G_c is acyclic apart from the sink loop. For cyclic G_c it is OPEN.
- DATA:
  - One-player switch-best climbs (p_strict/sb_1p_climb.py, Odd out-degree 1): 11 steps at n = 16, 18 at n = 32.
  - Two-player constant-reply climbs (p_strict/sb_2per_climb.py): 13 at n = 16 and at n = 32.
  - On the n = 16 two-player instance, N5 follows switch-best for all 13 steps, mostly single switches (sb_replies.py).
  - Earlier: sb_oneplayer.py, 16 at n = 40; sb_1p_general.py, ≤ 6 on random one-player games n ≤ 24.
  - All of this is linear-looking. A super-linear or exponential constant-case family would need switch-best to be slow on a
    one-player game with cycles; none was found.
- What a proof needs: Lemma S's induction (fix the vertices whose ρ*-successor is already optimal) works for tree vertices of the
  optimal strategy in a cyclic one-player game as well. The argument: if the current play from ρ*(x) passes through x, the
  closed cycle would beat x's optimal cycle node, a contradiction (sketch; not written out).
- The gap is the optimal CYCLE itself. Its edges need not be improving before it closes, and they can enter and leave the arena.
  A bound on cycle formation per cycle-node phase (≤ n² phases) would give a polynomial bound.

## 3b. Conjecture SB1 and the potentials that fail (DATA, p_strict/sb_settle.py)
Conjecture SB1: switch-best on a one-player game (⊖ out-degree 1, cycles allowed) is optimal after at most n steps.
- 906 runs: 300 random one-player games (n ≤ 20) plus the sb1p climb instances, 3 random starts each. max(steps − n) = 0.
- Climbs: 7 at n = 8, 11 at n = 16, 18 at n = 32, 17 at n = 64 (all ≤ n).
- All starts (p_strict/sb1_allstarts.py, 1,500 random one-player games n ≤ 7): max steps 1, 3, 3, 3, 3, 4 at n = 2..7. Two runs reach
  n (n = 3, 3 steps: a self-loop closes, then depth 2), so "≤ n − 1" is false; "≤ n" holds.
- Lemma S's step-wise potential FAILS with cycles. In 99 of the 906 runs some step settles no new vertex (Ω = Ω*). Neither the
  number of vertices with an optimal cycle node, nor that number plus #settled, nor the lexicographic pair, increases at every
  step.
- Typical failing run: n = 15, 2 steps, settled 10 → 10 → 15. The first step prepares a cycle and the second closes it.
- So a proof of SB1 needs an amortised argument, e.g. charge each cycle-preparing step to the cycle it closes. Not done.

## 3c. Lemma T (tree propagation; L-NEW reading, unrefereed): what is left of SB1 is the cycle tops
Setting:
- H is one-player (⊖ out-degree 1), VJ00 Ω, injective priorities.
- ρ* is optimal, Ω* = Ω_{ρ*}, λ* = Ω*'s cycle node. ρ_k is switch-best's run; "x settled at k" means Ω_{ρ_k}(x) = Ω*(x)
  (settled vertices stay settled).
- Write a ⊕ Ω for "prepend a to the play": a joins P if a is more relevant than the cycle node, and the length grows by 1.

Lemma T. If y = ρ*(x) is settled at k and x ≠ λ*(x), then x is settled at k + 1.
Proof: Ω*(x) = x ⊕ Ω*(y). This is valid because the ρ*-path from y to λ*(x) avoids x: if x lies on the ρ*-cycle, it comes after
the cycle node. Suppose x is not settled at k. Three cases.
- (i) (x, y) is not an improvement of ρ_k: Ω_k(y) ⊴ Ω_k(ρ_k(x)) ⊴ Ω*(ρ_k(x)) ⊴ Ω*(y) = Ω_k(y). The middle step holds because Ω_k ⊴ Ω*;
  the third because ρ* has no improvement. So all are equal, and Ω_k(x) = x ⊕ Ω_k(ρ_k(x)) = Ω*(x), i.e. x is already settled. (If x is
  the top of its ρ_k-cycle, then λ_k(ρ_k(x)) = x = λ*(y) = λ*(x), contrary to x ≠ λ*(x).)
- (ii) (x, y) is an improvement and the ρ_k-play from y avoids x: ρ̂ = ρ_k[x → y] lies in the arena and gives x the value
  x ⊕ Ω*(y) = Ω*(x). The arena optimum dominates it pointwise.
- (iii) (x, y) is an improvement and the ρ_k-play from y passes through x: IMPOSSIBLE.
  - Write the play as y, seg, x, …. Let u = λ*(x) = λ_k(x) and S = the vertices of seg more relevant than u. Then
    Ω*(x) = (u, P_k(x) ∪ S, k_k(x) + |seg| + 1).
  - Since x is not settled, either max(S) = s is even, or S = ∅ and u is odd (longer is better).
  - ρ̂ closes the cycle Z = {x} ∪ seg. Optimality gives reward(top Z) ⪯ reward(u).
  - Case s even: top Z ≠ s (else reward(top Z) > reward(u)). So top Z = x, x is odd, and x is more relevant than s and than u.
    Then x ∈ P_k(y). The ρ*-path from y has the same P (Ω*(y) = Ω_k(y)), so it passes x. So x lies on the ρ*-cycle, and
    λ*(x) ⪰ x in relevance, which contradicts λ*(x) = u.
  - Case S = ∅, u odd: if x is less relevant than u, then top Z is less relevant than u. An even top, or an odd one less relevant than
    u, beats u in reward: contradiction. So x is more relevant than u, and the same "ρ*-path from y passes x" argument contradicts
    λ*(x) = u. □
Consequence:
- Once every top of a ρ*-cycle is settled, switch-best is optimal within h more steps, where h = the depth of the ρ*-forest
  measured to the cycle tops (≤ n).
- SB1 therefore reduces to: the ρ*-cycle tops settle within O(n) steps (O(n) would give ≤ 2n overall).
- A top u settles exactly when some ρ_k-cycle through u has top u. Its cycle's edges need not be improvements before it closes;
  that is the open part.
Check: sb_settle.py's failing runs are exactly cycle-preparing steps (n = 15: 10 → 10 → 15), consistent with Lemma T.

## 4. Files
p_strict/sb_2per_climb.py, sb_alt_climb.py, sb_1p_climb.py, sb_replies.py, sb_alt_diag.py, n5_noreturn.py; instances in
instances/sbalt/, instances/sb2/, instances/sb1p/ (sha1 in p_strict/sb_instances.sha1); logs in p_strict/logs/.
