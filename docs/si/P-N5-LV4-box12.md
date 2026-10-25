# Referee packet P-N5-LV4: stale gates, and REL(S) removed at level −1 (ENT-X_{−1}, LV-PL′) (box 12)
L-SI successor 7 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~15:20Z (date -u), at the Lead's request (15:04Z). Frozen at
its commit: corrections go in a fixes file, never here.
- Self-contained: definitions, statements, full proofs, the status of every dependency, the data and the script.
- Source text: docs/si/N5-LV4-box12.md (lane write-up, l-si 689f7b61, sha1 9d1b90f4). Where they differ, this packet governs.
- Status: L-SI successor 7's proofs, unrefereed. Labels: PROVED (L-SI succ. 7); PROVED CONDITIONAL on X; OPEN; DATA.
- §1 holds on every game. §2-§4 are on 𝒞^1O: exactly one Odd vertex o with out-degree > 1. The script asserts it.
- These are lemmas about the candidate N5. They are not a running-time bound, not a TARGET.md claim, and not a step-4 pass.
  G-N5-TIME stays OPEN.
- Statements to sign:

| § | statement | label | condition |
| --- | --- | --- | --- |
| §1 | Lemma STALE-GATE | PROVED | none (every game) |
| §2 | Corollary EV-G | PROVED | none |
| §3 | Theorem ENT-X_{−1} | PROVED CONDITIONAL | P-N5-LV §3 (FLAT-ALL_{−1}) and §4 (PL_{−1} (b)) |
| §4 | Corollary LV-PL′ | PROVED CONDITIONAL | P-N5-LV §1-§4 |

- §5 is NOT TO SIGN. §6: data.
- Review order: P-N5-LV (sha1 d0d797f0, with its addendum a15a8871) first. This packet is queued right behind it (Lead 15:04Z).

## 0. Objects, dependencies and their status
- Objects: as in P-N5-FBW §0 (R31), P-N5-LV §0 and P-N5-ENT §0: N5, S4a / S4c, Ξ, W, gates (Ξ_k-improving Even edges), gate levels,
  M_k, lev, COARSE_L, (C1)-(C7), b_k(y) := Ξ_k(σ_k y), θ, w, R̄ / R / F, H1-H3, (h), r := lev(θ, w), THR, phase (λ_Ξ and τ constant),
  scope run S, c (the common cycle node of θ and w along S), x_s := σ̄_s(o).
  - A WINDOW GATE at k is a gate (y, z) with y ∈ R_k and z ∈ F_k (P-N5-RL §0).
  - The kinds (α), (β), (γ) of a gate at a level −1 THR fallback are those of P-N5-LV §1 (LV-SHAPE). A (β) gate is exactly a window
    gate there.
  - The LEVEL −1 BLOCK of a scope run S (P-N5-LV §4): its fallbacks f_1 < … < f_N with M = −1 and r ≥ 0.
    - They are consecutive fallbacks of S: levels are non-increasing (CLS2), r is non-increasing (Fact R), and −1 is the least level.
    - r ≥ 0 at every state of [f_1, f_N].
  - An interval (f_i, f_{i+1}) is DIRTY if COARSE_{−1}(Ξ) changes at some transition inside it, and CLEAN otherwise (R31 PL).
- LANDED (RESULTS), used:
  - SPEC S4c (docs/new/N5-ssi-global.md): at an Even fallback, every Even v with a gate switches to a ⊴-best gate target.
  - R15 (a) Ξ_k ⊴ Ξ_{k+1}; R15 (d) σ_{k+1}(v) ∈ {σ_k(v)} ∪ Iσ_k(v). So b_k(y) is ⊴-non-decreasing in k (P-N5-FBW §0).
  - R19 (a) Lemma G; R29 (a) Fact R, (C5)-(C7); R29 (c) OFFGATE; R29 (e) NL (i)-(iii) (for every L < ∞ with r_j > L); R31 CLS2, FB
    step (2) (R25 (d)).
  - R37 (c) FREE-FREEZE (unconditional given R36); R37 (e) MERGE′ (window gates of level −1 ≤ ℓ < ∞).
  - R38 (CN-LAST).
- SIGNED by both referees, in landing: P-N5-ENT (sha1 4fd22be7; fixes docs/si/P-N5-ENT-fixes-box11.md, sha1 72d052b5).
  - §1-§3 (FZ, BF, RB, WALK, CYC-EV, TEV-FB) are signed with no (P), at levels L ≥ 0.
  - §3 (e) below re-reads them at L = −1, step by step. That re-reading is part of what is to be signed here.
- IN REVIEW, used: P-N5-LV (sha1 d0d797f0): §1 LV-SHAPE; §2 LV-CN (its CN-LAST condition is discharged by R38); §3 FLAT-ALL_{−1},
  STRETCH_{−1}; §4 PL_{−1} (a)-(b).

## 1. Lemma STALE-GATE (PROVED, L-SI succ. 7; every game)
Let k0 be an S4c fallback at which Even switches, and let k > k0 be a later state of the same run. Then every gate (y, z) at k has
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
- Remark. In P-N5-RL's ENT setting (levels L ≥ 0) this is the first half of Proposition EV, obtained here without ENT-SHAPE (4). Together
  with no leave on (k0, k] (NL (ii)), it gives that z's play meets Ev := F_{k0+1} ∖ F_{k0}.

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
  - (Σ1) No fallback lies in (k0, k), since k0 and k are consecutive, and τ is constant (phase).
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
  - Suppose f_{i+1} has no (β) gate. Then LV-CN (P-N5-LV §2; CN-LAST is R38) says f_{i+1} + 1 is the last state of its phase. S is
    in-phase, so f_{i+1} is the last fallback of S, i.e. i + 1 = N.
  - So for i + 1 < N, f_{i+1} has a (β) gate, which is a window gate. ENT-X_{−1} makes (f_i, f_{i+1}) clean.
- (ii) COARSE_{−1}(Ξ_t v) is the same for all t ∈ [f_1, f_{N−1} + 1] and every v.
  - The intervals inside are clean by (i).
  - At each f_i with i < N, FLAT-ALL_{−1} (iii) applies: r_{f_i} ≥ 0, and (h) holds at f_i + 1 because S continues after f_i.
- (iii) Each of f_1, …, f_{N−1} has a level −1 tail (FB step (2)). STRETCH_{−1} (P-N5-LV §3) on [f_1, f_{N−1} + 1] gives N − 1 ≤ n·n_E. □
- Comparison with P-N5-LV:
  - Corollary LV-PL there gave ≤ n·n_E·(d_o + REL(S)). REL(S) and d_o are gone.
  - The one interval allowed to be dirty is the block's last, ending at a (β)-free fallback that ends the phase.
  - Corollary D1 (P-N5-ENT §5, now R36-unconditional) is the level ≥ 0 analogue, where a straddling interval can also be dirty. At level
    −1 none exists, since r ≥ 0 throughout the block.

## 5. NOT TO SIGN
- Lane, not in this packet: docs/si/N5-LV5-box12.md (l-si 0bf9a899, sha1 e2cb0703). It contains Lemma SAND, FLAT-ALL_{−1}^{none},
  Theorem LV-NONE (≤ n·n_E + 1 THR fallbacks with u* = none per scope run) and Corollary SCOPE-FB (≤ 4·n·n_E + 3 fallbacks per scope run).
  It becomes a packet only on the Lead's GO.
- Lane, not in this packet: docs/si/N5-LV3-box12.md (sha1 20ba05d7). It contains Lemma XG, Lemma ANTI and Corollary NEED-β, and CONJECTURE
  "in scope, THR ⇒ M ≥ 0", with its exact obstruction.
- OPEN: G-N5-TIME.

## 6. DATA (DATA, not proof; experiments/si/lv/stale.py, logs experiments/si/lv/logs/stale_named.txt, stale_lib.txt)
- STALE-GATE: every pair (k0, k) with k0 an Even S4c fallback and k > k0 in the same run. Every gate (y, z) at k is checked for
  Ξ_k(z) ≠ Ξ_{k0}(z).
- EV-G: every pair with k0 an in-phase THR fallback with (h) and k in the same phase (key (λ_Ξ, τ, λ_U), as reltrace.runs_of). Every
  gate target z ∈ F_k is checked for a σ_k-play not contained in F_{k0}.
- Runs are asserted equal to n5.py run() (coarse/mono.states). Only 𝒞^1O games are used: a game is skipped unless exactly one Odd vertex
  has out-degree > 1 (mono.odd_choice). Both checks run on every game kept.

| set | STALE-GATE checks | failures | EV-G checks | failures |
| --- | --- | --- | --- | --- |
| NAMED (experiments/si/lv/named.lst: coarse/named.txt, coarse/instances, riselast/instances, red/so/instances; 102 files) | 25,442 | 0 | 13,357 | 0 |
| LIB (experiments/new/box33/lib.txt, 234, first column) | 47,147 | 0 | 26,049 | 0 |

- Thin spot: the level −1 block is empty in all data (P-N5-LV §6). ENT-X_{−1} and LV-PL′ have vacuous hypotheses there and rest on the
  proofs. STALE-GATE and EV-G are exercised non-vacuously.
