# R167 self-referential level-2 gate: binds within a phase, but the RESTART of the level-3 drivers is never Ξ-improving (exact order model UNSAT); no |F|/n² growth (L-RED successor 39)
Started 20:56Z, written ~21:4xZ (date -u), 2026-10-31. Labels: DATA, PROVED (solver, for the stated abstract model only), READING, OPEN.
- The Lead's brief: build the missing gadget of R165 by design: a level-≥2 selector that re-climbs once per inner step while its rises
  are compared against the OLD level. Use R159's self-referential gate (hit_b6a_1) at level 2 and fbg's binding gates at level 1.
  Decisive output: |F|/n² growing with n in one family; otherwise the exact obstruction with the instance.
- Not a TARGET.md claim. G-N5-TIME stays OPEN.
- Sources opened: docs/red/R158-feedback.md, R159-depth.md, R165-nest.md; docs/new/N5-ssi-global.md SPEC S1–S5 (S4a: improving set
  by Ξ, choice by W); experiments/red/fb/fbsearch3.py, span/mkrw.py.

## 0. Answer
- NOT multiplied. No family with |F|/n² growing was found.
- The obstruction is S4a's Ξ-improvement condition on the level-3 driver's RESTART (the switch from its top rider back to a low rider
  when a new outer phase starts). It is not W-monotonicity: in W the restart is a rise (the outer root dominates).
  - Self-reference makes the level-2 gate level-matched in Ξ: the gate's escape ends at the same vertex q = hps as the gated reactor's
    comparison side bb_(k+1). This works inside a phase (model SAT, §2).
  - But then the drivers' riders all end at q in Ξ too, so Ξ no longer sees the outer root. The restart has to be paid by band markers,
    and those markers cannot also serve the closed gate, the E3 wave and the E3 flip. The exact order model is UNSAT (§2).
  - Without self-reference (every escape ends at the root's level), the very first closed gate is UNSAT: that is R158 (A).
- Real-engine instance (n5b, xeng identical, Oink OK): r167/instances/sr_K2_m6_m4 (mk167.py design D1, n 100).
  - At state 3, u_1 = rr_1 has risen.
  - The E3 driver hs2 sits on its top rider dd5: W(dd1) contains the ladder vertex MWL1, W(dd5) only MWLp0, so dd1 is W-better.
  - But Ξ(dd1) = {M, Bqp0, dd1, md2, x1} and Ξ(dd5) = {M, Bqp0, dd5, md2}: both end at hps, and dd5's marker is the higher, so
    the switch to dd1 is not Ξ-improving.
  - So hs2 / hps2 never switch, E3 never moves, and |F| = 22 (one W-run 1–23, the bare E1/E2 run).

## 1. The constructions (experiments/red/r167/)
- mk167.py (by design): span/mkrw.py K 2, plus:
  - fbg's level-1 gate a_2 → {r_1, g_2 → rr_m2};
  - E2 rr_i → {aa_i, bb_i → hps}, aa_i (i ≥ 2) Odd → {rr_(i−1) (τ), gg_i → rrr_m3};
  - E3 rrr_t → {aaa_t → rrr_(t−1) | hs2, bbb_t → hps2}.
  - NEW: the E3 drivers' riders are Odd, dd_i (MU2_i) → {rr_i (τ), x_i → hps}. The escape is self-referential: in Ξ it ends at hps,
    the comparison side of every E2 gate.
  - Band order D1: BA3 < BA2 < X < MU_1 < MU_2 < GM_2 < MU2_0 < GM2_2 < MU2_1 < GM2_3 < MU2_2 < …, with GM2_(k+1) between MU2_(k−1)
    and MU2_k.
- mk167g.py: the same graph with every marker placed by a genome. It has:
  - escape modes ESC 0–3 (0 = none, the fb3 shape; 1 = all to hps; 2 = from i ≥ 3; 3 = dd_1 / dd_2 to hs);
  - explicit placements and per-index escapes (used by mk167m.py, which builds a game from a z3 model).
- climb167.py: hill climb on (E3 switches in the longest W-run, |F|). K 2, m2 6, m3 4, one climb per ESC mode (ESC 0 ran 1,500
  iterations; ESC 1–3 were stopped after 914–1,137 iterations).
  - Best E3 = 16 in every mode. That is 2K·m3: one E3 wave plus one flip per phase, as on fb3 (R165).
  - |F| ≤ 34 at n ≈ 100–110.
  - The multiplying target, E3 re-armed per E2 step in every phase, would give about 48.
- score167.py (|F|, switches by class), xiprobe.py (Ξ and W path sets at a state).

## 2. The exact order model (r167/srz3.py, z3 4.x / pip z3-solver 5.3.3; not in the repo environment, check.sh skips without it)
- The model is the abstract Ξ-graph of the family, with values taken relative to q = Ξ(hps). T is the outer root's top symbol, reached
  only through u_1's advance side.
  - u_j (E2 reactors), bb_j (BB_j) → q;
  - aa_j (A_j) → {u_(j−1), gg_j (G_j) → L3};
  - L3: a-state → (BA3) hs2, b-state → (BBB) hps2;
  - riders ρ_j (R_j) → {mdd_j (M_j) → u_j} plus an optional escape x_j (X_j) → q or → T, chosen per j;
  - ρ_0 (R_0) → q.
- Every symbol has a free rank, a free parity, and free presence (absent = inert).
- Ξ(v) = Odd's minimum over the simple paths. Every cycle Odd could close must be Even-won.
- Order: the top present symbol of the symmetric difference decides (SPEC S1 path-set order).
- Requirements (J = 7 or 9 reactors; waves k = 3, 5, …):
  - RESTART: Ξ(ρ_1) ▷ Ξ(ρ_top-odd) once u_1 has risen; Ξ(ρ_2) ▷ Ξ(ρ_top-even) once u_2 has risen.
  - CLIMB / CLIMB2: the drivers' switches to ρ_k and ρ_(k+1) are Ξ-improving.
  - CLOSED: Ξ(aa_(k+1)) ⊴ Ξ(bb_(k+1)) while L3 is in the b-state, plus WAVE: BA3 + Ξ(hs2) ▷ Ξ(hps2).
  - OPEN: Ξ(aa_(k+1)) ▷ Ξ(bb_(k+1)) once L3 is in the a-state.
  - FLIP: Ξ(hps2) ▷ BA3 + Ξ(hs2) after u_(k+1) rose.
  - NEXT: the next gate is not blocked forever.
  - Options:
    - WREQ adds the same switch requirements in W (τ-graph).
    - TFREE lets T sit below band symbols (R165's "markers above the root" horn).
    - STAY forbids unintended driver switches (S4a: W-optimum among the Ξ-improving options).
    - HPSLATE lets hps2 skip its restart at step 2 and restart at step 4.
- Not modelled: I_τ = ∅ and the E1/ladder coupling. These omissions only drop constraints, so every UNSAT below stands. A SAT answer is
  only a candidate.
- Results (PROVED by the solver for this model; the unsat cores are printed by the script):

  | variant | result | unsat core (groups) |
  | --- | --- | --- |
  | J 7, default (T top) | UNSAT | RESTART@hps2, CLOSED@3/5, OPEN@3, WAVE@3/5, FLIP@3/5, CLIMB2@3 |
  | J 7, DROP=RESTART | SAT | – (one phase: the self-referential gate binds at every wave) |
  | J 7, DROP=CLOSED | SAT | – (no gate: R165's additive regime) |
  | J 7, ESCQ=0 (no self-reference) | UNSAT | CLOSED@3 alone (R158 (A)) |
  | J 7, HPSLATE=1 | UNSAT | CLIMB2@3 (the delayed restart ρ_4 ▷ ρ_6), CLOSED@5, WAVE@5, FLIP@5 |
  | J 7, TFREE=1 (+ W requirements) | UNSAT | RESTART@hps2 + W and Ξ groups |
  | J 9, STAY + WREQ | UNSAT | RESTART@hps2, … |
  | J 9, STAY + TFREE | UNSAT | |
  | J 9, STAY + WREQ + HPSLATE | UNSAT | CLIMB2@3 (delayed restart), … |
  | J 9, STAY + WREQ + DROP=RESTART + UNIFORM (period 2) | SAT | – (model: X_j and BB_j odd, decreasing in j, interleaved) |
  | J 9, STAY + WREQ + PHASE1 (drivers start on ρ_1 / ρ_0) | UNSAT | CLIMB2@1, CLOSED@1/3, FLIP@1, STAY (the floor ρ_0 acts as a restart) |

- So, within this family (the R165 / fb3 graph plus self-referential or root escapes, every marker placement):
  - a binding level-2 gate at consecutive waves is compatible with the per-step re-climb inside one phase;
  - it is incompatible with any restart of a driver that the gates read. Every core contains a restart.
- The SAT one-phase model was NOT realised in the real engine. mk167m.py with MID=1 (start mid-phase) moves τ at the riders (dd_j → x_j)
  from transition 1 on, because I_τ ≠ ∅ is not in the model. So the one-phase product stays a model-level statement.

## 3. Reading: why the restart kills it
- The gate must be level-matched (R158 (A), R159). Level-matching in Ξ means the escape's play and the comparison side's play share the
  tail q. The re-climbing driver feeds the gate, so the driver's Ξ-play ends at q too.
- At a phase change, the driver must go back from its top rider to a low one. In W this is a rise, paid by the new outer root.
- In Ξ the root is invisible (that was the point of the self-reference), so the restart must be a band-marker rise. Within the phase,
  however, the same riders must climb upwards in band order, gated by the same markers.
- The solver shows that no placement (any parities, inert markers, per-index escapes to q or to the root) satisfies the restart
  together with the closed gate, the E3 wave and the E3 flip of the next waves.
- Without self-reference, the root is visible and the first closed gate already fails.
- READING (not proved beyond the model): a level-2 gate can bind per inner step either within one phase (self-reference) or once per
  phase (root-visible), not both. So E3 re-arms m2/2 times in one phase or once per phase. Either way |F| = O(K(m2 + m3) + m2·m3), with
  no product of three.

## 4. Scores (pin sr_K2_m6_m4, n 100)
- |F| 22, |F|/n² 0.0022, one W-run (1–23), fallbacks 0, τ moves 1 (transition 0).
- Even switches by class in the W-run: rr 24, r 8, ladder 8. E3 (rrr) 0, drivers (hs2 / hps2) 0 after transition 0.
- anc.py (experiments/si/anc58 on trunk): MAXPLAT 1, MAXESC_SX 2, WESC 5.
- DESC* 12 (DESC 76; descstar ILP, LNEW=..).
- hier.py (l-new box107 on trunk): DEPTH 2 (NLEV1 5, NLEV2 17).
- Faithfulness: startck OK; xeng identical; Oink zlk + verify OK.
- Climb bests (scratch, not pinned): E3 16 = 2K·m3, |F| ≤ 34.

## 5. Status
- DATA: no |F|/n² growth. The self-referential design idles in the real engine (pin above). Climbs on the family stay at one E3 wave
  per phase.
- PROVED (solver, abstract model): the restart + binding-gate requirement sets are UNSAT (table). The one-phase set is SAT.
- OPEN:
  - outside the model: gates that read E3 at other positions than its head; reactors with more than two options; several E3 lines;
    escapes to other targets;
  - I_τ = ∅ as a further constraint;
  - realising the one-phase product (which would still be quadratic).
- G-N5-TIME stays OPEN.

## DONE / FINDINGS / NEEDS
- DONE: this note; r167/{mk167, mk167g, mk167m, climb167, score167, xiprobe, srz3}.py; pin r167/instances/sr_K2_m6_m4 (pins.sha1);
  check.sh block R167 (srz3 lines need z3, else skipped).
- FINDINGS:
  - DATA: the self-referential level-2 gate idles in N5. The level-3 restart is W-better but not Ξ-improving (sr_K2_m6_m4: |F| 22, E3 0;
    xeng, Oink OK).
  - PROVED (solver, model only): restart + binding gate at consecutive waves is UNSAT over all marker placements. Without
    self-reference CLOSED alone is UNSAT (R158 (A)). One phase without a restart is SAT.
  - READING: per-step binding and per-phase restart exclude each other, so no three-level product in this family.
- NEEDS: none from the owner.
