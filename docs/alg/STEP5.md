# STEP5: the Dom(prevV) removal keeps a thresholded core (L-ALG succ. 6, 2026-10-17; produced on Opus 5.5; unrefereed)
One-page brief for routing and for a referee after the Fable reset (D8/L27). Full record with data and killed
statements: docs/alg/GAP-C.md §18 (18a-18k). Algorithm: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7
(L22), pseudocode docs/alg/candidates/C5-DTL.md, every order datum (L26). "dtl.cpp N" = tools/oink/src/src/solvers/dtl.cpp.

## 0. Result (headline)
(ACYC) ⇒ (YZ) ⇒ Lemma P-KT, with NT-f, (FM), (WM) PROVED on the way (all readings of dtl.cpp, unrefereed; NT-f step (D)
independently re-read by the Lead and by L-RED, docs/red/R28-ntf-stepD.md, no gap found — not a referee signature).
- Lemma P-KT: at every depth-0 P piece (the −1 branch with Q empty, dtl.cpp 961-991) with D ∩ R ≠ ∅, the thresholded core
  KT survives the Dom(prevV) removal, at the level c1 of the least-maximum p-dominion of G[R] inside D (§4).
- It needs (YZ): the removed set equals the final pruning round's region union. (YZ) holds unless Dom(prevV) accepts a
  stored tangle using a vertex of old X or of an earlier top's part (YZ-read + NT-f), and even then it holds if the new part
  of that tangle has no cycle of the tangle graph (ACYC) (§6.1).
- The single open point is (ACYC), §6.1. Everything else of Step 5 is proved.

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
| FM+ | in a −1 call, each final region Z^f_τ lies in the round-r union of the regions of tops with index ≥ index(τ), for every round r, unless round r straddles (Lemma E (a), GAP-A-M §3) a tangle that round f attracts | PROVED; by NT-f the exceptional case never occurs |
| NT-f | the final pruning round of a −1 call accepts no stored tangle in its region loop | PROVED (reading; GAP-C.md 18k): the first such tangle's escapes lie in every earlier union (vertex-rule induction), its first-pruned top-priority vertex would have been rescued (q ≥ 1) or not been a candidate (q = 0). DATA 15,939/15,939 calls; INV-T (the same for intermediate rounds) is FALSE, 628 cases |
| FM, WM | Z_f ⊆ Z^r ⊆ A^r_t for every round r and level t | PROVED (corollary of NT-f + the FM+ induction) |
| P-KT | at every depth-0 P piece with D ∩ R ≠ ∅, KT(R \ Y_0) holds (Y_0 the removed set), witnessed at level c1 | PROVED given (YZ) Y_0 = Z_f only ((FM) is now proved) |
| YZ-read (sharpened) | by NT-f, Dom(prevV) accepts no tangle at all unless its first acceptance uses a vertex of old X or of an earlier top's part; without such an acceptance Y_0 = Z_f | PROVED (reading) |
| (YZ), (FM) | as above | DATA: 0 failures (YZ on 63,000+ P pieces, FM on 106,091 −1 calls; corpus both orders, unions). The YZ-read exception does occur once (strfam_S5_n46.pg, stable order: Dom fires the stored tangle {14,15,16,17} using a vertex of old X / an earlier top's part) yet Y_0 = Z_f and P-KT hold there |
| KT-STEP-first | the first depth-0 piece after which KT fails learns inside D | DATA 0 violations; with KT0 and P-KT it would give (K-in) |

## 4. Proof of P-KT (given (YZ); (FM) is PROVED, GAP-C.md 18k)
W1 := a p-dominion of H inside D ∩ R with the least maximum priority c1 (exists by T0). c1 has p's parity (otherwise W1
minus the opponent's attractor to its top priority contains a p-dominion of H with a smaller maximum). W1 is closed in H
(opponent vertices keep all their R-edges in W1), p wins it with σ1 staying inside. (FM) gives Z_f ⊆ Z^r ⊆ A^r_t for every
round r and level t.
(1) A'' := the plain p-attractor of X ∪ Z_f inside S_{c1}(R') ∩ {priority ≤ c1−1} (R' := R \ Z_f) lies in A^r_{c1−1} for
every round r: the level-t rescue pass is closed under attraction of vertices of priority ≤ t, and by T0 A'''s rules are
instances of the rescue rules.
(2) A_{c1}(R') = A'': a least-rank vertex x outside A'' has its witnesses in X ∪ Z_f ∪ A''; pr(x) ≤ c1−1 puts it in A'';
pr(x) = c1 (p's parity, so x ∈ V_1 and x leaves V at a round r(x)) makes x attract into A^{r(x)}_{c1−1} (p-owned: one edge; opponent-owned: all R-edges, at least one), so x was
rescued at round r(x): contradiction.
(3) If W1 ⊆ Z_f ∪ A'' then the priority-c1 vertices of W1 lie in Z_f; such a w attracts into A^{r(w)}_{c1−1} — if p-owned
through σ1(w) ∈ W1, if opponent-owned through all its R-edges, which lie in W1 — so w was rescued: contradiction. Hence
U := W1 \ (Z_f ∪ A_{c1}(R')) ≠ ∅.
(4) In F_{c1}(R') every p-vertex of U keeps σ1 inside U (σ1(v) ∈ Z_f ∪ A would put v into A), every opponent vertex of U keeps
an edge into U and all its remaining edges in U, no vertex of U is a dead end, and every play in U consistent with σ1 is a
W1-play: U ⊆ W_p(F_{c1}(R')). □

## 4b. Proof of NT-f (GAP-C.md 18k)
Let a best_vertices call return −1 after rounds 1..f, and suppose round f's region loop (690-708) accepts a stored tangle;
let t be the first one, accepted in the region of τ ∈ V_f at the pop of an escape e ∈ R (tangles are tried only at pops of
their escapes, 198-202).
(A) Every vertex x added in round f before t lies, for every round r, in the union of the round-r regions of the tops of
index ≥ index(τ_x) (τ_x the round-f top of x's region). Induction over round f's additions, all by attractVertices
(65-101): τ_x ∈ V_r is consumed or gets its region; a p-vertex added at the pop of v is attracted at v's round-r pop or
already taken (the region of v at round r has a top of priority ≥ pr(τ_x) ≥ pr(x)); an opponent vertex has all its R-edges
into vertices added before it (escape test 76-86) and is attracted or taken at the round-r pop of the last of them.
(B) So t's escapes in R lie in Z^r for every r (acceptance needs every escape in R to be in the current region or already
consumed, 150-157).
(C) No p-priority vertex of t is in V_f: after the acceptance it attracts into Z_f (p-owned: tangle successor in t;
opponent-owned: all R-edges into t ∪ escapes, 325-339), so it would not be a candidate.
(D) q := tpr(t) (p's parity), m_1 := a priority-q vertex of t pruned first, at round r_1. All priority-q vertices of t are
in V_{r_1} ⊆ Z^{r_1}. q = 0: t ⊆ Z^{r_1} and m_1 attracts into Z^{r_1}, so it is no candidate. q ≥ 1: (D1) round r_1's rescue
loop runs on the same bitset Z that the region loop leaves (703-705), so it starts as Z^{r_1} and only grows; line 724
pushes every member of Z at every level and 727-730 pop each one and call attractTangles, so e ∈ Z^{r_1} (by (B)) is popped
at level q−1 and attractTangle(t) (t ∈ tin[e]) is evaluated with the set ⊇ Z^{r_1}. (D2) At level q−1 the pop of e finds every priority-q vertex of t in the set, the rest of priority ≤ q−1, its escapes in R
in the set: either t joins the set, or t lies in it already (attractTangle's "nothing new" exit, 146); in both cases t ⊆ the
set, and m_1 then attracts into it: rescued. Either way m_1 is not pruned at r_1. □
Corollaries: (FM) Z_f ⊆ Z^r for all r ((A) covers every addition of round f); (WM) Z_f ⊆ A^r_t; (YZ-read sharpened).

## 5. (Superseded: the former counterexample shape for NT-f; NT-f is PROVED. The shape is kept in GAP-C.md 18h.)

## 6. What is not done
### 6.1 The single open point of Step 5: (ACYC)
(ACYC) For every stored tangle t_X that Dom(prevV, R) accepts at a P piece using a vertex of old X or of an earlier top's
part, the new part N_X := (vertices of t_X taken by that acceptance) contains no cycle of the tangle graph H_{t_X}
(p-vertices keep their tangle strategy, opponent vertices all their edges inside t_X).
Why it suffices (PROVED, GAP-C.md 18k end): a p-vertex of N_X has its tangle successor in the current region or in N_X (an
edge into X is excluded by Q empty, an edge into an earlier region would have pulled it there); an opponent vertex of N_X
has its R-edges in the current region, earlier regions or N_X, and its edges into old X are ignored by the vertex rule
(76-86); so with N_X acyclic the final round's region loop takes N_X by vertex rules and, regions being least fixed points,
Y_0 = Z_f.
Exact shape of a counterexample (for L-RED): a P piece whose Dom(prevV) accepts such a t_X with a p-won cycle C ⊆ N_X
(C ⊆ R, every vertex of C new). Sub-cases: (a) the straddle uses only an earlier top's part (no old-X vertex) — then if
the maximum m_C of C is a final top and is the maximum of N_X, the final round's rescue loop accepts t_X and rescues m_C,
a contradiction; so (a) needs ties or m_C below another new vertex; (b) the straddle uses old X — the rescue loop rejects
t_X (an old-X vertex is outside R), and nothing found so far excludes it. If m_C ∈ V_f, m_C is a final candidate, so C is
not inside Z_f and (YZ) fails; whether P-KT still holds on such a piece is open.
DATA: every firing observed (1 in the corpus, strfam_S5_n46.pg stable order; climbs from it, experiments/alg/
dtl_yzclimb.py, new parts up to 6 vertices) has an acyclic new part; (YZ) and P-KT hold on all data.

### 6.2 Beyond Step 5
- The S step and the T step of KT (GAP-C.md 18i, 18j) are DATA only. The T step needs the frame at recursion depth ≥ 1:
  (CORE-PASS-closed) DATA 45/45 says a T piece that breaks KT hands the recursion a p-dominion of G[Z'] inside D, and with
  it P-KT's proof runs unchanged inside the recursion; the S and T steps there remain. The S step is existential over the
  levels ((S-LEVEL) killed).
- Killed (instances in GAP-C.md 18d, 18f, 18j, 18k): K-frame (P-K), (K-STEP-first) by L-RED pk_viol_n20 (R27); HYB
  (strfam_S2_n4), JD (psolc_partial_..._n4_m6), ATTR, SEG-ALL, LASTD for T, per-round KEEP, MONO/R-MONO, P-A, INV-T
  (c_best_s34), (S-LEVEL) (cross_h_k1_n12_m18_17).
