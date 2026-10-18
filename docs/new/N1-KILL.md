# N1 KILL candidate: deep traps on switchallexp (L-NEW box 3, 2026-10-18 ~18:15Z by date -u). DATA, unrefereed

N1 = LS24 IncreasingDiscountPI on parity-induced rewards, experiments/new/anneal.cpp UNMODIFIED (the implementation that passed
step 2, docs/new/N1-step2.md). Family: Friedmann's switchallexp plus a "deep trap" on every Even choice vertex.

## The family (experiments/new/gen_deeptrap.sh N; deterministic, no seeds)
G_N = switchallexp(N) (experiments/hard-families/pgsolver_port.py) plus, for every Even vertex v with >= 2 successors, an extra
edge v -> t_v, t_v Odd with even priority P = B + 2 + 2k and the single edge t_v -> c_v, c_v an Odd self-loop of odd priority
q = B + 1 (B = max priority rounded up to even; experiments/new/alltrap.py), with k = floor(B/2) + 2. Traps lose for Even (the play
stays on c_v, odd top priority), so the winning regions on the original vertices are those of switchallexp (Odd wins everything).
n = 32N + 15; max priority 2B + 6 = O(N).

## Data (pinned: experiments/new/instances/killer/deeptrap_sae_N1..N7.pg, table deeptrap_sae.csv with sha1 per instance)
| N | n | sha1 (first 12) | N1 Even iterations | in how many phases | Odd iterations | phases | check |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 47 | f44eeb9c656e | 11 | 1 (all in one phase) | 3 | 184 | zlk OK, strategies verified |
| 2 | 79 | 99c96a0d913e | 31 | 1 | 8 | 309 | same |
| 3 | 111 | 594d25f5c9f4 | 71 | 1 | 17 | 442 | same |
| 4 | 143 | 8f6af4677bf0 | 151 | 1 | 34 | 580 | same |
| 5 | 175 | a7c6370227eb | 311 | 1 | 67 | 723 | same |
| 6 | 207 | 513427372388 | 631 | 1 | 132 | 870 | same |
| 7 | 239 | 835ce1326ca3 | 1244 | 1 | 261 | 1020 | same |
Even iterations 11, 31, 71, 151, 311, 631, 1244: ratios 2.8, 2.3, 2.1, 2.06, 2.03, 1.97, i.e. ~5·2^(N+1), all inside ONE phase
(anneal_c's nonzero=[...] lists one phase); n grows linearly, so ONE late phase makes 2^Θ(n) Howard switches. Plain VJ switch-all
on the same games (vjfast): 13, 33, 73 (N = 1..3), the same counter.
Re-run: `cd experiments/new; g++ -O2 -std=c++17 -o anneal_c anneal.cpp; ./gen_deeptrap.sh N > g.pg; ./anneal_c g.pg g.sol;
python3 check_sol2.py g.pg g.sol` (or check_sol.py for the Python Zielonka).

## Why it works (mechanism, unrefereed)
- Trap value at discount γ = 1 − 1/H: about n^P − H·n^q. While H < n^(P−q) it exceeds every real option (n^P dominates all original
  rewards and H n^q), so in every phase before release Even's optimum is "all traps" and Even's values are POSITIVE: the
  certificate (signs of values) cannot fire, although Odd wins everything. Phases before release: no Even switches.
- P − q = 2k + 1 > B + 2, so the traps release only after the horizon at which the original game's discounted order equals its
  parity order (Vöge / 1106.0778 Thm 9.5, Lemma 9.6). All traps release in the same phase (identical P, q).
- In that phase N1 runs Howard to the discounted optimum from "all traps" = the best-reward start, which is Friedmann's bad start
  for switch-all (box 1: plain VJ from best-reward start = all traps: 33, 73, 153, 313, 633, 1246). So the release phase replays
  Friedmann's counter. Box 1's trap runs (k = 1, 4) released too early (n^3, n^9), before the parity-like horizon, which is why they
  did not kill.
- Consistent with the ceiling (N1-step2.md): d grows with n and the long phase is late (2^j ≈ n^(P−q)).

## What a referee must check before this is called a kill
1. anneal.cpp against LS24 Fig. 12 / 2610.22149 Fig. 7.2 (box 1 transcription; the stop test here is the parity certificate,
   which fires no later than LS's mean-payoff-optimality test, so LS's version cannot stop earlier than this run).
2. The count is Even's Howard switches within one phase; each costs at least one evaluation of n exact values (bit cost only adds).
3. Robustness: the start strategy is irrelevant (traps dominate at the first phase); the schedule is irrelevant once a phase
   lands after release (any γ beyond the release horizon is parity-like for the original game).
