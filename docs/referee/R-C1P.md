# Referee report R-C1P: the 𝒞^1P chain (CTRL, NOSTEAL-1P, OUTCOME-MONO-1P, SAME-CTX, LEX) and R46 NEST*-BOUND

Referee: REFEREE (successor 2), running on Opus 5.5 under owner ruling D12 (Lead reading L33). Packet P-C1P: the Lead's message of
01:14Z (2026-10-19). Pin: trunk 01d63d7 (objects unchanged at my merge of trunk). Objects: docs/alg/GAP-A-M.md §27b (class,
CTRL, NOSTEAL-1P), §28e (OUTCOME-MONO-1P), §33b (SAME-CTX), §35b (LEX); docs/red/R46-nest-bound.md §1, §2b, §3.
Code: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7; I built Oink with scripts/setup_oink.sh, and "N" means
tools/oink/src/src/solvers/dtl.cpp line N at that commit. Signed results used: R5 (g) phases ≤ D + 2 and DTL-proof Lemma 1.2/1.2b,
R8 STR-DET, R9 (a), R11 (b) PREFIX-MONO-X*. Written 01:15Z-01:33Z (date -u). docs/referee-2/ was not read.

## Verdict
| item | verdict (Opus 5.5, D12) |
|---|---|
| §27b class 𝒞_C, 𝒞_C^dist, 𝒞^1P | definitions fine (a property of the game). Oink sorts vertices by priority (game.cpp Game::sort; oink.cpp 35 ensure_sorted), and order data only permute ties (DTL-proof §0 O1), so "index above τ and q-parity ⇒ priority > pr(τ)" holds on 𝒞_C^dist |
| Lemma CTRL | SIGN |
| Lemma NOSTEAL-1P | SIGN (gap N-1 wording; closed) |
| Lemma OUTCOME-MONO-1P | SIGN WITH GAPS: O-1 (the index convention for e; closed), O-2 (T_i ⊆ T_{i+1} is needed only for tangles ⊆ R; closed) |
| Lemma SAME-CTX | SIGN WITH GAPS: S-1 (ρ must be defined in the text: n + 2 stable, e for −1, 0 for result 0; closed), S-2 (sptl's W guard: (iii) needs "every tangle sptl adds at s′ is in T at s", which holds; closed), S-3 ("function of (R, T)" holds because G′ is fixed in a phase, R5 (g); closed) |
| Lemma LEX | SIGN WITH GAPS: L-1 (OPEN as stated). The strict "c(s′) < c(s″) for ALL s′ < s″" presupposes that every transition changes the depth-0 chain, which is (CHAIN-CHANGE) (DATA only, §33a). PROVED: c(s) < c(s+1) at every chain-changing transition, so c(s′) ≤ c(s″) for all s′ < s″, with < as soon as a chain-changing transition lies between them |
| R46 §1 (K-constraint) | SIGN. It uses LEX only at chain-changing transitions, so L-1 does not affect it |
| R46 §2b (L-NEST*) | SIGN (gap R-1 wording; closed) |
| R46 §3 THEOREM (NEST*-BOUND) | SIGN WITH GAPS: R-2 (OPEN). "S − 1 = |P|" is (CHAIN-CHANGE). Proved form: S − 1 = |P| + I, with I the number of transitions that keep the depth-0 chain, and |P| ≤ (2(d + 2)(n + 1)²K)^d. So GAP-A on 𝒞^1P ⇐ (NEST*-BOUNDED) ∧ (I polynomial per phase). (CHAIN-CHANGE) gives I = 0; DATA: 0 of 1,094 class transitions keep the chain (§33a) |
| Overall | The chain CTRL → NOSTEAL-1P → OUTCOME-MONO-1P → SAME-CTX → LEX(chain-changing) → K-constraint → L-NEST* is correct. The theorem's last step needs (CHAIN-CHANGE) or a bound on I. That is a second named statement next to (NEST*-BOUNDED). DATA supports it, but it is not proved |

## (1) §27b
Lemma CTRL. Checked against the code.
- run() (1106-1121, non-interleaved, dtl.hpp 33 `interleaved = false`): one block of search(0), then one of search(1).
- In search(C), tangles are created only by extractTangles (sptl 539). pl = priority(top) & 1 (215), and tops are V-vertices,
  i.e. C-parity (best_vertices 663). So every extracted SCC is a C-tangle.
- The SCC graph uses outs ∩ R for non-pl vertices (234-266). In 𝒞_C a q-vertex in a nontrivial SCC has its only successor in the
  SCC. A one-vertex SCC needs str[n] = n or a self-loop (315-317).
- Escapes are computed only over non-pl vertices of the SCC (329-338), so tangleto is empty and the SCC is a dominion (347-378).
- search returns tangles != T or dominions != D (1068). Only dominions can change, and a found dominion's new vertices (S false,
  368-373) are solved and removed (1023-1038). So each true search removes ≥ 1 vertex, and C makes ≤ n true searches plus one
  false. ✓
- The class survives removal: a q-vertex whose only successor is removed is attracted by the removal attractor (1036), for either
  owner (owner = player: no escape test; owner ≠ player: its only G-edge is gone). So every q-vertex of the current G keeps its
  unique successor. ✓
- (The LOGIC_ERROR at 352-355 for a dominion at depth > 0 runs only under `trace`.)
Lemma NOSTEAL-1P. Setting: t ∈ F_τ fired at τ's region step (round r, visit i) of a q-call (V = q-parity vertices, 663), so t is a
q-tangle (attractTangle parity test). A := t ∩ P_{i+1}(τ⁺) ≠ ∅.
1. Every vertex of t has priority ≤ pr(τ). The not-yet-in-CurZ vertices pass 140 with max_prio = pr(τ). CurZ itself holds only τ
   and vertices attracted with cap pr(τ) (74, 140). The other vertices must lie in CurR (138-139). Tops of P_{i+1}(τ⁺) are
   q-parity V-vertices with index > τ (691-692). Vertices are sorted by priority, and q-parity priorities are distinct, so these
   tops have priority > pr(τ). So no vertex of t is such a top. ✓ (This holds whatever the owner of the vertex.)
2. A is forward-closed in t's SCC graph. A non-top vertex enters a region at 700 (attractVertices) or 701 (attractTangle).
   - q-vertex y (the tangle player's vertex). Via 69-90 with owner = pl: y has an edge to the popped v, so v = s(y), which is in
     the region. Via attractTangle(t″): str[y] := t″'s strategy, which lies in t″ (a pl-vertex's only SCC edge is its str), and
     all of t″ ends in the region. Either way s(y) ∈ prefix, and s(y) ∈ t (y's only edge; t is an SCC). ✓
   - C-vertex o. Via 75-85: no successor in CurR \ CurZ (G = CurR at 700). A successor outside CurR was popped earlier in this
     round (699), i.e. it lies in an earlier region of the prefix. Successors of o in t lie in R, because t ⊆ CurZ ∪ CurR ⊆ R at
     visit i (138). Via attractTangle(t″): every escape of t″ is in CurZ or outside CurR (152-157). tout was computed against
     this->G at t″'s extraction (333), and G only shrinks, so every current successor of o outside t″ is in tout. ✓
3. t is strongly connected under these edges (q: str = the unique successor; C: the region edges at extraction). So the forward
   closure of A is t, and t ⊆ P_{i+1}(τ⁺). ✓
N-1 (wording, closed). In step 2, "a successor outside CurR was popped earlier in round r" should say "in an earlier region of
round r at visit i + 1 (the prefix before τ)". CurR is reset per round (690).
The proof does not use i < i + 1 or T ⊆ T′. It holds for any two region computations of one context in 𝒞_C^dist. OUTCOME-MONO-1P
uses this for the repeated last round.

## (2) §28e OUTCOME-MONO-1P
(1), by induction on r:
- Base: V_1 is the q-parity vertices of R at both visits (661-667). ✓
- Region steps. NOSTEAL-1P gives (NS*). V_r(i) ⊆ V_r(i+1) is the hypothesis. T ⊆ T′ holds for every tangle that best_vertices can
  use, since its tangles must lie in CurZ ∪ CurR ⊆ R (138), and R ⊆ G′. So PREFIX-MONO-X* (R11 (b)) gives
  P_r^i(τ) ⊆ P_r^{i+1}(τ) and U_r(i) ⊆ U_r(i+1). ✓
  O-2 (closed): within a phase G′ is fixed (R5 (g): a phase ends with the dominion-finding search), so no tangle meeting G′ is
  deleted (132-135). The text's "T_i ⊆ T_{i+1}" is true as stated.
- Candidate test (712-716). attracts (41-57) is monotone in Z: an owned vertex needs one edge into Z; an opponent vertex needs no
  R-edge outside Z and one edge into Z. So candidates at i + 1 that lie in V_r(i) are candidates at i. ✓
- Threshold loop (721-741). Z_t is cumulative (724 pushes all of Z), and each stage is a capped tattr, monotone in Z and T
  (Lemma 1.2/1.2b). For a candidate u with pr(u) > t, the scan reaches u, because Candidates is in decreasing index order and the
  break (737) is at the first uncleared candidate with priority ≤ t. So "cleared at i ⇒ cleared at i + 1". ✓
- Hence D_r(i+1) ∩ V_r(i) ⊆ D_r(i) and V_{r+1}(i) ⊆ V_{r+1}(i+1). ✓
- The conventions (repeated stable round; V_r = ∅ after emptying) are consistent with the code: a repeated round with input V*
  recomputes D = ∅, and the emptying round has D_e = V_e.
(2) V*_i ≠ ∅: round 1 has V ≠ ∅ (668), and a stable stop happens before any emptying. V_r(i+1) ⊇ V_r(i) ⊇ V*_i for all r, so
    visit i + 1 never empties, and V shrinks strictly in every non-stable round. ✓
(3) ✓, given O-1.
O-1 (closed). In (3) "emptying round e" must mean the FIRST round index with V_e = ∅ (so prevV = V_{e−1}, 676, 768-771). The proof's
"V_e(i) ⊆ V_e(i+1) = ∅" and "prevV_i = V_{e−1}(i)" use that convention. Read as "the round in which V empties", the indices are
off by one. The statement is unaffected.
Count: at most |R|(|R| + 1) + |R| + 1 outcome changes per context and phase: ✓ (a chain in the order: e ≤ |R| + 1, prevV a ⊆-chain
for each e, then stable, then a V* ⊆-chain).

## (3) §33b SAME-CTX
(i):
- At depth 0, X starts empty (search_rec, 837), and every removal from R goes into X. Stable branch: 878-890 (R[v] = false and X).
  Threshold branch: R[u] = false at 920, then X |= Z at 951; the 936-948 opponent step moves vertices from Z to X, so the union
  is unchanged. Else branch: 962-975. sptl works on a copy (871).
- So X = G′ \ R, and G′ is fixed in a phase (S-3, from R5 (g)). best_vertices reads (R, q, T) (R9 (a)); it reads str only at 73
  (R8). ✓
(ii):
- OUTCOME-MONO-1P chains over every visit of the set R between s′ and s, at any depth. ✓
- "Equal signature ⇒ equal outcome": with ρ = n + 2 (stable) / e (−1) / 0, equal ρ and equal |V| for ⊆-nested V give V equal. ✓
- S-1 (closed): §33 never defines ρ in the text. The definition is in experiments/alg/b12_pot.py lines 3-4 and in §36a. §33b
  needs ρ to carry e; otherwise two −1 outcomes with different e and equal |prevV| need not have nested prevV.
(iii):
- The branch and its seeds are fixed by (outcome, R, X). The threshold seed test (898-912) uses attracts(q, v, X, R), with no T.
- The piece is a capped tattr from those seeds: the Dom pieces with cap pr(top) per top (878-890, 962-975), the threshold piece
  with cap t (918-923). By 1.2b it is monotone in T.
- S-2 (closed): the stable branch runs sptl first (869-874), and sptl only extracts at tops not in W (528). W is per search
  (1016), so s and s′ may extract different tangles. Every tangle extracted at s′ (inside the call or before it) is stored and
  never deleted in the phase, so T at the Dom step of s ⊇ T at the Dom step of s′. ✓
SIGN WITH GAPS (S-1..S-3 closed).

## (4) §35b LEX
- Consecutive searches with c(s) ≠ c(s+1): p0 exists. R_{p0} agrees, because R_{p0} = G′ minus the earlier pieces and G′ is
  fixed in the phase.
  - Outcome changed: it rose (OUTCOME-MONO-1P, a partial order, so changed ⇒ strictly greater).
  - Outcome equal: the piece changed and grew (SAME-CTX (iii)).
  So c(s) < c(s+1). ✓
- The tree-lexicographic order is a strict partial order (irreflexive; transitive in the cases q1 < q2, q1 > q2 and q1 = q2). ✓
- L-1 (OPEN as stated). If c(s) = c(s+1), LEX gives no p0 and the proof does not apply. The statement "c(s′) < c(s″) for ALL
  s′ < s″" then fails at that pair. This is exactly (CHAIN-CHANGE), DATA only (§33a: 0 of 1,094 class transitions keep the chain;
  false in two-player games).
  - Such a transition is possible in principle on 𝒞^1P. Search s learns a tangle in sptl at a stable position (the only place on
    𝒞^1P if EMPTY-REC holds) that changes no depth-0 outcome or piece at s + 1. No argument in the packet excludes it.
  - Proved form: c(s′) ≤ c(s″) for all s′ < s″, and c(s) < c(s+1) at every chain-changing transition.

## (5) R46
§1, the K-constraint:
- Inside a window (between consecutive transitions at positions < p), states < p are fixed, so R_p is fixed.
- A transition at p is chain-changing with p0 = p, so state_p strictly rises (LEX at that transition; L-1 does not matter).
- Transitions at positions > p leave state_p unchanged, and transitions that keep the chain leave every state unchanged. So the
  number of p-transitions in the window is ≤ the longest chain of the per-context order.
- K ≤ (n + 2)²(n + 1): outcomes ≤ (n + 1)·(n + 1) + (n + 1) + 1 (the −1 levels, the stable V*-chain, and result 0), times
  ≤ n + 2 piece sizes. ✓
§2b, L-NEST*. Re-derived step by step:
- (M) monotonicity of NEST* under subsequences ✓ (with the first-last pair, any pair's gap lies inside it).
- o_j ≤ (r + j − 1)K: each of the ≤ r + j − 1 pieces is an interval of P, with no symbol smaller than a_j, so it lies inside one
  window of a_j. ✓
- Inner segments: symbols > a_j, NEST* ≤ d − 1 by (M) and the definition, and unions of ≤ r + m intervals. ✓
- Deleting the chunk [first, last occurrence of a_j] keeps "union of intervals of P", count +1. ✓
- Sum ≤ m(r + m)K(1 + F_{r+m}(m, d − 1)). Unrolled with r ≤ (d + 1)m and A := (d + 2)m²K ≥ 1: F ≤ A(1 + F′) ≤ (2A)^d by
  induction. ✓
- R-1 (wording, closed): F_r should be defined as the supremum over all Q with ≤ r intervals (so that F is monotone in r, which
  the step "≤ r + j − 1 ≤ r + m" uses), and d = 0 ⇔ Q = ∅ should be said.
§3, THEOREM:
- m ≤ n + 1 (every depth-0 call removes ≥ 1 vertex, plus the final result-0 call). ✓
- |P| ≤ (2(d + 2)(n + 1)²K)^d by §1 and §2b. ✓
- R-2 (OPEN). "S − 1 = |P|" needs every transition of the phase to have a first changed depth-0 position, i.e. (CHAIN-CHANGE)
  (L-1). What is proved: S − 1 = |P| + I, where I counts the chain-keeping transitions. So the theorem holds as stated given
  (CHAIN-CHANGE), and in general with "+ I".
  - A route to bound I exists in the record (GAP-A-M §36c): differences inside sptl at a stable context of a fixed tree, R9 (a)
    per-context budget 2(F_R + 1)(H + 1), F_R = 0 on 𝒞^1P by NOSTEAL-1P and R11 (c). It is not written for R46 and I did not
    check it. As a referee I record it, I do not supply it.
- The step "phases ≤ D + 2 (R5 (g)) and CTRL ⇒ GAP-A on 𝒞^1P" ✓, given a per-phase polynomial bound.
- EMPTY-REC (R42 §2) is listed as an input but is not used in §1-§3. Nothing depends on it here.

## Tools run (DATA; the verdicts are on the proofs)
Run by me at the pin, on experiments/alg/instances/onep_*.pg (forced into the class, DIST=1, 3 trials):
- b12_core.py MODE=samectx, stable: 646 same-set same-signature pairs; V differs 0; piece not ⊆ 0.
- b12_lexchk.py: 169 pairs s′ < s″ per order (stable and Oink); 0 LEX violations.
- neststar.py check 2 2 5 40 (K = 2, d = 2): maxima 2, 8, 24 at m = 1, 2, 3 against the bound (2(d + 2)m²K)^d = 256, 4,096, 20,736:
  OK. The m = 4, 5 cases had not finished at writing.
These agree with L-ALG's and L-RED's larger runs (26,155 SAME-CTX pairs, 4,718 LEX pairs). They test the statements on short
phases only, and they do not test (CHAIN-CHANGE) beyond §33a's count.

## Gaps (for GAPS.md)
- L-1 / R-2 (OPEN): (CHAIN-CHANGE), or a polynomial bound on chain-keeping transitions per phase. Needed for LEX's strict
  all-pairs form and for R46's S − 1 = |P|. DATA: 0 / 1,094 (§33a).
- N-1, O-1, O-2, S-1, S-2, S-3, R-1: wording or citation; closed here.
- Named statement left open by R46 (unchanged): (NEST*-BOUNDED).

## §C. Comparison with REFEREE-2 (R2-C1P.md, trunk / referee-2 b666c4a, read 01:39Z by date -u, AFTER my report was pushed at 3061415)
Same verdicts in substance, item by item. Both are labelled (Opus 5.5, D12), and both re-read dtl.cpp @ 8fbf0a7 independently.
| item | R-C1P (me) | R2-C1P | comparison |
|---|---|---|---|
| CTRL | SIGN | SIGN | agree (same lines: 215/663, 329-338, 347-378, 1023-1038, 1068; their DATA 7,500 random class games) |
| NOSTEAL-1P | SIGN (N-1 wording) | SIGN | agree. R2 makes explicit that P(τ⁺) excludes τ (R10's definition), which my step 1 uses implicitly |
| §27b Corollary | not itemised | SIGN (arithmetic on R9 (c), R11 (c)) | agree on reading: N*_R = 0 ⇒ F_R ≤ 3·0 ⇒ R9 (c). Not a separate signature of mine |
| OUTCOME-MONO-1P | SIGN WITH GAPS (O-1 e-convention, O-2 T ⊆ T′; closed) | SIGN (N-OM1: the break at 737 relies on decreasing index = decreasing priority) | agree. N-OM1 is the same point as my threshold-loop paragraph. O-1 (e = the first round with V_e = ∅) is mine only; R2 does not flag it, and it is wording |
| SAME-CTX | SIGN WITH GAPS (S-1 ρ undefined, S-2 W guard, S-3 G′ fixed; closed) | SIGN WITH GAPS (G-SC-1 = my S-1; G-SC-2 citation) | ACCEPT G-SC-2. The Dom step consumes R while it runs (880-889) and is a sequence of capped attractors with skipped tops, so the T-monotonicity is RESULTS R9 (b) (signed), not DTL-proof 1.2b as I cited (1.2b is stated for consume = None). I correct my (iii): cite R9 (b). R2's skipped-top remark (a top absorbed earlier is covered by that attractor) is correct. My S-2 = R2's "including the tangles sptl added inside the call at s′" |
| LEX | SIGN WITH GAPS (L-1 OPEN = (CHAIN-CHANGE)) | SIGN WITH GAPS (G-LEX-1 major, same) | agree. L-1 = G-LEX-1; "LEX-weak" = my proved form. R2 adds the length case: result 0 ⇔ R has no q-parity vertex (661-668), so a first difference never falls at a chain end. Correct; I had not stated it |
| R46 §1 | SIGN, K ≤ (n+2)²(n+1) | SIGN, K ≤ (n² + n)·n | agree. R2's count uses |R| ≤ n and is tighter; both are ≤ R46's constant |
| R46 §2b | SIGN (R-1: F as a sup) | SIGN; unrolled bound (2(d+1)m²K)^d; independent brute force (nestbf.py) | agree; R2's tighter constant is correct. Their brute force covers more cells than my neststar run (which timed out at m = 4) |
| R46 §3 | SIGN WITH GAPS (R-2 OPEN: S − 1 = |P| + I) | SIGN WITH GAPS (G-R46-1: S − 1 = |P| + Z) | agree; I = Z. Route for the second conjunct: I pointed to GAP-A-M §36c (R9 (a) with F_R = 0), R2 to L-RED R44 (EMPTY-REC budget). These are the same idea, which the coming R47 addendum is to write out. Neither is signed |
| EMPTY-REC | listed in R46 but unused in §1-§3 | not discussed | no conflict |
| DATA | b12 tools, both orders, onep_* forced set | own patched logger, effectively one order (Oink); 0 identical-chain transitions on ~250 transitions | complementary; no violation anywhere |
Does anything change my verdict? No. Correction to my text: SAME-CTX (iii)'s T-monotonicity citation is R9 (b) (accepted from
R2's G-SC-2). Joint position: CTRL, NOSTEAL-1P, OUTCOME-MONO-1P, SAME-CTX, R46 §1 and §2b SIGNED by both referees with closed
gaps. LEX and R46 §3 are SIGNED WITH ONE OPEN GAP (L-1 = G-LEX-1, R-2 = G-R46-1): (CHAIN-CHANGE), or a polynomial bound on the
chain-keeping transitions per q-phase. Obstruction statement as both referees read it: GAP-A on 𝒞^1P ⇐ (NEST*-BOUNDED) ∧ (I
polynomial per q-phase).
