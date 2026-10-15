# DTL: proof attempt for gauntlet step 4 (correctness and running time) — L-ALG, 2026-10-15

Status: IN PROGRESS (box 15:50Z-23:50Z). Every step below is marked PROVED / SKETCH / GAP. Nothing here is a result
until two referees sign it (CLAUDE.md). The object is van Dijk's research solver `dtl` in Oink at commit 8fbf0a7,
file src/solvers/dtl.cpp (line numbers below are of that file, release build: code under `#ifndef NDEBUG` and `trace`
is not part of the algorithm). Pseudocode: docs/alg/candidates/C5-DTL.md. Independent adversary: L-RED R8
(docs/red/R8-DTL.md, claude/l-red d6496f3); its Lemma M is unrefereed and is re-proved here where used, never cited.

## 0. Statement (written first; revised 17:45Z after CHECKER C3, docs/checker/C3-DTL-statement.md, claude/checker 5b924e7)

### 0.1 The algorithm A_DTL (what is claimed about)
Input: a parity game G = (V, V_E, V_O, E, pr) in TARGET section 1's encoding: n, the owner bit of each vertex, pr(v) in
binary with pr : V -> {0, ..., n}, and the edge list; V finite, every vertex has a successor (self-loops allowed, losing
ones included), max-parity; n = |V|, m = |E|, input length Θ((n + m) log n). If priorities outside {0..n} are given,
TARGET's compression (sort, keep order and parity) is applied first, on the encoding, before anything else (C-1).
Step 0 (input construction, charged): write the game in PGSolver text and run Oink's parser
`PGParser::parse_pgsolver_renumber` with bad-loop removal OFF (`--no-loops`, src/tools/solve.cpp:263), which builds the
out- and in-edge arrays (O((n + m) log n) word operations); then `game.ensure_sorted()` (oink.cpp:35; game.cpp:495
`std::sort` on priorities), i.e. reindex the vertices in SOME order that is non-decreasing in priority. Equal-priority
vertices may come out in any order (D-4): Theorems D1 and D2 are claimed for EVERY such order.
Step 1: `DTLSolver::run()` (dtl.cpp 1072-1161) with `interleaved = false`, all vertices enabled, G := V, as reached by
the command `oink --dtl --no-single --no-wcwc --no-loops` (the pinned A_DTL; Lead decision D-1 option (i), 16:02Z):
no single-parity solving, no winner-controlled-cycle removal, no self-loop removal by the parser or by
`Oink::solveSelfloops`, no inflate/compress/renumber, no bottom-SCC loop, release build (`NDEBUG`, scripts/setup_oink.sh:19),
`trace = 0` (D-3: with trace ≥ 1 a dominion at recursion depth ≠ 0 would call exit(-1) at dtl.cpp 349-354; with trace = 0 it
is accepted). The duplicate-tangle block dtl.cpp 385-424 IS part of the algorithm (`#define CHECK_UNIQUE (1 or !NDEBUG)`,
line 23): a new SCC whose sorted vertex set equals a stored tangle's (strategies not compared) is discarded and does
not count as a change (D-2). The loops 1109-1121 run Even's search to exhaustion, then Odd's (the comment at 1107 says
the opposite; the code is followed, A-2). Output: for every vertex v solved by `Solver::solve(v, player, str[v])` (1034): v
is put in W_player and, if owner(v) = player, sigma_player(v) := str[v]. Vertices never solved are output as unsolved
(Oink::solveLoop, oink.cpp:405-420, returns after run()). A_IDTL is the same with `interleaved = true` (1125-1138).
The ANALYSED OBJECT (E-2) is the pseudocode docs/alg/candidates/C5-DTL.md, updated to this pinned A_DTL (stack,
consumption, CHECK_UNIQUE, trace = 0, self-loops as given). Every proof below is about that pseudocode; the line numbers
of dtl.cpp are given so that the correspondence can be checked. The C++ ↔ pseudocode correspondence is a separate
itemised section (section 7) to be signed on its own (TARGET section 6, D2 change 2).

### 0.2 Theorem D1 (correctness and completeness)
For every parity game G as in 0.1 and every order of equal-priority vertices in step 0, A_DTL halts, solves every vertex
exactly once, and the output satisfies W_Even = W_E(G) and W_Odd = W_O(G) (TARGET section 1: W_E(G) = vertices from which
Even has a strategy, general = history-dependent, winning every consistent play under max-parity; W_O likewise;
W_E ⊔ W_O = V by determinacy). Moreover sigma_Even is a positional strategy on W_Even ∩ V_E such that every play starting in
W_Even, consistent with sigma_Even, against every (general) Odd strategy, stays in W_Even and is won by Even;
symmetrically sigma_Odd on W_Odd ∩ V_O. Same statement for A_IDTL, with "the exception `solver stuck` (line 1136) is never
thrown" added.

### 0.3 Theorem D2 (running time, word RAM of TARGET section 3)
Let tangles(G) be the final value of the counter `tangles` (line 463; it counts tangles KEPT after the duplicate check)
and dominions(G) of `dominions` (line 375). A_DTL is read as a RAM program whose C++ `int` and `unsigned int` are words
of TARGET section 3's RAM (B-2): the claim is about that RAM program, not about 32-bit overflow behaviour. There are
polynomials p_a, ..., p_e such that for every G as in 0.1 and every tie order:
  (a) tangles(G) ≤ p_a(n + m);
  (b) every call of best_vertices (643-776) executes at most p_b(n + m) pruning rounds (iterations of 674-773);
  (c) every call of search_rec (834-994), with its recursive calls, executes at most p_c(n + m) iterations of its loop
      850-993, at recursion depth ≤ d ≤ n + 1;
  (d) the number of calls of search (997-1069), i.e. the counter `iterations` (1111, 1119), is at most p_d(n + m);
  (e) the total number of word operations of A_DTL, measured from TARGET's encoding and including step 0 (compression
      if needed, parsing, edge arrays, sorting), the duplicate-tangle checks (385-424: O(tangles(G) · n) per extracted
      SCC), the tangle storage (443-458: O(n) per kept tangle, `tin` back-links included) and the dominion removal
      (1023-1040), is at most p_e(n + m), on a word RAM with words of O(log(n + m)) bits. Every number the program
      manipulates is a vertex index (< n), a priority or threshold (≤ n + 1 after compression; the sentinels -1 at
      lines 74, 117, 1036 and the initial thresholds 0 at 585/898 are constants), a queue/stack position (≤ n), a bit of
      an n-bit bitset (copies and resets cost O(n / w) words), or one of `tangles`, `dominions`, `iterations`, a tangle
      index: these are at most the number of steps executed, so they have O(log(n + m)) bits once (e) holds (B-1; not
      "by construction"). The unit-cost count therefore equals the bit-cost count up to the word-size constant.
Same for A_IDTL.

### 0.4 Diff against TARGET.md v1.0
- Section 1, objects: identical (finite V, successor-closed, self-loops allowed, pr into {0..n}, max-parity, general
  strategies in the definition of W_E, W_O). Priorities are used by dtl.cpp as follows (C-1, complete list): comparisons
  with a threshold `priority(u) <= t`, `priority(v) > t`, `priority(u) == t` (74, 140, 594, 613, 737, 901, 904, 937, 938)
  and through attracts (714, 738, 906); parity `& 1` (118, 215, 663, 1008, 1088); the loop `for (t = 0; t <= max_prio; t++)`
  with `max_prio = priority(nodecount()-1)` (721-722); initial thresholds `t = 0` at 585 (NDEBUG only) and 898 and
  `t = priority(v)` at 904; the sentinel `max_prio < 0` with -1 (74, 1036-1037) and `tpr[t] == -1` for deleted tangles
  (117, 134, 461 stores a priority); `std::sort` by priority (game.cpp:495). Commutation with TARGET's compression
  (applied before parsing, so Oink's int priorities never overflow): compression preserves order and parity, so every
  threshold comparison and parity test gives the same result on both games provided thresholds are mapped along;
  (i) an iteration of 721-722 at a threshold t such that no priority lies in (t', t] (t' the largest occurring
  priority ≤ t) attracts nothing new (every rule compares `priority ≤ t`, and the sets reached at t' and t coincide)
  and clears no candidate (737-738 test the same set), so the sequence of visited states is the same and only the
  number of empty iterations differs; (ii) the initial `t = 0` at 898 is compared only with occurring priorities and
  then replaced by `priority(v)` (904), so it acts as "below the least occurring priority" in both games (and a
  vertex of priority 0 attracts to X at level 0 in both). Hence A_DTL makes the same choices on G and on its
  compression, and the bound (e) is stated for the compressed game, whose n and m are the input's.
- Section 2, target statement: TARGET asks for (W_E(G), W_O(G)); D1 gives these as (W_Even, W_Odd) plus strategies.
  "Halts within p(n + m) steps": D2(e), measured from TARGET's encoding (E-3). Deterministic: for a fixed tie order yes
  (no randomness; the stack `Q` and Oink's edge-list order fix every choice); the theorems are claimed for every tie
  order, so the choice made by `std::sort` does not matter (D-4).
- Section 3, model: word RAM, O(log(n + m))-bit words: D2(e) as stated.
- D2 change 5 (strategies): D1 outputs positional strategies and states they win; the fleet's L-COMP check (step 2,
  to be re-run on the pinned command with `--no-loops`) verifies them on every test game.
- Section 5 step 4 / section 6 (E-1): D1 and D2 with their proofs are the refereed-only part of step 4; the Lean
  formalisation of correctness (TARGET section 6) is still owed and is L-FORMAL's; D2 change 2's correspondence item is
  section 7.
- Not claimed: anything about Oink's preprocessing, `--inflate/--compress`, parallel solvers, or games with disabled
  vertices. Evidence gathered before 16:02Z used the command without `--no-loops` (parser bad-loop removal and
  solveSelfloops on) and is therefore about a different algorithm on games with losing self-loops; the re-runs with
  `--no-loops` are listed in section 6.

### 0.5 What a GAP looks like here
If a step below is a GAP, the deliverable is the exact failing claim and a candidate instance shape (section 5).
Lead/L-RED route it; L-ALG does not contact L-RED.

## 1. Primitives and invariants (dtl.cpp 40-202, 210-471, 643-776)

Notation. G' := the member bitset `G` (unsolved vertices; 1082-1083, shrinks at 1035). T := the stored tangles
(`tv`, `tout`, `tpr`, `tin`; a tangle with tpr = -1 is deleted). p := the player of the current search; "opponent" = 1-p.
Vertices are indexed in non-decreasing priority (oink.cpp:35), so "for v from n-1 down" is a descending-priority sweep.
P_p := vertices whose priority has parity p. A "tangle attractor to Z_0 within R, escapes judged in Gx, threshold t"
is the loop pattern "Q := Z_0; while Q: v := pop; [R := R \ {v}]; attractVertices(p, v, R, Z, Gx, t);
attractTangles(p, v, R, Z, Gx, t)" (sptl 488-496, best_vertices 697-702 and 727-731, search_rec 883-888, 918-923,
967-975, search 1032-1038). Q is a STACK: uintqueue.hpp `pop()` returns `queue[--pointer]` (LIFO). The brief's phrase
"FIFO attractor order" does not describe the code; nothing below depends on FIFO.

### 1.0 Tie order and self-loops — PROVED (reading)
Tie order (D-4). Every argument below uses the index order only through "descending index = non-increasing priority"
(the loops 481, 691, 713, 878, 936, 962 and the ascending scan 899); no argument compares the indices of two vertices of
equal priority, and every set computed (attractors, regions, A, V) is the same for every tie order (Lemma 1.2: closures
are order-independent; the region decomposition processes equal-priority tops in index order, and the proofs only use
that a top processed earlier has priority ≥ a top processed later). The strategies str and the extracted SCCs DO depend
on the order; the theorems are claimed for each order and every proof below holds for each order.
Self-loops (D-1). A self-loop v → v is in outs(v) and ins(v). Effects, each covered where used: (s1) at the pop of a
region's top τ, τ ∈ ins(τ) with τ ∈ Z and str[τ] = -1, so a p-owned top with a self-loop gets str[τ] := τ (73) and the
region is closed at once; the SCC {τ} is nontrivial by 316 (`str[n] == n`), and its cycle has priority pr(τ) of parity p:
TS(ii) holds. (s2) An opponent-owned vertex u with a self-loop is never attracted by rule (V): at 78-85 its loop is a
successor in Gx \ Z while u ∉ Z. It can enter an attractor only through rule (T) or as the start vertex; as an
opponent-owned top of p-parity priority (u ∈ V), its region is closed iff all its other successors are outside R
(519-525; the loop target u itself is removed from R at 490), and then {u} is extracted by 317 (`str[n] == -1 and
has_edge(n, n)`) with escapes = u's other G'-successors outside {u}: a dominion iff it has none. (s3) attracts (40-57) for a
p-owned v with a self-loop: the loop counts iff v ∈ Z; for an opponent-owned v the loop is a successor in R \ Z unless
v ∈ Z, so an opponent-owned candidate with a self-loop never attracts (714, 738) and is pruned; it is solved, if p-won,
as a top (s2) or through a tangle. (s4) A p-vertex u ≠ top with a losing self-loop (opponent parity) never has str[u] = u:
str is set at 89 to the popped vertex v ≠ u (u ∉ Z at that time, so u is not being popped) or at 171 to a tangle
strategy, and tangle strategies at u are set by 89/73 in an earlier region; the only self-assignment is (s1) at a top,
whose priority has parity p. So every cycle used in TS is as analysed in 1.3, with the loop case (s1) included.
### 1.1 attracts (40-57) — PROVED (reading)
attracts(p, v, Z, R) = [owner(v) = p and v has a successor in Z] or [owner(v) != p and v has a successor in Z and no
successor in R \ Z]. Edges to vertices outside R ∪ Z are ignored (lines 52-55). This is the "escapes to outside R are
forgiven for p" convention; it is used with R = the current search_rec region and Z = X (906), Z = the union of regions
(714, 738).

### 1.2 Attractor semantics — PROVED
Lemma 1.2. The loop pattern above, started with Z = Z_0 and Q = Z_0 (every vertex of Z_0 on the stack), ends with Z =
the least set containing Z_0 and closed under
 (V) u ∈ R, (t < 0 or pr(u) ≤ t), and [owner(u) = p and u has a successor in Z] or [owner(u) != p, u has a successor
     in Z, and no successor in Gx \ Z]   (74-90; "successor in Z" because u is a predecessor of the popped v ∈ Z);
 (T) a tangle t' with tpr != -1, tpr ≡ p (117-118), all vertices in G' (132-135), all vertices in R ∪ Z (138), at
     least one not in Z (146), all vertices of priority ≤ t when t ≥ 0 (140), every escape in Z or outside Gx
     (152-158), AND at least one escape in Z (200-201: attractTangle is only called for t' ∈ tin[v] at the pop of
     v ∈ Z). Its vertices not in Z are added (163-182).
Proof. Every vertex that enters Z is pushed (90, 172) and popped exactly once; when v is popped, every predecessor of v
is checked against (V) (69-100) and every tangle with escape v against (T) (200-201). A (V)-premise for u becomes true
only when a successor of u enters Z (p's u) or when the last Gx-successor of u enters Z (opponent's u); that successor
is popped later, and u is checked then. A (T)-premise becomes true only when the last escape of t' inside Gx enters Z
(or holds from the start, in which case it needs some escape in Z to be checked at all); that escape is popped later.
Removing popped vertices from R (callers 490, 699, 885, 920, 969) does not change the closure: a popped vertex is in Z.
Minimality: every addition is justified by a rule. □
Consequence 1.2a (NOTE N1). A tangle whose escapes all lie outside Gx (e.g. all in higher regions or in X) is NEVER
attracted as a unit; its vertices enter Z, if at all, by (V). (Relevant to completeness, section 2.3.)
Consequence 1.2b (monotonicity in T). With T ⊆ T' (same Z_0, R, Gx, t) the closure under T' contains the closure under
T: rule (T) for an old tangle has the same premise and (V) is unchanged. (This is R8's (M1), re-proved.)
Strategy assignment (73, 89, 171): a p-vertex u pushed by (V) at the pop of v gets str[u] := v; a p-vertex pushed by (T)
gets its tangle strategy; a p-vertex already in Z with str = -1 (only the start vertex of a region, 485/694/881/965/908)
gets str := v at the first pop of a successor v (73). Membership of Z is order-independent (Lemma 1.2); str is not.

### 1.3 Every stored tangle is a p-tangle — PROVED
Definition. A stored tangle t = (U, s, O) with U = its vertex set (tv), s = its strategy on U ∩ V_p, O = tout. Property
TS(t): (i) s(u) ∈ U for u ∈ U ∩ V_p; (ii) in the graph H_t on U where p-vertices have the single edge s(u) and opponent
vertices keep all their edges inside U, every cycle has a maximum priority of parity p; (iii) every edge from an
opponent vertex of U to a vertex outside U goes to O or to a vertex solved at creation time (333: escapes are computed
against G').
Lemma 1.3. TS(t) holds for every tangle at creation, hence always (tangles are immutable; deletion only).
Proof by induction on creation order. Tangles are created only at 439-466 inside extractTangles, called only from sptl
539 on a closed region Z := the attractor to {top} within R (consumed) with threshold pr(top) (481-496). Let π(u) be
the push order in that attractor (top first). Facts: (F1) every u ∈ Z has pr(u) ≤ pr(top) (74, 140). (F2) a p-vertex
u ≠ top pushed by (V) has str[u] = v with π(v) < π(u) (v was in Z when u was pushed, 89). (F3) an opponent vertex
u ≠ top pushed by (V) at the pop of v: every successor of u lies in Z_then (π < π(u)) or outside R_start ∪ Z (R_start =
R at the start of this region; R_then ∪ Z_then ⊇ R_start). (F4) a vertex u pushed by (T) for tangle t': all vertices
of t' not yet in Z are pushed consecutively (164-172); u's p-strategy is s_{t'}(u) ∈ U_{t'}; an opponent u ∈ U_{t'} has
successors in U_{t'}, in O_{t'} ⊆ Z_then ∪ (outside Gx = R_then) (152-158), or solved. (F5) the top: closed means
str[top] != -1 if p-owned (515), i.e. top has a successor in Z (73); if opponent-owned, no successor in R_then (519-525).
Claim: every infinite play ρ inside Z consistent with str (p follows str; the opponent uses edges inside Z) either
visits top infinitely often or has a tail inside U_{t'} for one older tangle t' with p following s_{t'}. Proof: if top is
not visited infinitely often, drop a prefix so that ρ avoids top; let u* be the vertex of minimum π visited infinitely
often and drop a prefix so that all visited vertices have π ≥ π(u*). u* cannot be a (V)-pushed p-vertex (its str moves
to lower π, F2) nor a (V)-pushed opponent vertex (all its successors inside Z have lower π, F3). So u* was pushed by (T)
for some t'. Every vertex of U_{t'} either has π < π(u*) (it was in Z before t' fired) or was pushed by the same event
(F4). Hence the tail stays in the vertices of U_{t'} pushed by that event, p uses s_{t'} there (F4), and the opponent
uses edges inside U_{t'} (its other successors have lower π or lie outside Z). □(claim)
Now let C be an SCC extracted at 290-305, nontrivial (315-317). (i): a p-vertex n ∈ C has the single edge str[n] in the
restricted graph (268-285), and n lies on a cycle of C, so str[n] ∈ C. (iii): by construction 327-341. (ii): a cycle of
H_C is an infinite play inside Z consistent with str; by the claim it visits top infinitely often (then its maximum
priority is pr(top) by F1, parity p) or has a tail in an older tangle t' with p following s_{t'}; by the induction
hypothesis TS(t')(ii) applied to the cycle of that tail, the maximum priority has parity p. (Infinite play to cycle: the
set of vertices visited infinitely often is strongly connected in the play graph and its maximum-priority vertex lies on
a cycle inside it with that maximum.) □
Corollary 1.3a (tangle usability). If a tangle t' is attracted into an attractor Z (rule T), every play consistent with
the resulting str that stays in U_{t'} is won by p, and every exit of the opponent from U_{t'} lands in Z (escape in Z),
outside Gx, or in a solved vertex.

### 1.4 Dominions and their removal — PROVED
Lemma 1.4a. A set C extracted with escapes(C) = ∅ (347-379) is a p-dominion in G': p's strategy str keeps the play in C
(TS(i)), every opponent edge from C stays in C or goes to a solved vertex (TS(iii)), and every cycle of H_C has parity p
(TS(ii)); every infinite play in C ∪ (solved) consistent with str that stays in C is won by p.
Lemma 1.4b (trap property of dominion removal, 1023-1040). After the loop 1032-1038 for player p with solved set S:
(1) every vertex of S has a strategy (str) with which p wins from S against every opponent strategy in the whole game,
given that the vertices solved earlier are won by their recorded player (induction over solve order);
(2) no p-vertex of G' \ S has a successor in S, and every opponent vertex of G' \ S has a successor in G' \ S.
Proof. (2): attractVertices(p, v, G', S, G', -1) is run for every v ∈ S (every solved vertex is pushed, 1028/1036 via
90, and popped, 1033): a p-vertex of G' with an edge to v is attracted (74-90 with max_prio = -1 and owner = p), an
opponent vertex is attracted unless it has a successor in G' \ S (75-86). (1): by induction on the push order of S; the
dominion core (1024-1030) is won by Lemma 1.4a; a (V)-attracted p-vertex moves to an earlier-pushed vertex (89), an
attracted opponent vertex has all G'-successors in S_then (85) and its other successors in earlier-solved vertices, where
the earlier player wins; by (2) applied to the earlier solved sets, the opponent of the earlier player never has an
edge from G' into that player's solved set, so "earlier-solved vertex" means: solved for p (fine for p), or solved for
the opponent of p, which the opponent's vertex may enter — but then the play left S into a set won by the opponent
of... (this case cannot occur: an opponent-of-p vertex u ∈ S attracted at 75-86 has no successor in G' \ S; its
successors outside G' are solved; a successor solved for the opponent of p would have attracted u into that solved
set at that earlier removal by (2) for that player, contradiction with u ∈ G' now). A tangle-attracted vertex (1037)
follows its tangle strategy (Corollary 1.3a) until the play exits into S_then. So every play from S consistent with
str stays in S ∪ (p's earlier solved sets) and its tail is in a dominion core or an attracted tangle: won by p. □
Lemma 1.4c (the subgame). After removals, the subgame G' with all edges leaving G' deleted is a parity game (every
vertex keeps a successor, Lemma 1.4b(2) applied to both players), and W_p(G'-subgame) = W_p(G) ∩ G' for both p: an edge
from G' into a solved set S_q (q ∈ {Even, Odd}) exists only from q's opponent's vertices (Lemma 1.4b(2)), who lose by
using it (Lemma 1.4b(1)). All of dtl.cpp's attraction ignores edges leaving G' (1.1, 1.2, 333), i.e. runs on this subgame.

### 1.5 extractTangles — PROVED (reading)
On a closed region Z with its str, Pearce's algorithm from top (223-305) enumerates every SCC of the restricted graph
(p-vertices: the edge str[n] (268-285); opponent vertices: all edges into Z (234-266)) that is reachable from top, in
reverse topological order. Each nontrivial SCC (315-317) is a dominion if it has no escapes (347-379), else skipped if
its sorted vertex set equals a stored tangle's (385-424, CHECK_UNIQUE is `(1 or !NDEBUG)` = on), else stored (439-466)
with tin back-links (443) and tpr := pr(top) (461). NOTE N2: non-bottom SCCs are extracted too (their escapes may lie in
Z); NOTE N3: a closed region whose top is opponent-owned with all successors outside Z extracts nothing ({top} is
trivial unless it has a self-loop, 317).

### 1.6 The pruning round (643-776) — PROVED (reading, corrected against C5-DTL.md)
Round: regions Z_τ for the tops τ ∈ V in descending index, computed in ONE copy CurR of R that is consumed across tops
(690, 699): a top already inside a higher region gets no region (692). Hence Reg(V) := ∪ Z_τ is a disjoint top-down
decomposition; R_rem := R \ Reg(V). Candidates (712-716): v ∈ V with ¬attracts(p, v, Reg, R) (opponent-owned v: it
needs a successor in Reg and none in R \ Reg; note R here is the UNconsumed search_rec region). Threshold loop
(721-741): A_t := attractor to Reg within R (not consumed) with threshold t, cumulatively for t = 0..max priority; a
candidate u is cleared iff attracts(p, u, A_t, R) for some t < pr(u) (737: the scan over the descending candidate list
stops at the first candidate with pr(u) ≤ t, so clearing happens only for t strictly below pr(u)). Remaining candidates
leave V (752). Return 1 if nothing left or no candidates (716, 767), -1 with V := the previous round's V if V became
empty (768-771), else next round.
NOTE N5 (the pruning is an iteration, not a greatest fixpoint of a monotone operator). Write F(V) for the set of
survivors of one round started from V. R8 (M2) calls V* "the largest V such that ..."; that presumes F monotone (V ⊆ V'
⇒ F(V) ⊆ F(V')). F is monotone when no stored tangle straddles, but not in general: let t' = {a, c, d} be stored with
strategy a → c, c → d, where d (opponent-owned) has edges to c, a and to an escape e, pr(a) = max (p-parity) and
pr(c) > pr(d) so that c-d-c is a p-cycle; let a have an edge to a top τ_new with pr(τ_new) ≥ pr(τ) ≥ pr(a), where τ
is a top whose region contains e. With V ∌ τ_new: at the pop of e in Z_τ, t' fires (all
vertices in R), so c, d ∈ Reg(V). With V' = V ∪ {τ_new}: Z_τ_new is computed first and takes a by rule (V) (a → τ_new,
pr(a) ≤ pr(τ_new)); c and d are not taken (d escapes to the unattracted c, c's only edge goes to d); in Z_τ, t' no longer
fires (138: a is consumed), d escapes to c, c is not attracted: so {c, d} ⊆ R_rem(V'). A top whose rescue path ran through
c or d can then be a candidate in V' and a survivor in V. What the code computes is the specific descending iteration V_0 ⊇ V_1 ⊇ ... from V_0 = R ∩ P_p, and
every statement in this file is about that iteration.
Lemma 1.6 (structure of R_rem). Let y ∈ R_rem. If owner(y) = p: no successor of y lies in a region Z_τ with
pr(τ) ≥ pr(y). If owner(y) != p: y has a successor in R_rem, or every successor of y lies in Reg ∪ X ∪ (outside R) and
the lowest region (last computed) containing a successor has top priority < pr(y). Proof: when Z_τ is computed, all
higher regions are consumed (ignored, 80) and a lower region does not exist yet; rule (V) with threshold pr(τ). □

## 2. Correctness (Theorem D1)

### 2.1 Soundness — PROVED
Every vertex solved at 1034 is solved for the player p of the search in which it was found and gets str[v] with the
properties of Lemma 1.4b(1). Vertices are solved at most once: the dominion core is deduplicated by S (366-373), the
attractor adds only vertices of G' (74) and each solved vertex leaves G' (1035). With Lemma 1.4c (subgame semantics) and
positional determinacy, W_Even ⊆ W_E(G), W_Odd ⊆ W_O(G), and the output strategies are positional and winning from every
vertex of their region against every general opponent strategy (Lemma 1.4b(1) quantifies over all plays). □
(Theorem D1 except "every vertex is solved": soundness + strategies PROVED.)

### 2.2 Termination — PROVED (with an exponential bound only)
(i) One attractor terminates (each vertex pushed once). (ii) extractTangles terminates (Pearce). (iii) best_vertices:
each round except the last removes ≥ 1 vertex from V (765-771), so ≤ |V_0| + 1 ≤ n + 1 rounds. (iv) sptl repeats
(870-874) only while a new tangle or dominion was created (539, 464/377); each creates a new sorted vertex set (385-424)
or solves vertices later; so ≤ (number of tangles created in this call) + 1 passes. (v) search_rec: every iteration of
850-993 either returns (854), or removes ≥ 1 vertex from R: Dom(V,R) removes the tops of V (880/964, V ≠ ∅ because
result ≠ 0 and in the -1 case V := prevV ≠ ∅), the -1 branch with Q nonempty removes Z ⊇ Z_0 ≠ ∅ (920). So ≤ n
iterations per call. The recursive call (954) receives Z' := Z minus all vertices of priority t minus their opponent
attractor; every vertex of Z has priority ≤ t (921, threshold t), so every vertex of Z' has priority < t and the
recursion depth is ≤ d ≤ n + 1. (vi) search returns true only if `tangles` or `dominions` changed (1068); a new tangle
has a vertex set different from all stored ones (385-424; deleted tangles keep their tv, so a deleted set cannot be
re-created either — NOTE N4: this is stricter than needed), a dominion solves ≥ 1 vertex; so the number of searches is at
most 2^n + n + 2. Hence A_DTL and A_IDTL halt. □

### 2.3 Completeness ("every vertex is solved") — SKETCH, with the exact open claim
What must be shown (Lemma K). For p ∈ {Even, Odd} and the current G' (a parity game by Lemma 1.4c) with any set of
tangles satisfying TS: if W_p(G') ≠ ∅ then search(p) creates a new tangle or a dominion (returns true).
Why Lemma K is exactly completeness. dtl (1109-1121): Even's loop ends when search(0) returns false; by Lemma K then
W_E(G') = ∅, i.e. G' ⊆ W_O (Lemma 1.4c); Odd's loop then ends only when search(1) returns false, which by Lemma K (for
Odd) forces W_O(G') = ∅, i.e. G' = ∅. Conversely, a failure of Lemma K is observable: run() ends with G' ≠ ∅ (the check
1146-1151 is compiled out in release builds; a debug build throws "search was incomplete!"). idtl (1125-1138): "solver
stuck" is thrown iff both searches return false with G' ≠ ∅, impossible under Lemma K.
What is PROVED towards Lemma K:
K1 (dominion is found if closed). If some sptl region Z_τ (any pass) is closed with top τ such that the restricted graph
on Z_τ has a nontrivial SCC reachable from τ whose escapes are all outside X ∪ (higher sptl regions of this pass), then
that SCC is a dominion (no escapes at all: the escapes of an SCC of a closed region lie in Z_τ \ SCC, higher regions of
the pass, X, or solved vertices, by 1.2 (V)/(T) and F5; the first case is excluded for a BOTTOM SCC, which exists and is
nontrivial whenever every vertex of Z_τ has an out-edge in the restricted graph, i.e. always except NOTE N3).
K2 (duplicates have all escapes in X). A bottom SCC B of a closed sptl region Z_τ that equals a stored tangle t' has all
its escapes in X ∪ (outside R): if an escape e lay in a higher region Z_τ' of the same pass, then at the pop of the last
such e in Z_τ' all vertices of t' were in R (B ⊆ Z_τ lies below, unconsumed) and not in Z_τ', had priority ≤ pr(τ) ≤
pr(τ'), and all other escapes were in Z_τ' or outside its Gx, so rule (T) would have put B into Z_τ' — contradiction.
(Analogue of TL's Lemma 5 [van Dijk, CAV 2018, arXiv 1804.01023, Lemma 4-5, p.7-8, opened 16:40Z]; the TL proof uses
the "reduced region" and α-maximality, both absent here, so this is a new argument.)
K3 (first piece at depth 0). In the first iteration of search_rec(G', p, 0), X = ∅. If best_vertices returns 1 and some
sptl region is closed with a nontrivial reachable SCC, then by K1/K2 that SCC is a dominion or a new tangle (a
duplicate would have no escapes, hence be a dominion). So Lemma K holds in this case.
K4 (stable V* is p-won at X = ∅). Let V* be stable, Reg its regions, A := the final threshold-loop set. p has a
positional strategy ψ on A (attractor strategies inside regions toward their tops, threshold-loop strategies on A \
Reg, and at a top any successor in Reg or on its rescue path) such that every play from A consistent with ψ stays in
A ∪ (solved) and is won by p: the opponent cannot leave A (every opponent vertex of A was attracted with Gx = R, so its
successors are in A, X = ∅, or solved), every play reaches tops infinitely often or has a tail in an attracted tangle
(Corollary 1.3a), and between two consecutive tops τ, τ' the priorities are < pr(τ) (rescue path, threshold < pr(τ))
or ≤ pr(τ') (inside Z_τ'), so the maximum priority seen infinitely often is a top priority, parity p. So A ⊆ W_p(G').
Hence the first removed piece is p-won; by the same argument every later piece of type "stable regions" or type
"attractor to X" (the -1 branch with Q nonempty) is p-won PROVIDED X is p-won; pieces of type Dom(prevV, R) (the -1
branch with Q empty, 961-991) need not be p-won.
K5 (the lowest region at X = ∅; PROVED). Let V* be stable at X = ∅, τ_k the lowest top that has a region, A the final
threshold-loop set, Z_k the sptl region of τ_k (computed with all higher regions consumed). Then:
 (i) no p-vertex of A \ Reg has an edge into a higher region (it would have been attracted there: its priority is ≤ its
     rescue threshold < the top's priority, and it was never consumed);
 (ii) NOTE N3 cannot occur: an opponent-owned top with all successors in higher regions would have been attracted into
     the last of those regions (its priority is ≤ that top's), so it has no region of its own;
 (iii) A \ Reg ⊆ Z_k ∪ Str, where Str := the vertices pushed into A by rule (T) for a tangle t' that STRADDLES, i.e. has
     a vertex in a higher region (such a t' is not attracted into Z_k: 138-139). Proof: induction over the attraction
     order of A. A p-vertex y ∈ A \ Reg has str[y] in Z_k or in A \ Reg (by (i)), so it is attracted into Z_k. An
     opponent y ∈ A \ Reg has all its R-successors in A (it was attracted with Gx = R): those in higher regions are
     forgiven in Z_k's computation (outside Gx), the others are in Z_k by induction. A tangle t' fired into A has all
     escapes in A (forgiven or in Z_k by induction) and all vertices in R ∪ A; it is attracted into Z_k unless a vertex
     of it lies in a higher region (138) — the straddling case. □
 Consequence: Z_k is closed unless τ_k's successor (p-owned τ_k) or some successor (opponent-owned τ_k, which then has
 no successor outside A by stability) lies in Str \ Z_k. So at X = ∅ the lowest region is closed and productive
 (K1-K3) unless a stored tangle straddles a higher region and the opponent can stay forever inside its lower part
 (the lower part is then a p-winning sub-tangle Y that no vertex rule enters, because its opponent vertices keep a
 successor inside Y and its p-vertices follow the tangle strategy inside Y).
 Three generations are therefore needed for a failure of Lemma K at the first piece: a search s1 that learns the
 sub-tangle Y (so that Y is later a duplicate), a search s2 that learns t' ⊋ Y with top a ∈ t' (the top of t' is the
 only vertex of t' whose region-strategy can point into t' while a is attracted elsewhere later: 73), and a search s3
 in which a is absorbed into a higher region via an edge a → J (J a top only now: its rescue path must use t'), the
 region of every higher top is open, Y sits in R_rem, and after Dom(V*, R) → X the region of Y's top extracts only
 the duplicate Y. Every attempt to build s3 in the box collapsed at "every higher region is open": the first region
 (highest top, nothing consumed, X = ∅) is open only if the opponent can avoid that top forever from its successor
 inside A, and every attempted avoidance structure was itself attracted by the next tangle firing (an escape of a
 stored tangle popped in the highest region pulls the tangle in, then the attractor continues through its vertices).
The OPEN claims (GAP-C, two parts; neither refuted, neither proved):
(C-a) At X = ∅ with V* stable: some sptl region is closed with a nontrivial reachable SCC. What is known: an open region
Z_k of the lowest top τ_k forces τ_k "upward": by induction over the attraction order of A, A \ Reg ⊆ Z_k ∪ Up_k, where
Up_k = vertices from which some play consistent with ψ enters a higher region (a p-vertex y ∉ Z_k with pr(y) ≤ t has
str[y] in a higher region or in Up_k; an opponent y ∉ Z_k has a successor in R_rem ∩ A that is in Up_k; a tangle not
attracted into Z_k has a vertex in a higher region or an escape in Up_k, reachable inside the tangle by strong
connectivity). The same induction for a general top τ_i gives A_i \ Reg ⊆ Z_i ∪ Up_i ∪ Down_i. So the "top graph"
(τ → τ' if a ψ-play from τ enters Z_τ' before any other region) has an out-edge at every open or unproductive top and
hence a cycle; the cycle is a ψ-play with p-parity maximum. The step that does NOT close: the region of the first-in-sptl
top τ* of that cycle need not contain the cycle, because an opponent vertex w on the cycle inside a later region Z_j
may have a successor in a region Z_m with τ* > τ_m > τ_j (consumed when Z_j was computed, still present when Z_τ* was),
so w escapes Z_τ*. Then another cycle through τ_m exists, and the argument has to show that iterating this choice of
cycles ends in a top whose region is closed; no well-founded measure was found in the box.
(C-b) Pieces removed by Dom(prevV, R) (961-991) are treated as safe for p by every later attracts() although they need
not be p-won, and pieces removed by the -1 branch send every vertex of priority t to X without searching for p-tangles
of priority t (936-942). A failure of Lemma K would have to come from one of these two: a p-dominion D ⊆ R all of
whose p-priority vertices are pruned (so that D's vertices are removed through the -1 branch) while no closed region
elsewhere produces anything. Candidate instance shape (for L-RED), sharpened by K5: the three-generation straddling-tangle construction above
(first piece), or, for later pieces, a p-dominion D whose every p-priority vertex v has an
opponent "deviation" vertex of priority > pr(v) that is not attracted to any top because its two exits lead to two
different tops of equal priority smaller than its own (consumption cannot help when the deviation vertex's priority
exceeds both tops), covered on every cycle by a p-priority vertex that is itself pruned by the same mechanism one
level up; the ladder must close at the top with a vertex whose cover does not exist, which is why every attempt made
here collapsed (the top of the ladder is attracted). A counterexample needs the ladder to close through X (a piece
removed by Dom(prevV, R) earlier in the same search), i.e. two such dominion-like structures in one game, the first
removed as "distractions" with Q empty, the second using escapes into the first.
What a proof of Lemma K has to look like (for whoever continues). Any induction over the iterations of search_rec needs a
hypothesis of the form "if the iterations from state (R, X) on learn nothing, then R contains no structure of kind Φ".
Two natural choices fail: Φ = "p-dominion of R with exits into X forgiven" is refuted by a stored tangle t with all
escapes in X (it is such a structure, its SCC is a duplicate by K2, nothing is learned: consistent with the code), and
Φ = "p-dominion of R closed in G'" is what is wanted at depth 0 but is not preserved by the pieces: the −1 branch with Q
empty (961-991) removes Dom(prevV, R), which can contain vertices of such a dominion (c3: m and r), after which the
dominion is no longer inside R. The hypothesis must therefore carry the removed pieces along, e.g. Φ = "p-dominion D
closed in G' such that D ∩ R ≠ ∅ and every escape of every stored tangle inside D ∩ R lies in D ∩ X only if that
tangle is ...", and the step for a type-P piece must show that the regions of pruned tops never separate a closed
dominion from the tangle that would be learned in it. K5 (lowest region closed unless straddling) is the step for
type-S pieces at X = ∅; its extension to X ≠ ∅ holds verbatim (X is forgiven in both the threshold loop and the sptl
region), so after type-P/Z pieces the first stable set's lowest region is closed and its bottom SCC is new or has all
escapes in those pieces (K2). A failing search is therefore of one of two shapes: (α) straddling at the lowest top of
every stable set, or (β) the first stable set's lowest SCC is a stored tangle whose escapes lie in the type-P/Z pieces
removed before it in the same search. Shape (β) is the one to try first (it needs only two generations: the tangle is
learned in search s1 while its escape vertices are still "best"; in search s2 those escape vertices are pruned and removed
by the −1 branch before the tangle's region is reached). In c3 shape (β) is avoided because the stored tangle fires in the
threshold loop and rescues the higher top; (β) needs the escape vertices to be unreachable by any rescue path, i.e. of
priority above every surviving top's threshold.
K6 (where a search can lose its last chance; PROVED as stated, with X arbitrary). Let V* be stable at some iteration with
removed set X, τ_k the lowest top with a region, L_k its sptl region. K5(i)-(iii) hold verbatim with X ≠ ∅ (X is
forgiven in the threshold loop and in every region). Hence L_k is closed unless (α) τ_k's successor lies in the lower
part of a straddling tangle; and if L_k is closed it is productive (an opponent-owned τ_k with all successors in X ∪
consumed regions is impossible: with a successor in a consumed region it would have been consumed, with all successors
in X it would have been pruned), and its bottom SCC reachable from τ_k is new, a dominion, or (β') a stored tangle all of
whose escapes lie in X (K2 with X). So a search that learns nothing at its first stable set is of shape (α) or (β').
Orphan analysis for (α) (SKETCH, the chain a proof would follow). Let t' straddle with lower part Y ⊆ A \ Reg (the
opponent's safe set inside t' ∩ R_rem: p follows the tangle strategy inside Y, every opponent vertex of Y keeps a
successor in Y). (1) No stored tangle contained in Y has all its escapes in Reg ∪ X: it would fire into the last region
holding an escape (its vertices are unconsumed), contradicting Y ⊆ A \ Reg; so every stored tangle inside Y has an
escape in R_rem \ (itself). (2) After Dom(V*, R) → X, Y ⊆ R_2 and Y is p-closed in R_2 with exits only to X (forgiven).
(3) In iteration 2, Y's p-priority vertices start in V; the first stable set of iteration 2 has a lowest top; if it lies in
Y its region is closed (K6 again, unless a further straddle inside Y) and its bottom SCC is inside Y; by (1) that SCC is
not a stored tangle with all escapes in X_2 — unless its escapes leave Y only into X_2, which (1) excludes for stored
tangles inside Y — so it is new. The step that is not closed: the lowest top of iteration 2 may lie outside Y, and the
pieces removed before Y's turn (type P/Z inside iteration 2) may cut Y; a proof must show that cutting Y by the -1
branch leaves a p-closed remainder whose SCCs are still not stored. This is the same (C-b) obligation.
Route for excluding (α) (SKETCH, the most promising one found). Let t' straddle in search s3 with top a ∈ L_τnew and
lower part Y, and let s2 be the search that learned t' at top a. In s2, Y ⊆ Z_a: p forced the play from Y to a inside
R minus the regions of the tops above a (then), the opponent's exits into those regions being forgiven. In s3 the same
edges exist; a and the vertices of t' with a p-edge to a lie in L_τnew; a vertex of Y escapes L_τnew only through an
opponent exit into a region strictly between τ_new and a's former position or through a p-step to such a region; at
the computation of the LAST such region the exits above it are consumed and the forcing of s2 applies again (every
vertex of Y has priority ≤ pr(a) ≤ that region's top), so Y is absorbed there — unless a top that was above a in s2 is
no longer a top in s3 (its former region is now unattracted R_rem) or a sub-tangle used by the forcing in s2 straddles
itself in s3. The first case is a non-monotone change of the pruning between s2 and s3; by NOTE N5 and 1.2b (attractors
monotone in T, dominion removal only forgives more) such a change itself requires a straddling tangle in s3 whose top
was learned EARLIER than t' (creation order). Iterating, the straddling tangle with the earliest creation order has no
such cause, so it cannot straddle: contradiction. The two unproved steps in this regress: (r1) that the ONLY source of
non-monotonicity of the pruning across searches is a straddle (NOTE N5 shows straddles cause it; that nothing else
does needs a proof that V*_s ⊆ V*_{s+1} and Reg_s ⊆ Reg_{s+1} hold whenever no stored tangle straddles in s+1, with G'
shrinking by solved dominions in between); (r2) that the regress is well-founded (the straddling tangle causing the
pruning change must have been created strictly before t', not merely be different). If (r1) and (r2) hold, (α) never
occurs and, with K6 and the (β') analysis, every search's first stable set is productive; (C-b) would then remain only
for searches that start with the -1 branch.
Evidence for (r1) (experiments/alg/dtl_monotone.py): on 4,000 random games (n 5..14) plus tc+ N = 4..10 and c3, c4, the
stable set of the first best_vertices call of a search (∅ when that call returns -1) is contained in that of the next
search of the same player, restricted to still-unsolved vertices, in every case (0 violations); the first stable set of a
search after -1 pieces is NOT comparable (c3: {s, y, z} on a reduced region in search 1 vs {m, z} on the full region in
search 2), which is why (r1) must be stated per call on the same region.
Measurement of the (α) precondition (patched debug build, notebook item 9: at every stable pruning round, list the stored
tangles with vertices both in the regions and in the threshold-loop set outside the regions): tc+ N = 4, 6, 8: 16, 36, 64
such events over 7, 11, 15 distinct tangles (≈ 2N − 1), every run verified complete; 400 random games (n 6..14): 0 events;
c3, c4: 0. In the first tc+ event (search 2 of N = 4) the lowest region (priority 4, top Even-3-T) was still closed — its
top's successor lay inside its own region, not in the straddling tangle's lower part — and the pass learned two new
tangles. So straddling tangles exist in practice; (α) additionally needs the lowest top's successor inside the orphan,
which was never observed. The regress route above is therefore not available as stated (straddles do occur); what it
would have to show is that an orphan never contains the lowest top's successor.
For (β') (SKETCH). The stored tangle t = bottom SCC of L_k has escapes only in X. By K4, if all pieces in X are of type S
or Z, X is p-won and so is t ∪ Attr(X) — a p-won set that DTL never solves unless some later piece or search is
productive; then the search's remaining iterations must produce something new: the obligation is again (C-b). If some
piece in X is of type P, t's escapes may lead into opponent-won vertices, t is then not p-won and nothing is lost.
Attempts to realise (β') by hand (c4, section 6) fail for a reason that may be the key to (C-b): a stored tangle's
escape path to a surviving top passes only through priorities below that top's rescue threshold (the top is the cover
of the path's cycle), so the tangle fires in the threshold loop and rescues the top whenever the path's end is in Reg;
for the end to leave Reg, the top at its end must be pruned first, which needs a deviation structure of its own, and each
such structure is itself rescued by the tangles learned below it in the previous search (c4: {q, o} and {y, s} in search
1 rescue m and z in search 2).
Evidence (not proof): L-ALG 67,000+ games and L-RED's 120,000-mutation hill-climb for unsolved vertices found none; a
new oracle run on a DEBUG build (NDEBUG checks on: "search was incomplete!" and the depth-0 dominion check 349-355)
is experiments/alg/dtl_debug_fuzz.py (results in section 6).
Status of 2.3: SKETCH (K1-K4 PROVED; GAP-C open).

### 2.4 Theorem D1 summary
Soundness and strategies: PROVED. Halting: PROVED. Completeness: GAP-C (section 2.3). Theorem D1 is therefore NOT
established; its failure mode is a run ending with unsolved vertices (never observed).

## 3. Running time (Theorem D2)
Let |T| := tangles(G) (final), and cost(attr) := the cost of one attractor run (Lemma 1.2): each vertex of Z is popped
once, its in-edges scanned (O(deg_in)), and each tangle in tin[v] checked in O(|U_{t'}| + |O_{t'}|); a tangle is checked
once per escape popped: cost(attr) = O(m + Σ_{t'} |O_{t'}|(|U_{t'}| + |O_{t'}|)) = O(m + |T| n^2) =: W_A.
(b) Pruning rounds per best_vertices call: ≤ n + 1 (2.2(iii)). PROVED. One round costs: regions O(W_A), candidate scan
O(m), threshold loop (max priority + 1) ≤ n + 1 attractors each O(W_A) plus candidate rescans O(n · m): O(n W_A + n m).
One best_vertices call: O(n^2 W_A). PROVED.
(c) search_rec: ≤ n iterations per call, recursion depth ≤ d, every recursive call is made by an iteration that removes
the whole of Z from its parent's R, so the total number of iterations over all calls of one search is ≤ n(d + 1) ≤
n(n + 2). PROVED (2.2(v)). Per iteration: one best_vertices O(n^2 W_A); in the result-1 branch the sptl passes: each pass
costs ≤ n regions × (O(W_A) + extractTangles O(n + m) + duplicate check O(|T| n) (396-406)) = O(n W_A + n |T| n), and the
number of passes is ≤ (tangles + dominions created in this search_rec iteration) + 1; Dom(V,R) O(W_A); the -1 branch
O(n + W_A + m). So one search costs O(n(d+1) · n^2 W_A + (|T| + n + 1) · n(W_A + |T| n)) = O(n^4 (m + |T| n^2) + (|T| + n)
n (m + |T| n^2)).
(d) Searches: each search except the last one of each phase creates a tangle or a dominion (1068); dominions ≤ n (each
solves ≥ 1 vertex); so iterations ≤ |T| + n + 2 for dtl and ≤ 2(|T| + n) + 2 for idtl. PROVED.
(e) Total: O((|T| + n) · (n^4 (m + |T| n^2) + (|T| + n) n (m + |T| n^2))) = O(|T|^2 n^6 + |T| n^7 + n^8 + ... ) ⊆
O((|T| + n)^2 · n^4 · (m + n^2)) word operations, plus step 0 O((n + m) log n), plus the dominion removal O(W_A) per
search (covered). Every number is a vertex index, a priority ≤ n, a tangle index ≤ |T|, a stack pointer ≤ n, or a bit;
bitset copies/resets (837-840, 651-654, 871, 1014) cost O(n / w) words. Under (a) a tangle index has O(log n) bits and
unit cost = bit cost. PROVED conditional on (a). Without (a), |T| can in principle reach 2^n (every subset once), and
then nothing above is polynomial: the whole of D2 reduces to (a).
(a) The tangle count — GAP-A (open). What is PROVED: (a1) tangles are never re-learned (385-424), so |T| ≤ the number
of distinct vertex sets extracted; (a2) attractors, hence regions, are monotone in T for fixed inputs (1.2b); (a3)
with consumption, the head of a vertex (the top whose region takes it, in one round or one sptl pass on fixed R and V)
moves only to higher tops as T grows: a higher region can only grow (a2), so a vertex can be taken by a higher top and
never returned to a lower one (R8's (M3), re-proved from 1.2b and 1.6); (a4) a new tangle at top τ in a later search
requires a different (vertex set, strategy)-pair of the SCC, i.e. a change of Z_τ (a3: at most n events per top per
fixed (R, V)) or of str inside Z_τ. What is NOT proved: a polynomial bound on the number of distinct str assignments at
a fixed region vertex set. With the LIFO correction, str[u] for a (V)-pushed vertex is the vertex v on whose pop u was
pushed, i.e. the DFS parent of u in the depth-first traversal from top along reversed edges in Oink's `ins` order
(with tangle expansions interleaved). The DFS parent of u changes whenever the set of vertices or tangles present
changes the traversal order before u is reached. R8's potential argument ("BFS layers are non-increasing") assumed a
FIFO queue and does not apply; no replacement potential was found in the box. Concrete LIFO mechanism: at the pop of v, attractVertices pushes v's predecessors (in `ins` order, 69) and THEN
attractTangles pushes the vertices of every tangle in tin[v] (200-201, 164-172, in stored = sorted-index order); the stack
pops the tangle vertices first, so a newly learned tangle with escape v makes the whole DFS below v explore the tangle's
vertices (and everything reachable backwards from them) BEFORE v's vertex-predecessors; every parent assignment in that
subtree can change, and a later theft of one tangle vertex (a3) switches the tangle rule off again in that region,
restoring the old order for that tangle but not for the others learned meanwhile. Candidate instance shape (for L-RED): a
region whose DFS tree from top visits an Even vertex u via two different parents a, b depending on whether a vertex
(or tangle) x is already in Z when u's branch is explored; x's presence is toggled by thefts/growth at a higher top
(a3 budget n per top) — the question is whether the DFS reordering can be made to cascade so that one toggle at the
top flips the parents of polynomially many u's in a way that encodes a counter. Note that (a1)-(a3) give the same
"no reset" statement as R8 §1, and the budget of (a3) is n per top per (R, V)-context, but the number of contexts
(search_rec iterations × recursion levels × pruning rounds) is itself only bounded by (c) and (b), i.e. polynomially,
so the open quantity is exactly the number of str-changes per context.
Data for the shape of (a) (experiments/alg/dtl_pertop.py on the debug trace; a tangle's top = its maximum-index vertex):
| tc+ N | tangles | iterations | distinct tops | max tangles at one top | tops with 1 tangle |
| --- | --- | --- | --- | --- | --- |
| 2 | 8 | 5 | 8 | 1 | 8 |
| 4 | 30 | 10 | 26 | 3 | 24 |
| 6 | 58 | 14 | 49 | 5 | 46 |
| 8 | 94 | 18 | 80 | 7 | 76 |
| 10 | 138 | 22 | 116 | 9 | 108 |
tc N = 8, 12, 16: 17, 25, 33 tangles (2N+1), 6 iterations each, every top has exactly 1 tangle.
So on tc+ the ~1.4 N^2 total is ~1.2 N^2 tops with one tangle each plus two tops with N-1 tangles: no top cycles. The
conjecture that (a) needs is "at most n distinct SCCs are ever extracted at one top", and the open mechanism is the
str-change at a fixed region vertex set.
Status of 3: (b), (c), (d) PROVED; (e) PROVED conditional on (a); (a) GAP-A.

## 4. idtl vs dtl — PROVED (same proofs), one difference stated
Interleaved run (1125-1138) alternates search(0), search(1). Sections 1-3 never use that the phase is fixed: soundness
(2.1) holds per search; the trap property (Lemma 1.4b) was proved for interleaved removals (the case analysis in 1.4b(1)
covers earlier solved sets of either player); termination (2.2) counts tangles of both parities; D2(e) is the same bound
with twice the searches. Completeness is the same GAP-C for both players; "solver stuck" (1136) is exactly a
simultaneous failure of Lemma K for both players on a nonempty G', which is impossible since one of them wins something
in G' — so idtl can throw only if Lemma K fails for the player who wins G' ∩ W, which is the same event as dtl ending
with unsolved vertices. The one structural difference: in dtl a player's tangle set is frozen during the other's phase;
in idtl a p-tangle can be deleted (132-135) between two p-searches when one of its vertices is solved for the opponent,
which only shrinks T (never affects TS, 1.3).

## 5. Gaps and candidate instance shapes
| id | claim that is open | status | candidate instance shape |
| --- | --- | --- | --- |
| GAP-C | Lemma K (completeness): W_p(G') ≠ ∅ ⇒ search(p) learns a new tangle or a dominion | SKETCH (K1-K6 proved; failing shapes (α), (β') characterised) | section 2.3 (C-b): two pruned dominion-like structures, the first removed with Q empty, the second escaping into it |
| GAP-A | D2(a): polynomial bound on tangles(G) | open | section 3(a): a region whose DFS parents flip under a toggle at a higher top; counter over DFS reorderings |
Corrections to inputs found while proving: C5-DTL.md (LIFO stack; consumption in best_vertices), see its header; R8's
Lemma M part (c) and §5(a) assume FIFO/BFS and are void as written; (M1)-(M3) re-proved here (1.2b, 1.6, 3(a2)-(a3)).

## 6. Status table and evidence
| step | status | where |
| --- | --- | --- |
| 0 statement | written, diffed | section 0 |
| 1 primitives, TS, dominions, extraction, pruning | PROVED | 1.1-1.6 |
| 2.1 soundness + strategies | PROVED | 2.1 |
| 2.2 halting | PROVED (exponential bound) | 2.2 |
| 2.3 completeness | SKETCH; GAP-C | 2.3 |
| 3 (b)(c)(d) | PROVED | 3 |
| 3 (e) | PROVED conditional on (a) | 3 |
| 3 (a) tangle count | GAP-A | 3 |
| 4 idtl | PROVED (same) | 4 |
Re-runs on the PINNED command (`--no-loops`, after CHECKER C3 D-1): experiments/alg/dtl_check.py --no-loops, dtl and
idtl, regions against harness Zielonka and positional strategies verified by harness verify.py: instance library 126
games ok, every canonical game n = 1, 2, 3 (4 + 240 + 41,440) ok, each solver; the n = 4 sections need
experiments/alg/out/psolc_fail_n4.jsonl (518 s to regenerate, not re-run here). experiments/alg/dtl_debug_fuzz.py with
DTL_NO_LOOPS=1 (NDEBUG checks on, -t): seed 21, 20,000 random games with self-loops (rngame), dtl and idtl: 0 failures,
every run "solution verified". So no correctness failure appeared on the pinned algorithm.
Changelog after the 17:25Z park point (the Lead asked for §1-2.1 to stay stable): 17:45Z §0 rewritten per CHECKER C3;
§1.0 (tie order, self-loops) ADDED to §1; §7 (correspondence table) added; nothing in 1.1-2.1 changed.
Debug-build oracle (experiments/alg/dtl_debug_fuzz.py, NDEBUG checks on, dtl and idtl, -t so that a dominion at depth > 0
exits): seed 7, 30,000 random games (n 4..12, priorities ≤ n, out-degree 1..3): 0 failures, every run "solution verified";
seed 11, 20,000 games: 0 failures. Hand-built candidates (experiments/alg/instances/dtl_proof_c1.pg, c2, c3; all three are
won entirely by Even): c1, c2 solved in 1 iteration each (the c1 trace exposed the two transcription errors of C5-DTL.md);
c3 is the worked "ladder" of section 2.3 (z 6 → y 2 → s 0 → {y, w 1} → x 3 → r 1 → m 2 → n 1 → {z, m}): search 1 prunes s, y, z,
m in that order (best_vertices returns -1 twice: Dom(prevV = {m}) is removed with Q empty, then {w, x} is attracted to X at
threshold 3), the residual {z, y, s, n} is stable and learns the tangle {y, s}; search 2 learns {m, n} at the closed lowest
region; the tangles then fire upward into z's region and close it: dominion. c4 (11 vertices, three stored-tangle candidates: {q, o}, {y, s} learned in search 1, {m, n} in search 2, then the dominion)
was built for shape (β') and is solved in 2 iterations. Duplicate-tangle hill-climb (experiments/alg/dtl_dupclimb.py,
fitness = 1000 × unsolved + duplicate extractions, n = 12, 3 seeds × 20,000 mutations): best fitness 0 (no duplicate
extraction, no unsolved vertex, ever); tc+ N = 6 (58 tangles, 14 searches) has 0 duplicate extractions. So the (β')
configuration (a duplicate at a closed region) was never observed. This is the mechanism that defeated every
hand-built completeness counterexample: a stored tangle with an escape in a higher region is pulled into that region at
the escape's pop, and the region continues through the tangle's vertices.

## 7. Correspondence dtl.cpp @ 8fbf0a7 ↔ C5-DTL.md (itemised; to be signed separately, TARGET section 6 / D2 change 2)
| C5-DTL.md item | dtl.cpp lines | status |
| --- | --- | --- |
| conventions: sorted indices, stack Q, bitsets, str, tangles tv/tout/tpr/tin | oink.cpp:35; uintqueue.hpp pop = `queue[--pointer]`; dtl.hpp | re-read 2026-10-15, stack corrected |
| attracts | 40-57 | exact |
| attractVertices (incl. str at 73/89, escape test 78-85, threshold 74) | 65-101 | exact |
| attractTangle (deleted/parity 117-118, G' 132-135, R 138, maxpr 140, new 143-146, escapes 152-158, push 163-182) | 109-185 | exact |
| attractTangles = for t in tin[v] | 197-202 | exact |
| extractTangles: Pearce from top, is_tangle 315-317, escapes vs G' 327-341, dominion 347-379, duplicate check 385-424, store 439-466 | 210-471 | exact; CHECK_UNIQUE named |
| sptl: regions on the consumed copy, closed test, W, extraction | 476-546 | exact |
| best_vertices: V init, rounds, ONE CurR per round, candidates, threshold loop, prune, returns | 643-776 | exact after the 16:30Z correction |
| search_rec: result 0/1/-1 branches, Dom(V,R), lowest level, Z, t-level to X, opponent attractor, recursion | 834-994 | exact |
| search: copy of G', search_rec, W reset, dominion extension and removal, return value | 997-1069 | exact |
| run: dtl loops (Even then Odd), idtl loop and `solver stuck`, NDEBUG-only completeness check | 1071-1161 | exact |
| omitted as not part of A_DTL: computeDistanceValues 553-639 (NDEBUG/trace only), new_algorithm 778-831 (commented out), all `trace` output, `steps` (never incremented) | | |
