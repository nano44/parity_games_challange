# R2-C1P: second-referee check of the 𝒞^1P chain (CTRL, NOSTEAL-1P, OUTCOME-MONO-1P, SAME-CTX, LEX, R46 NEST*-BOUND). REFEREE-2, 2026-10-19 01:40Z (date -u)
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
