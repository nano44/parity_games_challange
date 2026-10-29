# T49: N5 / N5-SF and SBC against the tropical simplex method, the shadow-vertex rule and smoothed analysis
L-LIT successor 4 (Opus 5.5), D18. Lead's brief 2026-10-29 16:31Z (T49 (1)-(4)). Written 2026-10-29 from 16:41Z (date -u). Working note,
unrefereed, not a TARGET.md claim. CONJECTURE SF-POLY stays OPEN. Symbols as in docs/lit/T48-sbc-neighbours.md and P-N5-SF §0.
Labels: PROVED-in-source / PROVED (L-LIT, unrefereed) / READING / CONJECTURE / OPEN / DEAD / DATA / NOT OPENED.
Sources were opened by my subagents (t49/A tropical, t49/B shadow vertex). Key quotes were re-checked by me by grep; the notebook has
sha256 and pages. Page numbers are PDF pages of the arXiv versions unless marked.

## Summary
- (1) Neither N5's step nor F is a simplex pivot rule, tropical or classical.
  - The exact classical dictionary exists: Maat 2509.16075 Thm 3.4. On the LP of a nondegenerate longest-shortest-path game (sink parity
    games, Thm 4.9), feasible bases = Even strategies σ, and negative reduced cost = improving switch.
  - Under it, a pivot is ONE switch. F's steps switch about 8 Even vertices on average on switchbestexp_5 (2993 changes over 364 steps,
    DATA). They are the «great leaps» that ABGJ 1308.0454 p.3 separates from simplex paths.
  - SBC is not a pivot count of any rule. It counts basis steps at which the min-walk part of B^{-1} changes its argmin: a quantity of
    the basis, not a move (READING).
- (2) The transfer theorem says: a classical pivot rule that is combinatorial (1309.5925) or tropically tractable semi-algebraic
  (Benchimol thesis Thm 3.25, 5.3), and polynomial on ALL non-degenerate real LPs, gives a strongly polynomial MPG algorithm
  (1309.5925 Cor. 4.3).
  - Rules that qualify: Bland, least-entered (Zadeh), bounded lookahead, shadow vertex.
  - Undecided: Dantzig, largest improvement (thesis p.54).
  - No qualifying rule is known to be polynomial classically. Shadow vertex has worst-case Θ(n^⌊d/2⌋) 2-D shadows for fixed d
    (Amenta-Ziegler).
- (3) Smoothed analysis transfers to deterministic two-player MPGs and discounted games, via a policy-iteration variant with an evolving
  discount (Loff-Skomra 2402.03975 Thm 1.1; 2610.22149 Thm 1.2; Asadi-Chatterjee-Luo 2610.14150 Thm 13). It does not transfer to
  parity games.
  - Normalised Gaussian noise of size ρ drowns all priorities below the top unless ρ ≲ n^−d, which gives n^O(d) (READING).
  - The tropical shadow-vertex average case needs flip invariance and all-finite payments (1406.5433 Assumption B), which parity
    arenas violate.
- (4) F's run is not a 2-D shadow of the joint-play polytope (T48 SEGRET). DATA: it needs at least PIECES straight one-parameter
  pieces, 2, 4, 9, 16, 24, 29 on switchbestexp N = 1..6, about SBC/2.
  - A d-parameter family would give n^O(d² log n) via Chillara-Gajjar (READING). So SF-QP would follow if F's runs had bounded
    "parametric dimension". That is OPEN, and PIECES does not bound d for d ≥ 2.
- New cross-link (§5): Loff-Skomra p.7 and Ex. 3.5.
  - One-player games: a single free payoff gives ≤ n breakpoints per action (stated, «it can be shown»).
  - Two-player deterministic games: one free edge weight gives 2^Ω(n) breakpoints, and the edge enters and leaves the equilibrium cycle
    exponentially often. The construction is BNRC08 = ABGJ18 Prop. 20.
  - Consequence (READING): parametric amplification cannot beat the count of distinct parameter values. My T48 §1.5 "clock" hint is
    circular and is retracted there.

## 1. (1) Is N5's step or F a (tropical) pivot rule? Can SBC be read as pivots?
- PROVED-in-source, Maat 2509.16075 v2, Thm 3.4 (p.8): «Suppose the LP (3) is derived from a nondegenerate LSP, and let B be some basis
  of the LP. Then … 2. … basis B is feasible if and only if the basic variables consist of z and of xj for all j ∈ σ, for some
  admissible Player 0 strategy σ. 3. H1,e < 0 if and only if e is an improving move for strategy improvement, and the set of optimal
  solutions of the LP consists of a single vertex. It follows that for every possible run of strategy improvement in the LSP, there is
  an equivalent run of the simplex algorithm in the LP (3), and vice versa.»
  - Item 1 gives B^{-1} entries as walk polynomials walks^σ (t).
  - Def. 3.1 (nondegenerate: no zero-weight cycles, distinct weights for internally disjoint paths) is «a more relaxed condition
    compared to the condition of tropical genericity».
  - p.18: «the size of the coefficients of the LP will be doubly exponential».
  - p.18 (OPEN in source): «it is also conceivable that there is a variant of the tropical simplex method for which a similar tropical
    LP can be formulated: where the tropical simplex method would be equivalent to strategy improvement.»
- PROVED-in-source, ABGJ 1308.0454 v2 p.3: tropical simplex «move[s] along edges in the graph of the tropical polytope, whereas policy
  iteration type algorithms often take "great leaps" in the same graph».
- READING (with Maat's dictionary).
  - A simplex pivot changes one basic variable, i.e. one Even switch ("equivalent run" holds for single-switch strategy improvement).
  - N5's S4a and F choose Even's one-player optimum inside the improving arena, a multi-switch step. DATA: on switchbestexp_5,
    EVCHG = 2993 over 364 distinct-σ transitions (T48-sbc-embed-check.py).
  - So neither is a pivot rule on LP (3), classical or tropical. F's run is a path in the graph of strategies with leaps.
  - Whether the distinct-σ sequence is a subsequence of SOME monotone simplex path (each leap refined into single improving switches) is
    OPEN. If it were, for a rule in the transfer class, the transfer theorem would still bound nothing without a polynomial classical
    bound for that rule.
- READING (SBC). Odd's best reply does not appear as basic variables in LP (3). The bases are Even strategies, and Odd's minimisation sits
  inside the walk polynomials of B^{-1} (Thm 3.4 item 1). So a σ̄-change is a change of which min-walk dominates in some entry of
  B^{-1} between consecutive bases.
  - It is a property of the basis sequence, not a pivot. No opened source counts it.
  - In T48 §2's terms it is the opponent-response count that no paper bounds.

## 2. (2) The transfer theorem and which rules qualify
- PROVED-in-source, ABGJ 1309.5925 v2.
  - Thm 2.1 (p.5): MPG winning ⇔ feasibility of x_j̄ ⩾ 0, A⊙x ⩽ B⊙x.
  - Definition p.13: «the strategy φ is combinatorial if at every step k, the leaving index i_k^out is a function only of the history
    (I1, …, Ik) and of the collection of the signs of all the minors of the matrix M».
  - Prop. 4.1 (p.14): N_T(n, m, φtrop) ⩽ N_R(n, m, φ), by Tarski's principle.
  - Thm 4.2 (pp.15-16): «Let φ be a combinatorial pivoting strategy such that … each function φk can be defined in the arithmetic model
    of computation with oracle, … polynomially bounded by n, m and k. Suppose that the classical simplex algorithm equipped with φ is
    strongly polynomial on all non-degenerate linear programs over R. Then all tropical linear programs over the max-plus semiring T(R)
    can be solved by a strongly polynomial algorithm.»
  - Cor. 4.3: «Then mean payoff games can be solved by a strongly polynomial algorithm.»
  - Genericity is removed by a symbolic perturbation over Hahn series (Thm 3.12).
- PROVED-in-source, Benchimol PhD thesis (HAL tel-01198482).
  - Thm 3.25 (p.55): for a semi-algebraic rule and a sign-generic input, the tropical simplex reproduces the classical basis sequence.
  - Thm 5.3 (p.95): «Let φ be a tropically tractable pivoting rule. Suppose that the simplex method, equipped with φ, performs a number
    of iterations which is polynomial in m and n on all non-degenerate linear programs over R … Then any tropical linear program can be
    solved in polynomial time.»
  - p.54: Bland «semi-algebraic … also tropically tractable»; «the "least entered" rule is tropically tractable»; Dantzig: «it is unclear
    whether the polynomial (3.23) is tropically tractable»; largest improvement: «also unclear».
- PROVED-in-source, ABG 1406.5433 v2 Thm 7 (p.10): the tropical shadow-vertex rule is compatible with the classical one on strongly
  non-degenerate inputs, O(n⁴) per pivot. p.2: before it, «the only pivoting rules which have been tropicalized are combinatorial».
- Classical status of the qualifying rules:
  - Shadow vertex: worst case Amenta-Ziegler (abstract, opened): «a 2-dimensional projection of a d-dimensional polytope with n facets
    may have as many as Θ(n^⌊d/2⌋) vertices for fixed d»; Goldfarb's exponential examples NOT OPENED.
  - Least-entered: exponential (Disser-Friedmann-Hopp 1911.01074 Thm 6.18, opened 2026-10-14).
  - Bland: classical exponential example (Avis-Chvátal) NOT OPENED.
- READING (2).
  - The transfer runs one way: a polynomial classical rule ⇒ a polynomial MPG algorithm. It is a reason a parity breakthrough would
    follow from an LP breakthrough, not a tool for N5.
  - For parity inputs the tropical entries are the MPG payoffs (VJ/Puri weights), so bit-cost (TARGET.md §3) must be checked separately.
  - Neither N5 nor F is in the class (§1), so the theorem says nothing about them.

## 3. (3) Smoothed / average-case shadow vertex and transfer to games
- PROVED-in-source (classical LP).
  - Spielman-Teng cs/0111050 Thm 4.0.1 (p.38): E[|Shadow|] ≤ 58,888,678·nd³/min(σ, 1/(3√(d ln n)))⁶ for Gaussian perturbations;
    Thm 5.0.1 (p.59) for the two-phase algorithm.
  - Vershynin cs/0604055 Thm 1.2: O(log⁷ n (d⁹ + d³σ^−4)).
  - Dadush-Huiberts 1711.05667 Thm 13 (p.19).
  - Huiberts-Lee-Zhang 2211.11860 Thm 1.2: O(σ^−3/2 d^13/4 log^5/4 n); Thm 1.3: the first smoothed LOWER bound,
    Ω(min(1/√(dσ√log d), 2^d)). (Bach-Huiberts quote it with log^7/4; cite HLZ directly.)
  - Bach-Huiberts 2504.04197 §1.1: semi-random shadow O(√(σ^−1 √(d^11 log^7 n)) + d³ log² n), with σ^−1/2 optimal up to polylog.
  - Kelner-Spielman STOC'06: weakly polynomial randomized simplex.
  - Adler-Papadimitriou-Rubinstein 1404.3320 Thm 2: «The shadow vertex pivoting rule is tractable».
  - Disser-Skutella 1311.5935 Cor. 4: counting the vertices of a 2-D projection is NP-hard.
- PROVED-in-source (games).
  - Loff-Skomra 2402.03975 Thm 1.1 (p.6): a PI algorithm, time poly(φ·n) w.h.p., for deterministic two-player discounted / mean-payoff
    games with payoffs perturbed by Gaussian noise of s.d. 1/φ (ergodic case).
  - Loff-Skomra 2610.22149 Thm 1.2 (p.5): «given any n-state deterministic two-player (discounted or mean-payoff) game, played on any
    graph, it will run in time poly(n, 1/ρ) with high probability».
  - Asadi-Chatterjee-Luo 2610.14150 Thm 13: restarting PI is smoothed polynomial for discounted games. It counts arithmetic operations;
    a bit-cost check is needed.
  - Christ-Yannakakis 2212.00083 Thm 3 (p.26): Howard's PI needs 2^(∛N/6) iterations under structure-preserving perturbations of size
    1/N, already for one-player stochastic MDPs. Asadi-Chatterjee-Luo p.3: this «rules out such an extension» to stochastic games.
  - ABG 1406.5433 Thm 13 (p.15): tropical shadow vertex is polynomial on average under Assumption B: (i) flip invariance of rows/columns
    of A, B; (ii) A_ij, B_ij almost surely distinct and finite; (iii) W strongly non-degenerate. p.16: «The main restriction of the model
    is the flip invariance property.»
- READING (what blocks a parity transfer).
  - (i) Parity → MPG uses weights about n^p. Normalised to [−1, 1], all priorities below the top shrink to about n^−(d−j). A
    winner-preserving perturbation needs ρ ≲ n^−d, so poly(n, 1/ρ) = n^O(d), no better than known bounds.
  - (ii) Perturbed weights are generic MPG weights; the parity structure is gone. The smoothed theorem is about the perturbed game, and
    the original parity instance is a measure-zero, worst-case point.
  - (iii) ABG's model is complete bipartite (all A_ij finite) and flip-invariant. A fixed sparse parity arena is neither.
  - (iv) None of the opened game papers mentions parity games outside its references (grep). No smoothed result for parity games was found.
  - Combes-Touati 2007.08387 (random d-out graphs, i.i.d. priorities) is a random-instance model, not a smoothed one.

## 4. (4) Is F's run a multi-parameter shadow?
- PROVED-in-source.
  - Chillara-Gajjar(-Raja) 2607.21055 Thm 2 (p.5): |MSPC(G)| ∈ n^O(d log n) for d linear parameters, tight.
  - Gajjar-Radhakrishnan 1811.05115 Thm 3: n^((log n)² + O(log n)) for three parameters.
  - Shadow-vertex generalisations (max-slope rule, pivot-rule polytopes; Black-De Loera-Lütjeharms-Sanyal, abstract only) give no
    polynomial result.
- PROVED (L-LIT, T48 §1.4). On a straight line in any linear parameter space, a strictly optimal x → y path is optimal on one interval.
  So a run with a segment return (SEGRET > 0) is not one-parametric.
- DATA (docs/lit/T48-sbc-embed-check.py, PIECES=1): PIECES = the least number of consecutive windows of the distinct-σ sequence with no
  segment return inside a window (greedy, optimal). It is a lower bound on the straight pieces of any piecewise one-parameter path that
  realises the run.

| instance | #σ | SBC | PIECES |
| --- | --- | --- | --- |
| switchbestexp_1..6 | 21, 59, 136, 259, 365, 413 | 1, 4, 11, 26, 49, 56 | 2, 4, 9, 16, 24, 29 |
| H3 (H3_F.start) | 65 | 8 | 4 |
| friedmannsubexp_3, 4, 5 | 12, 15, 19 | 9, 12, 16 | 2, 2, 2 |
| fearnleysubexp_3, 4, 5 | 10, 13, 16 | 5, 6, 9 | 1, 3, 3 |

  - Cut indices vs σ̄-change indices (PIECES=2), switchbestexp_2: cuts 14, 33, 46; σ̄ changes 10, 29, 33, 42. Cuts follow σ̄-changes
    by 0-4 steps but are fewer (switchbestexp_4: 15 cuts, 26 σ̄-changes).
- READING (4).
  - A 2-D shadow is one straight line in objective space, i.e. one parameter. F's run needs about SBC/2 straight pieces on switchbestexp,
    so it is not a 2-D shadow of the joint-play (path) polytope.
  - A d-dimensional affine weight family in which every joint tree of the run is optimal somewhere would bound the run by the number of
    optimal trees over the family. That is the overlay of n per-vertex subdivisions with n^O(d log n) cells each: n^O(d² log n)
    (READING, crude count).
  - So CONJECTURE SF-QP (SBC ≤ n^O(log n)) would follow from "F's runs have O(1) parametric dimension". That is OPEN.
  - PIECES does not bound d for d ≥ 2: a curve in the plane can leave and re-enter a convex cone.
  - Nothing found in the literature defines or bounds the parametric dimension of a strategy-improvement run. Computing it on an instance
    is at least as hard as counting shadow vertices (NP-hard, Disser-Skutella Cor. 4); deciding it for d = 1 is the SEGRET test.

## 5. A cross-link found on the way: one free payoff, one player vs two players (Loff-Skomra)
- PROVED-in-source / stated, Loff-Skomra 2402.03975 v1.
  - p.7: «In the one-player case it can be shown that for every action there exist at most n break points … for the two-player case
    … this conjecture is wrong. An exponential example (Example 3.5) can be created using the construction of [BNRC08] that was also
    used in [ABGJ18] … the value of the game is a piecewise-linear function with 2Ω(n) break points.»
  - Ex. 3.5 (p.17): 2n states, edge (4, 2) parametrised by x ∈ [0, 2]; «the curve y2n(x) has exponentially many breakpoints … the
    (4, 2) edge alternates an exponential number of times between being included and excluded from the equilibrium cycle.»
  - p.14: in two-player games x ↦ λ(x, r−ij) is «no longer convex or concave».
- READING (for SF-POLY).
  - Odd's problem in N5-SF is one-player (G_σ). If Even's run only moved ONE effective payoff seen by Odd, each Odd action would flip at
    most n times (the one-player statement above; the proof is not given in the source, so this is READING).
  - The leapfrog needs Even's run to move many payoffs at once (T48 §1.3: Carstensen-type, many edges).
  - Any parametric amplification is capped by the number of distinct values its driving parameter takes. In F that parameter is driven
    by the σ-run itself, and SBC ≤ #σ − 1 (SBC-EQ).
  - Hence: (a) the super-polynomial count, if any, must come from the length of the σ-run, not from amplification inside Odd's problem;
    (b) my T48 §1.5 hint (Even clock + Carstensen network) is circular and is RETRACTED (marked in T48).
- READING (for N5 itself, two-sided). N5's τ-side is a two-player interaction. Ex. 3.5 says that in two-player deterministic games even a
  single monotone parameter can toggle an edge in and out of the equilibrium cycle 2^Ω(n) times. That is the two-player analogue of the
  leapfrog, with exponential rather than quasi-polynomial strength. It is a warning for any N5 proof that tracks equilibrium-cycle
  membership along one monotone quantity.

## 6. What this means for SF-POLY / N5
- PROVED-in-source:
  - Strategy improvement ≅ simplex on Maat's LP (single switches; nondegenerate LSPs incl. sink parity; doubly exponential coefficients).
  - The transfer theorem (1309.5925 Thm 4.2 / Cor. 4.3; thesis Thm 5.3) and its rule list.
  - Smoothed polynomial PI for deterministic 2-player MPG / discounted games (2402.03975, 2610.22149, 2610.14150).
  - Tropical shadow vertex polynomial on average under flip invariance (1406.5433 Thm 13).
  - One-parameter two-player value functions with 2^Ω(n) breakpoints (2402.03975 Ex. 3.5).
- PROVED (L-LIT, unrefereed): a run with SEGRET > 0 is not one-parametric (T48 §1.4).
- READING:
  - N5 and F are not pivot rules (multi-switch leaps), so neither the transfer theorem nor the shadow-vertex analyses apply to them.
  - SBC is a basis property, not a pivot count.
  - Smoothed results do not reach parity (noise drowns priorities).
  - Parametric amplification cannot create SBC beyond the σ-run length.
- DATA: PIECES ≈ SBC/2 on switchbestexp; multi-switch rate ≈ 8 per step on switchbestexp_5.
- CONJECTURE / OPEN:
  - SF-QP via bounded parametric dimension of F's runs (OPEN; no tool).
  - Is the distinct-σ sequence a subsequence of a monotone single-switch simplex path in Maat's LP (OPEN)?
  - A tropical LP on which strategy improvement = tropical simplex (OPEN in source, Maat p.18).
  - SF-POLY (OPEN).
- DEAD:
  - The "Even clock + Carstensen network" attack hint (circular; T48 §1.5 retracted).
  - The route "F is a shadow-vertex (2-D) path" (PIECES > 1 from switchbestexp_1).

## DONE / FINDINGS / NEEDS
- DONE: this note; PIECES in docs/lit/T48-sbc-embed-check.py (pushed 4ff31a84); T48 §1.5 retraction; notebook rows.
- FINDINGS:
  1. Maat Thm 3.4 is the exact SI ↔ simplex dictionary. N5 / F are multi-switch leaps, not pivot rules, and SBC is a basis property.
  2. Transfer theorem: a polynomial combinatorial or tropically tractable rule gives poly MPG. The qualifying rules (Bland,
     least-entered, shadow vertex) are not polynomial classically; Dantzig is undecided.
  3. Smoothed polynomial PI exists for 2-player deterministic MPGs (2026), but not for parity: noise drowns the priorities.
  4. F's run needs PIECES ≈ SBC/2 straight pieces, so it is not a 2-D shadow. Bounded parametric dimension would give SF-QP (OPEN).
  5. Loff-Skomra: a one-player single payoff gives ≤ n flips per action; a two-player single parameter gives 2^Ω(n). Parametric
     amplification is circular for SBC; T48's clock hint is retracted.
- NEEDS: none from the owner.
