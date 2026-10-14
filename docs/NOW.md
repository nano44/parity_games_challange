# NOW (rewritten, never appended; max 150 lines)
Updated: 2026-10-14 by Lead. Phase: M0, M1, M2 done; first attack lane L-STRUCT (weak separators) started 2026-10-14 18:54Z. Reporting: weekly checkpoint (D1, after M2).

## Milestones
| M | State | Evidence |
| --- | --- | --- |
| M0 Setup | done; TARGET v1.0 at a3777f1 (D2) | this commit; CI .github/workflows/verify.yml; backstop trigger in docs/agents/LEAD-BACKSTOP.md |
| M1 Reproduce hard families | DONE 2026-10-14 19:10Z (l-comp de7ea19): 12 of 13 families blow up as published, all strategies checked; counter_qpt superpolynomial but class open (targets a quasi-poly algorithm). Friedmann SI via REFEREE-checked PGSolver ports (reading L5). Bench LANDED on trunk (REFEREE OK ae532f6) | experiments/hard-families/README.md (l-comp) |
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
| L-LIT | session_01MxWPJxeciDocEdfd89xCF8 | claude/l-lit | opus-5-5 | high | parked (T5: S2 NEW, e911037) | Source checking and barrier analysis need judgement; Fable reserved for referee; move to Fable when step-3 sign-offs start |
| L-COMP | session_014bbtNwaVKxFymHpXynjURn | claude/l-comp | opus-5-5 | high | working (SAT hard cells for L-STRUCT, 6h box; ~380k ctx) | SAT engineering needs care; successor near 600k | Paper-to-code fidelity for M1 generators and the M2 implementation; drop to sonnet-5-5 for routine benchmarks after M2 |
| L-STRUCT | session_01VH4fd2Fq8XeXtyUfkwLJV1 | claude/l-struct | fable-5-1 | high | working | Attack lane (owner: most capable model at high effort); rank 1 approach, weak separators, T4 verdict OPEN |
| WATCHDOG | session_01JQNTX8zT3T3mWMt6ZmYzkn | none (never edits) | haiku-5-5 | high | working (cron :30, trig_019xE43BZ5qaDGwxDkZ5h5ik) | Routine liveness/overage checks; reports to Lead only (deviation from playbook: does not wake lanes, so idle sessions never get messages) |

## In flight
- L-COMP: parked after notebook handover; wakes for a new claim, review changes, or L-STRUCT SAT engineering.
- L-LIT: parked; T1-T4 on trunk (docs/lit/). T4: weak separators OPEN (Czerwinski et al. 1807.10546 §6).
- L-STRUCT: T1 likely FALSE (L-COMP: w(2,10)=4 < 5=s(2,8), l-comp 3e44d2c; REFEREE checking). Pivot to (c): structure of minimal weak witnesses; S3 statement (growth of w in d) before any proof.
- REFEREE: check T1 refutation (witness + s(2,8)=5 strong encoding), then S2 T2 statement.
- L-COMP: T1 refutation found; now growth data: w(2,d) d=12..20, w/s(3,d) d=8,10 V; then (3,8)V, paused runs. Box ends ~01:30Z.
- WATCHDOG: hourly at :30.

## Findings to carry
- C1 (REFEREE-checked, a data point, not M3): w(2,6)=3 < 4=s(2,6) in E, S, V; w^V(3,6)=6 < 7=s^V(3,6). Weak separators can be strictly smaller than strong ones.
- Landscape doc corrections (L-LIT, docs/lit/BARRIERS.md): d = O(log n) poly result is Jurdzinski-Lazic Thm 7 / Fearnley et al., not Calude et al.; upper-bound exponent is Jurdzinski-Lazic's; attractor-decomposition barrier is formally only Arnold-Niwinski-Parys Thm 5.1; Two Counters bound partly empirical; Random-Facet parity lower bound withdrawn (arXiv 1410.7871).
- Oink mspm at 8fbf0a7 is wrong on some games (crash at mspm.cpp:486; one answer rejected by Oink's verifier); excluded from agreement claims. Instances: experiments/harness/regressions/ (l-comp).
- PGSolver SI families (switchallexp, switchbestexp) target PGSolver's switch-all/switch-best SI, not Oink psi/ssi; port of stratimpralgs.ml queued in L-COMP.

## Live approaches
- A1 deterministic weak separators (L-STRUCT): outside the strong-separator barrier (T4). Algorithmic quantity is the diagonal w^V(n,n) (REFEREE d96b686); fixed-n growth in d is not algorithmic. Data: w=s on most small cells; w<s at (2,6),(2,10),V(3,6); s(2,2h)=h+1 but w(2,8)=w(2,10)=4. Lower-bound target T1 likely false; now measuring growth of w in d.

## Dead approaches (with obstruction): see docs/RESULTS.md "Dead ends"
- (none yet)

## Best result so far
- None of the fleet's own. Known: quasi-polynomial upper bound (to be source-checked by L-LIT).

## Owner questions open
- Q4: L-COMP built PGSolver (tcsprojects/pgsolver d3cd624) but the session's permission classifier refused to run the binaries; generators were ported to Python instead. Owner: allow running them (to diff the port against the original), or keep port + referee check?
- Q2: trunk branch: keep claude/vibrant-johnson-nxvvxo as trunk, or create `main`?
- Q3: environment setup script (Boost dev packages + scripts/setup_oink.sh) to save each session ~1 min of setup.

## Spend
- Sessions report usage.cost_usd in get_session. 2026-10-14 20:02Z: Lead $13.04 (369k ctx). 2026-10-14 19:02Z: L-COMP $14.13 (379k ctx; plan handover near 600k), WATCHDOG $0.01; REFEREE, L-LIT, L-STRUCT not yet reported.
