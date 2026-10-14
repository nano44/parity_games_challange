# NOW (rewritten, never appended; max 150 lines)
Updated: 2026-10-14 by Lead. Phase: M0, M2 done; M1 running; attack lanes wait for L-LIT's ranking (T2). Reporting: weekly checkpoint (D1, after M2).

## Milestones
| M | State | Evidence |
| --- | --- | --- |
| M0 Setup | done; TARGET v1.0 at a3777f1 (D2) | this commit; CI .github/workflows/verify.yml; backstop trigger in docs/agents/LEAD-BACKSTOP.md |
| M1 Reproduce hard families | 10 of 13 families confirmed (l-comp 4c0ae44): tc, tc+, counter_symsi, counter_rr/dp/m/core/rob/ortl, recursiveladder (port, awaits REFEREE). Open: counter_qpt (growth type), Friedmann SI games switchallexp/switchbestexp (need stratimpralgs port); strategy-checked re-run in progress | experiments/hard-families/README.md (l-comp) |
| M2 Audit arXiv 2511.03752 | DONE 2026-10-14 ~18:35Z: BROKEN (two independent 4-vertex counterexamples, cross-checked); RESULTS DE1 | docs/decisions/M2-arxiv-2511.03752.md |
| M3 Partial results | not started; attack lanes wait for TARGET approval and L-LIT ranking | - |
| M4 Target | not started | - |

## Roster (model, effort, one-line reason; revisit at each restart)
Lead session: session_014FBi6o334DvwT5Uw2kDfoN, environment env_013N6DGgsLr96BMjKj1hpw9i, branch claude/vibrant-johnson-nxvvxo.
Effort note: create_session exposes no effort knob; every session inherits effort "high" (verified per session with get_session).
Prices per Mtok in/out (platform docs, 2026-10-14): fable-5-1 $10/$50, opus-5-5 $4/$20, sonnet-5-5 $2/$10, haiku-5-5 $0.10/$0.50.

| Role | Session id | Branch | Model | Effort | State | Reason |
| --- | --- | --- | --- | --- | --- | --- |
| Lead | session_014FBi6o334DvwT5Uw2kDfoN | claude/vibrant-johnson-nxvvxo | opus-5-5 | high | working | Owner-chosen session; routing judgement; keeps context lean |
| REFEREE | session_01Ki9osXiyYf9heTLNk3FKED | claude/referee | fable-5-1 | high | working | Most capable model; finding the error in a claimed proof decides M2 and every claim after |
| L-LIT | session_01MxWPJxeciDocEdfd89xCF8 | claude/l-lit | opus-5-5 | high | working | Source checking and barrier analysis need judgement; Fable reserved for referee; move to Fable when step-3 sign-offs start |
| L-COMP | session_014bbtNwaVKxFymHpXynjURn | claude/l-comp | opus-5-5 | high | working | Paper-to-code fidelity for M1 generators and the M2 implementation; drop to sonnet-5-5 for routine benchmarks after M2 |

## In flight
- L-COMP: remaining M1 families (READMEs, sweeps), stratimpralgs port; harness has strategy verification (D2 change 5).
- REFEREE: R1 full report (short) incl. AM1-AM9 faithfulness verdicts; then PGSolver port checks; then review of L-COMP harness for landing.
- L-LIT: T1 done (l-lit a6c530f); T2 RANKING.md (gates first attack lane); T3 BARRIERS.md.
- Watchdog: add when a 4th working session starts (first attack lane).

## Findings to carry
- Oink mspm at 8fbf0a7 is wrong on some games (crash at mspm.cpp:486; one answer rejected by Oink's verifier); excluded from agreement claims. Instances: experiments/harness/regressions/ (l-comp).
- PGSolver SI families (switchallexp, switchbestexp) target PGSolver's switch-all/switch-best SI, not Oink psi/ssi; port of stratimpralgs.ml queued in L-COMP.

## Live approaches
- (none yet)

## Dead approaches (with obstruction): see docs/RESULTS.md "Dead ends"
- (none yet)

## Best result so far
- None of the fleet's own. Known: quasi-polynomial upper bound (to be source-checked by L-LIT).

## Owner questions open
- Q4: L-COMP built PGSolver (tcsprojects/pgsolver d3cd624) but the session's permission classifier refused to run the binaries; generators were ported to Python instead. Owner: allow running them (to diff the port against the original), or keep port + referee check?
- Q2: trunk branch: keep claude/vibrant-johnson-nxvvxo as trunk, or create `main`?
- Q3: environment setup script (Boost dev packages + scripts/setup_oink.sh) to save each session ~1 min of setup.

## Spend
- Child sessions report usage.cost_usd in get_session (Lead own record shows none). 2026-10-14 18:02Z: L-COMP $5.24.
