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
Lead reading of (c): every strategy flip spends a unit of a potential of size O(n^2) per vertex, so the number of distinct
(region, strategy) pairs, hence of tangles, is polynomial. Not proved line by line (the pusher-chain argument is where a
proof would have to be careful; see section 4), but it is the shape of the obstruction.

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
