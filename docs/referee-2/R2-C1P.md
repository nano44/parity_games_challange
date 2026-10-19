# R2-C1P: second-referee check of the 𝒞^1P chain (CTRL, NOSTEAL-1P, OUTCOME-MONO-1P, SAME-CTX, LEX, R46 NEST*-BOUND). REFEREE-2, 2026-10-19 01:29Z (date -u, at push)
Signature: (Opus 5.5, D12). Packet P-C1P (Lead 01:14Z).
A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7.
Objects at trunk 01d63d7:
- docs/alg/GAP-A-M.md §27b, §28e, §33b, §35b (L-ALG);
- docs/red/R46-nest-bound.md §1, §2b, §3 (L-RED).
I did not read docs/referee/ before pushing this report.
Code read: tools/oink/src/src/solvers/dtl.cpp and dtl.hpp at 8fbf0a7 (built by scripts/setup_oink.sh). Every dtl.cpp line number
cited in the objects was re-read in that file; they match (§6).
Signed results used as given: R7, R8 (STR-DET), R9 (a)-(c), R10, R11 (b)-(c), DTL-proof Lemma 1.2/1.2b.

## Verdicts (Opus 5.5, D12)
| item | verdict |
| --- | --- |
| §27b Lemma CTRL | SIGN |
| §27b Lemma NOSTEAL-1P | SIGN |
| §27b Corollary (GAP-A on 𝒞^1P ⇐ (CTX⁺), on signed R9 (c), R11 (c)) | SIGN |
| §28e Lemma OUTCOME-MONO-1P | SIGN (note N-OM1) |
| §33b Lemma SAME-CTX | SIGN WITH GAPS: G-SC-1 and G-SC-2 (both citation/definition gaps, closed here) |
| §35b Lemma LEX | SIGN WITH GAPS: G-LEX-1 (major). The proof covers only transitions whose depth-0 chain changes. "c(s′) < c(s″) for ALL s′ < s″" needs (CHAIN-CHANGE), which is DATA only (GAP-A-M §33a, R42 §3). Proved: c(s′) ≤ c(s″), strict whenever the chains differ |
| R46 §1 (K-constraint) | SIGN, with P read as the first-difference positions of the chain-CHANGING transitions |
| R46 §2b (Lemma L-NEST*) | SIGN (proof checked line by line; independent brute force agrees with every table value) |
| R46 §3 THEOREM (NEST*-BOUND) | SIGN WITH GAPS: G-R46-1 (major, = G-LEX-1). "S − 1 = \|P\|" needs (CHAIN-CHANGE). As proved: S − 1 = \|P\| + Z, where Z is the number of identical-chain transitions, and \|P\| ≤ (2(d+2)(n+1)²K)^d. So GAP-A on 𝒞^1P ⇐ (NEST*-BOUNDED) ∧ (CHAIN-CHANGE, or a polynomial bound on Z). Two named statements, not one |

## 1. §27b Lemma CTRL: SIGN
- Run structure. `--dtl` is the non-interleaved solver (dtl.hpp:33 `interleaved = false`; IDTLSolver alone sets it true).
  run() (1106-1120) makes Even's searches until one returns false, then Odd's. So each player has one block of searches.
- Every tangle that search(C) extracts is a dominion.
  - extractTangles computes escapes only from vertices with owner ≠ pl (329-338), against the member G (the current game).
  - In 𝒞_C a q-vertex has one successor. In a nontrivial SCC that edge stays inside, and a one-vertex SCC needs a self-loop
    (315-317).
  - So tangleto is empty, and the dominion branch runs (347-376: dominions++, vertices into SQ/dom_vector).
  - This holds at every depth, since the escapes are computed in the member G.
- search() returns true iff tangles or dominions changed (1068). In 𝒞_C only dominions can change.
  - A dominion's vertices are pushed to dom_vector unless already in S in this search. The first dominion of the search pushes them.
  - They are solved and removed (1018-1037).
  - So every true search(C) removes ≥ 1 vertex. C's block has ≤ n true searches plus one false: ≤ n + 1. ✓
- DATA: 0 violations of "#searches(C) ≤ n + 1" on 13 class instances and 7,500 random class games (§7).

## 2. §27b Lemma NOSTEAL-1P: SIGN
- R10's P(τ⁺) is "the union of the regions of processed tops of HIGHER index" (RESULTS R10), so τ itself is excluded. Step 1 is
  then right: a prefix top is a q-parity V-vertex with index above τ (692). Index order follows priority (O1), and q-parity
  priorities are distinct, so its priority is > pr(τ).
  - Every vertex of t has priority ≤ pr(τ): attractTangle refuses vertices above the cap (140), and CurZ grows only through
    attractVertices with max_prio = pr (74) and through the top itself.
- Step 2, entry routes into a region. There are exactly three: the top (692), attractVertices (66-108) and attractTangle
  (110-185). There is no other write to CurZ in 690-705.
  - q-vertex y (owner = player = q): attractVertices attracts y only through an in-edge from a popped region vertex, with no
    escape test. y's only successor is that vertex, which is in the region.
    - Through a tangle t″: y's stored strategy is its only edge, and attractTangle attracts all of t″.
    - Either way s(y) is in the prefix. s(y) ∈ t because t is an SCC in which q-vertices use their strategy.
  - C-vertex o: the escape test is "successor in CurR and not in CurZ" (76-85 with G = CurR). A successor outside CurR was popped
    in this round: it is in an earlier region or in the current one, and either way in P(τ⁺), since the current region belongs to
    a higher top. Otherwise it lies outside R.
    - Through t″: escapes outside Z must lie outside CurR (151-157).
    - So every R-successor of o is in the prefix, and t ⊆ R.
- Step 3: forward closure in t's SCC graph (q: unique edge; C: edges inside t) is all of t. ✓
- The proof is set-level and uses no order datum. It does not depend on the round or visit index.

## 3. §27b Corollary and §28e OUTCOME-MONO-1P
Corollary: N*_R = 0 ⇒ F_R ≤ 3·0 (R11 (c)) ⇒ R9 (c)'s bound with the per-context budget. With CTRL this gives GAP-A on 𝒞^1P
⇐ (CTX⁺). SIGN: arithmetic on signed results.
OUTCOME-MONO-1P: SIGN. Checked against 690-771:
- Region step: PREFIX-MONO-X* (R11 (b)) applies, since NOSTEAL-1P gives its no-new-steal hypothesis at every round, the repeated
  round included.
  - best_vertices adds no tangles, so the repeated round is the final round recomputed.
- Candidate test (705-716): attracts() (41-57) is monotone in Z for both owners. So a non-candidate at visit i is a
  non-candidate at i+1.
- Threshold loop (721-741): Z persists across t, and each stage runs attractVertices/attractTangles with fixed R and Gx = R, so
  1.2b applies. Hence Z_t(i) ⊆ Z_t(i+1) by induction on t.
  - Clearing a candidate at stage t uses attracts(u, Z_t), which is monotone.
  - N-OM1: the loop's `break` at the first candidate with priority ≤ t is equivalent to "check every candidate with priority > t".
    The reason: Candidates is filled in decreasing index (713-714), and index order follows priority (O1). The proof should say so.
- Hence D_{r}(i+1) ∩ V_r(i) ⊆ D_r(i), which gives (1). (2) and (3) follow as written.
- T_i ⊆ T_{i+1} holds because G′ is fixed in a phase and tangles are deleted only when they leave the game (133-134).

## 4. §33b SAME-CTX: SIGN WITH GAPS (G-SC-1, G-SC-2; both closed)
- (i) search_rec starts each call with X = ∅ (837). At depth 0, every vertex removed from R goes into X:
  - stable Dom (877-891: attractVertices into X with R[v] = false);
  - threshold piece (918-951: popped vertices are in Z, X |= Z at 951, and the opponent re-attraction at 944-948 writes into X);
  - Dom(prevV) (961-975).
  So X = G′ \ R at depth 0. Together with R9 (a), the call is a function of (R, q, T). ✓
- (ii) The outcome rises along all visits of R in the phase (OUTCOME-MONO-1P, applied transitively over the visits in between,
  at any depth).
  - G-SC-1 (definition). "σ = (ρ, |R|, |V|)" with "ρ = rank" is defined only in experiments/alg/b12_pot.py: rank = n + 2 if
    stable, the emptying round e if −1, 0 if the call returned 0. The §33b text needs ρ to include e. Otherwise two −1 outcomes
    with different e and equal |prevV| share a signature without nested prevV, and "equal |V| with V nested forces equal V" fails.
    With rank as in b12_pot.py, (ii) is correct. The definition must be in the text.
- (iii) Branch selection reads only (outcome, R, X): the attracts test and the threshold scan (898-912, test at 906) read (R, X).
  - G-SC-2 (citation). The Dom step consumes R while it runs (R[v] = false while popping, 880-889). It is also a SEQUENCE of capped
    attractors over the tops of V, a top already in X being skipped.
  - DTL-proof 1.2b as cited is stated for "consume = None". The T-monotonicity needed here is RESULTS R9 (b) (signed): "for a
    fixed tattr input I of a −1 attractor or a Dom step, the output is a triggered closure monotone in T". Cite R9 (b).
  - For the skipped tops: a top absorbed by an earlier top's attractor (cap ≥ its own) is covered by that attractor, so skipping
    loses nothing.
  - T at s ⊇ T at s′, including the tangles sptl added inside the call at s′. ✓

## 5. §35b LEX: SIGN WITH GAPS (G-LEX-1, major)
- The per-R order is a strict partial order: outcome order, then piece ⊊.
- Tree-lexicographic order: irreflexive, and transitive by the case analysis q1 < q2, q1 > q2, q1 = q2. At the deciding index the
  context R_q is common, because the states below are equal.
- Length case: if R_q agrees and one chain ends there, both end, because result 0 ⇔ R has no q-parity vertex (661-668). So a
  first difference never falls at a chain end. My checker never met that case (§7).
- G-LEX-1. The consecutive step "at p0 … so c(s) < c(s+1)" presupposes that p0 exists, i.e. c(s) ≠ c(s+1).
  - That is (CHAIN-CHANGE), which GAP-A-M §33a lists as DATA ("0 of 1,094"), L-RED R42 §3 leaves open ("survives every test
    made here"), and no reading proves.
  - Without it, an identical-chain transition gives c(s) = c(s+1), and the claim "c(s′) < c(s″) for ALL searches s′ < s″" is
    false at that pair.
  - What the proof does establish:
    - (LEX-weak) c(s′) ≤ c(s″) for all s′ < s″;
    - c(s) < c(s+1) at every chain-changing transition.
    That is all R46 §1 needs.
- DATA (§7): 0 LEX violations, 0 weak violations and 0 identical-chain transitions on every run I made.

## 6. R46: §1 SIGN, §2b SIGN, §3 SIGN WITH GAPS (G-R46-1, major)
§1 K-constraint. Let P be the first changed positions of the chain-CHANGING transitions.
- Inside a window (between consecutive transitions at positions < p), states 0..p−1 are fixed, so R_p is fixed.
- Each transition at p raises state_p strictly (LEX's consecutive step, valid because the transition changes the chain).
- Transitions at positions > p, and identical-chain transitions, leave state_p unchanged.
- Longest strict chain of the per-context order, with |R| ≤ n:
  - outcome levels ≤ n·n (−1: e ≤ n, prevV ⊊-chain ≤ n) + n (stable: V* ⊊-chain), plus the constant 0-outcome;
  - per outcome, piece ⊊-chain ≤ n.
  - So K ≤ (n² + n)·n ≤ (n + 2)²(n + 1). ✓
§2b L-NEST*: checked step by step.
- (M) holds by induction: a pair in the subsequence has a gap that is a subsequence of the gap in Q.
- Occurrences of a_j: Q_{j−1} has no symbol < a_j, and its ≤ r + j − 1 intervals of P are whole intervals of P. So the
  occurrences of a_j inside one interval lie in one window of a_j, at most K of them. ✓
- Inner segments: contiguous in Q_{j−1}, so unions of ≤ r + j − 1 intervals. They lie in a first-last gap of a_j above a_j, so
  NEST* ≤ d − 1 by (M). ✓
- Deleting the first-to-last chunk splits at most one interval: ≤ r + 1 intervals. ✓
- Sum: |Q| ≤ Σ_j o_j (1 + F_{r+m}(m, d−1)), with F monotone in r (take F as the supremum). ✓
- Unrolled: r_i ≤ 1 + i·m. Each factor m(r_i + m)K ≤ (d + 1)m²K, and the nested sum is ≤ (A + 1)^d ≤ (2A)^d. That gives
  ≤ (2(d+1)m²K)^d ≤ (2(d+2)m²K)^d. ✓
- Independent brute force (nestbf.py; my own NEST* and K-checker from the R46 text; exhaustive DFS, prefix-closed pruning).
  Maximum lengths:
  - K = 1, d = 1: 1, 3, 5, 7, 9, 11 (m = 1..6), i.e. K(2m − 1);
  - K = 2, d = 1: 2, 6, 10, 14, 18;
  - K = 3, d = 1: 3, 9, 15, 21;
  - K = 1, d = 2: 1, 3, 7, 13, 19;
  - K = 2, d = 2: 2, 8, 24;
  - K = 1, d = 3: 1, 3, 7, 15, 29.
  Every value is far below the bound, and the values equal R46's neststar.py and §2 table entries wherever they overlap.
  - The k-bit counter's first-difference sequence has NEST* = k − 1 for k ≥ 2 (k = 1 gives 1), and satisfies the K-constraint
    with K = 1 (counter.txt).
§3 THEOREM. Bound: |P| ≤ (2(d+2)(n+1)²K)^d, with m ≤ n + 1 because every non-final piece is non-empty (Dom of a non-empty V, or a
threshold seed). ✓
- G-R46-1: "S − 1 = |P|" holds only under (CHAIN-CHANGE). As proved: S − 1 = |P| + Z.
- So the exact obstruction statement is: GAP-A on 𝒞^1P ⇐ (NEST*-BOUNDED) ∧ (Z polynomial per q-phase), with (CHAIN-CHANGE)
  (Z = 0) the special case the data support.
- L-RED R44 (trunk) argues that a (CHAIN-CHANGE) violation costs only a polynomial factor: by EMPTY-REC, identical-chain
  transitions learn only in sptl at a fixed stable context, bounded by the per-context budget. That is an unrefereed reading,
  not cited in R46 and not in this packet. If it is signed later, G-R46-1 closes with it.
- The rest of §3 is consistent with signed results and CTRL: phases ≤ dominions + 2 (§21c), and C's searches ≤ n + 1.
- Measured NEST* (R46 §3, stable order) against mine (Oink order, my checker): nest3_n20 3/3, nest3_n24 3/3, onep_fdkey_n20 2/2,
  vrall_viol_n20 1/1, onep_lagdist_D8 1/1. All equal.

## 7. DATA (my probe; docs/referee-2/R2-C1P/)
- Patch r2log.patch: logging only, on a copy of 8fbf0a7 in the scratchpad. It logs the depth-0 best_vertices calls (R, result,
  emptying round, V) and the search boundaries, and R2_REV=1 reverses the ins(v) order.
- c1pcheck.py: my own analysis (written from the object texts). It splits q-phases (same player, same G′) and builds chains with
  piece_p = R_p \ R_{p+1}. It checks CTRL, CHAIN-CHANGE, LEX on all pairs, LEX-weak, the K-constraint against (n+2)²(n+1),
  NEST* and the theorem bound.
- Pinned instances (instances_oinkorder.txt; instances_revorder.txt):
  - onep_* ×8, xctx/vrall/xcov11, nest3_n20, nest3_n24;
  - up to 18 searches per phase (nest3_n24) and 153 pairs in one phase.
  - Every check: 0 violations. NEST* max 3, observed K max 13 (onep_lagdist_D8).
- R2_REV produced byte-identical depth-0 logs on every instance I compared (nest3_n24, onep_lagdist_D8, onep_vrj_n40,
  nest4_n80). So my data is effectively ONE order datum (Oink's). L-ALG's "stable" Python order was not reproduced (stated as
  skipped).
- Random class games (random_runs.txt): 7,500 games, n = 8..60, all-distinct and q-distinct priority modes, both orders.
  - 0 violations, but the q-phases are short (≤ 3 searches, 122 transitions). This calibrates nothing, as L-ALG also found.
- Not done: a LEX check on L-ALG's full 𝒞^1P set (forced library conversions), and climbs against (CHAIN-CHANGE). Both were done
  by the lanes (b12_lexchk.py, chainchg.py) and are not repeated here.

## 8. Summary for the Lead
- Signed: CTRL, NOSTEAL-1P, the §27b corollary, OUTCOME-MONO-1P, SAME-CTX (G-SC-1/2 closed), R46 §1 and §2b.
- Signed with a MAJOR gap: LEX and R46 §3. Both need (CHAIN-CHANGE), which is DATA only (no violation known: lanes 0/1,094 and
  0/5,566; mine 0/~250).
- Correct form of the obstruction statement: GAP-A on 𝒞^1P ⇐ (NEST*-BOUNDED) ∧ (Z poly), where Z = identical-chain
  transitions per q-phase. Candidate routes for the second conjunct: prove (CHAIN-CHANGE) on 𝒞^1P, or get R44's EMPTY-REC
  budget argument refereed.

## 9. §C: comparison with REFEREE's R-C1P (read 01:40Z by date -u, after my report was pushed at 1ecc8d56/b666c4a9)
Read: docs/referee/R-C1P.md at claude/referee 3061415 (merged into trunk per the Lead). Both reports: same pin 01d63d7, same pinned
dtl.cpp, all labelled (Opus 5.5, D12).
| item | REFEREE R-C1P | mine (R2-C1P) | comparison |
| --- | --- | --- | --- |
| CTRL | SIGN | SIGN | agree; both read 1068, 1106-1121 / dtl.hpp 33, and escapes in the member G |
| NOSTEAL-1P | SIGN (N-1 wording: "earlier region of round r at visit i + 1") | SIGN | agree. I accept N-1: it is the same "popped earlier in this round = in the prefix or in the current higher region" point I spelled out in §2. REFEREE adds that the proof holds for ANY two region computations of one context; I agree (it uses neither i < i+1 nor T ⊆ T′) |
| §27b corollary | not separately tabulated | SIGN | no conflict |
| OUTCOME-MONO-1P | SIGN WITH GAPS O-1 (e = FIRST round with V_e = ∅), O-2 (T_i ⊆ T_{i+1} via R5 (g)) | SIGN, note N-OM1 (break relies on index = priority order) | agree. O-1 is a convention point I did not raise; I accept it (my K count used e ≤ n, consistent with either convention). N-OM1 = REFEREE's "the scan reaches u … break at the first uncleared candidate with priority ≤ t" |
| SAME-CTX | SIGN WITH GAPS S-1 (ρ undefined in text), S-2 (sptl's W guard), S-3 (G′ fixed, R5 (g)) | SIGN WITH GAPS G-SC-1 (= S-1), G-SC-2 (cite R9 (b) for Dom/−1 T-monotonicity) | agree in substance. S-2 is a point I did not raise (W is per search, so s and s′ may extract different tangles; harmless because T only grows); I accept it. Citation difference: REFEREE cites 1.2b for the Dom pieces; I asked for R9 (b) because the Dom step consumes R (R[v] = false while popping), and 1.2b is stated for consume = None. R9 (b) is signed and states exactly the needed fact, so either way the step holds; I keep G-SC-2 as a citation note |
| LEX | SIGN WITH GAPS L-1 (OPEN): strict all-pairs form needs (CHAIN-CHANGE); proved: ≤ for all pairs, < at chain-changing transitions | G-LEX-1 (MAJOR): identical | agree exactly |
| R46 §1 | SIGN; L-1 does not affect it | SIGN; same reason | agree. K count: REFEREE (n+1)(n+1)+(n+1)+1 outcomes × (n+2) pieces; mine (n²+n)·n; both ≤ (n+2)²(n+1) |
| R46 §2b | SIGN (R-1: define F_r as a supremum; d = 0 ⇔ Q = ∅) | SIGN (I used F as the supremum, monotone in r) | agree; R-1 is the wording I assumed |
| R46 §3 | SIGN WITH GAPS R-2 (OPEN): S − 1 = \|P\| + I | G-R46-1 (MAJOR): S − 1 = \|P\| + Z | agree exactly (I = Z) |
| Route for the open gap | GAP-A-M §36c with R9 (a)/(c), F_R = 0 (recorded, not checked) | R44's EMPTY-REC budget argument (recorded, not checked) | the same route from two citations; the Lead has routed it to L-RED as R47 |
| DATA | L-ALG's tools at the pin (samectx 646 pairs, lexchk 169 pairs both orders), neststar.py K=2 d=2 | my own C++ logging patch + analyser (13 class instances, Oink order; R2_REV identical), my own nestbf.py | complementary: REFEREE ran the lanes' tools with the stable order; I ran independent code on the C++ (one effective order). Both 0 violations. nestbf.py and REFEREE's neststar run agree (K = 2, d = 2: 2, 8, 24) |
Do REFEREE's gaps change my verdicts? No. N-1, O-1, O-2, S-2, S-3, R-1 are wording/citation points, all closed, and none touches a
proof step I signed. L-1 / R-2 are my G-LEX-1 / G-R46-1.
Joint position: CTRL, NOSTEAL-1P, OUTCOME-MONO-1P, SAME-CTX, R46 §1 and §2b have two signatures (gaps closed). LEX (strict form)
and R46 §3 (S − 1 = |P|) have two signatures WITH the open gap (CHAIN-CHANGE) / (chain-keeping transitions polynomial per phase),
now routed to L-RED R47. Open named statements on 𝒞^1P: (NEST*-BOUNDED) and that gap.

## A1. Addendum: L-RED R47 (Theorem CK, chain-keeping transitions). REFEREE-2, 2026-10-19 02:08Z (date -u, writing start)
Signature: (Opus 5.5, D12).
- Object: docs/red/R47-chainkeep.md at trunk da63c40 (L-RED b9d7580), against pinned dtl.cpp @ 8fbf0a7.
- I did not read docs/referee/ on R47 before pushing this section.
- Signed inputs it uses: R5 (h) FDL, R8 STR-DET, R7 (d), R9 (a)-(b), R11 (c), and P-C1P's NOSTEAL-1P (two signatures).

### Verdicts (Opus 5.5, D12)
| item | verdict |
| --- | --- |
| §1 Lemma EMPTY-REC | SIGN (note A1-N1) |
| §2 (i) e* is not the −1 threshold attractor at a chain-keeping transition | SIGN |
| §2 (ii) Lemma DOM-MONO and its budget n·\|V\| | SIGN WITH GAPS: A1-G1 (an unneeded hypothesis; closed) |
| §3 Lemma SPTL-SANDWICH | SIGN WITH GAPS: A1-G2 (citation for T-monotonicity under consumption; closed) |
| §4 Theorem CK, I ≤ (n+1)(\|P\|+1)(H+1+n²) + 1 | SIGN (note A1-N2 on the "+1" case) |
| §5 consequence | SIGN. It closes my G-R46-1: GAP-A on 𝒞^1P ⇐ (NEST*-BOUNDED) alone. A1-N3: R47 quotes K = (n+3)(n+1)², R46 (n+2)²(n+1). Both are polynomial; immaterial |

### §1 EMPTY-REC (dtl.cpp 896-955): SIGN
- (a) Seeds. The scan at 899-911 runs in increasing index, which is priority order (O1). t is raised only while Q is empty, and the
  scan breaks at the first higher priority once Q is nonempty (902-904). So all seeds have priority exactly t. ✓
- (b) Every vertex of Z has a path inside Z to a seed.
  - attractVertices(q, u, R, Z, R, t) adds predecessors of the popped u. A q-vertex (owner = pl) is added because its unique
    edge goes to u. A C-vertex is added only with an edge to u. ✓
  - attractTangles is triggered only through tin[u], the tangles that have u as an escape target (443: tin is filled from
    tangleto). tangleto holds the targets of non-pl (C) edges of the tangle (329-338).
  - So an attracted tangle has a C-vertex with an edge to u ∈ Z. Every vertex of the tangle reaches that C-vertex inside the
    tangle: q-vertices by their stored strategy (their unique edge), C-vertices by internal edges. ✓
- (c) 935-940 move all priority-t vertices of Z (the seeds among them) to X and push them. 942-946 run
  attractVertices(1 − q, u, Z, X, Z, t), with Z[u] = false at each pop.
  - A C-vertex predecessor (owner = 1 − q = pl here) is added at once.
  - A q-vertex predecessor (opponent) has its only successor u already removed from G = Z, so it has no escape.
  - The cap t is no restriction (Z ⊆ priority ≤ t, from cap t at 916-921 and seeds of priority t).
  - By (b) the backward closure is all of Z, so Z = ∅ at 954. search_rec(∅) gets best_vertices → 0 (668) and returns at 854. ✓
- A1-N1 (wording). (b) should name the trigger fact (tin = escape targets, line 443) explicitly. The proof uses it.

### §2 (i): SIGN
- At a chain-keeping transition, suppose e* = the threshold attractor (916-921) at position j. FDL gives the same input (seeds,
  R_j, t, X) and a strictly larger output Z.
- All of Z leaves R_j in this iteration: R[u] = false at 920. The priority-t vertices and the 1−q-attracted vertices go to X;
  X |= Z at 951; nothing returns to R.
- So piece_j = Z grows, and the chain changes. Contradiction. ✓

### §2 (ii) DOM-MONO: SIGN WITH GAPS (A1-G1)
I re-derived the induction on the join order under T, across steps.
- Vertex rule: v ∈ R_j joined at step i under T. Every R-successor of a C-vertex v (the unique successor of a q-vertex) is in
  X_i(T), and none is in X_0 = G′ \ R_j. By induction, all of them are in X′_i \ X_0, so they joined under T′ during the call by
  step i, and were popped (every joiner is pushed: the top, 88-90, 170-172).
  - At the LAST of those pops (step k ≤ i, cap c_k ≥ c_i ≥ pr(v)), attractVertices examines v. It is not yet in X′ (or we are
    done), still in the current R, and has no R-successor outside X′. So v joins. ✓
- Tangle rule: the same argument on t's escapes inside R_j. There is at least one, because the trigger under T was a popped
  escape, which lies in R_j. t's other vertices are in X′ or in the current R, the cap holds, and t ∈ T ⊆ T′ is not deleted
  (G′ is fixed). ✓
- Tops: τ_i ∈ X′_{i−1}, or it is processed at step i under T′ (skip test `V[top] and !X[top]`). ✓
- The budget: a fixed Dom input (R, V) also fixes X_0 = G′ \ R (depth 0, my R2-C1P §4). Each X_i is a ⊆-chain over the phase
  and strictly grows at a Dom-e* transition (FDL). So there are ≤ |R|·|V| ≤ n² such transitions. ✓
- A1-G1 (closed). The proof needs only that the caps c_1 ≥ c_2 ≥ … are non-increasing along the loop. That holds by index order =
  priority order (O1) without "distinct q-priorities". The class hypothesis is harmless but not used here.
- R47's own remark is right: monotone step outputs do not give a strictly larger final piece. Hence a budget, not an exclusion.

### §3 SPTL-SANDWICH: SIGN WITH GAPS (A1-G2)
- (a) Line-by-line identification:
  - BV's final round (returns at 716 or 765-767; V = V* in both cases) and sptl pass 1 (481-499, called with a COPY of R at 871)
    process the same tops of V* in the same decreasing order.
  - Each uses a per-top target (BV: CurZ, reset per top at 704; sptl: member Z, reset at 542), cap priority(top), and a subgame
    consumed by all earlier regions of the round/pass (BV: CurR at 699; sptl: R at 490).
  - The skip tests agree: BV skips `Z[top]` (in an earlier region = popped); sptl skips `!R[top]` (popped). ✓
  - closed_region / W affect only extraction (512-541), not regions. ✓
- (b) The tangle sets T^j_s ⊆ T^j_s ∪ L_k ⊆ T_{s+1}: L_k is learned during s, T only grows in a phase, and s + 1 learns nothing
  before e*. ✓
- (c) The induction over k, with f_k monotone in T at a fixed input, sandwiches SP_s(a_k) between equal values. So no SP region of
  pass 1 differs. A pass ≥ 2 of s + 1 needs earlier learning in s + 1, which FDL excludes before e*. ✓
- A1-G2 (closed). f_k runs on a consumed subgame (R[v] = false while popping). 1.2b as cited is stated for consume = None. The
  needed fact is the signed R10 (a) EXACT (a region step is a triggered closure) with its T-monotonicity, as in R9 (b). This is the
  same citation point as my G-SC-2.

### §4 Theorem CK: SIGN
- (1) Identical logs: every extraction of s + 1 repeats one of s, and duplicates are skipped and not counted (CHECK_UNIQUE = 1,
  line 23; 383-416).
  - A dominion found at s would have ended the phase.
  - So s + 1 returns false (1068) and ends q's block: at most once per phase.
  - A1-N2: "once per phase" is in fact once per player block, because a false search ends the non-interleaved block (run()
    1106-1120). That only strengthens the "+1".
- (2) EMPTY-REC ⇒ e* at depth 0 at a common position j. §2 (i) and §3 exclude the threshold attractor and sptl. The opponent
  pass 942-946 is a function of Z, and the post-search dominion attractor (1018-1038) runs only if a dominion was found. So e*
  is in BV at R_j or in a Dom step with input (R_j, V_j). ✓
- (3) Budgets: e*-at-R ≤ (F_R + 1)(H + 1) = H + 1 (R9 (a); F_R = 0 by R11 (c) + NOSTEAL-1P); Dom ≤ n² per input. ✓
- (4) ≤ |P| + 1 maximal constant-chain blocks, hence ≤ |P| + 1 distinct chains. Each has ≤ n + 1 positions, because every
  non-final piece is nonempty:
  - stable: the first top of V* ⊆ R is not in X = G′ \ R, so it joins;
  - −1 with seeds: Z ⊇ seeds;
  - −1 without seeds: Dom(prevV), prevV ≠ ∅;
  - the final call returns 0.
  ✓ (The same fact I used for R46 §3.)
- (5) The sum is correct. ✓

### DATA (my own code on the pinned C++; docs/referee-2/R2-C1P/)
- r2log_a1.patch = r2log.patch plus "D top : X" before every V-top of both depth-0 Dom loops. a1check.py checks, per q-phase:
  DOM-MONO (the step-output vector of every Dom input seen in several searches is ⊆-monotone) and I against the CK bound with
  H = 0 (stricter than CK).
- 13 pinned class instances, 15 q-phases: I = 0 everywhere (|P| total 79); 0 bound violations.
- DOM-MONO: 163 same-input Dom pairs, 0 violations (a1_instances.txt).
- VACUITY (a1_control.txt): in all 163 pairs the step vector is IDENTICAL. So the DOM-MONO data is non-informative on these
  instances: no Dom input ever changed its output. This is consistent with GAP-A-M §22e ("e* never in sptl or Dom"), but it tests
  nothing. The verdict rests on the proof.
- EMPTY-REC: not re-measured (my log is depth-0 only); R42's 98/98 stands as the lanes' DATA.

### Net effect on P-C1P (Opus 5.5, D12)
- G-R46-1 / G-LEX-1 is replaced: S − 1 = |P| + I with I ≤ (n+1)(|P|+1)(H+1+n²) + 1.
- So, on the signed chain CTRL → NOSTEAL-1P → OUTCOME-MONO-1P → SAME-CTX → LEX(chain-changing) → K-constraint → L-NEST* → CK:
  GAP-A on 𝒞^1P ⇐ (NEST*-BOUNDED), one named statement. LEX's strict all-pairs form still needs (CHAIN-CHANGE), but nothing uses
  that form any more.

### §C-A1: comparison with REFEREE's A1 (docs/referee/R-C1P.md §A1, claude/referee 640ffae0; read after my A1 was pushed at 8e7a02c2)
Both: R47 SIGNED (Opus 5.5, D12), gaps closed, GAP-A on 𝒞^1P ⇐ (NEST*-BOUNDED). Item by item:
| item | REFEREE | mine | comparison |
| --- | --- | --- | --- |
| EMPTY-REC | SIGN | SIGN (A1-N1: name the tin = escape-target trigger, 443) | agree |
| §2 (i) | SIGN | SIGN | agree |
| DOM-MONO | SIGN, A1-3: only non-increasing caps used | SIGN WITH GAPS, A1-G1: the same point | agree (A1-3 = A1-G1) |
| SPTL-SANDWICH | A1-1: stable stop also at 765 | A1-G2: cite R10 (a)/R9 (b) under consumption; I already used both stops (716 and 765-767, V = V*) | agree. A1-1 is covered in my text; A1-G2 is a citation point REFEREE did not raise. It does not change the verdict |
| CK (1), CHECK_UNIQUE | A1-2: R47 must cite dtl.cpp 23 | I cited line 23 and 383-416 | agree (A1-2 is a request to R47; my check already rests on line 23) |
| CK (2), e* location | A1-5: search()'s dominion attractor (1032-1037) must be excluded; it is, by STR-DET: equal search_rec tattrs ⇒ equal extractions ⇒ no dominion at s+1 | I wrote "runs only if a dominion was found", WITHOUT showing that s+1 finds none | ACCEPT A1-5. Theirs is the complete argument: my sentence silently needed R8 STR-DET (identical tattrs ⇒ identical extractions, so s+1 finds a dominion only if s did, and s found none inside the phase). With A1-5 the case analysis of (2) is exhaustive |
| CK (3)-(5) | SIGN | SIGN | agree (both: R9 (a) original constants given R8, F_R = 0) |
| §5, K | A1-4: use R46's K ≤ (n+2)²(n+1); R47's (n+3)(n+1)² is SMALLER and unproved | A1-N3: "both polynomial; immaterial" | ACCEPT A1-4, and I withdraw "immaterial" as wording. (n+3)(n+1)² = (n+1)(n²+4n+3) < (n+1)(n²+4n+4) = (n+2)²(n+1). So R47's constant is a strict understatement with no proof, and the stated bound must use R46's signed K. The conclusion (polynomial) is unchanged |
Do REFEREE's gaps change my verdict? No: A1-1..A1-5 are closed wording or citation points, and A1-4 / A1-5 are now in my record as
above. Joint position: R47 Theorem CK has two signatures, with R46's K. The P-C1P chain gives
GAP-A on 𝒞^1P ⇐ (NEST*-BOUNDED), one named statement.
