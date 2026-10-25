# R69: RISE-LAST, XSN-RUN, RESTARTS and TEV (L-RED successor 16, box 39; GO 2026-10-25 09:55Z, date -u)
Targets (Lead 09:46Z brief, 09:55Z split, 10:06Z exitx, 11:14Z TEV):
- (1) PF-THETA: routed to successor 15 (Lead 09:55Z). Not climbed here; my counter pfx.py is a cross-check only (§1).
- (2) RISE-LAST (R68 §6): no COARSE_L(θ) change at an S4a step strictly between consecutive in-scope fallbacks k0 < k of a scope run,
  L = M_{k0}.
- (3) XSN-RUN (R68 §2): at most n − 1 crossings in the c_w = c_θ prefix of one fallback-free run.
- (4) P-N5-TOG §6 RESTARTS (docs/new/P-N5-TOG-box35.md, trunk): maximal (h)-runs per phase ≤ 1 + T + f.
- (5) L-SI succ. 5's CONJECTURE TEV and the TEV-RED configuration (docs/si/N5-RL-box10.md §5, l-si 90b5fb3f).
𝒞^1O only: exactly one Odd vertex with out-degree > 1, asserted in every checker. Labels per L40. G-N5-TIME stays OPEN.

## 0. Result
- **TEV as written: FALSE (CANDIDATE until the Lead re-runs).** tev_cex_n40.pg, sha1 17078f78ed830bd1af4ce1048bf7c821e287cc31.
  - The hit needs in-scope fallbacks strictly between k0 and t.
  - With k0 = the last fallback before t (TEV-LAST, the form EV+ / TEV-RED use), there are 0 failures. So NJB's route through TEV is
    not refuted (§5).
- RISE-LAST, XSN-RUN, RESTARTS (+ H3-CONST, H2-STICK, the restart classification): 0 failures on 292 library paths and every
  climb. NO KILL.
- XSN-RUN's margin is 1 at small n: 8 at n 10 (xrun8_n10.pg), and that 8 includes the prefix-exit crossing. The prefix-internal
  maximum seen is n − 3 at every size.
- G-TOG-1 (Lead 10:06Z): on the SPEC trace the prefix-exit crossing exists (26 in 269 distinct files, at most 1 per phase). On
  b6_xl2_n32, REFEREE-2's example, there is none (§3).

## 1. Tools (experiments/red/so/; written from the source texts; every trace asserted equal to n5.run in iterations and fallbacks)
- pfx.py: PF-THETA linear form (per scope run and level M; also the inclusive and per-interval variants) plus rfb0. It reproduces
  L-NEW's pf_best_3621/3622/3623 = 31/35/32 exactly.
- rx16.py: one pass per file. It checks:
  - RESTARTS (both 1 + T + f and the sharp 1 + toggles + f), RCLASS (each restart is an H1-toggle or an Even fallback), H3-CONST,
    H2-STICK (with L2-1's τ(o) = o case: ¬H2 there throughout);
  - PREFIX and XSN-RUN, counting crossings s → s+1 with c_w(s) = c_θ, so the prefix-exit transition is included. exitx counts exit
    crossings separately;
  - RISE (rfb0, sox3's definition), with thin = θ-changes at the S4a steps between in-scope fallback pairs, a near-miss count;
  - TEV and TEVLAST (§5).
- climb16.py: modes rise / rise2 / tev / tevl / xrun / rst; mutations soclimb.mutate. pfclimb16.py: written for PF-THETA, not run
  (routed away).
- Data: data16/rx16_lib.txt (303 rows, before the TEV columns), data16/rx16_tev_lib.txt (292 distinct files, all columns).

## 2. RISE-LAST (DATA)
- Library: 292 paths, 681 consecutive in-scope fallback pairs with M_{k0} ≠ ∞, rfb0 = 0.
- Climbs, 0 events:

| climb | seed | n | best (pairs checked / fallbacks / θ-changes between pairs) | instance |
| --- | --- | --- | --- | --- |
| rise (pairs) | njb_reabs65_n48 | 48 | 36 / 38 / – | rise_fb38_n48.pg (98ba3601…) |
| rise2 (thin) | pf_best_3622 | 40 | 5 / 7 / 51 | rise_thin51_n40.pg (47aaf46e…) |
| tev | rise_thin51_n40 | 40 | 15 / 16 / 0 | tev_cex_n40.pg (17078f78…) |

- rise_thin51_n40: 51 θ-changes at S4a steps between consecutive in-scope fallbacks, none of them a COARSE_L change. θ moves a lot
  below L there and never at or above L.
- Both instances are verified: n5 = n5b --mode spec (53/38 and 78/7), Oink zlk OK, strategies verified.

## 3. XSN-RUN (DATA), and the G-TOG-1 count
- Library maxima per n (crossings in the prefix of one fallback-free run, exit included; data16/rx16_lib.txt):
  12: 7, 16: 13, 20: 17, 24: 21, 32: 29, 40: 36, 48: 44, 64: 55.
- Climbs (xrun fitness = max prefix crossings − (n − 1), then exit crossings):

| n | start | best | best / (n − 1) | evaluations | instance |
| --- | --- | --- | --- | --- | --- |
| 8 | random | 5 | 0.71 | 2,066,166 | – |
| 10 | random | 8 | 0.89 | 1,007,722 | xrun8_n10.pg (c4a60fa7…; exitx 1) |
| 16 | x32_rand16 | 13 | 0.87 | 492,565 | – (no gain) |
| 24 | xc24 | 21 | 0.91 | 282,355 | xrun21_n24.pg (bdf0bf48…) |
| 32 | b6_xs_n32 | 29 | 0.94 | 191,368 | – (no gain) |
| 48 | x32_rand48 | 44 | 0.94 | 96,030 | – (no gain) |

- Every count is ≤ n − 2. Every count with the exit crossing removed is ≤ n − 3. R68's xrun climbs (n − 3 at n 12 and 20) agree.
  The large-n climbs did not move. So the margin data comes from n ≤ 10.
- R is NOT monotone inside the prefix: 753 of 3,480 library prefix crossings are not R-growth. So "XSN-RUN by counting R's growth" is
  no proof.
- READING (data): XSN-RUN ≤ n − 1 holds with a margin of 1. The sharper form "≤ n − 3, exit excluded" is a data pattern only.
- G-TOG-1 (Lead 10:06Z, SPEC trace): 26 prefix-exit crossings (S4a, start c_w = c_θ, end c_w ≠ c_θ, R changes) in 269 distinct
  files, at most 1 per phase. Example: so_sor5_n24 (42f9fa79…), S4a 21 → 22, c_w 5 → 4 with c_θ = 5, H2 true → false.
  - On b6_xl2_n32 (909c7371…): n5 = n5b 87/10. τ changes only at 0 → 1, H2 holds at every state, and c_w = c_θ = 11 on states 1-87.
    So 28 → 29 is an in-prefix crossing, and there is no exit. REFEREE-2's "At 29: ¬H2, ¬H3" does not match the SPEC trace (sent
    to the Lead 10:1xZ).

## 4. RESTARTS, H3-CONST, H2-STICK (DATA)
- Library (292 paths): 0 failures of RESTARTS (both forms), RCLASS, H3-CONST and H2-STICK.
  - 18 toggle restarts.
  - 4 fallback restarts: fbrestart_cex_n12 and fbrestart_cex_n24, each present twice in the corpus (library copy and scratch copy).
- Max (h)-runs per phase: 4 (tog6a_n32 and tog6b_n32: 3 toggles, 1 fallback). The sharp form 1 + toggles + f is met with equality
  on some files (slack 0).
- The rst climb fell to a degenerate maximum (one run, no toggles, no fallbacks: slack 0) and was stopped. That is trap 2 again.
  The sharp form follows from RCLASS, and RCLASS is what the climb should target.

## 5. TEV (L-SI succ. 5, CONJECTURE) and TEV-LAST
- Statement checked (docs/si/N5-RL-box10.md §5, verbatim): "After an in-scope THR fallback k0 of level L ≥ 0, at every later state t
  of the scope run that comes after a COARSE_L(θ) rise and has r > L on [k0+1, t], the threat's σ_t-play avoids Ev."
  - Ev := F_{k0+1} ∖ F_{k0}. R̄, F, r and THR are as in P-N5-FBW §0.
  - The rise is an S4a step j in (k0, t). The threat's play is the honest play from x_t = σ̄_t(o). It avoids o under H1, so it is
    the σ_t-play.
- Seeds rl_a / rl_b / rl_c (l-si 90b5fb3f, sha1 11bfdb71 / eeac0522 / 04ff3de5): 23 + 24 + 17 = 64 post-rise states, 0 failures.
  This equals L-SI's 64.
- Library: 143 post-rise states, 0 failures. Before a rise the threat meets Ev in 3,814 of 9,778 states.
- **Counterexample to TEV as written (CANDIDATE): tev_cex_n40.pg**, sha1 17078f78ed830bd1af4ce1048bf7c821e287cc31, n 40, o = 0.
  - Found by the tev climb from rise_thin51_n40.
  - Verified: n5 = n5b --mode spec 27/16, Oink zlk OK, strategies verified.
  - The witness:
    - k0 = 4: an in-scope fallback with (h), M = L = 33 and r = 38 (THR).
    - Ev = R̄_4 ∖ R̄_5 = {5, 8, 12, 15}.
    - States 5-19 are 15 more in-scope fallbacks (each M = 33), and 20-23 are S4a steps.
    - r = 38 > 33 on [5, 23].
    - The S4a step 22 → 23 changes COARSE_33(θ).
    - At t = 23, x_23 = 5 ∈ Ev, and its play meets 5 and 15.
  - Why the proof form survives: with k0 ∈ {11, 18, 19} (19 is the last fallback before t), Ev is a single vertex ({27}, {33}, {16})
    and the threat at 23 avoids it.
  - TEV-RED step (1) uses "no vertex leaves R at the S4a steps of (k0, t]", hence F_t ⊆ F_{k0+1}. Fallbacks in between break that,
    and that is exactly where the hit lives.
- TEVLAST (k0 = the last fallback before t; the form EV+ needs, with consecutive fallbacks k0 < k): 0 failures. Climbs, below.
- L-SI's threv.py (run from an l-si 90b5fb3f worktree) gives thr_ev_rise = 0 on tev_cex_n40. Its scan stops at the next fallback, so
  its 0-of-117 data covered TEV-LAST only (trap 3: a checker narrower than the statement).
- The TEV-RED configuration (an Even e with u_e both evicted at k0 and free at k, e re-routed into frozen F_{k0}, the threat through
  e after B ∖ A) never occurs, because TEVLAST never fails.
- TEV-LAST climbs: see §5b.

## 6. Labels
- CANDIDATE COUNTEREXAMPLE (until the Lead re-runs): TEV as written (tev_cex_n40).
- DATA, 0 failures: TEV-LAST, RISE-LAST, XSN-RUN, RESTARTS (PROVED in lane, given H2-STICK, H3-CONST, H3H2), H3-CONST and H2-STICK
  (PROVED in lane), PF-THETA cross-check (no climbing).
- CONJECTURE (L-RED): RISE-LAST, XSN-RUN (unchanged); data pattern "prefix-internal crossings ≤ n − 3".
- OPEN: NJB (its route via TEV-LAST stands), X per phase, f, G-N5-TIME.

## 7. Traps
- (1) Two sessions on one branch (successor 15 resumed box 39 at 09:44Z): merge origin before every push, use distinct file names.
- (2) A borrowed checker narrower than its statement (threv.py breaks at the next fallback).
- (3) A degenerate maximum (rst climb slack 0 at one run). Target the classification, not the slack.
- (4) A waiter on a climb I killed never ends; it was stopped at its time limit.
- (5) My 10:1xZ message stamp was a guess; date -u read 10:04Z. Stamp from date -u only.
