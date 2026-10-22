# R52: longest DTL phase S against n on two-player games (box 20; L-RED successor 11; produced on Opus 5.5, D15 / L37)
Status: DATA, unrefereed. Started 2026-10-22 07:34Z (date -u) on the Lead's GO for box 20: GAP-A directly on S growth in two-player
games, no 𝒞^1P restriction; exponent fit across n = 20, 30, 40, 60, 80.
Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7. S = the longest phase (maximal run of searches of one player
with no dominion before its last search; L-ALG's dtl_phasestats convention, read through experiments/red/carry/spp.py, unmodified).
Tools (experiments/red/sgrow/): smeasure.py (S, |G'| and iterations in BOTH orders via L-ALG's code, plus pinned Oink -v even / odd
iterations and 'verified'); oclimb.py (climb at fixed n; fitness from pinned Oink: F = max(even, odd iterations) − dominions, a lower
bound proxy for S; moves: add / remove edge, change priority in 0..2n−1, flip owner; neutral padding to grow n).

## 1. Structured families (logs/families_S.txt; both orders identical on every row; Oink verified)
| family | sizes n | S | reading |
| --- | --- | --- | --- |
| tc N = 2..6 | 22, 42, 68, 100, 138 | 2, 3, 3, 3, 3 | constant |
| tc+ N = 2..6 | 24, 54, 104, 180, 288 | 2, 4, 5, 6, 7 | N + 1 ≈ log n |
| counter_core, _dp, _m, _ortl, _qpt, _rob (N = 3, 5, 8) | 6-259 | 1 | constant |
| counter_rr / counter_symsi (N = 3, 5, 8) | 12-82 | 2 / 3 | constant |
| lagfam D = 2, 4, 8, 12 (L-RED R39) | 36, 50, 78, 106 | 9, 11, 15, 19 | D + 7 ≈ n / 7 |
| L-ALG spp_final_n20/30/40/60 (oink order) | 20, 30, 40, 60 | 19, 19, 19, 14 | prior climb bests |
| L-RED spp25_oink_n40 (R24) | 40 | 25 (stable 23) | prior best at n 40 |
- The published hard families (built against other solvers) give S ≤ 7. None grows faster than log n.

## 2. Climbs (2026-10-22 07:42Z-09:57Z by date -u; at most 2 jobs; logs/ holds every gain line)
| run | start | n | wall clock / steps | best F | note |
| --- | --- | --- | --- | --- | --- |
| c_n20_s1 | L-ALG spp_final_n20 | 20 | 40,000 steps | 20 | → s21_oink_n20 |
| g_n20 | spp_final_n20, seed 3120 | 20 | 600 s, 34,859 steps | 19 | → s20_n20 |
| c_n30_s1 | spp_final_n30 | 30 | 40,000 steps | 27 | |
| g_n30 | spp_final_n30, seed 3130 | 30 | 600 s, 28,557 steps | 28 | → s29_n30 |
| c_n40_s1 | L-RED spp25_oink_n40 | 40 | ~50 min, ≥ 6,880 steps (stopped, no gain after 08:21Z) | 33 | → s34_oink_n40 |
| g_n40 | s28_n30 + 10 neutral pads | 40 | ~10 min, ≥ 2,415 steps (stopped) | 28 | seed for g_n60 |
| a_n60 | s34_oink_n40 + 20 neutral pads | 60 | 2,100 s, 1,461 steps | 35 | → s36_oink_n60 |
| g_n60 | g_n40 best + 20 neutral pads | 60 | 2,100 s, 6,268 steps | 31 | → s32_n60 |
| a_n80 | a_n60 best + 20 neutral pads | 80 | 2,400 s, 964 steps | 34 | → s35_oink_n80 |
| g_n80 | g_n60 best + 20 neutral pads | 80 | 2,400 s, 1,989 steps | 33 | → s34_oink_n80 |
- Random padding (07:42Z-08:12Z, runs c_n40_s2, c_n60_s2, c_n80_s2 in logs/) collapsed the seeds to F ≤ 8: random new vertices create
  early dominions. From 08:12Z padding is neutral (priority 0, one successor into the old game, no incoming edge).
- An Oink evaluation costs 8 ms at n 20 but 0.2-1.5 s on the long-phase games at n 40-80 (tangles stay ≤ 88), so the step budget falls
  from ~35,000 at n ≤ 30 to ~1,000-6,000 at n ≥ 60. The large-n numbers are the least converged.

## 3. Best S per n (pinned instances in experiments/red/sgrow/instances/; logs/pinned_S.txt; Oink -v verified on every row, and the
pinned Oink count of the player owning the long phase equals the oink-order S on every row)
| n | instance | sha1 | S oink order | S stable order | |G'| | Oink even / odd | S/n (oink) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20 | s21_oink_n20 | da164511784449b906663c190757fd78c057f97c | 21 | 11 | 20 | 21 / 1 | 1.05 |
| 20 | s20_n20 | f866f507922324408f37d6ccceb121fb51ee8a6c | 20 | 20 | 20 | 20 / 1 | 1.00 |
| 30 | s29_n30 | 172a4328ac96a78fc1669690e956e750c4a23485 | 29 | 29 | 30 | 29 / 1 | 0.97 |
| 40 | s34_oink_n40 | 22ddda182cb4dd20d93232f1c9a0bbaed28d50b4 | 34 | 30 | 40 | 2 / 34 | 0.85 |
| 60 | s36_oink_n60 | 79db9615438e8913c7dc3646bd41833a860c2359 | 36 | 34 | 60 | 3 / 36 | 0.60 |
| 60 | s32_n60 | a74ac6e870e462cdaa8b0f9f2cecb1e299123dbe | 32 | 31 | 60 | 32 / 1 | 0.53 |
| 80 | s35_oink_n80 | 1fcf6967a8755ddc4101084c0b21d3e683b7a7cb | 35 | 33 | 80 | 3 / 35 | 0.44 |
| 80 | s34_oink_n80 | 6fbbeec64726387ed7aaaf3ef1175b9d7fa73b35 | 34 | 32 | 80 | 34 / 1 | 0.43 |
- Exponent fit (least squares of log S on log n over the best per n = 20, 30, 40, 60, 80): slope 0.36 (oink order: 21, 29, 34, 36, 35),
  0.34 (stable order: 20, 29, 30, 34, 33). With the budget caveat of §2, the best S is ≤ n at every n ≥ 30 and S/n falls with n.
- s21_oink_n20 is a new DATA point against (SPP) "S ≤ |G'|" (R24's target, DATA only, never a signed claim): in oink order an Even
  phase has S = 21 at |G'| = 20 (the 21st search learns nothing and ends the run; dtl_spp per-search tangles 3,1,1,2,1,4,1,1,1,3,1,1,1,1,
  1,3,1,1,1,1,0). Stable order gives S 11 on the same game. S − |G'| = +1: linear, not a growth signal.

## 4. Box-20 end (reading)
- No super-polynomial family, and no polynomial family above linear: the best S found grows like n^0.36 over n = 20-80 at this budget,
  and every structured family measured has S ≤ n/7 (lagfam) or S ≤ log n (tc+). S ≤ about n holds throughout, with one +1 excess at
  n = 20 in oink order.
- Limits: random-mutation climbs with an Oink proxy fitness; 2 seeds per n; small step budgets at n ≥ 60 (≤ 6,268 steps); two-player
  games only by construction (no class restriction); this is DATA and says nothing about GAP-A's proof status.
