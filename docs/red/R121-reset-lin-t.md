# R121: RESET-LIN-T (matched resets counted only at targets of switching edges) is false by the same observer plus ONE switch into it: #MAT = K(m − 1) at a switch target AND at the switching vertex itself, in one λ-run (248 > n = 233 at K = 8). DATA + READING; CARRY-SEG(-T) untouched
L-RED successor 30 (Opus 5.5; D1/D18; Lead 21:05Z target (1): "RESET-LIN-T: matched resets per vertex per λ-run, counted only at
targets of switching edges (the vertices R86 (c) and COMPOSE-FREEZE actually sum over). Also CARRY-SEG-T."). Written 2026-10-29 from
21:20Z (date -u). Labels: DATA / READING / OPEN / DEAD. Not a TARGET.md claim. Builds on R120 (wave observer o on mkr).

## 1. The device (DATA)
- obs2.py with TARGET=1 adds to R120's game:
  - an Even vertex e (priority 0, no in-edges) with edges {o, d};
  - d (Odd, single successor z), with priority Z, an odd marker just above z.
- The start sets σ(e) = d. Ξ(o) is far better than Ξ(d) and both end at z. So at the first transition e switches to o (traced:
  σ(e) = d at t = 0, o from t = 1 on), λ does not change, and the σ-run is otherwise mkr's.
- Now o is the TARGET of a switching edge inside the λ-run, and e is a SWITCHING vertex whose valuation copies o's from t = 1 on.
- Counts (matc.py with TARGETS=1: only vertices that are the target of an Even switching edge inside the λ-run are counted):
  | K | m | n | states | λ-runs | max #MAT over switch targets (vertex o) | / n |
  | --- | --- | --- | --- | --- | --- | --- |
  | 4 | 16 | 121 | 77 | 2 | 60 | 0.496 |
  | 8 | 32 | 233 | 281 | 2 | 248 | 1.064 |
  | 12 | 48 | 345 | 613 | 2 | 564 | 1.635 |
  The counts are R120's K(m − 1). The switching vertex e has the same count: 248 at K = 8 (independent counter).
- Checks at K = 8:
  - xeng.py: n5b = n5.py, state sequences identical.
  - Oink zlk OK, strategies verified.
  - L-NEW n5x + L-SI compose.matched: o 248, e 248.
- Pin: experiments/red/mix/instances/tobs_K8_m32.pg 80dd7685be50, .start 6e6c0547ebf2. check.sh gate (regenerates the pin; K = 4
  target count 60).

## 2. Reading
- DEAD as stated: RESET-LIN-T. Also dead: the "switching vertices" restriction (R120 §2's suggestion), by the vertex e.
- One switch costs one vertex. After it, the target's (and the switcher's) whole later P-history in the λ-run is counted, and an
  observer's history can be as long as the run. So any restriction by "this vertex switched / was switched to at some point of the
  λ-run" is reader-inflatable.
- A restriction that could survive must charge a P-change to a SWITCH EVENT near it in time. Examples:
  - only the P-changes of w between the switch into w and the next change of the switcher;
  - or count switches and bound P-changes per switch.
  R86 (c)'s sum is over (switching edge, λ-run) pairs of the target's rises. If its proof only uses rises of U(e) inside the window of
  a re-entry (box 33 RE-CHARGE), then the window form is what is needed, and the observer is harmless there: o is entered once, so it
  has one window. OPEN: L-SI should state the window form; I will attack that next if routed.
- CARRY-SEG-T (carries between matched resets at targets) is not killed here. The observer o has about K carries. The Even switching
  observer of R120 §3 has bursts of m < n − 1.

## DONE / FINDINGS / NEEDS
- DONE: obs2.py TARGET=1; matc.py TARGETS=1; pin tobs_K8_m32; check.sh gate; two engines, Oink, second counter at K = 8.
- FINDINGS:
  1. DATA: switch-target #MAT = K(m − 1) in one λ-run (248 > n at K = 8). RESET-LIN-T DEAD, and the switching-vertex form too.
  2. READING: "the vertex switched / was switched to" does not stop observers. A surviving law must be per switch window.
- NEEDS: none from the owner.
