# R67: adversary on L-NEW's box-33 lemmas: R-STICK, SN-PREFIX, ABS-L, EXIT-R (L-RED successor 15, box 37; GO 2026-10-25 03:13Z, date -u)
Targets (Lead 03:13Z):
- Source: docs/new/N5-K-box33.md §1-§2, §8-§9, read on claude/l-new fb157c31 (not packeted; not edited).
- (1) Lemma R-STICK; (2) Corollary SN-PREFIX; (3) Lemma ABS-L; (4) CONJECTURE EXIT-R, in the cases L-NEW has not proved;
  (5) X growth in the SN regime (c_w = c_θ).
- 𝒞^1O only: one Odd vertex with out-degree > 1, asserted in the checker. Referees were not contacted. Labels per L40. G-N5-TIME stays
  OPEN.

## 0. Result
- **CONJECTURE EXIT-R (§2) is FALSE as stated** ("if k is an ε-transition with old exit x0, then x0 ∈ R_t for every t from k+1 up to
  the next fallback transition of the phase, or the end of the phase").
- **Its consequence ε_{H1} ≤ (d_o − 1)(f + 1) per phase is FALSE too**: 6 > 5 at n 16, and 17 > 16 at n 48, both with f = 0.
- **ORX** ("each exit is the old exit of at most one ε-transition per fallback-free segment") is FALSE with EPS = 1, on the same
  instances.
- L-NEW's own box33/orx.py (EPS=1, run unmodified from an l-new fb157c31 worktree) reports EXITR_FAIL and ORX_FAIL on all 4
  instances. Its O-rise-only mode (no EPS) reports no failure on exitr_cex_n48, so EXIT-R restricted to O-rises was not refuted
  there.
- PROVED lemmas: 0 failures of R-STICK, SN-PREFIX, Lemma OR (a)/(b)/(c), TC-SPLIT and ABS-L (i)-(iii) with its count. Coverage: the
  241-file library and about 2.3 M climb evaluations.
- **J ≤ (d_o − 1)(f + 1)** is the bound L-NEW wanted to derive from EXIT-R (via J ≤ ε). It is NOT refuted, but it is attained with
  equality on 3 instances, and two climbs on J − (d_o − 1)(f + 1) stayed at 0.

## 1. Checker: experiments/red/so/sox2.py, written from the box-33 text
- Trace and helpers: sox.py (R66), asserted equal to n5.run.
- Notation:
  - R_k includes o (LP §0; CLS's R̄). F_k = V ∖ R_k.
  - W_k is the valuation of the (σ_k, τ_k)-play: si.py Engine on the arena with Odd fixed to τ_k.
  - H1: o is not on its H_k-cycle. H2: o is not on its (σ_k, τ_k)-cycle. H3: c_w = c_θ.
  - E_k and O_k as in P-N5-OE. ε-transition: O_k > E_k.
  - Scope run, M_{k0} and r_j as in P-N5-CLS §0 (l-si).
- Counters:
  - RSTICK: at an S4a in-phase step, x ∈ R_s with λ_W(x) ≠ λ_Ξ(x) implies x ∈ R_{s+1}.
  - RSTICK2: c_w(s) ≠ c_θ implies R_s ⊆ R_{s+1}.
  - PREFIX, PREFR, PREFN: on each maximal fallback-free run, the states with c_w = c_θ form a prefix; R is monotone after the prefix;
    there are ≤ n − 1 crossings after it.
  - XSN: X ≤ (f + 1)(n − 1) + f + X_SN.
  - OR_A, OR_F, OR_C: Lemma OR.
  - EXITR, ORX, TCS.
  - ABSL_i, ABSL_ii, ABSL_iii, ABSL_cnt.
- EXITR reading: t runs over the states k+1 .. (the index of the next fallback transition), i.e. up to the state at which that fallback
  is applied, or up to the last state of the phase. All four counterexamples have f = 0 in the failing phase, so any reading of "the
  next fallback" gives the same verdict.

## 2. The counterexamples (DATA; experiments/red/so/instances/)
Every one passed vrun.sh:
- 𝒞^1O asserted;
- n5.py = n5b.py --mode spec in iterations and fallbacks;
- check_sol2.py "zielonka(oink zlk) OK strategies verified";
- L-NEW's orx.py (EPS=1): EXITR_FAIL and ORX_FAIL.

| file | sha1 | n | o | d_o | it / fb | failing phase | ε in phase (all H1) | (d_o − 1)(f + 1) | J |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exitr_cex_n16.pg | 6971211eb3390c0e83d3d4b41e175e7bcbcfacc1 | 16 | 9 | 6 | 10 / 0 | 1-8, f 0 | 5 | 5 | 4 |
| epsseg_cex_n16.pg | 8d83f7c20e01a755bec27892c676bc8c9bc51bf2 | 16 | 9 | 6 | 11 / 0 | 1-9, f 0 | **6** | 5 | 5 |
| exitr_cex_n48.pg | 7a663df25ba44e15022ad94fe5f0709662dbca8d | 48 | 0 | 18 | 22 / 1 | 4-20, f 0 | 16 | 17 | 15 |
| epsseg_cex_n48.pg | b4c7dcb04fc2a156905fbe9ba2739e70e04c5c8c | 48 | 0 | 17 | 26 / 1 | 7-24, f 0 | **17** | 16 | 16 |

**epsseg_cex_n16, step by step** (succ(o) = {3, 7, 8, 11, 12, 13}; all transitions 1-9 are S4a; c_θ = λ(o) is fixed):
- The ε-transitions are 1, 5, 6, 7, 8, 9. Their old exits are 3, 3, 13, 8, 7, 12.
- Transition 1 (ε, O 15 > E 14): σ̄(o) 3 → 8, and 3 is absorbed: R_2 = {3, 9}, with Even 3's successor = o.
- Transitions 2-3: R grows to {3, 9, 13}.
- Transition 3 → 4: S4a, no fallback. R_4 = {9}: Even 3 has left R, so EXIT-R fails at t = 4.
- Transition 4: σ̄(o) 8 → 3, with O = E = 14, so not an ε-transition.
- Transition 5 (ε, O 13 > E 8): old exit 3 again, absorbed again (ORX fails).
- So exits can be released at S4a steps, not only at fallbacks.

**exitr_cex_n48:**
- Exit 13 is absorbed at ε-transition 4: 13's play 13 → 8 → 0 = o.
- At the S4a step 5 → 6, Even 13 switches 8 → 17, and its play no longer meets o.
- c_w = c_θ = 2 at states 3-7, the SN regime, where R-STICK is silent.

## 3. Other data (DATA; 0 failures of the proved lemmas)
| set | files / evals | phases | ε | ε in SN | ABS-L gaps checked | max X | max X_SN | max crossings after the SN prefix |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LIB: c1o_list.py 64, includes R66's instances | 241 | 296 | 311 | 274 | 377 | 84 (b6_xl_n48) | 75 (b6_xl_n48) | 12 (jcl_zcl_cu_n48) |
| climbs (soclimb2.py: exr, seg ×3, small, jb ×2, xsn ×2, post) | ≈ 2.3 M | — | 18 | — | — | 43 | 43 | 31 |
- X_SN climbs from random games:
  - xsn29_n32 (sha1 9fb07f42…): X = X_SN = 29, fallback-free.
  - xsn43_n48 (b9d41e3c…): X = X_SN = 43, fallback-free.
  - Every crossing is in the SN regime; X stays below n in both.
  - The library has X 84 at n 48 (b6_xl_n48), with fallbacks.
- post31_n48 (24f491b9…): 31 crossings after the SN prefix (X_SN 0), all adding to R, within ≤ n − 1 = 47 (Corollary SN-PREFIX).
- seg climbs: ε per fallback-free segment − (d_o − 1) reached +1 and never +2 (n 48: 86 k evaluations; n 16: 727 k).
- jb climbs: J − (d_o − 1)(f + 1) stayed at 0 (n 48: 44 k evaluations; n 16: 481 k).
- The xsn48 climb ended at X = X_SN = 44 (not pinned; xsn43_n48 is its earlier best).

## 4. n5b agreement
- vrun.sh now runs n5b with `--mode spec`. All 13 of my instances agree with n5.py in that mode.
- The default `--mode orig` (L-COMP's A5 reading) differs on xsn29_n32: 28 vs 29 iterations. The first difference is an S4a tie at
  Even vertex 4 (6 vs 0).
- This also explains R66's side note on nowake_cex_n32 (R66 §7).

## 5. Labels
- FALSE (counterexamples, verified):
  - CONJECTURE EXIT-R (§2);
  - its consequence ε_{H1} ≤ (d_o − 1)(f + 1);
  - ORX with EPS = 1 (all ε-transitions).
- DATA, no failure: Lemma R-STICK, Corollary SN-PREFIX, Lemma OR, Lemma TC-SPLIT, Lemma ABS-L (all PROVED by L-NEW; not refereed).
- CONJECTURE (L-RED, data only): (J-SEG) J ≤ (d_o − 1)(f + 1) per phase. Equality on 3 instances; 0 violations; two jb climbs flat at 0 (525 k evaluations).
- READING (L-RED):
  - The §4 loop (f ↔ J) cannot close through EXIT-R: absorbed exits are released by S4a steps in the SN regime.
  - (J-SEG) would close it on the J side if proved by another route. J1 + MONO is a natural candidate: each non-tame transition
    raises σ̄(o) above M_k.
- OPEN: X per phase (in the SN regime X_SN < n on the climbs, but 84 > n with fallbacks), K, G-N5-TIME.

## 6. Reproduce
- `python3 experiments/red/so/sox2.py <files>` (the library list: `python3 experiments/new/box32/c1o_list.py 64 | awk '{print $1}'`)
- `python3 experiments/red/so/soclimb2.py exr|seg|small|jb|xsn|post seed secs OUT (seed.pg | --rand n)`
- `experiments/red/so/vrun.sh experiments/red/so/instances/<file>`
- L-NEW's checker: `git worktree add <dir> fb157c31; cd <dir>/experiments/new/box33; EPS=1 python3 orx.py <game.pg>`
