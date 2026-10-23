# N8 screen: untested candidate mechanisms for (c), ranked (L-NEW successor 5, Opus 5.5; box 13, SCREEN ONLY, no code)
Lead brief 01:39Z 2026-10-23 (date -u). Rule applied first (notebook, DE25/DE26, BARRIERS B21): no candidate may rely on the parity →
discounted reduction without a γ-free argument (HMZ arXiv 1008.0530 Thm 6.5). Then: not covered by BARRIERS B1-B21, RANKING.md, or the
dead-end record DE1-DE27. Result: THREE candidates pass (§1-§3, ranked); FIVE screened out with the reason (§4). No code was written.
Every source below was opened in this session; sha256 prefixes of the PDFs (scratchpad) or the arXiv id with theorem number.

## Ranking (score = P(survives gauntlet step 2) × leverage; both are L-NEW estimates, not results)
| rank | candidate | P(step 2) | leverage | why this order |
| --- | --- | --- | --- | --- |
| 1 | N8a: Koh-Loho strategy iteration over a universal tree, with a GLOBAL pivot rule | ~0.15 | high: per iteration polynomial, worst case already quasi-polynomial; a polynomial pivot rule would be a polynomial algorithm | the authors leave exactly this open; nothing in B1-B21 covers SI over L(T) |
| 2 | N8b: Sherali-Adams lift of the positional-strategy + potential mixed-integer program | ~0.02 | very high: a constant level that is exact would put parity games in P | untested; cheap kill test; but prior for low-level exactness is poor |
| 3 | N8c: N5 with best-reply hysteresis (a player may not return to a best reply it left) | ~0.7 | low: N5 already survives step 2; the change targets the toggle mechanism of box 11 but brings no proof handle | survives easily, buys little |

## 1. N8a (rank 1): Koh-Loho tree strategy iteration with a global pivot rule
(a) Mechanism. Koh, Loho, "Beyond value iteration for parity games: strategy iteration with universal trees", arXiv 2108.13338 (LMCS 21(2)
2025; sha256 21ee0e4336252f7e). Fix an (n, d/2)-universal ordered tree T; node labelings µ: V → L̄(T) (leaves plus ⊤). Odd holds a
strategy τ; µ is the least fixed point of the one-player game (G_τ, π) that is pointwise ≥ the current µ (§1 p.3, "we force µ to increase");
an Odd arc violated w.r.t. µ is admissible; the pivot rule picks admissible arcs; terminate when none (Theorem 3.1: the result is the
pointwise minimal node labeling µ*, which decides winning by Jurdziński's Theorem 2.3). Each iteration is one least-fixed-point
computation: O(d(m + n log n)) for the perfect n-ary tree of height d/2 (Theorem 4.5), O(mn² log n log d) for the Jurdziński-Lazić tree,
O(mn² log³ n log d) for the Strahler tree (§1 p.3). The candidate is the PIVOT RULE: (i) "global": switch to the τ' that is optimal for
Odd in the arena gated by the admissible arcs (N5's one-sided step transplanted to L(T)); (ii) switch-all as the control.
Potential: Φ(µ) = Σ_v rank of µ(v) in L̄(T); it rises every iteration, so iterations ≤ n|L(T)| (§1 p.3, "trivially bounded"): quasi-polynomial
with the JL/Strahler tree. A polynomial bound needs a rule under which every iteration raises some vertex past a whole subtree of T
(a "level" of the tree), not a single leaf; the measure to bound is the number of (vertex, tree level) pairs that change.
(b) Coverage. Koh-Loho §1 p.3: "Identifying a pivot rule that may provide strictly improved (and possibly even polynomial) running time
is left for future research." B1/B2 (separator / universal-graph size) bound the SIZE of L(T), not the number of SI iterations, which may
leap across L(T); B3 (ANP, tree-driven nested fixpoint recursion with fixed trees) covers attractor-style recursion, not SI pivots; B8-B12
are proved for SI over VJ / discounted valuations; Friedmann's constructions (B8, arXiv 1106.0778, including the globally optimal rule:
abstract "the second variant computes the globally optimal improvement in each step") do not apply as theorems to the L(T)-valued
least-fixed-point framework, where a strategy may repeat (§1 p.3) and Ohlmann's impossibility (cited there) rules out VJ-type valuations
on L(T). Fleet: only cited in docs/sources/landscape-2026.md (rows 82, 144, 152); never implemented (grep 2108.13338 in docs/, experiments/,
notes/: L-LIT notes and the landscape only). Closest dead ends: DE4/DE7/DE8 (L-SI single-switch rules on VJ valuations) and N5 (alive,
G-N5-TIME); difference: the value domain is L(T) with forced-increase least fixed points, so every run is quasi-polynomial by construction.
(c) Cheapest kill test. Perfect n-ary tree of height d/2 (simplest least-fixed-point routine, Theorem 4.5), pivot rules global and
switch-all, on tc N = 1..8: tc is exponential for the progress-measure algorithms on the SAME tree (BARRIERS B6: spm/tspm), so the
question "does SI leap where value iteration crawls?" is answered on one family; then counter_qpt (built against the quasi-polynomial
algorithms; M1: super-polynomial for QPT). Kill = super-polynomial iteration growth on either; every run verified (verify.py + Oink zlk).
(d) Sources: 2108.13338 §1 p.2-3, Theorem 2.3, Theorem 3.1, Theorem 4.5; arXiv 1106.0778 abstract (sha256 46c96f44775aa2b0); BARRIERS B1-B3, B6.

## 2. N8b (rank 2): Sherali-Adams lift of the strategy + potential mixed-integer program
(a) Mechanism. With Jurdziński weights w(v) = (−n)^{p(v)} (O(d log n) bits, NO discount), Even wins everywhere iff there is a positional σ
whose graph has only positive cycles, iff ∃ σ ∈ {0,1}^E (one edge per Even vertex) and potentials π ∈ Q^V with π(v) ≤ w(v) + π(u) − 1/n
for every Odd edge (v, u) and for every Even edge with σ_vu = 1 (big-M: + M(1 − σ_vu), M = O(n^{d+2}), polynomial bits). Winning regions
by one such program per candidate region (or the standard attractor peeling). The candidate: solve the level-k Sherali-Adams lift (k
fixed) of this program and read the region from its feasibility. Level n is exact (arXiv 1405.0945 §1 p.2: "the relaxation at level n is
exact, i.e., the associated polytope is equal to the integral hull"); level k has n^{O(k)} variables, polynomial for fixed k (same page).
Measure: the smallest exact level k*(G) on each family; polynomial iff k* = O(1) on all games.
(b) Coverage. Not the discounted reduction (screen rule passed: weights only, no γ). Not Schewe's LP (§4, S1: doubly exponential
coefficients). Not B15/B21 (IPM complexity statements), not B19 (LDT weight compression: the lift pays the weights' bits). No BARRIERS
row, RANKING row or DE covers lift-and-project for parity or mean-payoff games; a search (2026-10-23) found none either. Closest dead
end: DE25 (N6, IPM on the JS LCP); difference: an exact-at-level-k polyhedral formulation with no discount and no path following.
Known danger: lift-and-project ranks are often n for tiny problems (arXiv 1605.03019 §1: Sherali-Adams needs n levels to detect an empty
integer hull of a simple polytope; sha256 cb6029755abff8a9).
(c) Cheapest kill test. Level 1 and 2 lifts on HIJ's arena (gen_hij.py, trivial games) and tc N = 1, 2 (with an off-the-shelf LP solver):
an integrality gap (lift feasible while Odd wins somewhere) at level 2 on tc 2 kills it; the growth of k* on tc N = 1..3 decides.
(d) Sources: arXiv 1405.0945 §1 p.2 (sha256 4c6956dc2f1db3ee); arXiv 1605.03019 §1 (sha256 cb6029755abff8a9); Schewe MFCS 2009 (§4).

## 3. N8c (rank 3): N5 with best-reply hysteresis
(a) Mechanism. N5 (docs/new/N5-ssi-global.md) plus a memory: once a player's best reply σ̄ (or τ̄) leaves a state, the gate excludes
improvements whose only effect is to bring the opponent's best reply back (box 11's toggle: σ̄ cycling among 4 states, sbe2_s21).
Potential: (Ξσ, Ξτ) as in R15 plus the number of forbidden best-reply states (≤ the number of distinct best replies seen).
(b) Coverage. Not discounted; N5 itself is not covered (T20 step 3 signed with caveats). Closest dead end: none; closest record:
N5-brchanges-box11.md (no invariant for best-reply changes) and N5-toggle-box11.md (toggles buy a constant per segment). Difference:
it forbids the toggle instead of bounding it. Weak point (stated now): box 11 showed toggles do NOT lengthen runs (§5 there), so the
change attacks a mechanism that is not the bottleneck; it gives no new proof handle for G-N5-TIME.
(c) Cheapest kill test: n5.py variant on the box-11 climbed instances (srev_vc25, it_sbe, glob_sbe; experiments/new/instances/br11b) and
the bench; kill = an incorrect run (the memory can block the optimum) or growth above N5.
(d) Sources: fleet files named above; RESULTS R15 (termination potential).

## 4. Screened out (with the reason)
- S1 IPM / LP solver on Schewe's LP for parity and payoff games (Schewe, "From parity and payoff games to linear programming", MFCS 2009,
  LNCS 5734 pp. 675-686; author PDF cgi.csc.liv.ac.uk/~sven/mfcs09.pdf, sha256 d27bbc79ab6b162b): §1 p.2 "the constants are exponential in
  the edge weights of the mean payoff game, and doubly exponential in the number of colours for parity games"; Cor. 6-8: polynomial only
  for a bounded number of colours. Exponential bit size, so a bit-model LP algorithm gives nothing (TARGET §3). Dead by bit cost.
- S2 multi-switch least-recently-considered SI with per-edge memory (outside B9: multi-switch, Θ(m) memory). Single-switch round-robin is
  exponential (Avis-Friedmann arXiv 1305.3944 v1 abstract, Theorem 4; sha256 d1fafb8b5d0b822c), and switch-all with Fearnley's snare
  memorisation is super-polynomial (Canavoi-Grädel-Rabinovich arXiv 1210.2459 abstract; sha256 02fca6a45515f2ec). Not covered by a
  theorem, but every history rule tried on VJ valuations has fallen to a Friedmann-type construction; low novelty, low leverage.
- S3 Schewe's optimal (globally optimal) strategy improvement: covered by Friedmann arXiv 1106.0778 (abstract; B8).
- S4 adaptive (lazily grown) progress-measure trees without a universal tree: ill-defined as a solver. A vertex can be declared ⊤ (Odd
  wins) only when its measure exceeds every leaf of a tree known to be universal (Jurdziński's Theorem 2.3 as restated in 2108.13338
  §2); without that guarantee lifting either never terminates on Odd's region or needs the universal tree, which brings B1-B3 back.
- S5 any further method on the discounted reduction (soft/regularised, barrier, homotopy): fails the screen rule unless a γ-free argument
  is supplied (DE25, DE26, B21; HMZ Thm 6.5).

## 5. Verdict for the Lead
N8a is the one candidate with both a real chance and real leverage: it is quasi-polynomial in the worst case by construction, its
open question (the pivot rule) is stated by its authors, and the cheapest kill test (perfect tree, tc, where value iteration on the same
tree is exponential) is a single family. N8b is a cheap long shot. N8c is not worth a box on leverage. Nothing was implemented.
