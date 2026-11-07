# R-P-TOWER-FUEL: REFEREE report on P-TOWER-FUEL (L-LOWER successor 5)
REFEREE successor 27 (Opus 5.5, D15). Written from 2026-11-07T14:41Z (date -u); the header time of record is the commit time.
Packet frozen at claude/l-lower 7f7ff6f587c88fcfc5302905732c975f5e75ce4d. I did NOT read docs/referee-2/ for this report.

## 0. Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §1 | premises R104 (definition), R105 ENC, R110 (𝓛^R_d), R113 ALIGN | all LANDED on trunk 9315f36c; both «…» premise quotes verbatim in their RESULTS entries (script) |
| §2 | Lemma 0 MOVE | SIGN |
| §2 | Lemma 1 DOUBLE-EQ (E1)-(E5) | SIGN (remark TF-2, optional: (E5) holds without F(j − 1) ≥ 1) |
| §2 | Lemma 2 PULSE-NEST | SIGN |
| §2 | Lemma 3 GAP-NEST (with the capped corollary) | SIGN |
| §2 | Lemma 4 DOMINANCE-FREEZE (a), (b) | SIGN |
| §2 | Lemma 5 CROSS-ECONOMY (i), (ii) | SIGN |
| §2 | Lemma 5 CROSS-ECONOMY (iii) | SIGN WITH GAP TF-1: statement true; the proof's inequality «\|D_s\| ≥ 2^(rank of the top element) > 2·max(\|θ\|)» is FALSE (fails on 57 of 86 RANK states of the corpus); repaired proof in §3 |
| §4 | instances I-ROOM, I-FUEL (DATA) | every count reproduced by my own simulator; unit slip TF-3 and scope slip TF-4 in the packet text |
| §5 | DATA counters | every counter reproduced exactly; MOVE, E1, E2, the γ clause of (E5), Lemma 4 (a) at every state and Lemma 5 (i) also checked (0 violations) |
| L-1 | the line | NOT YET: TF-L1, TF-L2, TF-L3 (DATA rule, required); TF-L4, TF-L5 optional; exact texts in §5 |
| §7 | TARGET.md diff | CLEAN |

Gaps of record: TF-1 (proof of (iii); closed by the repair in §3 once the lane takes it into a fixes entry). Packet-description slip
(Lead 14:36Z): the packet's report and the brief gave L-1 as «3,699 bytes»; it is 3,699 characters = 3,834 bytes (sha1 binds).

## 1. Objects
- At 7f7ff6f5 (worktree; `git merge-base --is-ancestor 7f7ff6f5 origin/claude/l-lower` true), sha1 of the bytes:
  - docs/lower/P-TOWER-FUEL.md a093e0e7…, 130 lines;
  - docs/lower/P-TOWER-FUEL-line-L1.txt 408470adbb1d80f0ed4f29b363867da3d6d430d4 (EQUAL to the brief), 3,834 bytes, 3,699 characters,
    64 «(» = 64 «)»;
  - experiments/lower/l5/p_tower_check.py 1ed48e10…; experiments/lower/check.sh 20f21b19…;
  - experiments/lower/l4/rec/G7_best_d28.txt b995fff21c1f8558eb3e1868ec5ce59a3d4ccfb3, experiments/lower/l5/rec/SL41_d28.txt
    c1b46c319fd614e5bcb0909b616a9f2833e0dfee: EQUAL to the packet.
- experiments/lower/check.sh at 7f7ff6f5: exit 0; its P-TOWER-FUEL block prints «pins OK: 3 files» and «P-TOWER-FUEL CHECK PASS»
  (scratch/tf_logs/lane_check_7f7ff6f5.out).
- My simulator: docs/referee/scratch/t3r_sim.py (successor 24, written from R104's text; sha1 c593409f…). No L-LOWER code imported by
  my scripts; the genome text format (d / xt / br / bp / gate / start, option m = 2x + k, W-target 2(l − 1) + k) is read by my own loader
  (tf_replay.load), from R110's 𝓛^R_d convention.

## 2. Premises (§1)
- All four are LANDED on trunk claude/vibrant-johnson-nxvvxo 9315f36c: «### R104 [refereed-only]», «### R105 [refereed-only]», «### R110
  [refereed-only]», «### R113 [refereed-only]» (RESULTS.md lines 9864, 10155, 11323, 12152).
- Quote check (scratch/tf_quotes.py: every «…» of the packet and of L-1, split at «…», searched in the line of each RESULTS entry):
  - the ENC quote: both fragments verbatim in R105's line, and only there;
  - the ALIGN quote: verbatim in R113's line;
  - the two other «…» in the packet («signed, not landed», «P-TOWER-FUEL CHECK PASS») are not quotes of RESULTS. L-1 has no «…».
- Uses match the premise scopes:
  - R104: the step (A-sets under the old state, key-least option of the A-set under the new state, lowest level first; distinct ranks
    and gate indices) is its definition («An IDEAL step moves every mover to the lexicographically least key (gate indices of the chain
    of W-targets under the new state, lowest level first) among its current option and the options with a strictly better Ξ-value»).
  - R113 is used for ALIGN and its notation (c_l, γ_l, flip, F(l), cv) only. PAIR-DOUBLE and T-BOUND are not cited: Lemma 1 re-proves
    F(j) ≤ 2F(j − 1) + 2, and «capped» is a definition.
  - R110: only the definition of 𝓛^R_d (W-pointing of option k to mover 2(l − 1) + k).
  - No R116, R119 or lane item is used in a proof (checked line by line in §3).

## 3. Proofs (each step re-derived)
- Lemma 0 MOVE: SIGN.
  - Degree 2: A_(s_(t−1))(x) is {s_(t−1)(x)} or both options (the other one iff strictly better under s_(t−1)).
  - The new option is the key-least option of the A-set under s_t (R104). By ALIGN at s_t (l ≥ 1), the key-least of both options is
    c_l(s_t). So x moves iff the A-set has both options and c_l(s_t) ≠ s_(t−1)(x), and then lands on c_l(s_t).
  - Own DATA: both directions and the landing option, 0 violations on 72,974 (step, mover of level ≥ 1) units of the 24 runs.
- Lemma 1 DOUBLE-EQ: SIGN.
  - Non-b-step (c_t = c_(t−1)): movers land on c_t, so each mover lowers Φ by 1; the ALIGN order changes only through the pair's states,
    so flip ≤ 1. With r movers: r = 0 gives flip 0 = drop; r = 1 gives flip ≤ 1 = drop (equality iff a flip); r = 2 gives flip ≤ 1 < 2.
  - b-step: a := Φ(t − 1) is the number of members on c_t; they cannot move (moving lands on c_t). The movers come from c_(t−1); the
    non-movers on c_(t−1) count in Φ(t). So Φ(t) = 2 − a − r, and h := flip − (Φ(t − 1) − Φ(t)) = flip − (2a + r − 2). I re-derived each
    case of the ALIGN expression: (0, 0) both on c_(t−1) before and after, order γ_j(c_(t−1)) both times, flip 0, h = 2; (0, 1) h = flip + 1
    ≤ 2; (0, 2) h = flip ≤ 1; (1, 0) states unchanged and split, order [s(2j) = c] flips with c, h = 1; (1, 1) h = flip − 1 ≤ 0; (2, 0)
    both on c_t, no flip, h = −2. Equal to the packet's table.
  - The b-steps of level j are the flips of pair j − 1 (R113's c_j is read off that pair's key order), so there are F(j − 1) of them
    and F(j) ≤ Φ(0) − Φ(T) + 2F(j − 1) ≤ 2 + 2F(j − 1). Equality forces (E1), (E2), equality at every non-b-step and h = 2 at every b-step
    (a = 0; r ≤ 1, with a flip if r = 1). (E3) follows as written.
  - (E4): (E1) and (E2) give Φ(0) = 2 ≠ 0, so step 1 is never a j-b-step. Each window starts with both members on 1 − c (Φ = 2 at s_0
    or Φ = 0 w.r.t. the previous c), must end with Φ = 0, a moved member cannot move again while c is constant (Lemma 0), and each move
    lowers Φ by 1: exactly one move each.
  - (E5): the derivation [first is 2j] = ¬γ_j(w) and γ_j(c′) = γ_j(w), w = 1 − c′, is correct.
  - TF-2 (optional remark, no change required): γ_j(c′) = γ_j(1 − c′) is already γ_j(0) = γ_j(1), from ONE window; then
    [first is 2j] = ¬γ_j(0) in every window. So (E5) holds without F(j − 1) ≥ 1. Own DATA: the corpus has one doubling level with
    F(j − 1) = 0 (DBL4_d20_F30, level 1); the γ clause and the same-first-mover clause hold there too (0 violations on all 62).
- Lemma 2 PULSE-NEST: SIGN.
  - By (E3) at level j, the (j + 1)-b-steps are exactly the moves of pair j, which by (E4) are the u₁(V), u₂(V). So [u₁(W), u₂(W) − 1] is
    a (j + 1)-window, and the induction hypothesis (levels j + 1, …, j + k doubling) puts two pair-(j + 1) moves ≥ k apart inside it;
    its length u₂ − u₁ is ≥ k + 1. Base k = 0: two moves at distinct steps ((E3)).
- Lemma 3 GAP-NEST: SIGN.
  - [u₂(W), u₁(W⁺) − 1] is a (j + 1)-window (no pair-j move strictly between); Lemma 2 at base j + 1 with k − 1 ≥ 0 gives length ≥ k + 1.
  - Corollary: capped levels 0, …, h − 1 make levels 1, …, h − 1 doubling (2(2^(l+1) − 2) + 2 = 2^(l+2) − 2); k = h − 1 − j; GAP needs
    k ≥ 1, i.e. j ≤ h − 2. Correct.
- Lemma 4 DOMINANCE-FREEZE: SIGN.
  - (a): by ENC the value of (x, k) is the sum of ε over chain_s(x, k) (acyclic: each option once). Common options cancel; the ranks are
    distinct, so the sign of v(x, 0) − v(x, 1) is that of the top term. The symmetric difference is non-empty ((x, 0) is on chain(x, 0)
    only, by acyclicity), so no tie.
  - (b): by (E4) consecutive moves of x lie in consecutive j-windows, whose c_j differ. At each move the A-set has both options, so the
    new option is π of the previous state: π_(s_(t−1))(x) ≠ π_(s_(t′−1))(x). By (a), dec differs at s_(t−1) and s_(t′−1) (stronger than «not
    constant»; own DATA: dec(s_(t−1)) = dec(s_(t′−1)) on 0 of the 1,390 units).
  - Own DATA for (a), stronger than the lane's counter: π computed by R104's set rule (t3r_sim.better) equals the parity rule applied
    to dec at EVERY state, for every mover: 0 violations on 77,674 (state, mover) units.
- Lemma 5 CROSS-ECONOMY:
  - (i): SIGN. v(2j, 0) − v(2j, 1) = ε(2j, 0) − ε(2j, 1) + D and v(2j + 1, 1) − v(2j + 1, 0) = ε(2j + 1, 1) − ε(2j + 1, 0) + D, from ENC with
    xt(2j, k) = A_k, xt(2j + 1, k) = A_(1−k). Own DATA: 0 violations at every state of the 4 crossed doubling pairs (185 units).
  - (ii): SIGN. Lemma 0 gives π_(s_(u₁−1))(f) = c = π_(s_(u₂−1))(x₂); option c is the A_c-side of 2j and the A_(1−c)-side of 2j + 1; both cases
    of f checked.
  - (iii): SIGN WITH GAP TF-1. The statement is true; the proof is not.
    - The packet: «Under the RANK hypothesis at s, |D_s| ≥ 2^(rank of the top element) > 2·max(|θ_(2j)|, |θ_(2j+1)|)». The first
      inequality is false: D_s is ±2^R plus lower terms of either sign, so |D_s| can be far below 2^R. Arithmetic witness: chain(A_0) △
      chain(A_1) = {even rank 10 on A_0's side; even ranks 9, 8, 7, 6 on A_1's side}, so D = 1024 − 960 = 64 < 1024; with the four
      pair-j ranks among {5, 4, …}, 2·max |θ| can be 2·48 = 96 > 64, so the second inequality fails as well.
    - Measured: the first inequality fails at 57 of the 86 RANK states (43 windows × 2) of the corpus (scratch/tf_logs/corpus.log,
      counter proofstep_absD_lt_2^R). The second held there (0 of 86), but the arithmetic shows it is not implied.
    - Repaired proof (to go into a fixes entry): fix s with the RANK hypothesis; let m* be the option of largest rank R in
      chain_s(A_0) △ chain_s(A_1) (chains of the current options). By acyclicity, (2j, k) and (2j + 1, k) lie on neither chain, and
      chain_s(2j, k) = {(2j, k)} ∪ chain_s(A_k), chain_s(2j + 1, k) = {(2j + 1, k)} ∪ chain_s(A_(1−k)). So chain_s(2j, 0) △ chain_s(2j, 1) is
      {(2j, 0), (2j, 1)} ∪ (chain_s(A_0) △ chain_s(A_1)), whose top element is m* (RANK); by Lemma 4 (a), the sign of v(2j, 0) − v(2j, 1) =
      D_s − θ_(2j) is the sign of m*'s term in D_s, which is the sign of D_s (D_s ≠ 0, its top term is m*'s). The same for 2j + 1 with
      D_s − θ_(2j+1). Hence [D_s > θ_(2j)] = [D_s > θ_(2j+1)] = [D_s > 0], and (ii) gives the sign change. ∎
    - The packet's closing clause «and nothing else is required of it there» is a READING, not part of the signed statement (L-1 does
      not carry it).

## 4. Replays with my own simulator (scratch/tf_replay.py on t3r_sim.py)
- Instances (scratch/tf_logs/inst.log). Both in 𝓛^R_28 and Ξ-acyclic (t3r_sim.in_LR).
  - I-ROOM G7_best_d28: stored start 11110011110011000111100110010001000101011001000100001100 (= packet); T 270; F[0..7] = 2 6 14 30 62
    126 222 158; doubling levels 1-5. PULSE, GAP ≥ 7 − j: levels 1-4: 0; level 5: 16 pulse violations (15 in windows opened by mover 9
    moving to option 1, 1 in the first window) and 14 gap violations (all opened by (9, 1)), every one of length 1; 30 (window,
    condition) units on 16 DISTINCT windows of 63. Level 6: 48 of 127 windows without one move of each of 12, 13 (they have 0 or 1 moves).
  - I-FUEL SL41_d28: stored start equal to the packet's; T 290; same F[0..7]; doubling 1-5; 0 violations at levels 1-5; level 6: 48 of
    127 windows fail. xt(12, ·) = (22, 11), xt(13, ·) = (11, 22): CROSS with A_0 = 22, A_1 = 11. Option 19 = (9, 1): rank 87, odd; xt(11, 1)
    = 9.
  - The «decided by (9, 1)» claim depends on the scope, which neither L-1 nor packet §4 states (TF-4). Measured, dec_s(12) or dec_s(13)
    equal to option 19:
    | scope (window [a, e]) | failing 6-windows | other 6-windows |
    | --- | --- | --- |
    | at SOME state s_(a−1), …, s_(e−1) (the lane's counter) | 48 / 48 | 0 / 79 |
    | at s_(a−1) only | 32 / 48 | 0 / 79 |
    | at EVERY state s_(a−1), …, s_(e−1) | 16 / 48 | 0 / 79 |
    | at some state s_a, …, s_e | 32 / 48 | 0 / 79 |
    The packet's «48 / none of the 79» is exact for the first scope only.
- Corpus (scratch/tf_logs/corpus.log): 24 runs (15 l3/kill, 7 l4/rec, I-ROOM, I-FUEL), all in 𝓛^R_d. Every lane counter reproduced
  EXACTLY: 62 doubling levels; 757 j-windows; E3, E4, E5 0; PULSE-NEST 0 on 757, attained 215; GAP-NEST 0 on 260, attained 12;
  DOMINANCE-FREEZE (a) 0 on 65,885 equal-decider (consecutive-state pair, mover) units (of 76,972), (b) 0 on 1,390; CROSS-ECONOMY 4
  pairs, (ii) 0 on 65 windows, (iii) 43 units, 0 violations. The 4 crossed doubling pairs are the packet's list.
- Extra counters (mine; 0 violations each): MOVE both directions 72,974; E1 and E2 on 62 levels; γ_j(0) = γ_j(1) on 62; PAIR-DOUBLE
  on every (run, level ≥ 1); Lemma 4 (a) at every state 77,674; Lemma 5 (i) at every state 185.
- Controls (scratch/tf_logs/mutants.log, 4 runs): keys under the OLD state → MOVE 59 violations; reversed parity rule → Lemma 4 (a)
  424; smallest-rank rule → Lemma 4 (a) 355. The PULSE and GAP counters are non-vacuous by their attained counts (bound + 1 fails on
  215 and 12 units).

## 5. DATA rule on L-1, clause by clause
| clause of L-1 | counter (unit, set, scope) | verdict |
| --- | --- | --- |
| MOVE | «no separate DATA» | OK (own count 72,974 available, not required) |
| DOUBLE-EQ, four clauses | «DOUBLE-EQ 0 violations»: no unit; the clauses have three different units | TF-L1 (required) |
| PULSE-NEST | 0 on 757 j-windows, attained 215 | OK |
| GAP-NEST (+ capped form) | 0 on 260 window pairs (k ≥ 1), attained 12 | OK |
| DOMINANCE-FREEZE (a), (b) | «65,885 equal-decider state pairs»: the unit is (consecutive-state pair, mover); «1,390 consecutive-move pairs»: unit not named | TF-L2 (required) |
| CROSS-ECONOMY | 65 windows of 4 crossed doubling pairs; sign clause on 43 | OK |
| I-ROOM | 30 = 15 + 14 + 1 (pulses and gaps named) | OK; optional TF-L5 (levels named, 16 distinct windows) |
| I-FUEL «48 of its 127 6-windows fail» | «fail» is not defined in L-1 | TF-L3 (required) |
| I-FUEL «decided by the option (9, 1)» | scope of the decider not stated; the count holds for one of four natural scopes (§4) | TF-L3 (required) |
| CROSS-ECONOMY wording «chains of A_0 and A_1» | chain of a mover = chain of its current option (the counter's reading) | TF-L4 (optional) |

Every number below is from my own scripts (tf_replay.py, tf_units.py; logs in scratch/tf_logs/). Byte test (scratch/tf_linefix.py,
linefix.out): each OLD occurs exactly once in L-1, each NEW once in the result; result sha1 d115d8df…, 4,366 bytes, 74 «(» = 74 «)»
(scratch/tf_logs/L1_proposed.txt; the lane's own L-2 binds, not this file).

- TF-L1 (required).
  - Old: «DOUBLE-EQ 0 violations;»
  - New: «DOUBLE-EQ 0 violations (no step moving both members and flips exactly at the steps moving a member: per (step, doubling
    level), 7,069; each member once per j-window: on the 757 j-windows; the same first mover: on the 61 doubling levels with F(j − 1) ≥
    1);»
  - p_tower_check.py must count and assert the 7,069 E3 units and the 61 E5 units (it counts neither today; its E5 loop runs over 62
    levels with the hypothesis inside).
- TF-L2 (required).
  - Old: «DOMINANCE-FREEZE 0 on 65,885 equal-decider state pairs and on 1,390 consecutive-move pairs;»
  - New: «DOMINANCE-FREEZE 0 on 65,885 (consecutive-state pair, mover) units with equal deciders and on 1,390 (member of a doubling
    pair, pair of consecutive moves) units;»
- TF-L3 (required).
  - Old: «while 48 of its 127 6-windows fail, in each of which the crossed pair 6 is decided by the option (9, 1) of rank 87 (in none of
    the other 79)»
  - New: «while 48 of its 127 6-windows do not contain one move of each of the movers 12 and 13 of the crossed pair 6, and in each of
    these 48 the option (9, 1) of rank 87 is dec_s(12) or dec_s(13) at some state s among s_(a−1), …, s_(e−1) of the window [a, e] (at
    no such state in any of the other 79)»
- TF-L4 (optional).
  - Old: «the largest rank in the symmetric difference of the chains of A_0 and A_1»
  - New: «the largest rank in the symmetric difference of the Ξ-chains of the current options of A_0 and A_1»
- TF-L5 (optional).
  - Old: «violates PULSE, GAP ≥ 7 − j only at level 5, 30 times»
  - New: «violates PULSE, GAP ≥ 7 − j (j = 1, …, 5) only at level 5, 30 times in 16 of its 63 5-windows»
  - If taken, p_tower_check.py must print and assert the 16 distinct windows.

## 6. Packet fixes asked (a fixes file; the packet stays frozen)
- TF-1 (required): Lemma 5 (iii) proof: replace the sentence «Under the RANK hypothesis at s, |D_s| ≥ 2^(rank of the top element) >
  2·max(|θ_(2j)|, |θ_(2j+1)|) (each θ is a difference of two terms of rank below it), so [D_s > θ_(2j)] = [D_s > θ_(2j+1)] = [D_s > 0]»
  by the repaired argument of §3 (the top element of chain(2j, 0) △ chain(2j, 1) is m*).
- TF-3 (required, §4 text): «30 at level 5 … (unit = 5-window; set = all 63 5-windows …)»: the 30 are (window, condition) units on 16
  distinct 5-windows; state the unit as (5-window, PULSE or GAP).
- TF-4 (required, §4 text): «In all 48 failing 6-windows the deciding element (Lemma 4) of 12 or 13 is option 19»: name the scope
  (some state s_(a−1), …, s_(e−1) of the window), as in TF-L3. Also, «Lemma 4 (b) is violated in exactly those windows by a parked β» is
  a READING: Lemma 4 (b) assumes a doubling level and level 6 is not doubling; no counter measures a constant decider between
  consecutive moves of 12 or 13 in those windows. Label it READING or measure it.
- §5 text: «E5 0 (unit = doubling level, 62)»: the hypothesis F(j − 1) ≥ 1 holds on 61 of the 62.
- Optional TF-2: (E5) without F(j − 1) ≥ 1 (§3).
- Description slip (Lead 14:36Z): «3,699 bytes» is 3,699 characters; L-1 is 3,834 bytes.

## 7. TARGET.md diff
- No statement in the packet or L-1 mentions a parity game, a winning region, an algorithm, a running time or a complexity class. All
  are about R104's IDEAL model on 𝓛^R_d (Ξ-acyclic). Nothing bounds T polynomially; the line says G-N5-TIME stays OPEN, not M3, not a
  gauntlet step, not a TARGET.md claim. CLEAN.
- Note, no change: «d» is the ladder depth (R110's convention), not TARGET.md's number of priorities; the landed lines R110 / R113 use
  it the same way.
- The ENC integers ±2^rank are a proof device of the model; no algorithm is claimed, so TARGET.md §3's bit-cost rule is not engaged.

## 8. Tools and outputs (committed)
docs/referee/scratch/: tf_quotes.py, tf_replay.py (loader, own R on t3r_sim, corpus and instance counters), tf_units.py,
tf_linefix.py; tf_logs/inst.log, corpus.log, mutants.log, units.log, linefix.out, L1_proposed.txt, lane_check_7f7ff6f5.out.

## §C. Fixes entry 1 and line L-2 (REFEREE successor 27; date -u at writing 2026-11-07T15:52Z)
- Objects at claude/l-lower 740f6c798860c24db35f12c5e19cac196b9b1f9b (worktree; ancestor of origin/claude/l-lower), sha1 of the bytes:
  - fixes docs/lower/P-TOWER-FUEL-fixes.md 0902efb9eaea48501e4289a8ce3980b235347ac8 (EQUAL to the Lead's relay), entry 1;
  - L-2 docs/lower/P-TOWER-FUEL-line-L2.txt d866ca50b0a0372efd9e93a2db0410801b3ddc15 (EQUAL), 4,586 bytes, 4,438 characters, 80 «(» =
    80 «)», 0 «|»;
  - packet a093e0e7… and L-1 408470ad… unchanged.
- experiments/lower/check.sh at 740f6c79: exit 0, «pins OK: 4 files», «P-TOWER-FUEL CHECK PASS» (scratch/tf_logs/lane_check_740f6c79.out).
  It now prints and asserts E3_units 7,069, E5_hyp 61, 119 j-windows, 16 distinct 5-windows, decider scopes 32 / 16, 188 of 188.
- Byte test (own script scratch/tf_fix1.py, tf_logs/fix1.out; the seven pairs written in my script: olds from the two reports, news as
  merged in fixes entry 1 §5): each OLD occurs once in L-1; each NEW once in L-2; L-1 with the seven replacements is byte-equal to L-2.
- Independence: I read docs/referee-2/R2-P-TOWER-FUEL.md (4bede4dd) only after 807984e3 was on origin.
- Merged strings, judged for meaning against my items:
  - M1 (W-2 (a), «and cv»): correct; cv is R113's notation (its line defines «cv_s(z) the integer value of z's current option»). MY MISS:
    L-1 used cv without listing it; REFEREE-2 caught it.
  - M2 (TF-L5 + TF-3 + W-2 (b)): carries the level range j = 1, …, 5, the 119 j-windows (3 + 7 + 15 + 31 + 63, my inst.log), the unit
    (5-window, PULSE or GAP) and 16 of 63. Every fact of TF-L5 and TF-3 present. MET.
  - M3 (TF-L3 + W-2 (c)): defines the 48 (not exactly one move of each of 12, 13), names the crossed targets (22, 11 = A_0, A_1), gives
    my scope «some state s among s_(a−1), …, s_(e−1)», adds «at every such state in 16» (my §4 table) and «at no such state in any of
    the other 79». MET. (Like my own text, «the option (9, 1) … is dec_s(12)» means the option component of dec; acceptable.)
  - M4 (W-4 (a)): names the 15 + 7 + 2 runs and the (run, level) unit. Correct (my corpus.log runs are exactly these 24). MY MISS: I
    passed «24 runs» without asking for the set.
  - M5 (TF-L1 + W-4 (b)): 7,069 (step, doubling level) for the first two clauses, 757 j-windows, 62 (run, level) pairs with 61 under
    the hypothesis. Equal to my tf_units.log. MET; «0 violations on 62, 61 with the hypothesis» is exact for the lane's counter, which
    tests the conclusion only where F(j − 1) ≥ 1 (and my extra count shows it holds on all 62).
  - M6 = my TF-L2 verbatim (contains W-4 (c)). MET. M7 = my TF-L4 verbatim. MET.
- Fixes entry 1 texts:
  - TF-1 (= W-1): CORRECT. The replaced sentence is the packet's; my repair is quoted byte-exactly (script tf_fixquotes.py: every «…»
    attributed to a referee occurs in that report, wrapped lines joined). REFEREE-2's route is the same argument written through ENC
    directly; both are sound. REFEREE-2's counts (|D| < 2^r* at 651 of 1,010 RANK states over all states of the 14 crossed pairs; |D| ≤
    2·max|θ| at 5) confirm on data that the packet's SECOND inequality fails too, which I had shown only by arithmetic.
  - TF-3: CORRECT (unit (5-window, PULSE or GAP), 30 units on 16 distinct windows; my inst.log).
  - TF-4 (= W-3): CORRECT. Every count in the new sentence measured by me on t3r_sim (tf_logs/fix1.out, inst.log): 48 / 48 at some
    pre-state, 32 / 48 at s_(a−1), 16 / 48 at every pre-state, 0 / 79 good; mover 9 on option 1 at every pre-state of 48 / 48 failing and
    17 / 79 good windows; dec non-constant on 188 of 188 consecutive-move pairs of 12, 13. «on 11's chain (11 → 9)»: at all 128 (state,
    member) hits the deciding side is the one with Ξ-target 11, with s(11) = 1 and option 19 on 11's current chain. The interpretation
    is labelled READING and Lemma 4 (b) is no longer said to be violated.
  - §4 (E5 hypothesis 61 of 62): CORRECT. TF-2 recorded, statement unchanged: correct (optional).
  - Description slip recorded: correct.
- Verdict: fixes entry 1 CORRECT. L-2 MATCHES (byte test and meaning). All statements SIGNED as in §0; CROSS-ECONOMY (iii) is now SIGN
  (TF-1 closed by the proof of record). TF-L1..TF-L5, TF-3, TF-4 CLOSED.

## §C add. 1. Line L-3 (CHECKER C134 R1-R4; R120) (REFEREE successor 27; date -u at writing 2026-11-07T19:08Z)
- Objects (sha1 of the bytes): L-3 at claude/l-lower 4f25ae6f (ancestor of origin/claude/l-lower) 7328e67345e1bb6a8605ccfa4f406d1020eabfdb,
  4,908 bytes, one line, 82 «(» = 82 «)», 0 «|», one « — », «gauntlet» 0 times; L-2 at 4f25ae6f d866ca50… unchanged; fixes c99bfd3a…
  (entry 2 appended). C134 read at claude/checker 23871f48 (§5).
- experiments/lower/check.sh at 4f25ae6f: exit 0, «pins OK: 5 files», «P-TOWER-FUEL CHECK PASS»; it now prints SL41_d28's 119
  j-windows (tf_logs/lane_check_4f25ae6f.out).
- Byte test (own script scratch/tf_l3.py, tf_logs/l3.out; R1-R4 written from C134 §5, wrapped lines joined by one space, applied in
  C134's order): each old string occurs once in the text it is applied to (R3's only inside R2's new text); the result is byte-equal to
  L-3.
- R1: CORRECT. Fixes entry 1 (L-LOWER successor 6) carries the proof of record of (iii) and the measured instance units / scopes
  that L-2 states.
- R2: CORRECT and correctly attributed. The proof of record is my repair, R-P-TOWER-FUEL §3 l. 107-112 at 807984e3 (checked: those
  lines are the «Repaired proof» bullet), restated byte-exactly in fixes entry 1 §1 (§C above). I signed it in §C; REFEREE-2's report
  on origin has «The proof of record (REFEREE's) is correct.» (l. 210), and its own repair is a second route. «signed by both referees»
  is true.
- R3: CORRECT, same meaning. No statement concerns an algorithm, so the line is neither a gauntlet step nor a step-4 pass; my §7 diff
  stands with the landed wording.
- R4: CORRECT. My own replay (tf_logs/inst.log, I-FUEL): 3, 7, 15, 31, 63 = 119 j-windows at j = 1, …, 5, 0 PULSE and 0 GAP
  violations of ≥ 7 − j.
- Verdict: L-3 MATCHES, by the byte test and in meaning. All statements stay SIGN as in §C.
