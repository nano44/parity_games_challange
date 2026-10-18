# Box 3 (b): two NEW (c) candidates, screened BEFORE code (L-NEW, 2026-10-18 from 18:40Z by date -u). Not implemented.

Screen used: docs/lit/BARRIERS.md B1-B20 (l-lit head), the dead-end record (N1, N2, N3 dead; docs/new/README.md), and the
deep-trap obstruction (docs/new/N3-blackwell-path.md, last section; DEEP-TRAP-LEMMA.md): a method dies if it must, at some
stage, cross "all traps -> parity-like optimum" by switch-all from the best-reward start, or if it reads reward MAGNITUDES so
that priority gaps hide structure; padding (isolated dummies per priority) blocks any priority compression.

## N4 TROP-SIMPLEX: tropical simplex with a fixed combinatorial rule on parity-induced mean-payoff games
Source (opened): Allamigeon, Benchimol, Gaubert, Joswig, "Combinatorial simplex algorithms can solve mean payoff games", arXiv
1309.5925 v2 (27 Jan 2014; SIAM J. Optim. 24(4) 2014), abstract page: every combinatorial simplex algorithm (pivoting depends
only on combinatorial data) has a tropical analogue that solves mean payoff games; tropical simplex over Hahn series plus a
symbolic perturbation making the MPG's LP non-degenerate; "any combinatorial simplex algorithm with a strongly polynomial
complexity (the existence of such an algorithm is open)" would give a strongly polynomial MPG algorithm. (Body NOT yet opened:
the exact theorem numbers, the LP built from the game, and the strategy extraction must be read before code.)
Pseudocode (to be fixed against the paper body): parity game -> MPG with weights (−n)^p (Jurdziński) -> for each vertex v, the
tropical LP whose feasibility decides "v winning for Even" (ABGJ's construction) -> symbolic perturbation -> tropical simplex
with the SHADOW-VERTEX rule (fixed, deterministic, combinatorial) -> winner of v; strategies from the final basis (each tight
inequality names an edge), verified by harness/verify.py.
Why new: no fleet lane runs a simplex on a tropical polyhedron (RANKING.md row 7 "IPM / tropical LP": never tried). Not SI: the
pivots walk a tropical polyhedron, not the strategy space; Friedmann's SI families have no known image there.
Barrier statement draft: B8-B12 (SI) do not apply (not an SI rule). B13 (Lemke / Cottle-Dantzig at fixed discount): different
polyhedron, no discount. B14 (AUSO): abstract, does not transfer. B15: IPMs, not simplex; only strong polynomiality. B19
(LDT): tropical simplex is presumably an LDT algorithm, but B19 bounds weight representability, NOT running time. Open risk:
classical shadow-vertex lower bounds (Goldfarb-type cubes) might tropicalize to MPG instances; whether such instances are images
of PARITY games (exponential weights (−n)^p) is the first question (the same question RANKING.md row 7 asks for IPMs).
Deep traps / padding: no discount, no horizon, no annealing; with weights (−n)^p every comparison of two sums of <= n weights is
decided by priority order, so priority GAPS change no comparison (gap-invariant), and isolated dummies add independent
constraints only. Deep traps are then just Odd-won side branches (top priority P on a path into an odd cycle). Neither kills
it by the N1 mechanism; whether the product structure of padding lengthens the shadow path must be checked in code.
Cost: HIGH (Hahn-series arithmetic or an exact perturbation, a tropical pivoting engine). More than one box.
Cheapest killer to try first: tropicalized Goldfarb-Sit / Klee-Minty-type shadow-vertex instances, then the M1 bench.

## N5 SSI-GLOBAL: symmetric SI whose step is the BEST subset of improving switches against the opponent's current strategy
Source (opened): van Dijk, Loho, Maat, "The worst-case complexity of symmetric strategy improvement", arXiv 2309.02223 (CSL 2024),
pdf sha256 10e6794d82aba465..: Algorithm 2 (SSI, Schewe-Trivedi-Varghese ICALP 2015): I ← f((Iσ ∩ {(v, τ̄(v))}) ∪ (Iτ ∩
{(v, σ̄(v))})) with τ̄, σ̄ optimal counterstrategies and f any improvement rule; Algorithm 3 (generalized SSI): f applied to
(Iσ ∩ Jσ(τ)) ∪ (Iτ ∩ Jτ(σ)), Jσ(τ) = {(v, w): Ξτ(w) ⊵ Ξτ(σ(v))}. Theorem 1 (p. 2): exponential "independently of the improvement
rule", any valuation in the literature; strengthened to Algorithm 3. p. 3: "one needs a different approach involving more than
only local information".
Pseudocode: start σ, τ (best-reward). Loop: compute Iσ (Even's improving switches for σ, VJ valuations) and Iτ. Let A_σ =
{σ' : σ'(v) ∈ {σ(v)} ∪ {w : (v, w) ∈ Iσ}} (keep or take an improving switch, per vertex). σ_new := the element of A_σ that is
OPTIMAL for Even in the one-player game "Odd fixed to τ" (Even restricted to the edges of A_σ): a one-player parity/VJ problem,
solved exactly. Symmetrically τ_new := the element of A_τ optimal for Odd against σ fixed. Apply both. Stop when Iσ = Iτ = ∅.
Correctness / termination: σ_new applies a SUBSET of improving switches to σ (each vertex keeps σ(v) or takes an edge of Iσ),
so it strictly improves Even's valuation unless no switch is taken (standard SI lemma); the same for τ; Lemma 5 of 2309.02223
(no improving pair => both optimal) gives correctness at the stop.
Why new: the selection is not a rule f on DLM's set I (Algorithms 2, 3): it chooses among ALL improving switches Iσ (not
intersected with the counterstrategy's edges) by a GLOBAL criterion that depends on τ on the whole arena (a one-player optimum),
which is the "more than only local information" DLM name as the open direction. Not in L-SI's S1-S7 (single or switch-all rules
on σ's own valuation only).
Barrier statement draft: B8 (named rules) and B9 (index-based, single switch) do not apply (multi-switch, valuation-based). B10
(randomized): deterministic. B11: formally outside (not f applied to I or to the Algorithm 3 set), but DLM's families are the
first test, since the selection may coincide with an f on I on their instances. B12 (path prediction): about all-switches SI.
Deep traps / padding: VJ valuations are priority-ORDER based (no magnitudes, no horizon), so gaps and padding change nothing;
in the deep-trap game every trap option is the worst option for Even under VJ (odd cycle q = B + 1 above every original
priority), so traps are never chosen after the first step and the run is that on switchallexp, where SSI-type methods are fast
(STV's motivation); N1's mechanism has no lever.
Cost: MODERATE: VJ valuations exist (experiments/si/, L-SI's engine; read only); the one-player optimum under VJ valuations can
be computed by SI for one player with Odd fixed (strongly polynomial for deterministic one-player? to be checked; for the
experiment any exact method will do, its cost counted separately). Checked as N1 (Zielonka + verify.py).
Cheapest killer to try first: DLM's families (Oink counter_symsi is van Dijk's symmetric-SI counter; check that it is the
2309.02223 family), then the 13-family bench and the deep-trap / padded families, then random games.

## Recommendation
N5 first (cheap, a direct test of the open direction DLM name). N4 only as a literature-first item (open the body of 1309.5925
and the tropicalized shadow-vertex lower-bound question) because its implementation is more than a box.
