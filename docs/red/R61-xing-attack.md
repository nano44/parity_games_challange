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

### 2b. Continuations (PENDING: climbs from run_x_inr2 at n 32 / 48 running until ~17:20Z, date -u)
- All four bests: 0 lemma violations, max non-(h) per phase 1.

## 3. (NH) (DATA and READING)
- Every non-(h) state the nh climbs find is SB+TAU: o lies on a cycle under both σ̄ and τ. Only frz24 (box 26) shows CN.
- Those phases are short: 21 states at n 24 and 15 at n 20, and the whole run is shorter than n (20 and 15 iterations).
- READING: with o on the cycle of both (σ, σ̄) and (σ, τ), o is a cycle node of both plays, so the band between θ and w vanishes.
  Such phases look like one-player phases of G_τ. A proof is L-NEW's; I have no counterexample.

## 4. Throttled re-entries: the first data for Theorem XA (DATA; Lead 15:48Z: "Theorem XA has no data")
- x31_re24 (n 24, sha1 49eaf50e…; reent climb from x31_lem_e24, 1,800 s): 33 throttled re-entries inside one stretch, after arena
  leaves. All 33 have u* = none (P(θ) = P(w), only lengths differ), which is XA's side case. N5: 6 iterations, n5b agrees, Oink OK.
- x31_ru24 (n 24, sha1 d4be0710…; reentu climb, which rewards u* ≠ none, seeded from re24): 20 throttled re-entries with
  u* ≠ none after arena leaves, in one stretch of 3 transitions, with 0 C3 failures.
  - So Theorem XA's claim (strict coarse rise at each re-entry) holds on 20 real instances of its main case.
  - N5: 7 iterations, n5b agrees, Oink zlk OK, strategies verified. coarsecheck.py (both cuts) reproduces the 20.
- These are data for the referees, not a kill: the runs are short.

## 5. (FBRE-F) (L-NEW CONJECTURE, docs/new/N5-NH-box28.md §5b @ l-new 2a195b3)
- Statement checked: in a (w, u*)-run, no vertex evicted by a fallback at run index ≥ n − 1 re-enters R in that run.
- Checker: experiments/red/xing/fbref.py (my own run segmentation, L-NEW's step / Rset / wvals unmodified).
- It reproduces L-NEW's data: returns_rt48 and returns_ph64 have 11 post-freeze evictions each, and 11 resp. 13 pre-freeze FBRE.

| instance | n | longest run | post-freeze evictions | re-entries of them (VIOL) | fallback waves in a run |
| --- | --- | --- | --- | --- | --- |
| returns_rt48 | 48 | 66 | 11 | 0 | 14 |
| returns_ph64 | 64 | 91 | 11 | 0 | 15 |
| run_x_inr2 (L-SI) | 32 | 47 | 8 | 0 | 3 |
| x31_lem_e24 | 24 | 50 | 2 | 0 | 4 |
| x31_lem_t32 | 32 | 52 | 2 | 0 | 5 |
| fb32 climb (PENDING, ends ~17:20Z) | 32 | | | | |

- "Waves" counts fallback transitions that evict at least one vertex inside one run. rt48 / ph64 have many small ones, not just two.
- No violation. Seeds for a ≥ 3-wave straddle exist: x31_lem_e24 and x31_lem_t32 have 4-5 waves across the freeze.

## 6. m_r: θ-changes per level in the longest phase (experiments/red/xing/levels.py; Lead 16:45Z, L-SI box 3 k-digit target)
- Level of a θ-change = VJ rank of the most relevant vertex of P(θ_k) Δ P(θ_{k+1}); "len" = only the length changed.

| instance | n | θ-changes | path-set levels used | max m_r over path-set levels | length-only changes |
| --- | --- | --- | --- | --- | --- |
| run_x_inr2 | 32 | 43 | 14 | 4 | 13 |
| rx32 (climb from it) | 32 | 44 | 13 | 4 | 21 |
| rx48 (climb from it, padded) | 48 | 45 | 11 | 4 | 26 |
| cu48b | 48 | 49 | 11 | 4 | 22 |
| x31_cu32 | 32 | 40 | 12 | 6 | 11 |
| x31_cu32i | 32 | 38 | 12 | 4 | 8 |
| x31_cu16 | 16 | 20 | 7 | 4 | 6 |
| theta_tp32 | 32 | 16 | 8 | 4 | 2 |

- (x31_cu32's 6 is at rank 18.) On every instance the high levels change once each and the low levels at most 4-6 times. Counts do
  not double going down the levels, as a k-digit counter would need.
- The climbs' gains since run_x_inr2 are almost all LENGTH-only θ-changes (13 → 21 → 26), not new path-set levels.
- READING: length-only changes at a fixed (cycle node, path set) are monotone in length (shorter or longer by the cycle node's
  parity), so there are at most n of them per path-set value. They multiply the count by at most n and do not nest.
- So the data show at most a 2-digit pattern (L-SI's 27S / 24S re-fixing one lower block), with the lower digit capped at about 4.
  A k-digit counter is NOT observed. Designing one by hand (each higher SELF re-arming the whole lower block) is OPEN; I did not
  build it this box.

## 7. Verdict for box 31 (labels per L40)
- Mei port: no kill (R60).
- L-NEW lemmas C, FBL, FBF, XA (and CR's C2 consequence): no counterexample. DATA on 12 climbed and named instances, n ≤ 48.
- (FBRE-F): no counterexample. DATA: 34+ post-freeze evictions over six instances, 0 re-entries.
- (CYC-u*): θ-changes in one (w, u*)-run reach about 43-44 at n 32-48, i.e. at most about 1.35n, with no growth from 32 to 48. m_r ≤ 6.
  CONJECTURE (data only): θ-changes per (w, u*)-run are O(n). No super-linear family found.
- (NH): only SB+TAU non-(h) states, in short phases.
- G-N5-TIME stays OPEN.
