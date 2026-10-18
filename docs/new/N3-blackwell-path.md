# N3 BLACKWELL-PATH: exact discount homotopy (parametric strategy following in gamma) (L-NEW; before code)

Status: PROPOSED (not implemented in box 1; N1 is its discretisation).

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
