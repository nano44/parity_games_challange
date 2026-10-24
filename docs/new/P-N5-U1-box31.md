# Referee packet P-N5-U1: W-tie cascades and w-changes inside a joint λ-phase of N5 (box 31)
L-NEW successor 11 (Opus 5.5, D15/D18). Written 2026-10-24, finished 20:42Z by date -u, at the
Lead's request (20:40Z message). Frozen at this commit: corrections go in a fixes file, never here.
- Self-contained: definitions, statements, full proofs, and the location of every dependency.
- Source text: docs/new/N5-U1T-box31.md §2-§7 (box 31). Where the two differ, this packet governs.
- Status: L-NEW's proofs, unrefereed. Lemmas about the candidate N5 (SPEC tie-breaks) on 𝒞^1O (exactly one Odd vertex o with more
  than one successor). Not a running-time bound, not a TARGET.md claim, not a step-4 pass. G-N5-TIME stays OPEN.
- Labels per statement: PROVED (L-NEW), READING, CONJECTURE, FALSE, OPEN, DATA.
- Statements: Lemma R (§1), Lemma TB (§2), Lemma CASC (§3), Theorem U1 (§4), Lemma WC (§5). Reduction (§6, READING). Refuted forms
  and open items (§7). Data (§8).

## 0. Objects and dependencies
- N5 and its SPEC: docs/new/N5-ssi-global.md (S1 valuations and Engine.evaluate, S2 improving edges, S4a/S4b/S4c, FIX 2, FIX 4;
  code experiments/new/n5.py, experiments/si/si.py l.78-205). Valuations (c, P, ℓ); ⊵ is Even's order; v ⊕ val extends a valuation
  by one step ((V1)).
- Phase: a joint λ-phase with τ fixed (P-N5-X-box28.md §0, RESULTS R21). Inside a phase S4b returns τ, so a transition is either a
  FALLBACK (S4c) or an S4a step with σ_{k+1} = the S4a optimum of the arena H_k (n5.py l.46-52).
- Ξ_k = honest valuation of σ_k (against Odd's optimal counterstrategy σ̄_k); W_k = valuation of the play of (σ_k, τ); θ := Ξ(o),
  w := W(o); R_k = vertices whose (σ_k, τ)-play reaches o (o ∈ R); F = V \ R; H1, H2, H3, (h); EQ / THR / OTHER: as in
  P-N5-NH-box30.md §0 (pinned c7981ee) with its fixes docs/new/P-N5-NH-fixes-box30.md.
- Crossing-free interval I, route form of each frame, piece J (both frames in route form; R, θ, w constant), c_θ := λ_Ξ(o),
  c_w := λ_W(o), π_v (v's σ-route: vertices of v's σ-path before its first visit of o), facts (R1)-(R4): P-N5-NH §3.
  (R1): on a piece, Ξ(v) = π_v ⊕ θ and W(v) = π_v ⊕ w for v ∈ R.
- A U1 PIECE is a piece with c_w strictly more relevant than c_θ. Every U1 state is OTHER (c_θ ≠ c_w, so H3 fails).
- Signed results used: R15 (a) (Ξ non-decreasing); R17 (F1) (a one-player optimum of an arena dominates, pointwise, every strategy
  of that arena); R19 (d) (SG) (a switched Even vertex y with λ(y) ≠ y gains strictly in Ξ); R20 (d) CR / Lemma P^c (the coarse
  freeze); the P-N5-NH signatures of F1°, TC, P3′ with the fixes (P3-1 = G-NH-1).

## 1. Lemma R (PROVED, L-NEW): the restriction step keeps every optimal edge
Setting. One call of Engine.evaluate (SPEC S1 (i)-(vi)) at a cycle node c with region R_c, after the loop over the vertices u ∈ R_c
with rank(u) > rank(c), in decreasing rank. The evaluated game's Odd player is the OPTIMISER.
Statement. Let x ∈ R_c, and let y ∈ R_c be a successor of x that is optimal for the optimiser at x in the cycle-node and path-set
components. Then the edge x → y survives the restriction. Hence the length step (S1 (iv)) chooses x's successor among the
survivors of optimal length, which are exactly the fully optimal edges:
- in the longest-path mode, the first such successor in list order (FIX 4);
- in the BFS mode, the first-discovered one (FIX 4).
Proof.
1. Invariant, by induction over the processed u: every surviving edge joins two vertices with the same membership in each processed
   set M_u.
   - "Even likes u": M = vertices reaching c without passing u. Then u and every q ∈ M keep only edges into M. A vertex
     q ∉ M ∪ {u} with a surviving edge into M would reach c avoiding u, so q ∈ M.
   - "Odd likes u": M = vertices reaching u without passing c. Every q ∈ M \ {u} keeps only edges into M. A vertex q ∉ M with an
     edge into M would reach u avoiding c.
   So after step u, for each vertex either every remaining path to c passes u or none does, and the processed vertices above u are
   already decided the same way at both ends of every surviving edge.
2. Let x → y be deleted at step u. Then y ∉ M, and x ∈ M or x = u. By step 1, x and y agree on every vertex processed before u.
   - Even likes u, x ∈ M: through y every path to c passes u, so u ∈ P; x's optimum avoids u.
   - Even likes u, x = u: y ∉ M, so the play through y returns to u before c. That cycle has top ⪰ u with even parity: worse for the
     optimiser than reaching c.
   - Odd likes u: through y no path reaches u (u ∉ P), while x ∈ M collects u.
   In each case u is the most relevant vertex at which the two path sets can differ, so y is strictly worse for the optimiser.
3. So no optimal edge is deleted. The length step runs on the survivors. Its distances are the optimal lengths, so the survivors of
   optimal length are exactly the fully optimal edges. □

## 2. Lemma TB (PROVED, L-NEW): S4a's tie-break is a monotone potential
Statement (any game; any transition k → k+1 at which S4a is applied and no fallback occurs). Let W_k = value of (σ_k, τ_k) and
W' = value of (σ_{k+1}, τ_k). Let v be an Even vertex with σ_{k+1}(v) ≠ σ_k(v) and W'(v) = W_k(v), and suppose v is not its own
cycle node. Let c be the cycle node of W_k(v).
- (TB-odd) If c has odd priority, then σ_{k+1}(v) < σ_k(v) as vertex indices.
- (TB-even) If c has even priority and W' = W_k at every vertex of v's σ_k-play from v to c, then pk_{k+1}(v) <lex pk_k(v). Here pk(v)
  is the root-first sequence of vertex indices of v's play, from c (excluded) back to v.
Proof.
1. σ_{k+1} is the optimiser's counterstrategy of one call Engine.evaluate on the dual of H_k (n5.py S4a). So W'(x) = W*_{H_k}(x),
   the H_k-optimal value, for every x. σ_k is a strategy of H_k, so W*_{H_k} ⊵ W_k pointwise by (F1).
2. If W'(x) = W_k(x), then σ_k(x) is an optimal edge of H_k at x:
   W*(x) ⊵ W*(σ_k x) ⊕ x ⊵ W_k(σ_k x) ⊕ x = W_k(x) = W*(x).
3. In the dual, c's parity flips. So c odd in G gives the longest-path mode, and c even gives the BFS mode (S1 (iv)).
4. (TB-odd) By step 2 and Lemma R, σ_k(v) is a survivor of maximal length. The recursion takes the first such in list order; the lists
   are sorted (n5.py passes sorted(opt[v])). So σ_{k+1}(v) ≤ σ_k(v), and the two differ.
5. (TB-even) The BFS runs over predecessors in increasing index, with layers in FIFO order.
   - By induction on the layer, the queue order of a layer is the lex order of the root-first index sequences of the BFS-tree paths.
   - Each tree path is the lex-minimum over all surviving shortest paths: a vertex is discovered from its earliest-queued surviving
     successor in the previous layer.
   - By step 2 at every vertex of v's old play, and Lemma R, that play is a surviving shortest path.
   - So the tree path of v, which is its σ_{k+1}-play, is lex ≤ the old play, and it differs because σ_{k+1}(v) ≠ σ_k(v). □

## 3. Lemma CASC (PROVED, L-NEW): W-flat runs in a route-form piece are short
Setting.
- J is a piece. A W-FLAT RUN is a maximal run of consecutive transitions of J, numbered 0, 1, …, none a fallback, at which W is
  unchanged at every vertex of R.
- The LEVEL of v ∈ R \ {o} is ℓ(v) := |π_v| ∈ [1, |R| − 1]. By (R1), W(v) = π_v ⊕ w, so ℓ is constant on a W-flat run.
Statement. In a W-flat run, an R-vertex of level ℓ switches only at run steps 0, …, ℓ − 2. Hence it switches ≤ ℓ − 1 times in the
run, and no R-vertex switches at a run step ≥ |R| − 2.
Proof.
1. Let v ∈ R \ {o} be an Even vertex that switches at a run step.
   - W' = W on R, and τ is fixed, so TB applies with c = c_w; v ≠ c_w because c_w ∈ F ∪ {o} in route form.
   - By TB steps 2-5, v's new successor is the key-minimum among the optimal edges of the arena at v.
   - The optimal edges at v are the arena edges to TIED successors z, i.e. W(z) ⊕ v = W(v). These have level ℓ(v) − 1.
   - A tied successor in F could be the minimum only with a crossing, which J excludes. So the minimum is taken over the tied
     R-successors in the arena.
   - The KEY of z is its index in the odd mode. In the even mode it is the root-first index sequence of z's σ_{k+1}-route from o to
     z, preceded by a prefix (o's W-continuation) that is common to all of R and does not affect comparisons inside R.
   - The ARENA at v (SPEC S2) is {σ_k(v)} ∪ {z : Ξ_k(z) ▷ Ξ_k(σ_k v)}.
2. Ξ_k(z) = π_z ⊕ θ with θ constant (R1), so it depends only on σ_k along z's route, i.e. on levels < ℓ(z). The key of z depends only
   on σ_{k+1} along z's route. Forced Odd vertices never switch, and τ(o) is fixed.
3. Induction.
   - Let S_ℓ be the first run step from which no vertex of level ≤ ℓ switches. A level-1 vertex has the single tied successor o, so
     S_1 = 0. Claim: S_ℓ ≤ S_{ℓ−1} + 1.
   - Let j = S_{ℓ−1}, let v have level ℓ, and let z1 := σ_{j+1}(v), the key-minimum of the arena at step j.
   - From step j on, every lower level is fixed. So Ξ(z) and the R-part of key(z) are the same at all steps ≥ j, for every
     candidate z of v (step 2).
   - Take a step j' > j with σ_{j'}(v) = z1, and any z ≠ z1 in the arena at j'.
     - Then Ξ(z) ▷ Ξ(z1) ⊵ Ξ_j(σ_j v), because z1 was in the arena at j.
     - So z ≠ σ_j(v), and z was in the arena at j. Hence key(z) > key(z1).
     - So v keeps z1 at j'. By induction on j', v does not switch after j.
4. So S_ℓ ≤ ℓ − 1, which is the statement. □
- The proof uses only: route form (Ξ and W on R are π ⊕ a constant terminal), W flat on R, no crossing, TB, and the arena rule. It
  covers U1 pieces, P3′ pieces and c_θ = c_w alike.

## 4. Theorem U1 (PROVED, L-NEW): U1 pieces have polynomially many R-changing transitions, given their fallbacks
Statement. Let J be a U1 piece with f fallback transitions. The transitions of J that change Ξ, W or σ somewhere on R number at most
    |R| + f + K + (K + f + 1)(|R| − 2),   where   K ≤ (f + 1)(|R| − 1)(|R| − 2).
This is O((f + 1)|R|³). With f = 0 it is ≤ |R|³.
Proof.
1. κ_w-freeze (PROVED, L-NEW; N5-U1-box30.md §1). Let κ_w(ρ) be ρ's vertices above c_w. Then κ_w(π_v) is constant for all v ∈ R
   from transition |R| of J on.
   - This is P3′ step 1 (P-N5-NH §3, signed with gaps closed) with κ_w in place of κ, and with (R3) swapped. If
     κ_w(ρ) ≠ κ_w(ρ′), the top t of the difference is above c_w, hence above c_θ. Every other vertex of A_θ(ρ) Δ A_θ(ρ′) lies in
     the κ_w-difference or strictly between c_θ and c_w. So t tops both differences, and both frames decide the same way.
   - Under ¬H2 (λ_W(o) = o) the P3-1 repair transfers verbatim.
     - In U1 this case has c_w = o and H1 (c_θ ∈ F, c_θ ≺ o).
     - A vertex of C_W has κ_w = ∅.
     - A κ_w-strict switch from such a vertex closes a cycle through o whose top t is even and above o. By (F1) this moves the
       vertex's W cycle node off c_w = o at k+1, against (R1). So the case does not occur.
2. After the freeze, W(v) = (c_w, κ_w(π_v) ∪ P(w), |π_v| + ℓ(w)), which moves only through |π_v| ∈ [1, |R| − 1].
   - At non-fallback transitions W is non-decreasing (TB step 1; τ fixed).
   - So each v ∈ R \ {o} has ≤ |R| − 2 W-changes per fallback-free stretch. Hence K, the number of post-freeze transitions with a
     W-change on R, satisfies K ≤ (f + 1)(|R| − 1)(|R| − 2).
3. Every other post-freeze non-fallback transition is W-flat on R. These transitions form ≤ K + f + 1 W-flat runs, and by CASC each
   run has ≤ |R| − 2 transitions with a switch on R.
4. A change of Ξ or W on R needs a switch on R: Ξ = π ⊕ θ and W = π ⊕ w with θ, w constant, and forced vertices never move.
5. Sum: ≤ |R| transitions before the freeze, plus f fallbacks, plus K, plus (K + f + 1)(|R| − 2). □

## 5. Lemma WC (PROVED, L-NEW): w-changes when the W frame closes at o (W-CYC)
Statement. Let I be a crossing-free interval on which ¬H2 holds (constant on I by TC (i)), with f_I fallback transitions. Then the
number WC(I) of transitions of I that change w satisfies
    WC(I) ≤ (f_I + 1)(|R|² − 1) + f_I ≤ (f_I + 1)|R|².
Proof.
1. Under ¬H2, o's W-play returns to o. So o lies on its W-cycle C_W ⊆ R, and c_w is the most relevant vertex of C_W. o's W-play
   is C_W itself, so no vertex before c_w on it is more relevant than c_w. Hence w = (c_w, ∅, d), where d ∈ [0, |R| − 1] is the
   distance from o to c_w.
2. At non-fallback transitions w is non-decreasing (TB step 1 at o; τ fixed). The order compares reward(c_w) first, and rewards are
   injective (S1). So c_w changes ≤ |R| − 1 times per fallback-free stretch, each change raising reward(c_w) strictly. With c_w
   fixed, the path set is ∅ and d moves monotonically, so ≤ |R| − 1 changes per value of c_w.
3. Per fallback-free stretch: ≤ (|R| − 1) + |R|(|R| − 1) = |R|² − 1 w-changes. There are ≤ f_I + 1 stretches, plus ≤ f_I fallback
   transitions. □
- In particular, if c_w = o (the W frame is in route form under ¬H2), then w = (o, ∅, 0) is constant.

## 6. The reduction (READING: an assembly with P-N5-NH §4 and its fixes)
- P-N5-NH §4 with the fixes: inside a phase, #transitions ≤ poly(n) · (1 + X + Σ_I (ROI(I) + WC(I))).
- WC(I): Lemma WC under ¬H1 ∧ ¬H2 gives WC(I) ≤ (f_I + 1)|R|².
- ROI on route-form pieces:
  - P3′ for c_θ ≻ c_w;
  - Theorem U1 for c_w ≻ c_θ;
  - c_θ = c_w has no OTHER state. Under ¬H1 ∧ ¬H2 this is fixes §4. Under H1 ∧ H2, H3 holds and so (h). In the mixed patterns
    c_θ ≠ c_w.
- Pieces per interval:
  - Under H2: ≤ max(1, |F|) (fixes §3).
  - Under ¬H2 the W frame is in route form iff c_w = o. Then the pieces change only with θ (≤ |F|, by TF), with c_w (≤ |R| per
    fallback-free stretch, Lemma WC step 2), or at fallbacks.
- So (NH') reduces to:
  - (X), the crossings;
  - the number of fallbacks at OTHER states (CONJECTURE NFB-O: none);
  - U2 / U3 (a frame not in route form): there the CASC argument holds on sub-runs where the frame cycles through o and σ̄(o) are
    frozen (N5-U1T-box31.md §7, Lemma CASC-C, outside this packet). The open count is the number of re-routings of those cycles at
    W-ties.

## 7. Refuted forms and open items
- FALSE (U1-T), "after the κ_w-freeze each R-vertex has ≤ 2 Ξ-changes per value of its W-length". Two instances, both in 𝒞^1O, both
  checked with n5.py and check_sol2.py (Oink zlk OK, strategies verified):
  - Propagation version: L-RED, experiments/red/xing/instances/u1t_cex_n32.pg (l-red 959184d9, sha1 63dfd7850222…; n5.py 12 / 1).
    U1 piece 0..7 (|R| 28): post-freeze per-vertex Ξ-changes reach 7 (vertex 10, with σ(10) fixed). Own-switch revisits: vertex 6,
    σ = 2 → 18 → 19 → 18. TB and CASC hold there (§8).
  - Own-switch version: L-NEW, experiments/new/box31/instances/u1t_cex2_n32.pg (sha1 6162a26f6f87…; n5.py 9 / 1). U1 piece 0..5
    (c_θ = 27, c_w = 8, |R| 28) is one W-flat run, and vertex 23 (level 9) switches at all 5 steps.
- What survives: Theorem U1 counts transitions per piece, not changes per vertex. (OB_R) counted per vertex fails on L-RED's instance
  (88 > 28); counted in transitions it holds there (7 ≤ 28; Lead 20:19Z).
- OPEN: NFB-O (fallbacks at OTHER states); U2/U3 re-routings; (X); G-N5-TIME.

## 8. DATA (experiments/new/box31/; scripts assert 𝒞^1O, exactly one Odd choice vertex)
- tbarena.py, 20,000 random one-player arenas (seed 51): TB-odd 511 cases, TB-even 998, 0 violations.
- tbcheck.py on N5 runs: 4,000 random games (seed 311), 4,000 random o-cyclic 𝒞^1O (seed 312), 101 named instances: 0 violations.
- casccheck.py (CASC, and Theorem U1's bound per U1 piece) and nrcheck.py (WC):
| instance | sha1 (12) | n5.py it / fb | U1 pieces | TB cases | CASC switches | max R-changing / U1 piece | violations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| n5-exhaustive b5_os_n16 | 6297686b34b4 | 26 / 7 | 4 | 0 | 0 | 2 | 0 |
| n5-exhaustive b5_os_n20 | 655e787ba7d0 | 34 / 7 | 7 | 0 | 0 | 2 | 0 |
| n5-exhaustive b5_os_n24 | 3aca11030505 | 53 / 7 | 8 | 0 | 0 | 7 | 0 |
| red/xing x32_waves32 | a0565c6ea950 | 81 / 9 | 0 (4 pieces) | 0 | 0 | — | 0 |
| n5-exhaustive b6_xw_n32 | 307974780862 | 79 / 10 | 0 (2 pieces) | 0 | 0 | — | 0 |
| red/xing u1t_cex_n32 (L-RED) | 63dfd7850222 | 12 / 1 | 1 | 17 | 13 | 7 | 0 |
| box31 u1t_cex2_n32 | 6162a26f6f87 | 9 / 1 | 1 | 35 | 35 | 5 | 0 |
| box31 u1flat_best_n32 | 4a3c81223a32 | 10 / 2 | 1 | — | 43 | — | 0 |
All rows: check_sol2.py "zielonka(oink zlk) OK strategies verified". WC: max WC(I) = 1 over all intervals with ¬H1 ∧ ¬H2 (1,343
random, 72 named), 0 violations.
- On L-RED's u1t_cex_n32, TB's potential across vertex 6's revisit: pk(6) at states 0, 2, 3, 5 is (…, 24, 30, 21, 2, 6) >
  (…, 24, 30, 4, 18, 6) > (…, 7, 0, 16, 19, 6) > (…, 7, 0, 1, 18, 6). The potential is v's route key, not σ(v); 18's own route
  dropped between the visits.
- Abstract model (cascade.py, DATA on the model only): the W-flat process runs ≤ L − 1 steps at every depth tried (L 3-8); one vertex
  reaches 6 switches at L = 8.
