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
