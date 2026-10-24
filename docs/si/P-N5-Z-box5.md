# Referee packet P-N5-Z: crossings of N5 reduce to reversals of R (box 4 lemmas)
L-SI successor 2 (Opus 5.5, D15/D18). Written 2026-10-24 20:20Z-20:50Z (date -u), at the Lead's request (20:2xZ). Version 2 (data corrections only, §9-§11), 20:4xZ.
- Self-contained: definitions, statements, full proofs, and the location of every dependency.
- Source text: docs/si/N5-X-box4.md §2-§4 and §8. This packet is the final form of what a referee needs. Where the two differ, this
  packet governs. In particular NOFE is stated here in a STRONGER form than box 4 §3: the "or on a (σ_k, τ)-cycle" escape is removed
  by the case analysis in §4.
- Status: L-SI's proofs, unrefereed. These are lemmas about the candidate N5 on 𝒞^1O. They are not a running-time bound, not a
  TARGET.md claim, and not a step-4 pass. G-N5-TIME stays OPEN.
- Labels per statement: PROVED (L-SI succ. 2), READING, CONJECTURE, OPEN, DATA.
- Statements:
  - §2 ACT;
  - §3 LOOP;
  - §4 NOFE;
  - §5 NOFL-E;
  - §6 GAP;
  - §7 LV′;
  - §8 WM;
  - §9 Corollary Z (from R21 (g) and LV′).
  Refuted forms: §10. Data: §11.

## 0. Objects and dependencies
- N5: docs/new/N5-ssi-global.md SPEC S1-S5.
  - S4a: Even's arena step. σ_{k+1} is a pointwise-optimal strategy of the one-player arena in which Even's vertex v may use only
    {σ_k(v)} ∪ Iσ_k(v) and Odd is fixed to τ_k.
  - S4c: fallback. It happens iff S4a returns σ_k and S4b (Odd's step) returns τ_k. Then every Even vertex with an Iσ edge switches to
    its best one, by (Ξ_k-key, index).
  - Code: experiments/new/n5.py, lines `if Is:` … `fb += 1`.
- Iσ_k (the gate): (v, z) ∈ Iσ_k iff z ≠ σ_k(v) and Ξ_k(z) ▷ Ξ_k(σ_k(v)) (experiments/si/si.py `improving`, successor-valuation
  comparison).
- Valuations: VJ00 (BRICS RS-00-48), notation of docs/new/N5-phase-bound-box10.md §1. Ξ_k := Ω_{σ_k, σ̄_k} (honest, against Odd's
  best reply σ̄_k); W_k := Ω_{σ_k, τ_k} (σ_k's valuation in the one-player game G_τ); θ_k := Ξ_k(o), w_k := W_k(o).
- λ_Ξ, λ_W: cycle-node maps. A PHASE is a joint λ-phase (λ_Ξ and λ_U constant) with τ constant. On 𝒞^1O τ is determined by τ(o),
  which is part of the phase key (box 28 convention).
- Convention in THIS packet: R_k := the vertices v ≠ o whose (σ_k, τ_k)-play reaches o; R̄_k := R_k ∪ {o}; F_k := V ∖ R̄_k.
  - R19-R21 put o into R. Their F equals this F, and both conventions give the same crossing transitions (R_{k+1} ≠ R_k).
- (h) at k: H1 (the honest play from o does not return to o), H2 (the W-play from o does not return to o), H3 (Ξ_k(o) and W_k(o) have
  the same cycle node). P-N5-RE §0. THR: (h) and Ξ_k ≠ W_k.
- Fact (F0), elementary: if a vertex u ≠ o keeps its edge at k → k+1 and τ_{k+1} = τ_k, then u ∈ R̄_k ⟺ its successor ∈ R̄_k. The
  successor is the same at both states, so this holds with the same successor.
- (F-pre), elementary (box 1 §2, "F-pre"): if y lies on neither valuation path (the path to the cycle node) and is neither cycle node, then y ⊕ a ◁ y ⊕ b iff a ◁ b. If the cycle nodes differ the
  comparison is decided by them; otherwise y enters both path sets or neither, and both lengths grow by 1.
- (VAL), elementary (VJ00 valuation of a lasso): if y ≠ λ(y) in a strategy pair's graph, then Ω(y) = y ⊕ Ω(succ(y)). y's path to its
  cycle node goes through succ(y) and does not return to y.
- Signed results used:
  - R15 (a): Ξ_{k+1} ⊵ Ξ_k.
  - R19 (a) Lemma G: (a) off R, Ξ = W, no (h) needed; (b) under (h), on R, Ξ = π ⊕ θ and W = π ⊕ w, with π the route to o.
  - R21 (a) Lemma XW: Ξ_k ⊴ W_k pointwise.
  - R21 (c) Lemma FBL-N (i): at an S4c fallback with τ unchanged, the fallback is Even's and σ_k is a pointwise arena optimum in G_τ.
  - R21 (g) Theorem X: a phase has ≤ (3n²(1 + X + O) + X + O + 1)(4n(n − 1) + 1) transitions, X = #crossing transitions,
    O = #OTHER-touching transitions.
  - R18 (d) Lemma S (c): N5's S4a step maximises V_{·, τ_k} over the arena, i.e. it is a pointwise-optimal gated best response.
- Step (K), used in §4-§6 (PROVED here, from FBL-N (i)). Let k → k+1 be a fallback inside a phase, and let (y, z) be an arena edge (in
  particular any edge of Iσ_k). Suppose the strategy σ_k[y → z] has W-value at y strictly above W_k(y). Then σ_k is not a pointwise
  arena optimum, contradicting FBL-N (i). So no such edge exists.

## 2. Lemma ACT (PROVED, L-SI succ. 2): every crossing has an active crosser
Let k → k+1 be a transition with τ_{k+1} = τ_k, and let S be the set of Even vertices v with σ_{k+1}(v) ≠ σ_k(v).
- (i) If R_{k+1} ⊄ R_k, some s ∈ S has s ∈ F_k, σ_{k+1}(s) ∈ R̄_k and s ∈ R_{k+1}.
- (ii) If R_k ⊄ R_{k+1}, then either:
  - some s ∈ S has s ∈ R_k, σ_{k+1}(s) ∈ F_k and s ∉ R_{k+1}; or
  - the (σ_{k+1}, τ)-graph has a cycle that avoids o, lies inside R_k and contains a vertex of S.
Proof of (i).
- Take x ∈ R_{k+1} ∖ R_k. Its (σ_{k+1}, τ)-play x = p_0, p_1, …, p_m = o reaches o; stop at the first visit.
- Let s_1, …, s_j be the vertices of S among p_0, …, p_{m−1}, in order. Then j ≥ 1: otherwise the play uses only old edges, and
  x ∈ R_k.
- Write M(u) ∈ {R̄, F} for u's membership at k. The vertices strictly between σ_{k+1}(s_i) and s_{i+1}, and between σ_{k+1}(s_j) and
  o, keep their edges. By (F0) they carry the same membership along each segment:
  - M(σ_{k+1}(s_i)) = M(s_{i+1});
  - M(σ_{k+1}(s_j)) = M(o) = R̄;
  - M(s_1) = M(x) = F, since the prefix p_0 … s_1 also uses old edges.
- So some i has M(s_i) = F and M(σ_{k+1}(s_i)) = R̄. If none did, induction on i would give M(σ_{k+1}(s_j)) = F.
- s_i lies on x's new play, which reaches o, so s_i ∈ R_{k+1}. □
Proof of (ii).
- Take x ∈ R_k ∖ R_{k+1}. Its new play never visits o and ends in a cycle.
- Define s_1, s_2, … (the vertices of S on the play, in order of first visit) and the segments as in (i). Here M(s_1) = M(x) = R̄.
- Suppose no s_i has M(s_i) = R̄ and M(σ_{k+1}(s_i)) = F. Then by (F0) along the segments, every vertex of the play lies in R̄_k. It
  is not o, so it lies in R_k, and this includes the final cycle.
- That cycle contains a vertex of S. A cycle of old edges inside R_k is impossible: old plays from R_k reach o.
- Otherwise the s_i found lies on x's new play, which avoids o, so s_i ∉ R_{k+1}. □
Terminology: s in (i) is an ACTIVE ENTRANT, s in (ii) an ACTIVE LEAVER. The other vertices of R_k Δ R_{k+1} are PASSIVE.

## 3. Lemma LOOP (PROVED, L-SI succ. 2): no new cycle inside R_k within a phase
If k and k+1 lie in one phase and H1 holds at k, the second alternative of ACT (ii) does not occur.
Proof.
- Let c := λ_{Ξ,k}(o), the cycle node of θ_k.
- c ∉ R_k:
  - c lies on the final cycle of o's honest play, and o is not on that cycle (H1).
  - The honest play and the (σ_k, τ)-play agree at every vertex except o. So c's (σ_k, τ)-play runs around that cycle and never
    reaches o.
- Every u ∈ R_k has λ_{Ξ,k}(u) = c:
  - u's honest play follows its (σ_k, τ)-route to o, then o's honest play.
  - That play cannot revisit a route vertex: from one, it would return to o, against H1.
  - So it ends in θ_k's cycle.
- Let C be a cycle of the (σ_{k+1}, τ)-graph that avoids o and lies inside R_k, and let t be its top vertex.
  - Since C avoids o, the honest play from t at k+1 is C, so λ_{Ξ,k+1}(t) = t.
  - t ∈ R_k, so t ≠ c = λ_{Ξ,k}(t). λ_Ξ changes, and k+1 is not in the phase. □
Corollary (PROVED). Inside a phase, at a transition with H1 at its start, every leave has an active leaver s ∈ R_k with
σ_{k+1}(s) ∈ F_k.

## 4. Lemma NOFE (PROVED, L-SI succ. 2): fallbacks enter only from o's W-play
Let k → k+1 be an S4c fallback inside a phase. Every switched edge y → z with y ∈ F_k and z ∈ R̄_k has y on o's W-play at k, i.e. the
(σ_k, τ)-play from o. Consequently, by ACT (i), a fallback transition with an entry switches such an edge.
Proof.
- (y, z) ∈ Iσ_k, because S4c switches gate edges only. So Ξ_k(z) ▷ Ξ_k(σ_k y).
- σ_k y ∈ F_k, because y ∈ F_k and (F0). So W_k(σ_k y) = Ξ_k(σ_k y) (Lemma G (a)).
- W_k(z) ⊵ Ξ_k(z) (XW). Together: W_k(z) ▷ W_k(σ_k y).
- Suppose y is not on o's W-play.
  - z's W-play is its route (vertices of R_k, which excludes y ∈ F_k) followed by o's W-play, which avoids y.
  - So in G_τ the switch σ_k[y → z] closes no cycle through y. Its W-value at y is exactly y ⊕ W_k(z).
- Case A: y ≠ λ_{W,k}(y). By (VAL), W_k(y) = y ⊕ W_k(σ_k y). By (F-pre), y ⊕ W_k(z) ▷ y ⊕ W_k(σ_k y) = W_k(y). y lies on neither
  valuation path: z's W-play avoids y, as just shown; σ_k y's path to its cycle node does not contain y, by (VAL).
- Case B: y = λ_{W,k}(y), i.e. y is the cycle node of its own W-cycle.
  - That cycle contains σ_k y, so W_k(σ_k y) has cycle node y.
  - W_k(z) has the cycle node of o's W-play, which does not contain y, so it differs from y.
  - Since W_k(z) ▷ W_k(σ_k y) and the cycle nodes differ, the cycle node of W_k(z) is strictly better than y.
  - y ⊕ W_k(z) keeps that cycle node; W_k(y) has cycle node y. Hence y ⊕ W_k(z) ▷ W_k(y).
- In both cases Step (K) applies: contradiction. □
Remarks.
- The original box 4 statement "fallbacks never enter" is FALSE (§10, nofe_cyc_n8). The proof shows where it fails: a tail on o's
  W-play, whose switch closes a cycle through o.
- READING, not used: by R18 (c)'s flat-case analysis, as summarised in P-N5-X §0, an improving arena edge at a pointwise optimum is flat
  with y = λ(y). That would add "y is a W-cycle node and the switch is W-flat".
- DATA (§11): 16 of 16 random cases have y a cycle node on o's W-play, Ξ = W at k, and (h) failing at k+1.

## 5. Lemma NOFL-E (PROVED, L-SI succ. 2): no evictions at fallbacks from Ξ = W states
If k → k+1 is an S4c fallback inside a phase, Ξ_k = W_k pointwise, and H2 holds at k, then no switched edge y → z has y ∈ R_k and
z ∈ F_k.
Proof.
- Suppose (y, z) is such an edge. It is in Iσ_k, so Ξ_k(z) ▷ Ξ_k(σ_k y), hence W_k(z) ▷ W_k(σ_k y) (Ξ_k = W_k).
- z ∈ F_k, so z's W-play avoids o, and hence avoids y: from y the W-play reaches o. So σ_k[y → z] has W-value y ⊕ W_k(z) at y.
- y is on no W-cycle: its W-play reaches o, and o's W-play does not return to o (H2). So y ≠ λ_W(y) and (VAL) gives
  W_k(y) = y ⊕ W_k(σ_k y).
- (F-pre) gives y ⊕ W_k(z) ▷ W_k(y). Step (K): contradiction. □
Corollary (PROVED; NOFL-E, ACT (ii), LOOP). From a state with Ξ = W and H1 ∧ H2, a fallback transition has no leave. Its entries come
only from NOFE's edges.

## 6. Lemma GAP (PROVED, L-SI succ. 2): throttled evictions land in the trust gap
If k → k+1 is an S4c fallback inside a phase and (h) holds at k, every switched edge y → z with y ∈ R_k, z ∈ F_k satisfies
    Ξ_k(σ_k y) ◁ Ξ_k(z) ⊴ W_k(σ_k y),
i.e. with π′ the route of σ_k(y) (empty if σ_k(y) = o): π′ ⊕ θ_k ◁ Ξ_k(z) ⊴ π′ ⊕ w_k.
Proof.
- The left inequality is (y, z) ∈ Iσ_k.
- Suppose Ξ_k(z) ▷ W_k(σ_k y). Then W_k(z) = Ξ_k(z) (Lemma G (a)), so W_k(z) ▷ W_k(σ_k y). Exactly as in §5:
  - z's W-play avoids y;
  - y is on no W-cycle (H2);
  - (VAL) and (F-pre) give an increase at y.
  Step (K) gives a contradiction.
- The π′-form is Lemma G (b) at σ_k(y) ∈ R̄_k. For σ_k(y) = o it reads θ_k ◁ Ξ_k(z) ⊴ w_k. □
Reading (integer form, not used in any proof). Inside a phase the crossing vertices all have cycle node c. A valuation with cycle node c
is then a pair (Σ ±2^rank, ±length) in Z² (lexicographic), and ⊕ is addition. The window above is π′ + (θ_k, w_k]: one interval of
width w_k − θ_k, the same for every vertex of R_k.

## 7. Lemma LV′ (PROVED, L-SI succ. 2): crossings are bounded by reversals of R
Give each crossing transition of a phase a sign:
- '+' if R_k ⊊ R_{k+1};
- '−' if R_{k+1} ⊊ R_k;
- '±' otherwise.
Let Z := #('±') + #(pure-sign crossing transitions whose sign differs from the sign of the previous pure-sign crossing transition).
Then
    X ≤ (n − 1)(Z + 1) + Z,   and Z ≤ X.
Proof.
- A maximal run of consecutive equal pure signs changes |R| strictly monotonically inside {0, …, n − 1}, so it has at most n − 1
  transitions.
- There are at most Z + 1 such runs, and at most Z '±' transitions. Z ≤ X is immediate. □
(This is the binary-counter amortization with potential |R|. Entries are increments, '−' runs are carries. INRs are entries and need
no separate charge.)

## 8. Lemma WM (PROVED, L-SI succ. 2): W never decreases at an arena step
Inside a phase, at every transition k → k+1 that is not an S4c fallback, W_{k+1} ⊵ W_k pointwise.
Proof.
- τ_{k+1} = τ_k (phase). σ_{k+1} is S4a's choice. By R18 (d) Lemma S (c) it maximises V_{·, τ_k} pointwise over the arena.
- σ_k belongs to the arena. Its valuation there is V_{σ_k, τ_k} = W_k (the same plays).
- Hence W_{k+1} = V_{σ_{k+1}, τ_k} ⊵ W_k. □
Corollary (PROVED). Inside a phase, every transition at which some W(v) decreases is an S4c fallback.

## 9. Corollary Z (PROVED, L-SI succ. 2, from the signed R21 (g) and LV′)
Inside one phase, with O := #OTHER-touching transitions,
    #transitions ≤ (3n²(1 + X + O) + X + O + 1)(4n(n − 1) + 1),   X ≤ (n − 1)(Z + 1) + Z,
so #transitions = O(n⁵ (1 + Z + O)).
- READING (consequence, as in R21): with Lemma Φ (≤ 2n(n − 1) + 1 joint λ-phases; box 21, PROVED by L-NEW, UNREFEREED) and τ-changes
  ≤ d − 1, N5 on o-cyclic 𝒞^1O is polynomial if Z and O are poly(n) per phase.
- OPEN (box 4 §10): (Z). Its hard part, by the data, is (C): the number of '+−' reversals per phase whose reversing transition is a
  fallback. A drain of consecutive evicting fallbacks counts once. By WM every W-lowering is a fallback, but W-lowerings can be far
  more numerous than reversals: x32_waves48 (L-RED) has 19 W-lowerings and Z = 4.
  The data say that on climbed instances they are exactly the evicting fallbacks (THR, GAP).

## 10. Refuted forms (DATA, each with a re-verified instance)
Each instance below was re-run with experiments/new/n5.py, checked with Oink zlk @ 8fbf0a7 plus verify.py (check_sol2.py), and the
counts were asserted equal to n5.run by the box 4 scripts.
- "A fallback transition has no entry" (box 4 first form of NOFE): FALSE.
  - Instance: experiments/si/xing/instances/nofe_cyc_n8.pg, sha1 f3868b39…, start nofe_cyc_n8.start (SIGMA0 1:2 2:3 3:2 4:7 5:0 6:5
    7:3, TAU0 0:7). n5.py: 2 iterations, 1 fallback.
  - At k = 1 (Ξ = W, (h) holds) the fallback switches 2 → 6. Vertex 2 is the cycle node on o's W-play 0 → 7 → 3 → 2.
  - R grows {1, 5, 6} → {1, …, 7}. Vertex 2's value (2, ∅, 0) is unchanged, and (h) fails at k+1.
  - Consistent with NOFE as stated in §4.
- (U*-DROP) "between consecutive leave transitions with w unchanged, rank(u*) strictly drops": FALSE.
  - experiments/si/xing/ustar.py, on fbref_cex_n32 (experiments/red/xing/instances, sha1 901674dc), lev_l_x
    (experiments/si/orlens/instances, 6c365ff7), run_x_inr2 (8a5a82a6) and x31_lem_t32 (60c15284): 15 of 15 checks fail. (Box 4 counted 19/19 by including s_rt32_final, which is
    NOT in 𝒞^1O: it has two Odd choice vertices, 14 and 28. Removed; see §11.)
  - u* is the top-ranked differing vertex and stays the same through every evicting fallback.
- (W-LAY) "between consecutive W-lowering transitions, at most n − 1 transitions change W": FALSE.
  - Instance: experiments/si/orlens/instances/thclimb_n16_s12.pg (sha1 6e0704b7), one phase of 16 transitions at n 16, all W-changing,
    no fallback (experiments/si/xing/wlay.py).
  - There θ changes at every transition and R grows 0 → 11 one vertex at a time.
- Potential no-gos (box 4 §7; not lemmas):
  - no function of (R, θ, w) rises at every crossing transition: x31_re24 (49eaf50e), states 1 and 5, 4 crossings between, (h)
    throughout;
  - no function of R-side data alone: lev_l_sc (86c17b07), R = ∅ at states 8 and 32, 16 crossings between.

## 11. Data (DATA, not proof; experiments/si/xing/, every script asserts its run equals n5.run)
- "Named instances" means 30 files:
  - experiments/si/orlens/instances/*.pg except s_rt32_final (15);
  - experiments/red/xing/instances fbref_cex_n32 and x31_* (14);
  - experiments/new/box28/instances/oc16_s2.
- s_rt32_final (sha1 93ba6aa3) is NOT in 𝒞^1O (Odd choice vertices 14 and 28). Box 4's tables included it by mistake. xclass.annotate
  now asserts exactly one Odd choice vertex.
- L-RED's later files in experiments/red/xing/instances (x32_*, u1t_cex_n32; all in 𝒞^1O): WM 0 violations.
  - W-lowerings: x32_waves48 19 (Z 4), x32_waves32 9 (Z 10), x32_nest40 1 (Z 2); 0 elsewhere.
- ACT: every crossing transition has an active crosser on 30 named instances and on 2 × ~2,600 random o-cyclic 𝒞^1O runs (n 8-16;
  leaves.py, seeds 401, 402). 0 exceptions.
- NOFE: 16 fallback transitions with a switched F_k → R̄_k edge in 4 × 3,000 random runs (seeds 401-404). All 16 tails lie on o's
  W-play (and are cycle nodes). No such fallback on the 30 named instances.
- WM: 0 violations on the 30 named instances and on 2 × ~1,700 random runs (wlay.py, seeds 601, 602). W-lowering transitions = evicting
  fallbacks on every named instance and every climb best.
- LV′: asserted on every phase scanned (zcount.py). Max Z: 7 on named instances, 18 on climbs at n 32 (zcl_fb2_n32, sha1 b00b6b69,
  n5 66/13, Oink OK; Lead re-run), 22 at n 48 (zcl_cu_n48, efe301af; 0 fallbacks).
- GAP (gapcheck.py): 309 switched R_k → F_k edges at fallbacks with (h), on the 30 named instances and the 7 climb bests
  (experiments/si/xing/instances/zcl_*). 0 violations of Ξ_k(σ_k y) ◁ Ξ_k(z) ⊴ W_k(σ_k y). Random runs (seed 401, 3,000 games) have
  0 such edges: vacuous.
- NOFE strong form (gapcheck.py, seed 401): 12 switched F_k → R̄_k edges at fallbacks, all with the tail on o's W-play.
