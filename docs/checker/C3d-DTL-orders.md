# C3d: statement diff of DTL-proof.md §0 for order data ω (CHECKER, 2026-10-16 ~00:35Z)

Diff: docs/alg/DTL-proof.md §0 at claude/l-alg 37bbe2f against the frozen ccff864 (L24), word-level (`git diff
--no-index --word-diff` of the two §0 extracts). Also read: the "Order data" paragraph of docs/alg/candidates/C5-DTL.md
at 37bbe2f. Code: Oink 8fbf0a7 (tools/oink/src). Statement diff only; no re-runs; no judgement on the proofs.

## Verdict: FAIL (three text fixes; nothing in the change is wrong in direction)
| item | verdict |
| --- | --- |
| (1) diff only at the expected places | PASS for what changed; **FAIL**: Theorem D1 (0.2) was NOT changed and still says "every order of equal-priority vertices", while 0.1 claims D1 for every order datum ω |
| (2) O1-O8 located correctly in Oink 8fbf0a7 | **FAIL (minor)**: O3 cites the wrong parser function; O4 and O8 line numbers off; O7 missing from §0.1's list |
| (3) "for every ω" is a strengthening with Oink's run as one instance | PASS (note N-2 on O3') |
| (4) no over-claim vs TARGET §1-3/§5; no C3/C3b item lost | PASS. **New finding NF-1** (a C3 miss of mine, not caused by this diff): the pinned parser always renumbers priorities; §0.1 step 0 does not say so |

## (1) The diff
Changed, as announced:
- 0.1: the "every order datum ω" sentence, with O1-O6 and O8 named and the pointer to C5-DTL.md / C5-orders.md.
- 0.3: tangles(G, ω) and dominions(G, ω); "every bound (a)-(e) is claimed for every ω"; "for every G ... and every order
  datum ω".
- 0.3(d): the A_IDTL counter is ⌊calls/2⌋ + 1.
- 0.4: determinism "for a fixed order datum ω".
Nothing else in §0 changed; every C3/C3b-era sentence is intact.
- F-1 (FAIL). §0.2, Theorem D1, is unchanged:
  - It reads "For every parity game G as in 0.1 and every order of equal-priority vertices in step 0, A_DTL halts ...".
  - §0.1 now says "Theorems D1 and D2 are claimed for EVERY order datum ω", and C5-DTL.md says "D1/D2 are claimed for
    every datum".
  - The theorem's own text is therefore narrower than what 0.1 says it claims. The two must agree.
  - Fix: "... and every order datum ω (0.1)" in D1, and in its A_IDTL sentence.

## (2) O1-O8 against Oink 8fbf0a7
| datum | cited | code | |
| --- | --- | --- | --- |
| O1 indexing non-decreasing in priority | game.cpp 478-505, std::sort | game.cpp:495 `std::sort(mapping, ..., priority(a) < priority(b))`, applied by unsafe_permute (534-575) | OK |
| O2 ins(v), one entry per edge, Oink: DECREASING index | oink.cpp 35, 37; game.cpp 868-906 | `ensure_sorted()` at oink.cpp:35, then `build_in_array(false)` at 37. The in-array does not exist before (the parser never builds it; `_inedges = NULL`, game.cpp:41/141), so it is built after the sort. 897-905 fill each list from its end while v ascends, so each list is in decreasing index, one entry per edge | OK |
| O3 outs(v): input edge order, targets renamed by the sort | pgparser.cpp 144-190, game.cpp 534-575 | game.cpp 534-575 (unsafe_permute renames targets, keeps list order): OK. **pgparser.cpp 144-190 is inside `parse_pgsolver` (line 71), not the parser the pinned command uses**: solve.cpp:263 calls `parse_pgsolver_renumber` (350), whose edge loop is 440-457 (`edges[id].push_back(n)` in input order) | **wrong citation** |
| O3' SCC emission order | dtl.cpp 283-299 | Pearce's finishVisiting at 287-300: root pushed first, then the stack part | OK |
| O4 tv sorted ascending | dtl.cpp 386 | `std::sort(tangle.begin(), tangle.end())` is at 389 (385 opens `#if CHECK_UNIQUE`) | line off by 3 |
| O5 dom_vector in O3' order, LIFO pops | (no line in 0.1) | 364-367 push in SCC vertex order; 1024-1030 push to Q; 1033 `Q.pop()` LIFO | OK |
| O6 threshold-loop re-push order, Oink: increasing index | dtl.cpp 723 | 723 `for (v = Z.find_first(); ...; v = Z.find_next(v)) Q.push(v)` | OK |
| O7 tin[v] in creation order | C5 only | 443 `tin[...].push_back(tidx)`, iterated by attractTangles (197-202) | OK in C5; **missing from §0.1's list** (it names O1-O6, O8 and calls O4, O8 fixed) |
| O8 counters; idtl = ⌊calls/2⌋ + 1 | dtl.cpp 1125 | `iterations++` is at 1126 (1125 is `while (true) {`). The formula holds: each round increments once and makes two calls; a run ending after search(0) has 2k − 1 calls and counter k, and a run ending at the round's emptiness test has 2k calls and counter k + 1 | formula OK; line off by 1 |
I found no other order-dependent choice on the release path beyond O1-O8 and their consequences (index sweeps follow
O1; attraction and escape orders follow O2/O3/O4/O7; the region stack follows these). This is not an exhaustive proof.

## (3) Strengthening
- Oink's run is one instance of ω. Each datum Oink fixes lies in the space 0.1 / C5 allow:
  - O1: sorted by priority;
  - O2, O3: lists with one entry per edge;
  - O3': one order of SCCs and of their vertices;
  - O5, O6: orders of the given sets.
- So a theorem for every ω implies it for Oink's run, and "for every ω" is a correct strengthening.
- N-2 (note). O3' as defined allows ANY processing order of the nontrivial SCCs reachable from top. Pearce's order (reverse
  topological, determined by O3) is only one of them.
  - The strengthened claim therefore covers orders the code can never produce.
  - That is legitimate but strictly harder to prove.
  - §1.5 at 37bbe2f still says extraction proceeds "in reverse topological order" (line 248). Either the proof uses only
    "some order" (then reword 1.5), or O3' should be restricted to orders consistent with Pearce (reverse topological).
  - L-ALG's choice; not a statement error.

## (4) TARGET and earlier items
- TARGET §2 needs a deterministic algorithm. A_DTL with Oink's ω is deterministic, and 0.4 says so per ω.
- No new over-claim.
- All C3/C3b items (A-1..E-3) are unchanged in the text.
- NF-1 (new; a miss in my C3 check, independent of this diff). `parse_pgsolver_renumber` (pgparser.cpp 492-511),
  which the pinned command always uses (solve.cpp:263), RENUMBERS PRIORITIES:
  - It sorts the distinct input values (flat_map).
  - It maps them to 0, 1, 2, ... in order, skipping one value where needed to keep parity (`if ((counter&1) !=
    (pair.first&1)) counter++`).
  - This is an order- and parity-preserving compression inside step 0, applied on every run, whatever the flags.
    (Oink's separate `--compress/--renumber` options remain off, as 0.1 says.)
  - Effects:
    - DTL never sees the input's priority values.
    - The game it solves has priorities in {0, ..., 2d − 1} or less.
    - The parser's flat_map costs O(n log n).
  - D1 is unaffected, by 0.4's own commutation argument (DTL depends on priorities only through order and parity). D2(e)
    is unaffected in kind (the cost is O(n log n), and priorities only get smaller).
  - But §0.1's step 0 must name it: "the parser maps the priorities order- and parity-preservingly to an initial segment
    (pgparser.cpp 492-511)". Then the description of A_DTL is complete.

## Fixes for PASS
1. F-1: D1 (0.2) "for every order datum ω", in both the A_DTL and A_IDTL sentences.
2. O3 citation: pgparser.cpp 440-457 (`parse_pgsolver_renumber`) instead of 144-190; O4 → dtl.cpp 389; O8 → 1126; add O7
   (fixed by the code: creation order, 443/197-202) to 0.1's list of fixed data.
3. NF-1: one sentence in 0.1 step 0 on the parser's priority renumbering (pgparser.cpp 492-511), noting that 0.4's
   commutation covers it.
4. N-2: optional. Reconcile O3' ("any order") with §1.5's "reverse topological order".
