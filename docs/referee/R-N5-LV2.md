# R-N5-LV2: REFEREE report on packet P-N5-LV2 (box 12: STALE-GATE, EV-G, ENT-X_{−1}, LV-PL′, SAND, FLAT-ALL_{−1}^{none}, LV-NONE, SCOPE-FB)
Referee: REFEREE (successor 9, session_01VsZYJ8FiTSj5Kazk715ZP7), Opus 5.5 (owner ruling D15, Lead reading L37).
- Routing: the Lead's message of 15:34Z (Lead's stamp); order NEB → PFZ (+ ext) → LV → LV2.
- Object: docs/si/P-N5-LV2-box12.md at pinned trunk 283bcb6, sha1 3b23a41fee6b705e20092d8dd49e7ce0b1408b03, 270 lines (checked with
  `git show 283bcb6:docs/si/P-N5-LV2-box12.md | sha1sum`). Author: L-SI successor 7.
- Written 2026-10-25T15:58Z onward by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: I did not read docs/referee-2/R2-N5-LV2.md. Its N-LV-1 / N-LV-2 on P-N5-LV reached me only as quoted in
  the packet's §0. D1: each statement treated as wrong until its proof checked.
- Premises re-read for this review: P-N5-ENT §0-§5 (docs/si/P-N5-ENT-box11.md), P-N5-FBW §3-§5 (R31), RESULTS R29, R30 (a), (b), R35 (a),
  R37 (c)-(e), R38 (f), and my own R-N5-LV.md (the P-N5-LV items used here are signed there).

## Verdicts
| § | statement | label | verdict (Opus 5.5, D15) |
| --- | --- | --- | --- |
| §1 | Lemma STALE-GATE (every game) | PROVED | SIGNED |
| §2 | Corollary EV-G | PROVED | SIGNED (premise FREE-FREEZE, R37 (c): its (P) is discharged by R36 for the one-player G_τ) |
| §3 | Theorem ENT-X_{−1} (with the L = −1 re-reading of P-N5-ENT §1-§3) | PROVED CONDITIONAL on P-N5-LV §3, §4 | SIGNED; conditions signed by me (R-N5-LV) (note LV2-N1) |
| §4 | Corollary LV-PL′ | PROVED CONDITIONAL on P-N5-LV §1-§4 | SIGNED; conditions signed by me |
| §5 | Lemma SAND (+ its three consequences) | PROVED | SIGNED |
| §6 | Lemma FLAT-ALL_{−1}^{none} | PROVED CONDITIONAL on P-N5-LV §1 | SIGNED; condition signed by me |
| §7 | Theorem LV-NONE | PROVED CONDITIONAL on P-N5-LV §1, §3 | SIGNED; conditions signed by me |
| §8 | Corollary SCOPE-FB (≤ 4·n·n_E + 3 fallbacks per scope run) | PROVED CONDITIONAL on (C-ENT), (C-LV), (C-PKT) | SIGNED with exactly those conditions. (C-PKT) = this report; (C-LV) = R-N5-LV (mine); (C-ENT) = P-N5-ENT PL-S″, converged with the R36 lift, landing as R40 |
| §10 | N5-LV3 material, OPEN | not to sign | not signed |
- No (P) beyond what R36 discharges. The conditional labels are exact: I traced each use of a P-N5-LV item (listed per section below).
  Nothing else in review is used.
- No gaps.
- VACUOUS IN DATA (lesson N-ENT-2): the level −1 block and the none part are empty in the packet's data and in mine. So ENT-X_{−1},
  LV-PL′'s block, FLAT-ALL_{−1}^{none} and LV-NONE rest on the proofs. STALE-GATE, EV-G and SAND occur often (§9).

## 1. STALE-GATE: checked
- Case 1: Ξ_k(z) = Ξ_{k0}(z) ⊴ b_{k0}(y) ⊴ b_k(y) contradicts the gate at k.
- Case 2: (y, z) is a gate at k0, so S4c moves y to a ⊴-best target z′. Then
  b_k(y) ⊵ b_{k0+1}(y) = Ξ_{k0+1}(z′) ⊵ Ξ_{k0}(z′) ⊵ Ξ_{k0}(z) = Ξ_k(z).
- b(y) is non-decreasing at EVERY transition of a run: S4b and Odd fallbacks leave σ, hence Ξ = Ξ_σ, unchanged; S4a and Even fallbacks
  move along gates (R15 (d)); R15 (a). So "every game" is correct. Correct.

## 2. EV-G: checked
- FREE-FREEZE (R37 (c)): "k0 an in-phase THR S4c fallback with (h), t > k0 a state of the same phase, z ∈ F_t and z's (σ_t, τ)-play in
  F_{k0} ⇒ Ξ_t(z) = Ξ_{k0}(z)". That is exactly EV-G's setting. With STALE-GATE (k0 is an Even fallback) it gives a contradiction.
  Correct.

## 3. ENT-X_{−1}: checked step by step against P-N5-ENT §0-§3
- (a): PL_{−1} (b) (condition) makes the first change an S4a step with lev(θ_j, θ_{j+1}) = O_j > −1. With H = V_{>c}, A = P(θ_{k0}) and
  B = P(θ_k). θ is monotone with the fixed cycle node c, so the COARSE_{−1} step cannot be undone ((C1), (C3)). So B ≠ A. Correct.
- (b), (Σ1)-(Σ6) at L = −1:
  - (Σ2): OFFGATE at k0 + 1 gives level ≤ M_{k0} = −1; NL (iii) needs only r_s > −1, and r ≥ 0 on the block.
  - (Σ3): NL (ii). (Σ4): M_k = −1. (Σ5): H1. (Σ6) = (a).
  Correct.
- (c), EV at −1:
  - EV-G's hypotheses hold: k0 is an in-phase THR fallback with (h), and z ∈ F_k. So z's play meets Ev (it lies in F_k ⊆ F_{k0} ⊔ Ev).
  - Ξ_k(z) = ρ ⊕ Ξ_k(q).
  - COARSE_{−1}(Ξ_k q) = COARSE_{−1}(Ξ_{k0} q) by NL (i) at −1 and FLAT-ALL_{−1} (iii) across k0 (condition).
  - Lemma G at k0 (q ∈ Ev ⊆ R_{k0}).
  - MERGE′ (a), (b) at ℓ = −1: R37 (e) covers −1 ≤ ℓ < ∞. y's route is low, so P(Ξ_k z) = B, and o ∉ H.
  - So B = (ρ ∩ H) ⊔ (π_q ∩ H) ⊔ A, a disjoint union: ρ ∩ P(Ξ_k q) = ∅; π_q ⊆ R_{k0}; A ⊆ {o} ∪ F_{k0}. Hence A ⊊ B. Correct.
  - LV2-N1 (precision, no gap): "ρ ∩ P(Ξ_k q) = ∅ (the play is simple before its cycle)" and (P2) along ρ need q on the pre-c path of
    z's play, i.e. q not on C_k.
    - z's play has cycle node c: a level −1 gate from y ∈ R keeps b_k(y)'s cycle node c.
    - CYC-EV (part (e), proved in this same setting with the rise (a)) says no Ev ∩ F_k vertex lies on C_k. So q precedes c and ρ is part
      of the pre-c path.
    - The text should cite CYC-EV here, as P-N5-RL's EV bookkeeping does at L ≥ 0.
- (d), EV+ at −1, h := top(B ∖ A) ⊆ ρ ∪ π_q:
  - h ∈ ρ: by MERGE′ (c) at −1, H-vertices of z's play lie on the suffix it shares with x_k's play, and q follows h.
  - h ∈ π_q: h ∈ P(θ_k), h ≠ o, so h lies on x_k's play ⊆ F_k (H1); h ∈ R_{k0}; so h ∈ F_k ∩ R_{k0} = Ev ∩ F_k.
  - Correct.
- (e), TEV-FB at −1. I re-read every step of P-N5-ENT §1-§3 with L = −1:
  - FZ: FLAT-ALL_{−1} (iii) across k0 (condition) and NL (i) with r_s > −1.
  - BF: (P2) and (C4) are defined for −1 ≤ L (P-N5-FB §1); level-free otherwise.
  - RB: the only level step is "gate of level > −1 ≥ M_k", i.e. (Σ4).
  - WALK (b): COARSE_{−1} keeps all of P ⊆ V_{>c} = H.
  - CYC-EV: "(c, ∅)" means P = ∅ along C_k below c.
  - TEV-FB Step 2's o ∉ H: o ∉ A forces rank o ≤ rank c = max(L, rank c).
  - Correct.
- Conditions used: PL_{−1} (b) in (a); FLAT-ALL_{−1} (iii) in (c) and FZ. Exactly as the packet lists.

## 4. LV-PL′: checked
- (i): a (β)-free f_{i+1} satisfies LV-CN's hypotheses, so f_{i+1} + 1 ends the phase, hence S (S is in-phase), and i + 1 = N. Otherwise
  f_{i+1} has a (β) gate = window gate, and ENT-X_{−1} applies to the consecutive block fallbacks f_i < f_{i+1}. Correct.
- (ii): clean intervals and FLAT-ALL_{−1} (iii) at f_i, i < N ((h) at f_i + 1, since S continues).
  - FLAT-ALL_{−1} (iii)'s proof uses (i) (routes); (i) needs H1 at k + 1 (N-LV-1 below), which (h) at f_i + 1 supplies.
- (iii): STRETCH_{−1} with e = f_{N−1} + 1, counting k < e. This is the form as stated, so N-LV-2 / my LV-N2 is not needed here.
  N − 1 ≤ n·n_E. Correct.
- Conditions used: LV-SHAPE (via LV-CN and "(β) = window"), LV-CN (§2), FLAT-ALL_{−1} (§3), STRETCH_{−1} (§3); PL_{−1} (b) (§4) through
  ENT-X_{−1}. That is P-N5-LV §1-§4, as labelled.

## 5. SAND: checked
- θ_t ⊴ θ_{t′} ⊴ w_{t′} = w_t (R15 (a), XW, w constant on S). (C5) gives lev(θ_t, θ_{t′}) ≤ r_t = −1, then (C2). Correct.
- Consequences:
  - r = −1 on [g_1, g_N]. r takes the values ⊥ (EQ), −1 and ≥ 0, and is non-increasing along S (Fact R). r_{g_1} = −1 gives r ≤ −1
    after g_1, and r_{g_N} = −1 gives r ≥ −1 before g_N.
  - So a fallback strictly inside is THR with r = −1 (not EQ), i.e. it is a g_i.
  - M = −1 at each g_i (FBW-S).
  - Correct.

## 6. FLAT-ALL_{−1}^{none}: checked
- The switched edges are (α), (γ), (β) by LV-SHAPE (condition), which covers r = −1.
- (i), with H1 at k + 1:
  - A switched cycle node (α or γ) keeps λ = itself (phase), so its honest play at k + 1 is a cycle through it. That cycle avoids o
    (H1 at k + 1), and it is therefore also its (σ, τ)-play, in F_{k+1}. For (γ) the target lies in R̄_k, which is the new point:
    handled correctly.
  - F_k plays follow σ_k inside F_k until a switched cycle node ((β) tails are in R_k), and then stay on that node's cycle.
  - Plays reaching o meet no switched vertex.
  - Correct.
- (ii)-(iv): R31's proof at M = −1 (as in my R-N5-LV §3: OFF at M_k = −1, TRANSFER at L = −1); (ii) also from SAND. None of it uses
  u* ≠ none. Correct.

## 7. LV-NONE: checked
- (1), at g_i (i < N): FLAT-ALL_{−1}^{none} (iii), (iv), with (h) at g_i + 1.
- (1), at an S4a step j strictly between g_i and g_{i+1}:
  - j is S4a: no other fallback of S lies inside (§5), and no S4b (phase).
  - TRANSFER keeps M ≤ −1, so E_j ≤ −1.
  - U-loc at L = −1 (R28 (a), any L): a COARSE_{−1} change needs a relevant change of level ≥ 0 on a path, and only σ̄(o) can make one
    (Even changes are ≤ −1; the other Odd vertices are forced). So O_j ≥ 0 > E_j: an ε-transition.
  - Lemma OR (c) (R30 (a): at an ε-transition, lev(θ_j, θ_{j+1}) = O_j; no further hypothesis) gives level ≥ 0.
  - SAND at r_j = −1 gives level ≤ −1. Contradiction. Correct.
- (2): STRETCH_{−1} on [g_1, g_{N−1} + 1], counting k < e: g_1 … g_{N−1}, each with a level −1 tail. Its proof has no r hypothesis
  (checked in R-N5-LV §3). N ≤ n·n_E + 1. Correct.
- Conditions used: LV-SHAPE (through §6) and STRETCH_{−1}, i.e. P-N5-LV §1, §3, as labelled. NL and FBL are indeed not used.

## 8. SCOPE-FB: checked
- The four classes are disjoint and exhaustive. In-scope fallbacks are Even, EQ (r = ⊥) or THR. For THR with r ≥ 0, FBW-S gives M ≤ r,
  and M ≥ −1.
- The bounds:
  - level ≥ 0: PL-S″ ≤ 2·n·n_E (P-N5-ENT §5: R31 PL (a) per block with D_M ≤ 1 (D1), n levels);
  - −1 with r ≥ 0: §4;
  - r = −1: §7;
  - EQ: ≤ 1, by R37 (d) EQ-END with CN-LAST (R38). It also follows directly: at an EQ state every gate is a length-only switch at a
    cycle node (FBW-S), so CN-LAST makes any EQ fallback end the phase.
- Sum 4·n·n_E + 3. Correct.
- The fallback without (C-ENT), n_E·(n·d_o + REL(S)) + 2·n·n_E + 3 via R35 PL-S′: correct.
- The "Reading" (it closes (CL-S) up to the conditions) is not signed, and the packet says the same.

## Notes for the lane's fixes file (none is a gap)
- LV2-N1: §3 (c): cite CYC-EV for "q lies on the pre-c path of z's play" before "ρ ∩ P(Ξ_k q) = ∅" and (P2) along ρ.
- LV2-N2 (statuses): P-N5-LV is signed by both referees (R-N5-LV 8054da2f; REFEREE-2 b1038bea per the git log). Its CN-LAST condition
  is discharged by R38.
- On N-LV-1 (REFEREE-2, relayed in the packet's §0): I accept it. My R-N5-LV §3 said "(i) FBL + H2 + the phase: level-free". The correct
  citation is R31's FBW-1 repair: an honest cycle through o is excluded by H1 at k + 1, not by H2, since the honest and W-plays differ at
  o. My lane missed it; it goes into my LV §C. With (h) at k + 1, both H1 and H2 hold, so no verdict changes.

## 9. DATA (DATA, not proof; own code docs/referee/scratch/lv2_probe.py on rl_engine, no lane imports; logs docs/referee/R-N5-LV2/)
- Files: docs/referee/R-N5-LV/files.txt (447 paths): 402 games run, 45 skipped (n > 64). STALE-GATE on all 402 (288 C^1O, 114 not).
  The rest on the 288 C^1O games.

| check | count | failures |
| --- | --- | --- |
| STALE-GATE (Even fallback k0, later state k, gate at k), every game | 70,267 | 0 |
| EV-G (in-phase THR fallback k0 with (h), later k in the phase, gate into F_k) | 34,389 | 0 |
| SAND (states after the first r = −1 state of a scope run) | 181 | 0 |
| scope runs; fallbacks by class: level ≥ 0 / −1 with r ≥ 0 / r = −1 / EQ | 236; 788 / **0** / **0** / 11 | — |
| SCOPE-FB total ≤ 4·n·n_E + 3 and the class bounds (max per run 37) | 236 runs | 0 |

- VACUOUS IN DATA: the level −1 block and the none part are empty (0 / 0), as in the packet's data and in my P-N5-LV climb (R-N5-LV
  §6.1). STALE-GATE, EV-G and SAND are exercised.
