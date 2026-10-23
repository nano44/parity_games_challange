# Draft RESULTS DE31-DE32 (Lead, 2026-10-23 19:42Z by date -u) — awaits CHECKER C24 (re-runs at the exact commit, statement diff)

- DE31 (2026-10-23): N9a = the fixed-level Sherali-Adams lift SA+_k of the 0-1 program ACYC for the query "Even wins every vertex"
  (L-NEW successor 7, box 18, (c) lane under D14/D15; docs/new/N9-screen.md §1; l-new 67884f3, eb4d33c; Lemma A (§1, PROVED by the lane,
  unrefereed): integral ACYC is feasible iff Even wins every vertex) is a DEAD END at gauntlet step 2 (incorrect answers, DATA): for
  each k ≤ 3 the level-k lift is feasible (answer "Even wins every vertex") on one-player games that Odd wins everywhere. Family
  circ(n,1,2) (every vertex Even's, every priority 1, edges v → v+1, v+2 mod n); least exact level k* = ceil(n/3) for n = 3..11
  (formula written before the n = 10, 11 runs, experiments/new/sa/results/circ12_sym_prediction.txt); wrong instances
  instances/circ12_n7.pg (k = 2, sha1 4a1973a88a1311966ef5d2f5382221aef3d09c3e) and circ12_n10.pg (k = 3, sha1
  5683b4e48a53988a71ca5eae386a4a03f8a08e27), Oink zlk: Odd wins every vertex; gaps survive tightening the strict constraints to +1.05
  (robust.py). Solver: scipy/HiGHS (infeasible verdicts by IPM; dual simplex agrees for n ≤ 8). Lead re-run (twoout.py circ 3 9 4 1 2
  --sym, scipy 1.18.1): k* = 1, 2, 2, 2, 3, 3, 3 for n = 3..9 (= ceil(n/3), = lane). READING (not proved): k* is unbounded on this
  family, so no fixed level is exact. Scope: this kills SA+_k of this encoding (ACYC), whose level 1 is already inexact on one-player
  games; it says nothing about lifts of other encodings.
- DE32 (2026-10-23): N9b = certified LP-guided peeling (round the level-1 lift of the region program REGION, certify the rounded
  strategy by a one-player solve, remove its attractor, repeat; sound by construction, at most n rounds; docs/new/N9-screen.md §2) is a
  DEAD END at gauntlet step 2 (incomplete: STUCK, no answer): stuck on 6 of 300 and 57 of 2,000 random games and on counter_symsi
  N = 2, 3; every game it solves agrees with Zielonka. Smallest: instances/peel_r1147.pg (n = 5, sha1
  68a8c41b926e2fd324b196c99c4c61ea6d2a91ed; Odd wins every vertex): STUCK after 1 round with 5 vertices left. Obstruction (lane, §2(f)):
  on peel_r26 (n = 6) the LP value equals |W_Odd| = 6 yet the rounded strategy wins nowhere, because the LP optimum is a mixture of
  strategies, so no rounding threshold helps (READING); on peel_r90 the outcome depends on which optimal vertex HiGHS returns.
  Not tested (lane, §2(f)): higher levels; rounding by conditioning. Lead re-run (peel.py instances/peel_r1147.pg): "STUCK after 1 rounds, 5
  vertices left"; Oink zlk: Odd wins all 5 vertices.
