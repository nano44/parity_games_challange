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

## Bench and killer families (interim table 20:2xZ by date -u; summarize_n5.py; start = best-reward except dlm1/dlm2 = DLM (σ0, τ0))
Iterations = N5 loop iterations; slope = local log-log exponent of iterations in n; fallback = classical switch-all steps taken
because N5 selection made no progress; every finished row: regions = Oink zlk (tl where zlk hit the 4 GB cap), strategies verified.
| family | N (n) covered | N5 iterations first .. last | slope (last 3) | fallbacks | rows checked |
| --- | --- | --- | --- | --- | --- |
| dlm1 | N = 1..40 (n = 4..82) | 1 .. 41 | [0.97, 0.98, 0.0] | 0 | 40/40 |
| dlm2 | N = 1..21 (n = 12..212); BUDGET600_REACHED at N = 22 | 2 .. 34 | [-0.61, 1.27, 1.25] | 0 | 21/21 |
| counter_symsi | N = 1..22 (n = 12..222); BUDGET600_REACHED at N = 23 | 7 .. 99 | [1.3, 0.22, 0.89] | 84 | 22/22 |
| deeptrap | N = 1..40 (n = 47..1295) | 4 .. 145 | [4.88, 0.55, 0.56] | 0 | 40/40 |
| padsae | N = 1..40 (n = 50..1220) | 5 .. 80 | [1.02, 1.02, 1.02] | 0 | 40/40 |
| switchallexp | N = 1..40 (n = 21..567) | 5 .. 80 | [1.01, 1.01, 1.01] | 0 | 40/40 |
| switchbestexp | N = 1..32 (n = 35..810); BUDGET600_REACHED at N = 33 | 20 .. 242 | [0.8, 1.47, 0.67] | 0 | 32/32 |
| recursiveladder | N = 1..40 (n = 5..200) | 1 .. 40 | [2.03, 0.0, 2.03] | 0 | 40/40 |
| tc | N = 1..26 (n = 8..2158); BUDGET600_REACHED at N = 27 | 1 .. 83 | [-1.9, 1.64, 1.51] | 3 | 26/26 |
| tc+ | N = 1..17 (n = 8..5304); BUDGET600_REACHED at N = 18 | 1 .. 178 | [0.25, 0.67, 0.57] | 7 | 17/17 |
| counter_core | N = 1..22 (n = 9..135); BUDGET600_REACHED at N = 23 | 2 .. 44 | [1.03, 1.02, 1.02] | 0 | 22/22 |
| counter_dp | N = 1..40 (n = 8..164) | 2 .. 40 | [0.0, 2.03, 0.0] | 0 | 40/40 |
| counter_m | N = 1..40 (n = 6..123) | 1 .. 21 | [1.97, 0.0, 1.98] | 0 | 40/40 |
| counter_ortl | N = 1..29 (n = 6..146); BUDGET600_REACHED at N = 30 | 2 .. 30 | [0.97, 0.97, 0.97] | 0 | 29/29 |
| counter_qpt | N = 1..40 (n = 2..80) | 1 .. 1 | [0.0, 0.0, 0.0] | 0 | 40/40 |
Random games (n5_random.py; harness/gen.py corpus): seed 1, 10,000 games n <= 60: AGREE 10000/10000, max 11 iterations; seed 2,
2,000 games n = 60..400: AGREE 2000/2000, max 15 iterations (n5/random.txt). Still running: counter_rob, counter_rr.
Reading (DATA, not a claim): no family shows super-linear growth of N5 iterations in n; the killers of N1/N2 (deeptrap, padsae)
and both DLM families are linear.
