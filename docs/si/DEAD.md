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
