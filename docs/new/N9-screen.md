# N9 screen: untested approaches for (c), ranked, top two tested (L-NEW successor 7, Opus 5.5, D15; box 18)
Lead GO 2026-10-23 16:16Z (date -u), brief received 16:04Z. SCREEN plus kill tests; nothing frozen; no running-time claim.
Lead criterion (16:16Z): prefer approaches whose correctness and progress do NOT come from a local-improvement potential; if one is
proposed, say exactly why a counter cannot lap it. The fleet lesson it encodes: every local-improvement pivot rule tried so far,
deterministic or random (N5, N8a, N8d, the DTL attacks), fell to a lapping counter, the last two with delay lanes (R53, R56 §4).
Labels: PROVED (full argument here), DATA (a committed script reproduces it), READING (interpretation), OPEN.

## Ranking (P = L-NEW estimate of surviving the kill test before it was run; leverage = what survival would buy)
| rank | id | approach | progress mechanism | P(kill test) | leverage | cost | tested in box 18 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | N9a | fixed-level Sherali-Adams lift (SA+_k) of a small-coefficient 0-1 program ACYC for "Even wins every vertex" | none: one LP feasibility test | 0.10 | very high (constant k exact = polynomial) | 1.5 h | YES: §1(f), level 1 and 2 not exact; k* grows on a one-player family |
| 2 | N9b | certified LP-guided peeling: round the level-1 lift of the region program REGION, certify by a one-player solve, remove the attractor, repeat | decided vertices (monotone, <= n rounds) | 0.05 | high | 1 h (reuses N9a) | YES: §2(f), stuck on 5- and 6-vertex games |
| 3 | N9c | simulation-pruning kernel: delayed-simulation quotient and dominated-edge deletion to a fixed point, with attractors | game size (monotone) | 0.02 | medium | 2-3 h | no |
| 4 | N9d | N4 revived: ABGJ tropical simplex with the shadow-vertex rule on the parity-induced mean-payoff LP | pivots (a local rule on a tropical polyhedron) | 0.05 | high | > 6 h | no (local pivoting; §4) |
Order: N9a and N9b are the only two whose progress is not a pivot potential at all and whose kill test fits in 2 h; N9a has the larger
leverage. N9c is a known heuristic (§3); N9d is local pivoting, the class the Lead's criterion warns against.

## 1. N9a (rank 1): fixed-level Sherali-Adams lift of ACYC
(e) Exact pseudocode (implemented in experiments/new/sa/sa.py).
- ACYC(G). Binary s_e for each edge e = (v, u) of an Even vertex v with >= 2 distinct successors; sum_u s_vu = 1 for each such v.
  For each odd priority p and each vertex x with pr(x) <= p, a continuous f_p(x) in [0, n]. For each edge x -> y with pr(x), pr(y) <= p:
  f_p(x) - f_p(y) >= [pr(x) = p] - M (1 - s_xy) with M = n + 1, where the M term appears only for variable edges (Odd edges and
  single-successor Even edges are always active).
- Lemma A (PROVED). ACYC(G) has an integral solution iff Even wins every vertex of G.
  Proof. Even wins every vertex iff some positional sigma leaves no cycle of G_sigma with odd maximum (positional determinacy;
  a cycle of G_sigma with odd maximum is reachable from each of its own vertices, so Odd wins there). A cycle has odd maximum p
  iff it lies in G_sigma[pr <= p] and contains a vertex of priority p. (=>) Fix such a sigma and an odd p. No cycle of
  G_sigma[<= p] contains a p-vertex, so f_p(x) := the largest number of p-vertices on a path from x in G_sigma[<= p] is finite,
  lies in [0, n], and satisfies f_p(x) >= f_p(y) + [pr(x) = p] on every active edge. For an inactive edge, f_p(x) - f_p(y) >= -n
  = 1 - M >= [pr(x) = p] - M. (<=) If some cycle C of G_sigma has odd maximum p, sum the constraints of its (active) edges:
  0 >= (number of p-vertices on C) >= 1, a contradiction. []
  All coefficients are at most n + 1 (no Jurdzinski weights, no discount), so every LP below has polynomial bit size.
- SA_k: multiply every constraint (including 0 <= s <= 1, 0 <= f <= n and the equalities) by prod_{e in S} s_e prod_{e in T} (1 - s_e)
  for disjoint S, T with |S| + |T| <= k; linearise s_e^2 = s_e, y_A = prod_{e in A} s_e (|A| <= k + 1), q_{A,x} = y_A f(x) (|A| <= k).
  SA+_k adds the products of each choice equality with q-monomials: sum_u q_{A + vu, x} = q_{A, x} (|A| <= k - 1), which are valid
  for every integral point. Monomials with two edges of one Even vertex are set to 0. Multipliers with two edges of one vertex in
  S u T, and T-factors of out-degree-2 vertices, are dropped: with the SA+ equalities they are linear combinations of kept
  multipliers (without SA+ they are not: dropping them first weakened K_3 at k = 1, which is how the SA+ equalities were found).
- Algorithm N9a(k): answer "Even wins every vertex" iff SA+_k(G) is feasible. Regions would need more queries; the kill test needs
  only this one, because any algorithm built on SA+_k inherits a wrong answer to it.
(a) Barrier to evade. No BARRIERS row is about lift-and-project. B15 and B21 bound interior-point PATH lengths, not the bit-model
  cost of one LP of polynomial size and bit size (ellipsoid or any polynomial LP algorithm). B19 (Loho-Maat-Skomra) is a weight-
  compression barrier for linear decision trees, not a running-time bound, and ACYC has no large weights. B1-B3 are about separator
  sizes and fixed-tree fixpoint recursions; SA has neither. The counter lesson: there is no iteration to lap; a counter could only
  appear as an integrality gap that persists to level k. The real barrier is therefore the integrality-gap literature for SA, whose
  typical mechanism (locally consistent fractional distributions over small sets of variables, as in the ATSP SA lower bounds of
  arXiv 1405.0945) is exactly what a cycle of many choices offers.
(b) Why it might evade (READING). The lift at level n is exact (1405.0945 §1, l.118-119: "the relaxation at level n is exact"), and
  parity cycles are certified by short potentials (Lemma A: values at most n), unlike mean-payoff weights. If odd cycles of every
  sigma could be refuted by products of few choice variables, a constant level would suffice.
(c) Cheapest falsification test. k*(G) = least k with SA+_k(G) infeasible on games that Odd wins somewhere, on (i) random games,
  four queries each (G, G[W_O] and the same on the dual game, where the answer is known from Zielonka); (ii) exhaustive tiny games;
  (iii) structured one-player families where every sigma has an odd cycle: the ring R_L, the complete digraph K_n, and the
  circulant circ(n, 1, 2) (v -> v+1, v+2 mod n), all vertices Even, all priorities 1. Kill = k* growing with n.
(d) Cost: 1.5 h (done). LP size at level k is about C(m, k) 2^k times the number of constraints; level 3 at n = 7 takes 273 s here.
(f) Results (DATA unless labelled; scripts in experiments/new/sa/, outputs in experiments/new/sa/results/).
- Sanity (sanity.py, 150 random games n <= 6): integral ACYC = Zielonka's "Even wins all" on all 150; SA+ at full level is exact on
  the 140 with <= 8 variable edges; feasibility is monotone in k; no yes-instance was ever infeasible (asserted in every script).
- Level 1, random (gaps.py, 3,000 games n = 3..14, 8,196 queries): 44 gaps (rand3000_n3-14_k1.txt). Level-1 gaps occur in
  one-player games (smallest seen: r2067 Q3, n = 4, every vertex of one player, every priority odd for the other).
- Level 1, exhaustive (exh.py): every game with n = 2, priorities <= 3 (576 games, 1,296 queries): 0 gaps; n = 3, priorities <= 2
  (74,088 games, 175,356 queries): 72 gaps (exh_n3_P2_k1.txt).
- Level 2 on the level-1 gaps: the first 20 of the 44 random gaps (the run stopped at its 1,200 s limit) all close at level 2
  (kstar_rand3000.txt).
- Families (all vertices Even, all priorities 1: Odd wins every vertex):
  | family | n | k* |
  | --- | --- | --- |
  | ring R_L, L = 1..6 | 3..18 | 1 |
  | K_n (no self-loops) | 2, 3, 4 | 1, 1, 2 (K_5 level 2 did not finish in 400 s) |
  | circ(n,1,2) | 3, 4, 5, 6, 7 | 1, 2, 2, 2, 3 |
  | circ(n,1,2) | 8, 9, 10 | running at this push (kmax 4) |
  | random 2-out, n = 7, seeds 1..40 | 7 | 2 on 39, 3 on 1 (seed 40) |
- Verdict on N9a (DATA): SA+_1 and SA+_2 give WRONG answers ("Even wins every vertex") on one-player games that Odd wins
  everywhere: circ(4,1,2) (k = 1) and circ(7,1,2) (k = 2; instances/circ12_n7.pg, sha1 4a1973a88a1311966ef5d2f5382221aef3d09c3e;
  Oink zlk: Odd wins all 7). For each fixed k the step-2 run would be incorrect on some circ(n,1,2) IF k* is unbounded there:
  that is a READING from k* = 1, 2, 2, 2, 3 (n = 3..7), not proved. Mechanism (READING): in circ(n,1,2) every sigma is a functional
  graph, so a cycle exists, but the cycle can use any of exponentially many choice patterns; a refutation by products of k choice
  variables must cover all of them, and locally consistent fractional choices survive as long as k is small against the cycle length.
  The gap is in the one-player core of the problem (detecting that every sigma closes an odd cycle), which a preprocessing step
  (one-player games are easy) does not remove from two-player games that embed it.

## 2. N9b (rank 2): certified LP-guided peeling
(e) Exact pseudocode (experiments/new/sa/peel.py).
- REGION(G): binary r_v (v in an Even dominion D), s_e for Even edges, f_p as in ACYC. Odd v: r_v <= r_u for each successor u != v.
  Even v: sum_u s_vu = r_v and s_vu <= r_u. Edge x -> y with pr(x), pr(y) <= p: f_p(x) - f_p(y) >= [pr(x) = p] - M (1 - a_xy) with
  a_xy = s_xy (Even x) or r_x (Odd x). Maximise sum_v r_v. Integral optimum = |W_E| (W_E is the largest Even dominion; proof as Lemma A,
  restricted to D).
- Round: solve the level-1 lift (multipliers 1, b, 1 - b for every binary b); sigma(v) = argmax_u s_vu (ties: lowest index).
  Certify: S = vertices from which sigma wins in G (Odd one-player solve on G_sigma); S is an Even dominion. If S is empty, do the
  same on the dual game for Odd. Remove the attractor of the certified dominion for its owner; repeat. STUCK if both sets are empty.
- Correctness (PROVED, elementary): every removed vertex is won by the claimed player (certified dominion plus its attractor), so
  every answer the procedure gives is correct; it stops after at most n rounds, each one polynomial-size LP plus linear work.
(a) Barrier to evade. B7 (polynomial partial solvers are incomplete by example) and the B4 gap: N9b is a partial solver, so it must
  be complete to matter. The counter lesson does not apply: progress is the number of decided vertices, which only grows and is at
  most n; there is no potential to lap. Its only failure mode is STUCK.
(b) Why it might evade (READING). The LP value is an upper bound on |W_E| that is exact on many games (level 1 reports 6.0 = |W_O| on
  r26 below), so the fractional strategy carries information that fatal-attractor rules (B7) do not use.
(c) Test: random games and the smallest members of the hard families; kill = a STUCK game. (d) Cost: 1 h (done).
(f) Results (DATA; peeltest.py; every solved game agrees with Zielonka, asserted).
- 300 random games (seeds 0..299, n = 3..12): solved 294, STUCK 6. Smallest: r26 and r90, n = 6, stuck in round 1
  (instances/peel_r26.pg sha1 86542531214dd56ef1e21adb6e816448ffbe8f13, peel_r90.pg sha1 0e11fe886ba50fddea428a1dd0369fb35bb7bfae;
  Oink zlk: Odd wins every vertex of both). On r26 the Odd-side level-1 LP value is 6.0 (exact), yet the rounded strategy wins
  nowhere; on r90 level 0 rounding happens to succeed and level 1 fails, so the outcome depends on which optimal vertex HiGHS returns.
- 2,000 random games (seeds 1000..2999, n = 3..14; peel_rand2000.txt): solved 1,943, STUCK 57. Smallest STUCK: r1147 and r2136,
  n = 5, round 1 (instances/peel_r1147.pg sha1 68a8c41b926e2fd324b196c99c4c61ea6d2a91ed, peel_r2136.pg sha1
  88fe33cbfe579dc8901308a5a9fe3ebcabf53a74). r1147: 5 vertices, 4 of them Odd's; Oink zlk: Odd wins every vertex.
- Hard families, smallest members (tc, tc+ N = 1, 2; counter_* N = 1..3 up to 33 vertices; switchallexp N = 3): run in progress at this push; so far STUCK on counter_symsi N = 2 (n = 22) and N = 3 (n = 32), round 1.
- Verdict (DATA): N9b as stated is incomplete, smallest STUCK instance at n = 5. Untested variants (not proposed for a box):
  higher level; rounding by conditioning (fix the most confident edge, re-solve, keep it only if the LP value does not drop). The
  rounding failure on r26 at an exact LP value says the fractional optimum is a mixture of strategies none of which wins on its own,
  so better rounding needs a different LP, not a different threshold.

## 3. N9c (rank 3, not run): simulation-pruning kernel
- Mechanism: compute a polynomial-time simulation preorder for parity games (delayed simulation, Fritz's thesis, Kiel 2006, ch. 3;
  §3.3 "this relation can be computed in polynomial time"; §3.4 restricted versions for quotienting and transition deletion; Janin's
  direct simulation is cited there), quotient and delete dominated edges, take attractors and SCC splits, repeat to a fixed point.
  Progress = the game shrinks (monotone): no counter can lap it.
- (a) Barrier: B7 / B4, as N9b: complete or useless. (b) Reading: none strong. Fritz §3.5 (l.8015-8018 of the text) already reports
  that "solving a given parity game using Jurdzinski's lifting algorithm directly is faster than first simplifying", and on tc-type
  games (every vertex has distinct behaviour) no edge is dominated. (c) Test: exhaustive n <= 4 games, kill = an irreducible game
  with undecided vertices. (d) Cost: 2-3 h (delayed simulation needs its own game). Expected to die at once; it buys no proof handle.

## 4. N9d (rank 4, not run): tropical shadow-vertex simplex (N4 revived)
- Mechanism: the ABGJ tropical simplex (arXiv 1309.5925, cited in N4N5-proposals.md, NOT re-opened in this box) with the shadow-
  vertex rule on the mean-payoff LP of the parity-induced game. Progress is a pivot on a tropical polyhedron: a local rule, so the
  counter lesson applies directly and the screen would need an argument why no lapping counter exists on tropical shadows; none is
  known to me. (c) Test: switchallexp and tc N = 1..6. (d) Cost > 6 h. Ranked last by the Lead's criterion; not proposed for a box.

## 5. Screened out before ranking
- k-consistency / bounded-width Datalog on the max-atom (tropical) CSP that encodes mean-payoff games. Bodirsky-Mamino, "Tropically
  convex constraint satisfaction" (arXiv 1506.04184; abstract l.9-16; Thm 5.1: CSP(Gamma_t) in NP ∩ co-NP) give membership, not a
  bounded-width result; the domain is infinite (integers), so k-consistency is not an algorithm as stated, and a finite-domain version
  needs domains of size about the progress-measure range, which brings back B1/B2.
- Bounded-register or bounded-memory "first cycle" games: register number is Theta(log n) in the worst case (BARRIERS B1 row and the
  Strahler/register line of its re-verification table): quasi-polynomial, not new.
- Any further method on the discounted reduction: fails the N6/N7 screening rule (HMZ 1008.0530 Thm 6.5; B21) without a gamma-free
  argument.

## 6. Status for the Lead
- N9a: DEAD at levels 1 and 2 (DATA, wrong answers on one-player games of size 4 and 7); k* = 3 at n = 7; unbounded k* is a READING.
- N9b: DEAD as a complete solver (DATA, STUCK at n = 5); sound by construction.
- N9c, N9d: not run (§3, §4). No candidate is live. No running-time claim is made anywhere in this file.

## 7. Sources opened in this box (scratchpad copies; sha256 prefixes)
- arXiv 1405.0945 v1 (ATSP integrality ratios in the Sherali-Adams hierarchy), 4c6956dc2f1db3ee: §1 l.95-119 (level n exact).
- arXiv 1506.04184 (Bodirsky-Mamino), e0e0e34de549a4d8: abstract l.9-16, §1 l.103-104, Thm 5.1.
- C. Fritz, Simulation-based simplification of omega-automata, PhD thesis, Kiel 2006 (macau.uni-kiel.de d1644.pdf),
  fa1253460e9058c3: ch. 3 intro (text l.6152-6175), §3.5 remark (l.8015-8018).
- docs/lit/BARRIERS.md B1-B21; docs/red/R53-n8a-counter.md §1-§3; docs/red/R56-r2-vj-switchsets.md §4 (fleet files).
