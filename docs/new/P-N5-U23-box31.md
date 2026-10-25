# Referee packet P-N5-U23: W-flat runs outside route form (U2, U3) inside a joint λ-phase of N5 (box 31 b)
L-NEW successor 11 (Opus 5.5, D15/D18). Finished 23:21Z by date -u. Lead request 23:2xZ ("freeze CASC-U2 / CASC-U3 as packet P-N5-U23"). Frozen at this commit;
corrections go in a fixes file, never here.
- Self-contained: definitions, statements, full proofs, and where each dependency is.
- Source text: docs/new/N5-U23-box31.md §1-§3. Where the two differ, this packet governs.
- Status: L-NEW's proofs, unrefereed. Lemmas about the candidate N5 (SPEC tie-breaks) on 𝒞^1O. Not a running-time bound, not a
  TARGET.md claim, not a step-4 pass. G-N5-TIME stays OPEN.
- Statements: Lemma CASC-U2 (§1), Lemma CASC-U3 (§2), both with a counting corollary. Open items (§3). Data (§4).

## 0. Objects and dependencies
- N5, SPEC, valuations, (V1), (F1), Ξ, W, θ, w, R (o ∈ R), F, H1, H2, phase (τ fixed), crossing-free: as in P-N5-U1-box31.md §0
  (RESULTS R24) and P-N5-NH-box30.md §0 (R22).
- Signed results used:
  - R24 Lemma R in the fully optimal form (fixes §1.1, invariant as in fixes §7.2);
  - R24 TB's CHOICE RULE (TB steps 3-5 with Lemma R; fixes §3, C-1). At an S4a step, every optimiser vertex v that is not its own
    W′-cycle node gets σ_{k+1}(v) = the key-minimum over the fully optimal arena edges with respect to W′. The key is the index if
    the cycle node has odd priority. Otherwise it is the root-first index sequence of the σ_{k+1}-play.
  - R24 CASC's induction (P-N5-U1 §3 step 3, with fixes C-2, C-3).
  - R15 (a); R19 (d) (SG); TC (i) (R22); the arena rule SPEC S2.
- A STRETCH is a maximal run of states of a phase with R, θ, w constant. Its transitions have both ends in it.
- A W-FLAT RUN is a maximal run of consecutive non-fallback transitions of a stretch with W unchanged at every vertex of R.
  - Inside a phase every non-fallback transition is an S4a step: S4b returns τ.
- U2: ¬H1 and c_θ := λ_Ξ(o) ≠ o, with the W frame in route form (H2, or λ_W(o) = o).
  - Under ¬H1 the honest cycle C_Ξ passes o, so c_θ ∈ R \ {o}.
- U3: ¬H2 and c_w := λ_W(o) ≠ o, with the honest frame in route form (H1, or λ_Ξ(o) = o). U23: ¬H1, ¬H2, c_θ ≠ o, c_w ≠ o.
- π_v (v ∈ R) is v's σ-route: the vertices of v's (σ, τ)-path before its first visit of o. "Tied": z is a tied successor of v if
  W(z) ⊕ v = W(v).

## 1. Lemma CASC-U2 (PROVED, L-NEW)
Statement. In a W-flat run of a U2 stretch, an R-vertex v of level ℓ(v) := |π_v| switches only at run steps 0, …, ℓ(v) − 2.
Proof.
1. Levels.
   - The W frame is in route form, so W(v) = π_v ⊕ w on R (P-N5-NH (R1), W half; it uses only H2 or λ_W(o) = o).
   - So ℓ is constant on a W-flat run. A tied successor z of v ∈ R \ {o} in R has ℓ(z) = ℓ(v) − 1, and v ∉ π_z.
2. Honest values are route functions with constant terminals.
   - Every v ∈ R has λ_Ξ(v) = c_θ: v's honest play follows σ (and forced edges) to o or into C_Ξ, and ends on C_Ξ, whose top is c_θ.
     λ_Ξ is constant in the phase.
   - For v ∈ R \ {o, c_θ}, v is not its own honest cycle node, so (V1) gives Ξ(v) = v ⊕ Ξ(σ(v)).
   - Ξ(c_θ) = (c_θ, ∅, 0), and Ξ(o) = θ is constant on the stretch.
   - Iterating (V1) along v's σ-path until its first vertex in {c_θ, o} (a prefix of π_v, since that path meets o at the end of π_v):
     Ξ(v) = (that prefix) ⊕ (a constant). So Ξ(v) depends only on σ at the vertices of π_v.
   - σ̄(o) and the other vertices of C_Ξ enter only through the constants θ and Ξ(c_θ).
3. The choice rule at a switching Even v ∈ R \ {o}.
   - v is not its own W cycle node: c_w ∈ F under H2, and c_w = o otherwise.
   - W′ = W on R at a W-flat transition. So the fully optimal arena edges at v that lie in R are the tied arena successors in R.
   - A tied successor in F could be the key-minimum only with a crossing, which the stretch excludes.
   - Keys in the even mode: the root-first sequence of z's σ_{k+1}-play from c_w is a prefix (o's W-continuation, common to all of R),
     followed by z's σ_{k+1}-route. Comparisons inside R therefore depend only on σ_{k+1} at the vertices of π_z.
   - The arena at v is {σ_k(v)} ∪ {z : Ξ_k(z) ▷ Ξ_k(σ_k v)} (SPEC S2).
4. Induction: R24 CASC step 3 verbatim, with steps 1-3 in place of R24 CASC steps 1-2.
   - Let S_ℓ be the first run step from which no vertex of level ≤ ℓ switches.
   - S_1 = 0: the only tied R-successor of a level-1 vertex is o.
   - Let j = S_{ℓ−1} and z1 := σ_{j+1}(v). For j′ > j with σ_{j′}(v) = z1, take any tied arena candidate z ≠ z1 at j′.
     - Ξ_{j′}(z) = Ξ_j(z), and the key of z is unchanged (steps 2 and 3: z's route lies at levels ≤ ℓ − 1, which are fixed from j on).
     - So Ξ_j(z) ▷ Ξ_j(z1) ⊵ Ξ_j(σ_j v), hence z ≠ σ_j(v) and z was in the arena at j, so key(z) > key(z1).
     - So v keeps z1, and S_ℓ ≤ S_{ℓ−1} + 1. □
Corollary (PROVED [f], L-NEW). Let a U2 stretch have f fallback transitions and K_W non-fallback transitions with a W-change on R.
Then its transitions that change Ξ, W or σ on R number ≤ f + K_W + (K_W + f + 1)(|R| − 2).
Proof.
- A change of Ξ or W on R needs a switch on R (step 2 and (R1); forced vertices and τ(o) are fixed).
- W-flat runs number ≤ K_W + f + 1.
- By the lemma a run has switches only at steps ≤ |R| − 3, since levels are ≤ |R| − 1. □

## 2. Lemma CASC-U3 (PROVED, L-NEW)
Setting.
- A U3 or U23 stretch. Under ¬H2, o lies on its W-cycle C_W = o → A1 → c_w → A2 → o: A1 is o's W-path to c_w, and A2 is c_w's σ-route
  back to o. w = (c_w, ∅, d), with d the W-length of o (R24 Lemma WC step 1).
- KIND: v ∈ R \ {o} is of kind A if c_w ∈ π_v, and of kind B otherwise. c_w and the vertices of A1 are kind A; those of A2 are kind B.
- An EVENT is a switch of an Even vertex of R that changes that vertex's kind, or a switch of c_w itself. c_w is its own W cycle node,
  so its choice is SPEC S1 (v) / FIX 2, not the choice rule.
- An EVENT-FREE SUB-RUN is a maximal part of a W-flat run with no event, with its steps numbered 0, 1, ….
Statement. In an event-free sub-run:
- (i) a kind-B vertex v switches only at sub-run steps ≤ |π_v| − 2;
- (ii) a kind-A vertex v whose σ-path reaches c_w after λ(v) steps switches only at sub-run steps ≤ L_B + λ(v) − 3, where L_B is the
  largest |π| over kind B (the bound is read as −1, i.e. never, for λ(v) = 1);
- (iii) no R-vertex switches at a sub-run step ≥ 2|R| − 4.
Proof.
1. Kinds are constant on the sub-run.
   - A vertex's kind changes only if it, or a vertex on its route, switches to a successor of the other kind.
   - If v switches from kind X to a successor of kind X, its kind and every kind upstream are unchanged. Otherwise the switch is an
     event.
2. Kind B. A kind-B route consists of kind-B vertices.
   - W(v) = π_v ⊕ w: the W-play of v is π_v, then o, then A1. So v's W-length is |π_v| + d.
   - A tied successor z of a kind-B v has W-length |π_v| + d − 1. It is either kind B with |π_z| = |π_v| − 1, or kind A, which would be
     an event.
   - Honest values: under H1, Ξ(v) = π_v ⊕ θ (P-N5-NH (R1)). If λ_Ξ(o) = o, Ξ(v) = π_v ⊕ (o, ∅, 0). Under ¬H1 (U23), §1 step 2 applies.
     In every case Ξ(v) depends only on σ at π_v, with constant terminals.
   - Keys of kind-B candidates: the root-first sequence of the W-play from c_w is (A1 part, o) followed by the route. That prefix is
     common to all kind-B candidates.
   - The induction of §1 step 4 over |π| on kind B gives (i). The base |π| = 1 has the single kind-B candidate o.
3. Kind A, with root c_w.
   - For kind-A v, the σ-path from v reaches c_w after λ(v) steps, and W(v) = (that path) ⊕ (c_w, ∅, 0) by (V1) along it. So the
     W-level is λ(v).
   - A tied successor of kind-A v has W-level λ(v) − 1. It is either kind A, or kind B (an event).
   - Honest values: Ξ(v) = (the σ-path from v to the first of c_w, o, c_θ) ⊕ (its value), by (V1), where o and c_θ carry constants.
     Ξ(c_w) = c_w ⊕ Ξ(σ(c_w)), where σ(c_w) is the first vertex of A2 (kind B).
   - From step L_B − 1 on, kind B does not switch, by (i). Also c_w does not switch on the sub-run. So Ξ(c_w), and hence every kind-A
     honest terminal, is constant from step L_B − 1.
   - Keys of kind-A candidates are their σ_{k+1}-paths to c_w.
   - Run the induction of §1 step 4 on kind A over λ, from step T := L_B − 1. Level 1 has the single candidate c_w, so it never
     switches. For λ ≥ 2, S^A_λ ≤ T + λ − 1, i.e. switches only at steps ≤ L_B + λ − 3. This is (ii).
4. (iii): L_B ≤ |R| − 1 and λ ≤ |R| − 1. □
Corollary (PROVED [f], L-NEW). Let a U3 or U23 stretch have f fallbacks, K_W non-fallback W-changes on R, and E event transitions.
Then its R-changing transitions number ≤ f + K_W + E + (K_W + f + E + 1)(2|R| − 4).
- What is NOT an event:
  - re-routings of A2 by kind-B vertices to kind-B targets;
  - re-routings of A1 by kind-A vertices to kind-A targets.
  Both are covered by (i) and (ii). This supersedes the frozen-cycle hypothesis of Lemma CASC-C (N5-U1T-box31.md §7).

## 3. Open items (exact)
- (E) The number of event transitions per W-flat run in U3 / U23: kind crossings, and c_w's own switches.
- (K_W) The number of non-fallback W-changes on R in U2 / U3 / U23 stretches.
  - Outside route form the honest order does not see every coarse W-difference, so R24's κ_w-freeze does not transfer as it stands.
- READING: with R24 §6, (NH') reduces to (X), NFB-O, (E) and (K_W).
- DATA (N5-U23-box31.md §5): every (E) and (K_W) transition seen is TAME in L-SI's sense (78 of 78). So neither can be charged to
  L-SI's J (Theorem FB).

## 4. DATA (experiments/new/box31/u23check.py, u23climb.py, tamecheck.py; 𝒞^1O asserted)
- Named 𝒞^1O instances: U2 stretches on sc32, wd16_s2, wf0_cex_n16, nfb16, obr_n32 and x31_lem_t32; U3 stretches on oc16_s2. They
  contain 0 W-flat switches, so the checks are vacuous there.
- experiments/new/box31/instances/u3ev_n16.pg (n 16, sha1 fc8905296787…, n5.py 6 / 0, check_sol2.py "zielonka(oink zlk) OK strategies
  verified"): one U3 stretch; 8 W-flat switches, all events (7 kind crossings, 1 c_w switch).
- No U2 W-flat switch was reached by the named sweep, by 3,000 random runs (seed 3301) or by two climbs. So CASC-U2 rests on its proof.
- 0 violations of (i), (iii) and CASC-U2 anywhere. (ii) is not checked separately; (iii) is.
