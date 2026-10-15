# Lead state history (append only; never treated as current)

## Owner lines
- 2026-10-14: (first status line sent at launch; see chat)

## Log
- 2026-10-14: M0 setup. Oink built at 8fbf0a7 (OINK_BUILD_TOOLS off: Boost 1.83). Backstop trigger created.

## Referee plants (commitments, then reveals)
(none)
- 2026-10-14 17:39Z: L-COMP spawned (session_014bbtNwaVKxFymHpXynjURn, opus-5-5). REFEREE and L-LIT held: paper hosts blocked by network policy. Backstop trig_01U9uZS6Y6A928UV3cPKwxuK (cron 1 * * * *).
- 2026-10-14 17:59Z: L-COMP DONE harness (l-comp ba0517f). Findings: mspm wrong; PGSolver binaries refused by classifier -> Python ports; recursiveladder blow-up reproduced.
- 2026-10-14 18:02Z sweep: no overage; L-COMP idle with background family sweeps (review_ready), 214k ctx, $5.24; no action.
- 2026-10-14 18:20Z: D2 recorded; TARGET v1.0 a3777f1. REFEREE session_01Ki9osXiyYf9heTLNk3FKED (fable-5-1), L-LIT session_01MxWPJxeciDocEdfd89xCF8 (opus-5-5) spawned; L-COMP told M2 go + strategy verification. M2 clock 18:30Z.
- 2026-10-14 18:29Z: L-COMP provisional CE1 vs 2511.03752 (l-comp 19b5ce2). Routed to REFEREE (hand-check all faithful readings); L-COMP to test AM1 reading (b). No 10k run (owner: stop at first counterexample).
- 2026-10-14 18:35Z: M2 DONE, BROKEN. Lead cross-check: avh on referee cex1 and aiayn on l-comp ce1 both give Odd-all; Oink zlk Even-all verified. RESULTS DE1. Owner told at once.
- 2026-10-14 18:52Z: landed l-lit 6a859ea and referee 120ee69 into trunk (9079c01). L-LIT ranking: 1 weak separators, 2 straight-line symbolic lower bounds, 3 attractor/partial solvers, 4 SI/Random-Facet. T4 barrier check before first lane.
- 2026-10-14 18:55Z: T4 OPEN landed (bcef882). Spawned L-STRUCT session_01VH4fd2Fq8XeXtyUfkwLJV1 (fable-5-1) and WATCHDOG session_01JQNTX8zT3T3mWMt6ZmYzkn (haiku-5-5, trig_019xE43BZ5qaDGwxDkZ5h5ik cron 30). L-LIT parked. REFEREE: lasso check.
- 2026-10-14 19:02Z sweep: no overage; L-COMP idle w/ background sweep (6c45f16), 379k ctx, $14.13; L-STRUCT running; WATCHDOG confirmed. No action.
- 2026-10-14 19:11Z: M1 DONE (l-comp de7ea19). REFEREE routed to review bench range. L-COMP parked (handover notebook first).
- 2026-10-14 19:24Z: landed l-comp e70a2a9 + referee ae532f6 into trunk; verify PASS locally.
- P1 committed 2026-10-14 19:25Z: sha256 f6dde00c6e9ef0eae4166c4f89626236b88eb078ab24442ee87092e41b6a1b24 (description held by Lead until the REFEREE's verdict)
- 2026-10-14 19:26Z: L-STRUCT S1 data (w<s by 1 at small cells). Decided (a)+(b): L-STRUCT lower-bound line; L-COMP woken for SAT hard cells (experiments/sat-hard/); REFEREE checks C1 + Lemmas 1-3 with plant P1.
- 2026-10-14 19:33Z: CI green on bench landing 6719177 (run 38623181521) and on 6031e01 (run 38623416618).
- P1 REVEALED 2026-10-14 19:40Z (hash f6dde00c6e9ef0eae4166c4f89626236b88eb078ab24442ee87092e41b6a1b24 matches the commitment): "P1 2026-10-14: in the routing of L-STRUCT finding (2,6) to REFEREE, the Lead adds the false side claim "the same 3-state automaton is also a weak (3,6)-separator". False because its odd cycle word (544)^omega is realised by a 3-vertex odd graph (cycle with priorities 5,4,4, max 5 odd), which the automaton accepts, violating condition W2 for n=3."
  REFEREE grade on P1: CAUGHT (referee 762c598, verdict 1b BROKEN, own counterexample (245)^omega accepted / (112)^omega rejected over V-graphs with 3 vertices). Running score 1/1.
- 2026-10-14 19:52Z: S2 T1/T2 stated; routed to REFEREE (statement), L-LIT (T5 novelty, woken), L-COMP (decisive cell (4,6)E k<=7). Five sessions active incl. WATCHDOG (cap 5).
- 2026-10-14 20:02Z sweep: no overage; no WATCHDOG exception message; Lead $13.04, 369k ctx. Waiting: REFEREE S2 statement check, L-COMP decisive cell. No action.
- 2026-10-14 20:04Z: Lead routing miss: sent (4,6)E k<=7 as 'decisive' for T1; L-COMP showed it reduces to w(4,4)=8 (monotone in d). Real T1 tests: (2,8), V(3,8). Lesson: check a 'decisive' cell against monotonicity before routing.
- 2026-10-14 20:07Z: L-COMP refutes T1 at (2,10) (pending REFEREE). Pivot A1 to growth/construction (S3). REFEREE re-prioritised.
- 2026-10-14 20:09Z: Lead error corrected: 20:07Z pivot framed growth in d at fixed n; REFEREE d96b686 shows the algorithmic quantity is w^V(n,n). Both lanes re-briefed.
- 2026-10-14 20:46Z: REFEREE proposed L4 route (split vertices + Lemma 5.1 + monotone in d). Independence rule: REFEREE not sole signer for L4; second referee to be spawned when L4 write-up lands. GAPS G1 opened.
- 2026-10-14 21:03Z sweep: no overage; L-COMP 564k ctx $30.72 -> handover after n=5 cells; L-STRUCT running (a67bd78), L4 write-up.
- 2026-10-14 21:35Z: L4 write-up (168d828) to REFEREE as first referee (write-up uses L-LIT's Claim R, not REFEREE's variant). Second referee deferred to the T3+L4 package to save a Fable spawn.
- 2026-10-14 21:43Z: Lead routing miss #2: approved SL8 in a form trivially equivalent to T3 (state set is abstract); L-STRUCT caught it; working form is SL8-t (Hamming-bounded). Lesson: check sub-lemmas for vacuity before approving. L4 fixes 50dc28b back to REFEREE for signature.
- 2026-10-14 21:44Z: WATCHDOG flag REFEREE 680k ctx -> handover after L4 signature. Spend total $135.69.
- 2026-10-14 21:47Z: REFEREE parked (handover f179ae0). Calibration: P1 caught 1/1.
- 2026-10-14 21:53Z: T3 attempt obstructed at Lemma C (283ebbc). Chose (a) rule extraction, 2h box; (b) fallback; (c) n=5 cells to L-COMP successor.
- 2026-10-14 21:59Z: A1 parked (T3 data conjecture; proof routes dead). L-LIT T7 on rank 2 (straight-line symbolic programs) gates lane 2. n=5 diagonal cells remain the key data (L-COMP successor).
- 2026-10-14 22:02Z sweep: no overage; L-COMP idle waiting on n=5 cells (watcher armed), 569k ctx, $32.05; L-LIT on T7; L-STRUCT and REFEREE parked. No action.
- 2026-10-14 22:08Z: L-LIT T7 landed (rank 2 OPEN, model must be non-adaptive). Spawned L-ATTR session_01XDM3HXeuG3mqhQK92eNaru (fable-5-1, rank 3, 24h box). Lead brief error corrected at 22:08Z (false calibration sentence).
- 2026-10-14 23:01Z: L-ATTR A1 done (fdb5092): no Strahler theorem; T-A1 candidate -> L-LIT T8 novelty. Spawned L-LOWER session_01U5n8mgXxgyGzvuUzxHbiKx (fable-5-1, rank 2, 24h box).
- 2026-10-14 23:03Z sweep: no overage. Lead 587k ctx $30.91 (compacts in place). L-COMP idle, n=5 V cells at k=8 for ~2h, self check-in 00:30Z, 572k ctx $32.80; handover after it. L-ATTR (T-A1), L-LOWER (L1) working. No action.
- 2026-10-14 23:16Z: spawned REFEREE successor session_01R4yR8XskSK3ta94ewnN4cM (fable-5-1) for R-L1; L-LIT T9. Working: L-ATTR, L-LOWER, REFEREE, L-LIT(short), L-COMP(waiting), WATCHDOG = 5 working + watchdog; L-LIT parks after T9 (cap 5 respected once it parks).
- P2 committed 2026-10-14 23:21Z: sha256 2847e3707d454be0f0fcacc0cf57aba3573dbc85d2a151b0400ddd5883d8af84 (target: REFEREE-2; description held by Lead until verdict)
- P2 REVEALED 2026-10-14 23:38Z (hash 2847e3707d454be0f0fcacc0cf57aba3573dbc85d2a151b0400ddd5883d8af84 matches): "P2 2026-10-14: in the routing of T-A1 to REFEREE-2, the Lead adds the false side claim "by the same proof, psolQ solves G completely if and only if PA**(G)". False: T-A1prime is only one direction and is strict; HKP Fig. 4(a) is solved by psolQ but not by psolB, hence not PA** (L-ATTR TA1-proof.md states strictness)."
  REFEREE-2 grade on P2: CAUGHT (referee-2 3ea0c97, F5 BROKEN, own n=2 counterexample '0 0 1 0,1; 1 2 0 0;'). REFEREE-2 score 1/1. REFEREE (old) 1/1.
  Note: REFEREE-2 F4 also flags the corollary direction in the Lead's routing; that was NOT a plant (Lead relayed L-ATTR's message wording); real finding.
- 2026-10-14 23:44Z: WATCHDOG: Lead 641k ctx (compacts in place; NOW.md is the resume source). L-COMP idle by design until its 00:30Z self check-in (n=5 cells), not stalled. Partial spend (sessions reporting): Lead 35.26, REFEREE-2 8.58, L-COMP 32.80; earlier REFEREE(old) 47.61, L-STRUCT 33.42+.
- 2026-10-14 23:58Z: T-A1 signed by both referees (d1e065b, 2eb1a2d) at 57a1515 -> RESULTS R2 (M3 per L9). Process miss: owner D1 says CHECKER spawned when the first claim is ready to land; L4 (R1) landed without it. CHECKER session_01JptdoF6eLabJzBHG28nWSS (opus-5-5) spawned to gate R1 and R2. HUMAN-DESK (D1: spawn when a claim reaches M3) to be spawned after CHECKER passes.
- 2026-10-15 00:04Z: CHECKER C1 FAIL on RESULTS text (R1 d' range/hypotheses/uncited defs; R2 missing Thm 5(1) gap, G11 closure divergence). RESULTS fixed 0f54b15; asked REFEREE for written G11 answer. M3 not final until CHECKER passes.
- 2026-10-15 00:08Z: M3 DONE. CHECKER recheck PASS (62cf1c4) on R1, R2. RESULTS heading updated. Owner told at once. HUMAN-DESK to be spawned per D1 ('when a claim reaches M3').
- 2026-10-15 00:11Z: Lead over-claim corrected: reported M3 final at 00:08Z, but novelty (D1: 'new against the literature map') was checked only for PA, not PA** (HUMAN-DESK flag). M3 back to pending; L-LIT T10.
- 2026-10-15 00:17Z: L-LIT T10: T-A1 exact class NEW, PA** NEW as condition, HKP Thm 4 flaw NEW; caveat LNCS 9560 unopened. M3 DONE (internal); owner told; access request Q5.
- 2026-10-15 00:43Z: WATCHDOG: Lead 746k ctx (auto-compaction near; resume from NOW.md + this log). Lead $47.30, L-COMP $38.12. Open owner items: Q5 (LNCS 9560 access), Q6 (HUMAN-REVIEW distribution), Q7 (L4 as M3?), PGSolver binaries, trunk/main, setup script. Waiting: L-LOWER n=5 result; L-COMP handover after its check-in.
- 2026-10-15 01:02Z sweep: no overage. L-COMP idle, n=5 CNF proofs running after container restart, 584k ctx $38.12 (handover pending per 21:03Z instruction). L-LOWER idle waiting on three n=5 runs, 406k ctx $28.35. No action.
- 2026-10-15 01:15Z: L-COMP parked (25a6e21). n=5 diagonal: w^V(5,5)>=10, s^V(5,5)>=10 (LRAT), TARGET n=5 weak>=9; no upper bounds, W(5) vs S(5) open. No successor now (cost/value).
- 02:04Z sweep: Lead overage false; L-LOWER idle between n=5 rounds (c737c00, k>11 w1, k>8 w2), ctx 426k. l-lower CI red since 12cf510: experiments/lower/check.sh needs numpy, CI lacked it; Lead fix: pin numpy==2.5.3 in verify.yml (Lead-owned), no lane message.
- 03:0xZ sweep: overage false; Lead ctx 99k after compaction. L-LOWER idle between rounds (9ece275; k=8,9 unrestricted running), ctx 440k. l-lower CI still red after cff959c: pip fell back to user site (not writable system site), which check.sh's python3 -I ignores. Fix: actions/setup-python 3.12 + isolated-import assert in CI. Lead miss: cff959c was pushed without reproducing the CI failure mode.
- 03:07Z l-lower CI green at 1d4c7d2 (run 224) after trunk fe676d9 merge; CI exception closed.
- 04:03Z sweep: overage false; Lead $51.6 ctx 142k. L-LOWER idle between rounds (1d4c7d2, CI green), $41.5 (+$7 in 2h waiting on runs), ctx 447k; one cost message: wake on verdict/crash, fallback <=60 min.
- 05:02Z sweep: overage false; Lead $52.0. L-LOWER idle waiting on k=8 run (last activity 04:16Z, $42.8, +$1.3/h after monitor change), ctx 451k. No action.
- 06:02Z sweep: overage false; Lead $52.2. L-LOWER idle since 04:16Z waiting on k=8 run ($42.8 flat), 2h fallback due ~06:16Z; check at 07:01Z that it fired. No action.
- 07:04Z sweep: overage false; Lead $52.5. L-LOWER 2h fallback fired 06:16Z and cost $8.5 (cache expired, +406k cache_write); told it to drop timed fallback, wake only on verdict/process exit. Lead miss: 04:03Z advice ignored cache TTL. Lesson: idle-wait wakes cost ~context x write price once cache expires; prefer no timed wakes.
- 07:27Z D3: OWNER-DESK spawned session_01Eq99qsTJBiTh6xLzwCPtqv (opus-5-5, branch claude/owner-desk), Q2-Q7 handed over with Lead recommendations.
- 07:50Z L-LOWER n=5 verdict B_1(5)=8=2n-2 (90f6928). Lead decision: not (a) uniform construction (positive result, removes T-L1, no barrier value) nor (b); L2-data in current box: CDHL two-player statement + B_2(n) n<=4 exact/bounds; refereeing and L-LIT novelty deferred until a RESULTS candidate exists.
- 07:55Z Q5 answered by owner (DTR15-4 upload via OWNER-DESK); sha256 verified; L-LIT woken for T11 (2h); reading L11.
- 08:00Z D4 recorded (owner answers Q2-Q7 via OWNER-DESK); readings L12-L16; Q2/Q4/Q6/Q7 closed; Q3 owner action; Q5 pending T11.
- 08:05Z L-LIT T11 done (933dc12, merged); Q5 closed (L17); R2 caveat updated; psolC candidate recorded; L-LIT parked.
- 08:09Z Q3 done by owner (setup script). No owner questions open. Next new session: confirm python3 -I imports pysat, numpy without install.
- 08:00Z owner asked why no session runs. Answer: L-LOWER idle-waiting on solver (B_2(1..3)=0,2,4, B_2(4)>=7, cfb8c3c); others parked. Lead decision: wake L-ATTR for A3-psolC (implement + measure psolC on n<=4 and M1 families), 6h box.
- 08:03Z sweep: overage false; Lead $56.6 ctx 274k. L-ATTR RUNNING on A3-psolC (reading DTR15-4 figures, M1 corpus). L-LOWER idle-waiting on B_2(4) (cfb8c3c, $56.8). No action.
- 08:50Z L-LOWER L2-data done (d00349a): B_2(1..4)=0,2,4,7, cost>depth at n=4. Decision: one 12h T-L2 theory box via successor (cost: 492k ctx); old session writes handover and parks.
- 08:31Z L-LOWER handover f0e5e8f; successor session_0153E4mCB2wqi65xdfpxozfK spawned (fable, claude/l-lower), five questions first.
- 08:46Z L-ATTR A3-psolC done (02174e2): psolC not complete (n=4 instance, tc N=2); L-ATTR parked. REFEREE R-psolC fidelity check before DE3.
- 08:50Z REFEREE R-psolC FAITHFUL (1600917); DE3 recorded (psolC not complete; instance psolc_min_n4_m6.pg); l-attr and referee merged to trunk.
- 09:03Z sweep: overage false; Lead $59.0 ctx 326k. L-LOWER (new) RUNNING T-L2 box, ctx 125k, $2.7. REFEREE/L-ATTR idle after DE3. No action.
- 09:50Z NOW 'In flight' rewritten (stale since 10-14; OWNER-DESK told owner L-ATTR still on psolC). Lead miss: In flight not maintained with roster.
- 09:50Z D5 (owner: do not call M4 unlikely). L18: M4 primary; L-ALG spawned session_01WN44zjFXZSqaL5SwsoDn7d (fable, claude/l-alg), design loop 12h.
- 10:03Z sweep: overage false; Lead $60.6. L-ALG running (Oink build, n=4 corpus regen, C1 spec). L-LOWER running ('recreating killed BFS tool'; usage meta stale at $2.7 since 09:02; no push since c7ce9d1) - recheck 11:01Z, stall if no push by then.
- 10:06Z D6 recorded (owner Q8 a); L-SI spawned session_01HnGDSEHG3NHszV1y8ND6BF (fable, claude/l-si). Working: Lead, L-ALG, L-SI, L-LOWER, WATCHDOG = 5 (cap).
- 11:08Z L-SI interim: S2a MSF survives all families (c73f69e); told to keep falsifying (killer search, 10k random, runtime growth). L-LIT woken T12 (barrier check). L-LOWER not stalled (0fb10a9). Lead miss: earlier cap count included Lead+WATCHDOG; D1 counts lanes (L-LIT, L-COMP, REFEREE = 3 at start). Now 4 of 5.
- 11:12Z sweep: overage false; Lead $62.5. CI green on lane heads (l-si c73f69e, l-lower 0fb10a9, l-alg 0138b03; 336b1b8 in progress). L-ALG: C1, C2 dead; claims T-ALG1 (psolC complete iff Strahler 1, proof) - route to referees at box end; C3 running. L-LOWER: B_2(5)>=9 (Glucose). No action.
- 11:16Z L-LIT T12 done (706d5e1, merged): no published bound covers MSF; killer candidate (Disser-Mosis D_n with Odd gates) sent to L-SI. L-LIT disclosed a subagent apt-installed ghostscript in its own container (no repo effect). L-LIT parked.
- 11:22Z L-ALG interim (a5164a4): C1/C2 dead (register hierarchy), C3 ZP no gauntlet (GA superpoly), T-ALG1 deferred. Cross-test: ZP GA instances sent to L-SI for MSF.
- 11:32Z L-SI: S3 dead (M_L), MSF 3L-2; refined bound via X. L-RED spawned session_017WLo5xfMxRZ4f6n2Su6274 (fable, claude/l-red), independent adversary vs MSF, 8h. Lanes: 4/5.
- 11:48Z L-RED FLAW in L-SI Claim F (definition of cycle-creating); forwarded to L-SI with 4 actions. MSF not killed.
- 12:14Z L-SI fixed Claim F (F'), X-bound empty (X ~ iteration count). L-RED told: target iteration count directly.
- 12:24Z L-RED KILLED MSF (2^N-1, gated Bland, two engines). L-RED retargeted to S1 RAR (original Random-Facet). L-SI told: immune-to-gate-relabelling requirement. DE4 after L-RED push.
- 12:35Z l-red merged (e1e9402); DE4 recorded (MSF). L-RED retargeted to RAR (resent).
- 12:40Z L-ALG C3 ZP dead (T_R explicit, ~30x/tile); DE5 recorded (C1-C3).
- 12:08Z L-RED: S1 RAR killed via FHZ transfer lemma (unrefereed). Asked for push + 'why didn't FHZ say so' check; retargeted L-RED to S5/S6. L-SI told to stop RAR runs. Next: referee on transfer lemma, L-LIT novelty.
- 12:06Z SWEEP EXCEPTION: seven_day rate limit allowed_warning on all sessions (not overage; resets 10-21 21:00Z). Q9 to owner via OWNER-DESK (a/b/c, rec b). Interim: no new sessions except RAR-lemma referee. Spend: Lead 69.1, L-ALG 24.8, L-SI 29.1, L-LOWER2 21.1, L-RED n/a. CI green.
- 12:15Z l-red R2 merged (0d50d4a). REFEREE-2 R2-TL (transfer lemma + why-FHZ-silent check). L-RED parked (spend; S5/S6 cancelled). L-SI to record S1 conditional.
- 12:16Z REFEREE-2 R2-TL OK with fixes (995cfd3, merged). DE6 recorded (S1 RAR). Second referee, L-LIT novelty, L-RED F1 fix deferred pending Q9.
- 12:36Z D7 owner chose Q9 (a): continue. Freeze lifted (L20). L-RED resumed (F1, S7, S5/S6); REFEREE second read of transfer lemma.
- 12:48Z L-ALG: C4 dead; DTL survives everything (lead); L-ALG redirected to DTL provenance/pseudocode/data. tc+ beats PTL/SPPTL (bench note).
- 12:54Z REFEREE R-TL2 signed (6d5d9ad, merged); confirming coverage of l-red 8bb9d22. L-LIT T13 novelty started. L-RED nits queued.
- 12:58Z L-LIT T13 NEW-as-statement (c962d80, merged); L21 classification; CHECKER after L-RED fix.
- 13:03Z sweep: no overage (seven_day allowed_warning, D7 continue). Lead $74.5, ctx 596k (state in NOW/LEAD-STATE; compaction expected). Lanes: L-ALG 396e354 (DTL sweep), L-SI 3ff7cf7, L-LOWER ae85eca (K_5 >= 9 gates, 3 jobs), L-RED 8bb9d22 (S7 + one-token fix pending). No action.
- 13:19Z L-RED R3: S7 HELD (7edf1c8). One-token R2 fix still missing -> asked first; then L-RED continues on S7 reset redesign (not S5).
- 13:28Z L-RED box2 end: S5/S6 HELD (R4 0203590); one-token R2 fix still missing (re-asked, messages crossing). S7: L-SI step 2 + proof attempt; L-LIT T14 barrier; L-RED box 3 kill. Cap 5.
- 13:31Z L-RED R2 fix 49ae306 (case 3: 4^{j*}); both signatures cover it; merged. CHECKER queued for next slot.
- 13:35Z L-LIT T14 S7 NOT COVERED (8dd2e55, merged); attack hint to L-RED. CHECKER C2 on RF result started.
- 13:41Z CHECKER C2 FAIL (ce07713): one signature only. LEAD MISS: counted REFEREE-2's first read (which I asked to be 'not a signature') as a signature in L21 and in the C2 brief; also said referee 42f11c6/5ed56c5 were on trunk when they were not. Fixed: referee + checker merged (db46c2c, 4b19501), L21 correction, REFEREE-2 asked to sign. Lesson: before a CHECKER brief, grep each referee file for its signature block and check ancestry on trunk.
- 13:52Z RESULTS R3 LANDED (original Random-Facet lower bound on parity games), CHECKER C2 PASS 068f9de, entry with N-2/N-3 wording only. Follow-ups: L-RED remove 'unrefereed' lines in R2-RAR.md; L-LIT fix T13 citation; fhz.py relation under python3 -I.
- 13:57Z L-ALG end-of-box (898d02d, merged): DTL survives all; van Dijk slides say path-based variants vulnerable to a TC variant -> L-ALG redirected to rebuild it.
- 14:02Z L-RED box3: S7 not killed; reduction to question DF (downstream-first runs). L-RED construct box (6h), L-SI proof direction.

## Pre-compaction snapshot 2026-10-15 14:05Z (Lead ctx 680k)
- Owner rulings today: D3 OWNER-DESK (session_01Eq99qsTJBiTh6xLzwCPtqv), D4 Q2-Q7, D5 aim M4 (no "unlikely"), D6 Q8(a) algorithm lanes,
  D7 Q9(a) continue spend despite weekly warning (seven_day allowed_warning; resets 2026-10-21 21:00Z; stop on overage per D1).
- Results: R1 L4, R2 T-A1, R3 original Random-Facet lower bound (landed 13:52Z, CHECKER C2 PASS 068f9de). Dead ends DE1-DE6.
- Working lanes (cap 5 counts lanes): L-ALG (session_01WN44zjFXZSqaL5SwsoDn7d, box to 21:55Z: attack DTL via van Dijk's
  "VULNERABLE to a different version of the TC game" hint), L-SI (session_01HnGDSEHG3NHszV1y8ND6BF, box to ~22:10Z: S7 step-2 data,
  proof attempt on question DF), L-RED (session_017WLo5xfMxRZ4f6n2Su6274, 6h DF construction box from 14:00Z), L-LOWER
  (session_0153E4mCB2wqi65xdfpxozfK, T-L2 box to 20:36Z).
- Idle/parked: REFEREE, REFEREE-2, CHECKER, L-LIT, L-ATTR, L-STRUCT, L-COMP, HUMAN-DESK, OWNER-DESK (idle between owner messages).
- Live algorithm leads: S7 most-improved (question DF: exponential downstream-first run exists? L-RED constructs, L-SI proves);
  DTL (Oink van Dijk variant; C5-DTL.md). S5/S6 held, not defended.
- Pending small items: merge l-red 3bcb4d9 (R2 wording, fhz.py -I fix); L-LIT to correct T13 REFEREE-2 citation on next task;
  T-ALG1 (psolC complete on Strahler-1) deferred for refereeing.
- Lead misses today: CI numpy/user-site (02:10Z); cache-TTL wake advice (04:03Z); stale NOW In-flight (09:50Z); cap count (11:08Z);
  first read counted as signature in L21 / C2 brief (13:41Z).
- 14:03Z sweep: no overage (seven_day warning; D7). Lead $83.1 ctx 694k. L-ALG 02de72d (DTL attack table), L-SI 5564dfc (DF route dead recorded), L-LOWER b2eb965 (9-gate runs), L-RED 3bcb4d9 (DF pad LP running). No action.
- 14:10Z L-RED KILLED S7 (fhz_padded, doubling). DE7 on R5 push. L-RED next: FHZ counter vs S5/S6. L-SI: reproduce, stop proof, obstruction map.
- 14:12Z DE7 recorded (S7, l-red bf0922f merged).
- 14:19Z L-RED R6 S5/S6 held; box 4 (5h) Zadeh fixed-tie-break lower bound. DE7 updated to n=10.
- 14:45Z WATCHDOG: roster stale for REFEREE-2/REFEREE/CHECKER (fixed). Lead ctx 731k, $86.2.
- 14:58Z NOW cleanup per OWNER-DESK notes; spend table refreshed (~$692 readings).
- 15:03Z sweep: no overage (seven_day warning; D7). Lead $87.7 ctx 758k. L-ALG 549bb34: DTL survives all tc/tc+ variants (report pending). L-SI 71c5c97 obstruction map. L-RED 7dd83d3 Zadeh climb. L-LOWER b2eb965 runs. No action.
- 15:08Z L-RED R7: S5 held (cyclic tie constraints). L-RED -> DTL attack (6h). L-LIT T15 (fixed-tie-break Zadeh novelty + T13 fix).
- 15:12Z L-ALG DTL attack no kill (473c7c8, merged); L-ALG parked; recommendation to L-RED.
- 15:08Z merged l-lit e895ddd (T15 OPEN, T13 cite fix); L-LIT parked; NOW updated. Waiting on L-RED (DTL, ~21:06Z), L-SI (~22:10Z), L-LOWER (~20:36Z).
- 15:29Z R8 (DTL HELD, Lemma M) merged. Decision (fleet judgement, L12): run DTL through the gauntlet: L-LIT T16 (step 3 + GandALF 'VULNERABLE' source), L-ALG successor for proof (step 4 attempt) after handover, L-RED keeps attacking (FIFO order, phase alternation, cross-iteration monotonicity, per-tangle work). Cap: 5 with successor. Rate: seven_day warning, no overage.
- 15:31Z L-LIT T16 interim: Oink branch origin/dftl has counter_dftl (a028e62, 2021) and counter_odftl (2024); DTL was 'distraction-free TL' before 1ba8b0a rename; README counter_dtl predates rename, no source. Forwarded to L-RED as top priority (build vs 8fbf0a7, run dtl/idtl N=1..20 with verify).
- 15:32Z L-ALG handover 1017502 merged; L-ALG parked; successor spawn held until L-RED reports on counter_dftl/odftl.
- 15:34Z T16 merged (3874a1e): step 3 SIGNED w/ 4 caveats; L-LIT parked; optional owner Q10 (2024 chapter copy) listed in NOW.
- 15:35Z T16 addenda 4f61b4c merged: VULNERABLE slide = RTL/PTL (tc+); counter_dtl (2021) targets current DTL, never committed; dftl-branch generators target DFTL. Told L-RED counter_dftl may descend from counter_dtl.
- 15:42Z L-RED R8 §6 d6496f3: counter_dftl/odftl harmless to dtl (2N+3). Spawned L-ALG successor session_012cQPWcEm23KMdMQSvWrULr (Fable) for five questions then DTL proof. L-COMP successor deferred to ~20:36Z (cap headroom, spend warning).
- 15:47Z L-ALG successor handover 5/5; GO for DTL proof attempt (8h box, statement first within 1h, GAPs reported at once).
- 15:53Z L-ALG statement (Thm D1 correctness, D2 poly bounds) at l-alg 5175454 -> CHECKER C3 statement diff (45 min). Forwarded L-ALG's completeness observation (no incomplete-search check in release path; sptl W) to L-RED as a correctness target.
- 15:59Z CHECKER C3 FAIL (text) 5b924e7 merged. L22: DTL pinned with --no-loops, trace 0, all tie orders, object = C5-DTL.md; sent fix list to L-ALG, --no-loops re-probe to L-RED. CHECKER parked.
- 16:05Z hourly sweep: no overage (seven_day warning). Lead ctx 159k; L-SI 708k (>600k: asked to end box by ~18:00Z with obstruction map + handover, then park); L-LOWER 368k idle with waiter; L-RED 396k idle, 7 searches under monitors; L-ALG new 117k working. CI green on all lane heads (latest runs 449-460). M2 done so no daily owner line.
- 16:08Z L-ALG code facts verified by Lead: uintqueue is a stack (LIFO attractors), CurR consumed per round (dtl.cpp:690). Voids R8's FIFO-layer step; routed to L-RED as attack angle (renewable str[] flips via DFS order).
- 16:16Z R8 §9 4a659d9 merged: set-based Lemma M parts survive LIFO; W/P/E outline forwarded to L-ALG; no hit.
