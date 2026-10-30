# R141: adversary against L-SI's [P-INT] / CONJECTURE INT-LIN (|I| ≤ n − 1 per W-constant interval). No counterexample: hill-climbing finds intervals ≤ 3 (n 8-16). The static-order tie-break lemma is DEAD (u23sw64_n32: 26 of 64 interval switches go UP in index). A common-exit embedding of a long SI run hits a Ξ-ceiling (READING)
L-RED successor 33 (Opus 5.5; D1/D18). Lead 2026-10-30 14:09Z: input L-SI 33 box 51b (l-si f2765662, docs/si/N5-GATE-box51b.md §5: Theorem
INTERVAL-SI, kill target «embed a long SI run as ONE G_I» with (R1) τ stable, (R2) W-tight simulated edges, (R3) no Ξ-improving edge
W-better). Written 2026-10-30 from 14:15Z (date -u). Labels: PROVED (lane) / DATA / READING / DEAD. Not a TARGET.md claim. G-N5-TIME OPEN.

## 1. Counter (wint/wint.py, n5b SPEC)
- W-constant interval: a maximal stretch of transitions with τ fixed, no fallback, σ changing, and W = val(σ, τ) unchanged at EVERY vertex
  (L-SI's definition).
- Calibration: wint.py gives 8 on u23sw64_n32, L-SI's data maximum.

## 2. Search (DATA)
- wint.py --search hill-climbs over random games (mutate succ / prio / owner, as R125's rclock; fitness = (longest interval, iterations)),
  480 s per seed:

  | seed | n | best interval | n − 1 |
  | --- | --- | --- | --- |
  | 1 | 8 | 1 | 7 |
  | 2 | 10 | 3 | 9 |
  | 3 | 12 | 1 | 11 |
  | 4 | 16 | 1 | 15 |

- Random play does not find long W-constant intervals. INT-LIN is unbroken, and the fleet maximum stays 8 (u23sw64_n32).

## 3. DEAD: the static-order tie-break lemma
- Hope: inside a W-constant interval every arena option ties (cycle node, path set and length). If SPEC S1's procedure then broke ties by
  successor list order, every vertex's choice index could only fall, giving |I| ≤ m_E.
- Test (wint/idxmono.py): u23sw64_n32 has 64 switches inside W-constant intervals, and 26 of them go to a HIGHER index (e.g. vertex 2:
  6 → 31; even W cycle node). Random runs (3,000 games, n 5-12): 21 interval switches, 14 of them upward.
- So S1's tie-break is not a static order. This agrees with L-SI's finding that it is neither Ξ-greedy nor switch-all.

## 4. READING: the common-exit embedding of a long SI run hits a Ξ-ceiling
- Construction. Put an Odd dummy d on every Even edge v → t of a simulated game G, with τ(d) = an exit X* to a cycle node c*. All W-plays
  then leave at the first dummy, so the options of v tie in W (R2), provided the dummies are irrelevant and lengths are equal.
- σ̄ must deviate from τ at the dummies (otherwise Ξ = W and nothing moves). So under σ, the G-route from t must be worse for Even than
  X*. Then every Ξ-value sits below the W ceiling v ⊕ X*, and the simulated run lives under that ceiling.
- (R1) needs the opposite comparison under τ̄. The one-step G-route must not be Odd-improving, i.e. its added path set {t, …} must have an
  even top, or, when nothing is added above c*, c* must be odd with the longer route.
  - c* odd makes σ̄ take X* everywhere (it is Odd's best cycle).
  - c* even with only lengths differing makes the longer G-route Odd-improving. This is L-SI's (R1) failure.
- What remains: simulated targets t whose own priorities are even and more relevant than c*, while σ̄'s continuation from t is still worse
  than X*. Friedmann's G_n has odd-priority targets on Even edges, so this needs a per-edge compensation that does not break the W-tie.
  Not built.

## DONE / FINDINGS / NEEDS
- DONE: wint/wint.py (interval counter + search; calibrated 8 on u23sw64_n32); wint/idxmono.py (tie-break order test) (632576eb); this
  note.
- FINDINGS:
  1. DATA: no long W-constant interval in a 4 × 480 s hill-climb (best 3 at n 10). INT-LIN unbroken.
  2. DEAD: the static-order tie-break (index monotonicity) lemma. Instance u23sw64_n32, 26 of 64 upward.
  3. READING: a common-exit embedding is caught between σ̄'s ceiling (Ξ < X*-route) and τ̄-stability (one-step routes must not be
     Odd-improving). The open design is per-edge compensation for odd targets. No kill.
- NEEDS: none from the owner.
