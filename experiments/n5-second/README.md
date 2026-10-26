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

## A1-A10 against the SPEC (docs/new/N5-ssi-global.md "SPEC (EXACT ...)" S1-S5, l-new c66ce20; Lead 20:59Z)
| # | settled by | SPEC vs my reading | mode |
| --- | --- | --- | --- |
| A1 rank | S1 "rank(v) = position of v in V sorted by (Ω(v), v)" | same | both |
| A2 start | S3 (PGSolver best-reward, key (r(w), ±w)) | same (pgsolver_si initial_strategy_by_best_reward) | both |
| A3 dual | S1 last item ("owner swapped, Ω + 1") | same; ids/successor order: S1 "Successor and predecessor lists are in increasing index order" | both |
| A4 Iσ, Iτ | S2 | same (strict, under Ξσ / Ξτ on G^d) | both |
| A5 tie-break of the optimum | S1 (iv)-(v): Odd's choice is produced INSIDE the VJ procedure (longest path: first strict maximum in successor order; shortest: BFS first discovery; cycle node: first successor on the DFS cycle) | DIFFERENT: my reading took per vertex the best successor by (valuation, index) | orig = mine, spec = S1 |
| A6 old σ | S4 "both steps computed from the SAME (σ, τ), applied together" | same | both |
| A7 fallback | S4c "maximising (Ξσ(w), w)" | same (PGSolver switch-all best, ties to the larger index) | both |
| A8 iterations | S4 "one iteration = one pass with Iσ ∪ Iτ ≠ ∅" | same | both |
| A9 output | S5 "Odd's strategy = σ̄ ... to the FINAL σ (Not τ)" | same choice of strategy; in spec mode σ̄ is S1's procedure choice | both |
| A10 valuation by reference to code | S1 now states the procedure in text (still citing si.py lines 78-205; "as in Friedmann 1106.0778 §3") | settled except as below | - |
STILL OPEN / unclear in the SPEC text (findings against the spec):
- S1 P-order: "signed weight Σ ±2^rank" is unit-cost big-integer arithmetic as written; equivalent to comparing the most relevant
  element of the symmetric difference (what pgsolver_si.py does, O(n) bit cost). The spec should say which, given TARGET §3.
- S1 (i)/(v): "DFS ... visiting only alive vertices of rank < rank(v)": the DFS visited-set is shared across v's successors (my
  reading, as PGSolver) or fresh per successor; it does not change WHETHER v is a cycle node but can change WHICH successor (v)
  picks. Not stated.
- S1 (iv) longest path: "recursion over successors": the restricted graph can still contain cycles away from v (vertices of rank
  < rank(v) that are not cycle nodes); the text does not say why the recursion terminates (it does in practice on all games run).
- S5 does not say what σ̄ is on a vertex where both the (iv) and (v) rules could apply; I use (v) for the cycle node only.

## Results
Snapshot 2026-10-18 23:50Z (tc spec mode still running at N = 26). Per row: game regenerated from L-NEW's `gen`, sha1 equal to
L-NEW's CSV on every row; regions = pinned Oink zlk (tl where zlk fails); both players' strategies verified by harness/verify.py.
"equal" = n5b iterations AND fallbacks equal to L-NEW's CSV. "noref" = Oink zlk and tl both did not finish (tc N = 25, 26; zlk and
tl time out at 300 s); there the strategies are verified (which certifies the regions) and at N = 25 the regions equal Oink dtl's.
Rows stop where L-NEW stopped (its BUDGET600 marker) or at this lane's 900 s (orig) / 600 s (spec) budget.
| family | orig: rows (equal / COUNT) | spec: rows (equal / COUNT) | largest N run (spec) | wrong region/strategy | repeated state |
| --- | --- | --- | --- | --- | --- |
| counter_core | 22 / 0 | 22 / 0 | 22 | 0 | 0 |
| counter_dp | 40 / 0 | 40 / 0 | 40 | 0 | 0 |
| counter_m | 40 / 0 | 40 / 0 | 40 | 0 | 0 |
| counter_ortl | 29 / 0 | 29 / 0 | 29 | 0 | 0 |
| counter_qpt | 40 / 0 | 40 / 0 | 40 | 0 | 0 |
| counter_rob | 1 / 18 | 19 / 0 | 19 | 0 | 0 |
| counter_rr | 40 / 0 | 40 / 0 | 40 | 0 | 0 |
| counter_symsi | 22 / 0 | 22 / 0 | 22 | 0 | 0 |
| recursiveladder | 40 / 0 | 40 / 0 | 40 | 0 | 0 |
| switchallexp | 40 / 0 | 40 / 0 | 40 | 0 | 0 |
| switchbestexp | 22 / 0 | 20 / 0 | 20 | 0 | 0 |
| tc | 7 / 17 (+2 noref) | 24 / 0 (+1 noref) | 25 | 0 | 0 |
| tc+ | 15 / 0 | 15 / 0 | 15 | 0 | 0 |
| dlm1 | 40 / 0 | 40 / 0 | 40 | 0 | 0 |
| dlm2 | 21 / 0 | 21 / 0 | 21 | 0 | 0 |
| deeptrap | 35 / 0 | 34 / 0 | 34 | 0 | 0 |
| padsae | 40 / 0 | 40 / 0 | 40 | 0 | 0 |
| total | 494 / 35 (+2 noref) | 526 / 0 (+1 noref) | | 0 | 0 |

Random games (results/random_orig.csv, random_spec.csv; `gen.py corpus out/rand2k 2000 20261018 --nmin 1 --nmax 120`, sha1 per
game): 2,000/2,000 correct in BOTH modes (regions = Oink zlk AND harness/zielonka.py, both strategies verified, no repeated state).
orig: max 11 iterations, 4 fallbacks in total (4 games); spec: max 11 iterations, 244 fallbacks (240 games). Iterations equal on 1,666
games, spec higher on 296, lower on 38 (|diff| <= 5). L-NEW has not run these files; its n5.py can be compared on the same sha1s.

Findings: (1) n5b in SPEC mode reproduces L-NEW's iteration and fallback counts on every row run of all 17 families; (2) in my
original reading (A5: optimum ties by (valuation, index)) counts differ only on counter_rob (2N vs 3N+1) and tc (both directions),
regions and strategies always right: the counts depend materially on the tie-break, the correctness does not; (3) the tie-break
moves the fallback rate on random games from 0.2% (orig) to 12% (spec) of games.

## Full state-sequence diff against n5.py (gauntlet step 2 completion; Lead 2026-10-26 01:53Z; seqdiff.py)
n5b.py (SPEC mode, unchanged since b49c9fc; written from the spec text only) against L-NEW's n5.py via n5x.trace(check=True) (n5.py's
loop, asserted equal to n5.run): per run, the FULL sequence of (sigma on Even, tau on Odd) states, the iteration count and the fallback
count. Starts: canonical; or a .start file (vertices it leaves out keep each implementation's OWN canonical choice); or one seeded random
start pair. DATA (exact on the listed inputs):
| input | runs | state sequences equal | counts equal | max iterations | fallbacks (total) | max n |
| --- | --- | --- | --- | --- | --- | --- |
| library: every experiments/**/*.pg with n <= 300 (out/ excluded; 8 files n > 300 and 1 unreadable skipped), .start when present (58) | 810 | 810 | 810 | 121 | 1,034 | 288 |
| rand_check corpus (gen.py corpus 2000 20261018 --nmin 1 --nmax 120; sha1s = results/random_spec.csv), canonical start | 2,000 | 2,000 | 2,000 | 11 | 244 | 120 |
| random C^1O (REFEREE-2 re_check.rand_game, 10,000 games, n 3-60, seed 20261026), canonical + one random start each | 20,000 | 20,000 | 20,000 | 10 | 1,416 | 60 |
Total 22,810 runs, 0 differences, 0 timeouts, 0 errors. The first library pass had 1 difference and 1 error, both harness-side:
dlmm_ML_L6.start is in L-SI's bare 'v:w' format (my reader parsed nothing) and fbh_drop9.start is partial (n5b needs every vertex);
fixed in seqdiff.py's reader (not in n5b), after which both are equal. Results: results/seqdiff/{lib,corpus2k,c1o10k}.json.
