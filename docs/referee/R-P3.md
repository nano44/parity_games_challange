# Referee report R-P3: packet 3 (K5', (α) restated and K6, Lemma O-P, the GAP-A first step)

Referee: REFEREE, running on Opus 5.5 under owner ruling D12 (Lead reading L33). Packet: the Lead's message of 10:44Z.
Pin: trunk 6e0082f, docs/alg/GAP-C.md §18l, §18n, §18p and DTL-proof.md §2.3 K5/K6. Code: tools/oink/src/src/solvers/
dtl.cpp @ 8fbf0a7 ("N" = that line). Written 10:45Z-10:48Z (date -u). I did not read docs/referee-2/R2-P3.md before
pushing this. The code facts C1-C6 of docs/referee/R-STEP5.md §0 are used without repeating them.

## Verdict
| item | verdict (Opus 5.5, D12) | lines checked |
|---|---|---|
| (a) K5' (GAP-C §18n "(C)") | REVISED in §C: my SIGN is WITHDRAWN; (iii') in the Up(Str) form is REJECTED (REFEREE-2's configuration). K5'' with Dep(Str): SIGN | 65-101, 110-185, 198-202, 481-526, 690-741 |
| (b) (α) restated with Up(Str); K6's closed case read with K5' | REVISED in §C: (α) with Up(Str) REJECTED (withdrawn); (α) with Dep(Str), ⇒ direction: SIGN; REFEREE-2's ⇔ form: SIGN WITH GAPS (G-α1). K6 closed case: SIGN WITH GAPS: G-b1 (wording, closed); remark R-b (W is harmless, closed) | 317, 385-424, 481-546, 862-991 |
| (c) Lemma O-P, given (YZ) (§18l) | SIGN (conditional on (YZ), as stated) | 110-185, 200-201, 643-776, 962-991 |
| (d) GAP-A angle, first step (§18p) | SIGN, for round r only, as stated | 65-101, 110-185, 198-202, 712-760 |

No REJECT in my first pass; after the comparison (§C) I withdraw (a) and the (α) part of (b) in the Up(Str) form.

## (a) K5' — SIGN WITH GAPS (Opus 5.5, D12)
Setting (K5): V* stable at X = ∅ (K6: any X, forgiven). Reg is the union of the final round's regions, which equal the first
sptl pass's regions (R-PROVED2 §c). τ_k is the lowest top with a region, Z_k its region, and A_< the rescue set after
level pr(τ_k) − 1.
- R-a (my reading). Z_k ⊆ Reg, so "A_< \ Reg ⊆ Z_k ∪ Up(Str)" says A_< \ Reg ⊆ Up(Str); the "Z_k ∪" is redundant. Under
  the other reading (Reg = the higher regions only) the statement is also true, by the same proof. Str should be read
  inside A_< (the vertices pushed into A_< by rule (T) for a straddling tangle). Up(Str) is read existentially: SOME
  ψ-play from the vertex reaches Str before Z_k.
- (i') Correct. Let y ∈ A_< \ Reg be p-owned with an edge to w in a higher region Z_σ. Then pr(y) ≤ level < pr(τ_k) ≤ pr(σ)
  by sortedness (C1). y is unconsumed in the whole region loop, since it is in no region. So at w's pop, 74-90 attracts y
  into Z_σ, which contradicts y ∉ Reg.
- (iii'), by induction over the attraction order of A_< \ Reg.
  - p-vertex y. Its rescue successor ψ(y) is not in Z_k: at ψ(y)'s pop y would have joined Z_k, since pr(y) < pr(τ_k) and
    y is unconsumed. ψ(y) is not in a higher region, by (i'). No region lies below Z_k. So ψ(y) ∈ A_< \ Reg is earlier,
    and y ∈ Up(Str) by the induction hypothesis.
  - Opponent vertex y. Its R-successors lie in A at its attraction (80, Gx = R). Suppose none of them is in A_< \ Reg.
    Then they all lie in Z_k ∪ higher regions. If one is in Z_k, y joins Z_k at the pop of the last of them in Z_k (the
    others are consumed). If all are in higher regions, y joins the last such region. Either way y ∈ Reg, a
    contradiction. So some successor is in Up(Str), and y ∈ Up(Str).
  - Vertex pushed by a fired tangle t'. If t' straddles (a vertex in a higher region), the vertex is in Str. Otherwise
    the text's case "escapes in Z_k ∪ Up(Str)" leaves out two sub-cases:
    - G-a1 (closed). All of t''s in-R escapes lie in higher regions. Then at the pop of the last of them, in the latest
      such region Z_σ, t' is alive, its vertices are unconsumed with priority ≤ level < pr(τ_k) ≤ pr(σ), and its other
      escapes are consumed or outside R. So 110-185 accepts t' into Z_σ, which contradicts its vertices being outside Reg.
      This is the K2 argument.
    - G-a2 (closed). All in-R escapes lie in Z_k ∪ higher regions, with at least one in Z_k. Then t' fires into Z_k at the
      pop of its last escape in Z_k (200-201), with the same priority bound. Contradiction.
    So a non-straddling t' has an escape in A_< \ Reg ⊆ Up(Str) (induction hypothesis). By the strong connectivity of t'
    under its strategy, an opponent vertex of t' reaches that escape on some ψ-play, so the pushed vertices are in
    Up(Str).
- Consequence. Correct.
  - p-owned τ_k: it is a non-candidate or is rescued at a level < pr(τ_k) (737), so ψ(τ_k) ∈ Reg ∪ A_<. A successor in a
    higher region would have absorbed τ_k (it would have no region of its own). A successor in Z_k makes the region
    closed (str[τ_k] ≠ −1, 73, 515). So Z_k is open only if ψ(τ_k) ∈ A_< \ Reg ⊆ Up(Str).
  - Opponent-owned τ_k: all its R-successors lie in Reg ∪ A_<, and it is open only if one of them lies in A_< \ Reg ⊆
    Up(Str).
- I re-checked this on k5.pg (R-PROVED2 §C3). There A_< = {a} (pr(τ_k) = 0, so no level below), A_< \ Reg = ∅, and Z_k is
  closed.

## (b) (α) restated; K6's closed case with K5'
(α), restated, is the contrapositive of K5' Consequence: "Z_k is open ⇒ τ_k's ψ-successor (or some successor, for an
opponent τ_k) lies in Up(Str) \ Z_k". As a definition of the failing shape it is exact. SIGN (Opus 5.5, D12).
K6's closed case: SIGN WITH GAPS (Opus 5.5, D12). The closed case uses neither K5 (i) nor (iii), only closedness:
- by SCC1, the one reachable SCC is τ_k's;
- it is nontrivial when closed (317), with K5 (ii) for an opponent τ_k;
- its escapes are not in L_k, a later region, R_rem or a higher region (B-thr (ii) and K2), so they lie outside R;
- the duplicate check (385-424) gives "new, dominion, or (β')".
- G-b1 (wording, closed). K6 says the (β') escapes "all lie in X". At depth ≥ 1 "outside R" also means outside the
  search_rec context (in an ancestor's X), and solved escapes are excluded by O0. Read "(β') a stored tangle none of
  whose escapes lies in R".
- R-b (closed, not stated in K6). Extraction also needs !W[τ_k] (528). This holds at the first pass of any piece. W[τ] is
  set only for a top τ of the current stable set (529), and the piece's Dom then puts τ into X (879-880). By the
  context-chain argument (R-PROVED2 §C5), τ is in no later context of the search. So "productive" is not blocked by W.
- K6's open case is "(α)", now read as restated. Its "Orphan analysis" and "Route" paragraphs are SKETCHES and are not
  signed here.

## (c) Lemma O-P (given (YZ)) — SIGN (Opus 5.5, D12)
Reading: "creates an orphan" means that after Dom(prevV, R) at a depth-0 P piece, some alive stored p-tangle t ⊆ R \ Y_0
has no escape in R \ Y_0, while before the piece it had an escape in R. Step by step:
- The removed in-R escapes lie in Y_0 = Z_f by (YZ), and Z_f ⊆ Z^r for every round r by FM (signed, R-STEP5 claim 3).
- No vertex of t lies in V_f, because every top of Dom goes into Y_0 (963-964). So every priority-q vertex of t
  (q = tpr(t) = max pr(t), of p's parity, by 1.5a) is in V_1 (662-667) and is pruned before round f. Let m_1 be one
  pruned first, at round r_1. All priority-q vertices of t are in V_{r_1} ⊆ Z^{r_1} (692).
- q = 0: t ⊆ Z^{r_1}, its in-R escapes are in Z^{r_1}, so m_1 attracts into Z^{r_1} (tangle successor, or all R-edges in
  t ∪ escapes) and is not a candidate (714).
- q ≥ 1: as NT-f (D1)/(D2), signed in R-STEP5. An escape e ∈ Z^{r_1} is pushed at level q−1 (724) and popped, and
  attractTangle(t) is evaluated (200-201). t is alive: deletion is permanent and t is alive now. t existed: no tangle is
  created inside best_vertices. Its vertices are in the set or have priority ≤ q−1, and its in-R escapes are in the set.
  So t ⊆ the set, m_1 is rescued (737-738), and it is not pruned at r_1. Contradiction.
Correct, conditional on (YZ) as stated, which follows from (ACYC). Without (YZ), an escape in Y_0 \ Z_f need not be in any
Z^r, so the hypothesis is used exactly there. The open cases named in the text (T pieces, barren stable pieces) are not
claimed.

## (d) The GAP-A angle, first step — SIGN (Opus 5.5, D12)
Reading: s → s+1 consecutive searches of one phase; e is the first differing tattr of the reduced log (FDL, signed with
G-h1 closed); e is the level-t_e attractor (724-731) of round r of a best_vertices call of the root call (depth 0).
- The candidate list of round r is the same in both searches. It is computed at 712-715 from V_r and the region union
  Z^r. Both are produced before e (the region loop at 690-706, earlier rounds and earlier pieces), and attracts reads
  only (V_r, Z^r, R). The pruning checks at levels < t_e (734-740) also read sets that are equal before e.
- The rescue sets for t ≥ t_e are monotone. At t_e: same input and a larger output (FDL (ii)). At t > t_e: the level-t
  call starts from the previous level's set (724) with R fixed, Gx = R, max_prio = t and no consumption (727-731 never
  clear R). Every member is pushed and popped, so the level-t output is the closure of its input under the level-t vertex
  rule and tangle rule. Each rule is monotone in the input set and in T (DTL-proof 1.2b). T_{s+1} contains every tangle
  s had at that point, since T only grows inside a phase and G is fixed. A zombie or deleted tangle answers false in both
  searches. By induction over t, rescue_t(s+1) ⊇ rescue_t(s).
- V_{r+1}(s+1) ⊇ V_{r+1}(s). A candidate u is cleared at the first level t < pr(u) with attracts(p, u, rescue_t, R)
  (737-738). For t < t_e this is identical in both. For t ≥ t_e, attracts is monotone in the set (40-57, both owners). So
  every candidate s clears is cleared by s+1, and s+1 drops a subset of what s drops at round r (749-760).
- Scope: round r only, as the text says. The step to rounds r' > r is open (the author's DV-MONO gap), and "DV never
  falls" is DATA. Nothing about later rounds is signed here.

## Open points after this report
1. (YZ)/(ACYC): Lemma O-P is conditional on (YZ).
2. The (α) shape itself: K6's open case, the "Orphan analysis" and the "Route" are SKETCH.
3. GAP-A: the step from round r to rounds r' > r in the root call (DV-MONO for the actual code) is open.

## Findings for the author (L-ALG), one line each
- G-a1/G-a2: K5' (iii') proof: add the two non-straddling tangle sub-cases (all in-R escapes in higher regions → fires
  there, K2; escapes in Z_k ∪ higher with one in Z_k → fires into Z_k).
- R-a: K5' (iii'): "Z_k ∪" is redundant (Z_k ⊆ Reg); Str should be read inside A_<.
- G-b1: K6 (β'): "escapes all in X" → "no escape in R" (depth ≥ 1; solved escapes excluded by O0).
- R-b: K6: note that W[τ_k] cannot block extraction at the first pass of a piece (tops go to X by Dom; context chain).

## §C. Comparison with REFEREE-2 (docs/referee-2/R2-P3.md @ d555ebf), added 10:57Z (date -u), Lead request 10:55Z
I read R2-P3 after my report was pushed (e3f3256).

### C1. K5' (iii'): REFEREE-2 is right; my G-a1/G-a2 argument does NOT handle its configuration, and I withdraw my SIGN
Where my step fails. My cases G-a1/G-a2 are correct for what they say: a non-straddling t' whose in-R escapes all lie in
Reg fires into a region. So t' has an escape e ∈ A_< \ Reg ⊆ Up(Str). The wrong step is my last sentence: "by strong
connectivity of t' under its strategy, an opponent vertex of t' reaches that escape on some ψ-play".
- t' is strongly connected only under its STORED strategy.
- An old vertex u ∈ t' ∩ Z_k keeps its own region strategy, because attractTangle skips vertices already in the set (169).
  So ψ(u) ≠ the stored strategy.
- A ψ-play from a new vertex x can then be forced through u into Z_k without ever reaching e.
REFEREE-2's configuration, re-checked by me:
- t' = {x, y, u, o}, stored strategies x → y and u → o; y (opponent) → x, u; o (opponent) → u, y, e; u ∈ Z_k by its own
  vertex rule.
- During Z_k's computation:
  - y is blocked by its edge to the unconsumed x (80);
  - x's only edge goes to y;
  - o is blocked by e;
  - t' is never tried, because its only escape e ∉ Z_k (attractTangles runs only at escape pops, 200-201).
- In the rescue loop, e is in the set (with e ∈ Str or in Up(Str)) and is popped. attractTangle(t') skips u (in Z) and
  pushes x, y, o (110-185).
- ψ-plays from x go x → y → {x, u}, and u leads into Z_k under its region strategy. So x, y ∉ Up(Str), and (iii') fails.
- With τ_k p-owned and its single edge τ_k → x, Z_k is open and τ_k's ψ-successor x ∉ Up(Str), so the Consequence fails
  too.
- Neither of us built an instance. The step is still refuted as a proof step.
Final verdict (a): K5' (iii') and its Consequence in the Up(Str) form: REJECT (Opus 5.5, D12), failing step = "a vertex
pushed by a non-straddling tangle lies in Up(Str)", configuration as above. (i') and (ii) remain signed.

### C2. K5'' with Dep(Str): SIGN (Opus 5.5, D12)
Dep(Str) is the least D ⊇ Str ∩ A_< closed under "v ∈ A_< \ Reg is in D when one of its rescue witnesses is in D". The
witnesses are:
- for a vertex-rule p-vertex, the vertex it was attracted to;
- for a vertex-rule opponent vertex, its R-successors;
- for a vertex pushed by a non-straddling t', the escapes of t' and the vertices of t' already in A_< \ Reg.
Induction over the rescue order:
- p-vertex. Its witness is not in Z_k (otherwise the vertex joins Z_k) and not in a higher region (i'), so it is in
  A_< \ Reg ⊆ Dep by the induction hypothesis.
- Opponent vertex. If all its R-successors were in Reg, it would have joined Z_k or the last higher region.
- Non-straddling t'. Suppose no witness lies in A_< \ Reg. Then:
  - it has an in-R escape, since it fired at the pop of an escape in the rescue set (200-201);
  - if all in-R escapes lie in higher regions, it fires into the last of them. Its vertices, including old ones like u,
    are unconsumed when that region is computed, with priority < pr(τ_k);
  - otherwise it fires into Z_k at the pop of its last escape in Z_k. Its vertices are in CurZ or unconsumed.
  Either way its new vertices are in Reg, a contradiction.
- Straddling tangles at levels < pr(τ_k) put their vertices in Str.
Consequence ("Z_k open ⇒ τ_k has a successor in A_< \ Reg ⊆ Dep(Str), so Str ≠ ∅"):
- p-owned τ_k. Open means no edge into Z_k (73, 515). An edge into a higher region would have absorbed τ_k. So τ_k is a
  candidate, rescued at a level < pr(τ_k) (737) through a successor in A_< \ Reg.
- Opponent τ_k. Open means an R-successor in unconsumed R after Z_k (519-525). That successor is not in Reg, so τ_k is a
  candidate rescued with all its R-successors in A_<.

### C3. (α) with Dep(Str): the ⇒ direction SIGN; REFEREE-2's "⇔" form SIGN WITH GAPS (Opus 5.5, D12)
- (α) with Up(Str) (§18n): REJECTED, withdrawn, with the same configuration as C1.
- REFEREE-2's repaired statement is "Z_k is open ⇔ τ_k has a successor in A_< \ Reg, and then A_< \ Reg ⊆ Dep(Str) ≠ ∅".
  The ⇒ direction is C2's Consequence, and it is all that K6 and the S-step reduction use.
- G-α1 (gap in the ⇐ direction; wording). For a p-owned τ_k, a successor in A_< \ Reg does not make Z_k open if τ_k also
  has an edge into Z_k: str[τ_k] is set at that vertex's pop (73), and the region is closed (515). REFEREE-2's converse
  covers only the opponent-owned τ_k.
  Fix: for p-owned τ_k read "τ_k has no successor in Z_k (hence one in A_< \ Reg)". For opponent-owned τ_k the statement
  is correct as written.

### C4. Agreed items
(c) O-P: SIGN. (d) GAP-A first step (round r only): SIGN. K6's closed case: SIGN. Both of us give the same wording fix:
"(β') escapes outside R", i.e. in G' \ R at depth > 0, not "in X". My R-b remark (W cannot block extraction at a piece's
first pass) is not in R2-P3, and it stands.

### Final verdicts after the comparison
(a): K5' (iii')/Consequence with Up(Str) REJECT; K5'' with Dep(Str) SIGN.
(b): (α) with Up(Str) REJECT; (α) with Dep(Str): ⇒ SIGN, ⇔ SIGN WITH GAPS (G-α1); K6 closed case SIGN WITH GAPS (G-b1
wording, closed; R-b).
My error: in G-a1/G-a2 I assumed that ψ follows the tangle strategy on every vertex of a fired tangle. It does not on
vertices that were already in the set (169).
