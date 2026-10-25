# N5 box 10 (L-SI successor 5): RISE-LAST and NJB seen from Even's nominal game; blocked edges
L-SI successor 5 (Opus 5.5, D15/D18, L37/L40). Started 2026-10-25 09:40Z (date -u), Lead GO 09:33Z, item (b).
- Labels: PROVED (L-SI succ. 5, unrefereed), PROVED CONDITIONAL (on a named premise), CONJECTURE, OPEN, DATA.
- Everything is on 𝒞^1O: exactly one Odd vertex o with out-degree > 1. Every script asserts it.
- These are lemmas about the candidate N5. They are not a running-time bound, not a TARGET.md claim, and not a step-4 pass.
  G-N5-TIME stays OPEN.
- Setting and notation: P-N5-FBW §0 (docs/si/P-N5-FBW-box9.md, RESULTS R31) and P-N5-NJB §0 with its fixes
  (docs/si/P-N5-NJB-fixes-box9.md). In particular:
  - in a phase τ is constant; e* := τ(o);
  - W := the (σ, τ) play valuation; Ξ := the honest valuation; θ := Ξ(o), w := W(o), r := lev(θ, w);
  - R̄ / R / F; (h); THR, EQ; scope runs (w constant).
- Targets (Lead):
  - NJB in its MINSET form;
  - L-RED 15's CONJECTURE RISE-LAST (docs/red/R68-xsn-njb-ent.md §6, trunk 06fbc11): inside a scope run, no COARSE_L(θ) rise happens
    between an in-scope fallback k0 (L := M_{k0}) and the next in-scope fallback. It implies NJB and ENT.
  - Read, not edited: L-NEW 15's PF-THETA (docs/new/N5-DROP-box35.md §8) and CN-LAST (same file §7).

## 0. The angle, and the result in one paragraph
- Angle (robust vs nominal optimisation, from the robust-MDP view of a one-Odd-choice game).
  - Inside a phase, Odd's only choice o is fixed to e* by τ. So Even faces a ONE-PLAYER game G_τ, whose play values are W (the
    "nominal" values).
  - Ξ = min over Odd's d_o choices at o of the play values (R18 Lemma S (a)). These are the "robust" values.
  - N5's S4a is a nominal optimisation (Even's optimum in G_τ) restricted to robustly improving edges (the gates). A fallback is the
    moment this gated nominal optimisation is stuck.
- Result:
  - Lemma BL-FORM (PROVED, unconditional): every W-improving edge that is not a gate (a BLOCKED edge) runs F → R̄. Its free value lies in
    the reverse window [π_u ⊕ θ, π_u ⊕ w).
  - Lemma BL (PROVED CONDITIONAL on (P), the same premise as R18): at every in-scope THR fallback there is a blocked edge. On F_k, the
    values are Even's optimum confined to F_k. The threat exit σ̄(o) is nominally deficient: Even's optimum in G_τ answers it only
    through R̄.
  - A fallback after a rise therefore needs three things at one state: a blocked edge, a window gate (R → F) and no W-improving gate.
  - The EQ branch of RISE-LAST is harmless: at most one more fallback, the phase's last (Corollary EQ-END, using L-NEW's lane-proved
    CN-LAST).
  - DATA: no fallback ever follows a rise, in the whole rest of the run, not only in its scope run. 35 / 39 (lib) and 18 / 20 (named)
    rises close the top gap (lt = r).
  - RISE-LAST itself stays a CONJECTURE. The exact point where the proof stops is in §5.

## 1. Lemma BL-FORM (PROVED, L-SI succ. 5; every state with (h))
Let k be a state with (h). Call an Even edge (v, u) with u ≠ σ_k(v) W-IMPROVING if W_k(u) ▷ W_k(σ_k v). Call it BLOCKED if it is
W-improving but not a gate (Ξ_k(u) ⊴ Ξ_k(σ_k v)). Then every blocked edge (v, u) satisfies:
- (a) σ_k(v) ∈ F_k (so v ∈ F_k) and u ∈ R̄_k;
- (b) π_u ⊕ θ_k ⊴ Ξ_k(σ_k v) ◁ π_u ⊕ w_k, where π_u is u's route to o (π_o = ∅);
- (c) Ξ_k(σ_k v) has the cycle node c := c_θ = c_w (H3).
Proof.
- Lemma G (R19 (a)) under (h): off R̄, Ξ = W. On R̄, Ξ(x) = π_x ⊕ θ and W(x) = π_x ⊕ w, with π_x ⊆ R.
- Route comparison (R-SAME). For routes π, π′ ⊆ R and a ∈ {θ, w}, the order of π ⊕ a against π′ ⊕ a does not depend on a.
  - Both values have the cycle node c (H3).
  - P(π ⊕ a) = (π ∩ V_{>c}) ⊔ P(a), and P(a) ⊆ {o} ∪ F is disjoint from R. So the symmetric difference of the path sets is
    (π Δ π′) ∩ V_{>c}, the same for a = θ and a = w.
  - If it is empty, the lengths differ by |π| − |π′| for both a, and the parity rule is c's for both.
  - This is (C7) applied to routes, as in R29 (a) CLU's proof.
- Cases for (v, u), with s := σ_k(v):
  - s, u ∈ F: Ξ = W at both, so W-improving ⇔ gate. Not blocked.
  - s ∈ R̄, u ∈ F: Ξ(u) = W(u) ▷ W(s) = π_s ⊕ w ⊵ π_s ⊕ θ = Ξ(s). The middle step is θ ⊴ w (XW, R21 (a)) and (C7) through π_s. So it is
    a gate. Not blocked.
  - s, u ∈ R̄: by R-SAME, π_u ⊕ w ▷ π_s ⊕ w ⇔ π_u ⊕ θ ▷ π_s ⊕ θ. So it is a gate. Not blocked.
  - s ∈ F, u ∈ R̄: W-improving means π_u ⊕ w ▷ W(s) = Ξ(s). Not a gate means π_u ⊕ θ ⊴ Ξ(s). This is (b).
  - v ∈ F: if v ∈ R, its play passes s and reaches o, so s ∈ R̄.
- (c): π_u ⊕ θ and π_u ⊕ w have the cycle node c. If Ξ(s) had a cycle node c′ ≠ c, then rew(c′) against rew(c) would place Ξ(s) below
  both values or above both. That is incompatible with (b). □
- Remark. A gate is the robust test and a W-improving edge the nominal test. They disagree only on edges from a free vertex into R̄:
  Even would like to route v through o (nominally), but Odd's threat θ makes the route look no better (robustly).

## 2. Lemma BL and Corollary BL-F (PROVED CONDITIONAL on (P), L-SI succ. 5)
Premise (P): VJ00 (BRICS RS-00-48) Lemma 5.8 "1 ⇒ 2" for one-player games: a strategy of a one-player game with no improving edge is
optimal. This is the premise R18 is conditional on (G-1OA-4, open by design). R17's F1 is signed without it.
Let k be an in-phase S4c fallback with (h) at k and θ_k ◁ w_k (THR). Let G_τ be the one-player game "Odd fixed to τ_k", with W* its
optimal values (pointwise; R17 (a) F1). Then:
- (a) σ_k is not optimal in G_τ: W_k ≠ W*.
- (b) Some Even edge is blocked at k, and its form is BL-FORM.
- (c) [BL-F1] On F_k, W_k equals the optimum of G_τ[F_k], the one-player game on F_k in which Even's edges into R̄_k are deleted.
- (d) [BL-F2] The threat exit x0 := σ̄_k(o) is nominally deficient: W_k(x0) ◁ W*(x0). Every free exit x with o ⊕ Ξ_k(x) ◁ w_k is
  deficient too.
- (e) By (c) and (d), Even's optimum from x0 in G_τ beats its optimum confined to F_k. So every optimal G_τ-play from x0 enters R̄_k:
  the threat can be answered only through o.
Proof.
- Step 0: Odd's improving set. Ξτ_k is the S1 valuation of τ_k on the dual game G^d.
  - By R18 Lemma S (a) on G^d, Ξτ_k is, vertex by vertex, the dual-best response to τ_k, i.e. Even's best play value in G_τ.
  - The dual valuation of a play is the same triple (c, P, ℓ): ranks and cycle tops are the same in G^d. Its order is the reverse
    of G's order:
    - rewards: for Ω(c) even, rew = 2·rank and rew_d = −(2·rank + 1); for Ω(c) odd, rew = −(2·rank + 1) and rew_d = 2·rank. The map
      is order-reversing in all four rank / parity cases.
    - path signs flip;
    - the length rule flips with the cycle node's parity.
  - So Ξτ_k ≅ W* with the order reversed. (o, x) ∈ Iτ_k ⇔ W*(x) ◁ W*(e*) in G's order (SPEC S2 on G^d).
- Step 1: if (o, x0) ∈ Iτ_k, then τ_new ≠ τ_k, and k is not a fallback.
  - S4b computes τ_new as Odd's optimal counterstrategy to σ_k in H′ (o restricted to {e*} ∪ Iτ_k(o)). By R18 Lemma S (a) on H′,
    V_{σ_k, τ_new}(o) ⊴ V_{σ_k, x0}(o).
  - x0 ∈ F_k (H1), so its play avoids o: V_{σ_k, x0}(o) = o ⊕ W_k(x0) = θ_k ((P2) at o, Lemma G).
  - θ_k ◁ w_k = V_{σ_k, τ_k}(o). So τ_new(o) ≠ e*.
  - S4c fires only if σ_new = σ_k and τ_new = τ_k (SPEC S4c).
- (a): suppose W_k = W*.
  - x0, e* ∈ F_k (H1, H2), so θ_k = o ⊕ W_k(x0) and w_k = o ⊕ W_k(e*).
  - o lies on neither play, so θ_k ◁ w_k gives W*(x0) = W_k(x0) ◁ W_k(e*) = W*(e*) ((C7)).
  - So (o, x0) ∈ Iτ_k, against Step 1.
- (b):
  - At k, S4a returned σ_k, so σ_k is optimal in the arena A(σ_k) against τ_k (R18 Lemma S (c); P-OPT, R31).
  - Let (y, z) be a W-improving gate at k. By R31 FBW Step 2, σ_k[y ↦ z] ∈ A(σ_k) strictly improves W at y, except in one case: y is
    its own W-cycle node, P(W z) = ∅, and lev(W σ_k y, W z) = −1 (an "exceptional" gate). The strict case contradicts P-OPT. So
    every W-improving gate is exceptional.
  - Suppose every W-improving edge were a gate, hence exceptional. Let σ′ switch each such tail c_i to its W-best improving target z_i.
    - Then W_{σ′} = W_k: CN-LAST (i)'s argument (docs/new/N5-DROP-box35.md §7, lane-PROVED by L-NEW, unrefereed), written for the
      fixed-τ play valuation:
      - z_i's play reaches c_i first, through vertices below c_i, and meets no other c_j;
      - every value is measured up to the first visit of its cycle node, so no value changes.
    - σ′ has no W-improving edge. At an unswitched tail it would have been W-improving for σ_k, hence exceptional, hence switched. At
      c_i, an edge better than z_i would have been a better improving target at k.
    - By (P), σ′ is optimal, so W_k = W_{σ′} = W*, against (a).
  - So some W-improving edge is not a gate: a blocked edge.
- (c):
  - G_τ[F_k] is well defined:
    - σ_k(F_k) ⊆ F_k;
    - Odd vertices in F_k other than o have one successor, and it lies in F_k (otherwise they would reach o);
    - o ∉ F_k.
  - Plays from F_k stay in F_k, so W_k restricted to F_k is σ_k's valuation in G_τ[F_k].
  - A W-improving edge inside F_k is a gate (BL-FORM, case s, u ∈ F), hence exceptional by (b). As in (b), switching them changes no
    value and leaves no improving edge in G_τ[F_k]. So by (P), W_k = Opt(G_τ[F_k]) on F_k.
- (d):
  - (o, x0) ∉ Iτ_k (Step 1), so W*(x0) ⊵ W*(e*) (Step 0).
  - W*(e*) ⊵ W_k(e*) (F1).
  - W_k(e*) ▷ W_k(x0), since θ_k ◁ w_k and (C7) through o.
  - For another free exit x with o ⊕ Ξ_k(x) ◁ w_k: (o, x) ∈ Iτ_k would also give τ_new ≠ τ_k (Step 1 with x in place of x0). So the
    same chain applies.
- (e):
  - A strategy of G_τ whose play from x0 stays in F_k is a strategy of G_τ[F_k] there. So its value at x0 is ⊴ Opt(G_τ[F_k])(x0) =
    W_k(x0) ◁ W*(x0).
  - Hence every optimal play from x0 leaves F_k. It can only do so along an Even edge into R̄_k. □
- Lemma CONF-MONO (PROVED; trivial). If F′ ⊆ F are both closed in this sense, then Opt(G_τ[F′]) ⊴ Opt(G_τ[F]) on F′. Reason: every
  strategy of G_τ[F′] is one of G_τ[F], and F1 applies in G_τ[F].
  - Use (OPEN how far it goes): between consecutive THR fallbacks k0 < k of a scope run, the free values at k are Opt(G_τ[F_k]). If
    F_k ⊆ F_{k0}, then W_k = W_{k0} on F_k: they are ⊴ Opt(G_τ[F_{k0}]) = W_{k0} by CONF-MONO and (c), and ⊵ W_{k0} since Ξ only rises
    (R15 (a)) and Ξ = W off R̄.
  - So in that case every free value is literally frozen from k0 to k. Only the vertices evicted at k0 can carry a free value that is
    new at k. Lemma FREE-FREEZE (§2b) is the vertex-by-vertex form, and it needs no fallback at k.

## 2b. Lemma FREE-FREEZE (PROVED CONDITIONAL on (P), L-SI succ. 5)
Let k0 be an in-phase THR S4c fallback with (h), and let t > k0 be a state of the same phase with (h). Let z ∈ F_t be a vertex whose
(σ_t, τ)-play lies inside F_{k0}. Then Ξ_t(z) = Ξ_{k0}(z), exactly (all three components).
Proof.
- Ξ_{k0}(z) ⊴ Ξ_t(z) (R15 (a)). Ξ_t(z) = W_t(z), since z ∉ R̄_t (Lemma G).
- Let σ′ be σ_t on the vertices of z's play and σ_{k0} on the rest of F_{k0}. Then σ′ maps F_{k0} into F_{k0}: the play's successors lie
  on the play, which lies inside F_{k0}, and σ_{k0}(F_{k0}) ⊆ F_{k0}.
  - So σ′ is a strategy of G_τ[F_{k0}]. τ is the same at k0 and t (one phase).
  - Its play from z is z's (σ_t, τ)-play, so its value at z is W_t(z).
- F1 in G_τ[F_{k0}] and BL-F1 at k0 give W_t(z) ⊴ Opt(G_τ[F_{k0}])(z) = W_{k0}(z) = Ξ_{k0}(z). □
- Meaning. After a THR fallback, for the rest of the phase, a free value can change only while the vertex's current play passes through
  R̄_{k0}: through the region evicted at k0, or through vertices that are in R̄_{k0} and later free.
  - This is stronger than NL (i) (frozen above L, only while r > L) on such vertices: it freezes every component, for every r.
- DATA: ffreeze.py, §4.

## 3. What this gives for RISE-LAST
- (R1) A rise needs r > L at its step (the sandwich of RDROP: θ_j ◁ θ_{j+1} ⊴ w and (C5)). r is non-increasing in a scope run
  (Fact R). Fallbacks after k0 have level ≤ min(L, max(r, −1)) (CLS2, FBW-S).
- **Corollary EQ-END (PROVED, L-SI succ. 5, using CN-LAST).** If θ_t = w at some state t of a scope run S, then:
  - every later state of S is EQ (θ is ⊴ w by XW and does not fall by R15 (a); w is constant in S);
  - S has at most one fallback after t, and that fallback is the last transition of its phase.
  Proof.
  - At an in-scope EQ fallback every gate is a length-only switch at its own cycle node (FBW-S, R31; with δ = ⊥, FBW (b) gives
    λ(y) = y).
  - CN-LAST (L-NEW, lane-proved, unrefereed) then makes it the last transition of the phase. □
  - So the EQ branch of RISE-LAST is harmless for counting.
  - Rises with r_{j+1} = ⊥ (θ reaches w): 20 / 39 (lib) and 7 / 20 (named). In all of them, no fallback follows (§4).
- (R2) THR branch. By BL, a THR fallback k after a rise needs, at the same state:
  - a blocked edge (v, u), v ∈ F_k, u ∈ R̄_k, in the reverse window;
  - a window gate (y, z), y ∈ R_k, z ∈ F_k, π ⊕ θ_k ◁ Ξ(z) ⊴ π ⊕ w, of level ℓ ≤ min(L, r_k) (FBL, FBW-S);
  - no W-improving gate.
- Merge-point form of a window gate (PROVED, L-SI succ. 5; elementary).
  - At level ℓ, COARSE_ℓ(Ξ z) = COARSE_ℓ(π ⊕ θ_k). The route π has no vertex above max(ℓ, rank c): it lies in R and P(Ξ z) ⊆ F.
  - If rank o > max(ℓ, rank c), then o ∈ P(θ_k), but o ∉ P(Ξ z). So rank o ≤ ℓ or rank o < rank c. This is ABS-O's observation.
  - Let m be the first common vertex of the σ_k-plays of z and of x0 = σ̄_k(o); both end in c's cycle. The prefixes before m are
    disjoint and have equal high parts above ℓ, so both have no vertex above max(ℓ, rank c).
  - The gate is decided by the top vertex of the "diamond" (y → z → … → m) ∪ (y → π → o → x0 → … → m): z's side wins if that top is
    even and on z's side, or odd and on the route side. Its rank is ℓ.
- (R3) BL-X is FALSE (DATA). One might hope that the blocked edge at a THR fallback lies on x0's own σ_k-play, i.e. that Even is blocked
  exactly at absorbing the threat. It does not have to: NAMED has 41 of 373 THR fallbacks without a blocked tail on x0's play (first:
  elim24_p52 at k = 13; cl9_rep_b at k = 6-21). The correct statement is BL (e): the OPTIMAL play from x0 enters R̄; the current play
  need not meet a blocked tail.

## 4. DATA (DATA, not proof; scripts in experiments/si/riselast/, logs in experiments/si/riselast/logs/)
- Sets:
  - NAMED = experiments/si/coarse/named.txt + experiments/si/coarse/instances/*.pg + instances/box9/*.pg (the packet's set);
  - LIB = experiments/new/box33/lib.txt (234, first column).
  - All runs are asserted equal to n5.py run() (mono.states), and 𝒞^1O is asserted per game.
- rlprobe.py: every rise above the last in-scope fallback level (lt > L), with what follows it.

| set | rises | lt = r (top gap closed) | r_{j+1} = ⊥ (θ = w) | run ended at the rise | fallbacks later in the scope run | fallbacks anywhere later in the run | how the scope run ends |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NAMED | 20 | 18 | 7 | 7 | 0 | 0 | N5 stops 13, ¬(h) next 6, phase change 1 |
| LIB | 39 | 35 | 20 | 11 | 0 | 0 | N5 stops 31, ¬(h) next 6, phase change 2 |

  - So after a rise N5 usually TERMINATES inside the same scope run, with no further fallback at all.
  - Typical trace (rltrace.py, cl9_norf_a):
    - one fallback at 11 (level 23, r 31);
    - then 23 S4a steps with exactly one gate each, every gate W-improving, and 0 R → F gates;
    - rises at 13 (lt 28), 19 (lt 31 = r: r drops to 24) and 34 (lt 24: θ = w);
    - then N5 stops.
- blocked.py, blf.py, ffreeze.py (0 violations in every row except BL-X, which is a data question):

| set | in-scope states | blocked edges (BL-FORM viol.) | in-scope THR fallbacks | with a blocked edge (BL (b)) | BL (a), BL-F1, BL-F2, F1 viol. | BL-X fails | FREE-FREEZE checks (viol.) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NAMED | 2,101 | 23,135 (0) | 373 | 373 | 0, 0, 0, 0 | 41 | 91,913 (0) |
| LIB | 4,458 | 50,491 (0) | 526 | 526 | 0, 0, 0, 0 | 4 | 177,919 (0) |

  - FREE-FREEZE: each check is a pair (k0 an in-scope THR fallback, t a later state of its scope run) and a z ∈ F_t whose play lies in
    F_{k0}. The other free vertices (play leaving F_{k0}): 83,756 / 184,438. They are the only ones allowed to change.
  - Logs: logs/{rlprobe,blocked,blf,ffreeze}_{named,lib}.txt, logs/rltrace_cl9_norf_a.txt.
- Climbs (rlclimb.py, a new fitness built from BL). After a rise, an in-scope state t scores
  3·[RF_t > 0] + 3·[blocked_t > 0] + (5 − min(W-improving gates, 5)). 11 means Even's side of a fallback is complete.
  - Fitness = (RISE-LAST violations, best score, post-rise in-scope states, rises).
  - 3 × 40 min, seeds 10001-10003, from cl9_norf_a, cl9_norf_b, x31_rx32. Results: §4c.

## 5. Where the proof stops (the exact obstruction, THR branch)
- Known ingredients:
  - after a rise, every k0-evicted tail whose old route survives has a gate back into R that is also W-improving (its route value rose
    above L, and r > L);
  - S4a refills R with them;
  - the free values are frozen above L (NL (i)) while r > L, and they are Even's confined optimum at each THR fallback (BL-F1).
- Missing: a reason why Even cannot become stuck again. Stuck means that the gated nominal optimisation has no W-improving gate while
  a window gate and a blocked edge coexist.
  - CONF-MONO freezes every free value when F_k ⊆ F_{k0}. Then a window gate (y, z) at k has z with the same free value as at k0, and y
    must be an entrant after the rise (NO-RF-OLD).
  - With the frozen value, ENT-SHAPE (4)'s rank-L bit flip of z needs z to be a vertex that is free at k but not at k0 (an evicted
    vertex, branch (iii-b) of the fixes file). When F_k ⊆ F_{k0} it can only come from (iii-b).
  - I have not excluded the case F_k ⊄ F_{k0}: vertices evicted at k0 that stay free until k and carry a free value that is new at k.
- **Proposition EV (PROVED CONDITIONAL on (P), L-SI succ. 5).** Take a violation of NJB in the ENT setting: S a scope run, k0 < k
  consecutive fallbacks of S with M_{k0} = M_k = L ≥ 0, r > L on [k0+1, k], and a COARSE_L(θ) rise in between. Let (y, z) be the
  level-L gate at k of ENT-SHAPE. Then z's σ_k-play meets the EVICTED REGION Ev := F_{k0+1} ∖ F_{k0}: vertices that were in R̄_{k0},
  became free at the fallback k0, and are still free at k.
  - Proof.
    - k0 is THR, since M_{k0} = L ≥ 0 and FBW-S give r_{k0} ≥ 0.
    - If z's σ_k-play lies inside F_{k0}, FREE-FREEZE gives Ξ_k(z) = Ξ_{k0}(z). Then z's rank-L bit β is the same at k0 and at k.
      ENT-SHAPE (4) says it is bad at k0 and good at k.
    - So the play leaves F_{k0}. All its vertices lie in F_k. No vertex leaves R at the S4a steps of (k0, k) (NL (ii), r > L), so
      F_k ⊆ F_{k0+1}. Hence the play meets F_{k0+1} ∖ F_{k0}. □
  - In particular both branches of the fixes file's (iii) need Ev:
    - (iii-b): z itself was evicted at k0;
    - (iii-a): z's F → F level-L rise must run through Ev. It is not a free-standing rise inside F_{k0}.
  - Class bookkeeping for that play (PROVED; NL (i) and FLAT-ALL (iii) on the Ev vertex q where z's play first meets Ev):
    - COARSE_L(Ξ_k z) = COARSE_L(ρ ⊕ Ξ_{k0} q) = COARSE_L(ρ ⊕ π_q ⊕ θ_{k0}), where ρ is the play from z to q and π_q is q's route at
      k0.
    - The gate gives COARSE_L(Ξ_k z) = COARSE_L(π ⊕ θ_k), with a low route π.
    - So, with A, B := the parts of P(θ_{k0}) and P(θ_k) above L: A ⊆ B, and B ∖ A = the vertices of ρ ∪ π_q above max(L, rank c).
    - The rise makes the top of B ∖ A even.
    - So the vertices by which θ rose (on the new threat's free play) are exactly high vertices on z's way into Ev, or on q's old route
      at k0.
- Target for L-RED (sharpened), in the order the events must happen:
  - a fallback k0 evicts a region Ev;
  - a rise follows (Mn emptied);
  - a free vertex z, whose play runs into Ev, has a rank-L bit flip;
  - an entrant y has a gate to z at the next fallback.
  - Its B ∖ A, the vertices by which θ rose above L, lies on z's way into Ev or on the old R-route of the first Ev vertex.
- Not covered by EV: RISE-LAST fallbacks at a level ℓ < L, and those after r has dropped to ≤ L. There ENT-SHAPE's bit argument is not
  available.

## 6. Status
- PROVED (L-SI succ. 5, unrefereed): BL-FORM; R-SAME; merge-point form of a window gate; CONF-MONO; Corollary EQ-END (using CN-LAST,
  L-NEW lane-proved).
- PROVED CONDITIONAL on (P) (= R18's premise, VJ00 Lemma 5.8 "1 ⇒ 2" for one-player games): Lemma BL (a)-(e), the use of CONF-MONO in
  §2, Lemma FREE-FREEZE (§2b), and Proposition EV (§5: an NJB violation's gate target has its play in the k0-evicted region).
- CONJECTURE: RISE-LAST (L-RED), NJB, ENT (L-SI succ. 4).
- FALSE (DATA): BL-X (a blocked tail on x0's current play).
- OPEN: RISE-LAST's THR branch; PF-THETA (L-NEW); REL(S); level −1 THR fallbacks (none seen in scope).
