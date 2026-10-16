# R10: the CARRY step for DTL, two-level reset+replay (L-RED, box 2026-10-16 08:12Z-16:10Z; produced on Opus 5.5)
Candidate: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7. Status words: DATA / READING / OPEN.

## Interim 1 (~09:30Z)
- DATA: the fast level works alone. experiments/red/carry/bsolo.py mB mA builds a chain b_1..b_mB that a cut (seed s,
  threshold above the chain) eats at a rate of one tangle per search. Each b_i's tangle carries private witnesses g_{i,j}
  (Even, pr 0, -> b_i). bsolo 4 2: 4 Even searches, one tangle each, plus the closing search
  (`python3 experiments/dtl/../red/dtl/dtl_flipflop.py` on the output; Oink MATCH: 2 dominions, 4 tangles, 7 iterations).
- READING (redundancy): in one best_vertices call, a stored tangle whose top is still in V adds nothing to the threshold
  attractor: plain attraction from the top rebuilds it once its escapes are covered. A tangle can change a pruning round
  only (i) after its top has been pruned, or (ii) by being lifted into a HIGHER top's region, where it covers vertices of
  priority between its top and that top (cap effect). This is why a deep-learned carry driver is hard to use in piece 0.
- First 2-level wiring (experiments/red/carry/carry2.py): the slow chain is eaten by an earlier cut (seed sA); eating a_j
  also eats the witnesses g_{.,j}, which kills every fast tangle of the old state (f1). The carry gate is an Even vertex
  p1_k that a high "stealer" top sigma takes while the fast level is unfinished, so the carry tangle has NO gate escape.
  First run (carry2 2 3): FAILS for a design reason. sigma's high cap pulls almost the whole game into its region at
  piece 0, so piece 0 is stable and nothing is counted. Next step: confine the stealer so its region holds only the
  p1's (lower its cap, or block the Even back-paths a_k -> p1_k).
