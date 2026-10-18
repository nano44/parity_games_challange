# R45: a compounding counter on 𝒞^1P: what it must do, and where it stalls (L-RED box 14; produced on Opus 5.5)
Status: READING (necessary conditions, each step tied to dtl.cpp @ 8fbf0a7) plus DATA (climbs), unrefereed.
Written 2026-10-18 22:40Z (date -u). Target: the Lead's 22:30Z order (date -u): take (CTX⁺) directly, build k nested swap gadgets
with resets on 𝒞^1P, or write the exact obstruction. Result: NOT BUILT in this box. This file gives the conditions any such family
must meet, and the data.
Setting: G ∈ 𝒞_C^dist, one phase of q = 1 − C under one order datum, G′ fixed. Lemmas used: EMPTY-REC (R42 §2), LEX and SAME-CTX
(L-ALG GAP-A-M §33b, §35b; readings), CTRL and NOSTEAL-1P (§27b).

## 1. What a long phase is made of (reading)
- (T1) Every search of the phase except the last learns at least one NEW q-tangle and no dominion.
  - search(q) returns true only if the tangle or dominion count changed (dtl.cpp 1068).
  - A dominion ends the phase, because the phase key (q, #dominions) changes.
  - So S ≤ τ + 1, where τ is the number of distinct tangles learned in the phase.
- (T2) By EMPTY-REC, every such tangle is born in sptl at a depth-0 STABLE call.
  - It is an SCC of the FIXED graph H: each q-vertex keeps its unique edge, and each C-vertex keeps its edges inside the region.
  - The SCC is reachable from a closed top a, inside a's region. That region is computed in the context R_j with the regions of
    the higher tops consumed first (dtl.cpp 477-551).
- (T3) So a super-polynomial phase needs super-polynomially many distinct pairs (stable depth-0 context R_j, top a) whose
  closed regions extract new SCCs.
  - By SAME-CTX (iii) and R9 (c) (F_R = 0 on the class), each context contributes polynomially many transitions.
  - Hence a super-polynomial phase needs SUPER-POLYNOMIALLY MANY DISTINCT STABLE DEPTH-0 CONTEXTS in one phase. This is (CTX⁺),
    restricted to stable calls.

## 2. How new contexts arise, and the three conditions a counter must meet (reading)
LEX: the chains c(s) increase strictly in the tree-lexicographic order. A transition first changes position p0 at an unchanged
context R, where the state rises: the outcome rises, or (case G) the piece grows. Contexts at positions > p0 are then recomputed.
A binary counter over k levels needs nesting depth NEST ≥ k (R41 §1). That means:
- (N1) CARRY. A context R at level ℓ rises ≥ 2 times in a phase, with rises of levels > ℓ between consecutive rises.
  - A case-G rise at ℓ means piece_ℓ absorbs vertices of R_{ℓ+1}. The trigger is a tangle learned below ℓ, now attractable into
    piece_ℓ: the carry.
- (N2) RESET. After a carry at ℓ, the levels below must rise ≥ 2 times AGAIN, each time learning a new tangle (T1). Tangles are
  never deleted inside a phase, so the old lower-level tangles must stop being usable in the new context.
  - attractTangle (dtl.cpp 110-196) rejects a stored tangle t only in these cases:
    - (r1) a vertex of t has left G (only at dominion removal, so never inside a phase);
    - (r2) a vertex of t is outside the current subgame R (line 138: `!R[v]`);
    - (r3) a vertex of t has priority above the cap (line 140);
    - (r4) an escape of t lies in the subgame G and not in Z (line 156: `if (G[v]) return false`).
  - A smaller context can only REMOVE blocking escapes: an escape that leaves the subgame stops blocking under (r4). And (r3)
    does not depend on the context.
  - So a reset of level ℓ+1 needs, for every tangle used by a lower level before the carry, one of two things:
    - (N2a) a vertex of the tangle was absorbed into the higher piece, which is (r2);
    - (N2b) an escape of the tangle stays inside the new subgame but drops out of the region, which is (r4) with a changed region.
  - Without (N2a) or (N2b), the lower levels restart already "advanced", and the counter collapses to an additive one: the
    staircase behaviour of leanT and lagfam (R39, R40).
- (N3) REGROWTH. A shrinking context can host only polynomially many level-ℓ+1 epochs, because case-G carries shrink R_{ℓ+1}.
  To re-run a sub-counter many times at a level, R_{ℓ+1} must regain vertices. By LEX this happens only in two ways:
  - (N3a) an OUTCOME rise at ℓ whose new piece is smaller than the old one. There are polynomially many outcome rises per context.
  - (N3b) a re-cut at a level < ℓ that places a vertex back at a lower position. This is the XCTX swap of R42 §1/§5: in
    vrall_viol_n20, vertices 9 and 10 move between positions 2 and 3.
  - So a counter of depth k needs the swap mechanism (N3b) at each of about k levels, nested, together with (N2) at each level.
- The XCTX/VR-NEW instances of this box meet (N3b) ONCE, at a single position, and none of them meets (N1) and (N2) together.

## 3. DATA (this box)
- experiments/red/xctx/nestclass.py: a class climb on (NEST, CARRIES, longest q-phase, −n), with class-preserving moves and vertex
  insertions (GROW 0.05, NMAX 60). Runs: from onep_fdkey_n20 (NEST 2 at the start; stable and oink orders) and from xcov11_n20
  (stable).
  - NEST 3 is REACHED inside 𝒞^1P: experiments/red/xctx/instances/nest3_n20.pg, sha1 4ac8e1f4955b0c8fbafb5d2f137dabff0844b829.
    - C = 1, priorities distinct.
    - Pinned Oink: 12 iterations (11 Even), solution verified.
    - Even phase of 11 searches, the same in both orders. First-difference positions [0, 5, 5, 2, 3, 3, 2, 2, 0, 3].
  - By 22:46Z (date -u) the climbs plateau at NEST 3: phases of 11-14 searches at n 20-24 (about 0.6 n, linear).
- Anatomy of nest3_n20 (experiments/red/xctx/tlog.py, stable order):
  - The carries are case-G absorptions: the piece at position 5 grows from {5,10,16} to {5,10,11,14,16} over s1-s3.
  - The tangles of the last stable piece EXTEND rather than reset: [0,15,17] at s3, then [0,7,15,17] at s6.
  - Vertex 7 returns to the last context after the outcome rise at position 2 (s4: rank 3 to 5). That return is (N3b).
  - Each epoch therefore re-learns the old tangle plus a returned vertex. This is the additive "extend by one" pattern of leanT
    (R40) inside the class, nested 3 deep, and it is bounded by the number of returnable vertices.
- Corpus NEST on 𝒞^1P before the climbs (stable order; nestclass.py positions): onep_fdkey_n20 2. Every other onep_* instance
  and every other instance of this box has 1 (lagdist_D8 is a single position repeated 13 times: an additive staircase).
- Two-player best: nest4_n80 has NEST 4 at n 80 (R41). It is not in the class.

## 4. Status, and the next construction to try
- NEST 3 is realised on 𝒞^1P (nest3_n20, one instance, not a family); in two-player games NEST 4 is the best seen.
  No super-polynomial growth has been seen: every phase observed is at most linear in n.
- The obstruction is not proved. (N1)-(N3) are necessary conditions, and no lemma shows they cannot hold together.
- Concrete next target (open): a 2-level class gadget.
  - Level 1: the swap of R42 §5, where a vertex v moves between positions p and p + 1.
  - Level 2: a tangle family below p+1 whose tangles contain v. Then each swap breaks them, by (N2a) when v is absorbed and by
    (N2b) when v leaves the region.
  - Test: if NEST reaches 3 at fixed size and then grows with k copies of the gadget, (CTX⁺) on 𝒞^1P is in danger. If (N2) and
    (N3b) prove incompatible (the swapped vertex cannot both break lower tangles and keep the higher context set equal in size),
    that is the obstruction.
