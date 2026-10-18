# K8's constant case and the best-reply-change reduction (box 7, L-NEW successor 2; GO 23:42Z, written 23:47Z by date -u)
## 1. Literature (sources opened; also in notes/L-NEW.md)
- VJ00 = Jurdziński & Vöge, BRICS RS-00-48 (pdf sha256 485a12de432a2a8c..), §7, p. 26-27:
  - Proposition 7.4: "The discrete strategy improvement algorithm terminates after O(n³) strategy improvement steps for one-player
    parity games." The algorithm's Improve is nondeterministic (any non-empty set of improvements, §4.4), so the statement covers
    every policy, switch-best included.
  - It is stated WITHOUT PROOF. The text contrasts it with one-player simple stochastic games (MDPs), where switch-all's polynomiality
    was open. That reads the "one player" as the improving player. Lead reading needed: the report does not say so explicitly.
  - The same page notes: at most O(n²) "substantial" steps (a loop value strictly improves).
- Asadi, Chatterjee, de Raaij, "Lower Bound on Howard Policy Iteration for Deterministic Markov Decision Processes", arXiv 2506.12254
  (UAI 2025), abstract page opened between 23:42Z and 23:47Z (date -u bounds):
  - mean-payoff deterministic MDPs: Howard's PI needs Ω̃(I) iterations (input size I);
  - "the best known upper bound is exponential".
  So for deterministic MDPs with GENERAL weights Howard's polynomiality is open. Parity weights are what make VJ00's one-player
  bound possible.
- Hansen-Zwick (ISAAC 2010, Ω(n²) for Howard on minimum mean-cost cycles) and Hansen-Kaplan-Zwick (SODA 2014, Dantzig's rule
  O(mn log n) on shortest paths, O(m²n² log² n) on deterministic discounted MDPs): bibliographic and abstract records only (no arXiv
  version found), NOT opened. Post-Ye (arXiv 1208.5083, opened in box 1): simplex with the highest-gain rule is strongly polynomial on
  deterministic discounted MDPs.
- Fearnley's MDP lower bound (Friedmann's construction carried to MDPs) uses random vertices, so it is not deterministic. Not
  re-opened in this box. Friedmann's one-player remarks: not opened.

## 2. K8's constant case is polynomial (conditional on VJ00 Prop. 7.4)
Suppose that, along a segment of N5's run, Odd's best reply b_k = σ̄_k is a constant strategy c.
- Then Ξσ_k = Θ_{σ_k, c} = Ω^{G_c}_{σ_k}, where G_c is the one-player game with Odd fixed to c.
- So the improvements of σ_k in G and in G_c coincide. N5's Even moves in the segment switch only such improvements (N4 of the
  G-N5-TERM reading), so they form an improvement sequence of G_c.
- By Prop. 7.4 the segment has O(n³) Even moves, whatever τ does.
- This covers K8's constant case (switch-best followed with a constant Odd reply).
Computer check of Prop. 7.4 in the player-⊕ reading (vj_1p_longest.py; one-player games with Odd out-degree 1; the LONGEST improvement
sequence over ALL policies and ALL starts, by exhaustive search): n = 4..9 gives 5, 9, 9, 16, 21, 14 (300 games; vj_1p_longest.txt).
That is far below n³ and consistent with the proposition, though small n cannot separate polynomial from exponential.

## 3. K9: the reduction to best-reply changes
By the same argument on both sides, for every N5 run:
    #Even moves ≤ C n³ (1 + #changes of Odd's best reply σ̄_k)   and   #Odd moves ≤ C n³ (1 + #changes of Even's best reply τ̄_k).
Every iteration moves σ or τ, so #iterations ≤ C n³ (2 + #changes of σ̄ + #changes of τ̄).
K9. A super-polynomial N5 run needs super-polynomially many changes of the opponents' best replies along it (conditional on Prop. 7.4).
Data (n5_brchanges.py; brchanges.txt):
| instance | iterations | changes of σ̄ / of τ̄ |
| --- | --- | --- |
| switchbestexp N = 4 | 47 | 4 / 4 |
| switchallexp N = 8 | 16 | 3 / 8 |
| counter_symsi N = 8 | 48 | 23 / 25 |
| deeptrap N = 8 | 33 | 10 / 8 |
| box-5 harmful-skip climb, n = 96 | 50 | 18 / 7 |
| box-4 lock, n = 24 | 19 | 6 / 7 |
| dlm2 n = 8 | 15 | 11 / 10 |
For comparison: Friedmann's switch-best run on switchbestexp has 24 changes of Odd's reply at N = 4, and 2^N distinct replies (box 6).
This is the measure a killer must drive up.

## 4. Status
- K8's constant case is closed, conditional on Prop. 7.4. The proposition is unproved in the source; like G-N5T-3, it needs a proof
  or a second source.
- The 2-periodic case is not done in this box.
