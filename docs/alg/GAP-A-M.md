# GAP-A, target (1): fixed-context monotonicity (M) of DTL's pruning — L-ALG, 2026-10-16 (produced on Opus 5.5, D8/L27)
Subject: A_DTL as frozen in DTL-proof.md §0 (L26, e144992), one order datum ω fixed throughout (every statement is for each
ω). (M) = L-RED's Claims P, Q (docs/red/R9-DTL-flipflop.md §3) = GAP-A-data.md §4c: at a FIXED context (player p, set R),
for stored tangle sets T ⊆ T', the pruning round of every vertex under T' is ≥ its round under T, and a stable V* does not
shrink. Status words: PROVED (argument written out here, unrefereed) / SKETCH / GAP / DATA / FALSE. Nothing here is a result
in the sense of CLAUDE.md (no referee, no Lean).

## Summary
- (M) is FALSE for A_DTL (section 4b, 08:29Z): in an actual run of the pinned Oink binary (20 vertices,
  experiments/alg/instances/dtl_mviol_n20.pg) the first best_vertices call of two consecutive Odd searches has the SAME
  context R = G' (no dominion, no deletion in between, Odd's tangle set grows by 3) and three pruning distances DECREASE
  (orig1, orig16: 8 → 7; orig19: 9 → 8), read off Oink's own `-t -t` trace. So Claim P, GAP-A-data F5 and (M) are DEAD.
  Before that, section 4 gave the shape at synthetic level (9 vertices, two hand-placed tangles, the stable V* loses a
  vertex); the old Lemma P/Q sketch (DTL-proof.md §3(a)) cannot be completed: its open case is real.
- PROVED: the pruning is governed by an IDEAL layered union Û that is monotone in (V, T) by construction (section 2), the
  code's union U is always ⊆ Û, and (M) holds for every context whose LATER run has no "deficit round" (U ≠ Û)
  (Theorem M-cond, section 3).
- PROVED: a deficit has exactly one cause (Lemma E): a stored tangle that straddles (one of its vertices is consumed by a
  higher region before its last escape is popped) and whose unconsumed rest contains a cycle whose maximum is a surviving
  top of LOWER priority. That top re-absorbs the rest at its own level, and every vertex that could have followed the rest
  at the higher level is lost.
- DATA: on unselected runs the deficit never occurred: U = Û in every pruning round of 53,059 rounds (random games n ≤ 30,
  tc and tc+ N ≤ 6, counter_* families, every instance in experiments/alg/instances); 0 Claim-P/Q violations at identical
  contexts (experiments/alg/dtl_ideal.py Ctx/pq_violations). But SELECTED runs do reach it: hill-climbs
  (experiments/alg/dtl_mclimb.py, fitness = violations ≫ survival-changing deficits ≫ deficits ≫ tangles) found actual DTL
  runs with deficit rounds in which the code prunes a vertex the ideal keeps, including from a random seed
  (experiments/alg/instances/dtl_deficit_n20.pg: Odd's phase, R = all 20 vertices, vertex 10 pruned by the code and kept by
  the ideal; stable order ω; Oink solves it, verified, 21 tangles, 5 iterations); seeded continuations reach 10 such rounds per
  run. A violation of (M) needs the same context visited EARLIER without the stealing tangle: found 08:29Z (section 4b).

Summary of sections 5-10 (added 10:06Z; target (2) and the follow-ups; every item unrefereed):
- Target (2), section 6: no global budget follows from what is proved. Counting (PROVED given the DATA line "contexts change
  only through results"): N_j ≤ K·C_j over DISTINCT level-j contexts, a product over nested pieces; the obstruction is
  fresh child contexts per parent state (replays). Driver lemma PROVED (with Lemma D2): a level-j change is driven by a
  tangle learned at a piece ≥ j in the previous search. DATA: 1 replay in 718 games; climbed instances show only
  revisits (dtl_replay4_n32, dtl_replay2deep_n32).
- Lemma D2 (PROVED): every sptl region lies in Dom(V*, R) ∪ X_before. Lemma D3 (PROVED): Dom is a layered closure,
  monotone in V and T. Lemma L-epoch (C6, PROVED reading): a stable piece learns again within an epoch only through V*
  growth, a lift (Dom grows) or a catch-up; conjecture (CU) excluding catch-ups is FALSE (dtl_cu_viol_n24.pg).
- Section 7: GAP-C step (r1) PROVED (per call, same region, no dominion in between); (r2) FAILS (L-RED R11).
- Section 8: reply to L-RED R10: C6 excludes the stealer gate (S); order gates are not covered by order data; a pure
  order gate by the last fast tangle at a fixed region set is impossible (PROVED with D2).
- Section 10: BARRIER for this proof route (not a DTL lower bound): APP(k), an abstract piece process satisfying every
  proved property, has 2^k + 1 searches on 2k + 1 vertices (experiments/alg/app_model.py). It violates the frontier
  property (F); (F) holds for cut-attractor carries (L-RED) and FAILS for pruning-driven changes in real A_DTL runs (8 of
  136 drivers at Dom(prevV) pieces learned at a later stable piece), which is APP's level type. What a polynomial proof
  needs: a bound on pruning-driven carries at −1 pieces (L-RED's MIRROR reading says they must be self-reinforcing).

## 1. Set semantics of one pruning round (PROVED, reading of dtl.cpp 643-776)
Fix p, R, the alive p-tangles T (tpr ≠ −1, parity p, all vertices unsolved; a tangle with a solved vertex never fires,
DTL-proof.md 1.2 (T)). For B ⊆ R and a threshold h, Attr_h(B) is the least superset of B closed under DTL-proof.md
Lemma 1.2's rules (V), (T) with Gx = R and threshold h (escapes judged in R, "≥ 1 escape in Z" included).
Round with input V ⊆ P_p ∩ R:
- Regions (690-706): tops τ ∈ V in descending index order, skipping tops already in Z; region Z_τ = the closure of {τ}
  under (V), (T) inside CurR_τ := R minus the earlier regions, threshold pr(τ), escapes judged in CurR_τ (exits into earlier
  regions and outside R are forgiven). By Lemma 1.2 each Z_τ is a least fixed point, so U := ∪ Z_τ depends on (V, T, R, ω)
  only, not on the stack order. A_q := the union of the regions of tops of priority ≥ q.
- Survival (712-765): Candidates = {v ∈ V : ¬attracts(v, U, R)}; the threshold loop computes W_t := Attr_t(U) for
  t = 0, 1, ... (each step is Attr_t(W_{t−1}) = Attr_t(U), closures), and a candidate u is cleared at the first t < pr(u)
  with attracts(u, W_t, R). Since U ⊆ W_t and attracts is monotone in its third argument (1.1),
  S(V, T) := V_next = {v ∈ V : attracts(v, U, R) or ∃ t < pr(v): attracts(v, W_t, R)}.
  DATA check: dtl_ideal.py asserts V_next = S(V, T) on every round of every run above (0 failures).

## 2. The ideal union and its monotonicity (PROVED)
Ideal union: Û := Û_{≥0} where, for q descending over ALL priorities, Û_{≥q} := Attr_q(Û_{>q} ∪ V_q) (V_q = tops of
priority q; Û_{>max} = ∅). An empty level changes nothing (Û_{>q} is already closed under threshold-q' rules for some
q' ≥ q). Ideal survival Ŝ(V, T) := the formula of section 1 with Û in place of U.
Lemma 2.1 (monotone). V ⊆ V', T ⊆ T' ⇒ Û(V, T) ⊆ Û(V', T'), and v ∈ Ŝ(V, T) ⇒ v ∈ Ŝ(V', T') for v ∈ V.
Proof. Attr_q is monotone in its base and in T (1.2b); induction on q gives Û_{≥q}(V,T) ⊆ Û_{≥q}(V',T'); Attr_t and attracts
are monotone. □
Lemma 2.2 (U ⊆ Û, hence S ⊆ Ŝ). Proof: by induction over the levels q (descending) and, inside a level, over the regions in
processing order and the push order, every vertex of a level-q region is derived by a rule of Attr_q whose premises lie in
A_{>q} ∪ (earlier level-q regions) ∪ (current region) ⊆ Û_{≥q}: (V) for a p-vertex uses its edge to the popped vertex;
(V) for an opponent vertex has every R-successor in the current region or in an earlier (consumed) region; (T) has its
vertices in R, the new ones of priority ≤ q, every escape in the current region, in an earlier region or outside R, and one
escape in the current region; the top is in V_q. □ Then W_t ⊆ Ŵ_t and S ⊆ Ŝ by monotonicity of Attr_t and attracts.

## 3. When the code agrees with the ideal (PROVED) and the one obstruction (PROVED)
(P*) for V: no p-priority vertex of R outside V attracts into Û(V, T) (¬attracts(m, Û, R) for m ∈ (P_p ∩ R) \ V).
Lemma E. Let V satisfy (P*), and let q be the HIGHEST level with A_q ≠ Û_{≥q} (if any), so A_{>q} = Û_{>q}. Then there is an
alive p-tangle t such that (a) some vertex of t lies in a region computed before the region holding t's last escape (the
straddle), and (b) the unconsumed rest Y := U_t \ A_q contains a cycle of H_t whose maximum vertex m is in V with
pr(m) < q.
Proof. A_q ⊆ Û_{≥q} by Lemma 2.2. Suppose some rule of Attr_q applies to x ∈ R \ A_q with pr(x) ≤ q and premises in A_q
(otherwise A_q is closed and contains Û_{>q} ∪ V_q, so A_q ⊇ Û_{≥q}).
 (V, p-vertex) x has a successor y ∈ A_q, in the region of τ_y with pr(τ_y) ≥ q. When y was popped, x was in CurR (it is in
   no region of priority ≥ q, and only such regions existed then) and pr(x) ≤ q ≤ pr(τ_y): x was attracted. Contradiction.
 (V, opponent) x has every R-successor in A_q and one there. Let τ* be the last region (processing order) holding a
   successor of x; at the pop of the last such successor all of x's successors are in Z or consumed: x was attracted.
   Contradiction.
 (T) Tangle t with every escape in A_q or outside R, one in A_q, Y := U_t \ A_q ≠ ∅, priorities of Y ≤ q. Let τ_e be the last
   region holding an escape. If no vertex of t lies in a region before τ_e, t fires at the pop of τ_e's last escape (every
   escape covered, every vertex in Z or CurR, priorities ≤ q ≤ pr(τ_e)): Y ⊆ A_q, contradiction. So (a) holds. For (b): a
   p-vertex y ∈ Y has s_t(y) ∈ U_t (TS(i)); if s_t(y) ∈ A_q the (V)-case puts y in A_q; so s_t(y) ∈ Y. An opponent y ∈ Y has
   all R-successors in U_t ∪ escapes (TS(iii)) and a successor in U_t (H_t is a nontrivial SCC); if none is in Y, all its
   R-successors are in A_q and the (V)-case puts it in A_q; so it has one in Y. Hence H_t restricted to Y has a cycle; its
   maximum m has parity p (TS(ii)) and pr(m) ≤ q, m ∉ A_q. If m ∉ V: Y ⊆ Û_{≥q} (t fires in the closure Û_{≥q} ⊇ A_q), so
   every R-successor of m is in U_t ∪ escapes ⊆ Û (a p-owned m: s_t(m) ∈ Y ⊆ Û), and m attracts into Û, contradicting
   (P*). So m ∈ V; pr(m) = q would put m ∈ V_q ⊆ A_q; so pr(m) < q. □
Lemma P*-inv (the pruning keeps (P*) while the code agrees with the ideal). V_0 = P_p ∩ R satisfies (P*) vacuously. If
U = Û at rounds 0..i−1 then V_1..V_i are the ideal rounds (S = Ŝ there), every m pruned at a round j < i has
¬attracts(m, Û(V_j), R), and Û(V_i) ⊆ Û(V_j) (Lemma 2.1, V_i ⊆ V_j): V_i satisfies (P*). □
Theorem M-cond. Fix (p, R) and T ⊆ T'. If the run under T' has no deficit round (U = Û at every round), then
V_i(T) ⊆ V_i(T') for every i, so pruning rounds never decrease and a stable V* does not shrink.
Proof. By Lemma 2.2 and Lemma 2.1, V_i(T) ⊆ V̂_i(T) (induction: S(V_i) ⊆ Ŝ(V_i) ⊆ Ŝ(V̂_i) on V_i), V̂_i(T) ⊆ V̂_i(T')
(Lemma 2.1 by induction), and V̂_i(T') = V_i(T') (no deficit). □
By Lemma E and Lemma P*-inv, the first deficit round of any run has the shape (a)+(b). So (M) can fail only through that
shape, in the LATER run (the one with more tangles).

## 4. The shape is real: (M) is FALSE for arbitrary tangle sets (synthetic; DTL reachability OPEN)
Instance (experiments/alg/dtl_m_synth.py; p = Even, R = all 9 vertices, index order as listed):
| vertex | priority | owner | successors |
| --- | --- | --- | --- |
| o | 1 | Odd | k, m, tau2 |
| w2 | 1 | Odd | w, tau |
| k | 2 | Even | o, w |
| m | 2 | Even | o |
| v | 2 | Even | x |
| w | 2 | Even | w2 |
| x | 3 | Even | o |
| tau2 | 4 | Even | tau2 |
| tau | 4 | Even | tau |
Tangles (both satisfy TS: every cycle has maximum priority 2): t = {k→o, m→o, o}, escapes {tau2}; t' = {w→w2, w2}, escapes
{tau}. Round 1 (V_0 = {k, m, v, w, tau2, tau}):
- T = {t}: regions tau: {tau}; tau2: t fires at tau2's pop, {tau2, k, m, o}, then x (priority 3 ≤ 4, edge to o) and v
  (edge to x); w: {w, w2}. U = all vertices, no candidate, result stable with v ∈ V*.
- T' = {t, t'}: tau's region fires t' and takes k (k → w): {tau, w, w2, k}; at tau2, t cannot fire (k consumed) and o is
  blocked by its edge to m: {tau2}; level 2: v: {v}; m: {m, o} (o's exits to k and tau2 are consumed, forgiven) — x has
  priority 3 > 2 and cannot follow. U misses x; v is a candidate (its only successor is x) and is not cleared at t ≤ 1:
  v is pruned at distance 1. Result stable with V* = {k, m, tau2, tau, w}: Claim Q fails (V* lost v), Claim P fails
  (v's round dropped from ∞ to 1). Here m (priority 2 < 4) is the lower survivor of Lemma E (b); Û ∋ x.
Verified twice: dtl_ideal.py's set-level code and L-COMP's dtl_py best_vertices on the injected tangles (same output).
What a DTL realisation needs (the shape for L-RED, and the climb's target): t learned at m in a context where tau2 is
forgiven (removed earlier in that search, or consumed), t' learned at w in a context where tau is forgiven, t' learned in a
later search than t, and the context R visited in a search between the two learnings and again after t'. Lemma E says no
other mechanism breaks (M).

## 4b. (M) fails in an actual A_DTL run (DATA, reproduced by Oink's trace and by the independent Python implementation)
Instance experiments/alg/instances/dtl_mviol_n20.pg (20 vertices; found by experiments/alg/dtl_mclimb.py seed 33 from
dtl_deficit_n20.pg, then relabelled so that Oink's std::sort is the identity; labels origK). Pinned command
`oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7: 17 tangles, 1 dominion (at the end of iteration 5), 6 iterations,
`-v`: solution verified. Even's phase: iterations 0, 1 (tangles 0-3, Even's, irrelevant to Odd's pruning). Odd's phase:
iterations 2, 3, 4, 5, all with G' = all 20 vertices until the dominion at the end of iteration 5. First best_vertices call
(context R = G'), Oink's "distance k:" lines:
| iteration | Odd tangles before it | orig1 | orig16 | orig19 | orig3 | orig17 | orig11 | orig0 | orig10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2-odd | 0 | 5 | 6 | 7 | 3 | 4 | 4 | 8 | 9 (last) |
| 3-odd | 5 | 8 | 8 | 9 | 7 | 6 | 8 | 10 | 11 (last) |
| 4-odd | 8 | 7 | 7 | 8 | 9 | 9 | 10 | 11 | 12 (last) |
From 3-odd to 4-odd the tangle set only grows (tangles 9, 10, 11 learned in 3-odd; nothing solved, nothing deleted) and
three distances go DOWN while others go up. experiments/alg/dtl_mviol_check.py reproduces both readings (Python: L-COMP's
dtl_py with Oink's order data, same counts; Oink: trace parse) and is in experiments/alg/check.sh.
Mechanism (dtl_ideal.Anatomy): as Theorem M-cond requires, the later visit has a deficit, from round 1 on: Odd tangles
learned in 3-odd at tops orig7, orig3, orig17 (a chain at increasing priority) straddle the regions of orig7 and orig1 (both
priority 15; descending index order processes orig7 first), orig3 (19) and orig17 (21); the ideal union contains orig5
(priority 16), which the code's union misses, and the ideal keeps orig6 at round 1, where the code prunes it. The
distance decreases at round 7 follow from the smaller code union in the rounds before.
Consequence: no invariant of DTL-reachable tangle sets excludes the shape (the Lead's split (b), 08:22Z): the shape is
reached. Lemma E and Theorem M-cond stand as PROVED statements; (M) itself is DEAD for A_DTL.

## 5. Consequences for GAP-A (reading)
- The nested-epoch argument of GAP-A-data.md §4c used (M) at every fixed context. It is now PROVED only for contexts whose
  later run has no deficit round (Theorem M-cond); section 4b shows piece 0 (the first call, R = G') moving backwards in an
  actual run, so even "the result at piece 0 changes at most n(n+1)+1 times per phase" is unproved for A_DTL.
- For the counter (L-RED): the deficit is a FIXED-context reset device. A tangle learned at a higher top steals a vertex of
  a lower structure's tangle in an earlier region; the rest is re-absorbed only by a lower-priority top, so vertices of
  higher priority that hung on it fall out of the union and distances at the same context go down. R9 §4(1) needed a
  reset and could only get one from a fresh context.
- A variant of DTL whose best_vertices uses Û for its candidate test (same sptl, same tangles) satisfies (M)
  unconditionally (Lemma 2.1). It is a different algorithm from the frozen A_DTL; noted as a design option only (Lead/owner
  decide; §0 is frozen, L26).
- No budget for piece-k changes follows from (M) alone; target (2) is unaffected by the repair above.

## 6. Target (2): a global budget for piece changes, or why none follows (from 08:40Z)
Setting: one phase (player p, no dominion, so G' and the alive tangle set only grow), searches s = 1, 2, ...; at depth 0,
search s is a sequence of pieces j = 0, 1, ... with context R_j(s), result res_j(s) ∈ {stable, −1, cut} with its V
(stable V* or the −1 return set), and removed set D_j(s); R_{j+1} = R_j \ D_j. For a transition s → s+1, its LEVEL is the
first j where (R_j, res_j, V_j) differ, or ∗ if all depth-0 pieces agree (progress inside a cut's recursion or in sptl).
6.1 Facts.
- (DATA, 0 exceptions) Contexts change only through results: at the level of every transition the two contexts are EQUAL
  (DTL 57 and C6 55 transitions with a depth-0 level on 600 random games n ≤ 24, every instance in experiments/alg/instances
  and tc+ N ≤ 5; experiments/alg/dtl_pieces.py). Equal (R_{j−1}, res, V) with a grown D_{j−1} (Dom or cut attractor grown by new
  tangles) would break this; it never happened. Not proved.
- (PROVED for C6 by Lemma 2.1; for A_DTL only under Theorem M-cond) At the level j of a transition the context is the same
  (by the DATA line), so the profile of piece j does not decrease and changes raise Σ distances ≤ n(n+1): at most
  K := n(n+1) + 1 transitions of level j while pieces < j keep their results (one EPOCH of level j).
- Counting (PROVED from the two lines above): with N_j := number of transitions of level j in the phase and E_j := number of
  level-j epochs = 1 + Σ_{i<j} N_i, N_j ≤ K·E_j, so N_j ≤ K(K+1)^j and the phase has at most (K+1)^L depth-0 transitions,
  L = the number of depth-0 pieces (≤ n), with the same structure recursively inside every cut (∗ transitions).
- Lemma D2 (sptl regions lie in Dom; PROVED, 09:25Z). At a stable piece with context R, removed set X_before and V*, every
  region of every sptl pass (computed with a tangle set T_pass ⊆ T, T = the set when Dom(V*, R) runs) lies in
  Dom(V*, R) ∪ X_before, in fact in the Dom regions of tops processed no later. Proof (claim per prefix of tops, in
  descending order; inside a region over the push order). A p-vertex u pushed at the pop
  of v: v lies in R, hence in a Dom region of a top at least as high (induction), and was popped there; u was then still
  in R or already in X, with pr(u) ≤ pr(τ) ≤ that top's priority: attracted. An opponent vertex: its R-successors are in
  Dom regions (induction) or outside R (forgiven in Dom too), and one is in R (the one popped in sptl); at the last Dom pop
  among them it is attracted. A tangle t fired in sptl: its vertices are in R, its escapes in Dom regions (induction) or
  outside R, one in R; at the last Dom pop among its escapes every vertex of t is in X or in the remaining R (popped
  vertices are in X), and attractTangle counts vertices already in X as attracted (dtl.cpp 136-137 with Z = X): t fires.
  Dom therefore has no straddle failure; that is the difference to the regions of best_vertices and sptl. DATA: 0 violations
  in 1,890 stable pieces (800 random games n ≤ 28, every instance, tc+ N ≤ 5; experiments/alg/dtl_sptldom.py; it checks the
  last pass).
- Driver lemma (PROVED for transitions whose level-j contexts are equal, i.e. every observed transition, 09:25Z). A
  transition of level j is driven by a tangle that is NEW (learned in search s) and fires in piece j's computation in
  search s+1 (first-difference argument: with the old tangle set the computation at an equal context is identical). Such a
  tangle was learned at a piece k ≥ j of search s, or inside the recursion of a cut piece k ≥ j: a tangle learned at a
  piece k < j lies in D_k(s) (an SCC of an sptl region, inside Dom by Lemma D2, or inside a cut's Z), and D_k(s) is
  disjoint from R_{k+1}(s) ⊇ R_j(s) = R_j(s+1). So carries come from deeper learning (R9's CARRY).
- Lemma N (towards "contexts change only through results"; SKETCH, 09:01Z, for C6 with Dom also computed as Û). Fix
  R; T ⊆ T'; suppose the ideal pruning gives the same result and the same V (stable V*, or the −1 return set A) under T and
  T'. Then Û(V, T) = Û(V, T') unless at the highest level q where they differ the new tangle's unconsumed part has its
  cycle maximum m in V with pr(m) < q (the Lemma E (b) shape again). Proof of the other case: at that level some t ∈ T' \ T
  applies to the T-closure; as in Lemma E its new part Y has a cycle of H_t with p-parity maximum m ∉ Û_{≥q}(V, T); if
  m ∉ V, m was pruned at some round i' under T', but m ∈ Y ⊆ Û(V, T') ⊆ Û(V_{i'−1}(T'), T') and all its R-successors lie
  in U_t ∪ esc(t) ⊆ Û(V, T'), so m attracts into it and survives round i': contradiction. Cut pieces are not covered
  (their attractor at threshold t can grow with T at an unchanged result). A_DTL and C6 as written remove Dom(V*, R),
  which contains the last round's consumed union U(V*, T) and can be larger (dtl.cpp 876-889: its target set X also holds
  the vertices removed by earlier pieces, and attractTangle counts tangle vertices in X as already attracted, so a tangle
  partly removed earlier can fire there but not in best_vertices' regions); Dom can grow through deficits and through
  such tangles.
- Refinement (PROVED for C6, 09:10Z; for A_DTL only under Theorem M-cond): (M) holds for ANY T ⊆ T', so also between
  non-consecutive visits of the same context: if a level-j context recurs in a later epoch, piece j resumes at a state at
  least as advanced. Hence N_j ≤ K·C_j with C_j := the number of DISTINCT level-j contexts in the phase (≤ E_j). DATA:
  dtl_replay4_n32 revisits a level-1 context (piece 1's context in searches 10-12 equals that of searches 5-7, piece 1's
  maximum distance 5 there and 7 on the revisit): 5 level-1 epochs, 4 distinct contexts; the root's −1 return set
  oscillates {5} → {5, 27} → {5} while its maximum distance rises 7 → 7 → 8, one bit of state.
  Mechanism (reading): two vertices' distances leapfrog (27 reaches the maximum 7, then 5 moves to 8); each flip raises a
  distance, so such a bit flips O(n) times per context, and the −1 return set (hence the next context) follows it.
6.2 The precise obstruction. The product comes only from REPLAYS: transitions of level j in an epoch other than the first
level-j epoch in which level j changed (some level i < j changed in between). With replays bounded, N_j ≤ K + (replays at
level j) and the phase has O(L·K + replays) transitions. Nothing proved bounds replays, for a concrete reason: when a level
i < j changes, R_j becomes a context not comparable to the old one (the −1 return set is re-cut, GAP-A-data F6/F7), and the
tangles learned in the old level-j epoch have escapes that were forgiven there (in the old D_{<j}) and are uncovered in the
new context, so they do not fire there (R9 §4(1)): piece j restarts with the stored tangles that ARE usable in the new
context, and how many level-j changes remain is not controlled by anything monotone. In A_DTL there is a second reset device
on top of this, at a fixed context (section 4b). Every global quantity tried so far is dead (GAP-A-data §5, F11 candidates
(a)-(c), P1; and here (M)/F5).
6.3 Measured replay structure (experiments/alg/dtl_pieces.py; replay depth = 1 + depth of the opening change when
that change is itself a replay; a k-digit counter has depth k − 1).
| run | transition levels per phase (∗ = deeper) | replays | replay depth |
| --- | --- | --- | --- |
| tc+ N = 4, 5, 6 | 0 2 1 0 / 0 3 2 1 0 / 0 4 3 2 1 0 (and the same after the phase break) | 0 | 0 |
| dtl_searches20_n32 | ∗ 0 1 0 0 1 ∗ ∗ 0 ∗ ∗ 0 ∗ 0, then ∗ ∗ 0 | 1 | 1 |
| dtl_replay4_n32 (climb on replay depth, 09:07Z; Oink: 42 tangles, 16 iterations, verified) | 1 0 1 0 1 0 1 0 1, then 1 0 | 4 | 1 |
| dtl_replay2deep_n32 (climb, 09:11Z; Oink: 35 tangles, 16 iterations, verified) | 1 0 2 1 2 1 1 2, then 1 0 | 3 | 2 |
| the other 717 games: 600 random (n ≤ 24), every file in experiments/alg/instances, tc N ≤ 6, tc+ N ≤ 5, counter_* | — | 0 | 0 |
tc+ is a one-pass SWEEP (each piece changes once, deepest first) and has no replay at all; its 2N + 2 searches are the
sweep, not a counter. Over these 718 games (A_DTL and C6 give the same histogram) exactly ONE replay occurs, of depth 1 (level 1 re-advancing
after the root moved, in a climbed instance).
The two climbed instances add no fresh structure: dtl_replay2deep_n32's depth-2 replay (piece 2 re-advancing after a
piece-1 replay) runs on only 3 distinct level-2 contexts; the context of searches 10-12 is that of searches 5-7 (piece 2's
maximum distance 5 there, 7 on the revisit), driven by a leapfrog bit at level 1 (return set {5} / {5, 22}). Counted over
distinct contexts (N_j ≤ K·C_j) neither instance shows a product.
6.3b Answer to target (2) (reading, 09:15Z). No global budget follows from what is proved, and the reason is precise:
every proved fact is compatible with a k-level counter. Per context, piece j changes at most K = O(n²) times (fixed-context
monotonicity, C6; A_DTL under M-cond); a parent context with its O(n²) results can hand the child up to O(n²) DISTINCT
contexts (the −1 return set is re-cut at each result change, GAP-A-data F7; a leapfrog of two distances is one bit), and a
child needs only O(1) changes per context to carry a counter digit; revisited contexts resume (refinement above) and cost
the counter nothing it needs. So the proved facts give C_j ≤ (K+1)^j and searches ≤ n^{O(k)} for k nested pieces, and no
more. Whether DTL can make every parent state a FRESH child context in which the child still has work is exactly the
open question; in all data the child contexts REVISIT (C_1 ≤ 4, C_2 ≤ 3 on the climbed instances, 1 elsewhere).
6.4 What would close GAP-A along this route (open; for the proof lane): a lemma charging every replay at level j to a
global resource, e.g. "a level-j replay needs a tangle usable in the new context that was usable in NO earlier level-j
context of the phase", with that resource bounded polynomially. What would kill it (for L-RED): a family whose replay depth
grows with n. Building block (DATA): experiments/alg/instances/dtl_replay4_n32.pg is a clean two-level alternation (piece 1
re-advances once after every root change, same under A_DTL and C6). Depth 2 would need a copy of this behaviour INSIDE
piece 1's context, reset by every root change: the root's change must return to piece 1's context vertices whose removal
the inner copy's learned tangles relied on for escape coverage, so that the inner alternation restarts with new sets. Climbs on C6 with fitness = replay depth ≫ replays ≫ searches are running (started 08:43Z).

## 7. Consequence for GAP-C: step (r1) of the (α)-exclusion route (PROVED, 09:04Z)
DTL-proof.md §2.3's route for excluding the straddling-tangle shape (α) needs (r1): "the only source of non-monotonicity of
the pruning across searches is a straddle", per call on the same region. Statement proved here: let s, s+1 be consecutive
searches of the same player with no dominion solved in s (so the same G', T_s ⊆ T_{s+1}, no deletion), and consider the
first best_vertices call of each (context R = G'). If in no round of the call in s+1 a stored tangle has the shape of
Lemma E ((a) and (b)), then V_i(s) ⊆ V_i(s+1) for every round i, the call in s+1 is stable whenever the call in s is, with
V*_s ⊆ V*_{s+1}, and the regions satisfy Reg_s ⊆ Reg_{s+1}.
Proof. Induction over the rounds of the call in s+1. V_0 satisfies (P*). If round i has (P*) and U ≠ Û, Lemma E produces a
tangle of the excluded shape; so U = Û at round i, the round is ideal, and (P*) passes to round i+1 (Lemma P*-inv). So no
round of s+1 has a deficit, and Theorem M-cond gives V_i(s) ⊆ V_i(s+1). If the call in s is stable, V_i(s+1) ⊇ V*_s ≠ ∅ for
every i, so the call in s+1 is stable and V*_{s+1} ⊇ V*_s. Regions: Reg_s = U(V*_s, T_s) ⊆ Û(V*_s, T_s) (Lemma 2.2) ⊆
Û(V*_{s+1}, T_{s+1}) (Lemma 2.1) = U(V*_{s+1}, T_{s+1}) = Reg_{s+1} (no deficit). □
Not covered: a dominion solved in between (R shrinks and tangles are deleted); the regress step (r2); and the fact that the
excluded shape DOES occur in actual runs (§4b), so the route needs (r2) to show that the earliest such tangle cannot have
it.

## 8. Reply to L-RED R10 (claude/l-red de8a431, "Sharper form": the 2CE carry needs a fixed-context gate at P1) (09:20Z)
- Bounded triggered deficits per context: NOT given by Lemma E / Lemma N. Inside one round at a fixed context the regions
  are a top-down nested structure (region k computed in R minus regions 1..k−1); a deficit needs a steal (a higher region
  growing into a tangle of a lower one). Only the highest region is monotone in T at a fixed round input; the round-1 input
  V_0 = P_p ∩ R is fixed, so steals by the first-round highest region are ≤ n per context; lower regions restart their
  growth after every steal above them: (n+1)^k over k tops, no polynomial. (READING.)
- C6 excludes R10's gate (S) outright (PROVED from Lemma 2.1 by induction over rounds: V̂*(T) ⊆ V̂*(T + T_last), and the
  result stays stable); with R10's reading "a stealer that stays in V* keeps y", every 2CE carry in C6 needs gate (O).
- Gate (O) (order: a new tangle changes LIFO pops / str inside a fixed region set) is NOT covered by "every order datum":
  ω fixes the static orders O1-O8; for each ω the pops and str still depend on the tangle set (a tangle fired at an escape's
  pop pushes its vertices with stored strategies before the popped vertex's other predecessors are popped). The (M)-lemmas
  here are about vertex sets and say nothing about str. (O) is DTL-proof.md Lemma S step (3): a tangle created between two
  occurrences and lying inside the region. DATA so far: L-RED R8 §12 measured zero strategy differences at recurring
  (top, region set) pairs; a pure order gate has never been observed.
- Refinement of (O) (PROVED with Lemma D2, 09:25Z): the gate tangle T_last is learned in search s AFTER P1, in a piece
  whose context excludes D_{P1} = Dom(V*_{P1}, R_{P1}); every sptl region of V*_{P1} lies in D_{P1} ∪ X_before (Lemma D2),
  so T_last is disjoint from a_{c+1}'s region S_s, so T_last can
  fire inside a_{c+1}'s region in search s+1 only if that region's vertex SET has grown to contain T_last. A pure order gate
  at a fixed region set is then impossible for T_last; any T_last-gate at P1 is a set-level lift (R10's open case (iv)).

## 9. C6 at a fixed stable context: Dom is monotone; what makes a stable piece learn again within an epoch (09:34Z)
Lemma D3 (Dom is a layered closure; PROVED, reading of dtl.cpp 876-889). Fix a context R and the set X_before removed
earlier in the same search_rec call. Dom(V, R) (the removal after a stable result) equals the layered closure D̂: for q
descending over the priorities of V, D̂_{≥q} := the least superset of D̂_{>q} ∪ V_q closed under the threshold-q rules in R
where X_before counts as forgiven for escapes and as already attracted for tangle vertices (attractTangle's `Z[v]` with
Z = X), and a tangle needs one escape in D̂ itself (N1: X_before is never popped). Proof: as Lemma E, level by level; the
vertex cases are Lemma E's; the tangle case cannot fail, because at the last Dom pop among the tangle's escapes every
vertex is in X (consumed or X_before) or in the remaining R. Hence Dom(V, R) is monotone in V and in T at fixed
(R, X_before). (Contrast: best_vertices' and sptl's regions treat consumed vertices as outside, which is where Lemma E's
straddles come from.)
Lemma L-epoch (what can make a stable piece learn again within an epoch, C6; PROVED, reading; corrected 09:35Z before
push: a first draft claimed a 2|R_j| + 1 bound and missed case (c)). Let piece j have the same context R_j, the same
X_before and a stable result in consecutive searches s_1 < s_2 < ... of one phase (an epoch of piece j; no dominion).
Then V*_j(s_i) and D_j(s_i) = Dom(V*_j, R_j) are non-decreasing (C6's Lemma 2.1 by induction over rounds; Lemma D3), and
every search s_{i+1} in which piece j learns a new tangle is of one of three kinds:
 (a) V*_j grew (at most |R_j| times);
 (b) a LIFT: a tangle t learned in s_i after piece j (a later piece or a recursion below it; its learning context excludes
     D_j(s_i)) fires in a piece-j sptl region of s_{i+1}; then t ⊆ D_j(s_{i+1}) (Lemma D2) and t ∩ D_j(s_i) = ∅, so D_j grew
     strictly (at most |R_j| times);
 (c) a CATCH-UP: the first pass of s_{i+1} repeats the final pass of s_i (Lemma S step (4): same V*, same firing tangles,
     same pushes and str; tangles learned in s_{i+1} before piece j lie in D_k, k < j, outside R_j), yet a top τ that had
     extracted in an EARLIER pass of s_i, and was then blocked by W (dtl.cpp 528, reset only per search), now extracts its
     final-pass SCC, which differs from the one it extracted. Catch-ups can chain, one step per search, entirely inside the
     fixed set D_j (a catch-up tangle lies in its region ⊆ D_j): NOT bounded by anything proved. This is the cross-search
     form of the in-search chain (GAP-A-data F3/F4).
So a stable piece learns in at most 2|R_j| searches of an epoch PLUS its catch-ups. GAP: a bound on catch-up chains at a
fixed region family.
Conjecture (CU) — FALSE (09:43Z): "a W-blocked top with a closed region has a stored tangle or a dominion as its SCC".
First data looked clean (experiments/alg/dtl_wblock.py, restricted to searches that have found no dominion yet: 441
blocked closed regions, 0 new SCCs; unrestricted, all 1,412 new ones were dominions inside searches that had already found
a dominion). A climb on the count found counterexamples within minutes: experiments/alg/instances/dtl_cu_viol_n24.pg
(dtl_pyref stable order; Oink solves it, verified), search 1 (no dominion yet), passes 3-5: the blocked top 19 has the new
SCC {3, 5, 6, 10, 11, 12, 16, 19}, with escapes, merging the stored tangles {5, 10, 11, 16, 19} (learned at 19 in pass 2)
and {3, 6, 12} (learned at 12 in pass 2). It is never extracted: in search 2 the piece's context has changed (|R| 17 → 13).
So case (c) of Lemma L-epoch is real at the level of sptl; what remains DATA only is that a catch-up has never been LEARNED
at an unchanged context (115 / 110 same-piece pairs above).
Consequence for gate (O) in C6 (R10's 2CE). The carry must be learned at P1 within one A-state (R10 (F), (G)). By Lemma
L-epoch the search that learns it is (a) a growth of V*_{P1}, (b) a lift of a tangle learned after P1 in the previous search
(for a gate tied to the fast level: its LAST tangle, and no earlier one), or (c) a catch-up at P1. Kind (c) needs no
input from the fast level at all: a catch-up chain at P1 is a self-running DELAY, one step per search, which a counter
could use as a timer if its length can be made to match the fast level's. None of (a)-(c) is excluded by proof ((CU), which would have excluded (c), is false). OPEN.
The LIFT gate in C6 (09:45Z, PROVED from Lemmas D2, D3, L-epoch; the Lead routed the lift to L-RED as an attack on
A_DTL, and sptl is the same in C6, so this applies to both once V*_{P1} is fixed): (i) within one A-state, P1 admits at
most |R_{P1}| lifts, each growing Dom(P1) strictly; (ii) a lifted tangle's vertices stay in Dom(P1) for the rest of the
A-state (Lemma D3), so they leave the context of every later piece, the fast level's included; (iii) a tangle learned
after C_B is lifted into P1 only if none of its escapes lies in C_B's attractor or elsewhere in R_{P1} outside P1's regions
(escapes there are in R and uncovered at P1). So a lift gate tied to the fast level's LAST tangle needs that tangle to have
no escape in C_B's attractor while every earlier fast tangle keeps one there (else it is lifted early, by (ii) eating
vertices of the fast level). This is a constraint on the attack, not an obstruction; OPEN.

## 10. Barrier for this proof route: an abstract piece process with exponentially many searches (09:53Z; Lead go 09:52Z)
Label: a BARRIER for proving GAP-A from the properties proved so far. NOT a lower bound for DTL: nothing here is a game.
Status: the model and the table are PROVED (by inspection of the definitions); "(F) is what it violates" is a READING.

10.1 The model APP(k). Vertices z and x_i^0, x_i^1 for i = 0..k−1 (n = 2k + 1), all of p-parity priority. Possible tangles
t(c) := {z} ∪ {x_i^{1−c_i} : i < k} for c ∈ {0,1}^k (2^k distinct vertex sets). A state is a set T of such tangles. For a
prefix c ∈ {0,1}^i define the digit r(c, T) := 1 iff t(c·0·1^{k−i−1}) ∈ T.
One search under T (depth 0 only; there is no recursion):
- for i = 0..k−1 (the LEVEL pieces): with c_0 := ε, b_i := r(c_i, T), c_{i+1} := c_i·b_i, piece i has context
  R_i := {z} ∪ {x_j^{1−b_j} : j < i} ∪ {x_j^0, x_j^1 : j ≥ i}; its pruning result is −1 with return set {x_i^{b_i}}, from the
  profile d(x_i^0) = 2, d(x_i^1) = 1 + 2·b_i, every other p-vertex of R_i at distance 1 (so the maximum leapfrogs from x_i^0
  to x_i^1 when b_i turns 1); its removed set is D_i := Dom({x_i^{b_i}}) := {x_i^{b_i}};
- piece k (the BOTTOM piece): context R_k = t(c_k) (the leftovers), result stable with V* = R_k, removed set D_k := R_k; its
  sptl learns the tangle t(c_k) if it is new.
The phase starts with T = ∅ and runs searches until one learns nothing. Learning t(c) with c = p·0·1^m flips the digit of
level i = |p| in context p (r(p, T) becomes 1); every deeper level gets a fresh context p·1·… whose digit is 0. This is a
binary counter with level k−1 as the least significant digit: the states 0^k, …, 1^k are visited once each, so the phase
has 2^k + 1 searches and 2^k tangles on n = 2k + 1 vertices.
Checked by simulation: experiments/alg/app_model.py (in check.sh for k ≤ 6; k = 10: n = 21, 1,025 searches) asserts the
trace-checkable axioms of 10.2 (counts, one tangle per search, at most one upward profile change per context, first
differences are upward changes at equal contexts driven by the previous search's bottom tangle, bottom contexts never recur).

10.2 Every proved property next to the axiom of APP(k) that satisfies it (for a referee to check the encoding).
| proved property (where) | how APP(k) satisfies it |
| --- | --- |
| Lemma W, DTL-proof.md §3(a): one extraction per top per search, so ≤ n tangles per search | one tangle per search, at one top of piece k |
| D2(d), §3(d): a search that learns nothing (and finds no dominion) ends the phase | the phase ends at the first search without a new t(c) |
| R_{j+1} = R_j \ D_j; D_j a function of (R_j, X_before, result, T) (C5-DTL.md §2) | R_{i+1} = R_i \ D_i with D_i = {x_i^{b_i}} |
| Fixed-context monotonicity: C6 Lemma 2.1 (A_DTL under Theorem M-cond, §3) | at context R_i (i.e. prefix c_i) the profile changes once, upward: d(x_i^1) 1 → 3 |
| −1 result = last survivors; argmax re-cut when the maximum moves (GAP-A-data F7; leapfrog, §6) | return set {x_i^0} → {x_i^1} when d(x_i^1) passes d(x_i^0) |
| Contexts change only through results (DATA, §6.1) | each R_i is a function of the earlier results |
| First-difference argument (§4d CARRY half; §6 driver lemma): a result at an equal context changes only if a NEW tangle fires there | b_i changes only when t(c_i·0·1^{…}) is added |
| Driver lemma (§6, PROVED with D2): the driver of a level-j change is learned at a piece ≥ j in the previous search | the driver of every level change is learned at piece k ≥ i |
| Lemma D2 (§6): learned tangles lie in Dom(V*, R) ∪ X_before | t(c_k) = R_k = D_k |
| Lemma D3 (§9): Dom monotone in V*, T at fixed (R, X_before) | D_i is constant while b_i is; D_k's contexts never recur |
| Lemma L-epoch (§9): within an epoch of a stable piece, learning needs V* growth, a lift or a catch-up | every epoch of piece k is a single search (2^k distinct contexts, each visited once) |
| N_j ≤ K·C_j (§6 refinement) | C_i = 2^i distinct level-i contexts, K = 1 change per context |
| Lemmas 2.2, E, P*-inv, M-cond, N; (r1) §7 | no deficits: the actual and the ideal pruning coincide (U = Û) |
| Termination, D2(c) (pieces per search ≤ n) | k + 1 pieces per search |

10.3 What APP violates that DTL might satisfy: the FRONTIER property (F).
(F) "A tangle that changes the result of a −1 or cut piece i between consecutive searches (pieces < i unchanged) is
learned in the first STABLE piece after piece i, i.e. in a context determined by the results of pieces ≤ i."
L-RED's R10 (F) argues it for cut-eaten levels (READING): the driver's escapes are covered in the cut of search s+1
without other new tangles, so in search s they are already outside R after the cut, its top is never a candidate, and the
first call after the cut is stable and learns it. APP violates (F) maximally: every driver is learned at the bottom piece,
whose context encodes every digit, and there is no stable piece between levels. If (F) held for every piece type, the
driver of level i would be learned in a context that does not see the deeper digits, so the carry from level i+1 to level
i would need a GATE at that stable piece that opens exactly when the deeper levels are exhausted: R10's (S)/(O)/lift
analysis, where C6 excludes (S) (§8) and R10 finds (O) failing in 2CE. That is where a polynomial bound could come from.
Status of (F) for −1 pieces with Q empty (Dom(prevV)), the level type APP uses: NOT implied by R10's argument (READING). The
driver's escapes are covered in piece i's pruning in search s+1 by regions of tops at some round r; with the old tangles
those regions are the same in search s, but only the return set's Dom is removed after piece i, so escapes in the regions
of the OTHER tops stay in R_{i+1} and the driver can be learned deeper, as in APP. So (F) for Dom(prevV) pieces is the
open property; proving it would rule out APP-like counters, and refuting it means building APP.
DATA (09:58Z; counts corrected 09:59Z after an analysis bug: the first run took the search number from list.index, which
returns the first EQUAL trace entry; fixed in experiments/alg/dtl_frontier.py; A_DTL, stable order; 500 random games n ≤ 24,
every dtl_* instance, tc+ N ≤ 5): drivers of changes at −1 pieces between consecutive searches: 169 (every change has one);
learned at the first stable piece after the changed piece 144; inside the recursion of a cut BEFORE that stable piece 15;
at a LATER stable piece 10 (dtl_deficit_n20: change at piece 0, a Dom(prevV) piece, drivers learned at piece 3, the second
stable piece; dtl_mviol_n20: change at piece 5, first stable piece 7, drivers learned at piece 9). So (F) is FALSE for A_DTL
as stated: drivers learned beyond the frontier occur in real runs, one step deep, not as a counter. The property a proof
would need is therefore weaker than (F) and quantitative (how deep, how often), or a different one.
Split by piece type and reconciled with L-RED (10:02Z; Lead 10:00Z; l-red ed14e43 R10 "Driver LOCALITY",
experiments/red/carry/drivers.py). My drivers are tangles that fire in the changed piece's PRUNING. At Dom(prevV) pieces
(−1, Q empty): 71 changes, 136 drivers, 8 learned at a later stable piece; at cut pieces (−1, Q nonempty), pruning-driven
changes: 21, 33 drivers, 2 learned later. L-RED's (F) 67/67 concerns drivers that fire in the CUT's attractor
(cut-driven carries), a different event; its 169 "later" drivers (116 files) are pruning-driven at domfirst pieces, as
here. Consistent reading: (F) holds for cut-attractor carries (L-RED's data and R10's argument) and FAILS for
pruning-driven changes, which is exactly the level type APP(k) uses (its digit lives in a Dom(prevV) piece's return set and
is advanced by a tangle learned after the deeper levels have run). So the property a polynomial proof needs is not (F) but
a bound on pruning-driven carries at −1 pieces.

10.4 For L-RED (realising APP(k) as a game; the model fixes what each piece must do, not the gadgets):
(1) level i: two p-priority tops whose pruning distances at piece i leapfrog exactly when the deepest-zero tangle arrives,
and a −1 result with Q empty (no vertex of R_i may attract into X, else it is a cut and R10's (F) applies);
(2) the bottom piece learns, in every state, a NEW tangle whose vertex set encodes the state (the leftovers);
(3) that tangle must fire at piece i* (the deepest zero) in the next search and change nothing at pieces < i*: its vertices
are present there too, so some escape must be uncovered at every piece < i* and covered (or forgiven) at piece i*. A
removed top is always in the union of regions while it survives, so the escape forgiven at i* should be a NON-top vertex
of D_{i*−1} = Dom({x_{i*−1}^{b}}), and it must lie outside every region at the pieces above.
(4) L-RED's MIRROR reading (l-red f954923, R10 "Outside 2CE"; READING): without a deficit, a pruning-driven carry at a
Dom(prevV) piece must be SELF-REINFORCING (from some round on, an escape of the driver is covered only by vertices the
driver keeps alive), else its top survives at that piece in the learning search, is removed by that piece's Dom, and is
never learned deeper. APP does not model escapes, so this is no contradiction; it is the shape APP's level drivers must
have, and if (M1) is proved it becomes an axiom APP must carry (then APP needs a self-reinforcing driver at every level).
(5) (10:23Z, from section 11) In APP as written, t(c) contains the vertex x_{i*}^1 it rescues, so the rescued vertex has
priority ≤ the driver's top. In the data, a carry whose top is already pruned rescues only candidates ABOVE its top
(17/17). A realisation should therefore either keep the rescued top outside the driver with the driver's top below it (a
cap carry), or make the rescued vertex the driver's own alive top (a self-reinforcing carry, MIRROR (M2)).

## 11. Pruning-driven carries: MIRROR tested, and the class it misses (10:17Z; Lead 10:07Z retarget)
Question (Lead): a bound on PRUNING-driven carries at −1 pieces, starting from L-RED's MIRROR reading (l-red f954923, R10
"Outside 2CE"): with no deficit, a carry C (top h, learned in search s after piece i) that changes piece i's pruning in
s+1 is either impossible (M1) or self-reinforcing (M2). Tool: experiments/alg/dtl_mirror.py, on the IDEAL pruning (C6
prototype), where MIRROR's no-deficit premise holds by construction. For every change at a −1 piece i between consecutive
same-player searches (no dominion, equal context): r0 = the first round whose ideal survivors differ; DRIVERS = tangles
learned in s whose removal undoes the change of round r0 (from the same round-(r0−1) set); h = top(C) (maximum priority).
DATA (300 random games n ≤ 22, every dtl_* instance, tc+ N ≤ 5; tangle parity taken at birth, see the script):
| | cut pieces (−1, Q nonempty) | Dom(prevV) pieces (−1, Q empty) |
| --- | --- | --- |
| changes | 20 | 69 |
| drivers with h ALIVE at r0 in s | 7 | 7 |
| of which h survives round r0 in s (MIRROR's "redundancy" step) | 7 | 7 |
| of which self-reinforcing (coverage of C's escapes in s's sets below pr(h) fails before h's death in s) | 7 | 7 |
| drivers with h already PRUNED before r0 (in s and s+1) | 7 | 10 |
| of which every rescued candidate has priority > pr(h) | 7 | 10 |
Changes with no single-tangle driver (several new tangles needed together) are not classified here.
Reading.
- Alive-top drivers: MIRROR's chain holds on all 14: redundancy (h alive and C's escapes covered ⇒ h survives) never
  fails, and every such carry is self-reinforcing (M2). MIRROR's (M1) argument is complete for this class modulo the
  redundancy step, which is a reading: for a singleton tangle {h} it is immediate (h's successors are h and C's escapes);
  for a larger C it needs C's cycles that avoid h to be rebuilt from tangles that exist at piece i in s, and sub-tangles
  learned in s itself (11 drivers contain one) are not there yet. Not proved.
- Dead-top drivers: 17 of the 31 identified drivers act AFTER their top was pruned (R10 interim 1, case (i)); MIRROR's
  first step ("h is not a candidate at r0 in s, so death_s(h) ≥ r0 + 1") does not apply to them, and nothing in MIRROR
  constrains them. In the data each of them rescues only candidates of priority above pr(h): the CAP effect (C is lifted
  into a set of a higher level or into a threshold attractor at t ≥ pr(h), where its vertices let higher candidates through).
  Partly forced: a carry that acts through the threshold loop below pr(u) and whose top is not yet in the set must have
  pr(h) < pr(u); a lift into a higher level's Û could in principle rescue a lower candidate, which the data never shows.
- So the class a bound must handle is: self-reinforcing alive-top carries, PLUS dead-top cap carries. MIRROR handles
  neither as a bound; it only shows that non-self-reinforcing alive-top carries do not occur.

## 12. Where the GAP-A route stands: the hypotheses still needed (10:20Z)
Child resets are real (DATA, experiments/alg/dtl_childmono.py; 400 random games n ≤ 24, every dtl_* instance, tc+ N ≤ 5):
after a change at depth-0 piece j between consecutive searches, the death rounds at piece j+1 DROP for some vertex present in
both child contexts in 4 of 38 comparisons (A_DTL and C6 alike; dtl_replay4_n32 after a root change: 3 → 1, 4 → 2,
4 → 3), rise in 21; at deeper pieces 0 drops in 14 comparisons. So "a vertex's death round at a level never decreases" is
DEAD as a cross-context potential, and the reset that APP(k) needs at a fresh child context does occur in real runs.
A polynomial bound on searches per phase along the route of sections 6, 10, 11 needs ALL of the following; none is proved:
(H1) cut-attractor carries obey the frontier property (F) (R10's argument, READING; data 67/67, L-RED);
(H2) a polynomial bound, across contexts, on PRUNING-driven carries at −1 pieces, in both classes of section 11:
     (a) self-reinforcing carries whose top is alive (MIRROR's (M2) shape; MIRROR's (M1) excludes the others modulo the
         unproved redundancy step), and
     (b) dead-top cap carries (a tangle acting after its top was pruned, lifted to rescue higher candidates);
(H3) a polynomial bound on catch-ups (Lemma L-epoch (c); (CU) is false) and on learning inside cut recursions (the same
     piece-tree structure one level down);
(H4) for A_DTL only: a polynomial bound on deficit-triggered changes at fixed contexts (Lemma E's straddle with lower pickup,
     real: dtl_mviol_n20); for C6 this item is void.
With (H1)-(H4) the counting of section 6 collapses: every transition is a pruning-driven change (H2), a cut-driven change
(H1: driver learned at a prefix-determined piece, so the carry needs a gate there, R10), a catch-up/recursion step (H3), or
a deficit (H4), and APP(k) is excluded because its every level is a pruning-driven carry (H2). Without them, APP(k) shows
that the proved facts allow 2^Θ(n) searches. Status: GAP-A OPEN; the route is (H1)-(H4).

## 11b. (H2b): a candidate potential for dead-top cap carries (10:34Z; Lead 10:22Z/10:25Z: statement and data before proof)
Data set for this section (experiments/alg/dtl_mirror.py, MIRROR_NMAX=30): every file in experiments/alg/instances, the
climbed games of this session (copied to experiments/alg/instances/climbs_1016/, 22 files), tc+ N ≤ 6, counter_* families, 800 random games n ≤ 30; ideal (C6)
runs; 449 changes at −1 pieces (347 at Dom(prevV) pieces, 102 at cut pieces).
- Φ (DEAD). R(u) := the maximum death round of u in the ideal pruning of any depth-0 −1 piece of the phase so far. "Every
  dead-top cap carry at a Dom(prevV) piece raises R(u) for some rescued u" fails 15 times in 258
  (experiments/alg/instances/cross_h_k1_n11_m17_37.pg, n = 11, search 1, piece 0: the rescued vertex reaches death 3,
  equal to its record from another −1 piece of the same search; siblings cross_h_k1_n12_m18_13 / _18). The record over ALL
  pieces is dead outright (rescued vertices already survive some stable piece).
- Φ_idx (CANDIDATE, 0 counterexamples). R_i(u) := the maximum death round of u in the ideal pruning of depth-0 piece INDEX i
  over the searches of the phase so far whose piece i returned −1 (a stable result counts as ∞). Values lie in
  {0, …, n+1, ∞} and there are ≤ n indices, so the R_i admit at most n²(n+2) raises per phase. Φ_idx: every dead-top cap
  carry at piece i raises R_i(u) for some vertex u it rescues. Data: dead-top carries whose piece stays −1: 142/142 raise
  R_i (103 at Dom(prevV) pieces, 39 at cut pieces, including the replays of dtl_replay4_n32 and dtl_replay2deep_n32); 157
  more turn the piece stable (a trivial raise). If Φ_idx holds, dead-top cap carries number ≤ n²(n+2) per phase, which is
  (H2b). Shifting a level to another index does not escape the bound.
- Φ_idx does NOT hold for alive-top carries: at cut pieces 23 of 38 that stay −1 raise no R_i (at Dom(prevV) pieces 1 of
  8). These are the self-reinforcing carries of section 11, MIRROR's (M2), and the class where the real replays live; (H2a)
  stays open.
- APP(k) violates Φ_idx at the second flip of any level (x_i^1 goes 1 → 3 at index i in every fresh context). An APP made
  of dead-top cap carries would have to raise the rescued vertex's death at that index every time.
- Status: CANDIDATE, DATA only, routed to L-RED as an attack target (10:33Z). No mechanism known: deaths at one index in
  different contexts are not comparable in general.
- Two candidate mechanisms for Φ_idx, both FALSE (10:40Z, same data set, dtl_mirror.py "lifts_to_max" / "maxdeath_monotone"):
  (a) "a dead-top cap carry lifts some rescued vertex to the current maximum death of its piece, or makes the piece stable":
  fails 80 of 258 at Dom(prevV) pieces and 22 of 41 at cut pieces (alive-top: 8/52 and 38/39 fail). (b) "the maximum death
  at a fixed piece index never decreases across the searches of a phase": decreases in 201 of 2540 consecutive pairs (first:
  search 1, piece 2, ∞ → 3, i.e. a stable piece turns −1 with max death 3). So Φ_idx is not the shadow of a monotone
  per-index depth; its raise is per vertex, and no mechanism is known. Status unchanged: CANDIDATE, DATA only.
