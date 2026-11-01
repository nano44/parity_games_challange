# N5-S4B (box 63): [S4b-OPT] is an instance of R57's standing premise 1E-N3, applied to the game H′, exactly as S4a's optimality is 1E-N3 applied to the dual of H. No further premise is needed; brute-force data agrees and a mutation control shows the check can fail
L-SI successor 38 (Opus 5.5; D18). Lead 2026-11-01 01:30Z, BOX 63: «does SPEC S4b (with FIX 3) realise the pointwise optimum of H′ against σ,
the Odd mirror of R57's 1E-N3 for S4a? … prove [S4b-OPT] from SPEC, or show where it fails, with an instance. If proved, it lifts L42's
restriction.» Written 2026-11-01 from 01:3xZ (date -u; see commit).
- Labels: PROVED (lane) / DATA / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN. Not a packet.
- Sources opened:
  - docs/new/N5-ssi-global.md: S1 (the procedure), S4a, S4b, S4c, FIX 3.
  - docs/RESULTS.md R57 (l. 2893: «under the standing SPEC premise 1E-N3») and R95 (l. 7476: «1E-N3: S1's procedure realises the
    pointwise optimum; for S4a, σ_new is the pointwise optimum of the one-player arena H_t»).
  - docs/referee-2/R2-N5-1E.md §2 and §8, N-1E-1 (REFEREE-2's reading of the premise; quoted below).
  - docs/DECISIONS.md L42.
  - experiments/new/box21/n5x.py step() l. 15-45 (the S4a / S4b code paths).

## 1. What 1E-N3 says (quoted)
- REFEREE-2, docs/referee-2/R2-N5-1E.md §2, N-1E-1: «VJ00's setting (§2) is every finite game graph with a successor at each vertex =
  TARGET §1's games; no class hypothesis. What remains SPEC's requirement, as in every landed N5 result: that S1's PROCEDURE outputs an
  optimal σ̄ (VJ00 §6).» §8: «S1's procedure computing an optimal σ̄ stays SPEC's requirement (VJ00 §6), as in R51».
- So 1E-N3 is a premise about the PROCEDURE, on every finite game graph with injective priorities and a successor at every vertex. For any
  such game G* and any Even strategy σ* of G*, S1's procedure returns an Odd strategy that is a pointwise optimum against σ* in G*.
- R95's premise text applies it to S4a. S4a runs S1's procedure on the dual of H_t, and reads the dual-Odd counterstrategy as an Even
  strategy of G (via Lemma R, the dual reading).

## 2. Lemma S4B-OPT (PROVED, lane, under 1E-N3 only)
- Statement. Let k be a state of an N5 run with I_τ_k ≠ ∅. Let H′_k be S4b's arena: Odd v keeps {τ_k(v)} ∪ I_τ_k(v), Even v keeps σ_k(v),
  priorities as in G. Let τ_new be S4b's output. Then for every positional Odd strategy ρ of H′_k and every vertex x,
  val(σ_k, τ_new)(x) ⊴ val(σ_k, ρ)(x) (SPEC S1 order; Odd minimises).
  - Moreover τ_(k+1) = τ_new, except in an Odd fallback (I_σ_k = ∅, σ_new = σ_k, τ_new = τ_k; then S4c moves τ).
- Proof.
  - H′_k is a finite game graph. It has G's priorities (injective after S1's rank tie-break), and every vertex has a successor: σ_k(v)
    for Even v, and τ_k(v) ∈ succ(v) for Odd v.
  - SPEC S4b: τ_new is «Odd's optimal counterstrategy (S1 procedure on H′, not dual) to σ». H′_k's only Even strategy is σ_k. n5x.step
    l. 30-37 does exactly this: Engine(Game(prio, owner, succ_H′)).evaluate(σ restricted), Odd's choices read from the result.
  - By 1E-N3 applied to the game G* := H′_k and σ* := σ_k, τ_new is a pointwise optimum against σ_k in H′_k:
    val_(H′_k)(σ_k, τ_new) ⊴ val_(H′_k)(σ_k, ρ) for every positional ρ of H′_k.
  - A value depends only on the play (SPEC S1). Every (σ_k, ρ)-play of H′_k is a (σ_k, ρ)-play of G with the same priorities. So the
    H′-values are the G-values.
  - Second sentence: SPEC S4d sets τ := τ_new, except that S4c (fallback) applies when σ_new = σ and τ_new = τ. By FIX 3, an Even fallback
    (I_σ ≠ ∅) leaves τ = τ_new. Only an Odd fallback (I_σ = ∅) replaces τ. □
- Corollary [S4b-KEEP] (PROVED, lane, under 1E-N3). At every τ-stretch transition k (τ_(k+1) = τ_k) with I_τ_k ≠ ∅, τ_k = τ_new is Odd's
  pointwise optimum of H′_k against σ_k. (A τ-stretch transition is never an Odd fallback, because an Odd fallback changes τ. If
  I_τ_k = ∅, H′_k has τ_k as its only Odd strategy.)
- Comparison with S4a. S4a needs 1E-N3 on the DUAL of H_k plus Lemma R, which reads dual-Odd strategies and dual values back on G. S4b
  needs 1E-N3 on H′_k directly («not dual»). So S4b's optimality is, if anything, the simpler instance of the same premise.
- What is NOT proved: 1E-N3 itself, i.e. the correctness of S1's procedure (VJ00 §6). It stays SPEC's requirement, as in every landed
  N5 result. The code's conformance to SPEC is DATA (R15 G-N5T-1).

## 3. DATA (experiments/si/anc58/s4bopt.py)
- At every state with I_τ ≠ ∅, the tool recomputes S4b's τ_new as n5x.step does. It then enumerates EVERY Odd strategy ρ of H′
  (when there are at most CAP of them) and checks val(σ, τ_new) ⊴ val(σ, ρ) at every vertex (OPTV = violations). Control S4AV: the same
  brute force for S4a's σ_new on H against τ (Even maximises).
- Box 62's instances (CAP 4096): n3all_maxph_0 2 states / 4 strategies; lcount2_n23 6 / 46; sym_h8_s1 25 / 302. OPTV 0, S4AV 0, and the
  run's τ_(k+1) = τ_new at every checked state (TAUNEW_EQ_RUN).
- Mutation control (MUT=1: the old τ in place of τ_new): OPTV 215 on lcount2_n23 and 677 on sym_h8_s1. So the check detects a
  non-optimal τ.
- Corpus (CAP 1024; anc58/s4bopt_corpus.txt): §5.

## 4. Consequence for L42 (READING; the Lead's decision)
- L42: «R57's standing SPEC premise (1E-N3) covers S1's procedure and S4a … It does NOT cover S4b». Lemma S4B-OPT shows that S4b IS
  covered by the same premise, by the same argument that covers S4a: 1E-N3 applied to S4b's arena H′ (no dual needed).
- If the Lead and the referees accept this, claims that use [S4b-OPT] or [S4b-KEEP] are as conditional as every landed N5 result
  (1E-N3 only), not more. Examples: L-NEW's O-ARENA (P-N5-STAIR, withdrawn under L42); box 62's [S4b-KEEP]; R168's corrected τ-constraint.
- Suggested next step: a two-referee check of §2. It is short, and the only point to verify is that 1E-N3's scope is «every finite game
  graph», as REFEREE-2's N-1E-1 already states.

## 5. Corpus result (DATA)
- anc58/runs4bopt.sh on anc58/corpus_fixed.lst (1,132 games, all completed): 7,772 states with I_τ ≠ ∅.
  - 6,719 of them enumerated in full (≤ 1,024 arena strategies each), 290,345 strategies compared, OPTV 0. 1,053 states were skipped as
    larger than CAP.
  - The run's τ_(k+1) = τ_new at 7,736 states. The other 36 are exactly the Odd fallbacks (ODDFB 36), as the Lemma's second sentence says.
  - S4a control: 16,430 states enumerated, S4AV 0.

## DONE / FINDINGS / NEEDS
- DONE: this note; anc58/s4bopt.py (+ runs4bopt.sh, s4bopt_corpus.txt); check.sh «box 63».
- FINDINGS:
  - PROVED (lane): S4B-OPT and [S4b-KEEP] under 1E-N3 alone (1E-N3 applied to H′; FIX 3 handles the fallback case).
  - DATA: brute force 0 violations; the mutation control fails as expected.
  - READING: L42's restriction can be lifted to «under 1E-N3», if the Lead and the referees agree.
- NEEDS: none from the owner.
