# GAP-A data: what bounds the number of tangles (L-ALG, box 2026-10-16 00:00Z–07:40Z)
Subject: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7 (DTL-proof.md §0). Everything here is measurement
or reading; nothing is a result. Status words: PROVED / SKETCH / GAP / DATA / DEAD. Scripts in experiments/alg/ (pinned command,
release build reads tangles from `-t -t`; the Debug build and a PATCHED Debug build, recipes in notes/L-ALG.md, read pieces).

## 1. Tools (all new this box)
| script | reads | reports |
| --- | --- | --- |
| dtl_tangle_family.py OINK G.pg [--sets] | release `-t -t` | tangle sets; laminarity (nested / crossing / disjoint pairs); per-top counts; (C-new) violations split into restart violations and in-search chain breaks; strict shrinks |
| dtl_heads.py G.pg TRACE | PATCHED debug trace | per-vertex removal head per search ('dom' top / 'cut' level / 'dis' top) and its transitions across same-player searches; depth-0 piece sequence per search; first stable piece's R and V* vs the previous search |
| dtl_distance.py G.pg TRACE | any `-t` trace | pruning distance of every vertex at the FIRST best_vertices call of each search; monotonicity across same-player searches |
| dtl_contexts.py G.pg PATCHED-TRACE | patched debug trace with distance lines | fixed-context monotonicity: for recurring depth-0 contexts, distance up/down counts, stable→−1 reverts, V* gains/losses |
| dtl_tops.py G.pg DEBUG-TRACE | debug trace | true tops (the `region` line before each tangle), per-top and per-(top, search) counts, coverage potential P1, membership-oscillation histogram |
| dtl_oscclimb.py DEBUG_OINK OUT n seed steps | debug | hill-climb for membership oscillation at small n (found depth 1 only at n ≤ 12 in 40k steps) |
| dtl_crossclimb.py OINK OUT n seed steps [--cnew / --pertop / --restart / --searches] [--seedgame G] | release | hill-climb on random games (n vertices, priorities ≤ n, out-degree 1–3, 1–3 mutations per step) for crossing tangles at one top / (C-new) violations / tangles at one top / restart violations / searches |
Instances kept (experiments/alg/instances/): dtl_cross3_n14.pg, dtl_pertop31_n18.pg, dtl_pertop28_n24.pg, dtl_cnew14_n20.pg,
dtl_restart7_n16.pg, dtl_restart8_n20.pg, dtl_searches15_n24.pg, dtl_searches20_n32.pg. dtl_tops.py G.pg DEBUG-TRACE gives the
TRUE top of every tangle (the `region` line preceding it) and the membership-oscillation histogram. All solved by A_DTL with verified strategies (`oink -v`).
PATCHED build: copy tools/oink/src to a scratch dir; in dtl.cpp search_rec add `ENTER depth d` after the bitset declarations,
`EXIT depth d` before the `result == 0` return, and in the stable branch's Dom(V,R) loop (876-889, untraced in Oink) print
`X ∪= DomStable(V)` once and, per top, `domregion <pr> <top> <vertices newly added to X>`; build Debug as in notes item 6.

## 2. What tc+ does (DATA, complete picture; tc+ N = 4, 6, 8, 10)
- Every tangle is learned at depth 0, in the ONE stable piece of each search; the −1 pieces and the recursion learn nothing.
- Search 0 of a phase: pruning removes two distraction sets, then the −1 cut at the opponent's top level removes the opponent's
  half (recursion on it learns nothing), then the stable piece on the player's half learns the gadget tangles (one per
  gadget, priority 4) and the top's tangle (containing them all, 2N−1 first-piece tangles in the predecessor's count).
- Search s ≥ 1: the pieces are dis(gadget_N), dis(gadget_{N−1}), ..., dis(gadget_{k}), STABLE, dis(1), cut(opponent half): the
  number k of distraction pieces before the stable piece drops by ONE per search; the stable piece's R grows (+3, +4, +5, ...
  vertices, SUPERSET every time from search 1 on) and its V* exchanges the rescued gadget's chain tops for the next gadget's
  (+k, −k(k−1)/2: triangular). The rescued gadget's chain (priorities 4, 6, 8, ...) learns one tangle per level (N−1 of them)
  and the top's tangle grows by the gadget (a chain at the top: 84 ⊂ 87 ⊂ 91 ⊂ 96 ⊂ 102 at N = 6, escapes 25, 22, 18, 13, 7).
  Search 0's top tangle crosses the chain (it was computed after the cut, with the opponent's half forgiven; 16 of its vertices
  fall into the cut from search 1 on: head 'dom' → 'cut' DOWN, the predecessor's "later pieces are re-cut").
- So tangles(tc+ N) ≈ N (gadgets) × N (chain) + 2N (top) and searches = 2N + 2: the quadratic count in N is sublinear in n ≈ 17N².

## 3. Findings (DATA unless marked)
F0 (PROVED, reading). Lemma W: within one call of search(), every vertex extracts tangles as a top at most once. sptl (dtl.cpp
   528-529) runs extractTangles only `if (closed_region and !W[top])` and sets W[top]; W is reset only at the end of search()
   (1016, "already did tangle this iteration", dtl.hpp 75); extractTangles is called nowhere else (§1.5). Hence the tangles
   created in one search ≤ |{tops that extract}| ≤ |P_p ∩ G'| ≤ n, and tangles(G) ≤ n · (number of search calls). With D2(d)
   (calls ≤ tangles + dominions + 2) this is circular, but it makes the reduction exact: GAP-A ⇔ polynomially many searches.
   It also means "max tangles per (top, search)" = 1 (dtl_tops.py, true tops from the Debug trace: 1 on every game tested).
F1 (DEAD) Laminarity. The family of stored tangle sets is far from laminar: tc+ N = 6: 166 nested, 205 crossing, 1,282 disjoint
   pairs. So |T| ≤ 2n by laminarity is out.
F2 (CORRECTED 00:50Z) "tangles per top". dtl_tangle_family.py identifies a tangle's top as its max-(priority, id) vertex, which
   merges equal-priority tops: the "31 tangles at one top" of dtl_pertop31_n18.pg are 31 tangles at the priority-17 LEVEL, which
   has 8 tops; with true tops (dtl_tops.py, Debug trace) the maximum per top is 4 there and ≤ searches everywhere (Lemma W).
   Per-level counts: 31 (n = 18), 23 (n = 20), 28 (n = 24), 30 (n = 30), 30 (n = 40) from the --pertop climbs.
F3 (EXPLAINED by F0; the chain is across equal-priority tops) In-search chain. Within ONE search, the tangles learned at one
   LEVEL (as identified by dtl_tangle_family.py) form a strictly growing chain
   (each later one a strict superset of the previous). Checked on tc+, 13 families, L-RED's chain/ladder/counter_dftl, 3 random
   batches, and every climbed instance including the ones optimised against it (fitness --restart's second component counts
   chain breaks: 0 in 12 climbs of 3k–30k steps). Mechanism (dtl_pertop31_n18, top v17 with 8 equal-priority tops): the region
   set is fixed, the fresh tangle fires in the next sptl pass and brings its stored strategies, the DFS parents of the other
   vertices change, and the SCC of the top grows by ≥ 1 vertex per pass (escapes 13, 12, 10, 9, 8, 7, 5, 4). This is the
   predecessor's (a4) "str change at a fixed region set" — with the correction that each step is a DIFFERENT top of the same
   priority (8 tops of priority 17 at n = 18): pass 1 the highest learns t1; pass 2 the next top's region absorbs t1 (fires)
   plus itself and learns t2 ⊃ t1; and so on; each top extracts once (W). A climb with fitness = chain breaks found 0 in 12k–25k
   steps at n = 12, 16, 20, consistent with: a top's region in a later pass contains the previous top's tangle as a unit.
   Consequence: nothing beyond F0 (≤ 1 per top per search).
F4 (DEAD) (C-new): "every new tangle at a top contains a vertex that no earlier tangle at that top contains" (would give ≤ n per
   top). FALSE: 20 violations in dtl_pertop31_n18 (the chain restarts each search from a base inside the previous chain's union),
   and even the RESTART (first tangle of a top in a search) can be covered: dtl_restart8_n20 (11 restart violations, 1 strict
   shrink), dtl_restart7_n16 (9, all caused by a dominion: the search-2 tangles are the search-1 tangles minus the solved
   vertex; the deletion charge of DTL-proof.md §3(a) covers these).
F5 (DATA, 0 exceptions) First-call distance monotone. At the first best_vertices call of a search (R = G', the same across
   same-player searches without a dominion) the pruning round in which a vertex is pruned never decreases as T grows (tc+ N = 6:
   105 increases, 0 decreases over 12 pairs). But it is NOT a potential: on tc+ N = 6 searches 1–5 have identical distance
   profiles while each learns new tangles (the progress is in the later pieces).
F6 (DEAD) Per-vertex heads monotone across searches; first stable piece's R monotone. Heads move DOWN on tc+ ('dom' → 'cut',
   16 vertices at N = 4, 50 at N = 6, 112 at N = 8; 'dom' → 'dis' 6/10/14). R of the first stable piece is CROSS (+1 −58) on
   counter_symsi 12 between searches 0 and 1 (search 0's first stable piece is a 1-top piece after a 2-vertex cut; in search 1
   the cut at that place takes 56 vertices because the −1 set shrank from 11 tops to 1).
F7 (DATA) The −1 return set is not monotone even though distances are: tc+ N = 4 search 0 returns {v60, v28, v6} (the last
   survivors, round 8); search 1 returns {v3, v4, v5, v6, v14} (survive longer with more tangles) while v60, v28 are pruned
   before the end. So the first distraction piece, hence every later context, is re-cut.
F8 (DATA; the counter-shape candidate) Oscillation of a vertex's membership in a top's SCC across searches with NO dominion in
   between: dtl_restart8_n20, top v6 (pr 14): v13 ∈ SCC in search 0, ∉ in search 1, ∈ in searches 2–4; v16 likewise (out in
   1–2, back in 3). Mechanism from the patched trace: search 0's first −1 set is {v9, v4, v19} and the two cuts after it remove
   2 + 2 vertices; search 0's tangles rescue v9 and v19, so search 1's first −1 set is {v4}, X is smaller, the lowest level that
   attracts to X changes, the cut removes 1 vertex, fewer exits are forgiven in the stable piece, and v13, v16 become
   DISTRACTIONS (removed before the stable piece). In search 2 the new tangle at v6 (now containing v9) rescues v13; in search
   3 v16. RULE (reading): rescue(A) ⇒ A's attractor is no longer removed before the stable piece ⇒ fewer forgiven exits ⇒
   some B can regress to a distraction; regress(B) ⇒ B's attractor is removed earlier ⇒ more forgiven ⇒ some A' can be rescued.
   A flip-flop is possible in principle; it ends unless each configuration produces NEW tangle sets (duplicate check), i.e. it
   must be driven by a lower counter (TL's tc idea applied to distraction status instead of region membership).

F9 (DATA; the strongest counter-like behaviour found) dtl_searches20_n32.pg (climb --searches, n = 32): 20 searches, 124
   tangles, Even's phase 16 searches with ONE dominion at the very end; searches 6–12 and 14–15 learn nothing at depth 0 and
   everything in the RECURSION (the −1 cut of 25–26 vertices at depth 0 is searched recursively and learns there). Top v19
   (priority 28, Odd-owned) learns 12 tangles over 12 searches with sizes 3, 15, 14, 17, 19, 18, 12, 15, 9, 9, 10, 18 and
   escapes 24, 14, 15, 12, 10, 11, 17, 14, 20, 20, 19, 11: four vertices change membership FIVE times each (in, out, in, out,
   in, out; v17 pr 2, v16 pr 26, v13 pr 14, v4 pr 26, all Odd-owned). So neither the SCC, its size nor its escape count is
   monotone at a top across searches, and the oscillation is not a 2-cycle. P1 "every learning search adds a new (top, vertex)
   coverage pair" (would give ≤ n² searches) is DEAD here (8 violating searches) and in dtl_cnew14_n20 (search 3: v7's SCC
   shrinks from {7, 14, 15} to {7, 15} with no dominion in between).
   Searches vs n in the --searches climbs after 10k–25k steps: n = 16: 9; 24: 16; 32: 20; 48: 12 (7k steps); 64: 12 (3k steps).

F10 (DATA; the flip-flop made visible) Full event sequence of dtl_searches20_n32.pg (patched trace; dKmJ = best_vertices at depth
   K returned −1 with J tops, dKSJ = stable with J tops, cut@t/x = the −1 cut at threshold t of x vertices, TP:k = a tangle of
   priority P with k vertices). Searches 6–12 (Even, no dominion) have an IDENTICAL depth-0 prefix: dis 3 tops, cut@21 of 1
   vertex, cut@27 of 25–26 vertices, recursion on that cut. Inside (depth 1): dis 4–5 tops, cut@21 of 1, then the cut@25 whose
   size FLIPS: 2, 2, 18, 3, 5, 6, 17 (searches 6–12). Small cut ⇒ the depth-1 stable piece is large and learns a chain of 7–9
   tangles up to priority 24; large cut ⇒ a further recursion (depth 2, even 3) learns a different chain there. So the context in
   which the priority-24 top (v19) learns alternates between depth 1 (sets of size 15–19) and depth 2 (sizes 9–12), which is
   F9's oscillation. The flip is driven by the depth-1 −1 return set (4, 4, 5, 2, 2, 4, 4 tops) and the tangles, through the
   lowest level attracting to X and the size of its attractor. Every flip learns NEW sets because the tangle set has grown in
   between; the climbs could not push this beyond 20 searches at n = 32 (seeded continuation: 20 after 6k more steps), 21 at
   n = 40, 19 at n = 48, 17 at n = 64 (early).

## 4. Reduction of GAP-A (reading of the data; F0 proved)
tangles = Σ_τ Σ_searches (chain length of τ in that search) ≤ n · #(τ, search) pairs with a restart.
- (F3 to PROVE) chain length ≤ n: needs "within one search at one top the SCC only grows": within a piece the region set is
  fixed except for thefts by higher tops (a3) and fresh tangles only add str; the open point is the str change (a4).
- Restarts: a top restarts in a search iff its SCC differs from every stored set. Across searches the context of the piece is
  re-cut (F6, F7, F8), so Lemma D (2n+1 sets per top under R-mono) does not apply; the oscillation F8 shows membership is not
  monotone. So GAP-A ⇔ polynomially many searches per phase (each search without a dominion restarts ≥ 1 top).
- Searches per phase: tc+ 2N+2; climbs for searches (fitness --searches, n = 24, 32) reach 7–8 after 1k steps; the oscillation
  instance has 5. No family with superlinear searches is known (L-LIT T16; L-RED R8).

## 4b. The proof obstacle, stated (reading)
A search is a tree of best_vertices calls (contexts (R, X), depth ≤ d). For a fixed context, more tangles give monotone
regions (predecessor's (a3), R-mono for the vertex cases) and, by F5's data, monotone pruning distances. Two consecutive
searches of a phase agree on a prefix of this tree and diverge at the first call whose result differs (−1 set, stable set or
regions); on tc+ the divergence point moves one piece earlier per search, on dtl_searches20_n32 it stays at depth 1 while the
depth-1 cut flips. A lexicographic potential (distances at context 0, then at context 1, ...) is therefore monotone in the
sense "the first differing component increases", but lower components reset, and such a potential bounds the number of
searches only by the PRODUCT of the per-component ranges, exponential in the number of pieces. What is needed is a GLOBAL
budget that every divergence consumes (as thefts per vertex per level do within one context), or the counter that shows no
such budget exists. The author's own progress check (computeDistanceValues, dtl.cpp 553-639, run at trace ≥ 3 before and
after each search, with the `throw "nothing changed!"` commented out at 1061) is exactly the first-call distance of F5, and
it does not change on tc+ searches 1–5: the author met the same obstacle.

## 4c. Fixed-context monotonicity (M) and the nested-epoch structure (DATA + reading, 01:15Z)
dtl_contexts.py (patched trace with distance lines): every depth-0 best_vertices call is recorded with its context R (unsolved
minus removed so far in the search); calls with the same (player, R) in different searches are compared in search order.
| game | depth-0 calls | recurring contexts | consecutive pairs | distance up / DOWN | stable→−1 | −1→stable | −1 set changed | stable V* gained / LOST |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tc+ N = 6 | 60 | 12 | 43 | 329 / 0 | 0 | 10 | 1 | 0 / 0 |
| dtl_searches20_n32 | 75 | 19 | 47 | 120 / 0 | 0 | 4 | 14 | 0 / 0 |
| dtl_searches15_n24 | 63 | 12 | 38 | 58 / 0 | 0 | 3 | 7 | 0 / 0 |
| r2_n32 best (23 searches) | 85 | 18 | 53 | 83 / 0 | 0 | 4 | 10 | 0 / 0 |
| dtl_cnew14_n20, dtl_restart8_n20, counter_symsi 12 | 37, 20, 32 | 12, 3, 1 | 20, 8, 2 | 40, 13, 5 / 0 | 0 | 5, 1, 1 | 1, 3, 1 | 0 / 0 |
(M) at a FIXED context, as T grows: pruning distances never decrease, a stable result never reverts to −1, a stable V* is the
same set every time the context recurs; a −1 return set changes only together with a distance increase. This is the
fixed-context monotonicity the predecessor's (a3)/R-mono give for regions, extended to the pruning; the vertex cases follow
the same R-mono induction (more tangles ⇒ bigger regions and A_t ⇒ more rescues at every round, given V-monotonicity of one
round, which N5 shows can fail with straddling tangles; measured never).
Consequence (reading). Two consecutive same-player searches share the context C_0 = G' (no dominion between). By (M) the
result at C_0 changes at most n(n+1) + 1 times in the phase (each change raises a distance; ≤ n+1 rounds). While it is
fixed, the next context C_1 = C_0 \ Dom(V_0) shrinks monotonically in T (Dom grows: ≤ n times) and its result changes
≤ n² times per fixed C_1; and so on down the depth-0 pieces and into the recursion. So the searches of a phase form NESTED
EPOCHS: an epoch of piece k is a maximal run of searches with the same results at pieces 0..k; inside it piece k+1 can change
O(n²) times; when piece k changes, piece k+1's context is a NEW set (the −1 return set changed arbitrarily, F7) and its
counter restarts. The bound this gives is Π_k O(n²) over the pieces, exponential; a polynomial bound needs a budget that a
change at piece k+1 consumes GLOBALLY (independent of the epoch of piece k); none of the measured quantities is one (§5).
NESTED contexts are NOT monotone (01:30Z, dtl_contexts.py second line): comparing a later same-player call whose remaining set
R' is a strict subset of an earlier call's R (more removed, more forgiven, more tangles): distances on R' go DOWN (tc+ N = 6:
0 of 17,337; dtl_searches20_n32: 54 of 3,270; r2_n32 best: 134 of 3,590; dtl_cnew14_n20: 39 of 144) and a stable call
reverts to −1 at the smaller context (42 pairs on tc+ N = 6, 9 on dtl_cnew14_n20; stable V* ∩ R' is never lost). Reason: the
removed vertices can be the witnesses of the good paths (lower regions, rescue paths). So the predecessor's hope "R-mono for
later pieces" is false as a statement about the pruning, and monotonicity lives ONLY at identical contexts.
Proof status of (M) = Claims P, Q (DTL-proof.md §3(a) Lemma P/Q, SKETCH): the induction over rounds goes through except for one
case: a p-priority vertex pruned in an early round and later re-absorbed through a tangle that straddles under the larger
tangle set, stranding a deadlocked remainder whose p-parity maximum is no longer a top. Everything else (vertex rules,
non-straddling tangles, candidates, rescues, and the pickup of a stranded remainder by its own p-parity maximum when that is a
top) is written out. The climb dtl_pclimb.py targets exactly this violation (patched build; fitness = P violations at
identical contexts).
Hand attempt at a Claim-P violation (02:20Z–03:00Z, experiments/alg/instances/dtl_pviol_attempt1.pg, 26 vertices, labels
t1/t2/tau/a/mstar/o/c/x/w/o2/r0-r3/o_k/y_k): a straddling tangle t = {tau, a, mstar, o, c} (cycles tau-a-mstar-o, a-mstar-o,
c-o; escape h into t2's region), a stealing chain g_0..g_3 of two-vertex tangles {r_k, o_k} whose escapes y_{k-1} (Even-owned,
priority just above r_k so that r_k's own region cannot take them) enter t1's region only after g_{k-1} fires there, the
witness w with tangle {w, o2} (escape r_3) that pulls a into t1's region, and x (priority 6) → mstar (7) as the rescue
witness to be stranded. Designed timeline: g_k learned one search after g_{k-1}; a stolen in search 4; x survives round 1 in
searches 1-3 and is pruned at round 1 in search 4. What A_DTL did: (i) t1 → c and t2 → r_0 (added so that t1, t2 are not
candidates) let t1's region absorb c → o → tau → ... and t2 via r_0, closing t1 into a DOMINION in search 0; (ii) the ladder
collapsed inside search 0: once a level is learned and removed by Dom, the next level's y is "the lowest level attracting to
X" and the −1 cut forgives it, the following level closes in the next piece, and so on — every level is learned in search 0.
Lesson (reading): within one search every piece sees all tangles learned in earlier pieces, so a cross-search delay exists
only when the enabling tangle is needed in an EARLIER piece than the one where it is learned; concretely, the top to be
rescued must have been REMOVED in a −1 (dis) piece before the stable piece that learns the enabling tangle. That is tc+'s
order (dis(gadget N) ... dis(gadget k), STABLE): the distractions with the highest pruning distance are removed first, one
dis piece each, and only then the stable piece learns. A P-violation (and a counter) must reproduce this removal order for
its delay stage; the pruned-but-not-removed vertices of a stable first call do not delay anything.
What a counter must do (the shape for L-RED): K "digits" = K nested pieces, each able to cycle through ≥ 2 results inside a
fixed epoch of the pieces above it, each cycle step learning a new tangle, and a change at piece k resetting piece k+1's
context to one where its cycle restarts with NEW sets (because T grew). dtl_searches20_n32.pg is a one-digit instance:
searches 6–12 keep the depth-0 results fixed (dis 3, cut@21/1, cut@27/25–26) while the depth-1 cut flips 2, 2, 18, 3, 5, 6,
17 (F10); searches 13–15 are a second epoch. The climbs (random mutations, fitness = searches) reach 0.7n searches at n = 16
and 32 and do not stack digits by themselves; a construction is needed.

## 5. Dead ends this box (with the instance)
| conjecture | killed by |
| --- | --- |
| tangle sets laminar | tc+ N = 4 (67 crossing pairs) |
| ≤ n tangles per top | dtl_pertop31_n18.pg |
| (C-new) new vertex per tangle at a top | dtl_pertop31_n18.pg (20), dtl_restart8_n20.pg (restarts) |
| heads non-decreasing across searches | tc+ N = 4 ('dom' 28 → 'cut' 27, 16 vertices) |
| first stable piece's R non-decreasing | counter_symsi 12 (search 0 → 1: +1 −58) |
| −1 return set monotone in T | tc+ N = 4 search 0 → 1 |
| first-call distance profile as a potential | tc+ N = 6: constant over searches 1–5 |
| P1: every learning search adds a new (top, vertex) coverage pair (searches ≤ n²) | dtl_cnew14_n20.pg search 3; dtl_searches20_n32.pg (8 searches) |
| per-top escape count or SCC size monotone across searches | dtl_searches20_n32.pg top v19 |
| pruning monotone across NESTED contexts (R' ⊂ R, more T) | tc+ N = 6: 42 stable→−1 reverts; r2_n32 best: 134 distance decreases |

## 6. Box summary (03:30Z)
PROVED: Lemma W (tangles ≤ n · searches); Lemma 1.5a (one reachable SCC). SKETCH: Lemma P/Q, one open case. DATA: F0–F10, (M)
at identical contexts (0 violations), nested contexts not monotone, oscillation depth 5 at n = 32, 20–23 searches at n = 32
(climbs), composition 2/3/4 copies → 30/30/35 searches. DEAD: §5 table. OPEN: a global budget for piece changes, or the
counter (removal-order delay device; L-RED R9 builds the two-level version). The box produced no result in the sense of
CLAUDE.md (nothing refereed), and GAP-A stays open with a sharper statement: the number of search calls per phase.
