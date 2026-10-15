# DTL: proof attempt for gauntlet step 4 (correctness and running time) — L-ALG, 2026-10-15

Status: IN PROGRESS (box 15:50Z-23:50Z). Every step below is marked PROVED / SKETCH / GAP. Nothing here is a result
until two referees sign it (CLAUDE.md). The object is van Dijk's research solver `dtl` in Oink at commit 8fbf0a7,
file src/solvers/dtl.cpp (line numbers below are of that file, release build: code under `#ifndef NDEBUG` and `trace`
is not part of the algorithm). Pseudocode: docs/alg/candidates/C5-DTL.md. Independent adversary: L-RED R8
(docs/red/R8-DTL.md, claude/l-red d6496f3); its Lemma M is unrefereed and is re-proved here where used, never cited.

## 0. Statement (written first, diffed against TARGET.md v1.0 sections 1-3)

### 0.1 The algorithm A_DTL (what is claimed about)
Input: a parity game G = (V, V_E, V_O, E, pr) exactly as TARGET section 1: V finite, every vertex has a successor,
pr : V -> {0, ..., n}, max-parity, n = |V|, m = |E|, input length Theta((n + m) log n).
Step 0 (Oink, oink.cpp:35 `game.ensure_sorted()`): sort the vertices by priority, non-decreasing, and reindex them
0..n-1 in that order; keep the owner, priority and edge lists. Cost O((n + m) log n) word operations.
Step 1 (dtl.cpp 1072-1161 `DTLSolver::run()` with `interleaved = false`, all vertices enabled, G := V): the loops of
lines 1109-1121: `while G != {}: if not search(0) break` then `while G != {}: if not search(1) break`.
Output: for every vertex v solved by `Solver::solve(v, player, str[v])` (line 1034): v is put in W_player, and if
owner(v) = player the positional strategy sigma_player(v) := str[v]. Vertices never solved are output as unsolved.
A_IDTL is the same with `interleaved = true` (lines 1125-1138).
Preprocessing switched off (as in every fleet run: `oink --dtl --no-single --no-wcwc`): no single-parity solving, no
winner-controlled-cycle removal, no self-loop removal, no priority compression/inflation/renumbering. The claim is
about the solver alone.

### 0.2 Theorem D1 (correctness and completeness)
For every parity game G as in 0.1, A_DTL halts, solves every vertex exactly once, and the output satisfies
  W_Even = W_E(G) and W_Odd = W_O(G)
(TARGET section 1 definitions: W_E(G) = vertices from which Even has a strategy, general = history-dependent,
winning every consistent play under max-parity; W_O likewise; W_E ⊔ W_O = V by determinacy). Moreover sigma_Even is
a positional strategy on W_Even ∩ V_E such that every play starting in W_Even, consistent with sigma_Even, against
every (general) Odd strategy, stays in W_Even and is won by Even; symmetrically sigma_Odd on W_Odd ∩ V_O.
Same statement for A_IDTL, with "the exception `solver stuck` (line 1136) is never thrown" added.

### 0.3 Theorem D2 (running time, word RAM of TARGET section 3)
Let tangles(G) be the final value of the counter `tangles` (line 463) and dominions(G) of `dominions` (line 375)
on input G. There are polynomials p_a, ..., p_e such that for every G as in 0.1:
  (a) tangles(G) ≤ p_a(n + m) (the tangle count);
  (b) every call of best_vertices (643-776) executes at most p_b(n + m) pruning rounds (iterations of the loop 674-773);
  (c) every call of search_rec (834-994), with its recursive calls, executes at most p_c(n + m) iterations of its loop
      850-993, at recursion depth ≤ d ≤ n + 1;
  (d) the number of calls of search (997-1069), i.e. the counter `iterations` (1111, 1119), is at most p_d(n + m);
  (e) the total number of word operations of A_DTL, step 0 included, is at most p_e(n + m), on a word RAM with words
      of O(log(n + m)) bits. Every number the algorithm manipulates is a vertex index (< n), a priority (≤ n), a
      tangle index (≤ tangles(G)), a queue/stack position (≤ n) or a bit of a bitset of n bits (lines 837-840, 651-654:
      bitset copies and resets cost O(n / log n) words each). No number has more than one word, so the unit-cost
      count equals the bit-cost count up to the constant of the word size (TARGET section 3, second bullet, is met by
      construction, not by assumption).
Same for A_IDTL.

### 0.4 Diff against TARGET.md v1.0
- Section 1, objects: identical (finite V, successor-closed, pr into {0..n}, max-parity, general strategies in the
  definition of W_E, W_O). DTL also accepts larger priorities; the bound (e) uses pr ≤ n only in the threshold loop
  `for t = 0..priority(nodecount()-1)` (722) and in the recursion-depth bound (c). For an input with priorities not in
  {0..n}, TARGET's compression step (O(n log n), charged to the algorithm) is applied before step 0; it preserves order
  and parity, and DTL's behaviour depends on priorities only through their order and parity (every comparison in
  dtl.cpp is `priority(u) <= t`, `priority(v) > t`, `priority(u) == t`, or `priority & 1`: lines 74, 140, 594, 613,
  663, 714 via attracts, 737, 901, 904, 937, 938, 1008), so A_DTL on the compressed game makes the same choices.
- Section 2, target statement: TARGET asks for (W_E(G), W_O(G)); D1 gives these as (W_Even, W_Odd) plus strategies.
  "Halts within p(n + m) steps": D2(e). Deterministic: yes (no randomness in dtl.cpp; the FIFO queue `Q` (uintqueue)
  and Oink's edge-list order fix every choice).
- Section 3, model: word RAM, O(log(n + m))-bit words: D2(e) counts word operations and names every number's size.
  No arithmetic on long numbers anywhere in dtl.cpp (no weights, no counters beyond `tangles`, `dominions`,
  `iterations`, `steps`, `curdist`, each ≤ p_e(n + m)).
- D2 change 5 (strategies): D1 outputs positional strategies and states they win; the fleet's L-COMP check (step 2)
  verifies them on every test game; the proof obligation is D1's last sentence.
- Not claimed: anything about Oink's preprocessing, `--inflate/--compress`, parallel solvers, or games with
  disabled vertices.

### 0.5 What a GAP looks like here
If a step below is a GAP, the deliverable is the exact failing claim and a candidate instance shape (section 5).
Lead/L-RED route it; L-ALG does not contact L-RED.

## 1. Primitives and invariants (dtl.cpp 40-202, 210-471)
TODO (next: 1.1 attracts/attractVertices/attractTangle semantics; 1.2 the pop-order potential; 1.3 tangle soundness
by induction on creation; 1.4 extractTangles finds exactly the bottom SCCs reachable from top; 1.5 escapes vs solved
vertices (trap property of dominion removal)).

## 2. Correctness of D1 (soundness of dominions; completeness; strategies)
TODO.

## 3. Running time of D2: (a) tangles, (b) rounds, (c) search_rec, (d) iterations, (e) total work at bit cost
TODO.

## 4. idtl vs dtl
TODO.

## 5. Gaps and candidate instance shapes
None recorded yet.

## 6. Status table
| step | status | where |
| --- | --- | --- |
| 0 statement | written, diffed | section 0 |
| 1 primitives | TODO | |
| 2 correctness | TODO | |
| 3 running time | TODO | |
| 4 idtl | TODO | |
