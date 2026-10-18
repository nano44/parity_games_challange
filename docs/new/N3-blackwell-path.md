# N3 BLACKWELL-PATH: exact discount homotopy (parametric strategy following in gamma) (L-NEW; before code)

Status: DEAD AS STATED (box 3 scoping, 2026-10-18 by date -u; argument + grid data, unrefereed): deep traps put the whole problem
into ONE degenerate breakpoint; see the last section.

## Exact pseudocode
For gamma in (0, 1): values of a strategy pair (sigma, tau) are rational functions x_v(gamma) (lasso sums).
1. At gamma = 0+: sigma, tau = greedy one-step choices (lexicographic in derivatives at 0+ for ties).
2. Loop: for every edge e = (u, w), advantage a_e(gamma) = x_w(gamma) - x_{sigma/tau(u)}(gamma) (rational function).
   gamma' := the smallest root > gamma of any a_e with the wrong sign after it (exact root isolation: Sturm sequences on
   the numerator polynomial, degree <= 2n). If none below 1: STOP (the pair is Blackwell optimal).
   Otherwise switch the edges whose advantage changes sign at gamma' (generic: one), set gamma := gamma'.
3. Output: the Blackwell-optimal pair; regions by the sign of the mean payoff (limit of (1-gamma) x_v). Verified as N1.

## Why new
A path-following method in the discount factor; no fleet lane and no RANKING row uses it. Unlike every SI rule of the
obstruction map, it has NO free choice: the switch sequence is determined by the game (no index, no tie-break in the
generic case), so the renumbering adversary of S5/S6 has no lever. The adversary must build games whose optimal strategy
changes exponentially often as gamma increases.

## Barrier statement draft
B8-B11: not a SI improvement rule (switches at breakpoints are not improvement steps of a fixed objective). B13: FJS's
Lemke is a homotopy in the covering vector at fixed discount; N3 homotopes the discount; no transfer known to L-NEW.
Closest known obstruction (L-NEW reading, source not yet opened): parametric shortest paths can have n^Theta(log n)
breakpoints (Carstensen; Gusfield) for LINEAR parameters; here the parameter enters multiplicatively. Bit cost: exact
roots of degree-2n polynomials with Θ(n d log n)-bit coefficients; breakpoints are algebraic, so comparisons need root
isolation: polynomial per breakpoint, number of breakpoints unbounded by anything L-NEW knows.

## Cheapest killer expected
A one-player (Even-only) family first: if the Blackwell path of a deterministic discounted MDP is long there, N3 is dead
without any two-player construction. Candidate: the parametric-shortest-path families of Carstensen (to be opened).

## Box 3 scoping with the N1 killer families (argument + grid data; unrefereed)
Tool: experiments/new/n3grid.cpp = anneal.cpp with gamma = 1 − c/2^j on a grid 8x finer than N1's (j = jj + 3, c = 15..8), solving
to the discounted optimum at every grid point (warm start) and counting changes of the optimal pair. A change between two grid
points is at least one breakpoint of N3's exact path, so the counts are LOWER bounds. Sanity: on switchallexp the Even totals
equal N1's (25, 42 at N = 2, 3); every final solution: regions = Oink zlk, strategies verified.
| family | N = 1..5: changes of the optimal pair on the grid | Howard iterations inside the one long grid interval |
| --- | --- | --- |
| switchallexp | 6, 10, 15 (N = 1..3) | 7, 9, 11 |
| deeptrap_sae (instances/killer/) | 1, 1, 1, 1, 1 | 11, 31, 71, 151, 311 |
| steptrap --rev (experiments/new/steptrap.py: distinct trap gaps, generic releases) | 5, 6, 7 (N = 2..4) | 31, 71, 151 |
Reading:
- On deep traps the optimal pair changes ONCE along the whole discount path: from "all traps" to the final strategy, at the
  release point γ*, where every trap edge changes sign at the same time (identical gaps). N3 as stated ("switch the edges whose
  advantage changes sign; generic: one") is undefined there. Any rule for this degenerate breakpoint must produce the optimum
  at γ* + ε from the all-traps optimum. γ* + ε is a parity-like discount for switchallexp, so this one step IS the original
  problem from Friedmann's best-reward start: by Howard it costs 2^Ω(N) (measured); by recursion (N3 on the game at γ* + ε) it
  loops; by a symbolic perturbation it becomes a pivot path whose length is exactly the open question.
- Distinct gaps (generic releases) do not remove the long interval: 5-7 changes on the grid, but one grid interval still holds
  31, 71, 151 Howard iterations, i.e. the optimum moves far inside it (several or degenerate breakpoints there; the grid
  cannot tell which).
OBSTRUCTION (for the barrier lane): a discount homotopy can be made trivial everywhere except at one point that carries the
entire problem (deep traps: gap P − q > max priority + 2). Hence any discount-schedule or discount-homotopy method is at least
as hard as its rule for crossing one degenerate breakpoint at a parity-like discount, which is a parity game solve from the
best-reward start. This covers N1 (Howard per phase, killed), N1m (with padding), and N3 (any breakpoint rule).
