# Dead SI candidates (L-SI). Each entry: the rule, the family or instance that killed it, the growth it showed, the commit.
Iteration tables: docs/si/RESULTS.md (generated); raw logs experiments/si/out/ (gitignored, regenerate with families.py).

## S4 (subgame-optimal start, then switch-all): DEAD 2026-10-15 10:50Z
- Killer: switchallexp (Friedmann's switch-all family, pgsolver_port.py). Iterations N=1..8: 10, 30, 70, 150, 310, 630, 1243, 2486,
  IDENTICAL to plain switch-all from the best-reward start (doubling per +1 in N: the same run).
  Also switchbestexp N=1..8: 21, 65, 130, 253, 466, 853, 1592, 2963 (b ≈ 1.87, switch-all: 21, 61, 141, 301, 621, 1261, 2541, 5101).
- Obstruction: the optimum σ' of the subgame V \ Attr_Odd(top priority) extends to a start on G that is no closer to σ* in the
  improvement order than the best-reward start: on switchallexp the attractor of the top priority (FinalSink's 16n+12, Odd's)
  is small and σ' restricted to the rest restarts the counter at zero, so the first switch-all step reaches the same strategy as
  from ι. The Lemma 4.3 argument needs σ* itself; an optimum of a subgame is not a surrogate.
- The S4:msf variant inherits msf's behaviour (not switch-all's) and is subsumed by S2.

## S2b LSF (least-significant-first single switch): DEAD 2026-10-15 10:52Z
- Killer: zadehexp (PGSolver zadehexp.ml, "Exponential Lower Bound for Zadeh's rule", port experiments/si/gens.py).
  Iterations N=2..10: 33, 89, 205, 441, 917, 1873, 3789, 15301 (N=10; N=9 not run): b ≈ 2.0 per +1 in N (n = 17N - 6).
  Contrast on the same games: switch-all 4-6, msf 12N - 9 (15, 27, ..., 135 at N=12), steepest 8N - 1, most-improved 8N - 5.
- Obstruction (reading, unrefereed): Zadeh's game is a counter whose cycle gates differ at low priorities (3-6) and whose
  bit selectors sit at priorities 2i + 11; a rule that always serves the least relevant open difference re-opens and
  re-closes the low gates once per higher-bit increment, as Zadeh's least-entered rule does (Disser-Friedmann-Hopp
  arXiv 1911.01074 Thm 6.18 is for Zadeh's rule with its tie-break; the LSF run is an observation, not a proof).
- Regression instance: experiments/si/instances/zadehexp_N5.pg (lsf: 441 iterations; pinned in check.sh).

## S3 steepest (single switch maximising the re-evaluated valuation of the switched vertex): DEAD 2026-10-15 11:20Z
- Killer: the sink-parity-game port of DLMM 2512.16684 Lemma 5.4's MDP M_L (L-LIT T12 section 4; experiments/si/gens.py
  dlmm_ML, start sigma_0 of the lemma). Iterations L=2..10: 4, 11, 26, 57, 120, 247, 502, 1013, 2036 = 2^(L+1) - (L+2),
  IDENTICAL to LSF's run (n = 3L + 4). MSF on the same games: 3L - 2 (4, 7, ..., 28); most-improved: L; switch-all: 2;
  Random-Action-Removal: 3.0 ... 14.4 (mean of 10 seeds, L=2..8).
- Obstruction (reading): the largest re-evaluated gain is the least significant switch here, exactly DLMM's f_Π ≡ 1 case
  (Lemma 5.4 is stated for {Bland, Dantzig, LargestIncrease}-ranking rules choosing the least-preferred switch; this is an
  observation on the port, not a theorem about parity games).
- The most-improved variant (count of vertices whose valuation improves) is linear here and remains open but is subsumed
  by the cost argument (O(n^2 m^2) per iteration) and is not pursued further.
- Regression instance: experiments/si/instances/dlmm_ML_L6.pg (lsf and steepest: 120 iterations from the start in dlmm_ML_L6.start).

## S2a MSF (most-significant-first single switch) and its variants msfa/msfc: DEAD 2026-10-15 12:23Z (killed by L-RED)
- Killer (L-RED, reported by the Lead 12:23Z; files claude/l-red experiments/red/gens_red.py gated_bland, instances
  gated_bland_N6/_N8.pg): the DLMM Bland counter with each a_i choice routed through a Friedmann simple cycle
  (1106.0778 section 6.1, Lemma 6.1) whose two Odd gate vertices carry even priorities decreasing in i. Exactly 2^N - 1
  iterations, n = 5N + 2, from the best-reward start; si.py and L-RED's independent vj.py agree on every row up to N = 13;
  msfa and msfc give identical counts.
- Mechanism (Lead's summary of L-RED): the 2-cycle through the gate sets the switch's LEVEL (the gate's even priority,
  decreasing in i, so MSF processes levels in Bland's order), Odd's current choice at the gate sets its SIGN (Odd goes back
  to a_i exactly when the counter's edge is improving), and the gate's exit sets its EFFECT (as in the plain counter).
  This refutes L-SI's obstruction (b) (notes/L-SI.md 11:25Z): the decoupling of level from effect that Dantzig lower
  bounds get from probability scaling is obtained here by an escaped cycle-creating switch. General lesson (L-RED, lemma in
  preparation): gate relabelling re-assigns the level of any switch, so every rule ranking improving edges by
  first-difference position inherits the index-based lower bounds (DLMM 2512.16684 Thm 4.3 class).
- L-SI reproduction (12:58Z, trunk b5fd882 experiments/red/gens_red.py gated_bland, run on si.py): MSF iterations for
  N = 2..12: 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095 = 2^N - 1 exactly (n = 5N + 2); msfa identical; lsf 1,
  switch-all N, zadeh 2N - 1, cunningham ~4N, Random-Action-Removal 1.8 .. 13.4 (mean of 10 seeds). L-SI's own gate
  variants built from the description before the push did not reproduce (wrong gate placement: the gates must sit on a
  relay d_i after a_i with the underlying priorities shifted above the gate priorities, gens_red.py docstring).
  Regression instance: experiments/si/instances/gated_bland_N6.pg (msf: 63). gated_bland and gate.py transforms are in
  experiments/si/families.py as standard falsification families from now on.
