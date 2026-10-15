# R2-TL: first-referee read of L-RED's Transfer Lemma (Random-Facet on FHZ shortest paths = RAR on sink parity games) — REFEREE-2, 2026-10-15 13:05Z
Claim refereed: claude/l-red 0d50d4a, docs/red/R2-RAR.md section "Transfer Lemma"; code experiments/red/fhz.py. Lead's brief
12:12Z (3 h box; first-referee read, not a signature). Sources opened by me (e-prints): FHZ = Friedmann-Hansen-Zwick arXiv
1410.7530v? (files introduction.tex, RandomFacet.tex, Actual-Construction.tex, Lower-RandomFacet.tex, Conclude.tex); the errata
arXiv 1410.7871 (errata.tex); Zwick arXiv 2607.06334 (RAR-arXiv.tex, section 4 and Appendix "Pseudocode of the RAR algorithm").
Fleet context: docs/si/candidates/S1.md and experiments/si/si.py at l-si 95d37d3 (best-reward start, rar); experiments/red/vj.py.
My code and outputs: docs/referee-2/R2-TL/ (tl_exhaustive.py, results_*.txt, relation_*.txt, lockstep*.txt).

## Verdict: OK with fixes (F1-F2 below; no error in the mathematics; the lemma holds, and FHZ Thm 6.3 transfers to P)

## 1. Prior plausibility (Lead's question 1): why FHZ do not state the parity-game transfer
Opened both papers and searched every file for "parity", "Markov", "MDP", "turn-based", "AUSO", "generalize", "extend".
- FHZ 1410.7530, introduction.tex lines 23-24 (verbatim): "The lower bound given in [SODA11] is for parity games, a class of
  deterministic 2-player games. The lower bounds given in [STOC11, Hansen12] are for LPs that correspond to Markov Decision
  Processes (MDPs), a class of stochastic 1-player games. ... Here, we obtain subexponential lower bounds for the running times
  of Random-Facet, Random-Perm and Random-Bland on LPs that correspond to standard acyclic shortest paths problems, the
  simplest form of deterministic 1-player games." Line 32-33: "In [SODA11, STOC11] and here we continue this line of work".
  Abstract (random_facet_shortest_paths.tex:85): "This shows that the stochasticity of the MDPs ... is not needed in order to
  obtain lower bounds for Random-Facet."
- Conclude.tex line 5 (the only open problem named): "Our lower bounds were all obtained using shortest paths problems. Another
  interesting open problem is whether similar lower bounds can be obtained using graphs in which the out-degree of each
  vertex is 2. Such binary instances would supply explicit Acyclic Unique Sink Orientations (AUSOs) on which Random-Facet
  takes subexponential time."
- Errata 1410.7871, section 1 (verbatim): "It should be stressed that the error is unrelated to the lower bound construction
  itself; it only involves the relationship between the Random-Facet algorithm and the modified version, Random-Facet*. In
  particular, the lower bound for Random-Facet* remains correct." and "The proof in [Hansen12] was presented for Markov
  decision processes. In [FHZ 2014] we transfer the lower bound construction to the setting of shortest paths where we again
  prove a 2^{Ω~(m^{1/3})} lower bound for Random-Facet". On parity games the errata says only (end of section 1): "It is not
  difficult to obtain similar examples for parity games." (about its 3-vertex cube examples).
Reading: neither paper names an obstruction to re-encoding shortest paths as sink parity games; FHZ's stated direction of
travel is the opposite one (from parity games and MDPs DOWN to the simplest deterministic 1-player setting, to show
stochasticity is not needed). The missing statement "hence also for parity games" is therefore not evidence of an error; the
transfer is specific to G_{n,r,s,t}'s cost structure (one class cost per level, class gaps ≥ 4^j, offsets < 2), as L-RED says,
and the SODA 2011 construction already was a parity game built on the same counter. No prior-plausibility objection.

## 2. The lemma, line by line (Lead's question 2)
Definitions checked against the sources.
- G_{n,r,s,t}: Table 1 (Actual-Construction.tex) transcribed correctly in R2-RAR.md and fhz.py (a0: 2^{2i+1} + (k-1)ε for all
  k ∈ [s]; b0: 2^{2i+1} + 1 + (j-1)ε; u0, w0: 2^{2i}; u1, w^j, a1, b1: 0; multiplicities t on a0, b0, u1, u0, w^j, w0; a1, b1
  single; target t = u_{n+1} = w_{n+1}; ε = 1/(rs)). Def. 5.2 "functional" verbatim. Initial tree: FHZ: "any initial tree B_0
  composed entirely of zero-edges" (the costly a0, b0, u0, w0). Thm 6.3 statement verbatim as quoted by L-RED.
- Random-Facet: errata Fig. 1 / FHZ section 2: pick e uniformly in F \ B, B' = RF(F \ {e}, B), IMPROVE(B', e) strict ("shorter"),
  pivot, recurse. Zwick's RAR (section 4 steps 1-5 and the Appendix pseudocode): identical recursion with "(c → b) ∈ H" as the
  test, i.e. r is a strictly improving action for b. L-SI's si.py `_rar` implements exactly this with the VJ key. Same recursion.
- VJ valuation on P (Friedmann 1106.0778 §3 as implemented in vj.py/si.py): (cycle node, path set of nodes more relevant than
  the cycle node, length); set order by the maximum of the symmetric difference; for an odd cycle node longer is better.
  Relevance with injective priorities p' = 2·rank + parity, rank by (priority, index): every priority-0 vertex (G-vertices,
  relays) ranks below the sink (priority 1), so the path sets contain class vertices only, as the lemma uses. Checked.
Proof steps.
- Reduction to prefixes: both paths from x to t, identical after the merge vertex (both follow B); G compares prefix costs, P
  compares prefix sets then lengths. Correct.
- (1) Level accounting (Lead's named item). A path from level i visits each level i..n exactly once (edges stay in a level or
  go up one) and pays one class cost per level: A = 0, B = 4^j, C = 2·4^j + δ with 0 ≤ δ < 2 (a-escape δ = (k-1)ε < 1,
  b-escape δ = 1 + (j-1)ε < 2: Table 1). Sum of costs below level i ≤ Σ_{j<i}(2·4^j + 2) = (2/3)(4^i − 4) + 2(i − 1) < 4^i − 2
  for all i ≥ 2 (and 0 for i = 1); verified symbolically and for i ≤ 30. Within a level, different classes differ by ≥ 4^j
  (B − A = 4^j, C − B = 4^j + δ); the text's "at least 4^j − 2" is weaker than true and still sufficient. Correct.
- (3) Different class sequences (the step L-RED flags). Re-derived in full: let j* be the highest differing level. Above j*
  the classes agree; at a level j > j* the two paths cannot both be on the u-side or both on the w-side without merging
  (same entry vertex), both class A merges at b_{j,1}, both class C merges at u_{j+1} (with a within-level offset difference
  only there), so between j* and the merge level both are class B on opposite sides, and the entry sides at j*+1 force
  w-side ∈ {A, B} and u-side ∈ {B, C} at j* with a strict class difference, w-side cheaper by ≥ 4^{j*}. Offsets at the merge
  level: a-escape d = k − 1 ∈ [0, s − 1] on the w-side, b-escape d = rs + j − 1 ∈ [rs, 2rs − 1] on the u-side: never equal, u-side
  larger. G: w-side wins by ≥ 4^{j*} − (4^{j*} − 2) − (δ difference < 2) > 0. P: the symmetric difference tops at the merge
  band (o_{j,d_u} odd on the u-side path) if such a level exists, else at band j* (A carries the even g_{j*}, the top of its band;
  B nothing; C an odd o), ordered A > B > C. Bands are disjoint and increase with the level (base_{i+1} = base_i + 4rs + 2 >
  base_i + 4rs). All verdicts agree; no ties arise since the sets differ. Correct as written.
- (2) Equal class sequences: see F1. The verdicts agree in every sub-case, including the one the text omits.
- Ties: a G-tie needs equal class sequences with equal offsets; then the P-sets are equal and I checked the P-lengths are
  equal in each sub-case (copies of one multi-edge: merge at the next vertex; w^j vs w^{j'} with class A: s chain edges each;
  with class C and equal k: k − 1 chain edges and one escape each). Correct, so ties are ties in both models (neither
  direction improving), which the run equivalence needs.
- Multi-edges as equal-length relays: x → m_ℓ → [shared o/g] → y per copy: equal sets and lengths, so copies tie. Correct.
- Best-reward start = B_0: si.py `initial("best")` ranks successors by (reward, index) with reward 0 for every relay (priority
  0, even), so it takes the highest-index relay; fhz.py appends the t costly copies after the zero-cost edges and creates
  relay ids in edge order, so the start is the LAST copy of each zero-edge: a tree of zero-edges, hence a valid B_0 (FHZ
  allow any). Note fhz.py's own driver uses the FIRST copy (`costly[0]`); both are valid B_0 and copies are interchangeable,
  so the distributions coincide. Correct (remark F2).
- Run equivalence: RAR's random set B on P is {relay edges of G-edges not in σ_B} (relays, g, o vertices have one successor),
  the same set as F \ B in G; the tests agree by the lemma; by induction the two recursions make the same choices and
  pivots, so the switch counts are equal run by run. Correct. The lemma's quantification over functional F is vacuous (the
  test depends only on (B, e); take F = E) and the recursion visits non-functional F too; harmless (remark F2).
- Sizes and priorities: |V(P)| = |V(G)| + |E(G)| + n(2rs + 1) class vertices + 1; distinct priorities n(2rs + 1) + 2 ≤ |V(P)|, so
  compression to {0..|V|} (TARGET §1) is available. Correct.

## 3. Checks run (Lead's question 3 and more)
- fhz.py `relation` on settings not in L-RED's list: (7,2,2,3) 300 samples, (9,3,1,2) 200, (5,1,4,1) 400: improving sets
  identical on all 900 random (F, B) pairs. `lockstep3 5 2 1 2` (2 seeds, three models incl. the generic VJ engine) and
  `lockstep 6 2 2 1` (2 seeds, 6,712 tests): all agree. Outputs in R2-TL/.
- Independent exhaustive check (tl_exhaustive.py: G from Table 1 and P from the lemma's description, written by me; VJ order
  from 1106.0778 §3): for EVERY tree B and EVERY edge e ∉ B, strict improvement in G ⟺ strict improvement in P.
  (2,1,1,1): 2,048 tests; (1,2,1,1): 672; (1,1,2,2): 18,144; (2,1,1,2): 414,720. 0 disagreements.
- Level accounting inequality: verified for i ≤ 30 (and symbolically).

## 4. Findings
- F1 (fix, case (2)). The sentence "If x is a chain vertex, both are escapes (the chain edge is unique): different copies of
  the same offset" omits the sub-case where one edge is the chain edge a1/b1 and the other an escape copy a0/b0 while the
  chain path also escapes later at the same level (class C on both, offsets k − 1 < k'' − 1, or ≥ rs on the b-chain). Verdicts
  still agree: G orders by offset, P by the larger odd o_{i,·} on the later escape; and if the chain path reaches w_{i+1}
  (class A) the classes differ and case (3) applies. Add the sub-case (two lines).
- F2 (remarks, no change in substance). (a) "differ by at least 4^j − 2" can be "≥ 4^j". (b) The quantifier "for every
  functional F" is not needed for the test (it depends on (B, e) only), and RAR's recursion also visits non-functional F;
  state the lemma for all trees B ⊆ E and e ∉ B. (c) fhz.py's B_0 uses the first copy of each zero-edge, si.py's best-reward
  start the last; both are FHZ B_0's and equivalent by symmetry; say so.
- No counterexample: none in 435,584 exhaustive tests plus 900 + 8,000-odd randomised tests.

## 5. What this read does and does not establish
- Established (modulo the first-referee status): the transfer lemma holds for G_{n,r,s,t}; RAR with VJ valuations on
  P_{n,r,s,t} from any zero-edge start performs, run for run, Random-Facet's switches on G from the same B_0; so FHZ Thm 6.3
  (e^{Ω(√n)} expected switches, parameters r = Θ(log n), s = Θ(√n log n), t = Θ(log n)) applies to S1 on sink parity games
  of size Θ(n^{3/2} log^3 n): S1 is not polynomial expected time. FHZ Thm 6.3 itself is a black box (published, opened).
- Not established here: that this "restores" a parity-game lower bound for original Random-Facet in the literature's sense
  (it does, for the fleet, as a refereed-only statement once double-refereed); nothing is Lean-checked.
- Gaps for the record: G-TL-1 FHZ Thm 6.3 taken as a black box; G-TL-2 the lemma's proof is prose (re-derived here, F1 to be
  applied); G-TL-3 run equivalence relies on si.py's `rar` matching Zwick's pseudocode (checked by reading; L-RED's
  si.py-vs-driver means 19.1/26.3 against 18.9/29.9 are consistent but not a proof).

## 6. SIGNATURE (second referee; claude/l-red 49ae306, docs/red/R2-RAR.md; 2026-10-15 13:50Z)
Revision checked (diff 0d50d4a..49ae306, docs/red/R2-RAR.md): F1's missing sub-case added to case (2) with the correct
offset argument; F2(a) "≥ 4^j"; F2(b) the lemma now quantifies over all trees B ⊆ E(G) and e ∉ B, with the strictness of
si.py's test named; F2(c) the last-copy / first-copy B_0 remark; the first referee's fix in (3) ("cheaper at j* by at least
4^{j*} > (sum below j*, < 4^{j*} − 2) + (offset difference, < 2)") is the inequality I re-derived in section 2. fhz.py changed
only in its docstring (now matching the code's band layout). Read after my first read: docs/referee/R-TL2.md (first referee,
"OK with fixes"); its case analysis (§3, Steps 1-3) is the same as mine and its findings 1-2 are my F1/F2(a) and the (3) fix.
Signed statement (exactly): "Transfer Lemma (R2-RAR.md, l-red 49ae306): for every tree B ⊆ E(G_{n,r,s,t}) and every
e ∈ E(G) \ B, e is a strictly improving switch for B in G_{n,r,s,t} (FHZ arXiv 1410.7530 Table 1) iff the relay edge of e is a
strictly improving edge for σ_B in P_{n,r,s,t} (fhz.py build(), VJ valuation of Friedmann 1106.0778 §3 with priorities made
injective by rank); ties in G are ties in P. Consequently Random-Facet on G from any zero-edge tree B_0 and Random-Action-
Removal with the strict VJ test (si.py `rar`) on P from σ_{B_0} are the same random process, switch for switch, and FHZ
Theorem 6.3 gives e^{Ω(√n)} expected switches of S1 on P_{n,r,s,t} with r = Θ(log n), s = Θ(√n log n), t = Θ(log n), a sink
parity game with Θ(n^{3/2} log^3 n) vertices and priorities compressible to TARGET's range: S1 is not polynomial expected
time (not M4-R)." Verdict: **OK**, signed as second referee at l-red 49ae306.
Gap list (for GAPS.md / RESULTS.md):
- G-TL-1. FHZ Thm 6.3 is a black box (published, errata-surviving; opened source; not re-derived by the fleet). Its
  parameters are asymptotic (r, s, t = Θ(·)); the measured growth tables are consistency data only.
- G-TL-2. The lemma's proof is prose, re-derived independently by both referees; machine-checked exhaustively only for small
  parameters ((2,1,1,1), (1,2,1,1), (1,1,2,2), (2,1,1,2): 435,584 (tree, edge) tests by REFEREE-2; the first referee's own
  cases) and by random sampling beyond.
- G-TL-3. S1's conventions are read from si.py at l-si 95d37d3: the improving test is strict (`key(val[r]) > key(val[b[v]])`),
  and the best-reward start (`initial("best")`) is the last relay of each vertex, a zero-edge tree. The signature is for
  that rule; a non-strict test, or a start that is not a zero-edge tree, is outside FHZ Thm 6.3's hypothesis.
- G-TL-4 (AUSO vs ties). Zwick's RAR is defined on AUSOs, where every edge of the hypercube is oriented; on P equal
  valuations occur (copies of a multi-edge, and the tie sub-cases of case (2)), so P's strategy space with the VJ order is
  not an AUSO as given. The run equivalence does not need it: the lemma makes the strict test agree with FHZ's strict
  "shorter" (ties are non-improving in both), which is what the recursion reads. The strict convention must be stated as
  part of S1's definition (it is, in R2-RAR.md and S1.md), and Zwick's upper-bound analysis is not invoked.
- G-TL-5. The lemma is specific to G_{n,r,s,t}'s lexicographic costs; it is not a reduction from shortest paths to sink parity
  games (R2-RAR.md says so). Novelty of the parity-game statement is L-LIT's to check.
- G-TL-6. Priority compression to {0..|V|} (TARGET §1) is order- and parity-preserving and the valuation reads only order and
  parity; stated, not formalised. Nothing is Lean-checked (not required at M3).
- G-TL-7. Supporting code: fhz.py's three models and vj.py (changed by 18 lines in this revision, not re-reviewed) are
  evidence, not part of the signed statement.
