# GAP-C: completeness of A_DTL — statement, proof map, open steps (L-ALG succ. 5, 2026-10-17T01:34Z by date -u; produced on Opus 5.5)
Unrefereed. Lead pick 00:48Z/01:09Z. A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7 (L22), pseudocode
docs/alg/candidates/C5-DTL.md (C5), every order datum ω (L26). Earlier work: docs/alg/DTL-proof.md §2.3 (K1-K6, shapes (α),
(β'), (C-b)), §5. Line numbers "dtl.cpp N" are tools/oink/src/src/solvers/dtl.cpp @ 8fbf0a7.

## 1. Statement
Lemma K (completeness step). Let p ∈ {0, 1}, let G' be the unsolved set when search(p) is called in a run of A_DTL (a
parity game with the edges leaving G' deleted, DTL-proof.md Lemma 1.4c), and T the stored tangles. If W_p(G') ≠ ∅ then
search(p) returns true (it creates a new tangle or a dominion).
Why it is completeness (PROVED, DTL-proof.md §2.3; run() = C5 lines 141-142, dtl.cpp 1072-1161): player 0's loop stops
at the first false search(0), so by Lemma K W_0(G') = ∅ then, i.e. G' ⊆ W_1; player 1's loop stops at the first false
search(1), so W_1(G') = ∅, hence G' = ∅. Soundness and strategies are PROVED separately (DTL-proof.md §2.1, Lemma 1.4b).
A failure of Lemma K is observable: the run ends with unsolved vertices (the release build does not check; C5 line 145).

## 2. Proof map (status of each step)
| step | content | status |
|---|---|---|
| K1-K4 | dominion found if closed; duplicates have all escapes outside the context (K2); first piece at X = ∅; stable V* at X = ∅ is p-won | PROVED (DTL-proof.md §2.3) |
| K5, K6 | the lowest region of a stable set is closed unless (α); if closed, its bottom SCC is new, a dominion, or (β') | PROVED (DTL-proof.md §2.3) |
| SCC1 (new) | in a closed sptl region Z_τ every vertex reaches τ in extractTangles' graph; so extractTangles(τ) finds at most ONE nontrivial SCC, the set C_τ reachable from τ | PROVED (reading), §3 |
| B-thr (new) | if C_τ equals a stored tangle t, then τ ∈ t, every escape of t lies outside the context R, and the LAST escape of t to be popped either (a) was popped in an attractor with threshold < pr(τ), or (b) was cut off from t by an ancestor's −1 step (t inside the recursion context, e moved to X at 936-950) | PROVED (reading), §3 (corrected) |
| NODUP | the duplicate case of SCC1 never occurs on DTL runs | DATA (§4); GAP-β |
| NO-ORPHAN | no stored p-tangle inside a context has all its escapes outside it (implies NODUP) | DATA (§4), 0 of 28,541 calls |
| (α) | the lowest region is open because its top's successor lies in the lower part of a straddling tangle | GAP-α |
| (C-b) | a p-dominion survives a search whose pieces never reach a productive closed region (all relevant pieces removed through the −1 branch) | GAP-Cb |
| (S2) | "a context containing a p-dominion is never pruned to −1" | FALSE (§4); the proof must follow the dominion through −1 pieces |

## 3. The new steps
Lemma SCC1 (PROVED, reading). Let τ be a top in sptl (dtl.cpp 477-550) with region Z_τ, computed from {τ} by the
consuming tangle attractor at threshold pr(τ) (493-500), and let H be extractTangles' graph on Z_τ (dtl.cpp 211-300:
p-vertices keep only str[v], opponent vertices keep every edge into Z_τ). Then every vertex of Z_τ reaches τ in H.
Proof by induction over the order in which vertices join Z_τ. τ: trivial. A p-vertex u attracted by attractVertices at
the pop of v (dtl.cpp 87-90) gets str[u] = v, v earlier; str is overwritten later only where it is −1 (line 73), which
excludes u. An opponent vertex u attracted at the pop of v has the edge u → v and no edge into CurR \ Z at that time
(75-86), so all its H-edges lead to earlier vertices, at least one exists. A tangle t2 attracted at the pop of an escape e
(attractTangles 198-202 → attractTangle 110-185, vertices added with their tangle strategy at 171): some opponent vertex
o ∈ t2 has the edge o → e, e earlier; from any newly added vertex of t2 a path inside t2 under t2's strategy reaches o
(t2 is strongly connected, DTL-proof.md 1.3); along it, a newly added p-vertex follows its tangle strategy, an opponent
vertex keeps the path edge, and an old vertex already reaches τ by induction. □
Consequences (PROVED): every vertex reachable from τ in H is in τ's SCC, so the SCCs reachable from τ (the only ones
extractTangles examines, 211-300) are τ's own; it is nontrivial when τ is closed and p-owned (str[τ] ≠ −1, 515) or has
an edge into Z_τ or a self-loop. DATA: every extractTangles call in C5 creates exactly one SCC (3,605 calls Oink order,
3,551 stable; none creates 0 or ≥ 2).
Lemma B-thr (PROVED, reading). If C_τ equals a stored tangle t (the duplicate check 385-424 fires), then (i) τ ∈ t and
pr(τ) = max pr(t); (ii) no escape of t lies in Z_τ (an opponent vertex of C_τ with an edge into Z_τ \ C_τ would make that
vertex reachable from τ) nor in a region of the same pass computed after Z_τ (opponent vertices of Z_τ have no edge into
CurR \ Z at their attraction, the closed check 512-525 covers τ) nor in a higher region of the same pass (K2); so every
escape lies outside the context R of the current search_rec iteration, i.e. in X or outside the search_rec context;
(iii) every such escape joined a removal in this search through a pop inside some tangle attractor (Dom(V, R) 878-890 /
962-991 with threshold pr(top); the −1 attractor 914-923 (seeds 899-912) with threshold t; the threshold vertices and the
opponent attraction 936-950 only move vertices that the −1 attractor had popped). Take the pop of the LAST escape e of t:
the other escapes are in that attractor's target or outside its Gx, and every vertex of t is in its R (contexts only
shrink along the search). Then exactly one of two things held (CORRECTED 01:38Z by date -u; the first version claimed (a)
only): (a) no vertex of t was in the attractor's target, so attractTangle (110-185) rejected t only through the priority
test: that attractor's threshold was < pr(τ); or (b) the pop was in a −1 attractor (914-923) of an ANCESTOR search_rec and
t was already inside its set Z (attractTangle returns "nothing new"), t then stayed in the recursion context (954) while
e was moved to X by the threshold-vertex step (936-942) or the opponent attraction (944-950). □
So a closed region at a top τ ∉ W is productive except in the duplicate case, and the duplicate case is exactly:
GAP-β (sharpened (β')). A stored tangle t with top τ = argmax pr(t), all of whose escapes are removed earlier in the same
search, the last one either (β-a) by an attractor of threshold below pr(τ), or (β-b) by an ancestor's −1 step that keeps t
inside the recursion context and moves the escape to X (threshold vertex of level t_0, or opponent-attracted to the
threshold vertices); τ survives the pruning as a stable top and its closed region is exactly t.
Smallest shapes (sketch, not built): two searches. Search 1 learns t at τ while an escape e of t is still in the context.
(β-a) search 2 removes e into X by a −1 branch at a level t_e < pr(τ) (e of priority ≤ t_e, attracting X) or by Dom(V, R)
of a lower top, before τ's stable piece. (β-b) search 2 takes a −1 branch at level t_0 whose attractor contains t and e,
e has priority t_0 (a threshold vertex) or is an opponent vertex forced to the threshold vertices, and t goes into the
recursion, where τ is a stable top. Nothing else in search 2 is productive. About 5-6 vertices plus a gadget that makes e
removable early only in search 2.
GAP-α (from DTL-proof.md §2.3 K5/K6; unchanged). The lowest top's region is open because its top's successor lies in the
lower part Y of a stored tangle that straddles a higher region. Smallest shape (DTL-proof.md §2.3): three generations —
s1 learns a sub-tangle Y, s2 learns t' ⊋ Y with top a, s3 absorbs a into a higher region via a top J whose rescue path uses
t', with every higher region open. The regress route that was meant to exclude (α) is DEAD (L-RED R11, DTL-proof.md §2.3).
GAP-Cb (from DTL-proof.md §2.3; restated). The p-dominion D is never inside a productive closed region of the search:
every piece meeting D is removed through the −1 branch (Dom(prevV, R) with Q empty, 962-991, which X then forgives, or
the threshold attractor 899-954, which sends priority-t vertices to X without a tangle search) and the recursions inside
it fail in the same way. Smallest shape (DTL-proof.md §2.3): two dominion-like structures, the first removed as
distractions with Q empty, the second escaping into it.

## 4. Data (this box)
- Exhaustive: every game with n ≤ 3 and priorities 0..3 (176,200 games; experiments/alg/dtl_gapc_exh.py), both order
  data: complete, regions equal to Zielonka's. Earlier: pinned Oink on all canonical n ≤ 3 and the n = 4 samples
  (experiments/alg/dtl_check.py, DTL-proof.md §6).
- NODUP: the duplicate check never fires: 192 corpus files (experiments/alg/instances, climbs_1016, experiments/red/**),
  both order data, 0 hits (experiments/alg/dtl_nodup.py); 20,000 random games per order (n = 4..16, gen.random_game):
  0 hits, 0 incomplete runs.
- (NO-ORPHAN), DATA (01:43Z by date -u; experiments/alg/dtl_orphan.py): an ORPHAN at a best_vertices call with context R is a
  stored p-tangle t ⊆ R all of whose escapes lie outside R (such a t is never re-checked inside R, since tangles are
  checked only at pops of their escapes); every duplicate of Lemma B-thr is an orphan at its piece. Corpus, every call at
  every depth: 0 orphans in 14,415 calls (Oink order; 1,552 stable calls) and 0 in 14,126 (stable order). NO-ORPHAN implies
  NODUP, hence GAP-β. Proof idea (SKETCH): orphans can only be created when a removal takes the last in-R escape of t
  without taking a vertex of t, i.e. (β-a) at a threshold below pr(t's top) or (β-b) by the −1 step's moves; at a Dom
  removal, attractTangle skips vertices already in the target (dtl.cpp 136-137) before its priority test (140-141), so if t's top-priority
  vertex m was removed before (m ∈ V processed earlier at threshold pr(m)), the priority test only applies to t's lower
  vertices; the open case is m pruned (m ∉ V) while its escape is removed by a lower top.
- Near misses (experiments/alg/dtl_gapc_shapes.py, Oink order, corpus): of 1,408 searches, 774 have W_p(G') ≠ ∅; 297 of
  those find a dominion; 125 learn exactly one new tangle and nothing else; 0 learn nothing.
- (S2) FALSE: in experiments/alg/instances/spp_final_n20.pg (Oink order) Odd wins all 20 vertices, yet the root
  best_vertices call of Odd's search returns −1 (experiments/alg/dtl_s2.py; 17 of 20 calls on 3 games with a dominion
  inside their context return −1). Every dominion is found through −1 pieces and deeper stable pieces.
- Long phases of a player who wins nothing: in spp_final_n20, 21 of the 28 searches have W_p(G') = ∅ (Even's long phase
  learns tangles for a player with no winning vertex); completeness is not at stake there.

## 5. What a proof of GAP-β would need (reading)
B-thr reduces GAP-β to a statement about thresholds: when the last escape e of t is removed at threshold θ < pr(τ), show
that τ cannot be a stable top later in the same search with region exactly t. The natural lever is the pruning: τ survives
only if τ attracts into the region union or is rescued at a threshold below pr(τ); t's own play from τ returns to τ only
through vertices of t, and e is gone, so the rescue must come from a lower region that reaches t's vertices; since t's
escapes are all outside R, no lower region can enter t except through t's vertices, which then would be attracted into
that lower region (priority ≤ its threshold?) — the priority comparison is the open point.

## 6. Toward NO-ORPHAN (01:45Z by date -u)
Lemma O0 (PROVED, reading). At the start of search(p) (context R = G') there is no orphan. Let t be a stored p-tangle with
t ⊆ G' and every escape solved. If the last escape e to be solved was solved for p, then at its pop in the dominion
attraction (dtl.cpp 1032-1038, attractTangles with no priority limit, Gx = G) every other escape is in S or already solved
(outside Gx) and every vertex of t is in G and not in S, so t is attracted and solved, a contradiction. If e was solved for
the opponent, the opponent vertex o ∈ t with the edge o → e is owned by the opponent, so attractVertices (74-90) puts o
into that solved set, and t is deleted on the fly (132-135), a contradiction. □
Lemma O1 (PROVED, reading). Suppose a removal Dom(V, R) (878-890 or 962-991) creates an orphan t (t ⊆ R after the removal,
t had an escape in R before, none after). Let m be the vertex of t of maximal priority q (parity p, since t is a genuine
p-tangle and strongly connected). Then m ∈ R \ V: m was pruned in this piece. Proof: at the pop of t's last escape in R,
in the attractor of some top τ_j ∈ V at threshold pr(τ_j), attractTangle (110-185) rejects t only through the priority
test (the escape test passes as in B-thr; no vertex of t is in X), so q > pr(τ_j). If m ∈ V, the Dom loop (top from high
index down) processes m before τ_j (higher priority) and puts m into X, contradicting t ⊆ R after the removal. □
For an orphan created by a −1 branch (914-950) every p-priority vertex of the piece was pruned (the call returned −1), so
again t's top vertex is a pruned distraction. So every orphan needs: t's top-priority vertex m is a distraction in the
piece where t's escapes are removed, those removals use thresholds below pr(m) (or the −1 moves of (β-b)), and m stays
in R. The OPEN step (GAP-β) is to show that m cannot then be a distraction: m's tangle t is a p-winning cycle structure
whose only exits are those escapes, so while they are in R, m's region or the threshold sweep should rescue m.
What blocks the obvious argument: in the threshold sweep (best_vertices, dtl.cpp 722-740; Q is refilled with all of Z at every
level, 724, so every tangle with escapes in Z is re-checked at each level) a tangle is attracted only at a level ≥
its maximal priority q = pr(m), so t can never help rescue m itself (rescue needs a level < pr(m)); m survives only
through a lower good path, which t's own vertices do not provide.
