# L-SI notebook (strategy-improvement design loop toward M4 / M4-R)
Overwrite the top sections; append to "Sources opened" and "Dead ends". Lane brief: Lead 2026-10-15 10:10Z, 12 h box to 22:10Z.

## Resume point
2026-10-15 10:20Z. Engine experiments/si/si.py validated (xcheck.py full: valuations equal to the PGSolver port on 1800
(game, strategy) pairs; switch-all counts equal the port's on 600 random games and switchallexp N=1..4; all 9 rules give
py-zlk's regions with verified strategies on 600 games). Candidates S1-S4 documented (docs/si/candidates/). Running:
families.py sweeps (out/fam_det.log, out/fam_rand.log), adversarial.py msf and rar (out/adv_*.log). Next: read the results,
write docs/si/RESULTS.md and DEAD.md, plots, check.sh, verify, push, message the Lead.

## Queue
1. Read sweeps; growth fits; DEAD.md entries with killer instances.
2. Adversarial searches for lsf, steepest, S4 (CPU-bound; 4 cores).
3. If any candidate shows polynomial growth everywhere: STOP and message the Lead.
4. End-of-box message: DONE / FINDINGS / NEEDS + candidate list with killers.

## Things only I know
- Engine conventions: priorities made injective by rank (p' = 2·rank + parity, rank by (pr, index)); path component a bitmask
  over ranks; comparison key = (reward of cycle node, signed weight Σ ±2^rank, ±length). Odd's final strategy = the
  restricted-graph counterstrategy recorded during evaluation (the argmin-over-successors shortcut is WRONG: it fails
  verify.py on 3/600 random games and on switchallexp, because a successor's path may pass through the vertex itself).
- The port counts the final non-improvable evaluation as an iteration: port K = my iterations + 1.
- Family generators: Oink tools in tools/oink/build (tc, tc+, counter_*), pgsolver_port.py for recursiveladder,
  switchallexp, switchbestexp. Sizes: switchallexp n = 14N + 7, switchbestexp n = 25N + 10, tc+ grows fast (N=8: 624).
- Hansen's 2012 thesis: pure.au.dk/portal/files/52906897/thesis.pdf → HTTP 403; www.cs.au.dk/~tdh/papers/dissertation.pdf
  (the URL the errata gives) → HTTP 404 (both 2026-10-15 ~10:10Z). Not opened. What it contains, per the errata 1410.7871
  p.2: an alternative 2^Ω~(m^{1/3}) lower bound for the original Random-Facet on MDPs (the published form is 1410.7530).

## Sources opened (arXiv id or DOI, theorem/section)
- Friedmann, "An exponential lower bound for the latest deterministic strategy iteration algorithms", LMCS 7(3:19) 2011,
  arXiv 1106.0778 (PDF opened 2026-10-15). Section 3: valuations, arena A_{G,σ}, improvement policy (conditions (1),(2)),
  Thm 3.2 (strict improvement), Thm 3.3 (regions from a non-improvable σ). Section 4: Lemma 4.1 (locally optimizing policy in
  poly time), Thm 4.2 (globally optimizing, [Sch08]), Lemma 4.3 ([Vög00]) with proof p.7: policy I^lin from a ≺-optimal σ*,
  at most |V_0| iterations; p.7 remark on intransitivity of optimal updates. Section 5: 1-sink games (definition). Thm 6.14:
  switch-all needs ≥ 2^n steps on G_n from ι_{G_n}; Thm 8.4: switch-best ≥ 2^n on H_n from ι_{H_n}.
- Zwick, "Improved subexponential analysis of the Random-Action-Removal algorithm for 2-player turn-based games and
  non-binary AUSOs", arXiv 2607.06334 v1. Section 4 (algorithm, steps 1-5), Appendix D Fig. 1 (pseudocode Rand-Act-Rem),
  Thm 8.2 (F(n,k) ≤ U(n,k), subexponential), section 3 (SI as AUSO on strategies with VAL_a ≺ VAL_b orientation).
- Friedmann-Hansen-Zwick, "Errata for: A subexponential lower bound for the Random Facet algorithm for Parity Games",
  arXiv 1410.7871 v1: abstract and p.1-2 (the RF = RF* claim is false; "The main result of [1] is thus flawed"; RF* bound
  stands; [5] Hansen thesis gives 2^Ω~(m^{1/3}) for RF on MDPs; [3] transfers it to shortest paths); section 2 (RF on
  shortest paths pseudocode).
- Friedmann-Hansen-Zwick, "Random-Facet and Random-Bland require subexponential time even for shortest paths",
  arXiv 1410.7530: Thm 6.3 (Random-Facet: ≥ e^Ω(√n) = e^Ω(M^{1/3}/log M) expected switches on G_{n,r,s,t}); p.1-2 (the SODA
  2011 bound was for parity games; the corrected bounds are for shortest paths / MDPs).
- van Dijk-Loho-Maat, "The worst-case complexity of symmetric strategy improvement", arXiv 2309.02223: Def. 2 (sink parity
  game), the generalisation J_σ(τ), J_τ(σ) (p.9, local valuation comparison), conclusion p.19-20 ("more than only local
  information", robustness against preprocessing).
- Disser-Loho-Maat-Mosis, "Lower bounds for ranking-based pivot rules", arXiv 2512.16684 v2: Thm 1.1 (informal: index-based,
  o(N/log N) memory, N^ω(1) on SI), Thm 1.2 (informal: MDP/LP rules ranking by index, reduced cost and objective improvement:
  2^Ω(√N); NOT stated for parity games), Thm 4.3 (ℓ-index-based rules, m^ω(1) on sink parity games), Lemma 4.6, Def. 3.4
  (neighbour ranking), p.3 "every deterministic memoryless pivot rule can be formulated as a ranking-based rule", Obs. 4.1
  (an N-memory rule solves a given game in linear time).
- Disser-Friedmann-Hopp, "An exponential lower bound for Zadeh's pivot rule", arXiv 1911.01074 v2: title page only (B8 source;
  not needed beyond the barrier table).
- Fearnley-Savani, LMCS 14(4:9) 2018, arXiv 1507.04500: title page only (B12).
- Fleet docs: TARGET.md v1.0; docs/DECISIONS.md D1-D6, L18-L19; docs/RESULTS.md DE1-DE3; docs/lit/RANKING.md §4;
  docs/lit/BARRIERS.md B8-B14; experiments/hard-families/README.md and pgsolver_si.py (port, stratimpralgs.ml line map).

## Dead ends
(see docs/si/DEAD.md once a candidate is killed; each entry here repeats the killer in one line)

## Freezing observation for MSF (2026-10-15 11:00Z; data + proof sketch, UNREFEREED, not a result)
Setting: VJ valuations, lexicographic order (cycle node first, then path set by rank, then length). Level of an improving edge
(v, w) = rank of the first difference between Ξσ(w) and Ξσ(σ(v)) (docs/si/candidates/S2.md). Call the switch cycle-creating
if v lies on the path set of Ξσ(w).
Claim F: a NON-cycle-creating single improving switch at level r changes no vertex's cycle node and no path bit of rank > r.
Data: experiments/si/freeze_test.py: 0 violations over ~6000 MSF switches on 6000 random games and ~6000 on 6000 1-sink
games (n ≤ 9), same for msfa and msfc; every observed violation is a cycle-creating switch (2-3 per 6000 games) or a
cycle-node change (all of them cycle-creating switches, to be re-checked).
Proof sketch: let τ be Odd's optimal counterstrategy for σ. Under (σ', τ) with σ' = σ[v→w], the play from any u either avoids v
(value unchanged) or runs P·v·(τ-path from w); the τ-path from w cannot re-enter P∪{v} (it would then reach v, contradicting
v ∉ path(w)), so its value is P ∪ {v} ∪ path(w) with the old cycle node, which agrees with the old value P ∪ {v} ∪ path(σ(v))
above rank r. Ξσ'(u) lies between Ξσ(u) (Friedmann Thm 3.2) and this value; two valuations agreeing above r sandwich only
valuations agreeing above r. Gap: the "cannot re-enter" step needs the τ-path from w under σ' to equal the one under σ,
true because the only changed edge is at v and the path avoids v.
Consequence (if F holds): in a run with no cycle-creating switches, MSF makes ≤ n switches at the top level, and level r is
revisited only after a higher-level switch; this gives only an exponential bound by itself (S_r ≤ n(1 + S_{>r})). The
adversary's tool is a high-level improving edge that is cycle-creating until low-level switches change the paths; then it
fires late and unfreezes everything below. Variants: msfa (prefer non-cycle-creating edges), msfc (prefer cycle-creating).

## Refinement (11:20Z, unrefereed): where MSF's iteration count can hide
Under Claim F and Friedmann Thm 3.2, in a stretch of an MSF run with no cycle-creating switch: a level-r switch at v makes
bit r of Ξ(v) good and bits above r never change (F) while Ξ(v) only improves, so bit r of v stays good until a switch at a
level > r; MSF takes the highest level available, and lower switches never create higher-level improving edges (F), so once
level k is exhausted it never recurs; hence at most n switches per level: ≤ n(n+1) switches in the stretch (sketch only; the
DLMM Bland counter shows the mechanism: MSF needs 1 switch, Bland/LSF 2^n - 1).
A cycle-creating switch (v on the path of w; the new cycle through v is even-dominated, level = rank of its dominator) either
changes some cycle node (at most n^2 such events in a run: each vertex's cycle node improves ≤ n times) or is "escaped" (Odd
reroutes, cycle nodes unchanged, high bits may change arbitrarily). So: MSF switches ≤ (n^2 + 1)·(n^2 + X + 1) with X = the
number of escaped cycle-creating switches. MSF is polynomial iff X is (modulo the sketch). The adversarial search now has an
objective "escapes" (adversarial.py --objective escapes) to maximise X directly.
