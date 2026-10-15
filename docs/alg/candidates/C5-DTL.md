# C5-DTL: Distance Tangle Learning as written in Oink (transcribed by L-ALG, 2026-10-15 13:20Z)

Corrections 2026-10-15 16:30Z (L-ALG successor, found while writing docs/alg/DTL-proof.md against the code): (1) `Q` is a stack
(LIFO), not a FIFO queue; (2) best_vertices computes its regions top-down with ONE copy CurR per pruning round, consumed across
tops (line 690 precedes the loop 691), so the regions are disjoint and vertices of lower regions are attracted only from what
higher tops left; the earlier text said "fresh copy per top, regions overlap". Both change strategy/region details, not set
membership of attractors. Everything else re-read against dtl.cpp @ 8fbf0a7 and found exact.

Status: CANDIDATE by the Lead's redirect (12:47Z): "the one complete solver nothing in the fleet's bench can hurt".
This is NOT the fleet's design: it is Tom van Dijk's unpublished research solver `dtl` in Oink, commit 8fbf0a7
(github.com/trolando/oink, src/solvers/dtl.cpp, 1163 lines; history and the author's own statements in notes/L-ALG.md
"C5-DTL provenance"). Cite it as van Dijk's code. No published definition, no running-time claim by anyone; the author's
README asserts a counterexample ("counter_dtl") that was never committed, and his GandALF 2019 slides call the path-based
variants "VULNERABLE! (to a different version of the TC game)". Pseudocode below is a line-by-line transcription of
dtl.cpp (release build: code under `#ifndef NDEBUG` and `trace` is omitted; `computeDistanceValues`, lines 553-639, is
called only under NDEBUG/trace and is NOT part of the algorithm). Written so that an adversary (L-RED) can target it.

## 0. Conventions (Oink)
Max-parity; player 0 = Even, 1 = Odd; vertices are indexed in non-decreasing priority order (oink.cpp:35
`game.ensure_sorted()`), so "for top from high index down" = from high priority down, and priority(n-1) = max priority.
`G` = bitset of unsolved vertices; `R`, `Z`, `X`, `V`, `W`, `S`, `CurR`, `CurZ`: bitsets; `str[v]` = current strategy
successor of v (-1 = none); `Q` a STACK (uintqueue.hpp: `pop()` returns `queue[--pointer]`, LIFO; CORRECTED 2026-10-15 16:30Z, it was
written as a FIFO queue before: every attractor below is depth-first in the order of Oink's edge lists). owner(v) ∈ {0,1}; outs(v), ins(v) the edge lists. Tangles: for each tangle t,
tv[t] = its (vertex, strategy) pairs, tout[t] = its escape vertices, tpr[t] = its priority (-1 = deleted), tin[v] = tangles
having v as an escape. Counters: tangles, dominions, iterations.

## 1. Primitives
attracts(p, v, Z, R) [lines 40-57]: if owner(v) = p: v has an edge into Z. Else: v has an edge into Z and NO edge into R \ Z
  (edges to vertices outside R ∪ Z are ignored).
attractVertices(p, v, R, Z, Gx, maxpr) [65-101]: for every predecessor u of v:
  if u ∈ Z: if owner(u) = p and str[u] = -1 then str[u] := v;
  else if u ∈ R and (maxpr < 0 or pr(u) <= maxpr):
     if owner(u) != p and u has an edge into Gx \ Z: skip (opponent escapes);
     else Z := Z ∪ {u}; str[u] := (v if owner(u) = p else -1); Q.push(u).
attractTangle(t, p, R, Z, Gx, maxpr) [109-185]: return false unless tpr[t] != -1 and tpr[t] mod 2 = p; for each vertex
  w of t: if w ∉ G (solved): delete t (tpr[t] := -1), return false; if w ∈ Z: continue; if w ∉ R: return false;
  if maxpr >= 0 and pr(w) > maxpr: return false; else mark "can attract new". If nothing new: return false.
  If some escape e ∈ tout[t] has e ∉ Z and e ∈ Gx: return false. Else add every w of t not in Z to Z with str[w] := its
  tangle strategy, push to Q; return true.
attractTangles(p, v, R, Z, Gx, maxpr) [197-202]: for each t ∈ tin[v]: attractTangle(t, p, R, Z, Gx, maxpr).
A "tangle attractor to Z within R, escapes judged in Gx, threshold maxpr" below means: Q := Z; while Q: v := Q.pop();
  [callers may also remove v from R]; attractVertices(p, v, R, Z, Gx, maxpr); attractTangles(p, v, R, Z, Gx, maxpr).

extractTangles(top, R, str) [210-471]: p := pr(top) mod 2. Run Pearce's SCC algorithm on the graph restricted to R where
  every p-vertex keeps only the edge str[v] and every opponent vertex keeps all its edges into R, starting from top (only
  SCCs reachable from top are found). For each SCC C that is nontrivial (|C| >= 2, or str[v] = v, or str[v] = -1 and v has a
  self-loop): escapes(C) := {w ∈ G \ C : some opponent vertex of C has an edge to w} [327-341].
  If escapes(C) = ∅: C is a dominion: every v ∈ C with its str[v] goes to the solve queue (S, SQ, dom_vector); dominions++.
  Else if C (as a sorted vertex set) equals an existing tangle's vertex set: skip (duplicate) [385-424].
  Else: new tangle t with tv = C's (v, str[v]), tout = escapes(C), tpr[t] := pr(top); tin[e] += t for e ∈ tout; tangles++.
  Returns whether any tangle or dominion was created.

## 2. The three layers
sptl(V, W, R, p) [476-546] ("single-player tangle learning" over the best vertices; R is consumed):
  changes := false
  for top from n-1 down to 0 with top ∈ V ∩ R:
    Z := {top}; str[top] := -1; Q := [top]
    while Q: v := Q.pop(); R := R \ {v}; attractVertices(p, v, R, Z, R, pr(top)); attractTangles(p, v, R, Z, R, pr(top))
    closed := (owner(top) = p) ? (str[top] != -1) : (top has no edge into R)       # R = what is left
    if closed and top ∉ W: W := W ∪ {top}; if extractTangles(top, Z, str): changes := true
    Z := ∅
  return changes

best_vertices(V, R, p) [643-776] (V is output; returns 0 / 1 / -1):
  V := {v ∈ R : pr(v) mod 2 = p}; if V = ∅: return 0
  curdist := 0
  loop:
    curdist++; prevV := V
    Z := ∅; CurR := R                                                      # line 690: ONE copy per round, consumed across tops
    for top from n-1 down to 0 with top ∈ V and top ∉ Z:          # "the current p region"
      CurZ := {top}; Q := [top]                                             # (CORRECTED 16:30Z: not a fresh CurR per top)
      while Q: v := Q.pop(); CurR := CurR \ {v}; attractVertices(p, v, CurR, CurZ, CurR, pr(top)); attractTangles(p, v, CurR, CurZ, CurR, pr(top))
      Z := Z ∪ CurZ                                                         # regions are DISJOINT (top-down decomposition of R by V)
    Candidates := [v ∈ V, descending, with not attracts(p, v, Z, R)]      # no "good path" yet
    if Candidates = []: return 1                                           # stable
    for t := 0 .. pr(n-1):                                                 # attract R to Z "slowly", threshold t
      Q := all of Z
      while Q: u := Q.pop(); attractVertices(p, u, R, Z, R, t); attractTangles(p, u, R, Z, R, t)
      for u in Candidates (descending priority): if pr(u) <= t: stop; if attracts(p, u, Z, R): remove u from Candidates
    V := V \ Candidates                                                    # the remaining candidates are distractions
    Z := ∅
    if nothing was removed: return 1
    if V = ∅: V := prevV; return -1
  (A candidate u is kept iff it can step into a set reached from the p-regions of V through vertices and tangles of
   priority <= t for some t < pr(u): "u has a good path to the region of a best vertex". curdist = number of pruning
   rounds = the "distance"; it is only reported, never used by the algorithm.)

search_rec(R, p, depth) [834-994] (R is consumed; X := vertices removed from R):
  X := ∅
  loop:
    V := ∅; result := best_vertices(V, R, p)
    if result = 0: return
    if result = 1:                                                          # stable best vertices
      repeat: Z := R; changed := sptl(V, W, Z, p)  until not changed       # learn tangles in the regions of V
      Dom(V, R) -> X: for top from n-1 down with top ∈ V \ X: X := X ∪ {top}; str[top] := -1; Q := [top];
          while Q: v := Q.pop(); R := R \ {v}; attractVertices(p, v, R, X, R, pr(top)); attractTangles(p, v, R, X, R, pr(top))
      continue
    # result = -1: every best vertex was a distraction in the last round; V = the previous round's V
    t := 0; Z := ∅; Q := []
    for v from 0 up to n-1 with v ∈ R:                                      # lowest priority level that attracts to X
      if pr(v) > t: if Q nonempty: break; t := pr(v)
      if attracts(p, v, X, R): Z := Z ∪ {v}; str[v] := -1; Q.push(v)
    if Q nonempty:
      while Q: u := Q.pop(); R := R \ {u}; attractVertices(p, u, R, Z, R, t); attractTangles(p, u, R, Z, R, t)
      for u from n-1 down while pr(u) >= t: if u ∈ Z and pr(u) = t: X := X ∪ {u}; Q.push(u)     # threshold vertices to X
      while Q: u := Q.pop(); Z := Z \ {u}; attractVertices(1-p, u, Z, X, Z, t)                 # OPPONENT attracts within Z to X
      X := X ∪ Z
      search_rec(Z, p, depth+1)                                               # recurse on the rest of Z
      Z := ∅
    else:
      Dom(V, R) -> X (as above, without sptl)

search(p) [997-1069]: T := tangles; D := dominions; CurG := G; search_rec(CurG, p, 0); W := ∅.
  If dominions were found: for each (v, s) in dom_vector: str[v] := s; Q.push(v); dom_vector := [];
    while Q: v := Q.pop(); solve v for p with strategy str[v]; G := G \ {v}; attractVertices(p, v, G, S, G, -1); attractTangles(p, v, G, S, G, -1)
    S := ∅.
  return tangles != T or dominions != D.

run() [1071-1161] (dtl, non-interleaved): G := all vertices.
  while G != ∅: iterations++; if not search(0): break
  while G != ∅: iterations++; if not search(1): break
  (idtl: alternate search(0), search(1) until G = ∅; error "solver stuck" if neither finds anything.)
  Output: the solved vertices with their strategies (Oink verifies the solution when run with -v).
  Note: dtl's run() can END WITH G != ∅ if search(1) stops finding tangles (the NDEBUG check "search was incomplete!" is
  compiled out in release builds); experiments/alg/dtl_check.py checks completeness on every game (section 5).

## 3. What differs from tl / ptl / rtl (L-ALG reading of the code, against van Dijk's published tl, arXiv 1804.01023)
- tl: regions top-down by priority over the whole subgame, tangles learned in every closed region, tangle attractor.
- DTL: for one player p at a time, it first PRUNES the set V of p-priority vertices by the "good path" test (best_vertices):
  a p-priority vertex survives a round iff it can reach the p-regions of the surviving vertices through priorities and
  tangles below its own priority; vertices that cannot are "distractions" and are dropped. Only when V is stable are
  tangles learned (sptl), only from regions headed by surviving vertices; the regions of V are then removed (Dom(V,R) -> X)
  and the search continues on the rest. When every best vertex is a distraction (result -1), the lowest priority level that
  can already step into the removed part X is attracted to X and the remainder Z of that attractor (minus the opponent's
  attractor to the threshold vertices) is searched RECURSIVELY (search_rec on Z). This is the "distance" (number of pruning
  rounds) view of van Dijk's GandALF 2019 slide 43 ("similar to 'distance to opponent region'", "a path-progressive measure").
- Not in tl: the pruning loop, the threshold-increasing attractor (t = 0..maxpr), the recursion on Z, one player at a time
  (Even to exhaustion, then Odd; idtl interleaves).

## 4. Running time (best argument available; everything "unproven" is so labelled)
Each primitive is polynomial per call; one search_rec iteration costs O((n + |tangles|) * (m + sum of tangle sizes) * d).
The recursion depth of search_rec is bounded by the number of distinct priority levels (each recursive call removes the
threshold level t from Z). What is NOT bounded by any argument I can give: (i) the number of tangles learned (tl's own
exponential families tc, tc+ learn exponentially many; DTL learns 4..49 on tc N = 2..24 and 8..190 on tc+ N = 2..12 in
measurement, but no argument says why); (ii) the number of outer iterations of search(p) (each needs a new tangle or
dominion, so it is bounded by the number of tangles, (i)); (iii) the number of search_rec loop iterations (each removes
something from R or recurses, so polynomial per call given (i)). Hence: polynomial iff the number of learned tangles is
polynomial. UNPROVEN, and van Dijk's own README and slides say a counterexample exists for the path-based variants.
Bit cost: only indices and priorities (O(log n) bits); tangle storage is explicit (each tangle is a vertex set), so memory
and time are polynomial in n + the number of tangles.

## 5. Data (experiments/alg/dtl_check.py, out/dtl_check_dtl.log; ptl_sweep.py, out/ptl_sweep.log, out/dtl_large.log)
Filled in section 5 of the box report and in RESULTS.md: correctness and positional strategies verified (harness verify.py)
on the library, all canonical games with n <= 3, the 1,380 psolC-partial n = 4 games, 20,000 random canonical n = 4
games, 4,000 random games n = 5..12; tangle-count growth on the 13 families, S_s and T_R.

## 6. For the adversary (what to target)
- The pruning keeps a p-vertex iff it has a path to the current p-regions through priorities below its own. A gadget
  where the only good paths run through a tangle of the opponent's... (tangles of the opponent are never attracted for p),
  or where the good path exists only after an opponent tangle is learned, delays pruning by one round per level; the
  question is whether rounds can be made to repeat exponentially (the TC mechanism applied to pruning rounds).
- The threshold attractor (t ascending) attracts lower vertices first; a counter whose bits sit at increasing priority
  levels and whose "good path" opens and closes with the parity of a lower counter is the natural attack (van Dijk's
  "different version of the TC game").
- Non-interleaved order (Even to exhaustion, then Odd): a game where Even's search finds tangles for ever without a dominion
  while Odd's dominion would end it quickly is a possible slow-down (idtl is the comparison).
