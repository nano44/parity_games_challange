# R214 MOVES-2D under attack (L-RED successor 52)
Started 2026-11-06 18:3xZ (date -u). Lead BOX R214 (CONJECTURE MOVES-2D, L-NEW box 181/185: «every mover moves ≤ 2d times in a run of
𝓛^R_d»). Model: RESULTS R104 IDEAL, 𝓛^R_d of RESULTS R110. Labels: DEAD (verified instance), EXACT-SAT (CaDiCaL 1.9.5 via pysat, one
solver, no proof file), DATA, READING. Not a TARGET.md claim. G-N5-TIME stays OPEN; the kill bounds nothing.

## 0. Answers
- **MOVES-2D is DEAD** (d 6 and d 8, and 7 more records), on L-LOWER 3's instances (claude/l-lower 4d747490, experiments/lower/l3/kill/),
  REPRODUCED with L-RED tools only (§3). Smallest: KILL_M2D_d6_mu13.json (sha1 5301c716…): d 6, T 13, mover 8 (level 4, Ξ-target)
  moves 13 > 2d = 12.
- My own searches did not kill it. Best is a tie at d 5: DENSE(5, 3, 10) is SAT. Witness r214/keep/dense_d5_l3_H10_cert.json (sha1 968ea733…):
  mover 6 (level 3, Ξ-target) moves at all 10 steps of a 10-step run. Certified (§2).
- Exact small-d maxima (EXACT-SAT, horizon T^R(d)): per-level maxima of moves, all movers (Ξ-targets and non-targets):
  - d 3: 1 / 3 / 4 (non-targets: the same).
  - d 4: 1 / 3 / 7 / 7-8 (non-targets: 1 / 3 / 7; top level r 8 UNKNOWN at 1 h).
- Task (1), data: non-Ξ-target movers never exceeded the target maxima at d ≤ 4. No stored genome before L-LOWER 3 (62 JSON, 97 text,
  d 2-8) had a mover above 2d.

## 1. Tools (experiments/red/r214/)
- fa.c: r212/fl.c with env ALLM=1 (SCORE=M scores every mover) and a per-mover table in eval mode (all 2^N starts). Search tool.
- mvck.py: per-mover max moves over all starts by r187/ideal.py. memb.py: 𝓛^R_d membership, condition by condition from R104 / R110.
- certM.py: renumber, best start for mover z, box 150 check, r189/lemck.py, mvck. lowrep.py: stored-start replay, lemck, box 150.
  renum.py: order-preserving gate / β renumbering (lemck needs 0..M−1).
- r200/xcnf.py env MOVEANY=1 (drop «z is a Ξ-target») and MOVENT=1 (force «z is not a Ξ-target»). The default and the MOVEZ query are unchanged.
- scan.sh (exact per-mover scans), dense.sh / run_dense_cubes.sh (DENSE(d, l, H) = move.py d H 2l H; every state is a start, so a
  dense window shifts to step 1), run_top4.sh (d 4 top level, any mover, cubes).

## 2. Exact queries and DENSE
| query | answer | time |
| --- | --- | --- |
| d 3 non-targets, z 0 / 2 / 4 | max 1 / 3 / 4 (r 2 / 4 / 5 UNSAT) | ≤ 262 s |
| d 4 non-targets, z 0 / 2 / 4 | max 1 / 3 / 7 (r 2 / 4 / 8 UNSAT) | ≤ 1,708 s |
| d 4 non-target z 6, r 8 | UNKNOWN (1 h cap); any-mover cubes paused at 202 done | |
| d 4 targets z 2 | max 3 (r 4 UNSAT 3.3 s) | |
| DENSE(5, 3, 9) | SAT, certified (sha1 47d0dc93…) | 2,692 s |
| DENSE(5, 3, 10) | SAT, certified (sha1 968ea733…), 10 = 2d | 530 s |
| DENSE(5, 3, 11), DENSE(4, 3, 8) | UNKNOWN at 2 h; (5, 3, 11) and (5, 4, 11) continue as cubes | |
- Certification (certM): box 150 VIOL 0 / XSIM 0, lemck 0 violations, mvck (all 1,024 starts) and fa agree. The H 10 run ends in
  ideal.py «stuck» (nothing changes), a run end under R104 (Lead 21:07Z).
- L-NEW seeds replayed: box185 h_d5_L4_ld6 (mover 8: 8 moves, T 11), ld4_1 (mover 6: 7); box186 dense_d5_D9 (sha1 5619d2bd…; mover 9: 9, T 9).
- Climbs (fa SCORE=M ALLM=1, d 5-8): d 5 at most 9 moves; d 6 10 (2d 12). Climbs are weak here, as before.

## 3. L-LOWER 3 instances: REPRODUCED (Lead 01:12Z adversary task)
Checks, all L-RED code except the extra box 150 run:
- memb.py: PASS, all 9.
- r187/ideal.py: replay from the stored start.
- fa: all starts, d ≤ 10.
- lemck: on renumbered copies, 0 violations, all 9.
- box 150: VIOL 0 / XSIM 0, all 9.
- r212/modelck.py: d 6 under MOVEZ 8 / MOVEMIN 13 is SAT, so my encoding admits the run.

Every run ends «nothing changes».

| file | d | T (stored = all starts) | max mover (level) | moves | 2d |
| --- | --- | --- | --- | --- | --- |
| KILL_M2D_d6_mu13 | 6 | 13 | 8 (4) | 13 | 12 |
| KILL_M2D_d8_mu21 | 8 | 24 | 15 (7) | 21 | 16 |
| REC_d7_mu17 | 7 | 17 | 8 (4) | 17 | 14 |
| REC_d8_mu24 | 8 | 25 | 8 (4) | 24 | 16 |
| REC_d9_mu29 | 9 | 31 | 15 (7) | 29 | 18 |
| REC_d10_mu32 | 10 | 33 | 15 (7) | 32 | 20 |
| REC_d10_tower_mu30 | 10 | 35 | 8 (4) | 30 | 20 |
| REC_d11_mu40 | 11 | 44 (stored start only) | 15 (7) | 40 | 22 |
| REC_d12_mu42 | 12 | 48 (stored start only) | 15 (7) | 42 | 24 |
- REC_d10_tower: on levels 0-3 the two movers of level l each move 2^(l+1) − 1 times (1, 3, 7, 15), so F = 2, 6, 14, 30. Level 4's
  mover 8 moves 30. READING: R113's per-level doubling is attained on 4 consecutive levels with support levels above. Exact small d
  shows the support matters (level 3 ≤ 8 at d 4).
- RECT_d11_T59 (d 11, T 59): NOT CHECKED, not on claude/l-lower at 4d747490.
- Pins: r214/lower3/pins.sha1 (originals and renumbered copies).

## 4. Support query and T^R table (Lead 01:22Z / 03:25Z)
- Least d for a 15-move level-3 Ξ-target ∈ [6, 10]:
  - d 5: UNSAT within horizon 16 only (1,206 s).
  - d 6 / 7 / 8: UNKNOWN at 2 h.
  - d 10: REC_d10_tower, movers 6 and 7.
  - Any mover: 15 at d 9 (sup_d9_l3_m15, mover 7, non-target).
  - Target-only climbs: 14 at d 8 and d 9.
- Level-4 target climbs: plateau at 28-30. No 31 was found.
- Certified T^R(d) lower bounds (r214/tw single-start climbs, TSC=1; all checked by memb, ideal.py, lemck 0, box 150 VIOL 0; fa over all
  starts where marked): d 8 38 (all), d 9 47 (all), d 10 53 (all), d 11 58, d 12 59, d 13 71, d 14 83. With d 5-7 = 16 / 22 / 26.
  Growth looks linear (about 6.6 per level). The max-T genomes are not towers: a single mover moves at most 8-12 times.
- tw_d9_T40 (a near-tower, F 2, 6, 14, 28) was superseded for T by tw_d9_T47.
