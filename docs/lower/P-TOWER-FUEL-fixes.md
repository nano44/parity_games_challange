# P-TOWER-FUEL fixes (append-only; the packet docs/lower/P-TOWER-FUEL.md stays frozen at 7f7ff6f5, line L-1 at 408470ad…)

## Fixes entry 1 (2026-11-07, L-LOWER successor 6; fix round 1; written by experiments/lower/l5/mkfix_tf.py)
Reports answered: REFEREE 27 claude/referee 807984e30699f4fa5b042dabb1bf1470a83ac928, docs/referee/R-P-TOWER-FUEL.md (all SIGN;
  CROSS-ECONOMY (iii) SIGN WITH GAP TF-1; L-1 NOT YET: TF-L1, TF-L2, TF-L3 required, TF-L4, TF-L5 optional); REFEREE-2 31
  claude/referee-2 4bede4dda1e0610627cf44661acb65555ccc456e, docs/referee-2/R2-P-TOWER-FUEL.md (all SIGN, (iii) on its repaired proof;
  L-1 MATCHES after W-2 (a)-(c), W-4 (a)-(c)). Merged under the Lead rulings of 15:18Z (Lead reading). Every «…» below is copied by the
  script from byte copies of the reports or of the packet (wrapped lines joined by single spaces).

### 1. TF-1 = W-1: proof of Lemma 5 (iii) (statement unchanged)
- Packet text replaced (§3, Lemma 5 proof): «Under the RANK hypothesis at s, |D_s| ≥ 2^(rank of the top element) >
  2·max(|θ_(2j)|, |θ_(2j+1)|) (each θ is a difference of two terms of rank below it), so [D_s > θ_(2j)] = [D_s > θ_(2j+1)] = [D_s
  > 0]». Both referees found this inequality false; their counts are on different state sets: REFEREE (RANK states at the two
  pre-states u₁ − 1, u₂ − 1 of the 43 corpus windows): «Measured: the first inequality fails at 57 of the 86 RANK states (43
  windows × 2) of the corpus (scratch/tf_logs/corpus.log, counter proofstep_absD_lt_2^R)»; REFEREE-2 (every corpus state of the
  14 crossed pairs at which RANK holds): «Measured on the 1,010 corpus states of the 14 crossed pairs where the RANK hypothesis
  holds (r2tower.out): |D| < 2^r* at 651, and |D| ≤ 2·max|θ| at 5.».
- Proof of record (REFEREE's repair; it uses only the packet's Lemma 4 (a), ENC and acyclicity): «fix s with the RANK hypothesis; let m*
  be the option of largest rank R in chain_s(A_0) △ chain_s(A_1) (chains of the current options). By acyclicity, (2j, k) and (2j + 1, k)
  lie on neither chain, and chain_s(2j, k) = {(2j, k)} ∪ chain_s(A_k), chain_s(2j + 1, k) = {(2j + 1, k)} ∪ chain_s(A_(1−k)). So
  chain_s(2j, 0) △ chain_s(2j, 1) is {(2j, 0), (2j, 1)} ∪ (chain_s(A_0) △ chain_s(A_1)), whose top element is m* (RANK); by Lemma 4 (a),
  the sign of v(2j, 0) − v(2j, 1) = D_s − θ_(2j) is the sign of m*'s term in D_s, which is the sign of D_s (D_s ≠ 0, its top term is
  m*'s). The same for 2j + 1 with D_s − θ_(2j+1). Hence [D_s > θ_(2j)] = [D_s > θ_(2j+1)] = [D_s > 0], and (ii) gives the sign change.
  ∎»
- Independent second route (REFEREE-2's repair, recorded, not needed for the record): «(iii) 2j and 2j + 1 have Ξ-edges to both A_0 and
  A_1, so by acyclicity no chain of A_0 or A_1 meets pair j, and D_s − θ_(2j) = v_s(2j, 0) − v_s(2j, 1) is (ENC) a signed sum of ±2^rank
  over the disjoint union {(2j, 0), (2j, 1)} ∪ (chain(A_0) △ chain(A_1)) with distinct ranks; under the RANK hypothesis its largest-rank
  term is that of D_s, so sign(D_s − θ_(2j)) = sign(D_s), and likewise for θ_(2j+1); so [D_s > θ_(2j)] = [D_s > θ_(2j+1)] = [D_s > 0];»
  REFEREE-2: «Checked pointwise at every state of every crossed pair: 0 violations on 1,010 RANK states, and |D| > max|θ| at all of
  them.»

### 2. TF-3: unit of the 30 I-ROOM units (§4)
- «(unit = 5-window; set = all 63 5-windows; scope = stored start)» reads «(unit = (5-window, PULSE or GAP): 30 units on 16 distinct
  5-windows; set = all 63 5-windows; scope = stored start)». p_tower_check.py now asserts the 16 distinct windows and the 119 j-windows
  of levels 1-5.

### 3. TF-4 = W-3: the I-FUEL decider sentence (§4)
- Packet text replaced: «In all 48 failing 6-windows the deciding element (Lemma 4) of 12 or 13 is option 19 = (mover 9, option 1), rank
  87, odd parity, on 11's chain (11 → 9), and in none of the 79 other 6-windows (unit = 6-window; set = all 127; scope = stored start).
  So the room conditions are met and the missing piece is fuel: Lemma 4 (b) is violated in exactly those windows by a parked β of the
  capped pair 4.»
- New text: «In each of the 48 failing 6-windows [a, e], option 19 = (mover 9, option 1), rank 87, odd parity, on 11's chain (11 → 9),
  is dec_s(12) or dec_s(13) at some state s among s_(a−1), …, s_(e−1); at s_(a−1) itself in 32 of the 48; at every such state in 16 of
  the 48; at no such state in any of the 79 other 6-windows (unit = 6-window; set = all 127; scope = stored start). Mover 9 is on option
  1 at every pre-state of all 48 failing windows (and of 17 good ones). Lemma 4 (b) is not applied here: level 6 is not doubling; its
  conclusion (a non-constant decider between consecutive moves) holds for all 188 consecutive-move pairs of 12 and 13. READING: the room
  conditions are met and the missing piece is fuel; the parked β of option (9, 1) of the capped pair 4 dominates the crossed comparison
  in those windows (DOMINANCE-FREEZE read as an interpretation, not applied as a lemma).»
- Counts re-measured by me with an independent simulator (experiments/lower/l6/sim6.py, Python big integers, not sharing code with
  p_tower_check.py): 48 / 48 at some pre-state, 32 / 48 at s_(a−1), 16 / 48 at every pre-state, 32 / 48 at some state s_a … s_e, 0 / 79
  good; mover 9 on option 1 at every pre-state: 48 failing, 17 good; decider non-constant on 188 of 188 consecutive-move pairs of 12,
  13. Equal to both referees: REFEREE §4 table (failing / other: some pre-state 48 / 48, 0 / 79; s_(a−1) only 32 / 48, 0 / 79; every
  pre-state 16 / 48, 0 / 79; some state s_a … s_e 32 / 48, 0 / 79) and «The packet's «48 / none of the 79» is exact for the first scope
  only.»; REFEREE-2 «- **§4 reading, false literally (W-3).** «Lemma 4 (b) is violated in exactly those windows by a parked β of the
  capped pair 4» does not hold literally: - for every pair of consecutive moves of 12 (94 pairs) and of 13 (94 pairs), dec is NOT
  constant between them, i.e. the conclusion of Lemma 4 (b) holds everywhere (r2fuel.out); - level 6 is not doubling, so (b) does not
  apply in any case; - what fails in the 48 windows is the move count (E4).» p_tower_check.py now asserts 32, 16 and 188.
- REFEREE's scope note on the same sentence: ««Lemma 4 (b) is violated in exactly those windows by a parked β» is a READING: Lemma 4 (b)
  assumes a doubling level and level 6 is not doubling; no counter measures a constant decider between consecutive moves of 12 or 13 in
  those windows. Label it READING or measure it.»

### 4. §5: hypothesis of (E5)
- «E5 0 (unit = doubling level, 62)» reads «E5 0 (unit = doubling (run, level) pair, 62; its hypothesis F(j − 1) ≥ 1 holds on 61 of
  them)». Optional TF-2 = N-1 noted, statement NOT changed (it stays as frozen and as in L-2): REFEREE «TF-2 (optional remark, no change
  required): γ_j(c′) = γ_j(1 − c′) is already γ_j(0) = γ_j(1), from ONE window; then [first is 2j] = ¬γ_j(0) in every window. So (E5)
  holds without F(j − 1) ≥ 1.»; REFEREE-2 «**N-1:** since {w, c′} = {0, 1}, one window already gives γ_j(0) = γ_j(1) and fixes the first
  mover as 2j iff ¬γ_j(0), so the hypothesis F(j − 1) ≥ 1 is not needed. The statement as written is true; no change is required.»

### 5. Line L-2 (docs/lower/P-TOWER-FUEL-line-L2.txt; made by experiments/lower/l5/mkL2_tf.py)
- sha1 d866ca50b0a0372efd9e93a2db0410801b3ddc15, 4586 bytes, 4438 characters, 1 line + «\n»; parentheses balanced (depth never
  negative); no «|». Each old string occurs exactly once in L-1, each new exactly once in L-2 (asserted by mkL2_tf.py). L-2 is not equal
  to either referee's predicted line (REFEREE d115d8df…, REFEREE-2 1a4e8dcc…): the Lead's rulings merge the two sets. Pinned in
  p_tower_check.py.
- Merge map (L-2 replacement → referee items; where both targeted one old string, ONE new string carries the facts of both):
  - M1 notation «… F(l) and cv)»: W-2 (a) (REFEREE-2; old and new copied from its report).
  - M2 I-ROOM: TF-L5 (REFEREE: «16 of its 63 5-windows», «(j = 1, …, 5)») + W-2 (b) (REFEREE-2: «at levels j = 1, …, 5 (unit = j-window;
  set = all 119 of them)») + TF-3 (REFEREE: unit (5-window, PULSE or GAP)); same old string in both reports.
  - M3 I-FUEL: TF-L3 (REFEREE: «at some state s among s_(a−1), …, s_(e−1) of the window [a, e]», «at no such state in any of the other
  79», the movers 12 and 13) + W-2 (c) (REFEREE-2: «do not have exactly one move of each member of pair 6 (crossed onto movers 22, 11)»,
  «at every such state in 16 of them»); same old string.
  - M4 corpus: W-4 (a) (REFEREE-2; new copied from its report: the 15 + 7 + 2 runs, «62 doubling (run, level) pairs»).
  - M5 DOUBLE-EQ: TF-L1 (REFEREE: 7,069 per (step, doubling level), 757 j-windows, 61 levels with F(j − 1) ≥ 1) + W-4 (b) (REFEREE-2:
  «on 7,069 (step, doubling level) units for its first two clauses, on the 757 j-windows for the third and on the 62 doubling (run,
  level) pairs for the fourth»); same old string.
  - M6 DOMINANCE-FREEZE: TF-L2 (REFEREE; new copied from its report) — it contains W-4 (c)'s fact (REFEREE-2: unit (consecutive-state,
  mover), «with equal deciders»), whose old string is a substring of TF-L2's.
  - M7 CROSS-ECONOMY chains: TF-L4 (REFEREE, optional, taken: one phrase; old and new copied from its report).
- p_tower_check.py (extended; it still pins L-1 and now pins L-2) prints and asserts every unit L-2 names: E3 units 7,069, E5 hypothesis
  levels 61 of 62, 119 j-windows at j = 1..5, 16 distinct 5-windows, decider scopes 48 / 32 / 16 / 0, 188 of 188, plus all old counters.

### 6. Description slip (REFEREE, REFEREE-2)
- «Packet-description slip (Lead 14:36Z): the packet's report and the brief gave L-1 as «3,699 bytes»; it is 3,699 characters = 3,834
  bytes (sha1 binds).» L-2 above is given in bytes and characters.

## Fixes entry 2 (2026-11-07, L-LOWER successor 7; fix round 2; written by experiments/lower/l5/mkfix2_tf.py)
Report answered: CHECKER C134 claude/checker 23871f4806e2670ccfb04d32fc8664e8ede9bc04, docs/checker/C134.md (landing check of RESULTS
  R120, first fill: FAIL E-1 to E-4; exact line L-3 in its §5), routed by the Lead 18:28Z. Verdict sentence: «All four are the drafter's
  flags with its exact strings: G-1 (R-B), G-7 (R-G), G-U (R-U) and G-9 (i) (R-S). The Lead ruled R-B and R-G (Lead reading) and
  recommended R-U and R-S; I take all four. R-C is not taken (N-1). No statement, proof, definition or instance changes.» Every «…»
  below is copied by the script from a byte copy of C134.md (wrapped lines joined by single spaces). The packet (frozen at 7f7ff6f5),
  L-1, L-2 and fixes entry 1 are unchanged; no statement, proof, definition, instance or counter changes.

### 1. The four findings (CHECKER C134 §3)
- E-1 (G-1, source note; the C122 E-3 / C132 E-2 / C133 E-2 class). «The note «(P-TOWER-FUEL, docs/lower/P-TOWER-FUEL.md; L-LOWER
  successor 5)» names only the packet. Fixes entry 1 (L-LOWER successor 6) carries the proof of record of CROSS-ECONOMY's sign-change
  clause (§1, REFEREE's repair; the packet's step is false: REFEREE 57 of 86 RANK states, REFEREE-2 651 of 1,010), and the measured
  I-ROOM unit (§2) and I-FUEL scopes (§3) that L-2's instance clauses state. Fix: R1 (R-B).»
- E-2 (G-7, L41; Lead ruling). «That proof of record is REFEREE's text (R-P-TOWER-FUEL §3, l. 107-112, read), signed by REFEREE (§C l.
  251-252) and checked by REFEREE-2 after its own independent repair (Add. 1 «The proof of record (REFEREE's) is correct.»). L41
  requires the scope tail to say so; L-2 has «referee» 0 times. Fix: R2 (R-G).»
- E-3 (G-U, scope-tail wording; my ruling on the UPDATE procedure). «L-2's tail reads «not M3, not a gauntlet step, not a TARGET.md
  claim»; every landed line R90-R119 except R112 reads «not M3, not a step-4 pass, not a TARGET.md claim» (the drafter's script on the
  titles; «gauntlet» 0 times there). R105's procedure (sentinel_build, which L-2's «(DATA: » form requires) asserts the landed words, so
  as written it applies only with a reading. With R3, L-3 has the landed words and R105's procedure applies unchanged. The meaning is
  the same: both referees' TARGET diffs say the scope with «not a gauntlet step» (REFEREE §7, REFEREE-2 l. 163) and «step-4 pass» names
  the same gauntlet step. Fix: R3 (R-U), applied after R2 (R2's new text carries the only occurrence).»
- E-4 (G-9 (i), set per clause; the C130 E-3 / C132 E-5 class). «I-FUEL's «meets PULSE, GAP ≥ 7 − j at levels 1-5» names no unit and no
  set, where I-ROOM's clause names «(unit = j-window; set = all 119 of them)». p_tower_check.py tests it (slack on SL41 at need 7 − j,
  asserted 0) but counts windows for G7_best_d28 only. My instrumented copy (below) gives SL41_d28 119 j-windows at j = 1..5 (3, 7, 15,
  31, 63). Fix: R4 (R-S).»
- N-1 (R-C not taken). «GAP-NEST's capped form «so with levels 0, …, h − 1 capped (F(l) = 2^(l+2) − 2) PULSE and GAP are ≥ h − j for 1 ≤
  j ≤ h − 2» is a consequence the counters cover: on such a run levels 1, …, h − 1 are doubling, so the counters' k at j ≤ h − 2 is ≥ h
  − 1 − j and PN, GN test PULSE, GAP ≥ k + 1 ≥ h − j. The R119 precedent («so R(y) ≥ moves(y)», covered) was not an E-item (C133).»

### 2. The replacements (C134 §5, applied to L-2 in this order)
- R1 (E-1): old « (P-TOWER-FUEL, docs/lower/P-TOWER-FUEL.md; L-LOWER successor 5)» → new « (P-TOWER-FUEL, docs/lower/P-TOWER-FUEL.md
  with its fixes entry 1, docs/lower/P-TOWER-FUEL-fixes.md; L-LOWER successors 5-6)»
- R2 (E-2): old «; G-N5-TIME stays OPEN; not M3, not a gauntlet step» → new «; the proof of record of CROSS-ECONOMY's sign-change clause
  is referee-originated (REFEREE R-P-TOWER-FUEL §3, restated in P-TOWER-FUEL's fixes entry 1 §1; REFEREE-2's own repair is a second
  route), signed by both referees; G-N5-TIME stays OPEN; not M3, not a gauntlet step»
- R3 (E-3): old «not a gauntlet step» → new «not a step-4 pass»
- R4 (E-4): old «meets PULSE, GAP ≥ 7 − j at levels 1-5 while» → new «meets PULSE, GAP ≥ 7 − j at levels 1-5 (unit = j-window; set = all
  119 of them) while»
- C134 §5 rule: «In the strings above, a wrapped line is joined to the next with one space.» R3 is applied after R2: its old string then
  occurs once, inside R2's new text (asserted).

### 3. Line L-3 (docs/lower/P-TOWER-FUEL-line-L3.txt; made by experiments/lower/l5/mkL3_tf.py)
- sha1 7328e67345e1bb6a8605ccfa4f406d1020eabfdb, 4908 bytes, 4758 characters, 1 line + «\n»; 82 «(» / 82 «)», depth never negative; no
  «|»; «gauntlet» 0 times. It equals CHECKER C134's target byte for byte: «L-3 with R1-R4 (my script): sha1
  7328e67345e1bb6a8605ccfa4f406d1020eabfdb with its newline (4,908 bytes), one line, 82 «(» / 82 «)», depth never negative, 0 "|", one «
  — », «gauntlet» 0 times.» (mkL3_tf.py asserts the sha1 and the byte count it reads from C134 §5).
- p_tower_check.py (extended; it still pins L-1 and L-2) now pins L-3 and asserts the set of R4's clause on SL41_d28: 119 j-windows at j
  = 1..5, (3, 7, 15, 31, 63) per level, the same counts as C134 §3 E-4 (its instrumented copy), here from the lane's own windows(j). No
  other counter changes.
