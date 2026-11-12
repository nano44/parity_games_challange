# R231 item (b): two hand-built re-arms that try to see the race without a route back into R (adversary vs CONJECTURE DEEP-k1, box 206)
L-RED successor 65. Written 2026-11-12 (date -u in the commit). Lead 05:58Z: «Try at most two hand-built designs … Measure Q_(>1) and T at
k = 1 on your engine for 3+ sizes. The aim is super-linear Q_(>1), or the exact obstruction with its instance.» Engine: experiments/red/
r221q/own.py (IDEAL-CYC); builders experiments/red/r231/carry231.py (CW(n)) + gate231.py; no L-NEW code. Labels: DATA / DEAD / READING.
Frozen: r231/inst/CWG{1,2,3,4}_{4,8,16}.json (sha1 in r231/inst/SHA1SUMS), for L-COMP 18's cross-check.

## 1. Designs (gate231.py on CW(n); MWR(n) names: race movers R, Q (W-target hv, Ξ-target R), hv → v)
- Design 1, GATED RE-ARM with a STATIC exit.
  - Build: a level-0 exit mover z0 (Ξ X) and a level-1 mover y with one option (W-target z0, Ξ-target R). Every carry chooser c_k gets one
    more option (before X) with Ξ-target y. MODE 1 has one shared y; MODE 2 has one y_k per k.
  - Intent: at y's gate Odd can follow the race (β → R) or leave it (e-face → e_y → z0 → X), so the re-arm sees the race but gives Odd an
    exit instead of a trap.
- Design 2, GATED RE-ARM with a DYNAMIC exit: as design 1 with y's W-target hv. Then y is a copy of the race mover Q, and its exit
  value moves with the race. MODE 3 has one shared y; MODE 4 has one y_k per k.
- k = 1 on every instance: c_k is entered only by W-edges, so there is no new Ξ-cycle.

## 2. DATA (cw231.py, dep231.py; out/cw231_CWG.out, out/dep231_CWG.out; unit: IDEAL-CYC Howard steps / loud steps; scope: all vertices)
| genome (n = 4 / 8 / 16) | N + M | D_mov | T | Q_(>1) | max change depth |
| --- | --- | --- | --- | --- | --- |
| CW(n) (R231-box206, baseline) | 157 / 303 / 643 | 12 / 38 / 92 | 30 / 59 / 114 | 2 / 7 / 14 | 3 / 8 / 16 |
| CWG1 (static exit, shared y) | 164 / 314 / 662 | 8 / 30 / 86 | 28 / 52 / 108 | 0 / 0 / 8 | 2 / 8 / 16 |
| CWG2 (static exit, y_k per k) | 168 / 326 / 690 | 8 / 30 / 86 | 28 / 52 / 108 | 0 / 0 / 8 | 3 / 8 / 16 |
| CWG3 (dynamic exit hv, shared) | 164 / 314 / 662 | 3 / 3 / 3 | 28 / 52 / 100 | 0 / 0 / 0 | 1 / 1 / 1 |
| CWG4 (dynamic exit hv, per k) | 168 / 326 / 690 | 3 / 3 / 3 | 28 / 52 / 100 | 0 / 0 / 0 | 1 / 1 / 1 |
- k 1 and BOX 206 must-0 counters 0 on all 12. Neither design beats CW on any measure; Q_(>1) is at most CW's at every size.
- Trace of design 1 (gface231.py, out/gface231_CWG1_8.out and out/gface231_CWG2_8.out; unit: states; set CWG1_8, CWG2_8):
  - Every c_k takes the re-arm option at t = 1 (CWG1 and CWG2), and Odd follows the race at y (β).
  - CWG1: y's gate flips to the exit (e) once, at t = 9, and stays e to the end (0 flips e → b).
  - CWG2: the y_k flip to e one at a time, at t = 9, 15, 21, 27, 33, 39, 45, and never flip back (0 flips e → b).
  - After t = 1 the number of c_k on the re-arm option never increases (7 → 1 at the end, t 52; per-c_k re-takes not logged separately).
  - So each y gate flips at most once and the re-arm population only shrinks: the carries are not re-armed.

## 3. DEAD (both designs) and the obstruction
- DEAD «gated re-arm with a static exit re-arms carries» (CWG1 / CWG2, n = 4, 8, 16; killing instance CWG1_16: Q_(>1) 8 < CW16's 14, T 108 < 114).
  - Obstruction (DATA): y's gate flips β → e once and never back, so the re-arm is one-shot.
  - READING: y's β-value is R's value, which rises over the run, while the static exit's value is constant. Once R passes the exit, Odd
    exits for good. Not proved here; it would need value monotonicity at R, i.e. R118 (c) DOM / STRICT, not checked for this use.
- DEAD «gated re-arm with a dynamic exit through the race's own exit (hv)» (CWG3 / CWG4; killing instance CWG3_16: D_mov 3, T 100, Q_(>1) 0).
  - Obstruction: the collapse of R231-cwr. The exit e_y → hv → v → qh → e_qh → c_k → y → R is a route back into R, so the race cycle traps
    and absorbs the carries; the numbers equal CWRR(n) exactly.
- READING (the dilemma behind both): a gate that re-arms a carry from the race needs an exit whose value moves with the race. In MWR every
  vertex that moves with the race either is the race (route back into R: trap) or is downstream of a static exit (one flip: one-shot).
  A super-linear Q_(>1) at k = 1 would need an exit value that rises AND falls relative to R's value. That is the same «value that rises
  later» resource as the depth-3 stall (R231-stall3: dynamic faces refused by Odd). Not found; DEEP-k1 untouched.
