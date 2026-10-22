# (SPP): searches per phase of A_DTL — statement, data, what is proved (L-ALG succ. 5, 2026-10-17T00:37Z by date -u; produced on Opus 5.5)
Unrefereed. Source of truth for details: docs/alg/GAP-A-M.md §21 (tools and counts), §17 (ledger). A_DTL = `oink --dtl
--no-single --no-wcwc --no-loops` @ 8fbf0a7 (Lead reading L22), pseudocode docs/alg/candidates/C5-DTL.md, every order datum ω
(L26). This file states a CONJECTURE (DATA only) and the reduction it would complete.

## 1. Statement
- Phase: a maximal run of consecutive search(p) calls of one player with no dominion found before its last call.
  S = number of searches in the phase; G' = the unsolved vertices at its start.
- (SPP) For every game and every order datum ω, every phase of A_DTL has S ≤ |G'|.
- (SPP-sharp) S ≤ max(1, |G'| − 1). Tight: experiments/alg/dtl_chainfam.py UP=1 has S = |G'| − 1 for every k, both order
  data; experiments/alg/instances/spp_chain_up_n43.pg: pinned Oink 43 iterations, 42 of them in Even's phase, verified.
- Already false: S ≤ (p-parity vertices of G') + c, S ≤ (distinct priorities of G'), S ≤ (distinct p-parity priorities);
  instance experiments/alg/instances/spp_final_n20.pg (Oink order: S = 19, |G'| = 20, 14 p-parity vertices, 13 priorities).

## 2. Data (GAP-A-M §21a, §21e, §21i)
| source | phases | violations of (SPP) / (SPP-sharp) |
|---|---|---|
| corpus: experiments/alg/instances, instances/climbs_1016, experiments/red/** (191 games) | 416 Oink order / 424 stable | 0 / 0 |
| exhaustive n ≤ 3, priorities 0..3 (176,200 games), both orders | all | 0 / 0 |
| random games n = 2..8, 3,000 seeds per order | all | 0 / 0 |
| hill-climbs on max S − |G'| (n = 6..18, 300k-400k steps each) | best S − |G'| = −1 (S = |G'| − 1 reached at n = 6, 8, 12) | 0 / 0 |
| hard families tc, tc+, counter_* (sizes up to 492) | S ≤ 8 | 0 / 0 |
Longest climbed phases (box 4 and L-RED R21): 19 searches at n = 20, 30, 40 (Oink order); 14 at n = 60.

## 3. What (SPP) would give (GAP-A-M §21c; PROVED given (SPP))
- Phases ≤ D + 2 (PROVED, from run(), C5-DTL.md lines 141-142: a false search(p) ends p's searches for good): D = number of
  searches that find a dominion ≤ n.
- Searches ≤ Σ_phases |G'| ≤ n(n + 2); tangles ≤ n · searches ≤ n²(n + 2) (Lemma W, DTL-proof.md §3).
- Running time (DTL-proof.md §3(e)): O(n¹⁰ (m + n²)) word operations; all stored numbers fit O(log n)-bit words, so unit
  cost equals bit cost (TARGET.md §3). Any polynomial bound S ≤ poly(|G'|) gives a polynomial bound the same way.
- With GAP-C (completeness, open, docs/alg/DTL-proof.md §2.3) this closes the D2 polynomial-time part of gauntlet step 4.

## 4. Proved facts that a proof of (SPP) can use (unrefereed)
- First-Difference Lemma (GAP-A-M §21d; reading; per referee G-h1, closed by both referees: stated on the log with repeated sptl passes deleted): consecutive searches s, s+1 of a phase agree up to the first tangle
  attractor whose output differs; it has the same input and a strictly larger output; the cause is a tangle that s learned
  later in its call order; s+1 learns nothing before that point. DATA: that first difference is always in best_vertices or
  in the −1 attractor of search_rec, never in sptl or Dom (949 / 916 transitions).
- Lemma DV*-MONO (GAP-A-M §21h): a clean ideal root distance DV* (a function of T alone) is pointwise monotone in T, so it
  changes at most n(n + 1) times per phase (DV = DV*, the author's debug DV, is an OPEN claim with data only). It moves in only 465 of 990 transitions (Oink order), exactly where the
  author's own distance values (dtl.cpp computeDistanceValues) move.

## 5. Why no simple potential works (GAP-A-M §21d-§21i; docs/alg/DEAD.md last section)
A phase is a nested counter: absorption steps (tangles learned in one search are absorbed into an earlier removal in the
next) alternate with RES changes of depth-0 pruning results, which re-open absorbed vertices; the re-opened vertices are
then re-learned in new tangles (spp_final_n20: 38 re-opened, 33 re-learned). Every quantity tried that ignores this
structure (tangle unions, tops, settled labels, removal indices, fixed-input attractor sums; 13 candidates) fails on the long
phases. The open step is a global reason why reset-then-re-learn epochs never cost more than one vertex per extra search
(designer reading, GAP-A-M §21i).

## 6. For the attacker (L-RED, via the Lead)
A counterexample needs a renewable reset at less than one fresh vertex per extra search: a blocker shared across chain
vertices and across epochs, kept open by the pruning (distractions) rather than by the attractors. Starting points:
dtl_chainfam.py (absorption chain, S = n − 1), spp_final_n20.pg (3 resets), spp_final_n40.pg (dominion building).
