# L9: level 8 at d 32 (BOX L9, L-LOWER successor 9; GO from the Lead 02:06Z 2026-11-08)
Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING. Model and notation as docs/lower/L7-design.md §0 and L8-design.md §0
(R104 IDEAL rules; pair j = movers 2j, 2j + 1; c_j = o(j − 1); j-window = maximal run of steps with c_j constant).

## 0. Instances and tools (experiments/lower/l9/)
- HIT7: frozen copy rec/LCOMP_L6_HIT7_F254_d28.txt, sha1 6a3b274d3af4d0d8f057f82c8f2919c84b7dd446 (= L8 §1g copy, = relayed);
  lifted to d 32 by lift.py (4 inert top pairs: options to the exit, ranks 112-127, constant preference = start) as
  rec/HIT7_lift_d32.txt, sha1 c76bd8c90824b52db36a801af7e8d9e2fa63c92f: T 299, F identical on levels 0-27, 0 on 28-31.
- fenc.c: a second simulator for any d ≤ 64. It decides each preference by ENC (the option of largest rank in chain(x, 0) △
  chain(x, 1)) and needs no big integers, so it is independent of sim6.py (Python big-integer sums). It agrees with sim6 and fev on
  HIT7, SL41, H6 (T and the whole F-profile, and MV).
- DATA (out/fev_vs_fenc_d32.out; unit = genome; set = 1): l5/fev.c is NOT valid at d ≥ 32. It sums ±2^rank in a signed __int128,
  and rank 127 overflows. On HIT7_lift_d32 fev reports F(31) = 1, while sim6 and fenc report 0: inert mover 63's rank-127 option
  is read as negative. From d 32 on, the two lane simulators are sim6.py and fenc.c.
  L-COMP's rclimb30.c uses 192-bit values (claude/l-comp, box30), which is not affected.
- win6.py (6-window move profile), gaps.py (o(l)-gap histograms), slack.py (PULSE-NEST / GAP-NEST room conditions for H capped levels).

## 1. What an 8th capped level needs, measured on HIT7 (PROVED part + DATA)
- PROVED (P-TOWER-FUEL Lemmas 2, 3, PULSE-NEST and GAP-NEST, with h = 8; WINDOW-CAP, L7 §2). With levels 0-7 capped:
  - every j-window has PULSE ≥ 8 − j and GAP ≥ 8 − j (1 ≤ j ≤ 6);
  - every gap between consecutive changes of o(6) (and the first and the last) is ≥ 2, so T ≥ 2·255 = 510.
  The §4 recipe of L8 («keep movers 0-13, HIT7's run plus PULSE_6 = 2», T ≈ 299 + 127) checks only the PULSE half at j = 6. It
  misses GAP at j = 6, and both conditions at j = 4, 5.
- DATA (slack.py, gaps.py; unit = j-window, or o(6)-gap; set = all windows; scope = stored start; out/slack8_HIT7.out, gaps_HIT7.out):
  | j | need (8 − j) | windows | PULSE < need | GAP < need | PULSE values | GAP values |
  | --- | --- | --- | --- | --- | --- | --- |
  | 1-3 | 7, 6, 5 | 3, 7, 15 | 0 | 0 | | |
  | 4 | 4 | 31 | 15 | 0 | 3 (15), 4 (8), 5 (8) | 5 (11), 6 (19) |
  | 5 | 3 | 63 | 63 | 27 | 2 (63) | 2 (27), 3 (27), 4 (8) |
  | 6 | 2 | 127 | 127 | 90 | 1 (127) | 1 (90), 2 (27), 3 (9) |
  HIT7's 6-windows (o(5)-gaps; o(5) is a function of pairs 0-5 only) have lengths 2 (91), 3 (27), 4 (9), summing to 299. Each
  6-window holds two o(6) changes, and these must be ≥ 2 steps apart, also across window boundaries. So the 6-windows average
  ≥ 4 steps, and the run of pairs 0-5 itself must be stretched from 299 to ≥ 510 steps.
- Exact obstruction to L8 §4 as written (PROVED by the counting above). No construction that keeps HIT7's trajectory of movers 0-11
  (with any change at levels ≥ 6) reaches F(7) = 510. At least 211 steps must be inserted into the run of pairs 0-5. At each
  inserted step a free lower mover must hold although under the same pair-0-5 state it moved in HIT7, so its chain must read a
  mover (necessarily of level ≥ 7) that changes at that step. That is §1d's need (i), now at levels 4, 5 and 6.
- The same pattern one level down (DATA, out/slack7_H6.out, slack7_SL41.out; same units). H6 (6 caps) against seven levels:
  - j = 4: 15 PULSE violations; j = 5: 63 PULSE and 9 GAP violations. So 7 caps could not be added to H6 directly.
  - SL41 (L-LOWER 5's room climb from G7_best, P-TOWER-FUEL §4 «I-FUEL») has 0 violations at j = 1-5, and HIT7 descends from it.
  READING: the 7th level came in two stages, ROOM (re-time the lower levels until Lemmas 2, 3 hold) then FUEL (the triggers of
  pair 6, L8 §1g). The 8th needs the same two stages, with a larger ROOM deficit: 322 violations at j = 4-6, against 87 at j = 4-5
  for H6 → 7.

## 9. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class. All are about the IDEAL
model's step sequence on 𝓛^R_d and its F-profile. Not M3, not a step-4 pass, not a TARGET.md claim.
