# R102: FB-LIN, the multi-switch carry route. No kill: f is the number of S4a stalls, and carries add stalls only as fast as the gate value rises; carry-count climbs plateau at 0.28n (CR 11 at n 40)
L-RED successor 24 (Opus 5.5; D14/D15/D18; Lead 2026-10-29 03:24Z: "NEXT box: the multi-switch carry route ... Θ(n) carries per phase,
each a multi-switch fallback, as in long121 with RF 7 of f 8 ... f > n in one phase, or a family where f/n or RF/n grows ... 60-90 min").
Written 2026-10-29 from 04:22Z (date -u). Labels: DATA / READING / OPEN. Builds on R100, R101 and my predecessor's R98 §3.

## 1. Measures (experiments/red/fb/fbphase.py, reuse(), MODE_RF)
- FM (mode 3): in-phase fallbacks of the phase that switch ≥ 2 vertices (carries).
- CR (mode 4): carries that re-switch a vertex switched by an earlier in-phase fallback of the same phase.
- At the seeds: long121_n40 f 8, FM 8, CR 7; pl130_n40 f 11, FM 11, CR 10; n3/out/ph7/best_7 (S3) f 23, FM 12, CR 9.

## 2. DATA: climbs (fbclimb.py, own start, fitness 100 f + 1000·measure + total fallbacks; 15-40 min each)
| seed | measure | best (f, measure) | shape |
| --- | --- | --- | --- |
| long121_n40 ×2 | FM | (16, 15), (15, 14) | mostly 2-switch fallbacks in a row: two parallel single waves (FM gamed) |
| pl130_n40 | FM | (12, 12) | same |
| best_7 | FM | (10, 10) | same |
| long121_n40 ×2 | CR | (11, 10), (13, 11) | carries as in long121; no growth beyond +4 |
| pl130_n40 | CR | (12, 11) | same |
| best_7 | CR | (12, 11) | same |
CR rises from 7-10 to at most 11 at n = 40 (0.28n), against f ≤ 0.79n for one wave (R101 §3).

## 3. DATA: grafting a wave onto long121's carries (fb/graft.py)
A chain c_1 … c_w (Even, priority P, c_i → {0, c_{i−1}}, c_1 → {0, SRC}) added to long121_n40 (gate 0), start c_i → 0 or c_i → c_{i−1}.
Sweep: SRC ∈ {31, 15, 12, 10, 2, 16, 36, 25, 23, 21} (the gate-attached vertices' alternatives and others), P ∈ {9, 11, 13, 23, 33}, both
starts, w ∈ {4, 8, 16}: 300 runs, every one gives f 8, CR 7, R1 0 exactly as long121 itself.

## 4. READING: why carries do not multiply (design obstruction, not a theorem)
- f counts STALLS: in-phase transitions where S4a and S4b change nothing (S4c fires only then). A wave of w fallbacks needs w consecutive
  stalls. In long121 S4a runs an ~18-step block after each carry, so the grafted chain can advance only at the stalls that already exist,
  and f does not move (§3).
- Two ways to get more stalls:
  - (a) Consecutive stalls: a wave. Reuse across waves needs the rest of the game to WAIT for the wave and then produce a new source. Waiting
    means a reader of the chain, and R100 §3's lock/trigger pair applies even when an S4a cascade runs between the reader and the new source.
    The new source z next to the chain end needs a lock: the z-side prefix weight must be below the attached gate prefix. The trigger needs the
    chain end plus the gate prefix below 0. Together they make the z-side prefix negative, and then the cascade's amplifier (an even vertex
    above the old source) cannot dominate it. Checked by hand on the reader → cascade → Odd release → z chain.
  - (b) Isolated stalls separated by S4a runs: carries. In long121 each carry needs Ξ(gate) to rise (S4a re-attaches the gate-attached
    vertices only then; R98 §3), and my predecessor's reading ties each rise to one high-rank penalty level walked by the gate's route. Carries
    per phase are then at most the number of rises of Ξ(gate) in the phase, plus a bounded number of extra fallbacks per carry (long121: 8
    fallbacks for about 6 rises). Each rise in long121 costs a penalty vertex, so f/n stays below 1 unless one vertex can supply several rises.
  - The question this leaves: can Ξ(gate) rise Θ(n) times in one phase with each rise followed by a stall? The number of Ξ-changes of one
    vertex in a phase is reader-inflatable (XR-LIN DEAD, L-SI), but a reader does not create stalls. I did not find a gadget whose rises each
    end in a stall.

## 5. OPEN
- A gate whose Ξ value rises Θ(n) times in one phase, each rise followed by an S4a stall with a W-rejected Ξ-improving edge (a carry).
  Equivalently: Θ(n) carries per phase at O(1) vertices per rise. Not attempted beyond the climbs.
- Nothing here bounds f. FB-LIN remains a CONJECTURE (data max 38 = 0.79n, fb38_n48, R101 §3).

## DONE / FINDINGS / NEEDS
- DONE: R102 (this file); fbphase.reuse modes 3 (FM) and 4 (CR); fbclimb --fm / --cr; fb/graft.py.
- FINDINGS:
  - Carry-count climbs plateau: CR ≤ 11 at n 40 (0.28n). FM climbs are gamed by parallel single waves.
  - Grafting a wave onto long121's carries changes nothing (300 variants, f 8): f is the stall count, and a wave adds stalls only if the
    game waits for it.
  - The carry route reduces to "Θ(n) rises of one gate's Ξ per phase, each ending in a stall" (READING). No gadget found.
  - FB-LIN unkilled.
- NEEDS: none from the owner.
