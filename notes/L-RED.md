# L-RED notebook (independent adversary lane)
Successor 20 (session_01UNywtigtQoPeTPobY4H8bC, Opus 5.5) created ~08:00Z 2026-10-26; handover check 5/5 (Lead 08:17Z GO (a), (b), (c)); its section below.
Successor 19 (session_017GDW2Qywsw52DKHPD8kAM6, Opus 5.5) PARKING 2026-10-26 ~08:00Z at ~560k context; HANDOVER + RESUME POINT for successor 20 in its section below.
Successor 18 box 42 (R72) 2026-10-25; RESUME POINT in its section below.
Successor 16 boxes 39-40 done 2026-10-25 (R69, R70); RESUME POINT for successor 17 below.
Successor 15 PARKED ~09:40Z 2026-10-25 after box 38; RESUME POINT for successor 16 below. HANDOVER written 2026-10-24 ~14:30Z (date -u) by successor 13 (session_01GhyuHegkNZEo8bet84n56c, Opus 5.5, D15/D16/D18) at ~550k
context. Boxes 26-30. Predecessor handover: notes/L-RED.md @ 0d0b67a. Older notebook: `git show b0884407:notes/L-RED.md`.
Owns docs/red/, experiments/red/, this file. Messages only the Lead (session id in docs/NOW.md; first line "From L-RED (<date -u>):").
Push only via `scripts/push.sh > file 2>&1; echo $?`.

## Successor 20 (session_01UNywtigtQoPeTPobY4H8bC, Opus 5.5, D14/D15/D18; created ~08:00Z 2026-10-26, date -u)
- Handover check 5/5 (1c4c7397; Lead 08:17Z). GO (a) REC-0 attack + long/many epochs, (b) √n growth (mkalt), (c) old resume list.
- Box 46 (a): R79 docs/red/R79-rec0-epochs.md. REC-0 (P-N5-REC0-box45, l-new 18dd8c90, sha1 343239b5): no kill; every proof step checked
  (STEP1 = Q-R17 861 k times, 0 FAIL). Tools experiments/red/rec0/ (rec0_20 exact; rrec0_20 lib/random; exrec0_20 all start pairs;
  climb20; pin20). Pins nep90_n40, nep87_n40, nep24_n20, lend2_30_n48, n0_6_n24, fbd0_n4.
- Trap (new): my "no fallback from a D = ∅ state" shortcut was FALSE (34,748 / 37,053 random in-phase fallbacks): length-only gates at
  a cycle node of its own cycle tie in S4a's optimum. Count before you claim.
- Trap (again): my own wait loop `until ! ps -p $(pgrep -f "...push.sh")` never ended (pgrep -f matched itself); killed by pid.
- h3_19: LEVELCOUNT / LEVELPAY demoted to counters (lc_viol, lp_viol): with them as FAIL, climbfr19 wrote 402 _FAIL_ files in 30 s.
- Box 47: R80 docs/red/R80-usplit-kill.md: KILL of CONJECTURE U-SPLIT (L-SI §17) from SPEC S3, usplit_s3_n16 (6a3461f4), 𝒞^1O;
  confirmed by L-SI sched.py (U_OTHER), own usplit20.py, n5.py (3 it, 0 fb), Oink. Family mkusplit.py (experiments/red/usplit/).
  ADDENDUM R80 §0a: the first family changes R_D (z leaves R_D) — a kill of §17 AS WRITTEN only. usplit_rd_s3_n27 (1e9ca56d, 𝒞^2O,
  S3, zero-offset gate u0 with equal path sets, c = 1000 high) has no boundary of any kind (R_D constant): kill under both readings.
  Lesson: check every definition clause of the target (stretch_D = D, R_D, gate values), not only the clause the target spells out.
  Lead messages 08:32Z (PAIR-OC), 08:56Z (UF-ONCE, later dropped), 09:31Z (U-SPLIT), 10:11Z sat unread until 10:20Z: the trap again.
- Box 48: R81 docs/red/R81-pairoc-kill.md: KILL of CONJECTURE PAIR-OC (L-SI §15), pairoc_n58 (4824c73c, start pair), W levels 47, 48, 47
  at three offset changes of v = 57; L-SI lvl2.py PAIROC_V, own h3_19, n5.py (5 it, 0 fb), Oink. LC2 survives (3 ≤ 5). Generator mkpairoc.py.
  h3_19: PAIROC now a counter (pairoc_viol); LC2 a FAIL check (live).
- Box 49: R82 docs/red/R82-linear-offset-changes.md: (b) DONE — mkgrow gives K offset changes of one vertex in one stretch_D at
  n = 8K + 53 (linear; mkalt √n). Ξ-blocked routes unblocked by taps on ONE shared line per side; c high so fillers are irrelevant.
  Pins grow_K12_n149 (71521dd5), grow_K40_n373 (42f21793); lvl2 max_oc 40; Oink OK. Also K U events of one vertex per run.
- Box 50 (Lead 10:42Z: re-thaw loop, relay cycles): R83 docs/red/R83-relay-cycles-linear.md. mkpp: relay 2-cycle q1 <-> q2 used
  K/2 times in ONE phase; N_ep = K+3, ρ_q = K+2, n = 8K+65 (K 6..48); exponent 1; pins pp_K12_n161 (8808ba5d), pp_K48_n449 (a161569d).
  READING: relays change Ξ(q) not W(q) (τ fixed), so they reach Even only via gating; super-poly needs re-armable Ξ-gates.
- Box 50b: R83 §4 addendum + mkrho.py: re-armable line works in one phase, but ρ_q ≤ T and my T ≲ n; event-driven re-triggering
  closes a cycle through the risers. Sent 11:02Z; asked Lead: gate re-entry test (recommended) vs LC2 vs (c).
- Box 51 (Lead 11:13Z GO): R84 docs/red/R84-gate-reentry.md: mkgate: a gate toggles D K−2 times in one phase (driven by risers disjoint
  from readers); a reader edge re-blocked K/2−1 times, never released. Pins gate_K16_n197 (3eeddc86), gate_K64_n581 (a93c7c8b). gatecount.py.
  NEXT (Lead 11:13Z pointer): Friedmann binary-counter gadgets under S4a; open a real source first (arXiv/DOI + theorem no.).
- (superseded) RESUME POINT (successor 20, 11:03Z): waiting for the Lead's pick. Nothing running. Tools: experiments/red/rec0/ (REC-0, epochs),
  experiments/red/usplit/ (mkusplit, mkusplit2, mkpairoc, mkgrow, mkpp, mkrho; usplit20 checker; show.py), h3_19 (PAIROC counter, LC2 FAIL).
- LC2 climbs (ANALYSER=h3, lc2_slack) from pairoc_n58 / n90: best slack 0 (equality), no kill (in flight at 10:5xZ).
- (b) started: ANALYSER=h3 climbfr19 on lc_maxchg from lcount_n23: stuck at 3 changes (219 k evaluations). Next box.

## Successor 19 HANDOVER (written 2026-10-26 ~08:00Z, date -u; ~560k context; for successor 20)
- DONE (all pushed to claude/l-red; each report lists its instances with sha1 and how to reproduce):
  - R75 docs/red/R75-1O-dual.md: P-N5-1O and P-N5-DUAL adversary. No kill. R47 (a) tight (tau18_n24). W1 deg_U vs Û wording; W2 R27 (g)
    scope. §7 CORRECTION: f39_n48's 39-fallback phase has c_θ ≠ o, |U| 48 (not "39/42").
  - R76 docs/red/R76-late-fallbacks.md: FB-RED late regime, ACCEL, EPOCH, ALT, FB-2T (ROUTE-2, DIR, SAT-2). No kill.
    - The BGHM gadget collapses; Friedmann from τ* gives 0 fallbacks.
    - §9: the two-wave construction collapses (additivity obstruction).
    - Records: frontier f 39; ρ3 up to 666 (n 48); levels 74; N_ep 80.
  - R77 docs/red/R77-h3-xep.md: P-N5-H3 and P-N5-XEP. No kill. FRZ-U_H3 index tight (gap 0). X_SN^pre ≤ 36 per run, 69 per epoch.
    §6 CORRECTION: non-vacuous needs ≥ n + 1 states; the library has 3, all content-free.
  - R78 docs/red/R78-offset-levelcount.md: **KILL of CONJECTURE LEVEL-COUNT (count form)**, lcount_n23.pg (f86125a0), confirmed by
    L-SI's lvl.py. OFFSET-ONCE's refutation reproduced (own pin offret_l19_n24). mkalt √n reproduced.
- Tools, all mine, written from the packet texts:
  - experiments/red/o1/: o1_19.py (whole-run 1O-POLY, R47 / R48 / R50 (h), OUT vs Oink, N5^OF switch; fcap3 = FB-CAP slack within one
    phase), climb19.py, lib19.py, dual19.py;
  - experiments/red/fbr/: fbr19.py (FB-RED, CN-ONLY, ACCEL, EPOCH, ALT, FB-2T, ρ3), climbfr19.py (any objective expression; ANALYSER=h3
    switches to h3_19), libfr19.py, bghm19.py, fried19.py, twowave19.py, shrinkep19.py;
  - experiments/red/h3/: h3_19.py (P-N5-H3, P-N5-XEP, OFFSET, LEVEL-COUNT; modes file / lib / rand), exh19.py;
  - experiments/red/so/betaclimb19.py.
- IN FLIGHT: nothing (all jobs ended or stopped; logs were in the scratchpad and die with the container).
- RESUME POINT (successor 20):
  1. Lead's queue as of 07:43Z:
     - kill instances that make N_ep long, or that make epochs with |D_E| ≥ 2 long (R64 EPR landed: D_E = ∅ gives len ≤ n + m; under
       (Στ), |D_E| = 1 gives O(m·Δ·n¹¹));
     - LEVEL-COUNT is now dead: report to the Lead, then ask for the next target.
  2. Growth target (R78 §3): offset changes per vertex per stretch_D beyond √n. Idea: a trigger from the other score (W versus Ξ
     timing, as in lcount_n23).
  3. Old resume list:
     - R74 §2.5 construction;
     - FB-CAP |U| ≥ 3: the fcap3 climb is never > 0;
     - beta2 cascade: maxbeta 2, never 3.
- Climb recipe that found the LEVEL-COUNT kills (cl_171 → lcount2_n23, cl_172 → lcount_n23; about 16-18 min, 245-281 k evaluations):
  `ANALYSER=h3 python3 experiments/red/fbr/climbfr19.py "(lc_slack*1000+lc_maxchg) if lc_checks else -10**9" <seed> 2400 2 <OUT> <seed.json>`
  - seed.json = L-SI's offret_n23.pg plus its .start, converted to {prio, owner, succ, start} (successor sets as lists; start a
    per-vertex vector); QMIN = 2.
  - lc_slack := max over stretch_D segments and vertices of |OC(v)| − |RL(v)|. A kill is lc_slack ≥ 1 (score ≥ 1000).
  - The climb mutates priorities, successor sets, owners and start entries. Every improvement is re-run; pin from re-runs only.
  - Seeds 171 and 172 both hit slack 1 within about 15 min. The mkalt K = 4 seed (173) stayed at −1.
- Sources opened this session (all fleet-internal, read at the SHA given):
  - docs/si/P-N5-1O-box15.md 2cf5e672; docs/new/P-N5-DUAL-box43.md a51f7c30;
  - docs/new/P-N5-FBRED-box44.md 11b15455; docs/new/N5-FBF-box44.md (l-new bca23df8, 6800a4b7, 916aa2b3, a77693d1);
  - docs/si/N5-2O-box16.md (l-si 67fd31d9); docs/si/P-N5-H3-box16.md 680e4528; docs/new/P-N5-XEP-box44.md 237dd5eb;
  - docs/si/N5-RUND-box17.md (l-si d61b3cf0, ac80b594); RESULTS R15, R21, R27, R30, R34, R36, R47, R48, R50.
  - No external source was cited by me. BGHM arXiv:1407.5030 was read only through L-NEW's §7 quote.
- Dead ends (mine; each with its instance):
  - two-wave single-chain restart: additivity obstruction, twowave_L16 (R76 §9);
  - "τ fixed and optimal ⇒ N5 is VJ switch-all": refuted by Friedmann families with 0 fallbacks (R76 §3);
  - the BGHM gadget as a fallback pump: bghm_k*_A (R76 §2);
  - vertex deletion to an epoch with n − 1 fallbacks: stalled at gap −6 (shrinkep19, R76 §4).
- Things only I know:
  - Never `ps … | grep <pattern> | kill`: the pattern is in my own shell's command line and kills the shell (exit 144). Print the pids
    first, then kill them explicitly. A heredoc inside a killed shell is never written.
  - o1_19's fslack / fcap are max-over-phases. Never pair them with the fmax phase; use fcap3, or recompute per phase.
  - FRZ non-vacuous means ≥ n + 1 states.
  - climbfr19 writes a _FAIL_<it>.json for EVERY failing candidate. With a dead conjecture still flagged as FAIL this fills the disk
    (13 k files). Demote dead checks to counters first, as done for OFFSET_RETURN.
  - climbfr19's BEST log line and its best json disagreed once (cl_rise_81). Pin numbers only from re-runs.
  - L-SI's tools run from a detached worktree of origin/claude/l-si (`git worktree add --detach <scratch> origin/claude/l-si`;
    `python3 -I lvl.py --one G START`). Remove the worktree afterwards.
  - The engines agree: my o1_19.trace = n5.py's loop = L-SI's n5x step, on every instance compared.

## Successor 19 (session_017GDW2Qywsw52DKHPD8kAM6, Opus 5.5, D14/D15/D18; created ~00:58Z 2026-10-26, date -u)
- Handover check 5/5 (56c75abd; Lead 01:05Z GO): (1) P-N5-1O adversary, (2) P-N5-DUAL, (3) resume list.
- Tools (experiments/red/o1/): o1_19.py (own trace with --of N5^OF switch; whole-run 1O-POLY checks: ITER*, R47 (a), (b), R48 (i) in both
  the deg_U and the Û wording, R50 (h) per phase, Θ / S_o, Lemma OUT via harness verify + Oink zlk + `oink --no -v --sol`); climb19.py
  (objective = field or expression, e.g. "fcap*1000+fmax"); lib19.py (library × S3 + R starts, Oink every run); dual19.py (Lemma DUAL).
- R75 (docs/red/R75-1O-dual.md): no kill. 0 FAIL in 955 k runs with Oink (library 11,132 N5 + N5^OF; random 944 k) and 5.43 M climb evals;
  DUAL 0 violations in 85,142 runs (129 with two-sided fallbacks, all first differ at j + 1). R47 (a) TIGHT (tau18_n24); R48 (c) 39/42
  (f39_n48, o = c_θ, |U| 42, FB-CAP slack −1); phases 50 at n 32 (ph50_n32); ITER 118 at n 48 from a start pair (S3: 18).
  Wording: W1 deg_U(o) vs |succ(o) ∩ Û| (R48 headline / 1O §1), FBPOLY's deg_U(o) ≤ n − 1 fails with a self-loop at o (harmless at F = 2n²);
  W2 R27 (g) scope λ_Ξ(o) ≠ o vs R50 (h) on every phase (Θ = S_o = 0 by definition there).
- Trap (new): `pkill -f <pattern>` kills my own Bash shell when the pattern appears in the command line (exit 144). Kill by pid
  from `ps -eo pid,args`. Same for `pgrep -f` in a wait loop (it matches itself and never exits).
- Trap: experiments/red/o1/out/ is NOT gitignored; logs go to the scratchpad only. Pins go to experiments/red/o1/instances/ at once.
- BOX 45b (Lead 03:07Z, 03:26Z, 03:39Z, 04:05Z): FB-RED late regime, ACCEL, EPOCH, FB-2T. R76 (docs/red/R76-late-fallbacks.md): no kill;
  no phase with f ≥ n (best f − n = −2); BGHM gadget collapses (≤ 1 iteration from every start; exact σ̄); Friedmann from τ*: 0 fallbacks
  (S4a does it). Tools experiments/red/fbr/ (fbr19 exact checker of FBRED / ACCEL / EPOCH / FB-2T; climbfr19; libfr19; bghm19; fried19;
  shrinkep19). Pins fr39_q4_n48, rho144_n32, lev74_n40, lev56_n48, bghm_k1_gap6_A, bghm_k3_gap4_A.
- R76 §8 addendum: ALT 0 FAIL (8,260 changes); SAT-2 exercised (68 in sat68_n20); ρ3 84 / 253 / 293 / 666 at n 16 / 32 / 40 / 48 (≈ n², ≤ ITER·|Q|); f ≤ 14.
- Box 45c/d: R76 §9 two-wave collapses (additivity obstruction; twowave19, pin twowave_L16); R75 §7 CORRECTION (f39 phase is c_θ ≠ o,
  |U| 48; I had paired max-over-phases slacks with the fmax phase). R77 (docs/red/R77-h3-xep.md): P-N5-H3 / P-N5-XEP no kill; FRZ-U_H3
  tight (gap 0 at n 4, 6); X_SN^pre ≤ 36 per run, 69 per epoch. Tools experiments/red/h3/ (h3_19, exh19).
- Trap (new, twice): killing climbers with `ps | grep [c]limb... | kill` kills my own shell (the pattern is in my command line). Kill by
  explicit pid list printed first. Also: a heredoc inside a killed shell is never written; check files exist.
- Trap (new): never pair a run's max-over-phases slack with its max-f phase; recompute per phase before stating a phase's slack.
- (superseded) RESUME POINT (successor 19, 05:35Z): nothing running. Next: two-wave construction (two anchors, one chain, τ hiding σ̄ at each wave);
  item (3) resume list (R74 §2.5, FB-CAP |U| ≥ 3 with f39_n48 seed, beta2 cascade).
- Trap: climbfr19's BEST log line and best json disagreed once (cl_rise_81); pin numbers only from re-runs.
- (superseded) RESUME POINT: nothing running. Next: item (3) resume list: FB-CAP climber with hard constraints
  |U| ≥ 3, f ≥ 2 seeded from f39_n48 (+ fbcap_eq_u4_n11); R74 §2.5 construction; beta2 cascade; phase-count climb toward R47 (b).

## Successor 18 (session_01D6HqejxBahRiMjurWjAtzT, Opus 5.5, D14/D15/D18; created ~19:40Z 2026-10-25, date -u)
- Handover check 5/5 (3b05d7f7; Lead 19:52Z). GO box 42 19:52Z: (1) red-team P-N5-FX (aa227b0b) and P-N5-FBPOLY (de244dcd) with exact
  checkers from the frozen texts; (2) K growth survey; (3) FB-CAP at |U| ≥ 3, beta2 cascade. Report docs/red/R72-fx-fbpoly-k.md.
- Tools (experiments/red/fbx/): fbx18.py (exact checker, every statement of FBPOLY §0.3-§6 + FX §1 (a), R-STICK); rfbx18.py, libst18.py,
  lib18.sh, loopfind18.py; k18.py (K from R27's definition, Kt and Ks); kclimb18.py (Kt objective).
- R72: no kill. 0 FAIL on library (252 S3 + 750 start-pair runs) and 8.5 M random runs. "Loop" kind occurs (exsw_loop_n15, start pair);
  K linear on kchain (K − 1 at n = 11K + 14), climbs Kt ≤ 6 at n 58 (kt6_n58), 9 at n 124; Ks ≠ Kt wording point.
- Trap (new): o = c_θ phases. EXIT-SWITCH's graphs G_Û / G_U^o both drop the terminal there; use G_U. My first fbx18 got it wrong
  (false FAIL_EXSW_graph); fixed before any reported number. Check every checker on an o = c_θ phase.
- Trap: a K climb on the switch count Ks is gamed by simultaneous wakes at one transition; climb on Kt.
- BOX 43 (Lead 21:00Z, read 21:39Z): red-team of N5-KW-box42 (L-NEW 21) and N5-KW-box15 (L-SI 10). R73: no kill. kw18.py (own W from the
  play; engine matches L-NEW's lib41 counts exactly: 424 runs, 1,061 CSTRICT, 4,661 WLAG, 34 kind changes, 2 c_w-switches). FRZ-U |R| − 1
  attained (frzu_tight_n14), CW-INT attained (cw11_n24); post-freeze kind changes and W-flat kind-B switches (CASC-B) never reached.
  Lead 20:15Z ask (loop_4102 seed climbs) superseded by 21:00Z; not done.
- Trap (new): ReadNotifications only when told; two Lead messages (20:15Z, 21:00Z) waited unread until my 21:39Z report. Check
  notifications at each report.
- BOX 44 (Lead 22:56Z, 23:07Z, 23:22Z): R73 §8 (cascb_witness seen, case (a)); R74 (post-freeze kind change not found; READING §2:
  needs a late BAND trigger of a kind-A length cascade; kmpst18.py start-pair climbs). DUAL / MIRROR NOT STARTED (context).
- RESUME POINT (for successor 19; 2026-10-26 ~00:30Z, date -u): nothing running.
  - Next (Lead's box 44 order): (2) P-N5-DUAL (docs/new/P-N5-DUAL-box43.md, sha1 a51f7c30, trunk df073cb5): check Lemma DUAL on our
    engine (N5 on G from (σ0, τ0) = mirror of N5^OF on G^d from (τ0, σ0)); hunt a 𝒞^1O phase from a non-S3 start or under Odd-first ties
    exceeding landed per-phase bounds. Tools: experiments/red/fbx/fbx18.py and experiments/red/kw/kw18.py both take --start.
  - Then: R74 §2.5 construction (post-freeze kind change); FB-CAP |U| ≥ 3; beta2 cascade (never started).
  - Tools: fbx18 (FBPOLY/FX exact), kw18 (KW notes, own W), k18 (K), climbers kwclimb18 / kmpst18 / kclimb18; random drivers
    rfbx18 / kwst18. Engine matches L-NEW lib41 counts exactly (R73 §0).
  - Read notifications at every wait: the Lead's messages queue silently.
- (superseded) RESUME POINT (2026-10-25 ~21:35Z, date -u): nothing running. Open: (a) FB-CAP |U| ≥ 3 (n 6 random ×
  all starts clean, 20.7 M runs; R72 §6 READING covers only the simplest |U| = 3, o = c_θ chain); (b) beta2 cascade, not started; (c) loop
  kind from S3; (d) K two-chain construction (R72 §8). Pins: experiments/red/fbx/instances/ (exsw_loop_n15 + start, kt6_n58).

## Successor 17 (session_01DJB52MMkzsddv3hXsMpos5, Opus 5.5, D14/D15/D18; created ~16:39Z 2026-10-25, date -u)
- Handover check 5/5 (4194c094; Lead 16:53Z). GO box 41 16:53Z: (1) P-FREEZE / HAT-FREEZE post-freeze regime at |U| ≥ 3 (P-N5-PFZ
  3c617e06, P-N5-RHO cd5df65c); (2) NHN post-freeze EV2 ends (docs/new/N5-NHN-box40.md 81302f57); (3) LV2 only if (1), (2) stall.
- Tools (experiments/red/frz/): pfz17.py exact checker (P-FREEZE a-c, LEN-TAIL, NO-CROSS-A, Y-FORM, HAT-FREEZE a-c, RHO-TAIL, NHN;
  regime counters with NONTRIVIAL = some vertex below Mopt at the run/phase start); climb17.py; shrink17.py (fast trace-only score);
  rs17.py / rsu17.py (random); exfz17.py (exhaustive, ex16 enumeration, all start pairs); fbwho.py (who switches at a fallback).
- pfz17 reproduces L-NEW's §8 (C) counts on box40/out exactly (YF 25, HFa 22, HFc 10). Their 5 post-hat phases at |U| = 3 are TRIVIAL.
- Mechanisms: cycle-node pump (Ξ-improving, W-neutral switch at a cycle node outside U; rhc_block_bk20_3 vertex 8): at most one per
  activity episode. Eviction chain (njb_reabs65_n48 fallbacks 43-67: one R vertex of U evicted per fallback; R values (c,{o,10}) <
  F values (c,∅) < W values (c,{o})). Chain vertices are all in U, so f stays below |U| − 1.
- R71 (docs/red/R71-freeze-regime-into.md): no kill. Post-freeze regimes at |U| ≥ 3 unreached (max f − (|U|−1) = −1 at |U| = 3, f = 1);
  CONJECTURE FB-CAP (in-phase Even fallbacks ≤ max(1, |U| − 2)) holds in all data; INTO 67/67 library + seeds 51/51, climbs min gates
  into R̄ = 1. INTO wording note: gate-free last post-rise state.
- RESUME POINT (for successor 18; written by successor 17, 2026-10-25 ~19:35Z, date -u):
  - Box 41 ended with no kill. R71 §0-§6 (pushed 8e429a89, merged to trunk) plus §7 addendum (FB-POLY / FB-PHASE / FX checks, n 5
    start-pair FB-CAP search).
  - Still running in the container (logs in experiments/red/frz/out/, gitignored; lost with the container):
    - fbcap17 rand 5 (fb5r2) and exh 4 (fb4x2);
    - fbpclimb17 × 4 (fp_b2, fp_b2s, fx_os40, fx_b2s);
    - shrink17 × 2 (g2_os40, g2_beta2).
  - Open targets:
    - (a) FB-CAP kill: a phase with ≥ |U| − 1 Even fallbacks at |U| ≥ 3. Best: equality at |U| = 4 (fbcap_eq_u4_n11).
    - (b) the beta2 cascade climb (Lead 18:16Z): ≥ 3 r = −1 fallbacks in one scope run. Not started.
    - (c) FX slack 0 (fx2_n11 at −2), and THETA-AFTER slack 0 (−1 so far).
    - (d) FREEZE-EXIT: needs (a) first.
  - Tools: pfz17 (PFZ / RHO / NHN), fbpoly17 (FBPOLY / FBPHASE / FX), fbcap17 (fast search), into17 (INTO), and climbers climb17,
    shrink17 (KIND / UMIN / GMIN), fbpclimb17 (OBJ=fx, START=1), intoclimb17.
  - Traps (new):
    - (1) Excess objectives collapse to |U| = 3. Use GMIN ≥ 2 and UMIN ≥ 4.
    - (2) awk argv fields differ between "ps -eo pid,args" and "ps -eo args"; check before kill.
    - (3) Monitors on chatty logs get suppressed; filter to hits / FAIL / FINAL only.
- Traps this box: pkill -f killed my shell again (exit 144); background jobs launched with & inside a short call died; part 3 of the
  library survey hit its 1800 s timeout with buffered output (lost).

## Handover check (successor 16)
Successor 16 = session_014kwWmBLu9B31iceFsng38k (Opus 5.5, D14/D15/D18/L37). Brief from Lead 09:46Z 2026-10-25. Check at 09:45Z (date -u).
1. Branch / head / trunk distance. Commands: `git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo`; `git merge --ff-only
   origin/claude/l-red`; `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`; `git merge-base`.
   - Branch claude/l-red, head 57c685df (successor 15's RESUME POINT commit). The fresh clone sat at 0d0b67a1, 1188 behind.
   - vs trunk claude/vibrant-johnson-nxvvxo: 1 ahead (57c685df), 82 behind; merge-base 0fe4d801.
2. Open work (notebook RESUME POINT for successor 16; `ls experiments/red/so/`): nothing in flight. Next steps:
   - box 39 (Lead 09:46Z): PF-THETA linear form (docs/new/N5-DROP-box35.md §8, trunk only, read with `git show`) first;
   - then RISE-LAST (R68; event = sox3.py rfb0), XSN-RUN (R68), P-N5-TOG RESTARTS if time remains.
   - Tools in experiments/red/so/ (sox*.py, soclimb*.py, vrun.sh); vrun.sh needs Oink: scripts/setup_oink.sh started 09:45Z.
3. GAPS rows (`git show origin/claude/vibrant-johnson-nxvvxo:docs/GAPS.md | grep -n N5`): G-N5-TIME (major, open, L-NEW owner;
   N5 makes polynomially many iterations; every lemma I attack feeds it). G-N5-TERM closed. GAP-A / GAP-C / G-NEST name L-RED as
   attacker but are paused under D18/L40 (A_DTL line).
4. Owner rulings verbatim (`git show <trunk>:docs/DECISIONS.md | sed -n ...`), status from `grep '^| D1[48]* ' docs/DECISIONS-INDEX.md`:
   - D1 (active): "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the
     fleet's own, as wrong until it passes the gauntlet below."
   - D14 (active): "D" / "You know it can also test prveiously not tested approaches, it can come up with it own as well"
   - D18 (active): "Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of
     mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them
     briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems."
5. Trap found: the target text is not on my branch. docs/new/N5-DROP-box35.md and P-N5-TOG-box35.md exist only on trunk
   (l-red is 82 behind), so `cat` fails; read them by `git show origin/claude/vibrant-johnson-nxvvxo:<path>`. Also: tools/oink/build
   is absent in a new container, so vrun.sh fails until scripts/setup_oink.sh has run.

## Successor 16 (session_014kwWmBLu9B31iceFsng38k, Opus 5.5, D14/D15/D18/L37; created ~09:44Z 2026-10-25, date -u)
- Handover check 5/5 (922406ce; Lead 09:55Z). GO box 39 at 09:55Z with a split: successor 15 kept PF-THETA; I took RISE-LAST, XSN-RUN,
  RESTARTS, then TEV (Lead 11:14Z) and N5-TEV-box11 / P-N5-ENT (Lead 12:34Z, 12:54Z). Report: docs/red/R69-rise-xsn-tev.md.
- KILLS (Lead re-ran both, 12:34Z: "TEV / TEV-LAST are confirmed refuted"):
  - TEV as written: tev_cex_n40 (17078f78). It needs intervening fallbacks.
  - TEV-LAST (k0 = the last fallback before t): tevlast_cex_n40 (ff1e9cb4). One fallback; L-SI's own threv.py agrees.
  - TEV-RED (1), (2), (4) hold there (its benign case). Wording: TEV-RED (3) "before e" should read "up to and including e".
- NO KILL: RISE-LAST, XSN-RUN, RESTARTS (+ H3-CONST, H2-STICK, RCLASS); N5-TEV-box11 FZ / BF / RB / WALK on 498 (Σ) pairs.
  - CYC-EV (rise form) and TEV-FB are vacuous: no (Σ) pair has a rise, which is RISE-LAST again.
- XSN-RUN margin 1 at n 10 (xrun8_n10; the 8 includes the exit crossing). Everywhere else ≤ n − 3 with the exit crossing excluded.
- G-TOG-1: 26 exit crossings on the SPEC trace (≤ 1 per phase). REFEREE-2's b6_xl2_n32 example does not match the SPEC trace.
- Tools (experiments/red/so/):
  - rx16.py: RESTARTS / H3-CONST / H2-STICK / XSN-RUN / RISE / TEV / TEVLAST / TEVCONF.
  - tevx16.py: N5-TEV-box11 in (Σ).
  - tevred16.py: TEV-RED (1)-(4) at one hit.
  - pfx.py: PF-THETA cross-check.
  - climb16.py modes: rise / rise2 / tev / tevl / conf / tx / xrun / rst. pfclimb16.py is unused.
  - data16/: library outputs.

- BOX 40 (GO 13:36Z; docs/red/R70-exh-nleq-lv.md). ex16.py exhaustive runs:
  - n 4 all starts, full space: 83,607,552 runs;
  - n 5 canonical subset: 81,000,000 games.
  - Every target is VACUOUS there: no fallback pair in a scope run, no in-scope THR fallback. The events start near n 11.
  - KILL: NL= (nleq_cex_n48, e72e4034; Lead-confirmed 15:52Z). The leave 40 → 9 at r = L is a bypass to a free vertex.
  - DATA: two (β)-fallbacks in one scope run (beta2_n11); LV-NONE / SCOPE-FB far from their bounds.
  - REFEREE-2's "no fallback after a rise" survives 1.5 M far-climb evaluations.
  - Tools: ex16 / rnd16 / nleq16 / lv16; climb16 modes far / nleq / lv / lvn.

## RESUME POINT (for successor 17; written by successor 16, 2026-10-25, date -u)
- Nothing in flight after R69. All scratch logs are in the container only; the verified bests are in experiments/red/so/instances/.
- Open targets, none started:
  - (a) A (Σ) pair with a COARSE_L(θ) rise (it must end at a fallback with M_k < L by TEV-FB). It would hit RISE-LAST and test P-N5-ENT.
    The tx and conf climbs found none.
  - (b) XSN-RUN at n ≤ 12 by exhaustive or random search, aimed at n − 1 (best: n − 2 at n 10). Exhaustive is infeasible past n 5 (R70 §3).
  - (d) NJB's straddle after NL= fell (R70 §4). (β)-fallback counts per scope run (R70 §5: 2 seen). The "no fallback after a rise" claim
    (R70 §6). All exhaustive tables at n ≤ 5 are vacuous; search at n ≥ 11.
  - (c) TEV-RED (5)'s configuration (TEVCONF): none seen. The TEV-LAST failures are all benign case (4).
- Traps (new):
  - (1) Two sessions on one branch: merge origin before each push, use distinct file names.
  - (2) Borrowed checkers narrower than the statement: threv.py stops at the next fallback.
  - (3) Degenerate maxima (the rst slack climb).
  - (4) Background jobs inside one Bash call die with it (they need their own run_in_background); waiters on killed climbs never end.
  - (5) Stamp messages from date -u only (a "10:1xZ" guess was wrong).

## Successor 15 (session_01M37vBg9T7zDX5aiPyPWPG7, Opus 5.5, D15/D18; created ~01:00Z 2026-10-25, date -u)
- Handover check 5/5 (0743d2e6). GO box 36 at 01:22Z (Lead): adversary on P-N5-SO (deb5ee44) and P-N5-LP §4 (d2c8121a + fixes).
- BOX 36 DONE (~03:10Z; docs/red/R66-so-attack.md). NO KILL: 0 failures over LIB 230 files, RAND 2,000 games, 8 climbs (~2.6 M evals).
  - Tools in experiments/red/so/:
    - sox.py: own checker from the frozen text (TH, SO, J <= S_o, K and 9 proof sub-claims).
    - soclimb.py: modes tie / sor / j / k / th.
    - sorand.py.
    - vrun.sh: n5 + n5b + Oink zlk + check_sol2 + sha1. Needs scripts/setup_oink.sh first; Oink is built in this container.
  - Findings (DATA):
    - SO's d_o-term is used: so_tie15_n32 has 15 θ-fixed changes in one θ-run.
    - "S_o <= Θ + O(1)" is false on climbed data: S_o 18 at Θ 1.
    - J = S_o = 19 is attained (so_j19_n48).
    - K = 2 (so_k2_n32), stuck at 2 for two climbs.
    - TH is far from tight.
  - READING: SO's tie-break key is a function of the H-path alone in si.py (longest-path mode: ascending ids; BFS mode:
    length-lex order of root-first id sequences). ⊕ strictness at the first switching vertex p holds because p is in neither value.
- BOX 37 (GO 03:13Z; docs/red/R67-exitr-attack.md): adversary on L-NEW box 33 (N5-K-box33.md §2/§8/§9 at l-new fb157c31).
  - CONJECTURE EXIT-R FALSE (exitr_cex_n16 / n48); its consequence ε_H1 <= (d_o-1)(f+1) FALSE (epsseg_cex_n16: 6 > 5;
    epsseg_cex_n48: 17 > 16); ORX (EPS=1) FALSE.
  - Confirmed by L-NEW's own orx.py, run from a worktree of l-new fb157c31: EPS=1 python3 orx.py <pg> in experiments/new/box33.
  - R-STICK, SN-PREFIX, OR, TC-SPLIT, ABS-L: 0 failures.
  - My CONJECTURE (J-SEG): J <= (d_o-1)(f+1), at equality on 3 instances.
  - Tools: sox2.py, soclimb2.py (exr / seg / small / jb / xsn / post).
  - vrun.sh runs n5b with --mode spec (the default orig mode is L-COMP's A5 tie-break and differs; R66 §7 correction).
- BOX 38 (GO 05:18Z; docs/red/R68-xsn-njb-ent.md). NO KILL.
  - X_SN is linear: ≤ 0.83n per fallback-free run. My CONJECTURE XSN-RUN: ≤ n − 1 per run.
  - NJB / ENT / MINSET / TOGGLE: 0 failures.
  - My CONJECTURE RISE-LAST: no COARSE_L(θ) rise between in-scope fallbacks of one scope run; rfb0 = 0 on 257 files and every climb.
  - Tools:
    - sox2.py: REL, RELe, NJB blocks, Mn, maxpre.
    - sox3.py: NO-RF-OLD, ENT.
    - sox4.py: TOGGLE.
    - soclimb2.py modes xsnf / jbf / rel / njb / xrun / mn; soclimb3.py (ENT); soclimb4.py (TOGGLE).
  - Trap 2 again: the mn fitness traded absorptions for |Mn| = 1.
  - Trap: sox's min |Mn| first skipped fallback states. minset.py includes the state of the next fallback; aligned.
- Next (if routed): K growth (hand-built wake chain, U1 pieces); X per phase (the remaining open core with K).
- Trap (box 36): the j fitness J − S_o reached a degenerate 0 (J = S_o = 0); fixed by counting only phases with J >= 1 (trap 2 again).
- Trap (box 36): killing by `ps | awk $12..` failed (the column was wrong). Use `ps -eo pid,etimes,args` and kill the pid itself.

- Successor 15, box 39 (Lead 09:42Z): PF-THETA linear form FALSE (pftheta34_n32: 34 > 32; docs/red/R69a-pftheta.md); parked for good ~10:35Z.

## RESUME POINT (for successor 16; written by successor 15, 2026-10-25 ~09:40Z, date -u)
- Successor 15 = session_01M37vBg9T7zDX5aiPyPWPG7 (Opus 5.5). Boxes 36-38. PARKED after box 38 (Lead 09:34Z). Nothing in flight.
- Reports in docs/red/:
  - R66: P-N5-SO / LP §4: no kill. SO's d_o-term is used; J = S_o is attained.
  - R67: EXIT-R, its consequence and ORX (EPS=1) are FALSE (exitr_cex_n16 / n48, epsseg_cex_n16 / n48). R30 lemmas: 0 failures.
  - R68: X_SN is linear. NJB / ENT / MINSET / TOGGLE: 0 failures. CONJECTURES XSN-RUN and RISE-LAST.
- Next box (Lead 09:34Z), for the successor: an adversary on RISE-LAST, XSN-RUN and PF-THETA (L-NEW).
  - RISE-LAST is with L-SI succ. 5 for a proof attempt.
  - Exact RISE-LAST event = sox3.py rfb0: a COARSE_L(θ) change at an S4a step strictly between consecutive in-scope fallbacks of one
    scope run.
- Tools: experiments/red/so/ (all written from the source texts; traces asserted equal to n5.run).
  - sox.py: SO / TH / J / K.
  - sox2.py: R30 lemmas, EXIT-R, REL / RELe, NJB blocks, Mn, maxpre.
  - sox3.py: NO-RF-OLD, ENT, rfb0 / gap.
  - sox4.py: L-MONO, Z-COUNT, TOGGLE.
  - Climbers: soclimb.py (tie / sor / j / k / th), soclimb2.py (exr / seg / small / jb / jbf / xsnf / rel / njb / xrun / mn / xsn /
    post), soclimb3.py (ENT), soclimb4.py (TOGGLE).
  - vrun.sh: sha1, 𝒞^1O, n5 + n5b --mode spec, check_sol2. Run scripts/setup_oink.sh first in a new container.
  - Library list: python3 experiments/new/box32/c1o_list.py 64.
- Traps:
  - (1) n5b's default --mode orig differs from SPEC ties; always use --mode spec.
  - (2) Degenerate maxima keep recurring (J = S_o = 0; |Mn| = 1 with no absorptions). Put the substantive key before the cheap one.
  - (3) Check a borrowed checker's ranges (minset.py includes the state of the next fallback).
  - (4) Kill climbs by pid from `ps -eo pid,etimes,args`.
  - (5) Seeds on other lanes' branches: `git show origin/<branch>:<path> > scratch`.
  - (6) Foreground sleep is blocked. Use a background until-loop with a deadline.

## RESUME POINT (for successor 15; written by successor 14, 2026-10-24 ~23:45Z, date -u)
- Successor 14 = session_01DYUCLfp4LkaCnY7moyVLAa (Opus 5.5). Boxes 31-35. Parks after box 35 (Lead 23:37Z).
- Reports, all in docs/red/:
  - R60: Mei port, no kill.
  - R61: L-NEW box 27 lemmas, no violation; FBRE-F refuted, fbref_cex_n32.
  - R62: (X) ≈ 0.86n on a random family; record X 65 at n 32.
  - R63: (U1-T) refuted, u1t_cex_n32 / u1t_own6_n32; (OB_R) holds.
  - R64: (C) ≤ 8, (CL) holds; J up to 10, j10_n24.
  - R65 (box 35): P-N5-U23 not refuted (0 violations, checked as frozen by u23x.py). First U2 W-flat switches (u2flat73_n32: 73).
    u23check.py gaps (U23 unchecked, (iii) at 2|R|, (ii) / corollaries untested). K_W ≈ 0.8n.
- Tools: experiments/red/xing/ (xclimb, u1t, u23x, ccclimb, jclimb, fbref, levels, wavetrace, nhwhy, xseed).
  - Most import L-NEW / L-SI modules read-only.
  - jclimb needs LSI = a worktree of l-si 25d16cc8; L-SI's coarse/ tools are also on trunk 7666336.
  - xclimb needs LNEW_BOX25 = a worktree of l-new ≥ 1322d958 experiments/new/box25. box25 is on trunk, so the trunk path works
    too.
- Recurring traps:
  - (1) A fitness tuple whose invalid sentinel (−1) beats real negative scores. Use −10^9.
  - (2) Degenerate maxima: empty blocks or stretches score as tight. Restrict to blocks with ≥ 1 event.
  - (3) Reference checkers may test a weaker statement than the frozen one (u23check vs P-N5-U23). Read the statement, then check
    the checker's thresholds.
  - (4) Waiters that wait on climbs you killed never end. Harmless, but reported as "stopped".
- Open kill targets, none started: a hand-built k-digit counter (R62 §1: X ≈ 2^(k−1)·n would follow); J super-linear (R64 §2);
  K_W / E growth (R65).

## Successor 14 (session_01DYUCLfp4LkaCnY7moyVLAa, Opus 5.5, D15/D18; created 14:36Z 2026-10-24, date -u)
- Handover check 5/5 (e16f5995). GO box 31 at 14:48Z (Lead), to ~17:50Z.
- BOX 31 item 1 DONE (b11dff73, docs/red/R60-mei-port.md):
  - Mei port (T31 iii), experiments/red/mei/.
  - Dantzig-SSI makes 2^h − 1 iterations, h 2-8 (faithful).
  - N5 makes h+1 iterations (Mei start) and h−1 (canonical); n5b agrees; zlk + verify OK. NO KILL.
  - The singleton-gate redesign is ruled out by Theorem W (k = 1).
  - Dantzig's non-eliminating window is 2^(h−1) − 1 (T31's 2^h − O(h) corrected).
- BOX 31 items 2-3 DONE (END ~17:30Z; docs/red/R61-xing-attack.md; last push 799d0a9a). Lead told at 17:27Z.
  - (FBRE-F) (L-NEW CONJECTURE, box 28 §5b) FALSE as stated: fbref_cex_n32 (sha1 901674dc…).
    - 33 post-freeze fallback evictees re-enter in one (w, u*)-run. L-NEW's own fbre.py agrees (evict_postfreeze 33, FBRE − prefreeze
      = 33).
    - CAVEAT: the eviction is at run index exactly n − 1 (the boundary), and the re-entries follow a θ-change at state 37.
    - n5 = n5b 56/8, Oink OK, verified.
  - Lemmas C / FBL / FBF / XA: 0 violations (12+ instances, n ≤ 48).
  - XA main-case data: x31_ru24 (27 re-entries, u* ≠ none, 0 C3 failures).
  - (CYC-u*) per run: 48 at n 32, 44 at n 48. m_r ≤ 6, no k-digit counter; gains are length-only θ-changes.
  - (NH): only SB+TAU, short.
  - Tools, experiments/red/xing/:
    - xclimb.py targets: lemmas, nh, cyc, cycu, reent, reentu, fbref. Needs LNEW_BOX25 = a worktree of l-new 1322d958 or later.
    - fbref.py, levels.py, nhwhy.py.
  - L-NEW box 28 tools: run them from a worktree of l-new 2a195b3 (experiments/new/box28/fbre.py), from inside that directory.
- BOX 35 DONE (GO 23:37Z, END ~00:47Z; R65). PARKED after it (last box, Lead 23:37Z). Nothing in flight.
- BOX 34 DONE (GO 21:07Z, END ~23:30Z; docs/red/R64-carries-J.md):
  - (C) ≤ 8 (no growth); (CL) 0 violations (ccclimb.py).
  - J per phase raised from 3 to 10 (j10_n24), 8 at n 32 / 48 (jclimb.py with L-SI tame.py at l-si 25d16cc8; LSI env = an l-si
    worktree). Linear-looking. All verified.
  - Context at box end ~445k. Handover planned at ~560k (Lead).
- BOX 33 DONE (GO 20:0xZ, END ~21:05Z; docs/red/R63-u1-attack.md):
  - (U1-T) REFUTED as stated, u1t_cex_n32 (63dfd785; Lead re-ran, merged 9769dc3): 7 per vertex at one W-length; own-switch
    cascade 2→18→19→18. u1t_own6_n32 gives 6 own switches.
  - (OB_R) in transitions per OTHER block NOT refuted: max excess 0 (obr_eq_n24).
  - Tool: experiments/red/xing/u1t.py (--climb, --own, --obr). L-NEW's box29 helpers are on trunk, so no worktree is needed.
  - Queued by the Lead after box 33: nest carries (evicting fallbacks) from L-SI's zcl_fb2_n32 (experiments/si/xing/instances).
- BOX 32 DONE (GO ~18:03Z, END ~20:05Z; docs/red/R62-x-attack.md): attack on (X).
  - Random seed family (L-NEW xclimb unmodified): X = 13/20/29/44/55 at n 16/24/32/48/64; X ≈ 0.86n; one wave each.
  - Structured wave climbs: X = 65 at n 32 (record; L-NEW's was 54) and 78 at n 48. About 3-4 waves; X ≤ 2n.
  - lev_l_sc's digit-2 replay is a crossing wave (peel + carry + replay). No third digit (nest40: one low digit).
  - CONJECTURE (data): X per phase O(n). No kill.
  - Next targets offered by the Lead (19:3xZ), pick one: L-NEW U1 / (OB_R) (seed experiments/new/box29/instances/u1_n32.pg,
    l-new 63252214), or L-SI (Z) R-reversals (zcl_fb2_n32, l-si bfd6700, Z 18 at n 32; X ≤ (n−1)(Z+1)+Z).
- NEXT (for successor or next box):
  - (FBRE-F') with the window at index ≥ n, or excluding re-entries after a θ-change: climb fbref with the boundary moved (edit
    fbref.py's `a - i >= g.n - 1`).
  - Hand-built k-digit counter on run_x_inr2's 27S/24S pattern (L-SI box 3); OPEN, not started.
  - Mei port (R60) is closed: no kill, singleton redesign impossible by Theorem W.
- Predecessor's elimclimb n 32 (seed 81) finished in ITS container: window 17, no gain (its note c8aaa5d5). Not rerun.
- Sources opened (box 31): Mei arXiv 2610.27386 v1 PDF, sha256 5b3265d3eb1c5b8ae79f…: Table 1 p.5, eq. (3)-(4), Thm 1 p.11,
  §5.1 eq. (35) and Thm 4 p.20.
- Trap (box 31): L-NEW's box25 tools import siblings by relative path (n5x in ../box21). Run them from a full l-new worktree,
  not from a partial copy.
- Trap (box 31): coarsecheck.py cuts stretches at fallbacks unless --withfb, although Lemma C claims "fallbacks included".
  xclimb runs both.

## RESUME POINT of successor 13 (superseded by the section above)
- Lead's TOP KILL TARGET (14:22Z), NOT STARTED:
  - Port Mei arXiv 2610.27386 (Dantzig simple SI takes 2^h − 1 iterations on deterministic games: discounted G_h Thm 1 p.11;
    mean-payoff Ĝ_h Thm 4 p.20) to a parity game.
  - Map the two cost scales to priorities so that the VJ order reproduces Mei's order.
  - Run N5 (experiments/new/n5.py, canonical start, plus experiments/n5-second/n5b.py) for h = 1..6.
  - Outcome either way: a long phase (report the law at once) or the exact step where N5's gate or trust differs from Dantzig
    on G_h.
  - Sources: L-LIT T30 (docs/lit/T30-elimination.md, trunk 4332f9f) and T31 (the construction spec, in progress). Open the paper
    yourself and record it in "Sources opened".
- elimclimb n 32 (seed 81, from returns_rt32, 3,000 s) FINISHED 15:04Z: window stayed at 17 (phase 53), no improvement in
  171,616 steps. The n 48 run (seed 82, from rt48) produced elimn_cex_n48 (window 49). Nothing in flight. PARKED 15:05Z
  (Lead 14:37Z).

## Box 30 (2026-10-24 12:58Z GO; DTL until the 13:20Z redirect (D18 / L40), then N5)
- DTL (ACYC), docs/red/R59-acyc.md §0-§3:
  - No failure. gap = 1 throughout (every cycle through a new part passes exactly one old-X vertex).
  - Random games give 0 straddles. Seeds: strfam_S5_n46, plus strfam_S6, which is richer.
  - Tools: experiments/red/acyc/.
- N5, R58 §12e and §13:
  - (ELIM-n) REFUTED: elimn_cex_n48 (sha1 d6062e86…), window 49 > n 48, verified, n5b agrees.
  - (CYC-ELIM): 5 in theta_tp32.
  - L-NEW Lemma RM / RE: 0 violations.
  - θ-changes per phase plateau at 16.
  - R58 §12e corrects §12d (ii): THETA re-entries are common; my retcheck class A was ill-posed while w is constant. L-COMP's
    thetaA_n17 has class A via a w rise.
- Tools (experiments/red/n5inj/): elimclimb.py (fitness noelimrun_both), cycelimclimb.py (thetaelim), lemmaclimb.py (L-NEW
  routemono/reentry), thetaclimb.py (--from, padding), phaseclimb.py (--returns), blockclimb.py, blockcheck.py, phasereturns.py,
  retcheck.py (class A only meaningful when w changes), rootsearch.py, ringsearch.py.
- Traps (new):
  - Importing thetaclimb.py runs its climb at import (top-level loop). Wrappers set its SECONDS to 0 via argv (see
    lemmaclimb.py).
  - Wait loops: a waiter is killed at its time limit; harmless.
  - Kill jobs only by exact argv: awk '$2=="python3" && $3=="<script>"'.
  - Long jobs: start each in its own run_in_background call (nohup inside a timed-out call dies).

## Box 27 (GO 01:52Z 2026-10-24, to ~04:55Z): 𝒞^1O family with super-linear iterations inside one λ-phase
- Box 26 extension, 01:47Z offer: R58 §9 Proposition X (PROVED, uses R17), pushed at f93e5175. The part that cannot reach o runs
  one-player N5. Corollary X1: (CH-1O) holds when o is on no cycle, so a kill needs o on a cycle.
- fts_best16 reading: o = 5's exits {2, 4, 9, 14, 15} sit on ONE σ-path 2→13→3→4→1→15→14→8→12→6→5 that returns to o (a ring).
  σ̄(o) walks along the ring 14→15→4→2 as the path improves (backward propagation); two laps in one phase.
- Tools: thetaclimb.py (fitness = θ-changes inside one λ-phase; --from seed), cdagseed.py (CDAG_k + o seeds; short as built).
- BOX 27 END (~04:15Z). R58 §10, NO KILL.
  - (a) θ-climbs: 13 / 16 θ-changes in one phase at n 16 / 24 (< n).
  - (b) pure-Y blocks: 27 / 49 at |Y| 21 / 33, so "block ≤ |Y|" (L-NEW data) is FALSE. But they hold only ≤ |Y| − 1 inside one
    λ-phase (in-phase climbs reach 20 / 31).
  - Conjecture STAT-PH (DATA conjecture only; Lead 04:31Z: not a target): in-phase pure-Y block ≤ |Y| − 1. o-acyclic 𝒞^1O is now
    SETTLED by L-NEW's refereed theorem (N5-1Oacyc-box24.md: blocks are segments of N5 on G_τ, bounded by R17), with Prop X.
    Lands as RESULTS R18.
  - Instances: theta_thf16, theta_thc24, block_bk20/32, blockph_bp20/32; all Oink zlk OK, strategies verified.
- BOX 28 (GO 04:31Z, END ~06:20Z): R58 §11, NO KILL on o-cyclic 𝒞^1O or with K = 2.
  - θ-changes per phase plateau at 16 (n 24-40).
  - Ring templates give one lap.
  - K = 2 phase climbs: 53 at n 32, 50 at n 48 (linear).
  - Trust events on my instances ≤ 4.
  - Instances: theta_tp32/tp40, phase2_pk32/pk48; all verified.
- BOX 29 (GO 06:30Z, END ~08:20Z): R58 §12, composition FAILS.
  - Re-root via the hub is θ-independent (Lemma G (c)): k = 4 roots give 10 in-phase iterations vs 9.
  - Re-entries: 20 / 20 by route improvement, 0 by θ overtaking w.
  - Returns per vertex climb to 12 (rt48), but in-phase stays ~1.6n up to n 64 (ph64: 103).
  - Instances: returns_rt32/rt48/rt64/ph64; all verified.
- PARKED 2026-10-24 08:27Z (Lead): N5 line STANDS DOWN (docs/agents/N5-STANDDOWN.md quotes R58 §12d). Box 29 merged at trunk 1119482.
  Wake only on a new named target.

## DONE box 26 (R58; 2026-10-23 23:06-23:20Z, date -u)
- §1: jump-ahead switches (N5 switches SSI would not make) mostly use SSI counter edges: sym_h16 14/17, DLM1 n8 38/38.
  N5 is slower than SSI on the climbed games (55 vs 29).
- §2 Theorem W (PROVED given (P) = VJ00 Lemma 5.8 "no improvement => maximum", via RESULTS R15 G-N5T-3).
  - Lemma 1: I(σ1) = I(σ2) ⇒ Ξσ1 = Ξσ2.
  - Lemma 2: flat stretches are at most 2n(n-1)+1 long (R15).
  - Theorem: moves with |I| ≤ k number ≤ (2n(n-1)+1)·Σ_{j≤k} C(m, j), for ANY SI-type run.
  - Corollary: width O(1) ⇒ polynomial; a run of length T needs width ≥ log(T/8n²)/log m.
  - DATA: premise holds on 41,111 strategies of 2,000 random games plus sym_h8 exhaustive (0 violations; ties are common:
    3,345 collisions with equal Ξ).
  - SSI-DLM1 n = 8: Odd's moves by |I| = C(8, k) exactly (the bound's shape is tight).
- §3: N5 widths on climbs / DLM. DLM: N5 takes the whole wide set. Climbs: 41/65 moves at width ≤ 3. Declines are mostly deferred,
  then taken.
- §5: O5 = (K1)-(K4). BRIBE false. Open: (STRETCH) plus a family with withdrawn generosity.
- (K2) WITHDRAWN 00:08Z: frozen-τ* climbs are long (L-NEW: fts_g29 66, fts_best24 43; mine: frz40 90).
- §7 (Lead 23:28Z, L-NEW Theorem B frozen branch): Corollary W2 says exclusion-only throttles are polynomial, so width must come
  from refusals.
- §8 climbs, all verified:
  - widthclimb n 32: wide_h16, 44 iterations, W 72; width up, length down.
  - frozenclimb, frz24/32/40: 39/66/90 iterations; longest λ-phase 11/28/36; ~all moves at gate width ≥ 3.
  - frz24's two laps lie in different λ-phases, so they are bounded by Lemma Φ. A kill must be super-polynomial inside one
    phase.

## DONE (box 24; docs/red/R56-r2-vj-switchsets.md §0-§4; head b0884407 before this handover)
- §1, item 1: N8d-R2's admissible sets vs VJ Random-Edge's improving sets on G_zeta (gz1-3). They differ from STATE 0.
  - M1: labels count only the improver's even priorities and truncate at odd ones, so entries into A_i / B_i look better than
    under VJ.
  - M2: truncation is idempotent, so lane tails are tight with the shortcut and lanes never unwind.
  - The first VJ step R2 cannot take is a b-lane tail shortcut (gz2 steps 178-209, gz3 420). It is not history: the fresh lfp gives
    the same.
- §2: HL_k = R53's H_k plus z-separated delay lanes on node 7 (fatal lap move) and node 8 (fatal 8:6->1 before 7's lane resets).
- §3: per-lap failure ε(L) by an EXACT absorbing chain on (laps, τ, µ). Steady multi-lap increments:
  6.2e-3 / 5.75e-4 / 3.92e-5 / 2.1e-6 / 1.0e-7 at L = 4..8.
  - Ratios ×10.8, ×14.7, ×18.3, ×21: at least exponential, not a power law.
  - They agree with the full-run estimates.
  - Lap scans over every lap start: L = 4 (900 laps) and L = 5 (300 laps).
- §4: dead-end packet. Family HLg_k = `experiments/red/kl24/hlgen.sh k L L`, L = 5, 6, 8, 10, n = 9 + 2k + 4L.

  | k | n | mean R2 dual pivots | seeds |
  | --- | --- | --- | --- |
  | 0 | 29 | 630 | 5 |
  | 1 | 35 | 32,201 | 5 |
  | 2 | 45 | 2,759,578 | 5 |
  | 3 | 55 | 388,769,332 | 2 |

  - Every output is verified: regions == Oink zlk, strategies pass verify.py.
  - kl_single.py equals kl2fast seed for seed.
  - PROVED: nothing new. READING: the mechanism and the schedule L(k) = Θ(k log k).

## DONE box 25 (R57; 2026-10-23 21:40-22:00Z, date -u)
- n5.py is faithful to SPEC S1-S5 (READING).
- On every counter family, N5's Odd moves about N times, early, then never; the rest is one Even pass over the lanes.
  Examples: gz2 374 iterations at n 389; switchbestexp 62 at n 160; H_k and HLg_k 3 iterations.
- DLM attempts: escape edges are counter edges. Pruning or laning them kills SSI's counter too (dl_*.pg verified).
- Obstruction (R57 §4): no lapping (R15); the opponent is an improver, not a best-replier; a kill needs two coupled counters whose
  shortcut edges are disjoint from counter edges.
- Tools: experiments/red/n5/n5tr.py, oddmoves.py, ssiedges.py, vjlane.py.

## IN FLIGHT
None (2026-10-24 17:30Z by date -u, successor 14 box 31 end). All climbs finished or stopped; scratch logs in the container only.

## NEXT for N5 (box 26)
- R58 §5 open form: (STRETCH) (one-sided stretches poly) and a family meeting (K1)-(K4). These need wide improving sets, held off
  by NON-optimal opponent generosity that the opponent later withdraws.
- An optimal opponent's generosity costs nothing (BRIBE counterexample), so it cannot be the mechanism.
- Check L-NEW successor 8's docs/new/N5-time-box21.md as it lands: Theorem W may serve its incompatibility proof as the
  bounded-width case.

## NEXT for N5 (box 25 leftovers)
- Prove or refute O4's incompatibility of R-a and R-b (R57 §6). Or build a game meeting both: a symmetric two-counter in which the
  jump-ahead switches use edges disjoint from the counter edges and threats.
- Seeds:
  - experiments/red/n5/instances/sym_h16_s1.pg (55 iterations at n 32; both players alternate).
  - DLM family 2 (experiments/new/dlm_gen.py 2 n).
- Tools: n5tr.py (trace, SSI-type marks), perswitch.py (per-vertex switches and returns), symclimb.py, vjlane.py, ssiedges.py.

## NEXT (for the Lead to route)
1. Answer CHECKER C23 questions on R56 §4 / DE30, if any.
2. Optional, only if a proof of the dead end is wanted. Close the gaps:
   - (G1) a bound ε(L) ≤ c·2^−L for EVERY lap type reachable in HLg_k. Two-lap scans exist only at L = 4 (26 BAD lap starts of 900,
     up to 0.24, from partial corruption) and L = 5 (worst 3.85e-3, ×63 smaller). L ≥ 6 is not scanned.
   - (G2) that lap failures are the only way R2 leaves the counter, which would give mean ≥ (1 − Σε)·counter length.
3. Other single-switch or randomized tree-SI rules: the same z-lane recipe applies to any rule whose failure is a race against a lane.

## Resume point
Box 26 working (R58 pushed). Start from R58 §5 (O5, STRETCH) and the tools in experiments/red/n5inj/. Older resume points below.
PARKED after box 24 (2026-10-23 ~15:45Z, date -u). Wake only on a new named target or on CHECKER questions.
- R56 §0-§4 are final: freeze them; corrections go in new sections.
- Start from R56 §4 and the tool list below.

## Sources opened
- Box 26: none opened. VJ00 Lemma 5.8 (premise (P) of R58) is cited through RESULTS R15 (referees opened BRICS RS-00-48,
  sha256 485a12de…), not opened by me.
- None new in box 24. Fleet-internal only: N8d-single.md §0, T26-N8d-step3.md, R53, R54, R55, n8d-second README, si.py.
- Earlier opened sources (Friedmann thesis, Koh-Loho arXiv 2108.13338): `git show b0884407:notes/L-RED.md`.

## Dead ends (box 26)
- Steering symmetric climbs to wide refused sets (widthclimb, R58 §8a): W 24 -> 72 while iterations fell 55 -> 44. Width is
  not the bottleneck.
- Conjecture BRIBE (a mover refusing r improving edges faces an opponent with ≥ r/poly improving edges): FALSE.
  - Instance: experiments/red/n5inj/instances/bribe_cex_n15.pg (sha1 392af465…). Even refuses 10 of 15, and Odd has It = ∅.
  - Obstruction: an optimal τ* is not the best reply to a suboptimal σ, so its generosity costs Odd nothing.
- Lane enforcement of R-b: jump-aheads use counter edges on the climbed games too (14/17), not only on DLM (R58 §1).

## Dead ends (box 24; each with the obstruction and the instance)
- Plain (no z) delay lanes against R2: lanes do not reset in label space (M2). On H_0 + plain lane, R2 means are 32.7 / 39.7 at
  L 4 / 8, flat. Instances: lanegen.py klmin_n13 7 L none.
- One lane only (on 7): laps grow only linearly in L (7.5 / 12.5 / 24.0 at L 8 / 16 / 24 on H_2). Killer: 8:6->1 picked before any
  of 7's lane nodes resets, probability about 1/(L+1) per lap. Trace: H2_L16 seed 3, iteration 21 (ktr.py).
- Fixed lanes (8, 8): super-polynomial over k = 0..2 only. ε > 0 caps the expectation near 34/ε; HL88_2 seed 3 stopped early at
  1,230,538. This forced the growing-lane family.
- One-lap exact ε understates the true ε: a lap can end "successfully" in a CORRUPTED state. Example: HL88_2 seed 3, lap 35,724
  (one-lap ε 2e-8), then lap 35,725 with ε 0.073. Use the m-lap increments.
- Earlier dead ends: `git show b0884407:notes/L-RED.md`.

## NEEDS
- Lead: none open. CHECKER C23 may ask questions.

## Things only I know
- Instruments (experiments/red/kl24/). All import experiments/n8d-second/kl2fast.py + kl2.py read-only; dual run = kl2.solve's.
  - lanegen.py G V L Z [LPRIO] [TARGET] [closed]: z-separated lane on Even node V.
    - The z priority must sit ABOVE the exit's lap-reset rise and BELOW the counted component: 23 between 22 and 28 for H_k.
    - 'closed' = lane starts inward.
  - hlgen.sh k L7 L8: HL_k = famgen H k + lane(7, L7, open, target 3) + lane(8, L8, closed, target 1). Reproduces the sha1s in R56.
  - solvecheck.py G seed [cap]: bench.py's check (Oink zlk -w 1 + verify.py) in-process. Use it whenever a run can exceed 1e7
    pivots: kl2.main has no cap option and its default 1e7 cap makes bench rows "ERROR: pivot cap".
  - r2mean.py G S: R2 dual pivots over seeds 1..S. LAPARC=v:w / LAPNODE=v give lap counts.
  - ktr.py G all|r2 [seed]: dual trace with labels (SHOW=nodes). Switch-all is pure Python: too slow beyond about 1e5 iterations.
  - laptrial.py / laptrial2.py: one-lap Monte Carlo from snapshots. Superseded by exactlap, kept as a cross-check.
  - exactlap.py G S W J [MAXSTATES]: EXACT failure probability from the lap-start snapshot (base seed S, W warm-up pivots, J-th
    increase of dual node 1's label). Options:
    - LAPS=m: failure within m laps. The steady ε is the increment.
    - FLOAT=1: doubles.
    - MAXPATH=1: most probable failing path.
    - SCAN=N (+ COND=1 redraw, SHOWABOVE=x): the chain at every lap start of one base run.
    - Costs: about 4x states per +1 of L; one lap at L 8 is 199k states (about 3 min); 3 laps at L 8 are 984k states (about 25 min).
- G_zeta comparison: experiments/red/gzeta/cmp.py (r2|vj modes; STOP_AT_LOSS=1) and lanes.py (lane timeline).
- Traps from box 26:
  - `pkill -f` on a pattern that occurs in my own wait loop killed my shell again (exit 144).
  - A nohup job started INSIDE a Bash call that the harness later times out is killed with it: frz32/frz40 were cut at
    ~1,890 s. Start long jobs in their own run_in_background call.
  - A wait loop using `pgrep -f "scripts/push.sh"` matches itself and never ends.
- Traps from box 24:
  - Lap boundary = node 1's label increases. τ at a lap event is NOT unique.
  - Pads are TOP from the start: compare the TOP count with the snapshot's, never with 0.
  - ε varies between laps: one snapshot can mislead by ×100. Scan, or use multi-lap increments.
  - Killing processes: `pkill -f` or `grep | awk` on a pattern that occurs in my own command line kills my shell (exit 144, three
    times). Select pids with awk on exact argv fields: $2=="python3" && $3=="<script path>".
  - Speed: kl2fast runs at about 27k pivots/s at n 45-55. 4 cores, 16 GB; 4-5 jobs were fine this box.
  - date -u was behind my own sense of elapsed time all box: always stamp with date -u (the Lead flagged a "12:2xZ" stamp).
