# N5 SSI-GLOBAL: second independent implementation (gauntlet step 2; L-COMP, Lead task 2026-10-18 20:51Z)
Subject: L-NEW's N5 (docs/new/N5-ssi-global.md on claude/l-new @ 8925171, section "Exact pseudocode").
Rule followed: implemented from that TEXT only. experiments/new/n5.py and L-SI's engine experiments/si/ were not opened
(fetch_lnew.sh extracts L-NEW's generators and CSVs with n5.py excluded and refuses to run if it appears).
Valuations: Vöge-Jurdziński, from L-COMP's own port of PGSolver's evaluate_strategy (experiments/hard-families/pgsolver_si.py,
class SI), which is REFEREE-checked and matched the PGSolver d3cd624 binary exactly (iteration counts and solutions,
experiments/hard-families/pgsolver-binary-diff.md). So the valuation code shares nothing with L-SI's engine.

| file | what |
| --- | --- |
| `n5b.py` | N5 (steps 1-5 of the spec), outputs regions + both players' positional strategies; `--start FILE` for a given (σ0, τ0) |
| `fetch_lnew.sh` | out/root = L-NEW's generators + CSVs (no n5.py) + this repo's hard-families, harness, tools |
| `cmp_family.py` | per L-NEW CSV row: regenerate, sha1 check, n5b, regions vs Oink zlk (tl if zlk fails), verify.py, counts |
| `rand_check.py` | own seeded corpus: n5b vs Oink zlk AND harness/zielonka.py, verify.py; counts per game with sha1 |
| `run_all.sh` | all 17 families, 4 in parallel, BUDGET s of n5b time per family |

## Ambiguities in the spec text (each a finding against the spec; reading chosen in brackets)
- A1 "injective rank" of priorities is not defined for equal priorities. [ties by vertex index, as PGSolver's VJ order]
- A2 "best-reward start for both" names no rule or tie-break. [PGSolver initial_strategy_by_best_reward; Odd: same on the dual]
- A3 the dual game: "owners swapped, priorities + 1" is given; successor order and vertex ids are not. [same ids, sorted successors]
- A4 Iσ, Iτ: "improving edges" is not defined in the text (strict or not, w.r.t. which valuation). [strictly better under Ξσ
  than σ(v); Iτ the same on the dual with Ξτ]
- A5 "Even's optimal strategy" in the restricted arena: optimal strategies are not unique and no tie-break is given; this can
  change σ' and therefore all counts. [PGSolver's counterstrategy rule: per vertex the successor of best valuation, ties by index]
- A6 step 3 says "Odd's optimal counterstrategy to σ": old σ or the σ' of step 2 is not explicit (steps 2-3 read as simultaneous).
  [old σ]
- A7 fallback "one classical switch-all step": which improving edge each vertex takes, and tie-breaks, are not given.
  [each vertex with an improving edge switches to its best successor under Ξσ, ties by index]
- A8 "iterations" is not defined (passes through steps 2-5, or including the final pass of step 1). [passes through 2-5;
  this reading reproduces L-NEW's counts, see results]
- A9 output: "Engine.regions(σ) (regions and both players' strategies)": which Odd strategy (τ, or σ̄ = optimal counter to σ) is
  not said. [winner = parity of Ξσ's cycle vertex; Even plays σ, Odd plays σ̄]
- A10 the spec defines the valuation only by reference to code ("L-SI's engine experiments/si/si.py") and to VJ00 without a
  section number; a reader without that code must supply VJ's valuation (cycle vertex, path set, length), its order and the
  counterstrategy algorithm. [PGSolver's, via pgsolver_si.py]

## Results
See results/<family>.csv and results/random.csv; summary below (filled at the end of the box).
