# R2-N5-VILB: second-referee check of packet P-N5-VILB (L-NEW box 44: facts (Aκ), (M1κ), (M2κ), κ-FB-ROUND; Lemma VI-LB on every game). REFEREE-2 (successor 13), written 2026-10-26 03:5xZ-04:0xZ (date -u)
Signature: (Opus 5.5, D15). Lead's order 03:54Z (its stamp), item (1).
Object: docs/new/P-N5-VILB-box44.md, `git show e7febdc2:docs/new/P-N5-VILB-box44.md | sha1sum` -> 872d4400194ed9d0f6ad9f6a2cc82f2f0821cd9f
(= the Lead's pin; = my tree), 87 lines (L-NEW successor 23, frozen at l-new 999e73f4). No fixes file.
Background read: RESULTS R15 (a), R17 (a), R38 (a); SPEC S1, S2, S4c, FIX 3; my R2-N5-FBRED (the same facts and κ-FB-ROUND, per class).
Independence: no docs/referee/ VILB file (`ls docs/referee | grep -i vilb` -> empty at 03:54Z); none opened. No lane script run.
Tools (own code): docs/referee-2/R2-N5-VILB/va_check.py (shared with P-N5-ACCEL), run_all.sh, logs/, climb/.
Labels: PROVED (L-NEW 23). Every game. A LOWER bound on progress; no count, no running time; G-N5-TIME stays OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | notes |
| --- | --- | --- |
| §1 (Aκ), (M1κ), (M2κ) | SIGN | — |
| §1 κ-FB-ROUND (per class) | SIGN | — |
| §2 Lemma VI-LB | SIGN | N-VILB-1 (Γ_c and the −∞ convention: consistent), N-VILB-2 (Odd step) |
| §3 (what VI-LB does not give), §4 ([BGHM] reading, obstruction) | not signed (as briefed) | §3 checked as a READING: accurate |
No gap. No (P). TARGET.md diff: not a claim of TARGET.md §2 (no count, no time).

## 1. §1: SIGN
Identical in content to P-N5-FBRED §1.1 (which I signed in R2-N5-FBRED §1) with c for c_θ: (Aκ) via (V1), λ_t(z) = c ≠ z, no double count; (M1κ)
S1's order at equal cycle node; (M2κ) R15 (a) + (M1κ), λ constant in a phase; κ-FB-ROUND: the two cases (non-gate: (Aκ), (M2κ); gate: S4c's
best key, x* ∈ U_c by (Aκ) at k + 1, (M2κ), (M1κ)). The in-phase fallback is Even's (τ constant; FIX 3) ✓. No class hypothesis ✓.

## 2. Lemma VI-LB: SIGN
- N-VILB-1 (Γ_c, the Lead's item). Γ_c: vertices U_c; Even maximises and EVERY Odd vertex (choice or forced) minimises over successors inside
  U_c; c is the target with value (0, 0); a play pays the sum of κwt_c over its vertices before c (a WALK sum: vertices may repeat), and −∞
  if it never reaches c. Val^{≤j} is the backward induction of the j-step truncation (not reaching c within j steps pays −∞), so the
  recursion (Val^{≤0} = −∞ off c; Val^{≤j}(z) = κwt_c(z) + max / min over succ(z) ∩ U_c of Val^{≤j−1}) and the sentence "the best payoff Even can
  force from z while reaching c within j steps" agree ✓. The empty-set conventions never fire for z ∈ U_c ∖ {c}: by (Aκ) next_t(z) ∈ U_c, so
  succ(z) ∩ U_c ≠ ∅ for every z ∈ U_c ∖ {c} ✓. −∞ is absorbing under + ✓. Note: −∞ in the game means "Odd avoids c"; in G that play has a
  different cycle node — that is exactly why §3 says there is no upper bound (correct).
- Proof ✓. j = 0: κ_t(c) = (0, 0) ((c, ∅, 0)); −∞ elsewhere. Step at t > g_j: z = c trivial. Even z ≠ c: k := g_j < t, κ-FB-ROUND at k for
  every successor x ∈ U_c, the hypothesis at k (k > g_{j−1}; every state if j = 1) for x (including x = c), (M2κ) from k + 1 ≤ t; max over
  x ✓. N-VILB-2 (Odd step, the Lead's item): (Aκ) gives κ_t(z) = κwt_c(z) + κ_t(σ̄_t z) with σ̄_t(z) ∈ succ(z) ∩ U_c, hence ≥ κwt_c(z) +
  min over succ(z) ∩ U_c of κ_t(x) ≥ κwt_c(z) + min Val^{≤j−1}(x) by the hypothesis AT t (t > g_j > g_{j−1}) ✓. This needs no fallback at the
  Odd vertex and holds for choice and forced Odd vertices alike (σ̄_t(z) is one of z's successors) ✓.
- "Every in-phase fallback is ≥ one VI round on every Γ_c" is the lemma's content ✓; the relation to R48's κ-HAT-FREEZE (a) (one-player
  relaxation with Odd choice vertices deleted) is a correct READING.

## 3. DATA (va_check.py; own SPEC N5 loop and honest frame; S3 + random starts)
| set | runs | phases | VILB checks (state × vertex, j = fallbacks so far) | max in-phase fallbacks | violations |
| --- | --- | --- | --- | --- | --- |
| lib41.txt × 3 | 1,236 | 7,168 | 986,781 | 33 | 0 |
| R2-N5-KW/files.lst (503 𝒞^1O) × 2 | 1,006 | 4,121 | 579,061 | 37 | 0 |
| box-43/44 instances (10) × 5 | 50 | 272 | 14,727 | 17 | 0 |
| random 𝒞^kO n 4-12 | 20,000 | 49,411 | 433,775 | 1 | 0 |
| climbs (4 × 3,000 steps, n 4-7; P-N5-ACCEL's epoch objective) | 47,996 | 100,875 | 662,903 | 1 | 0 |
Val^{≤j} is computed by its recursion on Γ_c (Odd min over ALL Odd vertices), with −∞ represented explicitly. Mutation control vi (check κ_t ≥
Val^{≤j+1}, one round too many) fails 774 times on lib41 (S3): the bound is attained at the j-th round in data, so VI-LB is tight there. As the
packet says, nothing in data has many fallbacks in one phase (max 37); the gadget regime of §4 is not exercised.

## 4. Notes
- N-VILB-1: Γ_c's −∞ convention and the j-step recursion agree; empty successor sets never occur inside a class.
- N-VILB-2: the Odd step uses (Aκ) at t only (σ̄_t(z) ∈ succ(z) ∩ U_c), so VI-LB treats every Odd vertex as a minimiser; this is the two-player
  strengthening of R48's κ-HAT-FREEZE (a).

## §C. Comparison with REFEREE's R-N5-VILB (REFEREE successor 12; referee dcb1451c, on trunk a2b77a9a). REFEREE-2 successor 14, 2026-10-26 05:0xZ (date -u)
Signature: (Opus 5.5, D15). Written by successor 14, who did not write §1-§4 above (successor 13 did). Independence held: this report
(f0e82d8a) was in origin/claude/referee-2 from 04:0xZ; R-N5-VILB was opened at 05:0xZ.
- Re-checked by successor 14 itself (04:2xZ pre-read, notebook resume point): VI-LB's induction (Even step at k = g_j > g_{j−1} with
  (M2κ) to t; Odd step by (Aκ) at t; base κ_t(c) = (0, 0)) and κ-FB-ROUND's two cases. Accepted from successor 13 without redoing: that S4c
  (FIX 3) moves every gate source to its best-key gate target (as in R48 / R2-N5-FBRED), and §3's data.

### C.1 Verdicts
| statement | REFEREE | REFEREE-2 | agree |
| --- | --- | --- | --- |
| §1 (Aκ), (M1κ), (M2κ), κ-FB-ROUND | SIGNED | SIGN | yes |
| §2 Lemma VI-LB | SIGNED | SIGN | yes |
| §2 relation to κ-HAT-FREEZE (a) | agreed as READING | correct READING | yes |
| §3, §4 | not signed; §3 agreed | not signed; §3 accurate | yes |
No NOT SIGNED item and no gap on either side.

### C.2 Joint note map
| REFEREE | REFEREE-2 | result |
| --- | --- | --- |
| VILB-N1: the empty-max / empty-min conventions never fire for z ∈ U_c ∖ {c} ((Aκ)) | N-VILB-1 (same, plus: Γ_c's −∞ convention and the j-step recursion agree) | identical |
| (Odd step: (Aκ) at t only, forced and choice Odd alike, "the class hypothesis: none") | N-VILB-2 | identical in substance |
| VILB-N2 (DATA): VI-LB exercised at every j up to 33, tight at 59% of finite lib41 checks; oddmax mutation bites (46,067) | §3: tight at the j-th round (the j + 1 control fails 774 times on lib41 S3); max 37 fallbacks in a phase | agree: two engines, VI-LB exercised and tight, mutations bite |
| READING: VI-LB implies κ-HAT-FREEZE (a) (deleting Odd choice vertices only lowers Even's value) | §2: the same READING | identical; REFEREE's one-line reason is correct |
Nothing open.

### C.3 Data comparison
| | REFEREE (vilb_probe.py) | REFEREE-2 (va_check.py) |
| --- | --- | --- |
| runs / phases | 7,151 / 20,531 | 70,288 / 161,847 (incl. 47,996 climb runs) |
| VI-LB checks | 777,048 | 2,677,247 |
| max in-phase fallbacks in a phase | 33 (lib41) | 37 (my 503 𝒞^1O files) |
| mutation controls | oddmax 46,067 failures | vi (j + 1) 774 failures |
| violations | 0 | 0 |
Both: the regime where VI-LB could force a count (many fallbacks in one phase, §4's gadget) is not reached.

### C.4 Result
Both referees SIGN §1 and Lemma VI-LB on every game, with no gap. For the fixes file: VILB-N1 = N-VILB-1 (optional wording). DATA:
VILB-N2 / §3. A LOWER bound on progress only; no count, no running time; G-N5-TIME stays OPEN. (Opus 5.5, D15)
