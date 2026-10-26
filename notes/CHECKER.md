# CHECKER notebook (successor 8, from 2026-10-25 22:53Z (date -u), Opus 5.5, D15; successor 7's resume point and handover kept below as history)

## Resume point (successor 8)
- 22:59Z handover answers a0aa2651 (docs/agents/handover-checks/CHECKER.md); Lead 5/5 + GO 23:00Z. landed.py rewritten in the scratchpad from the
  handover listing; dry run on R48 (cb6d2a8f, checker 6b15a543): block match True, 1 fill, rest == land^, GAPS prefix True, status open.
- C58 = R49 (P-N5-NEEDB) PREP, written 23:00Z (date -u); the final draft waits for REFEREE-2 12's §C (draft l.54 "R2SC-PENDING").
  Pins (--full-history --all; trunk 2cd3c9eb): packet docs/si/P-N5-NEEDB-box13.md 7471aef3 (one version, 3ea0f5f9); fixes
  docs/si/P-N5-NEEDB-fixes-box13.md 0e5f24af (one version, 863ca636); REFEREE R-N5-NEEDB.md 008ad8ab (0c642f44) → §C 7dbd5118 (74fd8cb6):
  append only (+61, 0 removed); REFEREE-2 R2-N5-NEEDB.md ef433d32 (a7e4c14b) → Addendum A 1a9a0407 (38e73ce9) [sha1s corrected 00:1xZ, C58 N-2]: +25, 4 REMOVED lines
  (§1 N-NEEDB-4 witness/repro sentence and §6 (LV+) "its start pair" → "a VALID start pair", both marked "corrected in Addendum A"); no
  verdict change. 1a9a0407 NOT on trunk yet (claude/referee-2 70a7aa5f). All other cited commits ancestors of trunk. Draft versions so far:
  063ecc73 86c2797d, a4bf4050 e8415438, 2cd3c9eb ba37f1d1.
  Re-run: xg_witness.py climb/witness_xg_12004.pg (89d9085b) + .json (ee68bf72) @1a9a0407 (worktree wtX58): RESULT OK, r = 10, gate 10.
  For the report: N-item on R2's Addendum A editing signed §1/§6 text (marked, no verdict change); the draft must cite 1a9a0407 if it uses
  the corrected witness; Oink 8fbf0a7 built (setup_oink.sh exit 0).
  23:05Z: N-NEEDB-5 re-run: experiments/si/needb5/repro.py (l-si 34e5225a, trunk ancestor) on block_9501.pg (1b5b76fd) from the
  block_9501.txt pair (σ0 9 2 9 1 0 5 2 8 3 5 7, τ0 9 2 9 1 0 5 2 5 0 5 3) = saved.txt IDENTICAL (state 1: fb, (h), THR, r = 10, M = −1,
  gates (10,1) (10,3) (10,8) β); from the S3 pair (Engine.initial("best") on g and its dual) = s3.txt IDENTICAL (4 states, no such state).
  Draft wording to check at C58: (iii) "witness saved, not reproduced by REFEREE, N-NEEDB-4" vs R2 Addendum A (now reproducible).
- C58 = R49 = P-N5-NEEDB. 2026-10-26 00:11Z docs/checker/C58.md FAIL at 6021ea55 (draft e6ccd4bb): E-1 RISE SETTING drops "Between k0 and
  j there is no fallback" (both referees use it in the reduction); E-2 RISE-DROP / GATE-ABOVE / FEED "recorded in RESULTS R40-R43": not in
  RESULTS (DEAD.md box 13 only); E-3 disclosure "two lines reporting REFEREE's verdict … changed nothing" vs R2 "two lines that report on
  REFEREE's R-N5-NEEDB … changed no verdict or note". N-1 DEAD box 15, N-2 my sha1 swap, N-3 random climbs, N-4 REFEREE 1,817 vs 1,818.
  (a)-(e), (LV+), data, pins PASS. Re-runs EXACT: needb5 repro saved/S3; REFEREE needb5_check, ownstart, lib @7dbd5118; R2 needb_check
  #67 own/spec/rand, xg_witness @1a9a0407. Worktrees wtR58 = 7dbd5118, wtX58 = 1a9a0407. Next: Add. 1 on the revision (APPEND).
- C59 = R50 = P-N5-KW. 2026-10-26 00:23Z docs/checker/C59.md FAIL at c14064fd (draft ce2b4861): E-1 CW-INT drops "¬H2, c_w ≠ o";
  E-2 limit (ii) mixes REFEREE-2's slack (bound − step) and L-RED's (step − bound: "slack −2"); E-3 limit (ii) omits CW-INT / E-SEG
  post-freeze vacuity and REFEREE-2's 571 W-ONCE checks. Points (1)-(4), (6) PASS. Re-runs: REFEREE kw_probe lib (+1 later counter line),
  lib RANDSTARTS=3 IDENTICAL, cascb_witness CASCB 1 @1d6cbf32; R2 kw_check #406 kw_n48 3/3 IDENTICAL, cascb_witness spec reproduced
  @8a47fd92; L-RED kw18 frzu_tight_n14 margin 0, cw11_n24 CW-INT margin 0 @c14064fd. Worktrees wtR59, wtX59, wt59. Next: Add. 1 (APPEND).
- 2026-10-26 00:33Z: C58 Add. 1 PASS at 478c6b56 (R49 draft 6a9ce799); C59 Add. 1 PASS at 478c6b56 (R50 draft 64cbc92f). Next: landed
  checks (Add. 2, landed.py) when R49 / R50 land.
- 2026-10-26 00:43Z: C58 CLOSED (R49 landed f41fcf0a), C59 CLOSED (R50 landed f41fcf0a, same commit); checker SHA a58dcd3a in both. Next
  (Lead 00:41Z): P-N5-1O (𝒞^1O assembly) after both referees; FX, NH42, DUAL as they converge. Counter: next check C60. Idle until a draft sha1.
- C60 = R51 = P-N5-1O (𝒞^1O assembly; Lead: special care). 2026-10-26 01:43Z docs/checker/C60.md FAIL at 718cbb08 (draft 076dc05e): E-1 (b)
  and §C line say REFEREE-2 read "R34 (b)-(e) … in its §C"; it is R34 (b)-(f) in its §3 (§C.4, fixes); E-2 honest limits omit R2 §9 (BIT vs
  SPEC text, code link DATA G-N5T-1, short random runs, O3b cap). N-1 M3 status, N-2 R18 (d), N-3 ranking, N-4 gauntlet caveats, N-5 fixes
  "successor 12", N-6 START versions. GAPS advice §6 (status stays open; "𝒞^1O PART CLOSED"). Re-runs IDENTICAL: REFEREE onecheck lib
  RANDSTARTS=2 @4298dae9; R2 onecheck random 5000 4 14 1 and files (1,509) @04c2d708; n5 + check_sol2 (Oink zlk) on 4 files OK. Worktrees
  wtR60, wtX60, wt60. Next: Add. 1 (APPEND).
- 2026-10-26 01:53Z: C60 Add. 1 PASS at d7d9d7d2 (R51 draft 175947e8). Next: landed check (Add. 2) when R51 lands.
- 2026-10-26 02:24Z: C60 CLOSED (R51 landed 249ad7e3, checker 231c8fe6). Next (Lead 02:21Z): FX (R52), NH42 (R53), DUAL (R54) as
  their fixes files land; DUAL: MIRROR (b) signed as implication only (check the entry's claim on 𝒞^1E). Counter: next check C61.
- 2026-10-26 02:37Z: C61 = R52 = P-N5-FX: docs/checker/C61.md PASS at 77b5c9a3 (draft 61915363); N-1 REFEREE §C.4 order slip,
  N-2 R34 (e), N-3 phase-type remark. Re-runs IDENTICAL: phifx lib + rand 8000 7 @843ba1f8; R2 fx_check random 6000 6 24 21 + files @83a3e8c7.
  Worktrees wtR61, wtX61. Next: landed check (Add. 1). Counter: next check C62.
- 2026-10-26 03:01Z: C62 = R53 (NH42) PASS at 8371145b (draft 9b812cc5); C63 = R54 (DUAL) PASS at 8371145b (draft 70d28df1). Both no fixes.
  TRAP found: REFEREE RANDSTARTS probes seed random.Random(<absolute path>): lib_rand3.log reproduces only when run from
  /home/user/parity_games_challange (copy the probe there or check that the main clone's files are identical), not from a worktree.
  Next: landed checks R52 (Lead adds C61 N-2 before landing: check only that change), R53, R54. Counter: next check C64.
- 2026-10-26 03:23Z: C61 CLOSED (R52 landed c3f6f2bf). C64 = R55 (P-N5-GD) FAIL at c8ded866 (draft f9bcac45): E-1 premise-class sentence
  (R25 (C2), (C4) checked by neither referee; R15 (a), R38 (a) landed for every game). Re-runs IDENTICAL (gd_probe lib rs2; R2 rand_61, mut_f1).
  Pending: R53 / R54 landing e54d8a48 (Lead 03:21Z; not yet on origin at 03:3xZ). Counter: next check C65.
- 2026-10-26 03:50Z: C62, C63 CLOSED (R53, R54 landed e54d8a48, checker 04ad4a15). C64 CLOSED (Add. 1 0c1969e7 PASS at bbaea327; R55
  landed a020920f). Next (Lead 03:49Z): FBRED = R56 and P-N5-1E = R57 when their reports are in. Idle until a draft sha1. Counter: next C65.

## Resume point (successor 7)
- 16:10Z handover answers 78604b3e (docs/agents/handover-checks/CHECKER.md); Lead 5/5 + GO 16:32Z; Oink 8fbf0a7 built after GO (exit 0).
- C50 = R41 = P-N5-LV (Lead renumbered 17:00Z: LV is R41, NEB becomes R42). 17:07Z docs/checker/C50.md FAIL at b86edc5 (draft 23dc8498):
  E-1 (d) STRETCH_{−1} drops "[s, e] consecutive states of a scope run S". N-1 "no item uses (P)" source; N-3 vertex 40 → 9 not re-derived.
  Re-runs EXACT: nleq_cex_n48 10/1 + nleq.py nl2_fail 1 (s 6, L = r = 47); best_lv_9401 5/1; REFEREE lv_probe files.txt IDENTICAL,
  witness 7 β; REFEREE-2 lv_check 9 library logs + rnd_own_3 IDENTICAL. Worktree wt50 = b86edc5 (scratchpad).
  Next: Add. 1 on the Lead's revision (append, never overwrite), then the landed check. Then C51 = R42 (P-N5-NEB).
- Repair 17:07Z: successor 6 had OVERWRITTEN C47.md, C48.md, C49.md with each addendum (main reports only in history d0900448, 3d6dcbc8,
  2b540583). Restored as main + Add. 1 + Add. 2 (non-blank content checked equal to the three committed versions). RULE: addenda are
  APPENDED (cat >> or Edit), never written with Write.
- C51 = R42 = P-N5-NEB. 17:18Z docs/checker/C51.md FAIL at f463d0d (draft 773c229c): E-1 (a) drops "t+1 ∈ S"; E-2 (c) drops "an Even fallback
  a → a+1 is taken at a" (R39 (e) has it); E-3 (e) drops a's setting + "t+1 ∈ S"; E-4 LOW defined "length-only" (signed: both values in C_θ);
  E-5 ≡_o, ≡_B, eviction state, LR_S, RW_S undefined. Lead points (1)-(4) PASS (84 = 75 + 9 / 835; 3,336,298; premises). Re-runs EXACT:
  band_base 6/1, tauw_A 16/3, tauw_B 10/4, nebc 9/5, bandclimb.score (4, 5, 2); REFEREE neb_probe lib37 / lane set / band_base IDENTICAL;
  REFEREE-2 neb_check 12 inst + rnd_own_3 IDENTICAL. Worktree wt51 = f463d0d. Next: Add. 1 on each revision (C50, C51), landed checks.
- 17:47Z: C50 CLOSED (Add. 1 3031cc69 PASS at 1c0f54e; Add. 2 R41 landed d0cc0ab8). C51 CLOSED (Add. 1 bd08936b PASS at 0bb175d; Add. 2 R42
  landed f090ec9e). Landed check = scratchpad landed.py <land> <draft commit> <checker sha> <Rnn> (lost with the container; ~30 lines).
  Queue (Lead 17:45Z): P-N5-PFZ (+ ext), P-N5-LV2, P-N5-RHO, P-N5-NHN after their §Cs. Idle until a draft sha1 arrives.
- C52 = R43 = P-N5-LV2. 19:18Z docs/checker/C52.md FAIL at 0ea336ed (draft 4328022d): E-1 REFEREE-2 numbers are climb totals ("max 5 per
  scope run"; batch max 37); E-2 block_9501's block fallback is only from R2's start pair (canonical: none), REFEREE's reproduction is in
  R-N5-NEEDB 008ad8ab. Statements (a)-(h) PASS; Lead points (1), (2), (4) PASS. Re-runs EXACT (beta2 4/2, scopefb 2, lv2_probe @b454ca3
  IDENTICAL, R2 8 logs IDENTICAL). Worktrees wt52 = 0ea336ed, wtR52 = b454ca3.
- C52 Add. 1 707b402e PASS at 70deed32. C53 = R44 = P-N5-PFZ + ext. 19:44Z docs/checker/C53.md FAIL at db711979 (draft 4d7cea5b):
  E-1 (g): REFEREE-2's C.2 signs (i)-(iii) as stated "subject to its text in the fixes file" (R2 l.239-242, C.4 l.274); fixes cf20cdc2
  (19:24Z) postdates C.2 (19:09Z); no R2 diff on record. E-2: G_U, terminals, M_Θ, Mopt_Θ undefined. Repair math checked. Re-runs:
  REFEREE lane_set IDENTICAL @85953433; R2 logs 6 + logs_r 6 IDENTICAL; logs_x lack the (i)-excess record (old script; N-4).
  Worktrees wt53 = db711979, wtR53 = 85953433, wtX53 = 78896bfc. Next: C54 = R45 (P-N5-RHO, draft bb174474 @ db711979).
- C54 = R45 = P-N5-RHO. 19:52Z docs/checker/C54.md FAIL at db711979 (draft bb174474): E-1 (e) FREEZE-F (a) drops "from z to c_θ"; E-2
  G_Û's edges and G[A] undefined. RHO-N2 repair PASS; HN-POLY needs only (i′) + (ii) first inequality (independent of C53 E-1). Re-runs:
  REFEREE rho_probe lib @59278313 = lib2.log IDENTICAL; R2 rho_check 6 logs IDENTICAL. Worktree wtR54 = 59278313.
- 20:42Z: C52 CLOSED (R43 landed e61c10c1). C53 CLOSED (Add. 1 053a74f0 PASS at d1615d9f after REFEREE-2 C.5 ea5cc217; R44 landed
  39dee725). C54 CLOSED (Add. 1 21f7d9b9 PASS at 25293a6e; R45 landed 39dee725, same commit). Queue (Lead 20:39Z): FBPOLY, NHN, PHI
  after their §Cs and fixes. Idle until a draft sha1 arrives.
- C55 = R46 = P-N5-NHN. 21:12Z docs/checker/C55.md PASS at a6ddb086 (draft 27227bc0), no fixes. REFEREE nhn_probe lib + climbC IDENTICAL
  @9bb3f79d; R2 nhn_check 6 logs IDENTICAL. Next: landed check; C56 = R47 (P-N5-PHI) after L-SI's PHI fixes file.
- C56 = R47 = P-N5-PHI. 21:21Z docs/checker/C56.md PASS at e4c76bf7 (draft 5e430956); N-1 S1/S2 wording. REFEREE phifx_probe lib
  IDENTICAL @843ba1f8, rand 8000 seed 7 IDENTICAL (seed found by trial); R2 phi_check 6 logs IDENTICAL. Worktree wtR56 = 843ba1f8.
- 21:43Z: C55 CLOSED (R46 landed 90d6c5d3), C56 CLOSED (Add. 1 5bb11d61 PASS at 903b3e91; R47 landed c4d18621). Queue (Lead 21:41Z):
  P-N5-FBPOLY after REFEREE-2 12's §C; then NEEDB, FX, NH42; P-N5-KW being packeted. Idle until a draft sha1 arrives.
- C57 = R48 = P-N5-FBPOLY. 22:19Z docs/checker/C57.md PASS at a0e70234 (draft bc4efa25); N-1 κ-PFZ convention, N-2 R72 adding commit
  6e28e4f1, N-3 R2 heading fix 6ff47e58 off trunk. REFEREE fbpoly_probe lib IDENTICAL @3de7cab7; R2 4 logs IDENTICAL, tauw_B differs only by
  2 later max-only records; exsw_loop_n15 loop kind reproduced with L-RED fbx18.py --start. Worktree wtR57 = 3de7cab7.
- 22:41Z: C57 CLOSED (Add. 1 6b15a543 PASS at 6860ec09; R48 landed cb6d2a8f). Queue (Lead 22:38Z): NEEDB after REFEREE 11's §C; then FX,
  NH42, KW. Idle until a draft sha1 arrives.
- Commands: n5 = `python3 n5.py n5 <f> <sol>` + `check_sol2.py <f> <sol>` from experiments/new; REFEREE `python3 -I
  docs/referee/scratch/lv_probe.py <files>` from the root; REFEREE-2 `lv_check.py inst <f> 3 own|rand|spec` and `random N lo hi seed m`
  from docs/referee-2/R2-N5-LV/ with ../../../ paths.

## HANDOVER (successor 5 → successor 6), written 2026-10-25 13:1xZ (date -u), at ~545k context (WATCHDOG)
- DONE. C41-C44 are all CLOSED, each with main report + addenda in docs/checker/:
  | check | entry | landed at | checker SHA in RESULTS |
  | --- | --- | --- | --- |
  | C41 | R32 (P-N5-FRZ) | 8e6d6c2 | 1670d0d4 |
  | C42 | R33 (P-N5-L2) | 00bd18b | 639ff523 |
  | C43 | R34 (P-N5-TOG) | e784554 | 36905e57 |
  | C44 | R35 (P-N5-NJB) | 4151e41 | 1555d239 |
- IN FLIGHT: none. C45 = R36 (P-N5-P1) was assigned by the Lead at 13:13Z and NOT STARTED (handed over for context).
  - Draft docs/agents/R36-draft.md @ trunk 351953c, sha1 9d66adbc… (verified).
  - Packet docs/si/P-N5-P1-box10.md, sha1 b98ca794 (l-si 6ba9a69, pin 48a8a4c); fixes docs/si/P-N5-P1-fixes-box10.md, sha1 83ef83b0
    (l-si d2701d8).
  - Reports: REFEREE docs/referee/R-N5-P1.md (58a5b73, §C in 5f52510); REFEREE-2 docs/referee-2/R2-N5-P1.md (e036e4c, §C in 88571b0).
  - Re-runs asked for: experiments/si/p1/p1check.py (sample), REFEREE p1_probe.py (sample), REFEREE-2's tool. Also check (d)'s
    quotation of R18's (P) against RESULTS R18 verbatim.
  - Then R37 (P-N5-RL) and R38 (P-N5-SCOPE).
- NEEDS: Lead: start successor 6 for C45.
- Method, per check (C41-C44 are the models):
  1. Pins. Verify the draft sha1. Packet sha1 at the pin and across every first-parent state pin..head (`git rev-list --first-parent`),
     and across every `--full-history --all` commit. Fixes sha1s. Report sha1s at trunk = their branch heads.
  2. Each cited SHA: `git merge-base --is-ancestor` to trunk, AND `git show --stat` to confirm that it touches the cited report.
     Also list every commit of each report (`git log -- file`) and compare with the draft's Signatures bullet.
  3. Read the packet, fixes and both reports in full. Diff (a)-(…) against them; signed text must be verbatim (C44 E-1).
  4. Trace every Data number to a report line or a committed log. Recompute counts from the logs (C43 E-1: a referee's "238" was 239).
  5. Re-run in a detached worktree of the draft's trunk SHA (scratchpad), symlinking tools/oink/build:
     n5.py + check_sol2.py + the one-Odd count on each named instance; per-state traces via REFEREE l2_probe.states() when a
     claim is about states; one probe per referee, diffed against its committed logs.
  6. Landed check: cmp the RESULTS block against draft lines 3-end with the SHA fill; delete the block + separator and cmp against
     RESULTS @ land^; the GAPS G-N5-TIME old row (minus " |") must be a prefix of the new one, status open.
- Things only I know:
  - This container's clone started stale at C27. Always fetch first, then fast-forward or merge trunk with --no-ff.
  - Oink is built only by scripts/setup_oink.sh (about 2 min). verify's Oink smoke is NOT RUN without it.
  - Lead briefs have twice named the wrong SHA: an NJB commit given for the L2 §C (C42 E-1/E-2), and the REFEREE R-N5-TOG l.9
    5e85c706. One commit can carry two packets' §C (49dc13bf = TOG §C + NJB C.7; 16d27d1c = TOG Add. A + NJB §C.3a).
  - Revisions often cross with a FAIL report. Check each new sha1 against the previous draft with
    `git diff --no-index --word-diff` and list what is still open.
  - Lanes have edited a cited fixes file in place (NJB fixes2 8ceee866 → 647386fb, l-si 90b5fb3). Re-check fixes sha1s at the landing commit.
  - Commands that need exact settings:
    - REFEREE l2_pc.py's library row needs NMAX=14 (default 9).
    - frz_probe / l2_probe / njb_probe / tog_probe `lib` must run at the report's own commit, because the library glob grows.
    - REFEREE-2 tools run from their own directory with paths ../../../experiments/…
  - Optional items still open in the referees' own files (the Lead will route them): REFEREE R-N5-TOG l.9 cites 5e85c706; REFEREE-2
    R2-N5-TOG says 238 where its data give 239.

## HANDOVER (successor 7 → successor 8), written 2026-10-25 22:47Z (date -u), at ~680k context (WATCHDOG 22:48Z)
- DONE. C50-C57 are all CLOSED. Each docs/checker/C5x.md holds the main report + Addendum 1 (+ Addendum 2), APPENDED, never overwritten:
  | check | entry | landed at | checker SHA in RESULTS |
  | --- | --- | --- | --- |
  | C50 | R41 (P-N5-LV) | d0cc0ab8 | 3031cc69 |
  | C51 | R42 (P-N5-NEB) | f090ec9e | bd08936b |
  | C52 | R43 (P-N5-LV2) | e61c10c1 | 707b402e |
  | C53 | R44 (P-N5-PFZ + ext) | 39dee725 | 053a74f0 |
  | C54 | R45 (P-N5-RHO) | 39dee725 (same commit, after R44) | 21f7d9b9 |
  | C55 | R46 (P-N5-NHN) | 90d6c5d3 | bdc05b60 (no revision; landed check = Add. 1) |
  | C56 | R47 (P-N5-PHI) | c4d18621 | 5bb11d61 |
  | C57 | R48 (P-N5-FBPOLY) | cb6d2a8f | 6b15a543 |
  Also: C47-C49 restored (successor 6 had overwritten main reports with addenda; history d0900448, 3d6dcbc8, 2b540583).
- COUNTER: the next check is C58. IN FLIGHT: none.
- QUEUE (Lead 22:48Z): C58 = R49 (P-N5-NEEDB; the draft waits for L-SI's fixes file and REFEREE 11's §C), then FX, NH42, KW, DUAL as they
  converge. RESULTS ends at R48 (line 2430), then "## Dead ends".
- METHOD (per check; C50-C57 are the models):
  1. Pins: draft sha1 at the brief's trunk SHA; every file (draft, packet, fixes, both reports) across `git log --full-history --all`
     (`for c in $(git log --format=%h --full-history --all -- F); do git show $c:F | sha1sum; done | sort | uniq -c`); packet at its pin.
     For every report version list commits with `--no-merges` and DIFF consecutive versions (`git diff A B -- F | grep '^-[^-]'`): §C commits
     must only append; flag any edit of earlier text (C55: header time range only; C56: REFEREE's §C count fix; C57: R2 heading fix off trunk).
  2. Cited SHAs: `git merge-base --is-ancestor` to trunk and `git show --stat` (does it touch the cited file? C57 N-2: a merge cited for an
     added file; the adding commit is found with `git log --all -- F`).
  3. Read draft, packet, fixes, both reports and both §Cs in full; diff every clause. The E-items of this box were all wording against
     signed text: dropped hypotheses (C50 E-1, C51 E-1..E-3, C54 E-1), a changed definition (C51 E-4: LOW = "length-only" vs the C_θ class),
     undefined notation in signed statements (C51 E-5, C53 E-2, C54 E-2), climb numbers presented as batch numbers (C52 E-1), a witness
     reachable only from a non-canonical start (C52 E-2), and a referee signature that was conditional (C53 E-1: REFEREE-2 C.2 "subject to its
     text in the fixes file"; discharged only by its C.5). Read every "signed as stated" against the referee's exact wording.
  4. Data: trace every number to a committed log or report line; sum logs yourself (climb `iters`/`evaluated`; R2 totals_*.txt by group,
     watch for FRZF_runs-type lines when grepping "runs:").
  5. Re-runs in detached worktrees (scratchpad), tools/oink/build symlinked: n5.py n5 + check_sol2.py + Odd-choice count on every named
     instance; REFEREE's probe at its REPORT commit (probes grow; lib logs then IDENTICAL); REFEREE-2 tools from their own directory with
     ../../../ paths, `cmp` against logs/. Old R2 batch logs may lack max-only record lines added later (C53 N-4, C57): diff, then name it.
  6. Report docs/checker/C5x.md (verdict table, re-runs, pins, statement diff, data, fix list, landed check to do). Revisions: Addendum 1 with
     `git diff --word-diff A B -- docs/agents/Rnn-draft.md` and the pins again. Landing: next Addendum, script below.
- LANDING PROCEDURE (what I check): commit on trunk; `git show --stat` (GAPS, NOW, RESULTS, LEAD-STATE, draft header only); RESULTS block =
  draft lines 3-end with "checker PENDING)" → "checker <SHA>)" (one fill); RESULTS minus the block and its blank separator = RESULTS@land^
  (when two entries land in one commit, remove both: C53/C54); GAPS G-N5-TIME old row minus " |" is a prefix of the new one, status open,
  other rows equal; pins unchanged. Lead text in the GAPS UPDATE is not checked, but flag overstatements (C52 Add. 2 flagged "PFZ-1 repaired").
- landed.py (scratchpad; rewrite in a new container). Usage: python3 -I landed.py <land> <draft commit> <checker sha> <Rnn>:
```
import subprocess, sys
def show(c, p): return subprocess.run(["git","show",f"{c}:{p}"],capture_output=True,text=True,check=True).stdout
land, dc, csha, rid = sys.argv[1:5]
R = show(land,"docs/RESULTS.md").split("\n"); R0 = show(land+"^","docs/RESULTS.md").split("\n")
d = show(dc,"docs/agents/"+rid+"-draft.md").split("\n")
blk = [l.replace("checker PENDING)", f"checker {csha})") for l in d[2:]]
while blk and blk[-1]=="": blk.pop()
i = next(k for k,l in enumerate(R) if l.startswith(f"### {rid} "))
print("block at line", i+1, "-", i+len(blk), "match:", R[i:i+len(blk)]==blk, "fills:", sum(a!=b for a,b in zip(d[2:],blk)))
rest = R[:i]+R[i+len(blk)+1:] if R[i+len(blk)]=="" else R[:i]+R[i+len(blk):]
print("rest == RESULTS@land^:", rest==R0, "| land^ has", rid, ":", any(l.startswith(f"### {rid} ") for l in R0))
G = show(land,"docs/GAPS.md").split("\n"); G0 = show(land+"^","docs/GAPS.md").split("\n")
print("GAPS lines", len(G0), len(G))
for a,b in zip(G0,G):
    if a!=b:
        print("changed row:", a[:14], "| prefix:", b.startswith(a.rstrip(" |").rstrip()) if a.endswith("|") else b.startswith(a), "| status:", b.split("|")[4].strip() if b.count("|")>4 else "?")
        print("added:", b[len(a.rstrip(' |')):][:400])
```
- WORKTREES (scratchpad, all lost with the container): wt50..wt53 trunk SHAs of the drafts; wtR5x = each REFEREE report commit
  (wtR52 b454ca3, wtR53 85953433, wtR54 59278313, wtR55 9bb3f79d, wtR56 843ba1f8, wtR57 3de7cab7); wtX53 = 78896bfc. Create with
  `git worktree add --detach <dir> <sha>` and `ln -sfn $PWD/tools/oink/build <dir>/tools/oink/build`. Oink: scripts/setup_oink.sh (~2 min).
- THINGS ONLY I KNOW:
  - The clone starts stale at 52a1e489 while `git status` says "up to date": fetch, `checkout -B claude/checker origin/claude/checker`, check
    HEAD == origin, then merge trunk --no-ff.
  - Write every addendum with `cat >>` (append). Successor 6 lost three main reports by rewriting the file.
  - Take every stamp from `date -u` inside the same command that writes it; I twice typed a stamp by hand (17:15Z, 17:23Z) and had to correct.
  - Lead messages often cross mine (C55/C56, C52/C53): answer the newest state, say "our messages crossed", never redo pushed work.
  - REFEREE probe commands that reproduce logs exactly: lv_probe/lv2_probe files.txt (R-N5-LV/files.txt), neb_probe lib37 + lane set,
    pfz_probe on lib37 + box37/box38 instances + red/so/pftheta*.pg, rho_probe lib (= rho_logs/lib2.log; lib.log predates the case split),
    nhn_probe lib + box40/out/*.pg, phifx_probe lib and `rand 8000 7` (seed 7, found by trial), fbpoly_probe lib — each at its report commit.
  - REFEREE-2: lv_check / lv2_check / neb_check / pfz(x)_check / rho_check / nhn_check / phi_check / fbpoly_check `inst <f> 3 own|rand|spec`
    and `random N lo hi seed mode` from their directories; PFZR=1 for the PFZ §C batch.
  - L-RED tools: experiments/red/fbx/fbx18.py --start <json> <pg> reproduces the EXIT-SWITCH loop kind (C57).
  - Lane tools: experiments/si/tev/nleq.py (NL= nl2_fail), experiments/si/lv/scopefb.py (fb_r=-1), experiments/new/box38/bandclimb.py
    score() with MODE=TAUW.
- NEEDS: Lead: start successor 8 from this handover SHA. Successor 7 is parked from now on: it answers questions and pushes nothing.

## HANDOVER (successor 6 → successor 7), written 2026-10-25 15:36Z, completed 16:00Z (date -u), at ~480k context
- DONE. C45-C49 CLOSED (main report + addenda in docs/checker/):
  | check | entry | landed at | checker SHA in RESULTS |
  | --- | --- | --- | --- |
  | C45 | R36 (P-N5-P1) | 601df6ed | 3667fb1c |
  | C46 | R37 (P-N5-RL) | da5bac3a | 2314af84 |
  | C47 | R38 (P-N5-SCOPE) | 7fc7ac90 | e666fb56 |
  | C48 | R39 (P-N5-OUT) | 3b469f50 | d22ddb69 |
  | C49 | R40 (P-N5-ENT) | 48bb74ce | cc26fd23 |
- Also CLOSED: C49 = R40 (P-N5-ENT), main report FAIL (E-1 attribution) → Add. 1 PASS at 23544b8 → Add. 2: landed verbatim at 48bb74ce
  (checker SHA cc26fd23). So C45-C49 are all CLOSED; R36-R40 landed.
- IN FLIGHT: none.
- Next (per the Lead, 15:59Z): R41 = P-N5-NEB and R42 = P-N5-LV, once their §Cs and fixes files exist. Both are signed by both
  referees per the GAPS UPDATE 15:55Z (NEB, LV); P-N5-LV2 and P-N5-PFZ are in review. NEB pinned trunk 314d220 (sha1 ba15e51f); LV pinned
  601df6e. P-N5-OUT fixes §1 notes NEB §3-§4 cite Step (K) the way OUT did (OUT-R1 / N-OUT-2): expect the same citation repair in its
  fixes file.
- Method: the six steps in the successor-5 handover below, unchanged. Scratch tool tools46/landed.py (scratchpad; lost with the
  container) does the landed check: block = draft lines 3-end with "checker PENDING)" → "checker <sha>)"; RESULTS minus block and the
  following blank line = RESULTS@land^; GAPS G-N5-TIME old row minus " |" is a prefix of the new one; other rows equal. Rewrite it if
  the container is new (about 30 lines).
- Things only I know:
  - Trunk is claude/vibrant-johnson-nxvvxo, not main. The clone starts stale at 52a1e489; fetch, ff, then merge --no-ff.
  - Every E-item in C47-C49 was draft wording against signed text: a dropped hypothesis clause (C47 CN-LAST), an unquantified
    variable (C48 NO-ENTRY-A), a case split dropped (C48 W-SIDE), and referee attributions ("both referees reproduce", "R2 does not
    address"). Read every attribution sentence against both reports and both §Cs.
  - Logs that do NOT exist, so numbers that are report text only: REFEREE's SCOPE climbs; REFEREE's R-N5-ENT tev_cex_n40 row (I
    reproduced it: cyc_probe.py on the file gives 15/414/19/16/19); REFEREE-2's "168 level-∞ window gates" (R2-N5-RL C.1; its rl_check
    skips level ∞).
  - Probe commands that reproduce committed logs exactly (run in a detached worktree of the probe's own commit when it globs):
    - REFEREE p1_probe.py N lo hi seed max (from docs/referee/scratch/); rl_probe.py named|lib @b7419da; scope_probe.py lib @fb6089b
      (python3 -I); out_probe.py lib37 @fa086876 and files; cyc_probe.py named|lib @d104aac2.
    - REFEREE-2 (from its own directory, paths ../../../experiments/…): R2-N5-P1/p1_check.py N lo hi seed 4000, mutation.py;
      R2-N5-RL/rl_check.py inst f 3 [--rand], tev_probe.py f; R2-N5-SCOPE/scope_check.py inst f 3 [--rand];
      R2-N5-OUT/out_check.py inst f 3 own|rand|spec; R2-N5-ENT/ent_check.py inst f 3 own|rand|spec.
    - Per-state traces: import docs/referee/scratch/rl_probe.py and call states(g) (set rl_probe.OO[0] = o before scope_runs). In
      a state dict "t" is τ_k; "fb" marks a fallback transition k → k+1.
  - Lead stamps run ~10 min ahead of this container's date -u; use date -u for my own stamps.
- NEEDS: Lead: start successor 7 for R41 (P-N5-NEB) and R42 (P-N5-LV). From now on successor 6 is parked: it answers questions and
  pushes nothing.

## Resume point (successor 6)
- 13:35Z (date -u): handover check pushed 043db45f. GO from the Lead (5/5) 13:36Z.
- C45 (R36, P-N5-P1) 13:46Z: docs/checker/C45.md PASS at fb1dfb9 (draft c25e2c16; unchanged at 314d220), no E-items; N-1 (d) inner quotes
  '1 ⇒ 2' vs R18's "1 ⇒ 2"; N-2 'discharged' = joint reading; N-3 (a)/(b) fixed cycle node; N-4 MERGE keeps RL-2 not repeated.
  Re-runs 7/7 IDENTICAL (lane 5101/5102, REFEREE p1_probe 6102/6103 from scratch/, REFEREE-2 p1_check 6101/6102 + mutation.py from its dir).
  Next: landed check when R36 lands; C46 = R37 (instances re-run already: rl_a/b/c 35/2 33/2 30/3, tev_cex 27/16, tevlast 11/1, inr2 32/1, all Oink OK, 1 Odd choice).
- C46 (R37, P-N5-RL) 13:55Z: docs/checker/C46.md PASS at fb1dfb9 (draft 3ee56629; unchanged at eb866134), conditional on R36 landing first.
  No E-items. N-1 FREE-FREEZE without (h) at t (covered); N-2 MERGE "FALSE"/N-RL-1; N-3 TEV FALSE = lane/L-RED record; N-4 gap map
  omits EQ-END remark + k0 row; N-5 R2 drafts 592128a4/fa0273de uncited; N-6 R2's 168 level-inf gates has no committed log.
  Re-runs EXACT: 6 instances; traces inr2 (0,6,29), tevlast (3,7,15), tev_cex (4,23); REFEREE named/lib @b7419da IDENTICAL;
  REFEREE-2 6 batch logs IDENTICAL + tev_probe. Worktree wtR46 = b7419da. Scratch tools46/trace46.py (uses rl_probe.states()).
- C47 (R38, P-N5-SCOPE) 14:03Z: docs/checker/C47.md FAIL at 314d220 (draft f3b27c34): E-1 (f) CN-LAST hypothesis garbled (drops
  "(Iσ_k ≠ ∅), and suppose"; reads "Even switches every gate"). N-1 WCH repair wording; N-2 R2 1f8a9109/8655f692 uncited; N-3 limit (iii)
  = REFEREE-2 climbs. Re-runs EXACT: wd16_s2 19/14, wd12_s1 8/7, pftheta 38/1 (33 θ-changes in 1 scope run after the level-31 fallback),
  oc12_s1 10/1 (k 6, M −1, ¬H1, gates 0→7, 7→8); REFEREE scope_probe lib @fb6089b = §8 exactly; REFEREE-2 6 logs IDENTICAL.
  Worktree wtS47 = fb6089b. Next: Add. 1 on the Lead's revision; landed checks R36, R37, R38.
- 14:07Z: C45 Add. 1: R36 landed verbatim at 601df6ed, C45 CLOSED. C46 Add. 1: R37 landed verbatim at da5bac3a (after R36), C46 CLOSED.
  C47 Add. 1 14:12Z: PASS at fa7d1231 (773af264; E-1 fixed, N-2, N-3 applied). C47 Add. 2 14:22Z: R38 landed verbatim at 7fc7ac90; C47 CLOSED.
  Next: C48 = R39 (P-N5-OUT), when the Lead drafts it (after REFEREE-2 9's OUT §C). Known: REFEREE OUT §C a8b8ef3; fixes
  docs/new/P-N5-OUT-fixes-box37.md 640a5db2 (l-new dd3f780).
- C48 (R39, P-N5-OUT) 14:52Z: docs/checker/C48.md FAIL at efa00f59 (draft e6eeb791): E-1 (e) NO-ENTRY-A last clause unquantified
  (signed: z ∈ R̄_t, ≡); E-2 (g) W-SIDE stated for every gate (signed: Case 1 + separate Case 2 clause); E-3 "both referees reproduce
  a break" (only REFEREE-2). Data and REFEREE sums (127, 391, 121, 88/889) PASS. Re-runs EXACT: 5 instances, nebc trace, REFEREE
  lib37/named @fa08687 + cex, REFEREE-2 15 logs. Worktrees wt48 = efa00f59, wtR48 = fa086876.
  C48 Add. 1 14:59Z: PASS at 9639fa20 (6760c1c6; E-1..E-3 fixed). C48 Add. 2 15:14Z: R39 landed verbatim at 3b469f50; C48 CLOSED.
  C49 (R40, P-N5-ENT) 15:36Z: docs/checker/C49.md FAIL at b427e45d (draft 019100c7): E-1 "REFEREE-2's report does not address the
  lift" is false (R2 §C C.1 l.200). N-1 tev_cex row unlogged (reproduced); N-2 "REFEREE 654" = all (Σ)-pairs. Re-runs EXACT: REFEREE
  cyc_probe named/lib @d104aac2 + tev_cex 15/414/19/16/19; REFEREE-2 ent_check 12 logs. Worktrees wt49 = b427e45d, wtR49 = d104aac2.
  C49 Add. 1 15:46Z: PASS at 23544b8 (28bbe2c3). Next: landed check, then handover (Lead agreed 15:45Z).
- Worktree wt45 = fb1dfb9 (scratchpad), tools/oink/build symlinked. Scratch tools46/run1.sh = n5 + check_sol2 + odd-choice count.
- Queue (Lead 13:48Z brief stamp): C45 = R36 (P-N5-P1), C46 = R37 (P-N5-RL), C47 = R38 (P-N5-SCOPE): draft docs/agents/R38-draft.md @ trunk 314d220,
  sha1 f3b27c34…; packet docs/new/P-N5-SCOPE-box36.md c3f5ed37 (l-new 8483279, pin 8998ee6); fixes e2550755 (l-new eb5477a);
  REFEREE fb6089b + 560ff4c, §C 257c3d8 (also RL climb numbers); REFEREE-2 6d6e4bc, §C fb6fa69; re-runs wd16_s2 (O-1),
  oc12_s1 (CN-LAST residue), pftheta_cex_n32 (§7 dead end), referee probe samples.

## Handover check (successor 6)
Written 2026-10-25 13:26Z (date -u). CHECKER successor 6 (Opus 5.5, D15 / L37), session_01XuHZ95RA84WV7mhDqDjRQ4. Predecessor:
successor 5, session_012hVNR58N2BoF9EB98pS6HX, handover commit 2694199d. Every answer measured from the repository; commands named.

1. Branch, head, distance to trunk.
   - Container started on claude/checker at 52a1e489 (C27 Add. 4); `git status`: "up to date with 'origin/claude/checker'" (stale ref again).
   - Trunk = claude/vibrant-johnson-nxvvxo (docs/NOW.md l.14; `git remote show origin` HEAD branch). There is no `main` (`git fetch origin main`:
     "couldn't find remote ref main").
   - `git fetch origin claude/vibrant-johnson-nxvvxo claude/checker`; trunk fb1dfb92. `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`:
     0 ahead, 1392 behind; `git merge-base --is-ancestor HEAD <trunk>`: yes; handover 2694199d is on trunk.
   - `git merge --ff-only <trunk>` → fb1dfb92; `git merge --no-ff <trunk>` → "Already up to date" (no merge commit possible: 0 ahead).
     This file's commit makes 1 ahead, 0 behind.
2. Open work and next step.
   - C41-C44 CLOSED (handover table; docs/checker/C41.md..C44.md). Nothing in flight from successor 5.
   - C45 = R36 (P-N5-P1): NOT STARTED. `sha1sum` at fb1dfb92: docs/agents/R36-draft.md c25e2c16… (= Lead brief), packet b98ca794…,
     fixes 83ef83b0…, addendum docs/si/P-N5-RL-P1-addendum-box10.md 5c29d93d…. `git log -- docs/agents/R36-draft.md`: 351953cc, fb1dfb92.
     Next: after GO, the six-step method (pins, cited SHAs with `git show --stat`, read in full, data trace, re-runs in a detached
     worktree of fb1dfb9, then landed check), report docs/checker/C45.md.
   - C46 = R37 (P-N5-RL): draft docs/agents/R37-draft.md 3ee56629… (= brief); packet 0a3c70cb…, fixes ac027458…, fixes2 b3e3cd93… (= brief).
     Next: after R36 lands; same method plus the named re-runs; report docs/checker/C46.md.
   - Later: R38 (P-N5-SCOPE). No docs/agents/R38-draft.md yet (`ls`). Note: the L-NEW fixes file the Lead waits for already exists:
     docs/new/P-N5-SCOPE-fixes-box36.md, sha1 e2550755…, l-new eb5477a2 (on trunk). Then OUT and ENT.
   - Branch heads 13:26Z (`git fetch` + `git merge-base --is-ancestor`): referee 6d480e7d on trunk; referee-2 ba6fac1b on trunk;
     l-new eb5477a2 on trunk; l-si 6cb8a22c OFF trunk (1 commit: docs/si/N5-STR2-box11.md only, not a cited file).
   - Oink: tools/ absent at start; scripts/setup_oink.sh run 13:2xZ, exit 0 (log in scratchpad).
3. GAPS rows. `awk -F'|' '$4 ~ /CHECKER/' docs/GAPS.md`: none; CHECKER owns no row. Relevant on the landing side: G-N5-TIME (major,
   L-NEW, open). Last UPDATE 11:51Z (R35 landed, CHECKER C44): "Open: NJB = ENT (CONJECTURE; lane reductions EV/EV+/TEV-RED in review as
   P-N5-RL), REL(S), level −1 fallbacks, out-of-scope fallbacks (P-N5-SCOPE in review; lane NO-ENTRY-A), θ-changes per HN stretch. Lane
   (unrefereed): Lemma P1 = (P) for one-player games." R36 and R37 each add one append-only UPDATE; landed check: old row (minus " |")
   is a prefix of the new one, status stays open.
4. Owner rulings verbatim (docs/DECISIONS.md, `grep -n -F`), status from docs/DECISIONS-INDEX.md (`grep -E "^\| *(D1|D15|D18|L37|L40) "`):
   - D1 (DECISIONS.md l.7; index "active"): "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
     claim, including the fleet's own, as wrong until it passes the gauntlet below."
   - D15 (l.278; index D15 "active", L37 "active"): "q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it"
   - D18 (l.333; index D18 "active", L40 "active"): "Focus on N5 and work toward proving it. Explore novel approaches, especially by
     connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
     where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems."
   For the gate: nothing landed stronger than both signatures (D1); "(Opus 5.5, D15)" labels (L37); PROVED / CONJECTURE / OPEN exact (L40).
5. Trap found. The R36 draft sha1 that successor 5 recorded as "verified" (9d66adbc… @ 351953c) is stale: the Lead revised the draft at
   fb1dfb92 (now c25e2c16…). A successor working from the handover's sha1 would check the wrong text. Check: `git log -- <draft>` and
   `sha1sum` at the brief's trunk SHA, never the handover's number. (Also: trunk is not `main`; and this container's `date -u` read
   13:26Z while the Lead's brief is stamped 13:35Z, so stamps across sessions can disagree by minutes.)

## Handover check (successor 5)
Written 2026-10-25 09:01Z (date -u). Predecessor: successor 4, session_01G2KY2Canmj54k82CwBrZYc, handover commit 4d8ba2b5
(C40 Addendum 1, "handover to successor 5"). Every answer measured from the repository; commands named.

1. Branch, head, distance to trunk.
   - Container started on claude/checker at 52a1e489 (C27 Add. 4), 'git status': "up to date with 'origin/claude/checker'" (stale
     remote ref). `git fetch origin claude/checker claude/vibrant-johnson-nxvvxo`: origin/claude/checker 737b1938, later 4d8ba2b5
     (Add. 1 landed 09:00Z, watched by a fetch loop). `git merge --ff-only origin/claude/checker` → 4d8ba2b5.
   - `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` at 4d8ba2b5: 1 ahead, 1 behind trunk 3e339bbb.
   - `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` → merge commit 21b82302: 2 ahead, 0 behind. This file's commit makes 3 ahead.
2. Open work and next step.
   - C28-C40 all CLOSED (`grep -n "CLOSED\|Addendum" docs/checker/C40.md`; C40 Add. 1: R31 landed verbatim at 3f2b5c1). Nothing pending.
   - C41 = R32 (packet P-N5-FRZ). docs/agents/R32-draft.md does not exist (`ls docs/agents/R32*`: none). Inputs at trunk 3e339bbb
     (`sha1sum`): packet docs/new/P-N5-FRZ-box34.md 39df373c… (frozen edbccb69; pin trunk 25fda0f per the Lead), fixes
     docs/new/P-N5-FRZ-fixes-box34.md 168de464…, docs/referee/R-N5-FRZ.md f542c2d7… (3a520ce7, Addendum 3171efc7), docs/referee-2/R2-N5-FRZ.md
     2039d70d… (20a73ca1, §C f546b43c). Still coming: fixes2 (L-NEW successor 15), REFEREE successor 7's §C.
     Branch heads 09:00Z (`git merge-base --is-ancestor`): referee 1f13a6f9 OFF trunk, l-new 5f02ceba OFF trunk, referee-2 f546b43c on trunk.
   - Next step: after GO, setup_oink.sh (tools/ absent in this container), then pre-check pins/sha1 across first-parent states, read
     packet + fixes + both reports, prepare the re-run list; on the Lead's draft sha1, the five checks as in C37-C40, report docs/checker/C41.md.
3. GAPS rows. `awk -F'|' '$4 ~ /CHECKER/' docs/GAPS.md`: no output; CHECKER owns no row (13 rows). Relevant (landing side):
   G-N5-TIME | major | L-NEW (L-LIT T22; referees later) | open; last UPDATE: "R31 [refereed-only] LANDED (P-N5-FBW + fixes; CHECKER
   C40) … In review: P-N5-FRZ (both referees signed; landing next), P-N5-L2, P-N5-NJB, P-N5-TOG". R32 adds one append-only UPDATE to
   this row; my landed check: old row is a prefix of the new one, status stays open.
4. Owner rulings verbatim (docs/DECISIONS.md), status from docs/DECISIONS-INDEX.md (`grep -E "^\| *(D1|D15|D18|L37|L40) "`):
   - D1 (row D1 "active"; key line): "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim,
     including the fleet's own, as wrong until it passes the gauntlet below."
   - D15 (row D15 "active"; L37 "active"): "q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it"
   - D18 (row D18 "active"; L40 "active"): "Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting
     ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where
     needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems."
   For the gate: no landed claim stronger than both signatures (D1); labels "(Opus 5.5, D15)" checked (L37 (1)); PROVED / CONJECTURE /
   OPEN and ASSUMPTION labels exact, nothing resting on an ASSUMPTION called PROVED (L40 (3), (4)).
5. Trap found. The container's clone was stale: local claude/checker AND its remote-tracking ref sat at 52a1e489 (C27, 2026-10-24),
   13 CHECKER reports behind, while `git status` said "up to date". Working from it would have re-done or contradicted C28-C40.
   Check: `git fetch` the branch first and compare `git rev-parse HEAD origin/claude/checker` after the fetch; fast-forward only.
   (Second, measured: tools/oink/build is absent here, so verify's Oink smoke is NOT RUN and re-runs cannot use zlk until setup_oink.sh.)

## Resume point (successor 5)
- IDLE 11:5xZ (date -u): C41-C44 all CLOSED (R32-R35 landed verbatim). Next per the Lead: P-N5-SCOPE and P-N5-RL once drafted.
- C41 (R32, P-N5-FRZ pinned 25fda0f) 09:21Z (date -u): main report docs/checker/C41.md: FAIL at eb3f659 (draft sha1 6d23f986…):
  E-1 REFEREE C.6 commit 9ad6bfba uncited (limit (iii)'s REFEREE half rests on it); E-2 "3,610 in climbs aimed at leaves" = all 12
  climbs (leave climbs 1,040); N-1 fixes2 unrefereed (content = REFEREE-2 C.4 row 4, checked); N-2 R29 (c) vs (e), outside the draft.
  Every re-run EXACT. Add. 1 d43a3222: rev. 2edf33e (d8369b2b) E-1 fixed, E-2 open, N-3 optional. Add. 2 7f5df64b: PASS at 06fbc11
  (5552686a). Add. 3: PASS at f87c5fd (b3f7fc67, + N-3). Add. 4: R32 landed verbatim at trunk 8e6d6c2
  (N-4 optional: GAPS UPDATE omits (L2), ¬H1 SN). C41 CLOSED. Next: C42 = R33 (P-N5-L2) when the Lead sends the draft sha1.
- Worktrees (scratchpad): wt = eb3f659, wtR = 3a520ce, wtC6 = 9ad6bfba; tools/oink/build symlinked; Oink built 09:1xZ (setup_oink.sh exit 0).

- C42 (R33, P-N5-L2 pinned 04b3f48) 10:3xZ (date -u): main report docs/checker/C42.md: FAIL at 8d95c31 (draft sha1 dbadd869…):
  E-1 REFEREE §C cited 5e85c70 (= R-N5-NJB §C) instead of ce241061; E-2 REFEREE-2 "+ e65cbcd" (NJB-only). N-1 limit (iv) "three
  climbs"; N-2 limit (v) vs box-35 DATA instances; N-3 l2_pc needs NMAX=14. Every re-run EXACT. Add. 1: PASS at 48478ab (8d9d6590; E-1, E-2, N-1, N-2
  fixed). Add. 2: R33 landed verbatim at trunk
  00bd18b. C42 CLOSED. Next: R34 (P-N5-NJB), R35 (P-N5-TOG) when the Lead sends draft sha1s (each after a lane fixes2).
- Worktrees: wt42 = 8d95c31, wtR42 = 7626354e. Scratch c42/trace.py = per-state trace via REFEREE l2_probe.states().

- C43 (R34, P-N5-TOG pinned d3daae1) 10:5xZ (date -u): main report docs/checker/C43.md: FAIL at 4be5bba (draft sha1 3b20da39…):
  E-1 "238 files" ×2 = REFEREE-2's text, but its files.lst / 484 logs / 31,434 runs give 239. N-1 fixes2 unrefereed (records only);
  N-2 REFEREE l.9 5e85c706; N-3 REFEREE-2's 238. Every re-run EXACT. Add. 1: PASS at 3c0c2aa (33dbffd3). Next: Add. 2 =
  landed-text check; then NJB = R35.
- Worktrees: wt43 = 4be5bba, wtR43 = fff6e624.

- C44 (R35, P-N5-NJB pinned a7d85b3) 11:3xZ (date -u): main report docs/checker/C44.md: FAIL at a627c7d (draft sha1 c28e6902…):
  E-1 (5′) paraphrased (signed = REFEREE l.27 / fixes NJB-2 verbatim); E-2 REFEREE-2 SIGN list omits ENT-SHAPE (1)-(4).
  N-1 l-si 90b5fb3f edits cited fixes2 in place (8ceee866 → 647386fb, off trunk); N-2 REFEREE C.5 3 rows; N-3 b6 fb18 also on SPEC.
  Every re-run EXACT. Worktrees wt44 = a627c7d, wtR44 = 524d93f5. Add. 1: rev. 7b1a47d (f730b554; fixes2 → 647386fb):
  E-1, E-2 OPEN. Add. 2: PASS at 3fc6cf1 (6f77aca6). Add. 3: R35 landed verbatim at 4151e41, C44 CLOSED.
  C43 Add. 2: R34 landed verbatim at e784554, C43 CLOSED.

## Resume point (successor 4, history)
- PARKED 16:22Z (date -u). C28 CLOSED:
  - main report b53136d7: FAIL E-1..E-6;
  - Add. 1 e5c46943: E-1..E-6 fixed, E-7 = the §A citation;
  - Add. 2 8f2ee01d: PASS at 1494ae1;
  - Add. 3: R19 landed verbatim at trunk 4155cde.
- C29 CLOSED 17:19Z (date -u):
  - main report 5a395403: FAIL E-1..E-3;
  - Add. 1 aa909fd0: PASS at 865a33a (REFEREE §C7 a1de721 signs the Corollary);
  - Add. 2: R20 landed verbatim at trunk c33700c.
- C30 CLOSED 19:3xZ (date -u):
  - main report 7bf19993: FAIL E-1..E-4;
  - Add. 1 679ea117: PASS at f9c75d2, including the R19 POST-LANDING NOTE (RESULTS l.882);
  - Add. 2: R21 landed verbatim at trunk e72db8d.
- C31 CLOSED 20:4xZ (date -u):
  - main report c500832b: FAIL E-1;
  - Add. 1 4db6e4c0: PASS at b112bd5;
  - Add. 2: R22 landed verbatim at trunk 200a511.
- C32 CLOSED 21:3xZ (date -u):
  - main report 2cd52a68: FAIL E-1;
  - Add. 1 0077eed8: PASS at 0d72267;
  - Add. 2: R23 landed verbatim at trunk 8de876b.
- C33 CLOSED 22:3xZ (date -u):
  - main report 0102170b: FAIL E-1; the R22 POST-LANDING NOTE PASS;
  - Add. 1 59a97995: PASS at a85316a;
  - Add. 2: R24 landed verbatim at trunk 7bcf681.
- C34 CLOSED 23:5xZ (date -u):
  - main report 298e4b6d: FAIL E-1, E-2;
  - Add. 1 4278b5a2: fixes part 2 PASS, E-1/E-2 still open;
  - Add. 2 e9f7b674: PASS at 7666336;
  - Add. 3: R25 landed verbatim at trunk 40ef7ed.
- C35 (R26, P-N5-U23 pinned 7666336) 00:4xZ (date -u):
  - main report docs/checker/C35.md: PASS at 37a4a06 (draft sha1 abd35e40…); optional N-1 (limit (v) "~90" relayed only via fixes §5;
    L-RED R65 off trunk 1c2f1d8f), N-2 (no change);
  - Add. 1: R26 landed verbatim at trunk eb8e22e. C35 CLOSED.
- C36 (R27 = P-N5-LP pinned bc42f2c + P-N5-SO pinned 1ef02bb) 01:5xZ (date -u):
  - main report docs/checker/C36.md: FAIL at e8c26f3 (draft sha1 d22885f8…): E-1 joint gap map's SO rows are REFEREE-2 §C only (REFEREE §C
    = Part 1 only); E-2 HI's "≤" Consequence single-signed (REFEREE HI-1); N-1 limit (v) wake type sourced only in notes/L-NEW.md; N-2.
  - Add. 1 c64ec130: PASS at 1d35e8e (draft sha1 a9ba93ec…; E-1, E-2, N-1, N-2 fixed);
  - Add. 2: R27 landed verbatim at trunk 58de2bc. C36 CLOSED.
- C37 (R28, P-N5-OE pinned 361d18c) 02:2xZ (date -u):
  - main report docs/checker/C37.md: PASS at f6786ba (draft sha1 a5229c8e…); optional N-1 (Reading "≡ Z" is one direction, REFEREE §3.6),
    N-2 (696b08c touches only notes/REFEREE.md);
  - Add. 1: R28 landed verbatim at trunk de7a635 (GAPS row: stale R27 "§C pending" clause replaced by the R28 update). C37 CLOSED.
- C38 (R29, P-N5-CLS pinned 486107a) 03:22Z (date -u):
  - main report docs/checker/C38.md: PASS at 42eccf9 (draft sha1 e4189cd3…); optional N-1 (N-CLS-2 is a row of REFEREE C.3 only);
  - Add. 1 f0cf7c90: PASS at 1efb9f9; Add. 2 7d31abaa: PASS at b2fcd17 (N-1 fixed);
  - Add. 3: R29 landed verbatim at trunk cf6801e. C38 CLOSED.
- C39 (R30, P-N5-SN pinned 2c70ef6 + fixes §2b) 04:47Z (date -u):
  - main report docs/checker/C39.md: FAIL at a9fc3c9 (draft sha1 08526310…): E-1 epsseg_cex_n48 re-absorption is transition 14, not 13;
    N-1 L-RED box 37 line sourced only in LEAD-STATE (R67 not on trunk); N-2 sample names; N-3 note.
  - Add. 1 262104b2: PASS at 91582c0 (E-1, N-1, N-2 fixed);
  - Add. 2: R30 landed verbatim at trunk 659f574. C39 CLOSED.
- C40 (R31, P-N5-FBW pinned e69772b) 08:41Z (date -u):
  - main report docs/checker/C40.md: PASS at 61c7cd1 (draft sha1 f2d4a606…); optional N-1 (REFEREE-2's committed logs predate its
    'tight' counter; outside the draft);
  - Add. 1: R31 landed verbatim at trunk 3f2b5c1. C40 CLOSED.
- PARKED for good (successor 4). The Lead starts CHECKER successor 5 for R32 (P-N5-FRZ).
- HANDOVER to successor 5. Every check C28-C40 is CLOSED; nothing is pending in docs/checker/. Next: R32 (P-N5-FRZ). The method is the five-step gate in
  'Conventions' plus: verify every sha1 at the pin and across first-parent states; check each cited commit is an ancestor; re-run named
  instances (n5 + check_sol2 + one-Odd count) and one probe per referee in a detached worktree (symlink tools/oink/build); trace every
  Data number to a referee file line; landed check = cmp block vs draft lines 3-end with the header fill, delete block + cmp rest vs
  the pre-landing RESULTS, GAPS row prefix (append-only, agreed with the Lead 02:46Z).
- Oink is built in this container (tools/oink/build, 8fbf0a7), so verify's Oink smoke now runs. In a worktree, symlink tools/oink/build.
- Handover check: docs/agents/handover-checks/CHECKER.md (f28356ae).

## Conventions (from C27, kept)
- Pin everything: draft trunk SHA, signed object sha1, report commits. Each cited commit must be an ancestor of the trunk pin.
- Re-fetch referee, referee-2 and lane heads before a verdict; name any head that is off trunk.
- Re-runs go in a detached worktree of the pin, scripts unmodified (scratchpad wt/); compare against the referees' logs with `diff`.
- Report E- items (required) and N- items (optional) with fixes. Addenda go at the end of the same file, one per draft SHA.
- Push: scripts/push.sh > file; echo $? (never piped). Oink built here at 19:0xZ by setup_oink.sh (a fresh container must rebuild it).

## Sources opened (for C28)
- docs/new/P-N5-RE-box26.md @52c7261 (sha1 8dba4576…); docs/referee/R-N5-RE.md @a3d1f70; docs/referee-2/R2-N5-RE.md @dd5aaa2;
  docs/new/N5-time-box21.md §3.5 (Lemma G (d), the source of the draft's (a) wording); docs/new/N5-xing-box27.md §6, §8, §9;
  docs/red/R58-n5-width.md §13c.

## Things only I know
- (successor 5) Briefs may name a SHA from the sibling packet (NJB vs L2 on the same branch): check each cited SHA with
  `git show --stat` against the report file. REFEREE l2_pc.py library row needs NMAX=14 (default 9).
- orx.py (EPS=1) ex_ORX = (first ε, second ε, exit) with transition indices; absorption = transition k with x0 ∈ F_k ∩ R_{k+1}.
  Scratch tool c39tools/trace33.py (scratchpad, not committed) prints σ̄(o) and exit-in-R per transition via box32/dormant.py.
- REFEREE oe_probe.py: `lib` and `rand|randb N lo hi seed` from the worktree root; its "random 50" ties = so_tie_nX_* summed over seeds 7101-7104.
- REFEREE's so_probe.py ignores file arguments (only `rand` / `lib` act); run `lib` from the worktree root to reproduce its Part 2 numbers.
- REFEREE-2's re_check.py `inst ... own` defaults to 20 runs; the logged file uses 30 (run_all.sh). With 30 the output is diff-identical
  (seeded Random(1)).
- REFEREE's re_probe.py runs from docs/referee/scratch/ (it imports the box25 tools by path).
- l-red 3551ed0a (box 31 xclimb) was off trunk at 15:24Z; not cited by R19.

## Dead ends
- None (a gate lane).
