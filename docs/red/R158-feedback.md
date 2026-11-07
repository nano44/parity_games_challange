# R158: FEEDBACK realised, ADDITIVE. An Odd gate on E1's reactor r_2 makes E1 WAIT for a whole E2 delay-line wave once per phase (fbg_K4_m6_m48: r_2 held through 48 source-free E2 switches). But only one gate per phase can bind, so |F| = K (m2 + c), |F|/n² stays flat (0.003–0.005, as obs_K12_m24), and hier DEPTH stays 2. Exact obstruction: the escape value of a gate must be compared with b_j's level, and a selector-driven delay line carries the NEW root (design A: every later gate opens early), while clamping it to b_j's level is either τ-improvable for Odd or loops back into the line (design B dies at step 0). No super-quadratic W-run
L-RED successor 37 (Opus 5.5; D1/D18). Brief (Lead, 2026-10-31 08:1xZ): «R158 = FEEDBACK … Route a re-climbing selector's W-rises into an Odd deviator, so that they become SOURCE EVENTS … and lengthen F. The target is a W-run longer than quadratic … If feedback cannot lengthen F, give the exact obstruction with the instance that blocks it.» Lead 08:36Z adds: score with L-NEW's hier.py (box 107; target h^W ≥ 3). Written 2026-10-31 from 08:50Z (date -u).
- Labels: DATA / READING (no new lemma). Not a TARGET.md claim. G-N5-TIME stays OPEN.
- Sources opened:
  - span/mkrw.py (engine E1);
  - docs/red/R157-reclimb.md (riders, root dominance);
  - docs/new/N5-ssi-global.md SPEC S1–S5 (S4a/S4b: Iσ by Ξ, choice by W; τ moves when Iτ ≠ ∅);
  - RESULTS R97 statement (SRC-COUNT);
  - l-new f63719c5 experiments/new/box107/hier.py docstring (DEPTH);
  - l-si c7f00306 experiments/si/sb53/ceilpot.py docstring. The l-si tip has moved past 6ca54248, which R157 used.
  - NOT opened: docs/new/N5-FINPOT-box107.md and l-lit T63 (Lead summary only).
- Engine: n5b SPEC (xcn.trace); xeng (second engine) and Oink 8fbf0a7 on every pin.

## 1. The construction (experiments/red/fb/)
- E1 = span/mkrw.py K m (pivots h, hp; reactors r_j: a_j → r_(j−1) or b_j → hp; an h-rise runs down the chain one reactor per step).
- E2 = a second reactor chain rr_1..rr_m2 (aa_i odd marker → rr_(i−1) (rr_0 = hs), or bb_i → hps), driven by two Even selectors hs / hps
  riding E1's reactors as in R157 (rider j: d_j → md_j → r_j; hs on odd j, hps on even j). An hs-rise runs down E2 one step per reactor; an
  hps-rise flips E2 back at once.
- FEEDBACK: E1's a_j (j ≥ 2) becomes an Odd gate a_j → {r_(j−1) (τ), g_j → rr_m2}. So r_j's switch b_j → a_j (W-better as soon as r_(j−1)
  rose) is Ξ-improving only when GM_j over E2's output beats b_j. The gate is an Odd deviator. Its Ξ-changes are source events, and the
  E2 wave between them is a source-free block. This is exactly SRC-COUNT's shape.
- fb/fbsearch.py: hill-climb over the marker priorities and parities (inert or placed in the band between E1's a-markers and the pivot
  ladder) of the superset gadget (rider route 2 → hp optional, b-markers optional). Objective: the longest W-run. K 2, m 6, m2 6, 4 seeds
  × 2,500 steps: best 37 (seed 2; others 33), ungated baseline 18. K 2, m 4, m2 3: 23 against 14.

## 2. DATA: the feedback binds once per phase, and the gain is additive
- Trace of the best genome (fb/fbtrace.py, K 2, m 6, m2 6): r_1 rises, hs → d1, then rr_1 … rr_6 switch one per step with gate g_2 closed,
  and only then r_2 rises (transitions 3–9). That is E1 WAITING for a full E2 wave. The other gates do not bind: r_4, r_5 and r_6 rise on
  consecutive steps. The same pattern repeats in every h-phase.
- Scaling (fb/fbscale.py on the same genome; extra E2 reactors copy the last aa-marker):

  | build | K | m2 | n | \|F\| | \|F\| / n² | E^S_F | longest source-free block | max XICH | AUP / ANDN | hier DEPTH |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | (m2 3) | 2 | 3 | 87 | 20 | 0.0026 | – | – | – | – | – |
  | best66 | 2 | 6 | 96 | 37 | 0.0040 | – | – | – | – | – |
  | (m2 12) | 2 | 12 | 114 | 49 | 0.0038 | – | – | – | – | – |
  | (m2 24) | 2 | 24 | 150 | 73 | 0.0032 | – | – | – | – | – |
  | fbg_K4_m6_m24 (pin) | 4 | 24 | 178 | 139 | 0.0044 | – | – | – | – | – |
  | fbg_K8_m6_m24 (pin) | 8 | 24 | 234 | 271 | 0.0049 | 64 | 24 | 41 (a4) | 2 / 9 | 2 (NLEV1 24, NLEV2 247) |
  | fbg_K4_m6_m48 (pin) | 4 | 48 | 250 | 235 | 0.0038 | 32 | 48 | 21 (a4) | 2 / 9 | 2 (NLEV1 16, NLEV2 219) |

  - |F| ≈ K(m2 + 10), i.e. one E2 wave per E1 phase.
  - E^S_F = 8K: the source events are the gates' Ξ-changes.
  - The longest source-free block is exactly m2: the E2 wave that E1 waits for.
  - SRC-SETTLE holds (VIOL 0, VIOL2 0, BLKV 0, srcsettle.py).
  - ceilpot (l-si c7f00306, run unchanged from a git archive): A falls at 262 / 271 (K8) and 226 / 235 (K4 m48) transitions; AUPSF 0.
  - Comparison: obs_K12_m24 has |F| / n² = 324 / 272² = 0.0044. The feedback family does not leave the quadratic band.
- xeng: identical state sequences on fbg_K8_m6_m24 and fbg_K4_m6_m48; Oink OK on both.

## 3. The exact obstruction (READING, with instances)
For a W-run gate to make E1's step j wait for E2's sub-wave j − 1, the value Ξ(a_j) = BA_j ⊕ min(Ξ(r_(j−1)), GM_j ⊕ Ξ(rr_m2)) must cross
Ξ(b_j) exactly when E2's output moves from grade j − 2 to grade j − 1 of the CURRENT phase.
- (A) LEVEL MISMATCH (design A, instance fb/instances/fbA_K4_m8_m8: |F| 44 = the ungated value, E2 never switches; xeng, Oink OK).
  - The selectors re-climb only because the root level dominates the rider markers (R157). So E2's output carries the NEW root H_(e+1)
    as soon as rider 1 has risen.
  - b_j carries the older hp-level V_e (b_j → hp). So for j ≥ 3, GM_j ⊕ Ξ(rr_m2) ▷ Ξ(b_j) holds by the root alone, and the gate is open
    before the sub-wave arrives.
  - Only j = 2 binds, because at the start of a phase E2 still carries the previous phase's root. That single gate is §2's additive
    term K · m2.
  - The trace shows it: «closed» in σ̄ (Odd prefers the escape) while Ξ(a_j) still beats b_j.
- (B) CLAMP (design B, instance fb/instances/fbB_K2_m6_m6: mkfb2.py, riders clamped by an Odd route 2 → q = min(h, hp), reset rider 0
  per selector). Putting E2 on b_j's level needs an Odd clamp at each rider: Ξ(d_j) = min(route 1 via r_j, route 2 at b_j's level).
  - S4b at step 0: Odd's improving set Iτ (computed against Even's optimum τ̄) is non-empty at q and every d_j, so τ moves at transition 0
    (q → h, d_j → mq_j). The τ-stretch ends there; longest W-run 6 (xeng, Oink OK).
  - Why it cannot be repaired by priorities (constraint reading):
    - (T) Iτ-stability of d_j. Under τ̄, opt(r_j) ⊵ opt(hp) because b_j → hp. So route 2 is not Odd-improving only if MQ_j beats MU_j
      (and RHO_j).
    - (C) A clean clamp in Ξ after r_j rises needs an even marker on route 1 above MQ_j, which contradicts (T).
    - Without (C), the rider on E2 takes route 1. Its Ξ-play re-enters E2 through its own gate: rr_m2 → … → sel → d_(j−1) → r_(j−1) →
      a_(j−1) → g_(j−1) → rr_m2.
      - An Odd-won loop makes E2's last switch non-improving (SI monotonicity), and E2 stalls.
      - An Even-won loop makes Odd at a_(j−1) leave the escape, which leaks the new root into E2. That is case (A) again.
    - Adding pre-rise detection by an odd b-marker β_j contradicts the gate's closability (GM_j ▷ β_j ▷ MU_j ▷ GM_j).
- So within this architecture (one shared delay line, gates on E1's a-routes, riders on E1's reactors), at most one gate per phase binds,
  and feedback adds K · m2 transitions; it does not multiply. This is a READING over two designs and one search space, not a lemma: a
  gate whose comparison side b_j carries the current root (with a reset by other means) is not excluded.

## 4. Pins (experiments/red/check.sh «R158»)
- fb/pins.sha1 (fbA_K4_m8_m8, fbB_K2_m6_m6, fbg_K4_m6_m24, fbg_K4_m6_m48, fbg_K8_m6_m24); fb/instances/fbg_genome.json (the seed-2
  genome);
- fbscale on fbg_K4_m6_m48 (|F| 235); wch on fbA (44) and fbB (6); xeng and Oink on fbg_K4_m6_m48 and fbA.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/red/fb/{mkfb, mkfb2, fbsearch, fbscale, fbtrace, fbval}.py, instances, pins, check.sh «R158». SHA: see the
  commit.
- FINDINGS:
  - DATA (new): a one-W-run FEEDBACK gate exists. E1 waits for a full E2 wave, which turns the wave into a source-free block of length m2
    between gate source events (E^S = 8K). But it binds once per phase: |F| = K(m2 + c), |F| / n² flat at 0.003–0.005, hier DEPTH 2,
    max XICH ≤ 41, AUP 2, ANDN 9.
  - READING (obstruction): gates on later reactors open early because the delay line carries the new root while b_j carries the old one
    (fbA_K4_m8_m8). Clamping the line to b_j's level is τ-improvable for Odd or loops back into the line (fbB_K2_m6_m6: τ moves at
    step 0).
- NEEDS: none.
