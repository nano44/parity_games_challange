# R-P-IDEAL-DBL: REFEREE report on P-IDEAL-DBL (L-SI successors 41/42, box 79)
REFEREE successor 26 (Opus 5.5, D15). Written from 2026-11-07T08:48Z (date -u); the header time of record is the commit time.
Packet frozen at claude/l-si f5263d5ab7a5631c82f201a05fe46710166c35fc. I did NOT read docs/referee-2/ for this report.

## 0. Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §0 | premises; AND-GATE (a)-(c) mapping onto landed R116 | AND-GATE quotes byte-equal to RESULTS at 97d17f63; mapping FAITHFUL. One premise «quote» (PATH-RISE) is not RESULTS text: DB-Q1 (citation fix, meaning equal) |
| §1 | Fact MP-LIN | SIGN |
| §2 | Lemma WINDOW-ONCE | SIGN |
| §2 | Lemma DBL-EQ (a), (b), (c) | SIGN (optional DB-3: say why step 1 is no l-b-step at a doubling level) |
| §2 | Lemma PASS-FREEZE (and its sufficient condition) | SIGN |
| §3 | Lemma HIT; Corollary FUEL-EXACT | SIGN |
| §4 | Lemma ALT-MIN (a)-(d) | SIGN |
| §4 | Lemma TOWER-NEED | SIGN (its PATH-RISE premise with DB-Q1) |
| §5 | FUEL-NEED; FUEL (i) | not reviewed for signature (CONDITIONAL on L-LOWER's unrefereed FEEDBACK (b), as the packet says) |
| §6 | DEAD-MAXPLUS, DEAD-DBLGAP, DEAD-DECAY | SIGN (own simulator; the IDEAL step is deterministic: distinct gate indices, no ties) |
| §6 | DEAD-REENTRY | SIGN WITH GAP DB-2 (the level l is not named; read literally the statement is false almost trivially) |
| L-1 | the line | NOT YET: DB-L1 (DATA rule), DB-L2 (REENTRY wording); exact texts in §5 |

## 1. Objects
- sha1 of the bytes at f5263d5a, all EQUAL to the Lead's relay:
  - docs/si/P-IDEAL-DBL.md 3573e93b…;
  - docs/si/P-IDEAL-DBL-line-L1.txt 93177184…;
  - experiments/si/box79/check79.sh 079a032d…;
  - pins.sha1: every entry equal (check79.sh runs sha1sum -c --strict).
- check79.sh at f5263d5a (worktree): «box 79 P-IDEAL-DBL (frozen) checks: PASS», exit 0. It re-ran dblcheck (CORPUS, LOWER),
  NEG=2, EXTRA, wiring and dead79, each byte-equal to its frozen output.
- Draft 2c396f6f → frozen: a word diff of the packet touches only the header, §0 (the R116 quote), the «(pending landing)» labels and
  the freeze-steps heading. No proof text changed.
- Corpus: experiments/si/box76/corpus_lr.json.gz has 208 entries. Each recorded blob sha1 equals `git rev-parse 9995f5a2:<path>` for
  208/208, so the corpus is the in-tree P-IDEAL-MOVES corpus of R116's DATA.

## 2. Premises (§0)
- AND-GATE: the packet's quote and R116's notation quotes are byte-equal to RESULTS.md at trunk 97d17f63, «### R116 [refereed-only]».
  The mapping is FAITHFUL:
  - (a) is the clause «moves at step t iff s_(t−1)(x) ≠ π_(s_(t−1))(x) = KP_(s_t)(x)»;
  - (b) is the «so moves(x) ≤ 1 + min(KF_x, PF_x)» bound;
  - (c) is «when π(x) changes at step t to b the value v(x, b) rises strictly at t».
  - Only (b) and (c) are used: ALT-MIN (c) and (a). No part of the draft's older wording (its (b) «If x moves at steps t < t′ …») survives
    in a proof.
  - R116's scope («at any degree elsewhere», a mover of degree 2, acyclic) contains ALT-MIN's hypotheses.
- R105 ENC / LOCAL / MONO, R110's 𝓛^R_d definition, R113 ALIGN and F0: quotes found verbatim in RESULTS.
- DB-Q1: the PATH-RISE «quote» «Then the number of steps at which cv(z) rises is at most P(z) − 1.» does not occur in RESULTS.md
  (2ccd037b9 or 97d17f63). R113's landed wording is «(PATH-RISE) at any degree, the current value cv(z) of every mover z rises at most
  P(z) − 1 times in a run». The meaning is the same and the packet uses exactly that.
  - Fix (packet fixes file): replace the quote by the landed wording.
  - Optional: the line's premise list names F0, which only §5 (not stated in the line) uses.

## 3. Proofs (each step re-derived)
- MP-LIN:
  - The induction x_j ≤ (A^⊗j ⊗ x_0) ⊕ max_(i<j) A^⊗i ⊗ b uses only the monotonicity of ⊗ and ⊕.
  - A length-i path splits into a simple path of length r ≤ k − 1 and cycles of total length i − r. That bounds the weight by
    λ(i − r) + r·a ≤ max(λ, 0)·i + (k − 1)·max(a, 0); the case λ < 0 is covered by λ(i − r) ≤ 0.
  - So C = (k − 1)·max(a, 0) + max(max x_0, max b).
- WINDOW-ONCE:
  - c_l(s) is read off the key order of the pair l − 1 (R113's definition), and that order changes exactly at the l-b-steps. So c_l
    is constant on [t_0, e].
  - By ALIGN, a mover lands on c; a second move would land on c again, but a degree-2 move changes the option.
- DBL-EQ:
  - (i) Off B, Φ(t) = Φ(t − 1) − m_t. On B (c flips), a non-mover is off c_t iff it was on c_(t−1), and every mover came from c_(t−1)
    to c_t, so Φ(t) = 2 − Φ(t − 1) − m_t. Telescoping gives the sum.
  - (ii) With no move, both on one option gives the order γ_l(j) twice. So a flip needs a split pair and a change of c, hence t ∈ B
    and Φ(t − 1) = 1.
  - (iii) F(l) ≤ M + B1 ≤ Φ(0) − Φ(T) + Σ_B h(Φ(t − 1)), with h = (2, 1, −2). Equality forces exactly the five conditions, and they
    restore equality (flips = moving steps gives F = M; B1 = 0; M = Σ m_t).
  - (iv) A doubling level has Φ(0) = 2 and Φ(t − 1) = 0 on B, so step 1 is not in B and there are exactly F(l − 1) + 1 windows.
    DB-3, optional: say this in the proof. Φ is 2 at each window's first state relative to the window's c, and 0 at its last, so
    both members move there, each once.
  - (v) Both members start on i = 1 − c, in order γ_l(i). The two moving steps are distinct and both flip, so
    γ_l(i) ≠ [A = p] ≠ γ_l(c), which gives γ_l(0) = γ_l(1) and A = p iff ¬γ.
- PASS-FREEZE:
  - With the pair l + 1 split and still, its order is [s(2l + 2) = c_(l+1)(s)], and c_(l+1) changes exactly at the flips of the
    pair l.
  - The sufficient condition: A_(s)(x) = {s(x)} at every state, so x never moves (R104's step uses the old state's A-sets).
  - The proof also works at l = 0. The line states no range.
- HIT:
  - (⇐) Let z be the first mover of the old chain that moves. The prefix up to z is kept; z jumps to a strictly better option under
    s_(t−1), and that option's value does not fall (ENC + MONO). So cv(y) rises.
  - (⇒) If nothing on the old chain moves, the chain and its states are kept, and LOCAL gives the same value.
  - A move of y is the case z = y.
- FUEL-EXACT: MONO makes every change a rise; then HIT applies to each y ∈ U_l, and the set is their union.
- ALT-MIN:
  - (a) is AND-GATE (c), one rise per change.
  - (b) holds because the changes of a binary π alternate.
  - (c) is AND-GATE (b) via moves ≤ 1 + PF.
  - (d) is ENC with a constant ε. Values of the two options are never equal, because the signed sums Σ ±2^rank of different β-sets
    differ: the top element of the symmetric difference dominates. So π is well defined.
- TOWER-NEED:
  - moves = f + 1 (DBL-EQ (b)) ≤ R(x) (HIT) ≤ P(x) − 1 (PATH-RISE);
  - f + 1 ≤ 2 + 2 min_k R(y_k) (ALT-MIN (c), (d)), which for f ≥ 2 excludes X.

## 4. Replays with my own code (docs/referee/scratch/; IDEAL simulator t3r_sim.py written by successor 24 from R104's text)
- dbl_replay.py computes, per run, F(l) from key orders under each state, moves, DBL-EQ (a) in both directions at every level ≥ 1, (b)
  and (c) at doubling levels, WINDOW-ONCE, and TOWER-NEED (moves, P, and R of both targets). Output dbl_logs/replay_own.out; input
  sha1s in dbl_logs/inputs.sha1.
- 16 runs, 0 violations:
  - the three DEAD instances;
  - EXTRA's four genomes;
  - the nine LOWER genomes; their doubling (run, level) count is 12, as in dblcheck.out.
- DBL-EQ on H6 (H6_d24_F126, stored start, T 209): F(0..5) = 2, 6, 14, 30, 62, 126, so levels 1-5 are doubling. Each member of the
  pair l moves exactly once per window (F(l − 1) + 1 = 3, 7, 15, 31, 63 moves), γ_l(0) = γ_l(1), and the first-mover rule holds.
  TOWER-NEED holds at every one of these levels.
- DEAD (each value equal to the packet and dead79.out):
  - MAXPLUS: dense_d5_l3_H10 from 1100110110, T 10. Mover 6 (level 3, a Ξ-target) moves 10 times. Levels 0-2 move at most 4 times,
    and so do 6's strict Ξ-descendants {0, 2, 3, 4, 5, 7, 8, 9} (dead_static_own.out). 10 > c + 4 for every c ≤ 5.
  - DBL-GAP: REC_d10_tower_mu30 from its stored start 00111111010010111010, T 35. F(0..3) = 2, 6, 14, 30; levels 1, 2, 3 are
    doubling with F(0) = 2.
  - DECAY: passfreeze77_d5 from 1101111101, T 10. F = 2, 2, 2, 6, 6; level 3 is doubling; movers 8 and 9 move 0 times; level 4 is
    the top, so it has no upward option; F(4) = F(3).
  - RE-ENTRY (static):
    - REC_d10_tower_mu30: mover 11 (level 5) is the Ξ-target of (1, 0) (level 0), and its option 0 has Ξ-target 3 (level 1).
    - KILL_M2D_d6_mu13: mover 5 (level 2) is the Ξ-target of (1, 0) and (2, 1) (levels 0, 1), and its option 0 has Ξ-target 3
      (level 1).
- Corpus, own simulator (dbl_corpus.py, dbl_logs/corpus_own_N10.out):
  - every genome of the frozen corpus with N ≤ 10 (193 genomes, read from git at 9995f5a2), every start: 63,208 runs, 140,293 steps;
  - 0 violations of DBL-EQ (a)-(c), WINDOW-ONCE, TOWER-NEED, HIT (1,297,600 (run, mover, step)), MONO, and ALT-MIN (a)-(d)
    (577,552 (run, mover));
  - 4,532 doubling (run, level).
  - dblcheck's CORPUS adds the stored-start runs of the 15 genomes with N > 10 (63,223 − 63,208 = 15 runs), which accounts for its
    larger counts.
- DEAD-REENTRY, DB-2: the packet's statement «The movers on the chains of the fuel targets U_l lie at levels > l» names no l and no
  reading of «chains».
  - U_l holds every Ξ-target of an upward option of a mover of level ≤ l, including targets of level ≤ l (e.g. level 0 → 1 at l ≥ 1).
    Read literally, the statement fails whenever such a target exists, which is nearly always.
  - The lane's own wiring79.py reads it as «the strict Ξ-descendants of y ∈ U_l».
  - The instances kill the intended statement, the strict Ξ-descendants reading: REC_d10_tower_mu30 at l = 1, …, 4 (11 ∈ U_l at
    level 5 > l, with descendant 3 at level 1 ≤ l), and KILL_M2D_d6_mu13 at l = 1 (5 ∈ U_1 at level 2, descendant 3 at level 1).
  - Fix: name that reading and those l in a fixes entry and in the line (DB-L2).

## 5. Line L-1: statement diff and DATA rule, clause by clause
- Statement diff: each statement in the line matches the packet. LEV-ADD in the line drops «a Ξ-target», which is a stronger claim,
  and the instance kills it too. PASS-FREEZE states no range; it holds for 0 ≤ l ≤ d − 2. HIT and ALT-MIN keep «at any degree» /
  «acyclic».
- DATA rule, checked against dblcheck.py's counters (every number of packet §7 equals dblcheck.out). The line's single clause «each
  statement 0 violations on its own unit over the 63,223 runs … and the 9 L-LOWER genomes, with controls» fails the rule:
  - MP-LIN has no counter («no separate DATA» in the packet), yet the clause covers it;
  - PASS-FREEZE has 0 units in LOWER, so «and the 9 L-LOWER genomes» is vacuous for it;
  - no unit is named;
  - HIT and ALT-MIN are stated at any degree, but every tested genome is degree 2, width 2;
  - TOWER-NEED's moves clause is counted by DBLb, not by TN.
- DB-L1 (required).
  - Old: «(DATA: each statement 0 violations on its own unit over the 63,223 runs of the frozen P-IDEAL-MOVES corpus and the 9 L-LOWER
    genomes, with controls; FUEL-NEED and FUEL (i), which use L-LOWER's unrefereed FEEDBACK (b), are not stated; no statement bounds
    T polynomially)»
  - New: «(DATA, experiments/si/box79/dblcheck.py, CORPUS = the 63,223 runs (140,395 steps) of the 208 𝓛^R_d genomes of the frozen
    P-IDEAL-MOVES corpus (l-new 9995f5a2; every start for N ≤ 10, the stored start otherwise), LOWER = the 9 runs of L-LOWER 3's kill
    genomes from their stored starts, counts given as CORPUS / LOWER, every genome of degree 2 and width 2 (so HIT and ALT-MIN,
    stated at any degree, are tested only there): WINDOW-ONCE 0 violations on 577,908 / 1,736 (run, level, window, member); DBL-EQ
    (a) 0 on 225,647 / 72 (run, level ≥ 1), both directions, with 4,534 / 12 doubling (run, level); (b) 0 on 11,052 / 176 (run,
    doubling level, window, member); (c) 0 on every doubling (run, level); PASS-FREEZE 0 on the 23,317 (run, level) of CORPUS whose
    pair above never moves and starts split (none in LOWER); HIT 0 on 1,298,948 / 5,216 (run, mover, step); FUEL-EXACT 0 on 288,870
    / 81 (run, level); ALT-MIN 0 on 577,740 / 162 (run, mover), (a) and (d) counted per (run, mover, k); TOWER-NEED's bounds on P
    and R 0 on 9,068 / 24 (run, doubling level, member), its moves clause through DBL-EQ (b); controls: ALT-MIN's bounds (b) and (c)
    minus 1 fail on 112,372 / 43 and 7,085 / 13 (run, mover), and with the key-least option taken regardless of availability HIT
    fails on 238,546 CORPUS (run, mover, step); MP-LIN no separate DATA; FUEL-NEED and FUEL (i), which use L-LOWER's unrefereed
    FEEDBACK (b), are not stated; no statement bounds T polynomially)»
  - Every number is in dblcheck.out / dblcheck_neg2.out, and every unit is the one dblcheck.py prints or counts. The NEG=2 HIT
    count 238,546 is over the NEG=2 run's own 574,938 units.
- DB-L2 (required).
  - Old: ««the chains of the fuel targets U_l stay above level l» (REC_d10_tower_mu30: 11 → 3; KILL_M2D_d6_mu13: 5 → 3)»
  - New: ««the strict Ξ-descendants of the fuel targets U_l lie at levels > l» (static Ξ-graph; REC_d10_tower_mu30: 11, of level 5,
    is in U_l through mover 1's option 0 and has the descendant 3 of level 1, so it fails for l = 1, …, 4; KILL_M2D_d6_mu13: 5, of
    level 2, is in U_1 and has the descendant 3 of level 1)»
- EXTRA (RECF4, DBL4, H5, H6; extra79.out, not cited in the line): 0 violations of every counter (4 runs, 442 steps, 16 doubling
  (run, level)). My own replay of the same four agrees (§4).
- TARGET.md diff: no statement mentions a parity game, a winning region or a running time. All are about R104's IDEAL model
  (MP-LIN about max-plus). Nothing bounds T polynomially, and G-N5-TIME stays OPEN.

## 6. Packet fixes asked (a fixes file; the packet stays frozen)
- DB-Q1: PATH-RISE quoted from the landed R113 text.
- DB-2: DEAD-REENTRY with the strict-descendant reading and the levels l.
- Optional DB-3: in DBL-EQ (iv), step 1 ∉ B at a doubling level, so there are F(l − 1) + 1 windows.

## 7. Tools and outputs (committed)
docs/referee/scratch/:
- dbl_replay.py, dbl_dead_static.py, dbl_corpus.py (with t3r_sim.py);
- dbl_logs/replay_own.out, dead_static_own.out, corpus_own_N10.out, inputs.sha1, check79_rerun.out.
