# Referee packet P-N5-LV2: stale gates; REL(S) removed at level −1; the u* = none fallbacks; at most 4·n·n_E + 3 fallbacks per scope run (box 12)
L-SI successor 7 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~15:35Z (date -u), at the Lead's request (15:16Z, 15:19Z; Lead's
stamps). Frozen at its commit: corrections go in a fixes file, never here.
- Self-contained: definitions, statements, full proofs, the status of every dependency, the data and the scripts.
- Source texts:
  - docs/si/N5-LV4-box12.md (lane write-up, l-si 689f7b61, sha1 9d1b90f4);
  - docs/si/N5-LV5-box12.md (lane write-up, l-si 0bf9a899, sha1 e2cb0703).
  Where they differ, this packet governs.
- An earlier one-part draft, docs/si/P-N5-LV4-box12.md (l-si 79281d48), was never reported, and this packet replaces it. It is removed in
  this packet's commit.
- Status: L-SI successor 7's proofs, unrefereed. Labels: PROVED (L-SI succ. 7); PROVED CONDITIONAL on X; OPEN; DATA.
- Scope: §1 holds on every game. §2-§8 are on 𝒞^1O: exactly one Odd vertex o with out-degree > 1. The scripts assert it.
- These are lemmas about the candidate N5. They are not a running-time bound, not a TARGET.md claim, and not a step-4 pass.
  G-N5-TIME stays OPEN.
- Statements to sign:

| § | statement | label | condition (in review) | hypotheses occur in data? |
| --- | --- | --- | --- | --- |
| §1 | Lemma STALE-GATE | PROVED | none (every game) | yes: 72,589 checks |
| §2 | Corollary EV-G | PROVED | none | yes: 39,406 checks |
| §3 | Theorem ENT-X_{−1} | PROVED CONDITIONAL | P-N5-LV §3, §4 | no (vacuous) |
| §4 | Corollary LV-PL′ | PROVED CONDITIONAL | P-N5-LV §1-§4 | statement yes (every scope run); its block is empty (vacuous) |
| §5 | Lemma SAND | PROVED | none | yes: 155 in-scope transitions with r = −1, 310 checks (§9) |
| §6 | Lemma FLAT-ALL_{−1}^{none} | PROVED CONDITIONAL | P-N5-LV §1 | no (vacuous) |
| §7 | Theorem LV-NONE | PROVED CONDITIONAL | P-N5-LV §1, §3 | no (vacuous) |
| §8 | Corollary SCOPE-FB | PROVED CONDITIONAL | stated in §8 | yes: every scope run (§9) |

- §9 is data. §10 is NOT TO SIGN.
- Review order (Lead 15:04Z): P-N5-LV first, then this packet.

## 0. Objects, dependencies and their status
- Objects: as in P-N5-FBW §0 (R31), P-N5-LV §0 and P-N5-ENT §0: N5, S4a / S4c, Ξ, W, gates (Ξ_k-improving Even edges), gate levels,
  M_k, lev, COARSE_L, (C1)-(C7), b_k(y) := Ξ_k(σ_k y), θ, w, R̄ / R / F, H1-H3, (h), r := lev(θ, w), THR, EQ, u* (u* = none iff r = −1),
  phase (λ_Ξ and τ constant), scope run S, c (the common cycle node of θ and w along S), x_s := σ̄_s(o), n_E := the number of Even
  vertices.
  - A WINDOW GATE at k is a gate (y, z) with y ∈ R_k and z ∈ F_k (P-N5-RL §0).
  - The kinds (α), (β), (γ) of a gate at a level −1 THR fallback are those of P-N5-LV §1 (LV-SHAPE), for r ≥ 0 and for r = −1. A (β)
    gate is a window gate.
  - The LEVEL −1 BLOCK of a scope run S (P-N5-LV §4): its fallbacks f_1 < … < f_N with M = −1 and r ≥ 0.
    - They are consecutive fallbacks of S: levels are non-increasing (CLS2), r is non-increasing (Fact R), and −1 is the least level.
    - r ≥ 0 at every state of [f_1, f_N].
  - THE NONE PART of S: its THR fallbacks with r = −1, g_1 < … < g_N (§7).
  - An interval between consecutive fallbacks is DIRTY if COARSE_{−1}(Ξ) changes at some transition inside it, and CLEAN otherwise
    (R31 PL).
- LANDED (RESULTS), used:
  - SPEC S4c (docs/new/N5-ssi-global.md): at an Even fallback, every Even v with a gate switches to a ⊴-best gate target.
  - R15 (a) Ξ_k ⊴ Ξ_{k+1}; R15 (d) σ_{k+1}(v) ∈ {σ_k(v)} ∪ Iσ_k(v). So b_k(y) is ⊴-non-decreasing in k (P-N5-FBW §0).
  - R18 (d) Lemma S (a); R19 (a) Lemma G; R21 (a) XW; R25 (d) FB step (2), (e) OFF; R28 (a) U-loc (any game, inside a phase).
  - R29 (a) Fact R, (C5)-(C7); (b) TRANSFER; (c) OFFGATE; (d) CN; (e) NL (i)-(iii) (for every L < ∞ with r_j > L).
  - R30 (a) Lemma OR, (b) TC-SPLIT.
  - R31: CLS2; FBW-S (the fallback level is at most r); FLAT-ALL's proof with the FBW-1 repair (H1 at k + 1); STRETCH with the FBW-2 repair.
  - R35: PL-S′.
  - R37: (c) FREE-FREEZE (unconditional given R36); (d) EQ-END; (e) MERGE′ (window gates of level −1 ≤ ℓ < ∞).
  - R38: CN-LAST.
- CONVERGED, landing as R40: P-N5-ENT (sha1 4fd22be7; fixes docs/si/P-N5-ENT-fixes-box11.md, sha1 72d052b5).
  - Both referees signed §1-§3 (FZ, BF, RB, WALK, CYC-EV, TEV-FB) with no (P), at levels L ≥ 0.
  - They signed §4-§5 (ENT-X, NJB-A, D1, PL-S″) CONDITIONAL ON (P). The R36 lift is YES (REFEREE §C d6b8aef9).
  - §3 (e) below re-reads §1-§3 at L = −1, step by step. That re-reading is part of what is to be signed here.
- IN REVIEW, used: P-N5-LV (sha1 d0d797f0, pinned trunk 601df6e; addendum a15a8871):
  - §1 LV-SHAPE; §2 LV-CN (its CN-LAST condition is discharged by R38); §3 FLAT-ALL_{−1}, STRETCH_{−1}; §4 PL_{−1} (b).
  - Known pre-reading notes (REFEREE-2, via the Lead 15:16Z), and how this packet avoids inheriting them:
    - N-LV-1 (FLAT-ALL_{−1} (i) cites H2 where R31's FBW-1 repair says H1 at k + 1). This packet uses FLAT-ALL_{−1} only through (iii)
      and (iv). Its own §6 (i) is argued from H1 at k + 1 throughout.
    - N-LV-2 (STRETCH_{−1} is stated for k < e, but PL_{−1} (a) needs k = e). This packet never uses PL_{−1} (a), and every use of
      STRETCH_{−1} below counts only fallbacks k < e (§4 (iii), §7 (2)).

## 1. Lemma STALE-GATE (PROVED, L-SI succ. 7; every game)
Let k0 be an S4c fallback at which Even switches, and k > k0 a later state of the same run. Then every gate (y, z) at k has
Ξ_k(z) ≠ Ξ_{k0}(z).
Proof. Suppose Ξ_k(z) = Ξ_{k0}(z). Since (y, z) is a gate at k, b_k(y) ◁ Ξ_k(z).
- Case 1: Ξ_{k0}(z) ⊴ b_{k0}(y). Then Ξ_k(z) = Ξ_{k0}(z) ⊴ b_{k0}(y) ⊴ b_k(y), since b(y) is non-decreasing. Contradiction.
- Case 2: Ξ_{k0}(z) ▷ b_{k0}(y).
  - Then z ≠ σ_{k0}(y), so (y, z) is a gate at k0.
  - At the Even fallback k0, y switches to a ⊴-best gate target z′ (SPEC S4c). So Ξ_{k0}(z′) ⊵ Ξ_{k0}(z).
  - Then b_k(y) ⊵ b_{k0+1}(y) = Ξ_{k0+1}(z′) ⊵ Ξ_{k0}(z′) ⊵ Ξ_{k0}(z) = Ξ_k(z) (R15 (a)). Contradiction. □
- Remark. This replaces the rank-L bit of ENT-SHAPE (2)-(4) (R35). There the bit was used to show that the window gate's target z is
  bad at k0 and good at k, i.e. Ξ_k(z) ≠ Ξ_{k0}(z). STALE-GATE gives this for every gate, at every level, including −1.

## 2. Corollary EV-G (PROVED, L-SI succ. 7)
Let k0 be an in-phase THR S4c fallback with (h), and k > k0 a state of the same phase. If (y, z) is a gate at k with z ∈ F_k, then z's
σ_k-play is not contained in F_{k0}.
- Proof. If it were, FREE-FREEZE (R37 (c)) would give Ξ_k(z) = Ξ_{k0}(z), against STALE-GATE. □
- Remark. In P-N5-RL's ENT setting (levels L ≥ 0) this is the first half of Proposition EV, obtained here without ENT-SHAPE (4). With no
  leave on (k0, k] (NL (ii)), z's play then meets Ev := F_{k0+1} ∖ F_{k0}.

## 3. Theorem ENT-X_{−1} (PROVED, L-SI succ. 7, CONDITIONAL on P-N5-LV §3 and §4)
Let k0 < k be consecutive fallbacks of a scope run S that both lie in its level −1 block. So M_{k0} = M_k = −1, and r ≥ 0 at every state of
[k0, k]. If k has a window gate (by LV-SHAPE, equivalently a (β) gate), then the interval (k0, k) is clean.
Proof. Suppose (k0, k) is dirty. Put L := −1 and H := V_{>max(L, rank c)} = V_{>c}.
- (a) A rise.
  - By PL_{−1} (b) (P-N5-LV §4), the first change j is an S4a step with lev(θ_j, θ_{j+1}) = O_j > −1. So COARSE_{−1}(θ) changes in
    (k0, k).
  - Every P(·) lies in V_{>c}, so A := P(θ_{k0}) ∩ H = P(θ_{k0}) and B := P(θ_k) ∩ H = P(θ_k).
  - θ is monotone (R15 (a)), and both values have cycle node c. So B ≠ A.
- (b) The facts (Σ1)-(Σ6) of P-N5-ENT §0 hold at L = −1.
  - (Σ1) No fallback lies in (k0, k), and τ is constant (phase).
  - (Σ2) (h) holds at every state of [k0, k], since each is the source of a transition of S. (A_s) holds for L = −1 on [k0+1, k]:
    - OFFGATE gives gates into F of level ≤ M_{k0} = −1 at k0 + 1;
    - then NL (iii) at each S4a step, which needs only r_s > −1.
  - (Σ3) No leave (NL (ii)). So F_k ⊆ F_s ⊆ F_{k0+1} = F_{k0} ⊔ Ev for s ∈ [k0+1, k], where Ev := F_{k0+1} ∖ F_{k0}.
  - (Σ4) M_k ≤ −1 (CLS2). (Σ5) c ∈ F_{k0} ∩ F_k (H1). (Σ6) is (a).
- (c) EV at L = −1. Let (y, z) be a window gate at k. Its level is M_k = −1.
  - By EV-G, z's σ_k-play is not contained in F_{k0}. It lies in F_k ⊆ F_{k0+1}, so it meets Ev.
  - Let q be its first Ev vertex, ρ the part of the play before q, and π_q q's route at k0. Bookkeeping as in P-N5-RL §6 (EV):
    - Ξ_k(z) = ρ ⊕ Ξ_k(q), with ρ ∩ P(Ξ_k q) = ∅ (the play is simple before its cycle).
    - q ∈ F_s for s ∈ [k0+1, k] (no leave). So COARSE_{−1}(Ξ_k q) = COARSE_{−1}(Ξ_{k0} q):
      - NL (i) with L = −1 at the S4a steps;
      - FLAT-ALL_{−1} (iii) across k0 (P-N5-LV §3; r_{k0} ≥ 0, (h) at k0 and k0 + 1). This is the first condition.
      In particular P(Ξ_k q) = P(Ξ_{k0} q), with cycle node c.
    - P(Ξ_{k0} q) = (π_q ∩ H) ⊔ A (Lemma G at k0, since q ∈ Ev ⊆ R_{k0}).
    - MERGE′ (a)-(b) at level −1 (R37 (e)): y's route has no H-vertex, P(Ξ_k z) ∩ H = P(θ_k) ∩ H = B, and o ∉ H.
    - Hence B = (ρ ∩ H) ⊔ (π_q ∩ H) ⊔ A. With (a), A ⊊ B.
- (d) EV+ at L = −1: the σ_k-play of x_k meets Ev. Let h be the top of B ∖ A.
  - If h ∈ ρ: by MERGE′ (c) at level −1, every H-vertex of z's play lies on the suffix that z's play shares with x_k's play. q comes after
    h on z's play, so q lies on x_k's play.
  - If h ∈ π_q:
    - h ∈ B ⊆ P(θ_k) and h ≠ o (routes avoid o). So h lies on x_k's play, which is in F_k (H1).
    - Also h ∈ π_q ⊆ R_{k0}. So h ∈ F_k ∖ F_{k0} ⊆ Ev.
- (e) TEV-FB at L = −1: the σ_k-play of x_k avoids Ev. These are P-N5-ENT §1-§3, read at L = −1 under (b):
  - Lemma FZ: across k0, FLAT-ALL_{−1} (iii) replaces FLAT-ALL (iii) (the first condition again); at the S4a steps, NL (i) with L = −1,
    whose hypotheses are (Σ2) and r_s > −1.
  - Lemma BF: uses (P2), (C4), Lemma G, (Σ5) and FZ. No level is used.
  - Lemma RB: its only level step is "a gate at k of level > L ≥ M_k is impossible". At L = −1 this is (Σ4).
  - Corollary WALK: uses RB and Lemma G, with H = V_{>c}.
  - Lemma CYC-EV: uses (Σ6), FZ, Lemma G and WALK (c). At L = −1, "COARSE_L(Ξ_k v) = (c, ∅)" reads P(Ξ_k v) = ∅.
  - Proposition TEV-FB: Steps 1-4 use (Σ3), (Σ6), FZ, BF and WALK (c). Step 2's "o ∉ H" holds as in P-N5-ENT; MERGE′ (b) also gives it.
- (d) and (e) contradict each other. □
- Where the conditions enter:
  - P-N5-LV §4 (PL_{−1} (b)): only in (a);
  - P-N5-LV §3 (FLAT-ALL_{−1} (iii)): in (c) and in FZ.

## 4. Corollary LV-PL′ (PROVED, L-SI succ. 7, CONDITIONAL on P-N5-LV §1-§4)
Every scope run S has at most n·n_E + 1 THR fallbacks with M = −1 and r ≥ 0.
Proof. Let f_1 < … < f_N be its level −1 block. If N ≤ 1 there is nothing to show.
- (i) Every interval (f_i, f_{i+1}) with i + 1 < N is clean.
  - Suppose f_{i+1} has no (β) gate. Then LV-CN (P-N5-LV §2, with CN-LAST = R38) says f_{i+1} + 1 is the last state of its phase. S is
    in-phase, so f_{i+1} is the last fallback of S, i.e. i + 1 = N.
  - So for i + 1 < N, f_{i+1} has a (β) gate, which is a window gate. ENT-X_{−1} makes (f_i, f_{i+1}) clean.
- (ii) COARSE_{−1}(Ξ_t v) is the same for all t ∈ [f_1, f_{N−1} + 1] and every v.
  - The intervals inside are clean by (i).
  - At each f_i with i < N, FLAT-ALL_{−1} (iii) applies: r_{f_i} ≥ 0, and (h) holds at f_i + 1 because S continues after f_i.
- (iii) Each of f_1, …, f_{N−1} has a level −1 tail (FB step (2)). STRETCH_{−1} (P-N5-LV §3) with s := f_1 and e := f_{N−1} + 1 counts
  the fallbacks k with s ≤ k < e, which are f_1, …, f_{N−1}. It gives N − 1 ≤ n·n_E. □
- Comparison:
  - P-N5-LV's Corollary LV-PL gave ≤ n·n_E·(d_o + REL(S)). REL(S) and d_o are gone.
  - The one interval allowed to be dirty is the block's last, ending at a (β)-free fallback that ends the phase.
  - P-N5-ENT's Corollary D1 is the level ≥ 0 analogue. There a straddling interval can also be dirty; at level −1 none exists, since
    r ≥ 0 throughout the block.

## 5. Lemma SAND (PROVED, L-SI succ. 7)
If t ≤ t′ are states of a scope run S with r_t = −1, then COARSE_{−1}(θ_{t′}) = COARSE_{−1}(θ_t).
- Proof. θ_t ⊴ θ_{t′} (R15 (a)), and θ_{t′} ⊴ w_{t′} = w_t (XW; w is constant on S). If θ_t ◁ θ_{t′}, then (C5) gives
  lev(θ_t, θ_{t′}) ≤ lev(θ_t, w_t) = r_t = −1. So the COARSE_{−1} values are equal (C2). □
- (This is Fact R's proof, read at r = −1.)
- Consequences inside the none part of S (§0, §7):
  - every state of [g_1, g_N] has r = −1. Fact R gives r ≤ −1 after g_1, and r ≥ r_{g_N} = −1 before g_N.
  - every S4c fallback of S inside [g_1, g_N] is one of the g_i: it has r = −1, so it is THR and not EQ.
  - by FBW-S, every g_i has M = −1.

## 6. Lemma FLAT-ALL_{−1}^{none} (PROVED, L-SI succ. 7, CONDITIONAL on P-N5-LV §1)
Let k be a fallback of a scope run with r_k = −1 (so M_k = −1 by FBW-S), and (h) at k and k + 1. Then R31 FLAT-ALL (i)-(iv) hold with
M := −1:
- (i) F_k ⊆ F_{k+1}, and every v ∈ R̄_{k+1} lies in R̄_k with the same route;
- (ii) COARSE_{−1}(θ_{k+1}) = COARSE_{−1}(θ_k);
- (iii) COARSE_{−1}(Ξ_{k+1} v) = COARSE_{−1}(Ξ_k v) for every v;
- (iv) M_{k+1} ≤ −1.
Proof.
- The switched edges. Each tail switches along a gate (R15 (d)). By LV-SHAPE (setting (LV), which includes r = −1), each gate is:
  - (α) F → F at the tail's own cycle node; or
  - (γ) F → R̄ at the tail y = c; or
  - (β) R → F.
  R31's proof instead uses FBL (u* ≠ none), which is unavailable here. LV-SHAPE replaces it. (γ) is the only kind FBL does not allow.
- (i) R31's proof with the FBW-1 repair (H1 at k + 1, not H2), plus one new point for (γ).
  - Let y′ be a switched cycle node (kind (α) or (γ)). It keeps λ(y′) = y′ (phase), so its H_{k+1}-play is a cycle through y′, its
    honest cycle.
    - If that cycle contained o, H1 would fail at k + 1. So it avoids o.
    - Off o the honest graph and the (σ, τ)-graph agree. So y′'s (σ_{k+1}, τ)-play is the same cycle, and y′ ∈ F_{k+1}.
    - For (γ) this is the new point: the target z lies in R̄_k, yet y′'s new play avoids o.
  - An F_k vertex's play under σ_{k+1}:
    - it follows σ_k inside F_k (F_k is closed under σ_k) until it meets a switched cycle node;
    - from there it follows that node's cycle, which avoids o;
    - (β) tails lie in R_k, so they are not met.
    So F_k ⊆ F_{k+1}.
  - A play that reaches o at k + 1 meets no switched vertex:
    - after a (β) tail it would continue in F_k, whose plays avoid o;
    - after a switched cycle node it would stay on that node's cycle, which avoids o.
    So it is the same play as at k, with the same route.
- (ii)-(iv): R31's proof verbatim.
  - It uses (i), H1, Lemma S (a), R15 (a), OFF at level M_k = −1, (C7), (C1), (C3), Lemma G (b) at k and k + 1 with the same route, and
    TRANSFER. None of these uses u* ≠ none.
  - (ii) also follows from SAND. □

## 7. Theorem LV-NONE (PROVED, L-SI succ. 7, CONDITIONAL on P-N5-LV §1, §3)
Every scope run S has at most n·n_E + 1 THR fallbacks with r = −1 (u* = none).
Proof. Let g_1 < … < g_N be those fallbacks. If N ≤ 1 there is nothing to show.
- (1) COARSE_{−1}(Ξ_t v) is the same for every t ∈ [g_1, g_{N−1} + 1] and every v. Induction along the states:
  - At each g_i with i < N: FLAT-ALL_{−1}^{none} (iii) and (iv).
    - (h) holds at g_i + 1, because S continues after g_i: its next transition is in S, and S's transitions have (h) at their source.
    - (iv) gives M_{g_i+1} ≤ −1.
  - At an S4a step j ∈ (g_i, g_{i+1}): suppose COARSE_{−1}(Ξ) is unchanged on [g_i + 1, j]. This is the argument of P-N5-LV's PL_{−1}
    (b), written here with landed lemmas only:
    - M_j ≤ −1, by TRANSFER from M_{g_i+1} ≤ −1;
    - every relevant Even change at j has level ≤ M_j ≤ −1 (R15 (d)), so E_j ≤ −1;
    - U-loc with L = −1 (R28 (a): any game, inside a phase) freezes COARSE_{−1}(Ξ v) unless v's path before λ(v) carries a relevant change
      of level > −1. So a change at j needs a relevant σ̄(o) change with O_j > −1 ≥ E_j: j is an ε-transition;
    - Lemma OR (c) (R30 (a)) then gives lev(θ_j, θ_{j+1}) = O_j ≥ 0;
    - but r_j = −1 (§5), so SAND gives lev(θ_j, θ_{j+1}) ≤ −1. Contradiction.
    So COARSE_{−1}(Ξ_{j+1}) = COARSE_{−1}(Ξ_j).
  - Every fallback of S strictly inside [g_1, g_N] is some g_i (§5).
- (2) Each g_i has a level −1 tail (FB step (2): M = −1 is attained by a switched edge). STRETCH_{−1} (P-N5-LV §3) with s := g_1 and
  e := g_{N−1} + 1 counts the fallbacks k with s ≤ k < e, which are g_1, …, g_{N−1}. It gives N − 1 ≤ n·n_E.
  - STRETCH_{−1}'s proof uses only the constant COARSE_{−1}, CN (R29 (d)), (P2), (C7), R15 (a), (d) and FB step (2). It has no r
    hypothesis.
- So N ≤ n·n_E + 1. □
- Note. Neither NL nor FBL is used. P-N5-LV §5 (i) names the missing "NL at L = −1"; it is not needed. SAND makes every θ-change at
  r = −1 a length change, and U-loc + OR show that only a θ-change of level ≥ 0 could move COARSE_{−1}(Ξ).

## 8. Corollary SCOPE-FB (PROVED CONDITIONAL, L-SI succ. 7)
Every scope run has at most 4·n·n_E + 3 S4c fallbacks.
Conditions, explicitly:
- (C-ENT) P-N5-ENT §5 PL-S″ (converged; R36 lift YES; landing as R40);
- (C-LV) P-N5-LV §1-§4 (in review);
- (C-PKT) this packet's §1-§7 (in review).
Without (C-ENT), the same proof gives n_E·(n·d_o + REL(S)) + 2·n·n_E + 3, using R35 PL-S′ instead.
Proof.
- Every fallback of S has (h) at its source state, and is in-phase, hence an Even fallback. It is EQ (r = ⊥) or THR.
- A THR fallback has r ≥ 0 or r = −1. If r ≥ 0, its level is ≥ 0 or −1. So the four classes below are disjoint and cover every fallback
  of S.
- The bounds:
  - level ≥ 0: ≤ 2·n·n_E (PL-S″; condition (C-ENT));
  - level −1 with r ≥ 0: ≤ n·n_E + 1 (§4; conditions (C-LV), (C-PKT));
  - r = −1: ≤ n·n_E + 1 (§7; conditions (C-LV) §1, §3, and (C-PKT));
  - EQ: ≤ 1. R37 (d) EQ-END: after the first state with θ = w, at most one fallback. CN-LAST, its condition, is R38.
- Sum: 4·n·n_E + 3. □
- Reading (not to sign): this closes R29's per-scope-run fallback count (CL-S) up to the conditions. G-N5-TIME still needs the rest:
  - scope runs per phase (R38 SCOPE-COUNT: polynomial in (T, f, X));
  - out-of-scope fallbacks;
  - S4a steps;
  - phases, and X.

## 9. DATA (DATA, not proof; experiments/si/lv/, logs experiments/si/lv/logs/)
- Sets:
  - NAMED: experiments/si/lv/named.lst (coarse/named.txt, coarse/instances, riselast/instances, red/so/instances; 102 files);
  - LIB: experiments/new/box33/lib.txt (234, first column).
- Runs are asserted equal to n5.py run() (coarse/mono.states). Only 𝒞^1O games are used: a game is skipped unless exactly one Odd vertex
  has out-degree > 1 (mono.odd_choice).
- stale.py:
  - STALE-GATE is checked at every pair (k0, k) with k0 an Even S4c fallback and k > k0 in the same run, for every gate (y, z) at k.
  - EV-G is checked at every pair with k0 an in-phase THR fallback with (h) and k in the same phase (key (λ_Ξ, τ, λ_U), as
    reltrace.runs_of), for every gate target z ∈ F_k.
- scopefb.py (per scope run, reltrace.runs_of):
  - SAND: after the first in-scope state with r = −1, COARSE_{−1}(θ) is checked at every later state of the run;
  - fallbacks by class, and the largest ratio of fallbacks to 4·n·n_E + 3.
- lvm1.py (P-N5-LV §6) and betasearch.py (N5-LV3, with perturbed start pairs): the level −1 block and the none part of every scope run
  are empty.

| set | STALE-GATE checks / fail | EV-G checks / fail | in-scope transitions with r = −1 | SAND checks / fail | scope runs | fallbacks per class (≥ 0 / −1, r ≥ 0 / r = −1 / EQ) | max per run | worst ratio to 4·n·n_E + 3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NAMED | 25,442 / 0 | 13,357 / 0 | 108 | 220 / 0 | 111 | 387 / 0 / 0 / 6 | 37 | 0.0067 (ccl_fbx_n32: 24 at n 32, n_E 28) |
| LIB | 47,147 / 0 | 26,049 / 0 | 47 | 90 / 0 | 182 | 526 / 0 / 0 / 8 | 33 | 0.0196 (n4all_maxph_0: 1 at n 4, n_E 3) |

- Thin spots, stated plainly:
  - The level −1 block and the none part are empty in all data. ENT-X_{−1}, LV-PL′'s block, FLAT-ALL_{−1}^{none} and LV-NONE have vacuous
    hypotheses there and rest on the proofs.
  - STALE-GATE, EV-G and SAND are exercised non-vacuously. SCOPE-FB's bound holds with a large margin.

## 10. NOT TO SIGN
- Lane, not in this packet: docs/si/N5-LV3-box12.md (sha1 20ba05d7). It holds Lemma XG, Lemma ANTI and Corollary NEED-β, and the
  CONJECTURE "in scope, THR ⇒ M ≥ 0" with its exact obstruction.
- OPEN: G-N5-TIME.
