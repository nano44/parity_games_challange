# R42: (XCTX@p0) and (CHAIN-CHANGE) on 𝒞^1P (L-RED box 14; produced on Opus 5.5)
Status: TWO KILLS ((XCTX@p0) §1, (VR-NEW_all) §5; DATA, both orders, L-ALG's unmodified checkers) plus one READING (Lemma EMPTY-REC), unrefereed.
Target: Lead box-14 item 1. The statements are attacked as written in L-ALG docs/alg/GAP-A-M.md §33a/§35a at l-alg 9ab9a3e6.
Started 2026-10-18 21:11Z (date -u). Pinned Oink @ 8fbf0a7 verifies every instance. L-ALG tools are used unmodified: b12_pot.py,
b12_core.py, fixd_oneplayer.py, fixd_ctx1p.py and b12_topchain.classgames, from the in-tree experiments/alg copies (the kill is
also reproduced with the l-alg 9ab9a3e6 copies). Tools: experiments/red/xctx/.

## 1. (XCTX@p0) is FALSE on 𝒞^1P (both order data)
Statement (GAP-A-M §35a, quoted). Setting: G ∈ 𝒞_C^dist, one phase of q = 1 − C, depth-0 chain c(s) = (state_0, …), state_p =
(R_p, ρ_p, V_p, piece_p), σ_s(p) = (ρ_p, |R_p|, |V_p|). At s → s+1 with c(s) ≠ c(s+1), p0 is the first changed position and R :=
R_{p0}(s) = R_{p0}(s+1). N := piece_{p0}(s+1) in case O (the outcome changed); otherwise N := piece_{p0}(s+1) \ piece_{p0}(s) (case P).
> (XCTX@p0): N ⊄ ⋃ { piece_{p0}(s′) : s′ ≤ s, R_{p0}(s′) ≠ R, |R_{p0}(s′)| = |R|, σ_{s′}(p0) = σ_{s+1}(p0) }.

Instance: experiments/red/xctx/instances/xctx_viol_n20.pg, sha1 742ba103cdb77cbb20e8d94e99120331568e84cd.
- Class membership. C = 1: every Even vertex (0, 4, 12, 14, 17, 18) has exactly one successor (fixd_oneplayer.inclass(g, 1) is
  True). The 20 priorities are pairwise distinct. b12_topchain.classgames(DIST=1) takes the file as in-class, with no forcing suffix.
- Pinned Oink `--dtl --no-single --no-wcwc --no-loops -v`: 6 iterations (even 5, odd 1), 1 dominion, 7 tangles, solution verified.
  The model's Even phase also has 5 searches.
- L-ALG's checker, unmodified, `CLASS=1 DIST=1`, stable and oink:
  - `MODE=xcover`: "covered cross-context 2", max covered fraction 1.0 at ((0,0), s 2, p0 2).
  - `MODE=core`: "CORE-ALL violations 1", first at ((0,0), 2, 2).
  - b12_core.xcover() called directly: at transition ((0,0), 2, 2), |piece_{s3}(2)| = 16, and the cross-context-covered set
    {1,…,10,12,15} contains N.
- The violating transition. Even phase (q = 0), s2 → s3, p0 = 2, case P.

| search | pos 0 piece | pos 1 piece | pos 2: context, (ρ, |R|, |V|), piece |
| --- | --- | --- | --- |
| s0 | {13,19} | {18} | G′∖{13,18,19}, (3, 17, 4), {1,…,10,12,15} |
| s2 | {19} | {11,13} | G′∖{11,13,19}, (3, 17, 4), {0,…,10,15,16,17,18} |
| s3 | {19} | {11,13} | G′∖{11,13,19}, (3, 17, 4), {0,…,10,12,15,16,17,18} |

  N = {12}. At s0 the context at position 2 is a different set of the same size (18 present at s2, 11 present at s0). It has the same
  signature, and its piece contains 12. So N lies inside the union.
- What survives on the instance: (VR-NEW_all). `b12_pot.py CLASS=1 DIST=1`, K-v-all: 0 violations in both orders. The new full
  key of s3 is below p0: vertex 14, at position 3, (14, 22, 3, 1, 1).
- Consequence (reading). The 𝒞^1P reduction "GAP-A ⇐ (XCTX@p0) ∧ (CHAIN-CHANGE)" (GAP-A-M §33c) is dead as stated. A replacement
  must put the novelty below p0, or must use more than the first changed position. Here N is covered, yet the transition still gets a
  new key, at position 3.
- How it was found. experiments/red/xctx/xscore.py, a class-preserving climb (fixd_oneplayer.mutate; distinct() after every move).
  - The score is graded: (violations, covered fraction of N, Σ cover, #same-signature different-context pairs, overlap with
    same-size pairs of any signature, #same-size different-context pairs, transitions).
  - The last two levels give the gradient that a raw cross-cover count lacks (L-ALG §35c: 0 everywhere).
  - Path: onep_fdkey_n20 (f1 = 3, ov1 = 14 at start); then xcov11_n20 after 4,776 steps (Oink order); then the kill after 3,457 more
    steps (stable order, seed 14). The first violation was saved at step 3,457, and further violating games at steps 7,036, 7,624,
    7,919 and 8,169; the pinned file is the step-3,457 one.
- Near miss on the way: xcov11_n20.pg (sha1 47023109c198db4315fb3e2044c4a9bc95e7070b; C = 1; pinned Oink 8 iterations, 7 Even,
  verified).
  - 11 of the 16 vertices of N are covered cross-context (Even phase, s5 → s6, p0 = 2); the uncovered ones are {0, 3, 15, 16, 17}.
  - Correction to my 21:22Z message to the Lead: there I listed 12 as uncovered, but 12 is covered.

## 2. Lemma EMPTY-REC (PROVED, reading; mechanical check)
Statement. Let every vertex of player q have exactly one successor (class 𝒞_C, q = 1 − C; distinct priorities are NOT needed). Then in
every search(q) of A_DTL, every recursive call search_rec(Z, q, depth+1) (dtl.cpp 954) has Z = ∅.
Proof (dtl.cpp @ 8fbf0a7, lines 898-955).
- (a) Every seed has priority exactly t. The loop 899-911 walks the vertices in priority order and raises t to priority(v) only while Q
  is empty. Once Q is nonempty it breaks at the first higher priority.
- (b) Every vertex of the threshold region Z reaches a seed inside Z. This uses only edges a q-vertex's unique edge or a C-edge, and
  goes by induction on attraction order (916-921).
  - A vertex added by attractVertices(player, u, …) is a predecessor of the popped u ∈ Z: a q-vertex through its unique edge, a
    C-vertex through its edge to u.
  - A tangle added by attractTangles(player, u, …) has u as an escape, so some C-vertex of the tangle has an edge to u. Every vertex
    of the tangle reaches that C-vertex inside the tangle. The tangle is an SCC under its strategy, and a q-vertex's strategy is its
    unique edge.
- (c) Every vertex of Z with priority t goes to X and onto Q (935-940). Then 942-946 run attractVertices(1−player, u, Z, X, Z, t).
  This attracts every C-predecessor of a removed vertex. It also attracts every q-predecessor whose successors in Z all lie in X; a
  q-vertex has one successor, so this happens exactly when that successor was removed. The cap t is no restriction: every vertex of
  Z has priority ≤ t.
- (d) Hence the removed set is the backward closure of the seeds in Z. By (b) that closure is all of Z, so Z is empty at 954.
  search_rec(∅) returns at once: best_vertices finds no q-vertex and returns 0. □
Mechanical check. experiments/red/xctx/dagchk.py on L-ALG's class set (b12_topchain.classgames, TRIALS=3 SEED=2, the onep_* files):
98 of 98 depth-≥1 search_rec calls of q-phases have an empty subgame. On the class set (deepclass.py: 998 games, 1,046 q-transitions)
the number of tangle births at depth ≥ 1 in q-phases is 0. The wrapper does see a depth-1 birth on the two-player deep1_n13 (R40).
Consequences (reading).
- On 𝒞_C, every tangle of a q-search is born in sptl at a depth-0 stable context. So (DEEP-STAB), (TREE-PIECE) and (TREE-PIECE⁺)
  restricted to 𝒞^1P are depth-0 statements, which matches L-ALG's §34b remark that the depth-0 chain always changes there.
- The −1 branch of a q-search on 𝒞_C is "remove the threshold attractor" with no recursion. L-ALG's "depth-0 only" hypotheses on the
  class hold for free.

## 3. (CHAIN-CHANGE) on 𝒞^1P: no kill; where a violation must live
Statement (GAP-A-M §33a, quoted): "(CHAIN-CHANGE) 'every transition of a q-phase changes the depth-0 states'".
Data:
- Class set: 0 identical-chain transitions in 1,046 q-transitions.
- 2,000 random class games: 0, but these have only 22 transitions.
- deeprand.py, 22:25-22:27Z (date -u). 300,000 games with n 4-10 per order (stable seed 101, oink seed 102), plus 100,000 with
  n 10-18 (stable, seed 103): 5,566 q-transitions, 0 identical-chain transitions, 0 tangle births at depth ≥ 1 in ANY phase.
- Climbs: chainchg.py (minimum chain distance) and chainfin.py (the transition into the last q-phase's final search), both orders,
  from onep_chainfail_n20, onep_topuniq_n20 and xcov11_n20. No violation; the best distance stays at about 2 positions.
Necessary conditions for a violation s → s+1 (reading; uses EMPTY-REC):
- (α) Search s learned something (otherwise the phase has ended). By EMPTY-REC that learning happened in sptl at a depth-0 stable
  position j.
  - If the tangle t learned at j is attractable at s+1 at some position i < j, then piece_i or the outcome at i changes. That is
    because t ⊆ R_j ⊆ R_i \ piece_i(s).
  - So t must be unattractable at every position i < j at s+1: every Dom cap and threshold cap there lies below a vertex of t, or an
    escape of t lies outside the attractor.
- (β) If s+1 itself learns, it does so in sptl at a depth-0 stable context (R_j, V*_j) equal to s's.
  - sptl repeats to a fixpoint inside s (search_rec, dtl.cpp 867-875), and the set W blocks only extraction, not region computation. So the
    new tangle must come from one of two sources.
  - Source (β1): a top that was in W during s's later passes. At s+1 it is re-extracted on a region that changed after it entered W.
  - Source (β2): a top whose region at s+1 attracts a tangle learned at s at a later position j′ > j.
  - In 𝒞_C the extraction graph is fixed: a q-vertex's strategy is its unique edge. The set reachable from a top can grow only
    through a vertex that a higher region consumed at s and released at s+1. The highest region is monotone in T, so this needs at
    least three tops with non-monotone consumption.
  - In case (β2) the tangle must also stay out of Dom(V*_j) at s+1. Otherwise piece_j changes.
- (γ) If s+1 learns nothing, it is the final search of the last q-phase, and then W_q(G′) = ∅ (completeness, GAP-C side).
  - Claim (SKETCH, reading; not checked line by line): if position 0 is stable, the union U of the round's regions is a q-dominion of G′, so W_q(G′) ≠ ∅.
    - U is Odd-closed (here Odd means the controller C). A C-vertex enters a region only if all of its successors lie in that
      region or in a region consumed earlier.
    - A q-vertex's unique successor lies in its region, and the top's successor lies in U by stability.
    - Inside a region, play moves down the attraction order, or stays inside a q-tangle that was attracted as a unit, whose
      cycles q wins. Between regions, C moves only to regions of higher tops; only tops jump elsewhere.
    - So every infinite play either ends inside one tangle block or visits tops infinitely often. In the second case its maximum
      priority is a top's priority, which has q's parity.
  - Hence case (γ) needs j ≥ 1, with t escaping into earlier pieces.
  - Such a violation would cost one search per phase, which is harmless for the count (#keys + 2). (β) is the only case that
    matters for a bound.
Status: (CHAIN-CHANGE) on 𝒞^1P survives every test made here. A violation needs (β1) or (β2) in the mid-phase case, or (γ) at the end.

## 5. (VR-NEW_all) is FALSE on 𝒞^1P (both order data), and (FD-WITNESS_all) with it
Statement (GAP-A-M §32-§33a, the b12_pot key K-v-all): every chain-changing transition of a q-phase gives some vertex a new full key
(v, ρ_j, j, |R_j|, |V_j|) that it held at no earlier search of the phase.
Instance: experiments/red/xctx/instances/vrall_viol_n20.pg, sha1 ed50585765541988d42aa4fa2b3d97c0b3bb8401.
- Class membership: n = 20, C = 1, `inclass(g, 1)` is True, and all priorities are distinct. classgames takes the file as in-class.
- Pinned Oink: 5 iterations (even 4, odd 1), 1 dominion, 6 tangles, solution verified. Zielonka solves it.
- L-ALG's unmodified `b12_pot.py CLASS=1 DIST=1`: "K-v-all violations 1" in BOTH orders, out of 3 transitions, 0 of them with an
  identical chain.
- `b12_fdwit.py CLASS=1 DIST=1`, both orders: no new-key vertex in the piece at j* nor at j* − 1, for each of K-v-rV, K-v-rs and
  K-v-all. So (FD-WITNESS_all) fails as well.
- `b12_core MODE=xcover`: cross-context cover fraction 1.0 at ((0,0), 2, 2).

The transition: Even phase, s2 → s3. Chains are (|R|, ρ, |V|, piece):

| search | pos 0 | pos 1 | pos 2 | pos 3 |
| --- | --- | --- | --- | --- |
| s0 | (20,4,4,{1,4,11,19}) | (16,3,2,{18}) | (15,3,3,{3,5,6,7,9,10,12,13,14,15}) | (5,2,2,{16}) … |
| s2 | (20,5,1,{19}) | (19,4,4,{0,1,4,11}) | (15,3,3, 13 vertices without 9, 10) | (2,22,1,{9,10}) |
| s3 | (20,5,1,{19}) | (19,4,4,{0,1,4,11}) | (15,3,3, the s2 piece ∪ {9,10}) | (0,0,0,∅) |

- At s3 the new keys of 9 and 10 are (9,3,2,15,3) and (10,3,2,15,3). Both were held at s0, at position 2 under the context
  G′∖{1,4,11,18,19}. That is a different set of the same size, with the same rank and |V|.
- Every other key of s3 was held at s2. Nothing new appears below p0: position 3 disappears.
Found by experiments/red/xctx/vrclimb.py (graded: margin, then #new keys, then key distance; class moves), stable order, seed 41,
2,110 steps from xctx_viol_n20 (margin 1, distance 2).
Consequence (reading):
- On 𝒞^1P, the depth-0 full-key pigeonhole (searches per q-phase ≤ #keys + 1) fails, and with EMPTY-REC so does the depth-0
  (TREE-PIECE⁺).
- What the instance shows is that the key must identify the CONTEXT SET, not only its size. With the set in the key, the count is
  (CTX⁺) again.

## 6. Files
- experiments/red/xctx/xscore.py: the graded (XCTX@p0) scorer and climb (GROW=p adds class-preserving vertex insertions).
- experiments/red/xctx/show.py: chains per q-phase.
- experiments/red/xctx/chainchg.py and chainfin.py: (CHAIN-CHANGE) climbs.
- experiments/red/xctx/deep.py, deeprand.py, deepclass.py and dagchk.py: depth-≥1 births and the EMPTY-REC check.
- experiments/red/xctx/vrclimb.py: the (VR-NEW_all) graded climb.
- experiments/red/xctx/instances/: xctx_viol_n20.pg (kill), xcov11_n20.pg (near miss), vrall_viol_n20.pg ((VR-NEW_all) kill, §5;
  pinned with b12_pot K-v-all = 1 in both orders). Both are pinned in experiments/red/check.sh
  (sha1, b12_core CORE-ALL = 1 and the xscore violation, both orders).
