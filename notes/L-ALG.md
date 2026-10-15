# L-ALG notebook — successor session (session_012cQPWcEm23KMdMQSvWrULr), 2026-10-15

## Resume point
- Task: DTL gauntlet step 4 (Lead go 15:50Z, box to 23:50Z). Deliverable docs/alg/DTL-proof.md (statement §0; §1 primitives
  PROVED; §2.1 soundness PROVED; §2.2 halting PROVED; §2.3 completeness SKETCH with GAP-C; §3 running time (b)(c)(d) PROVED,
  (e) conditional on (a), (a) GAP-A; §4 idtl; §5 gaps; §6 status + evidence). Last push: see git log (claude/l-alg).
- Lead session for messages: session_014FBi6o334DvwT5Uw2kDfoN. Push: scripts/verify.sh && git push -u origin claude/l-alg.
- If resumed: (0) Completeness: straddling tangles DO occur (tc+, measured), so (α) cannot be excluded by the regress of
  DTL-proof.md §2.3; the open step is "an orphan never contains the lowest top's successor" (never observed). (r1)
  monotonicity of the first pruning across searches holds on all 4,006 games tested and is still worth proving. (1) GAP-C: try to prove Lemma K by induction over search_rec iterations with the hypothesis Claim F
  "nothing learned in iterations ≥ i ⇒ W_p(R_i^#) = ∅" (R^# = R with all edges leaving R deleted); the three piece types
  (S) stable regions, (Z) level-t attractor to X, (P) Dom(prevV) with Q empty must be handled; K5 settles the lowest region
  at X = ∅ except for straddling tangles. (2) GAP-A: bound the number of distinct SCCs extracted at one top; data says ≤ n.
- Handover (docs/agents/LANE-RESTART.md step 1) still to be written if the session is replaced; this file is the draft.

## DONE (this session; all on claude/l-alg, verify PASS at every push)
- docs/agents/handover-checks/L-ALG.md (b720b0b; Lead re-measured 5/5).
- C5-DTL.md corrected: Oink's uintqueue is a STACK (LIFO), and best_vertices consumes CurR across tops within a round
  (dtl.cpp 690 precedes the loop 691). Both verified on a debug build trace (experiments/alg/instances/dtl_proof_c1.pg).
- docs/alg/DTL-proof.md (statement 5175454; sections b51c7d4, 11fbb49, later). experiments/alg/dtl_debug_fuzz.py (debug-build
  completeness oracle: 50,000 random games, 0 failures), experiments/alg/dtl_pertop.py (per-top tangle counts),
  experiments/alg/instances/dtl_proof_c1..c3.pg (hand-built all-Even-won ladders; c3 is the worked example of §6).

## IN FLIGHT
- none at the time of writing (a per-top run on tc N = 4..16 may still be in a background shell; results go to §3(a) if they
  arrive; nothing depends on them).

## NEEDS
- Lead: route GAP-C and GAP-A (docs/alg/DTL-proof.md §5) to L-RED; route the R8 corrections (FIFO/BFS void; (M2) union of
  attractors wrong) to L-RED; T-ALG1 (a) still unrouted (deferred 11:20Z).

## Things only I know
### Oink facts established this session (dtl.cpp @ 8fbf0a7 unless stated)
1. `Q` is a stack: include/oink/uintqueue.hpp `pop()` = `queue[--pointer]`. Every attractor is depth-first; str[u] = the
   vertex being popped when u was pushed (its DFS parent in the reversed graph). At one pop, attractVertices pushes the
   predecessors in `ins` order (69) and attractTangles then pushes tangle vertices (sorted index order, 164-172); the tangle
   vertices are popped first.
2. best_vertices regions: ONE copy CurR per round (690), consumed across tops (699); a top inside a higher region is skipped
   (692). Regions are disjoint; R_rem = R \ Reg. Candidates use the UNconsumed R (714).
3. attractTangle is only evaluated for tangles in tin[v] at the pop of v (200-201): a tangle none of whose escapes is popped in
   the current attractor is never attracted, even if all its escapes are outside Gx (NOTE N1 in the proof).
4. extractTangles extracts every nontrivial SCC reachable from top, not only bottom SCCs; in a closed region every vertex
   reaches top in the restricted graph, so the SCC containing top = the set reachable from str[top] under "p: parent edge,
   opponent: all edges in Z" (proof §3(a) remark).
5. Oink's CLI renumbers priorities by default (parse_pgsolver_renumber + Game::renumber: gaps removed, order and parity
   kept, +1 at a parity change, +2 at a same-parity step) and sorts vertices by priority; the trace prints the renumbered
   priorities (c3: 6 printed as 4). `--no-single --no-wcwc` disables the other preprocessing; self-loop removal is off by
   default.
6. Debug build: `cmake -S tools/oink/src -B <dir> -DCMAKE_BUILD_TYPE=Debug -DOINK_BUILD_NATIVE=OFF -DOINK_BUILD_EXTRA_TOOLS=OFF
   -DOINK_BUILD_TOOLS=OFF -DOINK_BUILD_TESTS=OFF && cmake --build <dir> -j4` (about 1 min; built in the scratchpad, not in
   the repo). It enables: `-t -t -t` attraction events ("attracted v by p (via u / forced / via tangle k)"), region prints
   with strategies, the assert at 648, the "search was incomplete!" throw (1149), and the exit on a dominion at depth != 0
   (349-355, only with -t). It is ~50x slower than release on tc+ N = 12.
7. Release trace (`-t -t`): "best vertices: ... (stable)", "distance k: v ..." (pruned vertices per round), "new tangle P (i)
   (depth d) v->s ... with k escape vertices", "dominion P (depth d) ...", "X ∪= Dom(V)", "X ∪= attracted with threshold t".
8. van Dijk's TL completeness proof (CAV 2018, arXiv 1804.01023, Lemmas 4-9 pp.7-8) uses the "reduced region" (remove
   vertices from which the opponent reaches lower regions) and α-maximality; DTL has neither, so its analogue (K2) is a new
   argument: a duplicate bottom SCC of a closed sptl region has all escapes in X (removed pieces).
### Why every hand-built completeness counterexample collapsed
- A stored tangle with an escape in a higher region fires into that region at the escape's pop (if none of its vertices was
  consumed before and its priorities fit), and the attractor continues through its vertices; consumption forgives all the
  opponent's exits to higher regions; the opponent's deviation vertex x is attracted into the region of its LOWEST cover
  unless pr(x) exceeds that cover, which breaks the covering. The only escape from this is a straddling tangle (top absorbed
  elsewhere, lower part opponent-closed), which needs three generations of tangles (§2.3).
9. Straddle detector (not in the repo; rebuild from this recipe): copy tools/oink/src to a scratch dir, in dtl.cpp add after
   the region loop of best_vertices (line 706) `bitset RegCopy(Z);` and before `Z.reset();` at 763, when `!changed_V and
   trace >= 1`, loop over tangles t with tpr[t] != -1 of the player's parity and print "STRADDLE-A tangle t" if some vertex
   is in RegCopy and another in Z but not RegCopy; build Debug as in item 6; run with -t. tc+ shows ≈ 2N-1 such tangles per
   run, random games none.
### Scripts
- `python3 -I experiments/alg/dtl_debug_fuzz.py <debug-oink> tools/oink/build/rngame <outdir> N [seed]`.
- `python3 -I experiments/alg/dtl_pertop.py <debug-oink> game.pg`.

## Sources opened (this session)
- van Dijk, "Attracting Tangles to Solve Parity Games", CAV 2018, arXiv 1804.01023 (PDF sha256
  23a25426f2ad487328fc823ef4c4feab0f95ab3c5b607715d294d332eefcbc05): Def. 1 (tangle, p.4), Lemmas 1-10 (pp.7-8: regions
  α-maximal; plays in a region won; reach top; new tangle's escapes in higher α-regions; bottom SCC unique; lowest region
  has a tangle; dominion iff no escapes; highest region's tangles are dominions; search terminates with a dominion).
- Oink source @ 8fbf0a7: src/solvers/dtl.cpp (all), include/oink/uintqueue.hpp, src/oink.cpp (35, 436-530), src/game.cpp
  (618-634 renumber), src/pgparser.cpp (350-), src/tools/solve.cpp (205-209, 263, 327).

## Dead ends (this session)
- Hand-built completeness counterexamples c1 (pruning returns -1 at top level), c2 (straddling tangle), c3 (ladder of
  deviations): all solved by DTL; mechanism recorded above. Random fuzz with the debug oracle: 0 failures in 50,000.
- Claim S'' ("non-transient p-priority vertices of a dominion are never pruned") is FALSE in general (c3: y and z are pruned),
  so completeness cannot go through "the pruning preserves dominion vertices"; it must go through the later iterations.
