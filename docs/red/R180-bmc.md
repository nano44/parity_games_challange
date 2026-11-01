# R180 Two-level replay in the IDEAL model: exact bounded model check (z3) on the 2-wide ladder at d = 2 shows the IDEAL dynamics never exceed 4 FL steps over ALL Ξ-structures, gate orders and starts (L = 4 SAT, L = 5 UNSAT), against TB's ceiling of 8; the ceiling chain itself is realisable only for 3 steps; d = 3 not decided (z3 time-out) (L-RED successor 42)
Started 2026-11-01 13:40Z (Lead's queue: (a′) after R179, date -u). Labels: DATA (computer-checked, exact within the stated model),
READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Answer
- No two-level replay found. On the smallest ladder it cannot exist.
  - At d = 2, every structure of the IDEAL model (R178 §1) on the 2-wide ladder of depth 2 (4 movers, deg 2) has fallback-free runs
    of at most 4 steps. This is exact (red/r180/bmc.py, z3-solver 5.3.3, pip, container only):
    - L = 4 is SAT, and the model replays in fastabs as a 4-step run;
    - L = 5 and L = 6 are UNSAT.
  - The quantification is over all of: Ξ-targets (acyclic G_X), one β per option with free rank and parity, all gate orders, all
    starts.
  - TB with adversarial availability reaches 8 on the same ladder (LADDERBF). Ξ can supply at most half of it.
- Forcing the dynamics to follow LADDERBF's own 8-step ceiling chain (fixed gates and states, red/r180/synth.py) is UNSAT already
  from its 4-step prefix; prefixes of 1-3 steps are SAT. So the exponential chain is not even locally realisable.
- d = 3 (6 movers; climbs reach 7, TB ceiling 22): bmc.py with L = 7..10 did not finish: no answer after 50+ CPU-minutes per instance;
  all four were stopped undecided at 14:45Z. So no exact claim at d = 3.
- READING: together with R178 (climbs linear, growth additive) and XI-NEW, the smallest case already shows the gap between TB's
  ceiling and what Ξ-availability can drive. IDEAL-LIN stays a CONJECTURE.

## 1. The encoding (bmc.py)
- Unknowns:
  - per face (v, k): Ξ-target xt ∈ {T} ∪ (movers \ {v}), with positions pos(v) such that xt = u ⇒ pos(u) > pos(v) (acyclic G_X);
  - β rank (distinct over the faces), β parity, gate index (distinct);
  - Boolean σ_t(v) for t = 0..L.
- Values: X_t(u) = W(face u, σ_t(u)) + X_t(xt of that face). W(face) = ±2^rank. These are fastabs' signed weights; ties are impossible.
- Step: A_t(v) = {σ_t(v)} plus the other option if its face value exceeds the current one. σ_(t+1)(v) = the key-least available
  option, where keys are compared in the NEW tree (σ_(t+1)) by lex order root-first. Level 0: the gate index. Level ≥ 1: the gate
  index if both reach the same W-target, else the targets' comparison.
- Run condition: σ_(t+1) ≠ σ_t for t < L, so no fallback and no stop.
- SAT models are replayed with r177/fastabs.simulate (equal to the si.py engine, fastver): the d = 2, L = 4 model replays as (4, opt).

## 2. Files
- red/r180/ladderchain.py (LADDERBF with chain output: chain_d2.json, 8 steps; chain_d3.json, 22 steps), synth.py (follow a given
  chain), bmc.py (free search), bmc_d2_L4.json (the SAT model). The d = 3 runs left no output (stopped undecided).
- check.sh block «R180»: bmc d = 2 at L = 4 (sat, replay 4) and L = 5 (unsat); synth on chain_d2 at prefix 4 (unsat).
  About 30 s in all; skipped when z3 is absent.

## 3. Next
- Faster exact search at d = 3: a bit-vector encoding, or symmetry breaking (ladder automorphisms, gate-order normal form).
- Proof side: the d = 2 UNSAT is a finite certificate. Its unsat core could suggest the invariant behind IDEAL-LIN (not extracted here).
