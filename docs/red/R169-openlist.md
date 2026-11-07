# R169 the R168 OPEN list: a second ladder rung as escape target makes the model SAT (restart + I_τ = ∅); mid-line gates and a third reactor option do not; the SAT candidate is NOT realised (the level-1 coupling breaks it) (L-RED successor 39)
Started 00:06Z (Lead GO, last box before parking), written ~01:4xZ (date -u), 2026-11-01. Labels: PROVED (solver, for the stated
abstract model only), DATA, READING, OPEN.
- The Lead's brief: close the model's OPEN list, so that the family's reading becomes «all variants UNSAT» or yields a SAT pattern to
  build. The list:
  - (i) gates reading E3 below its head;
  - (ii) E2 reactors with more than two options;
  - (iii) other escape targets (e.g. a second ladder rung);
  - (iv) the level-1 coupling, if cheap.
  For SAT: a faithful build. For all-UNSAT: the union of the cores (the proof side's lemma).
- Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Answer
- NOT all UNSAT. Option (iii) makes the model SAT: rider and static gate escapes may go to a second rung t2. In phase, t2's value is
  q-level with a band marker. Under τ̄ it is either the root plus a band symbol, or a higher even rung (t2 = a direct edge to hp,
  T2HI).
  - This holds for one copy with the idle restart AND I_τ = ∅ AND every R168 constraint (STAY, E2STAY, static escapes, first wave lost).
    J 5: SAT, also with T2HI.
  - J 7: SAT, including a period-2 UNIFORM pattern (models in experiments/red/r167/models/).
- (i) MID and (ii) THIRD do not rescue it:
  - MID: UNSAT with I_τ (no restart), and UNSAT with the restart (no I_τ).
  - THIRD: SAT with the restart without I_τ, but UNSAT with I_τ even without the restart.
- (iv) not modelled. The SAT pattern was NOT realised: the real build (mk169.py, K 2 / 3, m2 5, m3 4, n 103 / 117, valid start) solves
  in 5 iterations.
  - A random search over the markers outside the model (E1's MU_1, MU_2, GM_2, BE_1, BE_2 and t2's marker; 400 samples, K 3) found
    at most |F| 11 and at most 1 E3 switch in the longest W-run.
  - So the remaining obstruction (if any) sits in the level-1 coupling, which the model does not contain.
- Consequence for the proof side (L-SI box 62): the lemma «restart or I_τ kills the per-step re-arm» is FALSE at the model level once
  escapes may target a second ladder rung. A proof must use the level-1 / ladder structure, or exclude such escapes.

## 1. The model (experiments/red/r167/srz3c.py; z3-solver 5.3.3, pip, not in the repo environment)
- Starts from srz3b.py (R168: COPIES, STATICESC, SKIP1, HPS0 2, STAY, E2STAY, ITAU, IDLE-RESTART), plus options:
  - MID=1 (i): E3 gets a mid vertex below the head (head a → mid, b → hps; mid a → hs, b → hps).
    - The wave passes mid and then head (states b → m → a).
    - Each gate reads head or mid (free per gate) and must stay closed in both b and m.
  - THIRD=1 (ii): every reactor j ≥ 2 gets cc_j (C_j) → u_(j−1), the armed comparison side.
    - The reactor goes reset b → pre-armed c (all at once at PREARM, Ξ-improving and W-better) → risen a.
    - Gates compare aa_j with cc_j (R159's self-reference). No fall-back c → b.
  - EXTTGT=1 (iii): a sink T2 (in-phase value: a symbol T2 below the root).
    - Rider escapes may go to T2 or into the line's own E3 head.
    - Static gate escapes go to q or to T2 (free per gate).
  - QFIX (default on, new): τ̄ values tied to the ladder.
    - q's τ̄ value is T + QS, with QS a band symbol.
    - T2's τ̄ value is a higher even rung T2S > T (t2hi) or T + T2S.
    - T2HI=1 forces the first (t2 = a direct edge to hp).
  - ITAU now also covers the static escapes. srz3b's ITAU missed them, and its free QS was too loose: an odd QS on top made a J 5 SAT
    that no game can produce.
- Bug found and fixed during the box: srz3c first encoded the idle line's E3 state as an unconstrained Int. z3 could then switch every
  state constraint off. The fixed version reproduces srz3b's UNSAT exactly.

## 2. Results (PROVED by the solver for this model; base = COPIES STATICESC SKIP1 HPS0 2 STAY E2STAY; J 5 unless stated)

| options | restart | I_τ | result | core |
| --- | --- | --- | --- | --- |
| base | – | yes | UNSAT | waves 1, 3 + ITAU@ρ_1–ρ_4, ITAU@hh_2, hh_3 |
| MID | – | yes | UNSAT | waves + CLOSEDm@3 + ITAU@ρ_1–ρ_4, hh_2, hh_3 |
| MID | yes | – | UNSAT | waves + CLOSEDm@3 + IDLE-RESTART |
| THIRD | – | yes | UNSAT | waves + ITAU@ρ_1–ρ_3, hh_2–hh_5 |
| THIRD | yes | – | SAT | – |
| EXTTGT | – | yes | SAT | – |
| EXTTGT | yes | – | SAT | – |
| EXTTGT | yes | yes | SAT | – (also with T2HI) |
| THIRD + EXTTGT | yes | yes | SAT | – (loose QS; not rerun with QFIX) |
| MID + THIRD + EXTTGT | yes | yes | SAT | – (loose QS; not rerun with QFIX) |
| EXTTGT, J 7 | yes | yes | SAT | – |
| EXTTGT, J 7, UNIFORM (period 2) | yes | yes | SAT | – (models/ext_J7_uniform.json) |

- J 5 EXTTGT + T2HI model (models/ext_J5_t2hi.json; esc ρ_1 → T2, ρ_2 → T2, ρ_3 none, ρ_4 → own E3 head, ρ_5 → q; every static escape → T2):
  - ascending: A3− < A2+ < BB3− < A4− < BB4− < H2+ < GA4+ < BB5− < BB1+ < GA5− < BBBA+ < RA4+ < MA4+ < XA2+ < RA2− < XA1− < H5+ < QS− < BB2+
    < A1+ < XA5+ < RA5− < T+ < T2S+.
- Union of the UNSAT cores without EXTTGT (the candidate lemma, model-level):
  - {the wave groups (CLOSED, OPEN, FLIP, NEXT, CLIMB, CLIMB2, START)} together with EITHER
    - IDLE-RESTART (a driver's return to its low rider is not Ξ-improving and W-better), OR
    - ITAU at the riders ρ_1–ρ_4 and at the static escapes hh_j (the self-referential escapes to q are τ-improving against τ̄).
  - Within that, MID adds CLOSEDm, and THIRD trades the restart core for the ITAU core.

## 2b. [S4b-KEEP] instead of I_τ = ∅ (Lead 01:30Z, from L-SI box 62, claude/l-si d87527ecf, docs/si/N5-ITAU-box62.md: not opened by me)
- L-SI's point: I_τ = ∅ is sufficient for τ to stay, but N5's S4b keeps τ whenever τ is Odd's optimum in H′ against σ. So R168's
  «I_τ = ∅ alone UNSAT» did not exclude real runs.
- srz3c KEEP=1 replaces ITAU by [S4b-KEEP]:
  - For every Odd edge e other than τ's, a Bool inI_e ⇔ e ∈ I_τ, i.e. strictly worse for Even than τ's edge under τ̄ (max semantics, the
    QFIX τ̄ values).
  - In every state of the phase, in H′ (Odd keeps τ plus its I_τ edges, Even keeps σ), Odd must not strictly prefer an I_τ edge to τ's
    edge.
  - Ties are ignored, so KEEP as encoded is a RELAXATION of S4b: UNSAT stands, SAT is a candidate. It rests on S4b's optimality, which
    L42 marks as not covered by R57.
- Results (J 5; base = COPIES STATICESC SKIP1 HPS0 2 STAY E2STAY QFIX):

  | options | restart | result | core |
  | --- | --- | --- | --- |
  | base | – | UNSAT | the wave groups (START, CLIMB, CLIMB2, CLOSED, OPEN, FLIP, NEXT), which carry the KEEP constraints |
  | MID | – | UNSAT | waves incl. CLOSEDm@1/3 |
  | MID | yes | UNSAT | waves incl. CLOSEDm@3 + IDLE-RESTART |
  | THIRD | – | UNSAT | waves |
  | THIRD | yes | UNSAT | waves |
  | EXTTGT | yes | SAT (implied: the I_τ = ∅ model satisfies KEEP vacuously) | – |

- So R168's result 3 survives with the correct S4b semantics, for this model:
  - one phase without a restart is UNSAT under [S4b-KEEP];
  - the only SAT family member is still the second-rung escape (EXTTGT).

## 3. Real-engine attempt (DATA)
- mk169.py builds a game from a srz3c model:
  - mk167g graph, with static escapes per gate (target hps or t2);
  - a vertex t2 (marker T2) → hp;
  - rider escapes to hps / hs / t2 / the E3 head;
  - hps2 starting on dd_2.
- Model ext_J5_t2hi.json, K 2: n 103, 5 iterations, fallbacks 1, τ moves 2, longest W-run 1. K 3: n 117, the same. The start file is valid.
- e1search.py: 400 random placements of the markers outside the model (K 3). Best: E3 1 switch, |F| 2. Best |F| 11, with E3 0.
- Reading: the abstract model's assumptions about the level-1 side do not hold in mkrw's E1 / ladder once t2 → hp exists. Those
  assumptions are: q fixed during a phase, T reached only through u_1, and no other Odd deviations. The search did not find markers
  that restore them.
- Not done: a redesign of E1 for the t2 edge; Oink / xeng on these builds (nothing to pin: no run of interest).

## DONE / FINDINGS / NEEDS
- DONE: this note; r167/srz3c.py (MID, THIRD, EXTTGT, QFIX, T2HI, KEEP, static-escape ITAU, uniform hq); r167/mk169.py; r167/e1search.py;
  mk167g.py (t2, per-gate static target, escapes to t2 / E3 head); models/ext_J7_uniform.json, models/ext_J5_t2hi.json. WIP push 1534987a.
- FINDINGS:
  - PROVED (solver, model only): mid-line gates are UNSAT with the restart and UNSAT with I_τ.
  - PROVED (solver, model only): a third, armed reactor option is UNSAT with I_τ.
  - PROVED (solver, model only): escapes to a second ladder rung make restart + I_τ SAT (J 5 and 7, uniform at J 7).
  - PROVED (solver, model only, ties ignored): under [S4b-KEEP] the base, MID and THIRD are UNSAT. The one-phase core stands without
    I_τ = ∅.
  - DATA: the SAT pattern is not realised in mkrw's E1 (5 iterations; E1-marker search |F| ≤ 11, E3 ≤ 1).
  - READING: the family's reading is NOT «all UNSAT». The open obstruction is the level-1 coupling. The proof side's lemma must use it
    or exclude second-rung escapes.
- NEEDS: none from the owner.
