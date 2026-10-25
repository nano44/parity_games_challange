# R-N5-P1: REFEREE report on packet P-N5-P1 (premise (P) for one-player games: Lemma B, Lemma M, Lemma P1)
Referee: REFEREE (successor 8, session_01YRPeH49wEXXq7vW5qK35Gz), Opus 5.5 (owner ruling D15, Lead reading L37).
- Routing: P-N5-P1 was queued by the Lead at 12:01Z (Lead's stamp), to follow R-N5-RL and the SCOPE §C.
- Object: docs/si/P-N5-P1-box10.md at pinned trunk 48a8a4c, sha1 b98ca7941264affe4bfe79cb72b744d2ab158e07, 176 lines. Checked with
  `git show 48a8a4c:docs/si/P-N5-P1-box10.md | sha1sum`; 48a8a4c is on trunk.
- Author: L-SI successor 5.
- Written 2026-10-25 12:30Z onward by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: I did not read docs/referee-2/R2-N5-P1.md.
- D1: I treated the lemma as wrong until each step checked. As the Lead asked, I scrutinised Lemma B and P1 Step 5 hardest.

## Verdicts
| § | statement | packet label | verdict (Opus 5.5, D15) |
| --- | --- | --- | --- |
| §1 | real order (i)-(iii), extended order (i), (ii′), (iii); Lemma B (a)-(c) | PROVED | SIGNED |
| §2 | Lemma M, and the real-prefix remark | PROVED | SIGNED |
| §3 | Lemma P1 (Steps 1-6) and Corollary P1′ | PROVED | SIGNED |
| §4 | hypothesis match with R18's (P) and with P-N5-RL §0's (P) | PROVED, by inspection | SIGNED |
| §5 | what P1 discharges | READING | not signed as such; checked below, with one correction for P-N5-RL (TEV-RED, RL-1) |
| §6 | data | DATA | consistent with my own data (§6 below) |

No gaps.

## 1. §1 and Lemma B: checked
- The real order is SPEC S1 with Q1.
  - (i) is rew(c).
  - (ii): the top h of P Δ P′ decides. P′ is better iff (Ω(h) even and h ∈ P′) or (Ω(h) odd and h ∈ P). This is Q1's rule.
  - (iii): c odd means longer is better; c even means shorter is better. This is S1's length rule.
  - It is the engine key (rew(c), weight(P), d if c is odd else −d) of P-N5-FBW §0.
  - DATA: own key against the packet's clauses, on 994,142 random pairs of occurring values (ORD): 0 differences.
- The §1 fact behind every use of (i): for rank t > rank c, rew(t) < rew(c) iff Ω(t) is odd.
  - pp(t) ≥ 2·rank t > pp(c), and rew(c) ∈ {±pp(c)}.
  - rew is injective, since pp is injective and the sign of rew is the parity of pp. Correct.
- Lemma B (a).
  - For fixed c, the map to (ε_1 μ(h_1), …, ε_k μ(h_k), ε_c ℓ), with the h_i above c in decreasing rank, is injective. V_{>c} is
    finite, so the vectors have fixed length.
  - Lexicographic comparison at the first differing coordinate reproduces (ii′):
    - an even h with ε = +1: μ′(h) > μ(h);
    - an odd h with ε = −1: μ′(h) < μ(h).
  - It reproduces (iii): c even, ε_c = −1, ℓ′ < ℓ; c odd, ε_c = +1, ℓ′ > ℓ.
  - Different c are ordered by the injective rew. A total order.
  - DATA: 800,000 random extended pairs (multiplicities 0-2, cycle nodes mixed). (ii′)-(iii) never held both ways, nor neither way
    for distinct values. They agreed with the vector map whenever rew agreed. 0 failures.
- Lemma B (b): for sets, the vertices whose multiplicities differ are P Δ P′, with multiplicities 1 and 0. (ii′) is then (ii), and
  (i) and (iii) are shared. Correct. DATA: 374,589 set-valued pairs, 0 differences.
- Lemma B (c): real path parts are sets, because the play is simple before its first visit to c. Correct.
- The bridge's use is sound.
  - Every hypothesis and every conclusion of P1 compares real values.
  - Multisets occur only inside chains whose two ends are real.
  - A chain that is valid in ⊴ₓ, by (a), gives the same real comparison at its ends, by (c).
- The packet's reason for multisets is correct: the set prefix x ∪ P is not monotone when x is the top of P Δ P′.

## 2. Lemma M: checked
- Adding [x]·𝟙(rank x > rank c) to both multisets keeps every multiplicity difference. Adding 1 to both lengths keeps (iii), whose
  direction depends only on the shared c. So strict and equal comparisons are preserved, and with them ⊴ₓ. Correct.
- DATA: 559,604 random pairs, 0 failures.
- Real prefix: if x is not on y's play before its first visit to c, and x ≠ c, then the play x, (play of y) has the same cycle, and the
  same first visit to c one step later. P gains x iff rank x > rank c. Correct.

## 3. Lemma P1: checked step by step
- Step 1: the hypothesis "no Even edge (x, y) with V(y) ▷ V(σ x)" gives V(y) ⊴ V(σ x) by totality. Odd x has y = s(x). Correct.
- Step 2.
  - x ≠ c(x): x is off the cycle, or on it.
    - If x is on the cycle, s(x)'s play runs once around the cycle and returns to x last. It meets c(x) ≠ x first.
    - So x does not occur before the first visit to c(x), and the real prefix applies.
  - x = c(x): s(x) is on x's cycle, and the cycle's top is x, so V(s(x)) = (x, ∅, L − 1). This includes the self-loop case, L = 1.
  - Correct.
- Step 3: c(s(x)) = c(x) in both cases. V(y) ⊴ V(s(x)) and (i) give rew(c(y)) ≤ rew(c(x)). Correct.
  - DATA: 101,851 edges at improvement-free strategies, 0 failures.
- Step 4: x_i ≠ c0 = c(x_i) gives Step 2's first case. Then Step 1, B (c), and Lemma M on values all with cycle node c0 give
  V(x_i) ⊵ₓ x_i ⊕ V(x_{i+1}). The downward induction applies Lemma M to the tail inequality, whose two sides both have c0. Correct.
- Step 5, scrutinised. C is a simple cycle of H (edges of H, not of σ) with c(·) = c0 on C, and top t.
  - Case c0 ∈ C, y_0 = c0, p ≥ 2.
    - Step 4 on y_1 → … → y_{p−1} → y_0 is legal: y_1, …, y_{p−1} ≠ c0, because C is simple. It gives V(y_1) ⊵ₓ (c0, μ, p − 1).
    - V(c0) = (c0, ∅, 0) holds because c(c0) = c0 means c0 is the top of its own σ-cycle.
    - Step 1 on the H-edge c0 → y_1 gives V(y_1) ⊴ V(s(c0)) = (c0, ∅, L − 1).
    - So (c0, μ, p − 1) ⊴ₓ (c0, ∅, L − 1).
    - If t ≠ c0, then t is above c0 and is the top of μ, with μ(t) = 1 > 0. The two values differ, so the comparison is strict, and
      (ii′) at t forces t odd. The §1 fact then gives rew(t) < rew(c0).
    - Correct, including the role of Step 1 at the cycle node itself. This is the point where "no improving edge" is used at c0, and
      lengths cannot be ignored.
  - Case c0 ∉ C.
    - Step 4 once around C (m = p, x_m = y_0; all y_i ≠ c0) gives V(y_0) ⊵ₓ (c0, μ_0 + μ_C, ℓ_0 + p). μ_0 + μ_C may have
      multiplicity 2: C may share vertices with y_0's real prefix. This is exactly where multisets are needed.
    - If μ_C ≠ ∅: the multiplicities differ exactly on supp μ_C, whose top is t (t is C's top and is above c0). Here
      μ_0(t) < μ_0(t) + 1 with the left side ⊵ₓ, and strict since the two differ. So t is odd, and rew(t) < rew(c0).
    - If μ_C = ∅: C lies below c0, so rank t < rank c0. Only the length differs (ℓ_0 against ℓ_0 + p, p ≥ 1). The left ⊵ₓ the
      right excludes c0 odd, so c0 is even, and rew(t) ≤ pp(t) < pp(c0) = rew(c0).
    - Strict in both sub-cases.
  - Equality only for t = c0 ∈ C. Correct.
  - DATA: 39,211 simple cycles with constant c(·) (25,640 through c0), at improvement-free strategies: 0 failures.
- Step 6.
  - rew(c(v_i)) is non-increasing along the σ′-play (Step 3), and periodic on C′, hence constant there. c(·) = c0 on C′ by
    injectivity.
  - Step 5 gives rew(c′) ≤ rew(c0) ≤ rew(c(v_0)).
  - Strict case: clause (i).
  - Equal case:
    - c′ = c0 = c(v_0), c0 is the top of C′, and c(v_i) = c0 for all i.
    - The first visit v_b to c0 lies on the first pass, so v_0, …, v_b are distinct, and v_i ≠ c0 for i < b.
    - Step 4 then gives V(v_0) ⊵ₓ (c0, {v_i : i < b, above c0}, b), using V(c0) = (c0, ∅, 0). That is the real value V_{σ′}(v_0),
      whose cycle node is C′'s top, c′ = c0.
    - B (c) gives V(v_0) ⊵ V_{σ′}(v_0). b = 0 gives equality.
  - Correct.
- Corollary P1′: P1 makes V_σ the pointwise maximum over positional strategies, so it equals R17 F1's optimum W*. Two improvement-free
  strategies have equal valuations. Correct.

## 4. §4 hypothesis match: checked
- R18's G[X].
  - X is closed under successors: a successor with a path to o would give x one.
  - o ∉ X, and in 𝒞^1O every other Odd vertex has out-degree 1. So G[X] is a one-player game in §1's sense.
  - R18's (P) is stated for exactly this form ("an Even strategy with no improving edge is optimal").
- P-N5-RL's G_τ and G_τ[F_k] are this form (my R-N5-RL §2: closure checked).
- "Improving" is SPEC S2's, against Ξσ. In a one-player game, Ξσ = V_σ: Odd has one strategy (R18 Lemma S (a)).
  - DATA: own VJ procedure (rl_engine.evaluate, written from SPEC S1) against own play values, at 76,596 strategies: equal in every
    case (ENG).
- "Optimal" is the pointwise maximum over positional strategies (R17 F1). It is the full order, lengths at cycle nodes included. It
  is not CAV's coarser notion. Correct.
- Statement diff against R18's text, as quoted in RESULTS R18 Honest limits (ii) ("CONDITIONAL on (P) for one-player games (G-1OA-4,
  open by design): VJ00 Lemma 5.8 "1 ⇒ 2", used only in Lemma 1 on G[X]"): P1 is that statement for one-player games of this form.
  §0 quotes R18 verbatim. Checked against docs/RESULTS.md R18.

## 5. §5 READING: checked, with one correction
- R18: P1 is (P) on G[X]. With P1 signed by two referees, R18 (c) no longer needs G-1OA-4. That is for the Lead and CHECKER to record.
- P-N5-RL: BL (b) (Step 2b, on G_τ) and BL (c) (on G_τ[F_k]) are exactly P1's instances. So BL (b), (c), (e), FREE-FREEZE, EV and EV+
  would lose the (P) condition.
- Correction: the reading says TEV-RED "becomes PROVED without condition". My R-N5-RL does not sign TEV-RED as stated (RL-1, a proof
  gap independent of (P)). Only TEV-RED′ (no Ev vertex on the cycle of x_t's play) would become unconditional. EQ-END keeps CN-LAST.
- What it does not cover, and I agree:
  - the two-player Lemma 5.8 "1 ⇒ 2" (R15's G-N5T-3, the correctness of N5's output at S5);
  - VJ00's I1 / I2.
- P1 uses none of VJ00's OverProg, Prop. 5.10 or Prop. 5.6. Checked: the proof uses only §1's definitions and Steps 1-6.

## 6. DATA (DATA, not proof; own code docs/referee/scratch/p1_probe.py on rl_engine.py; logs scratch/rl_logs/p1_6102.txt, p1_6103.txt)
- Random one-player games (Odd out-degree 1 asserted).
  - All positional Even strategies enumerated; games with more than 5,000 / 20,000 strategies skipped.
  - Values are own play values. The order is SPEC's key, checked against the packet's clauses.

| seed | games | n | strategies | improvement-free | P1 violations | improving and non-optimal (control) | improving but optimal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6102 | 6,000 | 3-9 | 93,035 | 6,612 | 0 | 84,911 | 1,512 |
| 6103 | 2,000 | 8-13 | 185,085 | 2,471 | 0 | 181,895 | 719 |

- Other checks, 0 failures in each:
  - ORD 994,142 pairs;
  - Lemma B 800,000 pairs (374,589 set-valued);
  - Lemma M 559,604 pairs;
  - ENG 76,596;
  - Step 3 101,851 edges;
  - Step 5 39,211 cycles.
- The control shows that the check bites: 266,806 strategies with an improving edge are non-optimal and correctly not claimed.
- Strategies that are optimal but have an improving edge (2,231) are allowed; P1 does not exclude them. The packet's count of
  these (761 / 491 on its seeds) is consistent in kind. I did not re-classify them as own-cycle-node length-only cases (skipped).
- Instance-level evidence on the games where (P) is used: R-N5-RL §8. There, at 376 NAMED + 526 LIB in-scope THR fallbacks, W_k equals
  Opt(G_τ[F_k]) computed by my own VJ procedure on the dual, not by (P). That is BL (c).
- Thin spots: random games only, n ≤ 13 for the exhaustive check. The proof does not depend on size.

## TARGET.md diff
Not a claim of TARGET.md §2. Lemma P1 is a statement about one-player games, a class already solvable in polynomial time. The packet
says so (header: "not a running-time bound, not a TARGET.md claim, not a step-4 pass. G-N5-TIME stays OPEN"). It discharges a premise of
partial lemmas about N5 on a subclass (R18) and of P-N5-RL. G-N5-TIME stays open.

Signed: REFEREE (successor 8) (Opus 5.5, D15).

## §C. Comparison with REFEREE-2 (written 2026-10-25 12:46Z by date -u; REFEREE successor 8 (Opus 5.5, D15))
- Compared against: the FINAL docs/referee-2/R2-N5-P1.md at referee-2 e036e4c5, named by the Lead at 12:43Z (Lead's stamp). I read it
  after this report (58a5b734) was pushed.
- Verdicts: identical. Both referees SIGN Lemma B (a)-(c), Lemma M with the real-prefix remark, Lemma P1 (Steps 1-6) with Corollary
  P1′, and the §4 hypothesis match. Neither signs §5 as such. No gap in either report.
- N-P1-1 (REFEREE-2, wording): name the trivial cases m = 0 (Step 4) and b = 0 (Step 6, v_0 = c0).
  - I noted b = 0 ("b = 0 gives equality", §3) but not m = 0. Accepted, wording only.
- Both readings of §5 agree. With P1 signed by both, G-1OA-4 (R18) and P-N5-RL's (P) conditions are discharged. TEV-RED's own gap
  (RL-1 = G-RL-1) and EQ-END's CN-LAST condition are untouched, so it is TEV-RED′, not TEV-RED, that becomes unconditional.
- DATA: different code and different seeds, so not re-runs of each other. R2: 28,973 games / 1,030,157 strategies, with mutation
  tests. Mine: 8,000 games / 278,120 strategies, with a control. Both 0 violations. R2's mutation tests (odd-h rule flipped; a
  CAV-style coarse "improving") show its checker bites, as my control does for mine.
- Joint state: Lemma P1 is PROVED (L-SI succ. 5) and signed by both referees (Opus 5.5, D15), pending CHECKER.
  - Fixes-file line (L-SI, P-N5-P1): N-P1-1, add one line each for m = 0 and b = 0.
