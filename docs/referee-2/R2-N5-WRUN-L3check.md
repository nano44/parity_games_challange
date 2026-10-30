# R2-N5-WRUN-L3check: independent re-check of REFEREE's WRUN-L3 and WRUN-L4 on line L-2 (REFEREE-2 successor 23, Opus 5.5, D15)
Object: docs/new/P-N5-WRUN-box92-line-L2.txt @ l-new 85c12579 (sha1 8ab101e5…). REFEREE's items: docs/referee/R-N5-WRUN-C.md §4 at
claude/referee 6e83247a. I split L-2's claims part at each «; (Lemma|Theorem|Corollary» and read every clause for the binder of each free
symbol (F, X, g, z, v, t, τ).

## WRUN-L3: AGREE, REQUIRED. I missed it on L-1 (my R2-N5-WRUN.md §3 listed F as «bound»; it is defined, not quantified).
- The parenthesis defines quantities «for a W-run F», but the clauses then use F without a quantifier:
  - TRIPLE-RED: «E0_F(X, g) ≤ n, and |F| ≤ m_E + Σ RET_F ≤ …»;
  - RET-ΞRISE / FREE-RED: «RET_F(X, g) ≤ ΞCH_F(g) and FREE_F(X, g) ≤ RET_F(X, g) ≤ |F| ≤ …»;
  - ΞCH-PCH / RSTAR-PCH: «ΞCH_F(z) ≤ n(n + 1 + PCH_F(z)) and R*_F ≤ …»;
  - PREFIX-MON / LEVEL-RED: «PCH_F(v) ≤ n(2n + 1)^k + DEEP_{k,F}(v)» (v and F free);
  - NO-DEV: «if Ξ_t = W_t at every state of F then …»;
  - BIP-RED: «|F| ≤ SB_F + …».
  Only XI-RUN's clause quantifies («every W-run F has …»).
- The z defect is real and is worse than a missing binder. In the GAP-DEV / ΞCH-PCH / RSTAR-PCH clause, z is introduced as «a target z of
  an edge blocked at a state q of a W-run», so the following «ΞCH_F(z) ≤ n(n + 1 + PCH_F(z))» reads as a statement about blocked targets
  only. The packet's §6.2 is «for every W-run F and vertex z», and E2 (XI-CH-POLY ⇔ P*-POLY) needs it for every z.
- The proposed global binder («for every N5 run, every W-run F = [a, b] of it, every Even edge (X, g) and all vertices v, z: …») is right in
  substance. Two cautions so that it does not create new shadowing:
  1. GAP-DEV must then not re-introduce z: write «if (y, z) is blocked at a state q of F, then Ξ_q(z) ◁ W_q(z) and …» (with y free for the
     edge, z the global vertex). As now worded («a target z of an edge …»), the clause would rebind the global z.
  2. The sums Σ_{(X, g)} (TRIPLE-RED) and Σ_{(y, z) Even edge} (RSTAR-PCH) rebind X, g and z as summation indices. That is formally
     harmless, but a reader may take the global (X, g) or z for the summed one. Either rename the indices (Σ_{(X′, g′)}, Σ_{(y′, z′)}), or
     put only «for every N5 run and every W-run F of it:» in the global binder and quantify per clause («every Even edge (X, g) has …»,
     «every vertex z has …», «every vertex v and every k ≥ 1 …»).
  Either variant is acceptable. My preference is the second (global F only, per-clause edges and vertices), because XI-RUN, INT-XCH⁰ and
  WAIT-CYCLE′ quantify their own objects (a stretch R, a W-constant interval I, a block at any state of the run), and PREFIX-MON's monotonicity
  is about states t of the whole run, not of F.
- Content does not change; only quantifiers.

## WRUN-L4: AGREE, REQUIRED.
REL2-WRISE «(A2) the τ-play from z under σ_{s+1} with y → z avoiding y»: τ is bound only in the BIP-MON clause («τ_t ≡ τ (the W-run's Odd
strategy)»). I marked this optional on L-2 because Φ determines τ. Under the strict symbol test, which I apply elsewhere, it is a free
symbol, so I upgrade it to REQUIRED. Fix as REFEREE proposes: «the (σ_{s+1}[y → z], τ_s)-play from z avoids y».

## Verdict on L-2, revised
REQUIRED CHANGES: WRUN-L3, WRUN-L4 (Opus 5.5, D15). This supersedes «MATCHES» in my R2-N5-WRUN-L2.md (c2bfcc4c). Everything else there
stands. I will word-diff L-3.
