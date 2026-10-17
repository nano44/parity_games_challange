# Referee report R-STEP5: GAP-C Step 5 (completeness of A_DTL), claims (1)-(5)

Referee: REFEREE, running on Opus 5.5 under owner ruling D12 (Lead reading L33). Started 09:13Z, written 09:24Z-09:40Z
2026-10-17 (date -u). docs/referee-2/ was not read. The lane re-reads of NT-f step (D) (Lead; L-RED R28) were not used:
every step below was checked by me against the code.
Packet (pinned): trunk 8f41be8, docs/alg/STEP5.md and docs/alg/GAP-C.md §18g-§18k. Code: Oink 8fbf0a7,
tools/oink/src/src/solvers/dtl.cpp (built with scripts/setup_oink.sh; `git log -1` in tools/oink/src = 8fbf0a7).
Candidate A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum ω (L26).
"N" below = dtl.cpp line N. Machine checks (mine): docs/referee/scratch/step5_probe.py.

## Verdict
| claim | verdict (Opus 5.5, D12) |
|---|---|
| (1) KT definitions; KT(G') when D ≠ ∅; KT(R_end) fails (§18g) | SIGN (Opus 5.5, D12) |
| (2) Lemma NT-f (§18k A-D, D1, D2) | SIGN (Opus 5.5, D12); one uncited step, closed here (F2.1) |
| (3) FM and WM as consequences of NT-f | SIGN (Opus 5.5, D12) |
| (4) the (YZ) reading; (YZ) ⇐ (ACYC) (STEP5 §6) | (YZ) reading: SIGN (Opus 5.5, D12). (YZ) ⇐ (ACYC): SIGN WITH GAPS (Opus 5.5, D12), gaps G4.1-G4.2, both closed in §4 below |
| (5) Lemma P-KT given (YZ) (§18h steps 1-4, both owner cases) | SIGN WITH GAPS (Opus 5.5, D12), gap G5.1 (the case c1 = 0), closed in §5 below |

No REJECT. Nothing here touches (ACYC), which stays open (§6). Every statement signed is a reading of dtl.cpp @ 8fbf0a7 that
uses no order-specific choice (Q stack order, equal-priority indexing, in/out-list order, SCC emission order): it holds for
every ω.

## 0. Code facts used (read by me)
- C1 (sorted indices). Oink calls game.ensure_sorted() = sort(NULL) before solving (oink.cpp:35, game.hpp:178), and dtl.cpp
  relies on it (721 max_prio = priority(n−1); 937 break). So index(a) ≥ index(b) ⇒ pr(a) ≥ pr(b), for every ω.
- C2 (best_vertices 643-776). prevV := V at the start of each round (676). Region loop: CurR := R once per round (690),
  consumed across the tops of the round (699); CurZ is the current region only, reset after each top (704); the local
  bitset Z (652) accumulates the regions (703). The rescue loop (722-741) runs on that same Z, t ascending from 0;
  at every level every member of Z is pushed (724) and every pushed vertex is popped and given attractVertices and
  attractTangles with (R, Z, R, t) (727-731); candidates are listed in descending index (713) and checked after each level
  only while pr(u) > t (737). Z is reset only at 763. On "V became empty" V.swap(prevV) (770): the returned V is V_f, all of
  whose members were candidates of round f that no level rescued.
- C3 (attractTangle 110-185). A tangle vertex in Z is skipped (136), one outside R rejects (138), a new one above max_prio
  rejects (140); "nothing new" returns false (146); an escape not in Z and in Gx rejects (155-156). attractTangles is called
  only from a popped vertex v and tries exactly tin[v] (200-201), i.e. the tangles having v as an escape (443).
- C4 (attractVertices 65-101). A predecessor in Z only gets str (73); one in R with pr ≤ max_prio is added, an opponent one
  only if no successor lies in Gx \ Z (76-86).
- C5 (search_rec 834-991). Depth 0 is search_rec(CurG = copy of G, p, 0) (1014-1015) with X := ∅; S pieces (878-890),
  T pieces (914-951) and P pieces (961-991) each move exactly what they take from R into X, so X = G' \ R at depth 0.
  this->G is not changed during search_rec (solving happens after it, 1023-1039), and tangles are created only in sptl,
  never inside best_vertices or Dom.
- C6 (tangle creation). CHECK_UNIQUE is on (23). Escapes = all G-successors outside the SCC of its opponent vertices
  (327-339). tpr := pr(top) (461).

## 1. Claim (1): KT — SIGN (Opus 5.5, D12)
Definitions (§18g = STEP5 §2) checked as mathematics over the game G' (edges = edges of G'; "the game on Q_c" lets neither
player use an edge leaving Q_c, and the opponent's leaving edges are explicitly deleted; wording note only).
- KT(G') when D ≠ ∅: at depth 0 the first context is R = G', X = ∅ (C5). D = W_p(G') is a nonempty p-dominion of G'; take W1
  ⊆ D a p-dominion of G' with least maximum c1. c1 has p's parity: otherwise let B be the opponent's attractor to the
  priority-c1 vertices inside G[W1]; B ≠ W1 (else the opponent visits c1 infinitely often against σ1), W1 \ B is an
  opponent trap in G[W1], and if the opponent won all of G[W1 \ B] he would win all of W1 (standard Zielonka step); so p
  wins a nonempty part of it, a p-dominion of G' with maximum < c1, contradicting minimality. W1 ⊆ S_{c1}, A_{c1} = ∅,
  W1 is opponent-closed and σ1-closed, so W1 ⊆ W_p(F_{c1}). Correct.
- KT(R_end) fails: best_vertices returns 0 iff R has no p-priority vertex (661-668); every infinite play of any F_c on R_end
  is won by the opponent and dead ends lose for p, so W_p(F_c) = ∅ for all c. Correct.
- Data flow: X = G' \ R at depth 0 (C5) is what makes the KT frame's X the code's X. Checked.

## 2. Claim (2): Lemma NT-f — SIGN (Opus 5.5, D12)
Every step checked against the code:
- (A) Induction over round f's additions before t (all by attractVertices, t being the first tangle). Top: τ_x ∈ V_f ⊆ V_r,
  and in round r it is either inside a region of a higher-index top or gets its own (692). p-vertex x added at the pop of
  v: v ∈ A^r(τ_x) lies in a round-r region of a top σ with index(σ) ≥ index(τ_x), so pr(σ) ≥ pr(τ_x) ≥ pr(x) by C1; v is
  popped in round r, and at that pop x is in CurZ, consumed (in a region of index ≥ index(σ)), or attracted (74, 88).
  Opponent x: at its round-f addition every successor in CurR was in CurZ (80), so all its R-successors were added before
  it in round f (consumed or current region); at the round-r pop of the last of them no successor is in CurR \ CurZ (all
  are popped, 699), so x is taken or attracted, at a top of index ≥ index(τ_x). Correct; uses no order datum.
- (B) Acceptance needs every escape to be in CurZ or outside CurR (155-156), i.e. added in round f before t, hence (A).
  Correct.
- (C) t ⊆ CurZ ⊆ Z_f after acceptance. A p-vertex of t has its stored strategy inside t (the SCC is taken in the graph
  restricted by str, 268-285, and str is stored with it, 452-456); an opponent vertex of t has all G-edges in t ∪ escapes
  (327-339) and one edge in t (nontrivial SCC, or the self-loop case 317). So attracts(p, v, Z_f, R) (40-57) and v is no
  candidate (714), while every member of V_f is a candidate (C2). Correct.
- (D) q = tpr(t) is used as "the maximal priority in t". F2.1 (uncited step, closed): this needs top ∈ t, which the
  packet does not justify. It holds: DTL-proof.md Lemma 1.5a (every vertex of a closed sptl region reaches the top in the
  restricted graph, so the only nontrivial SCC reachable from the top is the top's; I re-derived it: vertex-rule edges go
  to earlier pushes, a firing tangle's new vertices reach the popped escape through the tangle's own strongly connected
  strategy graph, top has the earliest push) gives top ∈ t, and all vertices of an sptl region have priority ≤ pr(top)
  (494). So q = max pr(t), of p's parity, and M_q ≠ ∅. DATA (mine, step5_probe.py, 254 corpus files, both orders):
  6,815 stored tangles, top ∈ t and tpr = max pr(t) in all. Authors should cite Lemma 1.5a at (D).
  q = 0: t ⊆ V_{r_1} ⊆ Z^{r_1} (every V-vertex is in Z after the region loop, 692), escapes in R in Z^{r_1} by (B), so m_1
  attracts into Z^{r_1} and is no candidate at r_1. Correct. (f = 1 is covered: (C) puts M_q outside V_1, impossible.)
- (D1) Exactly as C2: the rescue loop runs on the bitset Z left by 703 (not reset before 763), so it starts as Z^{r_1};
  attractVertices and attractTangle only add; 724 pushes every member at every level including q−1 (q−1 ≤ max_prio);
  e ∈ Z^{r_1} is popped and attractTangle(t) is evaluated (t ∈ tin[e], 443/200-201). Correct.
- (D2) t is alive at r_1 (accepted at f > r_1; deletion is permanent, 134; no tangle is created inside best_vertices, C5).
  Every vertex of t is in R (accepted in round f from CurZ ∪ CurR ⊆ R), the priority-q ones are in Z, the rest have
  priority ≤ q−1 (q = max), every escape in R is in Z. So either t is added or the "nothing new" exit fires (146): t ⊆ Z
  in both cases. The candidate check after level q−1 reaches m_1 (pr = q > q−1, descending list, 737) and attracts holds:
  m_1 is rescued at r_1, contradiction. Correct.
DATA (mine, independent instrumentation of dtl_pyref through dtl_step5.S5, docs/referee/scratch/step5_probe.py, 254 .pg
under experiments/ with n ≤ 80): −1 calls 8,323 (Oink order) / 8,145 (stable), final-round acceptances 0 / 0.
Oink-order tangle count on strfam_S5_n46.pg = 30, equal to pinned Oink's ("found 1 dominions and 30 tangles", verified).

## 3. Claim (3): FM and WM — SIGN (Opus 5.5, D12)
By NT-f, every addition of round f is a vertex-rule addition, so (A) covers all of round f: Z_f ⊆ ∪_τ A^r(τ) ⊆ Z^r for every
round r (FM). WM: Z^r ⊆ A^r_t for every t because the rescue loop starts from Z^r and only adds (C2). The FM+ form in the
STEP5 table is (A) itself; its exceptional case is a round-f tangle acceptance, excluded by NT-f. Correct.
DATA (mine): FM failures 0 / 8,323 (Oink), 0 / 8,145 (stable).

## 4. Claim (4): (YZ) reading — SIGN (Opus 5.5, D12); (YZ) ⇐ (ACYC) — SIGN WITH GAPS (Opus 5.5, D12)
(YZ) reading (§18h end, STEP5 YZ-read and its NT-f sharpening). Dom(prevV, R) (962-976) against the final region loop
(690-706): same V (= V_f by 770), same R (nothing between 853 and 962 changes R: the scan 898-912 adds nothing at a P piece),
same tangle store (C5), tops high to low. With Dom's X = old X ∪ earlier parts ∪ current part and the loop's CurZ = current
region: the skip tests (963 X[top] / 692 Z[top]) agree; in attractVertices the "in Z" branch differs only for predecessors
in old X or earlier parts, which the loop finds outside CurR, so neither adds them; the escape tests (R[to] ∧ ¬X[to] vs
CurR[to] ∧ ¬CurZ[to]) both mean "pushed-not-popped excluded, unconsumed R"; in attractTangle the only different answer is a
tangle vertex in old X or an earlier part (Dom 136: skipped; loop 138: reject), and escapes there are accepted by both.
A Dom rejection or "nothing new" exit returns false as the loop does, so the runs diverge exactly at the first Dom
acceptance of such a tangle. Tangle deletion (134) has the same effect in both (a tangle with a vertex outside G can never
fire). Sharpening: before that point Dom's acceptances are the loop's, excluded by NT-f. Correct.
DATA (mine): P pieces (all depths) 4,476 Oink / 4,377 stable, Y_0 ≠ Z_f in 0 / 0; straddling Dom acceptances 0 / 1
(the stable-order one is strfam_S5_n46.pg, sha1 52a75d0c, as reported).

(YZ) ⇐ (ACYC) (§18k end, STEP5 §6.1). Steps (i) and (ii) are correct: a new p-vertex's stored successor is not in old X (it
would attract into X, and the P-piece scan found none) nor in an earlier part (it would have been attracted at that pop:
the earlier top has priority ≥ pr(τ_j) ≥ pr(v) by C1, v unconsumed); an opponent vertex's edges into old X are outside CurR
and ignored (80). Step (iii) is a sketch; two points are missing in the written proof:
- G4.1 (direction "loop region ⊆ Dom part" and the use of least fixed points). The packet cites "regions are least fixed
  points" and concludes equality. Needed and true: (a) a region computed by the worklist is the least set containing the
  top closed under the vertex rules and under "a tangle with an escape in the set, vertices in the set or unconsumed of
  priority ≤ pr(top), escapes in the set or consumed/outside", because both conditions are monotone and a tangle is retried
  at the pop of each of its escapes (C3), the last of which sees all of them in; this is DTL-proof.md Lemma 1.2 / GAP-A-M §1
  for the region loop, and the same holds for Dom's part with "in the set" widened to Dom's X. (b) Dom's rules contain the
  loop's (a tangle the loop accepts at a set has every vertex and escape in Dom's X or outside R), so, with equal consumed
  sets, loop region ⊆ Dom part. (c) Dom part ⊆ loop region by induction over Dom's additions: vertex rules are identical;
  a non-straddling acceptance is an instance of the loop's tangle rule at the loop region (closed, so nothing new); a
  straddling one is absorbed by (ACYC) as in (iii). Then the consumed sets agree for the next top. Closed here.
- G4.2 (trigger of the vertex rule for a new opponent vertex u). The vertex rule fires only at the pop of a successor of u
  in the current region; (ii) allows all of u's R-edges to go into earlier parts. That case is impossible: at the pop of
  the last such successor in the earlier parts, u (unconsumed, priority ≤ that top's) would have been attracted there, in
  both runs, so u would not be new. Hence every sink of H_{t_X}[N_X] has a trigger in the current region, and the
  reverse-topological absorption of (iii) goes through. Closed here.
With G4.1-G4.2 imported, (ACYC) ⇒ (YZ) is correct as stated.

## 5. Claim (5): Lemma P-KT given (YZ) — SIGN WITH GAPS (Opus 5.5, D12)
Setting checked: T0 (R a p-trap of G') from the empty scan: attracts(p, v, X, R) (40-57) is false for all v ∈ R (the scan
covers all of R when Q stays empty, 899-912): no p-vertex has an edge into X, an opponent vertex with one into X has one into
R; with X = G' \ R (C5), H = G[R] is a game and D ∩ R a p-dominion of H. Every p-priority vertex x of R is in V_1 (662-667)
and, the call returning −1, leaves V at a round r(x) as a candidate that no level t < pr(x) rescues (C2). W1, c1 (p's
parity, same Zielonka step as §1, inside H), W1 closed in H: correct.
- (1) A'' ⊆ A^r_{c1−1}: after level t every member of the rescue set has been popped at level t (724), so it is closed under
  level-t vertex rules (p-vertex: at the successor's pop; opponent: at the pop of the last successor); A'''s p-rule cannot
  use X (p-trap), its opponent rule needs all G'-edges in X ∪ Z ∪ A'', hence all R-edges in Z ∪ A'' and ≥ 1 of them (H is a
  game). With FM/WM (claim 3) Z ⊆ A^r_{c1−1}. Correct.
- (2) both owner cases: p-owned x (pr = c1) has one successor in Z ∪ A'' (not X); opponent-owned x has all R-edges there and
  at least one; either way attracts(p, x, A^{r(x)}_{c1−1}, R), so x is rescued at level c1−1 < c1 = pr(x). Correct.
- (3) both owner cases: w ∈ T ⊆ Z; p-owned via σ1(w) ∈ W1 ⊆ Z ∪ A''; opponent-owned via all R-edges in W1 (closed in H),
  at least one. Correct.
- (4) U ⊆ S \ A; σ1 stays in U (σ1(v) ∈ Z ∪ A would put v in A); an opponent vertex of U has its R'-edges in U ∪ A and at
  least one in U (else all edges in X ∪ Z ∪ A); in F_{c1}(R') edges into A are deleted and none go to Q_{c1} \ U; σ1-plays
  in U are W1-plays. Correct.
- G5.1 (c1 = 0, possible only for p = Even). "A^r_{c1−1}" is then A^r_{−1}, which the rescue loop (t ≥ 0) does not define,
  and "rescued at level c1−1" is vacuous for a priority-0 vertex. Fix (closed here): read A^r_{−1} := Z^r; then A'' = ∅,
  and in (2)/(3) the priority-0 vertex x (resp. w) attracts into Z ⊆ Z^{r(x)} (FM), so it is not a candidate at round r(x)
  (714): the same contradiction. NT-f (D) already treats q = 0 this way; P-KT should say so.
P-KT is then correct as a conditional statement, hypothesis (YZ).

## 6. What the chain still depends on
1. (ACYC) — OPEN (known). Only DATA (lane: every observed straddling firing has 1-2 new opponent vertices; mine: 1 straddling
   firing in 254 files × 2 orders). Not attacked here (referee role).
2. (YZ) — follows from (ACYC) (claim 4); otherwise DATA only. P-KT is conditional on it.
3. DTL-proof.md Lemma 1.5a (top ∈ every stored tangle; tpr = max priority) — used by NT-f (D) (F2.1); re-derived by me, not
   a separate referee signature of DTL-proof.md.
4. DTL-proof.md Lemma 1.2 / GAP-A-M §1 (a region is the least fixed point of its rules, tangle retried at each escape pop)
   — used in (4) G4.1; checked by me only for the use made here.
5. Code facts C1-C6 (§0), all read at 8fbf0a7; C1 (sorted indices) is what turns "higher index" into "priority ≥" in (A)
   and in (YZ)⇐(ACYC) (i).
6. Positional determinacy and D = W_p(G') for the parity game G' (DTL-proof.md Lemma 1.4c) — standard.
7. Scope: all of this is depth-0 P pieces of one search. The S step and T step of KT (GAP-C §18i-18j) are DATA only, and
   (K-in) / GAP-C as a whole is NOT established by this report.

## 7. Findings for the author (L-ALG), one line each
- F2.1 NT-f (D): cite DTL-proof Lemma 1.5a for "tpr(t) = max pr(t)" (top ∈ t).
- G4.1 (YZ) ⇐ (ACYC) (iii): write both inclusions; the region and Dom part as least fixed points with tangle retrial at escape pops.
- G4.2 (YZ) ⇐ (ACYC) (ii)-(iii): exclude a new opponent vertex whose R-edges all lie in earlier parts (it would have been taken there).
- G5.1 P-KT (1)-(3): treat c1 = 0 (A^r_{−1} := Z^r; use candidacy at 714 instead of rescue).
- Wording (claim 1): "all its edges" = edges of G'; in F_c neither player may use an edge leaving Q_c.
