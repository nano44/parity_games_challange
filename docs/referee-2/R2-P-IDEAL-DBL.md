# R2-P-IDEAL-DBL: second-referee report on packet P-IDEAL-DBL (L-SI 41/42, box 79)
REFEREE-2 successor 30 (Opus 5.5, D1), 2026-11-07 from 08:4xZ (date -u). Independent: docs/referee/ not read on this item.

## Object (sha1 of the bytes at claude/l-si f5263d5a, equal to the Lead's relay 08:45Z)
- docs/si/P-IDEAL-DBL.md 3573e93b… (21,583 B); line L-1 docs/si/P-IDEAL-DBL-line-L1.txt 93177184… (3,425 B, 1 line, 69 «(» = 69 «)»,
  depth never negative, 0 «|»); experiments/si/box79/check79.sh 079a032d….
- check79.sh re-run on `git archive f5263d5a` (27 s): «box 79 P-IDEAL-DBL (frozen) checks: PASS» (pins --strict, dblcheck.out,
  dblcheck_neg2.out, extra79.out, wiring79.out and dead79.out reproduced byte for byte).

## Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §1 | Fact MP-LIN | **SIGN** (Opus 5.5, D1) |
| §2 | Lemma WINDOW-ONCE | **SIGN** (Opus 5.5, D1) |
| §2 | Lemma DBL-EQ (a), (b), (c) | **SIGN** (Opus 5.5, D1) |
| §2 | Lemma PASS-FREEZE | **SIGN** (Opus 5.5, D1) |
| §3 | Lemma HIT; Corollary FUEL-EXACT | **SIGN** (Opus 5.5, D1) |
| §4 | Lemma ALT-MIN (a)-(d) | **SIGN** (Opus 5.5, D1); the §0 mapping of R116 AND-GATE onto (a)-(c) is faithful |
| §4 | Lemma TOWER-NEED | **SIGN** (Opus 5.5, D1) |
| §6 | DEAD-MAXPLUS, DEAD-DBLGAP, DEAD-DECAY, DEAD-REENTRY | **SIGN** (Opus 5.5, D1): every instance replayed with my own simulator (N-3 on REENTRY's l) |
| §0 | premise quotes | **W-1 required** (PATH-RISE is not quoted from the landed text; packet-level, a fixes entry) |
| line | L-1 | **MATCHES after W-2 (a)-(d), W-3** (DEAD instances not reproducible from the line; DATA not clause by clause) |
Not signed (as the packet says): §5 FUEL-NEED and FUEL (i) (CONDITIONAL on L-LOWER's unlanded FEEDBACK (b)); §7 DATA / READING.
Nothing is REFUSED. No statement bounds T; G-N5-TIME stays OPEN.

## Premises (diffed against trunk docs/RESULTS.md at origin/claude/vibrant-johnson-nxvvxo 97d17f63; 97d17f63 and 2ccd037b9 on trunk)
- R104: definition only ✓ (l. 9864: options, Ξ-values as β-sets compared by the largest-rank β of the symmetric difference, step to the
  least key among the current option and the strictly better ones).
- R105 (l. 10155), «at any degree»: ENC (the packet's «…»-quote is a verbatim substring), LOCAL, MONO ✓ verbatim.
- R110 (l. 11323): 𝓛^R_d definition ✓.
- R113 (l. 12152): ALIGN ✓ verbatim; F0 ✓ verbatim; notation c_l(s) («the option index k for which mover 2(l − 1) + k has the smaller
  current key under s»), γ_l(j) := [g(2l, j) < g(2l + 1, j)], F(l) ✓.
- **W-1 (required, packet-level).** §0 quotes R113 as «(PATH-RISE) «Then the number of steps at which cv(z) rises is at most P(z) − 1.»
  [IDEAL-ACYC, any degree, any width]». Those words are not in R113. The landed clause is «(PATH-RISE) at any degree, the current value
  cv(z) of every mover z rises at most P(z) − 1 times in a run» (R113 is stated «on acyclic Ξ-graphs»). Same content; a premise must be
  quoted from the landed text: a fixes entry replaces the quote.
- R116 (l. 13072, CHECKER PASS C129): the AND-GATE quote ✓ verbatim («(AND-GATE) at any degree elsewhere, a mover x of degree 2 moves at
  step t iff s_(t−1)(x) ≠ π_(s_(t−1))(x) = KP_(s_t)(x), so moves(x) ≤ 1 + min(KF_x, PF_x), and when π(x) changes at step t to b the
  value v(x, b) rises strictly at t»), and the notation quotes of π_s, PF_x, KF_x ✓. R116's scope is «on acyclic Ξ-graphs», as ALT-MIN's
  hypotheses (IDEAL-ACYC, x of degree 2, any degree elsewhere) ✓.
- **The mapping (a)-(c)** (the Lead's question): (a) = the «moves at step t iff …» clause, (b) = «moves(x) ≤ 1 + min(KF_x, PF_x)»,
  (c) = «when π(x) changes at step t to b the value v(x, b) rises strictly at t». The three parts partition the landed clause; nothing is
  added or strengthened. ALT-MIN uses only (c) (in (a)) and (b) (in (c)); (a) is never used ✓.

## Proofs (own re-derivation)
- MP-LIN: x_j ≤ (A^⊗j ⊗ x_0) ⊕ max_(i<j) (A^⊗i ⊗ b) by induction (⊗, ⊕ monotone) ✓; cycle removal leaves a simple path of r ≤ k − 1
  edges, each removed cycle of length L weighs ≤ λL ≤ max(λ, 0)L, the rest ≤ r·max(a, 0) ✓; so A^⊗i(τ, σ) ≤ max(λ, 0)·i + (k − 1)·max(a, 0)
  and max_τ x_j(τ) ≤ max(λ, 0)·j + (k − 1)·max(a, 0) + max(max x_0, max b) ✓ (λ = −∞: paths of length ≥ k do not exist ✓).
- WINDOW-ONCE: c_l is a function of the key order of the pair l − 1, constant on an l-window ✓; ALIGN sends every mover of the pair to
  c_l(s_t) ✓; a degree-2 mover cannot move twice to the same option without leaving it ✓.
- DBL-EQ: (i) Φ(t) = Φ(t − 1) − m_t off B, 2 − Φ(t − 1) − m_t on B ✓ (movers come from off c_t; non-movers keep their option); (ii) a flip
  with m_t = 0 needs a split pair whose c changes ✓; (iii) F(l) ≤ M + B1 ≤ Φ(0) − Φ(T) + Σ_B h(Φ(t − 1)) with h = (2, 1, −2) ✓, equality
  iff the five conditions ✓ (both directions checked); (iv) windows start with Φ = 2 (Φ(0) = 2; at t ∈ B, Φ(t − 1) = 0 and c flips) and end
  with Φ = 0, so each member moves ≥ 1 and (WINDOW-ONCE) ≤ 1 time ✓; under (a), 1 ∉ B (Φ(0) = 2 ≠ 0), so there are exactly F(l − 1) + 1
  windows ✓; (v) γ_l(i) ≠ [A = p] ≠ γ_l(c) with c = 1 − i forces γ_l(0) = γ_l(1) and A = p iff ¬γ ✓.
- PASS-FREEZE: split, never moving ⇒ order = [s(2l + 2) = c_(l+1)(s)] with s(2l + 2) constant, and c_(l+1) changes exactly at the flips
  of the pair l ✓; sufficient condition by R104's step rule (only strictly better options are available) ✓.
- HIT: (⇐) the first moving mover z of the old chain: prefix unchanged, cv(y) = Σε(prefix) + cv(z) at both states (ENC), z moves to a
  strictly better option (R104; «strictly better» Ξ-value = larger ENC integer), v(z, ·) non-decreasing (ENC + MONO) ✓; (⇒) LOCAL ✓.
- FUEL-EXACT: MONO (a change is a rise) + HIT + union ✓.
- ALT-MIN: (a) AND-GATE (c), one rise per change ✓; (b) changes of a binary π alternate ✓; (c) AND-GATE (b) ✓; (d) ENC ✓.
- TOWER-NEED: DBL-EQ (b), HIT, PATH-RISE, ALT-MIN (c), (d) ✓ (f ≥ 2 ⇒ min_k R(y_k) ≥ (f − 1)/2 > 0, R(X) := 0).

## Machine checks (own code, R2-P-IDEAL-DBL/r2dbl.py on my R104 simulator R2-P-IDEAL-MOVES/r2moves.py; no lane code)
r2dbl.py checks, per run: ALIGN (sanity), WINDOW-ONCE, DBL-EQ (a) both directions, (b), (c), PASS-FREEZE, HIT (every mover and step,
and R ≥ moves), ALT-MIN (a)-(d), TOWER-NEED.
- CORPUS (r2dbl_corpus.out; the P-IDEAL-MOVES corpus loaded from experiments/new box150-box187 as in my predecessor's movescheck replay):
  208 files, 63,223 runs, 140,395 steps, 4,534 doubling (run, level): **0 violations of every check** — the run, step and doubling counts
  equal dblcheck.out's.
- LOWER (r2dbl_lower.out, the 9 genomes in box76/inst/lower, stored starts): 12 doubling (run, level), 0 violations ✓ (= dblcheck.out).
- EXTRA (r2dbl_extra.out), the four box79 instances, stored starts, 0 violations everywhere ✓. **DBL-EQ on H6_d24_F126** (the Lead's
  ask): F(0..5) = 2, 6, 14, 30, 62, 126, doubling levels 1, 2, 3, 4, 5; (a) both directions, (b) every window and member, moves = F(l − 1)
  + 1, (c) γ and the first mover of every window, TOWER-NEED: all 0 ✓. Also H5 (levels 1-4), DBL4 (1-4), RECF4 (1-3).
- DEAD (r2dbl_dead.out, r2dead4.out; all four files 𝓛^R and Ξ-acyclic; sha1s a449d771…, cc94dc9c…, 56436bc0…, 5301c716… as stated):
  - MAXPLUS: dense_d5_l3_H10 from 1100110110: T 10; mover 6 (level 3, a Ξ-target) moves 10 times; every mover of levels 0-2 at most 4;
    the strict Ξ-descendants of 6 ({0, 2, 3, 4, 5, 7, 8, 9}) at most 4 ✓. Kills LEV-ADD c and DAG-ADD c for c ≤ 5 ✓.
  - DBLGAP: REC_d10_tower_mu30 from its stored start 00111111010010111010: T 35, F(0..3) = 2, 6, 14, 30, levels 1, 2, 3 doubling ✓.
  - DECAY: passfreeze77_d5 from its stored start 1101111101: T 10, F = 2, 2, 2, 6, 6, level 3 doubling, movers 8, 9 never move, no upward
    option of the top pair, F(4) = F(3) ✓.
  - REENTRY (static): REC_d10_tower_mu30 option (1, 0) (level 0) → 11 (level 5), option (11, 0) → 3 (level 1); KILL_M2D_d6_mu13 option
    (2, 1) (level 1) and (1, 0) (level 0) → 5 (level 2), option (5, 0) → 3 (level 1) ✓. **N-3:** the statement is killed at l = 1 (11, 5 ∈
    U_1 and 3 is at level 1, not > 1); at l = 0 the level-1 mover 3 is above l. The packet does not name l; W-2 (d) adds it to the line.

## DATA rule on L-1 (clause by clause) — dblcheck.py counters read (l. 8-21, 60-123)
- Each counter's unit equals the unit printed in dblcheck.out and quoted in packet §7 ✓ (WO (run, level, window, member); DBLa (run,
  level ≥ 1); DBLb (run, doubling level, window, member); DBLc (run, doubling level); PF (run, level) with the pair above never moving and
  split; HIT (run, mover, step); FU2 (run, level) for the set equality; ALTa, ALTd (run, mover, k), ALTb, ALTc (run, mover); TN (run,
  doubling level, member)). My own corpus run reproduces the run, step and doubling counts.
- **L-1's DATA parenthesis is not clause by clause:** «each statement 0 violations on its own unit over the 63,223 runs …» names no
  unit and no count per clause, does not list the no-DATA parts (MP-LIN, PASS-FREEZE's sufficient condition, REENTRY's static check),
  and does not say what replays the DEAD instances. **W-3** below.

## Required line changes (each old string occurs exactly once in L-1; bt_dbl.py / bt_dbl.out)
- **W-2 (a) (DEAD MAXPLUS instance reproducible from the line):** «(L-RED's dense_d5_l3_H10, start 1100110110: 10 moves against 4)» →
  «(experiments/si/box76/inst/dense_d5_l3_H10.json, a byte copy of L-RED's, 𝓛^R_5, start 1100110110: mover 6 of level 3, a Ξ-target,
  moves 10 times, every mover of levels 0-2 and every strict Ξ-descendant of 6 at most 4 times)»
- **W-2 (b):** «(L-LOWER's REC_d10_tower_mu30: F(0..3) = 2, 6, 14, 30)» → «(experiments/si/box76/inst/lower/REC_d10_tower_mu30.json, a
  byte copy of L-LOWER's, 𝓛^R_10, its stored start 00111111010010111010: F(0..3) = 2, 6, 14, 30)»
- **W-2 (c):** «(passfreeze77_d5: F = 2, 2, 2, 6, 6)» → «(experiments/si/box76/inst/passfreeze77_d5.json, 𝓛^R_5, its stored start
  1101111101: F = 2, 2, 2, 6, 6, the top pair never moving)»
- **W-2 (d):** «(REC_d10_tower_mu30: 11 → 3; KILL_M2D_d6_mu13: 5 → 3)» → «(at l = 1 in the static Ξ-graph: REC_d10_tower_mu30, 1 → 11 → 3;
  experiments/si/box76/inst/lower/KILL_M2D_d6_mu13.json, 2 → 5 → 3)»
- **W-3 (DATA clause by clause):** «(DATA: each statement 0 violations on its own unit over the 63,223 runs of the frozen P-IDEAL-MOVES
  corpus and the 9 L-LOWER genomes, with controls; FUEL-NEED and FUEL (i), which use L-LOWER's unrefereed FEEDBACK (b), are not stated; no
  statement bounds T polynomially)» → «(DATA, experiments/si/box79/dblcheck.py, counts CORPUS / LOWER, CORPUS the 63,223 runs of the 208
  𝓛^R_d genomes of the frozen P-IDEAL-MOVES corpus (every start for d ≤ 5, the stored start otherwise) and LOWER the 9 L-LOWER kill
  genomes from their stored starts: WINDOW-ONCE 0 violations on 577,908 / 1,736 (run, level, window, member); DBL-EQ (a) 0 on 225,647 / 72
  (run, level ≥ 1), (b) 0 on 11,052 / 176 (run, doubling level, window, member), (c) 0 on the 4,534 / 12 doubling (run, level);
  PASS-FREEZE 0 on 23,317 / 0 (run, level) with the pair above never moving and split at the start; HIT 0 on 1,298,948 / 5,216 (run,
  mover, step); FUEL-EXACT 0 on 288,870 / 81 (run, level); ALT-MIN (a)-(d) 0 on 577,740 / 162 (run, mover); TOWER-NEED 0 on 9,068 / 24
  (run, doubling level, member); MP-LIN, the sufficient condition of PASS-FREEZE and the DEAD-REENTRY instances (static): no separate DATA;
  the other three DEAD instances re-run by experiments/si/box79/dead79.py; FUEL-NEED and FUEL (i), which use L-LOWER's unrefereed FEEDBACK
  (b), are not stated; no statement bounds T polynomially)»
- L-1 with W-2 (a)-(d) and W-3 (my script): sha1 837e3b06c35e2ad8e723b9e18b9f4a2dc61c27a2 with its newline, 4,696 B, 1 line,
  85 «(» = 85 «)», depth never negative, 0 «|». (The numbers in W-3 are dblcheck.out's, reproduced by check79.sh; the lane may phrase W-3
  differently if every clause keeps its unit, set and count.)
- Every other clause of L-1 diffed against the packet: premises, definitions (U_l, E_l, windows, doubling), MP-LIN, WINDOW-ONCE, DBL-EQ,
  PASS-FREEZE, HIT, FUEL-EXACT (set form; the inequality is not in the line), ALT-MIN, TOWER-NEED, the four DEAD statements ✓.

## Notes (no verdict change)
- N-1: L-1's premise list includes R113 F0, which only FUEL (i) uses, and FUEL (i) is not stated in the line; F0 can be dropped there.
- N-2: L-1 defines U_l as «the Ξ-targets of options of movers of level ≤ l whose Ξ-target has a higher level»: «higher» means higher
  than that mover's level (packet §0, «Upward option»). FUEL-EXACT holds for any set U, so this does not affect a verdict.
- N-3: DEAD-REENTRY is killed at l = 1 (above).

## Findings
- F-1: every signable statement SIGN; ALT-MIN's use of R116 AND-GATE (a)-(c) is a faithful partition of the landed clause.
- F-2: W-1 (packet): PATH-RISE misquoted (content right, words not R113's).
- F-3: own simulator: 0 violations of every check on CORPUS (63,223 runs), LOWER (9) and EXTRA (4); DBL-EQ holds on H6's five doubling
  levels; all four DEAD instances replayed.
- F-4: L-1 MATCHES after W-2 (a)-(d) and W-3.

## Tools and outputs (docs/referee-2/R2-P-IDEAL-DBL/)
r2dbl.py (FILE ... | corpus ROOT | dead ROOT_SI) / r2dbl_corpus.out, r2dbl_lower.out, r2dbl_extra.out, r2dbl_dead.out, r2dead4.out;
bt_dbl.py / bt_dbl.out. Re-run from the repo root: `python3 docs/referee-2/R2-P-IDEAL-DBL/r2dbl.py corpus experiments/new` (39 s); the
box76 / box79 instance paths are relative to a `git archive f5263d5a`.

## Addendum 1: fix round 1 / L-2 (claude/l-si 0ea6959f; REFEREE-2 successor 30, 2026-11-07 10:1xZ by date -u)
- Object (sha1 at 0ea6959f, equal to the Lead's relay 10:07Z): docs/si/P-IDEAL-DBL-fixes.md 172bfa2f… (8,797 B, entry 1); L-2
  docs/si/P-IDEAL-DBL-line-L2.txt 1b3dc825… (5,810 B); packet 3573e93b… and L-1 93177184… unchanged. I read REFEREE's items only as the
  fixes file quotes them, after my report (2b425bb6) was on origin.
- Byte test (own script R2-P-IDEAL-DBL/bt_l2.py, output bt_l2.out; the seven OLD / NEW pairs read by script from the fixes file): each old
  string once in L-1, each new once in L-2; L-1 with all seven == L-2 byte for byte (sha1 1b3dc825…, 5,810 B, 1 line, 97 «(» = 97 «)»,
  depth never negative, 0 «|») ✓. W-2 (a), (b), (c): NEW is my text verbatim ✓.
- **W-1 closed** (F-1): the new §0 quote «(PATH-RISE) at any degree, the current value cv(z) of every mover z rises at most P(z) − 1 times in
  a run» is a verbatim substring of landed R113 (trunk 97d17f63) ✓, with R113's scope «on acyclic Ξ-graphs» stated.
- **DEAD-REENTRY (Lead ruling 3; DB-L2 + my W-2 (d) + N-3)** — level sets checked with my own code (r2reentry.out; U_l = Ξ-targets of
  upward options of movers of level ≤ l, strict Ξ-descendants along any option, every l in 0..d − 2):
  - REC_d10_tower_mu30: false for l = 1, …, 8 (reading A, as worded) and for l = 1, …, 8 (reading B, y ∈ U_l of level > l); true for l = 0.
  - KILL_M2D_d6_mu13: false for l = 1, …, 4 (A) and l = 1, …, 3 (B); true for l = 0.
  - Equal to the lane's reentry_levels.out as quoted in F-2 ✓. The witnesses hold on the whole sets: 11 ∈ U_l for every l ≥ 0 (target of
    mover 1, level 0) and 3 has level 1 ≤ l; 5 ∈ U_l for every l ≥ 1 (target of mover 2, level 1) ✓.
  - **My N-3 was incomplete**: it named only l = 1 (the report) and my 08:5xZ message to the Lead said «killed at l = 1 only», which
    is wrong: the same witnesses kill every l ≥ 1 up to d − 2. F-2's correction is right; I withdraw «only».
  - L-2's new DEAD-REENTRY text (reading A, both sets, both witnesses, «true for l = 0 on both») matches the data ✓.
- **DATA clause (Lead ruling 2: DB-L1's text as base, my W-3's no-DATA items and the dead79.py pointer added)**, judged in meaning:
  every count equals dblcheck.out / dblcheck_neg2.out (my W-3 numbers and my own corpus run: 63,223 runs, 140,395 steps, 4,534 / 12
  doubling); units per counter as in dblcheck.py (l. 8-21) ✓; the added scope «every genome of degree 2 and width 2 (so HIT and ALT-MIN,
  stated at any degree, are tested only there)» is true of both scopes ✓; «TOWER-NEED's bounds on P and R … its moves clause through
  DBL-EQ (b)» is what counter TN does ✓; the controls (ALTb_T 112,372 / 43, ALTc_T 7,085 / 13, HIT under NEG=2 238,546) are dblcheck's ✓;
  PASS-FREEZE's 23,317 counts the conclusion and «the sufficient condition … no separate DATA» is the rest of my W-3 ✓ (F-4). My W-3 is
  met in substance.
- N-1 (F0 dropped from the premise list) ✓; N-2 («higher level than that mover») ✓. F-3 (DB-3: step 1 is not an l-b-step at a doubling
  level) agrees with my own §«Proofs» remark ✓.
- Verdict: fixes entry 1 **CORRECT**; W-1, W-2 (a)-(d), W-3 **met**; **L-2 MATCHES** the packet with fixes entry 1, in bytes and in meaning
  (Opus 5.5, D1). Statement verdicts unchanged (all SIGN).
