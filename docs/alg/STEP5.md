# STEP5: the Dom(prevV) removal keeps a thresholded core (L-ALG succ. 6, 2026-10-17; produced on Opus 5.5; unrefereed)
One-page brief for routing and for a referee after the Fable reset (D8/L27). Full record with data and killed
statements: docs/alg/GAP-C.md §18 (18a-18j). Algorithm: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7
(L22), pseudocode docs/alg/candidates/C5-DTL.md, every order datum (L26). "dtl.cpp N" = tools/oink/src/src/solvers/dtl.cpp.

## 1. What Step 5 was
GAP-C.md §17: completeness (Lemma K) by induction over the depth-0 pieces of one search(p) fails at the −1 piece with Q
empty (dtl.cpp 961-991), which removes Dom(prevV, R) — neither p-won nor opponent-won — and must be "repaid" later.

## 2. Setting and definitions
search(p) on the unsolved set G' (a parity game; DTL-proof.md Lemma 1.4c); D := W_p(G'); σ a positional winning strategy
of p on D (plays from D stay in D). Depth-0 iteration with context R, X := G' \ R (every depth-0 piece moves exactly what it
takes from R into X). A P piece: best_vertices (643-776) returned −1 with V = prevV (676, 770) and the threshold scan
898-912 found no vertex attracting into X. Rounds 1..f of that −1 call: tops V_r, region unions Z^r (690-708), rescue
attractors A^r_t (722-740); Z_f := Z^f. Every p-priority vertex x of R leaves V at a round r(x) as a candidate (714) that is
not rescued at any t < pr(x).
KT (thresholded core). For c of p's parity: S_c := D ∩ R ∩ {priority ≤ c}; A_c := the plain p-attractor of X inside S_c (an
opponent vertex enters only when all its edges are in X ∪ A_c); F_c := the game on S_c \ A_c with the opponent's edges
leaving it deleted and dead ends lost for p. KT(R) :⇔ W_p(F_c) ≠ ∅ for some c.

## 3. Statements
| | statement | status |
|---|---|---|
| T0 | at a depth-0 P piece, R is a p-trap of G' (no p-vertex of R has an edge into X; an opponent vertex of R with an edge into X also has one into R), so H := G[R] is a game and D ∩ R is a p-dominion of H | PROVED (reading of attracts, 40-57) |
| KT0 | KT(G') holds when D ≠ ∅; KT fails at R_end (best_vertices returns 0: no p-priority vertex) | PROVED |
| YZ-read | Dom(prevV, R) (961-976) and the final round's region loop (690-708) are step-for-step equal until Dom's attractTangle accepts a stored tangle with a vertex in old X or in an earlier top's part of the Dom (Dom: "in Z", 136-137; region loop: rejected, 138-139) | PROVED (reading) |
| FM+ | in a −1 call, each final region Z^f_τ lies in the round-r union of the regions of tops with index ≥ index(τ), for every round r, unless round r straddles (Lemma E (a), GAP-A-M §3) a tangle that round f attracts | PROVED except that case |
| P-KT | at every depth-0 P piece with D ∩ R ≠ ∅, KT(R \ Y_0) holds (Y_0 the removed set), witnessed at level c1 | PROVED given (YZ) Y_0 = Z_f and (FM) Z_f ⊆ Z^r for all rounds |
| (YZ), (FM) | as above | DATA: 0 failures (YZ on 63,000+ P pieces, FM on 106,091 −1 calls; corpus both orders, unions) |
| KT-STEP-first | the first depth-0 piece after which KT fails learns inside D | DATA 0 violations; with KT0 and P-KT it would give (K-in) |

## 4. Proof of P-KT (given (YZ), (FM))
W1 := a p-dominion of H inside D ∩ R with the least maximum priority c1 (exists by T0). c1 has p's parity (otherwise W1
minus the opponent's attractor to its top priority contains a p-dominion of H with a smaller maximum). W1 is closed in H
(opponent vertices keep all their R-edges in W1), p wins it with σ1 staying inside. (FM) gives Z_f ⊆ Z^r ⊆ A^r_t for every
round r and level t.
(1) A'' := the plain p-attractor of X ∪ Z_f inside S_{c1}(R') ∩ {priority ≤ c1−1} (R' := R \ Z_f) lies in A^r_{c1−1} for
every round r: the level-t rescue pass is closed under attraction of vertices of priority ≤ t, and by T0 A'''s rules are
instances of the rescue rules.
(2) A_{c1}(R') = A'': a least-rank vertex x outside A'' has its witnesses in X ∪ Z_f ∪ A''; pr(x) ≤ c1−1 puts it in A'';
pr(x) = c1 makes x attract into A^{r(x)}_{c1−1} (p-owned: one edge; opponent-owned: all R-edges, at least one), so x was
rescued at round r(x): contradiction.
(3) If W1 ⊆ Z_f ∪ A'' then the priority-c1 vertices of W1 lie in Z_f; such a w attracts into A^{r(w)}_{c1−1} — if p-owned
through σ1(w) ∈ W1, if opponent-owned through all its R-edges, which lie in W1 — so w was rescued: contradiction. Hence
U := W1 \ (Z_f ∪ A_{c1}(R')) ≠ ∅.
(4) In F_{c1}(R') every p-vertex of U keeps σ1 inside U (σ1(v) ∈ Z_f ∪ A would put v into A), every opponent vertex of U keeps
an edge into U and all its remaining edges in U, no vertex of U is a dead end, and every play in U consistent with σ1 is a
W1-play: U ⊆ W_p(F_{c1}(R')). □

## 5. What is not done, and what killed the earlier frames
- (YZ) and (FM) are absences of straddling-tangle effects (GAP-A-M Lemma E), the family behind (α) and GAP-A's deficits.
- The S step and the T step of KT (GAP-C.md 18i, 18j) are DATA only; the T step needs the frame at recursion depth ≥ 1, where
  a core closed in G[R_d] is not guaranteed; the S step is existential over the levels ((S-LEVEL) killed).
- Killed (instances in GAP-C.md 18d, 18f, 18j): K-frame (P-K), (K-STEP-first) by L-RED pk_viol_n20 (R27); HYB
  (strfam_S2_n4), JD (psolc_partial_..._n4_m6), ATTR, SEG-ALL, LASTD for T, per-round KEEP, (S-LEVEL)
  (cross_h_k1_n12_m18_17).
