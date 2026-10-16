# GAP-A data: what bounds the number of tangles (L-ALG, box 2026-10-16 00:00Z–07:40Z)
Subject: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7 (DTL-proof.md §0). Everything here is measurement
or reading; nothing is a result. Status words: PROVED / SKETCH / GAP / DATA / DEAD. Scripts in experiments/alg/ (pinned command,
release build reads tangles from `-t -t`; the Debug build and a PATCHED Debug build, recipes in notes/L-ALG.md, read pieces).

## 1. Tools (all new this box)
| script | reads | reports |
| --- | --- | --- |
| dtl_tangle_family.py OINK G.pg [--sets] | release `-t -t` | tangle sets; laminarity (nested / crossing / disjoint pairs); per-top counts; (C-new) violations split into restart violations and in-search chain breaks; strict shrinks |
| dtl_heads.py G.pg TRACE | PATCHED debug trace | per-vertex removal head per search ('dom' top / 'cut' level / 'dis' top) and its transitions across same-player searches; depth-0 piece sequence per search; first stable piece's R and V* vs the previous search |
| dtl_distance.py G.pg TRACE | any `-t` trace | pruning distance of every vertex at the FIRST best_vertices call of each search; monotonicity across same-player searches |
| dtl_crossclimb.py OINK OUT n seed steps [--cnew / --pertop / --restart / --searches] [--seedgame G] | release | hill-climb on random games (n vertices, priorities ≤ n, out-degree 1–3, 1–3 mutations per step) for crossing tangles at one top / (C-new) violations / tangles at one top / restart violations / searches |
Instances kept (experiments/alg/instances/): dtl_cross3_n14.pg, dtl_pertop31_n18.pg, dtl_pertop28_n24.pg, dtl_cnew14_n20.pg,
dtl_restart7_n16.pg, dtl_restart8_n20.pg. All solved by A_DTL with verified strategies (`oink -v`).
PATCHED build: copy tools/oink/src to a scratch dir; in dtl.cpp search_rec add `ENTER depth d` after the bitset declarations,
`EXIT depth d` before the `result == 0` return, and in the stable branch's Dom(V,R) loop (876-889, untraced in Oink) print
`X ∪= DomStable(V)` once and, per top, `domregion <pr> <top> <vertices newly added to X>`; build Debug as in notes item 6.

## 2. What tc+ does (DATA, complete picture; tc+ N = 4, 6, 8, 10)
- Every tangle is learned at depth 0, in the ONE stable piece of each search; the −1 pieces and the recursion learn nothing.
- Search 0 of a phase: pruning removes two distraction sets, then the −1 cut at the opponent's top level removes the opponent's
  half (recursion on it learns nothing), then the stable piece on the player's half learns the gadget tangles (one per
  gadget, priority 4) and the top's tangle (containing them all, 2N−1 first-piece tangles in the predecessor's count).
- Search s ≥ 1: the pieces are dis(gadget_N), dis(gadget_{N−1}), ..., dis(gadget_{k}), STABLE, dis(1), cut(opponent half): the
  number k of distraction pieces before the stable piece drops by ONE per search; the stable piece's R grows (+3, +4, +5, ...
  vertices, SUPERSET every time from search 1 on) and its V* exchanges the rescued gadget's chain tops for the next gadget's
  (+k, −k(k−1)/2: triangular). The rescued gadget's chain (priorities 4, 6, 8, ...) learns one tangle per level (N−1 of them)
  and the top's tangle grows by the gadget (a chain at the top: 84 ⊂ 87 ⊂ 91 ⊂ 96 ⊂ 102 at N = 6, escapes 25, 22, 18, 13, 7).
  Search 0's top tangle crosses the chain (it was computed after the cut, with the opponent's half forgiven; 16 of its vertices
  fall into the cut from search 1 on: head 'dom' → 'cut' DOWN, the predecessor's "later pieces are re-cut").
- So tangles(tc+ N) ≈ N (gadgets) × N (chain) + 2N (top) and searches = 2N + 2: the quadratic count in N is sublinear in n ≈ 17N².

## 3. Findings (DATA unless marked)
F1 (DEAD) Laminarity. The family of stored tangle sets is far from laminar: tc+ N = 6: 166 nested, 205 crossing, 1,282 disjoint
   pairs. So |T| ≤ 2n by laminarity is out.
F2 (DEAD) "≤ n tangles per top". dtl_pertop31_n18.pg: n = 18, one top learns 31 tangles (44 tangles, 6 searches, 1 dominion).
   Also 23 at n = 20, 28 at n = 24, 24 at n = 30 (climbs --pertop, 100k steps).
F3 (DATA, 0 exceptions) In-search chain. Within ONE search, the tangles learned at one top form a strictly growing chain
   (each later one a strict superset of the previous). Checked on tc+, 13 families, L-RED's chain/ladder/counter_dftl, 3 random
   batches, and every climbed instance including the ones optimised against it (fitness --restart's second component counts
   chain breaks: 0 in 12 climbs of 3k–30k steps). Mechanism (dtl_pertop31_n18, top v17 with 8 equal-priority tops): the region
   set is fixed, the fresh tangle fires in the next sptl pass and brings its stored strategies, the DFS parents of the other
   vertices change, and the SCC of the top grows by ≥ 1 vertex per pass (escapes 13, 12, 10, 9, 8, 7, 5, 4). This is the
   predecessor's (a4) "str change at a fixed region set", observed as a chain of length 8 at n = 18.
   Consequence (if F3 is PROVED): ≤ n tangles per top per search, so |T| ≤ n · Σ_τ (searches in which τ learns) ≤ n² · searches.
F4 (DEAD) (C-new): "every new tangle at a top contains a vertex that no earlier tangle at that top contains" (would give ≤ n per
   top). FALSE: 20 violations in dtl_pertop31_n18 (the chain restarts each search from a base inside the previous chain's union),
   and even the RESTART (first tangle of a top in a search) can be covered: dtl_restart8_n20 (11 restart violations, 1 strict
   shrink), dtl_restart7_n16 (9, all caused by a dominion: the search-2 tangles are the search-1 tangles minus the solved
   vertex; the deletion charge of DTL-proof.md §3(a) covers these).
F5 (DATA, 0 exceptions) First-call distance monotone. At the first best_vertices call of a search (R = G', the same across
   same-player searches without a dominion) the pruning round in which a vertex is pruned never decreases as T grows (tc+ N = 6:
   105 increases, 0 decreases over 12 pairs). But it is NOT a potential: on tc+ N = 6 searches 1–5 have identical distance
   profiles while each learns new tangles (the progress is in the later pieces).
F6 (DEAD) Per-vertex heads monotone across searches; first stable piece's R monotone. Heads move DOWN on tc+ ('dom' → 'cut',
   16 vertices at N = 4, 50 at N = 6, 112 at N = 8; 'dom' → 'dis' 6/10/14). R of the first stable piece is CROSS (+1 −58) on
   counter_symsi 12 between searches 0 and 1 (search 0's first stable piece is a 1-top piece after a 2-vertex cut; in search 1
   the cut at that place takes 56 vertices because the −1 set shrank from 11 tops to 1).
F7 (DATA) The −1 return set is not monotone even though distances are: tc+ N = 4 search 0 returns {v60, v28, v6} (the last
   survivors, round 8); search 1 returns {v3, v4, v5, v6, v14} (survive longer with more tangles) while v60, v28 are pruned
   before the end. So the first distraction piece, hence every later context, is re-cut.
F8 (DATA; the counter-shape candidate) Oscillation of a vertex's membership in a top's SCC across searches with NO dominion in
   between: dtl_restart8_n20, top v6 (pr 14): v13 ∈ SCC in search 0, ∉ in search 1, ∈ in searches 2–4; v16 likewise (out in
   1–2, back in 3). Mechanism from the patched trace: search 0's first −1 set is {v9, v4, v19} and the two cuts after it remove
   2 + 2 vertices; search 0's tangles rescue v9 and v19, so search 1's first −1 set is {v4}, X is smaller, the lowest level that
   attracts to X changes, the cut removes 1 vertex, fewer exits are forgiven in the stable piece, and v13, v16 become
   DISTRACTIONS (removed before the stable piece). In search 2 the new tangle at v6 (now containing v9) rescues v13; in search
   3 v16. RULE (reading): rescue(A) ⇒ A's attractor is no longer removed before the stable piece ⇒ fewer forgiven exits ⇒
   some B can regress to a distraction; regress(B) ⇒ B's attractor is removed earlier ⇒ more forgiven ⇒ some A' can be rescued.
   A flip-flop is possible in principle; it ends unless each configuration produces NEW tangle sets (duplicate check), i.e. it
   must be driven by a lower counter (TL's tc idea applied to distraction status instead of region membership).

## 4. Reduction of GAP-A (reading of the data; nothing proved)
tangles = Σ_τ Σ_searches (chain length of τ in that search) ≤ n · #(τ, search) pairs with a restart.
- (F3 to PROVE) chain length ≤ n: needs "within one search at one top the SCC only grows": within a piece the region set is
  fixed except for thefts by higher tops (a3) and fresh tangles only add str; the open point is the str change (a4).
- Restarts: a top restarts in a search iff its SCC differs from every stored set. Across searches the context of the piece is
  re-cut (F6, F7, F8), so Lemma D (2n+1 sets per top under R-mono) does not apply; the oscillation F8 shows membership is not
  monotone. So GAP-A ⇔ polynomially many searches per phase (each search without a dominion restarts ≥ 1 top).
- Searches per phase: tc+ 2N+2; climbs for searches (fitness --searches, n = 24, 32) reach 7–8 after 1k steps; the oscillation
  instance has 5. No family with superlinear searches is known (L-LIT T16; L-RED R8).

## 5. Dead ends this box (with the instance)
| conjecture | killed by |
| --- | --- |
| tangle sets laminar | tc+ N = 4 (67 crossing pairs) |
| ≤ n tangles per top | dtl_pertop31_n18.pg |
| (C-new) new vertex per tangle at a top | dtl_pertop31_n18.pg (20), dtl_restart8_n20.pg (restarts) |
| heads non-decreasing across searches | tc+ N = 4 ('dom' 28 → 'cut' 27, 16 vertices) |
| first stable piece's R non-decreasing | counter_symsi 12 (search 0 → 1: +1 −58) |
| −1 return set monotone in T | tc+ N = 4 search 0 → 1 |
| first-call distance profile as a potential | tc+ N = 6: constant over searches 1–5 |
