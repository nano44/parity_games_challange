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
