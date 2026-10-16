# C5 orders: making C5-DTL.md a unique object, or claiming for every order (task A draft)
L-ALG, 2026-10-15 23:40Z. DRAFT for the Lead and CHECKER (L24: changes to DTL-proof.md §0 go through them). DTL-proof.md §0
is untouched by this file. Inputs: L-COMP's second implementation (trunk experiments/dtl-bench/README.md "Second independent
implementation", dtl_py.py docstring CH1-CH6, divergences #1-#3, failures/*.pg); dtl.cpp @ 8fbf0a7; game.cpp; oink.cpp.
Every line number below was re-read in tools/oink/src for this draft. Corrections 2026-10-16 00:45Z after CHECKER C3d: O3's edge
loop is pgparser.cpp 441-457 (parse_pgsolver_renumber, the pinned parser), O4's sort is dtl.cpp 389, O8's increment is 1126; the
parser always renumbers priorities (pgparser.cpp 492-511), now named in DTL-proof.md §0 step 0.

## 1. Inventory: every choice the computation makes that C5-DTL.md does not state
"Counts" = `tangles`, `dominions`, `iterations` and the stored tangle set; "regions" = the output W_Even/W_Odd;
"strategies" = the output sigma. Measured column: L-COMP xcheck on 238,071 games (exhaustive n ≤ 3, g10k, rngame, small50k,
127 family instances), Oink vs dtl_py in C5-literal mode and in `--order oink` mode.

| id | choice | what Oink does (lines) | where it enters the computation | can change | measured |
| --- | --- | --- | --- | --- | --- |
| O1 | index order of equal-priority vertices | step 0 `std::sort` on priorities (game.cpp 478-505; introsort, unstable above 16 elements) | every descending/ascending sweep; `ins`/`outs` contents after renaming | counts (via O2-O5); strategies in principle | counts differ (#2, n > 16); regions, strategies equal |
| O2 | order of ins(v) | `build_in_array` after `ensure_sorted` (oink.cpp 35, 37; game.cpp 868-906 fills each in-list from its end): predecessors in DECREASING index, one entry per edge | dtl.cpp 69: the push order at a pop, hence the DFS parents `str[u] = v` (73), hence the SCCs and the tangles | counts; strategies in principle (str = DFS parent) | counts differ (#2); regions, strategies equal |
| O3 | order of outs(v) | the vertex's edge line in input order, targets renamed by the sort permutation (parse_pgsolver_renumber's edge loop, pgparser.cpp 441-457, the parser of the pinned command; game.cpp 534-575 `unsafe_permute` keeps each out-list's order) | 83-90, 714, 738 (boolean tests: order-free); 329-337 (escape list `tout`, used only as a set at 143-146: order-free); Pearce 234-262 (traversal order) | only through O3' | - |
| O3' | order in which extractTangles emits the SCCs reachable from top, and the vertex order inside one SCC | Pearce's order: an SCC is emitted when its root finishes (283-299), root first then the stack pops; depends on O3 and on `str` | (a) new tangles' indices (433) and the append order of `tin` (437), hence the iteration order of attractTangles (200-201): when two firing tangles share a vertex, the earlier one sets its `str` (164-172); (b) `dom_vector` order (366-373) → O5 | counts; strategies in principle | not separated from O5 by L-COMP; (#3 attributes 3 games to the queue order) |
| O4 | vertex order stored in tv[t] | sorted ascending by index (389, `CHECK_UNIQUE` always on) | 125-141: the per-vertex checks run in this order and "solved ⇒ delete t" (132-135) precedes "not in R ⇒ return false" (137), so WHETHER a tangle is deleted at a given call depends on which of its vertices comes first; 164-172: push order of the tangle's vertices (DFS order below them) | counts | counts differ (#2) |
| O5 | the dominion solve queue | `dom_vector` = dominion SCCs in O3' order, each vertex once (366-373); all pushed in that order (1025-1029) and popped LIFO (1031-1037); every pop solves v, removes it from G and runs the attractor to S with tangles, which deletes (132-135) every tangle it examines that already has a solved vertex | which tangles are deleted during the extension and whether a tangle is absorbed as a unit or its remainder left in G: the next searches' tangle and dominion counts | counts (#3: dominions, iterations) | counts differ on 3 games (#3); regions, strategies equal |
| O6 | "Q := all of Z" in the threshold loop | `find_first/find_next`: pushed in increasing index, popped from the highest (723) | DFS order of the threshold attractor, hence `str` on R \ Z there (never read by extraction: those str are overwritten at the next region computation; read by attracts? no: attracts reads edges only) | nothing observable (str set here is overwritten before any extraction: 1.0 (s4) list) | dtl_py CH4 chose the same |
| O7 | iteration order of tin[v] | creation order (437 appends; 200-201 iterates) | same as O3'(a) | strategies in principle | - |
| O8 | the idtl `iterations` counter | 1126: incremented once per loop entry BEFORE the emptiness test; so iterations_idtl = ⌊c/2⌋ + 1 where c = number of search calls made; dtl: iterations = c (1111, 1119) | a counter only; no effect on the computation | the reported number | #1 (2-vertex instance) |

Not choices (already fixed by C5): LIFO stack (C5 §0); tops in descending index (sptl, best_vertices, Dom); candidates in
descending index; the −1 branch's ascending scan and descending threshold sweep; the duplicate test compares SORTED sets
(order-free); `escapes` deduplicated (order-free).
What NO order changes (Theorem D1's content): the final regions. Reason, not a new theorem: D1's proof (DTL-proof.md §2)
never reads a concrete order (see §3 below), and the measurement agrees (0 region differences in either mode). The output
STRATEGIES are order-sensitive in principle (str is a DFS parent) and were measured equal in both modes on every game; D1
claims only that they are positional and winning, which §2.1 proves for every order.

## 2. Where the proof of DTL-proof.md touches an order (re-read for this draft)
§0.1 line 18 ("in SOME order", O1 every); §1.0 tie order (D-4): "every argument uses the index order only through descending
index = non-increasing priority"; §1.2/1.3 attractor lemmas: "each vertex is popped once; str[u] = the vertex being popped
when u was pushed" (any order); §1.5 induction on CREATION order (the order of events in the run, well defined under any O3');
§2.3 K-lemmas: creation order again; §3(a) lines 506-510 describe Oink's `ins` order and the stored (sorted) tangle order as
the MECHANISM of str changes, not as a hypothesis; Lemma S step (4): "the same predecessor list (69) and the same tin list in
the same order (443)" = the orders are the same in both computations, which holds for any order data fixed for the run.
So: nothing proved so far depends on which order is used; every proof is about a run with FIXED but arbitrary order data.
The one place where an order is used as a fact is §1.0 (s4)'s list of str sources, which is order-free.

## 3. Option (i): pin Oink's orders in C5 and §0
Text that would be added to C5-DTL.md §0 (and mirrored in DTL-proof.md §0.1 step 0 and §7):
> Orders (pinned, dtl.cpp @ 8fbf0a7): ins(v) lists the predecessors of v in decreasing index, one entry per edge (game.cpp
> 868-906, built after the sort); outs(v) is the input edge line of v in input order with targets renamed; tv[t] is sorted
> ascending (dtl.cpp 389); extractTangles emits SCCs in Pearce's order (root first, then its post-order stack, 283-299) and
> dom_vector lists dominion vertices in that order, each once; tin[v] is iterated in creation order; "Q := all of Z" pushes
> in increasing index; iterations_idtl = ⌊(search calls)/2⌋ + 1.
Cost to the proof: no lemma is re-proved (§2 above). §7 gains seven rows, each a code fact. The step-2 evidence (`--order
oink`, all five counters equal on 238,071 games × {dtl, idtl}) then matches the claimed object exactly.
What (i) does NOT buy: counts are still not unique, because O1 alone changes them (L-COMP #2 lists O1; exhaustive n ≤ 3 shows
0 count differences only because introsort is stable below 17 elements) and L22/D-4 claims every O1. Unique counts need O1
pinned too, i.e. the unstable `std::sort` written into the statement and D-4 reversed. Also the pinned outs(v) order makes the
statement depend on the INPUT FILE's edge order, not on the game: two encodings of the same game are then two runs with
different counts, and D2 would be a statement about encodings. And a future GAP-A proof could lean on an order accident
(e.g. "the tangle vertices are explored in ascending index") without anyone noticing it is an accident.

## 4. Option (ii): claim D1 and D2 for every order
Text that would be added to C5-DTL.md §0 ("Order data"):
> The pseudocode is parametrised by order data fixed before the run: (O1) a vertex indexing non-decreasing in priority;
> (O2) for each v a list ins(v) containing each predecessor once per edge; (O3) for each v a list outs(v) of its successors;
> (O3') for each extractTangles call, an order in which the nontrivial SCCs reachable from top are processed and, for each
> SCC, an order of its vertices (used only for dom_vector); (O4) tv[t] sorted ascending by index (this one is the code,
> dtl.cpp 389, not a free choice); (O5) dom_vector in O3' order, LIFO pops; (O6) "Q := all of Z" pushes in any order;
> (O7) tin[v] iterated in creation order; (O8) iterations_dtl = number of search calls, iterations_idtl = ⌊calls/2⌋ + 1.
> Oink @ 8fbf0a7 is the instance: O1 = std::sort, O2 = decreasing index, O3 = input order renamed, O3' = Pearce order,
> O6 = increasing index (the list of §3 above).
Statement changes (for the Lead and CHECKER; DTL-proof.md §0 untouched here): §0.1 "every such order" → "every order datum
(C5 §0 Order data)"; §0.3 "tangles(G)" → "tangles(G, ω), the final value of `tangles` under order datum ω; (a) tangles(G, ω) ≤
p_a(n + m) for every ω" and the same for (b)-(e); §0.3 (d) for A_IDTL: "the counter `iterations` is ⌊calls/2⌋ + 1 (1125), so
a bound on calls bounds it" (a wording fix: at present (d) identifies the counter with the number of calls, which is exact
for dtl only); §0.4 "the stack Q and Oink's edge-list order fix every choice" → "for a fixed order datum, deterministic".
Cost to the proof: zero for everything PROVED (§2: all arguments hold for fixed arbitrary order data). For GAP-A: whatever
bounds tangles must do so for every ω. This is not a real loss of strength: O1 and O3 ARE the input encoding (vertex names
within a priority, edge line order), so the adversary of D2 already chooses them; O2, O3', O5 are functions of O1 and O3
under Oink; so "every ω" adds only the freedom to pick O2/O3'/O6 independently of O1/O3, and a bound that needs Oink's
coupling of them would be a bound about the parser, not about DTL. What is given up explicitly: uniqueness of counts. The
second implementation's role is then: regions and strategies must agree for ANY two order data (measured: yes), counts must
agree at EQUAL order data (measured: yes, `--order oink`), and the C5-literal counts are a second sample of the same bound.
§7 signs that Oink's choices are one instance of the order data (the list above), which L-COMP's `--order oink` mode
demonstrates mechanically on 238,071 games.
Risk to name: a counter shape that needs an adversarial O2 (e.g. ins order chosen per vertex to steer DFS parents) would
kill D2 under (ii) but not under (i). I would want to know that anyway: a DTL whose polynomiality depends on the in-edge
array being filled from the end is not the algorithm the fleet wants to claim.

## 5. Recommendation: (ii), with Oink's instance recorded
1. L22/D-4 already chose (ii) for O1; (i) cannot make counts unique without reversing it.
2. Nothing proved depends on an order; the proofs are already written for fixed arbitrary order data.
3. The extra generality is mostly reachable through the input encoding, so (ii) is barely stronger than (i) as a claim, and
   it keeps the GAP-A proof honest (no order accident can enter).
4. The unique-object requirement is met in the only sense that matters for a theorem: C5 + order datum ω is a deterministic
   program, and D1/D2 quantify over ω. What L-COMP needs for step 2 is the recorded instance (the list in §3), which it has.
Concrete edits if accepted: C5-DTL.md §0 gets the "Order data" paragraph of §4 (L-ALG file); DTL-proof.md §0.1, §0.3, §0.4 get
the four wording changes of §4 (Lead + CHECKER); DTL-proof.md §7 gets the seven instance rows (L-ALG, signed later).
If the Lead prefers (i): use the §3 text, keep D-4 as it is, and record in §0 that counts are unique only up to O1.

## 6. Two code facts found while drafting, for the proof (either option)
F1. Deletion is order-sensitive in a second way (O4): attractTangle (125-141) checks the stored vertices in tv order and
    returns "delete" at the first solved vertex but "false, keep" at the first vertex outside R; with tv sorted ascending a
    tangle with a low-index solved vertex and a high-index vertex outside R is deleted, the mirror tangle is kept. The
    deletion charge in DTL-proof.md §3(a) (M-cross caveat) counts deletions once per tangle, which is order-free; only
    WHEN a tangle is deleted varies.
F2. The −1 threshold vertices and the dominion-extension attractor use `str` as DFS parents too (1036-1037, −1 threshold);
    the output strategy sigma(v) for a vertex solved during the extension is the parent under O5's LIFO order, so the
    output strategy depends on O5 in principle; D1 claims only that it wins (§2.1 (s4) covers 1036-1037). Measured equal.
