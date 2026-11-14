# R188 A Ξ-counter inside IDEAL-ACYC: none found. exact z3 bounds on LADDERBF's 2-wide ladder: d 2 max 4, d 3 max 8 EXACT (relaxation L 9 UNSAT), versus TB ceilings 8 / 22; climbs d 4 ≥ 12, d 5 ≥ 18; middle-level moves flat (7 / 9 / 9 at d 4 / 6 / 8); box 139 up-recipe 2d − 1; no doubling anywhere (L-RED successor 44)
Started 2026-11-01 23:32Z (Lead GO R188 = (a)). Labels: EXACT (z3, machine-checked, not Lean), DATA, READING. G-N5-TIME OPEN. No kill.
Final note (02:0xZ). The d 4 L 12 / 13 relaxation runs (started ~00:08Z, timeout 7000 s) were still going at this commit; their outcome is added below when they end.

## Status
| d | IDEAL-ACYC max on the 2-wide deg-2 ladder | how | TB ceiling (LADDERBF) |
| --- | --- | --- | --- |
| 2 | 4 | EXACT: bmc3 L 4 SAT, L 5 UNSAT (as R180) | 8 |
| 3 | 8 | EXACT: run of 8 (bmcrel SAT, then bmc3 with that structure fixed SAT, fastabs replay 8); relaxation L 9 UNSAT (and L 10) | 22 |
| 4 | ≥ 12 | DATA: grow.py (new top level on the d 3 solution, 300k mutations) | 52 |
| 5 | ≥ 18 | DATA: grow.py on the d 4 champion | 114 |
- bmcrel.py relaxes β-weights to free integers. Every IDEAL-ACYC ladder instance is an instance of it, so its UNSAT is an upper bound.
- Moves per level: d 3 exact 2, 4, 7; d 4 2, 4, 7, 8; d 5 2, 4, 8, 7, 8. The top levels stop doubling.
- Pins (experiments/red/r188/instances): x3_L8_n48 (d 3, L_FL 8), g4_L12_n62 (d 4, L_FL 12). Both are realised with the R187 gadgets
  (realck: FAITHFUL = IDEAL, states equal) and pass startck, Oink --zlk + verify, --tl + verify and xeng.
- READING (mechanism a counter needs): two vertices at a level that both switch after a lower key flip must move at DIFFERENT
  steps (lag), so that their key order flips twice and the level above can move twice. In the DOWN class lag is impossible (CASC-M″),
  and a lagging vertex whose two options read the same target has a static Ξ order. So every level needs a pair of Ξ-targets that
  leapfrog once per lower carry.
- L-NEW box 139 recipe (Lead 00:02Z: Ξ-targets UP the ladder, lower-level faces dominant), upclimb.py, 200k mutations, d 3 / 4 / 5:
  - as stated (lower level more significant): T = 1 at every d. Obstruction (READING, immediate): x's two option values contain x's own
    two β's, which are then the most significant vertices of the symmetric difference, so x's Ξ order is static and x moves ≤ 1 time.
  - inverted (UPDOM=1, upper level more significant, so x's own faces are least significant): T = 5 / 7 / 9 = 2d − 1, below the
    unrestricted ACYC climbs (8 / 12 / 18). Every up-class instance is an ACYC ladder instance, so at d 3 it is ≤ 8 anyway.
- L-NEW box 140 score (Lead 01:24Z: moves at the MIDDLE level against d, the middle-out counter), midclimb.py, ACYC W 2 deg 2,
  150k mutations, 10 restarts: middle-level moves 7 / 9 / 9 at d 4 / 6 / 8 (runs 9 / 13 / 11). Flat: no middle-out counter found by search.

## Answer (for the Lead and L-NEW 47)
- No compounding found in IDEAL-ACYC: exact maxima 4, 8 at d 2, 3 (TB ceilings 8, 22); climbs grow by about 4-6 per level; top and
  middle levels stop near 8-9 moves.
- No obstruction lemma proved here. The exact small-d data and the immediate own-face-dominance obstruction (up-recipe as stated) are
  what I can give; the lag mechanism (READING above) is the shape a counter must realise at every level.
- Next (queue): bmcrel at d 4 with L 13 (and d 5 when d 4 settles) to extend the exact sequence; score by moves at the middle level in
  the exact model; (a′) the box 137 lap recipe.
- d 4 relaxation runs: bmcrel 4 12 and 4 13 both stopped UNDECIDED at the 7000 s timeout (02:06Z). So d 4 has no exact value: ≥ 12 (climb) only.
