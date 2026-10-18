# N1 DISC-ANNEAL: discount annealing with warm-started strategy iteration (L-NEW, 2026-10-18; written before code)

Status: IMPLEMENTED (experiments/new/anneal.py), UNDER TEST. Not killed on the data below; no claim. Treated as wrong until it passes the
gauntlet (D1). No running-time claim is made here.

## Exact pseudocode
Input: parity game G = (V, V_E, V_O, E, pr), n = |V|.
1. Rewards r(v) = n^pr(v) if pr(v) is even, -n^pr(v) if pr(v) is odd (Jurdziński's weights; Θ(d log n) bits each).
2. sigma := the best-reward start of L-SI's engine (each Even vertex to its successor of best reward; index ties).
3. For j = 1, 2, 3, ...:
   gamma_j := 1 - 2^-j (exact rational).
   Discounted game D_j: payoff of a play v0 v1 ... = sum_t gamma_j^t r(v_t); Even maximises, Odd minimises.
   Inner loop (Howard / switch-all strategy iteration for Even on D_j, warm-started at sigma):
     a. tau := Odd's optimal counter-strategy to sigma in D_j (one-player deterministic discounted game; solved
        exactly by Odd's own switch-all policy iteration started from Odd's previous tau, exact lasso evaluation).
     b. x := values of (sigma, tau) (exact rationals: lasso sums).
     c. for every Even vertex v: best := argmax_{w in E(v)} x(w) (ties: keep sigma(v), then smallest index).
        If x(best) > x(sigma(v)), set sigma(v) := best. (r(v) is common to all edges of v, so gamma*x(w) decides.)
     d. If no vertex switched: sigma is optimal in D_j; leave the inner loop.
   Stop test (a certificate, independent of any threshold theorem): win(v) := Even iff x(v) > 0; if sigma restricted to
   Even's region and tau restricted to Odd's region pass the strategy check of experiments/harness/verify.py (closure, and
   no cycle won by the opponent in each one-player restriction), STOP.
   (First version used "sigma has no Vöge-Jurdziński improving switch"; dropped 09:3xZ: a correct sigma need not be
   VJ-optimal, and on tc 4 the discounted optimum stabilised at j = 102 without ever being VJ-optimal.)
4. Output: the certified regions and both positional strategies; additionally compared with Zielonka in every test.
No priority merging: rewards use the input priorities. (anneal.py's default merges consecutive equal-parity priorities;
that variant is N1m and is NOT the candidate, see "Confound" below. All N1 data use --nocompress.)
Correctness of the output rests only on the certificate of step 3. Termination: for gamma >= gamma* (a threshold
depending on n and the rewards) the discounted optimum is parity-optimal [source needed: Puri / Zwick-Paterson, not yet
opened; used only for termination, and the stop test makes the output correct regardless].

## Why it is new against RANKING.md and the dead ends
- The fleet's SI lane (S1-S7, docs/si/) used Vöge-Jurdziński valuations, i.e. the gamma -> 1 limit, from fixed starts.
  S4 used a subgame optimum as start (DE8). No lane solved a sequence of discounted games with growing discount and warm
  starts. RANKING row 4 lists SI/LP/LCP; discount annealing as a schedule is not in it.
- DE8 (S4) showed that a start which is optimal for a DIFFERENT game (subgame) restarts Friedmann's counter at zero.
  N1's warm start is optimal for the same arena with a slightly shorter horizon; whether that also resets the counter is
  exactly what the first experiment tests.

## Barrier statement draft (honest)
- B1/B2/B3 (separators, universal graphs, black-box nested fixpoints): outside; values are discounted rationals, not
  automaton states or fixpoint queries. Says nothing about running time.
- B8 (classical SI, named rules): INSIDE in part. Each inner loop is switch-all (Howard) on a discounted game. HMZ
  1008.0530 Thm 6.5 bounds it by (m+1)(1 + log_{1/gamma}(n^2/(1-gamma))) = O(m 2^j j) at gamma_j: polynomial for each
  fixed j, exponential at the last j ~ d log n. Friedmann's families defeat switch-all for discount near 1 from his start
  (HMZ §7: "exponential for non-discounted 2TBSG, or when the discount factor is part of the input"). N1 is outside B8
  only through its start (the previous phase's optimum); the adversary still owns the game. This is the weak point.
- B9 (index-based single switch): outside (multi-switch, valuation-based). B10: deterministic. B11: not symmetric.
- B12: all-switches path prediction is PSPACE-complete; N1 uses all-switches inner loops, so its run is not predictable
  either; this is no iteration bound.
- B13 (Lemke / Cottle-Dantzig): FJS 0909.5653's Lemke is a homotopy in the covering parameter z at fixed discount
  (p.5: "how much further z can be decreased before σi ceases to be optimal"); N1 moves the discount itself. Outside as
  stated; no transfer argument either way.
- B14-B17: not applicable (no abstract cube; not an IPM; no automaton; complexity-class rows say nothing).
- Bit cost: gamma_j has j bits; lasso values have O(n j + d log n) bit numerators/denominators. Polynomial per step.

## Cheapest family expected to kill it
Friedmann's switchallexp (experiments/hard-families/pgsolver_port.py; switch-all from best-reward takes 10, 30, 70, ...
at N = 1..). If the last phases replay the counter, inner iterations double per N. Second: switchbestexp; then
randomfacetsubexp, M_L, gated_* (L-SI's bench), tc/counter_* (Oink).

## Data (2026-10-18, unrefereed, single implementation; regions = Zielonka and strategies verified on every row)
switchallexp (Friedmann's switch-all family; PGSolver port), Even switch-all iterations:
| N | n | plain VJ switch-all (vjfast) | N1 total | N1 largest phase | ablation: discounted switch-all straight at N1's final gamma |
| --- | --- | --- | --- | --- | --- |
| 2 | 35 | 30 | 25 | 9 | 30 |
| 3 | 49 | 70 | 42 | 11 | 70 |
| 4 | 63 | 150 | 64 | 13 | 150 |
| 5 | 77 | 310 | 90 | 15 | 310 |
| 6 | 91 | 630 | 120 | 17 | 630 |
The ablation reproduces Friedmann's counts exactly, as his transfer theorem predicts (1106.0778 §9, Thm 9.5 + Lemma 9.6,
1-sink games, rewards (-|V|)^Ω, discount close to 1). So the gain on this family comes from the annealing schedule, not from
the discounted objective. Full bench sweep: experiments/new/out/anneal/summary.csv (run_anneal.sh), recorded when done.

## Confound found and removed (09:45Z)
Merging consecutive equal-parity priorities (N1m) ALONE makes plain VJ switch-all polynomial on switchallexp: 10, 7, 9, 11, 13
iterations for N = 2..6 (vjfast on compress.py output) vs 30..630 on the input. Merging creates equal priorities, which the
engine ranks by index, so the counter's order breaks. An adversary blocks merging with isolated dummy vertices of the missing
parities, so merging is no defence and N1 is tested without it.

## Delay transform (candidate killer, experiments/new/delay.py) — did not kill (N1m data, N = 1..3)
Each Even choice edge subdivided by a chain of L Odd single-successor vertices (priority 0 on the start edge, 1 otherwise,
originals shifted by +2). Uniform L = 8, and L = 1 + 24·pr(w)/max or 1 + 24·(max - pr(w))/max: plain switch-all unchanged
(10, 30, 70); N1m 15/21/30, 15/24/34, 14/26/33, largest phase 2N+3 in every variant. Reading: N1 reveals a decision when
gamma^t · n^Δp outweighs the closer rewards, i.e. at horizon about t / (Δp ln n); uniform or monotone delays keep the
ORDER of reveals, so they do not force the counter into one phase. A killer must equalise reveal times (delay ∝ Δp per
decision), which needs chains of length ~ horizon · Δp · ln n per edge: polynomial, but beyond the exact Python engine.

## Further killer attempts (10:00-10:20Z, --nocompress), none killed
- Priority spreading p -> K p (experiments/new/spread.py), K = 3, 9, switchallexp N = 2..5: N1 counts identical to K = 1
  (25, 42, 64, 90); only the number of phases scales by K. The run depends on the order of reveals, not their horizon.
- Bit-indexed delays (bitdelay.py; chain c(i+1) or c(N-i) on edges of bit i's Even vertices, c = 2): plain VJ 15, 35, 75;
  N1 26, 44, 69 and 25, 43, 64 (N = 2..4); c = 8, N = 2: 26.
- Per-edge delay hill climb (delay_search.py, delays 0..12, switchallexp N = 2): best 49 Even iterations after 155 steps
  (base 25; plain VJ 30 on the undelayed game). Running; N = 3 next. A higher count at fixed N is not a family.
