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
CORRECTION (10:58Z; L-RED l-red 6a98d48, R13 last section; Lead 10:59Z, checked in dtl.cpp @8fbf0a7 lines 897-915; checked
here in experiments/alg/dtl_pyref.py search_rec). The −1 branch's threshold scan ("does R attract into X") never reads V.
When it finds a vertex, the piece CUTS: attractor Z at threshold t, X ∪= Z, R loses Z (tattr consumes from R), and the
recursion runs on Z. V is read only in the other branch, Dom(prevV). So the state of a depth-0 piece is
(R_j, res_j, V_j) at a stable or Dom(prevV) piece and (R_j, −1, D_j) at a cut piece, where D_j = R_j \ R_{j+1} is
the full set the cut removes. (11:23Z: the child call's R is NOT enough. The cut moves the threshold-priority part of
the attractor into X, so equal child sets can come with different D_j. The 10:58Z version used the child's R.) A −1 → −1 V change at a cut is
a PHANTOM, and attractor growth at an unchanged V is a real change. The LEVEL of a transition is the first j whose
corrected state differs. Counts in this file measured with (R, res, V) at cut pieces carry that error; the corrected
counts are in §11c. The counting argument above is unchanged in form; only the state it counts changes.
RE-MEASURED (11:24Z; experiments/alg/dtl_pieces.py e41ccfb + this commit). The old tracer had a bug: it never
restored the depth after a cut's recursion, so every depth-0 piece after the first cut went unrecorded. On every
experiments/alg/instances/dtl_*.pg, climbs_1016 and 600 random games n ≤ 24 (tc+ not re-run; no generator call in this
script), there are 640 games:
- old tracer: DTL 211 transitions with a depth-0 level (+116 "same"), C6 208 (+113); replay histogram max (depth 2,
  3 replays, dtl_replay2deep_n32); 17 games with a replay.
- fixed tracer, child-R cut state (10:58Z definition): 25 NEST transitions (context at the level shrank with an equal
  previous piece), all right after a cut. That is an artefact of the child-R state.
- fixed tracer, removed-set cut state (definition above): DTL 275 (+52 same), C6 270 (+51), NEST 0, FRESH 0. The
  6.1 DATA line ("contexts at the level are equal") HOLDS on the corrected count. Replays: 19 games, max (depth 2,
  5 replays) at climbs_1016/nest_nest_s81.pg.
6.1 Facts.
- (DATA, 0 exceptions) Contexts change only through results: at the level of every transition the two contexts are EQUAL
  (DTL 57 and C6 55 transitions with a depth-0 level on 600 random games n ≤ 24, every instance in experiments/alg/instances
  and tc+ N ≤ 5; experiments/alg/dtl_pieces.py). Equal (R_{j−1}, res, V) with a grown D_{j−1} (Dom or cut attractor grown by new
  tangles) would break this; it never happened. Not proved. [SUPERSEDED: these counts came from the buggy tracer and
  the old state (V at cuts). Corrected counts: RE-MEASURED paragraph above, which shows the same conclusion.]
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
6.3 [SUPERSEDED: old state (V at cuts) and the buggy tracer; corrected replay counts in the RE-MEASURED paragraph above]
Measured replay structure (experiments/alg/dtl_pieces.py; replay depth = 1 + depth of the opening change when
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
[NOTE 11:59Z: the data below (experiments/alg/dtl_frontier.py) finds the change level with the OLD piece state (V read
at cut pieces, §6 CORRECTION). Its tracer restores depth correctly, so it does not have the dtl_pieces bug. Phantom V
changes at cuts may be counted among the cut-piece changes. Not re-run (Lead 11:13Z: re-run only if an argument depends
on it).]
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
[SUPERSEDED counts: the first paragraph below used the buggy tracer (pieces after the first cut unrecorded); corrected
counts in §15.] Child resets are real (DATA, experiments/alg/dtl_childmono.py; 400 random games n ≤ 24, every dtl_* instance, tc+ N ≤ 5):
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
- Refinement (d), DATA (10:51Z, same data set, dtl_mirror.py 6312d50): in every dead-top cap carry whose piece stays −1,
  the HIGHEST rescued vertex (by priority, then index) is one that raises R_i: 142/142 (103 Dom(prevV), 39 cut). A proof
  may therefore follow the top rescued vertex u*. pr(u*) > θ ≥ pr(an escape above h) (R12 §8). (c), "every rescued vertex
  dies later than in the previous search", also holds 142/142. It is close to the definition of "rescued" (pruned at r0
  in s), so it carries no information about other contexts and is not evidence for Φ_idx.
- L-RED R13 near miss (experiments/red/carry/instances/phi_flat_alive_n32.pg, trunk 976cf2b), reproduced here.
  phi_drivers.py 5 1 on trunk: r0 = 1, same context, one driver t16 (top 7, pr 22) alive_survives_r0, rescues vertex 6
  (pr 20), not a cap carry. dtl_mirror.py (C6) on the same game: 10 changes at −1 pieces. The 4 dead-top carries all
  raise R_i, and the top rescued vertex raises it in each. 1 alive-top cut carry raises no R_i. That is the alive-top
  class (H2a), which Φ_idx does not cover (23/38 at cut pieces above). The near miss confirms the gap is in (H2a): it is
  not a Φ_idx counterexample.

## 11c. Φ_idx with the corrected piece state, and a data check of R12 §9 (11:01Z; Lead 10:59Z)
Same data set as §11b (experiments/alg/dtl_mirror.py at this commit, C6, MIRROR_NMAX=30, 800 random games). LEVEL now uses
the corrected state of §6 (cut piece: R, −1, attractor; STATE_V=1 gives the old count).
- Transitions at a −1 piece at an equal context: 347 (was 449). 329 of them are at Dom(prevV) pieces (was 347). The level moves in
  both directions: some old Dom(prevV) levels now sit behind an earlier cut-attractor change, and some real Dom(prevV)
  changes were hidden behind a phantom V change at a cut (dead-top carries there: 273, was 258). 18 are at cut pieces whose result type
  changes, and 56 are CUT-ATTRACTOR changes (same R, attractor grown), now counted separately as (H1)/(F) territory. Example:
  dtl_cu_viol_n24 search 3, piece 1, attractor 2 → 17 vertices.
- Φ_idx restated for Dom(prevV) pieces only (V is real state there). Every dead-top cap carry raises R_i(u) for some
  rescued u: 273/273. 115 stay −1, and in each of them the HIGHEST rescued vertex raises R_i (115/115). 158 turn the
  piece stable. Alive-top carries at Dom(prevV) pieces: 1 of 9 that stay −1 raises no R_i (unchanged class, (H2a)).
  Status: CANDIDATE, DATA only.
- R12 §9 (C-a) as stated is FALSE on data. "The carry fires at a threshold θ ≥ pr(e) for an escape e with pr(e) > pr(h)":
  12 dead-top carries (7 + 5 at Dom(prevV) pieces) have NO escape in R above pr(h). Smallest: dtl_proof_c3.pg, search 1,
  piece 0. The tangle {y, s} (top y, pr 2) has one escape in R, w (pr 1). The rescued vertex is z (pr 6). Covering w needs
  the threshold of x (pr 3) on its attraction path. The correct form is: covering some escape needs a threshold
  θ > pr(h), and that threshold may come from a vertex on the escape's attraction path rather than from the escape itself.
  This is a statement, not checked beyond this case.
- R12 §9 (C-c), first bullet ("piece i's own Dom cannot remove e"), FAILS on data in 17 cases (15 Dom(prevV), 2 cut). In
  search s, a high escape of C left R at piece i itself (e ∈ R_i, e ∉ R_{i+1}) and is outside R_P at C's learning piece
  P > i. Example: cross_h_k1_n10_m16_27.pg, search 1, piece 0, tangle 0 (top 2, high escapes 4 and 9). A likely reason
  is that §9's step "Dom(M_i) ⊆ piece i's final-round region" needs the reverse of Lemma D3's inclusion (Dom ⊇ regions;
  Dom's target X admits partly removed tangles, §9). Not checked further. In every other dead-top carry with a high escape,
  P > i and the escape left between i and P or lies in R_P (consumed at P): 224 + 1 all outside R_P, 36 with some in R_P.
  P ≤ i never occurs at Dom(prevV) pieces.

### 11c.1 What the Φ_idx data actually tests (11:09Z)
- Lemma F (fixed-context raise, C6; PROVED). Take one phase and depth-0 piece index i. Let s → s+1 be a transition with
  level i at a Dom(prevV) piece with the same context R, first differing round r0, and a driver C learned in s after
  piece i ran (so C ∉ T_s(i)). Then every vertex u that C rescues has d_s(u) = r0 < d_{s+1}(u). Also d_{s0}(u) ≤ d_s(u)
  for every earlier search s0 of the phase whose piece i has context R. So u raises its record over the SAME-CONTEXT
  searches at index i, whatever the driver's top status.
  Proof. Within a phase G is fixed, so the alive tangle set only grows: T_{s0}(i) ⊆ T_s(i) ⊆ T_{s+1}(i) \ {C}. By
  Lemma 2.1 and induction over rounds (the line-105 argument), V̂_r(R, T) is monotone in T for every r. Hence
  d_{s0}(u) ≤ d_s(u). The rounds of s and s+1 agree before r0, so u ∈ V̂_{r0−1}. Since u ∉ Ŝ(V̂_{r0−1}, T_{s+1} \ {C})
  ⊇ Ŝ(V̂_{r0−1}, T_s) = V̂_{r0}(T_s), d_s(u) = r0. And u ∈ V̂_{r0}(T_{s+1}), so d_{s+1}(u) > r0. □
- So the whole content of Φ_idx beyond Lemma F is the CROSS-CONTEXT case: the record to beat comes from a search whose
  piece i had a different context. DATA (same data set, dtl_mirror.py (f)), for the 115 dead-top cap carries at Dom(prevV)
  pieces that stay −1: in 113, NO earlier search of the phase has a −1 Dom(prevV) piece at index i in another context. In
  the other 2, u*'s other-context record is ≤ its same-context record. So the cross-context case is never exercised: 0 of
  115 have a binding other-context record. The 115/115 and 273/273 figures are evidence for Lemma F, which is proved, and
  NOT for Φ_idx's cross-context claim. That claim is exactly what an APP double flip needs (the same index, a new context,
  the same death round), and it is untested by this data set.
- Status of Φ_idx: same-context part PROVED (Lemma F, C6). Cross-context part UNTESTED. I withdraw "142/142 support" as
  support for the cross-context claim. Lemma F alone gives only the known per-context bound, so it gives no global bound.

### 11d. Φ_idx is FALSE: a cross-context counterexample (11:19Z)
Instance: experiments/alg/instances/phi_idx_flat_n20.pg (n = 20). A climb (scratchpad xclimb.py, fitness = violations of
the restated Φ_idx) found it in 190 steps from phi_idx_cutrec_n20.pg. Oink A_DTL: 11 tangles, 5 iterations, 1 dominion,
solution verified. dtl_pyref (A_DTL) and C6 give the same counts (5 / 11), and dtl_deficit.py finds 0 deficit calls, so
A_DTL and C6 coincide at depth 0 here. Vertex names below are ORIGINAL ids of the .pg file (corrected 11:46Z;
the 11:19Z text used internal indices, where internal 3 = original 17, internal 10 = original 19, internal 14 = original 14).
Conventions: V_0 is the initial candidate set and V_r the set after r pruning rounds; a vertex has death d when it is in
V_{d−1} and not in V_d. The −1 return set is the last nonempty V_r. L-RED's "round-6 set" is V_5 here.
- Phase of player 0, depth-0 piece index 2, every listed piece a Dom(prevV) −1 piece. Contexts: s1 |R| = 16; s2 |R| = 18;
  s3 and s4 equal, |R| = 17, with three different contexts in all.
- Death rounds at index 2: vertex 14 dies at 6 (s1), 5 (s2), 5 (s3), 6 (s4); vertex 19 at 7, 6, 6, 7.
- Transition s3 → s4: same context, first differing set V_5 (r0 = 5): {17, 19} → {14, 17, 19}. Then V_6 = ∅ in s3
  and {19} in s4, so the −1 return set goes {17, 19} → {19}. Tangles 7, 8, 9 are new since piece 2 of s3; all were
  learned in s3 inside the cut recursion of piece 3. Driver test at r0 = 5: only tangle 9 (vertices {1, 2, 5, 9, 10, 16},
  top 5, priority 16, top dead at round 2 in s3) is a driver. Removing it undoes V_5 and adding it alone suffices;
  tangles 7 and 8 are neither. This agrees with L-RED's independent A_DTL check (l-red 17db195: one driver t9 rescuing
  14). Dead-top cap carry: the rescued vertex 14 (pr 20) dies at 6 and so only EQUALS its record 6 from s1 (another
  context). Vertex 19 rises to 7, which equals its record 7 from s1. No vertex raises its index-2 record, whether records come from Dom(prevV) pieces or from
  all −1 pieces. The same flat change is a counterexample to L-RED's "flat" (any vertex) as well.
- Status: Φ_idx (original and restated) FALSE. The obstruction is exactly the untested cross-context case of §11c.1: a
  context visited earlier at the same index set a record that a later context's carry only reaches. Lemma F still holds:
  14 rises 5 → 6 against its same-context record. Earlier instance: phi_idx_cutrec_n20.pg. It breaks only the original
  definition: its records come from cut pieces at index 1 (deaths 6 and 5), and two consecutive Dom(prevV) carries at a
  new context reach 5 and 5.
- What this does NOT show: an exponential run, or a failure of a weaker potential (e.g. record raised within two carries,
  or a lexicographic record over (index, context class)). One flat change costs nothing asymptotically. The n²(n+2)
  bound needs every carry to raise, so (H2b) is again OPEN with no candidate potential.

### 11d.1 Second cross-context counterexample: nest_nest_s84 (11:34Z; L-RED R13 08599bf case, Lead 11:09Z)
experiments/alg/instances/climbs_1016/nest_nest_s84.pg, transition s13 → s14 (1-based searches), depth-0 piece index 1,
Dom(prevV) −1 piece with the same context (|R| 29). r0 = 5, and the return set grows {2, 27} → {2, 27, 30}. A_DTL and
C6 have the same trace here, and dtl_deficit finds 0 deficit calls. So it is not a deficit. It is not a catch-up either:
the drivers are learned in s13.
- Why "no driver": tangles 26, 27, 28 (all learned in s13 at piece 5) are REDUNDANT drivers. Each ALONE, added to the
  s13 set, gives the s14 round; removing any one leaves the others to do it, and only removing all three undoes the
  change. The single-removal driver test (dtl_mirror.py, L-RED's phi_drivers.py) reports no driver. That is an artefact
  of the test, not a new mechanism.
- Classification by sufficient singletons: tangle 26 (top 24, pr 26) is DEAD at r0 (24 ∉ V_4) and rescues 30 (pr 30):
  a dead-top cap carry. Tangle 27 (top 28) and tangle 28 (top 30) have alive tops.
- Φ_idx: vertex 30's index-1 death at Dom(prevV) pieces is 6 in s9-s12 (context |R| 31), 5 in s13 and 6 in s14
  (context |R| 29). The carry only reaches the record from another context: a second cross-context counterexample, of
  the same shape as §11d. It was in the §11b-§11e data set but went uncounted, because single-removal found no driver.
- Tool consequence: the driver counts of §11-§11e undercount redundant driver sets. A sufficient-singleton test is
  needed; not yet re-run.

### 11e. Re-run with the removed-set cut state, and what (H2b) reduces to (11:29Z)
- dtl_mirror.py with the cut state D_j = R_j \ R_{j+1} (§6), on the §11b data set plus the two new phi_idx instances:
  354 changes at −1 pieces with an equal context (336 at Dom(prevV) pieces, 18 at cut pieces), and 89 cut removed-set
  changes counted apart (was 56 with the child-R state). Dead-top cap carries at Dom(prevV) pieces: 286, of which 128
  stay −1. 127/128 raise the restated (Dom-only) record; the 1 exception is phi_idx_flat_n20 (§11d). Cross-context:
  124 have no other context at the index, 3 dominated, 1 binding (that same instance). Every §11b/§11c qualitative
  statement stands.
- Climb (scratchpad xclimb.py seed 93, n = 20, fitness = restated-Φ_idx violations): 5 flat dead-top carries in one
  phase out of 6 that stay −1, within 7,804 steps. Flat carries are not rare once the climb selects for them.
- Reduction (PROVED from Lemma F). In a phase, the number of dead-top (indeed all) carries at Dom(prevV) pieces of index
  i is ≤ n(n+2) · c_i, where c_i is the number of distinct Dom(prevV) contexts at index i in the phase. Each carry raises
  the same-context death of a rescued vertex, and deaths lie in {1, …, n+1} ∪ {∞}. So (H2b) follows from a polynomial
  bound on c_i (the converse is not claimed). That is §6's fresh-context question again. Φ_idx was the attempt to avoid
  it, and §11d shows it cannot be avoided this way. No new route; (H2b) OPEN.

## 13. (H4): deficit-triggered changes at fixed contexts, A_DTL (10:47Z; Lead 10:22Z "then (3) deficits")
Tool: experiments/alg/dtl_deficit.py (61fb52c). At every depth-0 piece of an A_DTL run it also computes the ideal (C6 rule)
result on the same tangle set and context. A change between consecutive searches of a phase is DEF (deficit-triggered)
when the ideal (result, V) at its first-difference piece is the same in both searches and the actual one differs. It is
LRN when the ideal result moved too. The first-difference piece always has the same context, because R_j is fixed by
pieces 0..j-1; measured ctx_changed = 0.
- CORRECTED 12:21Z (L-RED l-red 2bb9d89, R15 §1; reproduced here with this file's unmodified dtl_deficit.py on
  experiments/red/carry/instances/h4_notweaker_n20.pg: NOT_weaker = 1). The 10:47Z claim "V_actual ⊆ V̂, and an
  ideal −1 forces an actual −1" was too strong. What is PROVED (Lemmas 2.1, 2.2, line-105 induction) is the PER-ROUND
  inclusion V_i ⊆ V̂_i for every round i, with V_i = ∅ after the actual run has emptied. Consequences that ARE proved:
  an actual stable V* ⊆ V̂*; an ideal −1 forces an actual −1 (if V̂_i = ∅ then V_i = ∅); and the actual run empties no
  later than the ideal one. NOT proved, and FALSE: the −1 RETURN set (the last nonempty round) satisfies
  V_actual ⊆ V̂_return. The actual run can empty a round EARLIER (round 6 vs 7 there), so its return set is an earlier
  round's set. In h4_notweaker_n20: actual −1 with {8, 9} (internal ids), ideal −1 with {8}. L-RED's second climb has
  disjoint return sets.
- [MARKED 12:21Z: the "13/13 weaker" line tested the false return-set form (the dtl_deficit.py 'weaker' test compares
  return sets). It is not evidence for anything proved.]
- DATA (every file in experiments/alg/instances, climbs_1016, 1,500 random games n ≤ 28; 1,629 games). Deficit calls: 13 of
  9,858 depth-0 calls. Changes: 365, of which 5 are DEF and 360 LRN. At most 1 DEF per (piece, context), and at most 2 per
  phase (dtl_mviol_n20.pg). Directions: 3 up (−1 → 1, or V grows); 0 down; 2 are −1 → −1 with a different prevV
  (dtl_mviol_n20 search 4, piece 2, prevV {15} → {7}; climbs_1016/b_best_s33 search 5, piece 1, {14} → {9}). These two
  matter because the Dom(prevV) target changes. The climbed games that maximise replays and fresh contexts are not
  deficit-driven: their changes are LRN.
- Status of (H4): GAP. Not proved: a bound on DEF per context, and that a DEF change never goes down. The data supports
  "deficits are rare and never the engine of a replay". (H4) stays a separate hypothesis only for A_DTL; it is void for C6.
  The open shape is the −1 → −1 prevV move, which re-targets Dom without any change in the ideal result.
- Addendum 12:21Z: the h4_notweaker_n20 call is also a DEF change, −1 {8} → −1 {8, 9}, at a fixed ideal result
  (−1 {8}). So a DEF re-target can leave the ideal return set altogether. A bound on re-targets cannot lean on the ideal
  target.
- Audit (12:21Z): which lemmas used "V_actual ⊆ V̂" for −1 RETURN sets? None:
  - Theorem M-cond (§3) uses per-round sets and stable V* only.
  - Lemmas D2 and D3 concern Dom at stable pieces (the actual code).
  - Lemma N, Lemma L-epoch (including the Reg_s ⊆ Û(V*_s) step, stable V*), Lemma F, Lemma S and the n(n+2)·c_i
    reduction are stated for C6, where actual = ideal, so the inclusion is vacuous there.
  - §8's (O) refinement and §10 (APP) use no such inclusion.
  - The §13 DEF classification (up / down / other) compares actual return sets directly and uses no inclusion.
  So the error is confined to the struck §13 line.

### 13b. Why (H4) has the same shape as GAP-A: regions are LEXICOGRAPHICALLY monotone (13:09Z)
- Lemma R (PROVED, A_DTL code, actual_union). Fix (p, R) and ONE candidate set V, and let T ⊆ T'. List V's tops in
  descending order t_1, t_2, …. The region of t_k is Z_k = lfp({t_k}, CurR_k, pr(t_k), T), where
  CurR_k = R \ (Z_1 ∪ … ∪ Z_{k−1}), with Z_k = ∅ when t_k is already in an earlier region. Then either the region
  vectors are equal, or at the first index k where they differ, Z_k(T) ⊊ Z_k(T'). In the second case the later regions
  Z_{k+1}, … are unconstrained and can SHRINK.
  Proof. The lfp is monotone in the tangle set and in the base. If Z_1..Z_{k−1} agree, CurR_k agrees, so
  Z_k(T) ⊆ Z_k(T'). If Z_k(T) = Z_k(T'), continue to k+1. A top swallowed by a grown earlier region gets Z = ∅ under
  T'. That is covered by "the first differing region grew". □
- Consequence. Within one pruning round, the actual union is driven by a vector of regions that evolves like a
  counter: a carry (the first differing region grows) can reset every lower region. This is exactly what produces a
  deficit (Lemma E: a straddling tangle consumed by a higher region that grew). The per-call bound this yields is the
  number of lexicographically increasing steps of disjoint region vectors. That number is not polynomial in general
  (≤ n components, each a chain), so Lemma R gives NO polynomial bound on DEF changes per context, by itself.
- Reading: (H4) is the same carry/reset question as GAP-A, one level down: inside one best_vertices round instead of
  across depth-0 pieces. C6 removes it by construction (Û has no consumption). For A_DTL a bound on DEF per context
  would need a reason why region carries with resets cannot repeat. Not proved.
- DATA (scratchpad defclimb.py, fitness = DEF changes at one (index, context), n = 20). The corpus max was 1.
  - Order datum ω = stable (dtl_pyref default, (priority, id); L26 freezes DTL for every ω, so this counts for the
    proof but is NOT pinned-Oink behaviour). experiments/alg/instances/h4_def5_stable_n20.pg: player 1, phase after
    the first dominion, piece 0 (|R| = 18). The ideal (C6) result is STABLE with an 11-vertex V̂* in all 6 searches,
    while the actual result is −1 five times in a row, return sets (original ids) {13} → {13, 17} → {7, 13, 17} →
    {17} → {7} → stable {5, 7, 17}. All 5 transitions of the phase are DEF changes at this one context. The
    stable-order pyref takes 10 iterations here; in Oink order it takes 4 iterations and has 0 deficit calls
    (dtl_pyref --order oink and Oink both report 4, Oink verified). So this is a tie-breaking phenomenon of ω = stable.
  - Order ω = oink (DTL_ORDER=oink, exact against pinned Oink; Oink and dtl_pyref --order oink both 8 iterations,
    verified): experiments/alg/instances/h4_def4_oink_n20.pg (seed 123 from lemmaS_viol_n20). Player 1, piece 0, R = G'
    (|R| = 20). The ideal (C6) result is STABLE with the same 14-vertex V̂* in searches 4-8, while the actual is −1 in
    searches 4-7, return sets (original ids) {0, 4} → {4} → {4, 7, 8} → {7, 8} → stable {7, 8, 18}. That is 4 DEF
    changes at one ideal-stable context on pinned A_DTL.
  - Scaling (13:26Z; Oink order, h4_def4_oink_n20 padded with source-only vertices and climbed): n = 28:
    experiments/alg/instances/h4_def6_oink_n28.pg (Oink and dtl_pyref --order oink both 9 iterations, verified).
    Player 1, piece 0 after the first dominion (|R| = 26). The ideal is STABLE with the same 17-vertex V̂* in searches
    3-9; the actual is −1 in searches 3-8, return sets (original ids) {5, 6, 15} → {6} → {6, 11, 20} →
    {6, 11, 15, 20} → {7, 8, 11, 15, 20} → {7, 8, 15} → stable {7, 8, 15, 18}. That is 6 DEF changes at one
    ideal-stable context, and the whole phase after the dominion is spent there. n = 36 (seed 136): 5 at one context, 6
    in the phase, so far. Maximum per context so far: n = 20: 4, n = 28: 6, n = 36: 5 (climbs running). Too few points
    for a growth law; consistent with growth.
  - 13:35Z, n = 44: experiments/alg/instances/h4_def7_oink_n44.pg (Oink and dtl_pyref --order oink both 11 iterations,
    verified). Player 1, piece 0, R = G (|R| = 44). The ideal is STABLE with the same 26-vertex V̂* in searches 4-11.
    The actual, in original ids: −1 {36, 43} → {9, 20, 43} → {9, 20, 34, 36, 38, 43} → {43} → {34, 36, 38} →
    {34, 38} → stable (10 vertices) → stable (the 26 of the ideal). That is 7 DEF changes at one ideal-stable context.
    Max per context, Oink order: n = 20: 4, 28: 6, 36: 6, 44: 7.
  - 13:39Z, n = 44, same climb: experiments/alg/instances/h4_def8_oink_n44.pg (Oink and dtl_pyref --order oink both 11
    iterations, verified). Piece 0, R = G, ideal STABLE (27 vertices) in searches 3-11; actual −1 in searches 3-10,
    return sets (original ids) {5, 34} → {5} → {5, 6, 30} → {5, 6, 30, 34} → {6, 30} → {30} → {30, 34} → {34} →
    stable. That is 8 DEF changes at one ideal-stable context, the whole phase. Max per context, Oink order:
    n = 20: 4, 28: 6, 36: 6, 44: 8 (climbs running).
  - Key earlier instances agree in both orders and with Oink (iterations): phi_idx_flat_n20 5, nest_nest_s84 19,
    lemmaS_viol_n20 8.

### 13c. L-RED's question: one deficit-driven change per NEW straddling tangle? (13:21Z; Lead 13:13Z)
Tool: experiments/alg/dtl_straddle.py (Oink order, exact). At every depth-0 call it records the straddling tangles of
the rounds where the actual and ideal survivors differ. For consecutive calls at one context it splits those of the
later call into NEW (learned after the earlier call) and OLD.
- DATA, three pinned-A_DTL instances: h4_def4_oink_n20 (4 DEF at piece 0), lemmaS_Mdrop_n20 and lemmaS_viol_n20
  (both on trunk, experiments/red/carry/instances). At EVERY consecutive pair of calls at a deficit context (20 pairs
  over contexts |R| = 20, 19, 18, 14):
  - the later call has ≥ 1 NEW straddling tangle (1 to 3 of them);
  - every tangle that straddled in the earlier call still straddles: the straddling set only GROWS at a fixed context.
  Example, h4_def4_oink_n20, piece 0: straddlers {1} → {1, 3, 4} → {1, 3, 4, 5, 6} → {…, 7, 8, 9} → {…, 10, 11, 12}.
- So the data supports "each deficit-driven change at a context comes with ≥ 1 new straddling tangle there". The
  resulting bound is DEF changes per context ≤ (straddling tangles learned while the context is visited). But tangles
  are ≤ n · (searches) by Lemma W, so as a GLOBAL bound this is CIRCULAR, like c_i in §14. It bounds deficits by
  learning, not by n.
- What a non-circular (H4) bound would need: a per-context cap on straddlers. The straddling set is monotone in the
  data, and each straddler is a tangle with vertices in ≥ 2 regions of one round. Nothing proved caps how many distinct
  tangles can straddle at one context; tangles are subsets, so there can be many. Not proved; DATA only (20/20).
- Not tested: whether the NEW straddler is the one that prunes the leader (L-RED's M-drop mechanism). Its region
  bookkeeping per round is in dtl_straddle.py and can be extended.

### 13d. Per-context cap on straddlers: none from tangle combinatorics (13:32Z; Lead 13:31Z (b))
- DATA, Oink order (dtl_straddle.py; max straddling tangles in one call at one context / max DEF changes at one
  ideal-stable context): n = 20 (h4_def4_oink_n20): 11 / 4; n = 28 (h4_def6_oink_n28): 7 / 6; n = 36 (climb seed
  136, |R| = 35): 24 / 6; n = 44 (seed 144, |R| = 38): 9 / 6. So the number of straddlers is NOT what limits the DEF
  count: 24 straddlers produced only 6 changes. DEF max per context so far: 4, 6, 6, 6 at n = 20, 28, 36, 44 (Oink
  order; climbs running). The 4 → 6 step is real; whether it keeps growing is open.
- Reason there is no cap from combinatorics alone (READING, construction-free). A straddler is a tangle with vertices in
  ≥ 2 regions of one round. Tangles are distinct (vertex set, strategy) pairs. Two regions joined by a layered gadget
  with two parallel vertices per layer carry 2^k distinct p-dominated cycles, each a candidate tangle meeting both
  regions. So the POOL of possible straddlers at one context is exponential. Any per-context cap has to come from WHICH
  tangles DTL extracts: Lemma W gives ≤ 1 per top per search, i.e. ≤ n · (searches visiting the context), which is
  circular as in §13c. A non-circular (H4) bound must therefore count DEF changes by something other than straddlers:
  the data says DEF ≪ straddlers.
- Candidate quantity (DATA only, not yet tested): the region VECTOR at the deficit round. By Lemma R it moves
  lexicographically, and a DEF change needs a carry that changes a LEADER's survival. A bound would follow from "each
  carry at a fixed context raises the region of a top that is a current leader". Not stated as a lemma until checked.

### 13e. Deficit changes come through the THRESHOLD phase, not through region carries (13:37Z, DATA)
Tool: experiments/alg/dtl_regvec.py (Oink order). For every DEF pair (consecutive calls at one context, ideal (result,
V) unchanged, actual changed), take the first round r0 where the actual sets differ. Compare the actual region vectors
computed on the common V_{r0−1}.
- h4_def4_oink_n20, h4_def6_oink_n28, lemmaS_Mdrop_n20, lemmaS_viol_n20, h4_notweaker_n20: 19 DEF pairs. In 18 the
  region vectors at r0 − 1 are IDENTICAL. In 1 the first differing region grew, as Lemma R says (h4_def4_oink_n20,
  s1 → s2, top 17).
- So in 18 of 19 DEF changes the deficit (consumed regions) is the SAME in both searches. What changes is the threshold
  phase: survivors(V, U) with W_t = lfp(U, R, t, T), which gains the new tangles. The deficit fixes which vertices are
  in U; new tangles then attract differently from that fixed U, while the ideal Û already attracted everything.
- Consequence for (H4): Lemma R (region carries) is not the engine. The engine is "fixed deficient U plus a growing
  tangle set in the threshold closure". At a fixed ideal-stable context, a DEF change is a change of the threshold
  closure of a FIXED deficient union under new tangles. That closure is monotone in T for fixed U (lfp monotone).
  Monotone in T plus a fixed U gives survivors that grow round by round, but the ROUNDS (V_r) change, which changes U
  at later rounds. A candidate lemma is "at fixed context and fixed deficient region vector, the actual rounds are
  monotone in T". It is DATA-consistent (the wandering return sets in §13b come with region changes at later rounds)
  but NOT checked; stated here only as a target.

### 13f. The chain test (L-RED R15 §6 reading) is NEGATIVE; the deciding round mostly climbs (13:50Z; Lead 13:42Z, 13:46Z)
Tools: experiments/alg/dtl_straddle.py (CHAIN lines) and dtl_regvec.py, with the tangle set AT the call.
- All straddlers at one context, both orders. Never a chain once there are more than 2: h4_def4_oink_n20 (|R| 20) has
  11 straddlers with 28 incomparable pairs (Oink order); h4_def6_oink_n28 has 7 / 6; h4_def7_oink_n44 9 / 14;
  h4_def8_oink_n44 15 / 33; lemmaS_viol_n20, lemmaS_Mdrop_n20, h4_notweaker_n20, dtl_mviol_n20 and dtl_deficit_n20
  have 3 to 10 incomparable pairs each. In stable order: the same, except h4_def5_stable_n20, whose 3 NEW straddlers
  are a chain.
- DRIVERS only, i.e. new tangles necessary for the deciding round, or sufficient alone, at the call-time tangle set.
  Also not a chain. h4_def8_oink_n44 (Oink order), piece 0: the necessary non-singleton drivers of the DEF changes
  s3→s4, s4→s5 and s6→s7 are {4, 13, 14, 35}, {21, 24, 40} and {10, 31, 32, 33} (original ids): PAIRWISE DISJOINT.
  This is the first ANTICHAIN instance (for L-RED). In h4_def6_oink_n28 the non-singleton necessary drivers ARE nested,
  {4, 13, 14} ⊂ {1, 2, 4, 12, 13, 14, 24} ⊂ {+5} ⊂ {+0, 6, 9, 10, 11}, as L-RED saw, but a singleton driver {10}
  (s6→s7) and two sufficient-alone pairs break the chain. So "DEF per context ≤ n via a chain of new straddlers" is FALSE
  on data.
- Threshold-phase statement (Lead 13:46Z (2)). PROVED, trivially: at a DEF change with identical V_{r0−1} and identical
  region vector (18 of 19 cases, §13e), some threshold closure W_t = lfp(U, R, t, T) must be strictly larger in the
  later search. Survivors are a function of (V, U, (W_t)_t), and each W_t is monotone in T for fixed U. This does NOT
  give "≤ n per context": W_t is per round, and U at later rounds can change, so the potential is lexicographic over
  rounds, with resets below the deciding round, as in Lemma R.
- DATA: the deciding round r0 of successive DEF changes at one context climbs:
  - h4_def4_oink_n20: 1, 3, 6, 8, 10;
  - h4_def6_oink_n28: 4, 6, 8, 7, 9, 11;
  - h4_def8_oink_n44: 5, 7, 9, 8, 10, 13, 15, 17.
  At most one dip per run. If r0 were strictly increasing, DEF per context would be ≤ (number of rounds) ≤ n. The dips
  show it is not. Candidate (DATA only): "r0 increases except after a change of M", to be checked against M before it
  is stated as a lemma.

### 13g. Candidate (H4) potential: the pair (deciding round r0, actual round count M) (13:53Z, DATA only)
For each DEF change at one ideal-stable context: r0 is the first round where the actual sets differ, and M is the
number of actual rounds after the change (Oink order, dtl_regvec.py). As (r0, M):
- h4_def4_oink_n20: (3,9) (6,9) (8,11) (10,10).
- h4_def6_oink_n28: (4,9) (6,9) (8,9) (7,10) (9,12) (11,11).
- h4_def7_oink_n44: (5,10) (7,10) (9,11) (8,12) (10,14) (12,12), then the final step to stable (1,1).
- h4_def8_oink_n44: (5,11) (7,11) (9,11) (8,13) (10,16) (13,17) (15,19) (17,18).
- lemmaS_viol_n20: (4,9) (6,7). lemmaS_Mdrop_n20: (5,9) (7,8).
Observations, 29 steps in 6 runs (including the final step of h4_def7):
(a) r0 strictly increases between consecutive DEF changes, except at steps where M RISES (3 dips, each with M up)
    and at the final step where the actual reaches the ideal.
(b) When M DROPS (the Lemma S failures), r0 still increases.
(c) No pair (r0, M) repeats at one context.
Candidate (C-rM), DATA only: at one ideal-stable context, the pairs (r0, M) of successive DEF changes are pairwise
distinct. Since 1 ≤ r0 ≤ M ≤ n + 1, (C-rM) would give ≤ (n+1)² DEF changes per context: a POLYNOMIAL per-context (H4).
Not proved. The proof gap is what makes r0 climb at fixed M. A DEF change at round r0 leaves rounds < r0 unchanged and
grows a threshold closure at r0 (§13f). The changed rounds ≥ r0 then need a DIFFERENT, later first-differing round next
time, unless M grows. Routed to L-RED as an attack target: find a context where (r0, M) repeats.
- (C-rM) and (a) FAIL on the wider data (14:01Z; experiments/alg/dtl_crm.py, every instance n ≤ 64, climbs_1016, the defclimb and
  deep-climb snapshots and the trunk instances; DEF runs = ≥ 1 DEF change at one context with the ideal unchanged).
  - Oink order: 117 runs, 290 steps. (C-rM) fails in 3 runs, each with a repeated (r0, M):
    - climbs_1016/a_best_s32.pg, |R| 20: (1, 9) twice;
    - fresh_fixed_n32.pg, |R| 32: (2, 6) twice;
    - phi_idx_cutrec_n20.pg, |R| 20: (4, 7) twice.
  - Observation (a) fails at 17 dips of r0 without a rise of M (e.g. deep-climb snapshot from h4_def8_oink_n44, |R| 42:
    r0 = 7, 5, 8, 9, 7, 10, 11, 9, 11).
  - Stable order: 111 runs, 3 repeats, 19 such dips.
  These runs include contexts whose fixed ideal result is −1, not only ideal-stable ones; the ideal-stable restriction is
  untested. (C-rM) is DEAD as stated; (H4) per-context stays OPEN, with data growth 4 → 8 for n = 20 → 44.
- (C-rM-stable), 14:09Z, CANDIDATE, DATA only. Restricted to IDEAL-STABLE contexts (CRM_IDEAL_STABLE=1, same files):
  - Oink order: 38 runs, 147 steps, 0 repeats of (r0, M);
  - stable order: 36 runs, 135 steps, 0 repeats.
  All 3 repeats above were at contexts whose fixed ideal result is −1. Observation (a) still fails there (5 and 3 dips
  without an M rise), so r0 alone does not climb; the PAIR does not repeat.
  Statement: at a context whose ideal (C6) result stays STABLE, the pairs (r0, M) of successive deficit-triggered
  changes are pairwise distinct. With 1 ≤ r0 ≤ M ≤ n + 1, this gives ≤ (n+1)² DEF changes per ideal-stable context,
  which would make the per-context (H4) polynomial there. Not proved. Routed as an attack target: find an ideal-stable
  context where (r0, M) repeats.
- (C-rM-stable) is DEAD (14:18Z). experiments/alg/instances/h4_def9_oink_n28.pg, from defclimb seed 128 (Oink order;
  Oink and dtl_pyref --order oink both 13 iterations, verified) has 9 DEF changes at one IDEAL-STABLE context
  (|R| = 28). The steps (r0, rounds before → after) are: (3, 7→8), (3, 8→8), (6, 8→9), (8, 9→10), (7, 10→10),
  (9, 10→12), (9, 12→12), (11, 12→14), (11, 14→11). So (r0, M) = (3, 8) and (9, 12) each occur twice. No pair-based
  potential of this kind survives; (H4) per ideal-stable context stays OPEN. Max DEF at one ideal-stable context, Oink
  order: n = 20: 4, n = 28: 9, n = 44: 8 (climbs; the n = 28 climb ran longest).
- 14:26Z, n = 28, same climb: experiments/alg/instances/h4_def10_oink_n28.pg (Oink and dtl_pyref --order oink both 14
  iterations, verified). Player 1, piece 0, R = G (|R| = 28). The ideal is STABLE (23 vertices) in searches 4-14. The
  actual is −1 in searches 4-13, return sets (original ids) {14, 23} → {14, 23, 27} → {23, 27} → {23} → {23, 27} →
  {12, 20, 23, 27} → {7, 23, 27} → {20} → {7} → {20}, then stable {7, 12, 18, 20}. That is 10 DEF changes at one
  ideal-stable context, and the actual return set REVISITS earlier sets ({23, 27} and {20} twice each) while the ideal
  stays fixed. So the actual state at a fixed ideal-stable context is not even injective in time. Max per context,
  Oink order: n = 20: 4, n = 28: 10, n = 44: 8.
- 14:51Z, n = 28, same climb: experiments/alg/instances/h4_def11_oink_n28.pg (Oink and dtl_pyref --order oink both 15
  iterations, verified). Piece 0, R = G (|R| = 28). The ideal is STABLE (22 vertices) in searches 4-15. The actual is
  −1 in searches 4-14, return sets (original ids) {10, 14, 23} → {1, 10, 23} → {10, 23} → {1, 10, 23} →
  {1, 21, 23} → {21, 23} → {20, 21, 23} → {7, 21, 23} → {20} → {7} → {20}, then stable. That is 11 DEF changes at one
  ideal-stable context. Max per context, Oink order: n = 20: 4, n = 28: 11, n = 44: 8 (longest climb at n = 28; the
  count tracks search effort more than n so far).
- Compounding check (14:34Z; deep-climb seed 201, fitness = deeper contexts with ≥ 2 DEF changes, from
  h4_def8_oink_n44). experiments/alg/instances/h4_deep_oink_n44.pg (Oink 13 iterations, verified). In every search 4-12
  of player 1's phase, the depth-0 calls of pieces 0-3 are ALL deficit calls (ideal stable). Pieces 0, 1 and 2 each stay
  at ONE context throughout; piece 3 visits 4 contexts. So the deeper deficits are PARALLEL staircases at fixed
  contexts, not fresh children reset by the piece-0 staircase. Their total is ≤ (searches) × (pieces) anyway. No
  NESTED deficit compounding observed (the shape that would be exponential). Not excluded either.

### 13h. Parallel vs NESTED deficit runs: L-RED's h4_compound_n44 is nested (14:45Z; Lead 14:51Z by its clock)
Classification by context identity per piece (Oink order; dtl_deficit.build, read-only on L-RED's file from
origin/claude/l-red @ c204679, experiments/red/carry/instances/h4_compound_n44.pg; Oink 13 iterations, verified).
- Player 1's phase after the 2nd dominion, searches 5-13. EVERY depth-0 call at pieces 0-4 is a deficit call while the
  ideal stays stable (only the deepest pieces turn ideal −1 at the end).
  - Pieces 0 and 1 stay at ONE context each.
  - Piece 2 is moved to FRESH contexts by piece 1's DEF changes: C0 (s5-6) → C1 (s7-9) → C2 (s10-11) → C3 (s12).
  - Inside those, piece 3 visits fresh contexts C0, C1 (s7), C2 (s9), C3 (s10), C4 (s11), and piece 4 visits
    C0 … C5, all fresh.
  So a deficit staircase at a fixed parent sets off fresh child contexts that themselves carry deficit changes, three
  levels deep: NESTED, at small counts. L-RED's parent count is 3, with child runs 2, 1, 0.
- Contrast: h4_deep_oink_n44 (§13g) is PARALLEL: pieces 0-2 at fixed contexts, each with its own deficit staircase.
- My measure nested_ctx (distinct deeper contexts with ≥ 1 DEF change, in a phase whose piece 0 has DEF) is 5 on
  h4_compound_n44 and 4 on my own nested climb (seed 202). Climbs running: seed 203 from h4_compound_n44, seed 202 from
  h4_deep_oink_n44, both Oink order, n = 44.
- Status: the nested deficit shape EXISTS on pinned A_DTL (first evidence: L-RED). Whether K_parent × K_child grows
  with n is the next box's question; at n = 44 the products are tiny (3 × ≤ 2).
- h4_compound2x2_n44 (L-RED R15 §12, trunk; Oink 13 iterations, verified), classified with my tools (Oink order, 14:48Z).
  - Player 1's phase after the 1st dominion. Parent piece 0 stays at ONE context (|R| 43) with ideal stable. Its
    actual return set goes {15, 21, 41} → {21, 41} (s6) → {21} (s9) → {15, 34, 39} (s12) → stable (s13).
  - Child piece 1 gets FRESH contexts C1 (|R| 41, s6-8) and C2 (|R| 42, s9-11).
    - In C1 it runs {10, 11} → {7, 10, 11} → {2, 7, 10, 11};
    - in C2, {7, 10} → {7} → {7, 15, 34, 39}.
    Each is a 2-step DEF run with the ideal stable: genuinely fresh child contexts with deficit runs. NESTED, as
    L-RED says.
  - Does the child RESET? Deaths at piece 1 on common vertices, actual rounds:
    - s5 (|R| 40) → s6 (C1): 0 drop, 22 rise, M 6 → 10;
    - s8 (C1) → s9 (C2): 0 drop, 10 rise, M 10 → 12;
    - only s11 (C2) → s12 (C3, ideal −1, |R| 38) drops (8 vertices, e.g. 41: 11 → 7; M 16 → 7).
    So across the fresh-context changes that carry the nested runs, the child's deaths do NOT reset; they keep rising.
    The child's second run comes from its deficit return set wandering on top of rising deaths, not from re-climbing.
    A reset happens only on the move into an ideal −1 context.
  - Reading: in this instance the nesting is bounded by the child's rising round count (M 6 → 10 → 12 → 16). A
    potential "child M non-decreasing across parent DEF steps into ideal-stable child contexts" is suggested by this
    one instance only. NOT checked more widely; it is the first thing to test next box.
- Nested climb (15:05Z; seed 203 from L-RED's h4_compound_n44, Oink order, fitness = distinct deeper contexts with DEF):
  experiments/alg/instances/h4_nested7_oink_n44.pg (Oink 12 iterations, verified). Player 1, searches 3-11: every
  depth-0 call at pieces 0-4 is a deficit call with the ideal stable (piece 5 ideal −1). Distinct contexts per piece over
  the 9 searches: piece 0: 1, piece 1: 1, piece 2: 2, piece 3: 5, piece 4: 8, piece 5: 9. The number of fresh contexts
  GROWS with depth: each deficit change at piece j moves piece j+1 to a context it has not seen. That is the nested,
  multiplying shape, capped here by the 9 searches of the phase. Not yet measured: whether the per-level DEF counts
  multiply (K_parent × K_child) as n grows. (CM) on this game: 6 cases, 0 M drops and 0 child-death drops. The
  multiplying contexts come WITHOUT child resets.
- Child-M check (14:55Z, experiments/alg/dtl_childM.py, Oink order). Cases: a depth-0 piece j ≥ 1 whose context
  changes while piece j−1 makes a DEF change, with piece j's ideal result stable in both searches. Data:
  h4_compound_n44, h4_compound2x2_n44, every instances/h4_*.pg, the defclimb snapshots and lemmaS_*.
  - 123 cases, counting duplicates from snapshots that repeat committed instances.
  - The child's actual round count M NEVER drops: 0/123.
  - Individual child deaths DO drop in 4 cases (2 distinct games, h4_def9_oink_n28 and h4_def10_oink_n28, search 5,
    piece 1).
  Candidate (CM), DATA only: "across a parent DEF step, an ideal-stable child's actual round count does not decrease".
  With M ≤ n + 1, (CM) bounds the number of M-RISES of a child across its parent's DEF steps. It does NOT bound child
  DEF changes at equal M (§13g shows those repeat). So (CM) alone does not stop nesting, but it removes the "child
  re-climbs from scratch" shape at ideal-stable contexts. Not proved.

## 14. (H2b) via c_i: contexts per index (11:40Z; Lead 11:33Z, main slot)
Tool: experiments/alg/dtl_ctx.py (A_DTL, corrected state of §6). c_i is the number of distinct Dom(prevV) −1 contexts at
depth-0 index i in a phase. By §11e, carries at index i ≤ n(n+2) · c_i.
- DATA (dtl_* instances, phi_idx_* instances, climbs_1016, 600 random games n ≤ 26; 642 games):
  - max c_i = 4 (climbs_1016/nest_nest_s44.pg, n = 54, index 2), with 1,780 contexts on 1,756 (phase, index) pairs.
  - New contexts at index i come from a level-j change (j < i): 42 from a Dom(prevV) piece whose V changed, 7 from a
    cut whose removed set changed, 0 from a result-type flip.
  - Contexts RECUR: 3 returns to a context seen earlier at the same index, all in nest_nest_s81, index 1.
- Mechanism of the recurrence (DATA, nest_nest_s81, piece 0, fixed context G'). Every death round at piece 0 only
  rises (Lemma F; e.g. 31: 6, 7, 7, 8, 9, 10 and 17: 6, 6, 7, 8, 8). They rise in a STAIRCASE: one vertex at a time
  steps above the others, so the return set (the last nonempty round) alternates {31} → {17, 31} → {31} → {17, 31} →
  {31} (s5, s8, s10, s11, s13). Dom(prevV) of piece 0 alternates with it, so the context at index 1 alternates R4 / R6.
  The return set is not monotone as a set although every death is.
- PROVED for C6 (from Lemma F, which needs only that T grows): revisits are harmless for the per-context bound. At a revisited
  context the same-context records from the earlier visit still bind, because T only grew in between. So carries at
  index i ≤ n(n+2) · (distinct contexts), not visits.
- PROVED for C6 (counting; for A_DTL only under Theorem M-cond, deficits break Lemma F): by Lemma F, piece 0 (fixed context G') changes state at most n(n+2) times per phase: each change
  raises a death, or grows Dom / a cut's removed set at an unchanged V (≤ n). So c_1 ≤ n(n+2) + n + 1. In general
  c_{i+1} ≤ c_i · (n(n+2) + n + 1): the §6 product again, c_i ≤ K^i. Nothing proved bounds the product. The data
  (max c_i = 4 at n ≤ 54) shows no growth, but the climbs that reward fresh contexts plateau at 5-6 (§6.3b, notebook).
- Status: (H2b) reduces to c_i; c_i is bounded by K^i and by nothing better that is proved. GAP-A OPEN at the same place
  as §6.3b: fresh child contexts per parent state.
- ADDENDUM (11:51Z): the reduction is CIRCULAR. Trivially c_i ≤ (number of searches in the phase), since each search
  visits index i at most once. Conversely, a phase with many searches changes some depth-0 piece at every transition
  (or progresses at depth ≥ 1), which creates new contexts at later indices. The c_i climbs show this: scratchpad
  ciclimb.py seed 102, n = 24, reaches Σ_i (c_i − 1) = 40 with only 5 searches, because a change at piece 0 moves every
  later index to a new context. So "(H2b) follows from a bound on c_i" says no more than "(H2b) follows from GAP-A". The
  non-circular content is the growth of c_{i+1} relative to c_i, i.e. whether piece i's states RESET in a fresh context
  (§12 child resets: real, 4/38). That is §6.3b's open question and is unchanged by this section.

## 15. Child resets with the fixed tracer, and their anatomy (11:57Z)
Tool: experiments/alg/dtl_childmono.py at this commit (fixed tracer, corrected piece state). Data: dtl_*, phi_idx_*,
climbs_1016 and 400 random games n ≤ 24. After a change at depth-0 piece j between consecutive searches, the deaths at
piece j+1 (and deeper) are compared on vertices present in both contexts.
- DTL: 282 parent changes. At the child (j+1), 157 comparisons: deaths DROP for some vertex in 33 and rise in 73.
  Deeper (j+2 and below): drops in 55 of 215. C6: 277 parent changes, child drops in 31/153, deeper drops in 55/211.
  The §12 figures (4/38, deeper 0/14) were an artefact of the tracer bug. Resets are COMMON, not rare.
- Anatomy of the 33 DTL child resets:
  - 14: parent return set GREW (V ⊂ V'), so the child context SHRANK (more removed by Dom(prevV));
  - 12: parent return set SHRANK (V' ⊂ V, the staircase of §14), so the child context GREW;
  - 6: incomparable parent V and child context;
  - 1: parent was a cut.
  C6 is the same, with 4 incomparable cases. So resets come from both directions of the parent's return-set move. A
  potential that ignores context composition cannot be monotone across a parent change. An argument has to say which
  child-context changes can lower deaths and charge them to something.
- Examples (original ids, (vertex, death before, after)): dtl_replay2deep_n32 parent piece 1: (0, 3→1), (6, 4→2),
  (4, 4→3); dtl_pertop28_n24 parent piece 0: (0, 3→2), (5, 3→2), (10, 3→2), (15, 3→1).
- Status: DATA. This is the shape every exponential run needs (APP's fresh child context), and it occurs in 21% of
  parent changes in this corpus. Whether resets can compound across levels is the open question (§6.3b). The
  fixed-tracer fresh-context climbs (scratchpad nestclimb.py seeds 111, 112) measure it.
- Coarse cause of the resets (12:03Z, DATA, dtl_childmono.py "cause_"). The check uses the END-of-run tangle set, not the
  set at the time, so it only shows correlation. Over all 33 DTL resets: lost tangle only 13, new escape only 14, both 5,
  neither 1. (A shrink cannot show a new escape and a grow cannot show a lost tangle; the tally is not split by kind, so
  the per-kind attribution is not claimed.) C6: 13 / 14 / 3 / 1. Reading: a shrink resets through
  LOST tangles (tangles need all their vertices in R), and a grow resets through NEW escapes. No monotonicity lemma in R
  follows: the removed part D_j always contains the parent's return set, i.e. candidates whose layer seeds the ideal
  union, so even without lost tangles removing D_j can lower deaths. Not proved either way.

## 16. The staircase: what a depth-j staircase needs in order to give depth j+1 FRESH contexts (12:11Z; Lead 11:48Z)
Setting: C6, one phase, a depth-0 Dom(prevV) piece j at a FIXED context R returning −1 in consecutive searches; T only
grows. Notation: V_r(T) = the ideal rounds; M(T) = the number of rounds (so V_{M−1} is the −1 return set and every
vertex of it dies at M).
- Lemma S (PROVED, C6). (i) M never decreases. (ii) While M stays equal, the return set only grows. (iii) When M rises,
  the return set becomes V_{M'−1}(T'), the vertices that reach the new top death: the "leaders".
  Proof. By Lemma 2.1 and induction over rounds (as in Lemma F), V_r(T) ⊆ V_r(T') for every r. So V_{M−1}(T) ≠ ∅
  forces V_{M−1}(T') ≠ ∅, giving M' ≥ M. If M' = M, the return sets are V_{M−1}(T) ⊆ V_{M−1}(T'). (iii) is the
  definition. □
- Consequence (PROVED, C6). At a fixed context, piece j has at most (n+1) · n distinct return sets per phase: ≤ n + 1
  values of M, and within one value a growing chain of length ≤ n. With Dom(V) monotone in T (Lemma D3), each return set
  has ≤ n + 1 distinct Dom values. So the next index sees at most n(n+1)·(n+1) contexts per context of piece j: a
  per-level factor of the same polynomial kind as K in §6.
- Criterion (fresh vs recurrence; PROVED as a case split, C6). A step of the staircase moves index j+1 to
  R \ Dom_T'(V'). This is a RECURRENCE (an earlier context at j+1 again) only if V' repeats an earlier return set V of
  this staircase and Dom_T'(V') = Dom_T(V), i.e. Dom of that set has not grown. By (ii), a repeat can only happen across
  a rise of M: the new leaders equal an older return set, as in nest_nest_s81 (leader 31 at M = 7, 8, 9, 10; §14).
  Otherwise the step gives a FRESH context. So a staircase gives FRESH child contexts exactly when every M-rise brings
  new leaders, or Dom grew, and every equal-M growth step is fresh automatically.
- DATA (experiments/alg/dtl_stair.py; dtl_*, phi_idx_*, climbs_1016, 400 random games n ≤ 26; 442 games). Lemma S: 0
  exceptions ((i) and (ii)). Context changes at j+1 caused by a staircase step at j: M-rise 80 (65 fresh, 15
  recurrent), equal-M growth 44 (39 fresh, 5 recurrent), Dom-only 0. ("Fresh" is relative to all contexts at j+1 in
  the phase, so an equal-M step can still land on a context seen under a different j-context: the 5.)
- What this gives a counter builder (for L-RED). A level-j digit is a staircase at a fixed context. It offers at most
  n(n+1)(n+1) child contexts. To make each child context FRESH, the leaders must change at every M-rise. To make the
  child RE-CLIMB in each fresh context, the child context change must reset child deaths: a lost tangle (shrink) or a
  new escape (grow), §15. Nothing proved prevents both from repeating at every level, so the product K^L stands.
  A polynomial bound needs a reason why fresh child contexts that also reset cannot recur per parent step. That is the
  open core (§6.3b).
- Resets by staircase step type (12:17Z, DATA, dtl_stair.py "_RESET"; same 442 games). Among the context changes at
  j+1 caused by a staircase step at j, the child deaths DROP for some common vertex:
  - M-rise to a fresh context: 16 of 65;
  - equal-M growth to a fresh context: 13 of 39;
  - M-rise to a recurrent context: 0 of 15;
  - equal-M growth to a recurrent context: 1 of 5.
  So both step types reset children, and an equal-M growth step (a "cheap" step that does not raise M) does so as
  often as an M-rise. For a counter builder: a digit need not spend an M-rise per child reset. For a bound: charging
  resets to M-rises (≤ n + 1 per context) is NOT available.
- Lemma S on A_DTL (12:43Z; Lead 12:43Z relaying L-RED l-red 677e5d7: 0 violations in 604 fixed-context pairs, 139
  games). Own check: the actual rounds recorded by dtl_ideal.Ctx (every dtl_* instance plus h4_notweaker_n20), 308
  consecutive same-context −1 pairs: 0 M-drops and 0 equal-M return sets that fail to grow. That includes dtl_mviol_n20,
  where (M) itself fails: its drops hit non-leader vertices and leave M and the return set intact. Provability for
  A_DTL: PROVED only under Theorem M-cond, i.e. when the LATER run has no deficit round (then rounds are monotone and the
  C6 proof applies verbatim). With a deficit in the later run nothing proved prevents M from dropping. The per-round
  inclusion V_i ⊆ V̂_i only bounds the actual M by the ideal M, which says nothing about M across runs. So for A_DTL,
  Lemma S is DATA (0/308 here, 0/604 L-RED) plus PROVED-under-M-cond. A violation would need a deficit (Lemma E's
  straddle) that prunes a LEADER early, not just a lower vertex.
- Lemma S FAILS on A_DTL when the later run has a deficit (13:06Z; L-RED l-red d0b2400, R16 §5; Lead re-ran Oink:
  8 iterations, verified). Instance: experiments/red/carry/instances/lemmaS_viol_n20.pg (n = 20, on trunk). Odd
  searches 5 → 6, Dom(prevV) piece 2 (|R| 18), same context, −1 both times, M = 7 both times. The return set SHRINKS
  {7, 14, 15} → {7} in original ids: leaders 15 and 14 now die at rounds 5 and 6. Reproduced here with dtl_deficit.py
  (internal ids {5, 11, 12} → {11}): both calls are deficit calls, and the ideal (C6) result is STABLE in both
  searches. This realises the c0aaa02 caveat; the C6 proof is untouched. Consequence: on A_DTL the n(n+1)(n+1)
  child-context bound per context of §16 holds only with a bound on deficit steps, so (H4) moves toward the centre
  for A_DTL. Running (scratchpad defclimb.py, fitness = DEF changes at one (index, context)): seeded from
  lemmaS_viol_n20, 3 DEF changes at one context within 863 steps.

## 17. Ledger for a referee brief (13:42Z; Lead 13:31Z (c); every item unrefereed, produced on Opus 5.5)
"PROVED" = argument written out in this file by L-ALG, not refereed. Scope: C6 (ideal pruning, actual = ideal), A_DTL
(the frozen DTL for every order datum ω, L26), or A_DTL under Theorem M-cond (the later run has no deficit round).

PROVED
| Item | Scope | Where |
|---|---|---|
| Set semantics of one pruning round | A_DTL | §1 |
| Lemma 2.1: Û monotone in (V, T); Lemma 2.2: U ⊆ Û (per round) | A_DTL | §2 |
| Lemma E: the only deficit is a straddling tangle with a lower surviving cycle maximum | A_DTL | §3 |
| Lemma P*-inv; Theorem M-cond: no deficit in the later run ⇒ per-round monotone | A_DTL | §3 |
| Per-round inclusion V_i ⊆ V̂_i; actual empties no later; ideal −1 ⇒ actual −1 (NOT for −1 return sets) | A_DTL | §13 (corrected) |
| Lemma D2: sptl regions ⊆ Dom(V*, R) ∪ X_before | A_DTL | §6 |
| Lemma D3: Dom is a layered closure, monotone in V and T | A_DTL | §9 |
| Driver lemma: a level-j change is driven by a tangle learned at a piece ≥ j | A_DTL (equal level contexts) | §6 |
| Counting N_j ≤ K·E_j (product bound) | C6; A_DTL under M-cond; given the "contexts at the level are equal" DATA line | §6 |
| GAP-C step (r1) | A_DTL (same region, no dominion between) | §7 |
| (O) refinement; C6 excludes gate (S) | C6 / A_DTL with D2 | §8 |
| Lemma L-epoch (V* growth, lift or catch-up) | C6 | §9 |
| LIFT gate constraint | C6 | §9 |
| APP(k) barrier model and its property table | model | §10 |
| Lemma F: same-context raise of every rescued vertex | C6 | §11c.1 |
| Reduction: carries at index i ≤ n(n+2) · c_i; revisits harmless | C6 | §11e, §14 |
| c_i ≤ searches, so the reduction is circular | trivial | §14 |
| Lemma S: M non-decreasing; equal-M return set grows; fresh-vs-recurrence criterion; ≤ n(n+1)(n+1) child contexts per staircase | C6; A_DTL under M-cond | §16 |
| Lemma R: region vector lexicographically monotone in T (carries reset lower regions) | A_DTL | §13b |
| Threshold statement: a DEF change with equal V_{r0−1} and regions strictly grows some W_t (trivial; lexicographic only) | A_DTL | §13f |
| Region split: Attr_{q−1}(U) = Attr_{q−1}(A_q ∪ V^{<q}); level-q survival depends on lower levels only through the set V^{<q}, monotonically (box 4) | A_DTL | §18a |
| U equal at r0 ⇒ V_r0 grows (LEX-R in that case) | A_DTL | §18b |
| Extra tops X ⊆ Y (same T) hurt only vertices of their own priority or lower (box 4) | A_DTL | §18h |
| Phases ≤ D + 2 (D = dominion-finding searches ≤ n); with (SPP): searches ≤ n(n+2), tangles ≤ n²(n+2), O(n¹⁰(m+n²)) word ops, O(log n)-bit words (box 5) | A_DTL | §21c |
| First-Difference Lemma: consecutive searches agree up to the first differing tangle attractor, whose input is equal and output strictly larger; the cause is a tangle learned later in the earlier search (box 5; reading) | A_DTL | §21d |
| Lemma DV*-MONO: the clean ideal root distance DV* is pointwise monotone in T, so it changes ≤ n(n+1) times per phase (box 5) | any tangle sets | §21h |
| Per-context LRN budget: at a fixed context R, transitions whose first difference is at R and moves DV*_R are ≤ n(n+1) (DV*-MONO on the subgame R); S − 1 ≤ n(n+1)·(contexts) + #DEF + #ABS (box 5) | A_DTL | §21j |
| GAP-C lemmas (box 5): SCC1 (one candidate SCC per closed region), B-thr (how a duplicate arises), O0/O1 (orphans), OPP-EXIT, Theorem A (root call stable ⇒ productive inside W_p unless (α)) | A_DTL | GAP-C.md §3, §6, §11, §13 |

KILLED (FALSE / DEAD), each with its instance
| Claim | Instance (experiments/alg/instances unless noted) | Where |
|---|---|---|
| (M) / Claims P, Q / F5 at a fixed context, A_DTL | dtl_mviol_n20.pg (Oink-verified); synthetic dtl_m_synth.py | §4, §4b |
| (CU) W-blocked top's SCC is stored or a dominion | dtl_cu_viol_n24.pg | §9 |
| Invariant excluding the straddle-with-lower-pickup shape | dtl_deficit_n20.pg | §4 |
| Φ: global −1 death record raised by every dead-top cap carry | cross_h_k1_n11_m17_37.pg | §11b, DEAD.md |
| Φ_idx: per-index record (original and restated) | phi_idx_flat_n20.pg; climbs_1016/nest_nest_s84.pg; phi_idx_cutrec_n20.pg (original only) | §11d, DEAD.md |
| Φ_idx sub-mechanisms: lift-to-max; per-index max death monotone | data (80/258; 201/2540) | §11b |
| "V_actual ⊆ V̂ for −1 return sets" (my §13 claim) | red/carry/instances/h4_notweaker_n20.pg (L-RED) | §13 |
| Lemma S on A_DTL with a later-run deficit | red/carry/instances/lemmaS_viol_n20.pg, lemmaS_Mdrop_n20.pg (L-RED) | §16 |
| R12 §9 (C-a) as stated; (C-c) first step (L-RED reading) | dtl_proof_c3.pg; cross_h_k1_n10_m16_27.pg | §11c |
| "Deficit-triggered changes per ideal-stable context ≤ a constant", A_DTL Oink order | h4_def4_oink_n20 (4), h4_def6_oink_n28 (6), h4_def8_oink_n44 (8), h4_def10_oink_n28 (10), h4_def11_oink_n28 (11) | §13b, §13g |
| Chain of new straddlers / drivers at a context (L-RED reading R15 §6) | h4_def8_oink_n44 (disjoint drivers) | §13f |
| (C-rM): (r0, M) pairs never repeat at a context | climbs_1016/a_best_s32 (ideal −1 contexts) | §13g |
| (C-rM-stable): same at ideal-stable contexts | h4_def9_oink_n28 | §13g |
| §6/§12 counts from the buggy tracer (superseded, conclusions kept or corrected) | tracer fix e41ccfb | §6, §12, §15 |
| (LEX) per-context death vector lexicographically increasing, and (NR) ⇒ n(n+3) route (box 4) | lex_viol_oink_n20.pg (L-ALG) and red/carry/instances/lex_viol_inj_n28.pg (L-RED R18), A_DTL, Oink-verified, both orders; synthetic genuine: dtl_lexcounter.py | §18c, §18h, DEAD.md |
| (NR): a fallen vertex is never again the top changed vertex at that context | red/carry/instances/lex_viol_inj_n28.pg (L-RED R18) | §18j, DEAD.md |
| (F1) (L-RED): at most one fall step per context | red/carry/instances/f1_twofall_n48.pg (L-RED R19, A_DTL, Oink-verified); synthetic: dtl_twofall.py | §18k, DEAD.md |
| (F1-DEF): at most one DEF fall step per context | red/carry/instances/f1_twodef_n48.pg (L-RED R20, A_DTL, Oink-verified); synthetic: dtl_twofall.py | §18k, DEAD.md |
| A per-context potential over the actual state for (H4) | A_DTL: both lex_viol instances (no lexicographic potential over deaths); synthetic: dtl_staterevisit.py (state returns) | §18f, §18j |
| Per-round monotonicity in T at a fixed input, genuine tangles (synthetic) | dtl_lexcounter.py | §18c |
| Any potential on the actual per-context state for DEF changes (synthetic, genuine tangles) | dtl_staterevisit.py (pure DEF cycle) | §18f |
| "Fallers are strictly below the top riser in priority" (box 4 DATA pattern) | lex_viol_oink_n20.pg | §18h |
| (CM): child M never drops across a parent DEF step into an ideal-stable child context | cm_viol_oink_n28.pg (L-ALG) and red/carry/instances/cm_mdrop_both_n28.pg (L-RED R17), A_DTL, Oink-verified, both orders | §18i, DEAD.md |
| Per-phase potentials for (SPP) (box 5): tangle-vertex union, tops, (top, vertex) pairs, new-vertex-for-top; fixed-input attractor sums PSI1-PSI5; settled piece labels; PHI0 / LEX0 (depth-0 removal index); used-tangle set; LR-/LT-SETTLE; (CL) | C5 corpus, both orders: spp_final_n20/n30/n40, spp19_oink_n30 (failure counts in the tables) | §21d, §21e |
| "S ≤ P + c", "S ≤ d'", "S ≤ distinct p-parity priorities" (sharper forms of (SPP)) | spp_final_n20 (Oink: 19 vs P 14, d' 13) | §21a |
| The author's per-search check (DV changes at every tangle-learning search; dtl.cpp computeDistanceValues) | spp_chain_up_n43 (41 of 41 unchanged; pinned Debug Oink agrees), 525 of 990 corpus searches | §21f |
| Constant tangles per top per phase | spp_final_n40 (13 at one top) | §21e |
| (PHI-DV): PHI0 rises only when the root DV* moves | climbs_1016/nest_nest_s43 (69 counterexamples) | §21j |
| GAP-C (NODUP) the duplicate check never fires; (NO-ORPHAN) no stored p-tangle inside a context has all escapes outside it | red/carry/instances/gapb_dup_n20.pg (L-RED, l-red e4138a0; Oink 14 iterations, verified; both orders); in a search with W_p(G') = ∅ | GAP-C.md §8 |
| GAP-C (NO-ORPHAN-W): no orphan inside the winning region | red/carry/instances/gapbW_dup_n20.pg (L-RED, l-red 2b792b8; Oink 6 iterations, verified; both orders); the same search learns elsewhere inside W_p | GAP-C.md §12 |
| GAP-C (K-first), (K4-B): the first stable piece is the productive one / its regions lie in W_p | instances/kfirst_viol_union.pg (L-ALG; disjoint union of two corpus games; Oink 7 iterations, verified; both orders) | GAP-C.md §14 |
| GAP-C (FIRST-W): the first stable piece with a p-won top is productive | instances/firstw_viol_cross.pg (L-ALG; union with 3 cross edges, n = 30; Oink 6 iterations, verified; both orders) | GAP-C.md §16 |
| (ABS-mono) PHI0 never rises at a non-RES-d0 transition; (ABS-mono-pw) no vertex moves to a later depth-0 piece there | red/carry/instances/absmono_viol_n44.pg (L-RED R22, l-red cf9bdba; Oink 5 iterations, verified): Even's search 0 → 1, SHRINK at depth-0 piece 14, then piece 17 (same context) stable → −1 under the larger T; 7 vertices move later, PHI0 374 → 379; both order data | §21j, DEAD.md |

DATA candidates left after box 4 (A_DTL; every per-context (H4) POTENTIAL candidate is dead):
(U-MONO_DTL) same-input union monotone in T (701/701 Oink, 661/661 stable, §18h); (LEX-R) first differing round grows (775/775, 755/755); "no DEF-down step at an ideal-stable context" (0/181).
Box 5 DATA candidates (A_DTL): (SPP) S ≤ |G'| and (SPP-sharp) S ≤ max(1, |G'| − 1), tight (dtl_chainfam, spp_chain_up_n43, both orders, §21a-b); (DV-nofall) the author's DV never falls (0/1,237, 0/1,204; synthetic 0/101,600; Lemma DV-MONO = SKETCH + GAP, §21f-g); absorption (c1) 87/87, 75/75 (§21d).
OPEN: GAP-A via (H1) cut carries, (H2a) alive-top self-reinforcing carries, (H2b) dead-top cap carries (reduces to
c_i, circular), (H3) catch-ups and recursion, (H4) deficits on A_DTL (per context: 4 → 8 over n = 20 → 44, Oink
order). Core: whether fresh, resetting child contexts (§15, §16) or deficit staircases (§13b) can compound across
levels.

## 18. Box 4 (Lead "go" 16:01Z; produced on Opus 5.5): a lexicographic candidate for (H4), and its synthetic death (16:05-16:35Z)
Tools (experiments/alg): dtl_plateau.py (consecutive calls at one context: r0, direction, deaths, lex tests),
dtl_lexsynth.py (DTL's own tangles in random orders), dtl_lexfake.py (random vertex sets as tangles, or with
LEXF_GENUINE=1 generated genuine tangles, dtl_gentangle.py), dtl_lexcounter.py (the counterexample, in check.sh),
dtl_nestK.py and dtl_nestclimb.py (queue item 3). Corpus "C" below = experiments/alg/instances/*.pg and climbs_1016/*.pg
(145 files) plus every experiments/red/**/*.pg on trunk (25 files).

### 18a. Region split (PROVED, A_DTL, any T)
For a round input V and a vertex v ∈ V of priority q: Attr_{q−1}(U) = Attr_{q−1}(A_q ∪ V^{<q}), where A_q = the union of the
regions of tops of priority ≥ q and V^{<q} = the tops of priority < q. Proof: ⊇ since A_q ⊆ U and V ⊆ U. ⊆: a region Z_τ of a
top τ with pr(τ) < q is derived inside CurR_τ with threshold pr(τ) ≤ q − 1; every rule application inside CurR_τ is an
application in R with the earlier regions in the base (exits into earlier regions are forgiven in CurR_τ and are covered by
the base in R; the same argument as Lemma 2.2), so Z_τ ⊆ Attr_{q−1}(earlier regions ∪ {τ}); induction over the regions. □
Consequence: v survives iff attracts(v, Attr_{q−1}(A_q ∪ V^{<q}), R). A_q depends only on V^{≥q} and T. So survival of a
level-q vertex depends on the higher and equal levels through their regions, and on lower levels only through the SET
V^{<q}, monotonically.

### 18b. Candidate (LEX), stated 16:14Z with data (Lead message 16:14Z)
(LEX): at a fixed context (p, R), consecutive calls with T ⊆ T': if the actual death vector d (d(v) = first round without v,
INF for the stable result) changes, then at the highest-index vertex v* whose death changes, d_{T'}(v*) > d_T(v*).
Companion (LEX-R): at the first round r0 where the round sets differ, V_r0 grows.
- DATA, actual DTL runs, corpus C, every consecutive pair at a fixed context (dtl_plateau.py, PLATEAU_ALL=1):
  Oink order 775/775 (LEX) and 775/775 (LEX-R); stable order 755/755 and 755/755. The DEF pairs at ideal-stable contexts
  are 181/181 (Oink) and 159/159 (stable). 1,500 random games n ≤ 28 per order: 5/5 (contexts rarely recur).
- Deaths do fall: 16 steps (Oink order), e.g. lemmaS_viol_n20, lemmaS_Mdrop_n20, dtl_mviol_n20, b_best_s33. In all 16,
  every fallen vertex has strictly LOWER priority than the top riser. Σ_v d(v) falls in 6 steps: dead as a potential.
- Reset nesting (a riser that fell earlier at the same context): level 0 in all 343 contexts with changes (Oink order).
- PROVED part: if the region union U at round r0 is the same in both calls (617 of 775 Oink pairs), survivors at r0 are
  monotone in T (18a with A_q fixed, Attr and attracts monotone in T), so V_r0 grows: (LEX-R) in that case.
- Reading (what LEX would give): the state at a fixed context is a COUNTER whose digits are deaths in priority order; a
  higher digit's rise may reset lower digits. Injective in time, but only an exponential count. With the second candidate
  (NR) "a vertex that fell at a context is never again the top changed vertex there" (DATA only, 343/343 at level 0),
  each vertex is the top changed vertex ≤ n + 3 times, so ≤ n(n+3) changes per context: a polynomial per-context (H4).

### 18c. (LEX) is FALSE for genuine tangles in arbitrary learning order (synthetic, 16:30Z)
- Per round, monotonicity in T at a fixed input fails for random vertex sets used as tangles (experiments/alg/
  dtl_carrytest.py with CARRY_GENUINE=0, seeds 1-3 × 6,000 games: 4 failures in 63,787 region carries), and it does not
  fail with randomly generated GENUINE tangles (CARRY_GENUINE=1, seeds 1-3 × 15,000 games: 0 in 103,497 carries; there
  even the union U never shrank). A hand construction then broke it with genuine tangles.
- experiments/alg/dtl_lexcounter.py (9 vertices, p = 0, R = all, in check.sh): genuine tangles s = {y1, y2, y3, y4}
  (escape b) and σ = {y1, z} (escape a). Under {s} the pruning is stable on {a, b, e0, y1, y3}; under {s, σ} the only change
  is that e0, the LOWEST vertex, dies at round 1. So (LEX), (LEX-R) and per-round monotonicity in T all fail, at round 1
  with V_0 = all p-vertices ((P*) holds vacuously, as Lemma E requires).
  Mechanism: σ grows a's region by y1 (Lemma R carry); s straddles; its rest {y2, y3, y4} has the cycle y3 ↔ y4 with
  maximum y3 ∈ V, pr 2 < 4 (exactly Lemma E (b)); y3's own region re-absorbs the rest at threshold 2, but e2 (priority 3),
  which followed s into b's region at threshold 4, is in no region now; e0 (priority 0, opponent-owned) needs e2.
- A random search around this gadget (genuine extra tangles, random learning orders; scratchpad gadsearch.py, not
  committed) gives full-run (LEX) violations in 655 of about 350k variants.
- Status: (LEX) DEAD for arbitrary chains of genuine tangles; OPEN for A_DTL (0/775 on actual runs; 0/145 with DTL's own
  tangles reordered at R = all). A proof for A_DTL must use WHEN DTL learns a tangle (here: σ, which ties y1 to a higher
  top, learned after s). Not per-round set algebra. Routed to L-RED (Lead 16:33Z): realise the shape in a DTL run.
- What this means for queue item (1). The threshold-phase mechanism (§13e) is the U-equal case, where everything is
  monotone. The non-monotone part is the carry case, and its loss is exactly Lemma E's rest: vertices that followed the
  straddler at the HIGHER threshold and are re-absorbed only at the LOWER level of the rest's cycle maximum. A bound at a
  fixed (context, M) would have to charge each such loss; the counterexample shows the loss can hit a vertex of the lowest
  priority with nothing rising, so no lexicographic potential over deaths survives without DTL's learning order.

### 18d. (CM) recount (Lead 16:01Z: corpus and order datum with the count)
dtl_childM.py on experiments/alg/instances/*.pg, climbs_1016/*.pg and experiments/red/carry/instances/*.pg (157 files;
the 13 other red files not included): Oink order 51 cases, 0 M-drops, 2 with a child death drop (h4_def9_oink_n28,
h4_def10_oink_n28, search 5, piece 1); stable order 42 cases, 0 M-drops, 2 death drops. The earlier 0/123 and 0/129
counted uncommitted climb snapshots (and duplicates).

### 18e. Queue item (3): per-level DEF counts in one phase (dtl_nestK.py; k(j, C) = DEF changes at context C of piece j)
Corpus C (zp_* and strfam_S5 excluded: no DEF), Oink order. Phases with DEF at ≥ 2 levels:
| instance | n | searches | K_j = max_C k(j, C) | N_j = Σ_C k(j, C) | contexts c_j |
|---|---|---|---|---|---|
| h4_compound2x2_n44 | 44 | 9 | [4, 2] | [4, 4] | [1, 2] |
| h4_compound_n44 | 44 | 9 | [1, 3, 1, 1] | [1, 3, 2, 2] | [1, 1, 2, 2] |
| h4_nested7_oink_n44 | 44 | 11 | [1, 1, 2, 1, 1] | [1, 1, 3, 2, 2] | [1, 1, 2, 2, 2] |
| h4_deep_oink_n44 | 44 | 11 | [1, 2, 4, 0, 2] | [1, 2, 4, 0, 2] | [1, 1, 1, 0, 1] (parallel) |
| b_best_s33, lemmaS_Mdrop_n20 | 20 | 4 | [1, 1] | [1, 1] | [1, 1] |
Single-level maxima: n = 20: 4; n = 28: 11; n = 44: 8. In every phase the total DEF count is ≤ searches − 1, so the
nested product is capped by the phase length (≤ 13 here). Genuinely nested products (K_parent × K_child with fresh child
contexts): 1 × 1 at n = 20, 4 × 2 at n = 44 (h4_compound2x2_n44, L-RED's construction). Stable order: the same rows.
Climbs (dtl_nestclimb.py, fitness = DEF over ≥ 2 child contexts, then total DEF; Oink order; scratchpad, running) are
recorded in 18f at box end.

### 18f. The state at a fixed ideal-stable context can RETURN: a pure DEF cycle (synthetic, genuine tangles, 16:40Z)
experiments/alg/dtl_staterevisit.py (11 vertices, p = 0, R = all; in check.sh). Genuine tangles s = {y1, y2, y3, y4}
(escape b), σ = {y1, z} (escape a), τ = {y3, y4} (escape y1). Actual results: T = {}: e1 dies at round 1 (state s0);
{s}: stable on all 6 even vertices (s1); {s, σ}: s0 again; {s, σ, τ}: s1 again. The ideal (C6) result is the same stable
set (all 6 even vertices) at {s}, {s, σ} and {s, σ, τ}. So s1 → s0 → s1 is a pure DEF cycle at an ideal-stable context: a
DEF-DOWN step (never seen in DTL runs: 0 of 181 ideal-stable DEF pairs, §18b) followed by a DEF-up step back to an
earlier state. Mechanism of the repair: τ's only escape y1 sits in a's region (stolen there by σ), so τ fires inside a's
region and carries y3, y4 and then v, e0 (opponent, edges v, y3) up to threshold 6.
- A random search around the gadget (scratchpad gadrev.py, not committed) finds state revisits in 750 of about 390k
  variants.
- Answer to queue item (1), at the level of per-context set algebra (READING from 18c, 18f; synthetic, not DTL runs):
  there is NO function of the actual state at a fixed context (deaths, rounds, return set, (r0, M)) that a DEF change must
  increase, because the state can revisit with the ideal fixed. What IS monotone at a fixed context is only the round-1
  region vector (Lemma R, V_0 fixed), and that is lexicographic (counter-shaped). So any polynomial bound on DEF changes at
  a fixed (context, M) must use WHEN DTL learns the steal tangle (σ: a tangle of a lower top tied, via its escape, to a
  higher top's region, learned at a context without that higher top, e.g. a later piece where it was removed by Dom) and
  the repair tangle (τ). That is cross-context information, the same core as GAP-A (§6.3b, §16). On actual DTL runs
  neither DEF-down steps nor (LEX) violations have been seen (0/181, 0/775). Routed to L-RED with 18c.

### 18g. Queue item (2), (CM): anatomy of the cases, and why Lemma R + per-round inclusion cannot prove it (16:45Z)
experiments/alg/dtl_childM2.py, Oink order, the 157 files of 18d; all 51 (CM) cases:
| parent step (actual, piece j−1) | child context (piece j) | child actual result | child M | cases |
|---|---|---|---|---|
| −1 → −1, return set grows | SHRINKS | −1 → −1 | equal | 15 |
| −1 → −1, return set grows | SHRINKS | −1 → −1 | up | 4 |
| −1 → −1, return set shrinks | GROWS | −1 → −1 | up | 24 |
| −1 → −1, return sets incomparable | incomparable | −1 → −1 | up | 8 |
So every case is a deficit child (actual −1, ideal stable) under a deficit parent whose Dom(prevV) target moves. When the
child context grows (parent return set shrinks: the §14 staircase), M rose in 24/24.
- Why the PROVED tools do not reach (CM) (READING). Lemma R and the per-round inclusion V_i ⊆ V̂_i are statements at ONE
  context with growing T. (CM) compares two DIFFERENT child contexts R \ Dom(V) and R \ Dom(V'). The inclusion only gives
  "actual empties no later than ideal", and the ideal never empties here (stable), so it bounds nothing. Child deaths do
  drop across these steps (2 of 51) and across parent changes in general (§15: 33 of 157), so (CM) is a claim about the
  MAXIMUM death only. A proof would need a reason why the last-dying child vertex is never hurt by the context change.
- The synthetic shapes of 18c/18f give a plausible attack (for L-RED): a GROW step that adds a high top to the child
  context (it was in the parent's Dom before) whose region steals a straddler supporting the child's last-dying vertex,
  as σ steals y1 in dtl_lexcounter.py. No proof attempted beyond this reading; (CM) stays DATA (51/0 Oink, 42/0 stable).

### 18h. (LEX) FAILS in an actual A_DTL run (16:52Z); steals in DTL never shrink the union (DATA)
- experiments/alg/instances/lex_viol_oink_n20.pg (dtl_downclimb.py seed 201 from climbs_1016/b_best_s33.pg, fitness =
  (LEX) violations, DEF-down steps, fall steps; pinned Oink: 5 iterations, verified; dtl_pyref --order oink agrees:
  1 dominion, 9 tangles, 5 iterations). Odd's phase before any dominion, searches 3 → 4, alive tangles 2 → 3 (superset),
  context R = all 20 vertices (and the 8 smaller contexts of the same searches), ideal (C6) result the same stable 17-vertex
  set in both. Actual (−1 both times): the first differing round is r0 = 2, where vertex 17 (priority 21) now survives
  (LEX-R holds there: V_2 grows); at round 3 vertex 10 dies instead; vertex 17 dies at 4 instead of 2, and vertex 19
  (priority 21, HIGHER index than 17 in both order data) dies at 11 instead of 12; M 15 → 14. So the highest changed vertex
  FALLS, and the fall is at the top changed priority level (the "fallers strictly below the riser" pattern of 18b fails).
  dtl_lexviol_check.py (in check.sh) reproduces it in both order data (oink and stable).
- Consequence: (LEX) is DEAD for A_DTL (both order data), so the counter reading of 18b and the (LEX)+(NR) ⇒ n(n+3) route
  are dead. Status of (1): no per-context potential over the actual state; the state can even return (18f, synthetic).
- DATA that survives (experiments/alg/dtl_steal.py, corpus C; for every round whose input is the same in two consecutive
  calls at a context): every Lemma R carry STEALS (some later region loses vertices or a top is swallowed): Oink order
  701/701 carry rounds, stable 661/661. Yet the union U never shrinks (701/701, 661/661) and the survivors never shrink
  (701/701, 661/661). Candidate (U-MONO_DTL), DATA only: at a fixed context and a fixed round input V, U(V, T) ⊆ U(V, T')
  for the tangle sets T ⊆ T' of consecutive DTL calls. Synthetic genuine tangles break it (dtl_lexcounter.py), so a proof
  needs DTL's learning order. It would give per-round monotonicity in T (so every DEF change starts with V_r0 growing, as
  LEX-R), but nothing across rounds: lex_viol_oink_n20's fall comes from the input difference after r0 (17 alive as a top
  in later rounds), not from a carry.
- PROVED (from 18a): for inputs X ⊆ Y at the same T, every vertex of X whose priority is ABOVE every vertex of Y \ X
  survives in Y if it survives in X (A_q is unchanged, V^{<q} grows). So an extra top can only hurt vertices of its own
  priority or lower; lex_viol_oink_n20 is the same-priority case.
- Anatomy of lex_viol_oink_n20 (Oink order; regions per round, original ids; stored tangles at search 3: {11, 18} escape
  2, {6} escapes 1, 10; the new tangle at search 4: {13} escapes 0, 5, 6). Rounds 1-2: same inputs and same regions.
  Round 2 survivors differ (17 survives under the new tangle: the threshold phase, U equal). Round 3: in search 3, 17 is
  dead, so top 3 (priority 21) gets the region {2, 3, 5, 6, 10, 11, 18} (through the tangle {11, 18}). In search 4, 17 is
  alive and is processed before 3 (same priority, higher index); its region {17, 18} takes 18, the tangle {11, 18}
  straddles, and 3's region is only {2, 3}. Vertex 5 (priority 16) is then in no region, and vertex 10 dies at round 3.
  The lower deaths then propagate upward through the V^{<q} and same-level-region dependence of 18a, until 19 dies one
  round earlier. Same mechanism as dtl_lexcounter.py, with an extra same-priority TOP (a riser) as the stealer instead of
  a new tangle.
- What survives at a fixed context. (LEX-R) (the first differing round set grows) holds on lex_viol_oink_n20 and on all
  775/755 corpus pairs; it follows from per-round monotonicity at r0 (same input), i.e. from (U-MONO_DTL) at r0. It makes
  the round vector injective in time, but the number of ⊆-lexicographically increasing round vectors is exponential, so
  it gives no polynomial bound. Answer to queue item (1): no quantity of the per-context state is known to bound DEF changes
  at a fixed (context, M); the per-context facts that are true (Lemma R; LEX-R as DATA) are lexicographic, and the
  failures (lex_viol_oink_n20 on DTL; dtl_staterevisit.py synthetically) show why: a steal by a higher region (a riser or a
  new tangle) hurts the rest of a straddler only at the higher threshold, and the loss then propagates UP through the
  V^{<q} dependence of 18a.

### 18i. (CM) FAILS in an actual A_DTL run (17:00Z)
- experiments/alg/instances/cm_viol_oink_n28.pg (dtl_cmclimb.py seed 301 from h4_def9_oink_n28.pg, 126 climb steps;
  pinned Oink: 1 dominion, 18 tangles, 9 iterations, verified; dtl_pyref --order oink agrees). Searches 5 → 6 of one phase:
  depth-0 piece 0 makes a DEF change (same context, ideal result unchanged, actual −1 return set GROWS), so piece 1's
  context SHRINKS from 27 to 24 vertices; piece 1's ideal (C6) result is stable in both searches; the child's actual round
  count M DROPS 7 → 6 and 7 common child vertices die earlier. dtl_cmviol_check.py (in check.sh) reproduces it in both
  order data. The corpus count (§18d, 51/0) missed it because no committed instance had the shape; 126 climb steps found it.
- Type: the SHRINK row of §18g (parent return set grows, Dom(prevV) grows, the child loses vertices). §15's reading for
  shrink resets: lost tangles (a tangle needs all its vertices in the context).
- Consequence: (CM) is DEAD. Queue item (2) closes negatively: the child of a deficit parent can re-climb (its M drops)
  in an ideal-stable context, so nested deficit runs are not stopped by any monotone child round count.
- Anatomy of cm_viol_oink_n28 (Oink order, original ids; Odd's phase). Piece 0 (|R| 28, ideal stable both times): actual
  −1 return set {23} → {1, 2, 23, 27}. Piece 1's context loses {1, 2, 27} (Dom of the larger return set), nothing added;
  no stored tangle loses a vertex (so this reset is NOT §15's lost-tangle shape). The three removed vertices are p-parity
  TOPS of the old child context (priorities 19, 5, 17). New tangles between the searches: {5, 6, 17, 18}, {8}, {21}. Child
  deaths drop for 7 vertices (e.g. 14: 7 → 4, 9: 6 → 3, 4: 6 → 3); child M 7 → 6. The climb (seed 301) reached 3 M-drops
  in one run by step 3,155 (scratchpad, not committed).

### 18j. L-RED's box-4 instances under these tools; the r0 padding fix; state revisits on DTL (17:20Z)
- lex_viol_inj_n28 and lex_viol_tie_n28 (red/carry/instances, R18) under dtl_plateau.py, both order data: at s5 → s6
  (ideal-stable DEF step, U equal at r0 = 3, so LEX-R holds: V_3 grows) the top changed vertex 2 (priority 43) falls 8 → 7
  while 20 (priority 41), 18 and 7 rise; M 13 → 12; at six contexts of the same searches (|R| 28 … 23). The rise of the
  LOWER vertex 20 at round 3 propagates up over the later rounds (18a) until 2 dies a round earlier. Same mechanism as
  lex_viol_oink_n20 (an extra top, here of lower priority, then upward propagation), and as dtl_lexcounter.py with a riser
  in place of the new tangle. "DEF-down" in the result sense of §18f (stable result shrinks, or stable → −1) is still
  0 on DTL runs; in the death-vector sense the R18 step goes down. The distinction carries no weight once (LEX) is dead.
- Padding fix (L-RED caveat, Lead 16:30Z): dtl_regvec.py and dtl_crm.py padded the shorter round list with ∅, which is
  wrong past the last round of a STABLE call (its set stays at the fixpoint). Fixed (r[min(i, len − 1)]; a −1 run ends with
  ∅ explicitly). Re-run on the current corpus (experiments/alg/instances, climbs_1016, red/carry/instances): dtl_crm.py
  output is byte-identical before and after in all four settings (Oink/stable × all/ideal-stable: 372/237/345/208 steps,
  repeats 4/2/4/2, dips 18/5/19/4); dtl_regvec.py's class counts are unchanged (one detail line and one label change, a
  stable final step at r0 = 1). dtl_plateau.py (the LEX/LEX-R counts of §18b) always used the fixpoint rule. So §13g's
  (C-rM) verdicts and §16 stand.
- Full-state revisits on ACTUAL runs (experiments/alg/dtl_revisit.py; corpus C plus the R17/R18 files; maximal runs of
  consecutive searches of one phase at one context with T growing, ≥ 3 calls): Oink order 0 full-state revisits in 296
  runs (return-set-only revisits: 20 with the ideal fixed, e.g. h4_def10_oink_n28, 164 with the ideal moving); stable order
  0 in 301 (13 / 165). So on DTL data the per-context state is injective, as (LEX-R) implies; only synthetic genuine
  tangles (dtl_staterevisit.py) make it return.

## 19. Scoping note: C6 (ideal pruning) as the GAP-A target (Lead 17:08Z; at most one page)
C6 = docs/alg/candidates/C6-DTLhat.md: C5-DTL with best_vertices' consumed union U replaced by the ideal layered union Û;
sptl, Dom, cut, recursion, extraction unchanged. Prototype only: experiments/alg/dtl_c6proto.py (reuses dtl_pyref).
(a) Hypotheses of §12 on C6, per today's data. (H4) is VOID: Lemma F and Lemma S are PROVED for C6 (the actual run is the
    ideal run, monotone in T at a fixed context). The others are unchanged by the switch, and several kills were on
    deficit-free runs (A_DTL = C6 there):
    - (H1) cut-attractor carries obey the frontier property (F): READING (R10) plus DATA 67/67 (L-RED); not proved.
    - (H2a) alive-top self-reinforcing carries: OPEN; (F) FAILS for pruning-driven changes (8 of 136 drivers, §10, measured
      on A_DTL runs; C6 is identical on runs without a deficit round). APP(k) (§10) satisfies every C6 fact proved so far.
    - (H2b) dead-top cap carries: Φ, Φ_idx DEAD on C6 too (phi_idx_flat_n20 has 0 deficit calls); what remains is PROVED
      for C6: carries at index i ≤ n(n+2)·c_i (Lemma F), but c_i ≤ searches makes it circular (§14).
    - (H3) catch-ups: (CU) DEAD on C6 too (dtl_cu_viol_n24: 0 deficit calls in both order data); Lemma L-epoch PROVED (C6).
    - Child resets (§15): C6 31 of 153 child comparisons drop (A_DTL 33 of 157); the shape APP needs occurs in C6.
(b) What C6's GAP-A reduces to. With (H4) void, §6's counting is PROVED for C6: per context ≤ K = O(n²) changes, so
    N_j ≤ K·C_j over DISTINCT level-j contexts (revisits are free). Hence GAP-A for C6 ⇔ a polynomial bound on the number
    of distinct child contexts that a parent piece hands out AND in which the child still has work (fresh, resetting child
    contexts, §6.3b/§16). That is exactly the open core today; APP(k) shows the proved facts allow 2^k. C6 removes one
    obstruction (fixed-context resets, which today killed (LEX), (NR), (CM) on A_DTL); it does not touch the core.
(c) Completeness. CONFIRMED: no gain. [per referee: K5 (i)/(iii) are false as written, see GAP-C.md §18n (C); the C6 sketch
    needs the same restriction.] K4 carries over; K5 for C6 reduces to A_DTL's GAP-C shapes ((α) with the straddle
    set enlarged by the deficit, (β'), (C-b)); C6-DTLhat.md K5 sketch. DATA: prototype correct with verified strategies on
    1,530 games; completeness climbs (~19k steps, n = 16, 22) found no failure.
(d) Running time per search. One pruning round: one tangle attractor per priority level of V (≤ d + 1 levels) plus the
    unchanged threshold loop: O((d + n)·W_A), W_A = one tangle-attractor pass = O(m + Σ_{t ∈ T} (|t| + |esc(t)|)), the same
    order as C5's round (DTL-proof.md §3(b)). Rounds per call ≤ n; calls per search as in C5. So a search is polynomial in
    n, m and |T|, and |T| ≤ n·(searches so far) by Lemma W (extraction is unchanged). Only indices and priorities are
    stored: no large numbers (TARGET.md §3). The running-time bound of C6 is therefore polynomial iff searches per phase
    are, exactly as for A_DTL.
(e) Gauntlet steps 1-3 for C6 (TARGET.md §5):
    1. Exact pseudocode frozen in the lane notebook (C6-DTLhat.md already gives it as a one-function diff to C5-DTL.md; it
       needs the order datum ω and a freeze like L26) and ONE implementation. The prototype reuses L-ALG's dtl_pyref; a
       clean implementation (or a patched Oink best_vertices) is needed.
    2. Agreement with Zielonka on 10,000 random games and every hard family, strategies output and verified (L-COMP),
       runtime growth plotted; then a second independent implementation.
    3. Barrier statement and literature check (L-LIT): whether ideal layered pruning appears in van Dijk's DTL variants or
       elsewhere, and which lower-bound frameworks (e.g. attractor-decomposition) C6 lies outside. DTL's step-3 caveats
       (T16) carry over since only the pruning changes.
    Step 4 then starts from DTL-proof.md: soundness, strategies, halting carry over (reading in C6-DTLhat.md); GAP-C as
    A_DTL; GAP-A as in (b).
Reading (L-ALG): C6 is the cleaner target for a GAP-A proof (one fewer reset device, and every per-context lemma PROVED),
but the core question, fresh resetting child contexts, is identical. The switch is worth its gauntlet cost only if the
fleet commits to the GAP-A core proof on C6. It does not by itself move GAP-A.

## 20. The core on C6 (Lead L31, 17:27Z: C6 is the model for "fresh, resetting child contexts"): what is proved, what the data says, the missing lemma (17:35Z)
Setting: C6, one phase, a depth-0 Dom(prevV) piece j at a FIXED context R_j returning −1 in consecutive searches, its
child piece j+1 with context R_{j+1} = R_j \ Dom_T(V_j) (V_j the −1 return set).
- Lemma P (plateau chain; PROVED for C6 from Lemma S (ii) and Lemma D3). While piece j's round count M stays equal, its
  return set only grows (Lemma S (ii)) and T only grows, so Dom_T(V_j) only grows (D3: monotone in V and T) and the child
  contexts form a DECREASING chain R_{j+1}(s) ⊋ R_{j+1}(s') ⊋ … (length ≤ n). Every new child context inside a parent
  plateau is therefore a strict shrink; new vertices enter the child context only at a parent M-rise (≤ n + 1 per parent
  context). DATA agrees: dtl_stair.py (C6, stable order; corpus experiments/alg/instances + climbs_1016 +
  red/carry/instances + 400 random games n ≤ 26): all 55 child-context changes caused by equal-M growth are SHRINKs.
- Child resets on C6, by parent step type (same run; reset = a vertex common to both child contexts dies earlier):
  | parent step | child context | changes | child resets | child M drops (both −1) |
  |---|---|---|---|---|
  | equal-M growth (plateau) | SHRINK | 55 | 15 | 3 |
  | M-rise | GROW | 86 | 15 | 2 |
  | M-rise | SHRINK | 7 | 0 | 0 |
  | M-rise | incomparable | 45 | 7 | 1 |
  So on C6 the child re-climbs (its M drops) after both kinds of parent step, including inside a parent plateau where
  its context only shrinks. Shrinking the context is not monotone for the child (§15: lost tangles; also lost p-tops,
  §18i's anatomy on A_DTL).
- Counting this gives (PROVED for C6): per parent context, the child sees ≤ (n+1) plateaus × ≤ n contexts (Lemma P) and
  does ≤ K = O(n²) changes per context (Lemma S), so ≤ n(n+1)·K child changes per parent context, and c_{j+1} ≤
  n(n+1)(n+1)·c_j (§16). The product over the depth is the only remaining obstruction, and it needs resets at every level.
- The missing lemma, stated precisely (a target; no proof; no data yet beyond the table). Call a child reset NESTED if,
  in the same transition s → s+1, piece j+1's reset is followed by a reset of piece j+2 in its new context, and so on.
  A polynomial bound on searches per phase follows if (and, against APP(k), essentially only if) resets do not nest to
  depth growing with n, i.e. if "a reset of piece j+1 caused by a parent step leaves piece j+2 in a context where it does
  not need to re-climb" holds up to bounded depth. Measurement for the next box (cheap, dtl_stair.py extended): the depth
  of nested resets per transition on C6, on the corpus and on climbs whose fitness is that depth. Attack for L-RED: a C6
  instance with nested resets of depth ≥ 3. Note that a depth-2 nested reset already exists implicitly in
  h4_nested7_oink_n44 on A_DTL (fresh contexts at pieces 2-5 grow with depth), but there the children did not reset; the
  C6 question is whether fresh AND resetting contexts compound.
- Measured at once (17:33Z), experiments/alg/dtl_nestreset.py (C6, stable order): over the corpus (experiments/alg/
  instances, climbs_1016, red/carry/instances; 518 transitions) the nested-reset depth per transition is 0 in 480, 1 in
  15, 2 in 12, 3 in 11 (16 games, all climbed: dtl_replay2deep_n32, dtl_replay4_n32, flat_dead_carries_*, nest_nest_*,
  nest_seed*, phi_flat_alive_n32); 400 random games add no depth ≥ 2. But the measure is CHEAP to game: a climb on it
  (dtl_resetclimb.py seed 401 from dtl_replay2deep_n32; scratchpad, stopped) reached depth 13 at n = 32 within 617 steps,
  with 3-4 iterations in total: one transition shifts every later piece's context and nudges a death down, and no child
  then does any further work. So the depth of resets in ONE transition is not the obstruction. What the core needs is a
  reset FOLLOWED BY re-climbing work (further changes of the child in its new context before the parent moves again),
  i.e. §6's replays. Corrected target: replay depth (§6.3: max depth 2, 5 replays, nest_nest_s81 / dtl_replay2deep_n32),
  whose growth with n is the question; on C6 the climbs of §6.3 plateaued (notebook, successor 3).
- Replay-depth climbs on C6 (experiments/alg/dtl_replayclimb.py, fitness = replay depth ≫ replays ≫ longest phase;
  stable order; seeds from dtl_replay2deep_n32, which scores depth 1 under the corrected tracer): replay depth 3 reached
  at n = 32 (seed 601, step 2,671) and at n = 48 (seed 602, dtl_replay2deep_n32 padded by 16 priority-0 source vertices,
  step 330). Committed: experiments/alg/instances/c6_replay3_n32.pg (C6: 11 iterations, 26 tangles, 4 replays, depth 3,
  correct with verified strategies against Zielonka; A_DTL in stable order has the same (4, 3); pinned Oink 11 iterations,
  verified) and c6_replay3_n48.pg (C6: 13 iterations, 34 tangles, (3, 3); Oink 13 iterations, verified). Before this box
  the maximum anywhere was depth 2 (§6.3). Level sequence of the n = 32 phase: 3 1 1 2 0 1 3 2 3 0. Whether the depth
  keeps growing with n is the open measurement; climbs continue.

### 18k. L-RED's (F1) ("at most one fall step per context"; l-red 78469a8, Lead 18:34Z) is not structural (18:40Z)
- experiments/alg/dtl_twofall.py (in check.sh): two DISJOINT copies of the dtl_lexcounter.py gadget in one context
  (18 vertices, genuine tangles). Chain {s, s'} → {s, s', σ} → {s, s', σ, σ'}: e0 falls (INF → 1) at the first step, e0'
  at the second. Two fall steps at one context. Since disjoint components do not interact, the same holds for any number
  of copies: k fall steps on 9k vertices, with k steal tangles learned one per step.
- Random synthetic data says little either way: 2 chains with one fall and 0 with two in about 122k random chains
  (dtl_lexfake.py, genuine and fake tangles, n ≤ 12), and 63 one-fall / 0 two-fall chains in 34,980 chains around the
  gadget (scratchpad gadfall2.py).
- Reading: (F1) can hold for A_DTL only through WHEN DTL learns the steal tangles. [CORRECTED 19:16Z: the guess that
  DTL learns the steals of independent components in the SAME search is FALSE in general: L-RED R20's f1_twodef_n48 has
  two DEF falls at one context in two disjoint components.] A counter to (F1) on
  DTL needs a second steal tangle that becomes learnable only AFTER the first fall, i.e. a dependency from the first
  gadget's fall (or its repair) to the second gadget's steal. That is the attack recipe for L-RED. A proof of (F1) must
  show that DTL learns all steals that can bite at one context in one search, which is again cross-context information.
- (F1) DEAD on actual A_DTL (Lead 18:58Z): experiments/red/carry/instances/f1_twofall_n48.pg (L-RED R19, l-red 6b384b2; the
  disjoint union of lex_viol_oink_n20 and lex_viol_inj_n28 with injective priorities; Oink 8 iterations, verified): two
  fall steps at one context in both order data; one is a DEF step (ideal unchanged), the other an LRN step (ideal moved).
- (F1-DEF), the surviving DATA candidate: "at a fixed context, at most ONE DEF step (ideal unchanged) lowers any death".
  dtl_plateau.py (ctx_fallsteps; corpus C plus R17-R19 files), ideal-stable DEF pairs: Oink order 43 contexts with 0 fall
  steps, 47 with 1, 0 with ≥ 2; stable order 39 / 46 / 0. All pairs (ideal may move): Oink 352 / 47 / 1 (the R19
  instance), stable 348 / 46 / 1. Value if true: at a fixed context, DEF changes other than one are pointwise rises, so
  ≤ about 2n(n+2) + 1 DEF changes per context. Same caveat as 18k: in dtl_twofall.py BOTH falls are DEF steps (checked: the ideal
  (C6) result is the same stable 10-vertex set in all three states), so (F1-DEF) fails synthetically and a proof must use
  DTL's learning order.
- (F1-DEF) DEAD (Lead 19:02Z): experiments/red/carry/instances/f1_twodef_n48.pg (L-RED R20; Oink 11 iterations,
  verified), two DEF fall steps at one context in the two components of a union. Every per-context (H4) candidate stated
  in this box is dead; what remains at a fixed context is DATA only ((U-MONO_DTL), (LEX-R), no full-state revisit).

### 18l. Measurements for the next box: searches per phase is the headline; replay depth is weak (19:10Z)
- Replay depth (§6's replays2) is NOT padding-invariant (L-RED R20 §3, Lead 19:08Z): padding replay4_n32 with inert
  priority-0 sources keeps 13 searches but moves the depth between 1 and 4, because a priority-0 source becomes its own
  depth-0 piece and shifts the indexing. My c6_replay3_n48.pg was climbed from a priority-0-padded seed, so its depth 3 is
  suspect for the same reason; c6_replay3_n32.pg (unpadded) has depth 3, L-RED's replay4_n32.pg depth 4 (searches: 11 and
  13 iterations in total). A padding-invariant variant would count levels only over pieces that change at least once in
  the phase (trivial, never-changing pieces skipped); not implemented.
- Nest products (dtl_nestclimb.py NEST_FIT=prod, Oink order; final, all stopped 19:09Z): n = 20: 4 (K = [3, 2],
  3 child contexts, 9 searches in the phase); n = 28: 6 (K = [3, 3], 3 child contexts, 12 searches); n = 36: 2 (weak
  padded seed, stopped early); n = 44: 6 (K = [2, 3, 1], 11 searches). No growth with n; every product is capped by the
  phase length.
- Searches per phase, A_DTL, Oink order (dtl_searchclimb.py, fitness = max searches in one phase, then iterations;
  random-game starts, equal step budgets; scratchpad search/, started 19:09Z): numbers in the box-end ledger.
- ctx_fallsteps on f1_twodef_n48.pg (dtl_plateau.py, ideal-stable DEF pairs, both order data): 5 contexts with 2 fall
  steps, 2 with 1 (Lead 19:13Z asked for the re-run).
- Searches per phase, checkpoint 20:38Z (dtl_searchclimb.py, A_DTL, Oink order, random starts gen.random_game(n, n, 1, 3,
  seed 7n), climbs started 19:09Z, so equal WALL TIME; steps per second fall with n). Best per phase at equal STEP budgets
  (the logs record improvements only, so the n = 60 column is its value at its last improvement, step 8,729):
  | steps | n = 20 | n = 30 | n = 40 | n = 60 |
  |---|---|---|---|---|
  | 5,000 | 7 | 11 | 6 | 9 |
  | 8,729 | 9 | 13 | 6 | 14 |
  | 20,000 | 12 | 15 | 10 | (14 at ≥ 8,729) |
  | 38,000 | 14 | 17 | 11 | |
  | 54,000 | 16 | 18 | | |
  Snapshots committed as experiments/alg/instances/spp_n20.pg (phases 16/2/1 searches, 19 iterations), spp_n30.pg
  (18/1/1/1, 21), spp_n40.pg (7/11/1, 19), spp_n60.pg (14/2, 16); pinned Oink gives the same iteration counts, verified.
  Reading: the per-phase maximum keeps rising with the step budget at every n (the climbs have not converged), and at
  equal budget it is not monotone in n (n = 40 is a slow seed). Nothing here is above linear in n.
- Checkpoint 21:39Z: spp_n20.pg replaced by the climb's step-91,101 game: one phase with 18 searches at n = 20 (0.9 n;
  13 p-parity vertices, so more searches than p-parity vertices; Oink order; 21 iterations, pinned Oink same, verified).
  The same game in stable order has 11 searches in that phase (order datum matters a lot). spp_n40.pg replaced by the
  step-27,334 game: 14 searches in one phase (Oink; 21 iterations, verified). n = 30 last improved at step 38,146 (20:23Z,
  18) and n = 60 at step 8,729 (20:19Z, 14).

### 18m. Box-end headline: searches per phase vs n (A_DTL, Oink order; climbs 19:09Z-23:14Z, stopped)
experiments/alg/dtl_searchclimb.py, fitness = (max searches in one phase, iterations), random starts gen.random_game(n, n,
1, 3, seed 7n), mutate() of dtl_mclimb, 4 climbs in parallel (equal wall time ≈ 4 h 05 min). Steps reached (rate measured
under the same load, 22:33Z): n = 20 about 7.6 steps/s, n = 30 6.2, n = 40 1.0, n = 60 0.7. Final instances
experiments/alg/instances/spp_final_n{20,30,40,60}.pg (pinned Oink: 22 / 22 / 26 / 16 iterations, all verified).
| n | best searches in one phase | last improvement (step, time) | flat afterwards (≈ steps) | iterations | max/n | iterations/n |
|---|---|---|---|---|---|---|
| 20 | 19 (|G'| 20, 14 p-parity) | 111,532, 21:52Z | ≈ 37,000 (81 min) | 22 | 0.95 | 1.10 |
| 30 | 19 (|G'| 30, 20 p-parity) | 81,234, 22:07Z | ≈ 25,000 (67 min) | 22 | 0.63 | 0.73 |
| 40 | 19 (|G'| 40, 26 p-parity) | 31,568, 22:44Z | ≈ 1,800 (30 min) | 26 | 0.48 | 0.65 |
| 60 | 14 (|G'| 60, 34 p-parity) | 8,729, 20:19Z | ≈ 7,000 (3 h) | 16 | 0.23 | 0.27 |
At one common STEP budget (Lead 21:46Z; from the improvement logs): at 8,729 steps max/n = 0.45, 0.43, 0.15, 0.23
(9, 13, 6, 14 searches); at 20,000 steps (n = 60 never got there) 0.60, 0.50, 0.25; at 30,000 steps 0.60, 0.50, 0.40.
(c) of the Lead's 20:45Z: no phase has more searches than |G'|; spp_final_n20's long phase (player 0) has MORE searches
(19) than p-parity vertices (14); every long phase exceeds its top priority's vertex count (1-2). Order datum: the same
spp_n20 checkpoint game has 11 searches in that phase in stable order versus 18 in Oink order.
Reading: no super-polynomial signal. The best phase length is about 19 at n = 20, 30 and 40 alike, so at equal effort it
does not grow with n here; n = 20 and 30 have flattened, n = 40 and 60 were still slow. These are hill-climb lower bounds
on what DTL can be made to do, not upper bounds; the next box should rerun with equal STEP budgets, several seeds per n,
and seeds from L-RED's phase climbs.

## 21. Box 5 (successor 5, Lead "go" 23:28Z by the Lead's clock, box to ~07:30Z; produced on Opus 5.5): searches per phase (SPP)
Written from 23:53Z by date -u. Tools (experiments/alg): dtl_spp.py (phase table), dtl_spprand.py (random games),
dtl_sppclimb.py (climb on max S − |G'|), dtl_chainfam.py (tight family), dtl_sppprobe.py, dtl_psi.py, dtl_settle.py,
dtl_idx0.py (candidate potentials), dtl_firstdiff.py, dtl_piecediff.py, dtl_absorb.py (where consecutive searches differ),
dtl_spptree.py (full piece tree per search). Corpus C5 = experiments/alg/instances/*.pg, instances/climbs_1016/*.pg and
every experiments/red/**/*.pg on trunk 26417b3 (191 games).

### 21a. The statement (queue item 1; DATA, sent to the Lead 23:28Z)
Phase = a maximal run of consecutive search(p) calls of one player with no dominion found before its last call (the
dominion-finding search is the last of its phase; dtl_phasestats.py and L-RED replay.py convention). S = searches in the
phase, G' = unsolved vertices at the phase start, P = p-parity vertices of G', d' = distinct priorities of G'.
- (SPP) For A_DTL and every order datum ω, every phase has S ≤ |G'|.
- (SPP-sharp) S ≤ max(1, |G'| − 1). In C5, S = |G'| occurs only with |G'| = 1 (12 rows Oink order, 13 stable).
- Broken weaker forms: S ≤ P + c (spp_final_n20, Oink order: S = 19, P = 14; spp_n20 18 vs 13); S ≤ d' (spp_final_n20,
  Oink: 19 > 13); S ≤ number of distinct p-parity priorities (27 rows).
DATA (best phase per game, S/|G'|):
| instance | Oink order | stable order |
|---|---|---|
| spp_final_n20 | 19/20 (P 14, d' 13) | 11/20 |
| spp_final_n30 | 19/30 (P 20) | 19/30 |
| spp_final_n40 | 19/40 (P 26) | 17/40 |
| spp_final_n60 | 14/60 (P 34) | 14/60 |
| red/carry spp19_oink_n30 | 19/30 (P 18) | 16/30 |
| red/carry spp19_stable_n30 | 19/30 (P 20) | 19/30 |
| red/carry replay4_n32, phi_flat_alive_n32 | 11/32, 10/32 | same |
| red/carry h4_compound_n44, h4_compound2x2_n44, h4_def7_n28 | 9/42, 9/43, 9/27 | same |
| red/carry f1_twodef_n48, cm_mdrop_both_n28, lex_viol_inj_n28, lex_viol_tie_n28 | 8/48, 7/28, 6/28, 6/28 | 8, 7, 6, 5 |
| spp_chain_up_n43 (21b) | 42/43 | 42/43 |
C5: 416 phases (Oink order) / 424 (stable), 0 with S > |G'|. Random games gen.random_game, n = 2..8, 3,000 seeds per order:
max S = 2. Climbs (dtl_sppclimb.py, fitness = max over phases with |G'| ≥ 2 of S − |G'|, then S; 300k-400k steps from random
starts): best S = |G'| − 1 at n = 6 (Oink order), 8 and 12 (stable order); never S ≥ |G'|.

### 21b. Tightness: a family with S = |G'| − 1 in both order data (DATA, Oink-verified)
dtl_chainfam.py UP=1 k: a (pr 2k+1, Even, edges a, b), b (pr 2k, Odd, edges b, z), z (pr 2k, Odd, edges z, x_k), chain
x_1..x_k (x_j: pr 2(j−1), Odd, self-loop and an edge to x_{j−1}; x_1 → a); n = k + 3. A_DTL: Even's phase has n − 1
searches for k = 3, 12, 25, 40 in both order data; instances/spp_chain_up_n43.pg (k = 40): pinned Oink 43 iterations
(42 even), verified. Each search learns exactly one tangle {x_j} (escape x_{j−1}, already removed), and the next search
absorbs it into the preceding removal, so the stable piece where learning happens loses one vertex per search. With all
x_j at priority 0 (default) the same holds in stable order; in Oink order it collapses to 3 searches for k ≥ 25 (std::sort is
unstable above 16 equal keys; pinned Oink agrees). check.sh runs dtl_chainfam.py --check (k = 12, both order data).
Reading: the family is linear (about n iterations in all) and is the pure form of "each search but the last settles a
vertex". (SPP-sharp), if true, is exactly tight. A counter to (SPP) must reset such a chain and make it re-climb with
NEW tangles (tangles are never re-learned, (a1)); recipe sent to the Lead for L-RED (23:45Z).

### 21c. The phase bound and the cost model (queue item 3)
- Phases (PROVED, from run(), C5-DTL.md §2 lines 141-142 = dtl.cpp run() 1071-1161, non-interleaved branch; Lead ask
  23:32Z (b), answered 01:11Z by date -u). Line 141: `while G != ∅: iterations++; if not search(0): break`; line 142: the same
  for search(1). So player 0's searches are one maximal block at the start and player 1's one block after it; a search(p)
  that returns false ends ALL of p's searches for good (player 0 is never searched again after line 141 breaks, even when
  player 1's dominions later shrink G). Inside a block, a phase ends with a dominion-finding search (true, G shrinks, the
  block continues) or with the block's last search (false, or G = ∅). Hence player p has ≤ D_p + 1 phases, D_p = searches
  of p that find a dominion, and phases ≤ D_0 + D_1 + 2 = D + 2 ≤ n + 2.
  What this does NOT say: that the run is complete. A 0-dominion left in G when line 141 breaks is never found; that is
  exactly GAP-C (DTL-proof.md §5; §22 below).
- With (SPP): searches ≤ Σ_phases |G'| ≤ (n + 2)·n; tangles ≤ n·searches (Lemma W) ≤ n²(n + 2); with DTL-proof.md §3(e),
  O((|T| + n)² n⁴ (m + n²)) = O(n¹⁰ (m + n²)) word operations. Every stored number is a vertex index, a priority, a tangle
  index ≤ n³ + 2n², a stack pointer or a bit: O(log n)-bit words, so unit cost equals bit cost (TARGET.md §3). Any
  S ≤ poly(|G'|) gives a polynomial bound the same way. So (SPP) for every ω plus GAP-C (completeness) closes the D2
  polynomial-time part of gauntlet step 4. (SPP) is DATA only.

### 21d. Queue item 2: per-phase potentials tested on data (all DEAD) and what is PROVED instead
Candidates, each required to move strictly at every non-last search of a phase (C5, Oink order: 990 transitions in 247
phases with S ≥ 2; stable order 957):
| candidate | failures Oink / stable | example |
|---|---|---|
| UNION: union of the phase player's tangle vertex sets grows | 210 / 193 | spp_final_n20 searches 5-7, 9, 11-17 |
| TOPS: set of tangle tops grows | 281 / 256 | spp_final_n20: top 17 learns at searches 0, 3, 4, 6, 7, 11, 12, 15 |
| PAIRS: (top, vertex) incidences grow; NEWV: a new tangle has a vertex new for its top | 129 / 120 each | spp19_oink_n30 searches 9, 12, 14 |
| PSI1/PSI2/PSI3: sums of fixed-input tangle attractors (single sources at every threshold; region of v at pr(v); upper p-sets) | 24, 34, 33 of 37 (spp_final_n20/n30, Oink) | PSI2 flat for 18 searches |
| settled piece labels (dtl_settle.py) grow | 25 of 34 | spp_final_n30: none settles for 13 searches |
| PHI0 = Σ_v (index of the depth-0 piece removing v) falls | 300 / 290 | spp_final_n20: 18 → 72 at search 4 → 5 |
| LEX0: depth-0 removal-size vector rises lexicographically | 323 / 310 | same |
A potential of T alone (PSI) cannot work: a new tangle changes only attractors with the specific inputs the search produces.
A by-design per-vertex "settling" fails because the depth-0 results change (resets) and re-open absorbed parts.

First-Difference Lemma (PROVED, reading; A_DTL, any ω). Let s, s+1 be consecutive searches of one phase.
(i) A search is a deterministic function of (G', T_s) (T_s = tangles stored at its start): W is reset after each search and
    is read only by extraction; str is written for every vertex when it joins the current attractor before it is read; no
    dominion occurs before the last search of a phase, so S, dom_vector are empty.
[per referee, 10:15Z: G-h1 CLOSED by both referees (R2-PROVED2 §13.1). As written, (ii) is false literally: sptl's repeat
 loop (870-874) can give s an extra pass that s+1 skips (the SCC is now a duplicate, `more` is false), so a positional log
 misaligns. (ii) and (iii) are therefore stated on the LOG WITH REPEATED sptl PASSES DELETED: delete from s every repeated
 pass of an S piece before e. Proof (R2 §13.1): region by region, out(s pass 1) ⊆ out(s pass 2) ⊆ out(s+1 pass 1) =
 out(s pass 1) (1.2b), so pass 2 has the same regions; closedness is a set property (73; 519-525), so the same tops are
 closed, all already in W (529): pass 2 extracts nothing and sets no W bit; s+1 learns nothing in its one pass and has the
 same W. After the deletion both logs continue with Dom(V, R) on the same input.]
(ii) Let e be the first tangle-attractor computation (tattr), in the logs with repeated sptl passes deleted, whose output
    differs between s and s+1. Every computation
    before e is identical, so e has the same input (Z, R, Gx, maxpr) in both, and its output is STRICTLY larger in s+1.
    Proof: before e, s+1 extracts exactly the SCCs that s extracted there, which are now stored (duplicate check) and are
    not dominions (s is not the last search); so s+1 learns nothing before e and its tangle set at e is T_{s+1} = T_s^end ⊇
    T_s^e (the tangles s had at e). Attractors are monotone in T for fixed inputs (DTL-proof §3 (a2)), so the output grows,
    and strictly since it differs. □
(iii) Hence the difference is caused by tangles that s learned AFTER e in its call order, and s+1 learns only after e.
    So learning feeds back to an earlier point of the computation; the search log rises lexicographically (entries
    compared by ⊆ at the first difference). This is injective in time but gives no polynomial bound by itself (counter).
Mechanical check (experiments/alg/dtl_fdlcheck.py, box 5): (ii), (iii) and (iv) hold on all 990 (Oink) / 957 (stable)
transitions of C5, 0 violations; check.sh runs it on three long phases.
[per referee, 10:17Z (box 6): the checker now compares the logs with repeated sptl passes deleted (FDL_POSITIONAL=1 keeps
 the old alignment). It also had a defect: its "same caller" test in (ii) was vacuous, because the caller name was read one
 frame too high (always "tattr"); fixed (the caller is read in the checker's own tattr). dtl_firstdiff.py, the source of the
 DATA row below, was not affected. Re-run on the 238-file corpus (n ≤ 80), real caller test: reduced log 1,042 (Oink) /
 1,011 (stable) transitions, 0 violations; positional 1,042 / 1,011, 0 violations. Repeated passes dropped 325 / 339; kept
 because they differ from the previous pass 3,079 / 3,011; identical but extracting 0 / 0.]
DATA for (ii): the first differing tattr is in best_vertices (threshold loop: Oink 642, stable 605; regions: 266, 269) or in
the −1 attractor of search_rec (41, 42), never in sptl or Dom(V, R), in all 949 (Oink) / 916 (stable) transitions (counted
over consecutive pairs incl. into the last search). Piece level (dtl_piecediff.py; first differing best_vertices call by
tree position, context, result): Oink order RES at depth 0 (same context, other result) 710 of 990, GROW at depth 1 (a
−1 piece's recursion context grows) 107, SHRINK at depth 0 (a later sibling's context shrinks: more absorbed before it) 106,
deeper 32; stable 692 / 106 / 95 / 33 of 957 (incl. 1 GROW at depth 3).
Absorption (DATA, dtl_absorb.py): when the first piece-level difference is a SHRINK of piece k, some tangle learned by s
inside piece k's subtree lies wholly in the removed part: Oink 87/87, stable 75/75 (all of them: 81/87, 72/75; exactly the
removed part: 51/87, 44/75; s learned only inside piece k's subtree: 80/87, 69/75).
Reading (L-ALG): one phase is a nested counter. Inside an epoch (depth-0 results fixed) the depth-0 contexts only lose
vertices by absorption, ≤ |G'| steps; an epoch ends with a RES change at a depth-0 piece, which can re-open absorbed
vertices; the same holds one level down inside each −1 piece's recursion. spp_final_n20 (Oink order) has 4 epochs of
lengths 5, 3, 5, 6. (SPP) needs a reason why the epochs' total stays ≤ |G'|, i.e. why a reset re-opens only vertices whose
re-absorption is paid by vertices the reset settles. No such reason is known; the per-context results of §13-§18 (RES
changes at one context are DEF or LRN changes, up to 11 at one ideal-stable context) say a reset count per context is not
constant, so a proof must use the global phase.

### 21e. More "settling" forms (DEAD), the two phase mechanisms, resets are renewable on DTL runs (00:05Z by date -u)
- Hard families (Python A_DTL, both order data, identical): tc 4/8/12: S = 3 (|G'| 68/232/492); tc+ 3/5/7: S = 4/6/8
  (|G'| 54/180/434); counter_symsi 4/6: 3; counter_rr 4/6: 2; counter_core, _dp, _m, _ortl, _qpt, _rob (sizes 4/6, 3/4): 1.
- Further candidates (C5, Oink order; stable in brackets):
  | candidate | failures |
  |---|---|
  | the set of stored tangles attracted anywhere in the search grows; its vertex union grows | 467 / 246 of 990 |
  | (LR-SETTLE) some vertex of the learning regions of s is in no later learning region | 26 of 83 (spp_final_n20/n40, chain) |
  | (LT-SETTLE) the same with learned tangle vertices | 26 of 83 |
  | (CL) every transition moves some vertex to a lexicographically earlier full tree position | 159 of 990 (157 of 957) |
  So no literal "each search settles a vertex" holds. spp_final_n40's long Odd phase (19 searches) settles nothing in 17
  of them (LR-SETTLE and LT-SETTLE fail at searches 0-16).
- Two mechanisms in the long phases (dtl_spptree.py, Oink order). (A) ABSORPTION (spp_final_n20, n30, the chain): a fixed
  prefix of −1 pieces, then a stable learning piece that loses the tangles learned before. (B) DOMINION BUILDING
  (spp_final_n40, Odd): a long run of −1 distraction pieces (up to 20) and one stable piece at the end whose tangles at the
  same tops (17, 22) grow to most of G' until the last search finds the dominion; 17 of 18 transitions are depth-0 RES
  changes. The tangles at one top are not ⊆-monotone (top 22: vertex 12 in at search 6, out at 8).
- Resets re-open and the re-opened vertices are re-learned (experiments/alg/dtl_reopen.py; depth-0 removal index up =
  opened, down = closed; re-learned = in a tangle learned later in the phase), Oink order:
  | instance | S / G' | closed | opened | opened, then re-learned |
  |---|---|---|---|---|
  | spp_final_n20 | 19/20 | 87 | 38 (3 resets: 18, 14, 6) | 33 |
  | spp_final_n30 | 19/30 | 51 | 22 (1 reset) | 14 |
  | spp_final_n40 (Odd) | 19/40 | 303 | 110 | 98 |
  | red spp19_oink_n30 | 19/30 | 129 | 46 | 28 |
  So the renewable reset that a counter needs DOES occur on actual DTL runs. The phases stay short because absorption
  closes several vertices per search (spp_final_n20: 87 closings in 18 transitions), not because resets are impossible.
  The chain (21b) closes exactly one vertex per search. Attack recipe (sent to the Lead): a chain-like epoch (one closing
  per search) that a reset re-opens wholly and that then needs new tangles (new vertex sets).

### 21f. The author's own per-search potential: distance values (dtl.cpp computeDistanceValues) (00:21Z by date -u)
Source: dtl.cpp @ 8fbf0a7, computeDistanceValues (lines 553-639) and search() (lines 1001-1066), code under #ifndef NDEBUG
(not part of A_DTL). Under trace ≥ 3, search() computes val1 = DV(T) before and val2 = DV(T') after the search and, if the
search learned tangles without a dominion and no value changed, logs "nothing changed!" (the "throw" next to it is commented
out). DV(T)[v], for each p-priority vertex v of G, is the pruning round at which v is dropped, INF if it survives to a stable
round, computed at the ROOT context with escapes judged in all of G, one shared region set Z grown top-down in R = G (no
consumed CurR, no forgiven escapes), and the threshold sweep as written. So the author expected DV to move at every
tangle-learning search: a per-search progress measure ("distance tangle learning").
- Transcription: experiments/alg/dtl_distval.py (line by line on the dtl_pyref primitives).
- The C++ check is VACUOUS: val1/val2 are uninitialized stack arrays (int val1[nodecount()]), computeDistanceValues writes
  only the p-priority vertices of V, and the comparison loop runs over all vertices, so uninitialized entries differ and
  "nothing changed!" never prints. Checked with a Debug build of pinned Oink (scratchpad, cmake -DCMAKE_BUILD_TYPE=Debug,
  oink --dtl --no-single --no-wcwc --no-loops -t -t -t -v): 0 "nothing changed!" lines on spp_final_n20/n30/n40 and
  spp_chain_up_n43, while every reported change on the chain is an uninitialized entry (vertex 42: −961249931 ⇒ −961249765,
  41 times); no p-priority vertex value changes there. On spp_final_n20 the small-valued changes come in 3 groups, matching
  the transcription (changes at searches 0, 4, 12 of Even's phase). All changes printed are rises (5 ⇒ 6, 3 ⇒ MAX, ...).
- (DV-change), the author's expectation, is FALSE on data: DV is unchanged after 525 of 990 (Oink) / 493 of 957 (stable)
  tangle-learning searches of C5 phases; on the chain after all 41 (and the pinned C++ agrees).
- (DV-nofall) DATA: no DV value ever falls over any transition of any phase, C5: 0 of 1,237 (Oink), 0 of 1,204 (stable).
  Synthetic genuine tangles in arbitrary order (experiments/alg/dtl_dvsynth.py): box 4's counters dtl_lexcounter and
  dtl_staterevisit give no fall (their (LEX) falls are an artefact of consumption/forgiveness); random runs in 21g.
- Lemma DV-MONO (SKETCH with one GAP; any tangle sets T ⊆ T' of genuine p-tangles with escapes, G fixed): DV(T) ≤ DV(T')
  pointwise. (1) Region phase of one round, V ⊆ V', T ⊆ T' (PROVED, sketch): tops are processed in decreasing index, so the
  thresholds pr(top) are non-increasing over the stages; Z_T(after stage τ) ⊆ Z_T'(after stage τ) by induction over τ. An
  element (vertex or tangle) joins Z at the pop of a successor (escape) when its condition holds then (p-vertex: an edge into
  Z; opponent vertex: no edge into G \ Z, escapes judged in G; tangle: all escapes in Z, all vertices of priority ≤ the
  threshold). In T' every vertex popped in T by stage τ is in Z_T' by stage τ and was popped at a threshold ≥ pr(τ), so at
  the pop of the LAST required successor in T' the condition holds with a threshold at least the one used in T. A top τ
  skipped in T' (already in Z_T') was popped there at a higher threshold. (2) GAP: the threshold sweep (lines 593-620) seeds
  each level by an index scan and runs a closure plus a candidate check ONLY when its queue is nonempty at a level boundary;
  candidates of priority ≤ t are not checked at level t (break). With a larger initial Z (T'), a level of T can lose all
  its seeds, so its candidate check does not happen in T', and a candidate whose priority lies between that level and the
  next checked level is never re-checked. Monotonicity of the dropped set across such skipped levels is NOT proved.
  (3) Given (2), induction over rounds gives V_r(T) ⊆ V_r(T') for every r, hence the claim. Data agree so far (0 falls).
  DV is the ideal (C6-type, §2 Lemma 2.1, §19) root pruning, which is why it survives where (LEX) on the consuming
  best_vertices died (§18).
- Value as a potential: polynomial range (each value in 1..n or INF), pointwise monotone, so DV changes at most |V|·(n+1)
  times per phase; but it stays constant across long runs of searches (the chain: all of them), so (SPP) needs a second
  component for DV-plateaus (the absorption steps of §21d/§21e, in the −1 attractors and later pieces). Reading: the
  author's design intent was a per-search distance increase; the actual algorithm makes progress inside DV-plateaus by
  absorption in later pieces, which DV (a root-context quantity) does not see.

### 21g. DV on synthetic tangles, and how DV splits the transitions (00:28Z by date -u)
- Harness bug found and fixed before any report: the first random runs of dtl_dvsynth.py / dtl_dvfall.py /
  dtl_dvfall2.py built the solver on gen.random_game WITHOUT re-indexing vertices by priority, so "top-down" was not
  priority order; their results (3 "falls" in 4,073 chains, and the 0-fall counts) are VOID. Fixed with mkdtl()
  (re-index by (priority, id), as dtl_deficit.build does). Every other tool of this box uses the sorted build.
- Corrected runs, arbitrary genuine p-tangles (not DTL-learned), single additions T → T ∪ {t}: dtl_dvsynth.py 30000 7
  (chains, n ≤ 14): 4,194 chains, 11,151 additions, 0 falls; dtl_dvfall2.py 3000 11 5 9 (all genuine tangles on sets of
  size ≤ 4 per game): 13,368 additions, 0 falls; dtl_dvfall.py 40000 1 4 10: 77,104 additions, 0 falls.
  So the GAP of Lemma DV-MONO (a tangle is re-checked only at pops of its escapes; an escape that joins at a sweep level
  or a region stage below the tangle's top priority is never re-popped) has not been realised. My hand constructions
  failed for one recurring reason: the tangle's own top (its max-priority vertex, of p-parity) is itself a top of the
  region phase, and its region at that threshold tends to attract what the late route needed. Status: SKETCH + GAP,
  DATA 0 falls (DTL runs 0 of 1,237 / 1,204; synthetic 0 of about 101,600).
- DV against the piece-level first difference (§21d), C5, Oink order, 990 transitions: DV moves in 465 (454 with a RES
  change at a depth-0 piece, 6 SHRINK, 4 GROW deeper, 1 RES deeper); DV is still in 525: 256 RES changes at a depth-0
  piece other than the root piece, 141 GROW deeper (a −1 piece's recursion context grows), 100 SHRINK at depth 0
  (absorption), 22 SHRINK deeper, 6 RES deeper. So root DV sees the root pruning; the rest of the work happens in later
  depth-0 pieces and in recursions, where the same ideal distance would have to be taken at a context that itself changes
  (the per-context problem of §13-§18 again).

### 21h. DV*, a clean ideal distance: PROVED monotone, a global (per-phase) potential that rarely moves (00:32Z by date -u)
Definition (experiments/alg/dtl_dvstar.py). G fixed, p the phase player, T a set of p-tangles with escapes judged in G.
lfp(Z, θ) = the least superset of Z closed under: a p-vertex of priority ≤ θ with an edge into Z; an opponent vertex of
priority ≤ θ with all its edges into Z; a tangle all of whose vertices have priority ≤ θ and all of whose escapes are in Z
(its vertices join). One round on input V: Z := ∅; for each τ ∈ V in decreasing priority (ties by index), Z := lfp(Z ∪
{τ}, pr(τ)); C := the v ∈ V that do not attract into Z; for each priority level t ascending: Z := lfp(Z, t) and every v ∈ C
with pr(v) > t that attracts into Z leaves C; output V \ C. Start from V_0 = the p-priority vertices of G; DV*[v] = the round
at which v is dropped, INF if it is in a round with C = ∅ [per referee, REFEREE R-i: INF = "never dropped", which also
covers a round with C ≠ ∅ and every candidate rescued (V stays fixed, code line 767); the proof is unchanged].
Lemma DV*-MONO (PROVED). T ⊆ T' ⇒ DV*(T) ≤ DV*(T') pointwise.
Proof. lfp(Z, θ) is monotone in Z and in T (every rule is monotone in Z, and T' only adds rules). One round is monotone in
(V, T): with V ⊆ V', walk the list V' in decreasing priority; at τ ∈ V' \ V only the primed Z changes and it only grows
(lfp(Z' ∪ {τ}, θ) ⊇ Z'); at τ ∈ V both runs apply lfp(· ∪ {τ}, pr(τ)) to Z ⊆ Z', so Z ⊆ Z' throughout. "Attracts into
Z" is monotone in Z for both owners, so C' ∩ V ⊆ C at the start, and Z_t ⊆ Z'_t at every level t of the sweep (same
induction). If v ∈ V stays in C' to the end, then v ∈ C at the start and v never attracts into Z'_t ⊇ Z_t, so v stays in
C to the end. So V \ C ⊆ V' \ C'. Induction over rounds gives V_r(T) ⊆ V_r(T') for
every r (a round with C = ∅ is a fixpoint, and the primed round on a superset drops none of it by the same inclusion), so
a vertex dropped at round r under T' was dropped at a round ≤ r under T, and INF under T implies INF under T'. □
Consequences. DV* depends on T only, so in one phase (T only grows, G fixed) it is a GLOBAL potential: pointwise
non-decreasing, values in {1..n, INF}, hence it changes at most |V_0|·(n + 1) ≤ n(n + 1) times per phase. PROVED.
DATA (dtl_dvstar.py): on spp_final_n20, spp_chain_up_n43, spp_final_n40 (Oink order) DV* moves in only 10 of 83
transitions (0 falls, as proved); on C5 it moves in 465 of 990 transitions (Oink order) and 464 of 957 (stable), 0 falls:
exactly the transitions where the author's DV moves (21f: 990 − 525, 957 − 493).
DV = DV* as functions (DATA, 00:42Z by date -u; experiments/alg/dtl_dveq.py): equal on all 1,408 DTL-learned tangle sets of
the C5 phases (Oink order) and on 20,000 random (game, genuine tangle set) pairs (n ≤ 11, re-indexed by priority).
OPEN CLAIM (Lead 00:48Z): DV = DV* in general is NOT proved; until it is, Lemma DV-MONO for the author's debug DV is a
SKETCH with its GAP, and only DV*-MONO is PROVED. If DV = DV* holds in general, Lemma DV-MONO follows from DV*-MONO. Why the GAP scenario of 21f is rare (reading): a difference
needs a tangle τ outside Z whose escapes are all in Z before the sweep reaches τ's top priority; in round 1 every p-priority
vertex of τ is itself a top and its region pulls τ in vertex by vertex, so a difference needs a later round in which
τ's tops were already dropped as distractions. Not proved. So DV* bounds a minority of the searches; the rest (the
absorption and later-piece changes of 21d/21g) leave DV* (and DV) unchanged. Relation to the author's
DV (21f): the same rounds with Oink's re-check order; DV* removes the GAP by construction.

### 21i. Exhaustive small games, and why resets are expensive (designer reading) (00:37Z by date -u)
- experiments/alg/dtl_sppexh.py (harness/exhaustive.py: every game with n vertices, owners {0,1}, priorities 0..3, every
  non-empty successor set), both order data: n = 1 (8 games), n = 2 (576), n = 3 (175,616): 0 violations of (SPP-sharp).
- Reading (L-ALG, hand designs around dtl_chainfam, not a proof). For a phase to exceed |G'|, some vertex x must be
  learned in two tangles of different vertex sets after a reset, at less than one fresh vertex per extra search. Three
  facts from the pseudocode make that expensive. (1) Every out-edge of an opponent vertex x leads to an escape of every
  tangle containing x that does not contain its target, so a partner u on a new cycle through x is an escape of x's old
  tangle. (2) Old tangles stay stored and are re-absorbed in ONE search as soon as their open escapes close (the −1
  attractor chains through all stored tangles), so a reset that re-opens a chain is undone at once unless something keeps
  an escape of each old tangle open. (3) sptl consumes regions top-down, so a partner shared by several chain vertices goes
  to the highest one, whose region is not closed; the bottom vertex then finds only its old SCC (a duplicate). In every
  variant tried (one shared Even partner w with edges to all x_j; w with an edge to x_1 only; an Odd pool), the second
  epoch costs one search, or the chain stalls, or each re-learned x_j needs a private blocker vertex. So the cost of a
  renewable reset appears to be one vertex per re-learned vertex, which is what (SPP) would need. The attack direction
  for L-RED stays open: a blocker that is shared across chain vertices AND across epochs, kept open by the pruning
  (best_vertices distractions), not by the attractors.

### 21j. Option (a): the ideal distance at the first-difference context splits every phase into three step types (00:46Z by date -u)
[per referee, REFEREE-2 §10: the LRN reading (per DISTINCT context only; DV*_R uses tangles inside R) is in GAP-C.md §18n (A).]
experiments/alg/dtl_dvctx.py: for each transition s → s+1, the context R of the first differing best_vertices call (for a
SHRINK/GROW, the parent context, G' at depth 0) is the same in both searches; DV*_R = DV* on the subgame R (edges and
escapes outside R ignored, tangles inside R only, as best_vertices treats its context). DV*_R is monotone in T at fixed R
(Lemma DV*-MONO applied to the subgame R; PROVED). C5, Oink order, 990 transitions:
| first difference | DV*_R moves (LRN) | DV*_R still (DEF / absorption) |
|---|---|---|
| RES at a depth-0 piece | 572 | 138 |
| RES deeper | 7 | 0 |
| SHRINK at depth 0 (absorption) | 6 | 100 |
| GROW / SHRINK deeper (absorption into a recursion) | 4 | 163 |
Reading. Every transition is one of: (LRN) the actual result at a context changes and so does the ideal distance there,
at most n(n+1) times per DISTINCT context (PROVED); (DEF) the actual result changes with the ideal fixed (the (H4)
deficits of §13-§18; 138 of 990 here, up to 11 at one context in §13g); (ABS) the removal before a piece grows
(absorption; 263 of 990). So
  S − 1 ≤ n(n + 1)·(distinct first-difference contexts) + #DEF + #ABS,
and (SPP) or any polynomial bound needs polynomial bounds on the three right-hand terms. The first is exactly §19(b)'s
"distinct contexts" core (now with a PROVED per-context LRN budget for A_DTL itself, not only for C6), the second is (H4),
the third is the absorption chains of §21b/§21e. This is the (H1)-(H4) map of §12 restated for one phase with the new
global tools; no term is bounded yet.
Per long phase (dtl_dvctx.py DVC_V=1, Oink order): distinct first-difference contexts / LRN (max per context) / DEF / ABS:
| instance | S, |G'| | contexts | LRN (max/ctx) | DEF | ABS |
|---|---|---|---|---|---|
| spp_final_n20 | 19, 20 | 3 | 4 (2) | 0 | 14 |
| spp_final_n30 | 19, 30 | 3 | 3 (1) | 0 | 15 |
| spp_final_n40 (Odd) | 19, 40 | 12 | 16 (4) | 0 | 2 |
| spp_final_n60 | 14, 60 | 3 | 4 (2) | 0 | 9 |
| red spp19_oink_n30 / spp19_stable_n30 | 19, 30 | 3 / 5 | 6 (3) / 7 (3) | 0 | 12 / 11 |
| red replay4_n32 | 11, 32 | 6 | 7 (2) | 0 | 3 |
| spp_chain_up_n43 | 42, 43 | 1 | 0 | 0 | 41 |
So the longest phases have NO deficit step: they are absorption chains (A-type) or LRN runs over many contexts (B-type,
spp_final_n40). The deficit (DEF) steps of the corpus (138) sit in the h4_* / lex_* / cm_* instances, whose phases are
short (≤ 11). For (SPP) the two terms that the climbs push are #ABS (≤ |G'| − 1 so far) and n(n+1)·contexts (contexts ≤ 12).
Follow-up (00:55Z by date -u; dtl_phidv.py, dtl_dvctx.py DVC_PHI=1; C5, Oink order, 990 transitions):
- (PHI-DV) "PHI0 rises only when the root DV* moves": DEAD, 69 counterexamples (stable order 60); first:
  instances/climbs_1016/nest_nest_s43.pg, Odd's searches 0 → 1, PHI0 122 → 124 with DV* unchanged.
- (ABS-mono), DATA: PHI0 (the depth-0 removal-index sum, range ≤ n²) NEVER rises at a transition whose first piece-level
  difference is not a RES at a depth-0 piece: 0 rises in 280 such transitions (depth-0 SHRINK 106: all fall; deeper GROW
  145: 107 fall, 38 same; deeper SHRINK 22 and deeper RES 7: same). It rises at 184 of 710 depth-0 RES transitions: 139
  LRN (the ideal distance at that context moves) and 45 DEF.
- What (ABS-mono) would give (reading): between two depth-0 RES transitions PHI0 does not rise and it falls at every depth-0
  absorption, so S − 1 ≤ (#RES_d0 + 1)·(n² + 1) + #(transitions with PHI0 unchanged, all deeper), with #RES_d0 ≤ #LRN + #DEF
  and #LRN ≤ n(n + 1)·(distinct contexts) (PROVED). The deeper transitions would need the same argument one level down (a
  PHI at the recursion's context), which multiplies over the depth: the nested-counter core again, now with explicit
  per-level polynomial budgets for everything except DEF steps and context counts.
- KILLED (01:59Z by date -u): (ABS-mono) and (ABS-mono-pw) by L-RED R22, red/carry/instances/absmono_viol_n44.pg (both order
  data; reproduced here with dtl_dvctx.py DVC_PHI=1: one 'SHRINK d0 DEF PHI0 RISES' step; a later depth-0 piece at the
  same context goes stable → −1 under the larger tangle set, exactly the weak point named below).
- (ABS-mono-pw), DATA (01:00Z by date -u): POINTWISE form: at every transition whose first piece-level difference is not a RES
  at a depth-0 piece, no vertex moves to a LATER depth-0 piece: Oink order 280 of 280 (GROW 145, SHRINK 128, deeper RES
  7), stable order 269 of 269. Why a proof is not immediate: after the first difference, a later depth-0 piece runs at the
  same or a smaller context with a LARGER tangle set (T_{s+1} contains every tangle s learned, so at every position s+1's
  tangle set contains s's), and the actual best_vertices is not monotone in T (DEF steps), so its result could change and
  push vertices later. Attack target: such a later-piece change inside an absorption transition.

## 22. Box 7 (L-ALG successor 6, Lead GO 10:47Z by date -u; produced on Opus 5.5): the root call across consecutive searches (11:02Z by date -u)
Tool: experiments/alg/dtl_rootmono.py. The root call is the first best_vertices call of a search (depth 0, R = G'). RV(s)[v]
is the round at which the root call of search s drops the p-priority vertex v, and INF if v survives to a round that
returns 1. Transitions s → s+1 of one phase are classified by the first difference e* of the reduced logs (FDL, §21d).
Corpus: 238 files with n ≤ 80, plus gapb_dup_n20 and gapbW_dup_n20, both order data.

22a. Target 1 of the box is FALSE, and it is the known (M). The target was "the larger V_{r+1} of s+1 cannot make a later
round drop a vertex that s kept", i.e. (RMONO): RV(s+1) ≥ RV(s) pointwise. Failures (Oink / stable):

| first difference e* | transitions | RMONO fails |
|---|---|---|
| root threshold loop | 611 / 585 | 16 / 16 |
| root regions | 252 / 257 | 2 / 2 |
| after the root call | 194 / 185 | 0 / 0 |

Every failure has a deficit round, U ≠ Û (§3), in a root call: 18 of 18 in both order data. This is §4b's (M) at the
root context, dead since box 4.
Re-run with pinned Oink today: dtl_mviol_check.py printed "M-VIOLATION REPRODUCED". Oink's own -t -t first-call
distances fall: orig16 and orig1 8 → 7, orig19 9 → 8. The obstruction is Lemma E (§3): a straddling stored tangle whose
unconsumed rest is re-absorbed by a lower surviving top.

22b. What does hold at the root call (candidates; DATA, with proof routes).
- (RV-ND) If the root call of s has no deficit round, then RV(s) = DV*(T_s), with DV* from §21h and T_s the tangles at
  the start of s.
  - DATA: 1,363 / 1,363 deficit-free root calls (Oink), 1,354 / 1,354 (stable). With a deficit, RV ≠ DV* in 180 / 182
    and 168 / 170.
  - Route, PROVED (reading): with no deficit, Theorem M-cond's chain gives V_i = V̂_i, the ideal rounds of §2-3. The ideal
    rounds are DV*'s rounds:
    - Û_{≥q} = Attr_q(Û_{>q} ∪ V_q) is DV*'s Z after the tops of priority ≥ q. lfp at one threshold absorbs the tops of
      that priority one at a time or all at once.
    - Ŝ's test "attracts into Attr_t(Û) for some t < pr(v)" is DV*'s ascending sweep, since Attr_t is increasing in t.
- (PSI-MONO) Let Ψ(s) be the list of the root call's round unions U_r and rescue sets W_{r,t} (after each level t of the
  threshold loop). If RV(s) = RV(s+1) and neither root call has a deficit, then Ψ(s) ⊆ Ψ(s+1) componentwise.
  - DATA: 235 / 235 such root transitions (Oink), 230 / 230 (stable). Strict in 218 / 212.
  - Route, PROVED (reading): the V_r are the same in both searches. With no deficit, U_r = Û(V_r, T), which is monotone
    in T (Lemma 2.1). The code's rescue set at level t is the closure Attr_t(U_r) (DTL-proof Lemma 1.2: the pop loop with
    all of Z pushed computes the closure), monotone in U_r and T (1.2b).
- (POS-FALL) If, in addition, Ψ(s) = Ψ(s+1), then Φ_pos(s+1) < Φ_pos(s), where Φ_pos = Σ_r Σ_v (rank, in processing
  order, of the round-r region containing v).
  - DATA: 17 / 17 (Oink), 18 / 18 (stable). In every such case e* is a root region tattr: one region grows while the
    union stays fixed.
  - Not proved. FDL gives an equal input and a strictly larger output at e* with the earlier regions unchanged, so the
    new vertices come from later regions.
  - The gap: a later region is computed in a smaller arena CurR. The region attractor (Gx = CurR) is not monotone in its
    arena (an opponent vertex forgiven outside a small arena must cover more successors in a larger one), so a vertex
    could in principle move to a later region.
  - Data: in Ψ-growing transitions Φ_pos never rises (falls 43, equal 175, Oink order).
- Consequence (PROVED from the three, given POS-FALL). In one phase, order the deficit-free root-call transitions by
  (DV*, Ψ, −Φ_pos) lexicographically. Each one raises this triple:
  - (a) RV moves: then DV* moves, by RV-ND on both sides. DV* is pointwise monotone (DV*-MONO), so this happens at most
    n(n+1) times per phase.
  - (b) RV is fixed and Ψ grows strictly (PSI-MONO).
  - (c) Ψ is equal and Φ_pos falls (POS-FALL).
  - Transitions after the root call leave the root call identical, so they change nothing.
  - Ψ has at most (n+1)(d+2) components, each ⊆ G', and Φ_pos ≤ (n+1)n². So between two consecutive DV* moves or root
    deficit transitions there are at most H := (n+1)(d+2)n · ((n+1)n² + 1) + 1 deficit-free root transitions, and
    #(root-call transitions) ≤ (n(n+1) + #DEF_root + 1) · H + #DEF_root, where #DEF_root counts root transitions with a
    deficit on either side (Oink 174, stable 160 on the corpus).
- So, given POS-FALL, GAP-A at the root call reduces to bounding #DEF_root, the root transitions with a deficit, which are
  Lemma E's straddles.
- The other part of a phase is the transitions whose first difference lies after the root call: Oink 194, stable 185,
  i.e. 18% of all transitions. These are box target 3, the same frame at the first differing deeper call, which is the
  per-context problem (§21j).

22c. PREFIX-MONO and the root-call bound (reading, L-ALG; DATA first, below; 11:32Z by date -u)
Setting: one pruning round of best_vertices in context R, with input V and tangle set T.
- Tops are processed in decreasing index order. Index order follows priority (O1), so the priorities of processed tops
  never increase.
- A top τ ∈ V is PROCESSED iff τ ∉ P(τ⁺), where P(τ⁺) is the union of the regions of the processed tops of higher index.
  Then P(τ) := P(τ⁺) ∪ region(τ); otherwise P(τ) := P(τ⁺).
- Cl_q(B) is the least superset of B closed under the threshold-q rules in R (dtl_ideal.lfp): vertex rules for
  priorities ≤ q, and the tangle rule for an alive tangle with every vertex of priority ≤ q and every escape in the set or
  outside R.
- The round is STEP-IDEAL if P(τ) = Cl_{pr τ}(P(τ⁺) ∪ {τ}) for every processed τ. Otherwise it has a STEP DEFICIT.
- DATA: a step deficit occurs whenever the final union has a deficit (U ≠ Û, §3). The converse fails rarely (5 / 16
  root transitions, Oink / stable, have a step deficit but no final deficit).
(S0) For every processed τ, P(τ) ⊆ Cl_{pr τ}(P(τ⁺) ∪ {τ}). This is Lemma 2.2's induction restricted to one region: every
  derivation of the consuming attractor is a threshold-q rule whose premises lie in P(τ⁺) ∪ region(τ), and the consumed
  set lies outside Gx = CurR.
(S1) Cl_q is monotone in B and in T (1.2b). A set closed under the threshold-q′ rules is closed under the threshold-q
  rules for q ≤ q′.
Lemma PREFIX-MONO (PROVED, reading). Let V ⊆ V′ and T ⊆ T′, and let the round of the LATER run (V′, T′) be step-ideal.
Then P(τ) ⊆ P′(τ) for every index τ.
Proof, by induction over τ in decreasing order (P = P′ = ∅ above every top).
- If τ is not processed in run 1, then P(τ) = P(τ⁺) ⊆ P′(τ⁺) ⊆ P′(τ).
- If τ is processed in run 1 (τ ∈ V ⊆ V′, q = pr τ), then P(τ) ⊆ Cl_q(P(τ⁺) ∪ {τ}) by (S0).
  - If τ is processed in run 2: P′(τ) = Cl′_q(P′(τ⁺) ∪ {τ}) ⊇ Cl_q(P(τ⁺) ∪ {τ}) by (S1).
  - If not, τ ∈ P′(τ⁺) ≠ ∅, and P′(τ⁺) = Cl′_{q′}(…) for the last processed top τ′ > τ of run 2, with q′ = pr τ′ ≥ q.
    So P′(τ⁺) is threshold-q closed and contains P(τ⁺) ∪ {τ}. Hence P′(τ) = P′(τ⁺) ⊇ Cl′_q(P(τ⁺) ∪ {τ}) ⊇ P(τ). □
Corollaries, assuming the later run's round is step-ideal:
- (C1) U(V, T) ⊆ U(V′, T′).
- (C2) The rescue sets satisfy W_t ⊆ W′_t. The threshold loop has Gx = R, consume = None and all of Z pushed, so it
  computes Cl_t(U) (DTL-proof 1.2).
- (C3) Survivors: V_next ⊆ V′_next (the survivor formula S of §1 is monotone in U and W_t).
- (C4) NO-LATER: every v ∈ U(V, T) lies, in the later run, in a region whose top has index ≥ that of its region top in the
  earlier run (v ∈ P(τ) ⊆ P′(τ)).
- Over all rounds: if every round of the later run is step-ideal, then V_i ⊆ V′_i for all i. So the root pruning rounds
  never fall (RMONO), and a stable V* never shrinks. This strengthens Theorem M-cond (§3) to the prefix sets.
POS-FALL (PROVED, reading, from PREFIX-MONO and the First-Difference Lemma, §21d, signed). Let s → s+1 have the same RV
and the same Ψ (round unions and rescue sets), with s+1's root call step-ideal in every round, and let e* lie in the root
call.
- e* cannot be in a threshold loop: there its output would be strictly larger, contradicting equal Ψ.
- So e* is the region of some top τ_j in round r. It has the same input in both searches (P(τ_j⁺) is equal, since the
  earlier log entries are identical) and a strictly larger output.
- So some v ∈ region′(τ_j) \ region(τ_j) exists. v ∈ U_r(s) = U_r(s+1), and v ∉ P(τ_j), so in s its region top has a
  lower index than τ_j.
- With (C4) for every other vertex, Φ_top := Σ_r Σ_{v ∈ U_r} (n − index of v's region top) falls strictly. □
Theorem ROOT-BOUND (PROVED, reading). Fix a phase (G′ and p fixed). Call a transition s → s+1 CLEAN if the root call of
s+1 is step-ideal in every round, and DIRTY otherwise. Let Π(s) := (RV(s), Ψ(s), Φ_top(s)), ordered lexicographically by
RV pointwise ↑, then Ψ componentwise ⊆ ↑, then Φ_top ↓.
- A clean transition whose first difference e* lies in the root call raises Π strictly: either RV rises (RMONO, ≠), or
  RV is equal and Ψ grows strictly ((C1)-(C2), ≠ since FDL makes the output at e* strictly larger), or Ψ is equal and
  Φ_top falls (POS-FALL).
- A transition with e* after the root call leaves the root call, and Π, unchanged.
- Chain heights: RV has at most n(n+1) strict rises (values 1..n+1 or INF). Ψ has at most (n+1)(d+2) components, each
  ⊆ G′, so at most (n+1)(d+2)n strict rises. Φ_top ≤ (n+1)n² gives at most that many falls.
- Hence, per phase: #(transitions with e* in the root call) ≤ (#DIRTY + 1)·H + #DIRTY, where
  H := (n(n+1) + 1)·((n+1)(d+2)n + 1)·((n+1)n² + 1).
So GAP-A at the root call reduces to ONE statement: the number of DIRTY transitions per phase (the later root call has
a step deficit, i.e. Lemma E's straddle at some region step) is polynomial.
DATA (dtl_rootmono.py; corpus 238 files plus gapb_dup_n20, gapbW_dup_n20, kin_viol_n29; Oink / stable):
- Every prediction for clean root transitions holds (RMONO, Ψ monotone when RV is equal, Φ_top falls when Ψ is equal, no
  vertex moves to a lower-index top): 689 / 689 and 673 / 673.
- DIRTY root transitions: 179 / 174. Phases with one: 36 / 39.
- Max dirty per phase: 12 / 10, at most 0.43 / 0.32 of |G′|. The maxima are the h4_defK families, which were built in box
  4 to maximise deficits. There dirty = K + 1 (h4_def9/10/11_oink_n28: 10, 11, 12) and every transition of the long phase
  is dirty.
- Transitions with e* after the root call: 194 / 185 (box target 3).

22d. Sharper, DATA only: Π rises unless RV falls (11:42Z by date -u; dtl_rootmono.py "PI at root-e* transitions")
On all root-e* transitions (corpus plus gapb_dup_n20, gapbW_dup_n20, kin_viol_n29; Oink / stable):

| class | Oink | stable |
|---|---|---|
| Π rises through RV | 612 | 595 |
| Π rises through Ψ (RV equal) | 221 | 215 |
| Π rises through Φ_top (RV, Ψ equal) | 17 | 19 |
| RV falls | 18 | 18 |
| Ψ not monotone, or Π does not rise | 0 | 0 |

- The 18 falls lie in 16 phases, at most 2 per phase. The two 2-fall phases are L-RED's f1_twodef_n48 and
  f1_twofall_n48, which were built to have two falls.
- So the DIRTY transitions that do not lower RV behave as clean ones: 161 / 156. The step deficit is real there (a
  tangle straddles), but it does not break the order.
- NEWX ("a tangle of T_s newly excluded at the same region step") does not separate them: 102 / 95 NEWX transitions
  satisfy the predictions; all 18 falls are NEWX.
Candidate (PI-RISE, DATA only): every transition whose first difference lies in the root call and whose root RV does not
fall raises Π strictly.
- If it holds: #root-e* transitions per phase ≤ (#FALL + 1)·H + #FALL, where #FALL counts the (M)-failures at the root
  (RV falls).
- Proved part: PI-RISE on clean transitions (§22c).
- Open part: dirty transitions where RV does not fall. The step deficit there must not shrink Ψ. In the h4_defK phases
  the same stored tangle straddles at the same top in every search, and every transition is of this kind.

[12:20Z, per referee (packet 4, R-P4 / R2-P4): the reduction below holds with two more hypotheses, (STR-DET) and
(e* ∉ Dom), and with +1 per phase (G-e2). Wording fixes R-b1, G-d1/G-Ψ: see §22h. Statements unchanged otherwise.]
22e. Every context, not only the root: GAP-A ⇐ two named statements (11:54Z by date -u; dtl_rootmono.py "ANY-CONTEXT")
Nothing in 22c uses R = G′. A best_vertices call is a deterministic function of (R, p, T): it reads no X, no str value
before writing it, and no W, and the set of alive tangles changes only at dominions. So, for EVERY context R (any depth):
- Π_R(T) := (RV, Ψ, Φ_top) of the call best_vertices(·, R, p) under T is a function of T.
- PREFIX-MONO: for T ⊆ T′, if the call under T′ is step-ideal, then Π_R(T) ≤ Π_R(T′). So along a phase Π_R(T_s)
  changes at most (D_R + 1)·H times, where D_R counts the searches s whose (possibly hypothetical) call at R has a step
  deficit.
The −1 attractor of search_rec (914-923) at a T piece runs on input (seeds, R, t). The seeds are determined by the
identical preceding best_vertices call at R and by X. Its output is the plain threshold attractor, which is monotone in T
(1.2b). So for a fixed (R, X) it changes at most n times along a phase.
By FDL (§21d, signed), a transition's first difference e* is a tattr whose input is equal in both searches and whose
output is strictly larger. It lies in a best_vertices call at some context R, or in a −1 attractor at some (R, X)
(DATA: never in sptl or Dom).
- In the first case, Π_R(T_s) ≠ Π_R(T_{s+1}). If the call of s+1 is step-ideal, the change is a strict rise (22c); a
  dirty call can lower RV.
- In the second case, the attractor's output strictly grows.
Hence (PROVED, reading; given FDL, PREFIX-MONO and the 22c corollaries): per phase,
  S − 1 ≤ Σ_{R ∈ C_bv} ((D_R + 1)·(H + 1)) + Σ_{(R,X) ∈ C_T} n,
[per referee, R9 post-landing note (packet-7 comparisons, 15:53Z): the constants are 2(F_R + 1)(H + 1) per context and
≤ 2n per input.]
where C_bv is the set of distinct contexts of first-difference best_vertices calls and C_T is the set of distinct
first-difference −1 attractor inputs. So:
- GAP-A ⇐ (CTX) the numbers of distinct first-difference contexts |C_bv| and |C_T| per phase are polynomial, and (DIRTY)
  D_R is polynomial for each of them.
- This replaces box 5's S − 1 ≤ n(n+1)·contexts + #DEF + #ABS (§21j). The ABS steps are now inside the per-context
  budget, and DEF steps matter only where RV actually falls.
DATA at e* (corpus plus gapb_dup_n20, gapbW_dup_n20, kin_viol_n29; Oink / stable):

| at the first differing call | Oink | stable |
|---|---|---|
| Π rises, later call clean (depth 0 / > 0) | 814 / 25 | 787 / 25 |
| Π rises, later call dirty (depth 0) | 161 | 156 |
| RV falls (dirty, depth 0) | 18 | 18 |
| Ψ not monotone, or Π does not rise | 0 | 0 |
| e* in a −1 attractor (C_T) | 44 | 46 |

- Distinct first-difference best_vertices contexts per phase: at most 8 (spp_final_n40, spp22_oink_n40) in both orders,
  at most 0.29·|G′|.
- Box 5's long phases (§21j table) had at most 12 first-difference contexts under its parent-context convention.
Open: (CTX) and (DIRTY), both DATA only. (CTX) is the old "distinct contexts" core, which box 5 did not bound. What is
new is that every absorption step at a fixed context is now paid for by a proved polynomial budget.

22f. (DIRTY) sharpens to (FALL); the exact obstruction for (CTX) (12:06Z by date -u; dtl_rootmono.py "VISITS", RM_KSEQ=1)
(FALL), DATA. Π_R compared over all pairs of CONSECUTIVE VISITS of a context R (any depth) within a phase, not only at e*
(corpus plus gapb_dup_n20, gapbW_dup_n20, kin_viol_n29, meet_viol_n17; Oink / stable):

| class | Oink | stable |
|---|---|---|
| equal | 5,461 | 5,310 |
| rises through RV | 1,543 | 1,495 |
| rises through Ψ | 698 | 679 |
| rises through Φ_top | 93 | 100 |
| RV falls, all at dirty calls | 73 | 72 |
| Ψ not monotone, or Φ_top rises | 0 | 0 |

- Clean visits never descend, as PREFIX-MONO predicts.
- Descents per context per phase: at most 2 (L-RED's f1_twodef_n48 / f1_twofall_n48), and 1 elsewhere, in 16 phases.
- So the budget D_R of §22e can be replaced by F_R, the number of descents of Π_R along the phase:
  S − 1 ≤ Σ_{R ∈ C_bv} (F_R + 1)(H + 1) + n·|C_T|.
  [per referee, G6-a2 (packet 6): the display reads S − 1 ≤ Σ_{R ∈ C_bv} (F_R + 1)(H + 1) + n·(|C_T| + |C_Dom|) + 1, with
  the Dom term of §22j and the +1 of G-e2; F_R as in §22n (every non-rise).]
- GAP-A ⇐ (CTX) ∧ (FALL), where (FALL) says F_R is polynomial. The data maximum is 2.
(CTX), the obstruction, made exact.
- A depth-0 context R_{k+1} = G′ \ (pieces 1..k) is fixed exactly while positions 1..k are frozen. Since Π_R is a function
  of T, the transitions at any one context are bounded over the whole phase. So the count of transitions is
  ≤ (F + 1)(H + 1)·|C|, and |C| is the only open term.
- A new context at position k+1 needs a change at a position ≤ k. With this alone, |C| can grow like (B + 1)^k: the
  nested-counter core of boxes 4 and 5.
- What would cut it: monotone removal prefixes, X_k(s) ⊆ X_k(s+1). That would give ≤ n contexts per position, so
  |C| ≤ n². It is FALSE even on clean searches. The cause is the P piece.
  - Instance: experiments/alg/instances/spp_final_n20.pg, Oink order, Even's phase.
  - The root call is −1 in both searches, and e* is in its threshold loop at round 4, where RV rises.
  - prevV is {0, 12} in s and {2} in s+1, so piece 1 removes {0, 12} in s and {2} in s+1: disjoint sets.
  - In s+1 the vertices 0, 5, 8, 9, 11 leave in piece 3 or 5 instead of 1 or 2. Depth-0 results: s = (−1, −1, 0),
    s+1 = (−1, −1, −1, −1, 1, −1, 0).
- Reason: a P piece removes Dom(prevV) = Z_f (YZ), the regions of the final pruning round, i.e. the LEVEL SET of maximal
  RV. RV rising pointwise moves that level set arbitrarily (a longer pruning ends on different vertices). So the root's
  rise reshapes every later context.
- First-difference positions (RM_KSEQ=1): long phases are either all-root (spp_chain_up_n43: 41 transitions at
  position 1; h4_def11: 12) or blocks of deeper positions between root transitions. For example spp22_oink_n40:
  4 4 4 4 4 1 4 1 6 6 4 6 6 5 5 1 6 1 1 4 1.
- A bound on (CTX) therefore needs a reason why a P piece's level-set jump cannot happen at many positions in turn.
  Candidate to test next: does a context at position k ≥ 2 recur after a root change (the same set again)? If contexts
  never recur, distinct contexts and transitions coincide in count.

22g. Do (CTX) and (FALL) share a cause? The context tree (12:16Z by date -u; dtl_rootmono.py)
Answer to the Lead's 12:02Z question: NO, not on the data. They have different causes, and neither implies the other.
- (FALL) is a Lemma E effect. Every descent of Π_R (73 / 72) is at a dirty call: a stored tangle straddles a region step
  and its unconsumed rest is re-absorbed by a lower top.
- (CTX) grows without any straddle. The obstruction instance of 22f (spp_final_n20, Oink, Even's phase) is a CLEAN
  transition. The root's RV rises, and the P piece Dom(prevV) = Z_f then removes a different level set ({0, 12} → {2}),
  so all later contexts change.
- So GAP-A ⇐ (CTX) ∧ (FALL) is two statements. Merging them into "Σ_{R ∈ C_bv} (F_R + 1) is polynomial" is a
  restatement, not a reduction, and I do not claim it as the L32 criterion.
The context tree (DATA). Depth-0 contexts form a tree along a phase: each context R_k has successor contexts R_{k+1}.
- Recurrences: 433 / 425 times a context is visited, missed in some later search, then visited again. 56 / 55 phases
  have one.
- Distinct visited contexts at all depths reach 116 per phase (spp22_oink_n40, 21 transitions, |G′| = 38), i.e. up to
  3.05·|G′|. Yet first-difference contexts number at most 8.
- Distinct successors of one depth-0 context: at most 42. This is spp_chain_up_n43's root (41 transitions: an absorption
  chain whose piece 1 changes every search). Elsewhere at most 11 (h4_def11).
Reading (SKETCH, not proved). For a fixed context R the successor depends on the call's result and on the piece:
- S piece: Dom(V*, R), monotone in (V*, T), and V* never shrinks at clean calls (22c).
- T piece: Zall, monotone in T for fixed (R, X).
- P piece: Dom(prevV). Fixed while RV at R is fixed, and monotone in T then.
So between two RV changes at R the successor shrinks monotonically. That gives ≤ (#RV changes at R + F_R + 1)·(n + 1)
distinct successors per context, which is polynomial. The open part of (CTX) is then only the PRODUCT over the
positions of a search: the visited part of the context tree must be thin, whereas each node may have polynomially many
children. That is the nested-counter core in its sharpest form so far.

22h. Packet 4 imported (per referee: REFEREE R-P4 @ f74857c, REFEREE-2 R2-P4 @ 352da6e; trunk 6aa9260; 12:20Z by date -u)
Verdicts: no REJECT. Both sign (S0), PREFIX-MONO (gap closed), POS-FALL, ROOT-BOUND (gap closed) and the bit cost
(conditional on DTL-proof §3(e)). §22e is SIGN WITH GAPS, with two OPEN gaps (GAPS rows G-DOM and G-STR).
Wording fixes (closed):
- R-a1 / R-b1 / R-Cl. Cl_q in §22c is the TRIGGERED closure of dtl_ideal.lfp. A tangle fires only with ≥ 1 escape in
  the set, and only its NEW vertices need priority ≤ q; an opponent vertex needs ≥ 1 successor in the set. (S0) holds
  either way. C2 needs the trigger: the threshold loop pushes all of Z at every level (724), so it computes exactly the
  triggered closure, W_t = Cl_t(W_{t−1}) = Cl_t(U). A trigger-free closure would overstate W_t, because a tangle with no
  escape in the set is never tried (200-201).
- G-d1 / G-Ψ. A round that returns at 716 (no candidates) runs no threshold loop. Define W_{r,t} := Cl_t(U_r) for every
  round and level, so Ψ's components align. dtl_rootmono.py compares Ψ only when the two lists have equal length. On the
  data no RV-equal pair had unequal lengths ("Ψ not monotone": 0), so the counts of §22c-g stand.
  [CORRECTION 13:13Z: false for the cross unions. union411 of UNIONS=600 SEED=11 UM_CROSS=3 (Oink order; n = 39) has
  one RV-equal pair with Ψ lengths 18 vs 1, which the old tool counted as "Ψ not monotone". dtl_rootmono.py now implements
  the convention (W_{r,t} := Cl_t(U_r) via dtl_ideal.lfp for rounds returning at 716). Under it that transition is "Π
  rises (Ψ), later call dirty". Corpus, mixed unions and cross stable had no length mismatch. Full re-run with the fixed
  tool: §22n.]
- G-e2. A transition with no differing tattr can happen once per phase (the last search re-finds only duplicates and
  returns false, 1068). The bound reads S − 1 ≤ Σ_{R ∈ C_bv} (F_R + 1)(H + 1) + n·|C_T| + 1.
Hypotheses added to §22e (OPEN):
- (STR-DET) (REFEREE-2 §0, G-STR). If every tattr before a point has equal set output in s and s+1, then every SCC
  extracted before that point is equal.
  - The danger: extraction reads str (268). A tangle that s learned later can fire in s+1 and write its stored strategy
    (171) on vertices that in s joined by vertex rules (89). The set output stays equal while the strategies differ.
  - The weak form suffices for the counting: s+1 creates no tangle before its first set difference, and every
    transition but the last has a set difference.
  - The FDL (G-h1 closure) and R5 (h) rest on it too.
- (e* ∉ Dom) (G-e1 / G-DOM). The first difference never lies in a Dom tattr (878-890 or 962-991).
  - e* ∉ sptl is proved (R-P4): pass 1 recomputes the final round's regions, and repeated passes are deleted.
GAP-A ⇐ (CTX) ∧ (FALL) ∧ (STR-DET) ∧ (e* ∉ Dom), with §22f's (FALL) in place of (DIRTY).
Partial argument for (e* ∉ Dom) (L-ALG reading, SKETCH).
- Let e* be the Dom tattr at the j-th top τ_j of a piece P with context R and removed set X. Before e* the two searches
  agree, including P's best_vertices call and P's sptl passes.
- Dom's closure output is monotone in T for a fixed input (1.2b). So a difference at step j needs a tangle t created by s
  after e*, i.e. in a later piece. By the context-chain argument (R-PROVED2 §C5), the later contexts of the call exclude
  X and the whole of s's Dom removal of P, and ancestor contexts exclude the call's whole context. So t ∩ (X ∪ Dom_P(s))
  = ∅. In particular t is NOT an X-straddling acceptance at step j: it meets neither old X nor Dom's earlier parts.
- By the (YZ) reading (GAP-C §18h; R-STEP5 claim 4), Dom's step j differs from the final round's region step j (identical
  in s and s+1) only through X-straddling acceptances.
- So e* in Dom needs an OLD straddling tangle t′ ∈ T_s^{e*}, accepted at step j in both runs, whose accepted vertices let a
  NEW non-straddling t fire in s+1 within the same step.
- Open point: exclude that interaction, or give it a budget. t′ is accepted in both runs, so its vertices lie in Dom_P(s).
  The new t fires on escapes that t′ (or the chain after it) supplied, while its own vertices lie in R \ Dom_P(s). In
  the region loop t′ is rejected, which is why t does not fire there.
DATA for both hypotheses: §22h addendum below (corpus plus unions, both orders; running at 12:20Z).

22i. Lemma STR-DET (PROVED, reading; L-ALG 12:26Z by date -u). Closes G-STR, and with it the str part of G-h1 and R5 (h)
Statement. Let s → s+1 be consecutive searches of one phase. Align their reduced logs (§21d) up to a point π, and suppose
every tattr before π has the same input and the same SET output in both. Then:
- (a) no tangle of T_{s+1} \ T_s^π fires in any sptl region computation before π, where T_s^π is the tangle set s had at
  π [per referee, W-a1 (R-P5): read T_{s+1} \ T_s^ρ, where ρ is the point of the region in question; the proof
  covers it];
- (b) every sptl region computation before π is step-identical in s and s+1, including str;
- (c) every SCC extracted before π is the same, s+1 creates no tangle before π, and the W bits agree;
- (d) if no tattr differs at all, s+1 creates no tangle, returns false (1068) and is the last search of the phase (G-e2).
Code facts used (dtl.cpp @ 8fbf0a7):
- (F1) attractTangle (110-185) changes no state when it returns false. The only exception is deleting a tangle with a
  vertex outside G (133-137); a tangle learned inside G′ never triggers it.
- (F2) sptl (477-546) computes regions of a pass in disjoint arenas (R[v] = false at each pop, 489).
- (F3) Extraction reads str only on region vertices (extractTangles(top, Z, str), 539). Every such value is written
  during that region's own computation: the vertex rule writes at join (89); the tangle rule writes at join (171); line 73
  writes only for a target vertex with str = −1, and in sptl the only target is the top, reset at 485.
- (F4) Closedness is a set property: str[top] ≠ −1 iff some successor of top is popped in the region (73); for an
  opponent top it is 519-525.
- (F5) For the SCC C_τ extracted at top τ (SCC1), every escape of C_τ lies outside Z_τ. An opponent vertex of C_τ with an
  edge into Z_τ \ C_τ would make that vertex reachable from τ.
Proof of (a). Suppose a tangle t ∈ T_{s+1} \ T_s^π fires in s+1 in the pass-1 region Z_τ of a piece P before π. Then t is
created by s after the corresponding point. Its newly added vertices lie in Z_τ(s+1), which equals Z_τ(s) (equal set
output).
- Case A: s creates t in a later piece, at any depth. By the context chain (R-PROVED2 §C5), the later contexts exclude
  s's whole Dom removal Dom_P(s), and ancestor contexts after the call returns exclude the call's whole context. So
  t ∩ Dom_P(s) = ∅.
  - But Z_τ ⊆ Dom_P(s). Dom(V*, R) (877-890) processes the tops of V* in the same order with target X. By the induction
    of PREFIX-MONO's absorbed case (O1, (S0)), the Dom set after the tops ≥ τ is closed at threshold pr τ and contains
    the earlier pass-1 regions and τ, so it contains Cl_{pr τ}(P(τ⁺) ∪ {τ}) ⊇ Z_τ.
    [per referee, G-a2 (R-P5): the justification is replaced. PREFIX-MONO's absorbed case needs a step-ideal later run,
    and Dom is not known to be one. Direct argument: let D_τ be the union of Dom's parts for the tops of index ≥ τ.
    D_τ is closed under the threshold-pr(τ) rules in R, for any T ⊆ T_s^{Dom}:
    - p-vertices: 74, 88, with O1.
    - Opponent vertices: 80.
    - Tangles: Dom's target is X, and attractTangle skips vertices already in X (136), so an earlier part does not
      reject a tangle. This is exactly the X-straddle acceptance.
    Hence D_τ ⊇ Cl_{pr τ}(P(τ⁺) ∪ {τ}) ⊇ Z_τ by (S0), by induction over the tops.]
  - So t's new vertices lie in Dom_P(s) ∩ t = ∅. Contradiction.
- Case B: s creates t in piece P itself, at a top τ′ in some pass. Then t ⊆ Z_{τ′} of that pass.
  - The pass-k regions of s up to π equal its pass-1 regions as sets: region by region the inputs agree, and
    out(s, p1) ⊆ out(s, pk) ⊆ out(s+1, p1) = out(s, p1) by monotonicity in T (1.2b).
  - By (F2) the regions of one pass are disjoint, and t's new vertices lie in Z_τ. So τ′ = τ and t = C_τ.
  - By (F4) τ is closed in pass 1 iff it is closed in pass k, and W[τ] is set at its first closed extraction (529). So t
    was extracted at τ in pass 1.
  - By (F5) no escape of t lies in Z_τ. But a tangle fires only at the pop of an escape in the current set (200-201),
    and Z_τ is the same set in s+1. Contradiction.
Proof of (b)-(d).
- By (a) and (F1), every tangle of s+1 that s does not have at that point is tried and rejected without a state change.
  So each sptl region computation before π runs the same instruction sequence in both searches, and str agrees there by
  (F3). Tattrs outside sptl may write different str, but str is read only by extraction (F3), and the later tattrs read
  only sets.
- So every extraction before π computes the same SCC (SCC1) and the same W bits. Each SCC that s created there is stored
  in T_{s+1}, so in s+1 it is a duplicate (385-424) or a dominion found again. A dominion cannot occur before the phase's
  last search.
- (d) is (c) with π at the end of the log. □
Consequences:
- FDL (ii)/(iii) hold as written on the reduced log, and REFEREE-2's G-h1 hole closes: s+1's single pass extracts the
  SCCs of s's pass 1, by (b).
- So §22e's (STR-DET) hypothesis is discharged, given this reading. The open hypotheses are (CTX), (FALL) and
  (e* ∉ Dom).
DATA (dtl_rootmono.py, corpus plus gapb_dup_n20, gapbW_dup_n20, kin_viol_n29, meet_viol_n17):
- Weak STR-DET (s+1 creates no tangle before e*): 1,065 / 1,065 (Oink), 1,035 / 1,035 (stable).
- e* caller: bv-reg 282 / 286, bv-thr 739 / 703, search_rec (−1 attractor) 44 / 46. In Dom or sptl: 0 / 0.
- No transition without a set-level difference.
- Union runs (completed): mixed unions s1, weak STR-DET 6,031 / 6,031 (Oink), 6,153 / 6,153 (stable); cross unions s11,
  3,370 / 3,370 and 3,377 / 3,377. e* in Dom 0 and in sptl 0 everywhere.
- Signed by both referees (R-P5 @ ca03021, (a) SIGN WITH GAPS, both closed; R2-P5 @ 6d508da, all SIGN). G-STR CLOSED.
- Union runs: were pending at 12:26Z.

22j. (e* ∉ Dom) as a budgeted term, and why raw inputs do not help (12:34Z by date -u)
Per-input budget (PROVED, reading). Fix a tattr input I = (caller, Z_in, R, Gx, maxpr). Its output is the triggered
closure (DTL-proof 1.2), which is monotone in T (1.2b). Take transitions s₁ < s₂ of one phase whose first differences
e*₁, e*₂ have input I. Then
  o(I, T_{s₁+1}) ⊆ o(I, T_{s₂}^{e*}) ⊊ o(I, T_{s₂+1}), since T_{s₁+1} ⊆ T_{s₂} ⊆ T_{s₂}^{e*}.
So the transitions whose e* has input I form a strictly increasing chain of subsets of G′, at most n of them.
Consequence for G-DOM. Replace the hypothesis (e* ∉ Dom) by the term n·|C_Dom|, where C_Dom is the set of distinct
first-difference Dom-step inputs. The reduction then reads
  S − 1 ≤ Σ_{R ∈ C_bv} (F_R + 1)(H + 1) + n·(|C_T| + |C_Dom|) + 1,
[per referee, R9 post-landing note: with the constants 2(F_R + 1)(H + 1) per context and ≤ 2n per input.]
so GAP-A ⇐ (CTX⁺) ∧ (FALL), with (CTX⁺) counting the distinct first-difference contexts of best_vertices calls, −1
attractors and Dom steps.
The same bound for every tattr type, S − 1 ≤ n·|I_fd| + 1 with I_fd the distinct first-difference inputs, is valid but
VACUOUS on the data: |I_fd| ≈ S − 1. For example spp_chain_up_n43 has 41 inputs in 41 transitions, and spp22_oink_n40 21
in 21; the maximum is 0.95·|G′|, both orders. The per-context Π of §22c-e is what compresses the threshold-loop and
region inputs of one call into one context. The −1 attractor and Dom steps keep the per-input form.
Where a Dom e* would come from (§22h sketch, sharpened). The new tangle t must fire in s+1's Dom step j but NOT in s+1's
final-round rescue loop, which has W_max ⊇ U and Gx = R. If t fired there, a set difference would lie before e*.
- So some escape of t lies in Dom_{≤j}(s) \ W_max: a vertex that Dom gained only through an X-straddling acceptance of
  an old tangle t′. In the rescue loop t′ is rejected, because its X-vertex is outside R (137).
- The shape is therefore an old X-straddling t′ in Dom that feeds an escape of a tangle t that s learns later, inside
  R \ Dom_P(s).
- DATA: 0 Dom e* in corpus (1,065 / 1,035) and in cross unions (stable 3,377). Mixed unions and Oink cross are pending.
DATA, cross unions s11 (UM_CROSS = 3, 600 games, stable order): weak STR-DET 3,377 / 3,377; e* caller bv-reg 1,177,
bv-thr 2,083, −1 attractor 117, Dom 0, sptl 0; clean root transitions 2,284, all predictions hold; Π at root-e*: rises
2,799, RV falls 62.

22k. (CTX): CHAIN is dead; scaling on the SPP families (12:46Z by date -u; dtl_rootmono.py "CHAIN")
- (CHAIN) "the first-difference contexts of a phase form a chain under ⊆" would give |C| ≤ n + 1 per depth. It is FALSE.
  - Depth 0: 13 of 49 phases (Oink), 12 of 50 (stable). Depth > 0: 4 phases each.
  - Smallest instance: experiments/alg/instances/dtl_searches15_n24.pg, Oink order, incomparable first-difference
    contexts of sizes 14, 16, 24. Both orders: climbs_1016/nest_nest_s43.pg, sizes 26, 26, 32.
- Scaling of |C_bv| (first-difference best_vertices contexts per phase), Oink / stable:

| instance | first-difference contexts | transitions | n |
|---|---|---|---|
| spp_final_n20 | 4 / 3 | 18 / 10 | 20 |
| spp_final_n30 | 3 / 3 | 18 / 18 | 30 |
| spp_final_n40 | 8 / 6 | 18 / 16 | 40 |
| spp_final_n60 | 2 / 2 | 13 / 13 | 60 |
| spp19_oink_n30 | 2 / 2 | 18 / 15 | 30 |
| spp22_oink_n40 | 8 / 8 | 21 / 21 | 38 |
| spp25_oink_n40 | 10 / 9 | 24 / 22 | 38 |
| fresh_fixed_n24 | 2 / 2 | 8 / 8 | 24 |

- Maximum 0.26·|G′|, with no sign of superlinear growth in n.
- The visited context tree is much larger (up to 116 nodes, §22g), so the thinness that would be needed is that of the
  FIRST-DIFFERENCE nodes, not of all visited nodes.
- Counting facts (reading):
  - A transition with first-difference position k creates at most one new successor at the node R_k. It may re-create
    every node below k.
  - So #nodes ≤ n·S, and S ≤ |C|·B: no bound follows either way.
  - A proof must charge the new first-difference nodes below k to something that does not renew at the same rate.

22l. Is (FALL)'s "at most 2 per context" structural? No: DATA only (12:59Z by date -u; dtl_rootmono.py "FALL witness")
- Mechanism (Lemma E, §3). In 72 of 73 falls (Oink) and 71 of 72 (stable), every straddling witness tangle at the
  falling call was already stored at the PREVIOUS visit of the context. So a fall is not caused by a new tangle
  straddling. It is caused by new tangles enlarging an earlier region, which then steals a vertex of an OLD tangle, the
  victim. The victim's rest is re-absorbed by a lower top, and RV falls.
- Per (context, victim): at most 2 falls. 14 phases have max 1, and 2 phases have max 2: the f1_two* instances, where
  the same victim falls twice at the same context. So "one fall per victim and context" is FALSE as a rule.
- A structural bound would have to limit how often a fixed old tangle can be stolen from at a fixed context. Between two
  falls the prefix must stop stealing, which only a non-monotone (dirty) step can cause, and then steal again.
  NOT PROVED. The ≤ 2 is the maximum on the data, and L-RED's f1_twodef_n48 / f1_twofall_n48 were built to reach it.

22m. GAP-A after box 7: one-page state (L-ALG, 13:00Z by date -u)
Statement chain. All are readings of dtl.cpp @ 8fbf0a7, for every order datum. Signatures are those of REFEREE and
REFEREE-2 (packets 4 and 5).
1. FDL on reduced logs (§21d; signed, G-h1 closed given STR-DET). Lemma STR-DET (§22i; SIGNED by both). Every
   transition except the last of a phase has a first differing tattr e*: equal input, strictly larger set output.
2. PREFIX-MONO, POS-FALL, ROOT-BOUND (§22c; SIGNED by both). For every context R, Π_R(T) = (RV, Ψ, Φ_top) rises
   strictly at each transition whose e* lies in the call at R, unless that call has a step deficit. Its chain heights
   are polynomial: H = O(n^8).
3. Per-input budget (§22j; packet 6 pending). The −1 attractor and Dom steps carry at most n first-difference
   transitions per distinct input.
4. Hence, per phase (§22e, §22f, §22j):
   S − 1 ≤ Σ_{R ∈ C_bv} (F_R + 1)(H + 1) + n·(|C_T| + |C_Dom|) + 1.
OPEN (GAP-A ⇐ both):
- (CTX⁺): the numbers of distinct first-difference contexts (best_vertices calls, −1 attractors, Dom steps) per phase are
  polynomial.
  - DATA: at most 10 per phase (spp25_oink_n40), at most 0.26·|G′|. Dom first differences: 0 in all data.
  - Exact obstruction (§22f/g): a P piece removes Dom(prevV) = Z_f, the level set of maximal RV, which jumps when RV
    rises. This happens on CLEAN calls, and it re-creates every later context.
  - Known dead routes: monotone removal prefixes (ABS-mono-pw, box 5), (CHAIN) (§22k).
  - This is the nested-counter core. Each context has polynomially many successors (sketch, §22g), but the depth-0
    positions multiply.
- (FALL): F_R, the number of descents of Π_R along a phase, is polynomial.
  - DATA: descents only where RV falls, at most 2 per context (f1_two*).
  - Mechanism: new tangles enlarge an earlier region, which steals a vertex of an OLD tangle (Lemma E). The same victim
    can fall twice (§22l).
- (CTX⁺) and (FALL) have different causes (§22g), so this is two statements, not one.
DEAD this box (with instances):
- Root-call RMONO = (M) (dtl_mviol_n20, pinned Oink re-run).
- (CHAIN) (dtl_searches15_n24, Oink; nest_nest_s43, both orders).
- The raw per-input bound S ≤ n·|I_fd| + 1 is valid but vacuous (|I_fd| ≈ S − 1).
Targets for L-RED's successor:
- (a) A family with a bushy first-difference context tree: nested P pieces whose level sets jump at several depth-0
  positions in turn. spp22/spp25 are the current maxima.
- (b) A family where one context's Π falls more than twice: repeated stealing from the same victim, e.g. h4_defK or
  f1_two* grown.
- (c) PREFIX-MONO and STR-DET themselves (signed, but the referees welcome attacks).

22n. Packet 6 (REFEREE-2 R2-P6 @ 5ef09aa; REFEREE's report pending), and data with the G-Ψ convention (13:36Z by date -u)
REFEREE-2's verdicts (Lead 12:59Z). Imported here; §22f and §22j are unchanged until both reports are in.
- §22j Dom budget: SIGN, with reading R-I. A Dom input is (the whole current X, R, top, threshold). Dom pushes only the
  top (966), and its output is a monotone function of (I, T). (DOM-e*) is no longer needed: GAP-A ⇐ (CTX⁺) ∧ (FALL).
- §22f: SIGN WITH GAPS, gap G-F1. A region e* at a DIRTY call could leave Π_R unchanged (one vertex moves up, another
  down, and Φ_top compensates). Fix: F_R := descents of Π_R along the phase + the e*-at-R transitions at which Π_R does
  not rise. (FALL) is stated for this F_R.
- Signed as DATA only: "descends only where RV falls" and "≤ 2 per context". Proved: clean visits never descend.
G-F1 count (first differences where Π_R does not rise), dtl_rootmono.py with the G-Ψ convention implemented
(W_{r,t} := Cl_t(U_r) for rounds returning at 716; e9acfb86). Counts are Oink / stable:

| set | transitions with e* | Π_R does not rise | RV falls at e* | visit-level falls |
|---|---|---|---|---|
| corpus + 4 instances | 1,065 / 1,035 | 0 / 0 | 18 / 18 | 73 / 72 |
| mixed unions s1 (900) | 6,031 / 6,153 | 0 / 0 | 100 / 136 | 323 / 527 |
| cross unions s11 (600, UM_CROSS = 3) | 3,370 / 3,377 | 0 / 0 | 53 / 62 | 167 / 217 |

- The one case I reported at 13:08 (union411 of the cross unions, Oink order) was a tool artifact: Ψ lists of lengths
  18 vs 1 under the missing convention. With the convention it is "Π rises (Ψ), later call dirty".
- Falls per context, all sets: at most 2. The 2-fall phases are f1_twodef_n48, f1_twofall_n48 and, new, union807 of the
  mixed unions (stable order, n = 45).
- Falls whose witnesses are all OLDER than the previous visit: 316 / 323 and 521 / 527 (mixed), 159 / 167 and 210 / 217
  (cross). The stealing mechanism of §22l dominates everywhere.
- So, on these data sets: F_R = number of RV falls at R, and F_R ≤ 2. [Superseded by fall3_n76 below: 3 at one context.]
Packet 6 SETTLED (per referee: REFEREE R-P6 @ 9f77ff9 with comparison §C @ ad4be01, REFEREE-2 R2-P6 §5 @ c7634a7; both agree; Lead 13:30Z; 13:39Z by date -u):
- (1) G6-a1 = G-F1. F_R counts EVERY non-rise of Π_R at R along the phase: descents, incomparable steps, and Π-blind
  e*-at-R transitions. It is not only descents. (FALL): this F_R is polynomial per context.
- (2) G6-b2. (CTX⁺) counts Dom INPUTS (X ∪ Dom_{<j}, R \ Dom_{<j}, τ_j, pr τ_j), not Dom-loop contexts. REFEREE's probe
  shows the input varying at fixed (R, X, top) in 105 of 2,110 phase-contexts.
- G6-a2: §22f's display now carries the Dom term and the +1 (marked in place).
- G6-b1: Dom pushes only the top (966), and its output is a monotone function of (input, T).
- The §22h "equal lengths" sentence is corrected in place (13:16Z, e9acfb86).
- Joint verdict: GAP-A ⇐ (CTX⁺) ∧ (FALL), given STR-DET. Both (CTX⁺) and (FALL) are DATA only.
- (FALL) data update (L-RED R31; Lead re-run 13:42Z; L-ALG re-run 13:48Z: experiments/red/carry/instances/fall3_n76.pg,
  sha1 a85133ec; pinned Oink: 3 dominions, 56 tangles, 10 iterations, verified; dtl_rootmono.py both orders: max 3
  descents at one context, 3 falls of the same (context, victim) pair, phase of 5 transitions, |G′| = 76). Details: fall3_n76.pg has 3 descents of Π_R at ONE context in
  one phase, both orders. It is a union of three 1-descent gadgets (lex_viol_oink_n20, lex_viol_inj_n28,
  lex_viol_tie_n28) with cross edges, and the same old witness tangles are stolen at each descent. So "≤ 2" is dead as a
  data bound, as §22l said it might be. A "one steal per witness" bound is also false, since witnesses are reused.

22o. (CTX⁺): CTX-ROOT is dead (13:44Z by date -u; dtl_rootmono.py "CTX-ROOT", RM_LIGHT=1)
- (CTX-ROOT) "distinct first-difference contexts per phase ≤ 1 + the number of root transitions" would have reduced
  (CTX⁺) to the root's polynomial budget. It is FALSE. Corpus, Oink order: 5 of 261 phases.
- Smallest instance: experiments/alg/instances/dtl_cnew14_n20.pg. First-difference positions are 3 1 5: 3 contexts for
  1 root transition.
- Others: strfam_S4_n22 (2 3 1), strfam_S5_n46 (2 2 3 1), spp_final_n40 and spp22_oink_n40 (8 contexts, 6 root
  transitions).
- Obstruction: inside one block where the root is frozen, the first-difference positions are not constant (2 then 3,
  or 6 4 5), so deeper contexts change without any root change. Any bound must recurse into the blocks, which is the
  nested-counter recursion again (§22g, §22k).
- Context climbs (dtl_ctxclimb.py: spp25 and spp22 starts, both orders) are running to see how far the number of
  first-difference contexts per phase can be pushed.

22p. What a long phase looks like at depth 0 (DATA; spp22_oink_n40, Oink order, Odd's phase of 22 searches; 13:56Z by date -u)
Each search's depth-0 iterations as (call result, piece size). M is a −1 piece (P or T), S is a stable piece, E is the
end:
  s0  M1 M2 M1 M2 M3 M1 M1 M1 M1 M2 M1 M2 M2 M1 M2 M2 M1 M1 M2 M1 M2 M1 S4 E1
  s3  M1 M2 M1 M2 M3 M1 M1 M1 M1 M2 M1 M2 M2 M3 M4 S10 E1
  s7  M1 M3 M1 M2 M3 M2 M1 M2 M1 S22
  s8  M1 M1 M1 M2 M1 M2 M3 M1 M1 M1 M1 M2 M1 M2 M2 M1 S15
  s10 M1 M1 M1 M2 M1 M2 M3 M2 M1 M2 M1 S21
  s11 M1 M1 M1 M3 M1 M2 M3 M1 M1 M1 M1 M2 M1 M1 M2 M2 M4 S10
  s17 M1 M3 M1 M2 M3 S28
  s21 S38
- Reading: a phase is a run of small "distraction" −1 pieces, each removing a level set Dom(prevV) of 1-3 vertices, then
  ONE stable piece that grows as the learned tangles let vertices survive pruning.
- The number of depth-0 pieces falls overall (24 → 2) but RISES twice: s7 → s8 (9 → 16 M pieces) and s10 → s11 (11 → 17).
  At both, an early distraction piece changes its level set (M3 → M1 at position 2, or M2 → M3 at position 4). This is
  §22g's obstruction at work: the level-set jump re-creates every later context, and the run of distractions behind it
  is rebuilt.
- So a (CTX⁺) proof needs a potential that pays for the rebuilt distraction runs, for instance through the vertices that
  move from distraction pieces into the final stable piece (here 4 → 38). It must survive the two re-expansions. Not
  attempted further in this box.
- Tested (14:06Z, corpus plus kin, meet and fall3 instances, Oink order, dtl_rootmono.py "DISTRACTION"): the
  distraction mass (total size of the depth-0 −1 pieces) is NOT a potential.
  - It falls at 528 transitions, stays the same at 156 and rises at 372.
  - The rises: 159 at a −1 call whose RV changed, 194 at a −1 call with RV unchanged, 18 with e* outside best_vertices,
    and 1 at a stable call.
  - So the re-expansions are not confined to level-set jumps.

22q. What a descent is charged to: (FALL-V) (14:19Z by date -u; dtl_rootmono.py RM_FALLDET=1, "FALLS per (context, vertex)")
Instance experiments/red/carry/instances/fall4_n116.pg (L-RED R31; sha1 9b174a5e).
- L-ALG re-run: pinned Oink (`--dtl --no-single --no-wcwc --no-loops`) found 6 dominions and 82 tangles in 13 iterations,
  verified.
- dtl_rootmono.py finds 4 descents of Π_R at one depth-0 context (|R| = 113), in both orders.
- The step-deficit witnesses are IDENTICAL at all four descents: the same victim tangles, the same stealing region
  tops (file ids 20, 47, 65) and the same failing tops. So the deficit is static, and (victim, stealing top) cannot be
  what is used up.
- The vertices whose RV falls are DISJOINT across the descents, one gadget per descent (file ids):
  - visits 0 → 1: 48-67;
  - visits 1 → 2: 2-43;
  - visits 2 → 3: 72-91;
  - visits 3 → 4: 110.
- Reading: each gadget's vertices first gain RV through learning, then lose it once when the static deficit catches up.
  The chain of cross edges staggers the gadgets by one search each (L-RED's delay mechanism).
Candidate (FALL-V), DATA only: along a phase, each vertex's RV at a fixed context falls at most once.
- Consequence: the descents of Π_R at R number at most |R| ≤ n. Together with the non-rise steps that F_R also counts
  (0 on all data), (FALL) would follow, and GAP-A ⇐ (CTX⁺) alone, given STR-DET.
- DATA so far: corpus plus gapb_dup_n20, gapbW_dup_n20, kin_viol_n29, meet_viol_n17, fall3_n76 and fall4_n116, both
  orders. In all 18 phases with falls, every vertex falls at most once per context. Unions (completed 14:39Z): mixed
  unions s1, 106 (Oink) / 139 (stable) phases with falls; cross unions s11, 54 / 64. Max 1 fall per (context, vertex)
  in every one.
- Proof idea (not done). A fall of v at R needs a stolen victim (Lemma E). Where the later call is clean the prefixes
  grow (PREFIX-MONO), so a stolen vertex stays stolen and v cannot regain support from that victim.
- Gap: a NEW tangle could restore v's RV and then be stolen in turn. That is the shape for L-RED: v rises after its fall
  and falls again at the same context.
(CTX⁺) climb data (14:23Z by date -u; dtl_ctxclimb.py from spp25_oink_n40, seed 7, Oink order). Instance
experiments/alg/instances/ctx12_oink_n40.pg (n = 40, |G′| = 38).
- It has 12 distinct first-difference best_vertices contexts in one phase of 23 transitions in Oink order, and 9 in 20
  in stable order.
- Pinned Oink: 3 dominions, 46 tangles, 27 iterations, verified.
- The previous maximum was L-RED's ctx11_n40 with 11. Growth so far is +2 over the spp25 start, at fixed n.
RV shape of a falling vertex (14:45Z by date -u; corpus plus fall3_n76, fall4_n116, kin_viol_n29, meet_viol_n17; Oink /
stable). For each (context, vertex) whose RV falls at some visit:
- Before the fall, its RV never decreases: 443 / 440.
- After the fall, its RV stays constant (322 / 334) or rises again (121 / 106). It NEVER falls a second time.
So (FALL-V) is not a matter of "nothing happens after the fall": a vertex regains support and still does not fall again.
Route for a proof (reading; SKETCH):
- The code's region step equals the triggered closure with every tangle that meets the earlier prefix EXCLUDED
  (138-139: a tangle vertex outside CurR ∪ CurZ rejects it).
- So PREFIX-MONO's induction goes through unless the later prefix grows into a tangle that the earlier prefix did not
  meet: a NEW steal.
- A second fall of v would therefore need a second, independent steal that affects v after v recovered. The data has
  none. Cross-union shapes are running.

22r. Lemma PREFIX-MONO-X: Π_R can descend only at a NEW STEAL (PROVED, reading; L-ALG 14:54Z by date -u)
Setting as in §22c: one pruning round in context R with input V, tangle set T, tops processed in decreasing index (O1).
P(τ⁺) is the prefix before the processed top τ. Define the EXCLUDED tangles at τ:
  E_τ(T) := { t ∈ T alive : t meets P(τ⁺) and t ⊄ P(τ⁺) }.
Lemma EXACT. For every processed τ, P(τ) = Cl_{pr τ}(P(τ⁺) ∪ {τ}; T \ E_τ), where Cl is the triggered closure in R
(dtl_ideal.lfp) with tangle set T \ E_τ.
Proof.
- (⊆) is (S0) (R-P4 (a)). The code applies only closure rules. A tangle with a vertex in P(τ⁺) has that vertex outside
  CurR ∪ CurZ, so attractTangle rejects it (137). So only tangles of T \ E_τ fire.
- (⊇) Claim: P(τ⁺) is closed under the threshold-pr(τ) rules of T \ E_τ in R. This is the argument of R-P5 G-a2 for
  the code's own prefix, using O1: every earlier region has threshold ≥ pr τ.
  - A p-vertex u ∉ P(τ⁺) with pr(u) ≤ pr τ and an edge to w ∈ P(τ⁺): at w's pop u was unconsumed, so u was attracted
    (74, 88).
  - An opponent vertex with all R-edges in P(τ⁺) is attracted at the pop of the last of them (80).
  - A tangle t ∈ T \ E_τ with t ∩ P(τ⁺) = ∅, all escapes in P(τ⁺) or outside R, and one escape in P(τ⁺): at the pop of
    its last escape all its vertices are unconsumed, so it fires there and t meets P(τ⁺). Contradiction. A tangle with
    t ⊆ P(τ⁺) adds nothing.
  - So every rule instance with all premises in P(τ⁺) is already satisfied. The region's pop loop computes the closure
    of the remaining instances (DTL-proof 1.2: every instance with a premise in CurZ is tried at that premise's pop).
  So P(τ⁺) ∪ Z_τ ⊇ Cl. □
Lemma PREFIX-MONO-X. Let V ⊆ V′ and T ⊆ T′ for one round. Assume (NS), "no new steal": for every τ processed in the
EARLIER run, E′_τ ∩ T ⊆ E_τ, where E′_τ is computed from the later run's prefix P′(τ⁺), whether or not τ is processed
there. Then P(τ) ⊆ P′(τ) for every τ.
Proof, by induction over τ in decreasing order, as in §22c.
- τ not processed in run 1: P(τ) = P(τ⁺) ⊆ P′(τ⁺) ⊆ P′(τ).
- τ processed in both runs: P(τ) = Cl(P(τ⁺) ∪ {τ}; T \ E_τ) ⊆ Cl(P′(τ⁺) ∪ {τ}; T′ \ E′_τ) = P′(τ), by EXACT twice. Cl is
  monotone in its base and its tangle set, and T \ E_τ ⊆ T′ \ E′_τ by (NS).
- τ processed in run 1 only (τ ∈ P′(τ⁺)): by the closedness claim of EXACT applied to run 2, P′(τ⁺) is closed under the
  threshold-pr(τ) rules of T′ \ E′_τ ⊇ T \ E_τ (by (NS)). It contains P(τ⁺) ∪ {τ}. So
  P′(τ) = P′(τ⁺) ⊇ Cl(P(τ⁺) ∪ {τ}; T \ E_τ) = P(τ). □
Corollary. If (NS) holds at every region step of every round (rounds aligned with V_r ⊆ V′_r inductively), then the
§22c corollaries C1-C4 hold. The threshold loop has no exclusions: Gx = R, consume = None, so W_t = Cl_t(U) over all of
T. So RV does not fall and Ψ does not shrink. Hence a non-rise of Π_R between two visits of R requires a NEW STEAL: a
tangle of the earlier visit that the later visit's prefix newly meets without containing.
PREFIX-MONO (§22c) is the special case in which the later run is step-ideal.
DATA (dtl_rootmono.py RM_EXCL=1; corpus plus fall3_n76, fall4_n116, kin_viol_n29, meet_viol_n17; consecutive visits of
every context; Oink / stable):

| visit pairs | Oink | stable |
|---|---|---|
| new steal, with a descent | 86 | 85 |
| new steal, no descent | 661 | 624 |
| no new steal, no descent | 7,312 | 7,130 |
| no new steal, with a descent | 0 | 0 |

Consequence: F_R ≤ #(visit pairs at R with a new steal). (FALL) reduces to bounding new steals per context, i.e. how
often a later prefix grows into a stored tangle that the earlier prefix did not meet.
- In a stretch with no new steal, prefixes only grow. So a fixed (step, tangle) pair can be newly stolen again only after
  some new steal has shrunk the prefix.
- That suggests a potential argument over (step, tangle) pairs, but the number of stored tangles grows with S, so it is
  circular as it stands.
- (FALL-V) (§22q) is the data-side statement that this does not compound per vertex.
(FALL-V) is FALSE (14:58Z by date -u). Instance experiments/red/carry/instances/fallv_viol_n28.pg (L-RED, from a climb on
lex_viol_inj_n28; on l-red, sha1 21b235f4).
- L-ALG re-run: pinned Oink found 1 dominion and 17 tangles in 7 iterations, verified.
- dtl_rootmono.py, both orders: "FALLS per (context, vertex): max 2". At the ROOT context, vertex 14 (priority 27) has
  RV 4, 6, 5, 4, 4: a rise, then two falls. 8 (context, vertex) pairs fall twice.
- So "each vertex falls at most once per context" is dead. My shape count above (never a second fall) held only on the
  corpus and unions.
- PREFIX-MONO-X (§22r) survives on it: 17 / 17 descents have a new steal, and no descent occurs without one.
- So the charge for (FALL) that survives is the NEW STEAL (§22r, proved as a reading): F_R ≤ #(new-steal visits at R).
  How often a later prefix newly grows into a stored tangle at one context is the open question.
How loose the new-steal charge is (15:04Z by date -u; corpus plus fall3_n76, fall4_n116, fallv_viol_n28, f1_twofall_n48,
f1_twodef_n48; Oink order; "new-steal visits per context").
- New-steal visits per context per phase reach 8: h4_def10_oink_n28 and h4_def11_oink_n28, with 11 and 12 transitions.
  Next: dtl_replay2deep_n32 and h4_nested7_oink_n44 with 7, and h4_def8 with 7.
- Descents reach at most 4 (fall4_n116). So most new steals cause no descent, and F_R ≤ #new steals is far from tight.
- In the h4_defK family new steals occur at almost every transition, growing with K like the phase itself.
- So (NEWSTEAL) is a true reduction of (FALL), but bounding it is about as hard as bounding the phase. A useful charge
  would have to separate the steals that cause a descent from the rest. Not found in this box.

22s. PREFIX-MONO-X*: the tight charge is a RELEVANT steal (PROVED, reading; L-ALG 15:10Z by date -u)
Let F_τ ⊆ T \ E_τ be the tangles that FIRED (added vertices) at the processed step τ in the earlier run.
- EXACT*: P(τ) = Cl_{pr τ}(P(τ⁺) ∪ {τ}; F_τ). The code's derivation uses only F_τ, so ⊇. By EXACT, P(τ) is the closure
  over T \ E_τ ⊇ F_τ, so ⊆.
- (NS*) "no relevant new steal": F_τ ∩ E′_τ = ∅ for every τ processed in the earlier run. That is, no tangle that fired
  at τ before is newly met, without being contained, by the later prefix P′(τ⁺).
- Lemma PREFIX-MONO-X*: let V ⊆ V′, T ⊆ T′ and (NS*). Then P(τ) ⊆ P′(τ) for every τ.
  Proof: as §22r, with F_τ in place of T \ E_τ. In the processed-in-both case, F_τ ⊆ T′ \ E′_τ. In the absorbed case,
  P′(τ⁺) is closed under the rules of T′ \ E′_τ ⊇ F_τ. □
- Corollary: Π_R can fail to rise between two visits only at a relevant new steal. Such a steal means that some
  vertices of a tangle t that fired in τ's region before now lie in an EARLIER region (higher top), while t is not inside
  the prefix: t is split.
DATA (corpus plus fall3_n76, fall4_n116, fallv_viol_n28, f1_twofall_n48, f1_twodef_n48; RM_EXCL=1; consecutive visits of
every context; Oink / stable):

| visit pairs | Oink | stable |
|---|---|---|
| relevant new steal, with a descent | 122 | 121 |
| relevant new steal, no descent | 5 | 5 |
| no relevant new steal, no descent | 8,125 | 7,906 |
| no relevant new steal, with a descent | 0 | 0 |

- Compare plain new steals without a descent: 665 / 630. The relevant ones are the right charge: F_R ≈ #relevant new
  steals.
- Relevant new steals per context per phase: at most 4 (fall4_n116), then 3 (f1_twodef_n48, fall3_n76), and 2
  (fallv_viol_n28, f1_twofall_n48).
(FALL) ⇐ (RELSTEAL): relevant new steals per context are polynomial per phase.
- A relevant steal moves a vertex to an earlier region. Without descents prefixes only grow, so per round each vertex
  can move earlier at most n times.
- But a descent can move many vertices later again, which re-enables steals. So the count is #descents·n² circularly.
  This is the remaining core of (FALL).

22t. Packet 7 (REFEREE R-P7 @ 299bc58; REFEREE-2 pending), imported per referee; §22r unchanged (15:17Z by date -u)
- EXACT: SIGN WITH GAPS, both closed.
  - G7-a1: the rejection is at 138-139 ("not contained in Z+R"); 137 is the "already attracted" skip.
  - G7-a2: the "remaining instances" step, written out.
    - A p-vertex's trigger edge goes into Z_τ and is tried at that pop.
    - An opponent vertex with ≥ 1 successor in Z_τ is tried at the pop of the last one; its successors in P(τ⁺) are not
      escapes (80).
    - A tangle with ≥ 1 escape in Z_τ is tried at the pop of its last escape in Z_τ; escapes in P(τ⁺) pass (156 tests
      Gx = CurR).
    - A tangle with all escapes in P(τ⁺) or outside R is the closedness case.
  - REFEREE's probe (own closure): EXACT at 233,399 stable / 244,057 Oink region steps, 0 failures.
- PREFIX-MONO-X: SIGN. Wording: "PREFIX-MONO is the special case" should read "the same induction proves PREFIX-MONO with
  T′ in place of T′ \ E′_τ". A step-ideal run's prefixes are closed under all of T′. It is the same proof pattern, not a
  special case of the hypothesis.
- Corollary: SIGN WITH GAPS.
  - G7-c1 (closed): Π-blind e* steps also need a new steal. POS-FALL uses step-ideality only through (C4), which holds
    under (NS).
  - G7-c2 (stated): the bound is ONE-SIDED and loose. New steals outnumber falls about 8-13 to 1.
- Reduction (REFEREE): GAP-A ⇐ (CTX⁺) ∧ (NS-COUNT), given STR-DET. (NS-COUNT) says new-steal visit pairs per context are
  polynomial. (NS-COUNT) ⇒ (FALL), not conversely.
- §22s (PREFIX-MONO-X*, "relevant" steals) tightens the charge to (RELSTEAL), with 5 / 5 relevant steals without a
  descent. It is for packet 8.
Per-(context, round, top, tangle) counting (REFEREE's suggestion; DATA, 15:17Z; corpus plus fall3, fall4, fallv, f1_two*;
RM_EXCL=1):
- (STEAL-ONCE): every (context, round, top, tangle) is newly stolen at most once per phase. 91 phases with new steals and
  23 with relevant steals, in both orders, all with max 1.
- So the same tangle can be stolen repeatedly only at DIFFERENT steps. In fallv_viol_n28 tangle 2 is stolen at both
  falls, at different (round, top).
- Consequence: #new-steal visits per context ≤ (n + 1)·n·|T_phase|, but |T_phase| ≤ n·S (Lemma W), which is circular.
  (STEAL-ONCE) would need a bound on the tangles that can be stolen at a context independent of S.

22u. (FALL) ⇐ (STEAL-ONCE) ∧ (FIRED-R): two data statements, no S in them (15:23Z by date -u)
Chain (proved parts are readings):
- F_R ≤ #relevant-steal visits at R (§22s, PREFIX-MONO-X*).
- A relevant steal at a visit pair is a (round, top, tangle) with the tangle in F_τ, newly met by the later prefix.
- (STEAL-ONCE, DATA): each (context, round, top, tangle) is newly stolen at most once per phase.
- (FIRED-R, DATA): the distinct tangles that ever FIRE in region steps at context R during a phase number at most
  poly(|R|).
  - Corpus plus fall3_n76, fall4_n116 and fallv_viol_n28, Oink order: at most 17 per context, and at most 0.5·|R|.
    The maximum is climbs_1016/a_best_s31.
  - Cross unions s11 (600 games plus corpus; RM_EXCL=1, RM_LIGHT=1; 15:31Z), Oink / stable:
    - (FIRED-R): at most 13 per context, at most 0.5·|R|.
    - (STEAL-ONCE): max 1 in all 325 / 338 phases with new steals and all 63 / 74 with relevant steals.
    - PREFIX-MONO-X*: descents with a relevant steal 180 / 234; relevant steals without a descent 17 / 23; descents
      without a relevant steal 0 / 0. Plain new steals without a descent: 2,554 / 2,625.
- Then F_R ≤ (n + 1)·n·poly(|R|), and (FALL) holds. The circularity of §22t is gone, because (FIRED-R) counts only the
  tangles active at R, not |T_phase|.
- So GAP-A ⇐ (CTX⁺) ∧ (STEAL-ONCE) ∧ (FIRED-R), given STR-DET. All three are DATA only.
- A proof of (FIRED-R) needs a structure on the tangles that fire at a fixed context: each adds at least one new vertex
  to a region of R in some visit. I have no argument that their number is not ~ the number of searches.

22v. Toward (STEAL-ONCE): what a second steal needs (reading, SKETCH; 15:34Z by date -u)
- Suppose (R, r, τ, t) is newly stolen at visit pairs (s₁ → s₂) and later (s₃ → s₄), with s₂ ≤ s₃.
  - At s₂, P(τ⁺) of round r meets t without containing it.
  - At s₃, t is again not excluded: either P(τ⁺) no longer meets t, or it contains t.
  - Either way, between s₂ and s₄ some vertex of t leaves P(τ⁺) of round r, i.e. moves to a region whose top has index
    below τ, or out of the round's union.
- By PREFIX-MONO-X* (§22s), a prefix can shrink between two visits only if that transition has a relevant steal at some
  step that precedes (r, τ) in the step order (rounds ascending, tops descending), or a change of V in an earlier round
  (an RV change, itself charged to such a steal).
- Induction over the steps in that order gives only steals(step) ≤ 1 + Σ_{earlier steps} steals. That is exponential
  in the number of steps, so it does not explain the data's "max 1" (§22t, §22u: 0 exceptions in 416 / 429 phases with
  steals).
- The regularity the data shows is stronger: a prefix that has grown into a tangle never retreats from it far enough to
  re-steal it at the same step.
- A proof would need to show that the shrinks caused by earlier relevant steals never uncover the same tangle at the same
  later step. Not found.

22w. Packet 8 (REFEREE R-P8 @ fe4be51; REFEREE-2 pending), imported per referee; §22s and §22u unchanged (15:53Z by date -u)
- EXACT*: SIGN (a corollary of EXACT; no new assumption). PREFIX-MONO-X*: SIGN.
- Corollary: SIGN WITH GAPS, G8-1. Counted over consecutive visit pairs it needs the factor 3: F_R ≤ 3·N*_R, where N*_R
  is the number of relevant-steal visit pairs at R. §22s's "F_R ≈ #relevant steals" and §22u's first line omit it.
- §22u chain: VALID as a conditional. F_R ≤ 3(|R| + 1)|R|·#fired(R) given (STEAL-ONCE). So GAP-A ⇐ (CTX⁺) ∧ (STEAL-ONCE)
  ∧ (FIRED-R), given STR-DET. Both premises are DATA. (FIRED-R) is the real obstruction and has no argument yet.
- Wording correction to §22u: "at most 0.5·|R|" holds on L-ALG's data only. REFEREE's probe finds (FIRED-R) up to 14
  tangles per context and a ratio up to 0.62·|R| (Oink order) on small contexts. Read §22u's figure as "at most 14, and
  at most 0.62·|R|, on all data so far".
- R9 constants (post-landing note): per context 2(F_R + 1)(H + 1), per input ≤ 2n. Marked in the §22e and §22j displays.
Mixed-union data for §22u (UNIONS = 900, SEED = 1, plus corpus; RM_EXCL=1, RM_LIGHT=1; Oink / stable):
- (FIRED-R): at most 13 per context, ratio at most 0.5 / 0.47.
- (STEAL-ONCE): max 1 in all 665 / 703 phases with new steals and all 124 / 150 with relevant steals.
- PREFIX-MONO-X*: descents with a relevant steal 314 / 522; relevant steals without a descent 33 / 22; descents without a
  relevant steal 0 / 0.
(FIRED-R) climb and a caveat (16:08Z by date -u; experiments/alg/dtl_firedclimb.py, from climbs_1016/a_best_s31.pg).
- Oink order: 12 tangles at one context with |R| = 16 (0.75); continued to 13 (0.87). Stable order: 15 tangles with
  |R| = 17 (0.88).
- Pinned Oink solves the stable-order instance (n = 20) with 2 dominions and 14 tangles in 3 iterations, verified. The
  stable-order counts come from dtl_pyref under that order datum, so Oink's own run differs.
- CAVEAT. Every tangle that fires at R is a stored tangle, and Lemma W gives #tangles ≤ n·S, so #fired(R) ≤ n·S
  trivially. On short phases the data cannot distinguish (FIRED-R) from this bound. (FIRED-R) also FOLLOWS from GAP-A.
  So (FIRED-R) is a context-local form of GAP-A's tangle count, not an independently weaker statement.
  [Correction 16:11Z: "follows from GAP-A" is true of EVERY premise of the form "X is polynomial" with X ≤ poly(S),
  (CTX⁺) included, so that part is not specific. The specific point is that (FIRED-R) bounds tangles, and the tangle
  count is GAP-A's own core (Lemma W). (FIRED-R) is therefore unlikely to be much easier than GAP-A, unlike (STEAL-ONCE),
  which is a statement about repetition.]
- Its content is that the tangles active at one context do not grow with the phase length. Testing it needs LONG phases
  (S ≫ |R|), e.g. the spp/h4 families. There (corpus, unions) the maximum is ≤ 14 per context and ≤ 0.62·|R|. Climbs
  from long-phase starts: not run.
- The ratio to |R| climbs toward 1 on short phases. A count above |R| would at least show that no "≤ |R|" form holds.
- Final (16:19Z): experiments/alg/instances/fired18_stable_n20.pg has 18 tangles firing at one context with |R| = 18,
  ratio 1.00, in stable order. 30,000 more climb steps did not pass |R|. Pinned Oink solves it with 1 dominion and 16
  tangles in 4 iterations, verified. A long-phase climb from h4_def11_oink_n28 (Oink order) is running.

22x. Box 7 ledger (L-ALG successor 6, produced on Opus 5.5; Lead GO 10:47Z, box to ~18:50Z; 16:15Z by date -u)
SIGNED by both referees this box. All are readings of dtl.cpp @ 8fbf0a7, for every order datum.
- (S0), PREFIX-MONO, POS-FALL and ROOT-BOUND (packet 4).
- Lemma STR-DET (packet 5). It closes G-STR, so FDL and R5 (h) hold without condition.
- §22j per-input budget, folding Dom first differences into (CTX⁺), and §22f with F_R = every non-rise (packet 6).
- EXACT and PREFIX-MONO-X (packet 7; REFEREE signed, REFEREE-2 pending). EXACT* and PREFIX-MONO-X* (packet 8; REFEREE
  signed, REFEREE-2 pending).
REDUCTION (referee-signed as a conditional):
- GAP-A ⇐ (CTX⁺) ∧ (FALL) ⇐ (CTX⁺) ∧ (NS-COUNT) ⇐ (CTX⁺) ∧ (STEAL-ONCE) ∧ (FIRED-R), given STR-DET.
- Per phase: S − 1 ≤ Σ_{R ∈ C_bv} 2(F_R + 1)(H + 1) + 2n(|C_T| + |C_Dom|) + 1, with F_R ≤ 3·N*_R ≤ 3(|R| + 1)|R|·#fired(R)
  under (STEAL-ONCE).
OPEN, all DATA only:
- (CTX⁺): distinct first-difference inputs (best_vertices contexts, −1 attractors, Dom steps) per phase are polynomial.
  - Max 12 per phase so far: ctx12_oink_n40 (mine, Oink order) and ctx12_n40 (L-RED, both orders). No superlinear trend.
- (STEAL-ONCE): each (context, round, top, tangle) is newly stolen at most once per phase. 0 exceptions on the corpus,
  the special instances, and the mixed and cross unions (§22t-§22w).
- (FIRED-R): the tangles that fire at one context in a phase number poly(|R|).
  - Up to 18 at |R| = 18 on short climbed phases, and ≤ 14, ≤ 0.62·|R| on long-phase data.
  - It bounds tangles, so it is close to GAP-A's own core (§22w caveat).
DEAD this box, with instances (DEAD.md):
- Root-call RMONO = (M) (dtl_mviol_n20, pinned Oink re-run).
- (CHAIN) (dtl_searches15_n24; nest_nest_s43).
- (CTX-ROOT) (dtl_cnew14_n20).
- "F_R ≤ 2" (L-RED fall3_n76), then "F_R constant" (fall4_n116: 4, linear in parts).
- (FALL-V), per vertex (L-RED fallv_viol_n28).
- Per-tangle steal counting (fallv_viol_n28: tangle 2 is stolen at both falls).
- The raw per-input bound (vacuous), and distraction mass as a potential.
GAP-C this box: DE13 (kin_viol_n29) and DE15 (meet_viol_n17) recorded (§18r). The KT-chain S step, K-in, TW, K-low and
MEET are dead, and (PHASE-IN) ⇔ run completeness. Packet 3: K5'' and (α) with Dep(Str) signed (§18q).
Tools: experiments/alg/dtl_rootmono.py (env RM_DV, RM_LIGHT, RM_EXCL, RM_KSEQ, RM_WIT, RM_FALLDET, RM_ROUNDS),
dtl_union_dump.py, dtl_ctxclimb.py, dtl_firedclimb.py, dtl_meetd.py. dtl_fdlcheck.py logs R and Gx.
Next, for whoever continues:
- (a) (STEAL-ONCE) is the most structural statement left. A second steal of (r, τ, t) needs a prefix to retreat from t
  (§22v). Show that the retreats caused by earlier relevant steals never uncover the same tangle at the same step.
- (b) (FIRED-R) on LONG phases, by climbing from spp/h4 starts.
- (c) (CTX⁺) needs a potential that pays for the rebuilt distraction runs after a level-set jump (§22p).
Ledger addendum (16:36Z by date -u):
- The long-phase (FIRED-R) climb from h4_def11_oink_n28 (Oink order) did NOT stay long. Its best instance has a phase of
  5 searches (the start had 12): 18 tangles fire at one context with |R| = 22, out of 26 tangles in the whole run.
  Pinned Oink found 3 dominions and 26 tangles in 7 iterations, verified.
- So item (b) of "Next" is still open. A long-phase test needs a fitness that keeps S large. It is not saved as an
  instance.
- (CTX⁺) climbs: 12 first-difference contexts, reached from spp22 (stable) and from spp25 (Oink). The best instance is
  saved as ctx12_oink_n40.

## 23. Box 8 (L-ALG successor 6, Lead GO 16:43Z by date -u, box to ~00:45Z; produced on Opus 5.5)
Ledger correction (16:44Z, Lead 16:43Z): REFEREE-2 has also signed packets 7 and 8 (EXACT, PREFIX-MONO-X, EXACT*,
PREFIX-MONO-X*), in full agreement after the comparisons. R10 has landed, and R9's original constants hold given STR-DET.
Targets: (1) prove (STEAL-ONCE*); (2) (FIRED-R) on long phases; (3) (CTX⁺), only if (1) or (2) moves.

23a. Toward (STEAL-ONCE*): the invariant is (STAYS-MET) (DATA; 16:50Z by date -u; dtl_rootmono.py RM_EXCL=1 RM_PREF=1)
- A second relevant steal of (context, step σ, tangle t) needs t to FIRE again at σ. That needs every later prefix
  P(σ⁺) to be disjoint from t, i.e. the prefix must retreat from t entirely.
- DATA (corpus plus fall3_n76, fall4_n116, fallv_viol_n28, f1_two*; Oink / stable): after each of the 216 / 214 relevant
  steals, t NEVER fires again at σ, and every later visit's prefix at σ still MEETS t.
- So the observed invariant is (STAYS-MET): once a fired tangle is split at a step, it stays split for the rest of the
  phase. (STAYS-MET) ⇒ (STEAL-ONCE*).
- Prefixes do shrink. Between consecutive visits some step's prefix loses a vertex in 119 of 8,252 pairs (Oink order),
  all at relevant-steal pairs, as PREFIX-MONO-X* says. But no shrink ever removes ALL vertices of a previously stolen
  tangle.
Partial proof (reading).
- In round 1 the input V₁ (all p-priority vertices of R) is fixed. The first region is Cl({τ₁}; T), with no exclusions
  since its prefix is empty, so it is monotone in T. Hence the prefix at the second step of round 1 only grows, and
  (STAYS-MET) holds there.
- From the third step on, the second region is Cl(P ∪ {τ₂}; T \ E), where E grows with P. A stolen tangle at the third
  step may be met only through vertices of the second region. If one of the second region's fired tangles is later
  stolen, those vertices can leave. So the induction does not go through as stated.
- What is needed: when a region loses vertices through a relevant steal of its own fired tangle t′, it never loses every
  vertex through which an earlier-stolen tangle t is met at a later step. Not proved.
Sharper invariants (17:08Z by date -u; same data, Oink order):
- (MET-MONO) "a tangle met by a step's prefix stays met" is FALSE in general. 117 of the 119 visit pairs with a prefix
  shrink lose some met tangle.
- (STOLEN-PERM) holds in 216 / 216: after a relevant steal the STEALING vertices t ∩ P(σ⁺) stay in every later prefix at σ.
  It implies (STAYS-MET).
- (STEALER-MONO) holds in 216 / 216: the region that holds the stolen vertices never loses any vertex afterwards.
- Reading. By EXACT* and PREFIX-MONO-X*, region j can shrink only after a relevant steal at some step ≤ j. So the data
  says: once region j has stolen from a later step, no relevant steal happens at steps ≤ j again in the phase. That
  would be an ORDER on steals (each region steals only after the regions above it have stopped changing).
- Not proved. The obvious attack shape: after region 2 has stolen from region 3, let region 1 (monotone in round 1)
  grow into a tangle that fired in region 2. Target for L-RED.
- Union runs with all these checks are running.
Union data (17:28Z by date -u; RM_PREF=1 RM_EXCL=1 RM_LIGHT=1; corpus included). Relevant steals followed through the rest
of the phase. NO-REFIRE, STOLEN-PERM and STEALER-MONO each hold in every case:

| set | Oink | stable |
|---|---|---|
| cross unions s11 (600, UM_CROSS = 3) | 377 / 377 | 456 / 456 |
| mixed unions s1 (900) | 644 / 644 | 849 / 849 |

With the corpus and specials (216 / 214), that is 0 exceptions in 1,237 (Oink) / 1,519 (stable) relevant steals.

23b. (STEALER-MONO) KILLED on stealer_viol_n76; (STAYS-MET), (STEAL-ONCE*), (STOLEN-PERM) survive there (L-ALG succ. 7, 17:47Z by date -u)
- Instance: experiments/red/carry/instances/stealer_viol_n76.pg (L-RED, l-red 549f8de; n = 76, sha1 714ecc0f). Pinned Oink
  (`oink --dtl --no-single --no-wcwc --no-loops -v` @ 8fbf0a7): solved in 7 iterations, "solution verified (33 strategies)".
- Re-run (DATA), dtl_rootmono.py unmodified (l-alg e2f7e198 code), RM_EXCL=1 RM_PREF=1 RM_DV=0, with and without RM_LIGHT=1
  (identical counts; RM_LIGHT changes only the closure check `cl` and the deficit flags, not pref/regset/excl/fired):
  | order | STEALER-MONO | STOLEN-PERM | NO-REFIRE, stays met | relevant steals per triple |
  |---|---|---|---|---|
  | stable | FAILS 3, holds 14 | holds 17 | 17 / 17 | max 1 |
  | oink | holds 1 | holds 1 | 1 / 1 | max 1 |
  L-RED's numbers confirmed. No INCOMPLETE; no incorrect run.
- New tool experiments/alg/dtl_stealtrace.py (same model; RM_EXCL=1 RM_PREF=1; "STAYS-MET" there is the strict form: t meets
  every later prefix at σ, not merely "not met-but-not-contained"). Stable: STAYS-MET holds 17/17, NO-REFIRE 17/17, STEAL-ONCE*
  max 1 on all 5 contexts with relevant steals, STEALER-MONO FAILS 3/17. Oink: all hold (1 steal).
- (a) So (STAYS-MET) and (STEAL-ONCE*) survive on this instance in both orders. Only the route statement died.
- (b) Failing shape (stable order, phase 1, three depth-0 contexts |R| = 76, 75, 74, identical shape; vertex labels as in the
  file):
  - Visit 2, round 5: top 18 (pr 39) fires tangle 8 = {3, 7, 15}.
  - Visit 3: region (round 5, top 31) (pr 65) fires tangle 7 = {34} and contains 3. So tangle 8 is relevantly stolen at step
    (5, 18) with W = {3}.
  - Visit 4: a new top 68 (pr 89, above every old top) fires tangle 7 and absorbs 34 and 38. Region 35 (pr 65, processed
    before 31) now also takes 30 and 40 through 34. Region 31 shrinks from {3, 30, 31, 34, 38, 40} to {3, 31}.
  - The relevant steal at visit pair 3→4 is tangle 12 = {51, 55, 63} at steps (4, 66) and (5, 66), stolen by region 68. It is
    not one of region 31's own fired tangles.
  - Every lost vertex moved UP, into regions processed before 31. Region 31's own fired tangle 7 was CAPTURED whole by a
    higher region; that is not a steal. So the prefix at step (5, 18) keeps 3, 30, 34, 38 and 40, and W = {3} stays
    (STOLEN-PERM).
- Obstruction: a region can lose vertices by UPWARD MIGRATION. A new or grown higher region captures the region's fired tangle
  whole and takes its dependents. Nothing is stolen from the region, and the prefix of every step below it does not lose those
  vertices. (STEALER-MONO) is a statement about a single region and was the wrong unit; the prefix (a union) is the right one.
  The §23a "ORDER on steals" reading is also false here: a relevant steal at step (·, 66), above region 31, follows region 31's
  steal from step 18.
- (c) KILLED: (STEALER-MONO) as a statement about A_DTL (L22/L26: every order datum). Recorded in docs/alg/DEAD.md.
- §23a's counts: its 1,519 stable steals were taken with RM_PREF=1 RM_EXCL=1 RM_LIGHT=1 (unions: UNIONS/SEED/UM_CROSS, NMAX = 32)
  and DTL_ORDER=stable, so the counters are the same. The kill is in stable order, on an instance outside those sets: n = 76 is
  above the unions' NMAX, and the instance is new.
- What survives: (STOLEN-PERM) ⇒ (STAYS-MET) ⇒ (NO-REFIRE at σ) ⇒ (STEAL-ONCE*). Each arrow is PROVED (reading) as in §23a: a
  relevant steal needs t ∈ F_τ at the earlier visit, and firing at σ needs t disjoint from P(σ⁺).
- New candidate route (SKETCH, not proved). Call w ∈ P(σ) DEPENDENT on a fired tangle t′ at step σ′ > σ if w entered region σ′
  through t′, or through a vertex dependent on t′. Then by EXACT* and PREFIX-MONO-X*, w leaves P(σ) only after a relevant steal
  of a tangle it depends on. Upward capture keeps w inside P(σ). So (STOLEN-PERM) needs: the stealing vertices of a steal never
  depend on a fired tangle that is later relevantly stolen.

23c. Shrink-vertex analysis and (DEP-SAFE) (DATA; L-ALG succ. 7, 18:34Z by date -u; experiments/alg/dtl_shrinkdep.py @ l-alg b45bd87)
- Tool. Model and visits are those of dtl_rootmono.RM with RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0. It adds an ATTRACTION FOREST
  per best_vertices region step: each attracted vertex gets one parent, either ('v', popped vertex) or ('t', fired tangle,
  popped trigger). path(w) is the set of fired tangles on w's chain to the region top.
- Data sets:
  - corpus: 254 committed .pg under experiments/ with n < 80, plus stealer_viol_n76;
  - cross unions: UNIONS=600 SEED=11 UM_CROSS=3 NMAX=32, corpus included.
  - Both order data. No INCOMPLETE.
- Results (Oink / stable):

  | set | (DEP-SAFE) holds | lost vertices A / B / C |
  |---|---|---|
  | corpus | 154/154 / 169/169 | 815 / 388 / 816 and 1,219 / 477 / 973 |
  | cross unions s11 | 399/399 / 447/447 | 2,688 / 1,045 / 1,697 and 3,689 / 1,028 / 2,209 |

  - A: a tangle on path_x(w) is relevantly stolen at its own step.
  - B: w's region top is no longer a region top.
  - C: other.
  - A' (a path tangle plainly stolen, not fired) never occurs.
- Reading of C, checked on two cases (scratch script; round 5 in both):
  - stealer_viol_n76 (stable), |R| 75, visits 2→3, region top 14: path tangle 22 = {22, 24} with escapes {0, 4, 6, 14, 15, 16}.
    Escape 16 is in P_x and not in P_y, and is not in the region, so tangle 22 cannot fire at y.
  - climbs_1016/b_best_s33 (Oink), |R| 20, visits 1→2, region top 19: tangle 6 = {6}, escape 5, in P_x and not in P_y.
  - So the cause is an ESCAPE. A tangle escape (or, by the same rule, an opponent successor) that lay in the prefix above at
    x is back in Gx = CurR at y (dtl_pyref attractTangle lines 95-97, attractVertices line 74). The cause is thus another,
    higher loss. Only these two C cases were checked; the rest are unclassified. The single-parent forest cannot
  see this, so roughly 40% of losses (C) are cascades through escapes.
- (DEP-SAFE) "no path tangle of a stealing vertex is relevantly stolen later" holds on 1,169 relevant steals (DATA). The
  forest misses the escape cascades, though, so (DEP-SAFE) does not by itself imply (STOLEN-PERM).
  The route needs an escape-aware dependency:
  - w depends on every fired tangle on its chain, and on every prefix vertex that hides an escape of a tangle or of an
    opponent vertex on its chain.
  - Then: "a stealing vertex never depends on a later-stolen tangle or on a later-lost escape holder". SKETCH, not measured.
- Status: (STOLEN-PERM), (STAYS-MET) and (STEAL-ONCE*) remain DATA. No proof. No kill.

23d. (FIRED-R) on LONG phases (DATA; L-ALG succ. 7, 18:47Z by date -u; experiments/alg/dtl_firedlong2.py)
- Filter: L-RED's, from experiments/red/root/firedlong.py (l-red 2486288). A context counts in a phase of S searches if it is
  visited ≥ 2 times and S ≥ 2|R|. Same model and fired sets as dtl_rootmono.RM with RM_EXCL=1 RM_LIGHT=1 RM_DV=0.
- Data sets:
  - corpus: as in §23c, plus fall3_n76 and fall4_n116 (l-red);
  - mixed unions: UNIONS=900 SEED=1 NMAX=32, corpus included.
  - Both order data. No INCOMPLETE.
- Results:

  | set | order | counted contexts | max fired/\|R\| | max fired | max per step | NO-RETURN |
  |---|---|---|---|---|---|---|
  | corpus | Oink | 327 | 0.333 (3 at \|R\| 9, spp_n20) | 3 | 3 | holds 327 |
  | corpus | stable | 316 | 0.25 | 2 | ≤ 2 (1 in the 25 printed rows) | holds 316 |
  | mixed | Oink | 2,088 | 0.375 (3 at \|R\| 8, union758) | 3 | 3 | holds 2,088 |
  | mixed | stable | 2,132 | 0.25 | 2 | ≤ 2 (1 in the 25 printed rows) | holds 2,132 |

  - NO-RETURN: a tangle that fired at a step (round, top) and then did not fire there at a later visit where the step
    exists never fires there again in the phase.
- Birth of the fired tangles in these long-phase contexts. The birth arena is the sptl arena R′ of the extraction.

  | set (Oink / stable) | born in this phase, R′ ⊆ R | R′ ⊋ R | R′ incomparable with R | born before the phase |
  |---|---|---|---|---|
  | corpus | 13 / 7 | 2 / 0 | 12 / 7 | 0 / 0 |
  | mixed | 26 / 17 | 3 / 3 | 61 / 46 | 17 / 8 |

  Most fired tangles are learned in OTHER branches of the recursion (incomparable arenas), so a count of the tangles learned
  inside R does not bound #fired(R).
- Reading. Long phases (S ≥ 2|R|) exist only for small contexts here (|R| ≤ 9, S ≤ 25). There the fired count stays ≤ 3,
  well below L-RED's best long-phase ratio of 0.40. This is weak evidence that the fired set does not grow with phase length,
  but the filter selects contexts too small to test growth.
- Candidate sharp statement (DATA, being measured on all contexts): (FIRED-STEP) the number of distinct tangles that fire at
  one step (context, round, top) in a phase is bounded by a constant c. With the (|R| + 1)·|R| steps per context (R11 (d)) it
  gives (FIRED-R) with #fired(R) ≤ c(|R| + 1)|R|. It has the same per-step shape as (STEAL-ONCE*). With NO-RETURN, each
  (step, tangle) fires on ONE interval of visits. So (FIRED-STEP) asks how many times a step can switch to a NEW tangle.
- CORRECTION (19:56Z by date -u): NO-RETURN is FALSE in its all-steps form (§23h; stealonce_viol_n76, stable order, 7 of 42
  contexts). Its long-phase form is UNTESTED there: under the filter, 3 contexts qualify and nothing fires in them. The
  long-phase table above is DATA on the listed sets only; nothing in this section depends on NO-RETURN. (FIRED-STEP) itself
  is dead (§23e).

23e. (FIRED-R) on ALL contexts: three candidate structures KILLED, two DATA statements survive (L-ALG succ. 7, 19:16Z by date -u)
- Tool: dtl_firedlong2.py with FL_ALL=1 FL_SHOW=1, i.e. every context visited ≥ 2 times in a phase, with no long-phase filter.
  Model and data sets as in §23d, plus fired10_n20 (l-red). Both order data. No INCOMPLETE.

  | set | order | contexts | max fired | max fired/\|R\| | max distinct fired at one step | NO-RETURN | fired vertex sets distinct | laminar |
  |---|---|---|---|---|---|---|---|---|
  | corpus | Oink | 2,391 | 17 | 0.833 | 12 (fired18_stable_n20, \|R\| 18, S 3) | holds | yes, all | FAILS 56 |
  | corpus | stable | 2,359 | 18 | 1.0 (fired18_stable_n20) | 11 | holds | yes, all | FAILS 61 |
  | mixed | Oink | 13,519 | 20 (union322, \|R\| 48) | 0.833 | 12 | holds | yes, all | FAILS 480 |
  | mixed | stable | 13,755 | 23 | 1.0 (union825, union299, union616, union248) | 11 | holds | yes, all | FAILS 470 |

- KILLED (self-kills, each a candidate of this box; docs/alg/DEAD.md):
  - (FIRED-STEP) with a constant c: "at most c distinct tangles fire at one step (context, round, top) per phase". Killed by
    experiments/alg/instances/fired18_stable_n20.pg (l-alg 9ffee93; sha1 42307b22; pinned Oink 4 iterations, verified): 12
    distinct tangles fire at one step of a context with |R| = 18, in a phase of only 3 searches (Oink order). A single region
    step fires many tangles, so the per-step count is of order |R|, not constant.
  - (FIRED-LAMINAR): "the fired tangles of a context in a phase are pairwise nested or disjoint". Had it held, it would have
    given #fired(R) ≤ 2|R| − 1. Killed by experiments/alg/instances/c6_replay3_n32.pg (sha1 ac987535; pinned Oink 11
    iterations, verified; both orders): tangles {4, 7, 13, 17, 21, 25} and {8, 17, 21} cross, at contexts with |R| 32, 31, 29
    and 26. Contrast: ALL tangles born in a phase are not laminar either (tc+ 4, tc+ 6, spp_final_n20; scratch check).
  - (FIRED-TOP-INJ): "the fired tangles of a context have distinct top vertices". Killed by fired18_stable_n20 (stable, 2
    contexts).
- Survive (DATA, all 32,024 contexts):
  - (FIRED ≤ |R|): #fired(R) ≤ |R| per phase. It is TIGHT: equality 18/18 on fired18_stable_n20 (stable) and on four mixed
    unions.
  - (FIRED-DISTINCT): fired tangles of a context have distinct vertex sets.
  - NO-RETURN on these sets. It is FALSE in general (§23h, stealonce_viol_n76).
- Reading. (FIRED ≤ |R|) is tight and has no injective witness yet: not laminar, and not by the top vertex. Climb target for
  L-RED: fired/|R| > 1 (dtl_firedclimb.py's fitness, or firedlong.py without the filter). No proof route.

23f. (STEAL-ONCE*) KILLED (RESULTS DE20); the R11 count with the factor k; toward (STEAL-POLY) (L-ALG succ. 7, 19:34Z by date -u)
The Lead asked for this in §23e; §23e was already taken (FIRED-R), so it goes here, at the next free letter.
- Instance: experiments/red/carry/instances/stealonce_viol_n76.pg (L-RED R35, l-red 6af3a14; sha1 32c2da0b). It is
  stealer_viol_n76 with edge 3→31 replaced by 3→64 and edge 20→31 added. Pinned Oink: 1 dominion, 50 tangles, 7 iterations,
  "solution verified (33 strategies)" (L-ALG re-run 19:34Z).
- L-ALG re-run, dtl_shrinkdep.py, RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0:
  - stable order: (DEP-SAFE) FAILS 7 / holds 12. Every failure is at step (round 4, top 18), tangle 7, with stealing vertex 3
    and path tangle 9 relevantly stolen at the next pair.
  - Oink order: all hold.
  - So (DEP-SAFE), (STOLEN-PERM), (STAYS-MET), NO-REFIRE and (STEAL-ONCE*) are all FALSE as statements about A_DTL (L22/L26).
  - The mechanism is §23c's case A one level up, as the Lead reads R35. Vertex 3 enters region 66 through the path tangle;
    a new top 68 steals that tangle; 3 drops out of P(18⁺); tangle 7 refires at (4, 18); region 66 later fires a new
    tangle, holds 3 again, and steals tangle 7 a second time.
- (1) The R11 (d) count with the factor k. Lead reading checked: CORRECT, and stated precisely here.
  - Fix a context R and a phase. A quadruple is q = (R, round r, top τ, tangle t). Let k_q be the number of consecutive
    visit pairs of R at which q is a relevant steal, and k_R = max_q k_q.
  - N*_R ≤ Σ_q k_q, since every pair counted in N*_R has at least one relevant steal.
  - Only q with t ∈ F_τ at some visit count. So t is among the #fired(R) tangles, r ≤ |R| + 1 (dtl.cpp 748-760), and τ is a
    p-vertex of R, so at most |R| tops.
  - Hence F_R ≤ 3·N*_R ≤ 3·Σ_q k_q ≤ 3·k_R·(|R| + 1)·|R|·#fired(R). This is R11 (c) with G8-1's factor 3. The factor tightens
    to 2 given STR-DET (REFEREE-2 R2-P8 §7; one signature, not used).
  - So GAP-A ⇐ (CTX⁺) ∧ (STEAL-POLY) ∧ (FIRED-R), given STR-DET, where (STEAL-POLY) says k_R ≤ poly(|R|). The sum form,
    Σ_q k_q ≤ poly(|R|)·#fired(R), is weaker and also suffices.
  - Status: a reading of the signed R11 (c) chain with k replacing 1. Unrefereed.
- (2) Toward a bound on k (SKETCH, with the gap named):
  - A second relevant steal of q needs t ∈ F_τ again, i.e. t refires at (r, τ). That needs t ∩ P(τ⁺) = ∅. So between the two
    steals, every stealing vertex leaves P(τ⁺).
  - By PREFIX-MONO-X*, a vertex leaves P(τ⁺) only at a transition with a relevant steal at an EARLIER step: an earlier round,
    or the same round at a higher top.
  - The intervals between consecutive steals of q are disjoint, so the re-steals of q charge injectively to relevant-steal
    EVENTS at earlier steps: k_q ≤ 1 + #(events at steps before (r, τ)).
  - Gap: one event can be charged by many q, and summing over steps gives E(σ) ≤ #fired(R)·(1 + Σ_{σ′ before σ} E(σ′)),
    which is exponential in the number of steps (the §22v obstruction). A polynomial bound needs one of two things:
    - (a) DEPTH: chains event → re-steal → event have bounded length. On R35 the chain has length 2: the tangle at region
      66 is stolen by new top 68, then tangle 7 is re-stolen at 18.
    - (b) An injective charge: each event at σ′ un-steals at most poly(|R|) quadruples, and those quadruples' re-steals
      need distinct events.
  - Neither is proved. Measuring: k on large unions (n ≤ 120; UNIONS=300, SEED=7/8, UM_CROSS=4, NMAX=60; both orders).
    The chain-length statistic is next.

23g. (STEAL-POLY) ⇐ (STEAL-DEPTH): a charging reduction (reading, unrefereed; L-ALG succ. 7, 19:43Z by date -u; tool dtl_stealdepth.py)
Fix a context R and a phase. Q = number of quadruples q = (R, round, top, fired tangle) ≤ (|R| + 1)·|R|·#fired(R) (§23f).
An EVENT is a relevant steal (pair i → i+1, q). For q = ((r, τ), t), call a later event of q at pair i, with the previous
event of q at pair j < i, a RE-STEAL.
- Lemma CHARGE (reading). Every re-steal e of q at pair i has a CAUSE: an event at a pair m with j < m < i, at a step strictly
  earlier than (r, τ) in the step order (rounds ascending, tops descending). Distinct re-steals of the same q have distinct
  causes.
  Proof.
  - At visit j+1, t meets P_{j+1}(τ) without being contained in it.
  - At visit i, t ∈ F_τ, so t fired inside region τ. A firing tangle lies in CurR = R \ P_i(τ) (dtl_pyref attractTangle
    lines 86-89), so t ∩ P_i(τ) = ∅.
  - So some w ∈ t ∩ P_{j+1}(τ) has left P(τ) at some pair m with j+1 ≤ m ≤ i−1.
  - At that pair P_m(τ) ⊄ P_{m+1}(τ). By PREFIX-MONO-X* in its LOCAL form (see the gaps below) there is a relevant steal at
    a step before (r, τ) at pair m.
  - Consecutive re-steals of q own disjoint pair intervals (j, i), so their causes lie at distinct pairs.
- Depth. depth(e) = 0 for the first event of each q, and for a re-steal depth(e) = 1 + min over its causes of their depth.
  - A chain of causes goes strictly earlier in the step order, so depth ≤ (|R| + 1)|R| − 1 (PROVED, reading, given CHARGE).
  - This alone gives only an exponential bound.
- Counting. Let E_d be the number of depth-d events. Then E_0 ≤ Q. For fixed q, the depth-d re-steals inject into causes of
  depth d − 1 (choose a min-depth cause). Hence E_d ≤ Q·E_{d−1} ≤ Q^{d+1}.
- (STEAL-DEPTH_D): every event has depth ≤ D. Under it, Σ_q k_q ≤ Σ_{d ≤ D} Q^{d+1} ≤ 2·Q^{D+1}. So for constant D:
  (STEAL-DEPTH_D) ⇒ (STEAL-POLY) in the sum form of §23f. With (FIRED-R) this gives F_R ≤ 6·Q^{D+1}.
- Gaps, named:
  - G23g-1, CLOSED (reading, unrefereed): the LOCAL form of PREFIX-MONO-X*. The signed proof (§22r, "by induction over τ in
    decreasing order", three cases) uses (NS) only at the steps τ′ ≥ the current τ of the same round, given V ⊆ V′ for that
    round. So "(NS*) at every step of round r above σ, and V_r ⊆ V′_r" ⇒ P(σ) ⊆ P′(σ). The cases are: τ not processed in
    run 1; τ processed in both runs; τ processed in run 1 only. Each uses the hypothesis at τ alone, plus P(τ⁺) ⊆ P′(τ⁺) from
    the induction.
  - G23g-2, CLOSED (reading, unrefereed) by the §22r Corollary's round alignment: "if (NS) holds at every region step of
    every round (rounds aligned with V_r ⊆ V′_r inductively)". Contrapositive: if V_r ⊄ V′_r, then some region step of an
    earlier round has a relevant steal at that pair. That step is earlier in the step order, so it is a cause. The threshold
    loop has no exclusions (tattr with consume = None, Gx = R), so it adds no case. On cross unions s11 (stable) the tool
    prints "no cause" 0 times.
  - G23g-3: (STEAL-DEPTH_D) with constant D is DATA only. R35 (stealonce_viol_n76, stable order) has one re-steal, depth 1;
    its cause is the depth-0 steal of tangle 9 at (round 4, top 66) at pair 3.
- Status against L32. A named statement, (STEAL-DEPTH_D), with a proof route (CHARGE plus counting) to the (STEAL-POLY) part of
  GAP-A. GAP-A also needs (CTX⁺) and (FIRED-R), so this is not the L32 single-statement criterion.
- DATA for §23f/§23g (19:52Z by date -u). Big unions: corpus + UNIONS=300, SEED=7 / 8, UM_CROSS=4, NMAX=60 (n ≤ 120);
  dtl_rootmono.py RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0. No INCOMPLETE. The first stable runs were OOM-killed (4 × ~6 GB) and
  re-run two at a time.

  | seed | order | phases with relevant steals | k max | STOLEN-PERM | STEALER-MONO |
  |---|---|---|---|---|---|
  | 7 | Oink | 33 | 1 | 215 / 215 | holds 215 |
  | 7 | stable | 38 | 1 | 234 / 234 | holds 234 |
  | 8 | Oink | 48 | 1 | 392 / 392 | FAILS 14, holds 378 |
  | 8 | stable | 55 | 1 | 429 / 429 | FAILS 14, holds 415 |

  - dtl_stealdepth.py, cross unions s11 + corpus + R35 (stable): one re-steal in all, R35's (depth 1); 250 other contexts
    with steals have k = 1; "no cause" 0.
  - So random unions up to n = 120 show no re-steal in either order. R35 is a constructed shape. Note that STEALER-MONO also
    fails in the Oink order (seed 8).

23h. NO-RETURN KILLED with DE20 (L-ALG succ. 7, 19:56Z by date -u; L-RED R35 addendum, l-red d11271d)
- Instance: stealonce_viol_n76 (sha1 32c2da0b; pinned Oink 7 iterations, verified). L-ALG re-run with dtl_firedlong2.py
  (FL_ALL=1 RM_EXCL=1 RM_LIGHT=1 RM_DV=0):
  - stable order: NO-RETURN FAILS 7 / holds 35; at most 4 distinct tangles fire at one step; max fired 14 at one context
    (fired/|R| ≤ 0.333 at every context); FIRED ≤ |R| holds 42/42; FIRED-LAMINAR holds 42/42.
  - Oink order: everything holds (9 contexts).
  - Long-phase filter (stable): 3 contexts qualify, nothing fires in them, so the test is vacuous.
- Reading. This is the same event as the NO-REFIRE failure of §23f: tangle 7 fires at (round 4, top 18), stops firing there
  after the first steal, and fires there again after 3 drops out of the prefix. So the "one firing interval per
  (step, tangle)" form is false wherever STEAL-ONCE* is. The long-phase form stays UNTESTED, not confirmed.
- Dependence: no surviving statement of §23d-§23g uses NO-RETURN.
  - dtl_stealdepth.py, more sets (20:00Z by date -u): mixed unions s1 + corpus + R35, stable: again R35's single re-steal
    (depth 1); 588 other contexts with steals have k = 1. Cross unions s11 + corpus + R35, Oink: k max 1, depth 0 (212
    contexts). "No cause" 0 everywhere.

23i. (CTX⁺): (CTX-LAMINAR) KILLED (self-kill; L-ALG succ. 7, 20:05Z by date -u)
- Candidate: "the distinct first-difference contexts of a phase (all depths) are pairwise nested or disjoint". With it,
  #contexts ≤ 2n − 1 (laminar family), which is the C_bv part of (CTX⁺). It is weaker than (CHAIN) (DE16).
- Test: dtl_rootmono.py with the new flag RM_LAM=1. Default output is unchanged; the flag only adds the CTX-LAMINAR counter.
- KILLED by experiments/alg/instances/ctx12_oink_n40.pg (sha1 eca1246f; pinned Oink 27 iterations, verified; Oink order,
  12 contexts) and by dtl_searches15_n24.pg (sha1 767e14c6; pinned Oink 16 iterations, verified; Oink order, 4 contexts).
  Stable order on the same two files: FAILS 1, holds 3.
  - The crossing pairs are two large depth-0 contexts of the form G′ minus the pieces removed earlier in the search. Each
    lacks vertices the other has: e.g. on dtl_searches15_n24, {0, 1, 2, 5, 7, 9, 10, 13, 14, 15, 17, 20, 21, 23} and
    {0, 1, 2, 5, 6, 7, 8, 9, 13, 15, 17, 20, 23}.
- Reading. The depth-0 contexts of one search form a decreasing chain, R_i = G′ minus the pieces removed before. The
  first-difference context of (s, s+1) lies on chain(s) (FDL: the searches agree before e*). Across searches the chains are
  re-cut, so the contexts cross. This is the same re-cutting that killed (CHAIN). No (CTX⁺) route from set structure alone.

23j. (CTX⁺): context structure data (DATA; L-ALG succ. 7, 20:26Z by date -u)
- dtl_ctxpieces.py (RM_DV=0 RM_LIGHT=1, Oink order) on ctx12_oink_n40, ctx13_n40 (l-red), spp_final_n40 and spp_chain_up_n43.
  - The depth-0 contexts of each search form a decreasing chain from G′ (7/7 phases).
  - All depth-0 contexts over a phase are MANY: 126 at |G′| = 40 with S = 25 (ctx13_n40); 111 at 38 with S = 24.
    First-difference contexts are only 13 and 12 there. So (CTX⁺) is about which contexts carry a first difference, not
    about how many contexts exist.
  - Pieces (differences along a chain) repeat heavily: 585 of 877 were seen earlier in the phase. The maximum number of
    distinct pieces is 84 at |G′| = 43 (spp_chain_up_n43, S = 42), i.e. 1.95·|G′|.
- dtl_rootmono.py RM_BIRTH=1 (new flag; default output unchanged) compares e*'s context with the birth arenas (sptl arena at
  extraction) of the tangles learned by s. On ctx12_oink_n40, ctx13_n40 and spp_chain_up_n43 (Oink order): 91/91 transitions with e* in a
  best_vertices call land in the loose class "the context contains a birth arena at the same or greater depth"; 0 EQUAL a
  birth context.
  - The loose class is nearly automatic for depth-0 contexts, so this is NOT informative. A sharper test would be "e* lies on
    the call path to the birth of s's new tangle".
- No (CTX⁺) statement proposed. Candidate to measure next: (PIECES-POLY), distinct depth-0 pieces per phase ≤ 2|G′|
  (max 1.95 so far).

23k. Referee imports for packet 9 (§23f-§23g) (L-ALG succ. 7, 20:35Z by date -u)
The Lead asked for these as "§23j"; §23j was already taken (CTX⁺ data), so they go here. §23f-§23g are not rewritten.
Sources: REFEREE docs/referee/R-P9.md and REFEREE-2 docs/referee-2/R2-P9.md, on trunk 25111fa; both labelled "(Opus 5.5, D12)".
- Verdicts:
  - (a) §23f: SIGN from both.
  - (b) Lemma CHARGE: SIGN WITH GAPS from both, all gaps closed.
  - (c) the depth count: REFEREE SIGN WITH GAPS (G9-c1, closed); REFEREE-2 SIGN.
  - (d) the data: CONFIRMED by both.
  - No disagreement on the mathematics.
- G9-b1 (both; closed). CHARGE's proof must use the prefix BEFORE τ, P(τ⁺) of round r, wherever §23g writes P_{j+1}(τ) and
  P_i(τ). In §22r's notation P(τ) is the prefix after τ's region. With that reading "t ∩ P_i(τ) = ∅" is FALSE, since t fired
  inside region τ (REFEREE-2's probe: false at all 65 re-steals).
  Corrected step 2: a firing tangle's vertices lie in CurZ or CurR (dtl.cpp 136-139), and CurR = R \ P(τ⁺) minus the
  vertices popped in τ's own region (690, 699). So t ∩ P_i(τ⁺) = ∅.
  Then: take w ∈ t ∩ P_{j+1}(τ⁺) with w ∉ P_i(τ⁺), so i ≥ j + 2. Let m be the LAST visit in [j+1, i−1] with w ∈ P_m(τ⁺).
  Then P_m(τ⁺) ⊄ P_{m+1}(τ⁺).
  The correction is needed for strictness: with P(τ), a loss could be caused at step τ itself.
  The tool was already right: dtl_rootmono.py records pref[(round, top)] = Z BEFORE tattr, i.e. P(τ⁺), and
  dtl_stealdepth.py uses it.
- G9-b2 (REFEREE; closed). An intermediate visit can have fewer than r rounds.
  - "No candidates" stop (dtl.cpp 716 / 765) at round r′ < r: the later rounds repeat round r′, since the call is a function
    of (V, R, T). Use P^{(r′)} as a virtual round r. C3 gives V_r(m) ⊆ V_{r′+1}(m) ⊆ V_{r′}(m+1), unless a steal occurs at a
    round ≤ r′, which is itself a cause.
  - V′ = ∅ stop (768-771): it contradicts w ∈ P_m unless an earlier-round steal exists.
- Citations (REFEREE N9-b1 = REFEREE-2 G9-b2): the tangle rule is dtl.cpp 136-139 (138-139 for "!R[v] return false"), not
  dtl_pyref 86-89.
- G23g-1 and G23g-2: CHECKED and closed by both.
  - The local form needs τ′ ∈ V ⊆ V′ in the absorbed case, which §23g's hypothesis includes.
  - V_r ⊆ V′_r needs (NS*) at ALL steps of rounds 1..r−1, lower tops included (C1 uses the whole union). All of these steps
    are earlier than (r, τ).
  - The threshold loop (722-741) and the survivors (713-772) add no case.
- Forms of (STEAL-POLY) (REFEREE-2 N9-a1, REFEREE G9-c1), named:
  - SUM form, Σ_q k_q ≤ poly(|R|) per phase: F_R ≤ 3·Σ_q k_q directly, so GAP-A ⇐ (CTX⁺) ∧ (STEAL-POLY_sum), with no (FIRED-R).
  - k_R form, k_R ≤ poly(|R|): needs (FIRED-R), since Σ_q k_q ≤ k_R·Q.
  - §23f's "Σ_q k_q ≤ poly(|R|)·#fired(R)" form needs (FIRED-R).
  - (c) gives the sum form from (STEAL-DEPTH_D) only together with (FIRED-R): 2Q^{D+1} contains #fired(R)^{D+1}.
  - Working conclusion of both referees: GAP-A ⇐ (CTX⁺) ∧ (FIRED-R) ∧ (STEAL-DEPTH_D for a constant D), given STR-DET. All
    three premises are DATA.
- Constant D only (both). D = O(log n) gives only a quasi-polynomial bound. The proved D ≤ (|R|+1)|R| − 1 gives
  exp(Θ(n² log n)).
- N9-c1 (REFEREE-2): for Q = 1 there is no re-steal, since a cause is an event of another quadruple. So Σ = 1 ≤ 2, and the
  bound holds for all Q ≥ 1.
- The "R2-P8 §7" citation in §23f is CORRECT: c2ac652, line 139 (REFEREE-2 comparison; Lead checked). REFEREE's N9-a1 read an
  older R2-P8. Unchanged.
- REFEREE-2 data: random equal-priority tie-breaks of stealonce_viol_n76 give the re-steal in 32 of 50 orders (64 re-steals in
  320 runs). Each has a cause and depth 1. So DE20 holds under many order data; the pinned Oink order is among those without it.

23l. (CTX⁺): (PIECES-LAMINAR) KILLED; (PIECES ≤ 2|G′| − 1) is DATA but tracks S (L-ALG succ. 7, 20:42Z by date -u)
- dtl_ctxpieces.py (RM_DV=0 RM_LIGHT=1) on the corpus (Oink; 294 phases) and on the mixed unions s1 (stable; 1,711 phases,
  corpus included).
  - Depth-0 contexts of a search always form a decreasing chain (2,005/2,005 phases).
  - Max distinct pieces per phase: 89 at |G′| = 113 (fall4_n116), and 84 at |G′| = 43 (spp_chain_up_n43), the maximum ratio
    1.953.
  - Reused pieces: 4,172 of 9,143 (corpus) and 20,992 of 48,947 (mixed).
- (PIECES-LAMINAR) "the distinct depth-0 pieces of a phase are pairwise nested or disjoint" (which would give ≤ 2|G′| − 1):
  KILLED (self-kill). Instances: experiments/alg/instances/spp_chain_up_n43.pg and ctx12_oink_n40.pg (Oink order). The
  crossing pair on ctx12_oink_n40 is {0, 2, 4, 5, 6, 9, 10, 11, 12, 14, 16, ...} and {3, 8, 13, 25}.
- (PIECES ≤ 2|G′| − 1) holds on every phase measured, but on spp_chain_up_n43 the 84 distinct pieces come from S = 42
  searches, about 2 new pieces per search. So the piece count follows S, and bounding it is as hard as GAP-A. Not a route.
- (CTX⁺) state: no statement with a route. The data maximum is still 13 first-difference contexts (ctx13_n40).

23m. (FIRED ≤ |R|): self-attack climbs and (FIRED-HALL) KILLED (L-ALG succ. 7, 20:56Z by date -u)
- Climbs with dtl_firedclimb.py:
  - fitness (count, then ratio), 3,000 steps from fired18_stable_n20: stable order reaches 19 fired at |R| = 19 (ratio
    1.0); Oink order reaches 16 at 0.889.
  - FC_RATIO=1 (new: ratio first), 20,000 steps: from the 19/19 instance, no improvement (1.0); from fired10_n20, 0.857.
  - The ratio never exceeds 1.0, and no INCOMPLETE run.
- (FIRED-HALL) "the fired tangles of a context have a system of distinct representatives t ↦ v(t) ∈ t" (it would explain
  FIRED ≤ |R|): KILLED (self-kill). Tested with dtl_firedlong2.py (FL_ALL=1, stable order), a Kuhn matching. Instances:
  experiments/alg/instances/fired18_stable_n20.pg (|R| 18, 18 fired) and the climbed 19/19 instance (scratch, not kept).
  On fired18 the tangles inside {0, 3, 5, 9, 13, 14} are the singletons {0}, {3}, {5}, {9}, {14} plus {0, 9, 13},
  {0, 5, 9, 13, 14} and {0, 3, 5, 9, 13, 14}: 8 tangles on 6 vertices.
- Reading. FIRED ≤ |R| holds there only because other vertices of R carry no tangle. A nested chain plus singletons gives
  2k − 1 tangles on k vertices, so FIRED ≤ |R| has no local reason. The climbs' ceiling at 1.0 is a local optimum, not a
  proof. (FIRED-R) itself, poly(|R|), is unaffected and stays DATA.
- Tool fix: dtl_rootmono's RM_BIRTH bookkeeping (2ff12ff) used the attribute name _spR, which dtl_firedlong2's FL class
  also uses, so it broke FL's birth arenas (TypeError). Renamed to _spRk. Every dtl_firedlong2 result in §23d, §23e and
  §23h was produced before 2ff12ff, with the old code, so none is affected.

23n. Box-8 ledger, successor 7 (22:24Z by date -u; GO 17:46Z; box to ~00:45Z; produced on Opus 5.5)
SIGNED by both referees (packet 9; R-P9 and R2-P9, trunk 25111fa; imports in §23k):
- (a) The R11 count with the factor k: F_R ≤ 3·N*_R ≤ 3·Σ_q k_q ≤ 3·k_R·(|R|+1)·|R|·#fired(R) (§23f).
- (b) Lemma CHARGE, with G9-b1 (P(τ⁺)) and G9-b2 (fewer rounds) closed. G23g-1 (local PREFIX-MONO-X*) and G23g-2 (V
  alignment) are checked (§23g, §23k).
- (c) Depth recursion: E_d ≤ Q^{d+1}, so Σ_q k_q ≤ 2Q^{D+1} under (STEAL-DEPTH_D). This gives STEAL-POLY for constant D only.
- Conditional: GAP-A ⇐ (CTX⁺) ∧ (FIRED-R) ∧ (STEAL-DEPTH_D, constant D), given STR-DET. Also GAP-A ⇐ (CTX⁺) ∧
  (STEAL-POLY_sum).
PROVED (reading, unrefereed):
- STOLEN-PERM ⇒ STAYS-MET ⇒ NO-REFIRE ⇒ STEAL-ONCE* (§23b). All four statements are now FALSE.
KILLED this box (each with its instance, pinned Oink re-run; docs/alg/DEAD.md):
- (STEALER-MONO): stealer_viol_n76 (L-RED; DE19). Also fails in the Oink order on big unions (seed 8).
- (STEAL-ONCE*), (STOLEN-PERM), (STAYS-MET), NO-REFIRE, (DEP-SAFE): stealonce_viol_n76 (L-RED R35; DE20, stable order). In
  the Oink order: stealonce_both_n45 (L-RED R36; DE20 addendum).
- NO-RETURN (all-steps form): stealonce_viol_n76.
- (FIRED-STEP) with a constant, (FIRED-TOP-INJ), (FIRED-HALL): fired18_stable_n20.
- (FIRED-LAMINAR): c6_replay3_n32.
- (CTX-LAMINAR): ctx12_oink_n40, dtl_searches15_n24.
- (PIECES-LAMINAR): spp_chain_up_n43, ctx12_oink_n40.
DATA (unproved; script, flags and sets in each section):
- (STEAL-DEPTH_1): every event has depth ≤ 1, and k ≤ 2.
  - Random sets up to n = 120: no re-steal at all.
  - L-RED's instances, and climbs from them (dtl_depthclimb, 4 runs, ~2 h): up to 12 re-steals, all at depth 1.
- Relevant-steal pairs per context: N*_R ≤ 3 on every set.
- (FIRED ≤ |R|): tight (19/19). It has no local reason (FIRED-HALL is dead), so it is probably not robust.
- (FIRED-DISTINCT): fired tangles of a context have distinct vertex sets.
- (CTX⁺): at most 13 first-difference contexts per phase (unchanged). The depth-0 pieces of a phase number at most
  1.953·|G′|, but that count tracks S.
L32: NOT met. GAP-A still rests on (CTX⁺) and on either (STEAL-POLY_sum) or ((FIRED-R) and (STEAL-DEPTH_D)). (STEAL-DEPTH_D)
has a signed route to (STEAL-POLY); the other premises have none.
Open next:
- (1) depth: a structural reason for depth ≤ 1, or a depth-2 gadget by stacking two R35 levels. That needs a re-steal at
  (r, 66)-type steps. L-RED is climbing.
- (2) (CTX⁺): no route; the set-structure candidates are exhausted (CHAIN, CTX-ROOT, CTX-LAMINAR, PIECES-LAMINAR).
- (3) (FIRED-R): no route.

23o. GAP-A POSITION, in one place (L-ALG succ. 7, 22:30Z by date -u; for the successor; Lead request 22:27Z)
Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (L22/L26). Given STR-DET (R8).
SIGNED CONDITIONALS (both referees; RESULTS R11 and the packet-9 draft R12; §23k):
- (sum form) GAP-A ⇐ (CTX⁺) ∧ (STEAL-POLY_sum), where (STEAL-POLY_sum) says Σ_q k_q ≤ poly(|R|) per context and phase. The
  chain is S − 1 ≤ Σ_R 2(F_R + 1)(H + 1) + 2n(|C_T| + |C_Dom|) + 1 (R9) and F_R ≤ 3·Σ_q k_q (R11 (c) with k).
- (c) GAP-A ⇐ (CTX⁺) ∧ (FIRED-R) ∧ (STEAL-DEPTH_D for a constant D). Route: Lemma CHARGE plus E_d ≤ Q^{d+1}, so
  Σ_q k_q ≤ 2Q^{D+1}, with Q ≤ (|R|+1)|R|·#fired(R).
THE THREE DATA PREMISES:
1. (CTX⁺): polynomially many first-difference contexts, −1 attractor contexts and Dom inputs per phase.
   - Best data: max 13 first-difference contexts per phase (ctx13_n40, L-RED; CHECKER C11 re-run); 12 on ctx12_oink_n40; no
     n-trend at n = 40, 48.
   - Killed routes: (CHAIN) DE16; (CTX-ROOT) DE17; (CTX-LAMINAR) §23i; (PIECES-LAMINAR) §23l. The depth-0 piece count tracks
     S (§23l).
   - Structure known: the depth-0 contexts of a search form a decreasing chain from G′, and they are re-cut across
     searches.
2. (FIRED-R): #fired(R) ≤ poly(|R|) per context and phase.
   - Best data: max 23 fired at one context (mixed unions, stable); fired/|R| ≤ 1.0, tight at 19/19 after climbs; on long
     phases (S ≥ 2|R|) at most 3, ratio ≤ 0.375 (§23d, §23e, §23m).
   - Killed routes: (FIRED-STEP) with a constant, (FIRED-TOP-INJ), (FIRED-HALL), all on fired18_stable_n20; (FIRED-LAMINAR) on
     c6_replay3_n32; NO-RETURN on stealonce_viol_n76.
   - Caveat (R11 G-R11-6): it is a tangle count close to GAP-A's core, and the sum form does not need it.
3. (STEAL-DEPTH_D), constant D, or directly (STEAL-POLY_sum).
   - Best data: no re-steal at all on random sets up to n = 120 (both orders). On L-RED's two instances, and on 4 climbs
     from them: up to 12 re-steals, all at depth 1, k ≤ 2. N*_R ≤ 3 everywhere (§23g, §23n).
   - Killed routes: (STEAL-ONCE*) DE20, with (STOLEN-PERM), (STAYS-MET), NO-REFIRE and (DEP-SAFE); (STEALER-MONO) DE19;
     (MET-MONO) §23a.
BEST GUESS, which premise is most provable: the STEAL premise, in the form (STEAL-POLY_sum), attacked through the CHARGE
structure. Reasons:
- (a) It is the only premise with a signed proof skeleton. Every re-steal is charged to an event at a strictly earlier step
  (CHARGE), so the obstruction is now ONLY the multiplicative fan-out (one cause event may serve many re-steals). That is a
  sharp, local question.
- (b) The data is the cleanest of the three: depth ≤ 1, and k ≤ 2 even under targeted climbs. A depth-2 instance needs two
  stacked R35 levels, and it has not appeared.
- (c) A proof would not need (FIRED-R) if it bounds Σ_q k_q directly, e.g. by a potential over the step order that a cause
  event "pays" for all the re-steals it enables. Candidate: charge each re-steal to the VERTEX w whose loss from P(τ⁺) enabled
  it, and bound how often one vertex can leave and re-enter one prefix.
- (d) By contrast, (CTX⁺) and (FIRED-R) have had every set-structure route killed, and their counts are close to GAP-A's own
  (searches, tangles).
- Risk: if L-RED stacks two R35 levels, depth grows with nesting, and then only (STEAL-POLY_sum) via a non-depth argument
  survives.

- ADDENDUM (23:03Z by date -u; Lead 23:02Z): L-RED R37 (docs/red/R37-depth-obstruction.md, l-red fcc179b; a reading plus data,
  unrefereed) links the STEAL and CTX premises.
  - R37-1: a depth-D event needs a chain e_0..e_D with strictly increasing pairs and D+1 strictly ordered steps, so ≥ D+3
    visits of ONE context in ONE phase (tight, per L-RED). Hence depth ≤ V_R − 3, where V_R = visits of R in the phase.
    V_R is not bounded by S, since search_rec revisits R after each res = 1 round.
  - R37-2: every event pair needs a tangle learned in between (rests on an unproved determinacy reading).
  - Lockstep copies cannot reach depth 2 (cf. the union climb s9: 29 re-steals, all depth 1). A clock-gated lag design is
    written down, not built.
  - L-ALG note: a polynomial bound on V_R makes the STEAL premise trivial, without CHARGE or depth. Every event sits at a
    pair of consecutive visits, so k_q ≤ V_R − 1, N*_R ≤ V_R − 1, and F_R ≤ 3(V_R − 1) directly. So "(VISITS) V_R ≤ poly(|R|)
    per phase" with (CTX⁺) would give GAP-A by R9 alone. But (VISITS) is GAP-A in disguise: every search
    visits the root context G′ at least once (its first best_vertices call, depth 0), so V_{G′} ≥ S. Hence (VISITS) for
    R = G′ alone already bounds S, and the link gives nothing new. Through R12 (c) the depth bound gives only Q^(poly); the direct bound F_R ≤ 3(V_R − 1)
    is the stronger use.

23p. Vertex exits from a prefix: a polynomial charge that does not need constant depth (reading, unrefereed; DATA) (L-ALG
succ. 7, 22:42Z by date -u; tool experiments/alg/dtl_prefexits.py)
Definitions:
- An EXIT is a triple (step σ = (r, τ), vertex w, pair m) with w ∈ P_m(τ⁺) and w ∉ P_{m+1}(τ⁺); the prefix is BEFORE τ, as
  in G9-b1.
- X_R is the number of exits of context R in the phase. X(σ, w) is the number of exits of w at σ.
Lemma EXIT-CHARGE (reading; it uses only steps 1-3 of CHARGE as corrected in §23k, not the PREFIX-MONO part):
- Every re-steal (i, q), q = (σ, t), with previous event (j, q), contains an exit (σ, w, m) with w ∈ t and j < m < i.
- Distinct re-steals of the same q get distinct exits, because their intervals are disjoint.
- Hence Σ_q (k_q − 1) ≤ Σ_{exits (σ, w, m)} #{t fired at σ : w ∈ t} ≤ #fired(R)·X_R.
- So Σ_q k_q ≤ Q + #fired(R)·X_R ≤ #fired(R)·((|R| + 1)|R| + X_R).
Consequence (reading):
- (EXITS-POLY): X_R ≤ poly(|R|). Then (EXITS-POLY) ∧ (FIRED-R) ⇒ (STEAL-POLY_sum) for ANY polynomial bound; no constant D is
  needed.
- The local form (EXIT_c): X(σ, w) ≤ c for every step and vertex. It gives X_R ≤ c·|R|·(|R| + 1)|R|.
- Caveat: an exit happens only at a pair with a relevant steal at an earlier step (local PREFIX-MONO-X*). Each such pair
  gives at most |R|·#steps exits, so X_R ≤ N*_R·|R|·(|R|+1)|R|, and Σ_q k_q and X_R bound each other up to polynomial
  factors. (EXITS-POLY) is therefore a REFORMULATION of the STEAL premise, not a reduction of it. Its value is that (EXIT_c)
  is LOCAL: one vertex, one step.
DATA (dtl_prefexits.py; RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0; corpus of 254 files plus stealonce_viol_n76,
stealonce_both_n45 and stealer_viol_n76):
- stable order: exits per (context, step, vertex) are 1 in 3,073 cases and 2 in 22. The value 2 occurs only on
  stealonce_viol_n76 and stealonce_both_n45 (the DE20 instances). Max total exits per context: 3.78·|R| (fall3_n76, 287 at
  |R| 76).
- Oink order: 1 in 2,101 cases and 2 in 20 (only stealonce_both_n45). Max 3.43·|R|.
- So (EXIT_2) holds on all data. (EXIT_1) is FALSE on the DE20 instances, the same event as the re-steal.
Successor target: prove (EXIT_c) for some constant c, or a polynomial c(|R|). The question is how often one vertex can
leave and re-enter one step's prefix. A re-entry needs the prefix above to regrow around w, which in R35 is a NEW tangle
fired by region 66.

23q. Box 9: Lemma ENTRY-CHARGE: the STEAL premise without (FIRED-R) (reading, unrefereed; L-ALG succ. 7, 00:18Z by date -u)
Setting:
- As in §23g and §23k: one context R and one phase, steps σ = (r, τ), and P_i(σ⁺) = the prefix BEFORE τ in round r at
  visit i.
- P_i(σ⁺) is defined for every τ ∈ V_r, processed or not: it is the union of the regions of the tops above τ. If the visit has
  fewer than r rounds, use G9-b2's virtual round.
- An ENTRY is (σ, w, i) with w ∉ P_i(σ⁺) and w ∈ P_{i+1}(σ⁺). An EXIT is the reverse.
- X_R is the number of exits; N_ent is the number of entries.
- Events (i, q), q = (σ, t), are as in R11: t ∈ F_σ(i), and t meets P_{i+1}(σ⁺) without being contained in it.
Lemma ENTRY-CHARGE. Σ_q k_q ≤ |R|·N_ent ≤ |R|·(X_R + (|R| + 1)·|R|²).
Proof.
1. Fix an event (i, q). Since t fired in region σ at visit i, t ∩ P_i(σ⁺) = ∅ (dtl.cpp 136-139 with 690/699; G9-b1).
   Since t meets P_{i+1}(σ⁺), some w ∈ t gives an entry (σ, w, i). Map the event to one such entry.
2. Fan-out. Every event mapped to the entry (σ, w, i) has a distinct tangle t ∈ F_σ(i).
   - A tangle fires in a region step only if it has a vertex not yet in CurZ (dtl.cpp 143-146, can_attract_new). It then
     adds all its vertices to CurZ (165-172), and CurZ only grows during the step.
   - So every firing adds at least one new vertex, and |F_σ(i)| ≤ |A_σ(i)| − 1 < |R|.
   - Hence at most |R| events map to one entry, and Σ_q k_q ≤ |R|·N_ent.
3. For a fixed (σ, w), entries and exits alternate, so entries ≤ exits + 1.
   - There are at most (|R| + 1)·|R| steps (rounds ≤ |R| + 1, dtl.cpp 748-760; tops are p-vertices of R) and at most |R|
     vertices.
   - Summing gives N_ent ≤ X_R + (|R| + 1)·|R|². □
Corollaries (readings):
- (C1) (EXITS-POLY), X_R ≤ poly(|R|), implies (STEAL-POLY_sum). With the sum form signed in packet 9 (R12 (a)):
  GAP-A ⇐ (CTX⁺) ∧ (EXITS-POLY), given STR-DET. (FIRED-R) is NOT needed, and (STEAL-DEPTH) is not needed either.
- (C2) The local form (EXIT_c): every (σ, w) exits at most c times per phase. It gives X_R ≤ c(|R| + 1)|R|², so
  Σ_q k_q ≤ (c + 1)(|R| + 1)|R|³ and F_R ≤ 3(c + 1)(|R| + 1)|R|³ (R11 (c)).
- (C3) Converse, so this is an equivalence up to polynomial factors and not a reduction of the count: X_R ≤
  N*_R·|R|·(|R| + 1)|R|, because an exit needs a relevant steal at an earlier step at the same pair (CHARGE's local
  PREFIX-MONO-X*). What is new: the premise is now LOCAL (one vertex, one step) and FIRED-free.
DATA for (EXIT_c) (§23p, dtl_prefexits.py; corpus plus the DE19/DE20 instances): c = 2 on all data. Exits equal 2 only on
stealonce_viol_n76 and stealonce_both_n45 (22 and 20 cases, stable / Oink); 1 in 3,073 / 2,101 cases. Re-entry patterns:
§23r.
Status against L32: GAP-A ⇐ (CTX⁺) ∧ (EXIT_c), two named DATA statements. The STEAL side now has a proof route from a single
local statement. (CTX⁺) has none.

23r. Box 9: (EXIT_c) data and the shape of a proof (DATA plus SKETCH; L-ALG succ. 7, 00:23Z by date -u)
- Data: dtl_prefexits.py (now also counting re-entries; RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0). Sets: corpus plus
  stealonce_viol_n76, stealonce_both_n45, stealer_viol_n76 and resteal34_union_n90.

  | order | exits = 1 | exits = 2 | exits ≥ 3 | re-entries = 1 | re-entries = 2 |
  |---|---|---|---|---|---|
  | stable | 6,692 | 189 | 0 | 627 | 17 |
  | Oink | 2,106 | 20 | 0 | 49 | 0 |

  - Two exits occur only on DE20-derived instances (stealonce_*, resteal34_union_n90).
  - Re-entries occur on natural data too. Patterns 0101, 01001 and 10001 appear on f1_twodef_n48 and f1_twofall_n48, and
    010111 on fall3_n76.
  - So a vertex can leave a prefix and return without any re-steal, but no (step, vertex) has left 3 times. No INCOMPLETE
    run.
- Reformulation (reading). Within a round the prefixes are nested: P(r, τ⁺) grows as τ decreases. So w ∈ P_i(r, τ⁺) iff
  top_r^i(w) > τ, where top_r^i(w) is the top whose region holds w at visit i, or ⊥.
  - An exit of w at (r, τ) is exactly a downward crossing of level τ by the sequence (top_r^i(w))_i.
  - (EXIT_c) says: for every round and vertex, the top sequence crosses every level downward at most c times. By §23q this
    alone gives the STEAL side.
- Why the obvious proofs fail (named gap G23r):
  - (i) Exits at a step need a relevant steal at an earlier step (local PREFIX-MONO-X*), and every relevant steal is an
    entry at that earlier step (§23q, step 1). So exits at later steps are driven by entries at earlier steps, and
    re-entries are driven by growth.
  - (ii) The only signed monotone structure across visits is the first difference: at the first differing step the region
    grows strictly (FDL / EXACT*). The resulting lexicographic chain of prefix vectors gives only the bound
    (|R| + 1)^{#steps}, the §22v obstruction again.
  - (iii) A proof of (EXIT_c) therefore needs a per-vertex reason why top_r(w) cannot fall below the same level a third
    time. In R35 the second fall needs a NEW tangle in region 66 (R37-2: each event pair needs a tangle learned in
    between), so the reason must involve the learning dynamics, not the region geometry alone.
  - Precedent: per-vertex fall counts have died before: (FALL-V), DE18, for RV.
- Status: (EXIT_c) DATA (c = 2). No proof. Successor and climb target: EXIT ≥ 3 for one (step, vertex), e.g. three R35
  levels in series.

23s. Box 9: Lemma CHANGE-NEW: F_R ≤ 3·#fired⁺(R) UNCONDITIONALLY (reading, unrefereed; L-ALG succ. 7, 00:42Z by date -u; tool
experiments/alg/dtl_changenew.py)
Setting:
- One phase and one best_vertices context R (key (depth, R)), with consecutive visits x → y.
- T_x ⊆ T_y: within a phase tangles are only appended. tpr[t] = −1 (dtl.cpp 132-135) needs a vertex outside G, and G
  shrinks only in the dominion loop after a search (1031-1036), which ends the phase.
- #fired⁺(R) is the number of distinct tangles that fire (attractTangle returns true) at R in the phase, in region steps or
  in the threshold loop. D_R is the number of consecutive visit pairs whose set-level computations (the sequence of tattr
  calls: Z in, Z out, threshold) differ.
Lemma CHANGE-NEW. If the computations at x and y differ, some tangle t with ntv(x) ≤ t < ntv(y), i.e. born between the two
visits, fires at R in y.
Proof.
1. The call is a deterministic function of (R, T), given the order datum. It recomputes V from R (pyref 221; dtl.cpp 662-667).
   At set level it does not depend on str (STR-DET, R8).
   Let e_k be the first tattr call whose output differs. All earlier calls agree, so e_k has the same input Z, arena and
   threshold in both visits (the candidate tests, attracts, depend only on Z and R).
2. Region step. The prefix P(τ⁺) is the same, so each OLD tangle has the same exclusion status. By EXACT (R10 (a)),
   Z_out(x) = Cl(base; T_x \ E_x) and Z_out(y) = Cl(base; T_y \ E_y) ⊇ Z_out(x).
   - By EXACT* (R11 (a)), Z_out(y) = Cl(base; F(y)).
   - If F(y) ⊆ T_x, then F(y) ⊆ T_x \ E_x (the fired tangles are not excluded), so Z_out(y) ⊆ Z_out(x), and the outputs
     are equal: a contradiction.
3. Threshold loop. There are no exclusions (Gx = R, consume = None, dtl.cpp 726-731), and W_t = Cl_t(U) over all of T (§22r
   Corollary, the signed G-d1/G-Ψ convention). By soundness (S0), Z_out(y) ⊆ Cl(Z_in; used(y)). So the same argument
   applies.
4. In both cases a tangle of T_y \ T_x fires at e_k in y. □
Corollary (reading):
- Distinct differing pairs have disjoint birth intervals, so their new tangles are distinct, and D_R ≤ #fired⁺(R). A
  relevant-steal pair is a differing pair, so N*_R ≤ D_R.
- By R11 (c): F_R ≤ 3·N*_R ≤ 3·D_R ≤ 3·#fired⁺(R). This needs no STEAL premise at all; compare R11 (d)'s
  3(|R|+1)|R|·#fired(R), which needed (STEAL-ONCE*).
- With R9: GAP-A ⇐ (CTX⁺) ∧ (FIRED⁺-R), given STR-DET, where (FIRED⁺-R) says #fired⁺(R) ≤ poly(|R|). So there are two
  alternative routes for the per-context budget: (FIRED⁺-R) (this section) or (EXIT_c) (§23q, packet 10).
DATA (dtl_changenew.py; RM_EXCL=1 RM_LIGHT=1 RM_DV=0; sets include the corpus, the DE19/DE20 instances, fall3/fall4 and
ctx13_n40):

| set | order | differing pairs, CHANGE-NEW holds | contexts, D_R ≤ #fired⁺ and N*_R ≤ D_R | max D_R / #fired⁺ |
|---|---|---|---|---|
| mixed unions s1 | Oink | 14,008 / 14,008 | 17,427 / 17,427 | 1.0 |
| mixed unions s1 | stable | 14,202 / 14,202 | 17,739 / 17,739 | 1.0 |
| cross unions s11 | stable | 9,151 / 9,151 | 10,955 / 10,955 | 1.0 |

No INCOMPLETE run.
HONEST LIMIT. The bound is tight, and at the ROOT context it tracks S. On spp_chain_up_n43 the root context (|R| = 43) has
42 visits, D_R = 41 and #fired⁺ = 41: every search learns a tangle that fires at the root in the next search. So
(FIRED⁺-R) at G′ is close to bounding S directly, i.e. close to GAP-A's core (as R11 G-R11-6 warned for (FIRED-R)). It is
still ≤ |R| on all data (41 ≤ 43). The lemma's value is structural: per context, the budget F_R is at most 3 times the
number of NEW tangles that reach it, with no steal bookkeeping.
- Note (00:46Z by date -u): at G′, D_{G′} (differing consecutive root calls) is about S − 1 in the data; on spp_chain_up_n43
  it is 41 for S = 42. So (FIRED⁺ ≤ |R|) at the root would give S ≤ |G′| + 1 per phase, which is (SPP) itself (DATA, tight;
  GAP-A-M §21). The root-level form of (FIRED⁺-R) is therefore the old core conjecture, not a new route. Below the root it
  is a genuinely per-context statement.

23t. Referee imports for packet 10 (§23q) (L-ALG succ. 7, 00:50Z by date -u)
The Lead asked for "§23r or the next free letter"; §23r and §23s are taken, so the imports go here. §23q is not rewritten.
Sources: REFEREE docs/referee/R-P10.md (referee aabcefd) and REFEREE-2 docs/referee-2/R2-P10.md (referee-2 0cbe61e, §6
57468a8), both labelled "(Opus 5.5, D12)".
- Verdicts:
  - (a) ENTRY-CHARGE: SIGN WITH GAPS from both, closed. Step 2 (fan-out < |R| via can_attract_new, dtl.cpp 143-146 and
    165-172) was verified line by line by both.
  - (b) C1: SIGN. (c) C2: SIGN.
  - (d) C3: confirmed as an equivalence up to polynomial factors.
  - (e) data: confirmed.
- G10-a1 (both; closed), stated as ONE counting convention for §23q, §23p and §23r:
  - The step set is FIXED: every p-vertex τ of R and every round r ≤ |R| + 1 (dtl.cpp 748-760). "τ ∈ V_r", read per visit,
    is NOT used (REFEREE-2). P_i(r, τ⁺) is defined for every such (r, τ) at every visit.
  - Round convention (R2-P7 §3): after a "no candidates" stop (dtl.cpp 716 / 765) the last round is repeated for all later
    r. After a V = ∅ stop (768-771), P_i(r, τ⁺) = ∅ for all later rounds r.
  - Entries and exits are counted on this fixed grid, so the count "(|R| + 1)·|R| steps" in §23q step 3 is exact for the
    grid.
- N10-b1 (both; wording). "FIRED-free" is relative to §23g and §23p only. R12 (a)'s sum form and R11 (c) were already
  FIRED-free. What ENTRY-CHARGE removes is the #fired factor between exits and Σ_q k_q (§23p's #fired(R)·X_R).
- REFEREE-2's shorter route (signed). Step 1 alone gives N*_R ≤ N_ent: each relevant-steal pair has an entry at its pair.
  So F_R ≤ 3·N*_R ≤ 3(X_R + (|R| + 1)|R|²) without the fan-out step, and with (EXIT_c), F_R ≤ 3(c + 1)(|R| + 1)|R|². This
  is better than §23q's |R|·(...) bound on Σ_q k_q for the purpose of F_R.
- REFEREE's constants for (c): X_R ≤ c(|R| + 1)|R|². A constant c is strictly stronger than (EXITS-POLY); a polynomial c(|R|)
  is equivalent to it.
- Status: GAP-A ⇐ (CTX⁺) ∧ (EXIT_c), given STR-DET, is a SIGNED conditional (R12 (a) plus packet 10). Its premises are DATA.

23u. Box 9: the two routes meet. (EXIT_c) bounds D_R, the root included (SKETCH with one named gap; L-ALG succ. 7, 00:55Z by date -u)
Grid and conventions are those of §23t (G10-a1). §23s (packet 11) is frozen and not edited.
Claim. D_R ≤ N_ent + D_R^thr ≤ X_R + (|R| + 1)|R|² + D_R^thr, where D_R^thr is the number of differing pairs whose FIRST
difference is in a threshold loop.
Argument.
- Take a differing pair x → y whose first difference is a region step σ₀ = (r, τ₀).
  - By §23s step 2 (EXACT), the region there grows strictly: A_y(σ₀) ⊋ A_x(σ₀), and the prefix P(τ₀⁺) is the same.
  - Pick w ∈ A_y(σ₀) \ A_x(σ₀), and let σ′ = (r, τ₀ − 1) be the next grid step.
  - Then P_y(σ′⁺) ⊇ P(τ₀⁺) ∪ A_y(σ₀) ∋ w, while P_x(σ′⁺) = P(τ₀⁺) ∪ A_x(σ₀) ∌ w. So (σ′, w, x) is an entry.
  - Distinct pairs give distinct entries (the pair index differs).
- Hence D_R − D_R^thr ≤ N_ent, and N_ent ≤ X_R + (|R| + 1)|R|² (§23q step 3, on the §23t grid).
- If τ₀ is the lowest grid top of round r, use σ′ = (r + 1, max top), the first step of the next round. Then P(σ′⁺) = ∅ in
  both visits and the entry argument fails, so these pairs also belong to the gap.
Gap G23u (named). Bound the pairs whose first difference is in a threshold loop, or at the last region step of a round.
- There a new tangle grows W_t (§23s step 3), which changes V_{r+1}. The first effect on the grid is a new top u in round
  r + 1, and u may already sit inside another top's region in x, so an entry is not guaranteed.
- A candidate fix: count these pairs by the RV changes they cause (RV only rises there, §22r Corollary C1-C3). That would
  need an RV-type per-vertex bound, of the same local kind as (EXIT_c).
Consequences (if G23u closes):
- (EXIT_c) bounds D_R, the number of differing visit pairs, for every context, the root G′ included.
- With CHANGE-NEW: N*_R ≤ D_R ≤ poly. So the (FIRED⁺-R) route (§23s) and the (EXIT_c) route (§23q) MEET. At the root
  both are (SPP)-strength statements about how often the root call can change.
- (EXIT_c) at the root alone does not bound S. Searches whose root calls agree differ later; that is R9's sum over
  contexts, i.e. (CTX⁺).
- Data check, not run (context budget): D_R^thr per context. Successor target.

23v. Referee imports for packet 11 (§23s, CHANGE-NEW) (L-ALG succ. 8, 01:19Z by date -u; produced on Opus 5.5)
§23s is frozen and not rewritten. Sources: REFEREE docs/referee/R-P11.md (referee fc86762; its §C comparison is still
pending) and REFEREE-2 docs/referee-2/R2-P11.md (referee-2 aeedd00, comparison §5 bb8a625), both "(Opus 5.5, D12)", read on
trunk 3572651. No REJECT.
- Verdicts:
  - (a) Lemma CHANGE-NEW: SIGN WITH GAPS (REFEREE; N11-a1, G11-a1, both closed) / SIGN (REFEREE-2, N11-a1).
  - (b) Corollary D_R ≤ #fired⁺(R), N*_R ≤ D_R, F_R ≤ 3·#fired⁺(R) unconditionally, and GAP-A ⇐ (CTX⁺) ∧ (FIRED⁺-R) given
    STR-DET: SIGN from both (REFEREE-2 adds N11-b1).
  - (c) Honest limit: CONFIRMED by both. GAP-A ⇔ (CTX⁺) ∧ (FIRED⁺-R) up to polynomial factors, given STR-DET (necessity:
    Lemma W gives #fired⁺(R) ≤ |T_phase| ≤ n·S; contexts ≤ calls per search × S). An EQUIVALENCE, not a reduction. At G′
    alone (FIRED⁺-R) is necessary, not sufficient, and equals S − 1 on chain families (spp_chain_up_n43: 41 = 41, both orders).
  - (d) Data: CONFIRMED. dtl_changenew.py unmodified; REFEREE probe p11probe.py (corpus 138 files: 1,160 / 1,231 differing
    pairs, all with a NEW tangle firing AT the first differing tattr e_k, which is stronger than §23s's "fires at R in y");
    REFEREE-2 an11.py on instrumented pinned C++ (268 files: 3,028 / 3,066 differing pairs, 0 failures; 0 differing pairs with
    equal alive T; 4,350 / 4,265 identical pairs although new tangles were born, so a born tangle is necessary, not sufficient).
- N11-a1 (both; closed). STR-DET is NOT needed for §23s step 1. best_vertices reads str only at dtl.cpp 73, and there only to
  decide whether to write str; no set membership depends on str. STR-DET concerns extraction (268), which best_vertices does
  not call. So §23s step 1 reads: the set-level trace is a function of (R, p, alive T, order datum) by direct code reading.
- G11-a1 (REFEREE; closed). §23s step 3 (threshold level, dtl.cpp 722-731) follows DIRECTLY from DTL-proof Lemma 1.2: all
  of Z is pushed at 724, Gx = R and nothing is consumed, so out = Cl_t(Z_in; T) over all of T. The "§22r Corollary" cited in
  §23s is about cross-visit monotonicity under (NS) and is not the tool used. Then Z_out(x) ⊆ Z_out(y) ⊆ Cl_t(Z_in; used(y))
  by soundness, and the EXACT* contradiction applies (REFEREE-2 argues the same from the full re-push at 724).
- The state inventory (both referees, line for line), which is the proof of "a function of (R, p, alive T, order datum)":
  - V: cleared by the caller (852), asserted empty at 648, rebuilt from R (662-667). R is only read (CurR is a copy, 690).
  - Locals prevV, Z, CurR, CurZ, curdist (651-655). Candidates (global) is written (712-714) before it is read (735) in each round.
  - Q (global) is empty on entry: every producer drains it (488, 697, 727, 883, 918, 944, 967, 1032; the 898-912 seeding is
    drained at 918).
  - str: written at 73, 89, 171, 694; READ only at 73, to guard a str write.
  - attracts (41-57) reads Z, R and the static game; attractVertices (66-101) reads R, Z, the arena argument, priorities,
    ins/outs; attractTangle(s) (110-202) reads tpr, tv, tout, tin (tangle-id order; new ids appended at 443/458-461), this->G
    (132), R, Z.
  - Lazy deletion (132-135) may change tpr between visits, but a tangle with a vertex outside this->G returns false whether it
    is deleted at 117 or reaches 132, and no such tangle can fire (138-139, R ⊆ G). So only the ALIVE set T matters.
  - this->G is assigned only at 1082 (start) and 1035 (dominion loop after search_rec), so it is constant within a phase.
  - NOT read: depth, X, W, cur_depth, val, the dominion state (S, dom_vector), the pea_* arrays.
  - Tangles are only appended within a phase (push_back at 440/458-461, nothing removes an entry; tpr[t] = −1 only at 134 for a
    tangle with a vertex outside this->G). So T_x ⊆ T_y and "born between x and y" = ids in [ntv(x), ntv(y)).
  - Consequence (REFEREE-2): the context key (depth, R) is finer than needed; identical visits need only equal alive T.
- N11-b1 (REFEREE-2 only; REFEREE's §C pending, so ONE signature). The e*-at-R transitions are bounded by D_R directly: for an
  e*-at-R transition s → s+1 the calls at the e* position have equal input R and different outputs, so some CONSECUTIVE visit
  pair of R between them differs; two such intervals overlap only inside s+1 before π, where T is constant (STR-DET (c)), so the
  charged pairs are distinct. Hence #(e*-at-R) ≤ D_R ≤ #fired⁺(R) given STR-DET (≤ 2·D_R without it), and
      S − 1 ≤ Σ_{R ∈ C_bv} #fired⁺(R) + n(|C_T| + |C_Dom|) + 1,
  with no H and no F_R.
- What this changes for box 10 (L-ALG reading, unrefereed). With N11-b1 the per-context budget is D_R itself:
      S − 1 ≤ Σ_{R ∈ C_bv} D_R + n(|C_T| + |C_Dom|) + 1   (given STR-DET; one signature on the D_R form).
  So (D-POLY) "D_R ≤ poly(|R|) per context and phase" with (CTX⁺) gives GAP-A, and §23u's D_R ≤ N_ent + D_R^thr turns
  (EXIT_c) plus a bound on D_R^thr (gap G23u) into (D-POLY). That is the box-10 target.

23w. Box 10: gap G23u CLOSED (reading, unrefereed): D_R is bounded by the non-quiet pairs; the "RV rises" fix is KILLED
(L-ALG succ. 8, 01:41Z by date -u; produced on Opus 5.5; tool experiments/alg/dtl_drthr.py)
Grid, conventions and notation as in §23t (G10-a1): rounds r ≤ |R| + 1 with the round convention, grid tops = every p-vertex
of R, top_r^i(w) = the top whose region holds w in round r at visit i (⊥ = −1), U_r = the union of round r's regions, and
W_{r,t} := Cl_t(U_r; T) for every grid round and threshold level t (the G-Ψ convention, also for padded rounds; U_r = ∅ after
a V = ∅ stop). L = number of threshold levels (t ∈ {0} ∪ {q ∈ prios : 0 < q ≤ maxpr}, so L ≤ n + 1).
Definition. A consecutive visit pair x → y of R is QUIET if it has no entry and no exit on the grid. (An entry/exit is at a grid
step (r, τ); a vertex moving ⊥ ↔ region of the LOWEST grid top is invisible on the grid.)
DATA FIRST (dtl_drthr.py; RM_LIGHT=1 RM_DV=0; sets: corpus experiments/alg/instances/*.pg (141 files) plus stealer_viol_n76,
stealonce_viol_n76, stealonce_both_n45, fall3_n76, fall4_n116 (l-red carry); mixed unions UNIONS=900 SEED=1 NMAX=32; cross unions
UNIONS=600 SEED=11 UM_CROSS=3 NMAX=32 with DR_VIRT=1; both order data; the union runs also re-run the corpus files):

| set | order | differing pairs | 1st diff region (all have an entry) | 1st diff threshold: entry / NO entry | non-quiet pairs | quiet differing pairs, W grows strictly |
|---|---|---|---|---|---|---|
| corpus + DE19/DE20 | stable | 1,394 | 400 | 667 / 327 | 1,067 | 327 / 327 |
| corpus + DE19/DE20 | Oink | 1,354 | 378 | 636 / 340 | 1,014 | 340 / 340 |
| mixed unions | stable | 9,336 | 2,880 | 4,114 / 2,342 | 6,994 | 2,342 / 2,342 |
| mixed unions | Oink | 9,435 | 2,978 | 4,106 / 2,351 | 7,084 | 2,351 / 2,351 |
| cross unions | stable | 6,780 | 2,507 | 2,812 / 1,461 | 5,319 | 1,461 / 1,461 |
| cross unions | Oink | 6,878 | 2,543 | 2,838 / 1,497 | 5,381 | 1,497 / 1,497 |

- "No entry" ⇔ quiet on all data: 0 pairs with only invisible (⊥ ↔ lowest region) changes; no region first difference at the
  lowest grid top; 0 identical pairs with an entry.
- KILL of the §23u candidate fix "charge the threshold pairs to RV rises (§22r C1-C3)": at EVERY no-entry differing pair
  (8,318 over the six runs) RV is unchanged (neither rises nor falls). Killer: spp_chain_up_n43, root context (|R| = 43,
  42 visits): all 41 differing pairs are quiet, first difference in a threshold loop (rounds 2, 3, ...), RV equal, both orders.
- Max D_R = 41 = max quiet differing pairs in ONE quiet block (spp_chain_up_n43 root), both orders, all sets.
- Max exits per (step, vertex): 2 (stable; stealonce_viol_n76, resteal34_union_n90), 1 or 2 (Oink; 2 on stealonce_both_n45);
  with the virtual end-of-round step (DR_VIRT=1, an exit from U_r) on the cross unions: still 2 / 1.
Lemma QUIET-BLOCK (reading, unrefereed). Let x → y be quiet. Then for every grid round r and level t: U_r(x) ⊆ U_r(y),
W_{r,t}(x) ⊆ W_{r,t}(y), every round-r region of x other than the lowest grid top's equals that of y, and the lowest grid top's
region can only grow. If the set-level computations of x and y differ, then Φ := Σ_r |U_r| + Σ_{r,t} |W_{r,t}| rises strictly.
Proof.
1. Rounds by induction, claim (I_r): V_r(x) ⊆ V_r(y), and U_{r′}, W_{r′,t} are ⊆ for r′ < r. (I_1): V_1 = the p-vertices of R in
   both visits (dtl.cpp 662-667).
2. Round r. Quiet means top_r^x(w) = top_r^y(w) except for ⊥ ↔ low (the lowest grid top) moves. So every region of a top
   τ > low is equal, and the prefix before low is equal. If low is processed in x it is in V_r(x) ⊆ V_r(y) and outside the
   common prefix, so it is processed in y too, and by EXACT (R10 (a)) with equal prefix and T_x ⊆ T_y its region grows:
   A_x(low) ⊆ A_y(low). If low is processed only in y, A_x(low) = ∅. So a move low → ⊥ never happens and U_r(x) ⊆ U_r(y).
3. Threshold loop. Every threshold output is Cl_t(Z_in; T) over all of T (DTL-proof Lemma 1.2; §23v G11-a1), and the level chain
   gives Cl_t(Cl_{t′}(U_r)) = Cl_t(U_r) for t′ ≤ t (Cl_{t′} ⊆ Cl_t, idempotent). So the level-t output is W_{r,t}, also on a
   716 round by the G-Ψ convention. Cl is monotone in its base and in T, so W_{r,t}(x) ⊆ W_{r,t}(y).
4. Candidates (dtl.cpp 713-747). A top v ∈ V_r is dropped iff it is unattracted to U_r and to every W_{r,t} with t < pr v;
   attraction is monotone in the target set, so a top dropped in y is dropped in x if it is in V_r(x). Hence
   V_{r+1}(x) = V_r(x) \ cand_x ⊆ V_r(y) \ cand_y = V_{r+1}(y): (I_{r+1}).
5. Strictness. If Φ(x) = Φ(y), then U_r(x) = U_r(y) for all r, so (by 2) the round maps are equal, and W_{r,t}(x) = W_{r,t}(y).
   The computation is then a function of these sets: by induction V_r is equal (step 4 with equal sets), the region and
   threshold outputs are equal, and the stop decisions (716 / 765 / 768-771) are equal. So the computations are identical. □
Corollary (G23u CLOSED, reading). Within a maximal run of consecutive quiet pairs, Φ never decreases (step 1-3 hold at every
quiet pair, identical or not) and rises at every differing pair; Φ ≤ (|R| + 1)(L + 1)|R|. Let M_R be the number of non-quiet
pairs; each has an entry or an exit, so M_R ≤ N_ent + X_R ≤ 2X_R + (|R| + 1)|R|² (§23q step 3). Hence
    D_R ≤ M_R + (M_R + 1)·(|R| + 1)(L + 1)|R|.
- With (EXIT_c): X_R ≤ c(|R| + 1)|R|² (REFEREE's constant, §23t), so D_R ≤ poly(|R|, n) at EVERY context, the root included.
  This is §23u's claim with its gap closed; the threshold-loop and last-region-step pairs are absorbed by QUIET-BLOCK, not by an
  entry and not by RV.
- Conversely X_R ≤ D_R·(|R| + 1)|R|² trivially. So per context (D-POLY) ⇔ (EXITS-POLY) ⇔ (STEAL-POLY_sum) ⇔ (RELSTEAL) up to
  polynomial factors, and (FIRED⁺-R) ⇒ (D-POLY) (§23s). The two routes MEET: all per-context forms are one statement, and the
  local sufficient form is still (EXIT_c). This is a reformulation, not new progress on GAP-A.
- Honest reading of the killer: on spp_chain_up_n43 all the root's work is quiet: the region maps never change and every one of
  the 41 differing root calls is a strict growth of some W_{r,t}. So at the root the (SPP)-type count lives entirely inside one
  quiet block, where QUIET-BLOCK gives only Φ ≤ (|R|+1)(L+1)|R| per block: polynomial, but the factor that (SPP) would need to
  be linear is the block length.
Status: Lemma QUIET-BLOCK and the corollary are a reading, unrefereed; the data columns above are DATA. Candidate for the next
referee packet (short; the only new ingredients are steps 2 and 4).

23x. Box 10: (EXIT_c) proof attempt: where exits come from, one kill, and the exact missing step (L-ALG succ. 8, 01:54Z
by date -u; produced on Opus 5.5; tools experiments/alg/dtl_exitshape.py, dtl_netgrowth.py, dtl_roundfalls.py, dtl_exitclimb.py)
Grid and conventions as in §23t / §23w. The step order is: rounds ascending; within a round, grid tops descending, then the
virtual end-of-round step (prefix U_r).
Lemma EXIT-ORIGIN (reading, unrefereed). Let x → y be a consecutive visit pair of R with at least one exit (grid or virtual), and
let σ₁ = (r₁, τ₁) be its first exit step. Then (a) V_{r₁}(x) ⊆ V_{r₁}(y), and (b) the pair has a relevant steal at a step
(r₁, τ′) with τ′ > τ₁. So every exit of a pair is either in the round of a relevant steal above it, or later than an earlier
exit of the SAME pair; a "V-loss" exit (a higher top of V_r(x) missing from V_r(y)) is always secondary.
Proof. (a) No exit before σ₁ means U_r(x) ⊆ U_r(y) for r < r₁ (no vertex leaves U_r: the virtual step is included). Steps 3-4 of
QUIET-BLOCK (§23w) use only U ⊆ and T ⊆, so W_{r,t}(x) ⊆ W_{r,t}(y) and V_{r+1}(x) ⊆ V_{r+1}(y) for r < r₁. (b) In round r₁,
V ⊆ V′ and T ⊆ T′; if no relevant steal occurred at a step above τ₁ in round r₁, local PREFIX-MONO-X* (§23g G23g-1; signed
in R12 (b) as G23g-1) gives P_x(σ) ⊆ P_y(σ) for every step σ of round r₁ up to and including σ₁, so no exit at σ₁. □
DATA (dtl_exitshape.py; RM_LIGHT=1 RM_DV=0; corpus 141 files + stealer_viol_n76, stealonce_viol_n76, stealonce_both_n45,
fall3_n76, fall4_n116; both orders):
- Exits by round and cause (grid exits; cause 'Vloss' = a higher top of V_r(x) is missing from V_r(y)): stable round 1: 5 (all
  steal); rounds ≥ 2: 1,406 Vloss, 982 steal. Oink: round 1: 0; rounds ≥ 2: 663 Vloss, 239 steal.
- (DOWN_2) "top_r(w) falls at most twice per (context, round, vertex) per phase" (any level; implies (EXIT_2)): histogram of
  falls per (r, w) with ≥ 1 fall: stable {1: 1,840, 2: 283}, Oink {1: 891, 2: 12}. Max 2.
- (NET-GROWTH) KILLED (DEAD.md box 10; cm_viol_oink_n28, lex_viol_oink_n20). The obstruction is a round-index SHIFT: in
  lex_viol_oink_n20 (root, pair 1, stable) the later visit keeps 7 and 6 tops in rounds 3-4 (3 and 4 before), ends after 14
  rounds instead of 15, and rounds 5-15 show 0 entries and 146 exits.
- Round-count oscillation (dtl_roundfalls.py, same sets): falls of a context's round count per phase: stable {0: 1,417, 1: 179,
  2: 5}, Oink {0: 1,390, 1: 178, 2: 4}; max 2, on cm_viol_oink_n28 root: 5, 5, 8, 7, 9, 11, 10 (the last a res = 1 stop, which
  repeats its round and empties nothing).
Reading of the obstruction (why EXIT_c is hard):
- The per-visit grid vector, ordered by step, increases LEXICOGRAPHICALLY at every pair (QUIET-BLOCK steps 1-4 up to the first
  change, then the first change is growth: a new top or a strictly larger region with an equal prefix). (EXIT_c) is exactly the
  statement that this lexicographic chain is not a counter: a coordinate (σ, w) is reset (exit) only O(1) times. EXIT-ORIGIN
  says each reset is triggered by a growth at an earlier coordinate of the same pair, which is what a binary counter does. So a
  proof must show that DTL's growth at an earlier coordinate cannot RE-trigger the same reset more than c times, i.e. a
  per-vertex charge of re-entries to something consumed. Every candidate charge tried so far (RV, Φ_grid, depth) is dead or
  multiplicative.
- What a counter would need on A_DTL: one context whose round count (or one region's top set) oscillates ≥ 3 times in one phase
  under DTL's own learning. Data: round count falls ≤ 2, top_r(w) falls ≤ 2.
Status: Lemma EXIT-ORIGIN is a reading, unrefereed. (EXIT_c) and (DOWN_2) are DATA. No proof route closes; L32 is NOT met by this
section. Self-attack climbs (dtl_exitclimb.py, fitness exits ≥ 3, then round-count falls) are running from cm_viol_oink_n28 and
stealonce_both_n45.

23y. Box 10: (FIRED⁺-R) below the root: no birth locality (DATA; L-ALG succ. 8, 02:02Z by date -u; tool
experiments/alg/dtl_firedlocal.py; RM_LIGHT=1 RM_DV=0; corpus 141 files + stealonce_viol_n76, stealonce_both_n45, stealer_viol_n76,
fall3_n76, fall4_n116; both orders)
- Depth ≥ 1 contexts with ≥ 2 visits: 380 (stable) / 374 (Oink). Max #fired⁺(R)/|R| = 0.8 (dtl_searches15_n24, depth 1,
  |R| = 15, 12 fired⁺, 5 visits; both orders).
- Where the fired⁺ tangles of such an R were born (sptl context B): LOCAL B ⊆ R 277 / 284; INCOMPARABLE 277 / 301; ANCESTOR B ⊋ R
  2 / 3; born before the phase 14 / 4.
- Reading: half the tangles that reach a sub-context come from sibling-type contexts, so a "tangles fired at R are learned
  inside R" induction on depth is not available. (FIRED⁺-R) below the root has no route from locality. Not pursued further this
  box (task (3) was conditional on (1)-(2) stalling; (1) closed, (2) stalled at the counter obstruction of §23x).

23z. Box 10: can QUIET-BLOCK be made LINEAR? Two forms killed; block length ≤ 0.953·|R| stays DATA (L-ALG succ. 8,
02:22Z by date -u; tool experiments/alg/dtl_quietlin.py; RM_LIGHT=1 RM_DV=0; corpus 141 files + stealonce_viol_n76,
stealonce_both_n45, stealer_viol_n76, fall3_n76, fall4_n116; both orders)
Motivation: §23w bounds a quiet block by Φ ≤ (|R|+1)(L+1)|R|, but the longest block seen is 41 at |R| = 43 (spp_chain_up_n43
root). A LINEAR block bound would cap the threshold-only part of the root's work by |G′|, the (SPP) shape.
A_i := the vertices that join some U_r or W_{r,t} at quiet differing pair i.
- (QUIET-LIN) "each vertex is in A_i for at most one differing pair of a block": KILLED. 35 (stable) / 33 (Oink) failing pairs;
  a vertex is re-advanced up to 4 times in one block (spp_final_n30 root, |R| = 30, block 6). Smallest instances:
  experiments/alg/instances/dtl_cross3_n14.pg (sha1 90d95c85; pinned Oink 8 iterations verified) root pair 1 re-advances 0, both
  orders; fired18_stable_n20.pg (sha1 42307b22; pinned Oink 4 iterations verified), stable. Reading: one vertex joins W at
  different (round, level) slots at different pairs.
- (QUIET-NEWV) "every A_i has a vertex not in an earlier A_j of its block": KILLED. 4 failing pairs per order (323 / 336
  hold). Instances: experiments/alg/instances/spp_final_n30.pg (sha1 e57c2cf9; pinned Oink 22 iterations verified) root pair 16
  A = {6, 7, 15}, also |R| = 29 pair 3 and depth 1 |R| = 26 pair 2, both orders; spp_n30.pg (sha1 587697ae; pinned Oink 21
  iterations verified) |R| = 28 pair 6, both orders.
- DATA: max quiet block length / |R| = 0.953 (spp_chain_up_n43, 41 / 43), both orders. 88 / 88 quiet differing pairs advance
  exactly one vertex, the rest ≥ 2.
- Status: the polynomial QUIET-BLOCK bound stands (reading); a linear form has no surviving candidate. Not pursued further.

24. Box 10, continued (L-ALG successor 8; produced on Opus 5.5)
24a. U-shrinks need a deficit; grid exits without one are re-cuts inside U (reading + DATA; 02:34Z by date -u; tool
experiments/alg/dtl_exitshape.py EX_DEF=1, RM_LIGHT unset, RM_DV=0; corpus 141 files + stealonce_viol_n76, stealonce_both_n45;
both orders)
Notation: Û_r(V, T) = the IDEAL round union (dtl_ideal.ideal_union: the tops of V_r level by level, closure over all of T, no
exclusions); a round has a DEFICIT if U_r ≠ Û_r (rec["deficit"]). Actual ⊆ ideal (U_r ⊆ Û_r) as in the box-4 deficit
analysis (GAP-A-M §18; reading).
Lemma DEF-SHRINK (reading, unrefereed). For a consecutive visit pair x → y of R, let r be the first round with U_r(x) ⊄ U_r(y).
Then round r of y has a deficit.
Proof. For r′ < r, U_{r′}(x) ⊆ U_{r′}(y), so QUIET-BLOCK steps 2-3 (§23w; they use only U ⊆ and T ⊆) give V_r(x) ⊆ V_r(y).
Û is monotone in V and T (a closure with no exclusions). So U_r(x) ⊆ Û_r(V_r(x), T_x) ⊆ Û_r(V_r(y), T_y). If U_r(y) = Û_r(y), then
U_r(x) ⊆ U_r(y), a contradiction. □
Corollary (reading). If no call of R in the phase has a deficit round, then along the visits every U_r and every V_r only grows,
so W_{r,t} only grows, and the only falls of top_r(w) are RE-CUTS: w moves to a lower top's region inside the same U_r.
DATA: pairs with a fall of some top_r(w): stable 90, of which 89 have a U-shrink (all 89 with a deficit in y, and in x) and 1 has
no deficit in either visit (fired18_stable_n20 root |R| = 18, pair 1: no U-shrink, a re-cut, as the corollary says). Oink: 25,
all with a U-shrink and a deficit in y (and in x).
Reading: (EXIT_c) splits into (a) U-shrinks, charged to deficit rounds of the later visit (the old (H4)/Lemma E obstruction:
a straddling stored tangle), and (b) re-cuts inside U. (a) is the box-4 DEF count, which has no constant bound (§17) but has
not been shown super-polynomial; (b) is new and rare (1 pair in this data). Neither is proved.
