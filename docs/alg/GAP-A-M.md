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
- Driver lemma (SKETCH, 08:52Z). A transition of level j is driven by a tangle that is NEW (learned in search s) and fires
  in piece j's computation in search s+1 (first-difference argument: with the old tangle set the computation at an equal
  context is identical). Such a tangle was learned at a piece k ≥ j of search s, or inside the recursion of a cut piece
  k ≥ j: a tangle learned at a piece k < j lies inside D_k(s) (an SCC of an sptl region of V*, or inside a cut's Z), and
  D_k(s) = D_k(s+1) is outside R_j by the equal contexts. Open step: "every sptl region of the last pass lies in Dom(V*, R)"
  (both are top-down consumed attractors from V*; not written out). So carries come from deeper learning (R9's CARRY).
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
| the other 717 games: 600 random (n ≤ 24), every file in experiments/alg/instances, tc N ≤ 6, tc+ N ≤ 5, counter_* | — | 0 | 0 |
tc+ is a one-pass SWEEP (each piece changes once, deepest first) and has no replay at all; its 2N + 2 searches are the
sweep, not a counter. Over these 718 games (A_DTL and C6 give the same histogram) exactly ONE replay occurs, of depth 1 (level 1 re-advancing
after the root moved, in a climbed instance).
6.4 What would close GAP-A along this route (open; for the proof lane): a lemma charging every replay at level j to a
global resource, e.g. "a level-j replay needs a tangle usable in the new context that was usable in NO earlier level-j
context of the phase", with that resource bounded polynomially. What would kill it (for L-RED): a family whose replay depth
grows with n. Climbs on C6 with fitness = replay depth ≫ replays ≫ searches are running (started 08:43Z).
