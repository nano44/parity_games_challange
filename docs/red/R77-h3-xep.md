# R77: adversary on P-N5-H3 (C2-H3, TC-CLASS, WM-G, FRZ-U_H3) and on P-N5-XEP's residual X_SN^pre: no kill; FRZ-U_H3 is tight (gap 0) (L-RED successor 19, box 45d; Lead 05:44Z, date -u)
Targets:
- P-N5-H3 (docs/si/P-N5-H3-box16.md, sha1 680e4528, the same on trunk and l-si; L-SI successor 11);
- P-N5-XEP (docs/new/P-N5-XEP-box44.md, trunk sha1 237dd5eb; L-NEW successor 23).
Both are lane-PROVED and unrefereed. Labels per L40: DATA / READING. Every game class. Nothing here proves a bound.

## 0. Result
- **No kill. 0 FAIL on every check, in every run**:
  - P-N5-H3:
    - R55 (a), Ξ = W on F_D (also the sanity check of my W computation);
    - TC-CLASS;
    - C2-H3, at every level L from max(M_D, −1) to n − 1;
    - WM-G;
    - FRZ-U_H3.
  - P-N5-XEP: R-STICK_D, SN-PREFIX_D (a), and the X-EP bound.
- The Lead's kill shape, "a fallback-free (h3_D) run of ≥ n states whose COARSE_L(W) moves after state n − 1", was never seen.
  - Define the gap as the index of the last COARSE_L(W) change in a qualifying run, minus (n − 1). The kill needs gap ≥ 1.
  - Best gap 0, i.e. the freeze index of FRZ-U_H3 is attained. Instances: frzgap0_n4 (n 4, a 4-state run whose coarse W changes at
    every step up to state 3) and frzgap0_n6 (n 6, by climb).
  - So the n − 1 of CR-D / FRZ-U_H3 cannot be lowered in general.
- FRZ-U_H3 non-vacuous (a qualifying run of ≥ n states):
  - library: 4 runs, longest 3 states beyond n (pftheta34_n32);
  - exhaustive sweep: 2 runs.
  L-SI's own data had none; L-COMP's frz1_n24 is reproduced (a 25-state run at n 24, the freeze holds).
- X_SN^pre:
  - per epoch: up to 69 (x32_waves48, n 48, S3; 1.44·n);
  - per S4a run: up to 36 by climb (xsnpre36_n48, n 48: 36 crossings in one run of one epoch, all unsplit, 0 fallbacks); 33 in the
    library (nleq33_n48);
  - X-EP slack at most −36 (exitdrop_n3).

## 1. Tool: experiments/red/h3/h3_19.py (written from the packets' §1-§6 / §0-§4; not from L-SI's gdnc.py / tcdir.py or L-NEW's rstick.py)
- Per state k:
  - Ξ_k, σ̄_k from SPEC S1;
  - W_k(v), computed from the (σ_k, τ_k)-play itself: on the lasso, the cycle node is the top-ranked cycle vertex, P is the prefix before
    its first visit ranked above it, and ℓ is the number of edges to it;
  - D_k, u(v), R_D, (h3_D), M_D, lev, COARSE_L, as in P-N5-H3 §1.
- Checks:
  - RD_A: Ξ = W on F_D (R55 (a));
  - TCC: λ_Ξ(v) = λ_Ξ(u(v)) and λ_W(v) = λ_W(u(v)) on R_D;
  - C2H3: at every (h3_D) state and every L ∈ [max(M_D, −1), n − 1], COARSE_L(Ξ) = COARSE_L(W) on V;
  - WMG: W_{k+1} ⊵ W_k at every in-phase S4a step;
  - FRZ: on every maximal fallback-free in-phase run with (h3_D) at all its states, with L := max(max M_D, −1), COARSE_L(W) is constant
    from state k0 + n − 1 on. Recorded: run length, gap;
  - XEP:
    - RSTICK: at in-phase S4a steps, every split v ∈ R_D(s) stays in R_D(s + 1);
    - SNPREFIX: within each S4a run, the unsplit states of each v form a prefix;
    - crossings; X_SN^pre per epoch and per S4a run, as defined in P-N5-XEP §4;
    - the X-EP bound per phase;
  - OUT: harness/verify.py.
- Calibration:
  - frz1_n24 (L-COMP, trunk experiments/n5-exhaustive/instances/, sha1 aad1bce6…) from its start: one non-vacuous qualifying run of
    25 states, freeze holds;
  - qc_toggle (sha1 27850ecc): 1 X_SN^pre crossing, as in P-N5-XEP §5.
- Drivers:
  - `h3_19.py lib seed R nmax files…` (H3BEST=file saves the best starts);
  - `h3_19.py rand seed count nmin nmax kmax`;
  - exh19.py: random small games × EVERY start pair;
  - climbs: experiments/red/fbr/climbfr19.py with ANALYSER=h3.

## 2. Runs (0 FAIL everywhere)
| run | what | runs | checks |
| --- | --- | --- | --- |
| lib (seed 13) | 625 library files with an Odd choice vertex, n ≤ 60 (of the 705 in R75 §1) × (S3 + 3 starts) | 2,500 | C2-H3 440,622; TC-CLASS 288,884; WM-G 19,413; FRZ runs 9,021 (4 non-vacuous) |
| lib (seed 15, with XEP) | same files, new starts | 2,500 | C2-H3 432,365; TC-CLASS 298,212; WM-G 19,526; R-STICK_D 39,469; SN-PREFIX 168,117; crossings 10,745 |
| rand (seed 14) | 20,000 random games with 2-4 Odd choice vertices, n 5-14, half from random start pairs | 20,000 | C2-H3 334,738; TC-CLASS 128,151; FRZ 30,864 (all vacuous) |
| exh19 (seed 131) | 150,740 random games, n 4-7, × every start pair (≤ 400 per game) | 8,204,394 | 2 non-vacuous FRZ runs; best gap 0 |
| climbs | FRZ gap from best_low_21 (×2), FRZ gap and length from frz1_n24 (×3), X_SN^pre per run from nleq33_n48 | ≈ 0.5 M evaluations | best gap 0; X_SN^pre per run 36 |

## 3. Pinned (experiments/red/h3/instances/; start.json = per-vertex start and n5.py strings)
| file | sha1 | n5.py --start (ITER, fallback) | check_sol2.py | what |
| --- | --- | --- | --- | --- |
| frzgap0_n4.pg | d67be0e3d8bfc8d4944e404a9d652b743bd46924 | 3, 0 | zlk OK, strategies verified | FRZ-U_H3 tight: qualifying run of n = 4 states, coarse W moves into state n − 1 |
| frzgap0_n6.pg | faab662b413b32bfcc7dab18d7a77c050e705069 | 5, 0 | OK, verified | the same at n 6 |
| xsnpre36_n48.pg | bca1f450539b9747ff47dea7775ef809f9b15b83 | 39, 0 | OK, verified | 36 X_SN^pre crossings in one S4a run of one epoch |

## 4. READING
- FRZ-U_H3 / CR-D: the bound "constant from k0 + n − 1" is exact in the worst case (gap 0 attained at n 4 and n 6). A kill needs a coarse
  W move at index ≥ n of a qualifying run; none in 8.2 M exhaustive-start runs at n ≤ 7, nor in the climbs.
- X_SN^pre is the live residual: 36 unsplit crossings in one fallback-free run at n 48, i.e. 0.75·n per run, and 69 per epoch.
  - Nothing in the data grows faster than linearly in n per run.
  - X-EP gives no bound on it (OPEN in the packet).
  - A run with more than n of them would show that SN-PREFIX-style counting fails inside an epoch. Its climb from nleq33 rose 33 → 36 and
    stalled.

## 5. Not done / next
- An X_SN^pre climb at several n, for a growth law (the per-run value is the one the packet leaves open).
- Resume list (Lead's order): R74 §2.5, FB-CAP |U| ≥ 3, beta2.
