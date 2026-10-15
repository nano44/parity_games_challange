# R8: DTL (Oink's distance tangle learning, van Dijk's research solver) as a target (L-RED, 2026-10-15)

Lead's ask (15:06Z, 6 h): build a family on which DTL's learned-tangle count or total work is super-polynomial; first the
invariant DTL maintains (the analogue of R3's Lemma D), then the exact construction requirement, then a counter. Materials:
L-ALG's line-mapped pseudocode (claude/l-alg 898d02d, docs/alg/candidates/C5-DTL.md) and attack verdict (549bb34: every
tc/tc+ variant polynomial). Source read here: tools/oink/src/src/solvers/dtl.cpp @ 8fbf0a7 (best_vertices 643-776,
search_rec 834-994, search/run 997-1161; attractVertices 65-101, attractTangle 109-185, extractTangles 210-471, sptl
476-546, against L-ALG's transcription, which is accurate). Binary: tools/oink/build/oink --dtl --no-single --no-wcwc;
the release build still prints "best vertices", "distance k" and "new tangle ... with k escape vertices" at -t -t, enough
to see every tangle (vertex set, Even's strategy, escapes) and every pruning round.

Flags. Every Oink run in this report before 16:02Z used `--dtl --no-single --no-wcwc` (no single-parity / winner-controlled
preprocessing) but NOT `--no-loops`, so Oink's parser dropped losing self-loops that are not a vertex's only edge and
solveSelfloops ran before DTL (CHECKER C3, Lead 16:02Z: the pinned algorithm is now `oink --dtl --no-single --no-wcwc
--no-loops`). Section 8 re-runs the probes with --no-loops; the families of sections 2 and 6 have no self-loops except
where stated, so their counts are unaffected (spot checks in section 8).

## Verdict: HELD. No killer built; the invariant says DTL has no reset, and the one non-monotone ingredient (theft of a tangle's vertex by a higher region) is spent once per vertex per level
Every tangle DTL learns is a new bottom SCC of a region; across Even's searches the tangle set only grows and every
attractor, the pruning's surviving set, every region head and every tangle's usability (except by theft) are monotone in
it (section 1). So a tangle set can never be re-learned and a distraction never comes back: the TC resets have no
analogue. The free search over small games finds only the chain mechanism (one tangle per top per sptl pass, relearned
with one more vertex per search: O(n^2)), two-player optima are the same chains with Even's vertices passive, and a
census of 19,000 games finds Even's attractor strategy changing between two tangles only by theft, once per vertex and
top (section 2). What a killer would need is stated in section 3.

## 1. The invariant: during one player's search phase everything DTL computes is monotone in the tangle set (Lemma M)
Fix the player p = Even (run() searches Even to exhaustion, then Odd; the two phases never alternate, so during Even's
phase the only state that changes between searches is the set T of Even tangles, which only grows, and G, which only
shrinks when an Even dominion is solved). Write A_T(Z, R, t) for the tangle attractor to Z within R with threshold t
(attractVertices + attractTangles). Then, with T subset of T':
- (M1) A_T(Z, R, t) subset of A_T'(Z, R, t) for all Z, R, t: attractTangle only adds vertices and never blocks a vertex
  attraction (attractVertices runs first on every pop; a tangle is attracted iff all its escapes are in Z or outside R,
  and more tangles never un-satisfy that).
- (M2) [Corrected 17:30Z per the proof lane's NOTE N5 (claude/l-alg 6bb5d43, DTL-proof.md section 1.6): the one-round
  operator is NOT monotone in general (a straddling stored tangle whose top is taken by a new top's region can un-attract
  its lower part), so "greatest fixpoint" is wrong; what the code computes is the descending iteration of that operator
  from V = all p-priority vertices, and monotonicity in T across searches is exactly the proof lane's open step (r1),
  tested empirically in section 12.] The pruning of best_vertices is a greatest fixpoint: V* = the largest V such that every v in V can step into
  A_T(Reg_T(V), R, t) for some t < pr(v) (lines 711-741), where Reg_T(V) = the union of the DISJOINT regions of the tops
  of V, computed top-down from one copy CurR = R (line 690) that each top's attraction consumes (lines 691-706; restated
  16:15Z after the Lead's check; the union is still monotone in T because a vertex that a lower top loses is held by the
  higher top that took it). The operator is monotone in V and, by (M1), pointwise increasing in T; so V*_T subset of V*_T'.
  Pruned vertices ("distractions") are never heads of regions and no tangle is ever learned from them.
- (M3) Region heads move only upward: the head of a vertex (the top whose region takes it, tops processed in descending
  priority with R consumed) is a monotone function of T: a higher top's region can only grow (M1), so a vertex can be
  stolen by a higher top but never returned to a lower one. The same holds for the remainder levels (after Dom(V,R) -> X
  the next best_vertices runs on a smaller R, edges into X are ignored = safe, both monotone) and for the recursion of
  search_rec on Z (an attractor with threshold, monotone in T).
- (M4) A tangle's usability in a region is monotone except for theft: attractTangle fails only if an escape is in R \ Z
  (becomes satisfied as Z grows, never unsatisfied), a vertex has priority > maxpr (static), or a vertex is outside R (it
  was taken by a higher region: by (M3) this happens once per vertex per level and is never undone).
Consequences. (a) DTL has no reset: nothing learned is ever un-learned or re-learned (a tangle with a known vertex set
is skipped, extractTangles 385-424), a head never falls, a distraction never comes back. This is the exact opposite of
tangle learning's tc mechanism, in which the opponent's new tangle at a high priority removes the lower regions and
makes their tangles be re-learned with a new vertex set; in dtl the opponent has no tangles during Even's phase at all.
(b) A new tangle needs a new bottom SCC under Even's attractor strategy; with the vertex set of a region changing only
by thefts and growth (M3), a new SCC at the same top needs either a region change (at most n per level per top, since
each vertex enters or leaves a top's region at most once per level) or a change of Even's strategy str inside the region
with the same vertex set.
(d) Influence runs upward only (the analogue of R3's Lemma D). A tangle learned at head v consists of vertices of v's
region; by (M3) those vertices belong, in every later pass and search, to the region of v or of a higher head, so the
tangle can be attracted only in regions of heads at or above v (a lower head never sees its vertices in R), in the
pruning's attractors, and in later levels (the remainder after Dom(V,R) -> X and the recursion). So a tangle never
changes the regions below its own head: the downward influences that a counter needs (a higher event resetting lower
levels) are X (grows within a search), V* (M2) and thefts (M3), all monotone. In tc the downward influence is the
opponent's tangle at a higher priority, renewable because the opponent learns between the player's searches; dtl has no
opponent during a phase, and idtl's opponent tangles are never attracted for the player (parity check, attractTangle 113),
so they act only through G.
(c) [WITHDRAWN 16:15Z, see section 9: Oink's uintqueue is a STACK (uintqueue.hpp:72-74 pop returns queue[--pointer]),
so every attractor in dtl.cpp is depth-first, not breadth-first; the layer argument below does not apply. Kept as
written for the record.] Even's strategy str[u] is set by the FIFO attractor: str[u] := the first popped successor of u (attractVertices 80), or
the strategy of the first tangle that attracts u (attractTangle 170-180; vertices are popped in insertion order, and in one
pop the predecessors of the popped vertex come first, in Oink's edge-list order, then the tangles of tin[v] in creation
order). So str[u] changes only when the relative order of two attraction events changes. Under (M1)-(M4) the BFS layer
of every attraction event is non-increasing in T (every rule that fires keeps firing, thefts only remove escape
obligations) and a tangle event moves earlier or dies (M4); a flip of str[u] therefore needs one of: a layer crossing
(the later event's layer drops below the other's: at most as many as there are layers, per pair), a theft (disables a
tangle event; at most once per vertex per level), or a reorder inside one layer with the same pushers (impossible: the
within-layer order is the lexicographic order of the pusher chains, fixed by Oink's edge lists and tangle creation order,
and changes only when a pusher changes, which is again a layer or theft event).
Lead reading of (c): every strategy flip spends a theft or a layer crossing, or a lexicographic decrease of the pusher
chain. Thefts and crossings have polynomial budgets. The pusher chain is a tuple of (layer, slot) entries of length up to
n, and a lexicographically descending sequence of such tuples can be exponentially long, so (c) alone does NOT give a
polynomial bound; what closes it is (d): a chain changes only when a new vertex or tangle enters the region earlier, and
by (d) a new tangle enters only regions above its head, so the chain changes at a fixed head are driven by events below
it that are themselves monotone (vertices entering once per level, tangles learned below). A counter would need the
chain at one head to descend exponentially often, fed by exponentially many new tangles below it, which is the same
question one level down: the recursion bottoms out at the lowest head, whose region changes only by vertices entering
(polynomial). Not a proof (the induction over heads has to handle tangles whose vertices are all lower than their head
and the remainder levels), but the shape of the obstruction.

## 2. Evidence
- Strategy flips are thefts, once per vertex and top. Census (experiments/red/dtl/dtl_flips.py: every learned tangle's
  Even strategies from the -t -t trace, per Even vertex the sequence of its strategy in successive tangles): 9,000 random
  games (n = 8, 12, 16; at most 5 tangles each): 0 flips. 10,000 games on random walks from the many-tangle games (4,000
  from the n = 24 optimum, 4,000 from the two-player n = 20 optimum, 2,000 from tc+ N = 3): 6 games with a flip, all on
  the tc+ walk, at most 2 flips per vertex and never 2 at the same top. The one examined (scratchpad dtl/flip_walktcp.pg):
  Even-0-T (2/1) uses 4/1 in the top-4 tangles of searches 0 and 1 and 5/1 in search 2, because 4/1 was taken by the
  top-22 region in search 2 (it appears in that region's tangle of the same search); 10/1 switches 0/1 -> 9/1 once when
  0/1 leaves its region. Both are (M3)/(M4) thefts; no vertex ever returns to an earlier strategy at the same top.
- Strategy flips never happen on the standard families. From the -t -t traces (every learned tangle with Even's strategy on each of
  its vertices), per Even vertex the strategy used in successive tangles containing it: tc N = 4 (9 tangles, 24 Even
  vertices with a strategy), tc+ N = 3 (17 tangles), the evolved two-player games below (26, 31 tangles): 0 flips, every
  vertex uses one successor in all its tangles (scratchpad dtl/flips.py). So every new tangle in every run seen is a region
  change, never a strategy change.
- What the free search finds is the chain mechanism. Hill-climb over small games (experiments/red/dtl/dtl_search.py,
  fitness = DTL's tangle count, mutations add/remove edge, change priority, flip owner; 30,000-60,000 steps):
  | n | 10 | 14 | 18 | 24 | 30 | 16 (>= 40% Even-owned) | 20 (>= 40% Even-owned) |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | best tangle count | 8 | 11 | 35 | 56 | 27 | 26 | 31 |
  | Even searches / Odd searches | 1/1 | 2/1 | 4/3 | 3/0 | 2/1 | 3/3 | 3/3 |
  The n = 24 optimum is a ONE-player game (all 24 vertices Odd-owned, dense, 22 even priorities): each sptl pass extends
  one tangle by the next top (tangles {1,3}, {1,3,4}, {1,3,4,6,7}, ... up to 19 vertices: a chain of 19 tangles in one
  search), and the next search relearns the chain with one more vertex at the bottom (0, then 2 and 5) after that vertex
  stops being a distraction (its escapes fall into X); 3 searches x ~19 = 56. The hand-built chain family
  (gens_dtl.py chain n: Odd-owned, priorities 2..2n, i -> j for all j <= i+1) gives exactly n - 2 tangles in one search
  (n = 5..80). With at most one extraction per top per search (W, sptl 514-519) and at most n rescues (M2), this mechanism
  is O(n^2) tangles; the searches never found anything else (the two-player optima are the same chains, Even's vertices
  passive: 0 strategy flips).
- idtl (interleaved) learns the same counts on all of these (8, 11, 35, 56, 27, 26, 31; tc+ 3: 18 vs 17).
- Completeness probe: hill-climb with fitness = number of vertices DTL leaves unsolved (run() ends when Odd's phase
  finds nothing, the NDEBUG check is compiled out): no game with an unsolved vertex found (n = 8 and 12, 60,000 mutations each, best fitness stayed 0; L-ALG's
  dtl_check already covers 60,000 random and all canonical n <= 3 games). DTL is complete on everything seen.
- L-ALG's data (549bb34) are the other half: tc 2N+1, tc+ ~1.4 N^2, every template GA quadratic.

## 3. What a killer needs (the construction requirement)
By section 1 a super-polynomial tangle count needs exponentially many distinct bottom SCCs at some top across Even's
searches, with the tangle set only growing. Region changes are O(n) per top per level (M3), so the SCCs must differ by
Even's attractor strategy: some Even vertex u inside a stable region must alternate str[u] between two successors a and b
exponentially often, each alternation producing a new SCC (a's branch in, b's branch out, and back). Under (M1)-(M4) an
alternation a -> b -> a needs b's attraction event to move before a's and then a's before b's again; a tangle event can
only move earlier (M4, escapes covered) or die (theft), a vertex event's layer only decreases, and the within-layer order
is fixed by the pusher chains. So the requirement is: an attraction-event order that reverses exponentially often while
every event's layer is non-increasing and every tangle's usability is monotone-then-dead. A reversal can be bought by a
theft (the b-tangle loses a vertex to a higher region, str[u] returns to a) followed by a NEW b-tangle (a different vertex
set containing b, learned elsewhere) that is attracted earlier than a; each such cycle costs one theft (budget O(n^2) per
level, (M3)) and one new tangle that itself has to come from the same mechanism one level down. A counter built this way
has levels that consume thefts, and thefts are not renewable: that is the obstruction, and the reason the resets of tc
(renewable because the opponent's tangles arrive between Even's searches) have no analogue in dtl. In idtl the opponent's
tangles do arrive between searches, but an opponent tangle is never attracted for Even (attractTangle checks parity), so
it changes Even's attractors only through G (solved vertices) and the same monotonicity holds per phase.
Sharp open statement. Is there a family of parity games on which Oink's DTL (release path of dtl.cpp @ 8fbf0a7) learns
2^{Omega(n^c)} tangles? Equivalently: can the FIFO attractor's event order at one Even vertex reverse super-polynomially
often across searches although every attraction rule is monotone in the tangle set and every theft is permanent? L-RED's
answer in this box: no construction found and the potential argument of section 1(c) says none exists; the step that a
proof must nail down is the pusher-chain order (section 1(c), last item), which is where an index-dependent tie order
hides, exactly as in R7's S5.

## 5. The Lead's four weak points of Lemma M (15:35Z) and the TC-variant question (15:38Z)
(a) FIFO pusher-chain order at one Even vertex. The pop order of a region is the lexicographic order of pusher chains,
where a vertex event's chain is (chain of the pusher, slot of the vertex in the pusher's predecessor list) and a tangle
event's chain is (chain of the escape popped last, slot of the tangle in tin[escape] = creation order, slot of the vertex
in the tangle's stored list). A new tangle is appended after all older tangles of the same escape, so at the SAME pop an
older usable tangle always pushes first; a newer tangle can only push earlier by firing at an EARLIER pop (its last escape
popped earlier). Across passes every firing moves earlier or dies (M4) and every vertex event moves earlier (M1), so the
pair order (a before b, b before a) at a choice vertex u can reverse only when the later event overtakes, i.e. the
lexicographic minimum of the two chains strictly decreases. Lexicographic descents over tuples of length up to n are NOT
polynomially bounded in general; what bounds them here is that every chain change is caused by an event: a vertex joins
the region (once per vertex per level), a lower tangle is absorbed (its vertices change head, once per vertex per level,
M3), or a tangle of the same head fires before its own vertices are reached (then it pushes them with the strategy it was
learned with, which is the strategy of this very region at the time, so by itself it reproduces the SCC it came from; it
changes the SCC only through vertices OUTSIDE it whose earliest successor is now inside it, a change that is one-way:
nothing pushes those successors later again). The one open step for a proof: the same-head self-firing chain (a tangle
pushed earlier changes outside vertices' choices, which makes a new SCC, which is a new tangle, which fires at a different
escape ...); I argue it is short because each round only moves events earlier and the within-tangle push order is fixed
at learning time, but it is the step to nail. Targeted search for it: fitness = max number of tangles learned at ONE top
(injective priorities so the tangle priority names the top), hill-climbs at n = 12, 16, 20 (40,000 mutations each; fitness = max tangles at one top, and = max at one top
within one search) stayed at 1-3. On the many-tangle games of sections 2 and 6 (traces, top identified by the tangle's
priority, so several tops of equal priority may be merged): max tangles at one top priority within ONE search is 1-3
everywhere (chain 40: 1; evolved n = 24: 2; tc+ 3: 1; the three perturbed counters: 3), and across searches at most
18 (pert_dftl6, 13 searches): one new SCC per top per search, never a self-firing chain within a search.
(b) Phase alternation. dtl never returns to a player's phase (run 1123-1136: Even until search(0) fails, then Odd until
search(1) fails, then stop); so Even's tangle set is frozen when Odd starts, and nothing of Even's is renewed. idtl
alternates, but the opponent's tangles are never attracted for the player (attractTangle 113 checks tpr mod 2 = player),
so between two Even searches the only change caused by Odd is G shrinking by Odd's dominion (at most n vertices in
total) and the deletion of Even tangles that contain a solved vertex (at most |T| events, each the death of a tangle,
never a rebirth). Removal of a solved vertex makes attraction EASIER elsewhere (edges to solved vertices are ignored,
attractVertices 84-86), so for the surviving vertices (M1)-(M3) continue to hold across the removal except for the deleted
tangles, whose loss is a one-time event. Nothing becomes renewable: a renewable theft would need a region to shrink
repeatedly, and a region shrinks only when R shrinks (solved vertices, at most n times) or a rule dies (tangle deletion,
at most once per tangle). Theft "once per vertex per level" holds across phases because heads move only up within a
phase and a phase change only removes vertices.
(c) Subgame removal between iterations within a phase (Even dominion found by search(0), G shrinks, next search(0)):
same as (b): attraction on the remaining G is monotone in T and in the removal, the deleted tangles are the only loss,
and each loss is final. "No reset" survives: a vertex set learned before cannot be learned again (dedup is global and
tangles are deleted only when a vertex is solved, i.e. gone from G for good).
(d) Work per tangle. Measured on Oink (release, --no-single --no-wcwc): chain n = 50, 100, 200, 400, 800: 48..798
tangles, 0.0006, 0.002, 0.021, 0.10, 0.81 s (~n^2.6 total, ~n^1.6 per tangle); tc N = 4..20 (n = 68..1300): 9..41
tangles, pruning rounds that removed something 669, 4195, 12889, 29055, 54997 (~n^1.5), 0.003 .. 13.7 s (~n^2.9 total).
By the code: one best_vertices call is at most n rounds, each a region computation plus d threshold attractors, each
attractor O(m + sum of tangle sizes); one search_rec call runs at most n + (recursion depth) iterations; searches are at
most tangles + dominions. So total work is polynomial in n times the number of tangles, and the tangle count is the
whole question. Nothing in the measurements grows faster than n^3.
TC-variant question (15:38Z): "how would a TC game have to change to give DTL a renewable theft". In tc the renewable
event is the opponent's tangle learned at a high priority between the player's iterations: in tl's two-sided
decomposition that tangle's attractor removes the player's lower regions, their vertices fall out, and the player relearns
them with new vertex sets. A theft in DTL is a vertex moving to a higher head of the SAME player (M3); for it to be
renewable the vertex would have to move down again, i.e. the higher region would have to lose it, which needs a rule to
disappear or R to shrink; the opponent has no rule inside search(player) (attractVertices/attractTangles are called with
the player only, best_vertices 643-776 and sptl 476-546 never run the opponent's attractor; the only opponent attractor is
the one-step removal of the threshold vertices in search_rec 946-950, inside Z, before the recursion). So no TC variant
gives DTL a renewable theft: the part of Lemma M that rules it out is (M1)+(M3), one-sided attraction with the opponent
absent during a phase. The "different version of the TC game" van Dijk's slides mention would have to attack ptl/rtl's
two-sided decompositions, not dtl's; for dtl the only opponent action is the dominion removal, at most n events.

## 6. Oink's dftl branch: counter_dftl and counter_odftl (Lead 15:45Z, L-LIT T16)
Built from github trolando/oink branch dftl (tip ea51834, 2024-06; worktree + cmake in the scratchpad, same flags as
scripts/setup_oink.sh) with src/tools/counter_dftl.cpp restored from a028e62 (it is deleted at the tip) and the branch's
counter_odftl.cpp (d54dfad). Both generators transcribed to experiments/red/dtl/gens_dtl.py (counter_dftl n,
counter_odftl n; row-identical to the built generators' output at N = 3, 6; only the "parity K;" header differs). Pinned
8fbf0a7 --dtl / --idtl with -v (Oink verifies the solution) on N = 1..20, and the branch build's --dftl, --odftl, --dtl on
N = 1..12:
| N | counter_dftl: dtl = idtl tangles (iterations) | dftl (tip) | odftl | counter_odftl: dtl = idtl | dftl (tip) | odftl tangles (iterations) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 5 (2) | 4 | 4 | 5 (2) | 5 | 6 (2) |
| 2 | 7 (2) | 6 | 6 | 7 (2) | 8 | 14 (4) |
| 3 | 9 (2) | 8 | 8 | 9 (2) | 11 | 28 (7) |
| 4 | 11 (2) | 10 | 10 | 11 (2) | 14 | 52 (11) |
| 6 | 15 (2) | 14 | 14 | 15 (2) | 20 | 158 (26) |
| 8 | 19 (2) | 18 | 18 | 19 (2) | 26 | 470 (62) |
| 10 | 23 (2) | 22 | 22 | 23 (2) | 32 | 1352 (146) |
| 12 | 27 (2) | 26 | 26 | 27 (2) | 38 | 3770 (349), 2.2 s |
| 16, 20 | 35, 43 (2) | | | 35, 43 (2) | | |
Every run "solution verified", all vertices solved, dtl wall time below 10 ms at N = 20. DTL learns exactly 2N + 3
tangles in 2 iterations on both families (idtl the same); it is neither wrong nor super-polynomial here. ODFTL
(one-player distraction-free TL, the a028e62 algorithm kept under that name at the tip) is exponential on counter_odftl
(iterations 2, 4, 7, 11, 17, 26, 41, 62, 97, 146, ..., 349 at N = 12: ratio ~1.5-1.6, Fibonacci-like) and linear on
counter_dftl; the tip's two-player DFTL is linear on both (1 iteration). The ORIGINAL solver at a028e62 (built separately: worktree oink-a028, its own CMake) on counter_dftl: tangles
6, 14, 28, 52, 92, 158, 266, 442, 728, 1192, 3162 and iterations 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 610 for
N = 1..10, 12: the iteration counts are exactly the Fibonacci numbers F_{N+3}, so the 2021 counterexample is a
Fibonacci counter (growth 1.618^N), verified at every N. So the branch's counterexamples are the pairs (a028e62 DFTL,
counter_dftl) and (ODFTL at the tip, counter_odftl), as the fix commit d54dfad says ("Fix counter_odftl to have a tiny
tangle of the opponent after the distraction"); the tip's two-player DFTL is linear on both.
What the generators are built to break (dftl.cpp header, branch tip lines 19-48, read): DFTL's loop takes V = all
p-priority vertices, decomposes into regions headed by V top-down, learns tangles in closed regions, and "if no region is
closed, we assume that 'surely' the lowest top vertex is distracting, so we remove that vertex from V"; V is reset at
every iteration. The generator (comments in counter_odftl.cpp): an Odd dominion (top 0, "first [distracted] tangle" 1,
barrier 2, second tangle 3/4), Even's "distracted vertex" 5 / "distraction" 6 / "dominant" 7, and per level i two
Even-owned distracted vertices of even priority piv - 2i (edges to the two Odd tangles and to the level's distraction),
a distraction of even priority piv + 8 + 2i whose only way on is the level's dominant vertex of odd priority one higher,
behind a tiny Odd tangle of priority 1 (d54dfad). The high even distractions head the top regions and are never closed;
DFTL therefore removes the LOWEST tops (the distracted vertices) one at a time, the regions re-form with one vertex less,
and V is reset at the next iteration: the removals are relearned in every iteration with a different vertex set, the
Fibonacci-like growth. DTL's pruning is the opposite design: a distraction is a p-vertex with no good path (the high
distractions here, whose only continuation is a higher Odd priority, are pruned at the first round), the surviving set is
a greatest fixpoint, monotone across searches (M2), never reset. The author's own counterexample thus attacks exactly
the ingredient DTL replaced, and in Lemma M's terms it is (M2) that makes it harmless: on these families dtl's V* is
stable after one pruning and the 2N + 3 tangles are the Odd tangles' per-level copies learned once each.
Perturbation searches under dtl (fitness = tangles, single mutations: edges, priorities, owners; flags --no-single
--no-wcwc): from counter_dftl N = 6 (32 vertices): 100 tangles (from 15); from counter_odftl N = 6 (44 vertices):
154 (from 15; the largest ratio seen, 3.5 per vertex, 21 searches); from tc+ N = 3 (54 vertices): 92 (from 17). Two to three tangles per vertex, the chain shape again
(the perturbed counters: 14-21 searches, at most 3 tangles at one top priority within a search, at most 16 at one top
across searches; tangle sizes up to 41-49 of the vertices: nested chains). Fitness = unsolved vertices from
counter_odftl N = 6 (40,000 mutations): nothing unsolved.
Other games on the branch: none (the branch's diff against 8fbf0a7 is the solver, the two generators, CMake and README).

## 7. The universal-tree angle (Lead 15:50Z: van Dijk's ISoLA 2024 closing slide, "learning tangles moves vertices along the universal tree")
(b)-answer, Lead reading. DTL's state is a set of tangles (vertex sets with a strategy), not a labelling of vertices by
positions in a tree, and nothing in dtl.cpp compares or lifts per-vertex values: regions are attractors over the whole
subgame, a tangle is used as a unit, and the dedup is by vertex set. So the quasi-polynomial universal-tree lower bounds
(Czerwinski et al. 2019, for separating automata / per-vertex monotone labellings read along paths) do not transfer by
any reduction I can state: a bottom SCC is not a tree position, and DTL solves tc, which the progress-measure solvers
in Oink treat as quasi-polynomial, with 2N + 1 tangles. Where a tuple order DOES appear in DTL is section 5(a): the pop
order of a region is the lexicographic order of pusher chains, tuples of (layer, slot) of length up to n, and every
strategy change at a vertex is a lexicographic descent of such a tuple. A proof of the tangle bound will have to count
those descents, and that count has exactly the shape of a universal-tree argument (how many times can a tuple of
length d over [n] decrease lexicographically when each decrease is caused by one of polynomially many events?); if the
events can be chained, the count could be n^{O(log n)} rather than polynomial, which would make DTL quasi-polynomial
in the tangle count without being a universal-tree walker in the separating-automaton sense. (a)-answer: no family was
built that forces DTL along a tree; the search for self-firing chains at one head (section 5(a)) is the attempt.

## 8. Re-runs with --no-loops and self-loop-biased mutations (Lead 16:02Z)
Flags `--dtl --no-single --no-wcwc --no-loops` (the pinned algorithm), mutations biased toward self-loops (30%: add or
remove a self-loop, never leaving a vertex without successors) and toward swapping the ids of two equal-priority vertices
(15%: the tie order of Oink's sort), the rest as before.
- Spot checks of earlier counts with --no-loops: chain 40: 39 tangles (38 before: the chain family has self-loops), tc 4: 9,
  tc+ 3: 17, evolved n = 24 (12 self-loops): 57 (56 before), counter_odftl 4, 8: 11, 19; all "solution verified".
- Correctness (fitness = Oink's verifier failing, a solver error, or an unsolved vertex; 40,000 mutations each): n = 12,
  16, 24: best fitness stayed 0 in all three runs: no wrong answer, no unsolved vertex, no error, with self-loops and
  renumbering in play. (Earlier probes without --no-loops: n = 8, 12 free and from counter_odftl N = 6: also 0.)
- Tangle count with the same mutations: free search n = 18: 21 tangles (30,000 mutations; 35 without the loop bias and
  without --no-loops); perturbation from counter_odftl N = 6: 47 (20,000 mutations). Self-loops do not open anything:
  a winning self-loop is a one-vertex tangle learned once, a losing one is an escape.
- Renumbering within a priority class as an attack dimension (unstable std::sort): the swap mutation above was part of
  every run of this section; no effect beyond the noise of the climb was seen. Not searched systematically.

## 9. Corrections after the Lead's code check (16:10Z): LIFO attractor, consumed CurR
Verified in 8fbf0a7: include/oink/uintqueue.hpp lines 72-74 (pop returns queue[--pointer]) and 82-84 (push stores at
queue[pointer++]): Q is a stack, every attractor in dtl.cpp is depth-first; dtl.cpp line 690 `CurR = R` precedes the top
loop 691-706, so best_vertices builds a disjoint top-down decomposition (as sptl does). Consequences for this report:
- Survive unchanged: everything set-based. (M1) attraction sets do not depend on the pop order; (M2) with the restated
  disjoint decomposition; (M3) heads monotone; (M4) tangle usability; consequence (d) (upward-only influence); sections
  2, 5(b)-(d), 6, 7, 8 (data and the opponent-free argument); the "no reset" statement.
- Withdrawn: section 1(c) and section 5(a) (BFS layers, FIFO pusher chains, "older tangle pushes first"). Under LIFO the
  order is reversed in the one place that matters: at the pop of a vertex, its predecessors are pushed in edge-list order
  and the usable tangles of tin[v] after them in creation order, and the stack pops the LAST push first, so the NEWEST
  tangle fired at that pop is explored first and sets the strategies of its vertices before anything older. A new
  tangle therefore reorders the depth-first discovery immediately, with no permanent event paying for it. This is the
  renewable-looking mechanism the Lead asks about.
- What bounds it instead (Lead reading, to be proved or refuted by the proof lane):
  (W) one extraction per top per search (sptl 514-519, W reset in search 1016): within a search a top yields one
  extractTangles call, so a strategy alternation at one head needs one search per step; tangles per search <= n.
  (P, prefix lemma) Let t be the tangle learned at head k in search s from the region's depth-first run D_s, and let
  search s+1 differ from s only by t (same vertices in the region, same other tangles). The run D_{s+1} coincides with
  D_s up to the pop at which t fires (t did not exist in s and nothing else changed), t then pushes its vertices not yet
  discovered with the strategies they had in D_s (that is what t recorded), and every vertex discovered before that pop
  keeps its D_s strategy. So every member of SCC_s keeps its strategy and SCC_{s+1} contains SCC_s: the only change is
  that vertices outside t, now discovered from t's vertices (LIFO), may switch into it. Self-firing at one head is a
  monotone growth of the bottom SCC, at most n steps, not an alternation.
  (E, events) The prefix lemma fails exactly when something else changed at head k between the two searches: a vertex
  joined region k (at most n times per level), a vertex was stolen upward (at most n), a tangle was deleted (solved
  vertex, at most once per tangle), or a tangle from a LOWER head fired in region k for the first time. The last kind is
  the cascade the Lead names (T_k <= n + sum of lower T_j would be exponential); but a lower tangle fires at k only when
  its escapes are in Z_k, and its first firing absorbs its vertices into region k (they were in the lower region when it
  was learned, so they are new to k, (M3)): at most n first firings per head per level, and tangles that fire at the same
  pop as a consequence of the same Z_k growth form one event. Between two events the SCC sequence at head k is the
  monotone self-growth of (P). So tangles at head k per level = O(n) events x O(n) growth = O(n^2), polynomial overall.
  The step a proof must nail down is now (P)+(E): that nothing but these events changes a depth-first prefix at a head.
- Revised requirement for a killer: an Even vertex whose strategy alternates across searches needs, at each
  alternation, an event of (E) at its head: a new vertex, a theft, a deletion, or the first firing of a lower tangle; a
  construction has to make exponentially many such events happen at one head with a bounded vertex supply, which (E)
  says it cannot unless the first-firing count is not bounded by absorption (the case to try: lower tangles whose
  vertices were already absorbed by an earlier lower tangle fire later, when a further escape is covered: that firing
  is still tied to a Z_k growth event, which is what (E) counts).
- Searches aimed there (fitness = max tangles learned at one top priority within one search, and = max tangles in one
  search; mutations with self-loops and renumbering; from the n = 24 optimum and the perturbed counters): the per-top-within-one-search fitness is fooled by equal priorities (its optimum from the n = 24 game is 23 vertices
all at priority 10, 23 tops, one chain tangle each, one search: tops are only identifiable by priority in the trace), so
only the injective-priority runs count: n = 12, 16, 20 at most 3 per top within a search (section 5(a); the same fitness from the perturbed counter_odftl, whose priorities repeat, reached 24: equal-priority tops again); with --loops
and injective priorities, max tangles in one search at n = 16: 7 (40,000 mutations; the chain family alone gives n - 2 = 14 in one search, so the climb is weak evidence). No alternation at a single top
within a search was ever seen, as (W) predicts; across searches the self-firing chains grow monotonically (section 2:
the chain tangles are nested), as (P) predicts.

## 10. Hand constructions against (E) and (P) (Lead 16:40Z), what each did and why it stopped
Flags `--dtl --no-single --no-wcwc --no-loops`, generator experiments/red/dtl/gens_dtl.py ladder m (12 + 6m vertices).
- Ladder v1 (escapes of every lower tangle to an unclosed higher head H whose Odd vertex escapes to Odd's sink q): DTL
  learns 0 tangles, Odd wins all (2 iterations, verified). Why: a head is a best vertex only if its good path runs through
  priorities below its own and through Even's attractor; an escape to a sink Odd wins blocks the attraction of the
  escaping vertex, so H and then J are pruned, and pruned vertices stay in R, which blocks everything below. Lesson:
  every escape target of a usable tangle must itself be Even-winning through lower priorities.
- Ladder v2 (tower K_1 < ... < K_{m+2} of Even tops, each {K_i, w_i} escaping to K_{i+1}, the top a dominion; rungs u_s
  -> a_s with a_s escaping to K_1 and to x_s, X_s = {x_s, x_s'} escaping to a_{s-1}): 4, 6, 8, 10, 14, 18 tangles for
  m = 1, 2, 3, 4, 6, 8 (= 2m + 2), ONE iteration, J learns {J, b0} once. Why: the top dominion is found in pass 1 and the
  dominion attractor (search 1021-1030, attractTangles with maxpr -1) absorbs every tangle whose escapes are solved,
  i.e. the whole tower and then the ladder, in the same search. The rungs never staggered anyway: u_s is itself a top
  (even priority), its region consumes a_s, so every X_s is closed in pass 1, and in pass 2 all X_s fire in one cascade
  (X_s at the pop of a_{s-1}); W then caps J at one extraction per search, so the staggering "one rung per pass" is
  invisible: one tangle at J per search at most, and the search ends.
- Tower variants thought through and rejected before building (each kills the gadget): escapes cycling around the tower
  (no dominion in the tower) -> the lowest tangle's escape is covered by the chain of tangle firings and the whole tower
  closes as one dominion in pass 2; levels kept open by an escape to an Odd-priority vertex d_{i+1} above the next top
  (so that one level dissolves per search) -> the good path of each top would run through d_{i+1}, whose priority is
  above the top's own, and the pruning (threshold loop stops at pr(u), lines 752-758) removes the top.
- Shared-vertex lower tangles for (E)(1): a second tangle at head L containing a vertex of a first one must be learned
  while that vertex is in L's region, i.e. before the first fires at the higher head (the firing absorbs it, M3); its
  own firing then needs a further escape covered, which is a Z_k growth event, so the count of first firings is bounded
  by growth events even where it exceeds the absorbed vertices. Not built: every attempt to stagger escape coverings
  across searches ran into the two walls above (pruning below-own-priority, dominion attractor).
- (P) across non-events for (E)(2): a tangle fired at k reproduces the strategies it recorded on its own vertices; it
  cannot be "inconsistent" because tangle strategies stay inside the tangle and attractTangle refuses a tangle with a
  vertex outside R (line 128); the vertices it pushes change only the discovery of OUTSIDE vertices, which is the growth
  of (P). A shrunken lower region or a deletion changes which tangles fire, which is an (E) event by definition.
Sharpened requirement (replacing section 3): tangles at one head <= 1 + the number of (E) events at it, where events are
vertex joins (<= n), thefts (<= n), tangle deletions (<= |T|, each once) and Z_k growth events that cover a lower
tangle's last escape (<= n joins + absorptions); a flip of an Even vertex into or out of the head's SCC needs a push
from a tangle NEWER than the head's own newest, which only a lower head's tangle learned later in the same search (an
absorption event) or a region change can supply, and the absorption moves that tangle's vertices up for good. A killer
must therefore make one head see super-polynomially many such events, i.e. refute the "<= n per kind" counts; the per-
head counts observed (<= 9 at one head over 19 searches, section 9) are all event-driven.

## 11. GAP-C, completeness (Lead 16:50Z; proof lane claude/l-alg 11fbb49 docs/alg/DTL-proof.md 2.3 and 6, read)
Lemma K (if the player still wins somewhere, search(p) learns a new tangle or a dominion) is the whole of completeness;
its open cases are (C-a) every region open yet none productive, (C-b) pieces removed by Dom(prevV, R) treated as safe.
Oracle: a DEBUG build of the pinned 8fbf0a7 (scratchpad oink-debug; NDEBUG checks on, "search was incomplete!"), flags
--no-single --no-wcwc --no-loops -v -t. The proof lane's hand instances dtl_proof_c1/c2/c3: 2, 1, 2 tangles, verified,
no throw (dtl and idtl).
Fuzz on the debug build (dtl_fuzz.py, random games n = 8..28, out-degree 1..3, 30% self-loops, seed 5): dtl 6,000
games, idtl 6,000 games, 0 bad runs (every run verified, no throw; max 11 tangles). Hill-climbs with fitness = verifier
failure / error / unsolved vertex, self-loop and renumbering mutations: release build, dtl n = 20, 28 and idtl n = 16, 24 (40,000 mutations each);
debug build, dtl n = 12, 20 and idtl n = 16 (30,000 each): best fitness stayed 0 in all seven runs (no verifier failure,
no throw, no unsolved vertex, no "solver stuck"). Together with sections 2 and 8: no completeness or correctness
failure of the release path or the debug path found by any adversarial method used here.
Lead reading on why no counterexample was found, in the proof lane's terms. Every open sptl region is open because an
opponent vertex of its would-be cycle escapes to a vertex e in CurR \ Z (unconsumed, unattracted). Either e belongs to a
structure Odd wins from (then the region's head is rightly not productive: Even does not win there through that cycle),
or e is Even-winning, in which case the Even-winning cycle through e has an even maximum at some vertex v' with every
other vertex of the cycle below pr(v'), so v' is a best vertex (its good path runs below its priority through that very
cycle) and heads a region; the LOWEST such head has nothing lower to escape to but Odd-won junk, so its region is closed
and learns a tangle (K1-K3), and that tangle fires into the blocked region at its escape's pop in the next search ("known
tangles fire upward", the proof lane's c3). A straddling tangle t' (a vertex in a higher region) fires into THAT higher
region (its vertex there is in Z, the rest in R), so it unblocks upward too; its lower part Y, if it has an escape into
CurR \ Z, repeats the same case one level down. The chain of blockers is finite and strictly descends in the sptl order,
so it ends at a closed productive region unless it ends in Odd-won junk, which means Even does not win the blocked part.
What this does not cover: the (C-b) pieces (Dom(prevV, R) with Q empty, 961-991) treated as safe; the argument above is
about X = empty. For the later pieces the same descent applies inside R_rem with X forgiven: a p-dominion D inside R_rem
whose p-priority vertices are all pruned would need every one of them to lack a good path below its own priority INSIDE
D, which contradicts D being a p-dominion with p-parity maxima on its cycles (the maximum vertex of any cycle of D is a
p-vertex whose good path is that cycle). So I expect (C-b) to close by "the maximum of a p-won cycle is never a
distraction"; not proved here.

## 12. Second DTL box (Lead 17:25Z, 2 h): the proof lane's shapes (α), (β'), (r1), (r2) and GAP-A
Read: claude/l-alg 6bb5d43 docs/alg/DTL-proof.md sections 1.6 (NOTE N5), 2.3 (K5, K6, shapes (α)/(β'), the exclusion
route with (r1), (r2)), 5 and 6 (c3, c4, dupclimb). Corrections folded into R8: (M2) above; 1(c)/5(a) were already
withdrawn.
(r1) probe. experiments/red/dtl/dtl_vstar.py: from the -t -t trace, the set of vertices pruned by the FIRST
best_vertices call of each search (X empty, the "distance k" lines) and whether any vertex is pruned in search s+1 that
was not pruned in search s of the same player (the non-monotonicity (r1) must exclude without a straddle). On every
many-tangle game of this report (evolved n = 24, 20, 18, 14, 10; perturbed counter_dftl 6, counter_odftl 6, tc+ 3;
tc 4, tc+ 3, counter_odftl 6; the first five with priorities made injective): 0 newly pruned vertices across 60 same-player
search pairs. (Comparing the printed best-vertex SETS instead is not the right test: with result -1 the printed set is
the previous round's V, and 1-14 vertices "lost" that way all turn out to be rounds, not prunings.) Hill-climbs with
fitness = number of newly pruned vertices across consecutive searches (self-loop and renumbering mutations, n = 12, 16,
20, 30,000 mutations each): best fitness 0 in all three runs: no game with a non-monotone first pruning across consecutive
searches was found, with or without straddles, so no (r1) counterexample.
(β') probe. The debug build prints "duplicate tangle" at extraction; hill-climbs with fitness = duplicate extractions
(n = 14, 20, 30,000 mutations): best fitness 0 in both runs: no duplicate extraction ever, so no (β') configuration. The proof lane's c3/c4: 0 duplicates here as well.
Straddle detector (Lead 17:32Z, the proof lane's recipe from notes/L-ALG.md item 9): a copy of the pinned source in
the scratchpad (oink-det-src, Debug build oink-det) with two prints added to dtl.cpp: after each stable pruning result,
"STRADDLE tangle t: v(reg|orphan|out) ..." for every stored tangle of the player's parity with a vertex in a region of
that round and another vertex attracted by the threshold loop but in no region; and in sptl "REGION top X pr P closed
0/1" for every region computed. Counts on tc+ N = 4, 5, 6 (STRADDLE lines over the run): 16, 25, 36 (the proof lane
reports about 2N - 1 distinct tangles); on the perturbed tc+ 3 of section 6: 83. The (α) proxy (dtl_search.py --fitness
alpha: stable sets with a straddle whose first sptl pass leaves the LOWEST top's region open) is 0 on all of them: the
lowest region closes every time, as the proof lane saw in its inspected case. Climbs from tc+ 4, tc+ 5 and the perturbed
tc+ 3 with that fitness (detector build, self-loop and renumbering mutations, 12,000 each): best 0 in all three (104, 180 and 54
vertices): no mutation made a straddle leave the lowest region open.
(α), (β') by hand: the NOTE N5 shape was built literally (gens_dtl.py n5: t' = {a, c, d}, a -> tnew, tau's region
holding e, h as tnew's return): DTL solves it in 3 iterations with 3 dominions and 1 tangle, {tnew, h} and {tau, e} are
dominions in search 1, so the straddle never forms (the higher regions must stay open AND unpruned for three searches,
the two walls of section 10). No instance of (α) or (β') was reached in this box; the proof lane's c3/c4 and my ladders
all end in the same collapse (an open higher region is pruned or closes into a dominion whose attractor absorbs the
straddling candidate). Status: (α)/(β') unrealised, consistent with (r1) holding empirically.
GAP-A str-change count at a fixed region vertex set (Lead 17:36Z item 1): MEASURED. The detector build also prints
"SPTL top X" before each sptl region's attractor, "DOM top X" and "SOLVE attractor" before the removal attractors; at
-t -t -t every attraction event is printed ("attracted v by p (via w | forced | via tangle t)"). experiments/red/dtl/
dtl_strchanges.py rebuilds every sptl region (top + attracted vertices) with the strategy of each Even vertex (w, or the
strategy stored in tangle t from its "new tangle" line) and counts, for every (top, region vertex set) that occurs more
than once in the run, how often an Even vertex's strategy differs from its previous occurrence at the same pair:
| game | sptl regions | distinct (top, set) | pairs seen more than once | max repeats of one pair | max distinct sets at one top | strategy changes at a fixed (top, set) |
| --- | --- | --- | --- | --- | --- | --- |
| tc+ N = 4, 5, 6, 7, 8, 10 | 118, 202, 320, 478, 682, 1252 | 57, 82, 111, 144, 181, 267 | 26, 38, 52, 68, 86, 128 | 9, 14, 20, 27, 35, 54 | 9, 11, 13, 15, 17, 21 (= 2N + 1) | 0, 0, 0, 0, 0, 0 |
| evolved n = 24 / two-player n = 20 (injective) | 594 / 155 | 78 / 48 | 22 / 20 | 55 / 15 | 5 / 4 | 0 / 0 |
| perturbed counter_dftl 6 / counter_odftl 6 / tc+ 3 (injective) | 600 / 680 / 513 | 133 / 159 / 134 | 37 / 47 / 50 | 68 / 53 / 29 | 11 / 10 / 9 | 0 / 0 / 0 |
| tc 4 / counter_odftl 8 / chain 40 | 40 / 112 / 821 | 20 / 38 / 79 | 14 / 18 / 39 | 3 / 9 / 39 | 4 / 4 / 2 | 0 / 0 / 0 |
So the open quantity of GAP-A is ZERO on every game measured: a region with the same top and the same vertex set
always gets the same Even strategies, even when the pair recurs 68 times; what grows is the number of distinct vertex
sets at one top, and that grows linearly (2N + 1 on tc+, at most 11 elsewhere). Climbs with fitness = strategy changes
at a fixed pair (detector build, self-loop and renumbering mutations, n = 12, 16, 12,000 each): best 0 in both.

(M-cross) and the deletion route (Lead 17:53Z; proof lane Lemma S, DTL-proof.md 3(a)). Tool: experiments/red/dtl/
dtl_mcross.py on the detector build (which now also prints "DELETE tangle t" when attractTangle deletes a tangle with a
solved vertex). It rebuilds every sptl region of the FIRST PIECE of each search (the sptl blocks between the first stable
pruning result and the first DOM removal, last pass per top) and compares consecutive same-player searches: tops lost
(not solved), regions shrunk (minus solved vertices), heads moved down.
- Restricted to the proof's setting (X empty: searches whose FIRST pruning result is stable): 0 violations of all three on
  tc+ 4, 6, 8, the evolved and perturbed games, tc 4, counter_odftl 8, chain 40. But such searches are RARE: 2 of 10, 2
  of 14, 2 of 18 on tc+ 4, 6, 8; 1 of 3, 1 of 6, 1 of 11, 1 of 16, 3 of 10 on the others. On tc+ every other search starts
  with result -1 (the -1 branch removes a threshold attractor before any stable set), so Lemma S's hypothesis covers almost
  none of the tangles learned there.
- Unrestricted (first stable set of each search, whatever X is at that point): regions of the same top differ between
  searches with NO dominion and NO deletion in between: tc+ 4, Even-0-H (the highest top) has first-piece region 52 in
  search 0, 40 in search 1, 43 in search 2 (searches 0-2 learn no dominion; the first DELETE lines come after the
  dominion of search 4); search 1's region lacks Even-1-H, Even-2-H, Even-3-H, the Even-k-B-j and the Odd-*-Z/S vertices
  of search 0 and has the Even-*-S and Odd-*-B vertices instead. The pruning itself is monotone there (dtl_vstar.py: 0
  newly pruned vertices on tc+ 4, 6, 8), so the difference comes from X: the pieces removed by the -1 branch before the
  stable set differ between searches as the tangle set grows. So region monotonicity across searches holds at X empty
  and fails at X nonempty on tc+, without deletions. Heads also move down there (tc+ 4: Even-3-A-k from Even-0-H to
  Even-3-Z; counts 37, 135, 329 on tc+ 4, 6, 8).
- Deletions: 24, 48, 80 on tc+ 4, 6, 8; 57 on the evolved n = 24; 82 on the perturbed tc+ 3; all after dominions, as the
  code says. Recurring (top, set) pairs at first pieces: 0 after a deletion in every game; and section 12's measurement
  over ALL sptl regions (all pieces, all X) found 0 strategy changes at a recurring (top, set), so no deletion ever paid
  for a new SCC at a recurring pair: tangles-per-deletion is 0 here, not > 1.
- What this says for Lemma S: the determinacy "SCC = f(top, region set)" is what holds empirically, over all pieces; the
  route through (M-cross) at X empty proves it only for the rare X-empty first pieces; the statement to prove is the
  one measured: same (top, vertex set) implies same strategies whatever X was.

Third DTL box (Lead 18:02Z, 2 h): the nested-tangle shape and the deletion ratio. End state of the Lead's item 1 = a new
tangle learned at a (top, region set) pair that occurred before. dtl_strchanges.py now counts that over ALL sptl regions
(the "new tangle" line that follows a block's REGION line is charged to that block) together with DELETE events:
| game | new tangles at a recurring (top, set) | deletions | ratio |
| --- | --- | --- | --- |
| tc+ 4, 6, 8 | 0, 0, 0 | 24, 48, 80 | 0 |
| evolved n = 24 (injective) | 0 | 57 | 0 |
| perturbed counter_dftl 6 / counter_odftl 6 / tc+ 3 (injective) | 0 / 0 / 0 | 9 / 58 / 82 | 0 |
So no deletion ever produced a new SCC at a recurring pair and the deletion route's counter seed (ratio > 1) is absent.
Note on the nested-tangle end state as stated (theft of a t'-vertex v, later τ's region again S ⊇ U_t): with U_t' ⊆ S and v
stolen by a higher top, S cannot recur at τ while heads only move up (M3); it can recur only in pieces with X nonempty,
where regions are not monotone across searches (the (M-cross) paragraph above). Climbs with fitness = new tangles at a
recurring pair (detector build, self-loop and renumbering mutations; free n = 12, 16; from tc+ 4 and the perturbed
counter_odftl 6): NEWRECUR-PLACEHOLDER

## 4. What was not done
- No Lean or refereed proof of the polynomial bound; section 1 is a Lead reading with the gap named.
- No Python port of dtl (Oink's trace sufficed: every tangle, strategy, escape and pruning round is printed).
- Total work other than tangles (pruning rounds are at most n per best_vertices call, calls per search at most n + the
  recursion depth, searches at most the tangle count) was not measured separately.

## DONE / FINDINGS / NEEDS
- DONE: Lemma M (section 1) with the dtl.cpp line references; the requirement for a killer (section 3) and the open
  statement; tools experiments/red/dtl/ (dtl_search.py: tangle or unsolved-vertex hill-climb; dtl_flips.py: strategy-flip
  census; gens_dtl.py chain); data of section 2 (search optima n = 10..30 and two-player, chain n - 2, idtl equal,
  completeness probe clean, flip census); check.sh pins chain 10 = 8 tangles when the Oink build is present.
- FINDINGS: (1) DTL has no reset: tangle attractor, pruning survivors, region heads and tangle usability are monotone in
  the tangle set during one player's phase; (2) the only non-monotone event is theft (a tangle's vertex taken by a
  higher region), spent once per vertex per level, and every strategy change seen in 19,000 games is a theft; (3) the
  largest mechanism found is the chain (O(n^2) tangles, one-player games, Even passive); (4) a killer needs an
  attraction-event order at one Even vertex that reverses super-polynomially often under those monotonicities, which
  reduces to the pusher-chain (FIFO) order fixed by Oink's edge lists and tangle creation order; not found, and the
  potential argument says it does not exist (Lead reading, gap named).
- DONE (second half of the box, 15:35Z-): section 5 (the four weak points: FIFO order, phase alternation, subgame
  removal, work per tangle; the TC-variant question), section 6 (Oink's dftl branch built, both generators transcribed,
  dtl linear and verified on both, the original a028e62 DFTL a Fibonacci counter on counter_dftl, ODFTL on
  counter_odftl), section 7 (universal-tree angle), section 8 (--no-loops re-runs, self-loop and renumbering mutations,
  correctness probes clean), perturbation searches from the counters and tc+.
- FINDINGS (second half): (5) the author's own DTL-era counterexample attacks the "remove the lowest top" heuristic
  that DTL replaced by the good-path greatest fixpoint, and DTL learns 2N + 3 tangles on it; (6) no TC variant can give
  dtl a renewable theft, by (M1)+(M3) (one-sided attraction, no opponent during a phase); (7) the FIFO pusher-chain
  order is a lexicographic order on tuples, where a proof must count descents (universal-tree-shaped counting), and
  (d) upward-only influence is what should bound it; (8) with --no-loops, self-loops and renumbering: no wrong answer,
  no unsolved vertex, tangle counts unchanged within noise.
- DONE (16:50Z-, GAP-C): section 11: debug-build oracle, proof lane's c1-c3 re-run, 12,000 fuzz games and seven
  adversarial climbs clean, the unblocking argument for (C-a) and the "maximum of a p-won cycle is never a distraction"
  expectation for (C-b), both Lead readings.
- DONE (17:36Z-, bounded items): GAP-A measured (0 strategy changes at a fixed (top, region set) on tc+ 4..10 and every
  many-tangle game, distinct sets per top linear); the straddle detector rebuilt from the proof lane's recipe; (α)
  containment climbs from tc+ 4, 5 and the perturbed tc+ 3: proxy stayed 0.
- DONE (17:25Z-, second DTL box): section 12: N5 folded into (M2); (r1) trace probe (dtl_vstar.py: 0 non-monotone first
  prunings on 9 games, 60 search pairs) and climbs (0 at n = 12, 16, 20); duplicate-extraction climbs on the debug build
  (0 at n = 14, 20); the N5 shape built (collapses into dominions); (α)/(β') unrealised; GAP-A count not measured.
- NEEDS: Lead: the proof lane should treat section 1(c)+(d) (pusher-chain descents bounded through upward-only
  influence) as the statement to prove or refute; a refutation there is the only killer shape left that I can name.
