# T52: bounds on a per-W-run adoption sequence from fields not usually paired with parity games (DS sequences, forbidden 0-1 matrices, wqo / controlled bad sequences, matroid best-response dynamics, sorting / monotone circuits)
L-LIT successor 4 (Opus 5.5), D18, back to WORKING under D17/L39. Lead's brief 2026-10-30 13:09Z (T52). Written 2026-10-30 from 13:14Z
(date -u). Working note, unrefereed, not a TARGET.md claim. G-N5-TIME, R*-POLY and FL-POLY stay OPEN. Labels: PROVED-in-source /
PROVED (L-LIT, elementary, unrefereed) / READING (every N5 implication) / DATA / DEAD / OPEN / NOT OPENED.
Fleet inputs (read; not mine):
- l-new 893b9346 docs/new/N5-FREE-box85.md: Theorem FREE-RED; Lemma RET-ΞRISE; R89 R*-RISE as quoted there.
- docs/new/N5-WAIT-box84.md: Lemma WAIT-CYCLE′, Corollary DEAD-CYCLE, E0-BOUND, TRIPLE-RED; the §5 obstruction, the «reads» recursion.
- l-red docs/red/R135-desync-gate.md: Lemma WAIT-CYCLE.
- l-red docs/red/R136-pattern-clock.md: Lemma PAT-SW, Lemma ALT-ESCAPE.
- l-red docs/red/R137-free-returns.md: FREE_F(X, g) = K·m/4 at a chooser X → {O1, O2}.
Sources are in notes/L-LIT.md (sha256, pages); all opened 2026-10-30 unless noted.

## Summary (one line per candidate; details in §1-§5)
| candidate | opened source | hypothesis needed | given by the fleet's lemmas? | bound it would give |
| --- | --- | --- | --- | --- |
| Davenport-Schinzel (DS) sequences | Pettie 1204.1086 (λ_s); Nivasch 0807.0484 Thm 1.5 (generalized, Ex_u) | per vertex X: X's choice sequence in a W-run has no alternation a…b…a… of length s + 2 for a FIXED s (or: the switch sequence is r-sparse and avoids a fixed pattern u) | NO, and DEAD at fixed s: R137's chooser X (deg 2) alternates ≈ 2·128 times in ONE W-run (n 362) | Σ_X λ_s(deg X) = near-linear in m |
| forbidden 0-1 matrices (Füredi-Hajnal / Marcus-Tardos) | Fox 1310.8378 (states Marcus-Tardos (1)); Marcus-Tardos JCTA 2004 NOT OPENED | the vertex × transition switch matrix avoids a fixed permutation matrix P, AND transitions switch > c_P vertices on average | NO: no forbidden permutation is known; c_P = 2k⁴·C(k², k) ≥ 192 vs about 8 switches per transition (DATA) | T = O(n) under both conditions; otherwise nothing (mass ≤ c(n + T) is circular) |
| Higman / Dickson, controlled bad sequences | Figueira-Figueira-Schmitz-Schnoebelen 1007.2989; Schmitz-Schnoebelen 1103.4399 | the run, read in a wqo, is a BAD sequence with controlled norm | NO: N5's run is a GOOD (Ξ-monotone) chain; the wqo route gives only fast-growing bounds (F_k for N^k, multiply-recursive for Higman) | worse than the trivial exponential |
| matroid best-response dynamics (rank trick) | Ackermann-Röglin-Vöcking, ECCC TR06-067 (JACM 55(6) 2008) Thm 3 | strategies are matroid bases, and moves strictly improve a potential over POLYNOMIALLY MANY distinct local values (ranks) | PARTLY: Even strategies are the bases of a partition matroid; Ξ-monotone; RET-ΞRISE + R*-RISE reduce R*_F to ΞCH. Missing: XI-CH-POLY (each vertex's Ξ changes polynomially often per W-run) | R*_F ≤ Σ_e ΞCH_F(head e) ≤ m·p(n), hence R*-POLY |
| sorting networks / monotone circuits | none opened (no theorem whose hypothesis matches) | an inversion-type potential: a fixed order in which every switch removes an inversion | NO: returns exist (R137) | — |

- Main READING. Every polynomial bound found in these fields comes from one of two mechanisms:
  - (A) a FIXED forbidden pattern over a polynomial alphabet: DS, generalized DS, Marcus-Tardos;
  - (B) a monotone potential with POLYNOMIALLY MANY levels: Ackermann-Röglin-Vöcking's rank trick; Koh-Loho's universal-tree labels (T50) are the quasi-polynomial version.
- The fleet's lemmas do not give (A).
  - WAIT-CYCLE′, DEAD-CYCLE and ALT-ESCAPE are state-conditional forbidden configurations (route patterns, cycle rewards, shared
    continuations), not letter patterns.
  - R137 rules out any fixed alternation bound per vertex.
- (B) is one lemma away: XI-CH-POLY. Via RET-ΞRISE and R*-RISE it gives R*-POLY directly. With FL-POLY and FREE-RED it would give
  polynomial W-runs. XI-CH-POLY is a statement about one vertex's monotone Ξ chain per W-run (DATA max ΞCH 63 at gate_K64_n581), and
  it is the natural target for a rank / height argument.

## 1. Davenport-Schinzel sequences
- (a) PROVED-in-source.
  - Pettie, «Sharp bounds on Davenport-Schinzel sequences of every order», arXiv 1204.1086. Definition (p.3): λ_s(n) = Ex(abab… of
    length s + 2, n), the maximum length of a 2-sparse sequence over n letters with no alternating subsequence of length s + 2.
  - p.1 footnote: a lower envelope of functions crossing pairwise ≤ s times is a DS(n, s) sequence.
  - Bounds (PDF p.4, Theorem 1.2): λ_1 = n, λ_2 = 2n − 1, λ_3 = 2nα(n) + O(n√α(n)), λ_4 = Θ(n·2^α(n)), and n·2^((1±o(1))α^t(n)/t!)-type
    bounds for s ≥ 5 (t = ⌊(s − 2)/2⌋): near-linear for every fixed s.
  - Nivasch, «Improved bounds and new techniques for Davenport-Schinzel sequences and their generalizations», arXiv 0807.0484:
    - §1.1: generalized DS. «Let u … be a sequence with ‖u‖ = r distinct symbols and length |u| = s. Then we denote by Ex_u(n) the maximum
      length of an r-sparse, u-free sequence on n distinct symbols … The requirement of r-sparsity is necessary, since an (r − 1)-sparse,
      u-free sequence can be arbitrarily long.»
    - §1.2: Klazar's Ex_u(n) ≤ F_{r,s−1}(n) ≤ n·2^O(α(n)^(s−3)).
    - Thm 1.5 (PDF p.5): sharper, n·2^((1/t!)α(n)^t + …), t = ⌊(s − r − 2)/2⌋.
- (b) Hypothesis needed (two forms).
  - (DS-1) Per Even vertex X and per W-run F: the sequence of X's successive choices has no subsequence a…b…a…b… of length s + 2, s
    fixed. Then the switches of X in F number < λ_s(deg X), and |F| ≤ Σ_X λ_s(deg X) = O(m·2^poly(α(m))) for fixed s.
  - (DS-2) The per-W-run sequence of switch events, with letters = vertices or edges, is r-sparse and u-free for a fixed u. Then
    |F| ≤ Ex_u(alphabet) = near-linear.
- (c) Given by the fleet? NO.
  - DS-1 is DEAD. R137's chooser X (Even, priority 0, successors {O1, O2}) returns to one edge 128 times inside one W-run (n 362/378). So
    X's 2-letter choice sequence alternates about 256 times: s grows with n.
  - RET-ΞRISE bounds the alternation only by ΞCH_F(g), which is circular.
  - DS-2: no fixed forbidden letter pattern is proved.
    - WAIT-CYCLE′ forbids «σ_t(X) = g with σ_t|Even(π) = P after a REG block with (π, P)», which is conditional on a STATE pattern P.
    - DEAD-CYCLE forbids re-consistency of a cycle whose top reward fell below a member's current cycle reward, which is conditional on
      values.
    - ALT-ESCAPE forbids the two-gate interleaving only under a shared continuation; nested entries are open (R136 Addendum 1).
  - Missing lemma: FORB-u, a fixed u that every r-sparse cleaned switch sequence of a W-run avoids.
  - DATA caution (READING): mkrb W-runs are quadratic (R136 §3: about 2Km iterations at n ≈ 6(K + m)). If the cleaned per-W-run
    switch sequence over the n vertex letters is r-sparse, near-linear Ex_u(n) rules out every fixed u there. The r-sparse check on
    mkrb is a DATA ask (L-RED / L-COMP).
- (d) Bound it would give: near-linear in m per W-run (DS-1), or in the alphabet (DS-2).
- READING. The DS lens says exactly what kind of lemma would close R3-POLY: a bounded number of pairwise «overtakes» per pair of
  successors per W-run. The leapfrog (T48 §1.3, box 75) and R137 are precisely unbounded overtakes. DS bounds are for lower envelopes of
  functions with BOUNDED pairwise crossings. N5's successor Ξ chains are monotone but cross unboundedly often, as in Carstensen's
  instances (T51 §4).

## 2. Forbidden 0-1 submatrices (Füredi-Hajnal, Marcus-Tardos, Pettie)
- (a) PROVED-in-source (via Fox, «Stanley-Wilf limits are typically exponential», arXiv 1310.8378, p.3).
  - «Let ex(n, P) be the maximum possible mass of an n × n matrix that avoids P … Füredi and Hajnal conjectured that, for each
    permutation π, we have ex(n, π) = O(n) … Marcus and Tardos [21] proved that ex(n, π) ≤ 2k⁴·C(k², k)·n (1)» for a k-permutation.
  - Marcus-Tardos JCTA 107 (2004), DOI 10.1016/j.jcta.2004.04.002: NOT OPENED (the statement is used here only as Fox states it).
  - Pettie's light / heavy pattern results: NOT OPENED; Nivasch §1.1 notes that Alon-Friedgut used generalized DS for Stanley-Wilf.
- (b) Hypothesis needed. Encode W-run F as the 0-1 matrix M (rows = Even vertices, columns = transitions; 1 where the vertex switches).
  Mass(M) ≥ |F|. Super-additivity gives ex(n × T, P) = O(n + T), so mass ≤ c_P(n + T). That is circular, since mass ≥ T. It yields
  T = O(n) only if additionally every column has more than c_P ones, i.e. each transition switches > c_P vertices.
- (c) Given? NO, on both counts.
  - No forbidden permutation matrix is proved for M.
  - c_P = 2k⁴·C(k², k) is 192 already for k = 2, while N5-SF averages about 8 switches per transition (switchbestexp_5: 2993 / 364;
    T49 §1). Plain N5 is similar (T51 §5: EVCHG / #σ about 5).
- (d) Bound it would give: O(n) per W-run under both conditions; nothing otherwise.
- READING: the matrix route is the DS route with a worse constant. It adds nothing for N5 beyond §1.

## 3. Higman / Dickson: well-quasi-order length bounds for controlled bad sequences
- (a) PROVED-in-source.
  - Figueira-Figueira-Schmitz-Schnoebelen, «Ackermannian and primitive-recursive bounds with Dickson's lemma», arXiv 1007.2989 (LICS
    2011), p.2: a sequence over N^k is t-controlled if |x_i|_∞ < f(i + t). L_{k,f}(t) is the maximal length of a t-controlled bad
    sequence. «for linear control functions, L_{k,f} is at level F_k [of the Fast Growing Hierarchy], and more generally, for a control
    function f in F_γ, L_{k,f} is at level F_{γ+k−1}» (improving McAloon's F_{k+1}).
  - Schmitz-Schnoebelen, «Multiply-recursive upper bounds with Higman's lemma», arXiv 1103.4399 (ICALP 2011): multiply-recursive
    bounds for Higman's lemma (abstract; Main Theorem §5).
- (b) Hypothesis needed: the run (or a derived sequence) is BAD in a wqo (no i < j with x_i ≤ x_j), with a controlled norm.
- (c) Given? NO. N5's run is the opposite: Ξ is non-decreasing (a GOOD chain), and states never repeat (R15 (c)). Any bound by a wqo
  argument over finite strategy spaces is at least the height of the order, which is exponential (2^n values in P).
- (d) Bound it would give: F_k-level (for fixed k, primitive recursive but far above exponential), i.e. worse than trivial.
- DEAD as a polynomial route (READING; the bound is by the source's own level statement).

## 4. Matroid basis-exchange / matroid congestion games: the rank trick
- (a) PROVED-in-source. Ackermann-Röglin-Vöcking, «On the impact of combinatorial structure on congestion games», ECCC TR06-067
  (April 2006; JACM 55(6) 2008, DOI 10.1145/1455248.1455249), sha256 d13b2032bc8f8721.
  - Abstract (p.1): «the lengths of all best response sequences are polynomially bounded in the number of players and resources … the
    matroid property is a necessary and sufficient condition».
  - Thm 3 (PDF p.5): «Let Γ be a matroid congestion game. Then players reach a Nash equilibrium after at most n²·m·rk(Γ) best responses.»
  - Proof (PDF p.5): replace every delay value by its RANK in the sorted list of all ≤ n·m delay values. Lemma 4 (via Schrijver's perfect
    matching between S_i* \ S_i and S_i \ S_i*) shows a best response still strictly decreases the rank-delay. Rosenthal's potential in
    ranks is ≤ n²·m·rk(Γ).
  - PDF p.5: «Theorem 3 is independent of the delay functions. In particular, we do not assume monotonicity».
  - Thm 7 (PDF p.7): for any non-matroid inclusion-free class there are games with exponentially long best-response sequences.
- (b) Hypothesis needed for N5 (READING): (i) a potential that strictly moves at every counted step; (ii) polynomially many distinct
  levels of the local quantity entering it.
- (c) Given? PARTLY.
  - Even strategies are exactly the bases of the partition matroid ⊕_X U_{1,deg X}.
  - Ξ is monotone (MONO-XI; R15 (a)), which plays the role of (i).
  - RET-ΞRISE (box 85 §2) and R89 R*-RISE (box 85 §4: «late adoptions of an edge ≤ ΞCH_F(target)») reduce both returns and blocked late
    adoptions to the Ξ-change counts of target vertices.
  - What is missing is (ii), as one lemma: XI-CH-POLY, ΞCH_F(v) ≤ p(n) for every vertex v and every W-run F (equivalently, v takes
    polynomially many distinct Ξ values in F, since Ξ(v) is a monotone chain).
  - N5 is not a congestion game: Ξ is not a sum of per-resource delays. So Lemma 4's matching step has no analogue, and only the
    "levels" half of the trick transfers.
- (d) Bound it would give: R*_F ≤ Σ_(X, g) ΞCH_F(g) ≤ m·p(n), i.e. R*-POLY. With FL-POLY, FREE-RED gives
  |F| ≤ (n − 1)(m·p(n) + 1) + FL_F per W-run.
- DATA (fleet, existing). Max ΞCH_F 63 at gate_K64_n581 (n 581; box 85 §2). On pftheta34_n32 ΞCH = 34 = |F| (WCH 7). N5-SF's whole-run
  VALMAX was 290 at n 260 (box 55 (M4)). No super-polynomial ΞCH instance is known.
- READING. XI-CH-POLY is not easier than R*-POLY in general (ΞCH ≤ |F|). But it is a statement about ONE vertex's monotone chain per
  W-run. That is the form in which height arguments (this section; Koh-Loho, T50 §1) and the DEAD-CYCLE lemma act: DEAD-CYCLE removes a
  cycle from Ξ(v)'s future once v's cycle reward rises above the cycle's top. A per-W-run count of the distinct (cycle node, P) values of
  Ξ(v) is the concrete target.
- Elementary companion (PROVED, L-LIT): in the partition matroid with an ADDITIVE weight, every strictly improving sequence of single
  switches has length ≤ Σ_X (deg X − 1) ≤ m (each vertex's own weight rises). N5's non-additivity is exactly the «reads» coupling of box
  84 §5.

## 5. Sorting networks / monotone-circuit depth
- (a) No source opened. I found no theorem whose hypothesis is a sequence of local improvements under a monotone valuation that is not
  a fixed comparator schedule.
  - Monotone-circuit depth lower bounds concern circuit families, not the run lengths of a given dynamics.
  - The nearest opened result is Mulmuley-Shah's breakpoint-to-PRAM consequence (T51 §1), which gives only an ǫ log n depth bound.
- (b)-(d) READING. The sorting analogy is an inversion potential: a fixed total order on each X's successors in which every switch moves
  forward. That is "no returns", which R137 refutes (128 returns at one edge in one W-run). DEAD as stated.

## 6. Pointers for L-NEW 38 (copy for the Lead to relay)
- Target lemma XI-CH-POLY (§4). For every W-run F and vertex v, ΞCH_F(v) ≤ p(n). Then R*-POLY follows by R89 R*-RISE, and with FL-POLY,
  N5 W-runs are polynomial (FREE-RED). The template is the rank trick (Ackermann-Röglin-Vöcking ECCC TR06-067 Thm 3: «at most n²·m·rk(Γ)
  best responses», via ranks of ≤ n·m delay values). It needs polynomially many levels of Ξ(v) per W-run. DEAD-CYCLE is the natural tool
  to bound the cycle-node component; the P component is the open part (cf. T48 §1.3, box 55 (M4)).
- DS / forbidden matrices (§1-§2): would need a FIXED forbidden letter pattern or a bounded number of pairwise overtakes per successor
  pair. R137's chooser kills the per-vertex form (s grows with n). So these fields cannot close R3-POLY with the current lemmas.
- wqo / Higman (§3): wrong direction (bad sequences) and non-elementary bounds. Do not pursue.

## DONE / FINDINGS / NEEDS
- DONE: this note; notebook rows (Pettie 1204.1086, Nivasch 0807.0484, Fox 1310.8378, Figueira et al. 1007.2989, Schmitz-Schnoebelen
  1103.4399, Ackermann-Röglin-Vöcking ECCC TR06-067); NOT OPENED: Marcus-Tardos JCTA 2004, Füredi-Hajnal 1992, Pettie's 0-1 matrix papers,
  Sharir-Agarwal book.
- FINDINGS:
  1. DS / generalized DS: near-linear bounds need a fixed alternation or a fixed forbidden pattern. DEAD per vertex by R137 (deg-2 chooser,
     about 256 alternations in one W-run); no fleet lemma is a letter pattern.
  2. Forbidden 0-1 matrices: circular (mass ≤ c(n + T)) unless each transition switches > c_P ≥ 192 vertices. No help.
  3. Higman / Dickson: N5's run is a good chain, not a bad sequence; the bounds are F_k-level. DEAD for polynomiality.
  4. Matroid congestion games (Ackermann-Röglin-Vöcking Thm 3): the rank trick gives polynomial best-response sequences from
     polynomially many value levels. For N5 the one missing lemma is XI-CH-POLY, which gives R*-POLY via R*-RISE (READING).
  5. Sorting / monotone circuits: no matching theorem; an inversion potential is "no returns", refuted by R137.
- NEEDS: none from the owner.
