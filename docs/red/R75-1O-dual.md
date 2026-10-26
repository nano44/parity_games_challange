# R75: adversary on P-N5-1O (start pairs, per-phase bounds, Lemma OUT vs Oink) and on P-N5-DUAL (Lemma DUAL, N5^OF): no kill (L-RED successor 19, box 45; Lead GO 01:05Z, date -u)
Targets: P-N5-1O (docs/si/P-N5-1O-box15.md, sha1 2cf5e672, pinned trunk 291c110d) and P-N5-DUAL (docs/new/P-N5-DUAL-box43.md,
sha1 a51f7c30). Labels per L40: DATA / READING. 𝒞^1O only, except the DUAL check, which covers any class. Nothing here proves a bound.
D1: the candidate is wrong until checked. This report checks; it does not sign.

## 0. Result
- **No kill.** 0 FAIL in every run, across every check:
  - the bounds of Theorem 1O-POLY and its inputs R47 (a), (b), R48 (i), R50 (h);
  - Lemma OUT against Oink;
  - Lemma DUAL and its second sentence.
- The runs come from the S3 start and from random and climbed non-S3 start pairs.
- Closest approaches (§3):
  - R47 (a) is attained with equality: τ changes = d_o − 1 = 18 (tau18_n24).
  - R48 (c) at 39 / 42 in-phase fallbacks on an o = c_θ phase with |U| = 42 (f39_n48). The same phase is 1 below CONJECTURE FB-CAP's
    max(1, |U| − 2) = 40.
  - Phases: 50 at n 32, against R47 (b)'s 1,005. Above the "at most 30 phases" data note that P-N5-1O §2 quotes.
  - Iterations from a start pair: 118 at n 48 (S3 on the same game: 18). One phase alone has 114 transitions.
- Two wording points (§4), neither a gap in P-N5-1O:
  - (W1) the deg_U(o) versus |succ(o) ∩ Û| transcription in R48 / §1;
  - (W2) R27 (g)'s scope is λ_Ξ(o) ≠ o, but R50 (h) is used on every phase.

## 1. Tools (experiments/red/o1/, written from the packet texts; engine si.py read-only)
- o1_19.py (sha1 3803037a): own copy of n5.py's loop (`trace`), with an N5^OF switch (`--of`). Per run it computes:
  - ITER, and the bound ITER* = (n(n − 1) + d_o)(T* + 1), with T* from §2's chain at F = 2n² (exact big integers);
  - phases (maximal runs with (λ, τ) constant), against R47 (b) n(n − 1) + d_o;
  - τ changes, against R47 (a) d_o − 1;
  - per phase: f = in-phase Even fallbacks, against R48 (i) (a)-(c). Two forms are checked: FBPOLY's deg_U(o) = |succ(o) ∩ U|
    (FB_R48), and the RESULTS / §1 wording |succ(o) ∩ Û| (FB_R48hat). Also f ≤ F, and the FB-CAP slack f − max(1, |U| − 2);
  - per phase: T = in-phase transitions, against R50 (h) evaluated at the phase's own f;
  - per phase: Θ = Ξ(o) changes and S_o = relevant σ̄(o) changes (R27's definitions), with S_o ≤ d_o(Θ + 1). On o = c_θ phases,
    Θ = S_o = 0 (§4 W2);
  - N5 only: no Odd fallback inside a phase;
  - Lemma OUT, three checks:
    - W = {v : Ω(λ(v)) even} at the stop equals the output regions;
    - harness/verify.py: closure plus a one-player cycle test, for σ on W and σ̄ on V ∖ W;
    - Oink 8fbf0a7: `--zlk` (falling back to `--tl`) for W_E, and `oink --no -v --sol` on the written solution, which verifies
      both strategies. Sensitivity checked: a corrupted region is rejected (MISMATCH), as is a strategy leaving its dominion (Oink:
      "strategy leaves dominion").
- climb19.py (293a9a63): hill climb on (game, start pair) at fixed n. Mutations: a priority, an Even successor set, succ(o), a start
  entry, owner swaps that keep 𝒞^1O. Objective: one field of o1_19, or an expression over its fields. Every candidate gets all of
  o1_19's bound and OUT checks except Oink; every improvement is re-run with Oink.
- lib19.py (b3cedbba): library sweep. 𝒞^1O files with n ≤ 80, each run from S3 and 10 random start pairs, Oink on every run.
- dual19.py (f8374ae6): Lemma DUAL on our engine, for any class. For a start vector st, it compares three runs:
  - A = N5 on G from st;
  - B = N5^OF on G^d from st (the same per-vertex vector is the mirrored pair);
  - C = N5 on G^d from st.
  It checks A = mirror(B) statewise, and that A and mirror(C) first differ at j + 1 for the first two-sided fallback j → j + 1 of A
  (no difference if A has none). Two-sided means Iσ ≠ ∅ and Iτ ≠ ∅ at an S4c fallback.
- Library: lib41 (experiments/new/box41/lib41.txt) plus every .pg under experiments/red, experiments/new/box42-43, experiments/si,
  docs/referee and docs/referee-2. That is 705 files: 506 are 𝒞^1O with n ≤ 80; 665 have n ≤ 80 (any class, for DUAL).

## 2. Runs (every count is 0 FAIL)
| run | what | runs | Oink |
| --- | --- | --- | --- |
| lib19 N5 | 506 𝒞^1O files × (S3 + 10 start pairs) | 5,566 | every run |
| lib19 N5^OF | same files and counts, Odd-first tie rule | 5,566 | every run |
| o1_19 rand seed 11 | random 𝒞^1O, n 4-14, S3 + 20 start pairs per game | 354,375 | every run |
| o1_19 rand seed 12 | random 𝒞^1O, n 14-30, S3 + 8 start pairs | 329,121 | every run |
| o1_19 rand seed 44 --of | random 𝒞^1O, n 4-16, N5^OF, S3 + 10 start pairs | 260,843 | every run |
| climbs (9 run to completion, 1,800-2,700 s each; 2 early random-seed climbs stopped by me, not counted) | objectives ITER, fcap, PH (×2), TAU, fmax, fcap·1000 + fmax (×2), fslack·1000 + fmax; seeds: library bests and the pins | 5,425,967 evaluations | at each improvement |
| dual19 rand | random games with k = 1..4 Odd choice vertices, n 4-12, S3 + 5 start pairs | 82,482 | n/a |
| dual19 lib | 665 library files (any class) × (S3 + 3 start pairs) | 2,660 | n/a |
- DUAL: 0 violations of the first sentence (A = mirror(B)) in 85,142 runs. Two-sided fallbacks occurred in 129 runs (29 random,
  100 library). In every one, the plain mirror (C) first differs from A at exactly j + 1. With no two-sided fallback it never differs.
  This matches L-NEW's mirror.py data on an independent engine copy.
- Climb evaluations count Lemma OUT with harness/verify.py on every candidate; Oink runs only on the improvements and the pins.

## 3. Maxima and regimes (DATA)
| quantity | max seen | where (start) | landed bound there | ratio |
| --- | --- | --- | --- | --- |
| ITER | 118 (n 48, m 178, d_o 4) | iter118_n48 (start pair; S3 gives 18) | ITER* ≈ 5.6·10²⁷ | ~ 10⁻²⁶ |
| ITER / n | 2.75 | s_elim24_final (S3) | — | — |
| phases | 50 (n 32, d_o 13) | ph50_n32 (start pair; S3 gives 32) | R47 (b): 1,005 | 0.050 |
| τ changes | 18 (n 24, d_o 19) | tau18_n24 (start pair; S3 gives 11) | R47 (a): d_o − 1 = 18 | **1 (tight)** |
| in-phase Even fallbacks f | 39 in one phase, o = c_θ, \|U\| = 42 | f39_n48 (start pair; S3 gives f = 0) | R48 (c): \|U\| = 42 | 0.93 |
| FB-CAP slack f − max(1, \|U\| − 2) | 0, only at \|U\| ≤ 3 with f = 1; −1 at \|U\| = 42 (f39_n48) | many | CONJECTURE, not landed | — |
| R48 slack f − bound | 0, only in phases with f = 1 | df_cex (S3) and random | R48 | — |
| T per phase | 114 (iter118_n48) | start pair | T* ≈ 10²⁴ | ~ 10⁻²² |
| T / (m − n + 1) | 1.61 | returns_ph64 (S3) | R50 (h): (T_rel + 1) | — |
| Θ, S_o per phase | 60, 52 | rise_thin51_n40 (S3) | S_o ≤ d_o(Θ + 1): never violated | — |
- Regimes reached: o = c_θ phases with large |U| and many fallbacks (f39_n48); long single phases from start pairs (114 transitions);
  phase counts up to 50; Odd-first runs on the whole library. N5 never had an in-phase Odd fallback (FIX 3 / Φ-1O, as expected).
- What a start pair changes: in 4 of the 5 pins the start pair raises the count well above S3 on the same game (ITER 118 vs 18;
  f 39 vs 0; τ changes 18 vs 11; phases 50 vs 32 and 45 vs 22). So the S3 data in RESULTS undersample these regimes. The start-free
  reading of the bounds (R-N5-START) is what carries them, and the data agree.
- Growth (READING): nothing here approaches the polynomial bounds. The bounds are loose by ~20 orders of magnitude at n ≈ 50, and the
  climbs found no length law. The tightest landed bounds are the two small ones, R47 (a) (attained) and R48 (c) (93 %).

## 4. Wording points (READING; for the referees of P-N5-1O and the RESULTS keeper)
- (W1) R48 / P-N5-1O §1 versus P-N5-FBPOLY.
  - FBPOLY (§0, line 48; Theorem FB-POLY (a), line 230) proves f ≤ 1 + (|U| − 2)(deg_U(o) + |U|) with deg_U(o) := |succ(o) ∩ U|.
  - RESULTS R48's headline and P-N5-1O §1 write |succ(o) ∩ Û|, Û = U ∖ {o}. That is smaller by 1 exactly when o has a self-loop, so
    it is a stronger claim than the one proved. Neither form fails in any run (FB_R48 and FB_R48hat both 0).
  - Conversely, FBPOLY's step "deg_U(o) ≤ n − 1" (line 239), giving "≤ 1 + (n − 2)(2n − 1)", fails when o has a self-loop and
    succ(o) ⊆ U = V. Then deg_U(o) = n.
  - P-N5-1O is unaffected: F = 2n² ≥ 1 + (n − 2)·2n (+ 1 for any phase-ending fallback) for every n ≥ 1.
- (W2) R50 (h) cites "Θ and S_o (R27 (g))", but R27 (g) is signed only "per phase with λ_Ξ(o) ≠ o". P-N5-KW §8 says "Θ = 0 if c_θ = o
  (R27 (g) TH)". On an o = c_θ phase both counts are 0 by R27's own definitions:
  - θ = Ξ(o) = (o, ∅, 0) is constant;
  - a σ̄(o) change is relevant only if λ(o) ≠ o.
  So R50 (h) holds there with Θ = S_o = 0. Data agree: Θ = S_o = 0 on every o = c_θ phase seen (check OC_THETA_SO, 0 FAIL). Not a
  gap; the citation should read "R27's definitions" for that case.
- Also checked, no issue:
  - Step 3's monotonicity in f (every term of §2's chain is non-decreasing in F);
  - §2's chain formulas against RESULTS R34 (e), (f) (T_H, X_SN), R30 (c) (X), R27 (g) (Θ, S_o) and R50 (h) (N_Ξ, N_st, W_ch). The
    packet's N_Ξ uses F + N_st where R50 (h) has f + (N_st − 1), a harmless overestimate;
  - Lemma OUT steps 2-4 against SPEC S1 / S2 and R36 (c).

## 5. Pinned instances (experiments/red/o1/instances/; start = per-vertex vector; n5py_start = n5.py's --start strings)
| file | sha1 | start sha1 | n5.py --start (iterations, fallback) | check_sol2.py |
| --- | --- | --- | --- | --- |
| iter118_n48.pg | 0457f71b0587932b72c627b8a7b4c8417dc3fdaf | f5d24476 | 118, 9 | zielonka(oink zlk) OK strategies verified |
| ph45_n32.pg | 6c6b90990d1ab74e512f5f1df8c6aefba127b570 | 47edb2d6 | 46, 20 | OK, verified |
| ph50_n32.pg | 9c510170e36000ddb6886aebe6eaf1f06fe33fd2 | 097e70a2 | 51, 20 | OK, verified |
| tau18_n24.pg | 3f1e1f92ebaecc0691fc9fe6461a1d837b6215bc | 80647292 | 18, 0 | OK, verified |
| f39_n48.pg | 4390ee571003e3842edc48810f2c228e71dbb044 | 0d988962 | 46, 39 | OK, verified |
Reproduce, from the repo root:
- `python3 experiments/red/o1/o1_19.py file experiments/red/o1/instances/f39_n48.pg experiments/red/o1/instances/f39_n48.start.json`
- `python3 experiments/new/n5.py n5 <pg> out.sol --start "<n5py_start[0]>" "<n5py_start[1]>"`, then
  `python3 experiments/new/check_sol2.py <pg> out.sol`.

## 6. Not done / next
- Item (3), the resume list, is not started: R74 §2.5 construction, FB-CAP |U| ≥ 3, beta2 cascade.
- f39_n48 is the new FB-CAP seed: f = |U| − 3 at |U| = 42 (previous best: equality f = |U| − 2 at |U| = 4, R71 §7). The climbs from it
  collapsed into trivial phases (f = 1) and did not improve the slack. Next: a climber that keeps |U| ≥ 3 and f ≥ 2 as hard constraints.
- R47 (a) is tight. A phase-count climber could aim at R47 (b)'s n(n − 1) term; 50 of 1,005 so far.
