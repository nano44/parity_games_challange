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
Lead question 01:12Z (01:59Z by date -u): does a false search(0) prove that Even wins nowhere in the current G, so that Odd's
later removals cannot create an Even dominion? Yes, GIVEN Lemma K, and no extra gap: Lemma K gives W_0(G') = ∅ when line 141
breaks; every later unsolved set G'' ⊆ G' (Odd's dominion removals) satisfies W_0(G'') = W_0(G) ∩ G'' (DTL-proof.md Lemma
1.4c: winning regions of the subgame are restrictions), and W_0(G) ∩ G' = W_0(G') = ∅ by the same lemma, so W_0(G'') = ∅.
Without Lemma K the statement is exactly what is open; it is not a separate GAP.
A failure of Lemma K is observable: the run ends with unsolved vertices (the release build does not check; C5 line 145).

## 2. Proof map (status of each step)
| step | content | status |
|---|---|---|
| K1-K4 | dominion found if closed; duplicates have all escapes outside the context (K2); first piece at X = ∅; stable V* at X = ∅ is p-won | PROVED (DTL-proof.md §2.3) |
| K5, K6 | the lowest region of a stable set is closed unless (α); if closed, its bottom SCC is new, a dominion, or (β') | PROVED (DTL-proof.md §2.3) |
| SCC1 (new) | in a closed sptl region Z_τ every vertex reaches τ in extractTangles' graph; so extractTangles(τ) finds at most ONE nontrivial SCC, the set C_τ reachable from τ | PROVED (reading), §3 |
| B-thr (new) | if C_τ equals a stored tangle t, then τ ∈ t, every escape of t lies outside the context R, and the LAST escape of t to be popped either (a) was popped in an attractor with threshold < pr(τ), or (b) was cut off from t by an ancestor's −1 step (t inside the recursion context, e moved to X at 936-950) | PROVED (reading), §3 (corrected) |
| NODUP | the duplicate case of SCC1 never occurs on DTL runs | KILLED (§8): experiments/red/carry/instances/gapb_dup_n20.pg (L-RED) |
| NO-ORPHAN | no stored p-tangle inside a context has all its escapes outside it (implies NODUP) | KILLED (§8), same instance |
| NO-ORPHAN-W | no stored p-tangle inside R ∩ W_p(G') has all its escapes outside R | KILLED (§12): experiments/red/carry/instances/gapbW_dup_n20.pg (L-RED) |
| (α) | the lowest region is open because its top's successor lies in the lower part of a straddling tangle | GAP-α |
| (C-b) | a p-dominion survives a search whose pieces never reach a productive closed region (all relevant pieces removed through the −1 branch) | GAP-Cb |
| (S2) | "a context containing a p-dominion is never pruned to −1" | FALSE (§4); the proof must follow the dominion through −1 pieces |
| OPP-EXIT (new) | a learned tangle meets W_{1-p} only where the opponent's winning move is an edge the region forgives | PROVED (reading), §11 |
| K-in, TW, LOW-W | progress inside W_p, from a lowest region; learned tangles never straddle W_p's boundary | DATA (§9-§11), 0 violations |
| K-first | the FIRST stable piece's lowest region is productive inside W_p | KILLED (§14): instances/kfirst_viol_union.pg (276 of 891 mixed searches) |
| Theorem A | if the root call is stable, its lowest region is in W_p and is productive unless (α) | PROVED (reading), §13 |
| K4-B | the first stable piece's regions lie in W_p even after −1 pieces | KILLED (§14), union games |
| GAP-K | (K-low): some stable piece's lowest region is productive inside W_p | GAP (§12, §14); DATA 0 violations incl. 2,092 mixed union searches |

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

### 6a. The NO-ORPHAN mechanism on data (01:56Z by date -u; experiments/alg/dtl_orphan.py, dtl_nearorphan.py, dtl_nearorphan2.py)
- NEAR-ORPHAN at a call (context R, returned V): a stored p-tangle t ⊆ R with exactly one escape e in R and its
  top-priority vertex m ∉ V. Common: 5,375 (Oink order) / 5,298 (stable) on C5. So orphans are one removal away, often.
- Fate in the next sibling call (Oink order): e kept 3,431; e and ALL of t removed in the same removal 1,944; e removed
  with t kept (an orphan) 0; e removed with t partly kept 0.
- How t leaves (dtl_nearorphan2.py): taken AS A TANGLE in the removal in 1,618 cases, always at a threshold ≥ pr(m)
  (−1 attractor 1,419, Dom 199); m was already in the target in 1 case; taken vertex by vertex in 326. Never at a
  threshold below pr(m). The escape itself is often low: pr(e) < pr(m) in 2,554 near-orphans, pr(e) = pr(m) in 203,
  pr(e) > pr(m) in 2,618; so the reason is not the escape's priority.
- Reading (SKETCH for the Dom case): m was pruned at some round r0 while it was still a top, so m ∈ Z_{r0} and
  attractTangle skips m (136-137); t would then be attracted at a level < pr(m) (rescuing m through its strategy edge)
  unless its only in-R escape e is outside Z_{r0} at those levels. But e is removed by Dom(V*, R), i.e. lies in (roughly)
  the final round's regions. So the step closes if the ACTUAL region union is monotone in the top set (Z_{r0} ⊇ the final
  round's regions when V* ⊆ V_{r0}); for the IDEAL union that is Lemma 2.1 (GAP-A-M §2), for A_DTL it is exactly the
  deficit question of GAP-A (Lemma E straddles). GAP-β therefore meets GAP-A's (H4) core.

## 7. GAP-Cb: the dominion is not carried through −1 pieces (02:10Z by date -u; experiments/alg/dtl_cb1.py, dtl_s2.py)
(Cb1) "if the context R of a best_vertices call contains a p-dominion and that iteration learns nothing, the next sibling
context R' (R minus the iteration's removal) still contains one": FALSE in both semantics, C5, Oink order.
- Strict (exits from R' won by the opponent, dtl_s2.dom_inside): of 546 unproductive −1 iterations with a dominion inside
  R, 452 lose it. First instance: experiments/alg/instances/c1_k1_min_n7_m10.pg, the root piece (|R| 7 → 6).
- Forgiving (exits from R' deleted, DTL's context semantics, dtl_s2.dom_forgive): 565 of 2,892 lose it; first instances
  c1_k1_min_n7_m10.pg (root piece) and c6_replay3_n32.pg (depth-1 pieces (3, 2) and (4, 1)). (The 150 "result 0 with a
  dominion inside" rows of that run are an artefact of the dead-end rule, which gives stuck opponent vertices to p.)
Reading: the Dom(prevV, R) removal of a −1 iteration with Q empty (962-991) can take part of a p-dominion with nothing
learned, so no induction "a dominion inside the context persists until a stable piece" exists; whatever compensates must
be shown to come later in the same search (DTL-proof.md §2.3's (C-b) obligation, restated with instances). Every one of
these searches still learned something elsewhere (complete runs, NODUP data).

## 8. NODUP and NO-ORPHAN are FALSE; the GAP-β duplicate is realised, outside the winning region (02:21Z by date -u)
Instance: experiments/red/carry/instances/gapb_dup_n20.pg (L-RED, l-red e4138a0, sha1 2f433a31; Lead: pinned Oink 14
iterations, 1 dominion, 26 tangles, verified; pinned release Oink with -t prints "duplicate tangle"). Reproduced here
(dtl_orphan.py, dtl_nodup.py), both order data: one orphan call and one duplicate-check hit. Oink order: Even's search 1
(the second search) has depth-0 pieces −1 (|R| 20), −1 (|R| 17), recursion, stable |R| 12 (V* = {5, 8, 10, 11, 13, 17, 18},
learns T@8, T@5, T@11), then stable |R| 2 = {3, 4} with V* = {4}, whose closed region re-finds the stored tangle
{3, 4} (learned at top 4 in search 0; priority 12; all escapes outside {3, 4}): branch (β-b) / (β-a) of Lemma B-thr.
The run is complete and correct.
Key fact (dtl_gapc_shapes.subgame_win): |W_0(G')| = 0 in that search (Odd wins all 20 vertices; Even's whole block of
12 searches, 13 in stable order, runs with W_0 = ∅). So the duplicate does not touch Lemma K, which only concerns
searches with W_p(G') ≠ ∅; the search was productive anyway through the earlier stable piece.
Restated GAP-β: (NO-ORPHAN-W) at every best_vertices call of a search of p, no stored p-tangle t ⊆ R ∩ W_p(G') has all
its escapes outside R. A duplicate of Lemma B-thr inside the winning region would be such an orphan. Lemma O0, O1 and the
§6a reduction hold unchanged for it (the threshold argument does not use W_p). L-RED target: an orphan inside W_p(G')
(count with experiments/alg/dtl_orphan.py, which now reports orphans inside W_p).

## 9. The progress mechanism on data: learning happens inside the winning region (02:33Z by date -u; experiments/alg/dtl_kin.py)
(K-in), DATA: a search of p with W_p(G') ≠ ∅ either finds a dominion or learns at least one new tangle INSIDE W_p(G')
(W_p by Zielonka on G'). C5: Oink order 777 such searches: 299 find a dominion, 478 learn inside W_p, 0 violations; stable
order 767: 308 / 459 / 0. (K-in) is Lemma K with the location of the progress made explicit.
(TW), DATA: in those searches every newly learned tangle lies either wholly inside W_p(G') or wholly outside it: Oink
order 2,033 inside, 6 outside, 0 straddling; stable 1,993 / 6 / 0. (A genuine p-tangle can straddle in general: a p-vertex
of W_p with its tangle edge into W_{1-p} and an opponent vertex of W_{1-p} with an edge back; so (TW) is a property of
what DTL learns, not of tangles.)
(NO-ORPHAN-W), DATA: 0 orphans inside W_p(G') at any call (14,650 calls Oink order, 14,372 stable); the only orphan anywhere
is gapb_dup_n20's, outside W_p.
Proposed statement of GAP-C for the fleet (replaces "Lemma K with shapes (α), (β'), (C-b)" as the attack target):
  (K-in) W_p(G') ≠ ∅ ⇒ search(p) finds a dominion or learns a tangle t ⊆ W_p(G').
  Obligations, as before but restricted to W_p: (α-W) a straddling tangle that blocks the lowest region inside W_p;
  (β-W) an orphan inside W_p (NO-ORPHAN-W); (Cb-W) every piece meeting W_p leaves through the −1 branch with nothing
  learned inside W_p.
Where the progress inside W_p happens (02:48Z by date -u; experiments/alg/dtl_kin2.py, dtl_peel.py; C5, Oink order):
- Tangles learned inside W_p: 1,653 at depth 0 in a piece whose context lies inside W_p, 341 at depth 0 in a context that
  meets both regions, 39 at depth 1 (context inside W_p). First such tangle of each search: 636 / 66 / 12.
- (PEEL) "every vertex removed at depth 0 before the first productive piece is opponent-won": DEAD, 476 of 777 searches
  (first: experiments/alg/instances/c1_k1_min_n7_m10.pg, Even wins all 7 vertices and 5 are removed before the first
  productive piece). So DTL does not peel the opponent's region first; when it learns inside W_p, the earlier pieces have
  removed opponent-won AND p-won vertices.

## 10. (LOW-W): the progress comes from a LOWEST region inside W_p (03:13Z by date -u; experiments/alg/dtl_loww.py)
(LOW-W), DATA: every search of p with W_p(G') ≠ ∅ that finds no dominion has a stable piece (any depth) in one of whose
sptl passes the LOWEST top that gets a region learns a tangle inside W_p(G'). C5: Oink order 478 of 478, stable order 459 of
459 (lowest-top tangles outside W_p: 6 in each order, the 6 'outside' tangles of §9). Of the 2,033
tangles learned inside W_p in those searches, 1,822 come from the lowest top of their pass, 211 from a higher top.
(A first version of the tool took the last top of V in sptl order, which can be consumed by a higher region and has no
region of its own; it reported 261 false violations. The corrected tool re-implements dtl_pyref.sptl verbatim and records
the tops that get a region.)
Consequence for the proof (reading). K5/K6 (DTL-proof.md §2.3) already say: the lowest region of a stable set is closed
unless (α), and SCC1 + B-thr: a closed region at a top not in W is productive unless (β). So GAP-C reduces to statements
about ONE region (what was measured is the learned SCC, not the region):
  (Cb-W) some stable piece of the search has its lowest top (with a region) in W_p(G') (existence);
  (α-W)  that region is closed (no straddling tangle blocking its top's successor);
  (β-W)  its SCC C_τ is not a stored tangle (no orphan inside W_p);
  (TW)   C_τ lies inside W_p(G').
Data: a lowest top learns a tangle inside W_p in every case (478/478). L-RED target: a search with W_p ≠ ∅ where no stable piece has
its lowest region inside W_p (Cb-W fails), or where it does but that region is open (α-W) or a duplicate (β-W).
Random games (1,500 games gen.random_game(n, n, 1, 3), n = 6..20, seeds 50000-51499; both order data): weak evidence for
(K-in)/(LOW-W), because 2,363 of 2,365 (Oink order) searches with W_p ≠ ∅ find a dominion outright (2 / 2 hold); (TW) gets
a real test: 869 learned tangles inside W_p, 36 outside, 0 straddling (stable: 877 / 36 / 0).

## 11. Toward (TW) (03:32Z by date -u)
Honest evidence for (TW): only searches where BOTH players win something are informative (when W_p = G' every tangle is
trivially inside). Mixed searches (corpus + the 1,500 random games, Oink order): 842 searches, learned tangles 501 inside
W_p, 42 outside, 0 straddling (stable order 497 / 42 / 0).
Lemma OPP-EXIT (PROVED, reading). Let τ be a top whose sptl region Z_τ is closed, C_τ the SCC extracted at τ (Lemma SCC1),
and π a positional winning strategy of the opponent on W_{1-p}(G') (it keeps the play in W_{1-p}; W_{1-p} is a trap for
p). If C_τ ∩ W_{1-p} ≠ ∅, then some opponent vertex o ∈ C_τ ∩ W_{1-p} has π(o) outside the set CurR in which o was attracted,
i.e. π(o) lies in a region computed earlier in the same pass, in X, or outside the search_rec context (an edge the region
forgives). Proof. Suppose not. A p-vertex v ∈ C_τ ∩ W_{1-p} has all its edges in W_{1-p}, so str[v] ∈ W_{1-p}, and str[v] ∈
Z_τ (an H-edge), hence str[v] ∈ C_τ (everything reachable from τ is in C_τ). An opponent vertex o ∈ C_τ ∩ W_{1-p} was
attracted with no edge into CurR \ Z (dtl.cpp 75-86), so π(o) ∈ CurR implies π(o) ∈ Z_τ, an H-edge, so π(o) ∈ C_τ, and
π(o) ∈ W_{1-p}. So the play from any vertex of C_τ ∩ W_{1-p} that follows str for p and π for the opponent stays in
C_τ ∩ W_{1-p} forever; it is consistent with π, so the opponent wins it; it is a play in H inside the extracted p-tangle
(every cycle of H on C_τ is won by p, DTL-proof.md 1.3), so p wins it. Contradiction. □
What it gives: a learned tangle meets the opponent's winning region only through forgiven edges of the region (the
opponent's winning move leaves the context or goes into an earlier region). It does not exclude straddling by itself:
for that one would need the same with p's winning strategy on W_p, but H keeps only DTL's strategy edges for p, not p's
winning ones. Open step for (TW): show that a C_τ meeting W_p has no opponent vertex in W_{1-p} whose winning move is
forgiven, or find the straddling shape (L-RED: a learned tangle with an opponent vertex of W_{1-p} whose only winning move
goes into an earlier region or out of the context, inside a region whose top lies in W_p).

## 12. (NO-ORPHAN-W) is FALSE; the reduction restated with an existential (03:35Z by date -u)
Instance: experiments/red/carry/instances/gapbW_dup_n20.pg (L-RED, l-red 2b792b8, sha1 2ef690f9; Lead: pinned Oink 2
dominions, 8 tangles, 6 iterations, verified, -t prints "duplicate tangle" once). Reproduced here, both order data:
dtl_orphan.py "orphans inside W_p(G')": 1; dtl_loww.py: 3 of 3 searches satisfy (LOW-W). Anatomy (L-RED): Even's search 2,
|W_0(G')| = 19; the stored Even tangle {3, 17}, wholly inside W_0, 13 escapes, is re-found by a depth-1 call with |R| = 4
(a duplicate inside the winning region); the same search learns other tangles inside W_p, so the run is complete.
So (β-W) is false as a per-region statement: a lowest closed region inside W_p CAN re-find a stored tangle.
Restated reduction (the four parts become one existential):
  (K-low) If W_p(G') ≠ ∅ and search(p) finds no dominion, then AMONG the lowest regions of the stable pieces of the search
  (the candidates), at least one is closed, has its top in W_p(G'), and yields a NEW tangle inside W_p(G').
  DATA: holds in every case (dtl_loww.py: corpus 478/478 Oink, 459/459 stable; gapbW_dup_n20 3/3; gapb_dup_n20).
  PROVED around it: K5/K6 (a lowest region is closed unless (α)), SCC1 (one SCC), B-thr (how a duplicate arises), O0/O1,
  OPP-EXIT. GAP-K (the existential): why the candidates of one search cannot ALL fail (be open, outside W_p, or
  duplicates). Every route tried for a per-region version is dead (§4, §7, §8, §12). What an argument must use is the
  relation BETWEEN candidates of one search: a duplicate at a candidate exists only because earlier pieces of the same
  search removed all of its escapes (B-thr); so the earlier pieces themselves had to see those escapes, and a proof would
  show that one of those earlier pieces (or the recursion that removed them) contains a productive candidate inside W_p.
  Smallest shape that would break GAP-K (for L-RED; their current climb): a search with W_p ≠ ∅, no dominion, in which
  every candidate inside W_p is a duplicate of type (β-a)/(β-b) and every other candidate lies outside W_p or is open.

## 13. (K-first): the FIRST stable piece is the productive one; Case A proved up to (α) (04:01Z by date -u)
(K-first), DATA (experiments/alg/dtl_whichpiece.py; corpus + 1,500 random games): in every search of p with W_p(G') ≠ ∅ and
no dominion, the FIRST stable piece of the search (call order, any depth) is good: in one of its sptl passes the lowest top
that gets a region lies in W_p(G') and extracts a NEW tangle inside W_p(G'). Oink order 483 of 483 (31 of them mixed,
W_p ≠ G'), stable order 464 of 464 (31 mixed). (The LAST stable piece fails once in each order; "some piece" = LOW-W.)
This matches DTL-proof.md §2.3 K6 ("a search that learns nothing at its first stable set is of shape (α) or (β')"), now with
the location inside W_p.
Theorem A (PROVED, reading, given (α) does not occur). If the ROOT call (depth 0, first best_vertices call, X = ∅) of
search(p) returns 1, then its lowest region (top τ_k) lies in W_p(G'), and if it is closed (not (α), K5) it yields a new
tangle or a dominion, inside W_p(G'). Proof. K4 (DTL-proof.md §2.3, PROVED): the final threshold set A of a stable V* at
X = ∅ is p-won, A ⊆ W_p(G'); the regions are inside A, so τ_k ∈ W_p and C_{τ_k} ⊆ Z_k ⊆ W_p. By SCC1 the only candidate SCC
is C_{τ_k}; it is nontrivial when the region is closed (K5(ii)). It is not a stored tangle: by B-thr (ii) a duplicate has all
its escapes outside R = G', i.e. solved, which Lemma O0's argument excludes for any stored tangle (solved sets change only
between searches, and at the solving of a tangle's last escape the tangle is attracted or deleted; this holds equally for
tangles learned earlier in the same search, whose escapes lie in G' or are solved). So C_{τ_k} is new (or a dominion). □
Case split on data (experiments/alg/dtl_kfirst_case.py, Oink order, corpus + random): Case A (root call stable) only 2 of
483 searches. Case B, the first stable piece comes after −1 pieces: 481 (469 at depth 0 after 1 to 9+ calls, 12 at depth 1;
corrected 04:13Z, an earlier version said 474).
So the real obligation is Case B:
  GAP-K' (Case B). At depth 0, after −1 pieces have removed X (Dom(prevV) with Q empty, 962-991; threshold attractor and
  recursion, 899-954) with nothing learned, the first stable piece's lowest top lies in W_p(G'), its region is closed and
  its SCC is new and inside W_p. What is missing compared with Case A: K4 needs X to be p-won, and Dom(prevV) pieces need
  not be (DTL-proof.md §2.3); and B-thr allows duplicates whose escapes lie in X (the realised duplicates gapb_dup_n20 and
  gapbW_dup_n20 are at LATER stable pieces, consistent with (K-first)).
  Smallest shape that breaks GAP-K' (L-RED): a search with W_p ≠ ∅, no dominion, whose first stable piece (after −1
  pieces) has its lowest top outside W_p, or an open lowest region, or a duplicate there.
(K4-B), DATA (04:09Z by date -u; experiments/alg/dtl_k4b.py, Oink order, corpus + random): at the first stable piece of
every search with W_p(G') ≠ ∅ and no dominion, V* and the union of the final-round regions lie inside W_p(G'): 483 of 483
(31 mixed). With (K4-B), Theorem A's argument gives "lowest top in W_p" and (TW) for Case B as well, so GAP-K' becomes:
  (K4-B) the first stable piece's regions lie in W_p(G') even though X ≠ ∅ (K4's proof needs X p-won: an opponent vertex
         of A may have an edge into X, and the −1 pieces may have removed opponent-won vertices);
  (α)    its lowest region is closed;
  (β-1)  its SCC is not a stored tangle whose escapes all lie in X (B-thr with X ≠ ∅).
Reading of (K4-B): by OPP-EXIT-type reasoning, a vertex of A ∩ W_{1-p} would need the opponent's winning moves to leave A
into X ∩ W_{1-p}; a proof would show that every −1 piece removed before the first stable piece is a set from which the
opponent's winning moves cannot re-enter R. Not attempted further in this box.

## 14. Mixed test games: (K-first) and (K4-B) are FALSE; (K-low), (K-in), (TW) survive a real test (04:31Z by date -u)
Test set (experiments/alg/dtl_unionmix.py): disjoint unions of two corpus games (n ≤ 32 each, priorities kept), 900 pairs
(seeds 1-3), searches of p with W_p(G') ≠ ∅, |W_{1-p}(G')| ≥ 3 and no dominion: 891 mixed searches. Random games give
none (dtl_mixedgen.py: 0 of 12,000 random games qualify; every such search finds a dominion).
- (K4-B) "the first stable piece's regions lie in W_p": DEAD at once (the opponent-won component has its own p-priority
  tops); (K-first) "the FIRST stable piece's lowest region is productive inside W_p": DEAD, 276 of 891 mixed searches
  (88/304, 98/300 Oink order seeds 1-2; 90/287 stable order seed 3). Killer committed:
  experiments/alg/instances/kfirst_viol_union.pg (n = 26, Even wins 7; Even's searches 0 and 1 violate it in both order
  data; pinned Oink 7 iterations, verified). So the corpus results of §13 were an artefact of W_p = G' (or a single
  opponent vertex); Theorem A stands (it is about the root call).
- (K-low)/(LOW-W) "SOME stable piece's lowest region is productive inside W_p": holds on all 235 saved union games with a
  (K-first) violation, in every search with W_p ≠ ∅ and no dominion: 1,025 of 1,025 (Oink order), 1,067 of 1,067 (stable).
- (K-in): 0 violations there: 1,582 searches with W_p ≠ ∅ in Oink order and 1,647 in stable order (the two numbers are
  the two order data, not a gap; every one of them finds a dominion or learns inside W_p). (TW): 4,119 learned tangles inside W_p, 1,782 outside,
  0 straddling (stable 4,127 / 1,772 / 0): now a real test of (TW).
Current GAP-C statement (replaces §13's GAP-K'): (K-low) with GAP-K (the existential, §12), plus (TW) as the conjecture
that makes "inside W_p" automatic once a candidate's top is in W_p. Proved support: SCC1, B-thr, O0, O1, OPP-EXIT,
Theorem A, K5/K6.

## 15. The GAP-K mechanism on mixed games: the first stable piece with a top in W_p (04:44Z by date -u; experiments/alg/dtl_gapk.py)
Test set: the 235 union games of §14 (searches with W_p ≠ ∅, |W_{1-p}| ≥ 3, no dominion; 443 searches in each order).
- (FIRST-W), DATA: the first stable piece whose V* meets W_p(G') is productive (its lowest top lies in W_p and learns a new
  tangle inside W_p): 443 of 443 (Oink order), 443 of 443 (stable). On the corpus: 483/483 and 464/464 (§13's FIRST-W
  column). This is the GAP-K mechanism on data: stable pieces whose V* lies wholly in the opponent's region come first
  (1 to 3 of them: sequences "OPP OWN+G ...", "OPP OPP OWN+G ..."), then the first piece with a p-won top is the productive one.
- (V-sep), DATA with one exception: a stable V* lies wholly inside W_p or wholly inside W_{1-p}; 1 MIX piece in all these
  searches (not a FIRST-W failure). So (V-sep) is FALSE as stated (1 case) but nearly always true.
- What does NOT hold: before the first such piece, W_p is untouched (FALSE: some p-won vertices are already removed by
  −1 pieces in 443 of 443); its context lies inside W_p (216 inside, 227 meeting W_{1-p}, Oink order).
Restated GAP-K (the existential as a rule): (FIRST-W) the first stable piece with a top in W_p(G') has a closed lowest
region with its top in W_p and a new SCC inside W_p. Theorem A is its special case "the root call is stable and meets W_p"
(K4 then puts all of V* in W_p). What a proof must handle: the −1 pieces before it remove p-won vertices into X (so K4's
"X p-won" hypothesis fails), and its context may still contain opponent-won vertices.
L-RED target (sharper than an incomplete run, cheap to check with dtl_gapk.py, which prints "FIRST-W FAILS"): a search
with W_p ≠ ∅ and no dominion whose first stable piece with a p-won top is not productive inside W_p.
