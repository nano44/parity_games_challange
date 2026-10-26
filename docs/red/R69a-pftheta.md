# R69a: PF-THETA, linear form, refuted (L-RED successor 15, box 39; Lead 09:42Z / 09:55Z; written ~10:35Z, date -u)
Target:
- L-NEW's CONJECTURE PF-THETA, docs/new/N5-DROP-box35.md §8 (l-new 3939d3b): "in a scope run, while the last fallback has level M, θ
  changes at most n times (for each M)".
- Linear form; report the ratio per n over at least three sizes.
𝒞^1O only: one Odd vertex with out-degree > 1, asserted. Referees were not contacted. Labels per L40. G-N5-TIME stays OPEN.

## Counter: experiments/red/so/sox5.py (written from §8; trace asserted equal to n5.run)
- Scope run, M_k and θ as in sox3.py (P-N5-CLS §0).
- Per scope run S and level M, a stretch starts after an in-scope fallback of level M. It runs through later fallbacks of the same level,
  up to the next in-scope fallback of a different level (exclusive) or the end of S.
- The θ-changes at the stretch's transitions are summed per (S, M).
- On L-NEW's bests it reproduces §9's numbers: pf_best_3621 / 3622 / 3623 give 31 / 35 / 32.
- Climber: soclimb5.py, fitness (count − n, fallbacks). One 30-minute climb from each L-NEW best, plus one at n 24.

## Result
| instance (experiments/red/so/instances/) | sha1 | n | it / fb | fallbacks in the run | max θ-changes under one level | ratio | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| pftheta_cex_n32.pg | 9f526135e272fabcb38c1cc24a99a4418717f7ed | 32 | 38 / 1 | 1 (M 31) | **33** | 1.03 | > n: KILL |
| pftheta34_n32.pg | b291d7bb23c4f795b991a44d8f0b9e43ccb24a79 | 32 | 39 / 1 | 1 (M 31) | **34** | 1.06 | > n: KILL |
| pft40_n40.pg | 147fef53ab78335775345a5c74688ad6f4d7d914 | 40 | 54 / 4 | 4 (M 39) | 40 | 1.00 | = n |
| pft35_n48.pg | 5e2bce834f586e5a5981ad7e1fd9d6285ad49e14 | 48 | 41 / 1 | 1 (M 45) | 35 | 0.73 | < n |
- Every row passed vrun.sh: n5 = n5b --mode spec; check_sol2 "zielonka(oink zlk) OK strategies verified"; one Odd choice vertex (o = 0).
- L-NEW's own pfclimb.fit, run unmodified from an l-new 3939d3b worktree, gives (33, 1) on pftheta_cex_n32 and (34, 1) on
  pftheta34_n32. On the seed it gives 31.
- The n 24 climb, from a seed with no in-scope fallback, reached a scope run with 22 fallbacks but 0 θ-changes after them.

## Labels
- FALSE (verified): PF-THETA, linear form (≤ n). 34 > 32 at n 32.
- DATA: the best ratios are 1.06 (n 32), 1.00 (n 40), 0.73 (n 48). There is no sign of super-linear growth: the counts sit near n.
  - The kills come after a SINGLE fallback, i.e. inside one fallback-free run, where X-RUN + TH already give a poly(n) bound. As L-NEW's
    §9 says, they break the constant 1, not the poly form.
  - pft40_n40 is the only best with several fallbacks under one level (4 fallbacks at M 39), and it sits exactly at n.
- CONJECTURE (unchanged, L-NEW): the poly form of PF-THETA. A form "≤ c·n" with a small c > 1 is consistent with all data here.
