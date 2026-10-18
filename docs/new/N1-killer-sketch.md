# N1 killer: construction sketch (L-NEW, 2026-10-18 10:45Z; for routing to L-RED after gauntlet step 2)

Target: violate (PHASE-POLY) (docs/new/N1-disc-anneal.md): a family G_N, poly size, where ONE phase of N1 makes 2^Ω(N)
Howard switches. N1 = Loff-Skomra IncreasingDiscountPI (2610.22149 Fig. 7.2) with rewards (−n)^pr (sign as Jurdziński).

## What the data say N1 does on Friedmann's switchallexp (unrefereed reading)
- Straight at the final γ, Howard replays Friedmann's counter exactly (ablation = 30, 70, 150, 310, 630). With the schedule
  the count is ~2N² and the largest phase is 2N + 5 (the last one).
- At γ_j the discounted order sees a far, high-priority difference only once γ^t · n^Δp beats the nearer terms. The
  bits are therefore "revealed" over a range of j, and each phase starts from the optimum of the previous one. Plausible
  mechanism for the 2N² count: high bits settle first, and a lower bit, once visible, is set once. That is, NO RESET
  ever happens inside a phase.
- Invariances found: priority spreading p -> Kp leaves the run unchanged (only the phase count scales). Uniform,
  priority-monotone and bit-indexed delay chains (lengths up to 24, or 2(i+1)) leave the growth unchanged. Per-edge delay
  search at N = 2 raised the count from 25 to 49 (plain Howard on the base: 30); no family yet.

## The construction needed (two routes)
(A) Bottom-up reveal. Make bit i's decisions visible at phase j_i with j_0 < j_1 < ... (low bits first). In the phase
    where bit i appears, all lower bits are already visible and at their optimum. Howard from the state "bit i = 0, lower
    bits = optimum" then has to count through the lower bits again (Friedmann's reset). That is ~2^i switches inside one
    phase, so (PHASE-POLY) fails. Requirement: per bit, a delay or reward structure that hides bit i's long-range difference
    until horizon H_i, with H_i increasing in i. It must not change the VJ/Friedmann order at γ -> 1, which needs a
    1-sink game (Lemma 9.6 of 1106.0778). Small bit-indexed delays (c = 2, 8) did NOT do it. Unknown whether lengths of
    order H_i · Δp · ln n (polynomial, ~10^3-10^4 vertices at N = 4) do; this is beyond the exact Python engine (the C++
    port, item 4 of the Lead's list, is the prerequisite).
(B) Bait start. Make the optimum at every horizon below H equal to Friedmann's bad start σ_0, and reveal all of the
    counter between H and 2H. Then one phase is plain Howard from σ_0, i.e. Friedmann's 2^N. Obstruction seen: in a 1-sink
    game the chains' own rewards compete with the targets' path differences, so σ_0 is the short-horizon optimum only
    if x(σ_0(v)) sits above the sink baseline at short horizon. Friedmann's start does not have that property in general.
    A bait gadget (an extra early reward on σ_0's edges that vanishes in the VJ order: a priority below all original ones,
    repeated k times so that k·n^0 matters only at short horizons) is the next thing to try.
Either route needs the C++ engine for N >= 4. Cheapest first instance to try: switchallexp N = 2, 3 with route (B),
since it needs only O(n) extra vertices.

## Status
Sketch only. No instance kills N1 yet. Barrier rows that would then cover N1: none published (B8 covers fixed-γ
Howard only); a kill would be a new lower bound for LS24's IncreasingDiscountPI on worst-case (parity-induced) inputs.

## Route (B) first try (10:55Z, experiments/new/bait.py): did not kill
Chain of k priority-0 Odd vertices on each start edge (originals +2). Plain VJ Howard: 15, 35, 75 (still doubling, N = 2..4).
N1: k = 4: 30, 50, 72; k = 16: 33, 51, 74 (largest phase 9, 11, 13 = the last one). Regions = Zielonka, strategies verified.
