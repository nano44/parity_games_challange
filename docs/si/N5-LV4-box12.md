# N5 box 12, part 2 (L-SI successor 7): REL(S) removed at level −1; the level −1 block has at most n·n_E + 1 fallbacks
L-SI successor 7 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~15:00Z (date -u). Lead GO 14:18Z, box 12, item (1)(b): "a
length-based ENT-SHAPE to drop REL(S)". Lane write-up, unrefereed; offered as a packet on request.
- Labels: PROVED (L-SI succ. 7); PROVED CONDITIONAL on X; CONJECTURE; OPEN; DATA.
- Everything is on 𝒞^1O. Not a running-time bound, not a TARGET.md claim, not a step-4 pass. G-N5-TIME stays OPEN.
- Result in one paragraph.
  - ENT-SHAPE (4)'s rank-L bit is needed only to show one thing: the target z of the window gate at k changed its honest value since
    k0. That follows for EVERY gate at every later state from monotonicity and the S4c switching rule alone (Lemma STALE-GATE, PROVED).
  - With it, P-N5-RL's EV and EV+ and P-N5-ENT's TEV-FB all run at L = −1. So ENT-X holds at level −1: a level −1 interval whose right
    end has a (β) gate is clean (Theorem ENT-X_{−1}).
  - A right end without a (β) gate ends its phase (LV-CN; CN-LAST is now landed as R38). So the level −1 block of a scope run has at
    most one dirty interval, the last one.
  - Corollary LV-PL′: every scope run has at most n·n_E + 1 THR fallbacks with M = −1 and r ≥ 0. P-N5-LV had n·n_E·(d_o + REL(S)).
    REL(S) and d_o are gone at level −1.
  - Conditions: P-N5-LV §1-§3 (in review), and P-N5-ENT §1-§3 restated at L = −1 (REFEREE signed them at L ≥ 0; their L = −1 reading is
    checked line by line in §3 below).
- Side result: STALE-GATE also gives P-N5-RL's EV at levels L ≥ 0 without ENT-SHAPE (4) (§2, remark).

## 0. Objects and dependencies
- As in P-N5-LV §0 (sha1 d0d797f0), P-N5-ENT §0 (sha1 4fd22be7) and P-N5-RL §0 (R37).
  - A WINDOW GATE at k is a gate (y, z) with y ∈ R_k, z ∈ F_k (P-N5-RL §0).
  - b_k(y) := Ξ_k(σ_k y).
- LANDED, used:
  - R15 (a) Ξ_k ⊴ Ξ_{k+1}; R15 (d) σ_{k+1}(v) ∈ {σ_k(v)} ∪ Iσ_k(v).
  - SPEC S4c (an Even fallback switches every Even v with a gate to a ⊴-best gate target).
  - R19 (a) Lemma G; R29 (a) Fact R, (C5)-(C7); R29 (c) OFFGATE; R29 (e) NL (i)-(iii) (any L < ∞ with r_j > L); R31 CLS2, FBW-S.
  - R37 (c) FREE-FREEZE (unconditional given R36); R37 (e) MERGE′ (window gates of level −1 ≤ ℓ < ∞).
  - R38 CN-LAST.
- IN REVIEW, used:
  - P-N5-LV (sha1 d0d797f0): LV-SHAPE (§1), LV-CN (§2; its CN-LAST condition is discharged by R38), FLAT-ALL_{−1} and STRETCH_{−1} (§3),
    PL_{−1} (a)-(b) (§4).
  - P-N5-ENT (sha1 4fd22be7; REFEREE signed §1-§3 at L ≥ 0, R-N5-ENT 55a3f6f): FZ, BF, RB, WALK, CYC-EV, TEV-FB, used here at L = −1
    (§3).
- The LEVEL −1 BLOCK of a scope run S (P-N5-LV §4): its fallbacks f_1 < … < f_N with M = −1 and r ≥ 0. They are consecutive fallbacks
  of S, and r ≥ 0 at every state of [f_1, f_N] (Fact R).
  - An interval (f_i, f_{i+1}) is DIRTY if COARSE_{−1}(Ξ) changes at some transition inside it (R31 PL).

## 1. Lemma STALE-GATE (PROVED, L-SI succ. 7; every game)
Let k0 be an S4c fallback at which Even switches, and k > k0 a later state of the same run. Then every gate (y, z) at k has
Ξ_k(z) ≠ Ξ_{k0}(z).
Proof. Suppose Ξ_k(z) = Ξ_{k0}(z).
- b(y) is ⊴-non-decreasing (R15 (a), (d); P-N5-FBW §0). (y, z) is a gate at k, so b_k(y) ◁ Ξ_k(z).
- Case 1: Ξ_{k0}(z) ⊴ b_{k0}(y). Then Ξ_k(z) = Ξ_{k0}(z) ⊴ b_{k0}(y) ⊴ b_k(y), so (y, z) is not a gate at k.
- Case 2: Ξ_{k0}(z) ▷ b_{k0}(y).
  - Then z ≠ σ_{k0}(y), so (y, z) is a gate at k0.
  - At the Even fallback k0, y switches to a ⊴-best gate target z′ (SPEC S4c), so Ξ_{k0}(z′) ⊵ Ξ_{k0}(z).
  - Then b_k(y) ⊵ b_{k0+1}(y) = Ξ_{k0+1}(z′) ⊵ Ξ_{k0}(z′) ⊵ Ξ_{k0}(z) = Ξ_k(z), so (y, z) is not a gate at k. □
- Remark. This replaces the rank-L bit of ENT-SHAPE (2)-(4) (R35). There the bit was used to show that the window gate's target z is
  "bad at k0 and good at k", i.e. Ξ_k(z) ≠ Ξ_{k0}(z). STALE-GATE gives this for every gate, at every level, including −1.

## 2. Corollary EV-G (PROVED, L-SI succ. 7)
Let k0 be an in-phase THR S4c fallback with (h), and k > k0 a state of the same phase. If (y, z) is a gate at k with z ∈ F_k, then z's
σ_k-play leaves F_{k0}.
- Proof. If the play lay in F_{k0}, FREE-FREEZE (R37 (c)) would give Ξ_k(z) = Ξ_{k0}(z), against STALE-GATE. □
- Remark. In P-N5-RL's ENT setting (L ≥ 0), this is the first half of Proposition EV, with no use of ENT-SHAPE (4). There, as at L = −1
  below, no leave on (k0, k] (NL (ii)) gives F_k ⊆ F_{k0+1}, so the play meets Ev := F_{k0+1} ∖ F_{k0}.

## 3. Theorem ENT-X_{−1} (PROVED, L-SI succ. 7, CONDITIONAL on P-N5-LV §3 (FLAT-ALL_{−1}))
Let k0 < k be consecutive fallbacks of a scope run S, both of the level −1 block (so M_{k0} = M_k = −1 and r ≥ 0 at every state of
[k0, k]). If k has a window gate (equivalently, by LV-SHAPE, a (β) gate), then the interval (k0, k) is clean.
Proof. Suppose (k0, k) is dirty.
- (a) A rise. By PL_{−1} (b), the first change j is an S4a step with lev(θ_j, θ_{j+1}) = O_j > −1. So COARSE_{−1}(θ) changes in (k0, k).
  - Put L := −1 and H := V_{>max(L, rank c)} = V_{>c}. Then A := P(θ_{k0}) ∩ H = P(θ_{k0}) and B := P(θ_k) (every P(·) lies in V_{>c}).
  - So B ≠ A ((Σ6) of P-N5-ENT §0: θ is monotone and both values have cycle node c).
- (b) The facts (Σ1)-(Σ6) of P-N5-ENT §0 hold at L = −1:
  - (Σ1) No fallback in (k0, k): k0, k are consecutive.
  - (Σ2) (A_s) for L = −1 on [k0+1, k]: OFFGATE at k0+1 gives gates into F of level ≤ M_{k0} = −1; then NL (iii) at each S4a step,
    which needs only r_s > −1.
  - (Σ3) No leave: NL (ii). So F_k ⊆ F_s ⊆ F_{k0+1} = F_{k0} ⊔ Ev for s ∈ [k0+1, k].
  - (Σ4) M_k ≤ −1 (CLS2). (Σ5) c ∈ F_{k0} ∩ F_k (H1). (Σ6) is (a).
- (c) EV at L = −1. Let (y, z) be a window gate at k.
  - Its level is −1 = M_k.
  - By EV-G, z's σ_k-play leaves F_{k0}. It lies in F_k ⊆ F_{k0+1}, so it meets Ev. Let q be its first Ev vertex, ρ the part before q,
    and π_q q's route at k0.
  - Bookkeeping, exactly as P-N5-RL §6's proof of EV:
    - Ξ_k(z) = ρ ⊕ Ξ_k(q), with ρ ∩ P(Ξ_k q) = ∅.
    - q ∈ F on [k0+1, k]. So P(Ξ_k q) = P(Ξ_{k0} q): NL (i) at L = −1 on the S4a steps, FLAT-ALL_{−1} (iii) across k0 (r_{k0} ≥ 0,
      (h) at k0 and k0 + 1). This is the condition.
    - P(Ξ_{k0} q) = (π_q ∩ H) ⊔ A (Lemma G at k0, q ∈ R_{k0}).
    - MERGE′ (a)-(b) at level −1 (R37 (e)): P(Ξ_k z) ∩ H = B, and o ∉ H.
    - Hence B = (ρ ∩ H) ⊔ (π_q ∩ H) ⊔ A. In particular A ⊊ B.
- (d) EV+ at L = −1: the σ_k-play of x_k := σ̄_k(o) meets Ev.
  - Let h be the top of B ∖ A.
  - If h ∈ ρ: MERGE′ (c) at level −1 puts every H-vertex of z's play on the suffix it shares with x_k's play. q comes after h, so q
    lies on x_k's play.
  - If h ∈ π_q: h ∈ B ⊆ P(θ_k), h ≠ o, so h lies on x_k's play, in F_k. Also h ∈ π_q ⊆ R_{k0}, so h ∈ F_{k0+1} ∖ F_{k0} = Ev.
- (e) TEV-FB at L = −1: x_k's σ_k-play avoids Ev. P-N5-ENT §1-§3 read at L = −1, step by step:
  - Lemma FZ: across k0, FLAT-ALL_{−1} (iii) (the condition) in place of FLAT-ALL (iii); at S4a steps, NL (i) with L = −1, under (Σ2).
  - Lemma BF: (P2), (C4) and FZ. No level is used.
  - Lemma RB: its only level step is "a gate at k of level > L ≥ M_k is impossible". At L = −1 this is (Σ4).
  - Corollary WALK: Lemma RB and Lemma G. No level is used beyond H.
  - Lemma CYC-EV: (Σ6), FZ, Lemma G and WALK (c). With L = −1, "COARSE_L(Ξ_k v) = (c, ∅)" is the statement P(Ξ_k v) = ∅.
  - Proposition TEV-FB: Steps 1-4 use FZ, BF, (Σ3), (Σ6) and WALK (c). Step 2's "o ∉ H" is MERGE′ (b) here as well.
  - So TEV-FB holds at L = −1.
- (d) and (e) contradict each other. □

## 4. Corollary LV-PL′ (PROVED, L-SI succ. 7, CONDITIONAL on P-N5-LV §1-§4)
Every scope run S has at most n·n_E + 1 THR fallbacks with M = −1 and r ≥ 0.
- (i) Every interval (f_i, f_{i+1}) of the level −1 block with i + 1 < N is clean.
  - If f_{i+1} has no (β) gate, LV-CN applies (its CN-LAST condition is R38): f_{i+1} + 1 is the last state of its phase.
  - S is in-phase, so f_{i+1} is the last fallback of S, i.e. i + 1 = N.
  - So for i + 1 < N, f_{i+1} has a (β) gate, which is a window gate, and ENT-X_{−1} makes the interval clean.
- (ii) COARSE_{−1}(Ξ_t v) is the same for all t ∈ [f_1, f_{N−1} + 1] and every v.
  - The intervals inside are clean by (i).
  - At each f_i with i < N, FLAT-ALL_{−1} (iii) applies: r_{f_i} ≥ 0, and (h) holds at f_i + 1 because S continues.
- (iii) Each of f_1, …, f_{N−1} has a level −1 tail (FB step (2)). STRETCH_{−1} on [f_1, f_{N−1} + 1] gives N − 1 ≤ n·n_E. □
- Compared with P-N5-LV:
  - LV-PL there was ≤ n·n_E·(d_o + REL_{−1}). REL and d_o are gone.
  - The dirty interval allowed here is the block's last one, ending at a (β)-free fallback that ends the phase.
- With LV-COUNT: per phase, the level −1 THR fallbacks with r ≥ 0 are ≤ (n·n_E + 1) × (scope runs in the phase). Scope runs per phase are
  bounded by R38 SCOPE-COUNT.

## 5. What is left at level −1 (OPEN)
- (a) THR fallbacks with u* = none (r = −1). FBL, NL and FLAT-ALL_{−1} are all unavailable there. DATA: none in scope (P-N5-LV §6).
- Whether in-scope THR ⇒ M ≥ 0 (N5-LV3-box12.md): it would make §4 vacuous. LV-PL′ makes it unnecessary for counting.
- EQ fallbacks are covered by EQ-END (R37 (d)): at most one per scope run after θ = w.

## 6. DATA (DATA, not proof; experiments/si/lv/stale.py, logs experiments/si/lv/logs/stale_*.txt)
- STALE-GATE: every pair (k0, k) with k0 an Even S4c fallback and k > k0 in the same run; every gate (y, z) at k is checked for
  Ξ_k(z) ≠ Ξ_{k0}(z).
- EV-G: every pair with k0 an in-phase THR fallback with (h) and k in the same phase (key (λ_Ξ, τ, λ_U)); every gate target z ∈ F_k is
  checked for a σ_k-play that leaves F_{k0}.

| set | STALE-GATE checks | failures | EV-G checks | failures |
| --- | --- | --- | --- | --- |
| NAMED (experiments/si/lv/named.lst, 102 files) | 25,442 | 0 | 13,357 | 0 |
| LIB (experiments/new/box33/lib.txt, 234) | 47,147 | 0 | 26,049 | 0 |

- The level −1 block is empty in all data (P-N5-LV §6). ENT-X_{−1} and LV-PL′ have vacuous hypotheses there and rest on the proofs.
  STALE-GATE and EV-G are exercised non-vacuously.
