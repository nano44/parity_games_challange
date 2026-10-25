# Referee packet P-N5-RL: blocked edges, the confined optimum, the free freeze, and where an NJB violation must live (box 10)
L-SI successor 5 (Opus 5.5, D15/D18, L37/L40). Written 2026-10-25 11:15Z (date -u), at the Lead's request (11:14Z). Frozen at its
commit: corrections go in a fixes file, never here.
- Self-contained: definitions, statements, full proofs, the location of every dependency, the data and the scripts that produce it.
- Source text: docs/si/N5-RL-box10.md (lane write-up, l-si e625289). Where they differ, this packet governs.
- Status: L-SI successor 5's proofs, unrefereed. Labels: PROVED (L-SI succ. 5), PROVED CONDITIONAL on (P), CONJECTURE, FALSE, DATA.
  - Everything is on 𝒞^1O: exactly one Odd vertex o with out-degree > 1. Every script asserts it.
- These are lemmas about the candidate N5. They are not a running-time bound, not a TARGET.md claim, and not a step-4 pass.
  G-N5-TIME stays OPEN.
- Statements to sign:

| § | statement | label | uses (P) | uses CN-LAST |
| --- | --- | --- | --- | --- |
| §1 | Lemma BL-FORM (with R-SAME) | PROVED | no | no |
| §2 | Lemma BL (a), (d) | PROVED | no | no |
| §2 | Lemma BL (b), (c), (e) | PROVED CONDITIONAL on (P) | yes | no |
| §3 | Lemma CONF-MONO | PROVED | no | no |
| §3 | Lemma FREE-FREEZE | PROVED CONDITIONAL on (P) | yes, via BL (c) | no |
| §4 | Corollary EQ-END | PROVED, CONDITIONAL on CN-LAST | no | yes |
| §5 | Lemma MERGE (merge-point form of a window gate) | PROVED | no | no |
| §6 | Proposition EV | PROVED CONDITIONAL on (P) | yes, via FREE-FREEZE | no |
| §6 | Proposition EV+ | PROVED CONDITIONAL on (P) | yes, via EV | no |
| §6 | Proposition TEV-RED | PROVED CONDITIONAL on (P) | yes, via FREE-FREEZE | no |

- §7 is NOT TO SIGN: CONJECTURE TEV, RISE-LAST, NJB / ENT, and the dead end BL-X (FALSE). §8: data.

## 0. Objects, dependencies, and the premise (P)
- Everything in P-N5-FBW §0 (docs/si/P-N5-FBW-box9.md, sha1 88337bd6; RESULTS R31): N5, S4a / S4b / S4c, Ξ, W, H_k, gates, gate levels,
  M_k, lev, COARSE_L, (C1)-(C7), b_k(y) := Ξ_k(σ_k y), θ := Ξ(o), w := W(o), r := lev(θ, w), R̄ / R / F, H1-H3, (h), THR / EQ, phase
  (λ_Ξ and τ constant), scope run (w constant).
  - In a phase τ is constant. Write e* := τ(o). Under (h), e* ∈ F (H2) and σ̄(o) ∈ F (H1).
- Signed and landed results used:
  - R15 (a) Ξ_k ⊴ Ξ_{k+1}.
  - R17 (a) F1: the optimum of a one-player game dominates every strategy of that game pointwise.
  - R18 (d) Lemma R (the order of the dual game G^d is the exact reverse of G's) and Lemma S (a): L_σ = Ξ_σ is the pointwise minimum of
    V_{σ,τ′} over Odd's τ′, and U_τ, the valuation of τ on G^d, is the pointwise maximum of V_{σ′,τ} over Even's σ′, read in G's order.
    Neither needs (P).
  - R19 (a) Lemma G: off R̄, Ξ = W; under (h), on R̄, Ξ(x) = π_x ⊕ θ and W(x) = π_x ⊕ w, with π_x ⊆ R the route of x to o (π_o = ∅).
  - R20 (b) FBL.
  - R21 (a) XW (Ξ ⊴ W).
  - R29 (a) (C5)-(C7), Fact R, CLU's proof ((C7) through routes); (b) TRANSFER; (c) OFFGATE; (e) NL (i)-(iii).
  - R31: P-OPT; Lemma FBW with its proof's Step 2; FBW-S; CLS2; FLAT-ALL (i)-(iii) (FBW-1); STRETCH.
  - P-N5-NJB (sha1 f43a8823) with its fixes (6a337748, 8ceee866 / 647386fb): RDROP, NO-RF-OLD, ENT-SHAPE (1)-(4) and (5′). Both
    referees signed these, pending CHECKER (R2-N5-NJB §C.4). They are used in §6 only.
- CN-LAST: docs/new/P-N5-SCOPE-box36.md §6 (L-NEW successor 15; packet file sha1 c3f5ed37, at trunk 70b0f05), under review by both
  referees. It is used ONLY in §4 (EQ-END).
- **Premise (P).** In a one-player game (Odd has out-degree 1 at every vertex), an Even strategy with no improving edge is optimal: its
  valuation dominates that of every Even strategy, pointwise.
  - This is the premise RESULTS R18 is conditional on. R18 states it as "CONDITIONAL on (P) for one-player games (G-1OA-4, open by
    design): VJ00 Lemma 5.8 '1 ⇒ 2', used only in Lemma 1 on G[X]".
  - R18's source line: "Source for (P): Vöge-Jurdziński, BRICS RS-00-48 (pdf sha256 485a12de…), Lemma 5.8 '1 ⇒ 2'".
  - R18 also notes that a derivation of the one-player form exists (R-N5-1P §3 route (a)), read as sound by REFEREE-2 but not refereed
    as a signature.
  - Here (P) is used for two one-player games: G_τ ("Odd fixed to τ_k") and its restriction G_τ[F] (§2).
- Definitions (new):
  - An Even edge (v, u) with u ≠ σ_k(v) is W-IMPROVING at k if W_k(u) ▷ W_k(σ_k v).
  - It is BLOCKED if it is W-improving and not a gate (Ξ_k(u) ⊴ Ξ_k(σ_k v)).
  - A WINDOW GATE is a gate (y, z) with y ∈ R_k and z ∈ F_k.
  - G_τ: the one-player game in which every Odd vertex keeps only its τ_k-edge. Its play values under σ are V_{σ,τ_k}, so W_k is σ_k's
    valuation there. W* := its optimal valuation (R17 F1; = U_{τ_k} by R18 Lemma S (a)).
  - For a set F ⊆ V ∖ {o} closed under the plays of (σ, τ): G_τ[F] is the one-player game on F in which Even keeps its edges inside F
    and every Odd vertex keeps its τ-edge. Opt(G_τ[F]) is its optimal valuation.
  - H := V_{>max(L, rank c)} when a level L is fixed, with c = c_θ = c_w the common cycle node (H3). "High" means in H.

## 1. Lemma BL-FORM (PROVED, L-SI succ. 5; every state with (h))
**Lemma R-SAME.** At a state with (h), for routes π, π′ ⊆ R and a ∈ {θ, w}, the order of π ⊕ a against π′ ⊕ a does not depend on a.
Proof.
- Both values have the cycle node c (H3).
- P(π ⊕ a) = (π ∩ V_{>c}) ⊔ P(a), and P(a) ⊆ {o} ∪ F is disjoint from R.
  - For a = θ: the play is o, then σ̄(o) ∈ F, then F.
  - For a = w: the play is o, then e* ∈ F, then F.
- So the symmetric difference of the path sets is (π Δ π′) ∩ V_{>c}, the same for both a.
- If it is empty, the lengths differ by |π| − |π′| for both a, and the parity rule is c's for both. □
**Lemma BL-FORM.** At a state k with (h), every blocked edge (v, u) satisfies:
- (a) σ_k(v) ∈ F_k (hence v ∈ F_k) and u ∈ R̄_k;
- (b) π_u ⊕ θ_k ⊴ Ξ_k(σ_k v) ◁ π_u ⊕ w_k;
- (c) Ξ_k(σ_k v) has the cycle node c.
Proof. Put s := σ_k(v) and use Lemma G.
- Case s, u ∈ F: Ξ = W at both, so the edge is W-improving iff it is a gate. Not blocked.
- Case s ∈ R̄, u ∈ F: Ξ(u) = W(u) ▷ W(s) = π_s ⊕ w ⊵ π_s ⊕ θ = Ξ(s). The last step is θ ⊴ w (XW) through (C7). So it is a gate.
- Case s, u ∈ R̄: by R-SAME, π_u ⊕ w ▷ π_s ⊕ w iff π_u ⊕ θ ▷ π_s ⊕ θ. So it is a gate.
- Case s ∈ F, u ∈ R̄: W-improving is π_u ⊕ w ▷ Ξ(s), and not a gate is π_u ⊕ θ ⊴ Ξ(s). This is (b).
- v ∈ F: if v ∈ R, its play passes s and reaches o, so s ∈ R̄.
- (c): both ends of (b) have the cycle node c. A value with another cycle node c′ lies below both or above both, by rew(c′) against
  rew(c). □

## 2. Lemma BL (PROVED; parts (b), (c), (e) CONDITIONAL on (P))
Setting. k is an in-phase S4c fallback with (h) at k and θ_k ◁ w_k (THR). x0 := σ̄_k(o).
- (a) [no (P)] σ_k is not optimal in G_τ: W_k ≠ W*.
- (b) [(P)] Some Even edge is blocked at k.
- (c) [(P)] On F_k, W_k = Opt(G_τ[F_k]).
- (d) [no (P)] x0 is nominally deficient: W_k(x0) ◁ W*(x0). Every free exit x with o ⊕ Ξ_k(x) ◁ w_k is deficient too.
- (e) [(P), through (c)] Every optimal G_τ-play from x0 leaves F_k, along an Even edge into R̄_k.
Proof.
- Step 0 (Odd's improving edges at o).
  - By R18 Lemma S (a) on G^d and Lemma R, Odd's valuation Ξτ_k is W* with the order reversed: the same triples, the reverse order.
  - So by SPEC S2 on G^d, (o, x) ∈ Iτ_k iff W*(x) ◁ W*(e*) in G's order.
- Step 1: if (o, x) ∈ Iτ_k for a free exit x with o ⊕ Ξ_k(x) ◁ w_k, then τ_new ≠ τ_k, and k is not an S4c fallback.
  - S4b computes τ_new as Odd's optimal counterstrategy to σ_k in H′ (o restricted to {e*} ∪ Iτ_k(o), Even fixed to σ_k). By R18 Lemma
    S (a) on H′, V_{σ_k,τ_new}(o) ⊴ V_{σ_k,x}(o).
  - x ∈ F_k, so its play avoids o, and V_{σ_k,x}(o) = o ⊕ W_k(x) = o ⊕ Ξ_k(x) ◁ w_k = V_{σ_k,τ_k}(o). So τ_new(o) ≠ e*.
  - SPEC S4c fires only if σ_new = σ_k and τ_new = τ_k.
- (a): suppose W_k = W*.
  - θ_k = o ⊕ Ξ_k(x0) = o ⊕ W_k(x0) ((P2) at o, Lemma G, x0 ∈ F_k) and w_k = o ⊕ W_k(e*).
  - o lies on neither play, so θ_k ◁ w_k gives W*(x0) ◁ W*(e*) ((C7)).
  - So (o, x0) ∈ Iτ_k, against Step 1.
- (b):
  - Step 2a. Every W-improving gate is EXCEPTIONAL: its tail y is its own W-cycle node, P(W_k z) = ∅, and lev(W_k σ_k y, W_k z) = −1.
    - At k, S4a returned σ_k. So by P-OPT (R31), V_{σ′,τ_k} ⊴ W_k for every σ′ ∈ A(σ_k).
    - For a W-improving gate (y, z), R31's FBW Step 2 (stated with V := W_k and using only V(z) ▷ V(σ_k y)) shows that σ_k[y ↦ z] ∈ A(σ_k)
      strictly improves W at y, except in exactly the exceptional case. The strict case contradicts P-OPT.
  - Step 2b. Suppose every W-improving edge were a gate, hence exceptional, with tails c_1, …, c_p. Let z_i be a W_k-best improving
    target of c_i, and σ′ := σ_k[c_i ↦ z_i for all i].
    - W_{σ′} = W_k:
      - W_k(σ_k c_i) = (c_i, ∅, ·) and W_k(z_i) = (c_i, ∅, ·), so z_i's (σ_k, τ_k)-play reaches c_i through vertices less relevant than c_i;
      - it meets no other c_j first: c_j's play is its own cycle, which would make c_j the cycle node;
      - a play meeting no c_i is unchanged. A play that first meets some c_i agrees with the old play up to c_i and then runs on a
        cycle topped by c_i, so its value (measured up to the first visit of the cycle node) is unchanged.
      - This is CN-LAST (i)'s argument (P-N5-SCOPE §6), written here for the fixed-τ play valuation; it is not a use of CN-LAST.
    - σ′ has no W_{σ′}-improving edge.
      - At an unswitched v, σ′(v) = σ_k(v) and W is unchanged. An improving edge there would be W_k-improving, hence exceptional,
        hence switched.
      - At c_i, an edge (c_i, u) with W(u) ▷ W(z_i) ▷ W(σ_k c_i) would be a W_k-improving target better than z_i.
    - By (P) in G_τ, σ′ is optimal: W_k = W_{σ′} = W*. This contradicts (a).
  - So some W-improving edge is not a gate.
- (c):
  - G_τ[F_k] is well defined:
    - σ_k(F_k) ⊆ F_k;
    - every Odd vertex of F_k is not o and has one successor, which lies in F_k (otherwise it would reach o).
  - Plays from F_k under (σ_k, τ_k) stay in F_k, so W_k restricted to F_k is σ_k's valuation in G_τ[F_k].
  - Its improving edges are W_k-improving edges inside F_k. These are gates (BL-FORM, first case), hence exceptional (Step 2a).
  - Switching them as in Step 2b changes no value and leaves no improving edge. By (P) in G_τ[F_k], W_k = Opt(G_τ[F_k]) on F_k.
- (d):
  - (o, x) ∉ Iτ_k (Step 1), so W*(x) ⊵ W*(e*) (Step 0).
  - W*(e*) ⊵ W_k(e*) (F1).
  - W_k(e*) ▷ W_k(x), from o ⊕ Ξ_k(x) ◁ w_k = o ⊕ W_k(e*) and (C7).
  - x0 is such an exit, since o ⊕ Ξ_k(x0) = θ_k ◁ w_k.
- (e):
  - A G_τ-strategy whose play from x0 stays in F_k agrees on that play with a strategy of G_τ[F_k] (extend by σ_k on the rest of F_k).
    So its value at x0 is ⊴ Opt(G_τ[F_k])(x0) = W_k(x0) ◁ W*(x0).
  - Every Odd vertex of F_k keeps its successor in F_k, so the only way out is along an Even edge into R̄_k. □

## 3. Lemma CONF-MONO (PROVED) and Lemma FREE-FREEZE (PROVED CONDITIONAL on (P))
**Lemma CONF-MONO.** If F′ ⊆ F are closed (as in §0), then Opt(G_τ[F′]) ⊴ Opt(G_τ[F]) on F′.
- Proof: a strategy of G_τ[F′], extended arbitrarily inside F, is a strategy of G_τ[F] with the same plays from F′. Apply F1 in
  G_τ[F]. □
**Lemma FREE-FREEZE.** Let k0 be an in-phase THR S4c fallback with (h), and t > k0 a state of the same phase with (h). If z ∈ F_t and
z's (σ_t, τ)-play lies in F_{k0}, then Ξ_t(z) = Ξ_{k0}(z) (all three components).
Proof.
- Ξ_{k0}(z) ⊴ Ξ_t(z) (R15 (a)), and Ξ_t(z) = W_t(z) (Lemma G).
- Let σ′ be σ_t on the vertices of z's play and σ_{k0} on the rest of F_{k0}. Then σ′ maps F_{k0} into F_{k0}: the play is closed under
  its successors and lies in F_{k0}, and σ_{k0}(F_{k0}) ⊆ F_{k0}.
- τ is the same at k0 and t (one phase). So σ′ is a strategy of G_τ[F_{k0}], and its play from z is z's (σ_t, τ)-play: value W_t(z).
- By F1 and BL (c) at k0: W_t(z) ⊴ Opt(G_τ[F_{k0}])(z) = W_{k0}(z) = Ξ_{k0}(z). □

## 4. Corollary EQ-END (PROVED, CONDITIONAL on CN-LAST)
Let S be a scope run and t a state of S with θ_t = w. Then every later state of S is EQ. S has at most one S4c fallback after t, and it is
the last transition of its phase.
Proof.
- For s ≥ t in S: θ_t ⊴ θ_s (R15 (a)) and θ_s ⊴ w_s = w (XW; w is constant in S). So θ_s = w.
- At an in-scope EQ fallback, every gate has level −1, and its tail y has λ(y) = y. This is FBW-S (R31): at EQ, δ = ⊥, and FBW (b)
  makes y its own W- and Ξ-cycle node.
- CN-LAST (iii) then makes k + 1 the last state of its phase. So no second fallback of S follows. □

## 5. Lemma MERGE (PROVED; elementary)
Let (y, z) be a window gate of level ℓ ≥ −1 at a state k with (h), x0 := σ̄_k(o), and H := V_{>max(ℓ, rank c)}. Then:
- (a) y's route π (the route of σ_k(y)) has no vertex in H, and COARSE_ℓ(Ξ_k z) = COARSE_ℓ(π ⊕ θ_k).
- (b) o ∉ H.
- (c) Let m be the first common vertex of the σ_k-plays of z and x0. Their prefixes before m contain no vertex of H.
Proof.
- (a) lev(b_k y, Ξ_k z) = ℓ gives equal COARSE_ℓ, with b_k(y) = π ⊕ θ_k (Lemma G).
  - P(Ξ_k z) ⊆ F_k, since z's play avoids o. π ⊆ R_k is disjoint from it, so (π ∩ H) = ∅.
- (b) o ∈ H would put o in P(θ_k) ∩ H = P(Ξ_k z) ∩ H.
- (c) Both plays end in c's cycle, so they meet.
  - By (a)-(b), their H-parts are equal: P(Ξ_k z) ∩ H = P(Ξ_k x0) ∩ H.
  - Their prefixes before m are disjoint, and the suffixes from m coincide (σ_k is a function; Odd vertices other than o have one
    successor).
  - So each prefix's H-part is contained in the other prefix's H-part, and the two are disjoint. So both are empty. □

## 6. Propositions EV, EV+, TEV-RED (PROVED CONDITIONAL on (P))
Setting (THE ENT SETTING).
- S is a scope run, and k0 < k are consecutive fallbacks of S with M_{k0} = M_k = L ≥ 0.
- r > L on [k0+1, k], and some S4a step in (k0, k) changes COARSE_L(θ) (a RISE).
- Ev := F_{k0+1} ∖ F_{k0}: the vertices made free by the fallback k0.
- A, B: the parts of P(θ_{k0}), P(θ_k) in H = V_{>max(L, rank c)}.
- Facts used throughout:
  - k0 and k are THR (M ≥ 0 and FBW-S give r ≥ M ≥ 0).
  - (A_s) holds for L at every state of [k0+1, k] (OFFGATE, NL (iii)). NL (ii) gives no leave at the S4a steps of (k0, k), so
    F_s ⊆ F_{k0+1} for s ∈ [k0+1, k], and a vertex of F_s is in F on all of [k0+1, s].
  - NL (i) freezes COARSE_L(Ξ) on F at those steps. FLAT-ALL (iii) at k0 freezes COARSE_L(Ξ) at every vertex across k0.
  - COARSE_L(θ_k) ≠ COARSE_L(θ_{k0}), both with the cycle node c, and θ_{k0} ⊴ θ_k. So A ≠ B, and the top of A Δ B is even and in B.
  - By ENT-SHAPE (signed), there is a level-L window gate (y, z) at k, and z's rank-L bit β(Ξ z) is bad at k0 and good at k
    (ENT-SHAPE (4)).
**Proposition EV.** z's σ_k-play meets Ev. Moreover, with q the first Ev vertex on it, ρ the part of the play before q, and π_q q's route
at k0: A ⊆ B, and B ∖ A = (ρ ∪ π_q) ∩ H.
Proof.
- If z's σ_k-play lay in F_{k0}, FREE-FREEZE would give Ξ_k(z) = Ξ_{k0}(z), so β(Ξ z) would be the same at k0 and k. ENT-SHAPE (4)
  excludes this.
- The play lies in F_k ⊆ F_{k0+1}, so it meets F_{k0+1} ∖ F_{k0} = Ev.
- Class bookkeeping.
  - Ξ_k(z) = ρ ⊕ Ξ_k(q) along the play, with ρ ∩ P(Ξ_k q) = ∅ (the play is simple before its cycle).
  - q ∈ F on [k0+1, k], so P(Ξ_k q) ∩ V_{>L} = P(Ξ_{k0} q) ∩ V_{>L} (NL (i), FLAT-ALL (iii)) = (π_q ∩ H) ⊔ A (Lemma G at k0;
    π_q ⊆ R_{k0} is disjoint from P(θ_{k0})).
  - MERGE (a) at level L: P(Ξ_k z) ∩ H = P(θ_k) ∩ H = B, and o ∉ H (MERGE (b)).
  - So B = (ρ ∩ H) ⊔ (π_q ∩ H) ⊔ A. □
**Proposition EV+.** The σ_k-play of the new threat x_k := σ̄_k(o) also meets Ev.
Proof.
- Let h be the top vertex of B ∖ A; the set is non-empty by EV and A ≠ B.
- If h ∈ ρ: by MERGE (c) at level L, every H-vertex of z's play lies on the suffix shared with x_k's play. q comes after h on z's play,
  so q lies on x_k's play.
- If h ∈ π_q: h ∈ B ⊆ P(θ_k) and h ≠ o (routes avoid o), so h lies on x_k's play and h ∈ F_k. Also h ∈ π_q ⊆ R_{k0}, and
  F_k ⊆ F_{k0+1}. So h ∈ Ev. □
**Proposition TEV-RED.** Let t ∈ (k0, k] be a state after the rise. Suppose the σ_t-play of x_t := σ̄_t(o) meets Ev. Let e be the last Ev
vertex on it, f := σ_t(e) its successor on the play, u_e := σ_{k0}(e), and B_t := P(θ_t) ∩ H. Then:
- (1) e is Even, f's play lies in F_{k0}, and Ξ_t(f) = Ξ_{k0}(f).
- (2) u_e's route at k0 has no vertex in H, and COARSE_L(Ξ_{k0} u_e) = (c, A) = COARSE_L(θ_{k0}).
- (3) B_t = A ⊔ (the H-vertices of x_t's play before e).
- (4) If u_e ∈ R̄_t, then (e, u_e) is a gate of level > L at t.
- (5) At t = k, u_e ∈ Ev ∩ F_k.
Proof.
- (1)
  - Every vertex after e on the play lies in F_t ⊆ F_{k0+1} = F_{k0} ⊔ Ev and is not in Ev, so it lies in F_{k0}.
  - If e were Odd, its only successor would be its k0-successor, which is in R̄_{k0} since e ∈ R_{k0}. Contradiction.
  - FREE-FREEZE applies to f.
- (2)
  - COARSE_L(b(e)) is constant on [k0, t]:
    - across k0 by FLAT-ALL (iii), in b-form: if e is not a tail, b(e) = Ξ(u_e) and (iii) applies; if e is a tail, its target has the
      COARSE_L of the gate, of level ≤ L;
    - after k0 by NL (i), since e ∈ F on [k0+1, t] and Ξ(e) = e ⊕ b(e).
  - So COARSE_L(Ξ_{k0} f) = COARSE_L(Ξ_t f) = COARSE_L(b_t e) = COARSE_L(b_{k0} e) = COARSE_L(π_{u_e} ⊕ θ_{k0}).
  - P(Ξ_{k0} f) ⊆ F_{k0} and π_{u_e} ⊆ R_{k0}, so π_{u_e} ∩ H = ∅.
  - o ∉ H: o ∈ A would put o on f's free play.
- (3) Ξ_t(x_t) = (x_t's play up to e) ⊕ Ξ_t(f), with Ξ_t(f) = Ξ_{k0}(f) of class (c, A) by (1)-(2). o ∉ H.
- (4)
  - u_e ∈ R̄_t gives Ξ_t(u_e) = π′ ⊕ θ_t, whose H-part π′_H ∪ B_t strictly contains A (by (3), and B_t ≠ A after the rise).
  - Ξ_t(u_e) ⊵ Ξ_{k0}(u_e) (R15 (a)), and COARSE_L(Ξ_{k0} u_e) = (c, A) = COARSE_L(b_t e) (by (2)).
  - So Ξ_t(u_e) ▷ b_t(e) at a level > L, and u_e ≠ σ_t(e) = f (u_e ∈ R̄_t, f ∈ F_t).
- (5) M_k = L excludes gates of level > L at k, so by (4) u_e ∉ R̄_k, i.e. u_e ∈ F_k (in particular u_e ≠ o). And u_e ∈ R̄_{k0}, since e ∈ R_{k0}. So u_e ∈ F_k ∖ F_{k0} ⊆ Ev. □
- Consequence (the reduction). If NJB fails in the ENT setting, then at k (EV+, TEV-RED (5)):
  - the threat's play passes through an Even vertex e such that e and its k0-successor u_e were both evicted at k0 and are both free at k;
  - e is re-routed to a frozen f ∈ F_{k0} of class (c, A);
  - the rise vertices B ∖ A lie on the threat's play before e.

## 7. NOT TO SIGN
- CONJECTURE TEV (L-SI succ. 5, DATA). After an in-scope THR fallback k0 of level L ≥ 0, every later state t of the scope run that comes
  after a COARSE_L(θ) rise, with r > L on [k0+1, t], has the threat's σ_t-play disjoint from Ev. With EV+, TEV implies NJB and ENT.
- CONJECTURE RISE-LAST (L-RED 15, docs/red/R68-xsn-njb-ent.md §6). It implies NJB and ENT. Its EQ branch is EQ-END. Its THR branch is
  open, including fallbacks of level < L and those after r ≤ L, where ENT-SHAPE's bit argument does not apply.
- CONJECTURE NJB / ENT (P-N5-NJB §5).
- FALSE (DATA): BL-X, "at every THR fallback some blocked tail lies on x0's σ_k-play".
  - Fails at 41 of 373 NAMED THR fallbacks: first elim24_p52 at k = 13; also x31_lem_e24 at k = 23, 29, 37, and cl9_rep_b at k = 6-21.
  - Fails at 4 of 526 LIB THR fallbacks (x31_lem_e24 at 23, 29, 37; elim24_p52 at 13).
  - BL (e) is the correct form: the OPTIMAL play from x0 leaves F, while the current play need not meet a blocked tail.

## 8. Data (DATA, not proof; scripts experiments/si/riselast/, logs experiments/si/riselast/logs/, in this packet's commit)
- Sets:
  - NAMED = experiments/si/coarse/named.txt + experiments/si/coarse/instances/*.pg + instances/box9/*.pg;
  - LIB = experiments/new/box33/lib.txt (234, first column).
  - Runs are asserted equal to n5.py run() (coarse/mono.states), and 𝒞^1O is asserted per game.

| script | checks | NAMED | LIB | failures |
| --- | --- | --- | --- | --- |
| blocked.py | BL-FORM over blocked edges at in-scope states; BL (b) at in-scope THR fallbacks | 23,135 edges / 2,101 states; 373 / 373 | 50,491 / 4,458; 526 / 526 | 0 |
| blf.py | BL (a), BL-F1 (= BL (c)), BL-F2 (= BL (d)), F1 dominance | 373 fallbacks | 526 | 0 |
| ffreeze.py | FREE-FREEZE: (k0, t, z) with z's play in F_{k0} | 91,913 | 177,919 | 0 |
| threv.py | the threat's play meets Ev (all states / post-rise states with r > L) | 179 / 662; 0 / 47 | 425 / 1,353; 0 / 6 | — (TEV data) |
| rlprobe.py | rises above the last fallback level; fallbacks later in the run | 20 rises, 0 | 39 rises, 0 | — (RISE-LAST data) |

- EQ-END / CN-LAST data: rises that make θ = w: 7 (NAMED), 20 (LIB); no fallback follows any of them.
- Climbs (rlclimb.py; fitness from BL, per post-rise state 3·[window gate] + 3·[blocked edge] + (5 − min(W-improving gates, 5))):
  - 3 × 2,400 s, seeds 10001-10003, from cl9_norf_a, cl9_norf_b, x31_rx32; 0 violations.
  - The best score was 7 in all three: no window gate after a rise.
  - Bests, recommended as SEEDS for climbs on TEV, each re-verified (n5.py, check_sol2.py: Oink zlk OK, strategies verified;
    logs/climb_bests_verify.txt):
    - experiments/si/riselast/instances/rl_a.pg (n 32, sha1 11bfdb71, 35 iterations / 2 fallbacks);
    - rl_b.pg (n 32, eeac0522, 33 / 2);
    - rl_c.pg (n 32, 04ff3de5, 30 / 3).
  - On the three together: 31 rises, 0 fallbacks after; 64 post-rise states, 0 with the threat through Ev; FREE-FREEZE 1,212 checks,
    0 failures.
- Thin spots: post-rise states with r > L are few (47 + 6 + 64). The ENT setting itself never occurs, so EV, EV+ and TEV-RED have
  vacuous hypotheses in all data. They rest on the proofs.
