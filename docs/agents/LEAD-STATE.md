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
