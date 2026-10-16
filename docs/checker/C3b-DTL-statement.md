# C3b: re-check of DTL's step-4 statement (CHECKER, 2026-10-15 ~17:50Z)

Target: docs/alg/DTL-proof.md §0 and §1.0 at claude/l-alg ccff864, revised after C3 (docs/checker/C3-DTL-statement.md,
checker 5b924e7) and Lead reading L22. Code: Oink 8fbf0a7 (tools/oink/src, clean): dtl.cpp, solve.cpp, oink.cpp,
pgparser.cpp, uintqueue.hpp. Text only; no re-runs. No judgement on the mathematics of the proofs. Where the code
contradicts a "PROVED (reading)" claim in §1.0, I report it as a reading error.

## Verdict: §0 PASS; §1.0 FAIL (three reading claims do not match dtl.cpp). Overall FAIL until §1.0 is corrected.
| item | verdict |
| --- | --- |
| (1) C3 items fixed or explicitly deferred | PASS (all 15; deferrals explicit) |
| (2) §1.0 consistent with dtl.cpp @ 8fbf0a7 | **FAIL**: (s3) and (s4) contradict the code; (s2) is imprecise |
| (3) §0 over-claims vs TARGET §1-3, §5 | PASS (notes N-1, N-2) |
§0 can be frozen as the step-4 statement now. §1.0 is proof text and needs correcting before a referee reads §1-2.

## (1) C3 items
| C3 item | at ccff864 | |
| --- | --- | --- |
| A-1 input construction charged | §0.1 "Step 0 (input construction, charged)": PGSolver text, parser with --no-loops, edge arrays, sort; D2(e) "measured from TARGET's encoding and including step 0" | FIXED |
| A-2 comment at 1107 vs code | §0.1 "the comment at 1107 says the opposite; the code is followed" | FIXED |
| B-1 "by construction" | D2(e): counters "are at most the number of steps executed ... once (e) holds (B-1; not 'by construction')" | FIXED |
| B-2 int as RAM word | §0.3 "C++ `int` and `unsigned int` are words of TARGET section 3's RAM" | FIXED |
| B-3 uncharged costs | D2(e) names the duplicate checks (O(tangles(G)·n) per extracted SCC), tangle storage with `tin`, dominion removal | FIXED |
| C-1 compression | §0.4: list of priority uses (I checked 74, 117-118, 134, 140, 215, 461, 721-722, 898-904, 937-938, 1036-1037, 1088, game.cpp:495 against the code; 585/594/613/1008 are in NDEBUG-only code, as stated); sentences (i) and (ii) added; compression before parsing | FIXED |
| D-1 self-loops | A_DTL = `oink --dtl --no-single --no-wcwc --no-loops`. `--no-loops` turns off both the parser's removal (solve.cpp:263, `removeBadLoops` = false) and solveSelfloops (solve.cpp:329). Re-runs listed in §6 (n ≤ 3 exhaustive and the library; the n = 4 sections are "not re-run here", explicit) | FIXED; n = 4 re-run deferred explicitly |
| D-2 CHECK_UNIQUE | §0.1 names it; D2(a) counts tangles kept after the check | FIXED |
| D-3 trace = 0 | §0.1 pins trace = 0, citing 349-354 | FIXED |
| D-4 tie order | D1, D2 "for every order of equal-priority vertices"; §0.4 determinism note | FIXED |
| E-1 Lean | §0.4: "the Lean formalisation of correctness (TARGET section 6) is still owed and is L-FORMAL's" | DEFERRED explicitly |
| E-2 single object | §0.1: analysed object = C5-DTL.md (pinning paragraph at C5-DTL.md:8-10); correspondence §7, "to be signed separately" | FIXED (N-1) |
| E-3 measure from encoding | D2(e); option (i), so p_e is over the input game | FIXED |

## (2) §1.0 against dtl.cpp @ 8fbf0a7
Correct as read:
- Tie order: the loops cited (481, 691, 713, 878, 936, 962; ascending 899) are index sweeps.
- (s1): line 73, `if (owner(from) == pl and str[from] == -1) str[from] = v`, with from = v = τ at τ's own pop, gives
  str[τ] = τ for a p-owned top with a self-loop; 316 `(unsigned)str[n] == n` makes {τ} nontrivial.
- (s2) first sentence: at 78-85 an opponent-owned `from` with a self-loop sees `to = from` with `G[to] and !Z[to]`.
  Every call site passes Gx ⊇ R (494, 700, 729, 886, 921, 973 pass Gx = R; 1036 Gx = G), so the loop is an escape.
- `Q` is a stack: uintqueue.hpp:72-75, `pop()` returns `queue[--pointer]`.

Reading errors (FAIL):
- R-1, (s3), last clause. "For an opponent-owned v the loop is a successor in R \ Z unless v ∈ Z, so an opponent-owned
  candidate with a self-loop never attracts (714, 738) and is pruned" — contradicted by the code.
  - At 714 the set Z is the union of the regions of the round. The loop at 691-705 gives every v ∈ V a region (top,
    `CurZ[top] = true`) or finds it in a higher one (`!Z[top]`), so V ⊆ Z.
  - At 738 the set is A_t ⊇ Reg ⊇ V.
  - So for a candidate v the "unless v ∈ Z" case always applies. In attracts (40-57) the self-loop is a successor in Z
    (`hasZ = true`), not an escape.
  - An opponent-owned candidate with a self-loop attracts iff it has no successor in R \ Z. It is not pruned
    unconditionally.
  - Also, by the same lines (43-46), a p-owned v ∈ V with a self-loop always satisfies attracts(p, v, Z, ·), since
    v ∈ Z: it is never a candidate and never pruned. §1.0 does not state this.
- R-2, (s4). "str is set at 89 to the popped vertex v ≠ u ... or at 171 ...; the only self-assignment is (s1) at a top" —
  contradicted by search_rec 898-923.
  - The scan at 899-911 puts every v ∈ R with priority ≤ t and `attracts(player, v, X, R)` into Z with `str[v] = -1`
    (908) and pushes it. These are not tops: any priority ≤ t, any parity, either owner.
  - At v's pop (919-922, `attractVertices(player, u, R, Z, R, t)`), line 73 runs for every predecessor already in Z
    with str = -1. That includes v itself when v has a self-loop (v ∈ ins(v)), and it can run before any other Z-successor
    of v is popped (LIFO).
  - So a p-owned non-top v with a self-loop of opponent parity can get str[v] = v.
  - §1.2's own "Strategy assignment" paragraph lists 908 among the str = -1 start sites, so §1.0 (s4) also contradicts §1.2.
  - Whether this str value matters later (it may be overwritten by later regions) is for the proof. The reading claim
    as written is false.
- R-3, (s2), imprecise. "Then {u} is extracted by 317 (`str[n] == -1 and has_edge(n, n)`)".
  - The closed test at 519-525 checks u's successors against the CONSUMED R. Successors of u that lie in Z (attracted
    after u's pop and removed from R at 490) do not open the region.
  - Pearce's restricted graph (234-266) keeps u's edges into Z. If u has a successor w ∈ Z, w reaches u inside Z (w was
    attracted toward u), so u's SCC contains w and is nontrivial by size (315).
  - So {u} is the extracted SCC only when u has no successor in Z other than itself. Say so.

## (3) §0 against TARGET §1-3, §5
- §1 objects, encoding (n, owner bits, binary priorities, edge list), pr into {0..n}, self-loops allowed, max-parity,
  general strategies: as TARGET.
- §2: D1 gives (W_E(G), W_O(G)) with completeness; D2(e) gives p(n + m) from TARGET's encoding. Deterministic: A_DTL with
  the pinned build is deterministic, and the theorems hold for every tie order, which covers the one the library
  picks. As TARGET.
- §3: word RAM, unit cost = bit cost argued through D2(e)'s bound on every number. As TARGET.
- §5: step 2 re-runs on the pinned command (partly done, n = 4 deferred), step 4 prose + Lean owed (explicit), change 5
  strategies in D1. No over-claim found.
- N-1 (note). D1 and D2 are stated for A_DTL (the pinned C++ run) and proved on C5-DTL.md, with §7 as the bridge. D2(a)-(d)
  name C++ counters and line ranges.
  - That is consistent with E-2 only once §7 is signed. Until then a proof of D1/D2 on the pseudocode is a proof about
    A_DTL only through an unsigned correspondence.
  - §0.1 says this ("to be signed on its own").
- N-2 (note). §6 records the status of step 4 itself: 2.3 completeness is SKETCH (GAP-C) and 3(a) tangle count is GAP-A.
  So D1 and D2 are not proved yet. That is expected for a statement check, and §0 claims nothing beyond the statement.

## Fixes for PASS
1. R-1: correct (s3).
   - Candidates at 714/738 always lie in Z, so the self-loop counts as a successor in Z.
   - A p-owned V-vertex with a self-loop is never a candidate.
   - An opponent-owned one attracts iff it has no successor in R \ Z.
   - Then re-check every later use of (s3) in §1.6 and §2.3.
2. R-2: correct (s4) to include line 73 at the start set of 898-911 (str = -1 at 908); fix or restrict "the only
   self-assignment is (s1)", and re-check the uses in TS (§1.3).
3. R-3: restrict the (s2) singleton extraction to "u has no successor in Z other than itself".
After these, the CHECKER re-reads §1.0 only; §0 stands as checked here.
