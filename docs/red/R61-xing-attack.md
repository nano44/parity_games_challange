# R61: attack on L-NEW box 27 (C, FBL, FBF, XA, CR) and the counts (CYC-u*) / (NH) (L-RED successor 14, box 31; started 2026-10-24 15:00Z, date -u)
Target (Lead GO 14:48Z, updates 15:00Z / 15:23Z / 15:48Z): attack L-NEW's lemmas C, FBL, FBF and XA (docs/new/N5-xing-box27.md @ l-new
1322d958, now on trunk). Find a family with super-linear θ-changes in one joint λ-phase, ideally inside one (w, u*)-run (CYC-u*),
or with many non-(h) transitions (NH). Labels per L40. No running-time claim. G-N5-TIME stays OPEN.

## 0. Method
- experiments/red/xing/xclimb.py: a hill-climb on o-cyclic 𝒞^1O from the canonical start, using L-NEW's mutate.
  - L-NEW's checkers are imported UNMODIFIED from a detached worktree of l-new 1322d958:
    - coarsecheck.run: Lemma C / CR / XA, i.e. C1 (coarse Ξ = coarse W), C2 (last coarse change ≤ n − 1), C3 (re-entry ⇒ strict
      coarse rise). Run twice, with stretches cut at fallbacks and with --withfb, because Lemma C claims "fallbacks included" while
      the checker's default cuts at them.
    - fbfcheck.run: Lemma FBF (ENTRY_AFTER_FB, ROUTE_CHANGE_AFTER_FB).
    - fbedges.run: Lemma FBL (OTHER edges, fallbacks without a leave).
  - Fitness: (violations, exercise). The exercise term depends on --target:
    - lemmas = throttled (h)-fallbacks + post-fallback transitions + re-entries;
    - nh = non-(h) transitions per phase;
    - cyc = (θ, w)-stretches per phase;
    - cycu = (θ-changes inside one (w, u*)-run, θ-changes per phase);
    - reent = throttled re-entries.
  - The (w, u*)-run is my own count. It agrees with the Lead's per-phase numbers (s_tp32_final 35, sc32 32, cycelim_cex_n32 24,
    theta_tp32 16) and with L-SI's 17-in-one-run on inr2_n32 (sha1 9689990d…).
- experiments/red/xing/nhwhy.py: why (h) fails at each state of the longest phase: SB (o on a (σ, σ̄)-cycle), TAU (o on a
  (σ, τ)-cycle), CN (cycle nodes of Ξ(o) and W(o) differ).
- Every best is re-run with n5.py and with L-COMP's n5b.py (SPEC mode); the counts agree on all of them. Every best passes Oink
  zlk + verify.py (check_sol2.py).

## 1. Lemma attack: NO VIOLATION (DATA)
| climb | seed | n | budget | best | violations | exercise reached |
| --- | --- | --- | --- | --- | --- | --- |
| lemmas | elim24_p52 | 24 | 2,400 s | x31_lem_e24 (15c8211c…) | 0 | 4 throttled fallbacks, 43 post-fallback transitions; one throttled stretch of 50 transitions with 14 fallback leaves |
| lemmas | theta_tp32 | 32 | 2,400 s | x31_lem_t32 (60c15284…) | 0 | 5 throttled fallbacks, 48 post-fallback transitions; a stretch of 51 with 10 fallback leaves |
| nh | elim24_p52 | 24 | 2,400 s | x31_nh_e24 (169ad022…) | 0 | 21 non-(h) transitions in one phase |
| nh | random | 20 | 2,400 s | x31_nh_r20 (1fbb2add…) | 0 | 15 |
| cycu (×4) | §2 | 16-48 | 1,800 s | x31_cu16/24/32/48 | 0 | §2 |

- Seeds checked unmodified before climbing (elim24_p52 and seven earlier L-RED 𝒞^1O instances): 0 violations.
- Random games (L-NEW's --random 1500 8 16 731 --randstart) barely exercise the lemmas: 4 stretches in 1,500 games, so random
  sampling is not a test here.
- Long throttled stretches exist: 50 transitions at n 24 (2.1n) and 51 at n 32. That is within FBF's consequence (O(n³) per
  stretch) and its "≤ n leaves after the first fallback" (14 ≤ 24, 10 ≤ 32).
- No throttled re-entry inside a stretch was produced by any climb (reentries = 0, both cuts). This agrees with the referees'
  remark that Theorem XA has no data. The dedicated climb is in §3.

## 2. (CYC-u*) scaling (DATA; climbs, not a family; 1,800 s each, 4 cores shared)
| n | seed | θ-changes in one (w, u*)-run | θ-changes in one phase | per n (run / phase) | N5 iterations | best (sha1) |
| --- | --- | --- | --- | --- | --- | --- |
| 16 | theta_thf16 | 10 | 20 | 0.63 / 1.25 | 23 | x31_cu16 (5cd2d77d…) |
| 24 | elim24_p52 | 16 | 16 | 0.67 / 0.67 | 22 | x31_cu24 (80332de0…) |
| 32 | s_tp32_final | 21 | 40 | 0.66 / 1.25 | 49 | x31_cu32 (ab017611…) |
| 48 | s_tp32_final padded | 21 | 41 | 0.44 / 0.85 | 46 | x31_cu48 (a04a96d1…) |

- θ-changes inside one (w, u*)-run reach about 2n/3 and do not grow faster than n. Per phase they reach 1.25n.
- n 48 is limited by the budget: the padded seed gains little in 1,800 s. Continuation runs are in §2b.
- All four bests: 0 lemma violations, max non-(h) per phase 1.

## 3. (NH) (DATA and READING)
- Every non-(h) state the nh climbs find is SB+TAU: o lies on a cycle under both σ̄ and τ. Only frz24 (box 26) shows CN.
- Those phases are short: 21 states at n 24 and 15 at n 20, and the whole run is shorter than n (20 and 15 iterations).
- READING: with o on the cycle of both (σ, σ̄) and (σ, τ), o is a cycle node of both plays, so the band between θ and w vanishes.
  Such phases look like one-player phases of G_τ. A proof is L-NEW's; I have no counterexample.
