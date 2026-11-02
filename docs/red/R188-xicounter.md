# R188 A Ξ-counter inside IDEAL-ACYC (IN PROGRESS, interim): exact z3 bounds on LADDERBF's 2-wide ladder: d 2 max 4, d 3 max 8 or 9 (≤ 9 PROVED by solver, relaxation), versus TB ceilings 8 / 22; climbs d 4 ≥ 12, d 5 ≥ 18; no doubling (L-RED successor 44)
Started 2026-11-01 23:32Z (Lead GO R188 = (a)). Labels: EXACT (z3, machine-checked, not Lean), DATA, READING. G-N5-TIME OPEN. No kill.
Interim note, written while the d 3 L 9 and d 4 L 12 / 13 solver runs are going; the final note replaces this one.

## Status
| d | IDEAL-ACYC max on the 2-wide deg-2 ladder | how | TB ceiling (LADDERBF) |
| --- | --- | --- | --- |
| 2 | 4 | EXACT: bmc3 L 4 SAT, L 5 UNSAT (as R180) | 8 |
| 3 | 8 or 9 | EXACT: run of 8 (bmcrel SAT, then bmc3 with that structure fixed SAT, fastabs replay 8); relaxation L 10 UNSAT | 22 |
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
