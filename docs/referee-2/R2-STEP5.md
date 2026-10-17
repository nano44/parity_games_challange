# R2-STEP5: second-referee read of Step 5 of GAP-C (KT, NT-f, FM/WM, (YZ) ⇐ (ACYC), P-KT) — REFEREE-2, 2026-10-17 09:27Z (date -u)
Packet (pinned): trunk 8f41be8, docs/alg/STEP5.md, proofs in docs/alg/GAP-C.md §18a, §18g, §18h, §18k. Code: Oink dtl.cpp @ 8fbf0a7
(tools/oink/src/src/solvers/dtl.cpp, built with scripts/setup_oink.sh), pseudocode docs/alg/candidates/C5-DTL.md (§0 order data).
A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (L26). Also opened: docs/alg/DTL-proof.md §1.4-§1.6
at 8f41be8 (Lemma 1.5a, used by NT-f (D); re-derived below). Not read before this report was pushed: docs/referee/. L-ALG's and
L-RED's re-reads (R28) were not taken as checks. Produced on Opus 5.5 under D12.
My probe (assertions only, the algorithm unchanged): docs/referee-2/R2-STEP5/ (dtl_probe.patch = full diff of the instrumented
dtl.cpp; run.sh, relabel.py, gen.py, climb.py, agg.py; probe_results.txt).

## Verdicts (Opus 5.5, D12)
| claim | verdict |
|---|---|
| (1) KT definitions, KT(G'), ¬KT(R_end) (§18g) | **SIGN WITH GAPS** (G1: "all its edges" must be read as edges of the game G'; wording only) |
| (2) Lemma NT-f (§18k, A-D, D1, D2) | **SIGN WITH GAPS** (G2: step (D) needs DTL-proof Lemma 1.5a, tpr(t) = max priority of t and attained in t; I re-derived it, so it is cited, not open) |
| (3) FM and WM from NT-f | **SIGN** |
| (4) the (YZ) reading, and (YZ) ⇐ (ACYC) | **SIGN WITH GAPS** (G3: the step "the region loop takes N_X by vertex rules" skips the trigger condition; closed below) |
| (5) Lemma P-KT given (YZ) (§18h) | **SIGN WITH GAPS** (G4: the case c1 = 0 is not spelled out; G1 again) |
No REJECT. No step is data-only in the five claims; the DATA rows of STEP5 §3 (YZ, FM counts, KT-STEP-first) are not part of
what is signed. All gaps G1-G4 are closed in this report; none is a hypothesis.

Remaining hypotheses of Step 5 (what the signed chain still needs): (ACYC) (open, STEP5 §6.1). With (ACYC): (YZ), then P-KT at
every depth-0 P piece with D ∩ R ≠ ∅. Facts used without new proof: Oink's order datum O1 (vertex index non-decreasing in
priority; oink.cpp:35 and C5-DTL §0, relied on by dtl.cpp 721, 737) and the standard parity-game facts named in (1).
Outside these five claims and not refereed: FM+ as a separate row, KT-STEP-first, the S and T steps (18i, 18j), (K-in).

## 1. Code facts I checked myself (dtl.cpp @ 8fbf0a7)
- attracts 40-57: a p-owner needs an edge into Z. An opponent owner returns false at its first edge into R \ Z, so it
  returns true iff it has an edge into Z and none into R \ Z. Edges outside Z ∪ R are ignored.
- attractVertices 65-101: predecessors `from` of the popped v. If `from` is in Z, only str changes (73). If it is in R with
  pr ≤ max_prio, a p-owner is added. An opponent owner is added unless it has an edge into G \ Z (76-86). Everything added is
  pushed onto Q (90). Q is a stack (uintqueue.hpp pop = back); no argument below uses the order.
- attractTangle 110-185: the per-vertex scan, in order: not in this->G → delete and false; in Z → skip; not in R → false;
  pr > max_prio → false. Then "nothing new" → false (146). Then an escape in G \ Z → false (155-156). Otherwise every vertex
  not in Z is added and pushed. attractTangles 198-202 runs this on tin[v] of the popped v. tin[e] ∋ t iff e ∈ tout(t) (443).
  tout(t) holds the edges of t's opponent vertices that leave t and go into this->G at creation (327-339).
- best_vertices 643-776: a local bitset Z (652) shadows the member Z. Each round sets CurR := R once (690) and consumes it
  across tops (699). Tops run in descending index, skipping those already in Z (692). After each region, Z |= CurZ and
  CurZ.reset() (703-704). Candidates (713-715) are tested against the full union Z^r. The rescue loop (722-741) runs on that
  same bitset Z, with G = R. At each level t it pushes every member (724) and pops them with attractVertices and
  attractTangles at threshold t (727-731). It then checks the candidates in descending index and stops at the first one with
  pr ≤ t (737). Uncaught candidates leave V (749-752). V is empty after a round with changes → V.swap(prevV) and return −1
  (768-771), so the returned V = V_f, every vertex of which was a candidate not rescued in round f. R is never modified in
  best_vertices.
- search_rec 834-994: the threshold scan 898-912 breaks only when Q is non-empty, so with Q empty at 914 it has tested every
  v ∈ R. Z is empty at the scan: it is reset after S (875) and after T (955), and the scan adds nothing. Dom 961-991 uses the
  same R and the same V = V_f with `!X[top]`. In every piece, each vertex pushed is popped and removed from R (885, 920, 969).
  In T the moved set is exactly Z (936-951). The recursion's argument is the T piece's own Z. Hence at depth 0, X ∩ R = ∅ and
  X ∪ R = G' = CurG (1014) throughout. this->G does not change during search_rec (it changes only at 1035), so no tangle is
  deleted or created inside a best_vertices call (sptl is not called there).
- extractTangles 211-471 records tpr := pr(startvertex) (461) for every nontrivial SCC reachable from top.

## 2. Claim (1): KT, KT(G'), ¬KT(R_end) — SIGN WITH GAPS (G1)
- T0 (used by (1), (4), (5)): at a depth-0 P piece, every v ∈ R has ¬attracts(p, v, X, R). This is §1, the scan read to
  completion. So a p-vertex of R has no edge into X, and an opponent vertex of R with an edge into X also has one into R.
  With X ∪ R = G' (G' a game, DTL-proof §1.4), every vertex of R keeps an R-successor, so H = G[R] is a game.
  D ∩ R is a p-dominion of H: σ(v) ∈ D for a p-vertex, and σ(v) ∉ X, so σ(v) ∈ D ∩ R; opponent vertices of D keep all
  their G'-edges in D. Checked.
- KT(G'): X = ∅, so A_c = ∅. W1 is a least-maximum p-dominion of H = G' inside D. c1 has p's parity. This is Zielonka's step,
  re-derived:
  - If c1 had the opponent's parity, let A_o be the opponent's attractor to W1 ∩ pr^{-1}(c1) inside W1.
  - A_o ≠ W1, since otherwise the opponent forces c1 infinitely often inside the opponent-closed W1.
  - W1 \ A_o is an opponent-trap. p wins all of it by the usual composition argument, and its maximum is < c1. This
    contradicts minimality.
  - W1 ⊆ S_{c1}. σ1 stays in W1, W1 is opponent-closed (it is a dominion), and nothing is deleted inside W1. So
    W1 ⊆ W_p(F_{c1}). Checked.
- ¬KT(R_end): best_vertices returns 0 (668) iff R has no p-priority vertex. So every infinite play of F_c on R_end is won by
  the opponent, and dead ends are lost for p. Hence W_p(F_c) = ∅ for all c. Checked.
- G1 (wording). The definition of A_c says an opponent vertex enters "only if ALL its edges lie in X ∪ A_c". If this counts
  whole-game edges, the claim changes. An opponent vertex of G' can have an edge into a solved p-region outside G'
  (DTL-proof §1.4: such edges exist only from the loser's side). That edge would block attraction in A_c. Then P-KT step (4)
  ("at least one edge in U, else v ∈ A") fails at such a vertex: it becomes a dead end of F_c inside U.
  - Fix: read "edges" as edges of the game G' (= X ∪ R at depth 0), as dtl.cpp does: every test is R-relative, and 333 is
    G-relative.
  - With that reading everything below holds. I sign with that reading.

## 3. Claim (2): Lemma NT-f — SIGN WITH GAPS (G2)
Setting: a best_vertices call returns −1 after rounds 1..f, and t is the first tangle accepted by round f's region loop,
at the pop of e in the region of τ. For a round r and a top σ, let A^r(σ) := the union of round r's regions of tops with
index ≥ index(σ). By O1 these tops have priority ≥ pr(σ).
- (A) Checked, by induction over round f's additions before t. All of them come from attractVertices. Note that
  V_f ⊆ V_r, and R is the same in all rounds.
  - Top case. τ_x ∈ V_r is either inside Z at index(τ_x) in round r (692), so in a higher region, or it gets its own region.
  - p-vertex x attracted at the pop of v. Then v is in x's region and was added earlier, so v ∈ A^r(τ_x) by induction, in
    a region whose top τ' has pr(τ') ≥ pr(τ_x) ≥ pr(x). At v's round-r pop (699-700), x is in CurZ, or already consumed in
    a region of index ≥ index(τ'), or still in CurR and then added (no escape test for p).
  - Opponent vertex x. At its round-f addition, 80 requires no edge into CurR \ CurZ. So each R-successor of x is in CurZ
    or already popped in round f: added before x, hence in A^r(τ_y) ⊆ A^r(τ_x). In round r, at the pop of the last of these
    successors, CurR[y*] is already false (699 precedes 700). So x has no escape and is added, unless it is already taken.
  - A self-loop on x is a successor in CurR \ CurZ, which consistently blocks x in both rounds.
- (B) Checked. At acceptance each escape in R is in CurZ or not in CurR (155-156). Either way it was added in round f before
  t, so by (A) it is in Z^r for all r.
- (C) Checked. After the acceptance t ⊆ Z_f. A p-owned v ∈ t has its stored strategy edge inside t. That is a real edge
  (68-73 and 268-285).
  - An opponent-owned v ∈ t has an edge into t: t is a nontrivial SCC, or a self-loop (315-317).
  - Every edge of v that leaves t into this->G at creation is in tout(t). Since G only shrinks, every R-edge of v is in
    t ∪ (escapes in R) ⊆ Z_f.
  - So attracts(p, v, Z_f, R) holds and v is no candidate at 714. Every vertex of V_f is a candidate, so t ∩ V_f = ∅.
- (D) Checked, given G2.
  - Let q be the maximum priority of t, and m_1 ∈ M_q the first pruned, at round r_1 < f by (C).
  - At r_1, M_q ⊆ V_{r_1} ⊆ Z^{r_1}: tops are in the union.
  - q = 0: t ⊆ V_{r_1}, and m_1 attracts into Z^{r_1} by the argument of (C). So m_1 is not a candidate at r_1.
  - (D1) Checked. t existed and was alive throughout the call (§1). At level q−1 of round r_1, Z ⊇ Z^{r_1} ∋ e. Here e ∈ R,
    as it was popped from CurZ ⊆ R in round f. e is pushed at 724 and popped at 728, and t ∈ tin[e] is evaluated at 730 with
    G = R.
  - (D2) Checked. In 132-145, every vertex of t is in this->G and in R. The priority-q ones are in Z, the rest have priority
    ≤ q−1. In 153-157 the escapes in R are in Z and those outside R are skipped. So t is added, or the "nothing new" exit
    fires with t ⊆ Z.
  - m_1 then has priority q > q−1 and is reached by 734-740: the scan stops only at priority ≤ q−1, and an earlier rescue
    also suffices. It attracts, so it is rescued. Contradiction.
- G2. (D) takes q := tpr(t) and uses two facts: that q is the maximum priority of t, and that M_q ≠ ∅. tpr is
  pr(startvertex) (461), set for every SCC reachable from top. A non-top SCC would carry a tpr that need not occur in it,
  and M_q could be empty. This is excluded by DTL-proof Lemma 1.5a (one SCC reachable from top in an sptl region, namely
  top's).
  - I re-derived 1.5a. Every region vertex reaches top in the restricted graph, by induction on push order:
    - a vertex-pushed vertex points to an earlier one;
    - a vertex pushed by a firing tangle t' follows t''s stored edges until it meets an older vertex, or the opponent vertex
      of t' whose edge to the popped escape e caused the firing.
  - So t contains its top, tpr(t) = max pr(t), and this is attained (all region vertices have priority ≤ pr(top), 74 and
    140).
  - Probe: tpr = max and top ∈ t at every tangle creation, 48,285 tangles (§7).
  - G2 is a citation to a lemma outside this packet (DTL-proof 1.5a, which I have not seen refereed); I verified it as above.

## 4. Claim (3): FM and WM — SIGN
By NT-f, every addition of round f is a vertex-rule addition, so (A) covers all of Z_f: Z_f ⊆ A^r(·) ⊆ Z^r for every r.
WM: the rescue loop of round r starts on the bitset Z = Z^r and only adds (724-731), so Z^r ⊆ A^r_t for every t. Checked.

## 5. Claim (4): the (YZ) reading and (YZ) ⇐ (ACYC) — SIGN WITH GAPS (G3)
- YZ-read. Checked step by step. Dom runs with (R, Z = X, G = R) and the final loop with (CurR, CurZ, CurR). Both start from
  the same R, use V_f, and visit the same tops in the same order with the same skip test (X[top] vs Z[top]).
  - Induction invariant: R_Dom = CurR, and X ∩ R_Dom = CurZ ∩ CurR (= pushed, unpopped vertices of the current top).
    X \ R_Dom = old X ∪ earlier parts ∪ the popped current part, and the last of these equals CurZ \ CurR.
  - So 71/74/80 give identical answers in both.
  - In attractTangle the only difference is a vertex w ∈ old X ∪ earlier parts: Dom takes "in Z, skip" (136-137), the loop
    "not in R, reject" (138-139). Escapes in old X or in earlier parts are skipped by both.
  - Deletion (134) only ever returns false, and a tangle with a vertex outside this->G is accepted by neither.
  - str differs, and no set test reads str.
  - Sharpened form: before the first straddling acceptance, any Dom acceptance would be a round-f region-loop acceptance,
    which NT-f excludes. So without a straddling acceptance Y_0 = Z_f. Checked.
- (YZ) ⇐ (ACYC). Checked, with G3. Induction over the tops; Z_prev denotes the union of earlier parts, equal in both runs by
  the induction. Fix a top τ_j with loop region L and Dom part P_j.
  - L ⊆ P_j: Dom's rules contain the loop's (same vertex rules, and a weaker tangle membership test), and P_j is closed under
    them (each test is re-made at the pop of the last relevant vertex).
  - P_j ⊆ L, by induction on Dom's additions: a vertex rule or non-straddling tangle justified inside L stays in L.
  - For a straddling t_X with new part N_X, let N' := N_X \ L and take a sink v of H_{t_X} restricted to N' (one exists by
    (ACYC)).
    - p-owned v: its tangle successor is in L ∪ N'. It is not in old X (T0), and not in Z_prev (else v would have been
      attracted at that vertex's pop, the earlier top having priority ≥ pr(τ_j) ≥ pr(v), 140). Since v is a sink, the
      successor is in L, and the loop's vertex rule puts v in L.
    - Opponent v: its R-edges lie in Z_prev ∪ L ∪ N'. Those leaving t_X are escapes, in R ∩ (Z_prev ∪ P_j-so-far), and
      edges into old X are outside R. Since v is a sink, its R-edges lie in Z_prev ∪ L.
  - G3: the loop's vertex rule needs v to have an edge into L, because attractVertices is triggered only at pops in the
    current region (69). STEP5 §6.1 and 18k (iii) skip this ("reverse topological order").
  - Closure: if all of v's R-edges went into Z_prev, then at the round-f pop of the last of them v had no escape and
    pr(v) ≤ pr(τ_j) ≤ that top's priority. So v ∈ Z_prev, contradicting v ∈ R \ Z_prev. Hence v has an edge into L, and
    v ∈ L.
  - So N' = ∅, P_j = L, and Y_0 = Z_f.
  - The induction uses only the hypothesis of (ACYC) on each straddling acceptance. Checked.

## 6. Claim (5): Lemma P-KT given (YZ) — SIGN WITH GAPS (G4, G1)
- (1) Checked. After level t of round r's rescue loop the set is closed under vertex attraction of R-vertices of priority
  ≤ t. Members are pushed once at 724, and later additions are pushed when added, so every member is popped at level t. A
  p-vertex is caught at the pop of its successor, and an opponent vertex at the pop of the last of its R-successors.
  - A'''s rules are instances of these: a p-vertex of R has no X-edge (T0), and an opponent vertex has ≥ 1 R-edge. With
    Z_f ⊆ A^r_{c1−1} (claim 3) this gives A'' ⊆ A^r_{c1−1} for every r.
- (2) Checked. Take x of priority c1, p's parity, x ∈ R ⊆ V_1. It is pruned at some round r(x) ≤ f, since V is empty after
  round f. x attracts into Z_f ∪ A'' ⊆ A^{r(x)}_{c1−1}. The check at level c1−1 (734-740, priority c1 > c1−1) rescues it.
  Contradiction.
- (3) and (4) Checked. They use only that W1 is closed in H, σ1, (2), and the definition of F_{c1}. Opponent edges into
  A ∪ X ∪ Z leave Q_{c1} and are deleted.
- G4 (c1 = 0, p = Even). Then A'' = ∅ and there is no level c1−1 = −1. The argument must read "A^r_{−1} := Z^r, and
  rescued := not a candidate".
  - (2): x has priority 0, and its witnesses lie in X ∪ Z_f with Z_f ⊆ Z^{r(x)} (FM). So x attracts into Z^{r(x)} and is not
    a candidate at 714.
  - (3): the same for w.
  - Closed.
- G1 applies here as in §2.

## 7. Probes (pinned code, assertions only; docs/referee-2/R2-STEP5/)
dtl_probe.patch is the full diff of my instrumented copy of dtl.cpp @ 8fbf0a7: counters only, the algorithm unchanged. It
checks the following.
- At every −1 return (any depth): round f's region loop accepted no tangle (NT-f), and Z_f ⊆ Z^r for all r < f (FM).
- At every P piece (any depth): Y_0 = Z_f (YZ). Every Dom acceptance is classified: straddling means it uses a vertex of X
  outside the current part. Each one is checked for a cycle of H_{t_X} inside its new part (ACYC).
- At every tangle creation: tpr = max priority, and t ∋ top (G2).
- Order data: R2_REV=1 reverses every ins(v) iteration (O2); relabel.py permutes ids (O1 ties; it changed the counters in
  170 of 508 file/order pairs).

| set | runs | −1 calls | P pieces (depth 0) | NT-f / FM / YZ viol. | Dom acceptances (straddling / not) | ACYC viol. | tpr≠max / top∉t |
|---|---|---|---|---|---|---|---|
| corpus: 254 .pg under experiments/, 2 in-orders × 4 labellings | 2,026 | 70,276 | 37,968 (27,904) | 0 / 0 / 0 | 4 / 0 | 0 | 0 / 0 (28,384) |
| random games and unions with cross edges (gen.py, seeds 1-3000) × 2 in-orders × 2 labellings | 12,000 | 103,229 | 67,160 (65,742) | 0 / 0 / 0 | 0 / 0 | 0 | 0 / 0 (19,901) |
| climb from strfam_S5_n46.pg (climb.py, seeds 1-6 × 1500 mutants × 2 in-orders) | 18,000 | — | — | 0 | firings kept: last accepted states score 20, 6, 4, 24, 1, 6 | 0 | 0 |

- The one corpus firing is L-ALG's: strfam_S5_n46.pg with reversed in-lists ("stable"), 1 straddling acceptance, ACYC holds,
  Y_0 = Z_f. I reproduced it independently.
- The climbs produce many straddling firings, and never a cyclic new part or a YZ failure. The climb log keeps only
  violations and final scores, so I give no total firing count.
- DATA only; it supports and does not replace §2-§6.

## 8. Remaining hypotheses (for GAPS.md)
- (ACYC), STEP5 §6.1: open. It is the only hypothesis between the signed chain and "P-KT at every depth-0 P piece with D ∩ R ≠ ∅".
- G1: the KT definitions must say "edges of G'". This is a wording fix in GAP-C 18g and STEP5 §2.
- G2: NT-f (D) rests on DTL-proof Lemma 1.5a (tpr(t) = max pr(t) ∈ pr(t)). I re-derived it; it should be cited in 18k (D).
- G3: the trigger step of (YZ) ⇐ (ACYC) (an opponent sink of N' has an edge into the current region). Closed in §5; it should
  be added to 18k / STEP5 §6.1.
- G4: the case c1 = 0 in P-KT. Closed in §6; it should be added to 18h.
- O1 (index order non-decreasing in priority) is an Oink fact of the order datum, used by (A), (D) and P-KT (2).
- None of this is Lean-checked.

## 9. Comparison with the first referee (read after ce37984 was pushed; origin/claude/referee 8c2d012, docs/referee/R-STEP5.md)
- The two reports were written independently and give the same verdict on every claim: no REJECT, (3) SIGN, (4) and (5)
  SIGN WITH GAPS. Both find the same four points, and both close them the same way:
  - Their F2.1 = my G2: NT-f (D) needs DTL-proof Lemma 1.5a, i.e. top ∈ t and tpr = max pr(t). Both of us re-derived it
    and both checked it on data (theirs: 6,815 tangles; mine: 48,285).
  - Their G4.2 = my G3: a new opponent vertex whose R-edges all go into earlier parts would have been taken there.
  - Their G5.1 = my G4: the case c1 = 0, read as A^r_{−1} := Z^r, with candidacy at 714.
  - Their claim-(1) wording note = my G1: "all its edges" means edges of G'. They label it a note and SIGN (1), (2). I
    label it a gap and SIGN WITH GAPS. For (2) the difference is only in labelling (a cited lemma vs a gap). There is no
    disagreement on substance.
- They found one point I did not list separately. Their G4.1 asks for both inclusions of (YZ) ⇐ (ACYC) (iii) to be written
  out, with regions as least fixed points and tangles retried at escape pops. My §5 proves the same two inclusions inline,
  so I agree it belongs in the author's text.
- Their data are independent of mine: they used a Python reimplementation (dtl_pyref / dtl_step5) on the corpus in both
  orders; I used an instrumented copy of the pinned C++. Both report 0 NT-f / FM / YZ failures, and both found only the
  strfam_S5_n46 stable-order straddle.
- Union of the gap lists, for GAPS.md:
  - Lemma 1.5a citation (F2.1/G2).
  - Least-fixed-point write-up of (iii) (G4.1).
  - Trigger case (G4.2/G3).
  - c1 = 0 (G5.1/G4).
  - Edges of G' (wording/G1).
  - (ACYC) open.
