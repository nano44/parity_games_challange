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
| FIRST-W | the first stable piece with a p-won top is productive inside W_p | KILLED (§16): instances/firstw_viol_cross.pg |
| GAP-K | (K-low): some stable piece's lowest region is productive inside W_p | GAP (§12, §14); DATA 0 violations incl. 2,092 mixed union searches |
| K frame (18b) | K(R): D ∩ R not wholly p-attracted to X; K0 (K(G'), not K(R_end)) | K0 PROVED; route DEAD: (P-K), (K-STEP-first) KILLED by L-RED pk_viol_n20 (18f) |
| P-K1 (18f) | Case 1 of (P-K): max priority of D ∩ R of p's parity | PROVED given (YZ), (WM) |
| KT frame (18g) | KT(R): thresholded core at some p-parity level c | KT(G'), not KT(R_end) PROVED; (KT-STEP-first) DATA 0 violations |
| Step 5 = P-KT (18h) | a depth-0 P piece (Dom(prevV), Q empty) keeps KT | PROVED given (YZ) only ((WM_c1) PROVED via NT-f, 18k); (YZ) DATA 0 failures |
| S step, T step (18g) | a piece after which KT fails learns inside D (nothing learned in D before) | DATA only; S step contains (α), (β) |
| YZ-read (18h) | Dom(prevV) = final round's regions unless an X-straddling tangle fires in Dom | PROVED (reading); (YZ) itself DATA |
| FM, FM+ (18h) | final union of a −1 call inside every earlier round's union | PROVED (18k, via NT-f); DATA 106,091/106,091 calls |
| NT-f (18k) | the final pruning round of a −1 call accepts no stored tangle | PROVED (reading); intermediate-round analogue INV-T FALSE (c_best_s34.pg) |
| T step split (18i) | (CORE-PASS-closed): a T piece that breaks KT hands the recursion a p-dominion of G[Z'] inside D; then (REC) | DATA 45/45; P-KT carries over to depth 1 |
| S-LOC / S-LEVEL (18j) | S learning lies in the core of SOME KT level / of EVERY destroyed level meeting V* | S-LOC DATA 0 violations; S-LEVEL KILLED (cross_h_k1_n12_m18_17) |

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

## 16. Interacting mixed games: (FIRST-W) is FALSE; (K-low) and (K-in) still hold (04:50Z by date -u)
Test set: unions of two corpus games with 3 or 6 random cross edges between the components (dtl_unionmix.py UM_CROSS),
1,200 pairs (seeds 11, 12 Oink order with 3 cross edges; seed 13 stable order with 6): 188 mixed searches (W_p ≠ ∅,
|W_{1-p}| ≥ 3, no dominion).
- (K-first) fails in 35, (FIRST-W) in 4 (all with a MIX first piece meeting W_p: V* on both sides).
  Killer committed: experiments/alg/instances/firstw_viol_cross.pg (n = 30; both order data, dtl_gapk.py "FIRST-W FAILS";
  pinned Oink 6 iterations, verified).
- (K-low)/(LOW-W): 188 of 188; (K-in): 188 of 188.
So no rule that names the productive piece in advance survives (first piece, first piece with a p-won top); the GAP-C
statement stays the existential (K-low) (GAP-K) plus (TW). Data so far: 0 violations of (K-low) and (K-in) on the corpus,
1,500 random games, 235 disjoint unions, 1,200 interacting unions, both order data where run.

## 17. SKETCH of the GAP-K argument (Lead 04:56Z: a written sketch, no more experiments) (04:55Z by date -u)
Claim to prove (K-low): if D := W_p(G') ≠ ∅, search(p) finds a dominion or some stable piece's lowest region is closed, has
its top in D and yields a new tangle inside D. Contrapositive route: assume search(p) learns nothing and finds no dominion
(every candidate fails) and derive D = ∅. Notation: depth-0 iterations i = 1..m with contexts R_1 = G' ⊋ R_2 ⊋ ...,
removed sets Y_i (X_i = Y_1 ∪ ... ∪ Y_{i-1}), R_end = the last context (it has no p-priority vertex: best_vertices returned
0); −1 pieces with Q nonempty recurse on their attractor's rest, which is again a search_rec with the same structure.
Step 1 (PROVED; SCC1, K5/K6, B-thr). An unproductive search has, at every stable piece, every closed region at a top not in
W yielding nothing, so its lowest region is open with a straddling tangle (α) or re-finds a stored tangle all of whose
escapes lie outside the context (β-a/β-b of B-thr).
Step 2 (PROVED, trivial). Every infinite play that stays in R_end is won by the opponent (R_end has no p-priority vertex).
Step 3 (PROVED; Theorem A). If iteration 1 is stable, (α) is the only way to fail; so for an unproductive search either
iteration 1 is (α), or iteration 1 is a −1 piece.
Step 4 (SKETCH). Forgiving induction. Call a set Y ⊆ G' p-safe for context R if every opponent edge from R into Y is
"forgiven" by DTL (dtl.cpp 75-86 judge escapes in R only). Hypothesis H_i: D ∩ R_i ≠ ∅ implies the game on R_i in which the
opponent may not enter X_i still has a nonempty p-winning region inside D ∩ R_i. H_1 holds (D is a p-dominion of G'). A
stable unproductive piece keeps H (its removal Dom(V*, R_i) is, by K4 relative to X_i, p-won in that forgiving game, so
removing it leaves the rest of D p-winning in the smaller forgiving game). A −1 piece with Q nonempty (threshold attractor
to X_i) keeps H by the same attractor argument (its removal is p-attracted to X_i at threshold t).
Step 5 (GAP; the hardest step). A −1 piece with Q EMPTY removes Dom(prevV, R_i) (962-991), the region of the last
pruned "distractions". This removal is NOT p-won in general and NOT opponent-won either: (S2) shows contexts that are
entirely p-won are pruned to −1 (spp_final_n20, Odd's root call), and (Cb1) shows the p-dominion inside the context can be
destroyed by this removal with nothing learned (c1_k1_min_n7_m10, c6_replay3_n32). So H_i can FAIL across such a piece in the
strict sense, and in the forgiving sense the induction cannot conclude: at R_end the forgiving game lets p's vertices leave
into X (counted p-safe), so H_end does not contradict Step 2. What is needed instead is a statement that charges each
Dom(prevV) removal of p-won vertices to a LATER candidate of the same search: "if Dom(prevV, R_i) removes a p-won vertex v,
then some later stable piece has a closed lowest region inside D that is not a stored tangle". The data say exactly this
(K-low; the productive candidate follows OPP and MIX pieces, §15-§16), but no invariant that transports it is known: every
per-piece candidate (S2, Cb1, PEEL, K-first, K4-B, FIRST-W) is dead with an instance.
Step 6 (GAP, secondary). (α) at the candidate: the lowest region open because its top's successor lies in the lower part of
a straddling tangle (DTL-proof.md §2.3; the regress route is dead, R11). Plausibly reducible to Step 5 (a straddle needs a
tangle learned in another context), not shown.
Hardest single step: Step 5, the Dom(prevV)-with-Q-empty removal (dtl.cpp 962-991). It is the one place where DTL removes
vertices on an "optimistic for p" basis (later pruning forgives the opponent's exits into it) without a p-won certificate,
and the completeness proof must show that this optimism is always repaid by a later productive candidate inside W_p. It is
the same obligation as DTL-proof.md §2.3 (C-b), now with its quantitative form (K-low) and with instances showing that no
local invariant carries it.

## 18. Step 5 (box 6, L-ALG succ. 6, produced on Opus 5.5; 05:45Z by date -u): Dom(prevV) read exactly; invariant K
Unrefereed. Tools: experiments/alg/dtl_step5.py (piece tracer: S / T / P / E per search_rec iteration, every depth),
dtl_step5stats.py (segment, LASTD, HYB, JD, K counters), dtl_pnl.py (PNL*, YZ, MONO, R-MONO, KEEP). Test set (both order
data unless said): 238 corpus files (every .pg under experiments/ with n ≤ 80 that pg.py parses, plus L-RED's
kfirst_viol_n13.pg, origin/claude/l-red 46f3520); disjoint unions (UNIONS=900, seeds 1 Oink / 2 stable) and unions with 3
random cross edges (600, seed 11, Oink); only searches with D := W_p(G') ≠ ∅ and no dominion; unions only mixed ones
(|W_{1-p}| ≥ 3). "dtl.cpp N" = tools/oink/src/src/solvers/dtl.cpp @ 8fbf0a7.

### 18a. What the −1 branch with Q empty removes and leaves (task (1); reading of dtl.cpp 852-991, C5 §2)
- Trigger. best_vertices (643-776) returned −1 with V restored to prevV (676, 770: the tops of the last pruning round), and
  the threshold scan 898-912 found no vertex: no v ∈ R with attracts(p, v, X, R) (40-57). So: no p-vertex of R has an edge
  into X, and every opponent vertex of R with an edge into X also has an edge into R. At depth 0, X = G' \ R (every piece
  moves exactly what it takes from R into X: S 877-890, T 914-951, P 961-976), so R is a p-TRAP of G' (PROVED; DATA
  TRAP 1,582/1,582 corpus Oink) and H := G[R] is a parity game (every vertex keeps a successor in R).
- Removal (961-991). For each top of prevV from high index down that is not yet in X: X ∪= {top}, str[top] := −1, then the
  tangle attractor INTO X (the whole X) within R, escapes judged in R (opponent edges leaving R ignored), threshold
  pr(top), R consumed. Call the removed set Y_0.
- (YZ) Y_0 = Z_f, the union of the final pruning round's regions (690-708 with V = prevV). Reading: the two computations
  differ only in attractTangle (110-185) for a stored tangle with a vertex in X or in an earlier region of the same pass
  (counted "in Z" by Dom at 136-137, "not in R" by best_vertices' CurR at 138-139), so Dom can only take more. DATA: equal
  in 3,121/3,121 depth-0 and 1,136/1,136 deeper P pieces (corpus, Oink order).
- Every τ ∈ prevV was a candidate of the final round and was not rescued: ¬attracts(p, τ, Z_f, R) (a p-owned τ has NO
  edge into Z_f, so every region of a p-owned top is OPEN; an opponent-owned τ has an edge into R \ Z_f or none into
  Z_f), and for every t < pr(τ), τ does not attract into A_t, the threshold-t tangle attractor of Z_f within R (rescue loop 722-740;
  candidates 714-716, removal 747-760).
- Leaves R' = R \ Y_0. A p-vertex of R' with an edge into the region of τ has priority > pr(τ) (else attracted at 976);
  the next iteration's threshold scan (898-912) seeds at the lowest level holding a vertex that attracts into X ∪ Y_0 (a T piece),
  or, if none, another P piece.
- It is neither p-won nor opponent-won: kfirst_viol_n13 (Even's search 0, both orders) removes {6, 3} with 6 ∈ W_0, 3 ∈ W_1
  (original ids). Composition of depth-0 P pieces: corpus Oink D-only 1,539, W_{1-p}-only 35, mixed 8; disjoint unions Oink
  1,159 / 1,285 / 309, stable 1,108 / 1,439 / 257.

### 18b. Invariant K (definitions and the PROVED frame)
Fix a search of p, G', D = W_p(G') ≠ ∅, σ a positional winning strategy of p on D in G' (plays stay in D). For a depth-0
context R (X = G' \ R) let A_D(R) be the least A ⊆ D ∩ R with: a p-vertex of D ∩ R with an edge into X ∪ A is in A; an
opponent vertex of D ∩ R all of whose edges lie in X ∪ A is in A (X is a p-won SINK, as DTL's threshold step 897-912 and its
forgiving attractors treat it). Q(R) := (D ∩ R) \ A_D(R); K(R) :⇔ Q(R) ≠ ∅.
Lemma K0 (PROVED). (a) If Q(R) ≠ ∅, every p-vertex v ∈ Q(R) has σ(v) ∈ Q(R) (σ(v) ∈ X ∪ A would put v into A) and every
opponent vertex of Q(R) has an edge into Q(R) (else all its edges, which lie in D, are in X ∪ A); every play staying in
Q(R) and consistent with σ is a G'-play from D consistent with σ, so p wins it: Q(R) is a p-dominion of the subgame G[Q(R)]
(the game in which the opponent's edges LEAVING Q(R) are deleted). Closure used: σ-closed, and every opponent vertex keeps
at least one edge into Q(R); Q(R) is NOT opponent-closed in G' (an opponent vertex may also have edges into A ∪ X). Only
this is used downstream ((c) needs one infinite σ-consistent play inside Q(R)). (Clarified 06:20Z after the Lead's check.)
(b) K(G') holds (X = ∅, A = ∅, Q = D). (c) K(R_end) fails, R_end the context where best_vertices returns 0 (dtl.cpp
651-655): R_end has no p-priority vertex, so every infinite play inside Q(R_end) is won by the opponent, while (a) gives a
σ-consistent infinite play inside Q(R_end) (opponent picks an edge into Q) won by p; so Q(R_end) = ∅. (d) So in every search
with D ≠ ∅ some depth-0 piece turns K from true to false. □
Consequence (PROVED from K0): (K-in) follows from
  (K-STEP-first) the FIRST depth-0 piece after which K fails (a T piece counted with its recursion) learns a tangle inside D
  or finds a dominion.
At a P piece, A_D(R) = ∅ (the trigger: nothing of R attracts into X), so K(R) ⇔ D ∩ R ≠ ∅. Step 5 of §17 becomes:
  (P-K) A depth-0 P piece keeps K: if D ∩ R ≠ ∅ then D ∩ R ⊄ Y_0 ∪ A_D(R \ Y_0), i.e. the part of D left after Dom(prevV, R)
  is not all p-attracted to X ∪ Y_0. (The removal never needs repaying INSIDE its own piece; it only must not make D
  "attractor-only".)

### 18c. DATA (counts of depth-0 pieces in searches with D ≠ ∅ and no dominion) — both statements KILLED at 06:20Z, 18f
| statement | corpus Oink | corpus stable | unions Oink s1 | unions stable s2 | cross Oink s11 |
|---|---|---|---|---|---|
| (P-K): K broken by a P piece | 0 (kept 1,556) | 0 | 0 | 0 | 0 |
| (K-STEP-first) violations / searches | 0 / 512 | 0 / 493 | 0 / 738 | 0 / 692 | 0 / 116 |
| first break by S that learns / by T that learns | 497 / 12 | 478 / 12 | 713 / 18 | 662 / 24 | 109 / 3 |
| first break barren, but D-learning earlier in the search | 3 | 3 | 7 | 6 | 4 |
| (SEG-LAST) the last depth-0 segment (P piece to next P piece) meeting D learns inside D | 512/512 | 493/493 | 738/738 | 692/692 | 116/116 |
(K-STEP) per piece ("every barren piece keeps K") is FALSE: barren breaks after earlier learning, e.g. S at
experiments/red/carry/instances/gapbW_dup_n20.pg, T at experiments/alg/instances/cross_h_k1_n12_m19_42.pg (both Oink order).
So a proof of the S and T steps must use "nothing learned inside D so far in this search" (stored tangles then predate the
search); the P step needs no such hypothesis on data.

### 18d. Killed on the way (each with its instance; Oink order, corpus)
- (HYB) "the game on D ∩ R where a vertex without successor loses for p keeps a p-winning region across barren pieces":
  broken by P pieces 548 times; smallest experiments/alg/instances/strfam_S2_n4.pg (n = 4, Odd's search, W_1 = all four
  vertices: the P piece removes {0}; vertex 2's only edge then goes into X, so the game on D ∩ R' loses at 2; the next T
  piece takes 2 and the S piece after it learns {1}). Treating X as p-LOSING is wrong for DTL.
- (JD) "D ∩ R holds a set, closed for the opponent with X forgiven and p-closed inside R, with a p-priority vertex": broken by
  P pieces 86 times; smallest experiments/attr/instances/psolc_partial_n5-8_K60000_s2_1_n4_m6.pg (n = 4). Fix: let p use X
  too (that is K).
- (ATTR) "the D-vertices a P piece removes are p-attracted to the D left behind": 562 violations (smallest
  experiments/attr/instances/psolc_min_n4_m6.pg).
- (SEG-ALL) "every segment whose start meets D learns inside D": 364 of 512 searches violate (c1_k1_min_n7_m10.pg).
- (LASTD) "the piece removing the last D-vertex learns": false for T pieces (26; cross_h_k1_n12_m19_42.pg), mop-up after
  learning; true for S (389/389); a P piece is never last (0).
- (KEEP) per pruning round, "p-priority vertices in the greatest p-closed subset of Z^r are still in V_r": 144 violations
  (experiments/alg/instances/climbs_1016/c_best_s34.pg, round 4: vertex 16 pruned at round 3 while 2 ∉ Z^3, 2 ∈ Z^4 again).
  (MONO) Z^{r+1} ⊆ Z^r fails 135 times in 40,346 round pairs, (R-MONO) its p-closed part 125 times.

### 18e. (PNL*) and the route to (P-K) (SKETCH; GAP named)
(PNL*) DATA: Y_0 never contains a nonempty B ⊆ R holding a p-priority vertex in which every opponent vertex has all its
R-edges in B (at least one) and every p-vertex an R-edge into B: 3,121/3,121 depth-0 and 1,136/1,136 deeper P pieces
(corpus Oink; greatest such B empty in 2,615 + 897, nonempty without p-priority vertex in 506 + 239).
Proof of (PNL*) given (YZ) and monotonicity (PROVED part + GAP). Let B ⊆ Z_f be such a set. (i) prevV ∩ B = ∅: a p-owned
v ∈ prevV ∩ B has an edge into B ⊆ Z_f, an opponent-owned one has all R-edges in B ⊆ Z_f, so v attracts into Z_f, is no
candidate, stays in V, and best_vertices could not have returned −1 (PROVED). (ii) Let r0 be the last round with
V_{r0} ∩ B ≠ ∅ (B's p-priority vertex is in V_1). If B ⊆ Z^{r0}, the argument of (i) keeps V_{r0} ∩ B in V_{r0+1}: a
contradiction (PROVED). (iii) B ⊆ Z^{r_f} ⇒ B ⊆ Z^{r0}: holds if the region union is monotone along the rounds of one call
(GAP: (MONO) and (R-MONO) are FALSE on A_DTL, §18d; the failures come from straddling stored tangles, GAP-A-M Lemma E, the
same mechanism as (α)). PNL* holds on all data although (MONO) fails, so step (iii) needs an argument specific to B.
(P-K) is stronger than (PNL*) (Y_0 ∪ attractor instead of Y_0); its proof route is the same three steps with B replaced by
"the part of D whose attraction to X ∪ Y_0 uses no vertex of a pruned top's good path" — not written.

### 18f. (P-K): Case 1 PROVED (given (YZ), (WM)); Case 2 FALSE (06:11Z; status line 06:20Z by date -u)
STATUS 06:20Z: (P-K) and (K-STEP-first) are KILLED by L-RED R27 (l-red 1cad017/184e4d8),
experiments/red/carry/instances/pk_viol_n20.pg (sha1 942bd778; Lead: pinned Oink 1 dominion, 4 tangles, 2 iterations,
verified; Even wins all 20), both order data: Even's search 0 = P piece (prevV {8, 11, 12, 13}) removing 14 of the 20
D-vertices, then T at t = 15 removing {7}, then a stable piece learning {3, 5, 6} inside D; after the P piece
Q(R') = ∅. It is CASE 2 (max priority of D ∩ R = 17, the opponent's parity); (YZ), WM-global and (PNL*) hold on it
(dtl_pnl.py, both orders). So Lemma P-K1 below is not contradicted, and the K-frame of 18b is DEAD as a route to (K-in):
its "X is a p-won sink" lets p use a path 6 → 15 → 7 → X through a high opponent vertex (15, priority 17) that DTL's
threshold step (t = 15) never uses, while DTL's next stable piece finds {3, 5, 6} closed with its exits into X forgiven.
Setting: a depth-0 P piece, R a p-trap (18a), H = G[R], D_R := D ∩ R ≠ ∅ a p-dominion of H (PROVED: opponent vertices of
D keep all their edges in D, p's σ stays in D and, R being a p-trap, in R). Rounds r = 1..r_f of the −1 call, tops V_r,
region unions Z^r, Z := Z_f = Z^{r_f}; A^r_t := the threshold-t tangle attractor of Z^r within R (rescue loop 722-731);
A_t := A^{r_f}_t. A P-K violation means (COVER): D_R ⊆ Z ∪ A_D, A_D the plain p-attractor of Z inside D_R (with (YZ),
Y_0 = Z). Every p-priority vertex x of R leaves V at some round r(x) (the call ends with V = ∅), as a candidate that is not
rescued: (GAP_r) x does not attract into A^{r(x)}_{pr(x)−1} (p-owned: no successor there; opponent-owned: an R-successor
outside it). (WM) Z ⊆ A^{r(x)}_{pr(x)−1}; with (WM), GAP_r gives (GAP) x does not attract into A_{pr(x)−1}.
Lemma P-K1 (Case 1; PROVED given (YZ), (WM)). If M := max pr(D_R) has p's parity, (COVER) is impossible.
Proof. Let T_M := D_R ∩ pr^{-1}(M) (nonempty; all p-priority vertices, hence in V_1). Let A'' := the plain p-attractor of Z
inside D_R using only vertices of priority ≤ M−1; A'' ⊆ A_{M−1} (A_{M−1} is closed under that attraction within R ⊇ D_R:
an opponent vertex of D_R has all its R-edges in D_R). Let N := D_R \ (Z ∪ A'') and suppose N ≠ ∅; take x ∈ N of least
rank in A_D (COVER). If x is p-owned it was attracted through a successor y of smaller rank, so y ∈ Z ∪ A'' (y ∈ D_R would
be in N otherwise; a p-vertex of R has no edge into X at a P piece); then pr(x) ≤ M−1 puts x into A'', and pr(x) = M
contradicts (GAP) (y ∈ A_{M−1}). If x is opponent-owned, all its R-edges (at least one) lead to smaller ranks, hence into
Z ∪ A''; pr(x) ≤ M−1 puts x into A'', pr(x) = M contradicts (GAP). So N = ∅, D_R ⊆ Z ∪ A''. Vertices of priority M never
enter A'', so T_M ⊆ Z. For w ∈ T_M: p-owned, σ(w) ∈ D_R ⊆ A_{M−1}; opponent-owned, all R-edges in D_R ⊆ A_{M−1}; either
way w attracts into A_{M−1}, contradicting (GAP). □
DATA (corpus Oink): of 1,595 depth-0 P pieces with D ∩ R ≠ ∅, Case 1 holds in 1,380 ((WM) for T_M holds in all 1,380;
in 151 of them T_M ⊆ V_f, so (WM) is trivial there); (WM) for EVERY p-priority vertex of R ("WM-global") holds in
1,595/1,595 although (MONO) fails elsewhere (18d). (YZ) 4,257/4,257. Case 2 (M of the opponent's parity): 215.
Case 2 (FALSE as a statement: pk_viol_n20). What survives of the argument (PROVED, given (GAP) for every p-priority vertex of R and (COVER)): let π* be
the opponent strategy choosing in D_R a successor of largest level θ (θ(x) = least t with x ∈ A_t; finite on D_R by
COVER). For every cycle C formed by σ and π* in D_R, with maximum c (p's parity, σ wins): (i) θ ≥ c on C (a step from
θ ≥ c to θ < c at x would put x into A_{c−1} when pr(x) < c, and contradict (GAP) when pr(x) = c); (ii) the least θ on C,
k, is > c and of the opponent's parity, and the attraction path from C (p steers, π* follows) meets a vertex u_C ∈ D_R
with pr(u_C) = θ(u_C) = k (the first own-level vertex on the path; a p-parity one would contradict (GAP)). So under a
violation every p-won cycle of D_R is attracted to Z only through a higher opponent-parity vertex of D_R. The missing step
is the top of this ladder: the opponent's top priority M of D_R is visited finitely often by σ, and nothing found so far
forces a σ-play back through u_C. The plain abstraction (GAP + COVER only) is NOT contradictory: D = {w (p-owned, priority
2) → h, e; h (opponent, 1) → w; e (p-owned, 5) → f ∈ Z, w} satisfies both (GAP wrt the final A_t); the contradiction must
use the region of w at round r(w) (there h, whose only edge goes to w, lies in w's region, so w is not a candidate).
Case 2 DATA: O_M := D_R ∩ pr^{-1}(M) never meets Z_f (215/215); O_M meets Q(R') in 178/215; the maximum priority in Q(R')
has the opponent's parity in 178, p's parity in 37.
More DATA for 18f (06:18Z by date -u; dtl_pnl.py, ALL searches incl. those that find a dominion): corpus stable — Case 1
1,307 ((WM) holds in all), Case 2 224, WM-global 1,531/1,531, (YZ) 3,038 + 1,136, (PNL*) 3,038 + 1,136; 900 disjoint
unions Oink (seed 1) — Case 1 8,116, Case 2 1,240, WM-global 9,356/9,356, (YZ) and (PNL*) 20,300 + 9,516; 600 unions
with 3 cross edges Oink (seed 11) — Case 1 4,492, Case 2 828, WM-global 5,320/5,320, (YZ) and (PNL*) 13,171 + 5,072.
O_M never meets Z_f (215 + 224 + 1,240 + 828). Nearest Case 2 miss (attack seed for L-RED): experiments/alg/instances/
c6_replay3_n48.pg, Odd's search, a P piece with |R| = |D ∩ R| = 43, Z_f = {10, 38}: Q(R') = {21} only (original ids;
21 has priority 17, is Even-owned with a self-loop and an edge to 1). An opponent vertex on a p-won cycle of opponent
vertices can never be attracted first, so such cycles keep Q nonempty; a violation needs every such cycle to meet Z_f.

### 18g. Candidate KT (thresholded K; the Lead's lead 06:12Z) — DATA, not proved (06:32Z by date -u)
Definition. For a depth-0 context R (X = G' \ R) and c of p's parity: S_c := D ∩ R ∩ {priority ≤ c}; A_c := the plain
p-attractor of X inside S_c (a p-vertex enters with an edge into X ∪ A_c; an opponent vertex only if ALL its edges lie in
X ∪ A_c, so an edge to a D-vertex of priority > c blocks it); Q_c := S_c \ A_c; F_c := the game on Q_c in which the
opponent's edges leaving Q_c are deleted (forgiven, as DTL's regions forgive) and a vertex without successor loses for p.
KT(R) :⇔ some c has W_p(F_c) ≠ ∅. Differences from K: attraction to X only through priorities ≤ c (DTL's threshold step
and regions never use a path through a higher vertex, the pk_viol_n20 mechanism), and the core must be won by cycles.
PROVED: KT(G') holds when D ≠ ∅ (a p-dominion of H inside D with the least maximum has a maximum c1 of p's parity, lies in
S_{c1}, keeps σ inside and the opponent inside, and X = ∅); KT(R_end) fails (F_c on R_end has no p-won cycle).
DATA (dtl_step5stats.py "KTHR"; searches with D ≠ ∅ and no dominion; corpus = 238 files + kfirst_viol_n13 + pk_viol_n20):
| | corpus Oink | corpus stable | unions Oink s1 | cross Oink s11 |
|---|---|---|---|---|
| KT broken by a P piece | 0 (kept 1,557) | 0 (kept 1,493) | 0 (kept 2,064) | 0 (kept 455) |
| first KT-break barren with nothing learned inside D before | 0 / 513 | 0 / 494 | 0 / 738 | 0 / 116 |
| barren breaks after D-learning (S / T) | 1 / 3 | 1 / 3 | 7 / 0 | 0 / 4 |
On pk_viol_n20 (both orders) KT holds after the P piece at c = 12 (S_12 ∩ R' = {3, 5, 6}, A_12 = ∅, cycle 6 → 3 → 5 with
maximum 12), the T piece keeps it, the stable piece learns {3, 5, 6}.
Proof route for "P keeps KT" (SKETCH): take the core U at a level c where U holds a vertex of priority c; the argument of
P-K1 inside S_c (attraction only through priorities ≤ c) gives a contradiction at every p-owned vertex of priority c in U;
the open case is an opponent-owned priority-c vertex of U whose exit goes to a D-vertex of priority > c (forgiven by F_c,
not by GAP).

### 18h. Step 5 for KT: a P piece keeps KT — PROVED given (YZ) and (WM_c1) (06:44Z by date -u)
Setting of 18f (depth-0 P piece, R a p-trap, H = G[R], D_R = D ∩ R ≠ ∅ a p-dominion of H, Z := Z_f, every p-priority
vertex x of R leaves V at a round r(x) as a candidate that is not rescued).
Definitions. W1 := a p-dominion of H inside D_R whose maximum priority c1 is least among all such. c1 has p's parity: if it
had the opponent's, W1 minus the opponent's attractor (in W1) to its top priority is closed in H and contains a nonempty
p-dominion of H with a smaller maximum (Zielonka's step). W1 is CLOSED in H: every opponent vertex of W1 has all its
R-edges in W1, and p has a strategy σ1 that keeps every play in W1 and wins it. T := W1 ∩ pr^{-1}(c1) ≠ ∅.
(WM_c1): for every x ∈ D_R of priority c1, Z ⊆ A^{r(x)}_{c1−1} (the rescue attractor of x's round at threshold c1−1).
(YZ): Y_0 = Z (the P piece removes exactly the final round's region union).
Lemma P-KT (PROVED given (YZ), (WM_c1)). Let R' := R \ Y_0, S := D ∩ R' ∩ {priority ≤ c1}, A := the plain p-attractor of
X ∪ Z inside S (KT's A_{c1}(R'), X ∪ Y_0 being G' \ R'). Then U := W1 \ (Z ∪ A) ≠ ∅, and U ⊆ W_p(F_{c1}(R')), so KT(R').
Proof. (1) A'' := the plain p-attractor of X ∪ Z inside S ∩ {priority ≤ c1−1}. A'' ⊆ A^{r}_{c1−1} for every round r with
Z ⊆ A^{r}_{c1−1}: after the level-t pass of the rescue loop (722-731) the set is closed under attraction of vertices of
priority ≤ t (every element is popped once more after the last addition); a p-vertex of R has no edge into X (R is a
p-trap) and an opponent vertex of R keeps an R-edge, so A'''s rules are instances of the rescue rules.
(2) A = A''. Otherwise take x ∈ A \ A'' of least rank in A. Its witnesses (one successor if p-owned, all successors if
opponent-owned) lie in X ∪ Z ∪ (A of smaller rank) ⊆ X ∪ Z ∪ A''. If pr(x) ≤ c1−1, x ∈ A''. If pr(x) = c1 (p's parity),
x attracts into Z ∪ A'' ⊆ A^{r(x)}_{c1−1} by (WM_c1) and (1) (p-owned: one edge; opponent-owned: all R-edges, at least one),
so x would have been rescued in round r(x): contradiction.
(3) If U = ∅ then W1 ⊆ Z ∪ A'' by (2); A'' has no vertex of priority c1, so T ⊆ Z. Take w ∈ T: if p-owned, σ1(w) ∈ W1 ⊆
Z ∪ A''; if opponent-owned, all its R-edges lie in W1 ⊆ Z ∪ A'' (W1 closed in H). Either way w attracts into
A^{r(w)}_{c1−1}, so w was rescued: contradiction. So U ≠ ∅.
(4) U ⊆ Q_{c1}(R') = S \ A. A p-vertex v ∈ U has σ1(v) ∈ U (σ1(v) ∈ W1; σ1(v) ∈ Z ∪ A would put v into A). An opponent
vertex v ∈ U has all its R-edges in W1, hence its R'-edges in U ∪ A, and at least one in U (else all its edges lie in
X ∪ Z ∪ A and v ∈ A). In F_{c1}(R') the edges into A are deleted, so U is closed for the opponent, has no dead end, and
every play in U consistent with σ1 is a W1-play consistent with σ1, won by p. □
Remarks. No hypothesis KT(R) is needed: at every depth-0 P piece with D ∩ R ≠ ∅, KT(R') holds, witnessed at the level
c1 of the least-maximum p-dominion. This is Step 5 of §17 in the KT frame: the Dom(prevV) removal does not destroy the
low dominion's core at its own threshold, whatever p-won vertices it takes. Where K (18b) failed (pk_viol_n20, Case 2)
the argument works because W1 is closed in H with maximum c1 of p's parity, so Case 2 of 18f never arises at level c1.
DATA (dtl_pnl.py "P-KT", every depth-0 P piece with D ∩ R ≠ ∅, all searches): U ≠ ∅ in 1,596/1,596 corpus Oink (incl.
kfirst_viol_n13, pk_viol_n20), 1,532/1,532 corpus stable, 9,356/9,356 disjoint unions Oink s1, 4,613/4,613 cross unions
stable s13 (6 cross edges). (WM) for all p-priority vertices of R and (YZ) hold in every one of these pieces.
Open hypotheses: (YZ) (DATA 63,000+ P pieces, all depths; reading: Dom can only take more, through stored tangles with a
vertex in X or in an earlier region of the same pass) and (WM_c1) (DATA; implied by monotonicity of the region union
between round r(x) and the last round, which is FALSE in general (18d), so a proof must use the specific rounds).
What KT still needs for (K-in): the S step and the T step ("a piece after which KT fails learns inside D, as long as
nothing was learned inside D earlier in the search"); both are DATA only (18g), and the S step contains (α) and (β).
(YZ) by code reading (06:55Z by date -u; Lead order 06:48Z). Compare Dom(prevV, R) (961-976) with the final pruning round's
region loop (690-708), both over the same R, tops prevV from high index down, skipping a top already taken (X[top] /
Z[top]). The loops push the same vertex, pop it, and drop it from the consumed set (R[v] = false / CurR[v] = false) at the
same steps, as long as every attractVertices and attractTangle call returns the same answer:
- attractVertices(p, v, R, X, R, pr) vs (p, v, CurR, CurZ, CurR, pr): with the same consumed set, a predecessor u is "in
  Z" in Dom iff u ∈ X, in the region loop iff u ∈ CurZ; X ∩ R and CurZ ∩ CurR are both the pushed-not-yet-popped vertices of
  the current top, and the other members of X (old X, earlier tops' popped vertices) are outside R, so the membership test
  "u ∈ R" and the escape test "edge into Gx \ Z" give identical answers; only str differs.
- attractTangle (110-185): identical answers except for a stored tangle t with a vertex w that is in X but not in R (old X
  or a popped vertex of an earlier top): Dom skips w as "in Z" (136-137), the region loop rejects t (w ∉ CurZ, w ∉ CurR,
  138-139). Escapes in old X or in earlier regions are "in Z" for Dom and outside Gx for the region loop: same answer.
So (YZ-read, PROVED): Y_0 = Z_f unless, during Dom(prevV, R), attractTangle accepts a stored p-tangle that has a vertex in
old X or in an earlier top's part of this Dom; until the first such acceptance the two computations are step-for-step
equal. At a P piece no p-vertex of R has an edge into X, so such a tangle enters R from X only through opponent edges.
(YZ) is therefore NOT true by the code alone; it is the absence of an X-straddling tangle firing (the straddle family of
GAP-A-M Lemma E). DATA: never on 63,000+ P pieces (all depths, both orders, unions).
(WM_c1) reduced (07:11Z by date -u; Lead caution 06:48Z: why the c1 form escapes the 135 MONO failures).
(FM) In a −1 call, Z_f ⊆ Z^r for EVERY round r (the final union lies inside every earlier union; consecutive rounds may
still violate (MONO), as long as what the final round keeps was in each earlier union). (FM) ⇒ (WM) for every vertex and
level: Z_f ⊆ Z^r ⊆ A^r_t for all t (the rescue loop starts from Z^r). (FM) holds (PROVED) for every −1 call without a
deficit round (U = Û at each round, GAP-A-M §2-§3): Z_f = U(V_f) ⊆ Û(V_f) ⊆ Û(V_r) = U(V_r) by Lemmas 2.2, 2.1.
DATA (dtl_pnl.py "FM", every −1 call at every depth, all searches): 7,955/7,955 corpus Oink, 7,803/7,803 corpus stable,
57,864/57,864 disjoint unions Oink s1, 32,469/32,469 cross unions stable s13 — 106,091 calls, 0 failures, although
(MONO) fails in 135 round pairs of the corpus (Oink) alone. At the rounds that (WM_c1) uses, the deficit set Z_f \ Z^{r(x)}
is EMPTY in every case (2,322 corpus Oink, 15,144 unions, 7,280 cross unions): the c1 form escapes the MONO failures because
those failures never touch the final union of a −1 call. Why (FM) holds when deficits occur is OPEN: a deficit vertex of
round r lying in Z_f would come from a Lemma-E straddle at round r whose tangle is attracted in the final round; its
cycle maximum m (a p-priority vertex, GAP-A-M Lemma E (b)) would then attract into Z_f through its tangle strategy and
could not be a candidate of the final round, so such an m must have been pruned between r and r_f — the step from there
is not done.
So Step 5 (P-KT, 18h) holds for every P piece in which no X-straddling tangle fires during Dom(prevV) (YZ-read) and whose
−1 call satisfies (FM); both hypotheses are absences of straddling-tangle effects (GAP-A-M Lemma E), the mechanism that
also underlies (α) and GAP-A's deficits.

### 18i. The T step: statement, DATA, and the induction it needs (07:30Z by date -u)
A depth-0 T piece (−1, Q nonempty; 898-955): seeds = the vertices of the lowest level t that attract into X; Z_T := the
threshold-t tangle attractor of the seeds within R; Θ := Z_T ∩ pr^{-1}(t) and B := the opponent's attractor to Θ inside
Z_T go to X; the rest Z' := Z_T \ B is searched by search_rec(Z', p, 1); all of Z_T joins X.
(T-STEP) If KT(R) holds, nothing was learned inside D earlier in the search, and KT(R \ Z_T) fails, then the recursion
search_rec(Z', p, 1) learns a tangle inside D.
DATA (dtl_step5stats.py "T-STEP", searches with D ≠ ∅, no dominion, nothing learned inside D before the piece; c = least KT
level of R):
| | corpus Oink | corpus stable | unions Oink s1 | cross Oink s11 |
|---|---|---|---|---|
| c < t, core avoids Z_T (KT kept) | 804 | 787 | 1,846 | 315 |
| c < t, core meets Z_T, KT kept | 131 | 120 | 126 | 10 |
| c < t, core meets Z_T, KT fails, recursion learns inside D | 12 | 12 | 18 | 3 |
| c > t (core always avoids Z_T, KT kept) | 38 | 38 | 13 | 2 |
| c = t | 0 | 0 | 0 | 0 |
| KT fails and the recursion is barren | 0 | 0 | 0 | 0 |
(CORE-PASS) DATA: whenever a T piece breaks KT, the recursion context Z' has a KT core of its own (KT evaluated on Z' with
X = ∅, D ∩ Z', the opponent's exits from Z' forgiven): 12/12, 12/12, 18/18, 3/3.
So (T-STEP) splits into (CORE-PASS) and the depth-1 analogue of (K-in) (REC): "a search_rec call at depth ≥ 1 whose context
holds a KT core learns inside D". (REC) needs the whole frame at depth d ≥ 1: a P step, an S step and a T step inside the
call. Obstacle for the P step at depth ≥ 1: Lemma P-KT used a p-dominion W1 of H = G[R] inside D ∩ R that is CLOSED in H;
at depth 0 D ∩ R itself is a p-dominion of H (R is a p-trap of G'), at depth ≥ 1 it need not be (σ may leave the call's
context), and a KT core may have opponent exits to D-vertices above its level (forgiven by F_c, real in H). So (REC) needs
a core closed in G[R_d]; (CORE-PASS) would then have to pass such a closed core down. Not attempted further.

### 18j. The S step: DATA (07:41Z by date -u)
(S-STEP) If KT(R) holds at a depth-0 stable piece, nothing was learned inside D earlier in the search, and KT fails after
Dom(V*, R), then the piece's sptl passes learn a tangle inside D. DATA (dtl_step5stats.py "S-STEP"): 0 barren breaks in
every run (403 corpus Oink, 381 corpus stable, 467 unions Oink s1, 61 cross unions Oink s11 S pieces that break KT).
Where the learning sits (same runs): inside the least-level core U with its top in U: 227 / 218 / 333 / 46; inside D but not
inside U, V* meeting U: 161 / 148 / 84 / 11; inside D, V* AVOIDING U: 15 / 15 / 50 / 4. So the S step cannot be localized
to the least-level core (the K-first / FIRST-W lesson again): a stable piece whose tops all lie outside U can swallow U and
learn elsewhere in D. A proof needs another selection (e.g. the least level whose core meets V*'s regions); not attempted.
(FM+) A sharper reduction of (FM) (07:44Z by date -u). For a top τ ∈ V_f let A^r(τ) := the union of the round-r regions
of the tops with index ≥ index(τ) (those computed no later than τ's turn in round r; τ ∈ V_r, so τ itself is in it).
Claim: Z^f_τ ⊆ A^r(τ) for every τ ∈ V_f and every round r — PROVED except in one case. Induction over round f's
computation (tops high to low, pushes in order). τ: in A^r(τ). (V, p-vertex) y → v with v earlier in Z^f_τ, hence
v ∈ A^r(τ), i.e. in a round-r region of a top σ with pr(σ) ≥ pr(τ) ≥ pr(y): at v's pop in round r, y is consumed already
(in A^r(τ)) or attracted. (V, opponent) every R-successor of y lies in Z^f_τ or in an earlier round-f region, hence (IH,
also for the earlier tops) in A^r(τ); at the round-r pop of the last of them, y is consumed already or attracted
(pr(y) ≤ pr(τ) ≤ the top's priority). (T) the tangle t that round f attracts at τ has no vertex in an earlier round-f
region (138-139 would reject it), all escapes in A^r(τ) or outside R; at the round-r pop of its last escape (region of σ,
pr(σ) ≥ pr(τ)) attractTangle accepts t unless some vertex of t lies in an EARLIER ROUND-r REGION — the Lemma E (a)
straddle at round r. That case is the only gap: (FM) fails only if round r straddles a tangle that round f attracts.
And then (−1 condition): the maximum m of any p-won cycle of t lies in t ⊆ Z_f and attracts into Z_f (p-owned: by its
tangle strategy; opponent-owned: all its R-edges are in t or escapes), so m ∉ V_f: m was pruned between r and f.
(S-LOC) and (S-LEVEL) (08:00Z by date -u). (S-LOC), DATA: when a stable piece breaks KT (nothing learned inside D before),
its learned tangle lies inside the core of SOME KT level c of R, that core meets V*, and KT fails at that level after the
piece: 403/403 corpus Oink (227 at the least level, 176 only at a higher level), 381/381 stable, 467/467 unions Oink s1,
61/61 cross unions. (S-LEVEL) "every level-c core that the piece destroys and that meets V* gets a tangle inside it" is
KILLED: 524 violations corpus Oink (478 stable, 207 unions, 36 cross); first instance
experiments/alg/instances/cross_h_k1_n12_m18_17.pg (both orders). So the S step is existential over the levels, like
(K-low) over the pieces; no rule naming the level is known.
(FM, the open case; SKETCH, 08:04Z by date -u.) Let r be the LAST round with Z_f ⊄ Z^r, so Z_f ⊆ Z^{r'} for every r' > r, and let
t be a tangle that round f attracts (t ⊆ Z_f, its escapes in Z_f or outside R) and round r straddles. Every p-priority
vertex m of t attracts into Z_f (p-owned: its tangle successor is in t; opponent-owned: all its R-edges go to t or to
escapes), hence into Z^{r'} for every r' > r; so m is no candidate at any round after r, and m ∉ V_f: every p-priority
vertex of t was pruned at round r or earlier (PROVED). In particular t holds no top of rounds r+1..f, and the straddle at
round r is created by the regions of round r's extra tops (pruned at r) or of tops above them; a top π pruned at r whose
region holds a vertex of t has no edge into Z^r (a candidate), so if π ∈ t its tangle successor lies outside Z^r. The
contradiction (or an FM counterexample built from it) is not reached; L-RED has the target.
(CORE-PASS-closed), DATA (08:13Z by date -u): whenever a T piece breaks KT (nothing learned before), the recursion context Z'
holds a nonempty p-dominion of G[Z'] (closed: every opponent vertex keeps all its Z'-edges inside it) lying inside D:
12/12 corpus Oink, 12/12 stable, 18/18 unions, 3/3 cross. With such a W the proof of P-KT runs unchanged inside the
recursion (a P piece of search_rec(Z', p, 1) has its context R_1 a p-trap of G[Z'], so W ∩ R_1 is a p-dominion of
G[R_1]), which removes the depth-1 obstacle above for P pieces; the S and T steps inside the recursion remain.
(NT-f) and the equivalence (FM) ⇔ (NT-f) (08:28Z by date -u; experiments/alg/dtl_ntf.py).
(NT-f) The final round of a −1 call attracts no stored tangle in its region loop. DATA: 8,047/8,047 −1 calls corpus Oink
(+ climbed games), 7,892/7,892 stable, although an earlier round attracts a tangle in 3,117 / 3,060 of those calls.
(FM) ⇒ (NT-f): if round f accepts t, every p-priority vertex of t attracts into Z_f (tangle strategy / all R-edges into t
or escapes), so none is in V_f; at the last round r* at which one of them, m*, is in V, m* is a candidate, so t ⊄ Z^{r*}
while t ⊆ Z_f: (FM) fails at r*. (NT-f) ⇒ (FM): the only failing case of the (FM+) induction is a tangle that round f
accepts. So (FM) ⇔ (NT-f) (PROVED), and Step 5 rests on one clean statement about the last pruning round plus (YZ).
A counterexample to (NT-f) must have: a stored p-tangle t with an escape in R, accepted at round f at the pop of its last
escape inside the region of a final top τ (pr(t) ≤ pr(τ), no vertex of t in an earlier round-f region); every p-priority
vertex of t pruned before round f; at the last round r* holding one of them, t rejected by the straddle test 138-139 (a
vertex of t consumed by an earlier region of round r*), its escapes already attracted. Climbs from c_best_s34.pg and
dtl_deficit_n20.pg (experiments/alg/dtl_fmclimb.py, 4 runs × 4,000 steps, both orders) raised the latest round at which a
deficit vertex reappears to f−1 of f but never to f.
(YZ-read) exception observed: experiments/alg/instances/strfam_S5_n46.pg, stable order — Dom(prevV) fires the stored
tangle {14, 15, 16, 17} with a vertex in old X or in an earlier top's part; Y_0 = Z_f still holds there (the region loop
reaches the same set by other rules), and P-KT holds (25/25 depth-0 P pieces). So (YZ) is not implied by the reading;
it held on all data.

### 18k. (NT-f) PROVED, hence (FM) and (WM) PROVED; Step 5 rests on (YZ) alone (08:43Z by date -u)
Lemma NT-f (PROVED, reading). In the final round f of a best_vertices call that returns −1, the region loop (690-708)
accepts no stored tangle.
Proof. Suppose it does, and let t be the FIRST tangle accepted in round f, in the region of a top τ ∈ V_f, at the pop of
an escape e ∈ R (attractTangles is called only from popped escapes, 198-202).
(A) Every vertex x added in round f before t's acceptance lies in A^r(τ_x) ⊆ Z^r for every round r, where τ_x is the
round-f top of x's region and A^r(σ) := the union of the round-r regions of the tops with index ≥ index(σ). Induction
over round f's additions, all made by attractVertices (t is the first tangle): the top τ_x ∈ V_f ⊆ V_r is in A^r(τ_x)
(consumed earlier or given its own region); a p-vertex x added at the pop of v → x: at v's round-r pop (v ∈ A^r(τ_x) by
induction, in a region whose top has priority ≥ pr(τ_x) ≥ pr(x)) x is already in a region or is attracted (65-101); an
opponent vertex x has all its R-edges into vertices added before it (the escape test 76-86 with Gx = CurR), all in
A^r(τ_x) by induction; at the round-r pop of the last of them x is already taken or attracted.
(B) Hence every escape of t in R is in Z^r for every r: at the acceptance each escape in R is in CurZ or already consumed
in round f (150-157: an escape in CurR \ CurZ rejects t).
(C) No p-priority vertex of t is in V_f: after the acceptance t ⊆ Z_f; a p-owned v ∈ t has its tangle successor in t, an
opponent-owned v ∈ t has all its R-edges in t ∪ escapes (the escape set holds every edge of an opponent vertex of t that
leaves t, 325-339) and one edge into t; either way attracts(p, v, Z_f, R) holds (40-57) and v is no candidate, contradicting
the −1 result (every vertex of V_f is a candidate).
(D) Let q := tpr(t), the maximal priority in t (the priority of the top that learned t, p's parity), M_q := t ∩ pr^{-1}(q),
and m_1 ∈ M_q a vertex pruned FIRST, at round r_1 < f (by (C) every vertex of M_q leaves V before f). At round r_1 all of
M_q is in V_{r_1} ⊆ Z^{r_1}. If q = 0, all of t has priority 0 = p-priority, so t ⊆ V_{r_1} ⊆ Z^{r_1}, and by (B) and the
argument of (C) m_1 attracts into Z^{r_1}: not a candidate, contradiction. If q ≥ 1, run the rescue loop of round r_1
(722-740) to level q−1.
(D1) [Lead 08:50Z] Why e is popped at level q−1 with a set containing Z^{r_1}: the rescue loop works on the SAME bitset Z
that the region loop leaves at 703-705, i.e. Z = Z^{r_1} when the loop starts at 722; attractVertices and attractTangles
only add members; at the start of every level t, line 724 pushes every member of Z, and 727-730 pop each pushed vertex and
call attractTangles(player, u, R, Z, R, t). So at level q−1 the set contains Z^{r_1} ∋ e (by (B)), e is pushed at 724,
popped at 728, and attractTangle(t, ...) is evaluated at 730 (t ∈ tin[e], 200-201) with Z ⊇ Z^{r_1}.
(D2) At that evaluation: the set contains M_q and every escape of t in R; at the level-(q−1) pop of e
attractTangle(t) (110-185) finds t alive, every vertex in Z or in R with priority ≤ q−1 (the priority-q ones are in Z), and
no escape in R \ Z. Either some vertex of t is new and t joins the set, or t ⊆ Z already and attractTangle returns false
(the "nothing new" exit, 146) — in both cases t ⊆ Z after this pop [wording fixed 08:56Z by date -u, Lead 09:00Z after L-RED R28]; then the
candidate test at level q−1 (pr(m_1) = q > q−1, candidates in descending
priority) finds m_1 attracting into it (tangle successor, or all R-edges in t ∪ escapes): m_1 is rescued at round r_1,
contradiction. □
Corollary FM (PROVED). In a −1 call Z_f ⊆ Z^r for every round r: by NT-f every addition of round f is a vertex-rule
addition, and (A) applies to all of them. Corollary (WM) (PROVED): Z_f ⊆ Z^r ⊆ A^r_t for all r, t.
Corollary (YZ-read sharpened, PROVED). Dom(prevV, R) and the final round's region loop are step-for-step equal until Dom
accepts a tangle with a vertex in old X or in an earlier top's part (18h); before that point any acceptance in Dom would be
an acceptance in the region loop, excluded by NT-f. So Dom accepts no tangle at all unless that first acceptance is such a
straddling one, and (YZ) holds whenever Dom accepts no tangle. Observed once (strfam_S5_n46.pg, stable order; the
tangle {14, 15, 16, 17} uses a vertex of OLD X), with Y_0 = Z_f nevertheless.
Status of Step 5: Lemma P-KT (18h) is PROVED given (YZ) only. (YZ) can fail only through a tangle that Dom(prevV)
accepts using a vertex of old X or of an earlier top's part, at a moment when the region loop rejects it.
Unrefereed; Lemma NT-f is a reading of dtl.cpp @ 8fbf0a7 for every order datum (no step uses ω).
(YZ) anatomy (08:51Z by date -u; experiments/alg/dtl_yzclimb.py climbs from strfam_S5_n46.pg, 3 stable + 1 Oink seeds, up
to 3 X-straddling Dom firings per run, never Y_0 ⊋ Z_f). In every observed firing the tangle lies in OLD X except for one
or two new vertices (e.g. {14, 17} with 17 ∈ old X, 14 new; {14, 15, 16, 17} with 16 new), each OPPONENT-owned, whose
tangle edges into old X lie outside R and are ignored by the region loop's vertex rule (76-86), so the region loop takes
them as vertices and Y_0 = Z_f. Reading towards a proof (SKETCH): a new p-vertex v of such a tangle t_X has its tangle
successor in R (an edge into X would make v attract into X, contradicting Q empty at a P piece); so a (YZ) failure needs
the new part of t_X to contain a cycle of H_{t_X} that the region loop's vertex rules cannot enter; its maximum m is a
p-priority vertex, and if m ∈ V_f it is a final candidate, so the cycle is not inside Z_f — consistent only with
Y_0 ⊋ Z_f. Not closed.
(YZ) ⇐ (ACYC) (08:52Z by date -u; reading, PROVED). Let Dom(prevV, R) accept, in the region of its top τ_j, a stored tangle
t_X that uses a vertex of old X or of an earlier top's part, with new vertices N_X (in R, priority ≤ pr(τ_j)); by NT-f and
18h this is the only way Dom and the final round's region loop can differ. (i) A p-vertex v ∈ N_X has its tangle successor
in the current region or in N_X: not in old X (an edge into X would make v attract into X; Q is empty), not in an earlier
region (v would have been attracted there at that vertex's pop, the earlier top having priority ≥ pr(τ_j) ≥ pr(v); then v
would not be new). (ii) An opponent vertex of N_X has all its R-edges into the current region, earlier regions or N_X; its
edges into old X are outside R and ignored by 76-86. (iii) Hence, if N_X contains no cycle of H_{t_X} (ACYC), the region
loop attracts all of N_X by vertex rules into τ_j's region (reverse topological order of H_{t_X} on N_X), and since each
region is the least fixed point of its rules (GAP-A-M §1, Lemma 1.2) Dom's region and the loop's region coincide; repeated
for every such acceptance, Y_0 = Z_f. So Step 5 rests on (ACYC): "the new part of every X-straddling tangle that
Dom(prevV) accepts is acyclic in the tangle graph". DATA: every observed firing has 1-2 new opponent vertices (acyclic).
A (ACYC) failure needs a p-won cycle C of t_X entirely in R and new; if its maximum m_C is in V_f it is a final candidate,
so C ⊄ Z_f and (YZ) fails; whether P-KT survives such a piece is open. L-RED target.

### 18l. The S step as (S-LOW): the lowest region of the first KT-breaking stable piece learns (DATA; 09:16Z by date -u)
(S-LOW) At a depth-0 stable piece that breaks KT, with nothing learned inside D earlier in the search, the LOWEST top that
gets a region in the piece's FIRST sptl pass learns a new tangle (or finds a dominion). DATA (dtl_step5stats.py
"S-LOW"): 403/403 corpus Oink (incl. kfirst_viol_n13, pk_viol_n20), 384/384 corpus stable, 467/467 unions Oink s1,
61/61 cross unions Oink s11. Also (S-W*): at every such piece a p-dominion of G[R] inside D exists (W*, least maximum),
V* and the removed set meet it, and the learned tangle lies inside it in 394/403, 374/384, 467/467, 61/61.
Reduction (PROVED): K6 (DTL-proof.md §2.3: for any stable V* and any X, the lowest region of a pass is closed unless (α),
and a closed one yields a new tangle, a dominion or a (β') duplicate whose escapes all lie in X) turns (S-LOW) into
"neither (α) nor (β') occurs at the lowest region of the first KT-breaking stable piece". With KT0, P-KT and the T split
(18i), Lemma K (search(p) returns true when W_p(G') ≠ ∅) would follow from: (ACYC); (S-LOW) at every depth; (CORE-PASS-
closed) and the same frame inside recursions. Caveat: a KT core can contain an orphan (a stored tangle in R with every
escape in X: not plainly attracted to X, p-won with exits forgiven), so KT itself does not exclude (β'); a tangle-aware
attractor in KT would, and the NT-f trick (take the tangle's top-priority vertex pruned first) seems to carry P-KT over to
it for tangles without a vertex in old X — SKETCH, not written.
