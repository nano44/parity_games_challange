# N5 on o-cyclic 𝒞^1O, box 31: kind (T) in U1, then U2, U3, W-CYC
L-NEW successor 11 (Opus 5.5, D15/D18). Written 2026-10-24 20:23Z onward (date -u). Labels (L40): PROVED (by whom), READING,
CONJECTURE, FALSE, OPEN, DATA. Every PROVED here is L-NEW's, unrefereed.
- Notation: P-N5-NH-box30.md (pinned c7981ee, never edited) with its fixes file P-N5-NH-fixes-box30.md; N5-U1-box30.md (U1, kinds
  (L) and (T)). Phase = joint λ-phase with τ fixed; R, F, crossing-free interval I, piece J, π_v, θ, w, c_θ, c_w as there.
- Scope: lemmas about the candidate N5 (SPEC tie-breaks). Not a running-time bound, not a TARGET.md claim, not a step-4 pass.
  G-N5-TIME stays OPEN.
- ASSUMPTION (stated once, used where marked [f]): f := number of S4c fallback transitions in the stretch considered. CONJECTURE
  NFB-O says f = 0 at OTHER states; nothing here assumes it, the bounds carry f.

## Summary
| item | label | where |
| --- | --- | --- |
| U1-T (≤ 2 Ξ-changes per R-vertex per W-length value, after the κ_w-freeze) | **FALSE** (u1t_cex2_n32) | §1 |
| Lemma R: VJ's restricted graph keeps every optimal edge | PROVED | §2 |
| Lemma TB: S4a's tie-break is a monotone potential (min index if c odd; lexmin root-first BFS sequence if c even) | PROVED | §3 |
| Lemma CASC: in a W-flat run of a route-form piece, a level-ℓ R-vertex switches only at run steps ≤ ℓ − 2 | PROVED | §4 |
| Theorem U1: a U1 piece with f fallbacks has ≤ \|R\| + f + (K + f + 1)(\|R\| − 2) + K R-changing transitions, K ≤ (f+1)(\|R\|−1)(\|R\|−2) | PROVED [f] | §5 |
| Lemma WC (W-CYC): under ¬H2 on I, WC(I) ≤ (f_I + 1)\|R\|² | PROVED [f] | §6 |
| Lemma CASC-C: CASC outside route form (U2, U3) on sub-runs where the frame cycles through o are frozen | PROVED | §7 |
| Residual: re-routings of the frame cycles through o at W-ties (U2, U3) | OPEN | §7 |
| Abstract cascade model: run length ≤ L − 1 always; per-vertex switches reach ℓ − 2 | DATA (model) | §8 |

## 1. FALSE: U1-T
- First refutation: L-RED, experiments/red/xing/instances/u1t_cex_n32.pg (l-red 959184d9, sha1 63dfd785…; Lead re-run 12 / 1,
  Oink OK). Mechanism there (L-RED, Lead 20:19Z): mostly propagation (Ξ(10) rises at all 7 transitions through downstream route
  changes while σ(10) is fixed), plus own-switch revisits (vertex 6: σ 2 → 18 → 19 → 18; vertex 14: 25 → 5 → 28 → 25). My instance
  below, found independently, is renamed u1t_cex2_n32 (Lead 20:23Z); it refutes the own-switch version too (vertex 23 switches at
  every step of one W-flat run). TB and CASC on L-RED's instance: §10.
- Statement refuted (N5-U1-box30.md §2): "after the κ_w-freeze, each R-vertex has ≤ 2 Ξ-changes per value of its W-length".
- Instance: experiments/new/box31/instances/u1t_cex2_n32.pg (n 32, sha1 6162a26f6f87788b345854887bf0ed35b502e637). Found by
  experiments/new/box31/cascclimb.py (mode flat, seed 3, seeded from box29/instances/u1_n32.pg).
- Checks: n5.py 9 iterations, 1 fallback (not inside the piece); check_sol2.py "zielonka(oink zlk) OK strategies verified";
  box21 trace() == n5.run.
- Witness (runinfo.py; box29/u1vertex.py): states 0..5 form one U1 piece (c_θ = 27, c_w = 8, |R| = 28), κ_w-freeze at 0, and the
  whole piece is one W-flat run (W unchanged on R at all 5 transitions, no fallback). R-vertex 23 (W-level 9) switches at all 5
  transitions: 5 strict Ξ-changes (SG) at one W-length value. Vertices 5, 7, 11, 17, 18, 22 (level 8) switch 3 times each.
  u1vertex.py: post-freeze R-changes per vertex max 5, total 38.
- Mechanism: exactly the attack spec of box 30 §3 (a W-tight DAG whose lower layers improve and re-open honest-improving tied
  edges higher up), with the BFS tie-break (c_w = 8 has even priority). Its size is bounded by CASC (§4): 5 ≤ ℓ − 1 = 8.

## 2. Lemma R (PROVED, L-NEW): the restriction keeps optimal edges
Setting: one call Engine.evaluate(strat) (SPEC S1; si.py l.78-205), at a cycle node c with region R_c, after the loop over u ∈ R_c
with rank(u) > rank(c) (decreasing rank). Call the evaluated game's Odd player the optimiser.
Statement. Let x ∈ R_c and y a successor of x in R_c such that y is an optimal choice for the optimiser at x in the (c, P)
components (the value through y, extended by x, has the same cycle node and path set as x's optimal value). Then x → y survives
the restriction. Consequently x's choice is made among optimal edges only: in the longest-path mode it is the first successor in
list order of maximum length among survivors, in the BFS mode the first-discovered one, and every fully optimal edge competes.
Proof.
- Invariant (by induction over the processed u, decreasing rank): every surviving edge joins two vertices with the same membership
  in each processed u's set M_u. At step u, for "Even likes u" (M = vertices reaching c without passing u): u and every q ∈ M keep
  only edges into M; a vertex q ∉ M ∪ {u} with a surviving edge into M would reach c avoiding u, i.e. q ∈ M. For "Odd likes u"
  (M = vertices reaching u without passing c): every q ∈ M \ {u} keeps only edges into M; q ∉ M with an edge into M would reach u
  avoiding c. So after step u, either all remaining paths from a vertex to c avoid u or all pass u, and the higher processed
  vertices are already decided the same way along every surviving edge.
- A deleted edge x → y at step u has y ∉ M while x ∈ M or x = u, and (invariant) x, y agree on every higher processed vertex.
  - Even likes u: through y every path to c passes u (u ∈ P), while x's best avoids u (x ∈ M); or x = u and y ∉ M closes a cycle
    through u (top ≥ u, Even's) before reaching c. Either way strictly worse for the optimiser: u is the most relevant vertex where
    the two path sets can differ.
  - Odd likes u: through y no path reaches u (u ∉ P), while x ∈ M collects u. Strictly worse for the optimiser.
- So no optimal edge is ever deleted. Lengths are then computed on the survivors (S1 (iv)); the BFS distance and the longest
  distance are the optimal lengths, so the survivors of optimal length are exactly the fully optimal edges. □
- DATA: tbarena.py, 20,000 random arenas (seed 51), 0 cases where an optimal current edge lost (part of TB's check, §3).

## 3. Lemma TB (PROVED, L-NEW): the tie-break of S4a is a monotone potential (all games, any transition)
Statement. Let k → k+1 be a transition at which S4a is applied (I_σ ≠ ∅, no fallback). Let W_k = value of (σ_k, τ_k) and
W' = value of (σ_{k+1}, τ_k) in G. Let v be an Even vertex with σ_{k+1}(v) ≠ σ_k(v), W'(v) = W_k(v), and v not its own W-cycle
node. Let c be the cycle node of W_k(v).
- (TB-odd) If c has odd priority: σ_{k+1}(v) < σ_k(v) as vertex indices.
- (TB-even) If c has even priority and W' = W_k on v's whole σ_k-play from v to c: pk_{k+1}(v) <lex pk_k(v), where pk(v) is the
  root-first sequence of vertex indices of v's play from c (excluded) back to v.
Proof.
1. σ_{k+1} is the optimiser's counterstrategy of one call Engine.evaluate on the dual of the arena H_k (n5.py S4a), so
   W'(x) = W*_{H_k}(x), the H_k-optimal value, for every x; and σ_k is a strategy of H_k, so W*_{H_k} ⊵ W_k pointwise ((F1)).
2. If W'(x) = W_k(x) then σ_k(x) is an optimal edge of H_k at x: W*(x) ⊵ W*(σ_k x) ⊕ x ⊵ W_k(σ_k x) ⊕ x = W_k(x) = W*(x).
3. In the dual, c's parity flips: c odd in G gives the longest-path mode, c even gives the BFS mode (SPEC S1 (iv)).
4. (TB-odd) By Lemma R and step 2, σ_k(v) is among the survivors of maximal length; the recursion takes the first such in list
   order (hs[x] is sorted: n5.py passes sorted(opt[v])). So σ_{k+1}(v) ≤ σ_k(v), and ≠.
5. (TB-even) BFS over predecessors in increasing index, layers in FIFO order. By induction on the layer, the queue order of a layer
   is the lex order of the root-first index sequences of the BFS-tree paths, and each tree path is the lexmin over all surviving
   shortest paths (a vertex is discovered from its earliest-queued surviving successor in the previous layer). By step 2 at every
   vertex of v's old play and Lemma R, that play is a surviving shortest path, so the tree path of v (= its σ_{k+1}-play) is lex ≤
   it, and ≠ since σ_{k+1}(v) ≠ σ_k(v). □
- DATA: tbarena.py 20,000 random arenas (seed 51, half layered): TB-odd 511 cases, TB-even 998, 0 violations. tbcheck.py on N5 runs
  (4,000 random games seed 311, 4,000 random o-cyclic 𝒞^1O seed 312, 101 named instances, u1t_cex2_n32): 0 violations.
- Remark (the "lexicographic perturbation" reading of the brief): S4a's choice is the optimum of the arena for the perturbed
  objective (W, then the tie-break key); TB says the perturbation is never lost while W stands still.

## 4. Lemma CASC (PROVED, L-NEW): W-flat runs in a route-form piece are short
Setting. J is a piece (both frames in route form; phase, R, θ, w constant; crossing-free). A W-FLAT RUN is a maximal run of
consecutive transitions of J, numbered 0, 1, …, none a fallback, with W unchanged at every vertex of R. The W-level of v ∈ R is
ℓ(v) := |π_v| (W(v) = π_v ⊕ w, so ℓ is constant on the run). L := max ℓ over R \ {o} ≤ |R| − 1.
Statement. In a W-flat run, an R-vertex of level ℓ switches only at run steps 0, …, ℓ − 2. Hence each R-vertex switches ≤ ℓ − 1
times in the run, and no R-vertex switches at a step ≥ L − 1.
Proof.
1. At each step, for an Even v ∈ R \ {o} that switches: W' = W on R, so TB applies with c = c_w (v ≠ c_w: c_w ∉ R \ {o}).
   v's new successor is the key-minimum over the optimal edges of the arena at v (TB steps 2-5). Optimal edges at v are the arena
   edges to TIED successors z (W(z) ⊕ v = W(v)), which have level ℓ(v) − 1. A tied successor in F would be chosen only with a
   crossing, so on the run the minimum lies in R, and it is also the minimum over the tied R-successors in the arena.
   - Key: in the odd mode the index; in the even mode the root-first sequence of z's σ_{k+1}-route from o to z (the common prefix
     through o's W-continuation is the same for all of R and is dropped).
   - Arena at v (SPEC S2): {σ_k(v)} ∪ {z : Ξ_k(z) ▷ Ξ_k(σ_k v)}.
2. On R, Ξ_k(z) = π_z ⊕ θ (fact (R1)); with θ constant, Ξ_k(z) depends only on σ_k along z's route, i.e. on levels < ℓ(z). The key of
   z depends only on σ_{k+1} along z's route. Forced Odd vertices of R never switch; o's τ is fixed.
3. Induction. Let S_ℓ be the first run step from which no vertex of level ≤ ℓ switches. Level-1 vertices have the single tied
   successor o, so S_1 = 0. Claim S_ℓ ≤ S_{ℓ−1} + 1.
   - Let j = S_{ℓ−1}, v of level ℓ, and z1 := σ_{j+1}(v), the key-minimum of the arena at step j. From step j on, every lower level
     is fixed, so Ξ(z) and key(z) are the same at all steps ≥ j for every candidate z of v (step 2).
   - At a step j' > j with σ_{j'}(v) = z1: any z ≠ z1 in the arena has Ξ(z) ▷ Ξ(z1) ⊵ Ξ_j(σ_j v) (z1 was in the arena at j). So
     z ≠ σ_j(v) and z was in the arena at j, hence key(z) > key(z1). v keeps z1. By induction on j', v never switches after j.
4. So S_ℓ ≤ ℓ − 1, which is the statement. □
- The proof uses only: route form (Ξ and W on R are route-additive with constant terminal values θ, w), W flat on R, TB, the
  arena rule. It holds in U1, in P3′ pieces and with c_θ = c_w alike.
- DATA (casccheck.py): u1t_cex2_n32 35 switches, wf0_cex_n16, u1_n32, 101 named instances: 0 violations. Climb cascclimb.py
  (mode flat, every candidate checked, ~10⁵ candidates): 0 violations.

## 5. Theorem U1 (PROVED [f], L-NEW): U1 pieces are polynomial
Statement. Let J be a U1 piece with f fallback transitions. The transitions of J with a change on R (Ξ, W or σ on R) number at most
    |R| + f + K + (K + f + 1)(|R| − 2),   K ≤ (f + 1)(|R| − 1)(|R| − 2),
so O((f + 1)|R|³); with f = 0 (NFB-O) at most |R| + (|R|−1)(|R|−2) + ((|R|−1)(|R|−2) + 1)(|R| − 2) ≤ |R|³.
Proof.
1. κ_w-freeze (PROVED, L-NEW, N5-U1-box30.md §1): κ_w(π_v) is constant from transition |R| of J on. Under λ_W(o) = o (¬H2) its
   step 1 needs the P3-1 repair; it transfers verbatim (L-NEW): here c_w = o and H1 (c_θ ∈ F, c_θ ≺ o), a C_W vertex has κ_w = ∅,
   and a κ_w-strict switch from it closes a cycle through o whose top t is even and above o, against x's cycle node c_w = o at k+1.
2. After the freeze, W(v) = (c_w, κ_w(π_v) ∪ P(w), |π_v| + ℓ(w)) moves only through |π_v| ∈ [1, |R| − 1]. Between fallbacks, W is
   non-decreasing (TB step 1, (F1), τ fixed), so each v ∈ R \ {o} has ≤ |R| − 2 W-changes per fallback-free stretch: K transitions
   with a W-change on R, K ≤ (f + 1)(|R| − 1)(|R| − 2).
3. The other non-fallback transitions after the freeze are W-flat on R; they form ≤ K + f + 1 W-flat runs. By CASC each run has ≤
   L − 1 ≤ |R| − 2 transitions with a switch on R.
4. A change of Ξ or W on R needs a switch on R (Ξ = π ⊕ θ, W = π ⊕ w, θ, w constant; forced vertices fixed).
5. Sum: ≤ |R| (before the freeze) + f + K + (K + f + 1)(|R| − 2). □
Consequences (READING: assembly with the packet's §4 and its fixes).
- With P3′ (c_θ ≻ c_w) and the c_θ = c_w case (no OTHER state there: fixes §4 under ¬H1 ∧ ¬H2; H3 and so (h) under H1 ∧ H2;
  c_θ ≠ c_w in the two mixed patterns), every route-form OTHER piece has polynomially many
  R-only transitions, given its fallbacks.
- The number of route-form pieces per interval: under H2 ≤ max(1, |F|) (Corollary, fixes §3); under ¬H2 the W frame is in route form
  iff c_w = o, and w = (o, ∅, 0) there, so pieces change only with θ (≤ |F|, TF), with c_w (≤ (f + 1)|R|, Lemma WC step 2) or at
  fallbacks.
- So (NH') is reduced to: (X) (crossings), the fallback count at OTHER states (NFB-O), and U2 / U3 (§7).

## 6. Lemma WC (PROVED [f], L-NEW): W-CYC
Statement. Let I be a crossing-free interval with ¬H2 (TC (i): constant on I), with f_I fallback transitions. Then
WC(I) ≤ (f_I + 1)(|R|² − 1) + f_I ≤ (f_I + 1)|R|². In particular WC(I) is polynomial whenever the fallbacks are.
Proof.
1. Under ¬H2, o lies on its own W-cycle C_W ⊆ R, and c_w = λ_W(o) is the most relevant vertex of C_W. o's W-play is C_W itself,
   so no vertex before c_w on it is more relevant than c_w: w = (c_w, ∅, d) with d ∈ [0, |R| − 1] the distance from o to c_w.
2. At non-fallback transitions w is non-decreasing ((F1), τ fixed). The order compares reward(c_w) first; rewards are injective, so
   c_w changes at most |R| − 1 times per fallback-free stretch (each change strictly increases reward(c_w), c_w ∈ R). With c_w
   fixed, the path set is ∅ and d moves monotonically: ≤ |R| − 1 changes.
3. Per fallback-free stretch: ≤ (|R| − 1) changes of c_w plus ≤ |R|(|R| − 1) changes of d (≤ |R| values of c_w), so ≤ |R|² − 1
   w-changes. There are ≤ f_I + 1 such stretches, plus ≤ f_I fallback transitions. □
- If c_w = o (W route form under ¬H2), w = (o, ∅, 0) is constant: WC counts only changes into or out of c_w = o and the U3 lengths.
- DATA (nrcheck.py): 1,343 intervals with ¬H1 ∧ ¬H2 in 1,500 random o-cyclic 𝒞^1O runs (seed 3101): max WC(I) = 1; 0 violations of
  the bound; named instances in §9.
- With TC's Consequence (≤ 1 + WC(I) OTHER blocks under ¬H1 ∧ ¬H2), the OTHER-block count per interval is polynomial given f_I.

## 7. U2 and U3: Lemma CASC-C (PROVED, L-NEW) and the residual (OPEN)
Why CASC fails outside route form. CASC needs one order that serves both frames: the honest value of a candidate z must depend only on
vertices of lower W-level. Outside route form the two frames have different roots:
- U3 (¬H2, c_w ≠ o): W-levels count the distance to c_w ∈ C_W; honest values (H1) count the route to o. A vertex whose route
  passes c_w before o has an honest value that depends on c_w's arc to o, whose vertices have HIGH W-levels.
- U2 (¬H1, c_θ ≠ o): honest values are paths to the honest cycle C_Ξ through o (with σ̄(o) = e* ∈ R); W-levels count the route
  to o. The honest value of a vertex depends on C_Ξ.
Lemma CASC-C. Let C be the union of the frame cycles through o that exist (C_Ξ if ¬H1, C_W if ¬H2). In a W-flat run (θ, w, R, τ
constant, no fallback, W unchanged on R) consider a sub-run on which no vertex of C \ {o} switches and σ̄(o) is constant. Then a
vertex of R \ C of W-level ℓ (now: the W-length, the distance to the W cycle node) switches only at sub-run steps ≤ ℓ − 2.
Proof. As CASC. For z ∈ R \ C, the honest play follows z's σ-route to its first vertex u ∈ C, and Ξ(z) = path(z → u) ⊕ Ξ(u) by (V1).
Along that path the W-level drops by one per step (the W-play is the same σ-path, and c_w ∈ C is not passed before u), and Ξ(u)
is fixed while C and σ̄(o) are frozen. Keys (TB) depend on the W-path, which also stays below. Vertices of C do not switch by
hypothesis; level-1 vertices of R \ C have one candidate. The induction of CASC step 3 runs verbatim. □
Residual (OPEN). The number of C-re-routings inside W-flat runs: a vertex of C_W (resp. C_Ξ) switching to a tied successor, or σ̄(o)
changing, with W flat on R. Each one ends a sub-run; the rest is bounded by CASC-C (≤ L − 1 switching steps per sub-run).
- What a C_W re-routing must preserve (L-NEW, READING): w (so c_w and the distance d from o), and o on the cycle (else τ(o) leaves R:
  a crossing). So a vertex of the arc o → c_w re-routes into that arc, and a vertex of the arc c_w → o into that arc.
- DATA: nrcheck.py on 1,500 random runs (seed 3101): 18 U2/U3 stretches, 1 W-flat switch, which is a C-re-routing; 0 CASC-C
  violations. Named instances and the climb nrclimb.py (fitness: W-flat switches outside route form; every candidate checked): §9.

## 8. The abstract cascade model (DATA on the model, not on N5)
experiments/new/box31/cascade.py: the CASC setting as a pure combinatorial process (layered tight DAG, honest values = top of the
symmetric difference on V_mid, arena = current ∪ honest-improving, choice = min index or lexmin root-first sequence). Hill climbs
(4,000 candidates each) on depth L 3-8, width 3:
- run length to the fixpoint: always ≤ L − 1 (max L − 1 reached at every L), as CASC proves;
- max switches of one vertex: BFS mode 2, 3, 3, 4, 6 at L = 3, 4, 5, 6, 8; index mode ≤ 2 (= degree − 1 here).
So U1-T fails in the model too, and CASC's run bound is tight there.

## 9. Re-verification and further data
Every instance cited here or in box 30 was re-run with experiments/new/n5.py and experiments/new/check_sol2.py (Oink 8fbf0a7 built
by scripts/setup_oink.sh in this container) on 2026-10-24, finished before 20:27Z by date -u:
| instance | sha1 (first 12) | n5.py iterations / fallbacks | check_sol2.py |
| --- | --- | --- | --- |
| box29/instances/wf0_cex_n16.pg | 1de2ff5bcfb4 | 40 / 8 | zielonka(oink zlk) OK strategies verified |
| box29/instances/u1_n32.pg | f9577ca9ce16 | 16 / 1 | same |
| box31/instances/u1t_cex2_n32.pg (§1) | 6162a26f6f87 | 9 / 1 | same |
| box31/instances/u1flat_best_n32.pg (flat climb final) | 4a3c81223a32 | 10 / 2 | same |
| box31/instances/p3long_n14.pg (thw climb final) | 887cd20ac358 | 10 / 0 | same |
| box31/instances/nr_u23_n32.pg (nrclimb final) | d96f5603c625 | 14 / 1 | same |
| n5-exhaustive/instances/b5_os_n14.pg (thw seed) | 74e10e25d2b8 | 22 / 6 | same |
Further data (DATA):
- u1flat_best_n32: one U1 piece, one W-flat run of 5 transitions, vertices 15 and 23 (level 9) switch at all 5 steps; 43 R-switches;
  CASC and TB: 0 violations.
- p3long_n14 (for REFEREE's request, R-N5-NH §5): a P3′ piece (c_θ ≻ c_w) of 9 transitions, |R| = 11, a change on R at all 9, the
  last κ-change at transition 9 (P3′ step 1 allows ≤ |R| − 1 = 10), count 9 ≤ |R| + (|R| − 2)(|R| − 1) = 101. REFEREE's probe had
  at most 6 transitions and last κ-change 0. The climb (cascclimb.py thw) from b5_os_n14 got no further.
- nr_u23_n32: 3 stretches outside route form (U2 ∧ U3), 32 switches in W-flat runs, 5 of them C-re-routings, max 4 switches of one
  vertex in a run, longest W-flat run 7; CASC-C: 0 violations; TB: 34 cases, 0 violations.
- Named instances (box2x/instances, box29/out, n5-exhaustive, red/xing, box31): 155 route-form pieces (43 U1), 124 W-flat runs,
  CASC 0 violations; 72 intervals under ¬H1 ∧ ¬H2, max WC(I) = 1; 17 stretches outside route form, 0 CASC-C violations.

## 10. TB and CASC on L-RED's instance (Lead request 20:23Z)
experiments/red/xing/instances/u1t_cex_n32.pg (sha1 63dfd7850222…), canonical start. tbcheck.py: 17 TB-even cases, 0 violations.
casccheck.py: one U1 piece 0..7 (c_θ = 27, c_w = 8, |R| = 28), W-flat runs = transitions 1..2 and 3..7 (transitions 0 and 2 change W
on R, kind (L)), 13 switches, 0 CASC violations (vertex 14, level 9: run steps 0, 2, 3 ≤ 7; vertex 6, level 7: steps 0 and 1).
Why the revisit 18 → 19 → 18 at vertex 6 does not contradict TB. TB's potential is not σ(v) but v's whole route key pk(v), the
root-first index sequence from c_w = 8. Along the run (states 0, 2, 3, 5; W(6) = (8, length 9) throughout):
- state 0, σ(6) = 2:  (26, 27, 13, 23, 24, 30, 21, 2, 6)
- state 2, σ(6) = 18: (26, 27, 13, 23, 24, 30, 4, 18, 6)     21 → 4 at position 7
- state 3, σ(6) = 19: (26, 27, 13, 23, 7, 0, 16, 19, 6)      24 → 7 at position 5
- state 5, σ(6) = 18: (26, 27, 13, 23, 7, 0, 1, 18, 6)       16 → 1 at position 7
Strictly lex-decreasing at every switch. Between states 2 and 5 the route of 18 itself moved down (prefix (…, 24, 30, 4) to
(…, 7, 0, 1)), so "18" at state 5 is a lex-smaller route than "18" at state 2; the comparison 18 vs 19 changed because Ξ and keys
below changed, exactly the case TB allows. Vertex 14 (W-length 11 throughout states 1-7): pk goes (…, 21, 2, 6, 25, 14) →
(…, 16, 19, 3, 5, 14) → (…, 1, 18, 6, 28, 14) → (…, 1, 18, 6, 25, 14), again strictly decreasing at each switch (the last step at the
same prefix, 28 → 25).
