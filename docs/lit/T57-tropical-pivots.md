# T57: tropical simplex (ABGJ), the tropical central path, and Loho's abstract tropical LP, against N5's S4a step and S1's tie-break inside W-constant intervals
L-LIT successor T54-T57 (Opus 5.5), D18. Lead's brief 2026-10-30 16:10Z (T57, tropical geometry × SI; the "Maat tropical-SI direction"
lead of T49 / T50). Written 2026-10-30 16:11Z-16:40Z (date -u). Working note, unrefereed, not a TARGET.md claim. G-N5-TIME stays OPEN.
Labels as in T54. Builds on docs/lit/T49-tropical-simplex.md (same papers, opened then in an earlier container; re-opened here, so the
sha256 values below are this session's).

## Summary
- A tropical pivot is ONE leaving/entering pair: the valuation image of ONE classical pivot on a lift (ABGJ 1308.0454 Thm 1, Algorithm 1;
  ABG 1406.5433 p. 5). No opened paper identifies tropical bases with positional strategies, or a tropical pivot rule with a strategy-
  improvement rule. ABGJ 1308.0454 p. 3 explicitly CONTRASTS the two: policy iteration takes «"great leaps"» in the tropical polytope's
  graph.
- N5 is not a tropicalised pivot rule, at either level:
  - S4a (one W-run step) is an arena OPTIMUM: it switches a set of vertices at once, i.e. a "great leap".
  - S1's tie-break inside a W-constant interval also switches sets. Instance u23sw64_n32 (best-reward start): the 8 W-flat transitions
    switch 15, 6, 2, 14, 12, 10, 4 and 1 Even vertices, against 32-48 offered improving edges. The W-changing step 0 switches 17.
  - So no pivot-count bound transfers in either direction. 1309.5925 Thm 4.2 / Cor 4.3 transfer UPPER bounds from a classical rule that
    is strongly polynomial on all LPs to MPGs; Prop. 4.1 sends tropical lower bounds to classical ones. Neither applies to a non-pivot
    method.
- What does connect (READING). ABGJ make arbitrary MPG instances non-degenerate by a SYMBOLIC LEXICOGRAPHIC PERTURBATION (Hahn series
  ℝ[[t^G]], layers T(ℝ² × ℝ^(n+1)), 1309.5925 Prop. 3.6, Lemma 3.7). S1's static index tie-break inside G_I is a tie-break of the same
  lexicographic kind (T54 LEX-BFS, T55). On a perturbed non-degenerate program there are no degenerate pivots (1308.0454 p. 36: edges
  «have a positive length»). So W-flat steps are what remains of degeneracy once the perturbation is fixed by an index order instead of
  by generic E. The tropical papers give no bound on the perturbation layer itself.
- (b) The log-barrier lower bound (1708.01544 Thm A/B, 25, 30, Cor. 31) has no game reading at all («game» does not occur). It says
  nothing about one-player stretches.
- (c) Loho's abstract tropical LP (1612.01890): exponential (Thm 63, Cor. 67) or pseudo-polynomial (Thm 79) bounds. A feasible point
  gives a non-losing strategy (Thm 13, Ex. 14). Open (p. 53): long integer vectors ↔ hard instances «related to … parity games». No pivot
  rule with a polynomial bound; no SI correspondence.

## 1. (a) ABGJ tropical simplex
### 1.1 Allamigeon-Benchimol-Gaubert-Joswig, "Tropicalizing the simplex algorithm", SIAM J. Discrete Math. 29 (2015), arXiv 1308.0454v2: OPENED (sha256 6e7f8188…, pp. 1-4, 18-19, 31, 36-37)
- Theorem 1 (p. 2): «the algorithm traces the image by the valuation map of the path followed by the classical simplex algorithm applied to
  any lift … with a compatible pivoting rule» (compatible = the two rules select the same variables).
- Algorithm 1 (p. 3): «choose i_out ∈ I such that y_iout is tropically negative; K ← I \ {i_out}; pivot along the tropical edge E_K to …
  I′ = K ∪ {i_ent}». One tropical edge «consists of up to n ordinary segments». One pivot costs O(n(m + n)) (Theorem 36, p. 31).
- Prop.-Def. 19 (p. 18): «The tropical basic points of P(A, b) are exactly the valuations of the basic points of P(A, b) for any lift».
- p. 3: «A policy iteration algorithm based on a parametric mean payoff game is given there [GKS12]. These policies seem to have
  interesting connections with basic points. However, our present approach leads to a fundamentally different method: we move along
  edges in the graph of the tropical polytope, whereas policy iteration type algorithms often take "great leaps" in the same graph».
- Degeneracy: standard programs only (primal and dual non-degenerate, finite; Assumptions D-F). Proof of Thm 1 (p. 36): «the edges of the
  Puiseux polyhedron have a positive length». p. 37: criss-cross «should also tropicalize» (CONJECTURED).
### 1.2 ABGJ, "Combinatorial simplex algorithms can solve mean payoff games", SIAM J. Optim. 24 (2014), arXiv 1309.5925v2: OPENED (sha256 6ef1312e…, pp. 1-16)
- Theorem 2.1 (p. 5, citing AGG12 Thm 3.2): «The initial state j̄ is winning for Player Max … iff there exists a solution x ∈ T(ℝ)^n to
  … x_j̄ ⩾ 0, A⊙x ⩽ B⊙x». Rows are Max states, columns Min states.
- Tropical basic point (p. 7): «the unique point x ∈ P(A, b) activating a subset I ⊂ [m] of n inequalities … The set I is referred to as
  a tropical basis.» A basis is a set of n active inequalities, NOT a strategy.
- Combinatorial rule (p. 13): the leaving index «is a function only of the history (I1, …, Ik) and of the collection of the signs of all
  the minors of the matrix M». «Bland's rule, as well as certain lookahead rules … are combinatorial.»
- Prop. 4.1 (p. 14): N_T(n, m, φ^trop) ⩽ N_R(n, m, φ) (Tarski transfer).
- Theorem 4.2 (pp. 15-16): «Suppose that the classical simplex algorithm equipped with φ is strongly polynomial on all non-degenerate
  linear programs over ℝ. Then all tropical linear programs over the max-plus semiring T(ℝ) can be solved by a strongly polynomial
  algorithm.» Cor. 4.3: «… mean payoff games can be solved by a strongly polynomial algorithm.»
- Arbitrary (degenerate) inputs: symbolic perturbation. 0_T entries become infinitesimal layers in T(ℝ²) with lexicographic order
  (Prop. 3.6, p. 9). Ties are broken in T(ℝ² × H), H = ℝ^(n+1), by E with entries iδ_j, and Lemma 3.7 (p. 10): «E is sufficiently
  generic». Theorem 3.12 (p. 12) solves an arbitrary tropical LP. Degenerate pivots and stalling on the unperturbed program are not
  discussed.
### 1.3 Allamigeon-Benchimol-Gaubert, "The tropical shadow-vertex algorithm solves mean payoff games in polynomial time on average", ICALP 2014, arXiv 1406.5433v2: OPENED (sha256 7deeec2e…, pp. 1-6, 10, 13-16)
- p. 2: «So far [ABGJ14], the only pivoting rules which have been tropicalized are combinatorial». Shadow vertex is «semi-algebraic».
  Theorem 7 (p. 10): compatible under strong non-degeneracy.
- Theorem 13 (p. 15): «Under a distribution satisfying Assumption B, TropPCBC determines in polynomial time on average whether an initial
  state is winning for Player Max». Assumption B: flip invariance, A_ij ≠ B_ij both finite, strong non-degeneracy a.s. No worst-case or
  strongly polynomial claim. Parity arenas violate B (T49 §3).
- Not treated in 1308.0454 / 1309.5925 / 1406.5433: Dantzig, steepest edge, largest improvement, least-entered. "Tropically tractable" is
  a later ABGJ notion (SECONDARY; T49 cites Benchimol's thesis).

## 2. (b) ABGJ, "Log-barrier interior point methods are not strongly polynomial", SIAM J. Appl. Algebra Geom. 2 (2018), arXiv 1708.01544v2: OPENED (sha256 9608058c…, pp. 1-4, 15, 22, 26-27)
- Theorem 15 (p. 15): the tropical central path is val(C(µ)) = «barycenter of {z ∈ val(F) : tgap(z) ⩽ val(µ)}».
- Theorem 25 / A (p. 22): the total curvature of the central path of LW_r(t) (2r variables, 3r + 1 constraints) exceeds (2^(r−2) − 1)π/2 − ε.
  Theorem 30 (p. 27): polygonal curves in N_θ need ≥ 2^(r−1) segments. Corollary 31 / B: ≥ 2^(r−1) iterations.
- The family lifts a variant of the Bezem-Nieuwenhuis-Rodríguez-Carbonell instance (p. 3). The word «game» does not occur. Nothing on
  one-player stretches or on SI.

## 3. (c) Loho and coauthors
- Loho, "Abstract tropical linear programming", arXiv 1612.01890v2: OPENED (sha256 1696fd59…, pp. 1-4, 10-11, 39-41, 47-49, 53-54).
  - Signed tropical matroids replace basic points by basic covectors. Theorem 63: Algorithm 4 takes < C(n, |D|) iterations. Cor. 67: ≤ Σ_k
    C(n, k) oracle calls (exponential). Theorem 79 (p. 49): h ≤ 4dω in the realizable case, ω the largest integer entry («Algorithm 6 is
    pseudopolynomial», p. 48).
  - Theorem 13 (p. 10): «The set of non-losing states in V0 for player 1 equals the set of those i ∈ [d] for which there is a feasible
    point x for (A, Σ) with x_i ≠ ∞»; Ex. 14 (p. 11): «The non-losing strategy is obtained from the positive edges of the feasible point».
  - Open (p. 53): «Upper bounds that are polynomial in n and d would imply a polynomial runtime of Algorithm 6. Particularly long integer
    vectors would correspond to hard instances … related to … parity games». p. 54: comparison with the tropical simplex is open.
- Loho-Végh, "Signed tropical convexity", ITCS 2020, arXiv 1906.06686v2: OPENED (pp. 1-2, grep). Farkas lemma, Fourier-Motzkin,
  Minkowski-Weyl over signed tropical numbers. MPGs appear as motivation only; no algorithm.
- Koh-Loho, "Strategy iteration with universal trees", arXiv 2108.13338 (LMCS 2025): OPENED (pp. 3, 35). Appendix A restates the parity →
  tropical inequality reduction (Thm A.1, citing AGG12). No pivot correspondence. (T50 used this paper for KL-SF.)
- NOT OPENED: a separate Allamigeon-Gaubert-Loho tropical-LP paper (none listed under Loho on arXiv).

## 4. N5 against these sources, exactly
- S4a in a W-run: σ_{t+1} := Even's optimum against τ in the arena H_t = σ_t ∪ Iσ_t. That is a one-player optimisation, i.e. a full
  solve of a tropical LP restricted to H_t, not a pivot. It is the [GKS12]-type «great leap» of 1308.0454 p. 3.
  - Instance u23sw64_n32 (experiments/red/xing/instances/u23sw64_n32.pg, best-reward start). Even switches per transition: 17 (state 0 →
    1, W changes), then 15, 6, 2, 14, 12, 10, 4, 1 on the W-flat transitions 1-8, then 15 (fallback), 10, 3, 6, 7, 9, 1. Offered
    improving edges per state: 63, 41, 39, 32, 39, 48, 43, 38, 36, ….
  - A tropical (or Maat-classical, T49 §1) pivot changes one basis element. N5's step changes up to 17.
- S1's tie-break inside I: also a set switch (15, 6, 2, … above). Within I it is the plain-BFS first-in tree of the tight arena (T54
  LEX-BFS, T55 §3), a lexicographic tie-break among W-tight edges. READING: this plays the role of ABGJ's symbolic perturbation E
  (1309.5925 Lemma 3.7). ABGJ need generic E, while S1 uses a fixed index order. Neither supplies a bound on how often the second
  (perturbation) layer moves while the first (W) layer is fixed. That is exactly [P-INT].
- Could N5 be a pivot rule on a different LP? Only if each N5 transition were a single basis exchange. The counts above (up to 17
  vertices, often > 1 at W-flat steps) exclude that for any LP whose bases are Even strategies (Maat's dictionary). For ABGJ's MPG
  feasibility LP the question is moot: its bases are not strategies.

## 5. Table (the brief's (a)-(d))
| source (opened) | (a) statement | (b) hypothesis | (c) is N5's S4a / S1 a tropicalisation of it? | (d) bound transfer |
| --- | --- | --- | --- | --- |
| ABGJ 1308.0454 Thm 1, Alg. 1, p. 3 | tropical pivot = valuation of one classical pivot on a lift | non-degenerate standard LP; compatible rule | no: N5 switches sets («great leaps»), u23sw64_n32 17, 15, 6, … | none |
| ABGJ 1309.5925 Thm 4.2, Cor. 4.3 | classical strongly polynomial rule ⇒ strongly polynomial MPG | combinatorial rule, poly on ALL real LPs | no (not a pivot rule; bases ≠ strategies) | classical → tropical upper bounds only; no qualifying rule known |
| ABGJ 1309.5925 Prop. 4.1 | N_T ≤ N_R | same | no | tropical → classical lower bounds; not applicable |
| ABGJ 1309.5925 Prop. 3.6, Lemma 3.7 | symbolic lexicographic perturbation removes degeneracy | generic E | S1 is an index-order lexicographic tie-break (READING) | none on the perturbation layer ([P-INT] open) |
| ABG 1406.5433 Thm 7, 13 | tropical shadow vertex; poly on average | strong non-degeneracy; flip invariance (Assumption B) | no; parity violates B (T49) | none |
| ABGJ 1708.01544 Thm 15, 25, 30, Cor. 31 | tropical central path; 2^(r−1) IPM iterations | log-barrier IPMs in a wide neighbourhood | no game content | none |
| Loho 1612.01890 Thm 13, 63, 79 | abstract tropical LP: feasible point → non-losing strategy; exponential / pseudo-polynomial | signed tropical matroids | no | none (open problem p. 53 names parity games) |
| Loho-Végh 1906.06686; Koh-Loho 2108.13338 App. A | signed tropical convexity; parity → tropical inequalities | — | no | none |

## DONE / FINDINGS / NEEDS
- DONE: this note; notes/L-LIT.md (sources).
- FINDINGS:
  1. A tropical pivot is one basis exchange, the image of one classical pivot (1308.0454 Thm 1). No opened paper identifies tropical
     bases with strategies or tropical rules with SI rules. 1308.0454 p. 3 contrasts them («great leaps»).
  2. N5 is not a tropicalised pivot rule. S4a and S1 both switch sets (u23sw64_n32: 17 at a W-changing step; 15, 6, 2, 14, 12, 10, 4, 1
     at the W-flat steps). No pivot-count bound transfers in either direction: 1309.5925 Thm 4.2 goes classical → tropical and needs a
     rule polynomial on all LPs; Prop. 4.1 sends lower bounds the other way.
  3. READING: S1's index tie-break is the analogue of ABGJ's symbolic lexicographic perturbation (1309.5925 Prop. 3.6, Lemma 3.7). The
     tropical papers bound nothing on the perturbation layer, which is where [P-INT] lives.
  4. The log-barrier paper and Loho's abstract framework give nothing for one-player stretches. Loho p. 53 states that hard instances of
     his pseudo-polynomial method relate to parity games (OPEN).
- NEEDS: none from the owner.
