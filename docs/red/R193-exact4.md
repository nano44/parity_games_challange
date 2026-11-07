# R193 Exact d = 4 on the 2-wide degree-2 IDEAL-ACYC ladder: a faster exact encoding (bmc3 + redundant clauses from proved lemmas) re-decides d 3 in seconds (L 8 SAT 3 min, L 9 UNSAT 11 s; R188's relaxation needed ~40 min); d 4: max ≥ 12 stays the best bound (L 13 / L 14 exact UNDECIDED at their caps; the relaxation is SAT at L 13 but its structure does not lift) (L-RED successor 46)
Started 2026-11-02 13:50Z (queue item «exact d = 4 (better encoding)», R188 RESUME POINT (1); date -u). Labels: EXACT (z3, machine-
checked, not Lean), DATA, OPEN. Model: R188 / LADDERBF (2-wide, degree 2, option k of a level-l ≥ 1 mover has W-target 2(l − 1) + k),
r188/bmc3.py semantics (fastabs: acyclic Ξ via positions, face value = signed 2^rank sum along the chain), every IDEAL-ACYC genome a real
N5 FL run by RESULTS R104. Not a TARGET.md claim. G-N5-TIME OPEN.

## 0. Answer
- r193/bmc4.py = r188/bmc3.py (same variables, same symmetry breaking) + three families of REDUNDANT clauses, each a proved lane lemma
  that holds on every IDEAL-ACYC run, so no answer changes:
  - Ξ-reachability reach[x][y] (the closure equation over the Ξ-targets; one solution since the Ξ-graph is acyclic);
  - R189 Corollary RE-REVERSAL (degree 2): between two consecutive moves of x at steps t1 < t2, some y with reach[x][y] moves at a
    step in [t1, t2 − 1] (= R191 ROT-CAP at D = 2);
  - R178 XI-NEW (as used in box 144 CHAIN-BACK): if x moves at step t ≥ 2 and no mover of a lower level moves at t, some y with
    reach[x][y] moved at step t − 1.
- d 3 (re-decided, EXACT): L 8 SAT in 181 s (replay 8, stuck), L 9 UNSAT in 11 s. Same answer as R188 (max 8), which needed bmcrel
  (relaxation) ~40 min for L 9. REL=1 (free distinct integer weights + the same clauses): L 9 UNSAT in seconds.
- d 4 (final):
  - exact L 13: UNDECIDED at 7000 s (lemma clauses) and at 9000 s (lemma clauses + R189 Corollary LAG, LAG=1; sanity of LAG at d 3:
    L 8 SAT, replay 8; L 9 UNSAT); exact L 14: UNDECIDED at 9000 s.
  - relaxation (free distinct integer weights + clauses) L 13: SAT (5726 s; with LAG 4185 s; rerun with model dump 3384 s). A
    relaxation SAT gives no bound.
  - lift (R188's route: the relaxation's Ξ-targets, gates and start fixed in the exact model, ranks / parities free): UNSAT in 10 s.
    So that 13-step relaxed structure is not a real run; a second relaxation model (no LAG) does not lift either (UNSAT, 12 s).
    This rules out two structures, not L 13. (The route works at d 3: relaxation
    model → fixed exact SAT, replay 8.)
  - Bound unchanged: 12 ≤ max(d 4) (R188 pin g4_L12); no upper bound.

## 1. Runs (container-local logs in r193/out; 4 cores shared)

| run | encoding | result | time |
| --- | --- | --- | --- |
| d 3, L 8 | bmc4 exact | SAT (replay 8) | 181 s |
| d 3, L 9 | bmc4 exact | UNSAT | 11 s |
| d 3, L 9 | bmc4 REL | UNSAT | < 60 s |
| d 4, L 12 | bmc4 exact | stopped at 5313 s (redundant: R188 pin g4_L12 is a 12-step run) | — |
| d 4, L 13 | bmc4 exact | timeout | 7000 s |
| d 4, L 13 | bmc4 REL | SAT | 5726 s |
| d 4, L 13 | bmc4 REL + LAG | SAT (rerun with dump: 3384 s) | 4185 s |
| d 4, L 13 | bmc4 exact + LAG | UNDECIDED (cap) | 9000 s |
| d 4, L 14 | bmc4 exact | UNDECIDED (cap) | 9000 s |
| d 4, L 13 | exact, FIX = the REL + LAG structure | UNSAT | 10 s |
| d 4, L 13 | bmc4 REL (no LAG), rerun with dump | SAT | 5391 s |
| d 4, L 13 | exact, FIX = that second structure | UNSAT | 12 s |

## 2. The same clauses on R191's NEST question
- r191/nestbmc.py LEM=1 (reach, ROT-CAP at degree D, XI-NEW) + PIFIX: NEST(3) at degree 3, prefix 6 SAT in 223 s (exact); prefix 7
  timeout 5000 s. R191 Proposition NEST-DEAD-3 (PROVED, lane) says prefix 7 is UNSAT; z3 has not confirmed it.

## 3. Files
experiments/red/r193/bmc4.py (LEM=1 default; LAG=1 adds Corollary LAG; REL=1 relaxation, writes the model as a FIX file; FIX=file fixes
Ξ-targets, gates and start). Outputs in r193/out (gitignored).
