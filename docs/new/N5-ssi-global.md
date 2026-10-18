# N5 SSI-GLOBAL: symmetric SI, each player's step = its best subset of improving switches against the opponent's CURRENT strategy
(L-NEW box 3, 2026-10-18, by date -u; Lead pick 18:47Z. DATA, unrefereed.)

Order of work (stated plainly): the Lead asked for the "not covered by DLM" text BEFORE code. I checked it against the opened
text first (18:47-18:50Z, below), but wrote n5.py and ran the DLM validation (18:50Z) before writing this file (19:00Z).

## Exact pseudocode (experiments/new/n5.py, mode n5)
VJ valuations (Vöge-Jurdziński; L-SI's engine experiments/si/si.py, imported read-only): Ξσ = valuation of Even's σ against Odd's
optimal counterstrategy σ̄; Iσ = Even's improving edges. Odd's side on the dual game (owners swapped, priorities + 1): Ξτ, τ̄, Iτ.
Start: best-reward start for both (or a given pair, e.g. DLM's (σ0, τ0)).
Loop:
1. If Iσ = Iτ = ∅: stop (both optimal; 2309.02223 Lemma 5 for sink games; in general: no improving switch for σ means σ is
   optimal (classical SI), and the final regions/strategies are checked anyway).
2. Even: A_σ(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ}. σ' = Even's optimal strategy in the arena where Odd plays τ (fixed) and Even's v may
   use only A_σ(v), computed as Odd's optimal counterstrategy on the DUAL of that arena (Engine.evaluate = VJ00's procedure).
3. Odd: A_τ(v) = {τ(v)} ∪ {w : (v, w) ∈ Iτ}; τ' = Odd's optimal counterstrategy to σ in the arena where Odd's v may use only A_τ(v).
4. If σ' = σ and τ' = τ although Iσ ∪ Iτ ≠ ∅ (possible on non-sink games; see below): FALLBACK = one classical switch-all step for
   Even on Iσ (for Odd on Iτ if Iσ = ∅); counted.
5. σ, τ := σ', τ'.
Termination: σ' differs from σ only by edges of Iσ, so σ' is σ with a subset of its improving switches applied: Ξσ' ⊵ Ξσ, strictly
unless σ' = σ (standard SI lemma); the same for τ; step 4 always improves one side. So each iteration strictly improves σ or τ.
Output: Engine.regions(σ) (regions and both players' strategies), checked by check_sol2.py (Oink zlk + harness/verify.py).

## Why N5's step is NOT covered by 2309.02223 (opened pdf, sha256 10e6794d82aba465..; page numbers = running heads)
- Improvement rules (p. 5): "an improvement rule, which is a function f : P(E) → P(E) that takes as input a set of improving
  edges, and outputs a set of improving edges", with "f(S) ⊆ S for all S ∈ P(E)" and at most one outgoing edge per node.
- SSI (Algorithm 2, p. 7): "I ← f((Iσ ∩ {(v, τ̄(v)) | v ∈ V0}) ∪ (Iτ ∩ {(v, σ̄(v)) | v ∈ V1}))". So every SSI switch at an Even v
  is the edge (v, τ̄(v)), and only when that edge is improving.
- Generalized SSI (Algorithm 3, p. 8): "I ← f((Iσ ∩ Jσ(τ)) ∪ (Iτ ∩ Jτ(σ)))", with Jσ(τ) = {(v, w) : v ∈ V0 ∧ Ξτ(w) ⊵ Ξτ(σ(v))}.
- Theorem 1 (p. 2): SSI is exponential "independently of the improvement rule"; Theorem 13 (p. 14): also for generalized SSI.
- p. 3: "This suggests that one needs a different approach involving more than only local information to benefit from insights
  in the interplay of strategies for both players." p. 15: the algorithms "can make too few crucial switches, as they are
  distracted by their opponent's (bad) strategy".
N5 is outside both algorithms as DEFINED: (i) its switch at v can be any edge of Iσ, including edges w ≠ τ̄(v) (Algorithm 2 cannot
switch there) and edges with Ξτ(w) ◁ Ξτ(σ(v)) (outside Jσ(τ), so outside Algorithm 3); (ii) its choice is not a function of the
candidate SET alone: it is a one-player optimum over the whole arena against τ. Risk (why it might still behave like SSI): N5 also
steers by the opponent's current strategy τ (the p. 15 mechanism). DLM's own families were therefore the first test.

## First test: DLM's own families (generator: experiments/new/dlm_gen.py, transcribed from Table 1 pp. 9-10 and Table 2 p. 13,
with their start pair (σ0, τ0); NOT Oink's counter_symsi, which has the same sizes 10N + 2 but different priorities)
Validation of the engine: n5.py mode ssi (Algorithm 2 with SWITCH-ALL) reproduces Proposition 7 EXACTLY on family 1:
1, 5, 13, 29, 61, 125 = 2^(n+1) − 3 (n = 1..6); and on family 2 gives 2, 9, 23, 51, 107, 219, 443 = 7·2^(n−1) − 5 (n = 1..7), the
count Proposition 11 states for generalized SSI.
| family (start σ0, τ0) | n (paper) | SSI (Alg. 2, switch-all) | N5 iterations | check |
| --- | --- | --- | --- | --- |
| DLM family 1 (Table 1) | 1..6 | 1, 5, 13, 29, 61, 125 | 1, 2, 4, 4, 6, 7 (no fallback) | Oink zlk OK, strategies verified, every n |
| DLM family 2 (Table 2) | 1..7 | 2, 9, 23, 51, 107, 219, 443 | 2, 4, 7, 8, 11, 12, 13 (no fallback) | same |
So N5 defeats both DLM families (data). Larger n and the rest of the bench: experiments/new/n5/<family>.csv (runner run_n5.sh).

## Cost at bit cost (Lead item 4)
Per iteration: 2 valuations (Ξσ on G, Ξτ on the dual) + at most 2 one-player optima, each ONE call of Engine.evaluate, i.e. the
Vöge-Jurdziński counterstrategy computation (VJ00, as implemented by L-SI; polynomial; L-NEW has not opened VJ00 for its exact
bound), plus a fallback step (no extra evaluation). Valuations are (vertex, n-bit path set, length): comparisons cost O(n) bits; no
big-number arithmetic anywhere (no discount, no weights). So the cost is poly(n) per iteration; the open question is the
iteration count, which is what the sweeps measure (iterations and fallbacks per row).

## Deep traps and padding
VJ valuations depend only on the priority order (injective rank), so priority gaps and isolated dummies change nothing; a trap
option (top priority P on a path into an odd cycle of priority q = B + 1 above every original priority) is Even's worst option
under VJ. Measured: experiments/new/n5/deeptrap.csv and padsae.csv.

## STEP-2 REPORT (2026-10-18 20:3xZ by date -u; data at this commit; DATA, not a claim, D1)
Gauntlet step 2 for N5: agreement with Zielonka on 12,000 random games and on EVERY M1 hard family, growth plotted.
(d) Verifier: every row is checked by experiments/new/check_sol2.py = regions equal to Oink zlk (pinned 8fbf0a7; Oink tl where zlk
hit the 4 GB cap, labelled per row) AND experiments/harness/verify.py (L-COMP's strategy checker, the D2 change 5 tool) on BOTH
players' positional strategies. Random games: harness/zielonka.py + harness/verify.py in-process (n5_random.py). Counts per family
= the "rows checked" column (all rows of every family verified; no mismatch anywhere).
(e) Stops: Python engine, 600 s budget per family (run_n5.sh BUDGET); the stopping row is named in the table ("BUDGET600_REACHED at
N = k" means sizes 1..k-1 finished and k was not started); families without a stop ran to NMAX = 40.
Start pair: best-reward for both players, except dlm1/dlm2 = DLM's (σ0, τ0).
| family | N (n) covered; stop | N5 iterations first .. last | (a) local log-log slope in n, last 3 | fallbacks (total) | rows verified |
| --- | --- | --- | --- | --- | --- |
| counter_core | N = 1..22 (n = 9..135); BUDGET600_REACHED at N = 23 | 2 .. 44 | [1.03, 1.02, 1.02] | 0 | 22/22 |
| counter_dp | N = 1..40 (n = 8..164) | 2 .. 40 | [0.0, 2.03, 0.0] | 0 | 40/40 |
| counter_m | N = 1..40 (n = 6..123) | 1 .. 21 | [1.97, 0.0, 1.98] | 0 | 40/40 |
| counter_ortl | N = 1..29 (n = 6..146); BUDGET600_REACHED at N = 30 | 2 .. 30 | [0.97, 0.97, 0.97] | 0 | 29/29 |
| counter_qpt | N = 1..40 (n = 2..80) | 1 .. 1 | [0.0, 0.0, 0.0] | 0 | 40/40 |
| counter_rob | N = 1..19 (n = 14..1238); BUDGET600_REACHED at N = 20 | 3 .. 55 | [0.56, 0.56, 0.56] | 0 | 19/19 |
| counter_rr | N = 1..40 (n = 4..160) | 1 .. 2 | [0.0, 0.0, 0.0] | 0 | 40/40 |
| counter_symsi | N = 1..22 (n = 12..222); BUDGET600_REACHED at N = 23 | 7 .. 99 | [1.3, 0.22, 0.89] | 84 | 22/22 |
| recursiveladder | N = 1..40 (n = 5..200) | 1 .. 40 | [2.03, 0.0, 2.03] | 0 | 40/40 |
| switchallexp | N = 1..40 (n = 21..567) | 5 .. 80 | [1.01, 1.01, 1.01] | 0 | 40/40 |
| switchbestexp | N = 1..32 (n = 35..810); BUDGET600_REACHED at N = 33 | 20 .. 242 | [0.8, 1.47, 0.67] | 0 | 32/32 |
| tc | N = 1..26 (n = 8..2158); BUDGET600_REACHED at N = 27 | 1 .. 83 | [-1.9, 1.64, 1.51] | 3 | 26/26 |
| tc+ | N = 1..17 (n = 8..5304); BUDGET600_REACHED at N = 18 | 1 .. 178 | [0.25, 0.67, 0.57] | 7 | 17/17 |
| dlm1 | N = 1..40 (n = 4..82) | 1 .. 41 | [0.97, 0.98, 0.0] | 0 | 40/40 |
| dlm2 | N = 1..21 (n = 12..212); BUDGET600_REACHED at N = 22 | 2 .. 34 | [-0.61, 1.27, 1.25] | 0 | 21/21 |
| deeptrap | N = 1..40 (n = 47..1295) | 4 .. 145 | [4.88, 0.55, 0.56] | 0 | 40/40 |
| padsae | N = 1..40 (n = 50..1220) | 5 .. 80 | [1.02, 1.02, 1.02] | 0 | 40/40 |
Plots (a): docs/new/plots/n5_<family>.png (17): iterations and fallbacks against n, seconds per iteration against n, log-log.
(a) switchbestexp (Friedmann's switch-best family, nearest relative of a global best step), iterations per N = 1..32:
[20, 32, 41, 47, 55, 62, 68, 77, 83, 89, 98, 104, 110, 117, 123, 129, 136, 122, 150, 153, 159, 165, 171, 177, 183, 189, 195, 214, 220, 226, 237, 242]; about +6 per N (n = 25N + 10), slope in
n 0.7-1.5 over the last sizes, no fallbacks. Switch-best SI doubles on this family (M1 bench, experiments/hard-families/switchbestexp/README.md: PGSolver switch-best
23, 61, 137, ..., 4849 at N = 1..8).
(b) Fallbacks per N (a fallback = one classical switch-all step taken because N5's selection made no progress):
- counter_core: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/44 = 0.00
- counter_dp: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/40 = 0.00
- counter_m: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/21 = 0.00
- counter_ortl: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/30 = 0.00
- counter_qpt: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/1 = 0.00
- counter_rob: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/55 = 0.00
- counter_rr: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/2 = 0.00
- counter_symsi: [1, 4, 5, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]; fallback fraction at largest N 4/99 = 0.04
- recursiveladder: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/40 = 0.00
- switchallexp: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/80 = 0.00
- switchbestexp: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/242 = 0.00
- tc: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/83 = 0.00
- tc+: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1]; fallback fraction at largest N 1/178 = 0.01
- dlm1: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/41 = 0.00
- dlm2: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/34 = 0.00
- deeptrap: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/145 = 0.00
- padsae: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; fallback fraction at largest N 0/80 = 0.00
Only counter_symsi (4 per N, constant from N = 4), tc (3 in total) and tc+ (1-2 per N from N = 12) use fallbacks; the fraction at
the largest N is <= 0.04 everywhere. N5 does not degenerate into switch-all SI on any family.
(c) Measured cost: seconds per iteration against n (local log-log slope, last 3 sizes; Python, shared cores):
- switchbestexp: [1.88, 1.41, 2.53]
- tc: [2.72, 0.17, 2.62]
- tc+: [1.84, 1.8, 1.87]
- deeptrap: [1.19, 4.02, 1.94]
- padsae: [1.05, 3.18, 1.05]
i.e. about n^1.8-2.5 per iteration on the large families (VJ00 evaluations in Python), polynomial; no big numbers.
Random games: seed 1, 10,000 games n <= 60: AGREE 10000/10000 (max 11 iterations, 1,057 fallbacks in total); seed 2, 2,000 games
n = 60..400: AGREE 2000/2000 (max 15 iterations, 369 fallbacks) (n5/random.txt).
CAVEATS: one implementation (Python, L-SI's engine); sizes modest (n <= 5304, most families n <= 1300); the bench was built against
other algorithms, so it is weak evidence against N5; no barrier statement yet beyond N4N5-proposals.md; no adversarial family yet
(next item: own killer attempt).

## Killer attempt 1 (box 3, 20:39Z by date -u): adversarial hill climb, NOT killed
experiments/new/n5_adv.py n 4000 seed: random game (n vertices, out-degree <= 3, distinct priorities), mutations = edge target,
priority swap, owner flip; fitness = N5 iterations + 0.5 per fallback (the fallback trigger is where N5 hands over to classical
switch-all). Best found (pinned: experiments/new/instances/n5adv/best_n<n>_seed<n>.pg, every improved best checked: Zielonka +
verify.py, all OK):
| n | best N5 iterations | fallbacks in that run | sha1 (first 12) |
| --- | --- | --- | --- |
| 8 | 13 | 3 | 8c15f67e059e |
| 12 | 14 | 4 | 0a6d5f7c1d27 |
| 16 | 21 | 5 | 62a4c6e40a87 |
| 24 | 39 | 10 | 8aca328d1a66 |
Reading: <= 1.6 n iterations; no doubling. LEAD for the next attempt: the fallback share grows under adversarial pressure (25% at
n = 24, vs <= 4% on the bench). A family that forces N5's selection to stall at every step would make N5 = classical switch-all SI
(Friedmann-hard). Concrete design: a non-sink gadget where, against Odd's current τ, every improving switch of Even is worse than
staying (the one-player optimum keeps σ) while symmetric for Odd; then embed Friedmann's switchallexp counter behind it.

## Killer attempt 2 (20:43-20:44Z by date -u): maximise FALLBACKS (n5_adv.py ... fb), NOT killed
Fitness = fallback count (ties by iterations), 4,000 steps, n = 16, 24, 32 (seeds 116, 124, 132): best fallbacks/iterations 2/12,
13/31 (n = 24, instances/n5adv/best_fb_n24_seed124.pg sha1 f27b128efa82..), 9/35 (n = 32, best_fb_n32_seed132.pg sha1 0173afdccde9..);
every improved best checked (Zielonka + verify.py, all OK). The climb cannot make fallbacks dominate (<= 42%); forcing a stall at
every step needs a designed gadget (the lead above), not random search.
