# R2-P-TOWER-FUEL: second-referee report on packet P-TOWER-FUEL (L-LOWER successor 5)
REFEREE-2 successor 31 (Opus 5.5, D1), 2026-11-07 from 14:35Z (date -u). Independent: docs/referee/ not read on this item.

## Object (sha1 of the bytes at claude/l-lower 7f7ff6f587c88fcfc5302905732c975f5e75ce4d, FROZEN)
- docs/lower/P-TOWER-FUEL.md a093e0e7… (14,998 B, 130 lines); line L-1 docs/lower/P-TOWER-FUEL-line-L1.txt 408470ad… = the Lead's pin
  (3,834 B = 3,699 characters, 1 line, 64 «(» = 64 «)», depth never negative, 0 «|»; the Lead's «3,699 B» is the character count);
  experiments/lower/l5/p_tower_check.py 1ed48e10… (155 lines).
- p_tower_check.py re-run on `git archive 7f7ff6f5` (0.8 s): «P-TOWER-FUEL CHECK PASS» (R2-P-TOWER-FUEL/lanecheck_7f7ff6f5.out). Lane code
  was only run, never imported into mine.

## Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §2 | Lemma 0 (MOVE) | **SIGN** (Opus 5.5, D1) |
| §2 | Lemma 1 (DOUBLE-EQ) (E1)-(E5) | **SIGN** (Opus 5.5, D1); N-1 (F(j − 1) ≥ 1 not needed) |
| §2 | Lemma 2 (PULSE-NEST) | **SIGN** (Opus 5.5, D1) |
| §2 | Lemma 3 (GAP-NEST) and its h-capped corollary | **SIGN** (Opus 5.5, D1) |
| §2 | Lemma 4 (DOMINANCE-FREEZE) (a), (b) | **SIGN** (Opus 5.5, D1) |
| §2 | Lemma 5 (CROSS-ECONOMY) (i), (ii) | **SIGN** (Opus 5.5, D1) |
| §2 | Lemma 5 (iii) | **SIGN** (Opus 5.5, D1) on my repaired proof: the packet's proof has a FALSE step (W-1, required) |
| §4 | I-ROOM, I-FUEL counts | re-derived exactly by my own simulator (DATA, not signed); the §4 reading «Lemma 4 (b) is violated in exactly those windows» is false literally (**W-3**, required) |
| §5 | DATA | every counter reproduced exactly by my own code |
| §1 | premises | ✓ all LANDED on trunk, both «…» quotes verbatim |
| §7 | TARGET.md diff | ✓ |
| line | L-1 | **MATCHES after W-2 (a)-(c) and W-4 (a)-(c)** |
Nothing is REFUSED. No statement bounds T; G-N5-TIME stays OPEN.

## Premises (trunk docs/RESULTS.md at origin/claude/vibrant-johnson-nxvvxo 9315f36c; script R2-P-TOWER-FUEL/r2quotes.py, out r2quotes.out)
- R104 (l. 9864, landed): only the model definition is used (A-sets under the old state; least key among the current option and the
  strictly better ones, keys = gate indices of the W-chain under the NEW state, lowest level first; stop rule) ✓. No R104 theorem is used ✓.
- R105 (l. 10155): the ENC quote «the Ξ-order of β-sets … the current value of its Ξ-target» is verbatim, with the «…» elision ✓. Erratum
  E-2 corrects CHAIN-BACK, RANK_t and KEYFLIP's moves(x), not ENC, so it does not bear on this packet ✓.
- R110 (l. 11323): 𝓛^R_d definition («movers 2l and 2l + 1 on level l, all of degree 2, no other movers, option k of a mover of level l ≥ 1
  W-pointing to mover 2(l − 1) + k») ✓. Note E-3 concerns SC-ISO only ✓.
- R113 (l. 12152): the ALIGN quote is verbatim ✓; scope «on acyclic Ξ-graphs» ✓; c_l(s), γ_l(j), flip, F(l) and cv_s(z) are R113's
  notation verbatim ✓. The packet also uses cv (Lemma 5); L-1 omits cv from its notation list (W-2 (a)).
- Not used, as the packet says: R116, R119, lane DOUBLE-EQ′ / PULSE-NEST (re-proved here) ✓. Nothing «signed, not landed» is used ✓.

## Proofs (own re-derivation)
- **Lemma 0.** At degree 2 the A-set is {s_(t−1)(x)} or both options; ALIGN at the state s_t of the run gives KP_(s_t)(x) = c_l(s_t). So x
  moves iff the other option is strictly better under s_(t−1) and c_l(s_t) ≠ s_(t−1)(x), and it moves to c_l(s_t) ✓.
- **Lemma 1.** Non-b-step: 0 movers means no flip; 1 mover gives ΔΦ = 1 ≥ flip; 2 movers come from w = 1 − c (order γ(w)) and go to c
  (order γ(c)), so flip ≤ 1 < 2 ✓. b-step, a = Φ(t − 1): the movers were on c_(t−1) (they leave an option ≠ c_t), the non-movers toggle
  alignment, so Φ(t) = 2 − a − r ✓. I re-checked all six cases of h(a, r) = flip − 2a + 2 − r from the ALIGN order rule:
  (0,0) 2, (0,1) = 1 + flip ≤ 2, (0,2) = flip ≤ 1, (1,0) = 1 (split, c changes, so the order negates), (1,1) = flip − 1 ≤ 0,
  (2,0) = −2 (both on c_t, order γ(c_t) unchanged) ✓. Summing gives F(j) ≤ Φ(0) − Φ(T) + 2F(j − 1). Equality forces (E1), (E2) and
  (E3) ✓. (E2) with (E1) also excludes step 1 from being a j-b-step (Φ(0) = 2 ≠ 0), so the first window starts with Φ = 2 relative to its
  own c ✓. (E4): Φ starts the window at 2 (or 1 after an r = 1 opening step) and must reach 0 by the next b-step or T. Only moves lower
  it, and a member on c cannot move again while c is constant (Lemma 0) ✓. (E5): before the first move both members are on w = 1 − c′;
  the order goes γ(w) → [first = 2j] → γ(c′), and both steps are flips (E3), so γ(w) = γ(c′) ✓.
  **N-1:** since {w, c′} = {0, 1}, one window already gives γ_j(0) = γ_j(1) and fixes the first mover as 2j iff ¬γ_j(0), so the
  hypothesis F(j − 1) ≥ 1 is not needed. The statement as written is true; no change is required. Data: γ_j(0) = γ_j(1) on all 62
  doubling (run, level) pairs, 1 of them with F(j − 1) = 0.
- **Lemma 2.** By (E3) and (E4) at level j, the (j + 1)-b-steps are exactly {u₁(V), u₂(V)}. [u₁(W), u₂(W) − 1] starts at one, contains no
  other and is maximal, so it is a (j + 1)-window ✓. The induction hypothesis at base j + 1 (k − 1) puts its two moves ≥ k apart ✓.
  k = 0 is (E3) with (E4) ✓.
- **Lemma 3.** [u₂(W), u₁(W⁺) − 1] is a (j + 1)-window. Its two pair-(j + 1) moves are distinct and ≥ k apart (Lemma 2 at base j + 1),
  so its length is ≥ k + 1 ✓. Corollary: capped implies doubling, since 2(2^(l+1) − 2) + 2 = 2^(l+2) − 2; take k = h − 1 − j ≥ 1 for
  j ≤ h − 2 ✓.
- **Lemma 4.** chain(x, 0) △ chain(x, 1) contains (x, 0) and (x, 1), because acyclicity keeps x off the other chain, so dec is
  defined ✓. (a) is ENC with distinct ranks: the top term decides the sign ✓. (b): consecutive moves of x lie in consecutive j-windows
  (E4), whose c differ. Lemma 0 then gives π_(s_(t−1))(x) = s_t(x) ≠ s_(t′)(x) = π_(s_(t′−1))(x), and (a) does the rest ✓.
- **Lemma 5 (i), (ii)** ✓ as written: (i) is ENC; in (ii) both moves go to the window's c, and option c is the A_c-side of 2j and the
  A_(1−c)-side of 2j + 1.
- **Lemma 5 (iii): statement true, proof step FALSE.** The proof says «|D_s| ≥ 2^(rank of the top element) > 2·max(|θ_(2j)|, |θ_(2j+1)|)».
  - Both inequalities are false in general. For the first: D = 2^5 − 2^4 = 16 < 2^5. In general D = ±2^r* plus lower terms, so only
    |D| ≥ 1 + Σ_(ranks below r* not in the chains) 2^i follows.
  - Measured on the 1,010 corpus states of the 14 crossed pairs where the RANK hypothesis holds (r2tower.out): |D| < 2^r* at 651, and
    |D| ≤ 2·max|θ| at 5.
  - **Repair (mine).** 2j and 2j + 1 have Ξ-edges to both A_0 and A_1, so acyclicity keeps both chains of A_0, A_1 off pair j. So
    D_s − θ_(2j) = v_s(2j, 0) − v_s(2j, 1) is, by ENC, a signed sum of ±2^rank over the disjoint union {(2j, 0), (2j, 1)} ∪
    (chain(A_0) △ chain(A_1)), all ranks distinct. Under RANK its top term is D_s's top term, so sign(D_s − θ_(2j)) = sign(D_s), and
    likewise for θ_(2j+1). With (ii) this gives the conclusion.
  - Checked pointwise at every state of every crossed pair: 0 violations on 1,010 RANK states, and |D| > max|θ| at all of them.
  - **W-1** below.

## Machine checks (own code: R2-P-TOWER-FUEL/r2tower.py on my R104 simulator R2-P-IDEAL-MOVES/r2moves.py; own text-genome parser)
- Every genome passes my ok_lr (𝓛^R_d, distinct gates and ranks, Ξ-acyclic). Instance sha1s b995fff2…, c1b46c31… ✓; starts equal §4's ✓.
- **I-ROOM** G7_best_d28.
  - T 270, F = 2 6 14 30 62 126 222 158 …; levels 0-5 capped; level 6 not doubling ✓.
  - PULSE, GAP ≥ 7 − j at j = 1..5 (3, 7, 15, 31, 63 windows): 0 violations at levels 1-4; at level 5, 16 pulses and 14 gaps, all of
    length 1 ✓. 15 of the pulses and all 14 gaps are in windows opened by mover 9 moving to option 1; the 16th pulse is the first window ✓.
  - Every one of the 14 gap intervals ends at the next window's opening, so it lies inside the attributed window, and «in the
    5-windows opened by …» is accurate ✓.
  - Level 6: 48 of 127 windows lack exactly one move of each of 12, 13. Profile: 16 with only 12 moving, 16 with only 13, 16 with no
    move, 79 good ✓.
- **I-FUEL** SL41_d28.
  - T 290, the same F(0..7); 0 violations at levels 1-5; 48 of 127 fail at level 6 (same profile) ✓.
  - xt(12, ·) = (22, 11), xt(13, ·) = (11, 22), so the pair is crossed with A_0 = 22, A_1 = 11 ✓. Option 19 = (9, 1) has rank 87, odd
    parity, and xt(11, 1) = 9 ✓.
  - **Decider scope.** dec(12) or dec(13) is option 19 at SOME pre-state s_(a−1), …, s_(e−1) in all 48 failing windows and at no
    pre-state in any of the 79 good ones ✓. That is what p_tower_check.py tests.
  - At EVERY pre-state of the window it holds in only 16 of the 48 (W-2 (c)).
  - Mover 9 sits on option 1 at every pre-state of all 48 failing windows, and also of 17 good ones.
- **§4 reading, false literally (W-3).** «Lemma 4 (b) is violated in exactly those windows by a parked β of the capped pair 4» does not
  hold literally:
  - for every pair of consecutive moves of 12 (94 pairs) and of 13 (94 pairs), dec is NOT constant between them, i.e. the conclusion
    of Lemma 4 (b) holds everywhere (r2fuel.out);
  - level 6 is not doubling, so (b) does not apply in any case;
  - what fails in the 48 windows is the move count (E4).
- **§5 counters, exact** (same units as the packet; 24 runs, 1,999 steps): 62 doubling (run, level) pairs; E3 0 on 7,069 (step, doubling
  level) units; E4 0 on 757; E5 0 on 62; PULSE-NEST 0 on 757, attained on 215; GAP-NEST 0 on 260, attained on 12; DF (a) 0 on 65,885;
  DF (b) 0 on 1,390; CROSS 4 pairs (REC_d10_tower_mu30 level 3, REC_d12_mu42 level 6, REC_d9_mu29 level 6, RECF4_d20_F60 level 3 — the
  packet's four), (ii) 0 on 65 windows, (iii) 43 units, 0 violations ✓.
- **Extra checks** (mine; not in the packet):
  - MOVE iff, on 72,974 (step, mover of level ≥ 1) units: 0 violations;
  - (E1), (E2) directly: 0 violations;
  - DF (a) as the pointwise parity rule, on 77,674 (state, mover) units: 0 violations;
  - CROSS (i), at every state of all 14 crossed pairs (1,098): 0 violations.

## DATA rule on L-1 (clause by clause; counters read in p_tower_check.py l. 104-150)
- MOVE: «no separate DATA» is listed ✓ (my MOVE check above is extra).
- DOUBLE-EQ: «0 violations» names no unit and no count. The four clauses are tested by E3 (unit step × doubling level: two clauses),
  E4 (window) and E5 (doubling level). **W-4 (b).**
- PULSE-NEST «0 on 757 windows, attained on 215» ✓ and GAP-NEST «0 on 260 window pairs, attained on 12» ✓, each in counter units.
- DOMINANCE-FREEZE: the (a) unit is (consecutive-state, mover), not «state pairs». **W-4 (c).** (b) «1,390 consecutive-move pairs» ✓.
- CROSS-ECONOMY «65 windows of 4 crossed doubling pairs, its sign clause on 43» ✓ (43 = windows with RANK at both states).
- Corpus: «24 runs» names no set, and «62 doubling levels» are (run, level) pairs. **W-4 (a).**
- Instances: I-ROOM's «only at level 5» is measured over j = 1..5, but L-1 does not name that range or the unit. **W-2 (b).**
- I-FUEL: «fail» is undefined in L-1, and «is decided by» has no state scope; the measured scope is «at some pre-state». **W-2 (c).**
- The scope tail (not M3, not a gauntlet step, F(6) = 222 not claimed a cap, cyclic and non-𝓛^R genomes not covered, G-N5-TIME OPEN)
  equals §4 «Not claimed» and §7 ✓.

## Required changes
- **W-1 (packet, fixes entry; proof of Lemma 5 (iii)).**
  - Old (§3, spans a line break; the 1-line fragment occurs once): «(iii) Under the RANK hypothesis at s, |D_s| ≥ 2^(rank of the top
    element) > 2·max(|θ_(2j)|, |θ_(2j+1)|) (each θ is a difference of two terms of rank below it), so [D_s > θ_(2j)] = [D_s > θ_(2j+1)] =
    [D_s > 0];»
  - New: «(iii) 2j and 2j + 1 have Ξ-edges to both A_0 and A_1, so by acyclicity no chain of A_0 or A_1 meets pair j, and D_s − θ_(2j) =
    v_s(2j, 0) − v_s(2j, 1) is (ENC) a signed sum of ±2^rank over the disjoint union {(2j, 0), (2j, 1)} ∪ (chain(A_0) △ chain(A_1)) with
    distinct ranks; under the RANK hypothesis its largest-rank term is that of D_s, so sign(D_s − θ_(2j)) = sign(D_s), and likewise for
    θ_(2j+1); so [D_s > θ_(2j)] = [D_s > θ_(2j+1)] = [D_s > 0];»
  - The statement is unchanged.
- **W-3 (packet, fixes entry; §4 I-FUEL).**
  - Old: «So the room conditions are met and the missing piece is fuel: Lemma 4 (b) is violated in exactly those windows by a parked»
    (continuing «β of the capped pair 4.»).
  - Replace by a measured sentence, e.g.: «So the room conditions are met; in the 48 failing windows a member of pair 6 does not move
    while the β of option (9, 1) of the capped pair 4 (mover 9 on option 1 at every pre-state of those windows) decides 12 or 13 at some
    pre-state (READING: the missing piece is fuel). Lemma 4 (b)'s conclusion holds for all 188 consecutive-move pairs of 12 and 13.»
  - Alternatively, label the sentence READING with that counter.
- **L-1** (each old string occurs exactly once; own byte test bt_l1.py, output bt_l1.out):
  - W-2 (a): «with its notation c_l, γ_l, flip, F(l))» → «with its notation c_l, γ_l, flip, F(l) and cv)»
  - W-2 (b): «violates PULSE, GAP ≥ 7 − j only at level 5, 30 times» → «violates PULSE, GAP ≥ 7 − j at levels j = 1, …, 5 (unit = j-window;
    set = all 119 of them) only at level 5, 30 times»
  - W-2 (c): «while 48 of its 127 6-windows fail, in each of which the crossed pair 6 is decided by the option (9, 1) of rank 87 (in none
    of the other 79)» → «while 48 of its 127 6-windows do not have exactly one move of each member of pair 6 (crossed onto movers 22, 11),
    and in each of these 48 windows [a, e] the deciding element dec of mover 12 or 13 is the option (9, 1) of rank 87 at some state
    s_(a−1), …, s_(e−1) (at every such state in 16 of them; at no such state in any of the other 79)»
  - W-4 (a): «on 24 runs from the stored start, 62 doubling levels, 757 j-windows» → «on 24 runs from the stored start (the 15 genomes
    experiments/lower/l3/kill/*.json, the 7 genomes experiments/lower/l4/rec/*.json and the two instances), 62 doubling (run, level)
    pairs, 757 j-windows»
  - W-4 (b): «DOUBLE-EQ 0 violations;» → «DOUBLE-EQ 0 violations on 7,069 (step, doubling level) units for its first two clauses, on the 757
    j-windows for the third and on the 62 doubling (run, level) pairs for the fourth;»
  - W-4 (c): «0 on 65,885 equal-decider state pairs» → «0 on 65,885 (consecutive-state, mover) pairs with equal deciders»
  - L-1 with all six: sha1 1a4e8dcc317d64d691b9b0d8fbfb49fad375cb69, 4,425 B, 1 line, 73 «(» = 73 «)», depth never negative, 0 «|».
  - The lane may phrase these differently if every clause keeps its unit, set, scope and count. The new counts (7,069; 119; 16) are
    mine (r2tower.out); p_tower_check.py would need to print and assert them.
- All other L-1 clauses, diffed against the packet: premises, the window, doubling, PULSE, GAP and dec definitions, MOVE, DOUBLE-EQ (E3)-(E5),
  PULSE-NEST, GAP-NEST and its corollary, DOMINANCE-FREEZE, CROSS-ECONOMY (ii) and (iii) ✓.

## TARGET.md diff
No statement names a parity game's winning region, an algorithm, a running time or a complexity class (TARGET.md §2, §4). All are about
the IDEAL model's step sequence on 𝓛^R_d. Not M3/M4, not a gauntlet step (§5 does not apply); G-N5-TIME OPEN ✓.

## Findings
- F-1: every statement SIGN. MOVE, DOUBLE-EQ, PULSE-NEST, GAP-NEST, DOMINANCE-FREEZE and CROSS-ECONOMY (i), (ii) are proved as written.
- F-2 (W-1): Lemma 5 (iii)'s proof uses a false inequality (|D| ≥ 2^r* fails at 651 of 1,010 RANK states, 2^r* > 2·max|θ| at 5). The
  statement is true by my repair, which holds at 0 violations on the 1,010 states.
- F-3 (W-3): §4's «Lemma 4 (b) is violated in exactly those windows» is false literally (0 of 188 consecutive-move pairs at level 6).
- F-4: I-ROOM, I-FUEL and every §5 counter reproduced exactly by my own simulator. The I-FUEL decider claim holds at some pre-state,
  and at every pre-state in 16 of the 48 windows.
- F-5: L-1 MATCHES after W-2 (a)-(c) and W-4 (a)-(c). The Lead's «3,699 B» is L-1's character count (3,834 B).

## Tools and outputs (docs/referee-2/R2-P-TOWER-FUEL/)
r2tower.py / r2tower.out, r2fuel.py / r2fuel.out, r2quotes.py / r2quotes.out, bt_l1.py / bt_l1.out, lanecheck_7f7ff6f5.out. Re-run
with `git archive 7f7ff6f5 experiments/lower docs/lower | tar -x -C DIR`, then `python3 docs/referee-2/R2-P-TOWER-FUEL/r2tower.py DIR`
(2.4 s).

## Addendum 1: fix round 1 / L-2 (claude/l-lower 740f6c79; REFEREE-2 successor 31, 2026-11-07 15:5xZ by date -u)
- **Object** (sha1 at 740f6c79, equal to the Lead's relay 15:53Z):
  - docs/lower/P-TOWER-FUEL-fixes.md 0902efb9… (9,973 B, entry 1);
  - L-2 docs/lower/P-TOWER-FUEL-line-L2.txt d866ca50… (4,586 B, 4,438 characters, 1 line, 80 «(» = 80 «)», depth never negative, 0 «|»);
  - packet a093e0e7… and L-1 408470ad… unchanged;
  - p_tower_check.py cdba7abc…, re-run on `git archive 740f6c79`: «pins OK: 4 files» (L-1 and L-2 now pinned) and «P-TOWER-FUEL
    CHECK PASS», asserting 7,069 / 61 / 119 / 16 / 32 / 16 / 188 (lanecheck_740f6c79.out).
- **REFEREE's report** docs/referee/R-P-TOWER-FUEL.md (807984e3) was read only now, after my report (4bede4dd) was on origin. It agrees
  with mine on every point:
  - the same false inequality: its 57 of 86 states (pulse pre-states) and my 651 of 1,010 (every RANK state) are different sets; its
    «second held on 86» and my 5 failures elsewhere are consistent;
  - TF-2 = my N-1; TF-4 = my W-3 plus the scope; TF-L1/L2/L3 = my W-4 (b)/(c), W-2 (c); TF-L5 ≈ my W-2 (b);
  - the decider scope table equals my r2tower.out and r2fr1.out.
  - Its point that «and nothing else is required of it there» is a READING is right. I did not flag it; L-1 and L-2 do not carry it.
- **Byte test** (own script bt_l2b.py with the seven replacements written out literally; bt_l2.out): each OLD occurs once in L-1 and each
  NEW once in L-2, and L-1 + M1..M7 == L-2 byte for byte (sha1 d866ca50…) ✓. My predicted 1a4e8dcc… line is superseded by the Lead's
  merge, as stated.
- **Meaning, against my W items:**
  - M1 = my W-2 (a) verbatim ✓.
  - M2 contains my W-2 (b) verbatim, plus the 30's own unit (5-window, PULSE or GAP) and «16 of its 63». My own count: the 30 units lie
    on 16 distinct 5-windows, and 119 j-windows at j = 1..5 (r2fr1.out) ✓. The two «unit =» parentheses bind to different counts (the
    «only» over j-windows, the 30 over (window, condition)); both are right.
  - M3 contains every fact of my W-2 (c): the failure defined as «not exactly one move of each member», the crossing onto 22, 11, the
    «some state s among s_(a−1), …, s_(e−1)» scope, «every such state in 16», and «none of the other 79» ✓. It adds the mover names
    12, 13 (TF-L3). «dec_s(12) or dec_s(13)» at every state is my every-state count of 16 ✓.
  - M4 = my W-4 (a) verbatim ✓.
  - M5 carries my W-4 (b) units and counts (7,069 / 757 / 62) plus «61 of them with F(j − 1) ≥ 1» (TF-L1). My count: F(j − 1) = 0 on
    exactly 1 of the 62 ✓.
  - M6 (TF-L2) contains my W-4 (c) fact (unit (consecutive-state pair, mover), equal deciders) and names (b)'s unit ✓.
  - M7 (TF-L4) is the reading my code uses (chains of the current options) ✓.
- **Fixes entry 1, W-1 = TF-1 (§1):**
  - The proof of record (REFEREE's) is correct. chain(2j, 0) △ chain(2j, 1) = {(2j, 0), (2j, 1)} ∪ (chain(A_0) △ chain(A_1)), by
    acyclicity, with top m* under RANK. By Lemma 4 (a) the sign of D − θ_(2j) is that of m*'s term, which is the sign of D. Likewise for
    2j + 1.
  - It is the same argument as my route, phrased through Lemma 4 (a) instead of ENC directly. The Lead's choice of record is fine with me.
  - My second route and my counts are quoted verbatim (bt_fxq.out) ✓. The statement is unchanged ✓.
- **Fixes entry 1, W-3 = TF-4 (§3):**
  - The new §4 text states the measured scopes: 48 at some pre-state; 32 at s_(a−1); 16 at every pre-state; 0 of 79. My r2fr1.out gives
    the same, and 32 at some s_a … s_e.
  - Mover 9 is on option 1 at every pre-state of the 48 failing windows and of 17 good ones; Lemma 4 (b)'s conclusion holds on 188 of
    188 consecutive-move pairs (my r2fuel.out) ✓.
  - The interpretive clause is labelled READING and says Lemma 4 (b) is not applied ✓. **W-3 met.**
- **§2 TF-3 unit and §4 E5 «61 of 62»** ✓ (my counts). §6, the description slip ✓.
- **Verdict:** fixes entry 1 **CORRECT**; W-1, W-2 (a)-(c), W-3 and W-4 (a)-(c) **met**; **L-2 MATCHES** the packet with fixes entry 1,
  in bytes and in meaning (Opus 5.5, D1). Statement verdicts are unchanged: all SIGN, (iii) on the repaired proof now of record.

## Addendum 2: L-3 for CHECKER C134 (claude/l-lower 4f25ae6f; REFEREE-2 successor 31, 2026-11-07 19:1xZ by date -u)
- **Object** (sha1 at 4f25ae6f, equal to the Lead's relay 19:09Z):
  - L-3 docs/lower/P-TOWER-FUEL-line-L3.txt 7328e673… (4,908 B, 1 line, 82 «(» = 82 «)», depth never negative, 0 «|», one « — »,
    «gauntlet» 0 times);
  - fixes c99bfd3a… (entry 2 appended; entry 1 unchanged); L-2 d866ca50…, L-1 and the packet unchanged.
  - The source of R1-R4 is docs/checker/C134.md §5 at claude/checker 23871f48.
  - p_tower_check.py re-run on `git archive 4f25ae6f`: «pins OK: 5 files», SL41_d28 «119 j-windows at j = 1..5 (3, 7, 15, 31, 63)»,
    «P-TOWER-FUEL CHECK PASS» (lanecheck_4f25ae6f.out).
- **Byte test** (own script bt_l3.py with C134 §5's strings, applied in order; bt_l3.out): R1, R2, R4's old strings occur once in the
  text they are applied to, and R3's once, inside R2's new text. L-2 + R1..R4 == L-3 byte for byte, sha1 7328e67345e1bb6a8605ccfa4f406d1020eabfdb,
  4,908 B (= C134's prediction) ✓.
- **Meaning:**
  - R2 is true and is what my Addendum 1 says. The proof of record of (iii) is REFEREE's: its R-P-TOWER-FUEL §3 l. 107-112 is the
    repaired proof, restated in fixes entry 1 §1. My ENC repair is «an independent second route». Both referees signed (iii) on it; my
    Add. 1 reads «all SIGN, (iii) on the repaired proof now of record» ✓.
  - R4: SL41_d28 has 3 + 7 + 15 + 31 + 63 = 119 j-windows at j = 1..5 (my r2fr1.out «I-FUEL: 119»). Its 0 violations are my
    r2tower.out level 1-5 rows ✓.
  - R3: the packet is not an algorithm claim, so no gauntlet step applies (TARGET.md §5, my TARGET diff). «not a step-4 pass» is
    therefore true. It is the landed wording of R90-R119 (C134 E-3), and both are scope disclaimers of the same kind ✓.
  - R1: the source note now names fixes entry 1, which carries the proof of record and the measured I-ROOM unit and I-FUEL scopes ✓.
- **Verdict:** **L-3 MATCHES** the packet with fixes entries 1-2, in bytes and in meaning (Opus 5.5, D1). Statements all SIGN.
