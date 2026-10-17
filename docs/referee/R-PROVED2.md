# Referee report R-PROVED2: unrefereed PROVED readings of GAP-C and GAP-A, items (a)-(k)

Referee: REFEREE, running on Opus 5.5 under owner ruling D12 (Lead reading L33). Packet: the Lead's message of 09:41Z
(2026-10-17). Pin: trunk 43d63b0; code tools/oink/src/src/solvers/dtl.cpp @ 8fbf0a7 ("N" = that line). Started 09:33Z,
written 09:44Z-10:05Z by date -u. docs/referee-2/ was not read. Every step below was checked by me against the code; the
code facts C1-C6 of docs/referee/R-STEP5.md §0 are used without repeating them (sorted indices; best_vertices data flow;
attractTangle; attractVertices; search_rec moves exactly what it takes from R into X; tangle creation, CHECK_UNIQUE on).
Machine checks (mine): docs/referee/scratch/bthr_probe.py, docs/referee/scratch/fdl_random.py.

## Verdict
| item | verdict (Opus 5.5, D12) | lines checked |
|---|---|---|
| (a) Lemma SCC1 (GAP-C §3) | SIGN | 65-101, 110-185, 198-202, 211-305, 315-317, 477-546 |
| (b) Lemma B-thr (§3, corrected form) | SIGN WITH GAPS, ALL CLOSED (final, §C5): G-b1, G-b2 closed here; REFEREE-2's G-b1 closed by R2-PROVED2 §13.2, checked by me; finding F-b3 ((b) vacuous; agreed by REFEREE-2) | 110-185, 327-339, 385-424, 477-546, 862-991, 1023-1039 |
| (c) Theorem A (§13), root call stable, given no (α) | SIGN; it rests on DTL-proof.md §2.3 K4, K5(ii), which I re-checked in outline (§c) | 643-776, 477-546, 1014-1016 |
| (d) Lemmas O0 and O1 (§6) | O0: SIGN. O1: SIGN | O0: 65-101, 110-185, 1023-1039. O1: 110-185, 878-890, 962-991 |
| (e) Lemma OPP-EXIT (§11) | SIGN WITH GAPS: G-e1, G-e2 (both closed here) | 65-101, 110-185, 211-305, 512-526 |
| (f) Lemma K0 (§18b) | not covered by R-STEP5 claim (1), which was KT0 (§18g). Checked here: SIGN | 643-668, 850-854, 1014-1015 |
| (g) phases ≤ D + 2 (C5-DTL.md lines 141-142) | SIGN | 1023-1039, 1068, 1103-1121; solvers.cpp 77; dtl.hpp 33 |
| (h) First-Difference Lemma (GAP-A-M §21d) | SIGN WITH GAPS: G-h1. REVISED in §C: G-h1 is CLOSED by REFEREE-2's alignment argument, which I checked | 862-875, 477-546, 528-529, 1016, 385-424 |
| (i) Lemma DV*-MONO (§21h) | SIGN (with reading R-i of the INF case) | abstract definition (no code) |
| (j) per-context LRN budget ≤ n(n + 1) (§21j) | SIGN | as (i) |
| (k) (SPP) ⇒ searches ≤ n(n + 2) and O(n^10 (m + n²)), against TARGET.md §3 | SIGN (conditional on (SPP) for every ω) | DTL-proof.md §3 (b)-(e), Lemma W; 528-529, 539, 1016 |

No REJECT. After the comparison with REFEREE-2 (§C, §C5) no gap of packet 2 is open.

## (a) Lemma SCC1 — SIGN (Opus 5.5, D12)
Induction over the join order of Z_τ (sptl, 481-500, consumed set R, threshold pr(τ)).
- A p-vertex u joined by the vertex rule gets str[u] = v, v already popped (89). Later writes to str[u] are only 73, which
  requires str == −1, and 171, which requires u ∉ Z. A p-vertex of Z can have str = −1 only if it is the top (485), so u's
  edge is stable.
- An opponent vertex u joined at v's pop has no successor in R \ Z (80, Gx = R). So every successor of u inside Z_τ joined
  before it (a successor joining later would have been unconsumed, outside Z, when u joined). u → v is one such edge.
- A tangle t2 fired at the pop of an escape e (attractTangles only from popped vertices, 200-201). Some opponent vertex of
  t2 has e as a successor (escapes are opponent successors, 329-337). Inside t2 the stored strategies (171) together with
  all opponent edges make t2 strongly connected, and all of t2 lies in Z_τ. So from any newly added vertex a path inside t2
  reaches that opponent vertex or an older vertex. The extraction graph H uses str for p-vertices (268-285) and every
  opponent edge into Z_τ (248).
Consequence: every vertex reachable from τ is in τ's SCC, so Pearce from τ (224-305) emits τ's SCC only. It is nontrivial
exactly as stated (317; for p-owned τ, closed means str[τ] ≠ −1, 515).
Two remarks. First, the H of a p-vertex never leaves Z_τ: str values are members of Z_τ, and line 268 reads str without an
R test. Second, member Z is empty when sptl starts (reset at 542; the computeDistanceValues uses run only under trace).

## (b) Lemma B-thr — SIGN WITH GAPS (Opus 5.5, D12)
(i) Holds by SCC1, since every vertex of an sptl region has priority ≤ pr(τ) (494).
(ii) Correct as written. Escapes in Z_τ: an escape e ∈ Z_τ is the target of an H-edge from an opponent vertex of C_τ, so it
would be in C_τ. Escapes in a later region: the opponent vertex would have had an unconsumed successor outside Z when it
joined (80, 155-156), and the top is covered by the closed check (519-525). Escapes in a higher region: this is K2, which
I re-checked. At the pop of the last escape in that higher region, t is alive (it equals C_τ ⊆ G, so 132-135 never fired),
it has p's parity (an opponent tangle with the same vertex set would have an opponent-parity maximum), its vertices are
unconsumed with priority ≤ pr(τ) ≤ the higher top's, and its other escapes are consumed. So it would fire there.
Escapes left unconsumed in R: the same escape test excludes them.
- G-b1 (closed). (iii) says every escape outside R "joined a removal in this search through a pop". That is false for an
  escape solved in an earlier search, which is not popped in this one. The fix is Lemma O0's argument. If an escape of t
  was solved for the opponent, the opponent vertex of t with that edge was attracted (74-90 with pl = 1−p), so t would be
  dead. If the last escape was solved for p, t would have fired at 1037. So every escape of a live t ⊆ G' lies in G'.
- G-b2 (closed; how I read the statement). A vertex is popped again inside a recursion (918-923 pops Z_T, then the child
  pops it again). So "the LAST escape of t to be popped" must mean this: for each escape, take the pop at which it leaves
  the context chain of the current call. Then the attractor of the last such pop belongs to the current call or an
  ancestor, and its R contains the current context ⊇ t. Under any other reading the sentence "every vertex of t is in its R"
  fails.
- F-b3 (finding; it does not affect truth). Branch (b) cannot occur. Suppose t ⊆ Z_T and e ∈ Z_T is moved to X at
  936-950. When e is popped at 945, attractVertices(1−p, e, Z, X, Z, t) attracts every opponent-owned predecessor in Z of
  priority ≤ t with no escape test (75: owner = pl). That includes the opponent vertex o ∈ t with o → e, since every escape
  is an opponent successor. So t ∩ X ≠ ∅ and t is not inside the recursion context.
  The same holds when t is newly accepted at e's pop in a −1 attractor (a case the proof does not list). Then t ⊆ Z_T, and
  either e stays in the lineage (so it is not the last removal) or e moves to X and drags o along. In Dom pieces and in this
  call's own −1 attractor, acceptance or "nothing new" puts t into the removed part, which contradicts t ⊆ current R.
  So only the priority rejection is left, which is (a). B-thr holds in the stronger form "(a) always". The 01:38Z
  correction was not needed, and GAP-β's shape (β-b) is empty: GAP-β is (β-a) alone. The realised duplicates
  (gapb_dup_n20, gapbW_dup_n20) are (β-a).
  DATA (mine, bthr_probe.py, every .pg under experiments/ with n ≤ 80): 3,847 (Oink order) and 3,768 (stable) T pieces;
  8,059 and 7,880 live p-tangles lie inside Z_T; 0 cases of t ⊆ Z' with an escape in B, in both orders.

## (c) Theorem A — SIGN (Opus 5.5, D12)
Steps checked:
- Regions of the first sptl pass. They equal best_vertices' last-round regions (same V = V*, R and code path, 481-500 vs
  690-706). A tangle learned at a higher top lies in a consumed region and is rejected lower (138).
- Inclusion in W_p. They lie inside A ⊆ W_p(G') by K4.
- Nontriviality when closed, and no W block. W is reset at 1016, so W[τ_k] is false in pass 1.
- Not a duplicate. By B-thr (ii) with R = G', a duplicate's escapes would all be solved, and O0 excludes that. Tangles
  learned earlier in the same search were created with G = G' (333), so their escapes lie in G'.
K4 (DTL-proof.md §2.3), re-checked in outline:
- A is opponent-closed in G'. At X = ∅, every opponent vertex of A was attracted with Gx = R = G', or with the forgiven
  edges going into earlier (consumed) regions, which lie in A.
- Plays consistent with ψ are won by p. Between two consecutive top visits, the priorities are below the first top's (the
  rescue path, threshold < pr(τ)). After that they stay within regions whose tops increase along forgiven edges. So the
  maximum seen infinitely often is a top priority, or the play has a tangle tail. A tangle tail is p-won: every cycle of a
  stored tangle's graph is p-won, by induction over creation with SCC1.
- When the call returned at 716, the threshold loop did not run, and A := the union of the regions.
K5(ii) (an opponent top whose successors all lie in higher regions joins the last of them) re-checked against 75-90. The
theorem is conditional on its own premise "if it is closed", i.e. no (α).

## (d) Lemmas O0 and O1 — SIGN, SIGN (Opus 5.5, D12)
O0. In the dominion attraction (1032-1038: attractVertices/attractTangles(player, v, G, S, G, −1)), G[v] is cleared at 1035 before the pop's rules run. Case p: the other escapes are in S or out of G, and the vertices of t are in
G \ S (t ⊆ G'), so t fires at 1037. Case opponent: o is attracted unconditionally (74-90, owner = pl), so t is dead (132-135).
Escapes are recorded only while in G (333), so t existed when they were solved. Correct.
O1. At the pop of t's last escape in R during Dom(V, R): the vertices of t were never pushed (a pushed vertex is popped and
leaves R; t ⊆ R afterwards), so none is in X. The other escapes are in X or outside R. So the only possible rejection is
the priority test (140), which gives q > pr(τ_j). If m ∈ V, the loop at 878/962 reaches m before τ_j, because
index(m) > index(τ_j) by sortedness (q > pr(τ_j)), and m is removed from R. Contradiction. Correct. The −1-branch remark
after O1 is not part of the lemma.

## (e) Lemma OPP-EXIT — SIGN WITH GAPS (Opus 5.5, D12)
- G-e1 (statement; closed). "π(o) outside the set CurR in which o was attracted" is satisfied trivially when π(o) is a
  vertex of Z_τ popped before o joined, since such a vertex is also outside CurR. The intended statement, which the proof
  actually needs, is "π(o) ∉ Z_τ". With that, the "i.e." clause is right: π(o) ∉ Z_τ forces π(o) to have been consumed
  before o joined and not by Z_τ, so it lies in an earlier region of the pass, in X, or outside the search_rec context.
- G-e2 (proof; closed). The proof cites only the vertex rule (75-86). Two more cases are needed:
  - o joined through a fired tangle t2. Then π(o) is in t2, which is in Z_τ, or it is an escape of t2, which is in Z or not
    in R (155-156).
  - o = τ (opponent-owned). The closed test (519-525) leaves no successor in unconsumed R.
  With these, π(o) ∈ CurR implies π(o) ∈ Z_τ in all cases.
The rest is correct: str[v] ∈ Z_τ for p-vertices, W_{1−p} is a p-trap, and the play is a cycle of H, hence p-won as in (c).

## (f) Lemma K0 — SIGN (Opus 5.5, D12)
This is not R-STEP5's claim (1), which was KT0 of §18g. (a): a p-vertex of Q has σ(v) ∈ D (σ stays in D), and σ(v) ∉ X ∪ A
(otherwise v ∈ A). An opponent vertex of Q has all its edges in D (D is an opponent trap), and one of them in Q (otherwise
v ∈ A). (b): with X = ∅ the least A is ∅, because every vertex of G' has a successor. (c): R_end has no p-priority vertex
(661-668). The σ-play inside Q is infinite and is won by the opponent, yet it is consistent with σ from D, so Q = ∅.
(d): the depth-0 loop leaves only through result 0 (854). Correct.

## (g) phases ≤ D + 2 — SIGN (Opus 5.5, D12)
--dtl is DTLSolver with interleaved = false (solvers.cpp 77; dtl.hpp 33, set true only in IDTLSolver, 97). So run() takes
1106-1121: one block of search(0) followed by one block of search(1), and a false search ends its block for good. I read
"phase" as defined in SPP.md §1: a maximal run of one player's searches ending with a dominion-finding search or with the
block's end. Then player p has ≤ D_p + 1 phases. Each dominion-finding search solves ≥ 1 vertex (368-373, 1032-1035), so
D ≤ n. Oink's bottom-SCC mode is off by default (oink.hpp 171), so the solver runs once on the whole game. Correct.

## (h) First-Difference Lemma — SIGN WITH GAPS (Opus 5.5, D12)
(i) is correct. W is written only at 529 and reset at 1016. str is written at every join (89, 171, 485, 694, 880, 908,
965) before it is read (73, 268, 455). pea_vidx is cleared at 536. S and dom_vector are empty before a phase's last search.
- G-h1 (OPEN). In (ii), "every computation before e is identical" also needs identical control flow. Control flow can
  diverge at a point that is not a tattr: the sptl repeat loop `while (more)` (870-874), whose flag is extractTangles'
  return value (464, 377). Suppose search s learns a tangle t in some sptl pass, and search s+1 is identical up to that
  pass. Then s+1 re-finds t, it is a duplicate (385-424, skipped), and `more` is false. So s+1 runs one sptl pass fewer
  than s and goes straight to Dom(V, R) (878). The tattr logs are then misaligned. The next tattr of s is a pass-2 region
  (Z = {top}); that of s+1 is Dom's attractor (target X ∪ {top}). These have different inputs, so (ii) fails as stated, and
  (iii) fails too: the divergence is caused by a tangle s learned at that point, not after it. L-ALG's own checker
  (dtl_fdlcheck.py, positional alignment) would report this as a violation.
  Reachability: it needs t, new in s, to be an orphan at that piece of s+1. That means all its escapes lie outside the
  context, with the earlier removals of those escapes identical in both searches. Orphans are known to exist (NO-ORPHAN
  killed by gapb_dup_n20 / gapbW_dup_n20), but this particular pairing has not been seen.
  DATA: L-ALG's corpus has 0 violations in 990/957 transitions. dtl_fdlcheck.py on the two orphan instances, both orders,
  gives 0 in 12 + 3 and 13 + 3 transitions. Mine (fdl_random.py, random games n = 4..14, 1,500 seeds each, both orders)
  gives 0 in 293 + 293 transitions. Random games mostly end their phases at once, so this is weak evidence.
  Fix (for L-ALG): either (1) add hypothesis (ND): "no extractTangles call of s+1 before the first differing tattr meets a
  duplicate", or (2) state the lemma on the log with sptl passes removed. Option (2) needs a check that the extra passes of
  s only add tangles (and W bits) learned before e, and the W difference can then let s+1 extract, and learn, at a later
  top before e, which contradicts "s+1 learns nothing before e". The monotonicity core is correct whenever no such
  divergence occurs: for fixed input (Z, R, Gx, maxpr), the attractor output is monotone in T (1.2b).

## (i) Lemma DV*-MONO — SIGN (Opus 5.5, D12)
Checked against the abstract definition (no code involved): lfp is monotone in Z and T; regions are compared top by top in
the common order (Z ⊆ Z'); C' ∩ V ⊆ C; the sweep keeps Z_t ⊆ Z'_t; V \ C ⊆ V' \ C'; induction over rounds gives
V_r(T) ⊆ V_r(T'). Hence "dropped at r under T' ⇒ dropped at ≤ r under T".
- R-i (my reading). The definition gives INF only "in a round with C = ∅". It does not cover a round where C ≠ ∅ but every
  candidate is rescued (V then stays fixed, like code line 767). I read INF as "never dropped". The proof is correct under
  that reading, which matches the code.
Consequence: in one phase (G fixed, no tangle of G dies, T only grows) each coordinate is non-decreasing in
{1..|V_0|, INF}, so DV* changes at most |V_0|² ≤ n(n + 1) times. DV = DV* is correctly labelled OPEN in the doc and is not
signed here.

## (j) Per-context LRN budget ≤ n(n + 1) — SIGN (Opus 5.5, D12)
DV*_R is DV* on the subgame R, with tangles inside R only. T ⊆ T' implies the same for the tangles inside R, so DV*-MONO
applies at fixed R. Within a phase T only grows, so DV*_R is pointwise non-decreasing over the whole phase, whichever
transitions it moves at. An LRN transition at R is by definition one where DV*_R moves, so there are ≤ |V_0(R)|² ≤ n(n + 1)
of them per distinct context per phase. This does not depend on (h). The split into LRN/DEF/ABS is a definition and data;
only the budget is signed.

## (k) (SPP) ⇒ searches ≤ n(n + 2) and O(n^10 (m + n²)) — SIGN, conditional (Opus 5.5, D12)
- Searches ≤ Σ_phases |G'| ≤ (D + 2)·n ≤ (n + 2)·n, by (g) and (SPP) for every ω.
- Lemma W: extractTangles is called only at 539, at most once per top per search (528-529, reset 1016). By SCC1 each call
  creates ≤ 1 tangle. So tangles ≤ n·searches ≤ n²(n + 2).
- DTL-proof.md §3 (b)-(e) re-checked in outline:
  - ≤ n + 1 rounds per best_vertices call;
  - ≤ n(d + 1) search_rec iterations per search, because the recursion strictly lowers the top priority (936-942 removes
    level t);
  - sptl passes ≤ (new tangles + dominions) + 1;
  - W_A = O(m + |T| n²).
  The stated O((|T| + n)² n⁴ (m + n²)) is valid when (|T| + n)·n = O(n⁴), i.e. for |T| = O(n³), which (SPP) gives. Then the
  total is O(n^6 · n^4 · (m + n²)) = O(n^10 (m + n²)).
- TARGET.md §3, bit cost. Priorities are renumbered to ≤ n at step 0 (L26; charged O((n + m) log n)). Every stored number
  is a vertex index, a priority ≤ n, a tangle index ≤ n³ + 2n², a stack pointer or a bit. All fit O(log(n + m))-bit words,
  so unit cost = bit cost. Correct.
This signs the conditional only. (SPP) is DATA, and completeness (GAP-C) is open.

## Hypotheses and dependencies still open after this report
1. G-h1 (First-Difference Lemma): CLOSED after §C1. REFEREE-2's B-thr G-b1: CLOSED after §C5.
2. (SPP): DATA only. Item (k) is conditional on it for every ω.
3. (α) for Theorem A (its premise "closed"), and Case B (GAP-K'): open.
4. DTL-proof.md §2.3 K4 and K5(ii) and §3 (b)-(e): re-checked by me in outline only, as dependencies of (c) and (k). They
   are not separately signed here.
5. Code facts C1-C6 (R-STEP5 §0).

## Findings for the author (L-ALG), one line each
- F-b3: B-thr branch (b) is vacuous (944-948 pulls the escape's opponent predecessor in t into X); B-thr holds as "(a)"; GAP-β = (β-a).
- G-b1: B-thr (iii) must use O0's argument for escapes solved before the search.
- G-b2: B-thr: define "last escape popped" as the pop at which it leaves the current call's context chain.
- G-e1/G-e2: OPP-EXIT: state "π(o) ∉ Z_τ"; add the tangle-rule and top cases to the proof.
- G-h1: First-Difference Lemma: state the log alignment (delete repeated sptl passes before e, §C1); no hypothesis needed.
- K5: DTL-proof K5 (i)/(iii) false as written (k5.pg); use REFEREE-2's corrected form (§C3).
- R-i: DV* definition: give INF to "never dropped" (C ≠ ∅ with all candidates rescued).

## §C. Comparison with REFEREE-2 (docs/referee-2/R2-PROVED2.md @ 581902f), added 09:57Z (date -u) on the Lead's request (stamped 10:13Z by the Lead's clock)
I read REFEREE-2's report only after my report was pushed (50f2546). I re-checked each point of disagreement against the code.

### C1. First-Difference Lemma, G-h1: REFEREE-2 is right; my "OPEN" was wrong
We saw the same thing: s+1 skips sptl's repeat pass (870-874), so the tattr logs are not aligned position by position. The
difference is in what follows from it.
- I concluded that (ii) and (iii) fail.
- REFEREE-2 shows that the extra pass of s is a pure repetition. I checked the sandwich region by region (same inputs, by
  induction over the tops):
  - pass 1 of s ⊆ pass 2 of s, because T only grows (1.2b);
  - pass 2 of s ⊆ pass 1 of s+1, because T_s(pass 2) ⊆ T_{s+1};
  - pass 1 of s+1 = pass 1 of s, because that pass comes before e.
  So the regions are equal. Closedness depends only on the sets (73, 512-526), so every closed top already has W set
  (529), and pass 2 extracts nothing and sets no new W bit.
- That removes both of my follow-up worries. No W difference reaches later pieces, and s+1 does not learn before e.
- With the alignment "delete from s each repeated sptl pass before e", (ii) and (iii) hold as written. The repair is a
  convention for the log, not a new hypothesis.
- My error: I did not check whether the extra pass could change anything.
- Remaining item for L-ALG (wording): state the alignment convention. dtl_fdlcheck.py compares the logs position by
  position, so it should also drop repeated passes. On the corpus such misalignments evidently did not occur (0 caller
  mismatches).
Final verdict (h): SIGN WITH GAPS (Opus 5.5, D12). G-h1 is closed by the alignment argument; nothing is open.

### C2. B-thr (iii), REFEREE-2's G-b1: a separate case that my report missed; F-b3 does not close it
- REFEREE-2's case: t is created in the current search after the removal pop of its last in-G' escape. tout is computed
  against this->G (333), so escapes already in X are recorded. Then t did not exist at that pop, so it was never
  evaluated there, and neither (a) nor (b) applies.
- My F-b3 (and my G-b2) assumed that t existed at that pop. They do not touch this case.
- I agree with REFEREE-2's closed part. Within one S piece, W[τ] blocks a re-find at τ, and a re-find at another top of t
  is impossible.
- I also agree with the open part. Across S pieces (or later pieces of a recursion), t must have stayed outside
  Dom(V*, R) of its S piece. Dom runs after sptl with the larger tangle set and consumes top-down. Monotonicity of the union
  in T is the GAP-A deficit question (Lemma E; MONO is false in general), so nothing proved excludes this.
- The case is OPEN. REFEREE-2's data found 0 same-search duplicates.
F-b3 still stands, and here we disagree. REFEREE-2 writes that acceptance or "nothing new" in a −1 attractor means "(b)
must hold". I hold that (b) cannot occur.
- When e is moved to X at 936-950, its pop at 945 runs attractVertices(1−p, e, Z, X, Z, t).
- That call pulls into X the opponent vertex o ∈ t with o → e. o is owned by pl = 1−p, so there is no escape test (75). It
  is in Z, and pr(o) ≤ t because every vertex of Z_T has priority ≤ t. Every escape is an opponent successor (329-337).
- So t ∩ X ≠ ∅, and t cannot be in the recursion context.
- Data: 0 cases of that shape among 8,059 and 7,880 tangles inside a T region (bthr_probe.py).
- REFEREE-2's "both hold in the partial −1 case" concerns a t that is partly in Z_T. Such a t is not inside any later
  context of the chain either, so it does not change the conclusion.
Net for B-thr: the conclusion "(a)", for tangles that existed at the removal pop, is correct and (b) is empty. The
statement is unproven for REFEREE-2's G-b1 case.
Final verdict (b): SIGN WITH GAPS (Opus 5.5, D12). Open: REFEREE-2's G-b1 (same-search creation after the last escape left,
needing t ⊆ Dom(V*, R)). Closed: my G-b1 (= REFEREE-2's G-b3) and G-b2. Finding: F-b3.

### C3. DTL-proof K5 (i)/(iii): REFEREE-2's counterexample is correct; my Theorem A verdict stands
- k5.pg, checked by hand and by run:
  - Even vertices: a (priority 2, self-loop), b (4) → d, d (3) → a, y (5) → b.
  - The root best_vertices call of Even returns 1 with V* = {a, b} (dtl_pyref through dtl_step5, stable order).
  - Regions: Z_b = {b} (y has priority 3 > 2 after compression and is not taken), Z_a = {a}.
  - b is a candidate (b → d ∉ Reg). The rescue loop attracts d at level 1, which rescues b, and y at level 3. So
    A = {a, b, d, y}.
  - y ∈ A \ Reg is an Even vertex with an edge into the higher region {b}, so K5 (i) is false.
  - d and y are in neither Z_a nor Str = ∅, so K5 (iii) is false.
  - Pinned Oink: 1 dominion, 0 tangles, verified.
  - Cause: the rescue loop runs to max_prio (721-722), so A contains vertices attracted above every top.
- REFEREE-2's corrected form: restrict to A_< := the rescue set after level pr(τ_k) − 1, and replace Str by Up(Str).
  Checked in outline.
  - (i) holds for A_< \ Reg. Such a vertex has priority < pr(τ_k) ≤ every higher top's priority, and it was unconsumed,
    so it would have been attracted at that region's pop.
  - τ_k, if rescued, is rescued at a level < pr(τ_k) (737), so its ψ-successor lies in A_<.
  - I did not re-derive the induction A_< \ Reg ⊆ Z_k ∪ Up(Str) step by step. I accept it as REFEREE-2's.
- Effect on Theorem A: none.
  - My signature (§c) used only K4 (A ⊆ W_p(G')) and K5 (ii) (an opponent top whose successors all lie in higher regions
    joins the last of them). K5 (ii) is proved independently of (i) and (iii).
  - K4 survives the max_prio sweep. From a top, ψ follows a rescue path at levels < pr(τ), whose vertices have priority
    < pr(τ). Region vertices have no edge to vertices that no region took (80). So vertices attracted at high levels,
    like y, are only transient.
  - On k5.pg Theorem A's conclusion holds: the lowest region {a} is closed and is a dominion inside W_0.
  - Theorem A uses "closed" as its hypothesis. Only the meaning of the label "(α)" depends on K5 (i)/(iii), as REFEREE-2
    says.
  - REFEREE-2's G-c1 reading (the first sptl pass of the root S piece) is the reading I used.
Final verdict (c): SIGN (Opus 5.5, D12). Finding for L-ALG and the Lead: DTL-proof K5 (i)/(iii) is false as written
(k5.pg). GAP-C's map should mark K5 as "(ii) PROVED; (i)/(iii) corrected form per R2-PROVED2 §3", and "(α)" should be
defined with Up(Str).

### C4. Other differences
REFEREE-2 marks (f) K0 and (k) as SIGN WITH GAPS, where I signed them. I did not re-examine those gaps, because the Lead did
not ask. On the three points above, the final verdicts are: (b) SIGN WITH GAPS, (c) SIGN, (h) SIGN WITH GAPS (closed).

### C5. Follow-up (10:10Z by date -u; the Lead's message stamped 10:35Z): REFEREE-2 §13.2 closes its G-b1 — SIGNED
Two corrections to §C2:
- F-b3 is no longer disputed. R2-PROVED2 §13.2 checks it at 944-948, agrees with it, and withdraws its "partial −1"
  remark.
- REFEREE-2's G-b1 is closed by R2 §13.2. I checked the argument step by step against the code.
  - Tangles are created only by extractTangles, called only at 539 (sptl), and sptl runs only in S pieces (867-874). So t
    is created at a top a of an sptl region in some S piece P1 (call c, context R1, stable set V1). sptl takes tops only
    from V (482), so a ∈ V1. By SCC1, a ∈ t.
  - P1's Dom(V1, R1) (878-890) gives X[top] = true to every top of V1 (879-880; a top already in X stays in X). It pops
    each pushed vertex and sets R[v] = false (885). So after P1, a ∉ R_c, and R_c only shrinks afterwards.
  - Later contexts of c, and contexts of recursions started by later pieces of c, are subsets of R_c (search_rec(Z) with
    Z ⊆ R at 914-954), so they exclude a.
  - Ancestor case, at every depth (the Lead's question). c is search_rec(Z', p, d) called from a T piece of its parent c'.
    Before the call, c' has popped every vertex of Z_T ⊇ Z' and cleared it from R_{c'} (918-920), and it has put all of
    Z_T into X_{c'} (951). After c returns, Z is reset (955) and c' continues with R_{c'} ∩ Z_T = ∅. So every later
    context of c' and of its later recursions excludes Z' ∋ a. By induction up the chain, the same holds for c'' (which
    removed Z_T(c'') ⊇ R_{c'} at its own 920), and so on up to depth 0.
  - A search_rec context is never re-entered: each call has its own local X and Z (837-840).
  - So no context after P1 in search s contains a, and no duplicate of t can arise there. Within P1's own sptl passes,
    R2 §2 (W[τ] at 528, and the order of tops) excludes it.
  - Across searches, t was created before the next search, and B-thr (iii) applies with my G-b1 (= R2's G-b3, via O0).
Final verdict (b): SIGN WITH GAPS (Opus 5.5, D12). All gaps are closed: my G-b1 and G-b2, and REFEREE-2's G-b1 (by R2 §13.2,
checked). B-thr holds as "(a) always" (F-b3), and GAP-β = (β-a). This now agrees with REFEREE-2's verdict.
Packet-2 final verdicts that changed in §C: (b) as above; (c) SIGN; (h) SIGN WITH GAPS, closed.
