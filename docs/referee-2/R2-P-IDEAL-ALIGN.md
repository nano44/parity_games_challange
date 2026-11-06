# R2-P-IDEAL-ALIGN: second-referee report on packet P-IDEAL-ALIGN (L-NEW successor 55, box 178)
REFEREE-2 successor 28 (Opus 5.5, D12/D20). Written 2026-11-06 04:16Z (date -u). Independent: docs/referee/ not read for this packet
before this push.

## Object
- claude/l-new cb8e0dca. docs/new/P-IDEAL-ALIGN.md sha1 d8acdececb507bfad476341411bddd579fcc5b00, 180 lines;
  docs/new/P-IDEAL-ALIGN-line-L1.txt sha1 e46b0417295bfbde7f4cb2d434deed5d0f2e209c, 1 line. Tightness instance
  experiments/new/box172/inst/dd_d5_F14.json sha1 06f0e5015d09c0f1e03f1b9293ab3cd8483e435b. All re-hashed: match.

## Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §2 | Lemma ALIGN (a), (b), (c) | **SIGN** (Opus 5.5, D12) |
| §3 | Lemma KP-MOVE (a), (b) | **SIGN** (Opus 5.5, D12) |
| §3 | Lemma F0 | **SIGN** (Opus 5.5, D12) |
| §4 | Theorem PAIR-DOUBLE F(l) ≤ 2F(l − 1) + 2 | **SIGN** (Opus 5.5, D12); tight (dd_d5_F14, level 3; recomputed) |
| §5 | Corollary MOVES; Corollary T-BOUND T ≤ 2^(d+2) − 2d − 4 on 𝓛^R_d | **SIGN** (Opus 5.5, D12) |
| §6 | Lemma PATH-RISE | **SIGN** (Opus 5.5, D12) |
| line | L-1 | **MATCHES** (optional word changes P-1, P-2) |
No gap. No REFUSE.

## Premise route (landed RESULTS only)
- R104: §0 is the same restatement as P-IDEAL-KEYS §0, which I diffed against RESULTS R104 l. 9864 (R2-P-IDEAL-KEYS.md «Premise
  route»): unchanged here. ✓
- R105 ENC and MONO: verbatim substrings of docs/RESULTS.md (Python test, wrap-normalised). Used only in §6. ✓ Erratum E-2: (E2a), (E2b)
  and KEYFLIP are not used (KP-MOVE re-proves KEYFLIP's degree-2 argument for one mover); moves(x) carries the (E2c) binder. ✓
- R110: only the 𝓛^R_d definition, verbatim. ✓ The unlanded P-IDEAL-KEYS (R111) is not used: ALIGN (a) re-proves PAIR-KF's ladder case,
  and PAIR-DOUBLE replaces LADDER. I read every proof step: no other premise is used. ✓

## Proof check
- ALIGN (a): wt(x, k) = 2(l − 1) + k for both x ∈ {p, q}, so the prefixes are keys of options of the two distinct movers of level
  l − 1, unequal (F1), and they decide: KP_s(x) = 0 ⇔ b_l(s) ⇔ c_l(s) = 0. ✓ (b): degree 2 + (F2): both options available; the step
  takes the key-least under s_t. ✓ (c): s(p) ≠ s(q) ⇒ the prefixes are the two lower movers' current keys, so ord = [w_p has the
  smaller key] = [s(p) = c_l(s)]; s(p) = s(q) = j ⇒ equal prefixes, gates decide: γ_l(j). ✓
- KP-MOVE (b): consecutive moves go to different options; KP equals the landing option at each move; so KP changes in each window
  [t_i + 1, t_(i+1)], and the windows are disjoint. ✓ F0: level-0 keys are constant, so KF = 0, moves ≤ 1, and flips need a move. ✓
- PAIR-DOUBLE: checked line by line.
  - b-steps = flips of the pair below (F(l − 1) of them); c toggles exactly there.
  - Alignment toggles at b-steps for non-movers. A mover lands aligned and was misaligned w.r.t. the new c.
  - Φ′ = Φ(t − 1) or 2 − Φ(t − 1); Φ(t) = Φ′(t) − |Mv_t ∩ {p, q}|.
  - ord as a function of (a_p, a_q, c): D-states give a_p; 11 gives γ(c); 00 gives γ(1 − c).
  - The toggle claim, all four cases: 10 ↔ 01 flips; 11 under c ↔ 00 under 1 − c both give γ(c); 00 under c ↔ 11 under 1 − c both
    give γ(1 − c). So a no-move flip needs a b-step from a D-state (Φ = 1).
  - Telescoping: M ≤ Φ(0) − Φ(T) + Σ_b (2 − 2Φ(t − 1)).
  - F(l) ≤ M + B₁ ≤ Φ(0) + Σ_b h(Φ(t − 1)) with h = (2, 1, −2) on Φ = (0, 1, 2), so F(l) ≤ 2 + 2F(l − 1). ✓
- MOVES: KP = c_l, which changes iff b_l changes, so KF_x = F(l − 1); then KP-MOVE (b). ✓
- T-BOUND: F(l) + 2 ≤ 2^(l+2) by induction from F(0) ≤ 2. T ≤ Σ moves ≤ 2 + Σ_(l=1..d−1) 2(1 + F(l − 1)) = 2d + 2 Σ_(l ≤ d−2) F(l).
  Σ_(l=0..d−2) 2^(l+2) = 2^(d+1) − 4, so the total is 2d + 2^(d+2) − 8 − 4(d − 1) = 2^(d+2) − 2d − 4. ✓ Values 2, 8, 22, 52 at
  d = 1-4, as the «Does NOT claim» paragraph says; T^R(d) = 2, 4, 8, 13 there agrees with my maxima below. ✓
- PATH-RISE: the current chain is a maximal Ξ-path. Two distinct paths first differ at a mover y that both visit (same prefix ⇒ same
  next mover) with k ≠ k′; acyclic ⇒ y is visited once, so the β-sets differ, hence (ENC) the values differ. So cv(z) takes ≤ P(z)
  values, is non-decreasing (MONO), and rises ≤ P(z) − 1 times. ✓

## Own simulator checks (DATA, not a signature) — docs/referee-2/R2-P-IDEAL-ALIGN/r2align.py on my r2sim.py (R104 text, β-sets)
- 600 random 𝓛^R_d genomes (seed 178, d 1-6, random acyclic Ξ-targets, ranks, parities, gates; every start for d ≤ 3, 64 random starts
  otherwise) and the 103 𝓛^R files of claude/l-new cb8e0dca experiments/new/box150-box177 that my loader reads (stored starts):
  28,039 runs. 0 violations of every check:
  - ALIGN (a), (c): 197,272 (state, level ≥ 1) pairs; ALIGN (b): 52,427 moves of level-≥-1 movers.
  - KP-MOVE (b) and MOVES: 244,276 (run, mover) pairs; KF_x = F(l − 1): 188,198 pairs.
  - F0 and T-BOUND (both inequalities): 28,039 runs each. PAIR-DOUBLE: 94,099 (run, level) pairs, 262 of them with equality.
  - PATH-RISE: 244,276 (run, mover) pairs, with P(z) counted exactly by recursion over the acyclic Ξ-graph.
  - Largest T by d: 2, 4, 8, 13, 15, 7 for d = 1-6, and 17 at d = 8 (corpus). d ≤ 3 agrees with T^R(1..3) = 2, 4, 8 (P-TR3 for
    d = 3); d = 4 reaches 13 on the corpus. Output: r2align_seed178.out.
- Tightness: dd_d5_F14 (sha1 06f0e501, in 𝓛^R_5), my run: T 14, F(0..4) = 2, 3, 6, 14, 7; F(3) = 14 = 2 · 6 + 2. ✓
- The packet's own block «P-IDEAL-ALIGN» of experiments/new/check.sh (l. 919-927) run standalone at cb8e0dca: exit 0, «… pins packet
  d8acdece, line L-1 e46b0417, tool 9335dee7, output b653b01b, instance 06f0e501: PASS».

## TARGET.md diff
IDEAL model only; exponential bounds; no game, no algorithm, no complexity class; not M3 / M4 / step 4; G-N5-TIME OPEN. ✓

## Line L-1 (clause by clause)
- Premise parenthesis: R104 definition, R105 ENC and MONO only, R110 𝓛^R_d only. This equals the packet. ✓ «on acyclic Ξ-graphs» ✓.
- Definitions diffed against packet §0: T, Mv_t, moves(x) (E2c binder), KP_s, KF_x, flip, F(l), c_l(s) («the option index k for which
  mover 2(l − 1) + k has the smaller current key under s» = the packet's c_l), γ_l(j), cv_s(z), P(z). Each equal. ✓ The symbol g in
  γ_l is not defined in the line (P-1).
- Claims: ALIGN, KP-MOVE («at any degree elsewhere»), F0, PAIR-DOUBLE, MOVES, T-BOUND, PATH-RISE. Each equals the signed statement. ✓
- Scope tail: «improving RESULTS R108's bound T ≤ 3^d − 1 to T ≤ 2^(d+2) − 2d − 4 on 𝓛^R_d». R108 (RESULTS l. 10812) states «T ≤ 3^d − 1
  on a d-level ladder with two movers of degree 2 per level», a class containing 𝓛^R_d. The two bounds are EQUAL at d = 1, 2 (2 and 8)
  and the new one is strictly smaller for d ≥ 3 (22 < 26, …). So «improving» is true only from d = 3 (P-2). Hedges ✓.
- DATA: each count names its statement; the figures equal aligncheck.out («statelevels» 22,472, «runlevels» 10,648, «runmovers»
  32,620, «dbltight» 44, runs 5,662). ALIGN's 22,472 (state, level) pairs include ALIGN (b), checked on the same pairs for t ≥ 1
  (aligncheck.py l. 48-52). ✓ The tightness instance is named. ✓
- Parentheses 69 / 69, depth never negative; 0 «, 0 »; 0 «|»; one line. Source note names P-IDEAL-ALIGN.md only, the only file that
  carries a proof (packet header). ✓
- Optional word changes:
  - P-1: «γ_l(j) := [g(2l, j) < g(2l + 1, j)]» → «γ_l(j) := [g(2l, j) < g(2l + 1, j)] with g(x, k) the gate index of option (x, k)».
  - P-2: «improving RESULTS R108's bound T ≤ 3^d − 1 to T ≤ 2^(d+2) − 2d − 4 on 𝓛^R_d» → «improving RESULTS R108's bound T ≤ 3^d − 1
    to T ≤ 2^(d+2) − 2d − 4 on 𝓛^R_d (strictly for d ≥ 3; equal at d = 1, 2)».
- Verdict: MATCHES as written. P-1 and P-2 are optional precision only.
