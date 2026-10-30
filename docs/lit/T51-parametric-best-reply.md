# T51: parametric shortest-path breakpoints, monotone non-linear costs, and counts of the opponent's distinct best replies, for N5's σ̄
L-LIT successor 4 (Opus 5.5), D18, woken from park for this task. Lead's brief 2026-10-30 07:23Z (T51 (1)-(3)). It answers L-NEW 36,
box 75 (l-new 01588402, docs/new/N5-SBAR-box75.md §4). Written 2026-10-30 (date -u). Working note, unrefereed, not a TARGET.md claim.
Labels: PROVED-in-source (what an opened source proves) / PROVED (L-LIT, elementary, unrefereed) / READING (every N5 implication) /
DATA / OPEN / NOT OPENED. Sources are in notes/L-LIT.md "Sources opened" (sha256, pages). Earlier coverage: T48 §1-§3, T49 §5, T50 §2,
T39 rows 13-18. This note collects them for box 75 and adds §2 and the plain-N5 data in §4.

## Summary
- (1) Breakpoint bounds, one affine parameter, one s-t pair.
  - Upper: ≤ (2n+1)^(log n + 1)/2 (Gusfield 1980 Thm 4.5).
  - Lower: n^Ω(log n) (Carstensen 1983 with unbounded bit length; Mulmuley-Shah 2001 with O((log n)³)-bit weights; planar,
    Gajjar-Radhakrishnan Thm 1).
  - Mulmuley-Shah's PRAM statement is a consequence of the breakpoint bound, in the model "unbounded fan-in PRAM without bit operations".
  - Polynomial special cases: 0/1 slopes (≤ n² trees), integer slopes ≤ W (O(n²W)).
- (2) Monotone NON-linear costs.
  - PROVED (L-LIT): with arbitrary monotone edge costs there is NO bound beyond the number of paths. Every sequence of s-t paths (or
    shortest-path trees) is a sequence of strict optima for some monotone non-decreasing cost family.
  - Polynomial costs of degree q: n^O(log n + log q) (Chillara-Gajjar-Raja Thm 5); Gajjar-Radhakrishnan Thm 2.
  - PROVED (L-LIT): lexicographic-affine costs keep the one-interval property, so Gusfield's bound applies.
  - No source found on monotone non-linear one-player parity / mean-payoff families.
- (3) No source bounds the number of distinct best replies of the opponent along an SI run. The known results are all negative (T39
  rows 15-16, T48 §3):
  - Mei 2610.27386: 2^h − 1 changes for a single-switch rule;
  - Friedmann's G_n / H_n and the snare family: τ is a slave of the bit vector, 2^Ω(n);
  - DLM: SSI is exponential for every rule.
  The upper bounds go through an iteration count (HMZ with a discount, Mei-Sun-Ye forward games, Koh-Loho potential height), never
  through a best-reply count.
- READING (transfer to N5's σ̄). A Carstensen-type lower bound does not transfer as a count. The models differ in three exact points
  (§3): an exogenous parameter vs an endogenous run; a fixed graph with moving weights vs fixed weights with a moving edge set; one
  parameter vs a run that is not one-parametric. Carstensen's mechanism (argmin flips over two rising successor values) is the
  leapfrog itself and is compatible with MONO-XI.
- DATA (plain N5, new).
  - box 75's thetaA_n7: σ̄(6) = 5 → 1 → 5 with SEGRET 0, PIECES 1. This leapfrog is CONSISTENT with a one-parameter family.
  - Plain N5 on switchbestexp_1..3 and H3_F is NOT one-parametric (SEGRET 42, 279, 528, 275).

## 1. (1) Parametric shortest paths: the bounds and their exact models (PROVED-in-source)
- Gusfield, PhD thesis, UC Berkeley 1980 (ERL M80/22; scan, pp.83-87 read from page images, T48).
  - Model (p.83): fixed graph G, nodes s, t; edge i costs S(i) + λT(i), λ ∈ ℝ, arbitrary real S, T. P(λ) is the optimal s-t cost,
    «a piecewise linear convex function of λ» (concave for a minimum; the scan's wording). Breakpoints are counted.
  - Thm 4.5 (p.86): «Let G be any arbitrary graph with n nodes and two distinguished nodes s and t. Then for any parametric edge costs, the
    number of breakpoints of P(λ) for G is bounded from above by (2n + 1)^((log n)+1)/2.»
  - Proof (Thm 4.4, pp.84-86): halving at a middle column of the layered unrolling; «each path is minimum for at most one contiguous range
    of λ» (base case).
  - p.87: «the sub-exponential bound holds for any cost function with the property that no path is minimum for more than one contiguous
    range of λ.» (T48 §1.4: the induction needs this for every sub-pair.)
  - Thm 4.1 (p.59): costs S(i) + λT(i) with T(i) ∈ {0, 1}: at most n − 1 s-t breakpoints, n(n − 1)/2 for s-to-all.
- Carstensen 1983 (Math. Prog. 26, DOI 10.1007/BF02591893, and the Michigan PhD thesis): NOT OPENED (Springer login / 429; thesis not
  online). Its content as stated in opened sources:
  - Gajjar-Radhakrishnan 1811.05115 v3 p.2: «Carstensen [Car83a, Car83b] showed that ϕ(n, ∞) = n^Ω(log n)». Here ϕ(n, β) is the maximum
    number of pieces of the s-t cost function over n-vertex graphs with weights of bit length β; ∞ means unbounded bit length.
  - Same page: «Carstensen [Car83b, Page 100] presented a matching upper bound, ϕ(n, ∞) = n^(log n+O(1)), which she attributed to Daniel
    Gusfield».
  - Chakraborty-Fischer-Lachish-Yuster 1001.3749 v2 p.170: «in her example each linear function is of the form a_e + xb_e and both a_e and
    b_e are positive, and x varies in [0,∞]».
- Mulmuley-Shah 2001 (JCSS 63, DOI 10.1006/jcss.2001.1766): NOT OPENED (403 in T48). Pradyut Shah's 2001 Chicago dissertation abstract
  page was found by search but returned TLS failure / 503 (2026-10-30). Content as stated in opened sources:
  - Gajjar-Radhakrishnan p.2: Mulmuley & Shah «showed that ϕ(n, O((log n)³)) = n^Ω(log n)», i.e. Carstensen's bound with polylogarithmic
    bit lengths.
  - Gajjar-Radhakrishnan §1 "Consequences", Claim 4 (their planar analogue): «every unbounded fan-in PRAM algorithm (without bit operations) with at most
    n^α processors requires at least ǫ log n steps to compute the shortest s-t path in G_n». They say [MS01] derived the same for general
    graphs from ϕ(n, O((log n)³)) = n^Ω(log n). (The sentence before Claim 4 writes «PRAMs with bit operations»; their Claim 4 and the literature
    say «without». Read: without.)
  - The model, from Pellissier-Seiller 2002.10888 v2 §III, quoting Mulmuley's 1999 framework: input split into numeric and non-numeric
    data, arithmetic and comparisons on numeric data, and «the pointer involved in an indirect reference is not some numeric argument in the
    input or a quantity that depends on it»; no bit extraction. §VII Def. 35 defines parametric complexity as the number of breakpoints of
    an affine parametrization.
  - So Mulmuley-Shah is a breakpoint LOWER bound (same quantity as Carstensen, smaller bit length) plus a CONSEQUENCE for a restricted
    parallel model. It is not a lower bound on breakpoints "in a model".
- Gajjar-Radhakrishnan 1811.05115 v3: Thm 1, planar graphs, ϕ_pl(n, O((log n)³)) = n^Ω(log n) (refutes Nikolova's polynomial conjecture);
  Thm 2, univariate polynomial weights of degree ≤ d: n^(log n + (α(n)+O(1))) with d in the exponent (the PDF text garbles where d
  sits); Thm 3, three linear parameters: n^((log n)² + O(log n)).
- Chillara-Gajjar-Raja 2607.21055 v1: Thm 2-4, d parameters, n^O(d log n) (DAG / no negative cycles / undirected non-negative); Thm 5,
  univariate polynomial weights of degree q, n^O(log n + log q); matching n^Ω(d log n) (abstract).
- Polynomial special cases:
  - Young-Tarjan-Orlin cs/0205041 §2: slopes in {0, 1}: «at most n² trees», «no vertex acquires a new path more than n − 1 times»;
    p.16: slopes in {−K, …, 0}, Kn² trees.
  - Nishida 2609.29234: integer slopes |b(e)| ≤ W: O(n²W) breakpoints (min cycle mean); per-vertex path changes ≤ 2(n − 1)W.
- What is counted (all of the above): pieces of ONE s-t cost function = minimum number of s-t paths covering all parameter values. For
  trees: ≤ Σ_v (pieces at v) + 1 with one parameter.

## 2. (2) Monotone but non-linear costs
- PROVED (L-LIT, elementary). Let G be a graph, s, t fixed, and P_1, …, P_K ANY sequence of s-t paths (repetitions allowed, P_k ≠ P_{k+1}).
  Then there are edge-cost functions c_e(k) ≥ 0, each non-decreasing in k, such that P_k is the UNIQUE shortest s-t path at time k for
  every k.
  - Proof. Put c_e(0) = 1. At step k raise every edge not on P_k by M_k := 1 + Σ_e c_e(k − 1) (the total cost so far), and leave the
    edges on P_k unchanged. Costs only rise.
  - Every other s-t path Q contains an edge outside P_k (a path is determined by its edge set, so Q ⊄ P_k), so
    cost_k(Q) ≥ M_k > Σ_e c_e(k − 1) ≥ cost_k(P_k).
  - The same construction with "edges outside the tree T_k" realises any sequence of shortest-path trees to a sink: any other path from a
    vertex uses a non-tree edge.
  - So monotonicity of the costs alone gives no bound better than the number of s-t paths (exponential). Distances are monotone too.
- PROVED (L-LIT, elementary). Lexicographic-affine costs keep the one-interval property.
  - Setting: costs c_e(λ) ∈ ℝ^k compared lexicographically, each coordinate affine in λ. For two fixed paths the difference is an affine
    vector function D(λ).
  - Its lexicographic sign is the sign of the first coordinate not identically zero, except at that coordinate's single root. So the sign
    changes at most once, and a path is optimal on one interval.
  - Gusfield's proof uses only this, optimal substructure, and ordered-group arithmetic, so Thm 4.5's bound holds verbatim for
    lexicographic-affine costs. (READING-level care: ties at isolated roots are broken by the next coordinate.)
- PROVED-in-source: polynomial costs of degree q give n^O(log n + log q) (Chillara-Gajjar-Raja Thm 5). Degree ≤ d gives
  Gajjar-Radhakrishnan Thm 2.
- Literature on monotone NON-linear one-player parity / mean-payoff families: none found (T48 §2, T49 §5 searches).
  - The nearest is Loff-Skomra 2402.03975 p.7: in ONE-player deterministic games, a single free payoff gives «at most n break points»
    per action (stated, «it can be shown»; proof not in that passage).
  - In two-player games, Ex. 3.5 (p.17) gives 2^Ω(n) break points for one free edge weight (BNRC08 = ABGJ18 Prop. 20).
- READING (N5).
  - In box 75's reading, Odd's effective costs move monotonically in Ξ's order (MONO-XI) along Even's run. The first PROVED item above
    says that monotonicity alone cannot bound σ̄'s changes. Any bound needs a structural restriction on HOW the costs move: few parameters,
    affine or polynomial dependence, or bounded slopes (YTO, Nishida).
  - N5's costs are not of these forms. The weights (priorities, ±2^rank) are fixed, and Even's run changes the EDGE SET of G_σ.

## 3. (3) Distinct best replies of the opponent along an SI run
- PROVED-in-source, negative (T39 rows 13-18, T48 §3, T50 §3):
  - Mei 2610.27386 (T31): along a single-switch Player-1 rule the best reply «changes at every pivot: 2^h − 1 changes».
  - Friedmann 1106.0778 Lemma 6.1 / thesis Lemma 4.27: τ_σ(e_i) = h_i iff bit i is set (G_n, switch-all). The derived count is
    ≥ 2^(n−2) changes (READING in T48 §3).
  - Friedmann's snare preprint (DAM 2013) Lemmas 14-15: τ is a per-phase function of the bit vector.
  - Fearnley 1003.2976 Prop. 14 (p.8): switching a profitable back edge forces the opponent's best reply onto an escape. FixSnare
    (Prop. 16) makes the best reply use an escape within |W| iterations. No count of best-reply changes is given.
  - van Dijk-Loho-Maat 2309.02223 Thm 1: SSI is exponential for every improvement rule; both players' strategies change exponentially
    often.
  - Schewe-Trivedi-Varghese 1501.06484: no bound.
- PROVED-in-source, positive, but only through an iteration count:
  - HMZ 1008.0530 Thm 6.5 (discounted, constant γ).
  - Mei-Sun-Ye 2606.29568 Thm 1 (forward games; p.10 «each such pivot may change Player 2's optimal response»).
  - Björklund-Vorobyov DAM 2007 §6 (amortised recomputation by value increases, pseudo-polynomial).
  - Koh-Loho 2108.13338 p.3 (n|L(T)|, any rule).
- Searches with no result for a direct count: T48 notebook row (arXiv API queries; extended web search).
- READING (N5). No published theorem counts distinct best replies, so a polynomial σ̄-count for N5 would be new. Every published
  exponential best-reply count is driven by the improver's rule reclosing cycles. For plain N5, T34 / GATE-SHUT already records that the
  Friedmann flips do not occur for N5's τ (T39 row 16).

## 4. Could a Carstensen-type lower bound transfer to σ̄'s change count in N5? (READING throughout)
- The mechanism transfers; the count does not. Carstensen's instances have, at an internal vertex u, two successors whose distances rise
  monotonically in λ while u's argmin flips (after the potential shift of T48 §1.3, all distances non-decreasing). That is box 75's
  leapfrog: σ̄(q) revisits a value as two options' Ξ values both rise (MONO-XI).
- Exact differences in the models:
  1. Exogenous vs endogenous. Carstensen's λ is free; every value of λ is available. N5's "parameter" is Even's strategy along N5's own
     run, so σ̄ changes at most once per σ-change (SBC ≤ #σ − 1 for N5-SF; for plain N5 likewise per iteration). A super-polynomial
     σ̄-count therefore requires a super-polynomial σ-run first. Carstensen's network can only convert run length into σ̄-changes at rate
     ≤ 1 (T49 §5; T48 §1.5 retraction).
  2. Moving weights vs moving edge set. Carstensen: fixed graph, costs affine in λ. N5: fixed priority weights (±2^rank in Ξ's P
     component), and Even's switches change which edges of G_σ exist. Turning edge-set changes into affine costs forces each Even edge's
     availability to be a threshold in λ (T48 §1.4 E1). That is DEAD on data: Even vertices return to left edges (EVRET > 0).
  3. One parameter vs not one-parametric. The soft embedding (joint plays optimal for c + λd) needs every sub-pair x → y optimal on one
     λ-interval, so Gusfield's upper bound would then apply too. Data (§5): N5-SF and plain N5 violate it on switchbestexp_1..3 and H3_F
     (SEGRET > 0), so neither the upper nor the lower parametric bound is about N5's actual runs.
- What does carry over (READING).
  - Lower-bound side: a family on which N5's own run is long AND feeds a Carstensen-type Odd network would make σ̄ change once per run
    step there; it gives nothing beyond the run length.
  - Upper-bound side: the "monotone values + argmin" template has a floor of n^Ω(log n) even in the most favourable one-parameter case
    (T48 §1.3). With general monotone costs it has no bound at all (§2). So box 75's DEAD list (strictly monotone potentials of σ̄ alone)
    agrees with the literature. The monotone object must be the pair (σ, σ̄) via Ξ, as box 75 concludes.

## 5. DATA (new for plain N5; docs/lit/T48-sbc-embed-check.py, PLAIN=1)
| instance (S3 start unless noted) | runner | #σ | SBC | ODRET | SEGRET | PIECES |
| --- | --- | --- | --- | --- | --- | --- |
| thetaA_n7 (+ .start; box 75) | plain N5 | 4 | 2 | 1 | 0 | 1 |
| thetaA_n7 (+ .start) | N5-SF | 4 | 2 | 1 | 0 | 1 |
| switchbestexp_1 | plain N5 | 21 | 1 | 0 | 42 | 2 |
| switchbestexp_2 | plain N5 | 33 | 4 | 2 | 279 | 3 |
| switchbestexp_3 | plain N5 | 42 | 4 | 4 | 528 | 3 |
| H3 (H3_F.start) | plain N5 | 35 | 5 | 4 | 275 | 3 |
| switchallexp_4 | plain N5 | 9 | 3 | 2 | 0 | 1 |
- ODRET = σ̄ returns to a successor it left (summed); SEGRET / PIECES as in T48 §1.4 / T49 §4; PLAYRET = 0 on every row.
- READING. The box-75 witness thetaA_n7 shows a σ̄ revisit inside one phase that IS consistent with a one-parameter linear family (no
  sub-path return). So that instance does not separate N5 from parametric shortest paths. Larger runs do separate them.

## DONE / FINDINGS / NEEDS
- DONE: this note; PLAIN mode in docs/lit/T48-sbc-embed-check.py; notebook rows (Pellissier-Seiller 2002.10888; Shah dissertation page
  NOT OPENED).
- FINDINGS:
  1. Parametric breakpoints: Gusfield ≤ (2n+1)^(log n+1)/2 (any affine one-parameter family, per s-t pair). Carstensen n^Ω(log n)
     (unbounded bits, positive coefficients). Mulmuley-Shah: the same with O((log n)³) bits, giving an ǫ log n lower bound on unbounded
     fan-in PRAMs without bit operations with n^α processors. Polynomial cases: 0/1 or bounded integer slopes.
  2. PROVED (elementary): monotone non-linear costs alone allow ANY sequence of optimal paths or trees. Lexicographic-affine costs keep
     Gusfield's bound; degree-q polynomials give n^O(log n + log q).
  3. No source counts distinct opponent best replies along an SI run. All published counts are exponential lower bounds driven by the
     improver's rule. Upper bounds only come via iteration counts.
  4. READING: Carstensen's mechanism is the leapfrog, but the count does not transfer (endogenous run, moving edge set, not
     one-parametric). DATA: thetaA_n7 is one-parameter-consistent; plain N5 on switchbestexp_1..3 / H3_F is not.
- NEEDS: none from the owner. Mulmuley-Shah, Carstensen and Gusfield JACM originals stay NOT OPENED (owner-optional).
