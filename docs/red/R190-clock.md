# R190 The 3-wide / degree-3 «clock» escape from NEST-DEAD: neither exhibited nor killed exactly (z3 undecided at d 3); climbs scored by L-NEW's U (unchained least-mover steps) and DELSTEPS stay LINEAR in d (U ≈ 3.5 per level at width 3 / degree 3); the precise points where R189's NEST-DEAD proof breaks above width 2 / degree 2 (L-RED successor 45)
Started 2026-11-02 04:04Z (Lead GO R190, date -u). Brief: «the 3-wide clock escape from NEST-DEAD … With a third vertex per level, or
deg 3, a clock mover can supply the Ξ-descendant move that u_(d−1)'s re-reversal needs. Build that, with z3 at small d … Score: total
steps against d … If the clock also dies, state the generalised NEST-DEAD (width w, degree Δ) and its proof idea.» Score updates (Lead
04:33Z, 05:5xZ): DELSTEPS (L-NEW 48 box 143), then U (box 144 CHAIN-BACK: steps ≤ n_E(1 + U), so IDEAL-ACYC-POLY ⟺ U polynomial).
Labels: EXACT (z3), DATA, READING, OPEN. Model: IDEAL-ACYC (P-N5-REALIZE §2), every genome realisable by Theorem REALIZE. Not a
TARGET.md claim. G-N5-TIME OPEN. No kill.

## 0. Answer
- Not decided exactly. r190/clockbmc.py imposes NEST(d)'s move sets on u_l, v_l and leaves every other mover (the clocks) free, on a
  W-ladder of width w and degree D (option k of a level-l mover → mover w(l − 1) + (k mod w)). It reproduces R189 at w 2 / D 2 (NEST(2)
  SAT, NEST(3) UNSAT). At d 3:

| (w, D) | full NEST(3), 8 steps | prefix of 5 steps |
| --- | --- | --- |
| (2, 2) | UNSAT (R189) | UNSAT, 11 s (R189) |
| (3, 3) | undecided at 7000 s | undecided at 1500 s |
| (2, 3) | undecided at 7000 s | undecided at 1500 s |
| (3, 2) | undecided at 7000 s | undecided at 1500 s |
- DATA (climbs, r190/delclimb.py): with a clock, the constants roughly double, but the growth in d stays additive (§2). No compounding.
- The generalised NEST-DEAD is NOT proved (§1): R189's proof uses degree 2 (RE-REVERSAL) and width 2 (exactly b, p, q move at steps
  2-4). Both are genuine gaps, not presentation.

## 1. Where R189's proof breaks (READING, precise)
- Corollary LAG holds at every degree: if x stays at step t while option k is key-preferred under s_t, then k ∉ A_(s_(t−1))(x) (else
  the key-least available option would be k), so LAG-RELEASE applies.
- Corollary RE-REVERSAL needs x to RETURN to an option. At degree ≥ 3, x can go k1 → k2 → k3: at the second move k3 ▷ k2 under
  s_(t2−1), which does not contradict k2 ▷ k1 under s_(t1−1). So step (3) of NEST-DEAD (p moves at steps 3 and 5) yields no
  contradiction when p's step-5 option is a third one. What remains true: if p moves at t1 and t2 with no Ξ-descendant move in between,
  then the option chosen at t2 was already ▷ the option chosen at t1 under s_(t1−1), and was then not chosen only by key. So at degree
  D, a mover can make at most D − 1 consecutive moves «without descendant help», each to a key-better-now option (a chain in ▷ fixed
  since t1).
- Width ≥ 3: NEST-DEAD's steps (1)-(3) use «the only mover at step 2 is q» and «the movers at steps 3-4 are b, p, q». A free clock c at
  any level may move at steps 2-4 (its own moves need a key change below it or a fresh face, which the schedule does not forbid). If c
  is a Ξ-descendant of b (step 1), of q (step 2), or of p (step 3), the π-order contradiction disappears.
- So the generalised statement would need a POTENTIAL, not a fixed schedule: e.g. «the π-position of the last released mover in a
  window increases», with clocks charged to their own (key-side) releases. Not attempted; OPEN.

## 2. DATA: climbs (r190/delclimb.py; 60,000 mutations unless noted; acyclic Ξ forward in a mutable π)
- DELSTEPS (box 143: steps whose least-level mover moves while the key ranking of the level below is unchanged), seed 1:

| d | (w, D) = (2, 2): DELSTEPS / L | (3, 3): DELSTEPS / L |
| --- | --- | --- |
| 4 | 7 / 9 | 16 / 20 |
| 6 | 13 / 15 | 23 / 25 |
- U (box 144: step t ≥ 2 is chained iff a least mover of step t − 1 lies on the Ξ-chain, under s_(t−1), of the new option of a least
  mover of step t; U = unchained steps), seed 2 (d 10-12: seed 3, 40,000 mutations):

| d | (2, 2): U / L | (3, 3): U / L |
| --- | --- | --- |
| 4 | — | 14 / 18 |
| 6 | 10 / 13 | 22 / 23 |
| 8 | — | 28 / 32 |
| 10 | 14 / 18 | 34 / 38 |
| 12 | — | 31 / 35 (under-searched: below d 10) |
- Re-scored by U, the DELSTEPS bests give (3, 3): 7 at d 4, 11 at d 6; (2, 2): 1 at d 4, 4 at d 6.
- Reading: U and L grow by a constant per level (≈ 3.5 at width 3 / degree 3, ≈ 2 at width 2, the latter as L-NEW's U ≈ 2d).

## 3. OPEN / handover
- The degree-3 RE-REVERSAL escape (§1) is the sharpest open point: build a NEST-like schedule in which p visits three options in
  rotation, each move after the first enabled by key alone (no descendant move), and check whether the rotation can repeat.
- A faster exact encoding (bit-vectors, or fixing the u/v option structure) to decide the d 3 clock cases.
- Exact d = 4 (R188) and the (a′) box 137 lap recipe stay queued.

## 4. Files (experiments/red/r190/)
clockbmc.py (z3, NEST schedule on u/v with free clocks; width w, degree D), delclimb.py (climbs; SCORE=U for box 144's U, default
DELSTEPS). Outputs in r190/out are container-local (gitignored).
