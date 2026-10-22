# Box 11 option (2): a killer from the toggle structure with Odd moving: requirements, data, not built (L-NEW successor 4, Fable 5.1; written 2026-10-22 00:41Z by date -u)
Lead brief 00:27Z: after (c) and (b)-lite came out negative, try a killer design that uses the toggle structure (N5-brchanges-box11.md §3) WITH
Odd moving. Status: NOT BUILT; the requirements are written down, the climbs that target the mechanism are reported in §4, and the obstruction
is the circularity in §3. N5 is not killed. Tools: experiments/new/br/ (deviate.py, srev_climb.py, brtrace.py); instances/br11b.

## 1. What the toggle structure is, with Odd moving
In vc_g25.pg (n = 25, 15 Even vertices; N5-phase-bound-box10.md §5) Odd's best reply σ̄ is the SAME strategy c at all 27 iterations (brtrace.py:
one σ̄ state), so the whole run is one σ̄-segment: Even's honest gate is "improving in the one-player game G_c" throughout, and Even's honest
values Ξσ_k are G_c-values rising monotonically. Odd's τ_k moves at 17 iterations through 15 distinct best-reply states τ̄. Even makes 27 moves
(26 value-changing), above the one-player bound n − 1 = 24, and revisits targets (vertex 4: 7 → 5 → 2 → 5 → 2; vertex 23: 19 → 3 → 2 → 3 → 2).
deviate.py: at 22 of the 27 iterations Even's actual step (the optimum of the gated arena against the CURRENT τ_k) differs from the honest
switch-best step (the optimum of the same arena against c). So the run is one-player switch-best in G_c DISTRACTED by τ_k at almost every
step, and the distraction buys 2-3 extra moves over Theorem PH's bound. Same picture on seg_r16 (11 of 13 Even steps deviate, one σ̄ state),
seg_n24 (15 of 19); on the lane's older instances deviations are rarer (tc2: 7 of 69, sbe2_s21: 2 of 37).

## 2. Requirements for a super-polynomial run built this way
Let the segment have constant σ̄ = c (R1; vc_g25 shows a whole run can be one segment). Then:
- (R2) Even's moves form a one-player improvement sequence of G_c whose steps are "the τ_k-optimum among the honest improvements". For the
  sequence to be super-polynomial, exponentially many of its steps must be deviations (Theorem PH bounds the non-deviating stretches: a run of
  consecutive honest switch-best steps inside a λ-phase of Ξσ is ≤ n − 1 steps), each a K1 stall or a detour that keeps Even off the honest
  optimum of its arena while still switching honest-improving edges.
- (R3) The lures are τ_k. Odd's τ_k is itself N5's Odd step: the optimum in G_{σ_k} over Odd's honest gate (improvements against τ̄_k). Its
  honest values Ξτ_k rise monotonically for Odd, and τ never returns (Lemma NR). So exponentially many deviations need exponentially many Odd
  moves that each present a NEW lure, i.e. Odd's own improvement sequence must be super-polynomial, with σ_k as ITS lure.
- (R4) Both gates are honest. Every Even move raises Ξσ somewhere (except value-flat cycle-node switches), every Odd move raises Ξτ. The pair
  (Ξσ_k, Ξτ_k) is a strictly rising sequence in a product of two lex orders; its length is unbounded in principle (CDAG path sets).

## 3. The circularity (why no design was found in this box)
A toggle-driven killer must make two distracted one-player improvement sequences drive each other: Even's deviations are caused by τ_k, Odd's
by σ_k. In every instance so far one side converges first and the other then finishes as plain switch-best (vc_g25: Odd's last move at
iteration 21, Even then takes 5 honest steps; the box-9 tails: Even finishes, Odd's tail ≈ 1.4n). The lane's earlier kills of N5-following
designs apply here: K7/K8 (N5's Odd step reproduces a wanted lure sequence only when it is constant or 2-periodic), K10 (a lure must mask
Θ(n) honest improvements at once, and the masked set moves along the chain), Fact B (a vertex at the opponent's favourite target cannot be
masked). The new data add: with σ̄ constant, Odd's lures DID produce 22 deviations in 27 steps, so distraction is cheap locally; what is
missing is a mechanism that makes the lures RECUR (Odd would have to revisit lure configurations, which Lemma NR forbids for τ as a whole
and which the data show only at single vertices, up to 16 revisits at n = 24, N5-brchanges-box11.md §4).
