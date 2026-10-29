# T48: SBC (Odd's best-reply changes along N5-SF) in the light of parametric shortest paths, deterministic MDPs and the SI lower bounds
L-LIT successor 4 (Opus 5.5), D18. Lead's brief 2026-10-29 16:02Z (T48 (a)-(c)). Written 2026-10-29 from 16:17Z (date -u). Working note,
unrefereed, not a TARGET.md claim. CONJECTURE SF-POLY (docs/new/P-N5-SF-box55.md §5) stays OPEN.
Symbols as in P-N5-SF §0 (frozen, sha1 dbc2345f): F, σ^(j), σ̄(σ), Ξσ, G_σ̄, SBC, LAM, stretch; MONO-XI, NO-TRANSFER, leapfrog as in
docs/new/N5-SBC-box55.md. Labels: SOURCE (opened; notebook "Sources opened", sha256 there) / PROVED-in-source / PROVED (L-LIT,
unrefereed) / READING / CONJECTURE / OPEN / DATA / DEAD / NOT OPENED.
Tool: docs/lit/T48-sbc-embed-check.py (read-only on experiments/new/box54/n5sf.py, sha1 1ea3bdc7, and box21/n5x.py; S3 start unless a
start file is given). Snare instances: python3 -I docs/lit/T47-gen-pgsolver-snare.py friedmannsubexp|fearnleysubexp N (sha1s = T47 pins).

## Summary
- (a) The parametric-shortest-path bounds (n^(log n + O(1)) upper, n^Ω(log n) lower) are about ONE s-t pair under costs c + λd. L-NEW's
  P-leapfrog is exactly the mechanism behind the lower bound (READING, §1.3): monotone values plus a Bellman argmin over a fixed successor
  set permit n^Ω(log n) argmin changes. So no SF-POLY proof can use only MONO-XI + argmin structure.
- (a) The run of F does NOT embed in a one-parameter linear family (DEAD, §1.4, with instances). Gusfield's upper-bound proof needs every
  sub-pair x → y to be optimal on one contiguous range. Along F's run, play segments x → y return after being replaced (SEGRET > 0) on
  switchbestexp N = 1..5, H3_F, switchallexp 6, friedmannsubexp 2..5 and fearnleysubexp 4..5. The obstruction is exactly that: a
  sub-path is optimal, left, and optimal again. The smallest witness is switchbestexp_1, pair (15, 5): Even vertex 16 goes 5 → 14 → 5.
  So the quasi-polynomial route "SBC ≤ n^O(log n) via Gusfield" is closed for F as it stands.
- (b) No opened source bounds how often the OPPONENT's optimal response changes while the other player improves. Every two-player
  analysis counts outer iterations and treats the best response as a black box (HMZ Thm 6.5), or multiplies outer by fresh inner cost
  (Mei-Sun-Ye 2026, who name the obstacle, p.10). Björklund-Vorobyov 2007 §6 amortise the opponent's recomputation by counting value
  increases, which is pseudo-polynomial. The one-player results (Post-Ye; YTO; Asadi-Chatterjee-de Raaij; Fearnley ICALP 2010) bound or
  lower-bound the inner loop. For F that inner loop is already polynomial in the fleet (R17).
- (c) In Friedmann's G_n (switch-all), H_n (switch-best, sketched) and the snare-memorization family (DAM 2013, author preprint now
  OPENED), Odd's best reply is a function of the bit vector, so it changes ≥ once per increment, 2^Ω(n) times (READING; derived from
  the τ lemmas, no source states the count). The driver is Even's rule reclosing the same cycles; the arena only hides the escape value
  (Friedmann thesis p.104; snare preprint Thm 11). DATA: none of the three counters transfers to F at the sizes run (§3).

## 1. (a) Parametric shortest paths
### 1.1 What the sources prove (PROVED-in-source)
- Gusfield, PhD thesis, UC Berkeley 1980 (ERL M80/22; scan, read from page images).
  - Thm 4.5 (printed p.86): for any graph with n nodes, s, t and edge costs S(i) + λT(i), the number of breakpoints of P(λ) (the optimal
    s-t cost) is at most (2n + 1)^((log n)+1) / 2 (log base 2).
  - Proof (pp.84-87): Thm 4.4 on the layered graph G_{n×c}, by halving at a middle node A. «the shortest path from s to t consists of the
    shortest path from s to A, followed by the shortest path from A to t. As λ changes, the shortest path from s to A changes independently
    of the shortest path from A to t». The base case uses «each path is minimum for at most one contiguous range of λ». A general graph is
    unrolled into G_{n×n} (zero-cost arcs between copies, Bellman-Ford).
  - p.87: «the sub-exponential bound holds for any cost function with the property that no path is minimum for more than one contiguous
    range of λ.»
  - Thm 4.1 (printed p.59): with T(i) ∈ {0, 1}, at most n − 1 breakpoints for one s-t pair, and n(n − 1)/2 for the s-to-all problem.
- Gajjar-Radhakrishnan, arXiv 1811.05115 v3 (FOCS 2019).
  - Thm 1 (p.2): ϕ_pl(n, O((log n)³)) = n^Ω(log n) for planar graphs.
  - p.2 (prior work, secondary): «Carstensen [Car83a, Car83b] showed that ϕ(n,∞) = n^Ω(log n); her result was simplified and extended by
    Mulmuley & Shah [MS01], who showed that ϕ(n, O((log n)³)) = n^Ω(log n).» Also: Carstensen gave the matching upper bound
    n^(log n + O(1)), attributing it to Gusfield.
  - Thm 3: three linear parameters give n^((log n)² + O(log n)).
- Chakraborty-Fischer-Lachish-Yuster, arXiv 1001.3749 v2 (STACS 2010), pp.170-171 (secondary on Carstensen): «in her example each
  linear function is of the form a_e + xb_e and both a_e and b_e are positive, and x varies in [0,∞]». So the lower bound holds with all
  edge costs increasing in the parameter.
- Nikolova-Kelner-Brand-Mitzenmacher, ESA 2006 (author PDF).
  - Lemma 1: breakpoints correspond one-to-one to the extreme points of the 2-D shadow (dominant) of the path polytope.
  - Cor. 1: n^Θ(log n) extreme points in the worst case.
- Young-Tarjan-Orlin, arXiv cs/0205041 (Networks 1991). With slopes in {0, 1} (δ_{E′}), the algorithm «produces at most n² trees» and
  «no vertex acquires a new path more than n − 1 times». With slopes in {−K, …, 0}: at most Kn² trees.
- Nishida, arXiv 2609.29234: with integer slopes |b(e)| ≤ W, the parametric minimum cycle mean has O(n²W) breakpoints, and each
  vertex's path changes at most 2(n − 1)W times.
- Chillara-Gajjar, arXiv 2607.21055: |MSPC(G)| ∈ n^O(d log n) for d parameters, with a matching n^Ω(d log n).
- Disser-Skutella, arXiv 1311.5935 v2, Cor. 3-4: counting the vertices of a 2-D projection, or the basic solutions of a parametric
  min-cost flow, is NP-hard.
- NOT OPENED: Carstensen 1983 (Math. Prog. 26, DOI 10.1007/BF02591893, Springer login and 429; Michigan thesis not online); Gusfield JACM
  1983 (ACM 403); Mulmuley-Shah JCSS 2001 (403, author page TLS fail / 503); Karp-Orlin DAM 1981 (403); Kelner-Nikolova FOCS 2007 (TLS
  fail / 503); Nikolova thesis 2009 (429); Erickson SODA 2010 (404). Their content is used here only as stated in the opened sources
  above. Mulmuley-Shah's restricted model (PRAM without bit operations) is therefore not described here from the source.

### 1.2 Odd's best reply as a one-player optimum (READING)
- In G_σ, Odd has the only choices. σ̄(σ) minimises the VJ00 valuation: cycle-node reward first, then the P set (Σ ±2^rank over the
  vertices above the cycle node), then length (SPEC S1).
- Once the cycle node is fixed (a stretch with LAM constant), the P and length components are additive along the path to the cycle node.
  So σ̄ restricted there is a shortest-path tree with fixed weights ±2^rank (+ ε·length) on the graph G_σ.
- The parameter that moves along F's run is σ, i.e. the EDGE SET at Even vertices, not the weights.

### 1.3 The leapfrog is the parametric-shortest-path phenomenon (READING; a proof-template barrier)
- PROVED (L-LIT, elementary). Let a DAG with sink t have costs a_e + λ b_e. Put φ(v) := min over v-t paths of Σ b_e (so φ(t) = 0) and
  b′_e := b_e + φ(head) − φ(tail) ≥ 0. Every v-t path's slope is shifted by the same −φ(v). So each vertex's argmin and breakpoints are
  unchanged, and all distances D′_v(λ) are non-decreasing in λ.
- Hence parametric shortest paths satisfy both:
  - the analogue of MONO-XI (every vertex value monotone along the parameter);
  - the analogue of σ̄ (each choice is a Bellman argmin over a FIXED successor set).
  The s-t path still changes n^Ω(log n) times (Carstensen as stated in 1811.05115 p.2; with a_e, b_e > 0 directly, 1001.3749 p.170).
- At a vertex u with successors a, b, the two curves λ ↦ w_ua + D_a(λ) and w_ub + D_b(λ) are concave and non-decreasing. They can cross
  many times. Each crossing is one flip of u's argmin. This is L-NEW's leapfrog (N5-SBC-box55 §3) word for word.
- READING (barrier). Any argument that uses only (i) pointwise-monotone values and (ii) σ̄ = per-vertex argmin of successor values
  cannot bound SBC below n^Ω(log n). This holds even if the run were one-parametric. SF-POLY needs a property of F beyond MONO-XI +
  Bellman, e.g.:
  - F's switch-best structure;
  - the ±2^rank form of P;
  - or the fact that the parameter is a strategy driven by improving switches.
  This complements L-NEW's (M1)-(M4): those are exponential-scale kills on data; this is the quasi-polynomial floor even under the
  most favourable one-parameter structure.

### 1.4 Can the σ̄-changes of a run of F be embedded in a parametric family? (DEAD, with instances)
- Embedding E1 (faithful: weights simulate the edge set of G_σ).
  - In a family c + λd, an Even edge's availability (cost below a threshold) is a half-line in λ.
  - If exactly one edge per Even vertex is available at every λ, each Even vertex changes at most once.
  - With a local lower envelope (Even takes its cheapest edge), each Even vertex changes at most deg − 1 times and never returns to an
    edge it left. That gives #σ ≤ 1 + Σ_Even (deg − 1) ≤ m.
  - DATA: Even vertices change up to 95 times at out-degree 4, with EVRET = 5340 returns on switchbestexp_8 (n 210, m 490, #σ 490).
  - DEAD.
- Embedding E2 (soft: the joint play pair (σ^(j), σ̄^(j)) is the optimal tree of a one-player min problem with costs c + λ_j d on G,
  λ_1 < λ_2 < …; generic, so optima are strict).
  - Necessary for every pair (x, y): an x → y path that is optimal at λ_j and λ_l is optimal on all of [λ_j, λ_l], since its cost is
    affine. Gusfield's induction uses exactly this for the sub-pairs (s, A), (A, t).
  - A segment of x's play up to its first visit of y is an optimal x → y path (subpath optimality of a shortest-path tree; in the lasso
    case, READING: we take plays as paths to their cycle node).
  - SEGRET counts (x, y) segments that are used, replaced by a different segment, then used again.
  - The whole play from a vertex never returns (PLAYRET = 0 on every run). This follows from MONO-XI except on Ξ-plateaus.
  - But segments do return:

| instance (S3 start unless noted) | n | m | #σ | SBC | EVRET | PLAYRET | SEGRET | pairs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| switchbestexp_1 | 35 | 70 | 21 | 1 | 23 | 0 | 42 | 19 |
| switchbestexp_2 | 60 | 130 | 59 | 4 | 191 | 0 | 1286 | 351 |
| switchbestexp_3 | 85 | 190 | 136 | 11 | 677 | 0 | 9147 | 1105 |
| switchbestexp_4 | 110 | 250 | 259 | 26 | 1645 | 0 | 35051 | 2243 |
| switchbestexp_5 | 135 | 310 | 365 | 49 | 2824 | 0 | 76185 | 3754 |
| H3 (H3_F.start) | 63 | 149 | 65 | 8 | 215 | 0 | 2243 | 556 |
| switchallexp_1..5 | 21-77 | 41-177 | 6-11 | 1-4 | 4-12 | 0 | 0 | 0 |
| switchallexp_6 | 91 | 211 | 13 | 5 | 14 | 0 | 20 | 20 |
| friedmannsubexp_1 / 2 / 3 / 4 / 5 | 20 / 44 / 77 / 119 / 170 | 41 / 101 / 186 / 296 / 431 | 5 / 9 / 12 / 15 / 19 | 1 / 5 / 9 / 12 / 16 | 0 / 2 / 4 / 6 / 8 | 0 | 0 / 2 / 4 / 6 / 8 | 0 / 2 / 4 / 6 / 8 |
| fearnleysubexp_1 / 2 / 3 / 4 / 5 | 20 / 38 / 59 / 83 / 110 | 41 / 89 / 150 / 224 / 311 | 5 / 7 / 10 / 13 / 16 | 1 / 3 / 5 / 6 / 9 | 0 / 0 / 0 / 7 / 8 | 0 | 0 / 0 / 0 / 14 / 10 | 0 / 0 / 0 / 13 / 7 |

  (switchbestexp N = 6 / 7 / 8, without the segment count: #σ 413 / 457 / 490, SBC 56 / 60 / 75, EVMAX 83 / 91 / 95, EVRET 3637 / 4513 / 5340,
  PLAYRET 0.)
  - Witness (WIT=1): switchbestexp_1, pair (15, 5). The segment [15, 16, 5] is used at index 0. Later [15, 16, 14, 10, 5] is used, and
    [15, 16, 5] is used again at index 14. Owners: 15 Odd (succ 16), 16 Even (succ 1, 5, 14), 14 Even, 10 Even.
  - The return is Even vertex 16 going 5 → 14 → 5. In E2 Even is a minimiser of the same affine cost, so this is impossible.
- Exact obstruction (READING). A run of F is NOT one-parametric. It is a monotone walk in Even's improvement order on a product of
  per-vertex choices, and Even's improving switches revisit sub-paths (an Even vertex returns to an edge with the same continuation).
  - Every one-parameter linear family forbids such revisits for strict optima (affine path costs).
  - Gusfield's n^(log n + O(1)) bound therefore does not apply. Neither does the d-parameter n^O(d log n) (Chillara-Gajjar) with d = O(1).
  - The fixed-d results give no route either: each Even vertex's choice behaves like its own parameter.
- OPEN (not closed by this): an embedding of σ̄ ALONE (Odd's trees, with Even's choices encoded non-linearly), or an embedding into a
  lifted graph where G-paths do not map injectively. A time-indexed lift is circular (size × #σ).

### 1.5 For L-RED (READING; a design hint, not a construction)
- Carstensen-type Odd networks driven by an Even "clock" are the natural quasi-polynomial attack on SF-POLY.
- The 0/1-slope case is polynomial (Gusfield Thm 4.1; YTO ≤ n² trees), and bounded integer slopes give O(n²W) (Nishida). So the clock
  must realise super-polynomially many distinct slopes.
- Parity priorities supply weights ±2^rank, so slopes of exponential size are available in principle.

## 2. (b) Deterministic MDPs, one-player PI, and the opponent's response
| source | what it bounds | applies to F's inner one-player loop? | says anything on opponent-response changes? |
| --- | --- | --- | --- |
| Post-Ye, arXiv 1208.5083 v2, Thm 3.7 p.9: «at most O(n³m² log² n) iterations on deterministic MDPs with uniform discount using the highest gain pivoting rule»; Thm 4.8 (nonuniform, O(n⁵m³ log² n)); p.2 «Our results do not extend to policy iteration» | single-switch simplex, discounted DMDP, γ-free | READING: a one-switch analogue only. F's step on G_σ̄ is multi-switch switch-best, already bounded by R17 (n + m per λ-phase) | no |
| Hansen-Kaplan-Zwick, SODA 2014 (DOI 10.1137/1.9781611973402.63) | NOT OPENED (SIAM 403, no arXiv, no author copy); only a CRIS paraphrase seen | — | — |
| Hansen-Zwick, ISAAC 2010 (DOI 10.1007/978-3-642-17517-6_37) | abstract only (Aarhus Pure): «the first weighted graphs on which Howard's algorithm performs Ω(n^2) iterations»; full text NOT OPENED (slides were opened in T35) | lower bound for Howard on min-mean cycle (one player). N5's step is not Howard's | no |
| Asadi-Chatterjee-de Raaij, arXiv 2506.12254 v1 Thm 3.2: «(n^2+7n−6)/2 iterations» of Howard on a DMDP with 2n vertices | one-player Howard lower bound, Ω(n²) | same remark | no |
| Fearnley, arXiv 1003.3418 v1 Thm 17-18 p.12: «at least 2^n iterations» (total / average reward) | Howard on MDPs WITH random actions | no: F's inner problem is deterministic | no |
| Hansen-Miltersen-Zwick, arXiv 1008.0530 v1 Thm 6.5 p.11; p.9 «We assume here that this can be done in strongly polynomial time» | outer iterations, discounted 2-player, O(m/(1−γ) log(n/(1−γ))) | — | no: best response is a black box; Lemma 6.4 eliminates player-1 actions only |
| Mei-Sun-Ye, arXiv 2606.29568 v1, Thm 1 p.16: O(n⁶m⁴ log⁴ n) pivots, turn-based deterministic FORWARD games (no mixed-player cycles), uniform discount; p.10: «each such pivot may change Player 2's optimal response» | outer × fresh inner (Prop. 2) | — | names the obstacle; bounds it only by recomputation, NOT by counting changes |
| Björklund-Vorobyov, DAM 155 (2007), author PDF, §6 / Thm 6.1 | total opponent recomputation: «the sum of all n_i's does not exceed n^2·W» (vertex-value increases) | — | the only amortised opponent-side count found. It is pseudo-polynomial (W) and counts VALUE changes, not response changes |

- READING (b).
  - The one-player literature bounds the stretch length of SF-RED, the part that is already polynomial (R17). None of it touches SBC.
  - BV07's amortisation is the closest template: charge each opponent recomputation to vertex-value increases. For parity values (P has
    2^n values) this is exponential. That is again L-NEW's (M4).
  - A search for any bound on opponent best-response changes (arXiv API queries and extended web search, listed in the notebook) found
    none. OPEN in the literature as far as opened.

## 3. (c) Best-reply changes in the exponential SI lower bounds
| construction | source (opened) | Odd's best reply along the run | count | driver |
| --- | --- | --- | --- | --- |
| G_n, switch-all | Friedmann thesis Lemma 4.27 p.119 = LMCS 1106.0778 Lemma 6.1; Thm 4.41 p.134 | «If cycle i is closed, we have τσ(ei) = hi» (case 1), d_i when open and σ(d_i) ≺σ h_i (case 3); e_i are «the only player 1 controlled nodes with real choices» (p.118) | READING: τ restricted to {e_i} = the bit vector, ≥ 2^(n−2) changes (bit 1 flips every increment). No source states the count | rule: «the only role that player 1 has, is to hide the effect of some escape node» (p.104) |
| H_n, switch-best | thesis §4.6.2 pp.139-149, Thm 4.50; stubborn cycle p.143-144 | no τ lemma; proof «runs almost exactly the same» (p.149) | READING (on a sketch): tracks the bits, 2^Ω(n) | rule; the stubborn cycle defeats the one-step lookahead. DATA (T44/T45; L-NEW): F is linear on H_n |
| snare memorization (base rule: locally optimizing) | Friedmann, «A Superpolynomial Lower Bound for Strategy Iteration based on Snare Memorization», author preprint dated «February 13, 2013» (= DAM 161 (2013) 1317-1337, DOI 10.1016/j.dam.2013.02.007; not diffed against the published version) | Lemma 14 p.20: τσ(e_i) = h_i ⇔ (P1-2: b_i = 1; P3-4: b_i = 1 or i = µ1(b); P5: (b+1)_i = 1); Lemma 15 p.21: τσ(w_{i,j}) = q_j, τσ(v_{i,j}) = m_j as functions of b_j | READING: changes at every bit flip, exp(Ω(n)) = 2^Ω(√size) (Lemma 12: «|Hn| = O(n^2)») | arena + rule: Thm 26 p.25 holds for the locally optimizing base rule «no matter which particular snare rule is applied»; Thm 11 p.9: on the original G_n, snare memorization with Fearnley's or the greedy rule is polynomial. The new arena makes «every cycle look a bit differently in each iteration» (p.2) |
| Fearnley's snares | arXiv 1003.2976 v1, Prop. 14 p.8, p.12-13 | «closing the cycle forces Min's best response to use escape edge» (p.12) | per closing | rule: the oblivious policy «make[s] the same mistakes repeatedly» (p.13) |

- READING (c), the transfer question.
  - In all four cases τ is a slave of σ: Even closing an Even-dominated cycle forces the escape.
  - The exponential τ-count is inherited from Even's exponential σ-count. It is caused by the rule reopening and reclosing the same cycles.
  - By NO-TRANSFER (L-NEW, proved) a bound on SBC has to come from F's own σ-run. So these counts transfer to F only if F can be made to
    count, and nothing in the τ-gadgets forces that.
  - The snare family's arena ingredient (cycle contents depend on the higher bits) is the one piece built to defeat a rule that closes
    cycles eagerly, which N5-SF does in its stale frame (T46 §1 (c)). Hence it stays the natural kill target (T46, T47).
- DATA (this note, S3 start): F stays short on all three published families at the sizes run.
  - friedmannsubexp N = 1..5: #σ 5, 9, 12, 15, 19; SBC 1, 5, 9, 12, 16.
  - fearnleysubexp N = 1..5: #σ 5, 7, 10, 13, 16; SBC 1, 3, 5, 6, 9.
  - switchallexp N = 1..6: SBC 1, 3, 3, 3, 4, 5.
  - switchbestexp N = 1..8: SBC 1, 4, 11, 26, 49, 56, 60, 75, reproducing L-NEW's box-55 table.
  - The snare family's SBC grows about linearly in N here; n grows quadratically.

## 4. What this means for SF-POLY
- PROVED-in-source:
  - Parametric s-t shortest path: ≤ (2n + 1)^(log n + 1) / 2 breakpoints (Gusfield 1980 Thm 4.5); n^Ω(log n) is attainable, also planar
    (Gajjar-Radhakrishnan Thm 1); 0/1 slopes: ≤ n² trees (Gusfield Thm 4.1, YTO).
  - G_n and the snare family: τ is an explicit function of the bit vector (Lemma 4.27 / 6.1; snare Lemmas 14-15).
  - Snare memorization with Fearnley's rule is polynomial on G_n (snare Thm 11).
- PROVED (L-LIT, unrefereed): the potential shift in §1.3 (monotone values + Bellman argmin are compatible with n^Ω(log n) changes); the
  one-parameter impossibility in §1.4, given a SEGRET witness (strict optima, affine costs).
- READING:
  - The leapfrog is the parametric-shortest-path mechanism, so MONO-XI + argmin alone has a quasi-polynomial floor.
  - F's run is not one-parametric. The obstruction is sub-path revisits by Even's switches (SEGRET), so Gusfield's quasi-polynomial
    upper-bound route is closed for F as it stands.
  - In the published exponential families the τ-changes are rule-driven slaves of σ.
- DATA: SBC on the three families (§3); EVRET, PLAYRET = 0, SEGRET (§1.4).
- CONJECTURE (L-LIT, offered to L-NEW and L-RED, not claimed):
  - SF-QP (weaker than SF-POLY, OPEN): SBC ≤ n^O(log n). A route would need a "few effective parameters" structure of F's run, for
    example the per-stretch σ̄ as a parametric family in the threshold of the current stretch. No such structure is known.
  - The quasi-polynomial floor of §1.3 says it would also be the best a pure value/argmin argument can give.
- OPEN:
  - SF-POLY.
  - Any literature bound on opponent best-response changes during strategy improvement (none found).
  - An embedding of σ̄ alone.
  - The DAM 2013 published text vs the preprint.
  - Gusfield JACM 1983, Carstensen 1983, Mulmuley-Shah 2001, Karp-Orlin 1981 and HKZ 2014 originals: NOT OPENED, paywalled. Owner-optional;
    nothing here depends on them beyond the opened statements cited.

## DONE / FINDINGS / NEEDS
- DONE: this note; docs/lit/T48-sbc-embed-check.py; notebook entries for every source (notes/L-LIT.md).
- FINDINGS:
  1. The leapfrog is the parametric-shortest-path phenomenon. Monotone values + argmin permit n^Ω(log n) changes (barrier, READING).
  2. F's run does not embed in a one-parameter family. SEGRET > 0 from switchbestexp_1 on (DEAD with witness).
  3. No source bounds opponent best-response changes; Mei-Sun-Ye 2026 name the obstacle and multiply instead.
  4. Friedmann's snare preprint is OPENED (Lemmas 14-15, Thm 11, 26). τ is a bit-vector slave of σ, so the exponential counts are
     rule-driven.
  5. DATA: F is short on friedmannsubexp / fearnleysubexp / switchallexp at N ≤ 5-6.
- NEEDS: none from the owner. (Paywalled originals listed in §4 OPEN are owner-optional.)
