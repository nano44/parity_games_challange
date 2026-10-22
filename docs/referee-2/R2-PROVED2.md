# R2-PROVED2: second-referee read of the fleet's unrefereed PROVED readings (GAP-C, GAP-A) — REFEREE-2, 2026-10-17 09:47Z (date -u)
Packet: Lead message 09:53Z (Lead clock). Pin: trunk 20fe2ed. Files read at 20fe2ed: docs/alg/GAP-C.md §1-§13, §18b;
docs/alg/SPP.md; docs/alg/GAP-A-M.md §21c-§21j; docs/alg/DTL-proof.md §1.1-§1.5, §2.2, §2.3 (K1-K5), §3 (b)-(e) and
Lemma W; docs/alg/candidates/C5-DTL.md lines 100-146; TARGET.md §3.
Code: dtl.cpp @ 8fbf0a7 (tools/oink/src/src/solvers/dtl.cpp). docs/referee/R-PROVED2.md was not read before this report
was pushed. Produced on Opus 5.5 under D12.
Probes: docs/referee-2/R2-PROVED2/. dtl_probe2.patch is the full diff of my instrumented dtl.cpp: counters and dumps only,
the algorithm unchanged. Also there: k5.pg, climbdup.py and probe2_results.txt.
"N" = dtl.cpp line N.

## Verdicts (Opus 5.5, D12)
| item | verdict |
|---|---|
| (a) Lemma SCC1 (GAP-C §3) | **SIGN** |
| (b) Lemma B-thr, corrected (GAP-C §3) | **SIGN WITH GAPS**, all gaps closed (revised 10:00Z, §13): (i), (ii) signed. (iii) holds in the stronger form "(a) always" (REFEREE F-b3, which I accept). G-b1 is closed in §13 |
| (c) Theorem A (GAP-C §13), root-call-stable case, given no (α) | **SIGN WITH GAPS**: G-c1 (which sptl pass; reading fixed), G-c2 (DTL-proof K5 (i)/(iii) is false as written; Theorem A does not need it under my reading) |
| (d) Lemma O0, Lemma O1 (GAP-C §6) | **SIGN** (both) |
| (e) Lemma OPP-EXIT (GAP-C §11) | **SIGN WITH GAPS**: G-e1 (the "i.e." clause; closed by the same proof) |
| (f) Lemma K0 (GAP-C §18b) | **SIGN WITH GAPS**: G1 of R2-STEP5 ("all its edges" = edges of G'). Not covered by my R2-STEP5 claim (1), which was KT, so it is checked here |
| (g) phases ≤ D + 2 (C5-DTL lines 141-142; GAP-A-M §21c) | **SIGN** |
| (h) First-Difference Lemma (GAP-A-M §21d) | **SIGN WITH GAPS**: G-h1 (the computations of s and s+1 are not aligned step for step, because of sptl's `while (more)` loop at 870-874; closed) |
| (i) Lemma DV*-MONO (GAP-A-M §21h) | **SIGN** |
| (j) per-context LRN budget ≤ n(n+1) (GAP-A-M §21j) | **SIGN** (with the reading of "LRN at R" stated in §10) |
| (k) (SPP) ⇒ searches ≤ n(n+2) and O(n^10(m+n²)), bit cost (TARGET.md §3) | **SIGN WITH GAPS**: G-k1 (Lemma W needs SCC1; closed by (a)), G-k2 (a factor 2 in DTL-proof §3(c); harmless) |

No REJECT.
- One gap was open at first push: G-b1, a missing case in B-thr (iii). It is CLOSED in §13 (revision of 10:00Z).
- One finding lies outside the packet: DTL-proof K5 (i) and (iii) are false as written. The instance is k5.pg (4 vertices),
  and a corrected form is in §3. GAP-C's map lists K5 as PROVED. Only the meaning of "(α)" depends on K5.

## 1. (a) Lemma SCC1 — SIGN (Opus 5.5, D12)
Every vertex of an sptl region reaches τ in H. Checked by induction over the join order (sptl 481-496, R consumed at 490).
- Vertex-rule p-vertex u: str[u] = v (89), with v earlier. The only later writes are 73 (needs str = −1, which excludes u)
  and 171 (only for vertices not in Z).
- Vertex-rule opponent u: it has the edge u → v and none into R \ Z at its attraction (80). Every vertex that joins later
  was in R \ Z then. So all its H-edges go to earlier vertices.
- Tangle t2 fired at the pop of escape e. Some opponent o ∈ t2 has o → e, because e ∈ tout(t2) (329-337, 443). H_{t2} is
  strongly connected: the SCC edges at its creation are a subgraph of it. Follow an H_{t2}-path from a new vertex to o.
  - New p-vertices keep the tangle strategy (171), and 73 does not overwrite it.
  - New opponent vertices keep the path edge, since its target is in Z_τ after the acceptance.
  - The first old vertex on the path reaches τ by induction.
- Consequences checked:
  - Pearce explores only vertices reachable from τ (opponent edges filtered by R[to] = region, 248). For p-vertices it
    follows str[n] (268), which lies in Z_τ for every region vertex, including a closed p-owned top (str ≠ −1, 515). So
    the only SCC examined is τ's.
  - That SCC is nontrivial iff τ has a successor in Z_τ in H, or a self-loop (315-317). For a p-owned top: str[τ] set
    (73).
- Holds for every sptl region, closed or not, and for every ω. I re-derived the same lemma as DTL-proof 1.5a in R2-STEP5 G2.

## 2. (b) Lemma B-thr (corrected) — SIGN WITH GAPS (Opus 5.5, D12)
- (i) Checked. C_τ ∋ τ (SCC1). Every region vertex has priority ≤ pr(τ) (74, 140). The duplicate check (385-424)
  compares sorted vertex sets.
  - Added point (closed): the stored t is a p-tangle. A stored tangle of the opponent on the same set would share a cycle
    with C_τ (both players' strategies inside the set). That cycle would be won by both players.
  - t is not deleted, since t = C_τ ⊆ G now and G only shrinks.
- (ii) Checked. No escape of t can lie in:
  - Z_τ \ C_τ: it would be reachable from τ in H (SCC1).
  - a later region of the pass, or R_rem (never in a region of this pass): every opponent vertex of Z_τ has, at its
    attraction, no edge into the unconsumed R \ Z (80, 155-156 for tangle-attracted ones). An opponent τ is closed, so it
    has no edge into R (519-525).
  - a higher region of the pass: K2 (DTL-proof §2.3), re-checked. At the pop of the last such escape in the higher region
    Z_τ', all of t is unconsumed, outside Z_τ', and of priority ≤ pr(τ) ≤ pr(τ'). Every other escape is in Z_τ', consumed,
    or outside R. The two cases above exclude Z_τ, later regions and R_rem. So 110-185 would accept t into Z_τ', which
    contradicts t ⊆ Z_τ.
  Hence every escape lies outside the context R of the iteration. The R_rem case is not written in the text but follows
  from the first argument.
- (iii) Reading needed (G-b2, wording):
  - "Removal" of an escape e means the pop at which e left the chain of contexts containing the duplicate's context. That
    pop happens in a piece of the duplicate's own call or of an ancestor call.
  - For a −1 attractor (914-923), e leaves the chain only if 936-950 moves it to X. Otherwise e stays in the recursion
    context Z'.
  - With this reading, at that pop t ⊆ R_A ∪ Z_A, and the other in-G' escapes are in Z_A or outside Gx (checked).
  - attractTangle's possible answers:
    - rejection by the priority test (140), then θ < pr(τ). This includes the case "t partly in the −1 attractor's Z",
      which the text's "(a) no vertex of t was in the attractor's target" misses.
    - acceptance, or the "nothing new" exit (146). Both leave t ⊆ Z, so (b) must hold (t in the recursion context, e moved
      by 936-950). The text names only "nothing new".
    - For a Dom attractor no vertex of t can be in its target X: X never returns to a context. So (a) holds there as
      written.
  - So "(a) or (b)" holds as conclusions. "Exactly one" should read "at least one": both hold in the partial −1 case.
    Closed.
- G-b3 (closed): (iii) needs t to have an escape in G'. A tangle t ⊆ G' with all escapes solved contradicts Lemma O0 (§4).
- G-b1 (OPEN). (iii) assumes t existed (and was evaluated, t ∈ tin[e]) at the pop of its last in-G' escape. It does not
  cover a tangle created in the current search after that pop. tout is computed against this->G (333), so escapes already
  in X are recorded. Then neither (a) nor (b) describes the duplicate.
  - Closed part: such a t cannot become a duplicate within the sptl pass sequence of its own S piece.
    - At τ itself: W[τ] (528).
    - At another top τ'' ∈ t: τ'' would need index < index(τ) (otherwise τ'' had its own region in t's creation pass).
      Then in any later pass τ is processed first and is either a top with its own region or consumed above. Either way
      τ ∉ Z_τ'', so C_τ'' ≠ t.
  - Open part: across S pieces of one search, the claim needs t ⊆ Dom(V, R) of its S piece. That is a union-monotonicity
    statement of the GAP-A kind (MONO is false in general).
  - DATA (mine): same-search duplicates 0. Corpus: 254 files, 2 in-orders, 2 labellings, 1,014 runs, 6 duplicate events.
    Climbs: 6 × 1,500 mutants from gapb_dup_n20 / gapbW_dup_n20, keeping duplicates; 0 same-search duplicates.

## 3. (c) Theorem A — SIGN WITH GAPS (Opus 5.5, D12)
G-c1, my reading:
- "Its lowest region" is the region Z_k of the lowest top τ_k that gets a region in the FIRST sptl pass of the root S
  piece.
- That pass recomputes exactly the final round's regions of best_vertices. Both use the same R, the same V*, the same
  tangle set (no sptl inside best_vertices), and the same rules: (R, Z, R) in sptl 494-495 against (CurR, CurZ, CurR) in
  700-701, consumed across tops, skipping consumed tops.
- "Given no (α)" means "Z_k is closed".
Checked under that reading:
- K4 (DTL-proof §2.3): A ⊆ W_p(G'), where A is the final rescue set (or the union Reg if 716 returned).
  - The opponent cannot leave A. Region vertices were attracted with Gx = CurR, so their other edges go to consumed
    vertices (⊆ Reg) or outside G'. Rescue vertices were attracted with Gx = R. Tops are non-candidates or rescued
    (attracts with R-edges in the set).
  - Every ψ-play visits tops infinitely often or ends in an attracted tangle (Corollary 1.3a).
  - Between consecutive tops τ, τ' the priorities are ≤ max(pr(τ) − 1, pr(τ')): rescue levels are < pr(τ), and region
    vertices are ≤ their top.
  - So the maximum seen infinitely often is a top priority, which has p's parity.
- τ_k ∈ Z_k ⊆ A. W is empty in the first pass for every top except higher tops extracted earlier in the same pass (W is
  reset at 1016 and zero at start).
- SCC1 gives a single candidate SCC C_{τ_k} ⊆ W_p(G'), and it is nontrivial when Z_k is closed. An opponent τ_k whose only
  successors lie in higher regions would have been attracted into the last of them, unless it has a self-loop, which is
  itself nontrivial (317).
- Escapes empty: a dominion (347, tested before the duplicate check).
- A duplicate is impossible:
  - By B-thr (ii) (signed), all its escapes would lie outside R = G', i.e. be solved.
  - If t was stored before the search, O0 (§4) gives a contradiction.
  - If t was created earlier in this pass at a higher top, then t ⊆ that top's region, which is disjoint from Z_k.
  - So C_{τ_k} is new (or a dominion). □
G-c2 (finding about DTL-proof K5, which Theorem A cites only for the meaning of (α)):
- K5 (i) says "no p-vertex of A \ Reg has an edge into a higher region (its priority is ≤ its rescue threshold < the top's
  priority)". That is false. The rescue loop runs to max_prio (721-722), so A contains vertices attracted at levels above
  every top.
- Instance docs/referee-2/R2-PROVED2/k5.pg: Even vertices a(2) → a, b(4) → d, d(3) → a, y(5) → b. Oink renumbers them to
  0, 2, 1, 3, with priorities 0, 2, 1, 3. My dump at 767 (stable):
  - V* = {0, 2}, Reg = {0, 2}, A = {0, 1, 2, 3}.
  - y = 3 (priority 3) is in A \ Reg and has an edge into the higher region {b = 2}.
  - Lowest top τ_k = a = 0. y ∉ Z_k (priority 3 > 0) and y ∉ Str, so K5 (iii) "A \ Reg ⊆ Z_k ∪ Str" also fails.
- K5 (iii) has a second hole: in the induction, an opponent vertex (or a p-vertex via str) whose successor lies in
  Str \ Z_k is neither in Z_k nor in Str.
- Corrected form (my reading, checked):
  - Restrict to A_{<} := the rescue set after level pr(τ_k) − 1, and replace Str by Up(Str), the vertices from which a
    ψ-play reaches Str before Z_k.
  - Then (i) holds for A_{<} \ Reg, since priorities ≤ level < pr(τ_k) ≤ pr(higher top).
  - And A_{<} \ Reg ⊆ Z_k ∪ Up(Str).
  - K5's Consequence then holds: "Z_k is closed unless τ_k's ψ-successor lies in Up(Str) \ Z_k". A p-owned τ_k with an
    edge into a higher region would have been absorbed there. τ_k is rescued only at a level < pr(τ_k) (737).
- So "(α)" should be defined with Up(Str). Theorem A, read with "closed" as its hypothesis, does not depend on this.

## 4. (d) Lemmas O0 and O1 — SIGN (Opus 5.5, D12)
O0, checked (no stored p-tangle t ⊆ G' has all escapes solved at the start of search(p)). A stored tangle has ≥ 1 escape;
otherwise it was a dominion at creation (347). Let e be the last escape solved, popped at 1033.
- Solved for p: at the pop, attractTangles(p, e, G, S, G, −1) (1037) evaluates t (t ∈ tin[e]). t's vertices are in G and
  not in S (t ⊆ G' later). The other escapes are in S, or are not in G (skipped at 155-156). There is no priority bound
  (−1). So t is attracted and solved, which contradicts t ⊆ G'.
- Solved for the opponent: the opponent vertex o ∈ t with o → e is owned by the attracting player, so 74-90 adds it with
  no escape test. Then o is solved, which contradicts t ⊆ G'.
O1, checked. Take the pop of the last in-R escape e in Dom (878-890 or 962-991), in the part of τ_j at threshold pr(τ_j).
- t is alive and a p-tangle, and none of its vertices is in X (t ⊆ R after the removal). So 138 cannot reject, and
  "nothing new" cannot occur.
- The other in-R escapes were popped earlier, so they are in X. Escapes outside R are skipped. So the escape test passes.
- Only 140 rejects, so q := max pr(t) > pr(τ_j).
- q has p's parity: H_t is strongly connected and its cycles are p-won (TS(ii)).
- If m ∈ V, Dom reaches m before τ_j (higher index; O1 of the order datum) and puts it in X, which contradicts t ⊆ R.
- Hence m ∈ R \ V. Since m has p-priority, it was in V_1 (662-667) and was pruned.
- The −1-branch remark holds: every vertex of V_1 left V, and V_f was pruned too.

## 5. (e) Lemma OPP-EXIT — SIGN WITH GAPS (Opus 5.5, D12)
The proof by contradiction is correct and proves the existence statement as written: some o has π(o) ∉ CurR_o.
G-e1 (wording, closed): the gloss "i.e. π(o) lies in an earlier region, in X, or outside the context" does not follow from
π(o) ∉ CurR_o. π(o) can be a vertex of Z_τ that was already popped (consumed) when o was attracted.
- Fix: state the conclusion as "π(o) ∉ Z_τ".
- The same proof gives it. Assume π(o) ∈ Z_τ for every such o. Then π(o) is an H-edge, so π(o) ∈ C_τ ∩ W_{1−p}, and the
  str/π play stays in C_τ ∩ W_{1−p}. It is won by both players (π winning; every H-cycle on C_τ p-won, DTL-proof 1.3).
  Contradiction.
- π(o) ∉ Z_τ together with "no edge into CurR \ Z at attraction" (80; for tangle vertices 155-156; for an opponent τ the
  closed check 519-525) gives exactly the gloss: an earlier region, X, or outside the context.
Checked: a p-vertex of the trap W_{1−p} has str[v] ∈ W_{1−p} ∩ Z_τ ⊆ C_τ, and π exists by positional determinacy on G'.

## 6. (f) Lemma K0 — SIGN WITH GAPS (Opus 5.5, D12)
(a)-(d) are checked.
- (a): σ(v) ∈ D ∖ X ⊆ D ∩ R. If σ(v) ∈ A then v ∈ A. An opponent vertex of Q with no edge into Q has all its G'-edges in
  D = X ∪ A ∪ Q minus Q, so it is in A.
- (b): A_D(G') = ∅ by induction from ∅.
- (c): R_end has no p-priority vertex (668). A σ-consistent infinite play inside Q would be won by the opponent.
- (d): follows, since search_rec at depth 0 ends at R_end (2.2(v)).
Gap: as R2-STEP5 G1, "all of whose edges lie in X ∪ A" must mean edges of G'. Otherwise an edge into a solved p-region
blocks attraction, and (a)'s "else all its edges, which lie in D, ..." fails.

## 7. (g) phases ≤ D + 2 — SIGN (Opus 5.5, D12)
Reading: a phase is a maximal run of one player's searches that ends at the first dominion-finding search, or at that
player's last search.
- 1109-1121: player 0's searches form one block. The block ends at the first false search, or when G = ∅, and player 0
  is never searched again. Then player 1's block runs the same way.
- Inside a block, every phase but the last ends with a dominion-finding search. So player p has ≤ D_p + 1 phases, and in
  total ≤ D + 2.
- D ≤ n: a dominion found in a search is solved at 1032-1038 (its vertices are in G', S[v] marks at 368-373), so G loses
  ≥ 1 vertex.

## 8. (h) First-Difference Lemma — SIGN WITH GAPS (Opus 5.5, D12)
(i) Checked: a search is a function of (G', T_s, ω).
- W is reset at 1016.
- str is read only for vertices already in the current target (73, 268), and those were written in this search when they
  joined (89, 171, 485, 694, 881, 908, 965, 1027).
- Scratch state is reset before use: Candidates, pea_vidx (536), escapes (341), tangle/tangleto, member Z (542).
- A tangle with a vertex outside G that is not yet deleted ("zombie") answers false exactly as a deleted one, and the
  duplicate check sees its tv either way.
- No dominion occurs before the last search of a phase.
(ii) needs G-h1. "Every computation before e is identical" is false literally. When s learns a tangle in pass 1 of an S
piece, sptl repeats (`while (more)`, 870-874). In s+1 the same SCC is a duplicate, extractTangles returns false (464, 422),
and the repeated pass is skipped. So the two sequences of tattr calls are not aligned.
- Closed: align by deleting from s every repeated sptl pass of an S piece before e. Such a pass is a pure repetition.
- Proof. Go region by region with the same inputs (induction over the tops). s's pass-2 output is ⊆ s+1's pass-1 output
  (T_s^{pass 2} ⊆ T_{s+1}, monotone, 1.2b). That equals s's pass-1 output, since there is no difference before e. And
  that is ⊆ s's pass-2 output. So the regions are equal.
- Closedness is a set property (str[top] ≠ −1 iff some successor of top is popped in Z_τ, 73; for an opponent top,
  519-525). So the same tops are closed, all of them are already in W, and pass 2 extracts nothing.
- With this alignment, (ii) holds as written: same input at e, and a strictly larger output by 1.2b monotonicity in T.
- (iii) follows.
Not re-run: the data row (dtl_fdlcheck.py).

## 9. (i) Lemma DV*-MONO — SIGN (Opus 5.5, D12)
DV* is an idealised function, not A_DTL. Readings:
- "attracts into Z" means: a p-owner has an edge into Z; an opponent has all its G-edges in Z, and at least one.
- Escapes outside G are never in Z.
- T means the p-tangles of the phase.
Checked:
- Every lfp rule is positive in Z and in T, so lfp is monotone in both.
- The region walk over V' in decreasing (priority, index) gives Z ⊆ Z' at each step.
- C' ∩ V ⊆ C at the start, and Z_t ⊆ Z'_t at every sweep level.
- So V \ C ⊆ V' \ C', hence V_r(T) ⊆ V_r(T') for all r. A fixpoint round repeats.
- That gives pointwise DV*(T) ≤ DV*(T').
- In a phase G is fixed and T only grows. So each of the |V_0| ≤ n values moves monotonically through {1..n, INF}:
  ≤ n(n+1) changes in all.

## 10. (j) per-context LRN budget ≤ n(n+1) — SIGN (Opus 5.5, D12)
Reading: "LRN at R" = the transitions s → s+1 whose first-difference context is R (the same in s and s+1, by (h)) and with
DV*_R(T_s) ≠ DV*_R(T_{s+1}).
- DV*_R is DV* on the subgame R, with tangles inside R only. T ↦ {t ∈ T : t ⊆ R} is monotone, and §9 never uses that the
  subgame is a game.
- So along the phase, DV*_R(T_s) is pointwise monotone in s and changes at most |V_0(R)|·|R| ≤ n(n+1) times.
- The LRN transitions at R are a subset of those changes.
- The statement bounds LRN per DISTINCT context only. The number of contexts is not bounded (as §21j says).

## 11. (k) (SPP) ⇒ searches ≤ n(n+2) and O(n^10(m+n²)) at bit cost — SIGN WITH GAPS (Opus 5.5, D12)
Checked:
- Searches ≤ Σ_phases |G'| ≤ (D + 2)·n ≤ n(n+2), by (g) and (SPP) for the given ω.
- Lemma W: tangles ≤ n · searches.
  - 528-529: extraction only at a top not in W.
  - W is reset only at 1016, and extractTangles is called only at 539.
  - Hence |T| ≤ n²(n+2).
- DTL-proof §3:
  - W_A = O(m + |T| n²): each popped v scans ins(v) and tin[v], and a check costs O(|U| + |O|).
  - best_vertices: ≤ n+1 rounds (2.2(iii)), each round O(n W_A + n m).
  - sptl passes ≤ (tangles created) + 1 per iteration.
  - Arithmetic: total O(searches · (n⁴ W_A + (|T| + n) n (W_A + |T| n))). With |T| = O(n³) and searches = O(n²) this is
    O(n⁶ m + n^11) ⊆ O(n^10 (m + n²)).
- TARGET.md §3 bit cost:
  - Every stored number is O(log n) bits: vertex index, priority (the parser renumbers priorities to consecutive values,
    C5 §0), tangle index ≤ n²(n+2), stack pointer, Pearce index ≤ n, counters ≤ poly(n).
  - Bitset operations cost O(n/w) words.
  - No arithmetic on long numbers occurs.
  - Unit cost = bit cost up to O(1). Agreed.
G-k1 (closed): Lemma W needs "at most one tangle per extractTangles call". Pearce emits every SCC reachable from top
(290-305). That is SCC1, (a).
G-k2 (harmless): §3(c) says iterations ≤ n(d+1) per search. Each call also has its final, returning iteration, so the
count is ≤ 2n(d+1) + 1. The O-bound is unchanged.
Not checked: (SPP) itself (DATA only), and completeness, which this item does not need.

## 12. Remaining hypotheses and open points (for GAPS.md)
- G-b1 (CLOSED in §13; it was OPEN at first push): B-thr (iii) for a tangle created in the current search after its last in-G' escape left the context chain.
  Closed within one S piece's pass sequence. Open across S pieces: it needs t ⊆ Dom(V, R) of its S piece, a
  union-monotonicity statement. DATA 0 cases.
- G-c2 (finding, outside the packet): DTL-proof K5 (i) and (iii) are false as written (k5.pg). Corrected form in §3.
  "(α)" should be defined via Up(Str).
- Wording or citation fixes, all closed here:
  - G-b2: B-thr (iii), which pop; (a)/(b) read on conclusions; "at least one".
  - G-b3: B-thr cites O0.
  - G-c1: Theorem A, first sptl pass; hypothesis "Z_k closed".
  - G-e1: OPP-EXIT conclusion "π(o) ∉ Z_τ".
  - G1: K0, edges of G'.
  - G-h1: FDL, alignment through repeated sptl passes.
  - G-k1: Lemma W cites SCC1.
  - G-k2: factor 2 in §3(c).
- Unchanged open problems these items reduce to: (SPP) (DATA), GAP-C completeness (Lemma K), (α), (ACYC).
- Nothing here is Lean-checked.

## 13. Comparison with the first referee, and revisions (10:00Z by date -u)
I read docs/referee/R-PROVED2.md (referee 50f2546, pin 43d63b0) after 581902f was pushed. The Lead asked about three
points (10:13Z, Lead clock). My answers follow.

### 13.1 First-Difference Lemma, G-h1: my closure is correct, also in the "orphan in s+1" case
REFEREE's scenario is the case my §8 treats:
- s learns t in pass 1 of an S piece.
- s+1 re-finds the same SCC in its pass 1. It is now a duplicate, so `more` is false and s+1 goes straight to Dom.
- s runs pass 2 first.
REFEREE notes that a positional log then misaligns. I agree, and this is why I stated (ii) on the log with s's repeated
passes deleted. What remains to check is REFEREE's condition for that option (2): the extra pass of s adds no tangle and no
W bit. It holds:
- Suppose s and s+1 agree on every tattr of the S piece's pass 1. This is the premise: e lies later.
- Compare, region by region, s's pass 2 with s+1's pass 1. Every region has the same input, because the consumed sets are
  equal by induction.
- The tangle sets are ordered: s pass 1 at region j ⊆ s pass 2 at region j ⊆ T_{s+1}. These are T_s plus the tangles
  learned at higher tops of pass 1; then T_s plus all of pass 1; then T_s^end.
- By 1.2b, out(s p1) ⊆ out(s p2) ⊆ out(s+1 p1) = out(s p1). So every region of s's pass 2 equals its pass-1 region as a set.
- Closedness is a set property: for a p-top, str[top] ≠ −1 iff some successor of the top is popped in the region (73); for
  an opponent top, 519-525. So pass 2 has the same closed tops as pass 1, and each is already in W (529). Pass 2 extracts
  nothing, learns no tangle and sets no W bit.
- s+1's pass 1 learns nothing: its SCCs are those of s's pass 1, which are stored. So s+1 has exactly one pass, with the
  same W as s.
- After deleting s's pass 2, the next tattrs are both Dom(V, R) with the same input (V, R, X). The W sets are equal, and
  the tangle sets satisfy T_s^{Dom} ⊆ T_{s+1}.
- So (ii) holds on the reduced log. (iii) does too: the tangles learned by s before e are in T_s^e, so the difference at e
  comes from tangles learned after e.
- REFEREE's worry that "the W difference can let s+1 extract at a later top" does not arise, because the W sets are equal.
Verdict on (h) after comparison: SIGN WITH GAPS (Opus 5.5, D12). G-h1 is a real defect of the statement as written; it is
closed by stating (ii) and (iii) on the log with repeated sptl passes deleted, with the proof above. REFEREE marks it OPEN.
This is our only disagreement on substance. A checker with positional alignment (dtl_fdlcheck.py) must drop repeated passes
to match the lemma.

### 13.2 B-thr: REFEREE's F-b3 is correct, and it leads to closing my G-b1
- F-b3, checked at 944-948.
  - Every vertex moved to X at 936-950 is pushed (940, or 90) and popped (945).
  - At its pop, attractVertices(1−p, u, Z, X, Z, t) adds every predecessor from ∈ Z with pr(from) ≤ t that is owned by
    1−p, with no escape test: owner(from) = pl skips 76-86. Every vertex of Z has priority ≤ t (921).
  - Escapes are successors of opponent vertices (329-337). So when an escape e ∈ Z of t moves to X, the opponent vertex
    o ∈ t ∩ Z with o → e moves to X as well. Then t is not inside the recursion context.
  - So branch (b) is vacuous, and B-thr holds as "(a) always". GAP-β = (β-a).
- This also removes my G-b2 remark that "in the partial −1 case both hold". That case cannot occur. If t is partly in the
  −1 attractor's Z at e's pop:
    - If t ends inside Z, then e (in Z) moves to X and drags o along.
    - Otherwise t is split between X ∪ Z' and the remaining R, so t ⊄ R_dup.
  I withdraw that remark. My reading of "which pop" stands; it is the same as REFEREE's G-b2.
  My G-b3 (escapes solved before the search, via O0) is REFEREE's G-b1.
- My G-b1 is CLOSED by a different argument, which does not use F-b3.
  - Let t be created in the current search s, by extractTangles at the top a of an sptl region in S piece P1 (context R1,
    stable set V1). Only sptl creates tangles (439-466, called at 539).
  - By SCC1, a ∈ t.
  - P1's Dom(V1, R1) (878-890) puts every top of V1 into X (879-880: X[top] = true for each top of V1 not yet in X). So a
    leaves P1's call for good after P1.
  - Every later context in the chain is one of: a later context of P1's call, a descendant of a later piece (⊆ R1 minus
    P1's removal), or a context of an ancestor after P1's call returned (it excludes P1's whole call context). So no later
    context contains a, and t is never ⊆ R_dup there.
  - Inside P1's pass sequence a duplicate of t is impossible (§2). So a duplicate is always of a tangle created before
    search s, and (iii) applies.
  - DATA agrees: 0 same-search duplicates.
Verdict on (b) after comparison: SIGN WITH GAPS (Opus 5.5, D12). All gaps are closed: G-b1 (above), G-b2 (reading), G-b3
(O0). It holds in the stronger form "(a) always" (F-b3), with GAP-β = (β-a). REFEREE's verdict is the same.

### 13.3 K5 and Theorem A
- The k5.pg finding touches only K5 (i) and (iii), and the induction hole for successors in Str \ Z_k.
- K5 (ii) is unaffected. An opponent top whose successors all lie in higher regions is attracted at the round-f pop of the
  last of them: it is unconsumed, has priority ≤ that top's, and has no escape (699 before 700). I re-derived this in §3,
  and REFEREE re-checked it against 75-90.
- K4 is unaffected; both referees re-checked it.
- REFEREE's reading of Theorem A is mine: the first-pass regions equal best_vertices' last-round regions, and the premise
  is "if it is closed", i.e. no (α).
- Under that reading, Theorem A uses only K4, K5 (ii), SCC1, B-thr (ii) and O0, none of which k5.pg touches. It stands
  under both readings.
- k5.pg matters only if "(α)" is defined by K5's Consequence. The corrected Consequence (§3: rescue set below pr(τ_k),
  Up(Str)) keeps (α) = "Z_k open" as the right premise.
Verdict on (c) after comparison: SIGN WITH GAPS (Opus 5.5, D12), unchanged. G-c1 is a reading, the same as REFEREE's.
G-c2 is a finding about DTL-proof K5 that Theorem A does not depend on. REFEREE gives SIGN; we differ only in labelling.

### 13.4 Other differences (none on substance)
- (e): REFEREE's G-e2 (the tangle-attracted and top cases) is covered in my §5 by the same lines (155-156, 519-525).
- (f): REFEREE signs K0 without my "edges of G'" note. The note stands as wording, as in R2-STEP5 G1 / G-S5-5.
- (i): I adopt REFEREE's R-i: INF means "never dropped", which includes a round with C ≠ ∅ in which every candidate is
  rescued. My "a fixpoint round repeats" means the same, since such a round leaves V fixed.
- (k): we agree on the conditional. My G-k2 (the returning iterations, a factor 2) does not affect O(·).
- Both reports agree on (a), (d), (g), (i), (j).
- Union of open items after both reports: (SPP) DATA; (α) and Case B; (ACYC); the DTL-proof K5 (i)/(iii) correction
  (k5.pg); and REFEREE's G-h1, which I consider closed (13.1). That last point needs the Lead's routing.
