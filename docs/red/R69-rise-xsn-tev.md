# R69: RISE-LAST, XSN-RUN, RESTARTS and TEV (L-RED successor 16, box 39; GO 2026-10-25 09:55Z, date -u)
Targets (Lead 09:46Z brief, 09:55Z split, 10:06Z exitx, 11:14Z TEV, 12:34Z / 12:54Z N5-TEV-box11 = P-N5-ENT):
- (1) PF-THETA: routed to successor 15 (Lead 09:55Z). Not climbed here; my counter pfx.py is a cross-check only (§1).
- (2) RISE-LAST (R68 §6): no COARSE_L(θ) change at an S4a step strictly between consecutive in-scope fallbacks k0 < k of a scope run,
  L = M_{k0}.
- (3) XSN-RUN (R68 §2): at most n − 1 crossings in the c_w = c_θ prefix of one fallback-free run.
- (4) P-N5-TOG §6 RESTARTS (docs/new/P-N5-TOG-box35.md, trunk): maximal (h)-runs per phase ≤ 1 + T + f.
- (5) L-SI succ. 5's CONJECTURE TEV and the TEV-RED configuration (docs/si/N5-RL-box10.md §5, l-si 90b5fb3f).
- (6) L-SI succ. 6's N5-TEV-box11 (P-N5-ENT): FZ, BF, RB, WALK, CYC-EV, TEV-FB.
𝒞^1O only: exactly one Odd vertex with out-degree > 1, asserted in every checker. Labels per L40. G-N5-TIME stays OPEN.

## 0. Result
- **TEV: FALSE, also in its last-fallback form (CANDIDATE until the Lead re-runs).**
  - tevlast_cex_n40.pg, sha1 ff1e9cb4e5b230092de1d967ac8d3fadaa90c175: one fallback. L-SI's own threv.py agrees (thr_ev_rise 1).
  - tev_cex_n40.pg, sha1 17078f78ed830bd1af4ce1048bf7c821e287cc31: the as-written form with intervening fallbacks.
  - The route TEV ⇒ NJB (via EV+) is gone. NJB / ENT are NOT refuted, since neither hit has a second fallback after the failure.
  - TEV-RED (1), (2), (4) hold on the hit (its benign case (4)). The remaining route is "exclude configuration (5)". TEV-RED (3)
    needs a wording fix: "before e" → "up to and including e" (§5).
- RISE-LAST, XSN-RUN, RESTARTS (+ H3-CONST, H2-STICK, the restart classification): 0 failures on 292 library paths and every
  climb. NO KILL.
- N5-TEV-box11 / P-N5-ENT: FZ, BF, RB and WALK have 0 failures on 498 (Σ) pairs and in 2 climbs. CYC-EV and TEV-FB are vacuous,
  because no (Σ) pair has a rise (§5c).
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
- tevx16.py: N5-TEV-box11 in (Σ) (§5c). tevred16.py / tevred16b.py: TEV-RED (1)-(4) and the §5 lane reading at TEV failures.
- Data: data16/rx16_lib.txt (303 rows, before the TEV columns), data16/rx16_tev_lib.txt (292 paths, all columns),
  data16/tevx16_lib.txt.

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
- **Counterexample to TEV-LAST (CANDIDATE): tevlast_cex_n40.pg**, sha1 ff1e9cb4e5b230092de1d967ac8d3fadaa90c175, n 40, o = 0.
  - Found by the tevl climb from tev_cex_n40. TEVLAST means k0 is the last fallback before t, the form EV+ needs.
  - Verified: n5 = n5b --mode spec 11/1, Oink zlk OK, strategies verified.
  - L-SI's threv.py, unmodified, from an l-si 90b5fb3f worktree: TOTAL {'fb': 1, 'ev_size': 6, 'states': 5, 'thr_ev': 3,
    'post_rise': 2, 'thr_ev_rise': 1}, example (3, 7, 32).
  - Witness:
    - k0 = 3 is the run's only fallback: in scope, (h), M = L = 32, r = 38 (THR).
    - Ev = {5, 9, 12, 15, 16, 24}.
    - States 4-7 are S4a with r = 38, and COARSE_32(θ) rises at 6 → 7.
    - At t = 7 the threat's play is 5 → 15 → 35 → 26 → 28 → 11, which meets Ev at 5 and 15.
  - TEV-RED at the hit (tevred16.py, e = 15, the last Ev vertex):
    - (1) holds: e is Even, f = σ_7(e) = 35, f's play lies in F_3, and Ξ_7(f) = Ξ_3(f).
    - (2) holds: u_e = σ_3(e) = 21 ∉ Ev, and COARSE_32(Ξ_3 21) = COARSE_32(θ_3).
    - (4) holds: 21 ∈ R̄_7, (e, u_e) is an improving edge of level 33 > L at 7, and e re-enters R at 8 (σ_8(15) = 21).
    - So this is (4)'s benign case. Configuration (5), u_e ∈ Ev ∩ F_k at a fallback k, does not arise.
    - (3), as worded: B ∖ A = {15} = e itself (rank 33; A above L = {35, 28}, B = {15, 35, 28}), and the only vertex before e is 5
      (priority 14). "the vertices of the threat's play before e" is false as worded. The proof's "(play up to e) ⊕ Ξ_k0(f)", with
      e included, holds. Fix: "before e" → "up to and including e".
- TEVCONF (configuration (5): a TEVLAST failure at an in-scope fallback state t): conf climbs, §5b.

## 5b. TEV-LAST and configuration (5) climbs (DATA)
| climb (mode) | seed | n | best | instance |
| --- | --- | --- | --- | --- |
| tevl | tev_cex_n40 | 40 | first TEVLAST failures at it 233 | tevlast_cex_n40.pg (ff1e9cb4…) |
| tevl | rl_a (L-SI) | 32 | 7 TEVLAST failures in one file | tevlast7_n32.pg (d905038c…) |
| tevl | rise_thin51_n40 | 40 | 0 failures (TEV-LAST states 1) | – |
| conf | tevlast_cex_n40 | 40 | 0 TEVCONF; 11 TEVLAST failures | tevlast11_n40.pg (8421ab30…) |
| conf | tev_cex_n40 | 40 | 0 TEVCONF (27 fallbacks) | – |

- tevlast7_n32 and tevlast11_n40 are verified: n5 = n5b --mode spec (41/2 and 36/2), Oink zlk OK, strategies verified.
- tevred16b.py runs at EVERY TEVLAST failure (20 failures on tevlast_cex / tevlast7 / tevlast11 / one more climb best).
  - All of them are at S4a states, never at a fallback.
  - TEV-RED (1) holds at all 20.
  - TEV-RED (4) holds at all 4 where u_e ∈ R̄_t: the gate (e, u_e) of level > L exists, and e is back in R̄ at t + 1.
  - At 16 of them u_e ∈ Ev ∖ R̄_t: e and u_e are both evicted and free. That is configuration (5)'s shape, but at an S4a state, which
    TEV-FB does not cover.
- N5-TEV-box11 §5 lane reading ("not checked by data" there): WALK's v from v0 = the first and the last Ev vertex on the threat's
  play. 23 walks. Every one has the gate (v, a_j) of level > L at t, and v ∈ R̄_{t+1} (never on e*'s play). 0 failures. So the reading
  "a threat through Ev is absorbed back, one route vertex per step" matches the data.
- TEVCONF (configuration (5) at a fallback) needs a rise inside a (Σ) pair, i.e. a RISE-LAST violation. None was found.

## 5c. N5-TEV-box11 / P-N5-ENT (l-si 3f08db7, sha1 58a0b3cf; pinned as P-N5-ENT 4fd22be7) (DATA)
- tevx16.py, my own checker from the text, works in (Σ): consecutive in-scope fallbacks k0 < k, L = M_{k0} ≥ 0, r > L on [k0+1, k].
  It checks S3, S4, FZ, BF, RB, WALK (a) / (b) / (c), CYC-EV and TEV-FB.
- Library (294 files): 498 (Σ) pairs, 0 failures. Checked instances: FZ 13,173; BF 1,247; RB 708; WALK 1,296; WALK (c) 1,274.
  CYC-EV on all pairs (stronger than stated): 0 failures.
- No (Σ) pair has a COARSE_L(θ) change. So CYC-EV in its setting and TEV-FB are vacuous on all data, as L-SI's §6 says.
- tx climbs (fitness: failures, rise pairs, RB + WALK checks, pairs): from b6_xl2_n32 133 checks at 10 pairs (88,388 evaluations);
  from tev_cex_n40 119 checks at 17 pairs (66,710 evaluations). 0 failures, 0 rise pairs.
- The suggested target (a (Σ) pair containing a rise; by TEV-FB it must end at a fallback with M_k < L) was not reached. It is the same
  event as a RISE-LAST violation.


## 6. Labels
- CANDIDATE COUNTEREXAMPLES (until the Lead re-runs): TEV as written (tev_cex_n40) and TEV-LAST (tevlast_cex_n40).
- WORDING: TEV-RED (3) "before e" → "up to and including e" (tevlast_cex_n40).
- DATA, 0 failures: TEVCONF (configuration (5)); N5-TEV-box11 FZ / BF / RB / WALK (CYC-EV and TEV-FB vacuous); its §5 lane
  reading (23 walks); RISE-LAST, XSN-RUN, RESTARTS (PROVED in lane, given H2-STICK, H3-CONST, H3H2), H3-CONST and H2-STICK
  (PROVED in lane), PF-THETA cross-check (no climbing).
- CONJECTURE (L-RED): RISE-LAST, XSN-RUN (unchanged); data pattern "prefix-internal crossings ≤ n − 3".
- OPEN: NJB (its route via TEV is gone; via configuration (5) it stands), X per phase, f, G-N5-TIME.

## 7. Traps
- (1) Two sessions on one branch (successor 15 resumed box 39 at 09:44Z): merge origin before every push, use distinct file names.
- (2) A borrowed checker narrower than its statement (threv.py breaks at the next fallback). It still caught the TEV-LAST hit.
- (3) A degenerate maximum (rst climb slack 0 at one run). Target the classification, not the slack.
- (4) A waiter on a climb I killed never ends; it was stopped at its time limit.
- (5) My 10:1xZ message stamp was a guess; date -u read 10:04Z. Stamp from date -u only.
