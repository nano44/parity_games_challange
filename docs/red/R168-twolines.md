# R168 two E3 lines / two copies alternating per phase: still UNSAT. The idle restart fails, and I_τ = ∅ fails even with no restart at all (L-RED successor 39)
Started 22:19Z (Lead GO), written ~23:xxZ (date -u), 2026-10-31. Labels: PROVED (solver, for the stated abstract model only), DATA,
READING, OPEN.
- The Lead's brief, step by step:
  - two E3 lines ALTERNATING per phase, so that no driver ever restarts while its gates bind;
  - extend srz3 to that pattern first; if z3 says UNSAT, the obstruction is wider than the restart, so give the core;
  - if SAT, realise it in the real engine;
  - add I_τ = ∅ if cheap.
- Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Answer
- UNSAT in every faithful variant, and the obstruction is WIDER than R167's restart. Each of the following is UNSAT on its own:
  - (a) the literal design: two E3 lines sharing E2 (gates gg^A_j and gg^B_j on the same aa_j). The idle line's restart may happen at
    any transition of the other line's phase, and the idle line's E3 state is free per state.
  - (b) two FULL copies (own E2 + E3 each), alternating per phase. Each copy restarts while it is fully reset (every reactor unrisen),
    with a static escape per gate. This is the most favourable restart point.
  - (c) a single phase with no restart at all, once I_τ = ∅ is required: the riders' and gates' escapes are Odd-improving against
    τ̄. That is the τ movement seen in R167's mk167m build.
- With I_τ = ∅ dropped and no restart, a single phase is SAT (J 5 and J 7), as in R167. So the binding gates cost nothing inside one
  phase; both restarting and τ-stability kill the per-step re-arm.
- No real-engine build was attempted beyond a probe. An earlier model (without the E2-stay constraints) gave a SAT J 7 candidate. Its
  real build (mk168.py, K 2, m2 7, m3 4, n 115) showed reactors rising out of turn: rr4 and rr6 at transition 1, |F| 9. That prompted the
  E2-stay constraint below, which then made the candidate UNSAT.

## 1. The model (experiments/red/r167/srz3b.py; z3-solver 5.3.3, pip, not in the repo environment)
- Base: srz3.py's abstract Ξ-graph (R167 §2), with:
  - one or two lines L (riders ρ^L, drivers hs^L / hps^L, E3 head L3^L, gates gg^L_j on the shared aa_j);
  - STATICESC: an extra static escape hh_j (H_j) → q at each gate;
  - HPS0 ∈ {0, 2}: hps starts on the floor ρ_0 or on ρ_2;
  - SKIP1: the first wave of each phase may be lost, as R167's gate 2.
- The active line starts FRESH (hs on ρ_1, hps on ρ_HPS0) and runs the waves k = 1, 3, …, J − 2 with every R167 requirement:
  CLIMB / CLOSED / WAVE / OPEN / CLIMB2 / FLIP / NEXT, each in Ξ and in W (τ-graph).
- New necessary constraints:
  - STAY (drivers): no driver makes an unintended switch, i.e. no option is both Ξ-improving and W-better than the intended target.
  - E2STAY (new in R168): no E2 reactor above the next one rises (Ξ-improving and W-better). This includes the next one while the driver
    climbs.
  - IDLE-RESTART (COPIES): in the all-reset state, both drivers' switches back to ρ_1 / ρ_HPS0 are Ξ-improving and W-better. E3's
    state there is free.
  - Two-line mode: the idle line is high until its restart transition and low after it. The restart transition is free, and E3's state
    is free per state.
  - ITAU (I_τ = ∅):
    - for every Odd vertex with an alternative (gate escapes gg_j, rider escapes x_j), the alternative is not worse for Even than τ's
      edge under τ̄ (Even's best response to τ: all Even choices free, Odd on τ);
    - q's τ̄ value is a free symbol QS, which may sit above the root T (hps can reach the top ladder under τ̄).
- Every constraint is necessary for the intended run, so UNSAT is a solver proof for the model. SAT is only a candidate: the E1 / ladder
  coupling is still not modelled.

## 2. Results (PROVED by the solver for this model; cores = tagged state groups)

| variant (all: STAY, E2STAY, STATICESC, SKIP1, HPS0 2 unless stated) | J | result | core |
| --- | --- | --- | --- |
| one copy, one phase, no restart, no ITAU (DROPIDLE) | 5, 7 | SAT | – |
| one copy + IDLE-RESTART (= two full copies alternating) | 5 | UNSAT | ACLIMB2@3, AFLIP@3, ANEXT@3, AOPEN@3, ASTART, IDLE-RESTART |
| same | 7 | UNSAT | waves 1–5 groups + IDLE-RESTART |
| one copy, no restart, ITAU | 5 | UNSAT | waves 1, 3 groups + ITAU@ρ_1, ρ_2, ρ_4 |
| same | 7 | UNSAT | waves 1–5 groups + ITAU@ρ_1, ρ_2, ρ_4, ρ_5 |
| two lines on one shared E2, idle restart anywhere in the other phase (the Lead's literal design) | 5 | UNSAT | both phases' wave groups |
| one copy + IDLE-RESTART, no static escape, E2STAY off | 5 | UNSAT | waves + IDLE-RESTART |
| one copy, no restart, E2STAY off, WITHOUT SKIP1 (fresh start, the first wave must bind), static or not | 5 | UNSAT | the k = 1 / 3 groups (hence SKIP1) |

- Earlier runs without E2STAY (superseded; listed so that nobody reuses them):
  - one copy + IDLE + STATIC + SKIP1 + HPS0 2: SAT at J 5 and 7, and with ITAU at J 5 / J 7 UNIFORM;
  - two lines ONEPHASE: SAT at J 5 / 7.
  - All of these were spurious: they let unrisen E2 reactors rise out of turn, as the real build showed.
- Commands (from experiments/red/r167; 1–60 min each):
  - `STATICESC=1 SKIP1=1 COPIES=1 HPS0=2 [ITAU=1] [DROPIDLE=1] python3 srz3b.py J`;
  - two lines: `STATICESC=1 SKIP1=1 HPS0=2 python3 srz3b.py 5`.
  - Not in check.sh (runtime); R167's fast srz3 lines remain.

## 3. Reading
- R167 located the failure at the restart. R168 shows it is not the restart's timing or sharing that matters:
  - Restarting a copy while it is entirely reset fails.
  - So does handing off to a second line.
  - With I_τ = ∅, even a single phase from a fresh start fails.
- In the last case, the self-referential escapes that make the gate level-matched in Ξ (an escape to q = hps) are exactly the edges
  that Odd's τ wants under τ̄. They are temporary deviators in σ̄, but τ̄ does not see the phase structure, so the deviators are
  τ-improvements.
- So a binding level-2 gate inside one W-run needs escapes that are bad for Even now (Ξ) but good for Even at τ̄. With the
  self-referential tail that fails in every placement (model).
- READING, not proved beyond the model: in this family the level-3 re-arm per inner step cannot survive inside one W-run. The obstruction
  combines S4a's Ξ-improvement (drivers' restarts) and I_τ = ∅ (τ-stability of the gates' escapes).
- OPEN, outside the model:
  - gates reading E3 below its head;
  - reactors with more than two options;
  - other escape targets than q, T or a static q-escape;
  - the E1 coupling.

## DONE / FINDINGS / NEEDS
- DONE: this note; r167/srz3b.py (two lines / two copies, IDLE-RESTART, STATICESC, SKIP1, HPS0, E2STAY, ITAU, UNIFORM, MODEL_OUT);
  r167/mk168.py; mk167g.py options STATIC / HPS0 (WIP commit 6bf0d9f5 plus this commit).
- FINDINGS:
  - PROVED (solver, model only): the two alternating E3 lines on one E2 are UNSAT (J 5).
  - PROVED (solver, model only): two full copies alternating per phase, restarting while fully reset, are UNSAT (J 5, 7). The core
    contains IDLE-RESTART.
  - PROVED (solver, model only): with I_τ = ∅, one phase with no restart is already UNSAT (J 5, 7). The core contains ITAU at the
    riders.
  - PROVED (solver, model only): without the restart and without I_τ, one phase is SAT.
  - DATA: the pre-E2STAY candidate's real build (mk168, n 115) let reactors rise out of turn (|F| 9). That is why E2STAY was added.
- NEEDS: none from the owner.
