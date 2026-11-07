# R165 nested W-monotone counter: a third gated level ADDS (|F| = K(m2 + m3 + c)); no |F|/n² growth (L-RED successor 38)
Started 18:37Z (Lead GO 18:37Z), written ~21:xxZ (date -u), 2026-10-31. Labels: DATA, READING, OPEN.
- The Lead's brief: nest fbA's W-rise re-arm. Make the rung ladder a re-armable carrier whose W-rises come from a lower counter, so that
  re-arms paid by W-rises compound over ≥ 3 levels in one W-run.
- Score: PLAT, MAXESC, |F|/n², DESC*, depth.

## 0. Answer
- NOT multiplied. A third gated level inside one W-run adds its line length once per phase: |F| = K(m2 + m3 + c). |F|/n² does not grow.
- Attempt 1, fb/mkfb3.py: R158 design A (fbA) plus E3 and gates on E2. INERT: |F| and PLAT are identical to fbA's.
  - In fbA, E2 never switches, so gates on E2 never fire.
  - fbA_K4: n 185, |F| 44, PLAT 3. K8: |F| 88, PLAT 7. Both priority orders give the same.
- Attempt 2, fb/fbsearch3.py: fbg (R158's binding gates; E1 waits for an E2 wave once per phase) plus:
  - an E3 line rrr_1..rrr_m3;
  - Even selectors hs2 / hps2 riding E2's reactors;
  - Odd gates on E2's aa_i escaping to E3's output.
  - The new markers are placed by hill-climbing |F| from fbg's genome (4 climbs, about 750 evaluations each). Best: |F| 158 at K4,
    m2 = m3 = 12, n 215 (pin fb3_K4_m6_m12_m12, genome fb3_genome.json).
- Scaling of the climbed genome (fbscale3.py; one long W-run each, fallbacks 0):
  | K | m2 | m3 | n | \\|F\\| | \\|F\\|/n² |
  | --- | --- | --- | --- | --- | --- |
  | 4 | 6 | 12 | 179 | 50 | 0.0016 |
  | 4 | 12 | 6 | 197 | 128 | 0.0033 |
  | 4 | 12 | 12 | 215 | 158 | 0.0034 |
  | 4 | 12 | 24 | 251 | 218 | 0.0035 |
  | 4 | 24 | 12 | 287 | 206 | 0.0025 |
  | 4 | 24 | 24 | 323 | 266 | 0.0025 |
  | 8 | 12 | 12 | 271 | 294 | 0.0040 |
  - +5 per E3 vertex at m2 12 AND at m2 24 (12 → 24 adds 60 in both cases). A multiplicative level would add ≈ K·m2 per E3 vertex.
  - +4 per E2 vertex above m2 12, and +34 per rung (≈ m2 + m3 + 10). So |F| ≈ K(m2 + m3 + c), additive.
- Scores on the pin fb3_K4_m6_m12_m12:
  - anc.py (l-si 6370a35f): MAXPLAT 0, MAXESC_SX 1, WESC 1.
  - DESC* = 165 ≈ |F| (descstar ILP).
  - Even switches by class: E3 line rrr 108, E2 line rr 104, E1 reactors r 49, hs 19, hps 10, pivots 4 + 4. The E3 selectors hs2 / hps2
    NEVER switch.
- Faithfulness: xeng identical; Oink zlk + verify OK; fbscale3 rebuilds the pin byte for byte; start valid (startck; fbsearch3 repairs
  fbsearch's τ(b_j) non-edge, D-ODD-1).
- hier.py depth: NOT RUN in this box.

## 1. What caps the nesting (READING, with the instance)
- On fb3, E3 makes about 9 waves (108 / 12) and E2 about 9 (104 / 12): one wave per phase each, not one per E2 step.
- The level-3 driver hs2 never switches. Its value rises only when its fixed rider's reactor rises, i.e. with the root, once per
  phase.
- For the nesting to multiply, hs2 would have to re-climb (switch) once per E2 step, as R157's rcl selector does per E1 wave. Only then
  would E3 re-arm per E2 step.
- The climb never found that, and the reason is R158's obstruction one level down:
  - (A) a re-climbing selector's rises carry the NEW root (via its rider's reactor) while the gate compares against the OLD level (b's
    side), so the gate opens early;
  - (B) clamping is τ-improvable or loops back.
- The W-monotone form of the cap (READING, not proved):
  - Inside a W-run, every re-arm of level ℓ + 1 is a W-rise of its driver (R164).
  - A driver that does not switch rises only when the play it is fixed on rises, i.e. with the level above. That is one re-arm per
    outer W-rise.
  - A driver that does switch must take a W-rising target each time (S4a's arena optimum). Across one outer W-rise, its re-climb is a
    staircase of ≤ deg(driver) ascents (R156 k-SOURCE / R157), each of which must be paid by a separate inner W-rise of a different
    target.
  - So the re-arms of level ℓ + 1 per outer W-rise are at most the driver's out-degree: one level multiplies by deg, not by the inner
    wave length.
  - Compounding over L levels gives Π deg_ℓ ≤ (n/L)^L, which is not ruled out by this reading. But each factor needs a selector whose
    rises are gated by the OLD level (to avoid (A)), and no instance of that exists at any depth ≥ 2.
- Instance of the cap: fb3_K4_m6_m12_m12. Its selectors hs2 / hps2 have out-degree 6 each, switch 0 times, and E3 re-arms once per phase.

## 2. Status
- DATA: a third gated level is additive (fb3; slope table above). |F|/n² does not grow (0.0016-0.0040).
- DATA: PLAT 0 on fb3. Gating (waiting) removes the escape plateau, as on fbg (R164 §1b: fbA PLAT K − 1 vs fbg 0).
- OPEN: a selector at level ≥ 2 that re-climbs once per inner step, with its rises compared against the OLD level. That is R158 (A) at
  depth 2 and the exact missing gadget.
- G-N5-TIME stays OPEN. Nothing here is a counterexample or a theorem.

## DONE / FINDINGS / NEEDS
- DONE: this note; fb/mkfb3.py, fb/fbsearch3.py, fb/fbscale3.py; pin fb/instances/fb3_K4_m6_m12_m12 + fb3_genome.json (fb/pins3.sha1);
  check.sh block R165.
- FINDINGS:
  - DATA: nesting a third gated level adds; |F| = K(m2 + m3 + c), with no |F|/n² growth.
  - DATA: E3 re-arms once per phase because its selectors never switch.
  - READING: the cap is R158 (A) one level down; a non-switching driver re-arms once per outer W-rise, a switching one at most deg times.
  - Not run: hier.py depth.
- NEEDS: none from the owner. Lead: L-RED 38 parks after this box (handover: notes/L-RED.md «Successor 38 PARK»).
