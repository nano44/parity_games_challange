# R8: DTL (Oink's distance tangle learning, van Dijk's research solver) as a target (L-RED, 2026-10-15)

Lead's ask (15:06Z, 6 h): build a family on which DTL's learned-tangle count or total work is super-polynomial; first the
invariant DTL maintains (the analogue of R3's Lemma D), then the exact construction requirement, then a counter. Materials:
L-ALG's line-mapped pseudocode (claude/l-alg 898d02d, docs/alg/candidates/C5-DTL.md) and attack verdict (549bb34: every
tc/tc+ variant polynomial). Source read here: tools/oink/src/src/solvers/dtl.cpp @ 8fbf0a7 (best_vertices 643-776,
search_rec 834-994, search/run 997-1161; attractVertices 65-101, attractTangle 109-185, extractTangles 210-471, sptl
476-546, against L-ALG's transcription, which is accurate). Binary: tools/oink/build/oink --dtl --no-single --no-wcwc;
the release build still prints "best vertices", "distance k" and "new tangle ... with k escape vertices" at -t -t, enough
to see every tangle (vertex set, Even's strategy, escapes) and every pruning round.

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
- (M2) The pruning of best_vertices is a greatest fixpoint: V* = the largest V such that every v in V can step into
  A_T(Reg_T(V), R, t) for some t < pr(v) (lines 711-741), where Reg_T(V) = union of the attractors of the tops of V with
  threshold pr(top). The operator is monotone in V and, by (M1), pointwise increasing in T; so V*_T subset of V*_T'.
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
(c) Even's strategy str[u] is set by the FIFO attractor: str[u] := the first popped successor of u (attractVertices 80), or
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
(injective priorities so the tangle priority names the top), PERHEAD-PLACEHOLDER
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
counter_dftl; the tip's two-player DFTL is linear on both (1 iteration). So the branch's counterexample is the pair
(ODFTL, counter_odftl), as the fix commit d54dfad says ("Fix counter_odftl to have a tiny tangle of the opponent after
the distraction").
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
Perturbation search from counter_dftl N = 6 (32 vertices) under dtl (fitness = tangles, 40,000 single mutations):
PERT-PLACEHOLDER
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
- NEEDS: Lead: whether a written proof of the polynomial bound (section 1(c) made rigorous) is wanted from L-ALG or
  REFEREE, since it would turn DTL from "survives the bench" into a candidate with a running-time argument.
